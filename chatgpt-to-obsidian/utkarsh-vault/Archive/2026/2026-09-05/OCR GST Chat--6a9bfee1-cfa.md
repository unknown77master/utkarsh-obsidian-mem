---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a9bfee1-cfac-83ee-8f44-1f37bcaef079"
created: 1788608265.519619
updated: 1789571610.521775
resource_section: true
---

# OCR GST Chat

## User

which chat has context for ocr-gst filing project idea

## Assistant

Worked for 11s

## Assistant

The OCR → GST filing idea is in your chat titled **“Request for Event Approval”**, from **August 16, 2026**.

That’s the conversation where you shifted from pitching the Claude Code community meetup idea to this product concept:

- physical/digital receipts from email, Slack, etc.
- OCR extracts invoice/receipt data
- pushes structured data into DB / Excel / Google Sheets
- assists with monthly GST filing
- keeps a **human in the loop** rather than fully automating the process

You were using it as a **product pitch for an event application**. memcite

## User

should i use langchain langraph llama model olama for finetuning or should i use langchain langraph and sarvam multilingual ocr model api or should i make n8n workflow
think on it and give me entire tech stack, because physical recipets will be uploaded using entire react native app on appstore and playstore and digital will also be supported by mobile app, but taking photo by desktop is not possibe so that will not be included in desktop application, and electron for windows and mac react native 
right now lets fix entire tech stack

## Assistant

I’d design this as a proper product architecture, not as an n8n-first automation. The key decision is to keep OCR, extraction, validation, GST logic, and orchestration as separate layers so you can swap models later without rewriting the app.

## Assistant

Worked for 15s

## Assistant

For this product, I would **not fine-tune an Ollama/Llama model at the start**, and I would **not make n8n the core backend**.

Your strongest architecture is:

> **React Native + Electron → FastAPI → Sarvam Vision OCR → deterministic GST validation/extraction → LangGraph for human-in-the-loop workflow → PostgreSQL + object storage → GST/GSP APIs later**

The reason is simple: this is primarily a **document-processing + compliance workflow product**, not a chatbot. Sarvam Vision 1.5 is already purpose-built for OCR and schema-based extraction from invoices/forms in **22 Indian languages + English**, which is much closer to your problem than fine-tuning a generic Llama model yourself. Its `Extract` API can return exactly the fields you define as structured JSON/CSV/XLSX. citeturn551008search0turn551008search4

## Stack I would lock in

| Layer | Technology | Role |
|---|---|---|
| Mobile | **React Native + TypeScript** | Android + iOS, camera receipt capture, file upload |
| Desktop | **Electron + React + TypeScript** | Windows + macOS, digital invoice/file handling |
| Shared UI | React components/design tokens | Reuse between RN/web-style interfaces where practical |
| Backend | **Python + FastAPI** | Main API |
| Validation | **Pydantic** | Invoice schemas and API contracts |
| Workflow | **LangGraph** | OCR → validation → human review → approval → export/file |
| LLM abstraction | **LangChain, lightly** | Model/API integrations only |
| OCR/Doc AI | **Sarvam Vision 1.5 API** | OCR + structured invoice extraction |
| Primary DB | **PostgreSQL** | Companies, invoices, GST data, workflow state |
| ORM | **SQLAlchemy 2 + Alembic** | DB models + migrations |
| Cache/jobs | **Redis** | queues, caching, rate limiting |
| Background jobs | **Celery or Dramatiq** | OCR jobs, email sync, exports, reconciliations |
| File storage | **S3-compatible storage** | PDFs/images/original invoices |
| Auth | **Clerk / Auth0 initially**, later own auth if needed | Mobile + desktop authentication |
| Monitoring | **Sentry + OpenTelemetry** | errors/traces |
| AI tracing | **LangSmith** | LangGraph/model debugging/evaluation |
| Infrastructure | **Docker** | consistent deployment |
| Backend hosting | AWS / DigitalOcean initially | APIs/workers |
| DB hosting | Supabase / Neon / AWS RDS | managed Postgres |
| Secrets | Cloud secret manager | GST/API credentials |
| CI/CD | GitHub Actions | builds/tests/deployment |
| Mobile distribution | App Store + Play Store | customer app |
| Desktop distribution | electron-builder | `.exe`, `.dmg` |
| Optional automation | **n8n** | external integrations only |

### The AI portion

I would lock this in as:

**Sarvam Vision 1.5 → deterministic validation → optional LLM reasoning**

rather than:

**OCR → Llama everywhere.**

Sarvam's current Document AI exposes two useful modes:

- `Digitise` = complete OCR/layout/table extraction.
- `Extract` = you define a schema and it returns those fields directly.

For invoices, `Extract` is exactly what you want. citeturn551008search0

Your schema might contain:

```text
invoice_number
invoice_date

seller_name
seller_gstin
seller_address
seller_state

buyer_name
buyer_gstin
buyer_address
buyer_state

items\[\]
 description
 hsn_sac
 quantity
 unit_price
 taxable_value
 gst_rate
 cgst
 sgst
 igst

subtotal
discount
taxable_total

cgst_total
sgst_total
igst_total

round_off
invoice_total

currency
```

And additionally store per-field:

```text
value
confidence
source
manually_verified
```

That last part becomes extremely important.

## Do **not** trust OCR directly

This is the core architecture I'd use:

```text
 ┌─────────────────┐
 │ Receipt/Invoice │
 └────────┬────────┘
 ↓
 Image preprocessing
 ↓
 Sarvam Vision 1.5
 ↓
 Structured JSON
 ↓
 ┌───────────────────────┐
 │ Deterministic Validator│
 └───────────┬───────────┘
 ↓
 ┌──────── confidence ≥ threshold? ────────┐
 │ │
 YES NO
 │ │
 ↓ ↓
 Auto-accept fields Human Review UI
 │ │
 └────────────────┬────────────────────────┘
 ↓
 GST Ledger Database
 ↓
 Reconciliation Engine
 ↓
 Tax Summary
 ↓
 Human Approval
 ↓
 GST filing/API
```

The LLM should **never be the final authority on GST calculations**.

For example:

```text
taxable_value × GST rate
```

and

```text
CGST + SGST
vs
IGST
```

should be checked in normal Python code.

Similarly:

- GSTIN format
- state code
- invoice dates
- duplicate invoices
- totals
- tax arithmetic
- HSN/SAC validity
- seller/buyer matching

should largely be deterministic.

That makes the system much more defensible.

---

# Why Sarvam rather than fine-tuning Llama

Sarvam Vision currently supports document processing across **23 languages: all 22 constitutionally recognized Indian languages plus English**. That matters significantly for invoices from small Indian vendors where you may see Marathi, Hindi, Gujarati, Tamil, regional scripts, English and mixed text. citeturn551008search0turn551008search5

So for v1:

> **Do not fine-tune anything.**

You have no proprietary training dataset yet.

You don't know where OCR failures will actually occur.

You don't know which invoice layouts dominate.

And fine-tuning a chat model doesn't magically give you a great OCR model.

Instead, start collecting:

```text
original_document
OCR_output
corrected_output
OCR_confidence
document_language
vendor
document_type
errors
human_corrections
```

After you have maybe tens of thousands of labelled/corrected invoices, **then evaluate whether fine-tuning a model actually provides economic value**.

That dataset could eventually become one of your strongest assets.

---

# Where Llama/Ollama fits

I would **keep an abstraction for it but not put it in production path initially.**

Possible future architecture:

```text
AIProvider interface

├── SarvamProvider
├── OpenAIProvider
├── AnthropicProvider
└── LocalModelProvider
 └── Ollama
 └── Llama/Qwen/etc.
```

Ollama becomes useful later for companies saying:

> "We cannot send invoices outside our network."

Then you can offer:

```text
Cloud version
Sarvam API

Enterprise version
self-hosted OCR + local LLM
```

That's a legitimate enterprise feature.

But don't burden MVP development with it.

---

# LangChain vs LangGraph

Use both, but **LangGraph matters more here**.

LangGraph's current positioning is specifically around stateful, durable execution and human-in-the-loop workflows. citeturn551008search2

Your workflow naturally resembles a graph:

```text
INGEST
 ↓
CLASSIFY
 ↓
OCR
 ↓
EXTRACT
 ↓
VALIDATE
 ↓
confidence check
 ↓
 ┌──────────────┐
 │ │
 ↓ ↓
AUTO REVIEW
 │ │
 └───────┬──────┘
 ↓
RECONCILE
 ↓
GST PREPARATION
 ↓
HUMAN APPROVAL
 ↓
FILE / EXPORT
```

And occasionally:

```text
OCR FAILED
 ↓
retry
 ↓
alternate extraction
 ↓
manual review
```

That's where LangGraph makes sense.

### LangChain

Use LangChain only for things like:

```python
model.invoke()
structured_output()
tool bindings
prompt templates
```

Don't let your entire codebase become LangChain abstractions.

A clean architecture should instead look like:

```text
services/
 ocr/
 extraction/
 gst/
 reconciliation/
 ai/

workflows/
 invoice_processing.py
```

LangGraph orchestrates services.

It does not contain all business logic.

This prevents exactly the kind of spaghetti architecture that becomes painful later.

---

# Where n8n should sit

I would **absolutely use n8n**, but outside your core system.

Think:

```text
 YOUR CORE PRODUCT
 │
 ┌───────────┴───────────┐
 │ │
 FastAPI n8n
 │ │
 core GST engine integrations
```

n8n is excellent for:

```text
Gmail invoice attachment
 ↓
download PDF
 ↓
POST /api/invoices
```

or:

```text
Outlook
 ↓
invoice attachment
 ↓
your API
```

or:

```text
Slack
 ↓
uploaded receipt
 ↓
your API
```

or:

```text
Invoice approved
 ↓
Google Sheets
```

Sarvam itself has now published an n8n integration, so there is real compatibility there. citeturn551008search7

But I would **not** implement:

```text
OCR
→ GST calculations
→ invoice validation
→ accounting
→ filing
```

inside a giant n8n workflow.

Once you have hundreds of users and thousands of invoices:

💀

Keep n8n as your **connector layer**.

---

# Mobile architecture

I agree with your split.

## React Native

The mobile app becomes the primary capture device.

```text
React Native
│
├── Camera
│ ├── receipt capture
│ ├── multi-page invoice
│ ├── edge detection
│ └── crop/rotate
│
├── Gallery
│ └── existing images
│
├── File picker
│ ├── PDF
│ ├── JPG
│ └── PNG
│
├── Share Sheet
│
├── Invoice review
│
├── Corrections
│
├── Dashboard
│
└── GST summaries
```

