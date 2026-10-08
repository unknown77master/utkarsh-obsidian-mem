---
type: project-home
project_id: kaushalvaani
status: active
updated: 2026-10-08
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
| **Status** | Local v2 working tree; uncommitted, unmerged, and not deployed. |
| **Current focus** | Turn source-pinned NQR/NCO candidates into a reviewed, deployable graph release. |
| **Next milestone** | Record NCO permission evidence and approve mappings/rules, then assemble and verify a deployable release. |
| **Last reviewed** | 2026-10-08 |

## Start here

- [[Current State|Current state and blockers]]
- [[PRD|Product requirements and acceptance criteria]]
- [[Timeline|Timeline and decision log]]
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
- A newer NCO Volume I concordance candidate exists (3,445 occupation references); its combined release remains non-deployable.
- DGE's NCO site policy requires permission for reproduction. The owner reported permission, but the grant/reference is not recorded in project evidence.
- Canonical mappings and eligibility rules need a domain reviewer; live Aura, Modal, Vercel, Clerk, and Sarvam work needs owner account and secret configuration.
- Follow repository `09-docs/context/tasks.md` for the maintained checklist; the root `tasks.md` referenced in older notes is absent in this checkout.
