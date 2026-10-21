---
type: "maintained-project-context"
scope: "execution-backlog"
updated: "2026-10-21"
---

# Active Build Backlog

This is a maintained execution view of projects discussed in ChatGPT that were planned but not yet established as complete. Generated project indexes and chat-derived context remain authoritative for detailed history; statuses below preserve uncertainty where implementation evidence is missing.

## Daily operating rule

- Refresh this backlog in the daily Notion execution plan.
- Select at most one project for focused work per day; keep the rest deferred unless a hard deadline changes priority.
- OSS contribution work remains paused until the OSS agent is explicitly created.

## Pending projects

### Agent Relay — active design, not implemented

Goal: an OmniRoute-like OpenAI-compatible gateway for Codex Desktop and other agent work. It should route every request through a policy layer, use LAYA for model/reasoning-effort selection, and use CodeNotch for quota awareness.

Next: complete Phase 0—provider/integration matrix, baseline tests, ADRs, and a minimal deterministic routing contract before mutation. MVP sequencing is deterministic routing -> OpenCode worker through Herder -> validated patch; LAYA, OmniRoute compatibility, CodeNotch, and OSS integration follow.

### Codex fallback model / OmniRoute — planned dependency

OmniRoute reachability exists, but real provider acceptance and OAuth refresh remain untested. Next: document the OpenAI-compatible request/response, tool-call, streaming, health, and fallback contract needed by Agent Relay.

### Herder for coding agents — installed, remote execution not verified

Herder is installed on Windows and Omarchy. Next: run one disposable repository through Tailscale SSH, verify session lifecycle and artifact handoff, then decide between remote control and independent workspaces.

### OSS agent and OSS Control Center — paused

The OSS contributor agent is still at design review; preserve the existing v2 worktree. Typecheck and targeted lint pass, but root lint has an inaccessible Python temporary-test directory and needs a current report, snapshot delta, and scoped re-review. The P-stack direction is accepted as the engineering playbook, but implementation and Omarchy deployment are not verified.

Do not schedule OSS contribution work until the OSS agent exists.

### HarnessArena / Harnessly — planned, implementation status not established

Planned as a local tournament for open-weight coding agents with Docker isolation, reproducible traces, scoring, Gemma interview, and LAYA recommendations. Next evidence task: inspect the current repository/worktree and identify the first unfinished deliverable; do not infer completion from the PRD.

### WhatsApp Opportunity Monitor — not implemented or deployed

Planned as a read-only secondary-number Baileys + SQLite collector on Omarchy, with selected opportunity groups, n8n orchestration, relevance filtering, deduplication, expiry cleanup, and Notion/Calendar summaries. Intake-group choice remains unresolved. Next: deploy and pair the collector only after the secondary account and intake design are decided.

### OCR-GST / GST Operations Copilot — conceptual/partially planned

Target: receipts/invoices -> Sarvam Document AI extraction -> canonical record -> PostgreSQL -> human review -> Google Sheets. Next: pilot Decisions API routing for human review, damaged documents, and extraction-confidence thresholds using labelled examples; keep workers, credentials, connectors, policy gateway, approval cards, audit trail, and inspectable state separate.

### KaushalVaani — final-year project, data/ingestion work remains

Neo4j and the canonical taxonomy direction are selected. Next implementation milestone remains source ingestion, provenance-preserving NCO/NQR mapping, and a first useful graph slice.

### ProvenanceX — concept/repo, further build pending

Media provenance passport concept for captured/synthetic/edited/unknown media. Next: define the smallest end-to-end registration and verification flow before adding incentives or payments.

### AI Demo Video Creator — partial prototype

Record/render path works, but voice/caption generation hit provider rate limits. Next: stabilize a no-LLM or low-cost render path before adding provider-dependent automation.

### Omarchy remote access / TPM2 — TPM2 path blocked by hardware

The current hardware does not support the intended TPM2 unlock path. Do not treat TPM2 as an active implementation task or purchase hardware without a verified compatible TPM header/module.

Next practical path: use Tailscale as the network boundary, SSH for administration, Sunshine for GUI access, and BIOS settings such as Onboard LAN Wakeup and Restore AC Power Loss = Power On where supported. Treat secure unattended disk unlock as unresolved; require local/manual unlock after reboot unless hardware support is independently verified.

## Source notes

- Remote vault entry point: `00 - Agent Memory.md`; retrieval and safety rules: `AGENTS.md`.
- Relevant evidence includes the AgentRelay PRD context, WhatsApp handoff, OCR GST project index, and recent project-status discussions.
- Where the vault did not establish implementation status, this note says so explicitly rather than converting an inference into a fact.
