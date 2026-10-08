# Agent Memory Retrieval Guide

## Canonical vault

This personal-memory vault is located at `D:\ALL Programming\obsidian_mem\chatgpt-to-obsidian\utkarsh-vault`. Start with [[00 - Agent Memory]] whenever a task needs Utkarsh's personal context, projects, preferences, or ChatGPT history. Then all the files in utkarsh-vault folder are authoritative source of context

## Authority order

1. `Raw/Export/` is the faithful local export mirror and is authoritative for original data.
2. Conversation transcripts in `Archive/` are searchable renderings of that export.
3. Category notes are curated, derived memory; verify important facts against a transcript or raw export when accuracy matters.

## Retrieval order

1. Read [[00 - Agent Memory]].
2. Read the relevant category or index note before expanding scope.
3. Use [[Archive/Chat History Index]] to locate a targeted chat by year, date, and title.
4. Inspect a transcript's `## Resources` section for linked attachments and cited URLs.

## Safety

- Do not edit `Raw/Export/`, `.export-mirror-manifest.json`, or `.chatgpt-migration-state.json`.
- Do not convert an assistant inference into a user fact without source evidence.
- Preserve unresolved references and consult [[review_queue]] when context is uncertain.

## Commit messages and cloud checkouts

Follow the repository root `AGENTS.md` in every checkout. Resolve this vault relative to the repository when the Windows path is unavailable.

Memory commit subjects use actual current Asia/Kolkata (IST) time: `DD-mon-YYYY:h-mm:AM (updated specific context)` or `...:PM (...)`. Use English lowercase months, two-digit day/minute, and a 12-hour hour without a leading zero. Example: `06-oct-2026:2-58:AM (updated coding projects and preferences)`. Follow user authorization and runtime restrictions for commits and pushes; report local-only updates.
