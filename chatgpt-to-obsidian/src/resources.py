"""Resolve conversation metadata to local mirrored files and preserved web references."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import quote


@dataclass(frozen=True)
class AssetCatalog:
    """Maps export attachment identifiers to their mirrored relative paths."""

    assets: dict[str, str]

    def resolve(self, identifier: Any) -> str | None:
        if not isinstance(identifier, str) or not identifier:
            return None
        candidates = [identifier, f"{identifier}.dat"]
        if not identifier.startswith("file-"):
            candidates.extend([f"file-{identifier}", f"file-{identifier}.dat"])
        for candidate in candidates:
            if candidate in self.assets:
                return candidate
        return None

    def display_name(self, filename: str) -> str:
        return self.assets.get(filename, filename)


def load_asset_catalog(source: Path) -> AssetCatalog:
    """Read the local export's asset-name index; absent or malformed indexes are safe."""
    index = source / "conversation_asset_file_names.json"
    try:
        value = json.loads(index.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return AssetCatalog({})
    if not isinstance(value, dict):
        return AssetCatalog({})
    assets: dict[str, str] = {}
    for filename, display_name in value.items():
        if isinstance(filename, str) and (source / filename).is_file():
            assets[filename] = str(display_name) if isinstance(display_name, str) and display_name else filename
    return AssetCatalog(assets)


def _items(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, dict):
        return [value]
    return [item for item in value if isinstance(item, dict)] if isinstance(value, list) else []


def _walk_urls(value: Any, results: list[tuple[str, str]], seen: set[str]) -> None:
    if isinstance(value, list):
        for item in value:
            _walk_urls(item, results, seen)
        return
    if not isinstance(value, dict):
        return
    for key in ("url", "cloud_doc_url"):
        url = value.get(key)
        if isinstance(url, str) and url.startswith(("https://", "http://")) and url not in seen:
            seen.add(url)
            label = value.get("title") or value.get("name") or value.get("attribution") or "External resource"
            results.append((str(label), url))
    for child in value.values():
        if isinstance(child, (dict, list)):
            _walk_urls(child, results, seen)


def message_resources(metadata: Any, catalog: AssetCatalog) -> dict[str, list[tuple[str, str] | str]]:
    """Extract local assets, web references, and unresolved attachment identifiers."""
    if not isinstance(metadata, dict):
        return {"local": [], "web": [], "unresolved": []}
    local: list[tuple[str, str]] = []
    unresolved: list[str] = []
    known_local: set[str] = set()
    candidates = _items(metadata.get("attachments"))
    for reference in _items(metadata.get("content_references")):
        if "library_file_id" in reference:
            candidates.append(reference)
    for item in candidates:
        identifier = item.get("id") or item.get("library_file_id")
        filename = catalog.resolve(identifier)
        label = str(item.get("name") or (catalog.display_name(filename) if filename else None) or identifier or "Attachment")
        if filename:
            if filename not in known_local:
                known_local.add(filename)
                local.append((label, filename))
        elif identifier:
            unresolved.append(str(identifier))
    web: list[tuple[str, str]] = []
    seen_urls: set[str] = set()
    for key in ("content_references", "image_results", "search_result_groups", "conversation_context_citation_metadata"):
        _walk_urls(metadata.get(key), web, seen_urls)
    return {"local": local, "web": web, "unresolved": sorted(set(unresolved))}


def relative_asset_url(asset_filename: str) -> str:
    """Return a URL-safe path from an archive note to the mirrored export file."""
    return "../../../Raw/Export/" + quote(asset_filename.replace("\\", "/"), safe="/-_.~")
