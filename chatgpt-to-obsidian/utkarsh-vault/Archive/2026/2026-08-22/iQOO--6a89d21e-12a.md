---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a89d21e-12a0-83e8-8202-ba608ffb9656"
created: 1787417157.457274
updated: 1788607906.247761
resource_section: true
---

# iQOO

## User

Give me new ideas not that gst, audora or aideo

## Assistant

Worked for a couple of seconds

## Assistant

Absolutely. Looking at the available **7 domains** in the iQOO Hackathon, I’d avoid generic “AI chatbot” ideas. You want something that has a **clear problem → AI advantage → working prototype → measurable impact**.

Here are ideas that are substantially different from **GST, Audora, and AIdeo**.

## 🔥 My strongest ideas

### 1. 🧾 “Bill-to-Budget” — Personal Financial Autopilot
**Domain:** FinTech & Commerce

Instead of simply tracking expenses, the system understands a person's **financial behavior**.

**How it works:**
- User uploads bank statement / SMS / UPI history.
- AI categorizes transactions automatically.
- Detects recurring subscriptions.
- Predicts end-of-month cash flow.
- Identifies unusual spending.
- Gives recommendations like:
 > “Your food delivery spending increased 37% this month.”
- Creates a personalized monthly financial plan.

**Interesting part:** 
The AI doesn't just *show* analytics; it builds a **financial action plan**.

**MVP:** CSV/bank statement → transaction extraction → categorization → dashboard → AI recommendations.

**Potential:** ⭐⭐⭐⭐⭐

---

### 2. 🎓 “TeachBack” — AI That Knows Whether You Actually Understand

**Domain:** Smart Education

Instead of an AI tutor that keeps explaining things, make one that determines **whether the student genuinely understands the concept**.

Student selects:

> DBMS → Normalization → 3NF

AI teaches the concept briefly and then asks the student to **explain it back in their own words**.

It analyzes:
- Conceptual correctness
- Missing concepts
- Misconceptions
- Confidence
- Ability to apply the concept

Then generates:

> **Understanding: 72%** 
> You understand functional dependencies but are confusing 2NF and 3NF.

Then it gives a targeted question.

This creates a loop:

**Learn → Explain → Evaluate → Correct → Apply**

That's considerably more interesting than another ChatGPT tutor.

**Potential:** ⭐⭐⭐⭐⭐

---

### 3. 🏥 “PreCheck AI” — Intelligent Healthcare Intake

**Domain:** HealthTech

Before seeing a doctor, patients often have to explain:

> “Since when?” 
> “How severe?” 
> “What happened before that?” 
> “Any medications?”

Build an AI intake system that conducts a structured conversation.

Patient speaks naturally:

> “I've had this headache since yesterday and it becomes worse when I look at screens…”

AI converts it into a structured clinical intake:

```text
Chief complaint:
Headache

Duration:
1 day

Severity:
Moderate

Triggers:
Screen exposure

Associated symptoms:
...

Red flags:
None detected
```

Then gives the **doctor a concise summary**, rather than attempting to diagnose the patient.

The important distinction:

**AI isn't replacing the doctor. 
AI eliminates the information-gathering burden.**

**Potential:** ⭐⭐⭐⭐⭐

---

### 4. 🏠 “HomeMind” — AI That Understands Your Home

**Domain:** Smart Living

Use a phone camera to scan a room.

AI identifies:
- Appliances
- Furniture
- Lighting
- Windows
- Potential energy wastage

Then creates an intelligent home profile.

Example:

> “Your AC is running while the room has an open window.”

Or:

> “The room receives sufficient natural light between 9 AM–12 PM. You could reduce lighting usage during this period.”

With IoT integration, it could eventually control:
- Lights
- AC
- Fans
- Smart plugs

**MVP doesn't require actual IoT hardware.**

Camera → scene understanding → simulated IoT environment → recommendations.

**Potential:** ⭐⭐⭐⭐

---

### 5. 👨‍💻 “BugLens” — AI Debugger That Understands the Whole Project

**Domain:** Developer Tools

Not another Copilot.

Upload/connect a GitHub repository.

AI builds a map of:

```text
Frontend
 ↓
API
 ↓
Authentication
 ↓
Database
 ↓
External Services
```

Then when an error occurs:

```text
500 POST /api/orders
```

instead of simply saying:

> “Check your backend.”

it traces the likely path:

> Frontend sends `productId`
> ↓
> Express route receives request
> ↓
> Controller expects `product_id`
> ↓
> SQL query receives NULL
> ↓
> Database constraint fails

Then gives the **exact file + function + probable fix**.

This is particularly strong for a hackathon because you can demonstrate it live.

**Potential:** ⭐⭐⭐⭐⭐

---

### 6. 🔍 “RepoDoctor” — AI Technical Debt Scanner

**Domain:** Developer Tools

Give it a GitHub repository.

It analyzes:

- Duplicate code
- Dead code
- Security risks
- Poor architecture
- Circular dependencies
- Bad API patterns
- Missing error handling
- Environment-variable leaks
- Database bottlenecks

Then generates:

### Architecture Health

| Area | Score |
|---|---:|
| Security | 74 |
| Maintainability | 61 |
| Performance | 82 |
| Architecture | 68 |

But the important feature:

**It prioritizes problems by actual impact.**

> 🔴 Fix this first — authentication middleware can be bypassed.

rather than producing a 200-item generic lint report.

**Potential:** ⭐⭐⭐⭐⭐

---

### 7. 🧠 “MemoryOS” — Personal Knowledge Graph

**Domain:** Productivity

People have information scattered across:

- PDFs
- WhatsApp exports
- Emails
- Notes
- Documents
- Screenshots

Build a personal knowledge system that creates a **relationship graph**.

For example:

```text
Machine Learning
 │
 ├── Project X
 │ ├── Dataset
 │ └── Research Paper
 │
 └── Exam
 ├── Unit 3
 └── Assignment
```

User asks:

> “What did I need to complete for the ML project?”

AI retrieves information across the connected knowledge base and answers with sources.

The differentiator is **relationships + context**, not simply RAG.

**Potential:** ⭐⭐⭐⭐½

---

### 8. ⏱️ “FocusOS” — AI That Detects Why You Waste Time

**Domain:** Productivity

Instead of another Pomodoro app, use AI to understand work patterns.

It observes voluntarily connected activity:

```text
9:00 → VS Code
9:24 → YouTube
9:31 → VS Code
9:47 → Discord
10:02 → VS Code
```

AI identifies:

> “Your average uninterrupted coding session is 18 minutes.”

And detects context switching.

Then recommends:

> **Deep Work Window**
> 10:00–11:30 AM 
> Disable Discord + YouTube notifications.

Could even dynamically create focus modes.

**Potential:** ⭐⭐⭐⭐

---

### 9. 🏫 “ClassPulse” — AI Classroom Intelligence

**Domain:** Smart Education

A teacher records/streams a lecture.

AI extracts:

- Topics taught
- Questions asked
- Important concepts
- Student doubts
- Attendance
- Pace of teaching
- Topics requiring revision

After class:

> **Today's lecture**
>
> 4 concepts covered 
> 7 student questions 
> 2 concepts with high confusion 
> 3 students need revision

Students get personalized revision material.

Teachers get a **classroom intelligence dashboard**.

**Potential:** ⭐⭐⭐⭐½

---

### 10. 📦 “ReturnSense” — Predict Product Returns Before They Happen

**Domain:** FinTech & Commerce

For e-commerce companies.

AI analyzes:

- Product description
- Reviews
- Customer complaints
- Previous returns
- Product images
- Size information

and predicts:

> **Return probability: 38%**

More importantly:

> Main predicted reason: **size mismatch**

The company can proactively modify the listing:

> “Customers report this product runs one size smaller.”

This attacks a real business problem: **return logistics and revenue loss**.

**Potential:** ⭐⭐⭐⭐⭐

---

## 🥇 If I were choosing for your team

I'd shortlist these **five**:

| Rank | Idea | Domain | Why |
|---|---|---|---|
| 🥇 | **BugLens** | Developer Tools | Excellent live demo + technically impressive |
| 🥈 | **TeachBack** | Smart Education | Unique AI interaction + easy MVP |
| 🥉 | **ReturnSense** | FinTech | Strong commercial problem |
| 4 | **PreCheck AI** | HealthTech | Very practical + impressive AI |
| 5 | **RepoDoctor** | Developer Tools | Strong engineering depth |

### But there is one I particularly like for you:

**BugLens.**

Because you can build a genuinely impressive demo without needing hardware, proprietary datasets, or complicated integrations.

Imagine the judge gives you a broken repository.

You upload it.

Your system generates:

```text
PROJECT HEALTH
━━━━━━━━━━━━━━━━━━
Architecture 71/100
Security 83/100
Performance 64/100
Maintainability 58/100

3 Critical Issues Found
━━━━━━━━━━━━━━━━━━

🔴 Authentication bug
server/auth.js:47

🟠 N+1 database query
orders/controller.js:82

🟡 Unhandled API failure
api/payment.js:31
```

Then the judge clicks **“Investigate”**:

```text
Request
 ↓
Route
 ↓
Controller
 ↓
Service
 ↓
Database
 ↓
Failure
```

And the AI explains **why the bug occurs**, not merely what the error message says.

That gives you a very strong **“AI + engineering”** story rather than another wrapper around an LLM.

If the goal is **maximum shortlist/winning potential**, I'd build the idea around **a painful problem that AI can actually solve**, not around the AI model itself.

## User

I choose TeachBack

## Assistant

Good choice. **TeachBack** has a much stronger differentiation angle than a normal AI tutor.

I would lock the core concept as:

> **TeachBack — An AI learning system that measures understanding by asking students to explain concepts in their own words, detects misconceptions, and adapts the next learning step accordingly.**

### The core loop

**Learn → Teach Back → Analyze → Correct → Apply → Reassess**

Example:

**Topic:** DBMS — 3NF

AI gives a short explanation, then asks:

> “Explain 3NF as if you were teaching it to a classmate.”

Student responds by **voice or text**.

AI evaluates:

| Dimension | Result |
|---|---:|
| Concept understanding | 82% |
| Accuracy | 76% |
| Completeness | 68% |
| Misconceptions | 1 |
| Confidence | Moderate |

Then instead of repeating the whole chapter, it identifies the exact weakness:

> **You understand transitive dependency, but you're missing the requirement that the determinant must be a candidate key.**

Then it asks a targeted question.

### What makes it different

Don't position it as:

❌ *“AI tutor for students.”*

Position it as:

✅ **“An AI that verifies whether a student actually understands something.”**

That's the important distinction.

Most educational AI systems measure:

**Did you answer correctly?**

TeachBack measures:

**Can you explain why the answer is correct?**

That gives you a strong educational concept around **active recall, retrieval practice, and misconception detection**.

### MVP I would build

Keep V1 tight:

1. **Choose subject/topic**
2. AI generates a short lesson
3. AI asks a TeachBack question
4. Student responds by **text + optional voice**
5. AI evaluates the explanation against a concept rubric
6. Detects misconceptions
7. Generates a personalized follow-up question
8. Shows a **Concept Mastery Map**
9. Repeats until mastery

For the hackathon, I'd use **one subject deeply rather than trying to support everything**. For example:

> **Engineering students → DBMS / Data Structures / Operating Systems**

That makes the demo much more credible.

### The killer demo

Start with a deliberately wrong explanation.

Student says:

> “3NF means every table should have three normal forms and there shouldn't be duplicate values.”

TeachBack should respond:

> ⚠️ **Misconception detected**

Then visually highlight:

- ❌ Incorrect definition
- ⚠️ Missing functional dependency concept
- ⚠️ Confusion between normalization and duplicate removal

Then ask:

> **“Consider this relation. Can you identify the transitive dependency?”**

Student answers again.

The system updates their mastery.

That **before → misconception → intervention → improvement** sequence is what I'd build the entire pitch around.

If we're proceeding with this for the iQOO Hackathon, the next thing we should do is **freeze the product architecture and MVP scope before writing any code**, so we don't end up changing direction midway.

## User

ok lets freeze the product architecture and MVP scope before writing any code

## Assistant

Worked for 11s

## Assistant

Yes. Before touching code, we should make **TeachBack architecturally boring and predictable**: one clear pipeline, explicit contracts, minimal services, and no features that don't contribute to the core demo.

I would freeze the following as **TeachBack v1.0**.

