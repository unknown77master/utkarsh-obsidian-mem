---
type: project
project_id: kaushalvaani
profile: software
status: active
updated: 2026-10-02
review_after: 2026-11-02
coverage_areas:
  - architecture
  - provenance
  - evaluation
  - deployment
  - operations
---

# KaushalVaani

Human-facing entry point: [[Project Home]]. The primary code repository is `KaushalVaani` (local checkout folder `EchoQuery-RAG-based-STT`); code paths below are repository-relative.

## Purpose

Provide evidence-backed qualification and occupation pathways across English, Hindi, Marathi, and Hinglish for an academic judge demo.

## Current state

See [[Current State]]. The local v2 implementation is branch-only and has not been committed, merged, or deployed.

## Code map

- Architecture and identity: `09-docs/architecture/kaushalvaani-domain-model.md`, `09-docs/decisions/0002-canonical-identity-and-official-references.md`.
- API: `01-backend-api/app/api/routes/v2.py`; contracts: `00-contracts/v2/`.
- Graph releases: `01-backend-api/app/graph/`, `07-scripts/graph_release.py`, `05-data/seed/`.
- Frontend: `02-frontend/`; deployment: `01-backend-api/modal_app.py` and `09-docs/deployment/`.
- Maintained task ledger: `tasks.md`.

## Knowledge maintenance

- [[Project Home]]
- [[Handoff]]
- [[Inbox/Promotion Inbox]]
- [[Coverage]]
