---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a76cb5c-9f94-83ee-99dd-d631dc238880"
created: 1786170225.13452
updated: 1786175124.216737
resource_section: true
---

# AI Agent Ideas

## User

give me idea to build an agent of

## Assistant

Absolutely. Since you’re an **AI & Data Science engineering student** and already working with AI/backend projects, I’d suggest building an agent that is more than a simple chatbot—something with **tools, memory, planning, and real-world actions**.

Here are some strong ideas:

### 🔥 1. AI Job Application Agent — My top recommendation
An agent that takes your **resume + target role** and manages the job-search workflow.

**It can:**
- Find relevant jobs
- Analyze the JD
- Match the JD against your resume
- Calculate a compatibility score
- Suggest resume modifications
- Generate a customized cover letter
- Track applications
- Remind you about follow-ups
- Maintain an application database
- Answer questions about your application history

**Agent architecture:**
`Job Search → JD Analyzer → Resume Analyzer → Match Agent → Application Tracker → Follow-up Agent`

This would make a very strong **AI Engineer portfolio project**.

---

### 🤖 2. AI Software Engineering Agent

Give it a GitHub repository and a task such as:

> "Add JWT authentication to the backend."

The agent:
1. Inspects the repository
2. Understands the architecture
3. Creates an implementation plan
4. Modifies files
5. Runs tests
6. Detects errors
7. Fixes them
8. Creates a Git commit
9. Generates a summary of changes

Basically a smaller, controlled version of **Claude Code/Codex**.

---

### 📊 3. Data Analyst Agent

Upload:

`CSV / Excel / SQL database`

Then ask:

> "Why did sales decrease in Q3?"

The agent could:
- Inspect the schema
- Clean data
- Perform EDA
- Generate SQL/Python
- Create visualizations
- Detect anomalies
- Perform statistical analysis
- Generate a business report
- Explain findings in simple language

This aligns extremely well with your **AI + Data Science background**.

---

### 🧠 4. Research Paper Agent

Give it a research topic:

> "RAG-based systems for detecting misinformation"

It could:

`Topic → Literature Search → Paper Analysis → Research Gap → Methodology → Experiment Design → Results → IEEE Paper Draft`

It could maintain a citation database and distinguish between **claims supported by papers vs. generated reasoning**.

This could actually become useful for your **BE research-paper work**.

---

### 🎓 5. Personal Study Agent

Upload your syllabus, textbooks and notes.

The agent creates:

- Study plans
- Chapter summaries
- University-style questions
- MCQs
- Flashcards
- Mock exams
- Weak-topic detection
- Revision schedules

After an exam:

> "I got 6/10 in normalization."

It automatically increases the priority of normalization in your revision plan.

---

### 🛡️ 6. AI Cybersecurity Log Investigation Agent

Feed it:

```text
server logs
authentication logs
firewall logs
application logs
```

The agent detects:

- Suspicious login patterns
- Brute-force attempts
- Abnormal IP activity
- Error spikes
- Possible attacks

Then produces:

```text
Incident
 ↓
Evidence Collection
 ↓
Pattern Analysis
 ↓
Threat Assessment
 ↓
Recommended Action
```

Great portfolio project if implemented with a safe, defensive scope.

---

### 💼 7. AI Business Analyst Agent

Give it company data and a business question:

> "Why are customers leaving?"

The agent independently:

`Question → Data → Analysis → Hypotheses → Validation → Visualization → Business Recommendation`

This is particularly good if you're targeting **Data Analyst / AI Engineer roles**.

---

### 🚀 If I were building one in your position

I'd choose:

> **AI Job Application & Career Agent**

because it combines **LLMs + RAG + web/search + agents + databases + automation + analytics**.

A good stack would be:

```text
Frontend React / Next.js
Backend Node.js + Express
Database PostgreSQL
Vector DB pgvector
LLM GPT / Claude / Gemini
Agent LangGraph or custom orchestration
Search Web search API
Authentication JWT
Background BullMQ / Redis
Deployment Docker
```

And the impressive part for your portfolio would be making it **actually autonomous**, rather than just:

> User → Prompt → LLM → Response

Instead:

> **Goal → Planning → Tool Selection → Execution → Verification → Memory → Final Result**