# TeachBack — Frozen Product Architecture

## 1. Product Definition

> **TeachBack is an AI learning system that verifies conceptual understanding by asking students to explain a topic in their own words, identifies misconceptions, and generates targeted follow-up questions until the student's understanding improves.**

The central differentiator is:

**Traditional AI Tutor**

`Question → Answer → Explanation`

**TeachBack**

`Learn → Explain → Evaluate → Diagnose → Correct → Explain Again`

The second loop is the product.

---

# 2. Target User

### Primary user

**College students**, initially focused on technical/engineering subjects.

For the hackathon demo, we should constrain the content to subjects such as:

- DBMS
- Data Structures
- Operating Systems
- Computer Networks
- Machine Learning

We should **not** attempt to build a complete education platform for every school/college subject in MVP.

The underlying architecture will remain subject-agnostic.

---

# 3. MVP Scope

### Must have

| Feature | MVP |
|---|---|
| Student login | Basic |
| Subject/topic selection | ✅ |
| AI-generated learning material | ✅ |
| TeachBack question | ✅ |
| Text response | ✅ |
| Voice response | ✅ |
| Speech-to-text | ✅ |
| Concept evaluation | ✅ |
| Misconception detection | ✅ |
| Targeted corrective explanation | ✅ |
| Follow-up question | ✅ |
| Mastery score | ✅ |
| Session history | Basic |
| Multilingual interaction | ✅ |
| Evidence/source grounding | ✅ |

### Explicitly NOT in MVP

Do **not** add:

- Social learning
- Teacher marketplace
- Gamification
- Leaderboards
- Video lectures
- Parent dashboard
- Attendance management
- Live classroom
- Complex LMS integration
- Mobile application
- Autonomous AI agents
- Multiple independent microservices

These are distractions for the hackathon.

---

# 4. Core User Flow

This is the flow we should build everything around:

```text
 ┌───────────────┐
 │ Select Topic │
 └───────┬───────┘
 ↓
 ┌───────────────┐
 │ Learn │
 │ AI explanation│
 └───────┬───────┘
 ↓
 ┌───────────────┐
 │ TeachBack │
 │ Question │
 └───────┬───────┘
 ↓
 ┌─────────────┴─────────────┐
 ↓ ↓
 Text Response Voice Response
 │ │
 │ ┌─────▼─────┐
 │ │ STT │
 │ └─────┬─────┘
 │ │
 └──────────────┬────────────┘
 ↓
 ┌─────────────────┐
 │ Evaluate Answer │
 └────────┬────────┘
 ↓
 ┌──────────┴──────────┐
 ↓ ↓
 Correct Misconception
 │ │
 └──────────┬──────────┘
 ↓
 ┌─────────────────┐
 │ Targeted │
 │ Intervention │
 └────────┬────────┘
 ↓
 ┌─────────────────┐
 │ Follow-up │
 │ TeachBack │
 └────────┬────────┘
 ↓
 ┌─────────────────┐
 │ Mastery Update │
 └─────────────────┘
```

**This loop is the heart of TeachBack.**

---

# 5. High-Level Architecture

I recommend **one frontend + one backend + one AI engine + supporting infrastructure**.

Not 8–10 services.

```text
┌─────────────────────────────────────────────┐
│ FRONTEND │
│ React + Vite + TypeScript │
└──────────────────────┬──────────────────────┘
 │
 REST / WebSocket
 │
┌──────────────────────▼──────────────────────┐
│ BACKEND │
│ FastAPI │
│ │
│ Auth │ Sessions │ Topics │ Responses │
│ │ Evaluation │ Mastery │
└──────────────┬──────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────┐
│ AI ENGINE │
│ │
│ STT → Retrieval → Evaluation → Generation │
│ │
│ Sarvam STT │
│ Embeddings │
│ Qdrant │
│ Sarvam-105B │
└──────────────┬──────────────────────────────┘
 │
 ▼
┌─────────────────────────────────────────────┐
│ DATA │
│ │
│ PostgreSQL Qdrant Content │
│ User/session Vectors Documents │
│ Mastery Retrieval │
└─────────────────────────────────────────────┘
```

---

# 6. Frontend

### Stack

**React + Vite + TypeScript**

Keep the frontend focused on four screens.

### Screen 1 — Dashboard

```text
Welcome back

Your Learning
────────────────────

DBMS 78%
Data Structures 64%
Operating Systems 42%

\[ Continue Learning \]
```

### Screen 2 — Topic

```text
DBMS

Normalization

\[ Start Learning \]
```

### Screen 3 — TeachBack

This is the most important screen.

```text
┌────────────────────────────────────┐
│ Explain 3NF │
│ │
│ "Explain this concept as if you │
│ were teaching a classmate." │
│ │
│ 🎙 Speak │
│ │
│ ────────────────────────────────── │
│ Your response: │
│ │
│ \[................................\] │
│ │
│ Submit │
└────────────────────────────────────┘
```

### Screen 4 — Feedback

```text
Your Understanding

 76%
 ━━━━━━━━━━━

✓ Functional dependency
✓ Candidate key

⚠ Transitive dependency
 Needs improvement

AI Feedback
─────────────────
You correctly identified...

However, you confused...

\[ Try Again \]
```

That's enough for the MVP.

---

# 7. Backend Architecture

FastAPI should own the application contract.

Suggested structure:

```text
backend/
│
├── app/
│ ├── main.py
│ │
│ ├── api/
│ │ ├── auth.py
│ │ ├── topics.py
│ │ ├── sessions.py
│ │ ├── responses.py
│ │ └── health.py
│ │
│ ├── schemas/
│ │ ├── topic.py
│ │ ├── session.py
│ │ ├── response.py
│ │ └── evaluation.py
│ │
│ ├── services/
│ │ ├── session_service.py
│ │ ├── evaluation_service.py
│ │ ├── mastery_service.py
│ │ └── content_service.py
│ │
│ └── core/
│ ├── config.py
│ └── dependencies.py
│
└── tests/
```

No unnecessary repository/service abstraction everywhere.

---

# 8. AI Engine

This is where we need to be particularly disciplined.

The AI pipeline should be:

```text
User Response
 │
 ▼
┌──────────────┐
│ STT │
└──────┬───────┘
 │
 ▼
 Transcript
 │
 ▼
┌──────────────┐
│ Retrieval │
└──────┬───────┘
 │
 ▼
Relevant Concepts
 │
 ▼
┌──────────────┐
│ Evaluation │
└──────┬───────┘
 │
 ├── Understanding
 ├── Accuracy
 ├── Completeness
 ├── Misconceptions
 └── Missing concepts
 │
 ▼
 ┌──────────────┐
 │ Intervention │
 └──────┬───────┘
 │
 ▼
 Follow-up Question
```

### Important architectural decision

**Evaluation and generation are separate logical stages.**

Don't make one giant prompt:

> "Evaluate the student and generate feedback and a question."

Instead:

```text
Evaluator
 ↓
Structured Evaluation
 ↓
Intervention Generator
 ↓
Follow-up Question
```

This makes the system much easier to debug and demonstrate.

---

# 9. Evaluation Contract

This is one of the most important contracts in the entire project.

The AI evaluator should return structured data such as:

```json
{
 "overall_score": 76,
 "accuracy": 82,
 "completeness": 68,
 "understanding": 78,
 "misconceptions": \[
 {
 "concept": "transitive dependency",
 "severity": "medium",
 "explanation": "..."
 }
 \],
 "correct_concepts": \[
 "functional dependency",
 "candidate key"
 \],
 "missing_concepts": \[
 "transitive dependency"
 \],
 "recommendation": "targeted_revision"
}
```

The frontend should **never parse free-form AI text to determine scores**.

The backend receives structured output.

That is a hard architectural rule.

---

# 10. RAG Architecture

We should use RAG because TeachBack needs to evaluate answers against **actual learning material**, not the model's general knowledge.

```text
Learning Content
 │
 ▼
Document Processing
 │
 ▼
Chunking
 │
 ▼
Embeddings
 │
 ▼
Qdrant
 │
 │
Student Answer
 │
 ▼
Embedding
 │
 ▼
Similarity Search
 │
 ▼
Relevant Concepts
 │
 ▼
Evaluator
```

This also gives us a strong hackathon explanation:

> **The AI evaluates what the student said against the actual concepts they were supposed to learn.**

---

# 11. Multilingual Architecture

This should remain **multilingual end-to-end**, without adding a translation layer.

The architecture is:

```text
Indian-language Speech
 ↓
Sarvam STT
 ↓
Native-language Transcript
 ↓
Multilingual Retrieval
 ↓
Sarvam-105B
 ↓
Native-language Feedback
```

We've previously locked the multilingual approach around **10 Indic languages + English with no translation layer**, so we should preserve that decision rather than introducing translation into TeachBack. memcite

That is actually a strong differentiator for the India-focused hackathon.

A student should be able to:

> **Learn → Explain → Receive feedback**

in their preferred supported language.

---

# 12. Model Responsibilities

We should not make every model responsible for everything.

| Component | Responsibility |
|---|---|
| **Sarvam STT** | Speech → text |
| **Embedding model** | Text → vector |
| **Qdrant** | Semantic retrieval |
| **Sarvam-105B** | Evaluation + explanation + question generation |
| **Backend** | Orchestration + validation |
| **Frontend** | Interaction + visualization |

This separation is important.

---

# 13. Mastery Model

Don't over-engineer this into an ML research project.

For MVP, use a simple concept-level score.

Example:

```text
Concept: Normalization

Functional Dependency 92%
Candidate Key 84%
2NF 71%
3NF 54%
BCNF 38%
```

Overall topic mastery can be calculated from concept scores.

More importantly, we maintain:

```text
Student
 ↓
Topic
 ↓
Concept
 ↓
Attempts
 ↓
Mastery
```

This gives us a meaningful **Concept Mastery Map** without needing a complicated adaptive-learning algorithm.

---

# 14. Database Responsibilities

### PostgreSQL

Store application state:

```text
users
topics
concepts
sessions
responses
evaluations
mastery
```

### Qdrant

Store:

```text
learning content embeddings
concept embeddings
retrieval metadata
```

**Do not put application state into Qdrant.**

---

# 15. Session State

A session should look conceptually like:

```text
Session
│
├── Topic
│
├── Concepts
│
├── Initial lesson
│
├── TeachBack #1
│ ├── response
│ ├── evaluation
│ └── misconceptions
│
├── Intervention
│
├── TeachBack #2
│ ├── response
│ └── evaluation
│
└── Final mastery
```

This allows us to demonstrate:

> **Student started at 52% → intervention → reached 81%.**

That is much stronger than simply displaying an AI-generated score.

---

# 16. API Contract

Keep the initial API small.

```text
POST /api/sessions
GET /api/topics
GET /api/topics/{id}

POST /api/sessions/{id}/teachback
POST /api/sessions/{id}/voice

GET /api/sessions/{id}
GET /api/sessions/{id}/mastery

GET /api/health
```

We can add WebSocket streaming later only if the voice experience genuinely requires it.

**REST first.**

That prevents us from introducing unnecessary real-time infrastructure into the MVP.

---

# 17. Guardrails

TeachBack needs guardrails because the evaluator's output directly affects the student's learning.

Minimum protections:

### Input validation

Reject:

- Empty responses
- Extremely long responses
- Unsupported audio
- Invalid session IDs

### Evaluation validation

Backend verifies:

```text
score ∈ 0–100
severity ∈ allowed values
required fields exist
```

### Grounding

The evaluator receives retrieved learning context.

If sufficient evidence cannot be retrieved:

```text
evaluation_status = "INSUFFICIENT_CONTEXT"
```

It should **not confidently invent a misconception**.

### Off-topic response

If the student answers something unrelated:

> “Your response doesn't address the concept being evaluated.”

Then generate another TeachBack question.

---

# 18. What We Will Demonstrate

The final demo should be approximately:

### Scene 1 — Learn

Select:

> DBMS → Normalization → 3NF

AI teaches the concept.

### Scene 2 — Teach Back

AI asks:

> “Explain 3NF as if you were teaching a classmate.”

Student deliberately gives an incomplete answer.

### Scene 3 — AI diagnoses

```text
Understanding: 61%

✓ Functional dependency
✓ Candidate key

⚠ Transitive dependency
⚠ Complete 3NF condition
```

### Scene 4 — Intervention

AI explains **only the missing concept**.

### Scene 5 — Teach Back again

