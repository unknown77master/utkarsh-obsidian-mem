# Agent Memory Retrieval Guide

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

Memory commit subjects use actual current Asia/Kolkata (IST) time: `DD-mon-YYYY:h-mm:AM (updated specific context)` or `...:PM (...)`. Use English lowercase months, two-digit day/minute, and a 12-hour hour without a leading zero. Example: `06-oct-2026:2-58:AM (updated coding projects and preferences)`. Follow user authorization and runtime restrictions for commits and pushes; report local-only updates.
