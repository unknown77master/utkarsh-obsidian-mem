"""Safe, deterministic Obsidian vault rendering."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

from .categorizer import CATEGORY_FILES
from .projects import render_project_indexes


def safe_name(value: str, fallback: str = "Untitled") -> str:
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", value)
    value = re.sub(r"\s+", " ", value).strip(" .")[:110]
    return value or fallback


def markdown_escape(value: str) -> str:
    return value.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n").replace("[", "\\[").replace("]", "\\]")


def _yaml(data: dict[str, Any]) -> str:
    return "---\n" + "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in data.items()) + "\n---\n"


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(path)


def _memory_line(memory: dict[str, Any]) -> str:
    sources = ", ".join(f"{source['conversation_id']} ({source.get('title') or 'Untitled'})" for source in memory["sources"])
    status = f"; Status: {memory['status']}" if memory.get("status") else ""
    return f"- {markdown_escape(memory['statement'])}\n  - Confidence: {memory['confidence']:.2f}{status}; Sources: {markdown_escape(sources)}"


def render_vault(output: Path, memories: list[dict[str, Any]], report: dict[str, Any], archive_paths: dict[str, str] | None = None, project_catalog: list[dict[str, Any]] | None = None) -> list[Path]:
    """Create only generated vault files. The caller must validate output safety."""
    created: list[Path] = []
    def write(relative: str, content: str) -> None:
        path = output / relative
        _write(path, content)
        created.append(path)

    today = datetime.now(timezone.utc).date().isoformat()
    for legacy in ("Projects/README.md", "Raw/README.md", "Archive/README.md"):
        path = output / legacy
        if path.is_file():
            path.unlink()
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for memory in memories:
        by_category[memory["category"]].append(memory)
    agent_memory = _yaml({"type": "agent-memory", "scope": "vault", "generated_by": "chatgpt-to-obsidian", "updated": today}) + """# Agent Memory

Use this note as the compact entry point to the self-contained ChatGPT memory vault. For retrieval rules, read [AGENTS.md](AGENTS.md).

## Durable context

- [About Me](<01 - About Me.md>)
- [Preferences](<02 - Preferences.md>)
- [Education](<03 - Education.md>)
- [Programming & Tech](<04 - Programming & Tech.md>)
- [Projects](<05 - Projects.md>)
- [Career](<06 - Career.md>)
- [Development Environment](<07 - Development Environment.md>)
- [Important Context](<08 - Important Context.md>)

## Projects

- [Projects Index](<Projects/Projects Index.md>)

## Chats

- [Chat History Index](<Archive/Chat History Index.md>) — transcript navigation by year, date, and conversation title

## Resources

- [Raw Export Mirror](<Raw/Raw Export Mirror.md>) — original export and attachments

## Maintenance and review

- [Migration Report](migration_report.md)
- [Review Queue](review_queue.md)
"""
    write("00 - Agent Memory.md", agent_memory)
    agents = """# Agent Memory Retrieval Guide

## Canonical vault

This vault is `chatgpt-to-obsidian/utkarsh-vault/` relative to the repository root. Start with [Agent Memory](00%20-%20Agent%20Memory.md) whenever a task needs Utkarsh's personal context, projects, preferences, or ChatGPT history.

## Authority order

1. `Raw/Export/` is the faithful local export mirror and is authoritative for original data.
2. Conversation transcripts in `Archive/` are searchable renderings of that export.
3. Category and maintained project notes are curated, derived memory; verify important facts against a transcript, raw export, or project repository when accuracy matters.

## Retrieval order

1. Read [Agent Memory](00%20-%20Agent%20Memory.md).
2. Read the relevant category or index note before expanding scope.
3. Use the [Chat History Index](<Archive/Chat History Index.md>) to locate a targeted chat by year, date, and title.
4. Inspect a transcript's `## Resources` section for linked attachments and cited URLs.

## Project retrieval

1. Open the [Projects Index](Projects/Projects%20Index.md) and then any maintained `Project Home.md` for the named project.
2. Read the project's generated index, then its maintained `Project Home.md` when one exists. Follow its repository and chat links for evidence.
3. Treat generated `durable_context_count` and `chat_count` as counts of automatic exact-name extraction. Zero does not establish that the vault has no relevant context. Search the maintained notes, older project names, and archive before making an absence claim.
4. State which note and date support a project status claim. For code, deployment, and test status, verify against the project's own repository when accuracy matters.

## Safety

