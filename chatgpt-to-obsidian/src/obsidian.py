"""Safe, deterministic Obsidian vault rendering."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

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
    agent_memory = _yaml({"type": "agent-memory", "scope": "vault", "generated_by": "chatgpt-to-obsidian", "updated": today}) + "# Agent Memory\n\nUse this note as the compact entry point to the self-contained ChatGPT memory vault. For machine retrieval rules, read [[AGENTS]].\n\n## Durable context\n\n- [[01 - About Me]]\n- [[02 - Preferences]]\n- [[03 - Education]]\n- [[04 - Programming & Tech]]\n- [[05 - Projects]]\n- [[06 - Career]]\n- [[07 - Development Environment]]\n- [[08 - Important Context]]\n\n## Projects\n\n- [[Projects/Projects Index]]\n\n## Chats\n\n- [[Archive/Chat History Index]] — transcript navigation by year, date, and conversation title\n\n## Resources\n\n- [[Raw/Raw Export Mirror]] — exact local export mirror and attachments\n- [[04 - Programming & Tech]] — technology context\n\n## Maintenance and review\n\n- [[migration_report]]\n- [[review_queue]]\n"
    write("00 - Agent Memory.md", agent_memory)
    agents = f"# Agent Memory Retrieval Guide\n\n## Canonical vault\n\nThis personal-memory vault is located at `{output.resolve()}`. Start with [[00 - Agent Memory]] whenever a task needs Utkarsh's personal context, projects, preferences, or ChatGPT history.\n\n## Authority order\n\n1. `Raw/Export/` is the faithful local export mirror and is authoritative for original data.\n2. Conversation transcripts in `Archive/` are searchable renderings of that export.\n3. Category notes are curated, derived memory; verify important facts against a transcript or raw export when accuracy matters.\n\n## Retrieval order\n\n1. Read [[00 - Agent Memory]].\n2. Read the relevant category or index note before expanding scope.\n3. Use [[Archive/Chat History Index]] to locate a targeted chat by year, date, and title.\n4. Inspect a transcript's `## Resources` section for linked attachments and cited URLs.\n\n## Safety\n\n- Do not edit `Raw/Export/`, `.export-mirror-manifest.json`, or `.chatgpt-migration-state.json`.\n- Do not convert an assistant inference into a user fact without source evidence.\n- Preserve unresolved references and consult [[review_queue]] when context is uncertain.\n"
    write("AGENTS.md", agents)
    index = _yaml({"type": "index", "source": "ChatGPT export", "created": today}) + "# ChatGPT Memory\n\nThis vault is self-contained: it includes searchable transcripts and a complete local raw-export mirror.\n\n## Agent entry point\n\n- [[00 - Agent Memory]]\n- [[AGENTS]]\n\n## Personal Context\n\n- [[01 - About Me]]\n- [[02 - Preferences]]\n\n## Education\n\n- [[03 - Education]]\n\n## Technical\n\n- [[04 - Programming & Tech]]\n- [[07 - Development Environment]]\n\n## Projects\n\n- [[05 - Projects]] — durable project context\n- [[Projects/Projects Index]] — project navigation\n\n## Chats\n\n- [[Archive/Chat History Index]] — searchable history by year, date, and conversation title\n\n## Resources\n\n- [[Raw/Raw Export Mirror]] — raw export, attachments, and metadata\n- [[04 - Programming & Tech]] — technology resources\n\n## Career\n\n- [[06 - Career]]\n\n## Important Context\n\n- [[08 - Important Context]]\n\n## Maintenance\n\n- [[migration_report]]\n- [[review_queue]]\n"
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
        tech_links.append(f"[[Technologies/{safe_name(technology)}]]")
        matching = [memory for memory in memories if technology in memory.get("technologies", [])]
        body = _yaml({"type": "technology", "source": "ChatGPT export", "created": today}) + f"# {technology}\n\n" + "\n".join(_memory_line(memory) for memory in matching) + "\n\n## Related\n\n- [[04 - Programming & Tech]]\n"
        write(f"Technologies/{filename}", body)
    if tech_links:
        programming = output / "04 - Programming & Tech.md"
        programming.write_text(programming.read_text(encoding="utf-8") + "\n## Technologies\n\n" + "\n".join(f"- {link}" for link in tech_links) + "\n", encoding="utf-8", newline="\n")
    created.extend(render_project_indexes(output, memories, archive_paths or {}, project_catalog))
    write("Raw/Raw Export Mirror.md", _yaml({"type": "raw-export-index", "scope": "raw-export", "generated_by": "chatgpt-to-obsidian", "updated": today}) + "# Raw Export Mirror\n\n`Export/` is a faithful, local mirror of every file in the latest processed ChatGPT export, including conversation JSON, HTML, metadata, and attachments. It is maintained with checksums and makes this vault self-contained; no original export location is required to read the preserved data.\n")
    return created
