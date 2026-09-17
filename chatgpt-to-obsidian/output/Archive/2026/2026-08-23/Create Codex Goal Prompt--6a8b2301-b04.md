---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a8b2301-b040-83e9-a74c-dbd4ec0d153a"
created: 1787503385.412508
updated: 1787504417.174641
resource_section: true
---

# Create Codex Goal Prompt

## User

ok now complete or update D:\ALL Programming\Hacker_House\EchoQuery-RAG-based-STT\.claude\worktrees\utkarsh-rag-tasklist\notes\Utkarsh-TASK.md
D:\ALL Programming\Hacker_House\EchoQuery-RAG-based-STT\.claude\worktrees\utkarsh-rag-tasklist\notes\docs\superpowers\plans\2026-08-21-ai-rag-engine.md
D:\ALL Programming\Hacker_House\EchoQuery-RAG-based-STT\.claude\worktrees\utkarsh-rag-tasklist\notes\AI-RAG-TASKS.md tasks and phase according to these files and our current new decisions about deployment, Goal is entirely complete echoquery application.

give me persuing goal prompt for codex

## Assistant

Worked for 53s

## Assistant

Yes. I checked the current RAG plan and the deployment decision. The existing plan is now too narrow because it treats deployment and the rest of EchoQuery as a handoff, while your actual goal is **a completely working EchoQuery application**.

The current RAG baseline already has ingestion, chunking, embedding/index, and retrieval foundations implemented, with the remaining gates around real multilingual benchmarking, production provider selection, Sarvam-105B, orchestration, evaluation, integration, and deployment. fileciteturn0file0L11-L25 fileciteturn0file1L69-L87

The deployment decision is:

**DigitalOcean Droplet → Docker Compose → FastAPI + frontend + self-hosted Qdrant → Cloudflare**, with no Kubernetes, ECS, RDS, managed vector DB, or unnecessary AWS services. The planned Droplet size is 2–4 GB. fileciteturn3file0 fileciteturn7file0

One limitation: I cannot directly access your Windows `D:\...` worktree from this chat runtime, so I cannot honestly claim that I modified those three files on disk. Instead, the prompt below instructs Codex to **first update those exact files**, reconcile their contents with the current repository, and then pursue the complete application goal.

### Master Codex prompt

:::writing{variant="document" id="58321" title="EchoQuery — Complete Application Pursuit Prompt for Codex"}
You are the implementation engineer for the EchoQuery-RAG-based-STT repository.

Your objective is NOT merely to finish the RAG engine.

Your objective is:

> **Make the entire EchoQuery application complete, integrated, testable, deployable, and demonstrable end-to-end without changing the established architecture unless a real blocker requires it.**

You are working under an existing architecture. Do not redesign the project just because another architecture looks cleaner.

---

# 1. FIRST: READ THE REPOSITORY AND UPDATE THE PROJECT DOCUMENTATION

Before writing implementation code, inspect the current repository state, Git history/status, existing contracts, source tree, tests, and the following three files:

```text
.claude/worktrees/utkarsh-rag-tasklist/notes/Utkarsh-TASK.md
.claude/worktrees/utkarsh-rag-tasklist/notes/docs/superpowers/plans/2026-08-21-ai-rag-engine.md
.claude/worktrees/utkarsh-rag-tasklist/notes/AI-RAG-TASKS.md
```

Update all three files so they represent the CURRENT project state and the COMPLETE EchoQuery objective.

Do not blindly append another roadmap.

Reconcile the existing tasks with the repository's actual implementation.

Mark already verified work as complete.

Keep genuinely unfinished work open.

Remove obsolete restrictions that prevent completion of the whole application.

The documents must clearly distinguish:

- completed
- in progress
- blocked by credentials/external infrastructure
- pending human decision
- pending verification

The final task hierarchy must be phase-oriented and must cover the entire application.

---

# 2. AUTHORITATIVE ARCHITECTURE

The existing architecture remains authoritative.

The logical application flow is:

```text
User
 │
 │ Audio
 ▼
Frontend
 │
 │ WebSocket
 ▼
FastAPI
 │
 ▼
STT Service
 │
 │ Transcript
 ▼
RAG Orchestrator
 │
 ├── Query validation
 ├── Query preprocessing
 ├── Query embedding
 ├── Vector retrieval
 ├── Reranking
 ├── Context construction
 ├── LLM generation
 ├── Grounding verification
 └── Guardrails
 │
 ▼
Answer
 │
 │ WebSocket
 ▼
Frontend
```

The contracts remain the boundary between components:

```text
STT
 ↓
Transcript Schema
 ↓
FastAPI Contract
 ↓
RAG Pipeline API
 ↓
Answer Schema
 ↓
WebSocket Event Schema
```

Do not break these contracts casually.

If a contract genuinely needs to change to complete the application:

1. identify why;
2. inspect all consumers;
3. update the contract;
4. update affected implementations;
5. update tests;
6. update the relevant task/ADR documentation.

Never silently change an interface.

---

# 3. CURRENT RAG ARCHITECTURE

The RAG engine remains a focused Python source root under:

```text
03-ai-rag-engine/
```

The RAG architecture is:

```text
Canonical Documents
 │
 ▼
Offline Chunking
 │
 ▼
Offline Embedding
 │
 ▼
Persistent Vector Index
 │
 ▼
Query
 │
 ▼
Query Embedding
 │
 ▼
Vector Retrieval
 │
 ▼
Reranking
 │
 ▼
Context Construction
 │
 ▼
LLM Generation
 │
 ▼
Grounding / Guardrails
 │
 ▼
Structured Answer
```

Document chunking and corpus indexing remain offline.

Do NOT introduce online document chunking into the normal query path.

---

# 4. MULTILINGUAL REQUIREMENT

EchoQuery must support exactly these locales:

```text
en-IN
hi-IN
bn-IN
ta-IN
te-IN
kn-IN
ml-IN
mr-IN
gu-IN
pa-IN
od-IN
```

The system must preserve Indic/non-ASCII text.

Normalize ingested text using Unicode NFC.

Do not solve multilingual support by silently translating everything into English.

The RAG system must operate in the user's language wherever the selected models/providers support it.

The answer language must correspond to the query language.

Test multilingual behaviour rather than merely declaring language support.

---

# 5. MODEL / SERVICE DIRECTION

The production STT direction is:

```text
Sarvam STT
```

The production generation direction is:

```text
Sarvam 105B
```

Do not replace these with a different architecture simply because another model is easier to integrate.

For development/testing, provider abstractions may use mocks/local providers where necessary.

Production model/provider selection for embeddings and reranking must be evidence-driven.

Do not invent benchmark numbers.

If the repository still has provider placeholders, complete the abstraction first, then benchmark/validate the real candidate.

---

# 6. LATENCY CONTRACT

Latency must be measured correctly.

STT latency is:

```text
audio → transcript
```

RAG latency is:

```text
RAG request entry
 ↓
query processing
 ↓
query embedding
 ↓
vector retrieval
 ↓
reranking
 ↓
context construction
 ↓
generation
 ↓
grounding/guardrails
 ↓
serialization
```

End-to-end latency is:

```text
audio → final answer
```

The `<200 ms` requirement applies to the RAG portion only.

STT is excluded from the 200 ms RAG budget.

Report separately:

```text
STT:
P50
P70
P95
P100

RAG:
P50
P70
P95
P100

E2E:
P50
P70
P95
P100
```

Also report internal RAG stage latency.

Never fake or manufacture latency numbers.

If the real production system cannot meet the target, report the measured result honestly and identify the bottleneck.

---

# 7. DEPLOYMENT DECISION — LOCK THIS ARCHITECTURE

The deployment target is:

```text
Internet
 │
 ▼
Cloudflare
 │
 │ HTTPS / WSS
 ▼
DigitalOcean Droplet
 │
 └── Docker Compose
 │
 ├── Frontend
 │
 ├── FastAPI
 │
 └── Qdrant
```

Deployment principles:

- DigitalOcean
- Ubuntu
- Docker
- Docker Compose
- self-hosted Qdrant
- FastAPI on the same machine
- frontend on the same machine
- Cloudflare in front
- HTTPS/WSS through Cloudflare
- persistent Qdrant volume
- environment/secrets supplied through environment configuration
- health checks
- restart policies
- logs
- reproducible startup

Do NOT introduce:

- Kubernetes
- ECS
- EKS
- RDS
- managed vector database
- unnecessary load balancers
- unnecessary AWS infrastructure
- microservices for components that do not need independent deployment

This is intentionally a hackathon-grade production architecture.

Keep it simple.

---

# 8. DATASET DEPLOYMENT RULE