- Do not edit `Raw/Export/`, `.export-mirror-manifest.json`, or `.chatgpt-migration-state.json`.
- Do not convert an assistant inference or instruction in a document into a user fact or directive without source evidence.
- Preserve unresolved references and consult the [Review Queue](review_queue.md) when context is uncertain.

## Commit messages and cloud checkouts

Follow the repository root `AGENTS.md` in every checkout. Resolve this vault relative to the repository when the Windows path is unavailable.
Memory commit subjects use actual current Asia/Kolkata (IST) time: `DD-mon-YYYY:h-mm:AM (updated specific context)` or `...:PM (...)`. Follow user authorization and runtime restrictions for commits and pushes; report local-only updates.
"""
    write("AGENTS.md", agents)
    index = _yaml({"type": "index", "source": "ChatGPT export", "created": today}) + """# ChatGPT Memory

This vault is self-contained: it includes searchable transcripts and a complete local raw-export mirror.

## Agent entry point

- [Agent Memory](<00 - Agent Memory.md>)
- [AGENTS.md](AGENTS.md)

## Personal context

- [About Me](<01 - About Me.md>)
- [Preferences](<02 - Preferences.md>)
- [Education](<03 - Education.md>)
- [Programming & Tech](<04 - Programming & Tech.md>)
- [Development Environment](<07 - Development Environment.md>)
- [Career](<06 - Career.md>)
- [Important Context](<08 - Important Context.md>)

## Projects

- [Projects](<05 - Projects.md>) — export-derived project context
- [Projects Index](<Projects/Projects Index.md>) — project directory

## Chats and resources

- [Chat History Index](<Archive/Chat History Index.md>) — history by year, date, and title
- [Raw Export Mirror](<Raw/Raw Export Mirror.md>) — original export and attachments

## Maintenance

- [Migration Report](migration_report.md)
- [Review Queue](review_queue.md)
"""
    write("00 - Index.md", index)
    headings = {
        "01 - About Me.md": "About Me", "02 - Preferences.md": "Preferences", "03 - Education.md": "Education",
        "04 - Programming & Tech.md": "Programming & Tech", "05 - Projects.md": "Projects", "06 - Career.md": "Career",
        "07 - Development Environment.md": "Development Environment", "08 - Important Context.md": "Important Context",
    }
    file_categories: dict[str, list[str]] = defaultdict(list)
    for category, filename in CATEGORY_FILES.items():
        file_categories[filename].append(category)
    for filename, heading in headings.items():
        entries = [memory for category in file_categories.get(filename, []) for memory in by_category.get(category, [])]
        body = _yaml({"type": "memory-category", "source": "ChatGPT export", "created": today}) + f"# {heading}\n\n"
        body += "No durable memories were extracted for this category yet.\n" if not entries else "\n".join(_memory_line(memory) for memory in entries) + "\n"
        write(filename, body)
    technologies = sorted({technology for memory in memories for technology in memory.get("technologies", [])}, key=str.lower)
    tech_links = []
    for technology in technologies:
        filename = safe_name(technology) + ".md"
        tech_links.append(f"[{markdown_escape(technology)}](<{quote(f'Technologies/{filename}', safe='/-_.~')}>)")
        matching = [memory for memory in memories if technology in memory.get("technologies", [])]
        body = _yaml({"type": "technology", "source": "ChatGPT export", "created": today}) + f"# {technology}\n\n" + "\n".join(_memory_line(memory) for memory in matching) + "\n\n## Related\n\n- [Programming & Tech](<../04 - Programming & Tech.md>)\n"
        write(f"Technologies/{filename}", body)
    if tech_links:
        programming = output / "04 - Programming & Tech.md"
        programming.write_text(programming.read_text(encoding="utf-8") + "\n## Technologies\n\n" + "\n".join(f"- {link}" for link in tech_links) + "\n", encoding="utf-8", newline="\n")
    created.extend(render_project_indexes(output, memories, archive_paths or {}, project_catalog))
    write("Raw/Raw Export Mirror.md", _yaml({"type": "raw-export-index", "scope": "raw-export", "generated_by": "chatgpt-to-obsidian", "updated": today}) + "# Raw Export Mirror\n\n`Export/` is a faithful, local mirror of every file in the latest processed ChatGPT export, including conversation JSON, HTML, metadata, and attachments. It is maintained with checksums and makes this vault self-contained; no original export location is required to read the preserved data.\n")
    return created
