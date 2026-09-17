"""Noise-reducing, loss-aware conversation normalization."""
from __future__ import annotations

import hashlib
import json
import re
from typing import Any


def clean_text(value: str) -> str:
    return re.sub(r"[ \t]+", " ", re.sub(r"\n{3,}", "\n\n", value)).strip()


def normalize_conversation(conversation: dict[str, Any]) -> dict[str, Any]:
    messages: list[dict[str, Any]] = []
    last_key = ""
    for message in conversation.get("messages", []):
        content = clean_text(str(message.get("content") or ""))
        role = str(message.get("role") or "unknown").lower()
        if not content:
            continue
        # Repeated fragments commonly appear in regenerated/streamed messages.
        key = f"{role}\0{content}"
        if key == last_key:
            continue
        last_key = key
        messages.append({**message, "role": role, "content": content})
    normalized = {**conversation, "title": clean_text(conversation.get("title", "")) or "Untitled conversation", "messages": messages}
    fingerprint_payload = [(m["role"], m["content"], m.get("timestamp")) for m in messages]
    normalized["fingerprint"] = hashlib.sha256(json.dumps(fingerprint_payload, ensure_ascii=False, default=str).encode("utf-8")).hexdigest()
    return normalized
