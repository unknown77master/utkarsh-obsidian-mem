"""Incremental, checksum-verified preservation of the complete local export."""
from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from pathlib import Path

MANIFEST_NAME = ".export-mirror-manifest.json"
CHUNK_SIZE = 1 << 20


@dataclass
class MirrorStats:
    files: int = 0
    bytes: int = 0
    copied: int = 0
    skipped: int = 0
    removed: int = 0


def _hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(block)
    return digest.hexdigest()


def inspect_export(source: Path) -> MirrorStats:
    stats = MirrorStats()
    for path in source.rglob("*"):
        if path.is_file():
            stats.files += 1
            stats.bytes += path.stat().st_size
    return stats


def _read_manifest(raw_root: Path) -> dict[str, dict[str, object]]:
    path = raw_root.parent / MANIFEST_NAME
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        files = value.get("files")
        if isinstance(files, dict):
            return {str(name): entry for name, entry in files.items() if isinstance(entry, dict)}
    except (OSError, json.JSONDecodeError):
        pass
    return {}


def _write_manifest(raw_root: Path, files: dict[str, dict[str, object]]) -> None:
    path = raw_root.parent / MANIFEST_NAME
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps({"version": 1, "files": files}, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, path)


def _safe_destination(raw_root: Path, relative: Path) -> Path:
    destination = raw_root / relative
    try:
        destination.resolve().relative_to(raw_root.resolve())
    except ValueError as exc:
        raise ValueError(f"Unsafe export path: {relative}") from exc
    return destination


def _copy_with_hash(source: Path, destination: Path) -> tuple[str, int]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = destination.with_name(destination.name + ".tmp")
    digest, size = hashlib.sha256(), 0
    with source.open("rb") as reader, temporary.open("wb") as writer:
        for block in iter(lambda: reader.read(CHUNK_SIZE), b""):
            writer.write(block)
            digest.update(block)
            size += len(block)
    os.replace(temporary, destination)
    return digest.hexdigest(), size


def mirror_export(source: Path, output: Path) -> MirrorStats:
    """Mirror every source file under Raw/Export without ever writing to source."""
    raw_root = output / "Raw" / "Export"
    raw_root.mkdir(parents=True, exist_ok=True)
    previous = _read_manifest(raw_root)
    current: dict[str, dict[str, object]] = {}
    stats = MirrorStats()
    for path in sorted((item for item in source.rglob("*") if item.is_file()), key=lambda item: str(item).lower()):
        relative = path.relative_to(source)
        key = relative.as_posix()
        destination = _safe_destination(raw_root, relative)
        stats.files += 1
        source_size = path.stat().st_size
        stats.bytes += source_size
        recorded_hash = previous.get(key, {}).get("sha256")
        if destination.is_file() and isinstance(recorded_hash, str) and destination.stat().st_size == source_size and _hash(path) == recorded_hash and _hash(destination) == recorded_hash:
            digest = recorded_hash
            stats.skipped += 1
        else:
            digest, copied_size = _copy_with_hash(path, destination)
            if copied_size != source_size:
                raise OSError(f"Incomplete copy of {relative}")
            stats.copied += 1
        current[key] = {"sha256": digest, "bytes": source_size}
    for key in sorted(set(previous) - set(current)):
        destination = _safe_destination(raw_root, Path(key))
        if destination.is_file():
            destination.unlink()
            stats.removed += 1
    for directory in sorted((item for item in raw_root.rglob("*") if item.is_dir()), key=lambda item: len(item.parts), reverse=True):
        try:
            directory.rmdir()
        except OSError:
            pass
    _write_manifest(raw_root, current)
    return stats
