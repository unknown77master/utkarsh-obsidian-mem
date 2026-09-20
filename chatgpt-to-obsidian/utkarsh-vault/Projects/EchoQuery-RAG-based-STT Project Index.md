---
type: "project-index"
scope: "project"
project: "EchoQuery-RAG-based-STT"
generated_by: "chatgpt-to-obsidian"
updated: "2026-09-18"
durable_context_count: 2
chat_count: 1
local_repository_count: 1
github_repository_count: 0
---
# EchoQuery-RAG-based-STT Project Index

This note groups only project names stated explicitly in the export. It links to the canonical transcripts and their preserved resources; it does not copy or reinterpret them.

## Local repositories

- `D:\ALL Programming\0-WebDev\Hacker_House\EchoQuery-RAG-based-STT` — detected by `.git`
  - Remote: [https://github.com/utkarsh-wadalkar/KaushalVaani.git](https://github.com/utkarsh-wadalkar/KaushalVaani.git)

## Durable context

- The original EchoQuery phase was scoped as a three-person, multilingual voice-to-grounded-answer system: speech-to-text, vector retrieval and reranking, LLM answer generation, grounding checks, and guardrails.
- Utkarsh had previously worked with Voxtral Mini for multilingual speech-to-text and planned to use Codex while developing this project.

## Related chats

- [[Archive/2026/2026-08-16/EchoQuery--6a81ac51-789|EchoQuery]]

## Resources

- No linked transcript resources are available yet.

## Current B.E. project direction — 2026-09-17

EchoQuery is now the user's **B.E. Final Year Project**, not a hackathon-selection build. Useful engineering work from the earlier `EchoQuery-RAG-based-STT` phase should be reused selectively, but the current B.E. scope is authoritative.

EchoQuery / KaushalVaani is a **voice-first, multilingual livelihood intelligence system**. It should understand a beneficiary's skills, education, interests, language, and circumstances, reason over structured livelihood and qualification relationships, identify skill gaps, and provide explainable NSQF-aligned training and livelihood pathways.

Multilingual support is a **core requirement**, not an optional later feature. Multilingual input, understanding, reasoning interfaces, explanations, and voice output remain central to the project.

### Architecture direction

The new center of the system is a **Neo4j knowledge graph**, rather than classic vector RAG alone. The graph should represent entities and relationships such as beneficiaries, skills, occupations, sectors, qualifications, NSQF levels, NOS/modules, eligibility, progression paths, regions, and livelihood opportunities.

Preferred flow:

```text
Voice
  -> STT / language handling
  -> structured beneficiary profile
  -> Neo4j knowledge graph
  -> skill-gap reasoning
  -> candidate pathway filtering and ranking
  -> evidence-grounded explanation
  -> multilingual UI / TTS response
```

LLMs should not be the authoritative source for NSQF or qualification facts. Deterministic and graph-based components should perform the core skill-gap and pathway reasoning wherever possible; LLMs should mainly help with language understanding, clarification, and natural-language explanation of graph-derived evidence.

### Relationship to earlier RAG work

The earlier ingestion, chunking, embeddings, retrieval, reranking, generation, guardrail, evaluation, and observability work remains useful and should not be discarded blindly. Vector retrieval is no longer the architectural center, but it may remain as a supporting retrieval layer for unstructured text where useful, giving a hybrid graph + retrieval + LLM system.

### Low-latency direction

The earlier hackathon implementation emphasized a strict approximately **200 ms RAG latency target**. For the B.E. project, the hard 200 ms requirement is no longer the primary success criterion, but the **low-latency engineering philosophy remains important**.

Latency should be treated as a first-class measurable system property. Instrument major stages separately, including STT, profile extraction, graph queries, reasoning, ranking, LLM time-to-first-token, generation, and end-to-end response time. Evaluate P50, P95, and P99 rather than relying on one headline number.

Keep the deterministic reasoning core as short as possible:

```text
structured profile
  -> graph traversal / Cypher
  -> skill-gap calculation
  -> eligibility filtering
  -> candidate ranking
  -> evidence
```

The slower generative layer should come after that core wherever possible. Avoid placing an LLM in the critical path when deterministic graph/database computation can solve the same task faster and more reliably.

### Stable implementation principles

- Preserve multilingual capability as a first-class requirement.
- Keep Neo4j as the authoritative graph-grounded reasoning layer.
- Keep skill-gap analysis and pathway ranking explainable and evidence-backed.
- Reuse earlier RAG work selectively instead of starting over or deleting it prematurely.
- Optimize and measure latency continuously without forcing the entire project around a hard 200 ms claim.
- Prefer clean contracts and deterministic stages over tightly coupled LLM-heavy logic.
- Treat the B.E. project direction as the current source of truth when it conflicts with the earlier hackathon scope.
