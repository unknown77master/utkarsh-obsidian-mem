"""Discover local coding repositories and optionally public GitHub repositories."""
from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any
from urllib.error import URLError
from urllib.request import Request, urlopen

_SKIP_DIRECTORIES = {".git", ".hg", ".svn", ".venv", "venv", "node_modules", "__pycache__", "dist", "build", ".next", ".cache"}
_PROJECT_MARKERS = {"package.json", "pyproject.toml", "requirements.txt", "Pipfile", "Cargo.toml", "go.mod", "pom.xml", "build.gradle", "build.gradle.kts", "composer.json"}
_GITHUB_REMOTE = re.compile(r"github\.com[/:](?P<owner>[\w.-]+)/(?P<repository>[\w.-]+?)(?:\.git)?$", re.IGNORECASE)


class ProjectCatalogError(RuntimeError):
    """A configured project source could not be read."""


def _git_remotes(directory: Path) -> list[str]:
    config = directory / ".git" / "config"
    if not config.is_file():
        return []
    try:
        values = re.findall(r"^\s*url\s*=\s*(.+?)\s*$", config.read_text(encoding="utf-8", errors="replace"), flags=re.MULTILINE)
    except OSError:
        return []
    return list(dict.fromkeys(value.strip() for value in values if value.strip()))


def _github_url(remotes: list[str]) -> str | None:
    for remote in remotes:
        match = _GITHUB_REMOTE.search(remote)
        if match:
            return f"https://github.com/{match.group('owner')}/{match.group('repository')}"
    return None


def _marker(files: list[str]) -> str | None:
    markers = sorted(_PROJECT_MARKERS & set(files), key=str.casefold)
    if markers:
        return markers[0]
    if any(name.lower().endswith(".sln") for name in files):
        return "*.sln"
    return None


def discover_local_projects(roots: list[Path]) -> list[dict[str, Any]]:
    """Find Git repositories and standalone manifest-based coding projects, read-only."""
    projects: dict[str, dict[str, Any]] = {}
    for source_root in roots:
        root = source_root.expanduser().resolve()
        if not root.is_dir():
            raise ProjectCatalogError(f"Local project root does not exist: {source_root}")
        for current, directories, files in os.walk(root):
            has_git = ".git" in directories or (Path(current) / ".git").is_file()
            directories[:] = [name for name in directories if name.casefold() not in _SKIP_DIRECTORIES]
            directory = Path(current)
            marker = _marker(files)
            if not has_git and not marker:
                continue
            remotes = _git_remotes(directory) if has_git else []
            key = str(directory.resolve()).casefold()
            projects[key] = {
                "catalog_source": "local",
                "catalog_root": str(root),
                "name": directory.name,
                "path": str(directory.resolve()),
                "marker": ".git" if has_git else marker,
                "remotes": remotes,
                "github_url": _github_url(remotes),
            }
    return sorted(projects.values(), key=lambda project: (project["name"].casefold(), project["path"].casefold()))


def discover_github_repositories(username: str) -> list[dict[str, Any]]:
    """Read public repository metadata only; private repositories are never requested."""
    user = username.strip()
    if not re.fullmatch(r"[A-Za-z0-9-]+", user):
        raise ProjectCatalogError("GitHub username may contain only letters, numbers, and hyphens")
    url = f"https://api.github.com/users/{user}/repos?per_page=100&type=owner&sort=full_name"
    request = Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "chatgpt-to-obsidian"})
    try:
        with urlopen(request, timeout=20) as response:  # nosec B310 -- fixed HTTPS GitHub API endpoint
            value = json.loads(response.read().decode("utf-8"))
    except (OSError, URLError, json.JSONDecodeError) as exc:
        raise ProjectCatalogError(f"Could not read public GitHub repositories for {user}: {exc}") from exc
    if not isinstance(value, list):
        raise ProjectCatalogError(f"GitHub returned an unexpected repository response for {user}")
    projects = []
    for repository in value:
        if not isinstance(repository, dict) or not isinstance(repository.get("name"), str) or not isinstance(repository.get("html_url"), str):
            continue
        projects.append({
            "catalog_source": "github",
            "github_user": user,
            "name": repository["name"],
            "github_url": repository["html_url"],
            "description": repository.get("description") or "",
            "language": repository.get("language") or "",
            "updated_at": repository.get("updated_at") or "",
            "fork": bool(repository.get("fork")),
        })
    return sorted(projects, key=lambda project: project["name"].casefold())


def replace_catalog_source(existing: list[dict[str, Any]], refreshed: list[dict[str, Any]], source: str, identity: str) -> list[dict[str, Any]]:
    """Replace one complete source snapshot while retaining every unrelated source."""
    field = "catalog_root" if source == "local" else "github_user"
    retained = [item for item in existing if not (item.get("catalog_source") == source and item.get(field) == identity)]
    return retained + refreshed
