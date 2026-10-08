---
type: project-timeline
project_id: kaushalvaani
updated: 2026-10-08
---

# EchoQuery → KaushalVaani — timeline and decision log

Dates below describe evidenced conversations, commits, documents, or local artifacts. A document date is not proof of a deploy or test run. This timeline deliberately separates the former EchoQuery scope from the current KaushalVaani v2 scope.

| Date (IST where Git records it) | Milestone and evidence | State |
|---|---|---|
| 2026-08-16 | EchoQuery began as a voice-to-STT-to-RAG project for a hackathon brief. Utkarsh owned the AI/RAG and performance work; the brief emphasized chunking, grounding, latency, and P50/P70/P100 reporting. Repository initial commit `460489a`. See the archived [[Archive/2026/2026-08-16/EchoQuery--6a81ac51-789|EchoQuery conversation]]. | Historical direction. |
| 2026-08-17 | Repository folder structure and v1 application contracts were committed (`3b3d43a`, `749ac95`). | Historical v1 foundation. |
| 2026-08-18 to 2026-08-24 | ADR 0001 defined the v1 latency/grounding contracts; backend voice/STT/FastAPI work was committed on Aug 21 (`b37ee98`). The target was full online RAG below 200 ms, not a measured achieved result. | Later superseded by v2. |
| 2026-09-05 | A repository audit found the tracked EchoQuery app incomplete and not deployable; substantive RAG work was in an ignored experimental directory. The 93-test staged run had 90 passes, 1 missing-contract error, and 2 skips. See `09-docs/context/CURRENT-TASKS.md`. | Historical audit, not current acceptance. |
| 2026-09-16 to 2026-09-17 | An experimental worktree was briefly merged, then accidentally tracked nested content was removed (`02b1adb`, `03b166a`). Repository housekeeping continued through `9c9687a`. | Git history, not proof that the current v2 code was committed. |
| By 2026-09-17 | The GitHub repository was described as KaushalVaani: voice-first livelihood intelligence using knowledge graphs, multilingual profiling, skill-gap reasoning, NSQF-aligned training, and local pathways. The local folder still retained the EchoQuery name. See [[../KaushalVaani Project Index]]. | Product direction changed. Exact decision date is not evidenced here. |
| 2026-10-02 | The local v2 foundation replaced active vector-RAG/query/WebSocket routes with FastAPI v2, Neo4j deterministic reasoning, provenance/release tooling, Clerk boundary, React/Vite UI, Sarvam adapters, and optional Rumik speech. Recorded checks: 51 backend and 3 frontend tests passed, TypeScript and Vite build passed, and fixture/source checks passed. See repository `09-docs/context/tasks.md`. | Local working tree only; uncommitted, unmerged, undeployed. |
| 2026-10-02 | Four NCVET PDFs were source-pinned for healthcare, retail, automotive, and IT-ITeS. A 13-node/24-relationship summary release was verified and marked non-deployable. A mapping/rule review packet was created. Owner reported provider accounts, NCO access permission, and willingness to review mappings; specific evidence and approvals were still outstanding. | Source candidates, not a judge graph. |
| 2026-10-03 | NCO-2015 Volume I concordance was extracted as 3,445 distinct occupation-code references. A combined NCO/NQR candidate manifest was generated with 6,904 seed nodes and 13,806 relationships and remained `deployable: false`. Volume II-A/II-B are reference-only in the source manifest. See `05-data/seed/candidates/` manifests and review packet. | Local candidate; permission grant reference and semantic mapping approvals remain unrecorded. |
| 2026-10-06 | The root README describing KaushalVaani and local checks was committed (`6e9104d`). | Documentation commit only; local v2 implementation remains uncommitted. |
| 2026-10-08 | Project memory was reconciled against repository source, Git history, manifests, and prior Obsidian notes. A PRD and timeline were added; current state was corrected to mention the newer NCO candidate and the actual checklist path. | Memory update; no fresh app tests, live deployment, or judge acceptance is claimed. |

## Open decision log

- **Official-source rights:** Record the NCO export path and permission document/grant reference before treating NCO-derived content as publishable; recheck NQR document-level rights before a full corpus is released.
- **Mapping semantics:** Utkarsh is the stated reviewer, but each NQR-to-NCO/canonical relationship and eligibility route needs an explicit dated decision. Healthcare's `3259` is a group pointer; other candidate alignments also need semantic review.
- **Graph release:** Finish the national compact NQR/NSQF layer, deep four-sector NOS/skill/rule data, approved mappings, and verified local handoffs. Then capacity-preflight and rebuild Aura from a deployable manifest.
- **Evaluation and deployment:** Obtain counsellor labels, benchmark voice, configure provider secrets/budget, verify the live text-first flow, and complete two rehearsals. No completion evidence was found for these gates.
- **Compatibility:** The v2 working tree removes old `/api/v1/query/*` and `/ws/query` behavior. Reintroduction requires an explicit compatibility requirement and contract.

## Reading order

[[PRD]] → [[Current State]] → [[Handoff]] → repository `09-docs/context/tasks.md`. The repository is authoritative for code and acceptance evidence; [[Archive/2026/2026-08-16/EchoQuery--6a81ac51-789|the archived EchoQuery chat]] is historical context for the original direction.
