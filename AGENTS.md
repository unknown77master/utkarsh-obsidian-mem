# Obsidian memory repository

Read `chatgpt-to-obsidian/utkarsh-vault/AGENTS.md` before using personal memory. Resolve vault paths relative to this repository in cloud checkouts.

## Commit messages — all local and cloud agents

Every memory commit subject must use actual current **Asia/Kolkata (IST)** time:

`DD-mon-YYYY:h-mm:AM (updated specific context)` or `DD-mon-YYYY:h-mm:PM (updated specific context)`.

Use English lowercase months, two-digit day/minute, and a 12-hour hour without a leading zero. Example: `git commit -m "06-oct-2026:2-58:AM (updated coding projects and preferences)"`. Never reuse the example timestamp or vague placeholder descriptions.

Before editing, pull the configured upstream with `git pull --ff-only` when the working tree is clean. Preserve existing edits. After validated updates, follow the user's commit/push authorization and current runtime restrictions; clearly report local-only updates. Cloud edits must be pushed before a local checkout can retrieve them.

Stage only intended files. Never force-push, discard unrelated edits, or silently choose a conflict winner. Pause any local sync service and wait for its active cycle to finish before manual Git operations.

Keep changes focused, search before reading large files, and validate proportionally. Do not edit `Raw/Export/`, `.export-mirror-manifest.json`, or `.chatgpt-migration-state.json`.