Do NOT place the entire MSMARCO-XI dataset on the production server.

The dataset is used for:

```text
offline ingestion
offline processing
offline chunking
offline embedding/index construction
evaluation
benchmarking
```

Production should receive the resulting required index/artifacts, not the complete raw dataset.

Raw/generated datasets, indexes, and benchmark artifacts must not accidentally enter Git.

---

# 9. EXECUTION STRATEGY

You MUST work task-by-task.

Do not implement the whole repository in one giant uncontrolled change.

For each task:

```text
1. Inspect existing implementation.
2. Determine exactly what is missing.
3. Write/update tests where appropriate.
4. Implement the smallest clean change.
5. Run focused tests.
6. Run relevant integration tests.
7. Run formatting/compile/static checks available in the project.
8. Inspect the diff.
9. Update task documentation.
10. Only then proceed to the next task.
```

Do not repeatedly change direction.

Do not replace working architecture without a concrete technical reason.

Do not create speculative abstractions.

Do not create unnecessary files.

Do not create duplicate implementations.

Prefer simple, explicit, maintainable code.

---

# 10. PHASES

The project should now be tracked using these phases.

## PHASE 0 — Repository / Architecture Reconciliation

Complete:

- inspect repository
- inspect Git status/history
- inspect all existing contracts
- inspect current RAG implementation
- inspect backend
- inspect frontend
- inspect external-service adapters
- inspect infrastructure
- update the three task/plan documents
- reconcile completed vs remaining tasks
- verify there is one canonical implementation for each responsibility

Do not start feature development until the task documents accurately describe reality.

---

# PHASE 1 — RAG CORE COMPLETION

Complete the remaining RAG work.

### 1.1 Dataset

Verify existing MSMARCO-XI ingestion.

Requirements:

- streaming parquet loading
- schema validation
- deterministic IDs
- Unicode NFC
- metadata preservation
- deterministic output
- no mutation of raw data

Do not rewrite already-correct ingestion code.

### 1.2 Chunking

Complete real-corpus benchmarking of:

- fixed-size
- sentence-aware
- semantic

Then select the production strategy based on measured quality/performance.

Record the decision in the appropriate ADR.

### 1.3 Embeddings

Complete:

- multilingual benchmark
- production provider selection
- configuration
- batching
- persistence
- Qdrant integration
- metadata preservation
- deterministic IDs
- index reproducibility

### 1.4 Retrieval

Complete:

- top-k retrieval
- cross-lingual evaluation
- Recall@k
- MRR@k
- nDCG@k
- reranker evaluation
- latency measurement
- production retrieval/reranker decision

### 1.5 Generation

Complete:

- structured answer schema
- same-language generation
- Sarvam 105B integration
- timeout handling
- provider abstraction
- no-context behaviour
- unsupported-language behaviour
- grounded-false behaviour
- grounding guardrails

`grounded: false` is a valid answer state.

It is NOT automatically a pipeline error.

### 1.6 Orchestration

Complete the RAG orchestrator.

It must coordinate:

```text
validation
→ retrieval
→ reranking
→ context
→ generation
→ grounding
→ guardrails
→ response
```

The orchestrator coordinates.

Stage-specific logic belongs inside the respective components.

Add:

- request ID
- stage timing
- structured errors
- timeout handling
- bounded retries where appropriate
- structured logging
- observable failures

---

# PHASE 2 — RAG ↔ FASTAPI INTEGRATION

Connect the completed RAG engine to the existing backend.

The backend must consume only the agreed RAG protocol/result objects.

Verify:

```text
POST /query
```

or the existing agreed query contract.

Requirements:

- request validation
- request ID propagation
- locale validation
- RAG invocation
- structured Answer
- structured errors
- timeout handling
- observability

Do not duplicate RAG logic inside FastAPI.

FastAPI should be an integration boundary, not another RAG engine.

---

# PHASE 3 — STT INTEGRATION

Connect Sarvam STT to the application.

Flow:

```text
audio
 ↓
Sarvam STT
 ↓
Transcript Schema
 ↓
FastAPI
 ↓
RAG
```

Requirements:

- audio input validation
- STT provider abstraction
- Sarvam implementation
- transcript schema
- language/locale propagation
- request ID propagation
- STT timing
- timeout handling
- provider error handling

Do not mix STT implementation details into the RAG engine.

---

# PHASE 4 — WEBSOCKET / REAL-TIME FLOW

Complete the real-time application path.

Expected flow:

```text
Frontend
 │
 │ WebSocket
 ▼
FastAPI
 │
 ▼
STT
 │
 ▼
RAG
 │
 ▼
Answer
 │
 ▼
WebSocket
 │
 ▼
Frontend
```

Implement only the events defined by the existing WebSocket contract.

Requirements:

- connection lifecycle
- request ID
- audio/input events
- transcript event
- processing/status events if contract requires them
- answer event
- error event
- disconnect handling
- timeout handling

Do not invent a second WebSocket protocol.

---

# PHASE 5 — FRONTEND COMPLETION

Complete the frontend against the existing contracts.

The frontend must provide a usable EchoQuery experience:

```text
Start recording
 ↓
Speak
 ↓
STT feedback
 ↓
Processing
 ↓
Answer
```

It must:

- connect to WebSocket
- capture audio
- display transcript
- display answer
- display errors
- handle loading/processing state
- handle reconnect/disconnect appropriately
- display language where useful
- remain simple and demo-friendly

Do not redesign the product.

The objective is a functional multilingual voice RAG application.

---

# PHASE 6 — EXTERNAL SERVICES / CONFIGURATION

Complete the external-service layer.

Centralize configuration for:

- Sarvam credentials
- Sarvam 105B
- embedding provider
- reranker provider
- Qdrant
- frontend/backend URLs
- environment
- timeouts

Requirements:

- `.env.example`
- no secrets committed
- clear configuration errors
- development configuration
- production configuration
- provider timeout settings
- health/readiness checks

Do not hardcode credentials.

---

# PHASE 7 — DOCKERIZATION

Containerize the complete application.

Expected deployment structure:

```text
docker-compose.yml
 │
 ├── frontend
 ├── backend
 └── qdrant
```

Use persistent Qdrant storage.

Containers must have:

- health checks
- restart policy
- deterministic startup
- environment configuration
- sensible logging

Ensure backend waits for required dependencies to become ready rather than assuming startup order equals service readiness.

---

# PHASE 8 — DIGITALOCEAN DEPLOYMENT

Prepare the repository for deployment to a DigitalOcean Ubuntu Droplet.

Create/update only the required infrastructure files.

Provide:

- deployment documentation
- Docker Compose production configuration
- environment setup instructions
- Qdrant persistence
- firewall guidance
- service health checks
- restart behaviour
- update/redeploy procedure
- logs/troubleshooting
- Cloudflare configuration requirements

The deployment should be reproducible from a clean server.

Do not require Kubernetes.

Do not add unnecessary cloud infrastructure.

---

# PHASE 9 — CLOUDFLARE / HTTPS / WSS

Prepare the application to run behind Cloudflare.

Requirements:

```text
HTTPS
WSS
```

must work correctly.

Verify:

- frontend loads through HTTPS
- API requests work through HTTPS
- WebSocket works through WSS
- CORS is correct
- secure cookies/configuration are correct if used
- backend does not expose unnecessary ports publicly

Do not expose Qdrant publicly.

---

# PHASE 10 — COMPLETE EVALUATION

Create one reproducible evaluation flow.

Measure:

### Retrieval

```text
Recall@k
MRR@k
nDCG@k
```

### Grounding

```text
precision
recall
F1
```

### Latency

```text
STT P50/P70/P95/P100
RAG P50/P70/P95/P100
E2E P50/P70/P95/P100
```

### RAG stages

```text
query preprocessing
embedding
vector search
reranking
context construction
generation
grounding/guardrails
serialization
```

Evaluate across supported languages where representative test data exists.

Clearly label:

- fixture benchmark
- local benchmark
- production-like benchmark
- single-request benchmark
- concurrent benchmark

Never present a fixture result as production performance.

---

# PHASE 11 — SECURITY / RELIABILITY PASS

Before calling EchoQuery complete, verify:

- no secrets in Git
- no debug credentials
- Qdrant is not publicly exposed
- API validation exists
- WebSocket input is validated
- request sizes are bounded
- timeouts exist
- external calls fail safely
- errors do not leak secrets
- logs do not contain credentials
- container restart behaviour works
- health checks work
- unsupported locales fail correctly
- malformed input fails correctly

---

# PHASE 12 — END-TO-END DEMO

The final system must support this complete scenario:

```text
User opens EchoQuery
 ↓
Frontend connects
 ↓
User selects/speaks supported Indian language
 ↓
User records audio
 ↓
Audio reaches backend
 ↓
Sarvam STT produces transcript
 ↓
Transcript enters RAG
 ↓
Query is embedded
 ↓
Qdrant retrieves evidence
 ↓
Reranker selects evidence
 ↓
Context is constructed
 ↓
Sarvam 105B generates answer
 ↓
Grounding/guardrails validate answer
 ↓
Structured Answer returned
 ↓
WebSocket sends result
 ↓
Frontend displays answer
```

This is the definition of "complete".

A standalone RAG library is NOT complete EchoQuery.

A working backend without frontend is NOT complete EchoQuery.

A frontend mock without real STT/RAG is NOT complete EchoQuery.

Docker files without a working deployment are NOT complete EchoQuery.

---

# 11. TESTING STANDARD

Do not finish by saying "the code looks correct."

Every phase must have evidence.

At minimum, run the relevant:

```text
unit tests
integration tests
compile/type/static checks available in the repository
CLI smoke tests
contract validation
Docker build
Docker Compose validation
health checks
end-to-end test
```

For the RAG engine, maintain the existing test suite and ensure the full suite passes.

For the final application, create a temporary/mock external-service mode where necessary so that the complete application can be tested without consuming paid API calls.

Real provider tests must remain separately identifiable.

---

# 12. TASK EXECUTION DISCIPLINE

You are allowed to modify:

```text
00-contracts/
01-backend-api/
02-frontend/
03-ai-rag-engine/
04-external-services/
05-data/
06-evaluation/
07-scripts/
08-infrastructure/
09-docs/
```

because the current objective is the completion of the entire application.

However:

**Do not change architecture merely to make implementation easier.**

Contracts remain authoritative.

When changing a contract, document why.

When changing an architectural decision, create/update the relevant ADR.

---

# 13. DOCUMENTATION MUST STAY IN SYNC

After every completed phase, update:

```text
.claude/worktrees/utkarsh-rag-tasklist/notes/Utkarsh-TASK.md
.claude/worktrees/utkarsh-rag-tasklist/notes/docs/superpowers/plans/2026-08-21-ai-rag-engine.md
.claude/worktrees/utkarsh-rag-tasklist/notes/AI-RAG-TASKS.md
```

Do not leave the roadmap describing work that is already completed.

Do not mark work complete without verification.

Record:

```text
what changed
what was tested
what passed
what remains
what is externally blocked
```

---

# 14. HUMAN-OWNED GATES

Do not pretend you can perform actions requiring credentials or external approval.

Clearly identify gates such as:

- Sarvam credentials
- production API keys
- DigitalOcean account/server access
- Cloudflare DNS access
- production Qdrant/index deployment
- final production model/provider approval

Implement everything that can be implemented without those credentials.

Leave clean, documented integration points for the human-owned gates.

---

# 15. DEFINITION OF DONE

EchoQuery is DONE only when all of the following are true:

- \[ \] Contracts are internally consistent.
- \[ \] RAG engine is complete.
- \[ \] Multilingual retrieval is validated.
- \[ \] Production embedding/reranker choices are documented.
- \[ \] Sarvam 105B generation integration exists.
- \[ \] Grounding and guardrails work.
- \[ \] RAG orchestrator works.
- \[ \] FastAPI consumes the RAG pipeline.
- \[ \] Sarvam STT integrates with the backend.
- \[ \] WebSocket audio/query/answer flow works.
- \[ \] Frontend works against the real backend.
- \[ \] External service configuration is complete.
- \[ \] Docker images build.
- \[ \] Docker Compose starts the application.
- \[ \] Qdrant persistence works.
- \[ \] Health checks work.
- \[ \] Cloudflare-compatible HTTPS/WSS configuration exists.
- \[ \] DigitalOcean deployment instructions are reproducible.
- \[ \] Security/reliability checks pass.
- \[ \] End-to-end multilingual demo works.
- \[ \] Evaluation produces real measured results.
- \[ \] STT/RAG/E2E latency is separately reported.
- \[ \] Documentation matches the actual implementation.
- \[ \] No known critical integration bug remains.

---

# 16. IMPORTANT BEHAVIOUR

Do not stop after completing the RAG engine.

Do not stop after tests pass locally.

Do not stop after writing Docker files.

Do not stop after creating deployment documentation.

Continue through the phases until the COMPLETE EchoQuery application is functional.

At every point, prefer:

```text
inspect → implement → test → verify → document → next task
```

rather than:

```text
design → rewrite everything → hope it works
```

Keep the codebase minimal, maintainable, and architecture-consistent.

Do not create spaghetti code.

Do not introduce unnecessary frameworks.

Do not create speculative abstractions.

Do not change the project direction.

**Your final objective is a working EchoQuery application, not merely a completed task list.**
:::

## User

The new objective locks a different deployment architecture than the earlier discussion: Cloudflare in front of a single DigitalOcean Compose stack containing frontend, FastAPI, and Qdrant. I’ll reflect that explicitly in the three canonical task files and mark the older Vercel/DuckDNS guide as superseded rather than silently carrying conflicting deployment instructions forward. 
use digital ocean

## Assistant

Yes — **DigitalOcean is the deployment target**.

The deployment architecture should be locked as:

```text
 Internet
 │
 ▼
 Cloudflare
 HTTPS / WSS
 │
 ▼
 ┌─────────────────────────┐
 │ DigitalOcean Droplet │
 │ │
 │ Docker Compose │
 │ │
 │ ┌───────────────────┐ │
 │ │ Frontend │ │
 │ ├───────────────────┤ │
 │ │ FastAPI │ │
 │ ├───────────────────┤ │
 │ │ Qdrant │ │
 │ └───────────────────┘ │
 │ │
 │ Persistent Qdrant │
 │ volume │
 └─────────────────────────┘
```

So the Codex instruction should explicitly say:

> **Use DigitalOcean as the sole application hosting platform. Deploy the complete EchoQuery stack to a single DigitalOcean Droplet using Docker Compose. Cloudflare sits in front of the Droplet for DNS, HTTPS and WSS. Frontend, FastAPI and Qdrant run as Compose services on the same Droplet. Do not use Vercel, AWS, ECS, EKS, RDS, managed Qdrant, or other cloud deployment platforms unless explicitly required later.**

And yes, your statement about the old deployment guide is correct: **mark Vercel/DuckDNS instructions as superseded rather than mixing both architectures into the project documentation.**

The current project notes also support the DigitalOcean direction, including the 2–4 GB Droplet architecture and Docker Compose/Qdrant approach. fileciteturn7file0

### One important correction to my previous prompt

I would change this wording:

> `DigitalOcean Droplet → Docker Compose → FastAPI + frontend + self-hosted Qdrant → Cloudflare`

to the more precise:

> **Cloudflare → DigitalOcean Droplet → Docker Compose → Frontend + FastAPI + Qdrant**

because Cloudflare is the external entry point, while DigitalOcean is the actual compute/hosting platform.

For Codex, the deployment requirement should therefore be treated as **locked architecture, not a suggestion**.

## User

# Production Environment Setup

This is the environment-variable guide for the planned deployment:

```text
Frontend Vercel
Backend/RAG DigitalOcean Droplet
Reverse proxy Nginx
TLS Let's Encrypt via Certbot
Hostname DuckDNS subdomain
Vector DB Qdrant, private Docker service on the Droplet
```

> **Current status:** this is a preparation guide for the finished application. The repository is still incomplete, so this document does not claim that the current build is production-ready. Do not create production secrets or run the final deploy until the deployment gates near the end of this file are cleared.

The frontend must call an HTTPS API and a WSS WebSocket. A browser page served by Vercel over HTTPS cannot reliably call `http://DROPLET_IP` or `ws://DROPLET_IP`.

The names below match the current backend settings and deployment scripts. The repository `.env.example` files are templates only; do not commit real values to this repository. Use this guide as the source of truth for `DUCKDNS_DOMAIN`: the update script requires the short label, such as `echoquery-api`, not the full `.duckdns.org` hostname.

## Replacement Map

These are the values that must eventually be replaced with real deployment values. Everything beginning with `REPLACE_` or `VERIFY_` is intentionally unresolved.

