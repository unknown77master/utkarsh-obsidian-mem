"""Local-only extraction of explicit, durable user statements."""
from __future__ import annotations

import re
from typing import Any

from .categorizer import category_for, technologies_in

_DURABLE = re.compile(r"\b(i\s+(?:am|['’]m|use|prefer|like|dislike|work|study|build|develop|maintain|want|need|always|never|live)|my\s+(?:project|workflow|preference|setup|environment)|we\s+(?:use|build|maintain)|this\s+project)\b", re.IGNORECASE)
_TEMPORARY = re.compile(r"\b(today|tonight|tomorrow|this\s+(?:morning|afternoon|evening|week)|right\s+now|for\s+today)\b", re.IGNORECASE)


def _sentences(text: str) -> list[str]:
    return [part.strip(" \t\n-•") for part in re.split(r"(?<=[.!?])\s+|\n+", text) if part.strip()]


def extract_memories(conversation: dict[str, Any]) -> list[dict[str, Any]]:
    """Return conservative candidates; no fact is inferred from assistant text."""
    results: list[dict[str, Any]] = []
    for message in conversation.get("messages", []):
        if message.get("role") not in {"user", "human"}:
            continue
        for sentence in _sentences(message["content"]):
            if len(sentence) < 12 or len(sentence) > 600 or _TEMPORARY.search(sentence) or not _DURABLE.search(sentence):
                continue
            category = category_for(sentence)
            results.append({
                "statement": sentence,
                "category": category,
                "confidence": 0.82,
                "durability": "durable",
                "technologies": technologies_in(sentence),
                "sources": [{"conversation_id": conversation["id"], "title": conversation["title"], "timestamp": message.get("timestamp") or conversation.get("updated_at")}],
            })
    return results