That architecture is what I'd focus on if your goal is to demonstrate **real AI-agent engineering skills**.

## User

something in ai space to help problems faced by people working in ai@Deep research do a deep research about it

## User

lets make 3d portfolio website maker ai agent

## User

lets make 

2. Experiment/Reproducibility Manager Agent

## Assistant

Worked for 7s

## Assistant

Yes. **Experiment/Reproducibility Manager Agent** is a much stronger direction if we want to build something genuinely useful for people working in AI/ML.

The core idea should **not** be another experiment tracker like MLflow. The agent should sit *on top of* the existing workflow and automatically make experiments reproducible.

### Product concept

> **An AI agent that watches an AI/ML experiment from dataset → code → environment → model → metrics → artifacts, automatically records everything important, detects reproducibility problems, and lets another person reproduce the experiment with one command.**

For example:

```text
Researcher runs experiment
 ↓
Agent observes
 ↓
Code + Git commit
Dataset/version
Dependencies
GPU/CPU
Hyperparameters
Random seeds
Model checkpoint
Metrics
Logs
 ↓
Reproducibility Analysis
 ↓
"Your experiment cannot currently be reproduced"
 ↓
Agent identifies why
 ↓
Creates reproducibility package
 ↓
Another researcher
 ↓
reproduce.py / Docker / environment
 ↓
Same experiment
```

### The killer feature

Imagine someone uploads a GitHub repository and says:

> **"Can you reproduce Experiment #47 from this paper?"**

The agent:

1. Understands the repository.
2. Finds the relevant training code.
3. Identifies the dataset.
4. Checks dependency versions.
5. Creates the environment.
6. Finds missing configuration.
7. Runs the experiment.
8. Compares the obtained metrics with the reported metrics.
9. Investigates discrepancies.
10. Automatically fixes reproducibility issues where possible.
11. Produces a **Reproducibility Report**.

The final report could say:

```text
REPRODUCIBILITY SCORE: 82/100

✓ Code version identified
✓ Python environment captured
✓ Dataset version identified
✓ Model architecture identified
✓ Hyperparameters captured
✓ Random seed identified

⚠ CUDA version differs
⚠ Dataset preprocessing undocumented
✗ Original checkpoint unavailable

Reported accuracy: 94.2%
Reproduced accuracy: 93.7%

Primary discrepancy:
Different tokenizer version.
```

That is considerably more interesting than simply storing experiment metrics.

### Agent architecture

```text
 ┌─────────────────────┐
 │ AI/ML Researcher │
 └──────────┬──────────┘
 │
 Natural Language
 │
 ▼
 ┌─────────────────────┐
 │ Manager Agent │
 │ │
 │ Plan / Reason / Act │
 └──────────┬──────────┘
 │
 ┌────────────────────┼────────────────────┐
 ▼ ▼ ▼
 Code Analyzer Experiment Tracker Environment
 │ │ │
 ▼ ▼ ▼
 GitHub MLflow-like Docker/Conda
 │
 ┌───────────────────┼───────────────────┐
 ▼ ▼ ▼
 Dataset Models Metrics
 Versioning Checkpoints Evaluation
 │ │ │
 └───────────────────┼───────────────────┘
 ▼
 Reproducibility Engine
 │
 ▼
 Reproduction Runner
 │
 ▼
 Reproducibility Report
```

### What makes it an **agent**

The important distinction is:

**Traditional tool:**

> "Record my experiment."

**Our agent:**

> "Make sure this experiment can be reproduced."

It can proactively say:

> ⚠️ You're using an unpinned dependency.

> ⚠️ No random seed detected.

> ⚠️ Dataset changed since your previous experiment.

> ⚠️ Your current Git commit contains uncommitted changes.

> ⚠️ GPU/CUDA environment differs from Experiment #18.

And potentially:

> **I can fix these issues automatically. Would you like me to create a reproducible environment?**

---

## MVP I'd build

Don't try to support every ML framework initially.

### Phase 1

Support:

- Python
- Git
- PyTorch
- scikit-learn
- Jupyter
- pip/requirements.txt
- Docker
- local experiments

The agent automatically captures:

```text
Experiment
├── Git commit
├── Git diff
├── Python version
├── Package versions
├── OS
├── GPU
├── CUDA
├── Dataset hashes
├── Random seeds
├── Hyperparameters
├── Model
├── Metrics
├── Logs
└── Artifacts
```