React Native's New Architecture is already enabled by default in current releases, so it's a sensible long-lived choice rather than maintaining separate Swift/Kotlin apps. citeturn551008search6

A useful mobile feature would be:

```text
WhatsApp/email receipt
→ Share
→ Your App
→ Import invoice
```

This is important because a lot of Indian SMB invoice traffic is not coming through a neat ERP integration.

---

# Electron desktop

The desktop app should focus differently:

```text
Electron
│
├── Drag/drop invoice
├── Import PDF
├── Import Excel/CSV
├── Bulk invoice upload
├── Email integration
├── Invoice review
├── GST dashboard
├── Reconciliation
├── Reports
└── Filing approval
```

Correct: **do not build a desktop camera flow.**

It's a pointless feature for most desktop users.

Mobile:

> capture physical documents.

Desktop:

> process, reconcile and manage documents.

That's a clean product boundary.

---

# Digital receipts

You should support digital invoices through several ingestion paths.

```text
 Invoice Sources

 ┌──────────────┬──────────────┐
 │ │ │
 Physical Files SaaS
 │ │ │
 Camera PDF/JPG/XML Gmail
 Gallery CSV/XLSX Outlook
 Google Drive
 Slack
 WhatsApp*
```

WhatsApp deserves special consideration later because API access and user data flows are more constrained than email.

For MVP:

```text
Mobile upload
Desktop upload
Gmail integration
```

would be enough.

---

# PostgreSQL data model

I would use Postgres rather than MongoDB.

You have highly relational financial/compliance data.

Core entities:

```text
organizations
users
organization_members

gst_profiles
vendors
customers

documents
document_pages

invoices
invoice_items
invoice_taxes

ocr_runs
extraction_runs

field_corrections

ledger_entries
gst_periods

reconciliations
filing_drafts
filing_attempts

integrations
audit_logs
```

For example:

```text
Organization
 │
 ├── GSTIN
 │
 ├── invoices
 │ └── invoice_items
 │
 ├── filing_periods
 │
 └── users
```

Use normal relational columns for financial fields.

Use `JSONB` only where variability is useful:

```text
raw_ocr
model_metadata
provider_response
```

Don't dump your entire application into JSONB.

---

# Storage

Original invoices should never live directly inside Postgres.

Use:

**S3 / Cloudflare R2 / MinIO-compatible storage.**

Structure:

```text
organization/
 2026/
 09/
 invoice_uuid/
 original.pdf
 page-001.webp
 thumbnail.webp
```

Then PostgreSQL stores:

```text
storage_key
hash
mime_type
size
```

Calculate a SHA-256 hash.

That also helps detect duplicate invoice uploads.

---

# Security should be designed now

Because you're dealing with:

- GSTINs
- supplier/customer information
- invoice amounts
- company expenditure
- potentially bank/account information

build proper tenancy.

Every table should effectively be scoped by:

```text
organization_id
```

And preferably enforce separation with PostgreSQL Row Level Security or extremely strict backend authorization.

Also store a full audit trail:

```text
OCR extracted ₹12,450
 ↓
Utkarsh changed it to ₹12,540
 ↓
approved by Accountant X
 ↓
included in filing period August 2026
```

Never just overwrite the value.

For compliance software, auditability is a product feature.

---

# GST engine

This should be your own Python module.

Something like:

```text
gst_engine/
│
├── validators/
│ ├── gstin.py
│ ├── invoice.py
│ ├── tax_amounts.py
│ ├── hsn.py
│ └── place_of_supply.py
│
├── reconciliation/
│
├── calculations/
│
├── returns/
│ ├── gstr1.py
│ ├── gstr3b.py
│ └── ...
│
└── rules/
```

Important architectural principle:

> **GST rules belong in version-controlled code/rules, not prompts.**

GST requirements change.

For example, the current IRP documentation includes changes made in 2025–2026 such as a 40% GST rate and altered RSP invoice validations. citeturn229814search0turn229814search2

So make your rules version-aware:

```text
rules/
 2026-02-01.json
 2026-04-01.json
 ...
```

or Python rule modules.

That makes regulatory changes manageable.

---

# Filing itself

There is an important distinction:

> **OCR + preparation** is easy relative to **actual GST submission integration**.

Don't build your MVP around automating GST Portal UI.

Instead, build:

```text
documents
 ↓
extraction
 ↓
validation
 ↓
reconciliation
 ↓
GSTR preparation
 ↓
human approval
 ↓
export
```

Then integrate an authorized provider/API.

GST/e-invoicing infrastructure supports API-based integrations and solution-provider flows, including taxpayer authorization. Current IRP documentation also exposes onboarding, consent, authentication, IRN generation and related APIs. citeturn229814search0turn229814search3turn229814search4

Eventually:

```text
Your product
 ↓
GSP / ASP / IRP integration
 ↓
GST ecosystem
```

rather than browser automation.

---

# Human-in-the-loop

This should become one of your key differentiators.

Don't market it as:

> AI files GST automatically.

Build:

> AI does the tedious 90%; the accountant verifies the important 10%.

For every invoice:

```text
✓ Vendor GSTIN 99%
✓ Invoice no. 98%
✓ Invoice date 99%
✓ Taxable value 97%
⚠ HSN 998313 71%
⚠ IGST ₹1,240 arithmetic mismatch
```

Then:

```text
\[Approve\]
\[Edit\]
\[Reject\]
```

You can even give the reviewer the source crop next to each extracted field.

That is excellent UX.

---

# Where the "agent" actually helps

Don't build an autonomous **GST Agent™** just because agents are trendy.

Use agentic reasoning for ambiguous cases.

Example:

```text
Invoice extracted
 ↓
Validator detects:
Seller Maharashtra
Buyer Maharashtra
but IGST charged
 ↓
Agent gathers:
invoice fields
place-of-supply
GST rules
historical vendor behavior
 ↓
"Possible tax classification mismatch"
 ↓
Human review
```

Similarly:

```text
"Why isn't this invoice included in August GSTR-3B?"

"₹18,400 ITC is pending because six invoices have GSTIN/tax
mismatches."

"Show invoices where OCR confidence <80%."

"Why did GST payable increase this month?"
```

That's where an LLM is genuinely useful.

---

# Do you need RAG?

Eventually **yes**, but not for OCR.

RAG could cover:

```text
GST circulars
notifications
rules
company-specific policies
help documentation
accounting SOPs
```

Architecture:

```text
official GST documents
 ↓
parser
 ↓
chunking
 ↓
embeddings
 ↓
pgvector
```

Since you're already using PostgreSQL, I would start with:

**Postgres + pgvector**

rather than introducing Qdrant immediately.

Then your assistant can answer:

> Why was this invoice flagged?

using:

```text
invoice context
+
relevant GST rule
+
company policy
```

with citations.

---

# Monorepo

I would strongly recommend a monorepo.

```text
gst-platform/
│
├── apps/
│ ├── mobile/
│ │ └── React Native
│ │
│ ├── desktop/
│ │ └── Electron + React
│ │
│ └── web/
│ └── optional later
│
├── backend/
│ ├── api/
│ │ └── FastAPI
│ │
│ ├── workers/
│ │
│ ├── workflows/
│ │ └── LangGraph
│ │
│ ├── services/
│ │ ├── ocr/
│ │ ├── gst/
│ │ ├── ai/
│ │ ├── integrations/
│ │ └── reconciliation/
│ │
│ └── db/
│
├── packages/
│ ├── api-types/
│ ├── validation/
│ ├── design-tokens/
│ └── shared-types/
│
├── integrations/
│ └── n8n/
│
├── infrastructure/
│ ├── docker/
│ └── terraform/
│
└── docs/
```

That gives you one stable architecture that can grow without needing a rewrite.

---

# Final locked stack

I would commit to this:

```text
CLIENTS
────────────────────────────────

Mobile
React Native + TypeScript
iOS + Android
Camera + Files + Share Sheet

Desktop
Electron + React + TypeScript
Windows + macOS

BACKEND
────────────────────────────────

Python 3.13+
FastAPI
Pydantic
SQLAlchemy
Alembic

PostgreSQL
pgvector

Redis
Celery/Dramatiq

S3/R2 object storage

AI
────────────────────────────────

Sarvam Vision 1.5
 │
 ↓
Structured extraction
 │
 ↓
Python GST validation
 │
 ↓
LangGraph workflow
 │
 ↓
Sarvam-105B / other LLM only when reasoning is required

LangChain:
model/tool abstraction only

LangSmith:
tracing/evaluation

NO fine-tuning initially
NO Ollama initially

AUTOMATION
────────────────────────────────

n8n

Gmail
Outlook
Slack
Google Drive
Google Sheets
ERP/webhooks

n8n → FastAPI
NOT n8n → GST business logic

COMPLIANCE
────────────────────────────────

Custom GST rule engine
Human approval
Audit logs
Versioned GST rules
GSP/IRP/API integration later

INFRA
────────────────────────────────

Docker
GitHub Actions
AWS / DigitalOcean
Cloudflare
Sentry
OpenTelemetry
```

## And the most important architectural decision

Your product shouldn't conceptually be:

> **OCR → AI → GST filing**

It should be:

> **Capture → Extract → Validate → Reconcile → Review → Prepare → Approve → File**

AI participates in that pipeline, but **AI isn't the pipeline**.

That distinction will make this significantly more reliable, easier to build, easier to explain to investors/hackathon judges, and much easier to expand from "receipt scanner" into an actual **AI-assisted accounting/GST operations platform**. citeturn551008search0turn551008search2turn229814search0

## User

@Firecrawl find similar repo to https://github.com/karanb192/itr-wala but this is for itr not gst we need gst, or can this be used for gst too?

## Assistant

I’ll check the ITR-Wala repo itself first, then search GitHub for GST-focused equivalents and compare whether its architecture can be reused for GST or only as a reference.

## Assistant

I found a few genuinely GST-specific repos. The closest ones split into two groups: **invoice/OCR extraction** and **GST return preparation/filing utilities**—which is useful because your product needs both, while ITR-Wala itself only gives us the architectural pattern.

## Assistant

Worked for 51s

## Assistant

Yes — I found something much closer to your GST idea than `itr-wala`.

### Best match: Hisaabo

**Repo:** https://github.com/hisaabo/hisaabo

This is currently the most relevant open-source repo I found for what you're trying to build. It describes itself as an **agent-native financial operating system for India**, and it already has substantial GST functionality, including:

- GSTR-1 generation
- GSTR-3B generation
- GSTR-9
- GSTR-2B reconciliation
- CGST/SGST/IGST determination
- GSTIN validation
- HSN validation
- ITC tracking
- reverse-charge handling
- e-invoicing / IRN support
- e-way bills
- mobile app
- desktop app
- multi-tenant businesses
- audit trails
- MCP/AI-agent interface

Its architecture is also surprisingly close to what we were discussing:

```text
Web Mobile Desktop CLI MCP
 | | | | |
 └───────────┴─────────────┴───────────┴─────────┘
 ↓
 Typed API
 ↓
 GST/accounting
 rule engine
 ↓
 PostgreSQL
```

Their mobile client uses **Expo/React Native**, desktop uses **Tauri**, and everything talks to the same backend API. fileciteturn1file0

There is one particularly interesting detail for **our project**:

> **Invoice photo/PDF OCR is on Hisaabo's roadmap, not yet the core implemented workflow.**

They explicitly list:

```text
PDF invoice OCR
→ Photograph a purchase bill
→ extract line items
→ HSN codes
→ amounts
```

as an upcoming capability. fileciteturn1file0

That means your idea is actually sitting at an interesting intersection:

```text
 Hisaabo
 GST/accounting engine
 +
 your OCR layer
 +
 better mobile capture
 +
 AI validation/review
```

## Other useful GST repos I found

These aren't as complete as Hisaabo, but they're useful references for individual pieces.

| Repo | Useful for |
|---|---|
| **IamRamgarhia/Free-GST-Billing-Software** | GSTR-1 JSON generation, GSTR-3B preparation |
| **bhuvannarula/offlineGST** | Offline GSTR-1 invoice → GST JSON |
| **tks18/gstr-json-2-excel** | GSTR-1 / GSTR-2A JSON processing |
| **salilbh/GST-Returns-Automation---GSTR-3B** | GSTR-3B automation |
| **ayush2635/Invoiscope** | GST invoice OCR/extraction |
| **EFFICIENTCORPORATES/efffcorp-gst** | GSTIN utilities |
| **RithikBanerjee/open-source-.net-sdk** | GST return-filing API SDK |

The Firecrawl search specifically surfaced `Invoiscope` as an **“Intelligent GST Invoice Information Extractor”** using OCR/object detection, while the filing-oriented repos cover the downstream GST return side. fileciteturn2file0

So there isn't one obvious repo with exactly:

```text
mobile receipt camera
+
multilingual OCR
+
invoice extraction
+
human correction
+
GST reconciliation
+
GSTR preparation
+
AI assistant
+
desktop app
```

which is actually good for us.

---

# Can we just use ITR-Wala for GST?

### Not directly.

Do **not** fork `itr-wala`, rename variables from `income_tax` to `gst`, and build on top of it.

ITR and GST have fundamentally different domains.

`itr-wala` is built around:

```text
Form 16
AIS
26AS
salary
capital gains
deductions
income-tax slabs
87A
surcharge
cess
ITR-1/2/3/4
```

GST requires:

```text
sale invoices
purchase invoices
GSTIN
HSN/SAC
place of supply

CGST
SGST
IGST

B2B
B2C
credit notes
debit notes

ITC
RCM
GSTR-1
GSTR-3B
GSTR-2B
reconciliation
```

So its **tax engine itself is almost useless for GST**.

But there's something much more valuable in ITR-Wala.

## Steal the architecture philosophy

This part of ITR-Wala is excellent.

It explicitly separates:

```text
AI
↓
document reading
information extraction
interviewing
explanation
```

from:

```text
Python
↓
tax calculations
validation
cross-checking
rules
```

Its README basically argues:

> Never let the LLM calculate legally important tax values.

And it backs the deterministic engine with golden tests, schema validation, cross-document checks and fuzz tests. fileciteturn1file0

That is **exactly the philosophy we should copy**.

For our GST application:

```text
 AI / OCR
 │
 │ extracts
 ↓
 ┌─────────────────────┐
 │ Structured Invoice │
 └──────────┬──────────┘
 ↓
 GST Rule Engine
 ↓
 deterministic Python

GSTIN validation
CGST/SGST/IGST
tax calculations
place-of-supply
invoice classification
ITC eligibility
GSTR grouping
reconciliation
```

So:

> **Don't reuse ITR-Wala's tax code. Reuse its engineering philosophy.**

---

# Hisaabo changes my recommendation slightly

After seeing this repo, I would use **three open-source projects as references**, not build blindly from scratch:

```text
 OUR GST PLATFORM

 ┌─────────────┐
 │ React Native│
 │ Camera App │
 └──────┬──────┘
 │
 ↓
 Sarvam Vision OCR
 │
 ↓
 Invoice Schema
 │
 ┌────────────┴────────────┐
 ↓ ↓
 Human Review GST Rule Engine
 │
 ↓
 Reconciliation
 │
 ↓
 GSTR-1 / GSTR-3B prep
```

Reference code:

```text
Hisaabo
 ↓
GST engine
accounting model
GSTR logic
ITC
multi-tenancy
audit architecture

ITR-Wala
 ↓
deterministic-engine philosophy
validation philosophy
golden tests
LLM boundary

Invoiscope
 ↓
invoice/OCR ideas
```

Then **Sarvam Vision replaces the old-school OCR stack** in Invoiscope.

---

# One important Hisaabo limitation

There is a licensing issue you need to be aware of.

Hisaabo isn't MIT.

Its README says it uses the **O'Saasy License**, and specifically states that you may use/self-host/modify it but **cannot offer Hisaabo itself as a competing hosted service**. fileciteturn1file0

That's extremely important because **you want to build a SaaS**.

Therefore I would **not fork Hisaabo and turn it into your SaaS** without carefully reviewing the license/legal implications.

Instead:

### Use it as a reference implementation.

Read:

```text
packages/api
packages/shared
GST modules
invoice calculations
GSTR generators
reconciliation models
database schemas
tests
```

Understand how they model the GST domain.

Then independently implement our architecture.

By contrast, `itr-wala` is **MIT licensed**, which is much more permissive. fileciteturn1file0

---

# And I think our product direction is clearer now

Hisaabo is essentially:

> **Accounting system → GST**

Your product should be:

> **Documents → accounting/GST**

That's an important differentiation.

Hisaabo expects something closer to:

```text
User creates transaction
↓
accounting record exists
↓
GSTR generated
```

Our system:

```text
User photographs random shop receipt
 OR
drops PDF invoice
 OR
email attachment arrives
 ↓

 OCR

 ↓

"Shree Ganesh Traders"
GSTIN 27XXXXXXXX...
Invoice 8271
₹12,430
CGST ₹...
SGST ₹...

 ↓

AI understands document
 ↓
deterministic GST validation
 ↓
human fixes questionable fields
 ↓
transaction automatically created
 ↓
monthly reconciliation
 ↓
GSTR preparation
```

That is a much better wedge.

You don't need to convince an SME:

> "Replace Tally with us."

Instead:

> **"Send us all the bills you already receive. We'll turn them into filing-ready GST records."**

Then later you expand:

```text
Receipt OCR
 ↓
GST assistant
 ↓
Bookkeeping
 ↓
Reconciliation
 ↓
Accounting
 ↓
Compliance OS
```

That is the direction I'd lock in.

## User

ad this context of ocr-gst to ur memory for long term usage:

# Project Context — GST Operations Copilot

We are building a real product, not just a hackathon demo.

## 1. Product Vision

Build a human-in-the-loop GST Operations Copilot for Indian businesses that reduces the repetitive operational work involved in turning scattered invoices and receipts into clean, validated, GST-ready structured data.

The fundamental problem:

Businesses receive invoices/receipts from many different sources:

- Physical receipts/invoices
- Photos/scans of physical documents
- PDFs
- Digital invoices
- Email attachments
- Slack or other communication platforms
- Files uploaded manually
- Eventually other integrations used by businesses

Today, someone often has to:

Collect documents
→ open/read them
→ manually extract information
→ enter it into Excel/Google Sheets/accounting software/databases
→ verify the entries
→ find duplicates/errors
→ reconcile discrepancies
→ prepare the month's data for GST compliance/filing.

We want to reduce this friction.

Target workflow:

INGEST
→ OCR / DOCUMENT UNDERSTANDING
→ STRUCTURE
→ VALIDATE
→ DETECT EXCEPTIONS
→ HUMAN REVIEW
→ APPROVE
→ EXPORT / SYNC
→ GST-READY DATA

The key principle is:

AI handles repetitive operational work.
Humans remain responsible for important financial/tax decisions.

This is NOT intended to blindly or autonomously file GST.

---

# 2. Core Product Principle: Human in the Loop

Do not design this as:

"Upload invoice → AI automatically files GST."

Instead:

"Upload/ingest invoice → system extracts and validates → uncertain/problematic cases are surfaced → human reviews/edits/approves → verified data becomes GST-ready."

Every important extracted field should be editable before final approval.

Low-confidence or suspicious documents should NEVER silently flow through the system.

The application should make uncertainty visible.

---

# 3. Primary Users

Initial users could include:

- SMEs
- Retail businesses
- Manufacturing businesses
- Finance teams
- Accountants/bookkeepers
- GST/compliance operators

The product should eventually support organizations with multiple users and roles.

For the initial implementation, keep this simple.

---

# 4. Document Sources

## MVP

Start with direct uploads.

Support:

- Images of physical receipts/invoices
- Camera-captured receipts
- PDF invoices
- Digital invoice files

Mobile is especially important because physical receipts can be photographed directly.

## Future ingestion sources

The architecture should allow adapters/connectors for:

- Gmail/email
- Google Drive
- Slack
- other communication platforms
- accounting systems
- APIs
- bulk uploads

Do NOT implement every integration immediately.

Design a clean ingestion abstraction so additional sources can be added later without rewriting the processing pipeline.

---

# 5. Applications

The long-term product should support:

## Mobile

React Native application targeting:

- Android
- iOS

Mobile should support:

- Camera capture
- Gallery/file upload
- PDF upload
- Receipt/invoice review
- Exception resolution
- Dashboard

Physical receipt capture belongs primarily here.

## Desktop

Electron application targeting:

- Windows
- macOS

Desktop does NOT need camera capture.

It should support:

- file upload
- PDFs
- downloaded digital invoices
- review workflows
- bulk operations
- dashboards
- exports/integrations

We may also have a web application/dashboard if appropriate.

Do not duplicate business logic between clients.

All important processing should live behind backend APIs.

---

# 6. OCR / Document Intelligence

