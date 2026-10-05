---
type: project-home
project_id: kaushalvaani
status: active
updated: 2026-10-02
review_after: 2026-11-02
tags:
  - project-memory
---

# KaushalVaani

> [!summary] What this project is
> A non-commercial B.E. judge demo for evidence-backed, multilingual skill-pathway guidance for Indian learners and job seekers.

## At a glance

| | |
|---|---|
| **Status** | Local v2 foundation validated on `codex/kaushalvaani-foundation`; unmerged and not deployed. |
| **Current focus** | Build a provenance-pinned, reviewed NQR/NSQF and NCO graph release. |
| **Next milestone** | Obtain lawful NCO source access and mapping review; then assemble and verify a deployable release. |
| **Last reviewed** | 2026-10-02 |

## Start here

- [[Current State|Current state and blockers]]
- [[Handoff|Latest handoff]]
- [[Project|Project details and code map]]
- [[Inbox/Promotion Inbox|Knowledge awaiting review]]
- [[../KaushalVaani Project Index|Earlier project index]]

## Implementation map

The FastAPI v2 API performs deterministic profile, eligibility, skill-gap, ranking, and evidence assembly over Neo4j. A React/Vite frontend presents text first; Modal L4 Rumik speech is optional. Official source data is normalized into immutable, verifiable graph releases.

## Important commands

| Action | Command from repository root |
|---|---|
| Backend tests | `cd 01-backend-api; .\.venv\Scripts\python.exe -m pytest -q` |
| Source package | `01-backend-api/.venv/Scripts/python.exe 07-scripts/verify_source_package.py 05-data/seed/candidates/source-package.manifest.json` |
| Graph candidate | `01-backend-api/.venv/Scripts/python.exe 07-scripts/graph_release.py verify --seed 05-data/seed/candidates/nqr-four-sectors-2026-10-02.release.json --manifest 05-data/seed/candidates/nqr-four-sectors-2026-10-02.manifest.json` |

## Risks and next actions

- The four-sector NQR candidate is intentionally non-deployable and contains summary facts only.
- DGE's NCO site policy requires permission for reproduction; a licensed export or written permission is needed before NCO ingestion.
- Canonical mappings and eligibility rules need a domain reviewer; live Aura, Modal, Vercel, Clerk, and Sarvam work needs owner account and secret configuration.
- Follow the repository's `tasks.md` for the maintained checklist.
