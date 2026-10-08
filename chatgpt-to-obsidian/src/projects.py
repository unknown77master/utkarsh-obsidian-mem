"""Project navigation notes derived from explicit, local project references."""
from __future__ import annotations

import hashlib
import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote

_AFTER_PROJECT = re.compile(
    r"\b(?:my\s+)?project\s+(?:(?:called|named)\s+)?[\"'`*]*(?P<names>[A-Za-z0-9][A-Za-z0-9_-]*(?:\s+(?:and|&)\s+[A-Za-z0-9][A-Za-z0-9_-]*)*)",
    re.IGNORECASE,
)
_BEFORE_PROJECT = re.compile(
    r"\b(?:this|my|our|the)\s+(?P<name>(?:[A-Za-z0-9][A-Za-z0-9_-]*\s+){0,2}[A-Za-z0-9][A-Za-z0-9_-]*)\s+project\b",
    re.IGNORECASE,
)
_NON_NAMES = {
    "a", "an", "the", "this", "that", "my", "our", "your", "project", "projects", "scope", "statement",
    "section", "context", "includes", "include", "for", "of", "to", "in", "on", "with", "about", "work",
    "working", "building", "developing", "coding", "creating", "using", "personal", "growth", "future", "new",
    "problem",
}
_ACRONYMS = {"ai", "api", "csv", "gst", "ml", "ocr", "pdf", "sql", "ui", "ux"}


def _yaml(data: dict[str, Any]) -> str:
    return "---\n" + "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in data.items()) + "\n---\n"


def _write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8", newline="\n")
    temporary.replace(path)


def safe_name(value: str, fallback: str = "Untitled") -> str:
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "-", value)
    value = re.sub(r"\s+", " ", value).strip(" .")[:110]
    return value or fallback


def markdown_escape(value: str) -> str:
    return value.replace("\x00", "").replace("\r\n", "\n").replace("\r", "\n").replace("[", "\\[").replace("]", "\\]")


def _display_name(value: str) -> str:
    return " ".join(part.upper() if part.isupper() or part.casefold() in _ACRONYMS else part[:1].upper() + part[1:] for part in value.split())


def _project_names(statement: str) -> list[str]:
    """Return only names written explicitly next to the word 'project'."""
    names: list[str] = []
    for match in _AFTER_PROJECT.finditer(statement):
        for name in re.split(r"\s+(?:and|&)\s+", match.group("names"), flags=re.IGNORECASE):
            normalized = name.strip(" .,:;!?*`'\"")
            if normalized and normalized.casefold() not in _NON_NAMES:
                names.append(_display_name(normalized))
    for match in _BEFORE_PROJECT.finditer(statement):
        words = [word for word in match.group("name").split() if word.casefold() not in _NON_NAMES]
        if words:
            names.append(_display_name(" ".join(words)))
    return list(dict.fromkeys(names))


def _archive_href(relative: str) -> str:
    return quote("../" + relative.replace("\\", "/"), safe="/-_.~")


def _managed_project_index(path: Path) -> bool:
    try:
        header = path.read_text(encoding="utf-8")[:700]
    except OSError:
        return False
    return 'type: "project-index"' in header and 'generated_by: "chatgpt-to-obsidian"' in header


def _remove_stale_indexes(projects_directory: Path, retained: set[Path]) -> None:
    if not projects_directory.is_dir():
        return
    for path in projects_directory.glob("*.md"):
        if path not in retained and _managed_project_index(path):
            path.unlink()


