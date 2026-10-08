"""Optional searchable conversation archive renderer."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

from .obsidian import _write, _yaml, markdown_escape, safe_name
from .resources import AssetCatalog, message_resources, relative_asset_url


def _archive_date(timestamp: Any) -> tuple[str, str]:
    try:
        value = datetime.fromtimestamp(float(timestamp), timezone.utc)
        return str(value.year), value.date().isoformat()
    except (TypeError, ValueError, OSError):
        return "Unknown year", "Unknown date"


def _index_frontmatter(scope: str, transcript_count: int, year: str | None = None, date: str | None = None) -> str:
    data: dict[str, Any] = {"type": "chat-index", "scope": scope, "generated_by": "chatgpt-to-obsidian", "updated": datetime.now(timezone.utc).date().isoformat(), "transcript_count": transcript_count}
    if year:
        data["year"] = year
    if date:
        data["date"] = date
    return _yaml(data)


def _index_link(label: str, relative_path: str) -> str:
    return f"[{markdown_escape(label)}](<{quote(relative_path, safe='/-_.~')}>)"


def _resource_section(conversation: dict[str, Any], catalog: AssetCatalog) -> str:
    local: list[tuple[str, str]] = []
    web: list[tuple[str, str]] = []
    unresolved: set[str] = set()
    seen_local: set[str] = set()
    seen_web: set[str] = set()
    for message in conversation.get("messages", []):
        found = message_resources(message.get("metadata"), catalog)
        for label, filename in found["local"]:
            if filename not in seen_local:
                seen_local.add(filename)
                local.append((label, filename))
        for label, url in found["web"]:
            if url not in seen_web:
                seen_web.add(url)
                web.append((label, url))
        unresolved.update(found["unresolved"])
    lines = ["## Resources", ""]
    if local:
        lines.extend("### Local attachments\n".splitlines())
        lines.extend(f"- [{markdown_escape(label)}]({relative_asset_url(filename)})" for label, filename in local)
        lines.append("")
    if web:
        lines.extend("### External references\n".splitlines())
        lines.extend(f"- [{markdown_escape(label)}]({url})" for label, url in web)
        lines.append("")
    if unresolved:
        lines.extend(["### Unresolved export references", ""])
        lines.extend(f"- `{identifier}`" for identifier in sorted(unresolved))
        lines.append("")
    if not local and not web and not unresolved:
        lines.append("No structured attachments or external references were present in this conversation.\n")
    return "\n".join(lines)


def archive_conversation(output: Path, conversation: dict[str, Any], previous_relative: str | None = None, catalog: AssetCatalog | None = None) -> Path:
    year, date = _archive_date(conversation.get("created_at"))
    filename = f"{safe_name(conversation['title'])}--{safe_name(conversation['id'])[:12]}.md"
    path = output / "Archive" / year / date / filename
    relative = path.relative_to(output).as_posix()
    if previous_relative and previous_relative != relative:
        previous = output / previous_relative
        try:
            previous.resolve().relative_to((output / "Archive").resolve())
        except ValueError:
            previous = None
        if previous and previous.is_file():
            previous.unlink()
    resources = _resource_section(conversation, catalog or AssetCatalog({}))
    frontmatter = _yaml({"type": "chatgpt-conversation", "source": "ChatGPT export", "conversation_id": conversation["id"], "created": conversation.get("created_at"), "updated": conversation.get("updated_at"), "resource_section": True})
    blocks = [frontmatter, f"# {markdown_escape(conversation['title'])}\n"]
    for message in conversation.get("messages", []):
        role = str(message.get("role") or "unknown").capitalize()
        blocks.append(f"## {role}\n\n{markdown_escape(message['content'])}\n")
    blocks.append(resources)
    _write(path, "\n".join(blocks))
    return path


def render_archive_indexes(output: Path, archive_paths: dict[str, str], previous_indexes: list[str] | None = None) -> list[str]:
    """Link every transcript into year and date navigation notes."""
    archive_root = output / "Archive"
    grouped: dict[str, dict[str, list[str]]] = {}
    for relative in archive_paths.values():
        path = output / relative
        try:
            path.resolve().relative_to(archive_root.resolve())
        except ValueError:
            continue
        if not path.is_file() or path.name.endswith("Chat Index.md"):
            continue
        parts = Path(relative).parts
        if len(parts) < 4:
            continue
        year, date = parts[1], parts[2]
        grouped.setdefault(year, {}).setdefault(date, []).append(relative)
    current: list[str] = ["Archive/Chat History Index.md"]
    root_lines = [_index_frontmatter("archive", sum(len(items) for dates in grouped.values() for items in dates.values())), "# Chat History Index", "", "Every transcript is organized by its UTC creation year, date, and chat topic.", ""]
    for year in sorted(grouped):
        year_transcripts = sum(len(items) for items in grouped[year].values())
        year_readme = f"Archive/{year}/{year} Chat Index.md"
        current.append(year_readme)
        root_lines.append(f"- {_index_link(f'{year} — {year_transcripts} chats', f'{year}/{year} Chat Index.md')}")
        year_lines = [_index_frontmatter("year", year_transcripts, year=year), f"# {year} Chat Index", ""]
        for date in sorted(grouped[year]):
            date_transcripts = len(grouped[year][date])
            date_readme = f"Archive/{year}/{date}/{date} Chat Index.md"
            current.append(date_readme)
            year_lines.append(f"- {_index_link(f'{date} — {date_transcripts} chats', f'{date}/{date} Chat Index.md')}")
            date_lines = [_index_frontmatter("date", date_transcripts, year=year, date=date), f"# {date} Chat Index", ""]
            for relative in sorted(grouped[year][date], key=str.lower):
                topic = Path(relative).stem.rsplit("--", 1)[0]
                date_lines.append(f"- {_index_link(topic, Path(relative).name)}")
            _write(output / date_readme, "\n".join(date_lines) + "\n")
        _write(output / year_readme, "\n".join(year_lines) + "\n")
    _write(archive_root / "Chat History Index.md", "\n".join(root_lines) + "\n")
    for relative in previous_indexes or []:
        if relative in current:
            continue
        path = output / relative
        try:
            path.resolve().relative_to(archive_root.resolve())
        except ValueError:
            continue
        if path.is_file() and (path.name == "README.md" or "generated_by: \"chatgpt-to-obsidian\"" in path.read_text(encoding="utf-8", errors="replace")):
            path.unlink()
    legacy_root = archive_root / "README.md"
    if legacy_root.is_file():
        legacy_root.unlink()
    return current