| Variable | Where it belongs | Replace it with | Where to get it |
| --- | --- | --- | --- |
| `DROPLET_RESERVED_IP` | Droplet operator environment | DigitalOcean Reserved IPv4 address | DigitalOcean Control Panel -> Networking -> Reserved IPs. Attach it to the Droplet first. |
| `DUCKDNS_DOMAIN` | Droplet operator environment | Short label, for example `echoquery-api` | The subdomain you create at DuckDNS. Do not include `.duckdns.org`. |
| `DUCKDNS_TOKEN` | Droplet operator environment, secret | DuckDNS account token | The token shown after signing in at DuckDNS. |
| `API_HOSTNAME` | Droplet operator environment | Full hostname, for example `echoquery-api.duckdns.org` | Combine the DuckDNS label with `.duckdns.org`. |
| `LETSENCRYPT_EMAIL` | Droplet operator environment | A real monitored email address | Your own email; Let's Encrypt uses it for certificate notices. |
| `VERCEL_ORIGIN` | Used to derive backend allowlists | Exact production URL, for example `https://echoquery.vercel.app` | Vercel project -> Deployments -> production deployment. Copy the URL without a trailing slash. |
| `SARVAM_API_KEY` | Backend API environment, secret | Real Sarvam API key | Sarvam developer dashboard/API-key page. |
| `SARVAM_LLM_MODEL` | Backend API environment | Exact supported model ID | Sarvam's current model documentation or dashboard; do not guess it. |
| `EMBEDDING_MODEL` | Backend and indexer environments | Benchmark-selected multilingual embedding model | The project's multilingual quality/latency benchmark. This is not decided safely yet. |
| `EMBEDDING_DIMENSION` | Backend and indexer environments | Output dimension of the selected embedding model | The selected model's documentation/configuration. Rebuild Qdrant whenever this changes. |
| `RERANKER_MODEL` | Backend and indexer environments | Benchmark-selected reranker, or an empty value | The project's retrieval quality/latency benchmark. Leave empty if it cannot fit the latency budget. |

The public Vercel variables are derived rather than independently purchased or generated:

```text
VITE_API_BASE_URL=https://API_HOSTNAME
VITE_WS_URL=wss://API_HOSTNAME/ws
```

## 1. Values To Obtain First

### DigitalOcean

1. Create the Droplet in the region closest to the users and the model provider. Bangalore is preferred when available.
2. Reserve a DigitalOcean Reserved IP and attach it to the Droplet. Use the Reserved IP, not the temporary Droplet IP, for DNS.
3. Record:

```text
DROPLET_RESERVED_IP=your IPv4 address from DigitalOcean
```

4. In the DigitalOcean firewall, allow only TCP `22`, `80`, and `443`. Restrict SSH (`22`) to your own public IP when possible. Do not expose Qdrant `6333`.

### DuckDNS