def _project_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def _project_groups(memories: list[dict[str, Any]], catalog: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    groups: dict[str, dict[str, Any]] = {}
    unclassified: list[dict[str, Any]] = []
    for memory in memories:
        if memory.get("category") != "project":
            continue
        names = _project_names(memory.get("statement", ""))
        if not names:
            unclassified.append(memory)
            continue
        for name in names:
            key = _project_key(name)
            group = groups.setdefault(key, {"name": name, "memories": [], "local": [], "github": []})
            group["memories"].append(memory)
    for project in catalog or []:
        name = project.get("name")
        if not isinstance(name, str) or not name.strip():
            continue
        key = _project_key(name)
        group = groups.setdefault(key, {"name": name, "memories": [], "local": [], "github": []})
        group["local" if project.get("catalog_source") == "local" else "github"].append(project)
    result = sorted(groups.values(), key=lambda group: group["name"].casefold())
    if unclassified:
        result.append({"name": "Unclassified Project Discussions", "memories": unclassified, "local": [], "github": [], "unclassified": True})
    return result


def _sources(memories: list[dict[str, Any]]) -> list[dict[str, Any]]:
    known: dict[str, dict[str, Any]] = {}
    for memory in memories:
        for source in memory.get("sources", []):
            conversation_id = source.get("conversation_id")
            if conversation_id:
                known.setdefault(conversation_id, source)
    return sorted(known.values(), key=lambda source: ((source.get("title") or "Untitled").casefold(), source["conversation_id"]))


def _index_content(group: dict[str, Any], archive_paths: dict[str, str], updated: str, has_project_home: bool = False) -> str:
    memories = group["memories"]
    sources = _sources(memories)
    frontmatter = _yaml({
        "type": "project-index",
        "scope": "project",
        "project": group["name"],
        "generated_by": "chatgpt-to-obsidian",
        "updated": updated,
        "durable_context_count": len(memories),
        "chat_count": len(sources),
        "local_repository_count": len(group["local"]),
        "github_repository_count": len(group["github"]),
    })
    explanation = (
        "This generated index groups exact project-name matches from the export and repository catalogue. "
        "Its counts describe automatic extraction, not all available project context."
    )
    if group.get("unclassified"):
        explanation = (
            "These conversations contain durable project context, but no unambiguous project name was stated. "
            "They remain grouped here for review rather than being assigned an invented project name."
        )
    lines = [frontmatter + f"# {group['name']} Project Index\n", explanation]
    if has_project_home:
        home_directory = safe_name(group["name"])
        lines.extend(["", "## Start here", "", f"- [{markdown_escape(group['name'])} Project Home](<{home_directory}/Project Home.md>) — maintained context and links to current status, requirements, and history."])
    if group["local"]:
        lines.extend(["", "## Local repositories", ""])
        for project in group["local"]:
            lines.append(f"- `{project['path']}` — detected by `{project['marker']}`")
            for remote in project.get("remotes", []):
                remote_text = markdown_escape(remote)
                if remote.startswith("https://"):
                    lines.append(f"  - Remote: [{remote_text}]({remote})")
                else:
                    lines.append(f"  - Remote: `{remote_text}`")
    if group["github"]:
        lines.extend(["", "## Public GitHub repositories", ""])
        for project in group["github"]:
            details = [project.get("language"), "fork" if project.get("fork") else "", project.get("updated_at")]
            suffix = "; ".join(markdown_escape(value) for value in details if value)
            description = markdown_escape(project.get("description") or "")
            lines.append(f"- [{markdown_escape(project['name'])}]({project['github_url']})" + (f" — {suffix}" if suffix else "") + (f": {description}" if description else ""))
    lines.extend(["", "## Durable context", ""])
    lines.extend(f"- {markdown_escape(memory['statement'])}" for memory in memories)
    if not memories:
        lines.append("- No statements were automatically assigned to this exact project name. Check maintained notes and earlier names before concluding that context is absent.")
    lines.extend(["", "## Related chats", ""])
    for source in sources:
        target = archive_paths.get(source["conversation_id"])
        title = markdown_escape(source.get("title") or "Untitled conversation")
        if target:
            lines.append(f"- [{title}](<{_archive_href(target)}>)")
        else:
            lines.append(f"- {title} (transcript unavailable; conversation ID `{source['conversation_id']}`)")
    if not sources:
        lines.append("- No chats were automatically assigned to this exact project name.")
    lines.extend(["", "## Resources", ""])
    resource_links = []
    for project in group["github"]:
        resource_links.append(f"- [{markdown_escape(project['name'])} repository]({project['github_url']})")
    for source in sources:
        target = archive_paths.get(source["conversation_id"])
        if target:
            title = markdown_escape(source.get("title") or "Untitled conversation")
            resource_links.append(f"- [{title} resources](<{_archive_href(target)}#Resources>)")
    lines.extend(resource_links or ["- No linked transcript resources are available yet."])
    return "\n".join(lines) + "\n"


def render_project_indexes(output: Path, memories: list[dict[str, Any]], archive_paths: dict[str, str], catalog: list[dict[str, Any]] | None = None) -> list[Path]:
    """Build a root map and one index per known project without duplicating chats."""
    projects_directory = output / "Projects"
    updated = datetime.now(timezone.utc).date().isoformat()
    groups = _project_groups(memories, catalog)
    paths: list[Path] = []
    used_names: set[str] = set()
    index_rows: list[tuple[dict[str, Any], Path, int]] = []
    project_homes: list[tuple[str, Path]] = []
    for group in groups:
        filename = safe_name(f"{group['name']} Project Index")
        key = filename.casefold()
        if key in used_names:
            suffix = hashlib.sha256(group["name"].encode("utf-8")).hexdigest()[:8]
            filename = f"{filename}--{suffix}"
        used_names.add(filename.casefold())
        path = projects_directory / f"{filename}.md"
        project_home = projects_directory / safe_name(group["name"]) / "Project Home.md"
        has_project_home = project_home.is_file()
        _write(path, _index_content(group, archive_paths, updated, has_project_home))
        if has_project_home:
            project_homes.append((group["name"], project_home))
        paths.append(path)
        index_rows.append((group, path, len(_sources(group["memories"]))))
    root = projects_directory / "Projects Index.md"
    root_lines = [
        _yaml({
            "type": "project-index",
            "scope": "projects",
            "generated_by": "chatgpt-to-obsidian",
            "updated": updated,
            "project_count": len(groups),
        }) + "# Projects Index\n",
        "Use this map to retrieve local repositories, public GitHub repositories, durable context, source chats, and their resource sections. "
        "[Projects](<../05 - Projects.md>) remains the consolidated memory-category note. Generated counts refer only to automatic exact-name extraction; check maintained project homes and older names before concluding that context is absent.",
        "",
    ]
    if project_homes:
        root_lines.extend(["## Maintained project homes", ""])
        for name, home in project_homes:
            root_lines.append(f"- [{markdown_escape(name)}](<{home.relative_to(projects_directory).as_posix()}>)")
        root_lines.append("")
    root_lines.extend(["## Project indexes", ""])
    if index_rows:
        for group, path, chat_count in index_rows:
            sources = []
            if group["local"]:
                sources.append(f"{len(group['local'])} local")
            if group["github"]:
                sources.append(f"{len(group['github'])} GitHub")
            if chat_count:
                sources.append(f"{chat_count} chat{'s' if chat_count != 1 else ''}")
            root_lines.append(f"- [{markdown_escape(group['name'])}](<{path.name}>)" + (f" — {', '.join(sources)}" if sources else ""))
    else:
        root_lines.append("- No durable project references were extracted yet.")
    _write(root, "\n".join(root_lines) + "\n")
    paths.append(root)
    _remove_stale_indexes(projects_directory, set(paths))
    return paths
