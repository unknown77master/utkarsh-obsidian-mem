"""Transparent lexical deduplication and cautious contradiction flags."""
from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any

STOPWORDS = {"a", "an", "the", "i", "am", "is", "are", "to", "and", "or", "with", "my", "this", "that", "of", "in", "on", "for", "it", "use", "using"}


def _tokens(statement: str) -> set[str]:
    return {word.strip(".") for word in re.findall(r"[\w+#.]+", statement.lower()) if word.strip(".") and word.strip(".") not in STOPWORDS}


def _similar(left: str, right: str) -> bool:
    a, b = _tokens(left), _tokens(right)
    if not a or not b:
        return False
    return len(a & b) / len(a | b) >= 0.72 or a <= b or b <= a


def merge_candidate(memories: list[dict[str, Any]], candidate: dict[str, Any]) -> bool:
    """Merge equivalent facts and return whether a duplicate was merged."""
    for memory in memories:
        if memory["category"] == candidate["category"] and _similar(memory["statement"], candidate["statement"]):
            known = {source["conversation_id"] for source in memory["sources"]}
            memory["sources"].extend(source for source in candidate["sources"] if source["conversation_id"] not in known)
            memory["confidence"] = max(memory["confidence"], candidate["confidence"])
            memory["technologies"] = sorted(set(memory.get("technologies", [])) | set(candidate.get("technologies", [])))
            return True
    memories.append(candidate)
    return False


def remove_conversation(memories: list[dict[str, Any]], conversation_id: str) -> None:
    kept: list[dict[str, Any]] = []
    for memory in memories:
        memory["sources"] = [source for source in memory["sources"] if source["conversation_id"] != conversation_id]
        if memory["sources"]:
            kept.append(memory)
    memories[:] = kept


def contradiction_candidates(memories: list[dict[str, Any]]) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    """Flag likely mutually exclusive explicit current platform claims for review."""
    flags: list[tuple[dict[str, Any], dict[str, Any]]] = []
    current = [m for m in memories if m["category"] == "environment" and re.search(r"\b(?:use|using|run|running)\b", m["statement"], re.I)]
    for index, first in enumerate(current):
        for second in current[index + 1:]:
            if first.get("status") and second.get("status"):
                continue
            platform_a = set(re.findall(r"\b(?:windows\s*\d+|windows|linux|macos)\b", first["statement"], re.I))
            platform_b = set(re.findall(r"\b(?:windows\s*\d+|windows|linux|macos)\b", second["statement"], re.I))
            if platform_a and platform_b and platform_a != platform_b:
                flags.append((first, second))
    return flags


def resolve_current_environment(memories: list[dict[str, Any]]) -> None:
    """Use explicit timestamps to retain platform history while marking the newest fact.

    Missing timestamps deliberately leave claims unresolved for the review queue.
    """
    candidates: list[tuple[dict[str, Any], str, float]] = []
    for memory in memories:
        if memory["category"] != "environment" or not re.search(r"\b(?:use|using|run|running)\b", memory["statement"], re.I):
            continue
        platforms = re.findall(r"\b(?:windows\s*\d+|windows|linux|macos)\b", memory["statement"], re.I)
        timestamps = [source.get("timestamp") for source in memory.get("sources", [])]
        try:
            timestamp = max(float(value) for value in timestamps if value is not None)
        except (TypeError, ValueError):
            continue
        if platforms:
            candidates.append((memory, platforms[-1].lower(), timestamp))
    platforms = {platform for _, platform, _ in candidates}
    if len(platforms) < 2:
        return
    newest = max(timestamp for _, _, timestamp in candidates)
    for memory, _, timestamp in candidates:
        memory["status"] = "current" if timestamp == newest else "historical"