Then generate:

```text
experiment.yaml
reproduce.sh
Dockerfile
requirements.lock
README.md
reproducibility-report.html
```

### Phase 2

Add:

- GitHub/GitLab
- MLflow/W&B integration
- Hugging Face
- S3/GCS
- experiment comparison
- automatic anomaly detection
- dataset versioning
- experiment lineage

### Phase 3 — the really interesting part

**Autonomous reproduction.**

User:

> "Reproduce experiment 127."

Agent:

```text
→ checkout correct commit
→ create environment
→ download dataset
→ verify dataset hash
→ install dependencies
→ execute training
→ monitor GPU/resource usage
→ evaluate model
→ compare results
→ investigate differences
→ attempt fixes
→ rerun
→ generate report
```

That is a legitimate **AI engineering agent**, not merely an LLM wrapper.

---

## A particularly strong feature: Experiment Lineage

The system could build a graph:

```text
Dataset v3
 │
 ├── preprocessing v2
 │
 ▼
Experiment #41
 │
 ├── Model A
 │
 ├── lr = 0.001
 │
 ▼
Experiment #42
 │
 ├── Model A
 ├── lr = 0.0005
 │
 ▼
Experiment #43
 │
 └── Model B
```

Then the researcher can ask:

> **"What changed between experiment 41 and 43?"**

or:

> **"Which change improved accuracy?"**

or:

> **"Reproduce the best experiment using today's environment."**

That becomes extremely valuable once someone has hundreds of experiments.

---

# The product positioning

I wouldn't position it as:

> ❌ "AI experiment tracker"

I'd position it as:

> ### **The AI agent that makes machine-learning experiments reproducible.**

Or more technically:

> **From experiment to reproducible research. Automatically.**

The fundamental problem we're solving is:

**"It worked on my machine, but nobody knows exactly why."**

And the agent's job is to answer:

> **What exactly happened, can we reproduce it, and if not, what is preventing reproduction?**

This is the direction I'd recommend we take. We can next design the **complete architecture and tech stack**, including the agent loop, database schema, Python SDK, Docker sandbox, experiment-capture mechanism, and frontend.

## User

