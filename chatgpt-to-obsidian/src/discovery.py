"""Read-only discovery of ChatGPT export files."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Inventory:
    source: Path
    conversation_files: list[Path] = field(default_factory=list)
    memory_files: list[Path] = field(default_factory=list)
    shared_files: list[Path] = field(default_factory=list)
    html_files: list[Path] = field(default_factory=list)
    asset_count: int = 0
    other_json_files: list[Path] = field(default_factory=list)

    @property
    def all_files(self) -> list[Path]:
        return self.conversation_files + self.memory_files + self.shared_files + self.html_files + self.other_json_files


def _looks_like_conversations(path: Path) -> bool:
    name = path.name.lower()
    if "shared" in name or "asset" in name or "file_name" in name:
        return False
    if name == "conversations.json" or name.startswith("conversations-"):
        return True
    # Keep this cheap and local: only inspect a short prefix, never the whole file.
    try:
        with path.open("rb") as handle:
            prefix = handle.read(32_768).lower()
        return b'"mapping"' in prefix and (b'"conversation_id"' in prefix or b'"current_node"' in prefix)
    except OSError:
        return False


def discover(source: Path) -> Inventory:
    """Return an inventory without changing *source* or opening binary assets."""
    if not source.is_dir():
        raise FileNotFoundError(f"Source directory does not exist: {source}")
    inventory = Inventory(source=source)
    for path in source.rglob("*"):
        if not path.is_file():
            continue
        suffix, name = path.suffix.lower(), path.name.lower()
        if suffix != ".json":
            if suffix in {".dat", ".bin", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".pdf", ".zip"}:
                inventory.asset_count += 1
            elif suffix in {".html", ".htm"}:
                inventory.html_files.append(path)
            continue
        if _looks_like_conversations(path):
            inventory.conversation_files.append(path)
        elif "memory" in name:
            inventory.memory_files.append(path)
        elif "shared" in name and "conversation" in name:
            inventory.shared_files.append(path)
        else:
            inventory.other_json_files.append(path)
    for paths in (inventory.conversation_files, inventory.memory_files, inventory.shared_files, inventory.html_files, inventory.other_json_files):
        paths.sort(key=lambda p: str(p).lower())
    return inventory


def format_inventory(inventory: Inventory) -> str:
    lines = ["Found:"]
    for path in inventory.all_files:
        lines.append(f"  {path.relative_to(inventory.source)}")
    if inventory.asset_count:
        lines.append(f"  {inventory.asset_count} asset files (ignored during first pass)")
    lines.extend(["", f"Conversation files: {len(inventory.conversation_files)}"])
    return "\n".join(lines)