Student gives an improved explanation.

### Scene 6 — Mastery improvement

```text
Before ██████░░░░ 61%

After ████████░░ 84%
```

### Scene 7 — Multilingual

Repeat a short interaction in an Indian language using voice.

That gives the judges:

**AI + Education + Voice + Multilingual India + Measurable learning improvement.**

---

# 19. Frozen MVP Boundary

This is the boundary I recommend we **do not cross during implementation**:

```text
 TEACHBACK MVP
 │
 ┌────────────────┼────────────────┐
 │ │ │
 Learn TeachBack Mastery
 │ │ │
 Content Text / Voice Concept
 │ │ scores
 │ STT
 │ │
 └───────────────┼────────────────┘
 │
 RAG
 │
 Evaluation
 │
 Misconception
 │
 Intervention
 │
 Reassessment
```

Everything we build should directly support this loop.

---

# 20. Final Technology Stack

| Layer | Decision |
|---|---|
| Frontend | **React + Vite + TypeScript** |
| Styling | Tailwind CSS |
| Backend | **FastAPI** |
| API | REST |
| Database | **PostgreSQL** |
| Vector DB | **Qdrant** |
| STT | **Sarvam STT** |
| LLM | **Sarvam-105B** |
| Embeddings | Multilingual embedding model |
| RAG | Custom lightweight pipeline |
| Auth | Simple authentication |
| Deployment | Docker |
| Languages | **10 Indic languages + English** |
| Translation | **None** |

The important point is that **we are freezing the architecture, not necessarily every implementation detail of an external model/API**. If an SDK changes, we replace the adapter—not redesign TeachBack.

---

# 21. Architecture Principle

I would put this at the top of the project README:

> **TeachBack is not an AI tutor. It is an AI understanding-verification system.**

And our core architectural invariant is:

> **Every TeachBack cycle must produce a structured evaluation of the student's understanding and use that evaluation to determine the next learning action.**

That is the product contract.

**I would now consider the product architecture and MVP scope frozen.** The next step should be to define the **exact contracts/schemas and repository structure** before implementing the backend, frontend, or AI pipeline. memcite

## User

“TeachBack” — AI That Knows Whether You Actually Understand

Domain: Smart Education

Instead of an AI tutor that keeps explaining things, make one that determines whether the student genuinely understands the concept.

Student selects:

SPPU-> SEMESTER-> DBMS subject -> Normalization topic → 3NF all concepts in that topic from sppu syllabus, so we will need knowledge base of all subjects and experties in them, so sujjest me which tech would be appropriate and we can make it expandable also with silimar university's subjects. 

AI teaches the concept briefly and then asks the student to explain it back in their own words.

for now we support only sppu only 

It analyzes:

Conceptual correctness

Missing concepts

Misconceptions

Confidence

Ability to apply the concept

Then generates:

Understanding: 72%

You understand functional dependencies but are confusing 2NF and 3NF.

Then it gives a targeted question.

This creates a loop:

Learn → Explain → Evaluate → Correct → Apply

That's considerably more interesting than another ChatGPT tutor.

## Assistant

Worked for 4s

## Assistant

Yes — **this changes the architecture in an important way**.

TeachBack should not be built as a generic RAG tutor where we dump PDFs into a vector database and ask an LLM questions. If the product promise is:

> **SPPU → Programme → Semester → Subject → Unit → Topic → Concept**

then the system needs a **curriculum-aware knowledge architecture**.

That will also make it expandable later to other universities without redesigning the core system.

SPPU already has multiple engineering patterns/programmes and newer 2024/2025 patterns, so we should treat **university + programme + pattern + semester + subject** as first-class entities rather than hard-coding SPPU subjects. citeturn0search0turn0search4

# 1. The architecture I recommend

Use **three layers of knowledge**, not one.

```text
 TEACHBACK KNOWLEDGE SYSTEM
 │
 ┌────────────────┼────────────────┐
 │ │ │
 ▼ ▼ ▼
 CURRICULUM KNOWLEDGE ASSESSMENT
 LAYER LAYER LAYER
 │ │ │
 SPPU / Pattern Concepts Questions
 Semester Explanations Rubrics
 Subject Examples Misconceptions
 Unit Relationships Scenarios
 Topic Sources Evaluation criteria
```

This distinction is extremely important.

---

# 2. Curriculum Layer

This answers:

> **What is the student supposed to learn?**

For example:

```text
University
└── SPPU
 └── Programme
 └── B.E. AI & Data Science
 └── Pattern
 └── 2024 Pattern
 └── Semester
 └── Semester IV
 └── Subject
 └── DBMS
 ├── Unit I
 ├── Unit II
 ├── Unit III
 ├── Unit IV
 └── Unit V
```

Then:

```text
Unit III
└── Normalization
 ├── Functional Dependency
 ├── 1NF
 ├── 2NF
 ├── 3NF
 ├── BCNF
 ├── Multivalued Dependency
 └── ...
```

**This should be structured data.**

Do not rely on vector search to determine the curriculum hierarchy.

---

# 3. Knowledge Layer

The curriculum tells us:

> **3NF exists in the syllabus.**

The knowledge layer tells us:

> **What does 3NF actually mean?**

For every concept, we should eventually have:

```text
Concept
├── Definition
├── Prerequisites
├── Key principles
├── Examples
├── Counterexamples
├── Common misconceptions
├── Related concepts
├── Applications
├── Difficulty
├── Learning objectives
└── Source references
```

For example:

```text
3NF

Prerequisites:
 ├── Functional Dependency
 ├── Candidate Key
 └── Super Key

Core concepts:
 ├── Transitive Dependency
 └── Non-prime attributes

Common misconceptions:
 ├── "3NF means three tables"
 ├── "3NF removes all redundancy"
 └── "Every non-key attribute must be independent"

Application:
 └── Schema decomposition
```

This is what makes TeachBack **intelligent rather than just RAG over PDFs**.

---

# 4. Assessment Layer

This is the layer that makes TeachBack unique.

Every concept should eventually have an **assessment model**.

For 3NF:

```text
3NF
│
├── Recall
│ └── Define 3NF
│
├── Explain
│ └── Explain 3NF in your own words
│
├── Distinguish
│ └── Difference between 2NF and 3NF
│
├── Apply
│ └── Identify whether a relation satisfies 3NF
│
└── Diagnose
 └── Identify the violation in a schema
```

Now the AI isn't randomly generating questions.

It knows:

> **This student has demonstrated recall but hasn't demonstrated application.**

So the next question can deliberately target application.

---

# 5. Technology Stack

For this architecture, I would use:

| Requirement | Technology |
|---|---|
| Application database | **PostgreSQL** |
| Knowledge graph | **Neo4j** |
| Vector search | **Qdrant** |
| Backend | **FastAPI** |
| AI orchestration | Python |
| LLM | Sarvam-105B |
| STT | Sarvam |
| Embeddings | Multilingual embedding model |
| Document ingestion | Python |
| Frontend | React + TypeScript |
| Object storage | S3-compatible storage |
| Deployment | Docker |

But there is an important question:

## Do we actually need Neo4j?

For the **first MVP**, I would say **no**.

We can model the curriculum relationships directly in PostgreSQL.

```text
universities
programmes
patterns
semesters
subjects
units
topics
concepts
concept_relationships
```

Then use:

**PostgreSQL + Qdrant**

instead of:

**PostgreSQL + Neo4j + Qdrant**

This keeps the system considerably simpler.

If the knowledge relationships become genuinely graph-heavy later, Neo4j can be introduced.

---

# 6. So the frozen architecture should be

```text
 ┌─────────────────────┐
 │ React UI │
 └──────────┬──────────┘
 │
 REST / WebSocket
 │
 ┌──────────▼──────────┐
 │ FastAPI │
 │ │
 │ Curriculum Service │
 │ Learning Service │
 │ TeachBack Service │
 │ Assessment Service │
 │ Mastery Service │
 └───────┬───────┬──────┘
 │ │
 ┌────────────┘ └─────────────┐
 ▼ ▼
 ┌─────────────┐ ┌─────────────┐
 │ PostgreSQL │ │ Qdrant │
 │ │ │ │
 │ Curriculum │ │ Knowledge │
 │ Concepts │ │ Embeddings │
 │ Users │ │ Content │
 │ Sessions │ │ Retrieval │
 │ Mastery │ └─────────────┘
 └─────────────┘
 │
 ▼
 ┌─────────────────┐
 │ AI Pipeline │
 │ │
 │ STT │
 │ Retrieval │
 │ Evaluation │
 │ Intervention │
 │ Question Gen. │
 └─────────────────┘
```

---

# 7. The most important architectural decision: PostgreSQL is the source of truth

This is where I would strongly deviate from a typical RAG project.

The LLM should **never decide what the syllabus contains**.

For example, if the user selects:

```text
SPPU
→ B.E. AI & DS
→ 2024 Pattern
→ Semester IV
→ DBMS
```

the backend queries PostgreSQL.

```text
GET /curriculum/...
```

PostgreSQL says:

```json
{
 "subject": "Database Management Systems",
 "units": \[
 {
 "name": "Normalization",
 "topics": \[
 "Functional Dependency",
 "1NF",
 "2NF",
 "3NF",
 "BCNF"
 \]
 }
 \]
}
```

**Only then** does the AI operate on those concepts.

This guarantees curriculum accuracy.

---

# 8. Qdrant has a different job

Qdrant should answer:

> **"What information do we have about this concept?"**

Not:

> "What concepts are in the syllabus?"

For example:

```text
Query:
"Explain why a relation violates 3NF"
```

Qdrant retrieves:

```text
3NF definition
Functional dependency
Candidate key
Transitive dependency
Example schema
Common misconception
```

Then the evaluator gets those documents as grounding context.

---

# 9. Concept IDs are critical

Every concept should have a stable ID.

Example:

```text
sppu-be-aids-2024-sem4-dbms-unit3-3nf
```

But internally I'd use UUIDs and retain human-readable slugs.

Something like:

```text
concept_id:
 7e3b...

slug:
 dbms-normalization-3nf
```

Why?

Because later the same concept may exist in multiple curricula.

For example:

```text
SPPU
└── DBMS
 └── 3NF

VTU
└── DBMS
 └── 3NF

Mumbai University
└── DBMS
 └── 3NF
```

The **concept itself** can be shared.

The **curriculum mapping** can differ.

This is the key to expansion.

---

# 10. Separate Curriculum from Knowledge

This is the architecture I'd strongly recommend:

```text
 ┌───────────────┐
 │ CONCEPT │
 │ │
 │ 3NF │
 └───────┬───────┘
 │
 ┌────────────┼────────────┐
 │ │ │
 ▼ ▼ ▼
 SPPU VTU MU
 mapping mapping mapping
 │ │ │
 ▼ ▼ ▼
 Unit 3 Unit ? Unit ?
```

So:

### Curriculum

> SPPU AI&DS 2024 → DBMS → Unit III → Normalization → 3NF

### Knowledge

> 3NF → definition, examples, misconceptions, applications, prerequisites

### Assessment

> 3NF → explanation questions, application questions, misconceptions

These three should **not be mixed together**.

---

# 11. How we populate SPPU

This should be a proper **content ingestion pipeline**, not manual copy-pasting.

```text
Official SPPU syllabus PDF
 ↓
 PDF ingestion
 ↓
 Structure extraction
 ↓
University / Programme
 ↓
Pattern / Semester
 ↓
Subject
 ↓
Unit
 ↓
Topic
 ↓
Concept
 ↓
Human/AI validation
 ↓
PostgreSQL
```

SPPU publishes syllabus material through its official university infrastructure, and the university currently has multiple patterns/programmes, so storing the source document and pattern metadata is important. citeturn0search0turn0search7

For the hackathon, we should **manually validate the extracted curriculum** for our supported SPPU programme rather than blindly trusting an LLM extraction.

---

# 12. But where does the actual teaching material come from?

This is another important distinction.

The syllabus might say:

> Normalization: 1NF, 2NF, 3NF, BCNF

That is **not enough to teach the student**.

We need a content corpus.

I'd create:

```text
Knowledge Base
│
├── Official SPPU syllabus
│
├── Approved textbooks
│
├── Faculty-created explanations
│
├── Open educational resources
│
├── Examples
│
├── Practice problems
│
└── Assessment knowledge
```

Each document gets metadata:

```json
{
 "university": "SPPU",
 "programme": "BE_AI_DS",
 "pattern": "2024",
 "subject": "DBMS",
 "unit": "3",
 "topic": "Normalization",
 "concept": "3NF",
 "content_type": "explanation",
 "source": "..."
}
```

Then retrieval can be **curriculum-filtered**.

---

# 13. This gives us powerful retrieval

Suppose the student is currently studying:

```text
SPPU
BE AI&DS
2024 Pattern
Semester IV
DBMS
Unit III
Normalization
3NF
```

We should not perform a generic vector search across the entire database.

We first apply metadata filters:

```text
university = SPPU
programme = BE_AI_DS
pattern = 2024
subject = DBMS
topic = Normalization
concept = 3NF
```

Then perform semantic retrieval.

So:

**Metadata filtering → semantic search**

rather than:

**semantic search over everything**

This significantly reduces irrelevant context.

---

# 14. The TeachBack evaluator becomes much stronger

The evaluation pipeline becomes:

```text
Student explanation
 │
 ▼
Speech → Text
 │
 ▼
Current Concept
 │
 ▼
Curriculum Context
 │
 ▼
Knowledge Retrieval
 │
 ▼
Expected Concept Model
 │
 ▼
AI Evaluator
 │
 ├── Correct concepts
 ├── Missing concepts
 ├── Misconceptions
 ├── Conceptual accuracy
 ├── Application ability
 └── Confidence
```

The critical part is **Expected Concept Model**.

For 3NF, we can explicitly know what a good explanation should contain.

For example:

```text
3NF expected understanding

Must understand:
✓ Functional dependency
✓ Candidate key
✓ Non-prime attribute
✓ Transitive dependency

Should understand:
✓ Determinant condition
✓ 3NF condition
✓ Decomposition implications

Application:
✓ Determine whether relation satisfies 3NF
```

Now the AI is evaluating against a **rubric**, not merely asking another LLM:

> "Is this answer good?"

That is a much more defensible architecture.

---

# 15. This also solves your "all subjects" problem

You said:

> "all concepts in that topic from SPPU syllabus, so we will need knowledge base of all subjects and expertise in them"

I would **not** create an expert AI model for every subject.

Instead, create a **Universal Knowledge Model**.

```text
 Knowledge Model
 │
 ┌─────────────────┼──────────────────┐
 ▼ ▼ ▼
 DBMS DSA ML
 │ │ │
 concepts concepts concepts
 │ │ │
 rubrics rubrics rubrics
 │ │ │
 questions questions questions
```

The AI model stays the same.

The **knowledge + curriculum + assessment data changes**.

That's the scalable architecture.

---

# 16. Expansion to other universities

Later we can add:

```text
University
├── SPPU
│ ├── BE AI&DS
│ ├── BE Computer
│ └── BE IT
│
├── VTU
│ ├── BE CSE
│ └── BE AI&ML
│
├── MU
│ └── BE Computer
│
└── AKTU
 └── B.Tech CSE
```

No change to:

- Frontend architecture
- Evaluation engine
- RAG engine
- Mastery engine
- AI model
- Session architecture

Only the **curriculum/content data** expands.

That's exactly what we want.

---

# 17. One more thing: don't make "confidence" purely AI-generated

This is a subtle but important point.

If the student says:

> "I'm 95% confident."

that doesn't mean they understand the concept.

So TeachBack should distinguish:

### Student confidence

Self-reported:

```text
Confidence: 9/10
```

### Demonstrated understanding

AI/evaluation:

```text
Understanding: 62%
```

Then we can identify:

> **Confidence gap detected**

```text
Confidence: 92%
Demonstrated: 62%

⚠ Possible overconfidence
```

That is a **very interesting feature for TeachBack**.

---

# 18. Final frozen architecture

I would now revise our previous architecture to this:

```text
 TEACHBACK
 │
 ┌──────────┴──────────┐
 │ │
 CURRICULUM SYSTEM LEARNING SYSTEM
 │ │
 PostgreSQL PostgreSQL
 │ │
 University → Programme Sessions
 → Pattern → Semester Attempts
 → Subject → Unit Mastery
 → Topic → Concept
 │
 │
 └──────────┬──────────┘
 │
 Current Concept
 │
 ┌──────────▼──────────┐
 │ KNOWLEDGE BASE │
 │ │
 │ PostgreSQL metadata │
 │ + Qdrant vectors │
 │ + source documents │
 └──────────┬──────────┘
 │
 Relevant Context
 │
 ┌──────────▼──────────┐
 │ AI ENGINE │
 │ │
 │ STT │
 │ Evaluation │
 │ Misconception │
 │ Intervention │
 │ Question Generation │
 └──────────┬──────────┘
 │
 Structured Result
 │
 ┌──────────▼──────────┐
 │ MASTERY ENGINE │
 │ │
 │ Concept scores │
 │ Progress │
 │ Confidence gap │
 └─────────────────────┘
```

## My recommendation

**Freeze this as the architecture.**

And for the hackathon, don't try to populate *every SPPU subject* before the demo. Build the **platform architecture for all SPPU subjects**, but populate a **high-quality vertical slice** first:

> **SPPU → B.E. AI & DS → 2024 Pattern → Semester → DBMS → Normalization → 1NF/2NF/3NF/BCNF**

Once that works end-to-end, adding another subject should primarily be a **content-ingestion task, not a software-development task**.

That is the architectural property I would optimize for.

**Next, we should define the actual PostgreSQL schema + Qdrant payload schema + concept/assessment JSON contracts.** Those contracts should be frozen before we start building the ingestion pipeline or AI evaluator.

## User

in knowlwdge and assessment, lets add pyqs also

## Assistant

Worked for a couple of seconds

## Assistant

Yes. **PYQs should definitely be part of TeachBack**, and they can make the system substantially more useful for SPPU students.

But I would make one architectural correction: **PYQs should be a cross-cutting assessment resource**, rather than simply dumping them into the knowledge base.

# Updated Knowledge + Assessment Architecture

```text
 TEACHBACK KNOWLEDGE SYSTEM
 │
 ┌───────────────────┼───────────────────┐
 │ │ │
 ▼ ▼ ▼
 CURRICULUM KNOWLEDGE ASSESSMENT
 LAYER LAYER LAYER
 │ │ │
 Syllabus Concepts Questions
 Units Explanations Rubrics
 Topics Examples Misconceptions
 Concepts Applications PYQs
 Prerequisites │
 Misconceptions │
 │
 ┌──────────┴──────────┐
 │ │
 Practice Questions SPPU PYQs
```

## 1. PYQs in the Knowledge Layer

PYQs provide **exam-context knowledge**.

For example, for **3NF**, our knowledge system can know:

```text
3NF
│
├── Definition
├── Functional Dependency
├── Candidate Key
├── Transitive Dependency
├── Examples
├── Common Misconceptions
│
└── PYQ Evidence
 ├── Explain 3NF
 ├── Differentiate 2NF and 3NF
 ├── Check whether relation is in 3NF
 └── Normalize given relation
```

This tells the AI:

> **What aspects of 3NF have historically been important in SPPU examinations?**

That's valuable context.

---

# 2. PYQs in the Assessment Layer

This is where PYQs become directly useful.

Suppose the student has demonstrated basic understanding of 3NF.

Instead of generating another generic question:

> "What is 3NF?"

TeachBack can escalate to:

> **"Let's test your application of 3NF using an SPPU previous-year style question."**

Then present a PYQ or a **PYQ-derived question**.

The student solves/explains it.

The system evaluates:

```text
Conceptual Understanding 84%
Application Ability 63%
Exam Readiness 71%
```

This gives us a second dimension beyond conceptual mastery.

---

# 3. I would distinguish 3 types of questions

This is important.

### A. TeachBack Questions

Generated specifically to test understanding.

```text
"Explain 3NF in your own words."
```

Purpose:

**Conceptual understanding**

---

### B. Application Questions

Generated from the concept model.

```text
"Given R(A,B,C,D) and these dependencies,
determine whether R satisfies 3NF."
```

Purpose:

**Ability to apply the concept**

---

### C. PYQs

Actual historical SPPU questions.

```text
\[SPPU PYQ\]

"Explain 3NF with suitable example."
Year: 2024
Marks: 5
```

Purpose:

**Exam readiness**

---

# 4. This gives TeachBack a much better learning progression

Instead of:

```text
Learn
 ↓
Question
 ↓
Score
```

we get:

```text
 LEARN
 ↓
 TEACH BACK
 ↓
 Concept Understanding
 ↓
 ┌──────┴──────┐
 ↓ ↓
 Weak Area Strong Area
 ↓ ↓
 Intervention Application
 ↓ ↓
 Teach Back PYQ Practice
 ↓ ↓
 └──────┬──────┘
 ↓
 Exam Readiness
```

---

# 5. PYQ Metadata

I would store significantly more than just the question text.

For example:

```json
{
 "pyq_id": "uuid",
 "question": "Explain 3NF with suitable example.",
 "university": "SPPU",
 "programme": "BE_AI_DS",
 "pattern": "2024",
 "semester": 4,
 "subject": "DBMS",
 "unit": 3,
 "topic": "Normalization",
 "concepts": \[
 "3NF",
 "Functional Dependency"
 \],
 "year": 2024,
 "exam": "End Semester",
 "marks": 5,
 "question_type": "theory",
 "difficulty": "medium",
 "frequency": 3,
 "source": "..."
}
```

The important fields are:

- **Year**
- **Pattern**
- **Semester**
- **Subject**
- **Unit**
- **Topic**
- **Concept(s)**
- **Marks**
- **Question type**
- **Difficulty**
- **Source**

---

# 6. PYQs should be linked to concepts

This is probably the most valuable architectural decision.

Don't store:

```text
PYQ → DBMS
```

Store:

```text
PYQ
 │
 ├── 3NF
 ├── Functional Dependency
 └── Normalization
```

Then we can calculate things such as:

### SPPU Exam Frequency

```text
Normalization
━━━━━━━━━━━━━━━━━━━━

Functional Dependency ██████████
2NF ███████
3NF █████████
BCNF █████
Decomposition ████████
```

And tell the student:

> **3NF has appeared frequently in previous SPPU papers.**

That is much more useful than a generic "important topic" label.

---

# 7. PYQ Frequency becomes an additional signal

We can calculate:

```text
Concept Importance =
 Syllabus Importance
 +
 PYQ Frequency
 +
 Recent Appearance
 +
 Concept Dependency
```

For example:

| Concept | Syllabus | PYQ Frequency | Priority |
|---|---:|---:|---|
| Functional Dependency | High | High | 🔴 |
| 2NF | High | Medium | 🟠 |
| 3NF | High | High | 🔴 |
| BCNF | Medium | Medium | 🟠 |

This can eventually power:

> **"What should I study next?"**

---

# 8. Don't let the LLM invent PYQs

This should be a hard rule.

If the system says:

> **SPPU PYQ — 2023**

that question must exist in our verified PYQ database.

The LLM can:

- Explain the PYQ
- Evaluate the student's answer
- Identify concepts tested
- Generate a similar practice question
- Generate hints
- Compare the student's answer with expected concepts

But it should **never fabricate historical exam questions or their year**.

---

# 9. Actual PYQ vs PYQ-derived

We should explicitly distinguish these.

### Actual PYQ

```text
type = "PYQ"
source_verified = true
year = 2024
```

### PYQ-derived

```text
type = "PYQ_DERIVED"
source_pyq_id = ...
```

Example:

**Original PYQ**

> Explain 3NF with an example.

**Generated practice**

> A relation has functional dependencies X → Y and Y → Z. Explain whether the relation can violate 3NF and why.

The second question is **inspired by the PYQ**, but we never pretend it was actually asked by SPPU.

---

# 10. Updated Data Architecture

Our knowledge base now becomes:

```text
 KNOWLEDGE BASE
 │
 ┌───────────────────────┼────────────────────────┐
 │ │ │
 ▼ ▼ ▼
 Curriculum Concept Knowledge PYQ Corpus
 │ │ │
 ├─ Subject ├─ Definition ├─ Question
 ├─ Unit ├─ Explanation ├─ Year
 ├─ Topic ├─ Examples ├─ Marks
 └─ Concept ├─ Prerequisites ├─ Exam
 ├─ Misconceptions ├─ Concepts
 └─ Applications └─ Source
```

Then:

```text
 ASSESSMENT ENGINE
 │
 ┌────────────────┼────────────────┐
 ▼ ▼ ▼
 TeachBack Application PYQ
 Questions Questions Practice
 │ │ │
 └────────────────┼────────────────┘
 ▼
 Evaluation
 │
 ┌─────────────┼─────────────┐
 ▼ ▼ ▼
 Knowledge Application Exam
 Mastery Mastery Readiness
```

---

# 11. This gives us three meaningful scores

Instead of one arbitrary "72%" score, TeachBack can eventually show:

```text
 3NF PROGRESS

Concept Understanding 84%
Application Ability 71%
SPPU Exam Readiness 68%

Overall Mastery 76%
```

And the student gets:

> **You understand the theory of 3NF well, but your application ability needs improvement. Based on SPPU PYQs, practice relation-decomposition problems next.**

That is a **much stronger product**.

---

## Updated product loop

So I would now freeze the TeachBack learning loop as:

> **Learn → Explain → Evaluate → Correct → Apply → Practice PYQ → Reassess**

And the knowledge architecture as:

> **Curriculum + Concept Knowledge + PYQ Corpus + Assessment Rubrics**

This also reinforces our scalability goal: adding another university later means adding its **curriculum, knowledge mappings, and PYQ corpus**, while the core TeachBack engine remains unchanged.

## User

ok give mw prompt to generate just MVP just to show judges of hackathon, so that they can shortlist our team, our idea is to make:

## Assistant

Yes. For the **shortlisting MVP**, we should deliberately build a **convincing vertical slice**, not the full TeachBack platform we architected.

The prompt should tell the coding agent to **freeze scope**, use real SPPU DBMS content/PYQs, and make the demo feel like a real product.

You can give this directly to Codex/Claude Code/etc.:

:::writing{variant="document" id="58321" title="TeachBack — Hackathon MVP Build Prompt"}
# TeachBack — Hackathon MVP

## 1. Objective

Build a polished, working MVP of **TeachBack**, an AI-powered learning system whose core purpose is to determine whether a student actually understands a concept.

TeachBack is **not a generic AI tutor**.

The core product loop is:

**Learn → Explain → Evaluate → Correct → Apply → Practice PYQ → Reassess**

The MVP is being built specifically as a **hackathon judge demonstration**. The goal is to make the concept immediately understandable within a 3–5 minute demo and demonstrate enough real functionality to convince judges that the underlying product can scale.

Do not build the complete production platform. Build a highly polished vertical slice of the final architecture.

---

# 2. Product Concept

The student navigates:

**SPPU → Programme → Semester → Subject → Unit → Topic → Concept**

For the MVP, support only:

**SPPU → B.E. Artificial Intelligence & Data Science → DBMS → Normalization**

The Normalization topic should contain:

- Functional Dependency
- 1NF
- 2NF
- 3NF
- BCNF
- Decomposition

The application should demonstrate the concept most strongly using **3NF**.

The system should be architected so that additional SPPU subjects and other universities can be added later through data/content ingestion rather than rewriting application logic.

---

# 3. Core Demo Scenario

The primary demo should work like this:

### Step 1 — Select curriculum

The student sees:

```text
University
SPPU

Programme
B.E. Artificial Intelligence & Data Science

Subject
Database Management Systems

Topic
Normalization
```

Then the available concepts:

```text
Functional Dependency
1NF
2NF
3NF
BCNF
Decomposition
```

Student selects:

**3NF**

---

### Step 2 — Learn

Show a concise, well-designed learning card.

Example:

```text
3NF — Third Normal Form

A relation is in 3NF when, for every
non-trivial functional dependency X → A,
either X is a superkey or A is a prime attribute.

Key ideas:
• Functional dependency
• Candidate key
• Prime attribute
• Transitive dependency
```

Do not make the lesson unnecessarily long.

Provide:

**\[Start TeachBack\]**

---

# 4. TeachBack Interaction

Ask:

> **"Explain 3NF in your own words, as if you were teaching it to a classmate."**

Support:

### Text response

A text box where the student can type their explanation.

### Voice response

A microphone button.

The voice flow should be:

```text
Voice
 ↓
Speech-to-text
 ↓
Transcript
 ↓
Evaluation
```

For the MVP, if real STT credentials are unavailable, provide a clean fallback/demo mode rather than breaking the application.

Do not fake a successful API response while pretending real STT happened.

Clearly isolate the STT provider behind an adapter.

---

# 5. AI Evaluation

This is the most important part of the MVP.

Evaluate the student's explanation against a **structured 3NF concept rubric**.

The evaluator must identify:

### Conceptual correctness

Does the student correctly explain 3NF?

### Missing concepts

What important concepts are absent?

### Misconceptions

What did the student misunderstand?

### Confidence

Allow the student to optionally provide a self-reported confidence score.

### Ability to apply

Determine whether the student appears capable of applying the concept, rather than only recalling its definition.

---

# 6. Structured Evaluation Output

Never depend on parsing free-form LLM text.

The AI evaluator must return structured JSON matching a defined schema.

Example:

```json
{
 "overall_score": 72,
 "conceptual_correctness": 78,
 "completeness": 64,
 "application_readiness": 58,
 "confidence": 85,
 "confidence_gap": true,
 "correct_concepts": \[
 "functional dependency",
 "candidate key"
 \],
 "missing_concepts": \[
 "prime attribute",
 "transitive dependency"
 \],
 "misconceptions": \[
 {
 "concept": "3NF",
 "severity": "medium",
 "explanation": "The student is confusing the removal of transitive dependency with the complete definition of 3NF."
 }
 \],
 "recommended_action": "targeted_intervention"
}
```

Validate this response on the backend before sending it to the frontend.

---

# 7. Feedback Screen

After evaluation, show something visually impressive but academically meaningful.

Example:

```text
Your Understanding

72%
━━━━━━━━━━━━━━━━

Conceptual Correctness 78%
Completeness 64%
Application Readiness 58%

✓ Functional Dependency
✓ Candidate Key

⚠ Prime Attribute
⚠ Transitive Dependency

Possible misconception:
You are confusing the removal of
transitive dependency with the complete
definition of 3NF.
```

Then show:

### AI Intervention

Do not repeat the entire lesson.

Explain only the identified weakness.

Example:

> A transitive dependency occurs when a non-key attribute depends on another non-key attribute through the key. In 3NF, this must be handled so that every non-trivial dependency satisfies the 3NF condition.

Then:

**\[Try Again\]**

---

# 8. Second TeachBack

Ask a targeted question based on the detected weakness.

For example:

> "Consider the dependency A → B and B → C, where A is a candidate key and B and C are non-prime attributes. Explain why this can violate 3NF."

The student responds again.

Evaluate again.

Show:

```text
Previous Understanding 72%
New Understanding 86%

↑ 14 points
```

This demonstrates that TeachBack actually **adapts to the student's weakness**.

---

# 9. PYQ Integration

Integrate real/verified SPPU previous-year questions where available.

Do not fabricate PYQs.

Every PYQ must have metadata:

```text
University
Programme
Subject
Unit
Topic
Concept
Year
Marks
Exam type
Question
Source
```

Show a section:

## SPPU PYQ Practice

Example:

```text
Previous Year Question

Explain 3NF with a suitable example.

SPPU
DBMS
Normalization
5 Marks
2024
```

Allow the student to attempt the question.

The AI should evaluate whether the student demonstrates the concepts required by the PYQ.

Clearly distinguish:

**Actual PYQ**

from:

**AI-generated practice question inspired by PYQ**

Never claim an AI-generated question was asked by SPPU.

---

# 10. Knowledge Base

For the MVP, create a small but high-quality knowledge base for:

**DBMS → Normalization → 3NF**

Include:

- Definition
- Functional dependencies
- Candidate keys
- Super keys
- Prime/non-prime attributes
- Transitive dependency
- 1NF/2NF/3NF relationships
- Examples
- Counterexamples
- Common misconceptions
- Application examples
- Relevant PYQs

Use RAG where appropriate.

Do not create a huge fake knowledge base just to claim scalability.

The MVP should demonstrate the architecture using a small, trustworthy dataset.

---

# 11. Curriculum Architecture

Do NOT hard-code the UI around "DBMS → 3NF".

Create curriculum entities conceptually like:

```text
University
 ↓
Programme
 ↓
Pattern
 ↓
Semester
 ↓
Subject
 ↓
Unit
 ↓
Topic
 ↓
Concept
```

For the MVP, populate only the relevant SPPU DBMS Normalization data.

The architecture must allow another subject to be added through data without changing the evaluation engine.

---

# 12. Recommended MVP Architecture

Use a simple architecture.

```text
React + TypeScript
 │
 │ REST
 ▼
FastAPI Backend
 │
 ├── Curriculum Service
 ├── Learning Service
 ├── TeachBack Service
 ├── Evaluation Service
 ├── PYQ Service
 └── Mastery Service
 │
 ├───────────────┐
 ▼ ▼
 PostgreSQL Qdrant
 │ │
 Curriculum Knowledge
 Sessions Embeddings
 Mastery Retrieval
 PYQs
 │
 ▼
 AI Layer
 │
 ├── LLM
 ├── Embeddings
 └── STT
```

Do NOT introduce microservices.

Do NOT introduce Kafka.

Do NOT introduce Kubernetes.

Do NOT introduce an agent swarm.

Do NOT build unnecessary infrastructure.

This is a hackathon MVP.

---

# 13. Technology

Use:

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS

### Backend

- Python
- FastAPI
- Pydantic

### Database

- PostgreSQL

### Vector database

- Qdrant

If Qdrant significantly slows down the MVP, implement a clean vector-store abstraction and allow a local/simple implementation for the demo.

### AI

Use the configured LLM provider/model through environment variables.

Do not hard-code API keys.

### STT

Use Sarvam STT through an adapter.

The architecture must allow replacing the STT provider later.

---

# 14. Repository Structure

Create a clean structure similar to:

```text
teachback/
│
├── frontend/
│
├── backend/
│ ├── app/
│ │ ├── api/
│ │ ├── schemas/
│ │ ├── services/
│ │ ├── ai/
│ │ ├── db/
│ │ └── core/
│ │
│ └── tests/
│
├── knowledge/
│ ├── curriculum/
│ ├── concepts/
│ ├── pyqs/
│ └── sources/
│
├── scripts/
│ ├── ingest_curriculum.py
│ ├── ingest_knowledge.py
│ └── ingest_pyqs.py
│
├── docker/
│
├── docs/
│
├── .env.example
├── docker-compose.yml
└── README.md
```

Keep the implementation minimal.

---

# 15. Important Design Principle

The LLM must NOT decide what the syllabus contains.

The curriculum database is the source of truth.

The LLM operates on:

```text
Current curriculum context
+
Current concept
+
Retrieved knowledge
+
Assessment rubric
+
Student response
```

Then produces a structured evaluation.

---

# 16. Evaluation Rubric

Create a deterministic concept rubric for 3NF.

Example:

```text
3NF RUBRIC

Required concepts:

1. Functional Dependency
2. Candidate/Super Key
3. Prime Attribute
4. Non-Prime Attribute
5. Transitive Dependency
6. 3NF condition

Application:

1. Identify functional dependencies
2. Identify candidate key
3. Identify prime/non-prime attributes
4. Detect transitive dependency
5. Determine whether relation satisfies 3NF
```

The evaluator should use this rubric rather than relying entirely on model intuition.

---

# 17. Confidence Gap

Add one small but impressive feature.

Ask:

> "How confident are you in your answer?"

Student selects:

```text
1 2 3 4 5
```

Compare this with demonstrated understanding.

Example:

```text
Confidence 90%
Demonstrated 61%

⚠ Confidence Gap

You appear more confident than
your demonstrated understanding
of this concept suggests.
```

This should be presented carefully as an **indicator**, not a psychological diagnosis.

---

# 18. Mastery

For MVP, maintain concept-level mastery.

Example:

```text
Normalization

Functional Dependency 91%
1NF 88%
2NF 73%
3NF 86%
BCNF 42%
```

Do not build a complex machine-learning mastery model.

Use a transparent scoring mechanism based on evaluation results.

---

# 19. Demo Mode

The application must have a reliable demo path.

Create a seeded demo account/session or allow the judge to enter directly into the experience.

The demo should never depend on:

- Random LLM output
- Missing database records
- Manual backend intervention
- Hard-coded frontend screenshots

However, external AI providers may fail.

Therefore implement graceful fallback handling.

If an AI request fails:

```text
AI service temporarily unavailable.

\[Try Again\]
```

Do not silently display fake AI results.

---

# 20. UI Requirements

The UI should look like a serious modern education product.

Prioritize:

- Clean typography
- Excellent spacing
- Clear hierarchy
- Responsive layout
- Progress indicators
- Concept mastery visualization
- Smooth transitions
- Loading states
- Error states
- Voice recording state
- Evaluation state

Avoid excessive animations.

The important information should be visible immediately.

---

# 21. Judge Demo Flow

Optimize the application specifically for this sequence:

### 0:00–0:30

Select:

```text
SPPU
→ AI & DS
→ DBMS
→ Normalization
→ 3NF
```

### 0:30–1:00

AI gives concise concept explanation.

### 1:00–1:45

Student explains 3NF incorrectly/incompletely.

### 1:45–2:15

TeachBack detects:

```text
72% understanding

Missing:
• Prime attribute
• Transitive dependency

Misconception:
Confusing 2NF and 3NF
```

### 2:15–2:45

AI provides targeted intervention.

### 2:45–3:15

Student answers the targeted question.

Score improves:

```text
72% → 86%
```

### 3:15–3:45

Show:

**SPPU PYQ**

and demonstrate application/exam readiness.

### 3:45–4:00

Show the larger vision:

```text
Today
SPPU → AI&DS → DBMS

Tomorrow
SPPU → All Engineering Subjects
 ↓
Other Universities
 ↓
Personalized AI Learning
```

---

# 22. What NOT to build

Strictly avoid scope creep.

Do NOT implement:

- Social features
- Teacher accounts
- Parent accounts
- Leaderboards
- Chatbot mode
- Video generation
- Recommendation marketplace
- Payment system
- Mobile app
- Complex analytics
- Full SPPU database
- Multiple universities
- Multi-agent architecture
- Autonomous agents
- Fine-tuning models
- Custom ML models for grading
- Complex Neo4j graph infrastructure

The MVP succeeds if one concept works **extremely well**.

---

# 23. Acceptance Criteria

The MVP is considered complete only when this works end-to-end:

```text
SPPU
 ↓
AI & DS
 ↓
DBMS
 ↓
Normalization
 ↓
3NF
 ↓
Learn
 ↓
TeachBack
 ↓
Text/Voice response
 ↓
AI evaluation
 ↓
Structured misconception detection
 ↓
Targeted intervention
 ↓
Follow-up question
 ↓
Improved evaluation
 ↓
PYQ practice
 ↓
Mastery update
```

A judge should be able to understand the product without us explaining the architecture for five minutes.

---

# 24. Implementation Strategy

Build in this order:

### Phase 1
Repository + database + curriculum data

### Phase 2
Frontend curriculum navigation

### Phase 3
Concept learning page

### Phase 4
TeachBack text interaction

### Phase 5
Structured AI evaluation

### Phase 6
Targeted intervention + second attempt

### Phase 7
PYQ integration

### Phase 8
Mastery visualization

### Phase 9
Voice/STT

### Phase 10
UI polish + demo reliability

Do not start with voice.

The **TeachBack evaluation loop is the product**. Voice is an enhancement.

---

# 25. Definition of Done

Do not declare success because the UI looks good.

The MVP is successful when a judge can see:

> **The system knows what the student was supposed to learn, listens to what the student actually understands, identifies exactly where they are wrong, gives targeted remediation, and verifies improvement.**

That is the core innovation.

Build toward this statement above everything else.

:::

## User

just one sem one subject one topic because i want to record a video for shortlisting process

## Assistant

Exactly. For the **shortlisting video**, we should make the MVP much narrower. Don't build the platform yet.

The demo should prove **one thing extremely well**:

> **TeachBack can take a student from learning one concept → explaining it → detecting the misunderstanding → teaching the missing part → testing them again.**

I'd freeze the video MVP as:

```text
SPPU
 ↓
B.E. AI & Data Science
 ↓
Semester IV
 ↓
DBMS
 ↓
Normalization
 ↓
3NF
```

Everything else can be shown as future scalability.

Here is the **revised prompt** I'd give to the coding agent:

:::writing{variant="document" id="74126" title="TeachBack — Shortlisting Video MVP"}
# TeachBack — Shortlisting Video MVP

Build a **small, polished, end-to-end MVP of TeachBack** specifically for a hackathon shortlisting video.

Do NOT build the complete TeachBack platform.

The purpose of this MVP is to demonstrate the core product idea convincingly in a **2–4 minute recorded demo**.

---

# 1. Product

**TeachBack — AI That Knows Whether You Actually Understand**

TeachBack is not a generic AI tutor.

The core loop is:

**Learn → Explain → Evaluate → Correct → Re-explain → Improve**

The system should determine whether a student actually understands a concept by asking them to explain it in their own words.

---

# 2. STRICT MVP SCOPE

Support exactly:

```text
University:
SPPU

Programme:
B.E. Artificial Intelligence & Data Science

Semester:
Semester IV

Subject:
Database Management Systems (DBMS)

Topic:
Normalization

Concept:
3NF — Third Normal Form
```

Do NOT build:

- Other semesters
- Other subjects
- Other topics
- Other universities
- Teacher dashboard
- Student social features
- Leaderboards
- Full LMS
- Mobile app
- Complex analytics
- Neo4j
- Microservices
- Agent architecture

We only need one excellent demonstration.

---

# 3. What the Video Must Demonstrate

The video should show this exact journey:

```text
SPPU
 ↓
AI & DS
 ↓
Semester IV
 ↓
DBMS
 ↓
Normalization
 ↓
3NF
 ↓
Learn
 ↓
TeachBack
 ↓
Student explains
 ↓
AI evaluates
 ↓
Misconception detected
 ↓
Targeted intervention
 ↓
Student explains again
 ↓
Understanding improves
 ↓
SPPU PYQ
```

The judge should understand the entire product within a few minutes.

---

# 4. Application Screens

Build approximately 5 screens.

## Screen 1 — Curriculum Selection

Create a polished selection interface.

Show:

```text
University
SPPU

Programme
B.E. Artificial Intelligence & Data Science

Semester
Semester IV

Subject
Database Management Systems

Topic
Normalization
```

Then:

```text
Concepts

Functional Dependency
1NF
2NF
→ 3NF
BCNF
Decomposition
```

Only **3NF** needs to be fully functional.

Click:

**Start Learning**

---

# 5. Screen 2 — Learn

Show a concise explanation of 3NF.

Example:

```text
3NF — Third Normal Form

A relation is in Third Normal Form when,
for every non-trivial functional dependency
X → A, either X is a superkey or A is a
prime attribute.

Key concepts:

• Functional Dependency
• Candidate Key
• Prime Attribute
• Non-Prime Attribute
• Transitive Dependency
```

Include a simple example.

Do not overload the page with textbook content.

At the bottom:

**\[ Start TeachBack \]**

---

# 6. Screen 3 — TeachBack

This is the HERO screen.

Display:

> **Can you teach this concept?**

Then:

> "Explain 3NF in your own words as if you were teaching it to a classmate."

Provide:

```text
┌──────────────────────────────────┐
│ │
│ Type your explanation here... │
│ │
│ │
└──────────────────────────────────┘

 🎙 Record Answer

 \[ Submit Answer \]
```

Support text input.

Add voice input if practical.

If voice is implemented, use real STT through an adapter.

Do not let voice integration delay the core demo.

---

# 7. Screen 4 — AI Evaluation

After submission, show a polished evaluation state.

Then display:

```text
Your Understanding

72%
━━━━━━━━━━━━━━━━━━━━

Conceptual Correctness 78%
Completeness 64%
Application Readiness 58%

✓ Functional Dependency
✓ Candidate Key

⚠ Prime Attribute
⚠ Transitive Dependency
```

Then:

### Misconception Detected

> You understand functional dependencies, but you are confusing the role of transitive dependencies in 3NF.

Then show:

### Targeted Feedback

> In 3NF, a non-trivial dependency must have a superkey as its determinant, or its dependent attribute must be prime. The important point is that simply removing duplicate data does not define 3NF.

Then:

**\[ Try Again \]**

The feedback must be based on the student's actual response.

---

# 8. Second TeachBack

Do NOT ask the exact same question.

Generate a targeted question based on the detected weakness.

Example:

> "Suppose A is a candidate key and A → B and B → C, where B and C are non-prime attributes. Explain why this may violate 3NF."

Student answers.

Evaluate again.

Display:

```text
Understanding Improved

72% → 86%

↑ 14 points
```

This improvement is the most important moment of the demo.

The judge should immediately understand:

> TeachBack doesn't simply give an answer. It identifies the student's weakness and verifies whether the intervention worked.

---

# 9. PYQ Screen

After the second successful TeachBack, show:

## Test Your Exam Readiness

Display a **verified SPPU PYQ** related to Normalization/3NF.

Example structure:

```text
SPPU Previous Year Question

Explain 3NF with a suitable example.

DBMS
Normalization
5 Marks
\[Year\]
```

Use only an actual verified PYQ.

Do not fabricate the year or claim an AI-generated question is an SPPU question.

Allow the student to attempt it.

The AI should evaluate whether the response covers the required concepts.

---

# 10. Data

For this MVP, create a small curated knowledge base specifically for:

**DBMS → Normalization → 3NF**

Include:

### Concept knowledge

- 3NF definition
- Functional dependency
- Candidate key
- Super key
- Prime attribute
- Non-prime attribute
- Transitive dependency
- 2NF vs 3NF
- Examples
- Counterexamples
- Common misconceptions
- Application examples

### Assessment knowledge

- TeachBack questions
- Application questions
- 3NF evaluation rubric
- Targeted intervention examples

### PYQs

Include a small set of verified SPPU PYQs related to Normalization.

Every PYQ must have:

```text
question
year
marks
subject
topic
concept
source
```

---

# 11. 3NF Evaluation Rubric

Create a structured rubric.

The evaluator should check whether the student's explanation demonstrates:

```text
Functional Dependency
Candidate/Super Key
Prime Attribute
Non-Prime Attribute
Transitive Dependency
3NF condition
```

For application questions:

```text
Identify functional dependencies
Identify candidate key
Identify prime/non-prime attributes
Identify transitive dependency
Determine whether relation satisfies 3NF
```

The LLM must evaluate against this rubric.

Do not simply ask:

> "Is the student's answer correct?"

---

# 12. Structured AI Output

The evaluator must return structured JSON.

Example:

```json
{
 "overall_score": 72,
 "conceptual_correctness": 78,
 "completeness": 64,
 "application_readiness": 58,
 "correct_concepts": \[
 "functional_dependency",
 "candidate_key"
 \],
 "missing_concepts": \[
 "prime_attribute",
 "transitive_dependency"
 \],
 "misconceptions": \[
 {
 "concept": "3NF",
 "severity": "medium",
 "explanation": "..."
 }
 \],
 "recommended_action": "targeted_intervention"
}
```

Validate the response using Pydantic.

Do not parse scores from natural-language AI output.

---

# 13. Architecture

Keep the architecture minimal.

```text
React + TypeScript
 │
 │ REST
 ▼
FastAPI
 │
 ├── Curriculum
 ├── Learning
 ├── TeachBack
 ├── Evaluation
 └── PYQ
 │
 ├──────────────┐
 ▼ ▼
 PostgreSQL Qdrant
 │ │
 Curriculum 3NF Knowledge
 PYQs Embeddings
 Session Retrieval
 Evaluation
```

For this MVP, it is acceptable to simplify further if Qdrant adds unnecessary setup complexity.

The architecture must still keep retrieval behind an abstraction so Qdrant can be introduced without changing the application layer.

Do NOT add Neo4j.

Do NOT add microservices.

Do NOT add Kafka.

Do NOT add Kubernetes.

---

# 14. Important Product Rule

The application must not pretend that the LLM knows the SPPU syllabus.

The curriculum data is the source of truth.

The AI receives:

```text
Current curriculum
+
Current concept
+
Concept rubric
+
Retrieved knowledge
+
Student response
```

and produces the evaluation.

---

# 15. UI Design

The UI should look like a polished modern AI education product suitable for a hackathon presentation.

Prioritize:

- Clean typography
- Strong visual hierarchy
- Minimal interface
- Progress indicators
- Concept mastery
- Evaluation cards
- Clear misconception highlighting
- Smooth loading states
- Professional dashboard

Avoid unnecessary animations.

The **evaluation and improvement screens should receive the most visual attention**.