Documents need to be converted into structured invoice/receipt data.

We need to handle Indian invoices and receipts, potentially containing:

- English
- Hindi
- Marathi
- other Indian languages
- mixed-language documents

The OCR/document extraction layer should therefore be provider-independent.

Do NOT tightly couple the application to one OCR vendor/model.

Create a clear interface such as:

DocumentExtractor

which can have implementations/adapters for different OCR/document intelligence providers.

We may evaluate multilingual OCR APIs such as Sarvam or other capable document models.

Do not introduce local LLM fine-tuning unless there is evidence that it is necessary.

Fine-tuning is NOT an MVP requirement.

---

# 7. Important Fields to Extract

The normalized invoice schema should be capable of representing fields such as:

Document metadata:
- document ID
- source
- original filename
- document type
- upload timestamp

Invoice information:
- invoice number
- invoice date
- vendor/supplier name
- vendor GSTIN
- buyer name
- buyer GSTIN
- place of supply

Financial information:
- subtotal/taxable value
- CGST
- SGST
- IGST
- cess if applicable
- discounts if present
- total invoice amount
- currency

Line items where available:
- description
- quantity
- unit price
- HSN/SAC
- taxable value
- tax rate
- tax amount

Extraction metadata:
- OCR confidence
- field-level confidence where possible
- raw OCR/document output
- extractor/provider
- processing status

Do not assume every receipt contains every field.

Fields must support missing/unknown states.

---

# 8. Normalized Data Model

OCR provider output must NEVER become our application data model directly.

Pipeline:

Raw document
→ OCR provider response
→ normalization layer
→ canonical Invoice schema
→ validation
→ exception generation
→ human review
→ approved record

This separation is important because OCR providers may change later.

Use strongly typed schemas and explicit contracts.

---

# 9. Validation Layer

OCR is only extraction.

After extraction, validate the resulting data.

Examples:

- GSTIN format validation
- invoice number presence
- invoice date validity
- arithmetic consistency
- subtotal + taxes ≈ total
- CGST/SGST consistency
- IGST consistency
- tax percentage calculations
- missing mandatory fields
- malformed monetary values
- duplicated invoice numbers
- potential duplicate documents
- suspicious OCR output

Validation rules should be deterministic wherever possible.

Do NOT use an LLM for something that can be reliably validated with normal code.

AI should complement deterministic validation, not replace it.

---

# 10. Exception Engine

Instead of treating every issue as a generic "OCR failed" error, create structured exceptions.

Examples:

MISSING_GSTIN
INVALID_GSTIN
LOW_OCR_CONFIDENCE
MISSING_INVOICE_NUMBER
DUPLICATE_INVOICE
TOTAL_MISMATCH
TAX_MISMATCH
UNREADABLE_DOCUMENT
MISSING_DATE
AMBIGUOUS_FIELD

Each exception should contain:

- type
- severity
- affected field(s)
- explanation
- suggested action where appropriate
- resolution status

This becomes the core of the human review experience.

---

# 11. Human Review Workflow

Documents should have explicit states.

Example:

UPLOADED
→ PROCESSING
→ NEEDS_REVIEW
→ APPROVED
→ EXPORTED

And failure states where necessary.

A reviewer should be able to:

- see the original document
- see extracted fields
- see confidence/validation warnings
- edit incorrect fields
- resolve exceptions
- approve the document
- reject/delete invalid documents

Maintain an audit trail.

For important changes record:

- original value
- edited value
- user
- timestamp
- reason/action where appropriate

Financial workflows need traceability.

---

# 12. Duplicate Detection

Duplicate receipts are a realistic problem.

Use multiple signals rather than filename alone.

Potential signals:

- file hash
- perceptual/image similarity where useful
- GSTIN
- invoice number
- invoice date
- amount
- vendor

Initially implement simple reliable duplicate detection.

Do not overengineer ML-based similarity unless necessary.

---

# 13. Storage

We need to distinguish:

1. Original documents
2. Raw OCR results
3. Normalized structured records
4. Validated/approved records
5. Audit history

Do not put everything into one giant database table.

Use object storage for uploaded files and a relational database for application/financial metadata.

Preserve the original document for auditing/review.

---

# 14. Output / Integrations

Once records are approved, businesses should be able to use the data in their existing workflow.

MVP:

- CSV export
- Excel export

Future:

- Google Sheets
- databases
- accounting systems
- ERP integrations
- APIs/webhooks

Build exports around the canonical internal schema rather than OCR-specific output.

---

# 15. GST Filing Boundary

This is important.

The initial product should create:

GST-READY / FILING-READY DATA

rather than automatically submitting tax returns without human oversight.

Future GST portal/API integration can be investigated separately.

Any actual filing operation must require explicit human confirmation and appropriate compliance/security controls.

Never fabricate tax rules or assume regulatory behavior.

Keep GST-specific business rules isolated so they can be tested and updated as regulations change.

---

# 16. AI / Agent Architecture

Do not add AI frameworks simply because this is an AI product.

LangChain, LangGraph, n8n, LlamaIndex, local LLMs, fine-tuning, agents, etc. should only be introduced when they solve a concrete requirement.

For the core document pipeline, prefer straightforward application code:

Upload
→ Queue
→ OCR
→ Normalize
→ Validate
→ Generate exceptions
→ Persist
→ Review

If we later introduce workflows requiring stateful AI orchestration, LangGraph can be evaluated.

If simple external business automations/integrations become necessary, n8n can be evaluated.

Neither should become the core architecture by default.

Avoid framework-driven architecture.

---

# 17. Reliability

Document processing should be asynchronous.

Uploading a document should not require the client to keep an HTTP request open while OCR completes.

Think in terms of jobs.

Example:

POST document
→ document stored
→ processing job created
→ worker processes OCR
→ normalized data stored
→ validation executed
→ status updated
→ client receives/polls status

Processing must support:

- retries
- idempotency
- provider timeouts
- malformed documents
- partial OCR responses
- provider outages
- duplicate submissions

Never create duplicate financial records because a job was retried.

---

# 18. Security

Invoices contain sensitive business/financial information.

Treat security as a first-class requirement.

At minimum consider:

- authentication
- authorization
- organization-level data isolation
- secure object storage
- encrypted transport
- secrets management
- audit logs
- minimal retention of unnecessary OCR/provider data
- signed/private document URLs
- safe file validation
- upload size limits
- MIME/type validation

Never expose original documents publicly.

---

# 19. UX Philosophy

The UI should NOT look like a generic AI dashboard.

Avoid:

- excessive gradients
- glowing AI elements
- meaningless AI animations
- giant chatbot interfaces
- clutter

The product is an operations tool.

Design should feel:

- professional
- calm
- trustworthy
- fast
- financial/business oriented
- information dense where appropriate
- easy to audit

AI should mostly work behind the scenes.

The main UX should revolve around:

Dashboard
Documents
Review Queue
Approved Records
Exceptions
Exports
Integrations

One of the most important screens will likely be the review interface:

Original invoice on one side
+
Structured extracted fields on the other
+
Clearly highlighted exceptions/confidence issues.

---

# 20. MVP

Do NOT attempt the entire vision immediately.

A strong first vertical slice is:

1. User authentication
2. Upload receipt/invoice image or PDF
3. Store original securely
4. Send document through OCR/document extractor
5. Normalize result into canonical schema
6. Run deterministic validations
7. Generate structured exceptions
8. Show document + extracted data in review UI
9. Allow human corrections
10. Approve record
11. Store audit history
12. Export approved records as CSV/Excel

That gives us the complete core loop:

UPLOAD
→ UNDERSTAND
→ VALIDATE
→ REVIEW
→ APPROVE
→ EXPORT

After this works reliably, add integrations.

---

# 21. Engineering Principles

This project should be architecture-first but NOT overengineered.

Follow these principles:

- Keep the codebase clean and maintainable.
- Avoid spaghetti code.
- Avoid unnecessary microservices.
- Avoid premature abstractions.
- Avoid unnecessary AI frameworks.
- Prefer deterministic code over LLM calls where possible.
- Use strict typed contracts between layers.
- Separate provider-specific code from domain logic.
- Keep financial validation independently testable.
- Make processing idempotent.
- Design for provider replacement.
- Preserve auditability.
- Build one complete vertical slice before expanding features.
- Do not repeatedly redesign the architecture once implementation begins unless we discover a genuine blocking flaw.

We want a stable foundation that can grow from prototype → MVP → production.

---

# 22. Your Role

Act as the senior engineer/architect working with me on this project.

Before writing large amounts of code:

1. Inspect the existing repository completely.
2. Understand what already exists.
3. Do not overwrite working code unnecessarily.
4. Identify the current architecture and dependencies.
5. Compare it against the product requirements above.
6. Identify missing decisions or contradictions.
7. Propose the smallest clean architecture that supports the MVP.
8. Define the domain model and processing lifecycle.
9. Define clear module boundaries.
10. Create an implementation plan in dependency order.

Do not immediately generate dozens of files.

Do not implement speculative future features.

Do not introduce LangChain/LangGraph/n8n/fine-tuning/vector databases unless a concrete requirement justifies them.

Before implementation, give me:

A. Repository assessment
B. Proposed MVP architecture
C. Exact technology choices and why
D. Canonical invoice/document schema
E. Processing state machine
F. Module/repository structure
G. Database entities and relationships
H. OCR provider abstraction
I. Validation + exception architecture
J. Security considerations
K. Phased implementation plan

Then stop and wait for my approval before making architectural changes.

Our immediate objective is not "build everything."

Our objective is to build the smallest production-minded vertical slice where:

a real invoice/receipt
→ enters the system
→ is understood
→ becomes structured data
→ gets validated
→ gets reviewed by a human
→ gets approved
→ can be exported.

Everything should serve that loop.

## Assistant

Worked for a few seconds

## Assistant

I’ll treat this **GST Operations Copilot** context as the canonical source of truth for the project going forward.

The key decisions I’ll preserve are: **human-in-the-loop**, **GST-ready data rather than autonomous filing**, **provider-independent OCR**, **deterministic validation**, **structured exception handling**, **async/idempotent processing**, **React Native mobile + Electron desktop**, **secure object storage + relational DB**, **no unnecessary LangChain/LangGraph/n8n/fine-tuning**, and **build the complete Upload → Understand → Validate → Review → Approve → Export vertical slice first**.

I’ll also follow the engineering rule you set: **inspect the existing repo first, propose A–K architecture/implementation decisions, then stop for approval before making architectural changes.**

