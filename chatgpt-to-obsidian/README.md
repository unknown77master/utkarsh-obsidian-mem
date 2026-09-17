# ChatGPT to Obsidian (local only)

This dependency-free Python tool converts an extracted ChatGPT data export into a traceable, evolving Obsidian knowledge base. It reads the source export without changing, moving, renaming, or deleting it. Normal migrations are local-only; public GitHub metadata is retrieved only when `--github-user` is explicitly configured.

## Usage

```powershell
python migrate.py --source "D:\path\to\extracted-export"
```

Without `--output`, the permanent vault location is `chatgpt-to-obsidian\utkarsh-vault`. Pass `--output` only when deliberately creating a different vault.

To keep the vault’s project catalogue current with your coding workspace and public GitHub repositories:

```powershell
python migrate.py --source "D:\path\to\extracted-export" --projects-root "D:\ALL Programming" --github-user "utkarsh-wadalkar"
```

The project roots and GitHub users are saved in the migration state after that first run. Later normal migrations rescan them automatically. Private repositories are never requested from GitHub; a private project is catalogued from its local Git repository when its parent root is configured.

To keep refreshing until stopped, add `--watch`. Local roots and the ChatGPT export are checked every five minutes by default; public GitHub is checked at most once per hour in watch mode. Change those intervals with `--watch-interval` and `--github-refresh-interval`:

```powershell
python migrate.py --source "D:\path\to\extracted-export" --watch --watch-interval 300 --github-refresh-interval 3600
```

Inspect a large export without changing the destination:

```powershell
python migrate.py --source "D:\path\to\extracted-export" --dry-run
```

Searchable transcripts and the full raw export mirror are created by every normal migration. `--archive-conversations` remains accepted for compatibility:

```powershell
python migrate.py --source "D:\path\to\extracted-export" --archive-conversations
```

## What it processes

The tool recursively discovers every plausible conversation JSON file, including numbered `conversations-000.json` files. It streams top-level JSON arrays one record at a time, follows the current conversation branch, tolerates empty or malformed records, and logs failures in `migration_report.md` rather than failing the whole run.

Only explicit user statements matching conservative durable-context rules become candidates. The local extractor does not use an API or infer facts from assistant responses. It categorizes, source-tracks, lexical-deduplicates, and flags likely platform contradictions for `review_queue.md`. The extraction module is deliberately isolated so an optional local-LLM provider can replace or supplement it later without changing discovery, parsing, state, or vault writing.

## Repeat runs and safety

The destination stores `.chatgpt-migration-state.json`, containing conversation fingerprints and extracted-memory source references. A later run skips unchanged conversations, processes only new or changed ones, and refreshes changed-conversation candidates. Do not edit that state file by hand. The output path is rejected when it is the source or inside the source, protecting the export from accidental writes.

The vault is self-contained. It contains category notes, searchable conversation transcripts under `Archive/<year>/<date>/`, and a checksum-verified copy of every original export file under `Raw/Export/`. Archive folders use descriptive index notes—`Chat History Index.md`, `<year> Chat Index.md`, and `<date> Chat Index.md`—that link directly to conversation titles. Each transcript preserves structured local attachments, external references, and unresolved export IDs in its `## Resources` section.

`AGENTS.md` is the canonical retrieval guide for AI agents, while `00 - Agent Memory.md` is the compact human- and machine-readable entry point. The raw mirror includes binary attachments, JSON, HTML, and metadata, so the vault does not require the original export to remain available. On repeat runs, unchanged files are verified and skipped; changed raw files are replaced and raw files no longer in the latest export are removed from the mirror.

## Project navigation

`Projects/Projects Index.md` is the root map for projects. It links to one `<Project Name> Project Index.md` note per known local repository, public GitHub repository, or explicitly named ChatGPT project. Each project index contains its local repository paths, public GitHub links when available, durable project context, direct links to related archived chats, and links to those chats' `## Resources` sections. Project context that does not state a reliable name is retained in `Unclassified Project Discussions Project Index.md` instead of being assigned an invented project.

## Current export inspection

The export supplied with this project has four numbered conversation files containing 352 conversations. Its conversations use a `mapping` graph; messages have `author`, `content.parts`, timestamps, and metadata. No separate memory JSON was present.