---

# 16. Demo Reliability

The application must have a deterministic demo path.

Seed the required:

```text
SPPU
AI & DS
Semester IV
DBMS
Normalization
3NF
```

and all required knowledge/PYQ data.

Do not require the developer to manually insert data during the recording.

If an external AI service fails, show a proper error state.

Do not silently fake a successful AI response.

For development/testing, provide a clearly separated mock provider that can reproduce the demo flow without external API calls.

---

# 17. Future Scalability

Do NOT implement additional universities now.

However, do not hard-code the database schema or service interfaces around 3NF.

The data model should conceptually support:

```text
University
 → Programme
 → Pattern
 → Semester
 → Subject
 → Unit
 → Topic
 → Concept
```

Today:

```text
SPPU → AI&DS → Sem IV → DBMS → Normalization → 3NF
```

Future:

```text
SPPU → Other subjects
VTU → Other programmes
MU → Other programmes
```

Adding these later should primarily be a content-ingestion problem, not a rewrite of the AI engine.

---

# 18. Shortlisting Video Target

The complete demo should be recordable in approximately **2–4 minutes**.

Recommended sequence:

### 0:00–0:20
Show the product and select:

**SPPU → AI&DS → Semester IV → DBMS → Normalization → 3NF**

### 0:20–0:45
Show the short AI lesson.

### 0:45–1:20
Student gives an incomplete explanation.

### 1:20–1:50
TeachBack detects the specific misconception.

### 1:50–2:15
AI provides targeted intervention.

### 2:15–2:45
Student answers the targeted question.

### 2:45–3:00
Show:

**72% → 86%**

### 3:00–3:30
Show SPPU PYQ and exam-readiness evaluation.

### 3:30–4:00
End with the scalability vision:

```text
Today:
One SPPU subject + one topic

Architecture:
Curriculum-aware + knowledge-grounded

Future:
All SPPU subjects
 ↓
Other Universities
 ↓
Personalized AI learning
```

---

# 19. Definition of Done

The MVP is complete only when the following works without manual intervention:

```text
Select 3NF
 ↓
Learn 3NF
 ↓
Explain 3NF
 ↓
AI evaluates explanation
 ↓
Specific misconception detected
 ↓
Targeted intervention
 ↓
Targeted question
 ↓
Student answers again
 ↓
Understanding improves
 ↓
SPPU PYQ
 ↓
Exam readiness
```

The MVP should make the following statement demonstrably true:

> **TeachBack doesn't just tell students the answer. It determines what they understand, identifies what they don't understand, teaches the missing concept, and verifies improvement.**

Do not expand the scope until this exact flow is stable, polished, and recordable.
:::

## User

and frontend should look good quality not ai slop. and make mvp such that if we do get selected picking up and completing it completely is not difficult

## Assistant

Yes. That should be an explicit requirement in the build prompt.

The mistake would be building a **throwaway hackathon prototype** that looks impressive in a video but becomes painful to continue. We should instead build a **small production-shaped vertical slice**: narrow in data, but clean in architecture.

I would add these requirements to the previous prompt:

:::writing{variant="document" id="31684" title="TeachBack — Final MVP Engineering & UI Requirements"}
# TeachBack — Final MVP Engineering & UI Requirements

These requirements extend the existing TeachBack shortlisting MVP specification.

The MVP has two equally important goals:

1. **Look polished enough to make judges take the product seriously.**
2. **Be architecturally clean enough that, if selected, the team can continue development without throwing away the MVP.**

The MVP is intentionally narrow in **content scope**, not careless in **engineering quality**.

---

# 1. Product Scope — DO NOT EXPAND

The functional demo remains exactly:

```text
SPPU
 → B.E. Artificial Intelligence & Data Science
 → Semester IV
 → DBMS
 → Normalization
 → 3NF
```

Only 3NF needs the complete TeachBack loop.

Do not implement additional subjects or universities.

However, the software architecture must be reusable.

---

# 2. IMPORTANT PRINCIPLE

Build:

> **A production-shaped vertical slice, not a disposable prototype.**

This means:

### Narrow data

Only one subject/topic/concept.

### Clean architecture

The services, database schema, API contracts, AI adapters, and frontend components should already support future expansion.

If the team gets selected, we should be able to continue by:

```text
adding data
+
adding ingestion
+
adding concepts
+
adding PYQs
+
adding evaluation rubrics
```

rather than rewriting the application.

---

# 3. Frontend Quality Is A Core Requirement

The frontend must NOT look like generic AI-generated UI.

Avoid the typical:

- Huge gradient hero
- Excessive glassmorphism
- Neon purple AI aesthetic
- Floating glowing blobs
- Excessive rounded cards
- Random dashboard charts
- Generic "AI-powered" badges
- Excessive shadows
- Unnecessary animations
- Every section inside a card
- Giant text with little information
- Stock AI illustrations

The product should look like a **real education product designed by a professional product/UI team**.

Think:

**calm + academic + modern + focused**

rather than:

**"look, this is AI!"**

---

# 4. Visual Design Direction

Use a restrained design system.

### Typography

Use a high-quality modern sans-serif such as:

- Inter
- Geist
- Plus Jakarta Sans

Choose ONE and use it consistently.

### Layout

Prefer:

```text
wide content area
clear hierarchy
generous whitespace
strong alignment
consistent spacing
```

Do not fill the screen with cards.

### Color

Use a restrained primary color and neutral palette.

AI should not be represented through gradients everywhere.

Use color primarily for meaning:

```text
Normal
Positive
Warning
Error
Information
```

For example:

```text
✓ Correct concept
⚠ Needs attention
✕ Misconception
```

Do not use color alone to communicate information.

---

# 5. Create A Small Design System

Before building pages, define:

```text
colors
typography
spacing
border radius
shadows
buttons
inputs
cards
badges
progress indicators
modal/dialog
toast
loading states
```

Create reusable components.

For example:

```text
components/
├── Button
├── Select
├── ProgressBar
├── ConceptBadge
├── ScoreCard
├── EvaluationSection
├── MisconceptionCard
├── QuestionCard
├── AudioRecorder
└── PageHeader
```

Do not duplicate styles across pages.

---

# 6. Navigation Should Feel Like A Learning Product

Use a simple application shell.

Example:

```text
┌──────────────────────────────────────────────────────┐
│ TeachBack Profile │
├──────────────┬───────────────────────────────────────┤
│ │ │
│ My Learning │ │
│ │ │
│ Curriculum │ Main Learning Area │
│ │ │
│ Progress │ │
│ │ │
└──────────────┴───────────────────────────────────────┘
```

But don't create unnecessary pages.

For the demo, navigation can be minimal.

---

# 7. Curriculum Selection Should Feel Real

Instead of five giant dropdown cards, create a clear academic hierarchy.

Example:

```text
Learning Path

SPPU
B.E. Artificial Intelligence & Data Science
Semester IV
Database Management Systems

Normalization

Concepts
────────────────────────────────────

✓ Functional Dependency
✓ 1NF
✓ 2NF
→ 3NF
○ BCNF
○ Decomposition
```

The selected concept should have an obvious active state.

This should communicate:

> "I know exactly where I am in the curriculum."

---

# 8. Learning Page

The learning page should feel like a proper educational reading experience.

Example structure:

```text
Normalization / 3NF

3NF — Third Normal Form

Short explanation...

Key idea

Functional dependency...

Example

...

Common mistake

...

────────────────────────────

Ready to explain it?

\[ Start TeachBack \]
```

Do not turn every paragraph into a separate card.

Use typography and spacing to create hierarchy.

---

# 9. TeachBack Page Should Be The Hero

This is the most important screen.

The UI should create a feeling of:

> "Now I have to prove that I understand this."

Example:

```text
3NF
TeachBack

Can you teach this concept?

Explain 3NF as if you were
teaching it to a classmate.

────────────────────────────────

\[ Write your explanation... \]

 0/1000

 🎙 Record answer

────────────────────────────────

 \[ Submit \]
```

The interface should feel focused and distraction-free.

---

# 10. Evaluation Experience

Do not immediately dump a wall of AI-generated text onto the screen.

Use progressive information hierarchy.

First:

```text
Your understanding

72%
```

Then:

```text
Conceptual correctness 78%
Completeness 64%
Application readiness 58%
```

Then:

```text
What you got right

✓ Functional dependency
✓ Candidate key
```

Then:

```text
What needs attention

⚠ Prime attribute
⚠ Transitive dependency
```

Then:

```text
Misconception detected

You are confusing...
```

Then:

```text
Targeted explanation
```

This makes the evaluation feel like a **diagnostic report**, not a chatbot response.

---

# 11. Avoid Fake "AI Thinking"

Do not implement fake animations such as:

```text
AI is thinking...
Analyzing neural patterns...
Understanding your response...
```

Do not create fake terminal logs.

Use a simple professional loading state:

```text
Evaluating your explanation...
```

with a subtle progress indicator.

The product should demonstrate actual intelligence through the result.

---

# 12. Score Visualization

Do not create a giant circular gauge just because it looks "AI".

A clean score presentation is preferable:

```text
72%

Understanding
━━━━━━━━━━━━━━━━━━░░░

↑ 14 points from previous attempt
```

Use meaningful comparison.

The improvement is more important than the number itself.

---

# 13. Misconception UI

This is a key product feature.

Make it visually distinct.

Example:

```text
MISCONCEPTION

2NF vs 3NF

You correctly identified functional
dependencies, but your explanation
suggests that removing partial
dependencies is sufficient for 3NF.

Why this matters

3NF also considers transitive
dependencies...
```

Then:

**\[Explain This Concept\]**

This should feel like the system has diagnosed the student.

---

# 14. Second Attempt

Make improvement visually obvious.

Before:

```text
72%
```

After:

```text
86%
```

Then:

```text
+14 points

Your explanation now correctly
covers transitive dependency.
```

This is likely the strongest moment in the video.

---

# 15. PYQ Experience

Do not make the PYQ look like another random card.

Make it resemble an examination question.

Example:

```text
SPPU • DBMS • 5 Marks

Previous Year Question

Explain Third Normal Form (3NF)
with a suitable example.

────────────────────────────

Concepts tested

Functional Dependency
Candidate Key
Transitive Dependency

\[ Attempt Question \]
```

This connects:

**understanding → application → exam preparation**

which strengthens the product story.

---

# 16. Backend Architecture

Keep the backend production-shaped.

Use:

```text
backend/
└── app/
 ├── api/
 │ ├── curriculum.py
 │ ├── learning.py
 │ ├── teachback.py
 │ ├── pyq.py
 │ └── health.py
 │
 ├── schemas/
 │ ├── curriculum.py
 │ ├── teachback.py
 │ ├── evaluation.py
 │ └── pyq.py
 │
 ├── services/
 │ ├── curriculum_service.py
 │ ├── learning_service.py
 │ ├── teachback_service.py
 │ ├── evaluation_service.py
 │ └── mastery_service.py
 │
 ├── ai/
 │ ├── llm.py
 │ ├── stt.py
 │ ├── embeddings.py
 │ └── prompts/
 │
 ├── db/
 │ ├── models/
 │ └── session.py
 │
 └── core/
 └── config.py
```

Keep business logic out of API route handlers.

---

# 17. AI Provider Abstraction

Do not call the LLM directly from random files.

Create an interface similar to:

```text
LLMProvider
 └── SarvamProvider
```

Likewise:

```text
STTProvider
 └── SarvamSTTProvider
```

and:

```text
EmbeddingProvider
 └── MultilingualEmbeddingProvider
```

This means if the hackathon infrastructure changes later, we replace the adapter instead of rewriting the evaluation engine.

---

# 18. Prompt Management

Do NOT bury giant prompts inside Python functions.

Store them separately:

```text
ai/
└── prompts/
 ├── evaluate_teachback.txt
 ├── generate_intervention.txt
 ├── generate_followup.txt
 └── evaluate_pyq.txt
```

Version them.

The evaluator should receive explicit:

```text
curriculum context
concept definition
expected concepts
misconceptions
retrieved knowledge
student response
```

This will make later prompt improvement much easier.

---

# 19. Database Design

Even though the MVP contains one subject, don't create tables such as:

```text
dbms_3nf_questions
dbms_3nf_answers
```

Instead use generic entities.

Conceptually:

```text
universities
programmes
patterns
semesters
subjects
units
topics
concepts

pyqs
concept_pyqs

sessions
attempts
evaluations
mastery
```