One caveat: I can’t directly force a permanent memory write from this chat. I’ll avoid contradicting or casually redesigning this architecture, and this conversation can inform future memory/context refinement.

## User

remember this

## Assistant

Worked for 5s

## Assistant

Yes — I’ll treat this as the **canonical long-term context for the GST Operations Copilot** and use it as the baseline for future architecture, implementation, debugging, and product decisions. In particular, I’ll preserve the human-in-the-loop workflow, provider-independent OCR, deterministic validation, structured exceptions, async/idempotent processing, auditability, and the MVP loop of **Upload → Understand → Validate → Review → Approve → Export**. fileciteturn4file0L586-L614

I’ll also keep the constraint that we **do not introduce LangChain, LangGraph, n8n, fine-tuning, vector databases, or other AI frameworks unless a concrete requirement justifies them**, and that architecture should stay stable unless we find a genuine blocking flaw. fileciteturn4file0L618-L637

For future implementation work, I’ll also follow your A–K review process before making major architectural changes. fileciteturn4file0L643-L680

One product detail: ChatGPT’s Memory is created asynchronously rather than through a manual “save memory” command from the chat. You can review what’s retained under **Settings → Personalization → Memory summary**.

## User

the workflow should be: clients receipts is scaned by ocr, extract data-> llm identify structure with image and data from ocr-> uploads it in clients google sheets. this is the ocr pipeline/workflow then we will plan gst workflow. gst pipeline is not confirmed yet 

Worked for 44s

Understood. The confirmed first product is now:

```
Receipt image/PDF
→ OCR text extraction
→ LLM receives the receipt image + OCR output
→ LLM returns structured receipt data
→ system appends the structured row to the client’s Google Sheet
```

GST validation, review/approval flows, CSV/XLSX exports, and filing are deferred until the GST workflow is defined. The current `.context` files still describe the earlier GST-ready MVP, so they need to be revised once we lock these three decisions:

## Assistant

Worked for 16s

## Assistant

Got it. This supersedes the earlier “GST-ready MVP” as the **confirmed first workflow**.

For now, the product scope is strictly:

```text
Client receipt / invoice
 ↓
Image or PDF upload
 ↓
OCR extracts raw text/data
 ↓
LLM receives:
 • original image/document
 • OCR output
 ↓
LLM identifies the document structure
 ↓
LLM returns normalized structured data
 ↓
System writes/appends that data
to the client’s Google Sheet
```

So the architecture should now be designed around **OCR + multimodal LLM structuring + Google Sheets sync**.

The following are **not confirmed yet** and should be treated as deferred: GST validation rules, GST exception engine, GST filing workflow, GSTR preparation, approval/review mechanics for GST, reconciliation, and direct GST integrations.

This also means some earlier decisions change: **Google Sheets is now part of the first confirmed pipeline**, not merely a future integration, while the earlier Upload → Validate → Review → Approve → CSV/Excel flow is no longer the canonical MVP.

I’ll treat the project as having two separate layers from now on:

```text
PHASE 1 — CONFIRMED
Receipt ingestion
→ OCR
→ multimodal LLM structuring
→ Google Sheets

PHASE 2 — NOT YET CONFIRMED
Structured accounting data
→ GST processing / validation
→ GST workflow
→ compliance / filing preparation
```

That separation is important because we should first make the **document-to-structured-data pipeline reliable**, then design the GST pipeline on top of its output rather than mixing both prematurely. memcite

## User

does this has more than xlsx ?

## Assistant

Worked for 6s

## Assistant

Yes. **Hisaabo is much more than XLSX/Excel.** In fact, its core system is not spreadsheet-based at all.

It uses a structured accounting/GST backend with PostgreSQL, and supports several data/output paths:

- **CSV** exports for reports and invoices
- **JSON** through its CLI/API
- **Tally XML** export for import into Tally Prime
- **PDF** generation for GST-compliant invoices
- **GSTR-1 / GSTR-3B / GSTR-9** generation
- **GSTR-2B reconciliation**
- API/tRPC access for structured data
- MCP/CLI access for agents
- CSV bank-statement imports for multiple Indian banks citeturn360820search0

So conceptually it is:

```text
Structured financial database
 ↓
 API
 ↓
 ┌───────────────┐
 CSV JSON XML
 PDF GST data
```

not:

```text
Excel file
→ processing
→ Excel file
```

For **your current OCR pipeline**, this is relevant because you should also avoid making `.xlsx` the canonical storage format.

A cleaner design is:

```text
Receipt
→ OCR
→ LLM structuring
→ Canonical JSON
→ Database
→ Google Sheets sync
```

Then Google Sheets is only an **output/integration destination**, not the source of truth.

Later, the same structured record can feed:

```text
Google Sheets
CSV
XLSX
Tally
ERP
GST pipeline
API
```

That will be much easier to scale than building the data model around Excel.

## Assistant

Pick **1 — Managed intake tab**.

For your current OCR → LLM → Google Sheets pipeline, it is the cleanest MVP choice because you control the schema and can append rows reliably without asking every client to configure column mappings.

Use something like a dedicated tab named:

`Receipts_Intake`

with fixed columns such as:

```text
document_id
uploaded_at
vendor_name
vendor_gstin
invoice_number
invoice_date
subtotal
cgst
sgst
igst
total_amount
currency
source_file
ocr_confidence
processing_status
```

Why not the others yet:

- **Map existing columns** adds setup complexity, mapping UI, validation, and edge cases too early.
- **Create new spreadsheet** is okay, but less friendly if the client already has a bookkeeping spreadsheet they want to keep using.

So the best first behavior is:

```text
Client connects Google Sheet
→ system creates/uses one controlled tab
→ OCR pipeline appends standardized rows there
→ client's other tabs remain untouched
```

Later, once the pipeline is stable, add **option 2** as an advanced integration mode for businesses that already have established sheet layouts.

## User

https://github.com/hisaabo/hisaabo/blob/main/LICENSE can i sell this to my clients

## Assistant

Worked for 5s

## Assistant

Not safely as a hosted SaaS if what you sell is substantially similar to Hisaabo.

The license explicitly says you **may not use Hisaabo or a derivative work to offer a hosted or managed service that competes with Hisaabo as a commercial SaaS product**. It does allow personal/internal self-hosting, research, and building products that are **not substantially similar hosted services**. fileciteturn5file0L2-L2

So for your case:

- If you **fork Hisaabo and host it for clients** as your GST/accounting SaaS, that likely violates the non-compete clause.
- If you **sell an on-prem/self-hosted deployment** for a client’s own business use, the license text explicitly permits self-hosting, but you should still be careful about whether you are providing a managed service around it.
- If you **study Hisaabo and independently build your own OCR → structured data → Google Sheets product**, without copying substantial Hisaabo code, that is much safer.
- If your product later becomes a **GST/accounting SaaS substantially similar to Hisaabo**, you should not base it on Hisaabo code unless you get separate commercial permission from the copyright holder.

For your current product, I would use Hisaabo as an **architecture/reference repo only**, not as the codebase you commercialize.

This is a license interpretation, not legal advice. If you plan to sell to real clients, get a lawyer to review the exact deployment model before shipping.

## User

yes this is what i want to make fro gthe start

## Assistant

Worked for a few seconds

## Assistant

Then yes — **your end goal is a GST/accounting SaaS from day one**, not just an OCR utility.

That changes one important thing: **do not build on Hisaabo code**. Use it only as a reference for domain modeling, GST flows, auditability, and accounting concepts. Its license is risky for a competing hosted SaaS.

Your product should be its **own codebase and architecture**:

```text
Phase 1
Receipt / Invoice
→ OCR
→ Multimodal LLM structuring
→ Canonical JSON
→ Database
→ Google Sheets sync

Phase 2
Canonical financial data
→ GST validation
→ reconciliation
→ review / exceptions
→ GST-ready records

Phase 3
Accounting/GST SaaS
→ multi-client organizations
→ dashboards
→ ledgers
→ GSTR workflows
→ integrations
→ filing APIs later
```

So even though the **current confirmed workflow** is OCR → LLM → Sheets, we should design the data model and backend so it can grow into the GST/accounting SaaS without a rewrite.

The critical principle is:

> **Google Sheets is an output, not the database.**

Use:

```text
Receipt
 ↓
OCR
 ↓
LLM
 ↓
Canonical Invoice Record
 ↓
PostgreSQL
 ├── Google Sheets
 ├── CSV/XLSX
 ├── future GST engine
 └── future accounting workflows
```

This gives you a real product foundation instead of locking your business logic into spreadsheets.

And for Hisaabo specifically: **study it, don't fork it**. Reimplement the ideas you need independently.

## Assistant

Worked for a couple of seconds

## Assistant

Pick **1 — Header + line items**.

For your Phase 1, that is the right choice because your LLM is already identifying document structure. If a receipt or invoice has line items, you should capture them from day one rather than throw that information away and later redesign the schema.

A good rule is:

```text
Always capture header fields.
Capture line items when present.
Allow line items to be empty for simple receipts.
Never fabricate missing fields.
```

So the canonical shape should look roughly like:

```json
{
 "document_type": "invoice",
 "vendor_name": "...",
 "vendor_gstin": "...",
 "invoice_number": "...",
 "invoice_date": "...",
 "subtotal": 0,
 "cgst": 0,
 "sgst": 0,
 "igst": 0,
 "total": 0,
 "line_items": \[
 {
 "description": "...",
 "quantity": 1,
 "unit_price": 0,
 "hsn_sac": null,
 "tax_rate": null,
 "taxable_value": 0,
 "tax_amount": 0
 }
 \]
}
```

For a small receipt with no meaningful item breakdown:

```json
{
 "document_type": "receipt",
 "vendor_name": "...",
 "total": 540,
 "line_items": \[\]
}
```

The important part for Google Sheets is that **header data and line-item data should not be forced into one flat row model**.

I’d structure Sheets like this:

```text
Receipts_Intake
- document_id
- vendor
- invoice_number
- date
- subtotal
- cgst
- sgst
- igst
- total
- source
- status
```

and optionally:

```text
Receipt_Line_Items
- document_id
- line_no
- description
- quantity
- unit_price
- hsn_sac
- tax_rate
- taxable_value
- tax_amount
```

`document_id` links them.

That gives you a clean Phase 1 now and avoids a painful migration when GST processing eventually needs item-level HSN/SAC and tax data.

## Assistant

Worked for a couple of seconds

## Assistant

Choose **1 — Header + line items**.

That matches the product we are actually building:

```text
Receipt / invoice
→ OCR
→ LLM sees image + OCR output
→ extracts header fields
→ extracts line items when present
→ stores canonical structured data
→ syncs to Google Sheets
```

The important rule should be:

- Always extract header-level fields.
- Extract line items whenever the document contains them.
- Allow `line_items = \[\]` for receipts that do not provide useful item-level detail.
- Preserve missing/unknown fields as `null`; do not guess.
- Do not make GST-specific validation part of Phase 1 yet.

This gives us richer data now without committing to the GST workflow prematurely, and avoids having to redesign the schema later when item-level HSN/SAC, tax rates, quantities, etc. become useful.

## Assistant

Choose **1 — Two managed tabs**.

That fits the Phase 1 design best because you already decided to capture **header + line items**. The clean Google Sheets output should therefore be relational rather than trying to cram everything into one row.

Use:

```text
Invoice Register
- document_id
- source_file
- vendor_name
- vendor_gstin
- invoice_number
- invoice_date
- subtotal
- cgst
- sgst
- igst
- total_amount
- currency
- processed_at
- status
```

and:

```text
Line Items
- document_id
- line_no
- description
- quantity
- unit_price
- hsn_sac
- taxable_value
- tax_rate
- tax_amount
```

`document_id` links both tabs.

I would **not choose “Map client columns” for the first release**. That immediately creates per-client schema mapping, setup UI, validation, missing-column handling, renamed columns, incompatible layouts, and support overhead.

The best rollout is:

```text
v1
Two managed tabs with fixed schema

v1.x / later
Optional client column mapping

later
Custom accounting/ERP destinations
```

This also keeps your internal canonical schema independent of Google Sheets, which is important because Sheets should remain an output destination, not your system of record.

## User

this

## Assistant

Worked for a couple of seconds

## Assistant

By **“later: Custom accounting/ERP destinations”**, I mean that after Google Sheets works reliably, your approved structured invoice data should be able to sync directly into the accounting systems your clients already use.

Examples could include:

- **Tally Prime**
- **Zoho Books**
- **QuickBooks**
- **SAP**
- **Oracle NetSuite**
- **Odoo**
- custom client ERP/database systems
- generic **REST API / webhook** destinations

So the long-term output layer should look like:

```text
Canonical Invoice Data
 ↓
Destination Adapter
 ↓
 ┌───────────────┬──────────────┬─────────────┐
 Google Sheets Tally Zoho Books
 CSV/XLSX ERP API Webhook
```

The important design choice is: **do not write Tally-, Zoho-, or Sheets-specific logic inside the OCR pipeline.**

Instead, keep something like:

```text
destinations/
├── google_sheets/
├── csv/
├── xlsx/
├── tally/
├── zoho_books/
└── generic_webhook/
```

Each adapter converts the same canonical invoice object into the destination's required format.

For example:

```text
OCR + LLM
 ↓
Canonical Invoice
 ↓
GoogleSheetsDestination.write(invoice)
```

Later:

```text
TallyDestination.write(invoice)
ZohoBooksDestination.write(invoice)
ERPWebhookDestination.write(invoice)
```

This is why choosing **two managed Google Sheets tabs now** is still fine. Google Sheets is simply your **first destination adapter**, not something your whole product architecture depends on.

For your current MVP, though, I would implement **Google Sheets only** and leave the destination interface clean enough to add Tally/ERP later. That keeps the scope tight without creating a future rewrite.

## User

i want 3rd option

## Assistant

Then choose **3 — Map client columns**.

For what you want commercially, that actually makes sense: different clients will already have their own Google Sheet formats, and forcing everyone into your fixed two-tab schema can create friction.

The flow becomes:

```text
Client connects spreadsheet
→ your app reads the existing header columns
→ client maps your canonical fields to their columns
→ save that mapping per client
→ OCR + LLM produces canonical invoice data
→ sync layer transforms canonical fields using the saved mapping
→ append/update the client’s sheet
```

Example:

```text
Your canonical field Client column
vendor_name → Supplier
invoice_number → Bill No
invoice_date → Date
total_amount → Grand Total
vendor_gstin → GST Number
```

For line items, I would still keep a separate strategy. Either the client maps to a second sheet/tab for line items, or you initially support header-level mapping only and add line-item mapping next.

The important thing is to keep this distinction:

```text
OCR/LLM output
→ Canonical Invoice Schema
→ Client Mapping
→ Google Sheet
```

not:

```text
OCR/LLM
→ directly guess client sheet columns
```

That way each client can customize their sheet layout without corrupting your core data model.

So yes: **3 is the right choice if flexibility for real client onboarding is more important than the simplest MVP.**

## User

dose this plan sound good?

# Phase 1: Document Intelligence to Google Sheets

## Summary

Build an independent, single-user web product that turns receipts and invoices into reviewed canonical financial records, then syncs them to the user’s Google Sheet.

```text
Image / PDF
→ Sarvam Document AI Extract
→ canonical financial-document record
→ PostgreSQL
→ human review
→ mapped Google Sheets sync
```

Google Sheets is an output, never the system of record. GST validation, reconciliation, accounting, GSTR workflows, organization workspaces, and CA-firm products remain later phases. Hisaabo is reference-only; do not fork or reuse its code.

## Implementation changes

- Establish a Python backend using FastAPI, Pydantic v2, SQLAlchemy, Alembic, PostgreSQL, Redis-backed jobs, and private object storage; pair it with a React/TypeScript web client.
- Implement single-user Google OAuth authentication and Sheets authorization. The user selects a destination spreadsheet and maps canonical fields to existing columns.
- Create a canonical financial-document model for both receipts and invoices:
 - original document and metadata;
 - supplier, document number/date, GSTIN when available, currency, subtotal, tax values, discount, and total;
 - optional line items with stable IDs, description, quantity, unit price, HSN/SAC, taxable value, tax rate, and tax amount;
 - null/unknown support, exact decimal storage, provenance, confidence, and review revisions.
- Integrate the current Sarvam Document AI API:
 - use `/doc-ai/v1/job/extract` as the primary path;
 - submit the original file plus our versioned JSON schema;
 - consume asynchronous job results and persist `result`, field confidence, source annotations, provider/model details, and schema version;
 - handle `completed`, `partially_completed`, `failed`, and `rejected` separately.
- Use Sarvam `Digitise` only as a benchmark/fallback path for difficult documents, full text/layout archival, and extraction debugging. Do not automatically run OCR plus a second LLM call for every document.
- Define lifecycle states: `UPLOADED → QUEUED → PROCESSING → NEEDS_REVIEW → READY_TO_SYNC → SYNCED`, plus `PROCESSING_FAILED` and `SYNC_FAILED`.
- Build a review interface with the original document beside editable extracted fields and line items. A user must explicitly confirm before any Sheet write.
- Support mapped Sheets synchronization for an existing invoice/register tab and line-items tab. Add hidden managed columns for stable record ID, line-item ID, revision, and sync status; use those identifiers to update rows after corrections rather than append duplicates.
- Update `.context` during implementation to replace the earlier GST-first MVP description with this confirmed roadmap and Sarvam integration boundary.

## Test plan

- Validate canonical schemas, nullable fields, decimals, line items, versioning, and extraction-result parsing.
- Test Sarvam job polling, partial completion, invalid schema/output, rate-limit/provider failures, and retry-safe job processing.
- Run a benchmark comparing direct `Extract` with `Digitise` plus a secondary structuring path on representative, consented receipts and invoices; measure field accuracy, schema validity, latency, and cost.
- Verify no Sheet synchronization occurs before human approval.
- Verify OAuth revocation, invalid mappings, missing headers, and Sheets API failures leave records recoverable.
- Verify corrected records update their existing document and line-item rows without duplicate output.

## Assumptions and future boundary

- Phase 1 is single-user only. Organization and CA-firm offerings will be separate future products/codebases after this product proves demand.
- Sarvam Document AI is the initial production provider; the integration remains provider-isolated so it can be replaced later.
- Direct `Extract` is the default because it already performs multimodal OCR and schema-based extraction. `Digitise` is retained for comparison and fallback.
- Phase 2 adds GST validation, deterministic rules, duplicate detection, reconciliation, exceptions, and GST-ready records over the same PostgreSQL data.
- Phase 3 adds accounting workflows, ledgers, dashboards, integrations, and eventual filing APIs with explicit human confirmation.

## Assistant

Worked for 7s

## Assistant

Yes — this plan is strong, and it’s much cleaner than the earlier GST-first version. I’d approve it with a few targeted changes before implementation.

The biggest positive is that Phase 1 is now a real vertical slice:

```text
Document
→ extraction
→ canonical record
→ database
→ human review
→ client-specific Google Sheets sync
```

That gives you a complete commercial workflow without prematurely committing to GST logic.

A few changes I’d make:

- **Keep Sarvam isolated behind `DocumentExtractor` from day one.** Your plan says this, but I’d make it explicit in the implementation section. Nothing outside the provider adapter should know about `/doc-ai/v1/job/extract`, Sarvam job IDs, or Sarvam result shapes.
- **Do not call the canonical model only “invoice”.** Since Phase 1 supports receipts and invoices, use something like `FinancialDocument` or `FinancialDocumentRecord`, with `document_type = receipt | invoice | unknown`.
- **Keep Google Sheets sync as a separate destination layer.** The mapping engine should operate on the canonical record, not Sarvam output.
- **Treat `partially_completed` as reviewable, not automatically failed.** Sarvam documents that as a terminal state distinct from failed/rejected, so you should persist whatever valid result exists and route it to review with a warning. citeturn122929search1turn122929search4
- **Use exact decimal types throughout.** PostgreSQL `NUMERIC`, Python `Decimal`, and string/number serialization rules that never round monetary values through binary floats.
- **Do not automatically use Digitise as a retry fallback without a reason code.** Your current wording is good. I’d make fallback manual/configurable initially, because automatic second-path processing can quietly double cost and latency.

Your Sarvam assumptions are also technically aligned with the current docs. `POST /doc-ai/v1/job/extract` is asynchronous, requires a schema or config, and returns terminal states including `completed`, `partially_completed`, `failed`, and `rejected`. Extract results include the structured `result` plus annotations with confidence and source references. citeturn122929search0turn122929search1

Also, your choice to make **Extract the primary path** is correct. Sarvam explicitly positions Extract for invoices/forms and structured key-value capture, while Digitise is for full-document OCR/layout preservation. citeturn122929search0turn122929search5

I would slightly revise the lifecycle to distinguish extraction success from review state:

```text
UPLOADED
→ QUEUED
→ PROCESSING
→ EXTRACTED
→ NEEDS_REVIEW
→ READY_TO_SYNC
→ SYNCING
→ SYNCED
```

with:

```text
PROCESSING_FAILED
SYNC_FAILED
REJECTED
```

Why add `EXTRACTED` and `SYNCING`? Because they make retries and observability much cleaner. For example, if Sheets fails, you know extraction is complete and you do not rerun Sarvam.

For Google Sheets mapping, your hidden managed columns are a very good idea. I would minimally require:

```text
__record_id
__line_item_id
__record_revision
__sync_version
__last_synced_at
```

That gives you deterministic updates and prevents duplicate appends after retries or user edits.

One thing I would add to the test plan is a **mapping-compatibility test**. Since you chose client-owned column mapping rather than managed tabs, you need tests for:
- renamed columns
- deleted columns
- duplicate headers
- incompatible type expectations
- line-item mapping to the wrong tab
- mapping changes after records have already synced

I’d also change this assumption:

> “Organization and CA-firm offerings will be separate future products/codebases”

to:

> “Organization and CA-firm features are future phases and are not part of Phase 1.”

I would **not decide now that they must be separate codebases**. That is premature architecture. Your current backend can remain single-user while still leaving room for `owner_id` / `workspace_id` later. Splitting into separate products or codebases should be a business decision after demand is proven.

So my final verdict is:

**Approve the plan, with these adjustments:**
1. provider adapter boundary made explicit;
2. canonical model named around generic financial documents;
3. add `EXTRACTED` and `SYNCING` states;
4. treat `partially_completed` as reviewable;
5. keep Digitise fallback manual/configurable initially;
6. add Sheets mapping compatibility tests;
7. defer the “separate codebase” decision for org/CA products.

With those changes, this is a solid Phase 1 architecture and I would stop redesigning it unless implementation uncovers a genuine blocker.

## User

can you refresh me about that repo which was most close to waht we are doing about gst

## Assistant

Worked for a couple of seconds

## Assistant

Yes — the repo we found that was **closest to your GST product direction** was **Hisaabo**:

**GitHub:** https://github.com/hisaabo/hisaabo

It was much closer than `itr-wala` because Hisaabo is built around **Indian business finance + GST workflows**, not income tax.

What made it relevant to us was that it already covers a lot of the downstream GST/accounting side:

- GST-compliant sales and purchase invoices
- CGST / SGST / IGST logic
- GSTIN validation
- HSN/SAC handling
- GSTR-1 generation
- GSTR-3B generation
- GSTR-9
- GSTR-2B reconciliation
- ITC tracking
- e-invoicing / IRN
- e-way bills
- bank reconciliation
- multi-business support
- audit trails
- mobile + desktop + web-style clients
- APIs / CLI / MCP

Its architecture was also very relevant conceptually:

```text
Web / Mobile / Desktop / CLI / MCP
 ↓
 Typed API
 ↓
 GST + accounting logic
 ↓
 PostgreSQL
```

The important difference is that **Hisaabo starts from structured business transactions**, while **your product starts from messy documents**.

So Hisaabo is roughly:

```text
User/business creates transaction
→ accounting record
→ GST logic
→ GSTR workflows
```

Your product is:

```text
Receipt / invoice image or PDF
→ Sarvam Document AI
→ canonical financial record
→ human review
→ Google Sheets sync
→ later GST validation/reconciliation/accounting
```

That means your strongest differentiation is still:

> **documents first, GST/accounting later**

Another key point: Hisaabo’s roadmap included **PDF invoice OCR / photographed purchase bill extraction**, which overlaps with your Phase 1, but that was not its core implemented foundation when we checked.

And the license mattered a lot: Hisaabo uses an **O'Saasy-style non-compete license**, so for your commercial SaaS you should **study it, not fork it**. Use it as a reference for GST domain modeling, accounting flows, testing, auditability, and APIs, but keep your code independent.

We also found smaller repos useful for individual pieces, such as:
- `ayush2635/Invoiscope` — GST invoice OCR/extraction ideas
- `bhuvannarula/offlineGST` — GSTR-1 JSON generation
- `tks18/gstr-json-2-excel` — GSTR JSON processing
- `salilbh/GST-Returns-Automation---GSTR-3B` — GSTR-3B automation

But **Hisaabo was the closest overall product reference**. memcite

## Resources

### Local attachments
- [Pasted text(5).txt](../../../Raw/Export/file_00000000026081fa97f97796d12f65a4.dat)