1. Sign in at \[DuckDNS\](https://www.duckdns.org/).
2. Create a subdomain, for example `echoquery-api`.
3. Set its IPv4 address to `DROPLET_RESERVED_IP`.
4. Copy the DuckDNS token from the DuckDNS account page. It is a secret and must remain on the server.

Use these values. `API_HOSTNAME` is the public DNS name; `DUCKDNS_DOMAIN` is the short DuckDNS label used by `08-infrastructure/deployment/duckdns-update.sh` and must not include `.duckdns.org`:

```text
DUCKDNS_DOMAIN=echoquery-api
DUCKDNS_TOKEN=replace_with_the_token_from_duckdns
API_HOSTNAME=echoquery-api.duckdns.org
DROPLET_RESERVED_IP=your IPv4 address from DigitalOcean
```

Check DNS from your computer before requesting a certificate:

```powershell
Resolve-DnsName echoquery-api.duckdns.org -Type A
```

The returned address must equal the Reserved IP. If the address changes later, update DuckDNS before renewing TLS:

```bash
curl "https://www.duckdns.org/update?domains=echoquery-api&token=DUCKDNS_TOKEN&ip=DROPLET_RESERVED_IP"
```

Create a server-only operator file for the DuckDNS and certificate scripts:

```bash
sudo install -d -m 700 /etc/echoquery
sudo touch /etc/echoquery/deployment.env
sudo chown root:root /etc/echoquery/deployment.env
sudo chmod 600 /etc/echoquery/deployment.env
sudo nano /etc/echoquery/deployment.env
```

Contents:

```dotenv
API_HOSTNAME=echoquery-api.duckdns.org
LETSENCRYPT_EMAIL=REPLACE_WITH_REAL_EMAIL
DUCKDNS_DOMAIN=echoquery-api
DUCKDNS_TOKEN=REPLACE_WITH_DUCKDNS_TOKEN
DROPLET_RESERVED_IP=REPLACE_WITH_DIGITALOCEAN_RESERVED_IP
```

The deployment scripts read these values from their **process environment**; they do not automatically load this file. When the project is ready, load it explicitly:

```bash
sudo bash -c 'set -a; . /etc/echoquery/deployment.env; set +a; bash /opt/echoquery/08-infrastructure/deployment/duckdns-update.sh'
```

### Vercel

After the frontend is deployed, copy its exact production origin, for example:

```text
VERCEL_ORIGIN=https://echoquery.vercel.app
```

Use the exact origin with no trailing slash. Preview deployments have different origins; add them to the allowlist only when you intentionally want previews to call production.

### Sarvam

Create/copy the API key from the Sarvam developer dashboard. This key belongs only in the DigitalOcean backend environment. Never put it in a Vercel `VITE_*` variable.

```text
SARVAM_API_KEY=replace_with_the_real_sarvam_key
SARVAM_LLM_BASE_URL=https://api.sarvam.ai
SARVAM_LLM_MODEL=VERIFY_CURRENT_MODEL_ID_IN_SARVAM_DASHBOARD
```

The model ID must be copied from Sarvam's current documentation/account. Do not guess it.

## 2. DigitalOcean Backend Environment

Create this file on the Droplet only:

```bash
sudo install -d -m 700 /etc/echoquery
sudo touch /etc/echoquery/api.env
sudo chown root:root /etc/echoquery/api.env
sudo chmod 600 /etc/echoquery/api.env
sudo nano /etc/echoquery/api.env
```

Put the following in `/etc/echoquery/api.env`, replacing every value marked `REPLACE_` or `VERIFY_`:

```dotenv
# Runtime
APP_ENV=production
APP_HOST=0.0.0.0
APP_PORT=8000
LOG_FORMAT=json

# Public browser endpoints. These must match the Nginx certificate hostname.
PUBLIC_API_ORIGIN=https://echoquery-api.duckdns.org
PUBLIC_WS_ORIGIN=wss://echoquery-api.duckdns.org/ws

# Browser security. Use the exact Vercel origin, without a trailing slash.
CORS_ALLOWED_ORIGINS=https://echoquery.vercel.app
WS_ALLOWED_ORIGINS=https://echoquery.vercel.app

# Supported locale contract
SUPPORTED_LOCALES=en-IN,hi-IN,bn-IN,ta-IN,te-IN,kn-IN,ml-IN,mr-IN,gu-IN,pa-IN,od-IN

# Retrieval and latency controls
RAG_TOP_K=5
RAG_FETCH_K=20
RAG_TOTAL_DEADLINE_MS=200
MAX_QUERY_CHARS=2000

# Qdrant is private inside the Docker Compose network. Do not use the public IP.
QDRANT_URL=http://qdrant:6333
QDRANT_COLLECTION=echoquery_chunks_v1
QDRANT_DISTANCE=cosine

# These are selected only after the real multilingual benchmark.
EMBEDDING_MODEL=VERIFY_BENCHMARK_SELECTED_MODEL
EMBEDDING_DIMENSION=VERIFY_BENCHMARK_SELECTED_DIMENSION
RERANKER_MODEL=VERIFY_BENCHMARK_SELECTED_RERANKER_OR_EMPTY

# Sarvam generation
SARVAM_API_KEY=REPLACE_WITH_SARVAM_API_KEY
SARVAM_LLM_BASE_URL=https://api.sarvam.ai
SARVAM_LLM_MODEL=VERIFY_CURRENT_MODEL_ID_IN_SARVAM_DASHBOARD
SARVAM_LLM_TIMEOUT_MS=150
SARVAM_LLM_MAX_RETRIES=0

# Guardrails
GROUNDING_ENABLED=true
GROUNDING_TIMEOUT_MS=25

# The current Settings class does not consume METRICS_ENABLED or PROMETHEUS_ENABLED.
# Do not add those flags expecting them to enable an exporter.
```

### What each backend value comes from

| Variable | Replace with | How to get it |
| --- | --- | --- |
| `PUBLIC_API_ORIGIN` | `https://API_HOSTNAME` | Build from the DuckDNS hostname after DNS resolves. |
| `PUBLIC_WS_ORIGIN` | `wss://API_HOSTNAME/ws` | Same hostname; use `wss`, not `ws`. |
| `CORS_ALLOWED_ORIGINS` | Vercel production URL | Copy from the Vercel deployment URL. |
| `WS_ALLOWED_ORIGINS` | Vercel production URL | Usually the same value as CORS. |
| `SARVAM_API_KEY` | Secret API key | Sarvam dashboard; keep server-only. |
| `SARVAM_LLM_MODEL` | Current supported model ID | Sarvam model documentation/dashboard. |
| `EMBEDDING_MODEL` | Benchmark winner | Choose only after the multilingual retrieval benchmark. |
| `EMBEDDING_DIMENSION` | Dimension of that winner | Read from the selected embedding model; it must match Qdrant. |
| `RERANKER_MODEL` | Benchmark decision or empty | Keep only if its quality gain fits the latency budget. |
| `QDRANT_COLLECTION` | Versioned index name | Change when vector dimension/model changes, then rebuild the index. |

These values can remain as shown because they are deployment choices rather than secrets: `APP_ENV`, `APP_HOST`, `APP_PORT`, locale list, `RAG_TOP_K`, `RAG_FETCH_K`, timeout controls, logging flags, and the internal Qdrant URL. `METRICS_ENABLED` and `PROMETHEUS_ENABLED` are not current runtime settings; observability is currently emitted through structured logs and latency fields.

Do not claim the 200 ms target from these settings. The full path still needs a real benchmark over a reasonable query set covering preprocessing/chunking where applicable, embedding, Qdrant, reranking, generation, grounding, and final serialization. The required report is P50/P70/P100; P95 may be included as an additional percentile.

## 3. Indexer Environment (Optional)

The current ingestion and index-build scripts take paths and model settings as command-line arguments, not from an automatic `.env` loader. If you keep an operator environment file for repeatable runs, keep it separate from the API file so it cannot accidentally expose index credentials through the API container:

```bash
sudo touch /etc/echoquery/indexer.env
sudo chown root:root /etc/echoquery/indexer.env
sudo chmod 600 /etc/echoquery/indexer.env
sudo nano /etc/echoquery/indexer.env
```

Suggested values:

```dotenv
APP_ENV=production
QDRANT_URL=http://qdrant:6333
QDRANT_COLLECTION=echoquery_chunks_v1
EMBEDDING_MODEL=VERIFY_BENCHMARK_SELECTED_MODEL
EMBEDDING_DIMENSION=VERIFY_BENCHMARK_SELECTED_DIMENSION
DATA_RAW_DIR=/app/data/raw
DATA_PROCESSED_DIR=/app/data/processed
DATA_CHUNKS_DIR=/app/data/chunks
DATA_INDEX_DIR=/app/data/indexes
```

The corpus, selected model artifacts, and index must be installed on the Droplet through the controlled deployment/indexing process. Do not place the raw dataset or generated index in Git. Before using a real embedding model, replace both `EMBEDDING_MODEL` and `EMBEDDING_DIMENSION` after the multilingual benchmark and rebuild the versioned Qdrant collection.

## 4. Nginx and Certbot Values

Nginx needs the same hostname used by `PUBLIC_API_ORIGIN`. Certbot needs an email for renewal notices. A bare DigitalOcean IP cannot receive a normal Let's Encrypt hostname certificate, so issue the certificate for the DuckDNS name:

```text
API_HOSTNAME=echoquery-api.duckdns.org
LETSENCRYPT_EMAIL=your-real-email@example.com
```

Install the certificate after:

1. DuckDNS A record resolves to the Reserved IP.
2. Nginx is listening on port `80`.
3. The DigitalOcean firewall allows port `80`.

On the Droplet:

```bash
sudo certbot --nginx \
 --domain echoquery-api.duckdns.org \
 --email your-real-email@example.com \
 --agree-tos \
 --no-eff-email \
 --redirect

sudo certbot renew --dry-run
```

Keep port `80` open for the HTTP-01 renewal challenge. Certbot manages the certificate under `/etc/letsencrypt/live/echoquery-api.duckdns.org/`.

When the application and deployment files are ready, the repository deploy script must also receive the operator values in its process environment:

```bash
sudo bash -c 'set -a; . /etc/echoquery/deployment.env; set +a; ENV_FILE=/etc/echoquery/api.env bash /opt/echoquery/08-infrastructure/deployment/deploy.sh /opt/echoquery'
```

Do not run that command against the current incomplete repository until the host-Nginx connectivity gate below is fixed.

## 5. Vercel Environment Variables

Set these in the Vercel project for the Production environment. They are public browser configuration, not secrets:

```dotenv
VITE_API_BASE_URL=https://echoquery-api.duckdns.org
VITE_WS_URL=wss://echoquery-api.duckdns.org/ws
VITE_APP_ENV=production
```

Never set any of these in Vercel frontend variables:

```text
SARVAM_API_KEY
DUCKDNS_TOKEN
QDRANT_URL
QDRANT_API_KEY
SSH_PRIVATE_KEY
EMBEDDING_MODEL credentials
```

If the frontend uses a different build prefix (for example `NEXT_PUBLIC_` instead of `VITE_`), keep the same public values but follow the frontend framework's required prefix. The backend still owns all provider and vector-database secrets.

This repository currently uses Vite, so `VITE_` is the correct prefix. Set the variables in Vercel under **Project Settings -> Environment Variables**, scope them to **Production**, and redeploy after changing them. These variables are visible in the browser bundle and therefore must never contain secrets.

## 6. Current Repository Deployment Gates

Clear these before treating the environment setup as deployable:

- \[ \] Select the real multilingual embedding model, its dimension, and the reranker decision through project-specific benchmarks.
- \[ \] Complete and verify the production Sarvam, Qdrant, STT, RAG, guardrail, and frontend microphone/WebSocket integrations.
- \[ \] Fix API reachability between host Nginx and Docker. The current Nginx upstream is `127.0.0.1:8000`, while the production Compose file only uses `expose: 8000`; `expose` does not publish the container port to the host. A later code change must either bind `127.0.0.1:8000:8000` or place Nginx on the same Docker network and proxy by service name.
- \[ \] Verify the frontend production build and dependency lockfile before enabling Vercel deployment.
- \[ \] Run a real end-to-end production benchmark and demonstrate full RAG P100 strictly below `200 ms`; setting `RAG_TOTAL_DEADLINE_MS=200` alone is not evidence.
- \[ \] Confirm the production health endpoint checks actual dependencies rather than only returning a process-level success response.

## 7. Final Preflight Checklist

- \[ \] Reserved IP is attached to the Droplet.
- \[ \] DuckDNS A record resolves to that Reserved IP.
- \[ \] `/etc/echoquery/api.env`, `/etc/echoquery/deployment.env`, and optional `indexer.env` are mode `600` and not in Git.
- \[ \] Nginx uses `API_HOSTNAME` and proxies `/api/`, `/health`, and `/ws` to the API container.
- \[ \] Qdrant has no public `6333` port mapping.
- \[ \] Certbot issues and renews the certificate successfully.
- \[ \] Vercel variables use `https://` and `wss://`.
- \[ \] Backend CORS and WebSocket allowlists contain the exact Vercel origin.
- \[ \] `https://echoquery-api.duckdns.org/health` succeeds from an external network.
- \[ \] A WebSocket connection succeeds from the deployed Vercel frontend.
- \[ \] Production P50/P70/P100 latency is measured across a reasonable test set before calling the strict P100-under-200-ms requirement satisfied.

## Assistant

Yes. **This document is now obsolete for the new architecture** because it still assumes Vercel + DuckDNS + host Nginx + Certbot.

Do **not** let Codex merge this configuration into the new plan. The correct action is to mark it **SUPERSEDED** and replace it with the DigitalOcean-only architecture.

Use this exact instruction in the Codex prompt:

```text
IMPORTANT DEPLOYMENT DOCUMENTATION MIGRATION

The repository contains an older production environment guide that describes:

 Frontend Vercel
 Backend/RAG DigitalOcean
 Reverse proxy Nginx
 TLS Let's Encrypt / Certbot
 Hostname DuckDNS
 Vector DB Qdrant

THIS ARCHITECTURE IS SUPERSEDED.

Do NOT implement, preserve, or extend the Vercel + DuckDNS + host-Nginx + Certbot deployment architecture.

The new and authoritative deployment architecture is:

 Internet
 │
 ▼
 Cloudflare
 │
 │ HTTPS / WSS
 ▼
 DigitalOcean Droplet
 │
 ▼
 Docker Compose
 ├── frontend
 ├── FastAPI backend
 └── Qdrant

Deployment rules:

1. DigitalOcean is the sole application hosting platform.
2. Frontend runs inside Docker Compose on the DigitalOcean Droplet.
3. FastAPI runs inside Docker Compose on the same Droplet.
4. Qdrant runs inside Docker Compose on the same Droplet.
5. Qdrant must remain private and must NOT expose port 6333 publicly.
6. Cloudflare is the public entry point.
7. Cloudflare provides the public DNS and HTTPS/WSS edge.
8. The browser connects to the Cloudflare hostname.
9. Frontend API requests use HTTPS.
10. Frontend WebSocket connections use WSS.
11. Do not use Vercel.
12. Do not use DuckDNS.
13. Do not use Let's Encrypt/Certbot as the application's TLS architecture.
14. Do not require a host-level Nginx reverse proxy.
15. Do not introduce AWS, ECS, EKS, RDS, Kubernetes, managed Qdrant, or another hosting platform.
16. Keep the deployment as one reproducible Docker Compose stack.

The deployment should preferably expose only the required public HTTP/HTTPS entry point from the Droplet and keep internal services on the Docker network.

Use a production topology equivalent to:

 Cloudflare
 │
 ▼
 DigitalOcean Droplet
 │
 └── Docker Compose
 │
 ├── frontend
 │
 ├── backend
 │
 └── qdrant
 │
 └── persistent volume

The exact Cloudflare-to-Droplet TLS/origin configuration must be implemented according to the selected Cloudflare setup, but the application must ultimately support:

 https://<production-domain>
 wss://<production-domain>/ws

The frontend must NOT contain hardcoded Vercel URLs.

Use environment variables for the public API/WebSocket origin.

Replace the old production guide with a new DigitalOcean deployment guide covering:

- DigitalOcean Droplet provisioning
- Docker installation
- Docker Compose
- production environment variables
- Cloudflare DNS
- Cloudflare SSL/TLS configuration
- frontend/backend routing
- WebSocket/WSS support
- Qdrant persistence
- Qdrant private networking
- health checks
- restart policies
- logs
- deployment/update procedure
- rollback procedure
- firewall rules
- secrets management
- production smoke test

Mark the old Vercel/DuckDNS guide explicitly as:

 SUPERSEDED — DO NOT USE

Do not delete historical information if it is useful for understanding previous decisions. However, it must be impossible for a developer following the current documentation to mistake the old architecture for the current deployment architecture.

The current deployment architecture is LOCKED unless a future explicit architectural decision changes it.
```

### The important architectural change

The old document has:

```text
Vercel
 ↓
DuckDNS
 ↓
Nginx
 ↓
DigitalOcean
 ↓
FastAPI + Qdrant
```

We now want:

```text
 Cloudflare
 HTTPS / WSS
 │
 ▼
 DigitalOcean Droplet
 │
 Docker Compose
 │
 ┌────────────┼────────────┐
 ▼ ▼ ▼
 Frontend FastAPI Qdrant
 PRIVATE
```

This is significantly cleaner for the hackathon because **the entire EchoQuery application is deployed as one unit**. Frontend/backend/Qdrant versioning, networking, environment configuration and deployment can all be controlled through the same Compose stack.

Also, the old guide's `VERCEL_ORIGIN`, `VITE_API_BASE_URL=https://echoquery-api...`, DuckDNS scripts, Certbot scripts, and host-Nginx assumptions should **not appear in the new production configuration**.

The current Notion architecture already identifies the DigitalOcean direction and a 2–4 GB Droplet with Docker Compose. fileciteturn7file0

So for the three task files, I would make **DigitalOcean + Cloudflare + single Compose stack the explicit Phase 8/Deployment source of truth**, and mark the Vercel/DuckDNS guide as superseded.

## User

no cloud flare u stupid or what

## Assistant

You're right. I misunderstood your correction.

**No Cloudflare. No Vercel. No DuckDNS.**

The deployment architecture is simply:

```text
Internet
 │
 ▼
DigitalOcean Droplet
 │
 ▼
Docker Compose
 ├── Frontend
 ├── FastAPI / RAG Backend
 └── Qdrant
```

For the public application:

```text
https://<DIGITAL_OCEAN_DOMAIN_OR_IP>
 │
 ▼
 Frontend
 │
 ├── /api → FastAPI
 └── /ws → FastAPI WebSocket
 │
 └── Qdrant (private Docker network)
```

### Deployment decisions now locked

- **Hosting:** DigitalOcean
- **Server:** Single DigitalOcean Droplet
- **Orchestration:** Docker Compose
- **Frontend:** Docker container on the Droplet
- **Backend:** FastAPI container on the Droplet
- **RAG:** inside backend/application stack
- **Vector DB:** Qdrant container
- **Qdrant:** private Docker network; no public `6333`
- **Reverse proxy:** Nginx **inside the Compose stack**, if needed
- **TLS:** handled by the chosen DigitalOcean/Nginx deployment mechanism, not Cloudflare
- **Vercel:** ❌
- **Cloudflare:** ❌
- **DuckDNS:** ❌
- **AWS:** ❌
- **Kubernetes:** ❌

The Codex prompt should therefore say:

> **Deploy the complete EchoQuery application to a single DigitalOcean Droplet using Docker Compose. Frontend, FastAPI/RAG backend, Nginx, and Qdrant run on the Droplet. Qdrant remains private on the Docker network. Do not use Cloudflare, Vercel, DuckDNS, AWS, or any managed hosting/vector service. The objective is one self-contained DigitalOcean deployment that can be started, stopped, updated, and reproduced with Docker Compose.**

And the old production guide should be marked:

```text
SUPERSEDED — OLD DEPLOYMENT ARCHITECTURE

The previous Vercel + DigitalOcean + DuckDNS + Certbot deployment
architecture is obsolete.

Current deployment:
DigitalOcean Droplet + Docker Compose.
```

**That's the architecture we should use going forward.**

## User

abeeeee stupid yes vercel yes duck dns

## Assistant

😂 Okay, got it now. **Vercel + DuckDNS YES. Cloudflare NO.**

The correct final architecture is:

```text
 Internet
 │
 ┌────────┴────────┐
 │ │
 ▼ ▼
 Vercel DuckDNS
 Frontend API Domain
 │ │
 │ HTTPS │ HTTPS / WSS
 │ ▼
 │ DigitalOcean Droplet
 │ │
 │ ┌──────┴──────┐
 │ │ Nginx │
 │ └──────┬──────┘
 │ │
 │ FastAPI
 │ │
 │ RAG Engine
 │ │
 │ Qdrant
 │
 └────── HTTPS / WSS ──────►
```

### Locked deployment decisions

| Component | Decision |
|---|---|
| Frontend | **Vercel** |
| Backend/RAG | **DigitalOcean Droplet** |
| Vector DB | **Qdrant**, private Docker service |
| Reverse proxy | **Nginx** |
| Public API hostname | **DuckDNS** |
| TLS | **Let's Encrypt + Certbot** |
| Frontend → API | HTTPS |
| Frontend → WebSocket | WSS |
| Cloudflare | ❌ **Do not use** |
| AWS | ❌ |
| Kubernetes | ❌ |

So the old `Production Environment Setup` you pasted is actually **the correct deployment architecture**. It should **not** be superseded.

The only thing we need to do is make sure Codex treats that architecture as authoritative while completing the rest of EchoQuery.

### Corrected instruction for Codex

```text
DEPLOYMENT ARCHITECTURE — LOCKED

The production deployment architecture is:

Frontend:
 Vercel

Backend/RAG:
 DigitalOcean Droplet

Vector database:
 Qdrant running as a private Docker Compose service on the Droplet

Reverse proxy:
 Nginx on the DigitalOcean Droplet

TLS:
 Let's Encrypt / Certbot

Public backend hostname:
 DuckDNS subdomain

Network flow:

 User
 │
 ▼
 Vercel Frontend
 │
 ├── HTTPS ──────────────► DuckDNS hostname
 │ │
 │ ▼
 │ Nginx :443
 │ │
 │ ▼
 │ FastAPI
 │ │
 │ ▼
 │ RAG Engine
 │ │
 │ ▼
 │ Qdrant
 │ (private Docker network)
 │
 └── WSS ───────────────► /ws

This architecture is LOCKED.

DO NOT introduce Cloudflare.

DO NOT replace Vercel with another frontend host.

DO NOT replace DuckDNS with another DNS provider.

DO NOT replace DigitalOcean with AWS or another cloud provider.

DO NOT replace Qdrant with a managed vector database.

DO NOT replace Nginx + Let's Encrypt/Certbot with Cloudflare.

The existing Production Environment Setup document describing:

 Frontend Vercel
 Backend/RAG DigitalOcean
 Reverse proxy Nginx
 TLS Let's Encrypt via Certbot
 Hostname DuckDNS
 Vector DB Qdrant private Docker service

is therefore the AUTHORITATIVE deployment architecture.

Preserve it and make the implementation satisfy its deployment gates.

The final objective remains:

 COMPLETE ECHOQUERY APPLICATION

not merely a completed RAG engine.

Implement and verify:

 Frontend
 ↓
 Vercel
 ↓ HTTPS/WSS
 DuckDNS
 ↓
 Nginx
 ↓
 FastAPI
 ↓
 STT
 ↓
 RAG Orchestrator
 ↓
 Qdrant + Retrieval
 ↓
 Sarvam LLM
 ↓
 Grounding / Guardrails
 ↓
 Answer
 ↓
 WebSocket
 ↓
 Vercel Frontend

All deployment documentation, task lists, infrastructure files,
environment templates, health checks, and tests must remain consistent
with this architecture.
```

**Now we're aligned:** **Vercel + DigitalOcean + DuckDNS + Nginx + Let's Encrypt + private Qdrant.**

## User

### 5. Harness your model

Your model/pipeline should be run inside a proper harness — structured orchestration around the model (tool calls, retries, structured input/output handling, error recovery) rather than a single raw prompt-in, text-out call.

### 6. Guardrail your model

Add guardrails around your model — handling for off-topic queries, unsafe/inappropriate inputs, hallucination checks, or answers not grounded in the retrieved context. Show that your system knows when *not* to answer, not just how to answer

prompt for this also

## Assistant

Absolutely. For EchoQuery, these two requirements should be implemented as **real system capabilities**, not just mentioned in the documentation.

Use this as an additional Codex task prompt:

```text
## ECHOQUERY — MODEL HARNESS + GUARDRAILS IMPLEMENTATION

Implement the following two hackathon requirements as production-quality,
testable capabilities in the existing EchoQuery architecture:

1. HARNESS THE MODEL
2. GUARDRAIL THE MODEL

Do NOT create a separate experimental pipeline.
Integrate these capabilities into the existing RAG orchestrator and
existing contracts.

The goal is to demonstrate that EchoQuery is a properly orchestrated,
controlled multilingual RAG system rather than a simple:

 query → prompt → LLM → text

pipeline.

============================================================
1. MODEL HARNESS
============================================================

Create/complete a structured model execution harness around the LLM.

The harness must sit between the RAG orchestrator and the LLM provider.

Architecture:

 RAG Orchestrator
 │
 ▼
 Model Harness
 │
 ├── Input validation
 ├── Prompt/context construction
 ├── Model invocation
 ├── Timeout handling
 ├── Retry policy
 ├── Structured output parsing
 ├── Output validation
 ├── Failure recovery
 └── Observability
 │
 ▼
 LLM Provider
 │
 ▼
 Structured Model Result

Do NOT put orchestration logic directly inside the Sarvam provider.

The provider should be responsible for communicating with the model.

The harness should be responsible for controlling model execution.

------------------------------------------------------------
1.1 STRUCTURED INPUT
------------------------------------------------------------

Define/use a structured model request containing, as appropriate:

- request_id
- query
- locale
- retrieved_context
- source metadata
- system instructions
- generation configuration
- timeout/deadline
- grounding requirements

Do not pass arbitrary unstructured dictionaries through the entire pipeline
when an existing schema can be used.

Reuse existing contracts where possible.

------------------------------------------------------------
1.2 STRUCTURED OUTPUT
------------------------------------------------------------

The harness must require a structured model result.

At minimum:

- answer
- locale
- citations/source references where applicable
- confidence/grounding information where defined
- refusal/no-answer state
- model metadata if useful for observability

The exact schema must remain consistent with the existing Answer Schema.

Do NOT allow arbitrary raw LLM text to become the final API response.

If the model returns malformed structured output:

 model output
 ↓
 parser
 ↓
 validation failure
 ↓
 controlled recovery/refusal

Do not silently accept malformed output.

------------------------------------------------------------
1.3 RETRIES
------------------------------------------------------------

Implement bounded retries only where retries make technical sense.

Retry transient provider failures such as:

- temporary network errors
- rate-limit responses when retryable
- transient 5xx provider failures

Do NOT retry:

- invalid request
- unsupported locale
- malformed prompt/context
- grounding failure
- safety refusal
- deterministic schema validation failures

Respect the overall RAG deadline.

A retry must never cause the system to exceed the configured request deadline.

If:

 remaining_deadline <= retry_cost

do not retry.

The system should prefer a controlled failure over uncontrolled latency.

------------------------------------------------------------
1.4 TIMEOUTS
------------------------------------------------------------

Every model invocation must have an explicit timeout.

The harness must receive the overall RAG deadline.

Example:

 request deadline
 │
 ├── retrieval
 ├── reranking
 ├── context construction
 └── generation
 │
 └── model timeout

Do not create independent timeouts that can collectively exceed the
overall request deadline.

Record timeout events in structured logs.

------------------------------------------------------------
1.5 ERROR RECOVERY
------------------------------------------------------------

The harness must convert provider failures into controlled application
results.

Examples:

 Provider timeout
 → controlled model error

 Provider 5xx
 → retry if deadline allows
 → otherwise controlled failure

 Invalid model output
 → validation failure
 → bounded recovery/refusal

 Unsupported language
 → structured unsupported-language result

The frontend must never receive a raw provider exception or traceback.

------------------------------------------------------------
1.6 OBSERVABILITY
------------------------------------------------------------

Record structured metadata for every model execution:

- request_id
- model/provider
- locale
- start/end time
- latency
- retry count
- timeout status
- output validation status
- grounding status
- failure category

Never log:

- API keys
- secrets
- authorization headers
- unnecessary sensitive user data

------------------------------------------------------------
2. MODEL GUARDRAILS
============================================================

Add guardrails around the complete RAG generation path.

The system must demonstrate:

 "EchoQuery knows when NOT to answer."

Guardrails must operate before and after generation.

Architecture:

 User Query
 │
 ▼
 Input Guardrails
 │
 ├── allowed → RAG
 │
 └── rejected → controlled response
 │
 ▼
 User

 RAG
 │
 ▼
 Model Harness
 │
 ▼
 Output Guardrails
 │
 ├── grounded/safe → Answer
 │
 └── rejected → controlled no-answer
```

------------------------------------------------------------
2.1 OFF-TOPIC DETECTION
------------------------------------------------------------

EchoQuery is a domain-grounded RAG system.

If a user asks something outside the available knowledge domain,
the system must not hallucinate an answer.

Implement an off-topic/relevance check using the existing architecture.

Possible signals include:

- retrieval score
- evidence availability
- query/domain classification
- minimum relevance threshold

Do NOT rely exclusively on a hardcoded keyword blacklist.

Example:

 Query:
 "Who won the football World Cup?"

 Retrieved evidence:
 no relevant evidence

 Result:
 controlled no-answer

The system should communicate that it cannot answer from the available
knowledge rather than generating a fabricated answer.

------------------------------------------------------------
2.2 NO-EVIDENCE GUARDRAIL
------------------------------------------------------------

If retrieval produces no sufficiently relevant evidence:

 retrieved_context = insufficient

the system must NOT call the LLM simply to "try anyway".

Return a structured no-answer state.

For example conceptually:

 grounded = false
 answer = "I don't have enough information in the available sources
 to answer this question."

Use the project's actual Answer Schema rather than inventing a parallel
response format.

This state must be testable.

------------------------------------------------------------
2.3 LOW-CONFIDENCE RETRIEVAL
------------------------------------------------------------

Do not treat:

 top_k > 0

as proof that evidence exists.

Implement a meaningful relevance threshold based on the selected retrieval
and reranking configuration.

The threshold must be configurable.

Do not invent a threshold without evaluating it.

Use evaluation data to determine an appropriate threshold where possible.

Document the decision.

------------------------------------------------------------
2.4 GROUNDEDNESS CHECK
------------------------------------------------------------

After generation, verify that the answer is supported by retrieved context.

The system should detect cases where the model:

- introduces unsupported facts
- contradicts retrieved evidence
- answers beyond the available context
- invents citations
- ignores the evidence

Use an appropriate grounding strategy consistent with the existing
latency architecture.

Possible mechanisms include:

- citation/source requirement
- claim/evidence matching
- entailment-style verification
- model-based verifier
- deterministic source checks

Choose the simplest reliable method that fits the existing architecture.

Do not add an unnecessarily expensive second LLM pipeline unless evaluation
shows that it is required.

------------------------------------------------------------
2.5 HALLUCINATION HANDLING
------------------------------------------------------------

If the generated answer fails grounding validation:

 DO NOT return it as a normal successful answer.

Instead:

 answer
 ↓
 grounding check
 ↓
 FAIL
 ↓
 controlled no-answer/refusal

Example:

 "I couldn't verify that answer from the available sources."

The exact wording should be implemented through the Answer Schema.

The important requirement is:

 unsupported model output ≠ successful answer

------------------------------------------------------------
2.6 SAFETY / INAPPROPRIATE INPUT
------------------------------------------------------------

Add an appropriate lightweight safety guardrail for clearly unsafe or
inappropriate requests.

Do not build an unnecessarily complex moderation platform.

The system should have a controlled refusal path for requests that should
not be answered.

The safety decision must occur before generation where possible.

The final response must not expose internal guardrail implementation details.

------------------------------------------------------------
2.7 LANGUAGE-AWARE GUARDRAILS
------------------------------------------------------------

Guardrails must work with all supported EchoQuery locales:

 en-IN
 hi-IN
 bn-IN
 ta-IN
 te-IN
 kn-IN
 ml-IN
 mr-IN
 gu-IN
 pa-IN
 od-IN

Do NOT implement guardrails using English-only assumptions.

Unicode must remain intact.

If the query is supported but evidence is insufficient, return the
controlled no-answer response in the user's language where supported.

------------------------------------------------------------
3. INTEGRATE INTO THE EXISTING ORCHESTRATOR
============================================================

The final pipeline should conceptually become:

 Request
 │
 ▼
 Input Guardrails
 │
 ├── rejected → structured refusal
 │
 ▼
 Query Validation
 │
 ▼
 Query Embedding
 │
 ▼
 Retrieval
 │
 ▼
 Relevance / Evidence Guardrail
 │
 ├── insufficient → structured no-answer
 │
 ▼
 Reranking
 │
 ▼
 Context Construction
 │
 ▼
 Model Harness
 │
 ├── timeout
 ├── bounded retry
 ├── structured output validation
 └── failure recovery
 │
 ▼
 Generated Answer
 │
 ▼
 Grounding Guardrail
 │
 ├── FAIL → controlled no-answer
 │
 ▼
 Final Answer
 │
 ▼
 FastAPI / WebSocket
 │
 ▼
 Frontend

Do not duplicate this logic inside FastAPI.

The RAG orchestrator owns the pipeline.

The model harness owns model execution.

Guardrail components own validation decisions.

Providers only communicate with external services.

------------------------------------------------------------
4. IMPORTANT LATENCY REQUIREMENT
============================================================

Guardrails and the model harness must respect the existing RAG latency
budget.

The current RAG target is:

 total RAG latency < 200 ms

This must be measured, not assumed.

Do not blindly add expensive model calls.

In particular:

 retrieval
 + reranking
 + generation
 + grounding
 + retries

must fit within the overall deadline when the real production
configuration is evaluated.

If a guardrail cannot fit within the production latency budget:

1. measure it;
2. document the bottleneck;
3. prefer a deterministic/lightweight alternative;
4. do not silently remove the guardrail.

Do not claim the 200 ms target is achieved simply because a
RAG_TOTAL_DEADLINE_MS=200 setting exists.

------------------------------------------------------------
5. TEST REQUIREMENTS
============================================================

Add tests proving the harness and guardrails actually work.

At minimum:

MODEL HARNESS:

- valid model request
- structured output parsing
- malformed model output
- timeout
- transient provider failure
- retry succeeds
- retry exhausted
- deadline prevents retry
- unsupported locale
- provider error conversion

GUARDRAILS:

- valid in-domain query
- off-topic query
- no retrieved evidence
- low-relevance evidence
- grounded answer
- hallucinated/unsupported answer
- contradictory answer
- unsafe/inappropriate input
- multilingual no-answer
- multilingual grounded answer

END-TO-END:

 query
 → guardrail
 → retrieval
 → reranking
 → harness
 → grounding
 → Answer

Verify that the final API/WebSocket response is always a valid
contract-compliant response.

------------------------------------------------------------
6. DEMONSTRATION REQUIREMENT
============================================================

Create a small deterministic demonstration/evaluation set showing:

CASE 1 — Normal question

 Query → evidence → answer

CASE 2 — Off-topic question

 Query → rejected/no-answer

CASE 3 — No evidence

 Query → retrieval insufficient → no-answer

CASE 4 — Hallucinated model output

 Query → model generates unsupported claim
 → grounding fails
 → no-answer

CASE 5 — Provider failure

 Query → transient failure
 → bounded retry
 → successful answer

CASE 6 — Unsupported language

 Query → structured unsupported-language response

The evaluation output must clearly show that EchoQuery can distinguish:

 answerable
 unanswerable
 unsafe
 unsupported
 provider failure

rather than treating every request as:

 "ask the LLM and return whatever it says."

------------------------------------------------------------
7. DOCUMENTATION
============================================================

Update the canonical task documents:

 .claude/worktrees/utkarsh-rag-tasklist/notes/Utkarsh-TASK.md
 .claude/worktrees/utkarsh-rag-tasklist/notes/docs/superpowers/plans/2026-08-21-ai-rag-engine.md
 .claude/worktrees/utkarsh-rag-tasklist/notes/AI-RAG-TASKS.md

Add explicit tasks for:

 Model Harness
 ├── structured input
 ├── structured output
 ├── retries
 ├── timeouts
 ├── error recovery
 └── observability

 Guardrails
 ├── off-topic detection
 ├── evidence threshold
 ├── no-evidence refusal
 ├── grounding verification
 ├── hallucination handling
 ├── safety handling
 └── multilingual behaviour

Mark them complete only after tests and integration verification pass.

------------------------------------------------------------
8. DEFINITION OF DONE
============================================================

This requirement is complete only when:

\[ \] Model calls go through the model harness.
\[ \] Model input is structured.
\[ \] Model output is schema-validated.
\[ \] Transient failures have bounded retries.
\[ \] Overall deadlines are respected.
\[ \] Provider failures become controlled application errors.
\[ \] Model execution is observable.
\[ \] Off-topic queries are handled.
\[ \] No-evidence queries do not hallucinate.
\[ \] Low-relevance retrieval can produce no-answer.
\[ \] Generated answers undergo grounding validation.
\[ \] Unsupported/hallucinated answers are rejected.
\[ \] Unsafe/inappropriate requests have a controlled refusal path.
\[ \] Guardrails support the required locales.
\[ \] Guardrails are integrated into the actual RAG orchestrator.
\[ \] FastAPI/WebSocket receives only contract-compliant results.
\[ \] Tests cover success and failure paths.
\[ \] A deterministic demonstration proves the behaviour.
\[ \] Latency impact is measured.
\[ \] Documentation reflects the implementation.

MOST IMPORTANT:

Do not implement "guardrails" as a README claim.

Do not implement "model harness" as a wrapper that merely calls the
same LLM function.

The evaluator must be able to see actual orchestration:

 validation
 → controlled model execution
 → retry/recovery
 → structured output
 → evidence validation
 → grounding
 → refusal when appropriate

That behaviour is the deliverable.
```

## User

just tell this:

### 5. Harness your model

Your model/pipeline should be run inside a proper harness — structured orchestration around the model (tool calls, retries, structured input/output handling, error recovery) rather than a single raw prompt-in, text-out call.

### 6. Guardrail your model

Add guardrails around your model — handling for off-topic queries, unsafe/inappropriate inputs, hallucination checks, or answers not grounded in the retrieved context. Show that your system knows when *not* to answer, not just how to answer

dont add any thing extra from ur knowledge

## Assistant

Use this prompt:

```text
Implement the following two requirements in EchoQuery:

### 5. Harness your model

The model/pipeline must run inside a proper harness with structured orchestration around the model.

Implement:
- Tool calls where required
- Retries
- Structured input/output handling
- Error recovery

Do not use a single raw prompt-in, text-out model call.

### 6. Guardrail your model

Add guardrails around the model.

The system must handle:
- Off-topic queries
- Unsafe/inappropriate inputs
- Hallucination checks
- Answers that are not grounded in the retrieved context

The system must be able to recognize when it should not answer, rather than only knowing how to generate an answer.

Integrate both requirements into the existing EchoQuery pipeline without changing the established architecture.
```

## Resources

### Local attachments
- [2026-08-21-ai-rag-engine.md](../../../Raw/Export/file_00000000eb0082118c14ea3bf7ea93a6.dat)

### External references
- [HH Task_2](https://chatgpt.com/c/6a81ac51-7894-83ee-9d19-b4c68d755e51)