Today they contain:

```text
SPPU
AI&DS
Semester IV
DBMS
Normalization
3NF
```

Tomorrow they can contain thousands of concepts.

---

# 20. Data Ingestion Must Be Separate From Application Code

Create seed/ingestion data:

```text
knowledge/
├── curriculum/
│ └── sppu_ai_ds_sem4.json
│
├── concepts/
│ └── dbms_normalization.json
│
└── pyqs/
 └── dbms_normalization.json
```

Create scripts that load this data.

Do not hard-code syllabus data inside React components or FastAPI routes.

This is extremely important for future expansion.

---

# 21. RAG Architecture

Keep retrieval isolated:

```text
KnowledgeRetriever
 │
 ├── metadata filter
 └── semantic search
```

The evaluator should not know whether the knowledge came from:

- Qdrant
- PostgreSQL
- local JSON
- another vector database

It only receives:

```text
RetrievedKnowledge\[\]
```

This makes the architecture easier to expand.

---

# 22. Don't Overbuild RAG

For the MVP, the knowledge corpus is tiny.

Do not create an elaborate multi-stage RAG pipeline.

Use:

```text
Current concept
 ↓
metadata filtering
 ↓
vector retrieval
 ↓
top relevant chunks
 ↓
evaluation
```

That's sufficient.

If Qdrant adds too much operational overhead for the first demo, implement a clean retrieval interface with a local backend first.

---

# 23. Testing

Even for a hackathon MVP, create basic tests for the most important logic.

At minimum:

### Evaluation schema

Invalid AI output should be rejected.

### Curriculum

3NF must belong to:

```text
SPPU → AI&DS → Sem IV → DBMS → Normalization
```

### Session

A second TeachBack attempt must belong to the same session.

### Mastery

A valid second evaluation should update mastery.

### PYQ

PYQs must contain valid source metadata.

Do not spend days writing tests.

Test the critical contracts.

---

# 24. Environment Configuration

Use:

```text
.env
.env.example
```

Example:

```text
LLM_API_KEY=
LLM_MODEL=
STT_API_KEY=
DATABASE_URL=
QDRANT_URL=
QDRANT_API_KEY=
```

Never hard-code credentials.

The project should run locally using documented setup instructions.

---

# 25. Documentation

Create a concise README containing:

```text
1. What TeachBack is
2. Architecture
3. MVP scope
4. Setup
5. Environment variables
6. Running locally
7. Loading demo data
8. Running tests
9. Demo flow
10. Future expansion
```

Also include an architecture diagram.

The README should make it possible for another teammate to understand the project without asking the original developer.

---

# 26. Future Development Must Be Additive

After the hackathon, these should be possible without changing the core:

```text
Add another concept
 ↓
Add another topic
 ↓
Add another subject
 ↓
Add another semester
 ↓
Add another SPPU programme
 ↓
Add another university
 ↓
Add multilingual content
 ↓
Add teacher dashboard
```

The core TeachBack engine should remain:

```text
Curriculum
 ↓
Concept
 ↓
Knowledge
 ↓
Student explanation
 ↓
Evaluation
 ↓
Intervention
 ↓
Reassessment
```

---

# 27. Definition of Engineering Success

Do not optimize for the number of features.

The MVP is successful if:

### Product

A judge immediately understands the problem and solution.

### UX

The application looks like a real product rather than an AI-generated demo.

### AI

The system identifies a real weakness in the student's explanation.

### Adaptation

The second question is based on that weakness.

### Measurability

The system demonstrates improvement.

### Architecture

The implementation can continue into the full product without being rewritten.

---

# 28. Final Rule

Before adding any feature ask:

> **Does this improve the 3NF TeachBack demonstration or make the eventual product easier to build?**

If the answer is no, do not build it.

The goal is:

**Small scope + high polish + real AI behavior + clean architecture.**

Not:

**Large scope + shallow features + impressive-looking screenshots.**
:::

## User

our teach back was rejected, time for new idea

## Assistant

Yep 😭 — and the screenshot changes the game: **Smart Education/HealthTech/FinTech are gone**, while the finale tracks now include **Mobility, Community App, Smart Living, Productivity, Developer Tools, and Open Innovation**.

TeachBack being rejected means I would **not reskin it**. We should pick something built specifically for these finale tracks.

Given your AI/RAG/agents + Python/full-stack background, my first instinct is **Developer Tools or Productivity**. Those let us build something technically impressive without hardware dependencies.

I’d target ideas with a demo like: **input something messy → AI actually takes/coordinates actions → visible result in <60 seconds**, rather than another chat interface.

A few directions I think have real potential: an **AI incident investigator** that ingests logs/errors + repo context and traces the likely failure across files/services; a **local-first developer memory** that understands a codebase and automatically maintains architectural/project context across coding-agent sessions; an **AI workflow recorder** where you demonstrate a repetitive desktop/browser task once and it generates a reusable automation with human approval gates; or a **community coordination agent** that turns a messy group/community stream into decisions, tasks, duplicate-question resolution, and member-to-member matching.

But I don't want to throw another 20 generic ideas at you like last time. **We should search what is already winning/launching in AI developer tools, productivity, on-device AI, and hackathons right now, then find an underserved problem that fits these exact tracks.** That'll give us a much better shot than brainstorming in isolation.

## Resources

### Local attachments
- [1000089089.jpg](../../../Raw/Export/file_0000000075308207a1242e9896d1c593.dat)
- [a4162cfc-9a2b-4b43-9dfc-1c48ad64f2a4.png](../../../Raw/Export/file_00000000f90081fab23e0f8c05e37200.dat)

### External references
- [HH Task_2](https://chatgpt.com/c/6a81ac51-7894-83ee-9d19-b4c68d755e51)
- [SPPU - Internal Marks Sytem](https://intmarks.unipune.ac.in/default.aspx?utm_source=chatgpt.com)
- [Login](https://pcrtada.unipune.ac.in/Student/Dashboard/LogintoSPS?utm_source=chatgpt.com)
- [Entrance Test Syllabus | MTech Programme in M&amp;S | Academic Programmes | Centre for Modeling and Simulation | Savitribai Phule Pune University](https://scms.unipune.ac.in/programmes/oee-syllabus-mtech.shtml?utm_source=chatgpt.com)
- [Result](https://onlineresults.unipune.ac.in/SPPU?utm_source=chatgpt.com)
- [Academic : Department of Computer Science : University of Pune](https://beta.unipune.ac.in/dept/science/computer_science/cs_webfiles/academic.htm?utm_source=chatgpt.com)
- [Boards And Meetings Circulars](https://sppudocs.unipune.ac.in/sites/circulars/_layouts/mobile/view.aspx?List=85ab0d02-7304-478b-a04b-240d0a46dcae&View=96b19d89-ba06-4885-ac3b-89f4a3053952&ViewMode=Detail&utm_source=chatgpt.com)
- [Academic : Department of Computer Science : University of Pune](https://www.unipune.ac.in/dept/science/computer_science/cs_webfiles/academic.htm?utm_source=chatgpt.com)
- [Dattakala Group of Institutions](https://bcud.unipune.ac.in/utilities/college_search/CEGP015700_ENG/Pune_University_College?utm_source=chatgpt.com)
- [Ajeenkya DY Patil School of Engineering](https://bcud.unipune.ac.in/utilities/college_search/CEGP015720_ENG/Pune_University_College?utm_source=chatgpt.com)
- [D.Y.Patil College of Engineering](https://bcud.unipune.ac.in/utilities/college_search/CEGP010530_ENG/Pune_University_College?utm_source=chatgpt.com)
- [Dr.D.Y.Patil Institute of Technology,](https://bcud.unipune.ac.in/utilities/college_search/CEGP014270_ENG/Pune_University_College?utm_source=chatgpt.com)
- [Login](https://exampcr.unipune.ac.in/Student/Dashboard/LogintoSPS/bonus%20ios%20ninja%20app?utm_source=chatgpt.com)
- [Jayawantrao Sawant College of Engineering](https://bcud.unipune.ac.in/utilities/college_search/CEGP012120_ENG/Pune_University_College?utm_source=chatgpt.com)
- [unipune.ac.in](https://exampcr.unipune.ac.in/Student/Dashboard/CheckDates?utm_source=chatgpt.com)
- [Technology: BSC Data Science Entrance Syllabus](https://sppudocs.unipune.ac.in/sites/news_events/dept_circulars/_layouts/mobile/dispform.aspx?ID=104&List=a4990cc3-1897-44e7-ab76-d9099c953f89&View=b4e7e942-a3b1-433d-a212-71decc921ef1&utm_source=chatgpt.com)
- [Syllabus-2025](https://collegecirculars.unipune.ac.in/sites/documents/Syllabus2025/Forms/AllItems.aspx?Mobile=1&utm_source=chatgpt.com)
- [NewsandAnnouncements - B.Sc. Data Science Entrance syllabus.](https://sppudocs.unipune.ac.in/sites/news_events/Lists/News%20and%20Announcements/DispForm.aspx?ID=8515&utm_source=chatgpt.com)
- [MSc Programme in Scientific & Computing | SCMS-SPPU](https://cmstest.unipune.ac.in/programmes/msc.shtml?utm_source=chatgpt.com)
- [Academics — Dept. of Computer Science · SPPU](https://unipune.ac.in/pucsd/pages/academics.html?utm_source=chatgpt.com)
- [Boards And Meetings Circulars: Circular No-36-2024- Autonomous Colleges - Syllabus Upload_24022024](https://sppudocs.unipune.ac.in/sites/circulars/_layouts/mobile/dispform.aspx?ID=1102&List=85ab0d02-7304-478b-a04b-240d0a46dcae&View=96b19d89-ba06-4885-ac3b-89f4a3053952&utm_source=chatgpt.com)
- [Syllabi : Savitribai Phule Pune University offers undergraduate, postgraduate and doctoral programs in sciences, languages, social sciences, law, management and other interdisciplinary programs.](https://www.unipune.ac.in/university_files/Syllabi.htm?utm_source=chatgpt.com)
- [Boards And Meetings Circulars - Circular No-264-2025_26092025.pdf](https://sppudocs.unipune.ac.in/sites/circulars/Boards%20And%20Meetings%20Circulars/Forms/DispForm.aspx?ID=1347&utm_source=chatgpt.com)
- [Syllabi : Savitribai Phule Pune University offers undergraduate, postgraduate and doctoral programs in sciences, languages, social sciences, law, management and other interdisciplinary programs.](https://www.unipune.ac.in/UNIVERSITY_FILES/syllabi.htm?utm_source=chatgpt.com)
- [Boards And Meetings Circulars: Circular No. 35-2023 Syllabus Upload-Autonomous Colleges_23022023](https://sppudocs.unipune.ac.in/sites/circulars/_layouts/mobile/dispform.aspx?ID=990&List=85ab0d02-7304-478b-a04b-240d0a46dcae&View=96b19d89-ba06-4885-ac3b-89f4a3053952&utm_source=chatgpt.com)
- [Syllabi : Savitribai Phule Pune University offers undergraduate, postgraduate and doctoral programs in sciences, languages, social sciences, law, management and other interdisciplinary programs.](https://www.unipune.ac.in/university_files/syllabi.htm?utm_source=chatgpt.com)
- [Syllabus — Dept. of Computer Science · SPPU](https://unipune.ac.in/pucsd/pages/syllabus.html?utm_source=chatgpt.com)
- [Syllabus-2024: S. E. Computer Science and Engineering (Data Science ) Syllabus_19062024](https://collegecirculars.unipune.ac.in/sites/documents/_layouts/mobile/dispform.aspx?ID=194&List=9b6804d5-31f1-40c1-9e48-6fb319fb7680&View=bf3d90fd-b3c4-466b-96fa-f1fbaa4bad6c&utm_source=chatgpt.com)
- [Affiliation Circulars](https://sppudocs.unipune.ac.in/sites/circulars/_layouts/mobile/view.aspx?List=af436354-dca6-4fb3-8298-f5e02ba95c17&View=e3a28b80-a605-4432-be04-842d8855c705&ViewMode=Detail&utm_source=chatgpt.com)
- [NewsandAnnouncements - Autonomous Colleges - Syllabus Upload \[Circular...](https://sppudocs.unipune.ac.in/sites/news_events/Lists/News%20and%20Announcements/DispForm.aspx?ID=8292&utm_source=chatgpt.com)
