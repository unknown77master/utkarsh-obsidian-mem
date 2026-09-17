"""Streaming-tolerant parsers for known and adjacent ChatGPT export schemas."""
from __future__ import annotations

import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any


class ExportParseError(ValueError):
    pass


def iter_json_array(path: Path, chunk_size: int = 1 << 20) -> Iterator[Any]:
    """Yield a top-level JSON array one element at a time.

    This keeps a large export out of RAM. A broken whole file raises
    ExportParseError; callers can log it and continue with the next file.
    """
    decoder = json.JSONDecoder()
    buffer, started, eof = "", False, False
    with path.open("r", encoding="utf-8-sig", errors="replace") as handle:
        while True:
            if not eof and len(buffer) < chunk_size:
                data = handle.read(chunk_size)
                if data:
                    buffer += data
                else:
                    eof = True
            buffer = buffer.lstrip()
            if not started:
                if not buffer:
                    if eof:
                        raise ExportParseError("empty JSON file")
                    continue
                if buffer[0] != "[":
                    raise ExportParseError("expected a top-level JSON array")
                buffer, started = buffer[1:], True
                continue
            buffer = buffer.lstrip()
            if buffer.startswith(","):
                buffer = buffer[1:]
                continue
            if buffer.startswith("]"):
                return
            if not buffer:
                if eof:
                    raise ExportParseError("unterminated JSON array")
                continue
            try:
                value, end = decoder.raw_decode(buffer)
            except json.JSONDecodeError as exc:
                if eof:
                    raise ExportParseError(f"malformed JSON near character {exc.pos}: {exc.msg}") from exc
                data = handle.read(chunk_size)
                if not data:
                    eof = True
                else:
                    buffer += data
                continue
            yield value
            buffer = buffer[end:]


def _text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return "\n".join(part for item in value if (part := _text(item)))
    if isinstance(value, dict):
        for key in ("text", "content", "parts", "result"):
            if key in value:
                return _text(value[key])
    return ""


def _primary_nodes(mapping: dict[str, Any], current_node: Any) -> list[dict[str, Any]]:
    """Use the active branch when present, otherwise a stable timestamp order."""
    selected: list[dict[str, Any]] = []
    seen: set[str] = set()
    node_id = str(current_node) if current_node else ""
    while node_id and node_id not in seen:
        seen.add(node_id)
        node = mapping.get(node_id)
        if not isinstance(node, dict):
            break
        selected.append(node)
        node_id = str(node.get("parent") or "")
    if selected:
        return list(reversed(selected))
    nodes = [node for node in mapping.values() if isinstance(node, dict)]
    return sorted(nodes, key=lambda node: (node.get("message") or {}).get("create_time") or 0)


def parse_conversation(record: Any, source_file: str) -> dict[str, Any]:
    """Turn one schema-variant record into a plain, normalized-ready dict."""
    if not isinstance(record, dict):
        raise ExportParseError("conversation record is not an object")
    conversation_id = record.get("conversation_id") or record.get("id")
    if not conversation_id:
        raise ExportParseError("conversation has no id")
    mapping = record.get("mapping") or {}
    if not isinstance(mapping, dict):
        raise ExportParseError("conversation mapping is not an object")
    messages: list[dict[str, Any]] = []
    for node in _primary_nodes(mapping, record.get("current_node")):
        message = node.get("message")
        if not isinstance(message, dict):
            continue
        author = message.get("author") or {}
        metadata = message.get("metadata") or {}
        content = _text(message.get("content") or {})
        messages.append({
            "id": str(message.get("id") or node.get("id") or ""),
            "role": str(author.get("role") or "unknown"),
            "timestamp": message.get("create_time"),
            "content": content,
            "model": metadata.get("model_slug") or record.get("default_model_slug"),
            "metadata": metadata,
        })
    return {
        "id": str(conversation_id),
        "title": str(record.get("title") or "Untitled conversation"),
        "created_at": record.get("create_time"),
        "updated_at": record.get("update_time"),
        "messages": messages,
        "metadata": {"default_model": record.get("default_model_slug"), "source_file": source_file},
    }