### External references
- [Request for Event Approval](https://chatgpt.com/c/6a815dcb-7e94-83ee-a606-ece9f3b02a01)
- [Import News API Sheets](https://chatgpt.com/c/67b0ce0a-31e4-8007-9f54-d618e986f00e)
- [Skills List Extraction](https://chatgpt.com/c/68690bb6-7d0c-8007-a453-1e4ad4a1857f)
- [iQOO](https://chatgpt.com/c/6a89d21e-12a0-83e8-8202-ba608ffb9656)
- [Get API Key Instructions](https://chatgpt.com/c/6989f9f4-f594-8323-affd-1fac010257df)
- [CC](https://chatgpt.com/c/6a27f70d-820c-8320-b7e1-23c3d744951a)
- [Global Low Latency Firebase](https://chatgpt.com/c/69a00336-9f0c-83a6-b1f8-e0d4f6d56f2a)
- [Internship Details for Google Form](https://chatgpt.com/c/6a369cc1-85c8-83e8-8fbc-a2fa9aae95d8)
- [WT Insem](https://chatgpt.com/c/68a030a0-6440-8331-8f76-e769f035dafd)
- [Cloud Relational Data Management](https://chatgpt.com/c/670e8fe5-8824-8007-a955-23d2798e763d)
- [InSem](https://chatgpt.com/c/6791cb15-defc-8007-b9b8-9bc9976d94a6)
- [AI Platform Engineer Projects](https://chatgpt.com/c/6a6f7f2c-e4f0-83ee-ad93-a24a8c555201)
- [Document Intelligence Overview | Sarvam API Docs](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/overview?utm_source=chatgpt.com)
- [Change Log | Sarvam API Docs](https://docs.sarvam.ai/changelog?utm_source=chatgpt.com)
- [Building for Indian Languages | Sarvam API Docs](https://docs.sarvam.ai/api/getting-started/building-for-india?utm_source=chatgpt.com)
- [langgraph | LangChain Reference](https://reference.langchain.com/python/langgraph?utm_source=chatgpt.com)
- [Build workflows with Sarvam AI in n8n | Sarvam API Docs](https://docs.sarvam.ai/api/integration/n8n?utm_source=chatgpt.com)
- [About the New Architecture · React Native](https://reactnative.dev/architecture/landing-page?utm_source=chatgpt.com)
- [E-invoice API Integration | e-Invoicing Sandbox | Developer Portal](https://einvoice6.gst.gov.in/content/api-integration/?utm_source=chatgpt.com)
- [Deciding Which APIs to Integrate - IRIS IRP](https://einvoice6.gst.gov.in/content/kb/deciding-which-apis-to-integrate/?utm_source=chatgpt.com)
- [Onboarding APIs | Wiki - IRIS IRP](https://einvoice6.gst.gov.in/content/onboarding-apis-wiki/?utm_source=chatgpt.com)
- [APIs Categories - IRIS IRP](https://einvoice6.gst.gov.in/content/kb/apis-categories/?utm_source=chatgpt.com)
- [Models | Sarvam API Docs](https://docs.sarvam.ai/api/getting-started/models?utm_source=chatgpt.com)
- [Initialise Job | Sarvam API Docs](https://docs.sarvam.ai/api-reference-docs/document-intelligence/initialise?utm_source=chatgpt.com)
- [Open-Source Models | Sarvam API Docs](https://docs.sarvam.ai/api/getting-started/models/open-source?utm_source=chatgpt.com)
- [Change Log | Sarvam API Docs](https://docs.sarvam.ai/api-reference-docs/changelog?utm_source=chatgpt.com)
- [Document Translation API Overview | Sarvam API Docs](https://docs.sarvam.ai/api/api-guides-tutorials/doc-translation/overview?utm_source=chatgpt.com)
- [Sarvam Vision | Sarvam API Docs](https://docs.sarvam.ai/api/getting-started/models/sarvam-vision?utm_source=chatgpt.com)
- [Create Document Translation Job | Sarvam API Docs](https://docs.sarvam.ai/api-reference/translate-document/create-doc-translation?utm_source=chatgpt.com)
- [AI for all from India | Sarvam API Docs](https://docs.sarvam.ai/?utm_source=chatgpt.com)
- [IRIS Invoice Registration APIs to make your applications e-invoice ready](https://einvoice6.gst.gov.in/content/gujrati/e-invoice-apis-for-solution-providers/?utm_source=chatgpt.com)
- [Core APIs | Wiki - IRIS IRP](https://einvoice6.gst.gov.in/content/core-apis-wiki/?utm_source=chatgpt.com)
- [Core APIs | Wiki - IRIS IRP](https://einvoice6.gst.gov.in/content/hindi/core-apis-wiki/?utm_source=chatgpt.com)
- [API Credentials - IRIS IRP](https://einvoice6.gst.gov.in/content/kb/api-credentials/?utm_source=chatgpt.com)
- [Registration - IRIS IRP](https://einvoice6.gst.gov.in/content/kb/api-integrator-registration/?utm_source=chatgpt.com)
- [API User Onboarding - IRIS IRP](https://einvoice6.gst.gov.in/content/kb/api-user-onboarding/?utm_source=chatgpt.com)
- [IRIS IRP6 - GSTN Authorized e-Invoice Registration Portal](https://einvoice6.gst.gov.in/content/?utm_source=chatgpt.com)
- [Overview of Onboarding APIs - IRIS IRP](https://einvoice6.gst.gov.in/content/kb/overview-of-onboarding-apis/?utm_source=chatgpt.com)
- [GSTR 1](https://tutorial.gst.gov.in/contextualhelp/Einv/GSTR_1.htm?utm_source=chatgpt.com)
- [Create and Submit GSTR3B](https://tutorial.gst.gov.in/userguide/returns/Create_and_Submit_GSTR3B.htm?utm_source=chatgpt.com)
- [Manual_GSTR-10](https://tutorial.gst.gov.in/userguide/returns/Manual_GSTR-10.htm?utm_source=chatgpt.com)
- [Manual](https://tutorial.gst.gov.in/userguide/returns/GSTR7_Manual.htm?utm_source=chatgpt.com)
- [E-Invoice Apis for Solution Providers - IRIS IRP](https://einvoice6.gst.gov.in/content/e-invoice-apis-for-solution-providers/?utm_source=chatgpt.com)
- [Manual](https://tutorial.gst.gov.in/userguide/returns/manual_GSTR4annual.htm?utm_source=chatgpt.com)
- [Onboarding APIs | Wiki - IRIS IRP](https://einvoice6.gst.gov.in/content/hindi/onboarding-apis-wiki/?utm_source=chatgpt.com)
- [Access to Sandbox - IRIS IRP](https://einvoice6.gst.gov.in/content/kb/access-to-sandbox/?utm_source=chatgpt.com)
- [Request Rejected](https://developer.gst.gov.in/apiportal/taxpayer/returns/apilist/v2.2?utm_source=chatgpt.com)
- [GSTR3B](https://tutorial.gst.gov.in/userguide/returns/GSTR3B.htm?utm_source=chatgpt.com)
- [Request Rejected](https://developer.gst.gov.in/apiportal/taxpayer/returns/apilist?utm_source=chatgpt.com)
- [Durability | langgraph | LangChain Reference](https://reference.langchain.com/python/langgraph/types/Durability?utm_source=chatgpt.com)
- [Durability | langgraph_sdk | LangChain Reference](https://reference.langchain.com/python/langgraph-sdk/schema/Durability?utm_source=chatgpt.com)
- [Deep Agents vs LangChain vs LangGraph](https://www.langchain.com/blog/deep-agents-vs-langchain-vs-langgraph?utm_source=chatgpt.com)
- [LangChain and LangGraph Agent Frameworks Reach v1.0 Milestones](https://www.langchain.com/blog/langchain-langgraph-1dot0?utm_source=chatgpt.com)
- [LangGraph vs Temporal: AI Agent Orchestration Compared](https://www.langchain.com/resources/langgraph-vs-temporal?utm_source=chatgpt.com)
- [main | langgraph | LangChain Reference](https://reference.langchain.com/python/langgraph/pregel/main?utm_source=chatgpt.com)
- [LangGraph - Python API Reference | LangChain Reference](https://reference.langchain.com/python/langgraph/overview?utm_source=chatgpt.com)
- [LangChain vs. AutoGen in 2026: What the Maintenance Announcement Changed](https://www.langchain.com/resources/langchain-vs-autogen?utm_source=chatgpt.com)
- [LangGraph: Agent Orchestration Framework for Reliable AI Agents](https://www.langchain.com/langgraph?utm_source=chatgpt.com)
- [Fault Tolerance in LangGraph: Retries, Timeouts and Error Handlers](https://www.langchain.com/blog/fault-tolerance-in-langgraph?utm_source=chatgpt.com)
- [durability | langgraph_sdk | LangChain Reference](https://reference.langchain.com/python/langgraph-sdk/schema/CronUpdate/durability?utm_source=chatgpt.com)
- [Ollama](https://ollama.com/?utm_source=chatgpt.com)
- [Improved performance and model support with GGUF · Ollama Blog](https://ollama.com/blog/improved-performance-and-model-support-with-gguf?utm_source=chatgpt.com)
- [Ollama's highest performance on Apple Silicon yet with MLX · Ollama Blog](https://ollama.com/blog/mlx-performance?utm_source=chatgpt.com)
- [llama3](https://ollama.com/library/llama3?utm_source=chatgpt.com)
- [ollama launch · Ollama Blog](https://ollama.com/blog/launch?utm_source=chatgpt.com)
- [lm · Ollama](https://ollama.com/search?q=lm&utm_source=chatgpt.com)
- [llama3.3](https://ollama.com/library/llama3.3?utm_source=chatgpt.com)
- [llama2](https://ollama.com/library/llama2?utm_source=chatgpt.com)
- [llama3.2](https://ollama.com/library/llama3.2?utm_source=chatgpt.com)
- [Ollama](https://ollama.com/search?o=newest&utm_source=chatgpt.com)
- [Tools models · Ollama](https://ollama.com/search?c=tools&o=newest&utm_source=chatgpt.com)
- [Blog · Ollama](https://ollama.com/blog?utm_source=chatgpt.com)
- [Report updation for Drive against Fake Registration](https://gstn.org.in/reports/?utm_source=chatgpt.com)
- [React Native 0.84 - Hermes V1 by Default · React Native](https://reactnative.dev/blog/2026/02/11/react-native-0.84?utm_source=chatgpt.com)
- [New Architecture is here · React Native](https://reactnative.dev/blog/2024/10/23/the-new-architecture-is-here?utm_source=chatgpt.com)
- [Advanced Topics on Native Modules Development · React Native](https://reactnative.dev/docs/the-new-architecture/advanced-topics-components?utm_source=chatgpt.com)
- [React Native 0.76 - New Architecture by default, React Native DevTools, and more · React Native](https://reactnative.dev/blog/2024/10/23/release-0.76-new-architecture?utm_source=chatgpt.com)
- [Advanced Topics on Native Modules Development · React Native](https://reactnative.dev/docs/the-new-architecture/advanced-topics-modules?utm_source=chatgpt.com)
- [Architecture Overview · React Native](https://reactnative.dev/architecture/overview?utm_source=chatgpt.com)
- [Render, Commit, and Mount · React Native](https://reactnative.dev/architecture/render-pipeline?utm_source=chatgpt.com)
- [Blog · React Native](https://reactnative.dev/blog?utm_source=chatgpt.com)
- [React Native 0.80 - React 19.1, JS API Changes, Freezing Legacy Arch and much more · React Native](https://reactnative.dev/blog/2025/06/12/react-native-0.80?utm_source=chatgpt.com)
- [React Native 0.85 - New Animation Backend, New Jest Preset Package · React Native](https://reactnative.dev/blog/2026/04/07/react-native-0.85?utm_source=chatgpt.com)
- [Threading Model · React Native](https://reactnative.dev/architecture/threading-model?utm_source=chatgpt.com)
- [OCR GST Chat](https://chatgpt.com/c/6a9bfee1-cfac-83ee-8f44-1f37bcaef079)
- [GitHub - hisaabo/hisaabo: The simplest open source solution to manage your business finances. Simple as 1 - 2 - 3 · GitHub](https://github.com/hisaabo/hisaabo?utm_source=chatgpt.com)
- [Hisaabo · GitHub](https://github.com/hisaabo?utm_source=chatgpt.com)
- [hisaabo/.env.example at main · hisaabo/hisaabo · GitHub](https://github.com/hisaabo/hisaabo/blob/main/.env.example?utm_source=chatgpt.com)
- [GitHub - sajjanin/GSTR1JsonXLProcessor: An excel utility to process GST Json file downloaded for viewing · GitHub](https://github.com/sajjanin/GSTR1JsonXLProcessor?utm_source=chatgpt.com)
- [GitHub - bhumin18/smart-invoice: Full-stack Smart Invoice + GST Tool for India with Flask API and React frontend · GitHub](https://github.com/bhumin18/smart-invoice?utm_source=chatgpt.com)
- [GitHub - harshith187/GST: Converts ERPNext sales excel file to GSTR1 json format · GitHub](https://github.com/harshith187/GST?utm_source=chatgpt.com)
- [GitHub - tks18/gstr-json-2-excel: A Python Based Utility for Processing GST-Return JSON Files to Multiple Formats · GitHub](https://github.com/tks18/gstr-json-2-excel?utm_source=chatgpt.com)
- [GitHub - ritusmoikaushik/gstextract-core: Open-source Python library for extracting structured data from Indian GST invoice PDFs. Powers gstextract.com. · GitHub](https://github.com/ritusmoikaushik/gstextract-core?utm_source=chatgpt.com)
- [GitHub - surajgit79/Hisaab: Accounting Software comprising Nepal VAT rules and regulations. · GitHub](https://github.com/surajgit79/Hisaab?utm_source=chatgpt.com)
- [GitHub - AnujSureshkumar/synthetic-finance-data: Synthetic Indian-finance datasets (chart of accounts, payroll, GL, GST invoices, GSTR-2B, leases) that power the AI-for-finance portfolio. All data synthetic · GitHub](https://github.com/AnujSureshkumar/synthetic-finance-data?utm_source=chatgpt.com)
- [GitHub - vishnu27597/gstr1-mcp-server: MCP server for filing Indian GST GSTR-1 returns via sandbox APIs. Works with Claude, Kiro, ChatGPT, Cursor. · GitHub](https://github.com/vishnu27597/gstr1-mcp-server?utm_source=chatgpt.com)
- [Extract Fields | Sarvam API Docs](https://docs.sarvam.ai/api-reference/doc-ai/job/extract?utm_source=chatgpt.com)
- [Libraries & SDKs | Sarvam API Docs](https://docs.sarvam.ai/api/getting-started/sdks?utm_source=chatgpt.com)
- [FAQs | Sarvam API Docs](https://docs.sarvam.ai/docai/resources/faq?utm_source=chatgpt.com)
- [Digitise a document | Sarvam API Docs](https://docs.sarvam.ai/docai/how-to/digitise-a-document?utm_source=chatgpt.com)
- [Extract structured fields | Sarvam API Docs](https://docs.sarvam.ai/docai/how-to/extract-fields-from-a-document/extract-structured-fields?utm_source=chatgpt.com)
- [Welcome to Doc Agents | Sarvam API Docs](https://docs.sarvam.ai/docai/getting-started/overview?utm_source=chatgpt.com)
- [Get your config_id | Sarvam API Docs](https://docs.sarvam.ai/api/api-guides-tutorials/document-intelligence/how-to/get-your-config-id?utm_source=chatgpt.com)
- [Pricing | Sarvam API Docs](https://docs.sarvam.ai/api/getting-started/pricing?utm_source=chatgpt.com)
- [Get Status | Sarvam API Docs](https://docs.sarvam.ai/api-reference/legacy/document-intelligence/get-status?utm_source=chatgpt.com)
- [Job Lifecycle | Sarvam API Docs](https://docs.sarvam.ai/api/api-guides-tutorials/dubbing/job-lifecycle?utm_source=chatgpt.com)
- [Get Download Links | Sarvam API Docs](https://docs.sarvam.ai/api-reference-docs/document-intelligence/get-download-links?utm_source=chatgpt.com)
- [Start Job | Sarvam API Docs](https://docs.sarvam.ai/api-reference/legacy/document-intelligence/start?utm_source=chatgpt.com)
- [Initialise Job | Sarvam API Docs](https://docs.sarvam.ai/api-reference/legacy/document-intelligence/initialise?utm_source=chatgpt.com)