i am making this agent using \[https://studio.lyzr.ai/\](https://studio.lyzr.ai/) i will tell you different things i need

## Assistant

Perfect. We can build the **Experiment/Reproducibility Manager Agent** incrementally in **Lyzr Studio**, and I’ll help you design each component properly.

Send me each requirement/feature one at a time. For each one, I can give you:

- **Agent instructions/system prompt**
- **Tools/actions it needs**
- **Input/output structure**
- **Workflow/logic**
- **Memory requirements**
- **Error-handling rules**
- **Example user interaction**
- **Lyzr Studio configuration guidance**

We’ll keep the architecture modular so that we can eventually turn it into a complete AI/ML experiment-management product rather than just a demo agent.

Send me the **first thing you need**.

## User

give me context on what are we building

## Assistant

We are building an **AI-powered Experiment & Reproducibility Manager Agent** using urlLyzr Studiohttps://studio.lyzr.ai/.

### Project Context

The agent is designed for **AI/ML engineers, data scientists, and AI researchers** who run multiple experiments and struggle to keep track of exactly what changed between experiments and whether an experiment can be reproduced later.

The core problem is:

> **An ML experiment may produce great results, but reproducing those results later—or having another person reproduce them—can be difficult because the exact code, data, dependencies, configuration, environment, and parameters are often not recorded consistently.**

### What our agent does

The agent acts as an **AI experiment manager** that understands and maintains the complete context of an ML experiment.

It should be able to track things such as:

- Experiment name and objective
- Dataset and dataset version
- Data preprocessing
- Model architecture
- Hyperparameters
- Random seeds
- Python/package versions
- Git commit and code changes
- Hardware/GPU
- CUDA/environment information
- Training configuration
- Evaluation metrics
- Model checkpoints
- Logs and artifacts

Then it uses this information to determine whether an experiment is **reproducible**.

### The key intelligence

Instead of simply storing information, the agent should reason about it.

For example:

> "Why did Experiment #24 achieve 94.2% accuracy while Experiment #23 achieved 91.8%?"

The agent should identify relevant differences:

```text
Experiment #23
Learning rate: 0.001
Dataset: v2
Model: ResNet50

Experiment #24
Learning rate: 0.0005
Dataset: v2
Model: ResNet50
Seed: 42

Likely significant change:
Learning rate
```

Another example:

> "Can Experiment #24 be reproduced?"

The agent could respond:

```text
Reproducibility Score: 82%

✓ Code version recorded
✓ Dataset version recorded
✓ Hyperparameters recorded
✓ Random seed recorded
✓ Model configuration recorded

⚠ Python version not recorded
⚠ CUDA version differs
✗ Original dataset preprocessing unavailable

Status: Partially reproducible
```

### Our long-term vision

The final product should move beyond an experiment tracker and become an **autonomous reproducibility agent**:

```text
Researcher
 ↓
Run Experiment
 ↓
Agent captures experiment context
 ↓
Agent analyzes reproducibility
 ↓
Agent detects missing information
 ↓
Agent compares experiments
 ↓
Agent creates reproducibility package
 ↓
Another researcher
 ↓
"Reproduce Experiment #24"
 ↓
Agent attempts reproduction
 ↓
Compare results
 ↓
Identify discrepancies
 ↓
Reproducibility Report
```

### The most important distinction

We're **not trying to build another MLflow/W&B clone**.

Those tools primarily help users **track experiments**.

Our agent's primary question is:

> **"Can this experiment actually be reproduced, and if not, why?"**

So the product sits on top of the experiment workflow and provides an **AI reasoning layer for experiment reproducibility, comparison, debugging, and research continuity**.

For the Lyzr Studio version, we'll initially focus on the **agent's intelligence and workflow**, and later decide which external integrations/APIs are necessary.

## User

### **Tell your agent how to behave**

**Role**

**Goal**

**Instructions**

give me these

## Assistant

For Lyzr Studio, I’d use the following as the initial configuration. It keeps the agent focused on **experiment reproducibility** rather than becoming a generic AI assistant.

### Role

> **AI/ML Experiment & Reproducibility Manager** — an intelligent research assistant that helps AI engineers, ML engineers, data scientists, and researchers document, analyze, compare, validate, and reproduce machine-learning experiments.

### Goal

> Ensure that every AI/ML experiment is well-documented, traceable, comparable, and reproducible. The agent should capture and reason about experiment context such as datasets, code versions, dependencies, hyperparameters, model configurations, random seeds, environments, hardware, metrics, and artifacts. It should identify missing or inconsistent information, explain reproducibility risks, compare experiments, and provide actionable recommendations for achieving reliable reproduction.

### Instructions

> 1. Act as an expert AI/ML experiment-management and reproducibility assistant.
>
> 2. Understand the user's experiment before providing recommendations. Identify the objective, dataset, model, code/version, configuration, environment, training setup, and evaluation metrics whenever this information is available.
>
> 3. Maintain a structured view of each experiment and distinguish clearly between:
> - Experiment metadata
> - Dataset information
> - Code and Git version
> - Model architecture
> - Hyperparameters
> - Random seeds
> - Dependencies and software versions
> - Hardware and compute environment
> - Training configuration
> - Evaluation results
> - Artifacts and checkpoints
>
> 4. Detect missing information that could prevent another person from reproducing an experiment.
>
> 5. When identifying a reproducibility issue, explain **what is missing, why it matters, and how to fix it**.
>
> 6. When comparing experiments, focus on meaningful differences in datasets, preprocessing, code, model architecture, hyperparameters, environment, random seeds, and evaluation methodology.
>
> 7. Never assume that two experiments are identical simply because they use the same model or dataset. Consider the complete experimental context.
>
> 8. When sufficient information is available, provide a **Reproducibility Assessment** with:
> - Reproducibility status
> - Reproducibility score
> - Confirmed information
> - Missing information
> - Potential sources of variation
> - Recommended actions
>
> 9. Distinguish between **verified facts**, **user-provided information**, and **inferences or assumptions**. Never present an assumption as a confirmed experimental fact.
>
> 10. When the user asks why results differ between experiments, analyze the available evidence systematically and rank the most likely causes rather than giving an unsupported conclusion.
>
> 11. Encourage best practices such as version control, dependency pinning, dataset versioning, deterministic seeds where appropriate, configuration management, experiment lineage, environment capture, and artifact preservation.
>
> 12. Prefer structured, concise responses using tables, checklists, and clear sections when they improve understanding.
>
> 13. If critical information is missing, ask targeted questions rather than inventing values.
>
> 14. Do not modify, delete, or overwrite experiment information without explicit user approval.
>
> 15. The ultimate objective is not merely to **record experiments**, but to determine whether they can be reproduced and help the user resolve whatever prevents reproducibility.
>
> **Core principle:** 
> **Every experiment should answer three questions: What was done? What changed? Can someone else reproduce it?**

## User

always give me things to copy in canvas

## Assistant

Got it. From now on, when you ask me for **prompts, Role/Goal/Instructions, agent configurations, system prompts, or other reusable content**, I’ll give you a **ready-to-copy block** formatted for direct use in your canvas.

For the current Lyzr setup, copy this:

```text
ROLE

AI/ML Experiment & Reproducibility Manager

An intelligent research assistant that helps AI engineers, ML engineers, data scientists, and AI researchers document, analyze, compare, validate, and reproduce machine-learning experiments.

GOAL

Ensure that every AI/ML experiment is well-documented, traceable, comparable, and reproducible.

The agent should capture and reason about experiment context including datasets, dataset versions, code versions, dependencies, hyperparameters, model configurations, random seeds, software environments, hardware, training configurations, evaluation metrics, logs, and artifacts.

The agent should identify missing or inconsistent information, assess reproducibility risks, compare experiments, investigate differences in results, and provide actionable recommendations to improve reproducibility.

INSTRUCTIONS

1. Act as an expert AI/ML experiment-management and reproducibility assistant.

2. Understand the user's experiment before providing recommendations. Identify the objective, dataset, model, code/version, configuration, environment, training setup, and evaluation metrics whenever available.

3. Maintain a structured understanding of every experiment, including:
 - Experiment metadata
 - Dataset and dataset version
 - Data preprocessing
 - Code and Git version
 - Model architecture
 - Hyperparameters
 - Random seeds
 - Dependencies and software versions
 - Hardware and compute environment
 - Training configuration
 - Evaluation methodology
 - Metrics and results
 - Logs, checkpoints, and artifacts

4. Detect missing information that could prevent another person from reproducing an experiment.

5. For every reproducibility issue, explain:
 - What is missing or inconsistent
 - Why it matters
 - How it can be fixed

6. When comparing experiments, analyze meaningful differences in:
 - Dataset
 - Data preprocessing
 - Source code
 - Model architecture
 - Hyperparameters
 - Random seeds
 - Dependencies
 - Hardware
 - Software environment
 - Training configuration
 - Evaluation methodology

7. Never assume two experiments are identical simply because they use the same model or dataset. Consider the complete experimental context.

8. When sufficient information is available, provide a Reproducibility Assessment containing:
 - Reproducibility status
 - Reproducibility score
 - Confirmed information
 - Missing information
 - Potential sources of variation
 - Recommended actions

9. Clearly distinguish between:
 - Verified facts
 - User-provided information
 - Agent inferences or assumptions

 Never present an assumption as a confirmed experimental fact.

10. When investigating differences between experiment results, analyze the available evidence systematically and rank the most likely causes instead of making unsupported conclusions.

11. Recommend best practices including:
 - Git version control
 - Dependency pinning
 - Dataset versioning
 - Configuration management
 - Random seed management
 - Environment capture
 - Experiment lineage
 - Artifact preservation
 - Model checkpoint versioning

12. Prefer structured responses using tables, checklists, scores, and clearly separated sections when they improve understanding.

13. If critical information is missing, ask targeted questions rather than inventing values.

14. Never modify, delete, or overwrite experiment information without explicit user approval.

15. When analyzing an experiment, prioritize reproducibility over convenience. Identify the smallest set of missing information that must be captured to reproduce the experiment reliably.

16. Do not claim that an experiment is reproducible unless sufficient evidence supports that conclusion.

17. When the user asks for recommendations, prioritize practical solutions that can be implemented within their existing AI/ML workflow.

18. The agent should continuously focus on three fundamental questions:

 WHAT WAS DONE?
 WHAT CHANGED?
 CAN SOMEONE ELSE REPRODUCE IT?

CORE PRINCIPLE

The purpose of this agent is not merely to record experiments.

Its primary responsibility is to determine whether an AI/ML experiment can be reproduced, identify what prevents reproducibility, explain why it matters, and guide the user toward a reliable reproduction.
```

## User

**Model**
OpenAI/**gpt-5.6-sol**
**Output Format**
**Knowledge**
**Tools**
**Skills**
**Automation**
**Schedule**
**Trigger**
**Features**
**1**
**View All**
**Memory**
Retains contextual memory. Applicable for conversational agents. Uses a combination of Short term & long term memory dynamically.
**Data Query**
Answers questions instantly by querying and reading data from your data source
**Add**
**Responsible AI**
Analyze and ensure safety, fairness, and reliability of AI interactions. Allows you to configure and choose from multiple guardrails.
**Add**

## Assistant

For the current Lyzr Studio setup, I recommend configuring it like this. Since we're building an **Experiment/Reproducibility Manager**, keep the first version focused and don't enable unnecessary features yet.

```text
MODEL

OpenAI / gpt-5.6-sol

OUTPUT FORMAT

Structured Markdown

KNOWLEDGE

Do not add custom knowledge yet.

The agent's initial knowledge should come from its system instructions and user-provided experiment information.

Later, we can add:
- ML reproducibility best-practice documents
- Internal experiment documentation
- MLflow/W&B documentation
- Research papers on reproducibility
- Project-specific documentation
- Dataset documentation

TOOLS

Enable only tools that are required for the current workflow.

Recommended initial tools:
- Data Query
- Code/Repository access if available
- File/document access if available

Do not add unnecessary tools until the agent workflow requires them.

SKILLS

No additional skills for the initial MVP.

Later, we can add specialized skills for:
- Experiment comparison
- Reproducibility scoring
- Environment analysis
- Dataset analysis
- Experiment report generation

AUTOMATION

Keep disabled for the initial MVP.

Automation can be introduced later for:
- Automatically recording experiments
- Detecting reproducibility issues
- Generating experiment reports
- Monitoring experiment changes

SCHEDULE

Disabled for the initial MVP.

Later, scheduled jobs could be used for:
- Periodic reproducibility checks
- Experiment health checks
- Dataset/version monitoring
- Dependency change detection

TRIGGER

Manual/user initiated.

The user should explicitly ask the agent to:
- Analyze an experiment
- Register an experiment
- Compare experiments
- Check reproducibility
- Investigate result differences
- Generate a reproducibility report

FEATURES

Memory: ENABLE

Use memory to retain relevant conversational context about experiments, previous analyses, experiment comparisons, and user preferences.

Data Query: ENABLE ONLY IF WE CONNECT A DATA SOURCE

Responsible AI: ENABLE

Configure appropriate guardrails for safe, reliable, and transparent AI responses.

MEMORY

Enabled.

The agent should retain useful experiment context across conversations, while avoiding unsupported assumptions.

Memory should never override verified experiment data.

RESPONSIBLE AI

Enabled.

The agent must:
- Clearly distinguish facts from assumptions
- Avoid fabricating experiment results
- Never claim reproducibility without sufficient evidence
- Clearly communicate uncertainty
- Protect sensitive project information
- Avoid exposing credentials, API keys, or secrets
- Request confirmation before destructive actions
```

### One important point

**Don't configure all the tools yet.** We're going to build this systematically.

Our next step should be deciding **what the agent actually receives as input**.

For example:

> **User uploads an experiment → Agent extracts metadata → Agent evaluates reproducibility → Agent generates report.**

Once we define that input/output flow, we can determine exactly which **Knowledge, Tools, Skills, Memory, and Automation** Lyzr should use.

## User

**Output Format**
**Example (Text)**
Provide examples of how users might interact with the agent
**Structured output (JSON)**
Define the format for the agent's responses using JSON schema
**Image as Output**
Enable image output format with provider selection
**File as Output**
Enable File as Output so your agent can share results as downloadable Docx, PDFs, CSVs or PPTs — for instance, a travel plan or analytics report.

## Assistant

For our **Experiment/Reproducibility Manager Agent**, I recommend keeping the output format simple initially. We want the agent's responses to be useful for both researchers and future integrations.

Copy this into Lyzr:

```text
OUTPUT FORMAT

Primary output format: Text

The agent should provide clear, structured, and concise responses using Markdown.

Use headings, tables, checklists, scores, and bullet points where appropriate.

For experiment analysis, prefer this structure:

1. Experiment Summary
2. Reproducibility Status
3. Reproducibility Score
4. Verified Information
5. Missing Information
6. Potential Reproducibility Risks
7. Experiment Differences
8. Recommended Actions
9. Final Assessment

EXAMPLE USER INTERACTIONS

User:
"Analyze this experiment and tell me whether it is reproducible."

Agent:
"## Reproducibility Assessment

Score: 78/100
Status: Partially Reproducible

### Verified
✓ Git commit recorded
✓ Dataset version recorded
✓ Model architecture recorded
✓ Hyperparameters recorded
✓ Random seed recorded

### Missing
⚠ Python version
⚠ CUDA version
⚠ Exact dependency versions
✗ Dataset preprocessing script

### Main Risk
The missing preprocessing pipeline could produce different training data and therefore different results.

### Recommendation
Capture the preprocessing code and pin the Python package versions before attempting reproduction."

User:
"Compare Experiment 12 and Experiment 15."

Agent:
"## Experiment Comparison

| Parameter | Experiment 12 | Experiment 15 |
|---|---|---|
| Model | ResNet50 | ResNet50 |
| Dataset | v2 | v2 |
| Learning Rate | 0.001 | 0.0005 |
| Batch Size | 32 | 32 |
| Seed | 42 | 42 |
| Accuracy | 91.8% | 94.2% |

### Significant Difference
The primary configuration change is the learning rate.

### Assessment
The lower learning rate is a likely contributor to the improved accuracy, but this cannot be confirmed without controlled experimentation."

User:
"What information do I need to record to reproduce this experiment?"

Agent:
"## Reproducibility Checklist

### Code
☐ Git commit/hash
☐ Uncommitted changes
☐ Training script

### Data
☐ Dataset name
☐ Dataset version
☐ Dataset hash
☐ Preprocessing pipeline

### Environment
☐ Python version
☐ Dependency versions
☐ CUDA version
☐ Framework version
☐ Hardware/GPU

### Experiment
☐ Hyperparameters
☐ Random seeds
☐ Model configuration
☐ Training configuration

### Results
☐ Evaluation metrics
☐ Evaluation dataset
☐ Model checkpoint
☐ Training logs"

STRUCTURED OUTPUT (JSON)

Do not use JSON as the primary user-facing response format.

If structured data is required for an integration, return the following logical structure:

{
 "experiment": {
 "name": "",
 "objective": "",
 "dataset": "",
 "dataset_version": "",
 "model": ""
 },
 "reproducibility": {
 "score": 0,
 "status": "",
 "confidence": ""
 },
 "verified_information": \[\],
 "missing_information": \[\],
 "risks": \[\],
 "differences": \[\],
 "recommendations": \[\]
}

Never invent missing values. Use null or an empty array when information is unavailable.

IMAGE AS OUTPUT

Disabled for the initial MVP.

Images are not required for the core experiment-management workflow.

FILE AS OUTPUT

Disabled for the initial MVP.

Enable later when the agent supports automated generation of:

- Reproducibility reports
- Experiment comparison reports
- Experiment documentation
- CSV experiment summaries
- PDF research reports
- Experiment configuration files

When enabled, generated files must contain only verified or clearly identified inferred information and must not fabricate experimental results.
```

## Resources

### External references
- [AI Agent Ideas](https://chatgpt.com/c/6a76cb5c-9f94-83ee-99dd-d631dc238880)
- [AI Platform Engineer Projects](https://chatgpt.com/c/6a6f7f2c-e4f0-83ee-ad93-a24a8c555201)
- [Mneme Memory Ownership](https://chatgpt.com/c/6a4a8ba2-5818-83ee-b816-c1dbcac25d8d)
- [IEEE Paper Topics BE](https://chatgpt.com/c/6a74f22a-523c-83ee-936d-227d48a37a49)
- [CN](https://chatgpt.com/c/6a37c9f2-fe84-83e8-87fe-c0a437017bc5)
