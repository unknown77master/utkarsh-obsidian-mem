---
type: product-requirements
project_id: kaushalvaani
updated: 2026-10-08
status: working-specification
source_of_truth: repository
---

# KaushalVaani — product requirements

This is the project memory summary as of 2026-10-08. It describes the intended academic B.E. judge demo and distinguishes implemented local code from verified live behavior. For exact contracts and changes, use the repository documents cited below. The local checkout is named `EchoQuery-RAG-based-STT`, while its current product name and GitHub remote are KaushalVaani.

## Problem and intended outcome

Indian learners and job seekers need understandable, evidence-backed routes from their current education, skills, experience, location, and aspirations to occupations, qualifications, training, and possible local opportunities. KaushalVaani should explain why a pathway is suitable, what facts are missing, what skills need work, and which official records support the advice. It is a non-commercial academic demonstrator, not a production counselling service.

## Users, scope, and success

- Primary user: an individual learner or job seeker. The judge/operator is the secondary user for the demo.
- Languages: English (`en-IN`), Hindi (`hi-IN`), Marathi (`mr-IN`), and Hinglish (`hi-Latn-IN`). The knowledge taxonomy is India-wide; verified Maharashtra handoffs are prioritized for Pune, Thane, and Nashik.
- Core completion: the learner confirms a profile, receives a ranked text pathway with eligibility, skill gaps, reasons, and official source links, and can understand an actionable handoff or the precise missing facts. Optional speech follows only after the text result exists.
- Evaluation headlines: counsellor-labelled top-1 recommendation correctness and explanation faithfulness. Report NQR coverage, task completion, and stage/end-to-end latency separately. No measured correctness or live latency result is recorded yet.

## Required user journey

1. The user signs in through Clerk and enters a typed narrative or uploads audio for best-effort Sarvam Saaras v4 transcription. A transcription failure leaves typed input usable.
2. Sarvam-105B may propose structured profile facts, with evidence/confidence and sensitivity markers. The user edits and explicitly confirms fields. Failed extraction falls back to manual confirmation; only confirmed values become a profile snapshot.
3. The backend retrieves facts from a pinned Neo4j knowledge release, evaluates eligibility with `ELIGIBLE` / `INELIGIBLE` / `UNKNOWN`, calculates skill gaps, and ranks pathways deterministically for `best_fit`, `quickest_upskill`, `aspirational`, and `most_accessible`. Missing required facts produce `UNKNOWN`.
4. The text result shows the official NQR/NCO references, source evidence, eligibility, gaps, and explanation. An LLM may explain computed facts but may not decide eligibility or activate mappings. A deterministic template remains available if explanation fails.
5. The user may request a short Rumik voice summary afterward. Voice failure must leave the complete text recommendation usable. The user can retrieve history and delete all user-linked graph data.

## Knowledge and trust requirements

- NQR/NSQF supplies the qualification backbone; NCO-2015 supplies official occupation references. Internal canonical occupations and skills are distinct from official identities. A qualification may prepare for an occupation without being identical to it.
- Every official fact must retain publisher, source URL/version/date, source snapshot, and hash. A `KnowledgeRelease` pins the facts, schema, mapping decisions, and seed checksum. Historical recommendation snapshots keep their original evidence.
- Only reviewed `APPROVED` or valid `AUTO_CARRIED` mappings may affect current recommendations. Source-stated alignment codes alone are not approvals. Stale records and unverified providers must not appear as current actionable handoffs.
- Graph import must pass schema/identity validation, capacity preflight, idempotent import, and exact post-import verification. A source-only or fixture release cannot become the judge graph by changing a flag.
- The graph must not invent a result when Aura is unavailable. Profile extraction proposals are not persisted before confirmation. Contact/login PII is not copied to Neo4j, and deletion removes user-linked records.

## Architecture and operating constraints

`React/Vite on Vercel -> FastAPI on Modal CPU -> Neo4j AuraDB Free`; Sarvam handles STT and optional profile/explanation language work; an internal Modal L4 worker serves pinned Rumik/Mimi speech. The recommendation endpoint is text-first and never waits for TTS. The default GPU state is scale-to-zero; the runbook warms one L4 briefly for the demo. The plan targets near-zero normal operating cost with a ₹300–₹500 contingency and a Modal budget cap, subject to real usage checks.

The v2 API includes transcription, profile extraction/confirmation, profile retrieval, user-data deletion, recommendation creation/history, separate speech, and health/readiness. The old EchoQuery v1 query and WebSocket routes are intentionally removed from the local v2 implementation; compatibility would require a separate decision.

## Acceptance evidence required before calling the demo ready

- A legally usable, reviewed, deployable NQR/NCO release with national compact coverage, deeper healthcare/retail/automotive/IT-ITeS detail, approved mappings/rules, and only verified local offerings where available.
- Capacity estimate and clean Aura rebuild match the release manifest, hashes, counts, schema, mappings, and representative recommendation outputs.
- Counsellor-labelled evaluation set with disjoint development/evaluation cases; measured top-1 correctness and explanation faithfulness; documented coverage, task completion, and latency.
- At least 20 warm Rumik samples balanced across the four languages, cold/warm latency, time to first audio, memory, intelligibility, and cost; A10 only if L4 misses its criteria while memory-safe.
- Live Clerk, Sarvam, Aura, Modal, and Vercel flow verified, including typed fallback, text-only fallback, history, deletion, and failure behavior; two complete judge rehearsals with redacted evidence and measured spend.

## Current implementation boundary (2026-10-08)

The local `codex/kaushalvaani-foundation` working tree contains v2 contracts, FastAPI graph reasoning and profile flows, React frontend, Modal definitions, graph tooling, and tests. It is uncommitted and not known to be deployed. On 2026-10-02, repository notes record 51 passing backend tests, 3 passing frontend tests, TypeScript/Vite build, and fixture/source checks; these are historical validation records, not a fresh October 8 test run.

Four pinned NCVET qualification PDFs support a 13-node/24-relationship non-deployable summary candidate. A later NCO Volume I concordance candidate contains 3,445 occupation references and, together with those NQR records, an estimated 6,904 seed nodes and 13,806 relationships (plus 5,000/10,000 runtime reserve). Its manifest was generated 2026-10-03 and says `deployable: false`. The permission document/grant reference has not been recorded, and no occupation mapping or eligibility interpretation has been approved. The national NQR layer, deep skill/NOS/rule detail, verified local offerings, clean Aura rebuild, live deployment, labelled results, voice benchmark, and rehearsals remain open.

## Decisions and references

- Current domain and rule model: repository `09-docs/architecture/kaushalvaani-domain-model.md`.
- Identity/provenance decision: `09-docs/decisions/0002-canonical-identity-and-official-references.md`.
- API and schemas: `09-docs/api/api.md`, `00-contracts/v2/`.
- Source candidates and review: `05-data/seed/candidates/README.md`, `mapping-review-packet.md`, `nco-2015-source-package.manifest.json`, `nco-national-nqr-four-sectors-2026-10-02.manifest.json`.
- Deployment, evaluation, cost, rehearsal: `09-docs/deployment/modal-vercel-aura.md`, `09-docs/evaluation/kaushalvaani-evaluation.md`, `09-docs/operations/cost-model.md`, `09-docs/operations/judge-demo-runbook.md`.
- Working checklist: repository `09-docs/context/tasks.md` (some existing notes refer to a root `tasks.md`, which is absent in this checkout).
