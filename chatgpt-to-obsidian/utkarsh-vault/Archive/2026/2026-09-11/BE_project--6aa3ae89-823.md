---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6aa3ae89-8230-83ee-944b-49974d284f05"
created: 1789111946.163452
updated: 1789658074.615895
resource_section: true
---

# BE_project

## User

Modify this above PDF according to this SIH problem statement. Search about this problem statement, about its novelty, and all the topics present in that PDF. Make give me output as a PDF. I want to present this PDF for my fourth-year project, and this PDF will act as an ideation idea presentation to my teacher.
SIH26097 solution
The problem isn't merely:
"AI recommends courses."
It's:
"A person with limited digital literacy can simply speak in their own language, and the system guides them from their current skills → skill gap → NSQF-aligned training → livelihood opportunity."
That is a much stronger product story.
And for the hackathon, I'd make Marathi + Hindi + English the MVP languages, then architect the system so additional Indian languages can be plugged in without changing the core recommendation engine. This keeps the implementation realistic while demonstrating the multilingual requirement properly.

## Assistant

Worked for 28s

## Assistant

Done. I rebuilt the original two-page ideation PDF around **SIH26097**, while retaining its presentation structure: Abstract → Research Gap → Novelty → Keywords → References → Proposed System Flow. fileciteturn0file0L9-L31 fileciteturn0file0L35-L90

One important correction from the initial framing: **SIH26097 is officially about SC communities under the PM-AJAY Grant-in-Aid component, not specifically persons with visual impairment.** The problem asks for a multilingual, voice-based livelihood assistant that profiles beneficiaries, identifies skill gaps, recommends NSQF-aligned pathways, considers local opportunities, and can work through low-tech channels such as IVR, WhatsApp voice notes, mobile, or kiosks. citeturn644637search5turn784546search8

I also strengthened the final-year-project novelty around the product story you described:

**spoken aspirations → structured livelihood profile → skill-gap analysis → NSQF/NQR training → local livelihood opportunity**

The PDF includes **Marathi + Hindi + English as the realistic MVP**, a language-independent recommendation architecture, local opportunity-aware ranking, explainable recommendations, low-connectivity design, NSQF/NQR retrieval, and a bounded technical architecture suitable for a fourth-year AI & DS project. This aligns well with PM-AJAY's actual requirement that skilling reflect beneficiary interest, local skill-gap/job-market relevance, NSQF compliance, certification, and wage/self-employment outcomes. citeturn784546search0turn644637search0

### PDF
\[**Download SIH26097 Final Year Project Ideation PDF**\](sandbox:/mnt/data/SIH26097_Final_Year_Project_Ideation.pdf)

I named the concept **KaushalVaani — AI-Driven Voice Livelihood & NSQF Skilling Assistant** in the PDF; the name can easily be changed later if your team already has one.

## User

Implementing knowledge graph in this Idea, is what sir wants

## Assistant

Worked for 6s

## Assistant

Yes — and I’d make the **knowledge graph a core part of the recommendation engine**, not something added just to satisfy the project requirement.

For this problem, a KG fits naturally because SIH26097 is fundamentally about connecting many related entities: a beneficiary’s education, current livelihood, skills, interests, constraints, local opportunities, job roles, NSQF levels, qualifications, NOS modules, training pathways, and self-employment/wage-employment options. The official problem explicitly asks the system to infer suitable NSQF-aligned training, skill gaps, relevant trades, and region-specific livelihood opportunities from a conversational profile. citeturn489185search1

The **National Qualification Register is especially graph-friendly** because qualifications already contain relationships such as job role, sector, NSQF level, eligibility criteria, learning modules/NOS, progression pathways, and employment opportunities. citeturn489185search4turn489185search5

A good revised architecture would be:

**User speaks → STT → profile extraction → Knowledge Graph → skill-gap reasoning → recommendation/ranking → explanation → TTS**

The KG could contain relationships like:

```text
Beneficiary
 ├── HAS_SKILL ──────────────> Welding
 ├── INTERESTED_IN ──────────> Manufacturing
 ├── HAS_EDUCATION ──────────> 10th Pass
 ├── LIVES_IN ───────────────> Pune District
 ├── PREFERS ────────────────> Wage Employment
 └── HAS_CONSTRAINT ─────────> Low Mobility

Welder Assistant
 ├── BELONGS_TO ─────────────> Manufacturing Sector
 ├── HAS_NSQF_LEVEL ─────────> Level 3
 ├── REQUIRES_SKILL ─────────> Welding Basics
 ├── REQUIRES_SKILL ─────────> Workplace Safety
 ├── ELIGIBLE_WITH ──────────> 10th Pass
 ├── PROGRESSES_TO ──────────> Welder
 └── AVAILABLE_IN ───────────> Maharashtra

Training Qualification
 ├── PREPARES_FOR ───────────> Welder Assistant
 ├── CONTAINS_NOS ───────────> NOS-001
 └── ALIGNS_WITH ────────────> NSQF Level 3
```

Then your **skill-gap analysis becomes actual graph reasoning** rather than asking an LLM to guess.

Suppose the beneficiary says:

> “I completed 10th. I help my father repair agricultural machinery. I know basic welding and want a job near my village.”

Your NLP layer extracts:

```text
Education = 10th
Skill = Basic Welding
Experience = Machinery Repair
Interest = Mechanical Work
Mobility = Local Only
EmploymentPreference = Wage Employment
```

The graph could traverse:

```text
Basic Welding
 ↓ MATCHES_SKILL

Welder Assistant
 ↓ REQUIRES

Safety Procedures
Blueprint Reading
Advanced Welding

 ↓ TRAINED_BY

NSQF Qualification X
 ↓ LEADS_TO

Welder / Fabricator
 ↓ DEMAND_IN

Local manufacturing / repair ecosystem
```

The output becomes much stronger:

> **Recommended pathway: Welder Assistant → Welder** 
> You already possess basic welding experience. 
> Missing competencies: workplace safety and blueprint interpretation. 
> You satisfy the education requirement. 
> This pathway is aligned with an NSQF-recognized qualification and matches your preference for nearby wage employment.

That is explainable because the answer is backed by explicit graph relationships.

### What I would change in your project novelty

Your current PDF describes the recommendation system mainly as:

**profile → skill gap → NSQF retrieval → local opportunity matching → ranking**

I would upgrade it to:

**Multilingual Voice AI + Livelihood Knowledge Graph + Graph-Based Skill-Gap Reasoning + Explainable Recommendation**

The strongest novelty statement would be:

> **A multilingual voice-first livelihood intelligence system that converts conversational beneficiary profiles into a structured knowledge graph and performs graph-based reasoning across skills, NSQF qualifications, occupations, progression pathways and regional livelihood opportunities to generate explainable skilling recommendations.**

That sounds substantially more like a serious **AI & Data Science final-year project** than a conventional voice chatbot.

For the KG itself, I would model roughly these core node types:

| Node | Example |
|---|---|
| `Beneficiary` | User-001 |
| `Skill` | Welding |
| `Interest` | Automotive Repair |
| `Occupation` | Welder |
| `Qualification` | NSQF Welder Qualification |
| `NSQFLevel` | Level 3 |
| `NOS` | Welding Safety NOS |
| `Sector` | Manufacturing |
| `EducationLevel` | 10th Pass |
| `Location` | Pune |
| `LivelihoodOpportunity` | Fabrication Workshop |
| `EmploymentType` | Wage Employment |
| `TrainingProvider` | Training Centre |

And relationships such as:

```text
HAS_SKILL
INTERESTED_IN
LIVES_IN
HAS_EDUCATION
PREFERS_EMPLOYMENT
REQUIRES_SKILL
HAS_QUALIFICATION
ALIGNED_WITH
BELONGS_TO_SECTOR
HAS_NOS
PROGRESSES_TO
QUALIFIES_FOR
AVAILABLE_IN
HAS_OPPORTUNITY_IN
TRAINED_BY
SIMILAR_TO
```

The NQR is useful here because its official records already expose eligibility, progression pathways, learning modules/NOS and NSQF levels, which gives you real graph edges instead of inventing a taxonomy. citeturn489185search5turn489185search7

For implementation, I would use **Neo4j** for the final-year project. It is easier to demonstrate visually to your guide because you can literally show the beneficiary node connected to skills, jobs and NSQF qualifications. You also get Cypher queries that make your recommendation logic understandable.

For example:

```cypher
MATCH (u:Beneficiary {id: $user_id})-\[:HAS_SKILL\]->(s:Skill)
MATCH (job:Occupation)-\[:REQUIRES_SKILL\]->(s)
MATCH (q:Qualification)-\[:PREPARES_FOR\]->(job)
MATCH (q)-\[:ALIGNED_WITH\]->(level:NSQFLevel)
WHERE q.minEducation <= u.educationLevel
RETURN job, q, level
```

Then calculate missing competencies:

```cypher
MATCH (u:Beneficiary {id: $user_id})
MATCH (job:Occupation {id: $job_id})-\[:REQUIRES_SKILL\]->(required:Skill)
WHERE NOT (u)-\[:HAS_SKILL\]->(required)
RETURN required
```

This gives you a clean distinction:

**LLM/AI does understanding. 
Knowledge Graph stores domain knowledge and relationships. 
Graph reasoning determines valid pathways. 
Ranking chooses the best pathway. 
LLM converts the result into natural Marathi/Hindi/English.**

That separation is also safer than letting an LLM invent NSQF recommendations.

I would therefore update your system flow in the PDF to:

**Voice Input → Language Detection/STT → Conversational Profile Extraction → Beneficiary Knowledge Graph → NSQF/NQR Knowledge Graph → Graph-Based Skill Gap & Path Reasoning → Local Opportunity Ranking → Explainable Recommendation → TTS**

And I’d rename the central component from **“NSQF/NQR Retrieval”** to **“Livelihood & NSQF Knowledge Graph”**.

This addition actually strengthens your original project substantially rather than changing its direction. Your uploaded ideation PDF currently positions the system around voice profiling, skill-gap analysis and NSQF-aligned recommendations; a KG becomes the structured intelligence layer connecting those pieces. fileciteturn0file0L35-L63

If this is what your sir specifically expects, the next PDF version should make **Knowledge Graph Architecture, KG Schema, Graph-Based Recommendation, and KG Novelty** visibly central instead of mentioning KG only as part of the tech stack.

## User

Give all this PDF

## Assistant

Worked for 5s

## Assistant

Done. I updated the ideation document so the **Knowledge Graph is now the core intelligence layer**, not just an extra technology.

The PDF now includes the complete KG concept we discussed: **KG node/relationship schema, graph-based skill-gap reasoning, beneficiary example, NSQF/NQR graph integration, explainable recommendation paths, Neo4j/Cypher implementation, multilingual architecture, revised novelty, MVP scope, evaluation metrics, and the complete system architecture**.

### Updated PDF
\[**Download SIH26097 - Knowledge Graph Final Year Project Ideation**\](sandbox:/mnt/data/SIH26097_Knowledge_Graph_Final_Year_Project_Ideation.pdf)

The central project positioning is now:

> **Voice Input → Multilingual Understanding → Beneficiary Knowledge Graph → Livelihood & NSQF Knowledge Graph → Graph-Based Skill-Gap Reasoning → Local Opportunity Ranking → Explainable Recommendation → Voice Output**

This should make the **AI & DS contribution** much clearer when you present the idea to your sir.

## User

@Firecrawl **Use firecrawl skill to crawl all the research paper publications like IEEE, POPUS, everything and give me all the research paper, at least three research paper related to this topic Give me the links also so that I can download this research paper**

## Assistant

Worked for 26s

## Assistant

I used Firecrawl’s research-paper index and searched the topic from three angles: **knowledge-graph skill matching**, **career/education recommendation**, and **multilingual voice access for low-digital-literacy users**. The best papers for your SIH26097 + Knowledge Graph project are below.

- **KG-First, LLM-Fallback: A Hybrid Microservice for Grounded Skill Search and Explanation** — arXiv:2605.01582. This is probably the **closest paper to your proposed architecture** because it explicitly combines authoritative competency frameworks with a **knowledge graph first, LLM fallback** approach for grounded skill search and explanations. Very useful for justifying why your system should keep NSQF/NQR facts in the graph and use an LLM only for understanding/explanation. 
 Download/search: urlarXiv paperhttps://arxiv.org/abs/2605.01582 
 PDF: urlDownload PDFhttps://arxiv.org/pdf/2605.01582

- **Job Posting-Enriched Knowledge Graph for Skills-based Matching** — arXiv:2109.02554. This paper directly addresses the idea that job seekers possess some skills while occupations require others, and that reducing the **skill gap** improves job fit. It is highly relevant to your graph relation design: `HAS_SKILL`, `REQUIRES_SKILL`, occupation matching, and gap computation. 
 Download/search: urlarXiv paperhttps://arxiv.org/abs/2109.02554 
 PDF: urlDownload PDFhttps://arxiv.org/pdf/2109.02554

- **Community-Based Data Integration of Course and Job Data in Support of Personalized Career-Education Recommendations** — arXiv:2006.13864. This one is especially useful for your **training → skills → job/livelihood** pathway because it integrates course descriptions and job data while explicitly discussing skill mismatch between what courses teach and what jobs require. 
 Download/search: urlarXiv paperhttps://arxiv.org/abs/2006.13864 
 PDF: urlDownload PDFhttps://arxiv.org/pdf/2006.13864

- **HRGraph: Leveraging LLMs for HR Data Knowledge Graphs with Information Propagation-based Job Recommendation** — arXiv:2408.13521. This is strong support for using a KG for job matching, skill relationships, learning-gap identification, and recommendation. It also helps justify combining **LLMs + graph reasoning** rather than choosing only one. 
 Download/search: urlarXiv paperhttps://arxiv.org/abs/2408.13521 
 PDF: urlDownload PDFhttps://arxiv.org/pdf/2408.13521

- **Explicit Knowledge Graph Reasoning for Conversational Recommendation** — arXiv:2305.00783. This is valuable for the **voice conversation → clarification → recommendation** part of your project. The paper studies conversational recommendation where the system asks questions to understand current user preferences and explicitly reasons over a knowledge graph. 
 Download/search: urlarXiv paperhttps://arxiv.org/abs/2305.00783 
 PDF: urlDownload PDFhttps://arxiv.org/pdf/2305.00783

- **JobSphere: An AI-Powered Multilingual Career Copilot for Government Employment Platforms** — arXiv:2511.08343. This is one of the most relevant papers for your **Indian multilingual government-employment use case**. It addresses navigation complexity, limited language options, personalized support, government employment systems, and supports **English, Hindi and Punjabi**. This is strong literature support for your Marathi + Hindi + English MVP. 
 Download/search: urlarXiv paperhttps://arxiv.org/abs/2511.08343 
 PDF: urlDownload PDFhttps://arxiv.org/pdf/2511.08343

- **Labour Market Information Driven, Personalized, OER Recommendation System for Lifelong Learners** — arXiv:2005.07465. This one supports your idea of combining **labour-market demand + skill decomposition + learning recommendations**. It extracts skills demanded by jobs and recommends learning content to help users progress toward those skills. 
 Download/search: urlarXiv paperhttps://arxiv.org/abs/2005.07465 
 PDF: urlDownload PDFhttps://arxiv.org/pdf/2005.07465

- **LLM-Assisted Knowledge Graph Completion for Curriculum and Domain Modelling in Personalized Higher Education Recommendations** — arXiv:2501.12300. This is useful if you want to explain how an LLM could help **populate or complete your KG**, while the graph remains the structured source for recommendation. 
 Download/search: urlarXiv paperhttps://arxiv.org/abs/2501.12300 
 PDF: urlDownload PDFhttps://arxiv.org/pdf/2501.12300

- **Towards Explainable Job Title Matching: Leveraging Semantic Textual Relatedness and Knowledge Graphs** — arXiv:2509.09522. Useful for the **explainability** argument: dense semantic matching alone may miss domain relationships, while a KG can improve both alignment and interpretability. 
 Download/search: urlarXiv paperhttps://arxiv.org/abs/2509.09522 
 PDF: urlDownload PDFhttps://arxiv.org/pdf/2509.09522

- **C3-IoC: A Career Guidance System for Assessing Student Skills using Machine Learning and Network Visualisation** — PMC9715283. This paper is useful for the broader career-guidance angle because it maps education, skills and experience to career possibilities using a knowledge base and network visualization. 
 Full text: urlPMC articlehttps://pmc.ncbi.nlm.nih.gov/articles/PMC9715283/

For your **literature review**, I would make these your core three:

1. **KG-First, LLM-Fallback** — architecture closest to your system. 
2. **Job Posting-Enriched Knowledge Graph for Skills-based Matching** — strongest for skill-gap reasoning. 
3. **JobSphere** — strongest for multilingual career guidance in an Indian/government context.

Then use **Community-Based Data Integration...** and **HRGraph** as secondary support.

Your research-gap argument can then become very clear: existing work separately covers **knowledge-graph skill matching**, **course/job recommendation**, **multilingual career assistants**, and **conversational recommendation**, but your proposed system combines these into one India-focused pipeline:

**regional-language voice interaction → beneficiary profile → livelihood/NSQF knowledge graph → skill-gap reasoning → local opportunity-aware recommendation → explainable voice output.**

One limitation: Firecrawl’s paper index is strongest for arXiv/PubMed-style sources; it does **not guarantee complete IEEE/Scopus coverage**. So I can also run a second pass specifically against **IEEE Xplore, Springer, ScienceDirect, ACM, Semantic Scholar and Scopus-indexed publisher pages** and give you a cleaner shortlist of **peer-reviewed journal/conference papers only**, excluding preprints.

## User

@Firecrawl give IEEE papers

## Assistant

Worked for 21s

## Assistant

Yes. I searched **IEEE Xplore specifically** for papers that map closely to your project: **Knowledge Graph + skill-gap analysis + career/skilling recommendation + multilingual/voice interaction**.

These are the strongest IEEE papers I found:

1. **AI-Powered Skill Gap Analysis and Career Path Recommendation System** 
 This is very close to your project because it focuses on **skill-gap analysis and career-path recommendation**, and the IEEE result explicitly mentions **knowledge graph visualization**. 
 urlIEEE Xplore paperhttps://ieeexplore.ieee.org/document/11634695/

2. **Skill-Based Recommender System for Internship and Industry Hiring using Knowledge Graphs** 
 Introduces a **knowledge-graph-driven recommender framework** representing skills, job roles, and opportunities as interconnected entities. This strongly supports your proposed graph schema. 
 urlIEEE Xplore paperhttps://ieeexplore.ieee.org/document/11354307/

3. **Development of a Knowledge Graph-Based Model for Recommendation** 
 Uses **heterogeneous knowledge graphs** to bridge skills/competencies and job recommendations, including suggestions for additional courses. Very relevant to your **current skill → missing skill → training → job** pipeline. 
 urlIEEE Xplore paperhttps://ieeexplore.ieee.org/document/10804810/ 
 urlDirect IEEE PDFhttps://ieeexplore.ieee.org/iel8/6287639/10380310/10804810.pdf

4. **Knowledge Graphs in Education and Employability** 
 This is especially useful for your literature review because it discusses how knowledge graphs can connect **education, skills and labour-market requirements** and help identify employment-market needs. 
 urlDirect IEEE PDFhttps://ieeexplore.ieee.org/iel7/6287639/9668973/09840388.pdf

5. **Leveraging Knowledge Graphs for Personalized Internship Recommendations** 
 Builds personalized recommendations by integrating **course syllabi, student competencies and internship/job requirements through a knowledge graph**. Good supporting work for profile-to-opportunity matching. 
 urlIEEE Xplore paperhttps://ieeexplore.ieee.org/document/10987407/

6. **SkillBridge: A Job-Course Matching Framework Using Pre-Trained Language Models and Graph Representation** 
 Highly relevant because your architecture also needs to bridge **jobs and training courses**. This work combines pretrained language models with graph representations for job-course matching. 
 urlIEEE Xplore paperhttps://ieeexplore.ieee.org/document/11006254/

7. **Enhancing Career Matching with BERT and Graph Neural Networks** 
 Combines **BERT semantic understanding + Graph Neural Networks** to build dynamically updated career representations. Useful if later you want to make your graph-ranking layer more sophisticated than rule-based Cypher traversal. 
 urlIEEE Xplore paperhttps://ieeexplore.ieee.org/document/10985284/

8. **Sankalp: AI-Powered Career Guidance System** 
 This is one of the **closest overall matches** to your proposed application. The IEEE result specifically describes a **Voice Assistant module enabling multimodal and multilingual interaction**, and also mentions a **Knowledge Graph connecting careers, skills and subjects**. 
 urlDirect IEEE PDFhttps://ieeexplore.ieee.org/iel8/6287639/10820123/11271208.pdf

9. **A Seamless ChatGPT Knowledge Plug-in for the Labour Market** 
 Focuses on improving access to labour-market information through a conversational interface. It is useful for the **LLM/conversational layer** of your system rather than the KG itself. 
 urlDirect IEEE PDFhttps://ieeexplore.ieee.org/iel8/6287639/10380310/10731911.pdf

For your **fourth-year project literature review**, I would prioritize these four:

**Sankalp** → strongest match for **voice + multilingual + career guidance + KG**. 
**AI-Powered Skill Gap Analysis and Career Path Recommendation** → strongest for **skill-gap reasoning**. 
**Knowledge Graphs in Education and Employability** → strongest academic foundation for **KG + education + labour market**. 
**Development of a Knowledge Graph-Based Model...** → strongest for **graph-based job/course recommendation**.

These give you a strong research lineage for your novelty claim:

> Existing IEEE work covers career guidance, skill-gap analysis, multilingual voice interaction, education/employability graphs and job-course matching, but your proposed system combines these around **PM-AJAY beneficiaries and NSQF/NQR-aligned livelihood pathways in Indian regional languages**.

Note that some IEEE PDFs may require institutional/IEEE access even when a direct PDF URL exists.

## User

Give me official website of SIH for problem statement 26097. I want to write down the problem statement for my project. So give me the website of SIH so that I can verify it. You don't send me the problem statement, send me the website where that 26097 problem statement is.

## Assistant

Worked for a few seconds

## Assistant

The **official Smart India Hackathon website** is:

urlSmart India Hackathon — Official Websitehttps://www.sih.gov.in/

That is the **AICTE/MoE official SIH domain**. citeturn0search12

For **SIH26097**, go to the official site and open the **Problem Statements** section, then search/filter for **`SIH26097`**.

I specifically searched the official `sih.gov.in` domain, but Google currently isn't exposing an individually indexed official page for `SIH26097`. So I would **not use the `sih2026.vuce.in` mirror as your official citation** for your fourth-year project; use `sih.gov.in` and verify the PS there.

## User

What is project domain

## Assistant

For your **SIH26097 + Knowledge Graph project**, I recommend writing the project domain as:

**Domain: Artificial Intelligence & Machine Learning (AI/ML)**

If your college form allows a more specific domain, use:

**Artificial Intelligence & Machine Learning — Knowledge Graphs, Multilingual Voice AI & Recommendation Systems**

And if it asks for an **application area** separately:

**Application Area: Skill Development, Career Guidance & Livelihood Recommendation**

So for your final-year project form, my preferred entry is simply **Artificial Intelligence & Machine Learning (AI/ML)**.

## User

Any other than Domain: Artificial Intelligence & Machine Learning (AI/ML) 
Suggest oneline multiple answer

## Assistant

- **Knowledge Graphs & Intelligent Recommendation Systems**
- **Natural Language Processing & Conversational AI**
- **Multilingual Voice-Based Intelligent Systems**
- **AI for Skill Development & Career Guidance**
- **Knowledge-Based Systems & Semantic AI**
- **Intelligent Decision Support Systems**
- **AI for Social Impact & Digital Inclusion**
- **Semantic Web & Knowledge Engineering**
- **Graph-Based AI & Recommendation Systems**
- **Conversational AI for Livelihood & Skilling**
- **AI-Driven Education & Employability Systems**
- **Human-Centered AI & Assistive Technologies**

## User

do you know my project EchoQuery

## Assistant

Yes. **EchoQuery** is your SIH project for **SIH260097**, originally developed as **EchoQuery-RAG-based-STT**.

The core idea is a **multilingual voice-based RAG system**, aimed at vocational-training/accessibility use cases. Your architecture has included **STT → query processing → RAG/vector retrieval → generated answer**, with FastAPI + WebSockets on the backend and Qdrant as the vector database.

I also remember you tested **Sarvam** and **Voxtral Mini** for STT, worked with the **AI4Bharat MSMARCO-XI** multilingual dataset, and structured the repo into contracts, backend API, RAG engine, external services, data, evaluation, scripts, infrastructure, and docs.

So yes—I have the project context. What are you planning to do with EchoQuery now? memcite

## User

there are some changes to it, i am going to use Neo4j as graph knowledge base

## Assistant

Yes. I’ll treat this as the **updated EchoQuery architecture going forward**:

**EchoQuery will use Neo4j as its graph-based knowledge base**, rather than relying only on the earlier vector-database/RAG approach.

This actually matches the architecture in your latest project abstract: the Knowledge Graph is defined as the core intelligence layer, with Neo4j + Cypher for graph storage/traversal, while the LLM/NLP layer handles profile extraction, clarification, and natural-language explanations. fileciteturn4file0L39-L43 fileciteturn4file0L120-L122

So I’ll consider the new EchoQuery flow roughly:

**Voice → STT/Language Detection → Profile Extraction → Neo4j Knowledge Graph → Graph Traversal/Skill-Gap Reasoning → Recommendation/Ranking → LLM Explanation → TTS**

And Neo4j would hold relationships such as `Beneficiary → HAS_SKILL → Skill`, `Occupation → REQUIRES_SKILL → Skill`, `Qualification → ALIGNED_WITH → NSQFLevel`, `Qualification → PREPARES_FOR → Occupation`, and `Occupation → HAS_OPPORTUNITY_IN → Location`. Your abstract already defines these node types and relationships. fileciteturn4file0L44-L61

So from now on, when we discuss **EchoQuery**, I’ll base suggestions on the **Neo4j Knowledge Graph architecture**, not the old Qdrant-only RAG design. memcite

## User

ok i want to update codex on it, he is far behind on this, please give me, prompt so that it updates projects .context folder

## Assistant

Yes. Since Codex is significantly behind, I’d give it a **context-reconciliation prompt**, not an implementation prompt. The goal is for it to inspect the repository and update `.context/` so future agents stop working from the old Qdrant/vector-RAG assumptions.

Your latest document explicitly makes the Knowledge Graph the core intelligence layer and specifies Neo4j/Cypher, beneficiary subgraphs, graph-based skill-gap reasoning, and a hybrid AI architecture. fileciteturn4file0L39-L43 fileciteturn4file0L75-L100

Use this prompt with Codex:

```text
You need to bring this repository's `.context/` documentation up to date.

IMPORTANT:
This is primarily a CONTEXT/DOCUMENTATION reconciliation task.
Do NOT start implementing the new architecture.
Do NOT refactor working code just to make it match the new plan.
First inspect the repository, understand the current implementation and existing `.context/` files, then update `.context/` so future coding agents have an accurate source of truth.

PROJECT: EchoQuery

EchoQuery has changed significantly from its earlier architecture. Some existing repository context may still describe an older RAG/vector-database-centric design. That information must not be treated as the current target architecture.

==================================================
CURRENT PRODUCT DIRECTION
==================================================

EchoQuery is now a multilingual, voice-first livelihood intelligence and skilling recommendation system based on SIH26097.

The product story is:

User speaks naturally
→ understand beneficiary
→ construct structured beneficiary profile
→ map profile into a Knowledge Graph
→ identify skill gaps
→ traverse NSQF/NQR-aligned training pathways
→ connect pathways to occupations/livelihood opportunities
→ rank suitable pathways
→ explain recommendation
→ return response through voice/text

The important product insight is:

This is NOT simply:
"AI recommends courses."

It is:

"A person with limited digital literacy can speak in their own language, and the system guides them from their current skills → skill gap → NSQF-aligned training → livelihood opportunity."

==================================================
KNOWLEDGE GRAPH IS NOW CORE
==================================================

Neo4j is now the intended graph knowledge base.

The Knowledge Graph is NOT an optional visualization layer.

It is intended to become the structured intelligence/domain layer connecting:

- beneficiaries
- skills
- interests
- education
- occupations/job roles
- sectors
- qualifications
- NSQF levels
- NOS/modules
- eligibility requirements
- progression pathways
- locations
- livelihood opportunities
- employment types
- training providers

Representative node types:

Beneficiary
Skill
Interest
Occupation
Qualification
NSQFLevel
NOS
Sector
EducationLevel
Location
LivelihoodOpportunity
EmploymentType
TrainingProvider

Representative relationships:

HAS_SKILL
INTERESTED_IN
LIVES_IN
HAS_EDUCATION
PREFERS_EMPLOYMENT
REQUIRES_SKILL
BELONGS_TO_SECTOR
ALIGNED_WITH
HAS_NOS
PREPARES_FOR
PROGRESSES_TO
ELIGIBLE_WITH
AVAILABLE_IN
HAS_OPPORTUNITY_IN
TRAINED_BY
SIMILAR_TO

These are conceptual relationships, not necessarily a finalized database schema.
Do not invent implementation details where the repository/context has not decided them yet.

==================================================
TARGET REASONING MODEL
==================================================

The intended separation of responsibilities is:

Voice/STT layer
 ↓
Language / speech understanding
 ↓
Structured beneficiary profile extraction
 ↓
Beneficiary subgraph
 ↓
Neo4j Livelihood + NSQF Knowledge Graph
 ↓
Graph traversal / skill-gap reasoning
 ↓
Candidate pathway generation
 ↓
Hybrid ranking
 ↓
Explanation generation
 ↓
TTS / UI response

The LLM should NOT be the authoritative source for NSQF facts or qualification relationships.

Conceptually:

LLM/NLP:
- understand user conversation
- extract structured information
- ask clarification questions
- generate natural-language explanations

Neo4j Knowledge Graph:
- represent domain entities
- represent relationships
- store grounded qualification/livelihood knowledge
- support graph traversal
- support skill-gap reasoning
- provide provenance/evidence paths

Rules / deterministic logic:
- eligibility constraints
- invalid pathway filtering
- hard constraints where appropriate

Ranking layer:
- beneficiary/profile fit
- skill-gap distance
- interests/preferences
- local opportunity relevance
- other future graph-derived features

==================================================
GRAPH-BASED SKILL GAP EXAMPLE
==================================================

Example spoken input:

"I completed 10th. I help my father repair agricultural machinery.
I know basic welding and want a job near my village."

Possible structured profile:

Education = 10th
Skill = Basic Welding
Experience = Machinery Repair
Interest = Mechanical Work
Mobility = Local Only
EmploymentPreference = Wage Employment

Conceptual graph reasoning:

Beneficiary
→ HAS_SKILL
→ Basic Welding

Basic Welding
→ MATCHES / RELATED_TO
→ Welder Assistant

Welder Assistant
→ REQUIRES_SKILL
→ Workplace Safety
→ Blueprint Reading
→ Advanced Welding

Missing competencies
→ COVERED_BY
→ relevant Qualification

Qualification
→ ALIGNED_WITH
→ NSQF Level

Qualification
→ PREPARES_FOR
→ Occupation

Occupation
→ HAS_OPPORTUNITY_IN
→ relevant local livelihood ecosystem

The system should eventually be able to explain:

- why this occupation/pathway fits
- which existing skills contributed
- which skills are missing
- which qualification bridges the gap
- what progression is possible
- what livelihood/employment path it can lead to

==================================================
MULTILINGUAL STRATEGY
==================================================

MVP languages:

- Marathi
- Hindi
- English

The core recommendation/graph system should remain language-neutral.

Do NOT create separate recommendation logic or separate graphs per language.

Preferred conceptual boundary:

speech/language
 ↓
normalized structured semantic profile
 ↓
same graph/recommendation engine

Additional Indian languages should later be pluggable through STT/TTS/language adapters without redesigning the core reasoning system.

==================================================
NSQF / NQR
==================================================

The target graph should eventually incorporate curated NSQF/NQR-aligned knowledge such as:

Qualification
NSQF level
Occupation/job role
Eligibility
Skills/competencies
NOS/modules
Progression pathways
Sector
Training relationship

Do NOT assume arbitrary LLM-generated qualification data is valid.

The graph should eventually be populated through a controlled ingestion/normalization pipeline from authoritative/curated data.

==================================================
CURRENT VS TARGET ARCHITECTURE
==================================================

This repository may currently contain code/config/docs for the OLD architecture, including:

- Qdrant
- vector retrieval
- RAG
- embeddings
- MSMARCO-XI
- previous STT experiments
- older SIH assumptions
- old architecture diagrams
- old service boundaries

DO NOT blindly delete these references.

Inspect what actually exists.

Classify architecture information into:

1. CURRENTLY IMPLEMENTED
2. CURRENT TARGET
3. LEGACY / SUPERSEDED
4. STILL UNDECIDED

This distinction is extremely important.

For example:

If Qdrant is currently implemented but Neo4j is only the new target:

Correct documentation:
"Qdrant exists in the current implementation, but the target architecture is moving toward Neo4j as the primary structured knowledge/reasoning layer."

Incorrect documentation:
"Qdrant has been removed."

Do not claim migrations or implementation work have happened unless they actually exist in the repository.

==================================================
WHAT TO DO
==================================================

1. Inspect the repository structure.

2. Read:
 - AGENTS.md files
 - README
 - `.context/`
 - architecture docs
 - contracts
 - backend structure
 - AI/RAG modules
 - infrastructure/config
 - relevant tests

3. Determine what EchoQuery currently implements.

4. Determine which `.context/` information is stale or contradictory.

5. Update `.context/` to establish a clean source of truth for the new direction.

Prefer MODIFYING existing context files over creating many redundant files.

Only create a new context file when the information clearly does not belong in an existing one.

==================================================
THE UPDATED CONTEXT SHOULD CAPTURE
==================================================

At minimum:

PROJECT PURPOSE
- What EchoQuery now is
- Target users/problem
- Core product story

ARCHITECTURE
- Current implementation
- Target architecture
- Neo4j's role
- LLM's role
- voice/STT/TTS boundaries
- recommendation/ranking boundaries

KNOWLEDGE GRAPH
- purpose
- conceptual entities
- conceptual relationships
- graph reasoning responsibilities
- skill-gap reasoning
- explainability/provenance

DATA
- authoritative NSQF/NQR intent
- ingestion principles
- language-neutral representation
- current datasets that still exist
- legacy datasets/components where applicable

MULTILINGUAL
- Marathi/Hindi/English MVP
- language adapter boundary
- normalized semantic profile

MIGRATION STATUS
Clearly distinguish:

Implemented now
Planned next
Legacy
Experimental
Unknown / needs decision

NON-GOALS / GUARDRAILS
- Do not let the LLM invent authoritative NSQF facts.
- Do not duplicate recommendation engines per language.
- Do not treat Neo4j as merely visualization.
- Do not claim a legacy component has been removed unless code confirms it.
- Do not prematurely design a huge ontology.
- Do not add unnecessary microservices.
- Preserve clean contracts and minimal architecture.

==================================================
IMPORTANT ENGINEERING PRINCIPLES
==================================================

Keep the architecture deliberate and minimal.

Avoid:
- spaghetti architecture
- unnecessary services
- premature abstractions
- giant ontology design before MVP needs are known
- rewriting working components without reason
- mixing language-specific concerns with domain reasoning
- using an LLM where deterministic graph/rule reasoning is more appropriate

Prefer:
- explicit contracts
- typed schemas
- clear ownership boundaries
- provenance
- testable graph queries
- deterministic constraints
- small composable components
- incremental migration

==================================================
DELIVERABLE
==================================================

Update ONLY the relevant `.context/` documentation in this task unless a tiny adjacent documentation correction is absolutely required.

Do not implement Neo4j yet.
Do not install dependencies.
Do not modify application behavior.
Do not perform the Qdrant → Neo4j migration.

After updating `.context/`, report:

1. Files inspected
2. Context files changed
3. Stale assumptions removed/corrected
4. Current implementation as discovered from code
5. New target architecture recorded
6. Current-vs-target differences
7. Open architectural decisions that should NOT be guessed
8. Any contradictions still present elsewhere in the repository

The final `.context/` documentation should be sufficient for a fresh Codex/Claude agent to enter this repository and understand that:

Neo4j + graph-based reasoning is the new target direction,
but existing code must be treated according to its actual migration state.
```

One thing I intentionally did here is **not tell Codex that “Qdrant is gone.”** Your previous EchoQuery implementation did use Qdrant, whereas the new project document establishes Neo4j as the recommended KG implementation. fileciteturn4file0L120-L122 This prompt forces Codex to inspect the actual repo and document the transition accurately instead of rewriting history or immediately ripping out working components.

Also, your latest abstract already defines the KG entities/relationships and graph-based skill-gap flow, so those are included as the new source-of-truth concepts. fileciteturn4file0L44-L72

I’d run this with your **review/Sol or Astra profile**, because this is mostly repository-wide context reconciliation rather than coding. memcite

## User

which skill should i use with model tera high or xhigh

## Assistant

Worked for a couple of seconds

## Assistant

For **this exact task—reconciling the whole EchoQuery repo and updating `.context/`—use:**

**Model:** `gpt-5.6-terra` 
**Reasoning:** `high` 
**Skill:** **Planning / architecture skill** if you have one; otherwise **no special skill is necessary**.

I would **not use xhigh initially**. This task requires broad repository inspection and careful current-vs-target reconciliation, but the actual edits are documentation. OpenAI's current guidance positions Terra for everyday repository work and higher reasoning for harder analysis; increasing effort also increases allowance usage and doesn't automatically improve results. citeturn0search11

From the skills you've told me you have installed, I would specifically **avoid** `feature-dev`, `superpowers`, frontend/design skills, and similar implementation-heavy skills here. They can encourage unnecessary implementation/subagents when all you want is `.context/` reconciliation.

So I'd run:

```toml
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
```

Then paste the prompt I gave you.

If **Terra High** finishes but misses architectural contradictions, misunderstands the old Qdrant state, or doesn't inspect enough of the repository, *then* rerun/review with **Terra xhigh**. xhigh is better reserved for unusually difficult cross-cutting analysis rather than being the default. citeturn0search0

For the **later actual Neo4j migration**, that's where I'd consider **Terra xhigh or Sol high** because it will involve contracts, data modelling, Cypher queries, migration decisions, tests, and integration across several modules. memcite

## User

suggest a good one like \[mattpocock / skills\](https://github.com/mattpocock/skills) how to use this for making echoquery

## Assistant

Worked for a few seconds

## Assistant

Yes — I checked urlMatt Pocock's skills repositoryhttps://github.com/mattpocock/skills, and it actually fits **EchoQuery very well**. I would use it rather than hunting for one generic “software architect” skill.

The repo is explicitly designed around preventing agent-built codebases from accumulating architectural complexity, with workflows for domain modelling, architecture decisions, specs, TDD, implementation, and review. citeturn0search0turn0search2

### For EchoQuery, use this workflow

First install the engineering skills into Codex:

```powershell
cd "D:\ALL Programming\Hacker_House\EchoQuery-RAG-based-STT"

npx skills@latest add mattpocock/skills
```

Select at least:

```text
setup-matt-pocock-skills
ask-matt
grill-with-docs
to-spec
to-tickets
implement
improve-codebase-architecture
```

The repository recommends installing `setup-matt-pocock-skills` and running it once per repository before the other engineering workflows. citeturn0search16turn0search7

Then I would **not jump directly into `/implement`** for Neo4j.

Use this sequence:

```text
/setup-matt-pocock-skills
 ↓
/grill-with-docs
 ↓
/to-spec
 ↓
/to-tickets
 ↓
/implement
 ↓
/improve-codebase-architecture
```

For **where you are right now**, `/grill-with-docs` is probably the most valuable skill. It interrogates the design while simultaneously building the project's domain model and updating `CONTEXT.md`/ADRs. citeturn0search0

Give it your updated EchoQuery context:

```text
/grill-with-docs

We are redesigning EchoQuery's knowledge/retrieval architecture.

The repository contains an older multilingual voice-RAG implementation.
The new target architecture introduces Neo4j as the primary structured
knowledge base and graph-reasoning layer.

Target product flow:

Voice
→ STT / language identification
→ structured beneficiary profile
→ beneficiary subgraph
→ Neo4j livelihood + NSQF knowledge graph
→ graph-based skill-gap reasoning
→ candidate pathway generation
→ local opportunity-aware ranking
→ explainable recommendation
→ TTS

MVP languages:
- Marathi
- Hindi
- English

The graph should model concepts including:

Beneficiary
Skill
Interest
Occupation
Qualification
NSQFLevel
NOS
Sector
EducationLevel
Location
LivelihoodOpportunity
EmploymentType
TrainingProvider

Potential relationships include:

HAS_SKILL
INTERESTED_IN
LIVES_IN
HAS_EDUCATION
PREFERS_EMPLOYMENT
REQUIRES_SKILL
BELONGS_TO_SECTOR
ALIGNED_WITH
HAS_NOS
PREPARES_FOR
PROGRESSES_TO
ELIGIBLE_WITH
AVAILABLE_IN
HAS_OPPORTUNITY_IN
TRAINED_BY

Important:

Do not assume Qdrant or the existing RAG pipeline should simply be deleted.

Inspect the repository and challenge the architecture.

I want us to determine:

1. What Neo4j should own.
2. What the LLM should own.
3. Whether vector retrieval still has a legitimate role.
4. How NSQF/NQR data should enter the graph.
5. What belongs in the beneficiary subgraph.
6. What graph schema is sufficient for the MVP.
7. How skill-gap reasoning should work.
8. Which decisions should be deterministic.
9. How recommendation ranking should work.
10. How recommendation provenance/explainability should work.
11. Where multilingual normalization belongs.
12. What the migration path from the current architecture should be.

Avoid overengineering.

Do not implement anything yet.

Interrogate the architecture until the important decisions are resolved,
and record durable terminology/architectural decisions in the project's
context documentation and ADRs.
```

This is much better than telling Codex, *“implement Neo4j.”*

The skill's domain-modelling discipline is particularly useful here because it distinguishes between **terminology problems** and **module/seam problems**, and can record hard-to-reverse choices as ADRs. citeturn0search13

Once that session settles questions like:

```text
Is Neo4j replacing Qdrant?
 │
 ┌─────┴─────┐
 ↓ ↓
 YES NO
 │
 Hybrid retrieval?
 │
 ┌───────┴────────┐
 ↓ ↓
 Vector search Graph search
 │ │
 └───────┬────────┘
 ↓
 Candidate set
 ↓
 Graph reasoning
 ↓
 Rank
```

then run `/to-spec`. That skill explicitly explores the repository, uses your established domain vocabulary and ADRs, and converts the decisions into an implementation specification. citeturn0search4

Then `/to-tickets` can split the migration into small tracer-bullet pieces instead of asking one giant Codex session to rewrite EchoQuery. citeturn0search2

For example, you could end up with:

```text
T01 — Define canonical graph domain model
 ↓
T02 — Add Neo4j infrastructure + configuration
 ↓
T03 — Implement graph repository interface
 ↓
T04 — Build NSQF/NQR ingestion pipeline
 ↓
T05 — Build beneficiary subgraph writer
 ↓
T06 — Implement skill-gap Cypher queries
 ↓
T07 — Candidate occupation/pathway retrieval
 ↓
T08 — Hybrid ranking
 ↓
T09 — Explanation/provenance contract
 ↓
T10 — Connect voice pipeline
 ↓
T11 — Evaluation
```

Each ticket can then go through `/implement`, which Matt's workflow couples with TDD and code review rather than allowing the coding agent to make the entire architectural migration in one uncontrolled pass. citeturn0search0

Finally, periodically run:

```text
/improve-codebase-architecture
```

That skill scans for architectural “deepening” opportunities—places where interfaces are leaking, modules are too shallow, or understanding one concept requires jumping through many files. Matt specifically recommends periodically running it against an agent-built codebase. citeturn0search15turn0search0

### One change I'd make for your `.context/` setup

Matt's skills expect their own domain-document conventions around `CONTEXT.md` and ADRs, while **you already have an established `.context/` directory** for EchoQuery. His setup skill normally configures where domain docs live and records that configuration under `docs/agents/`. citeturn0search7

So when `/setup-matt-pocock-skills` asks where project/domain documentation should live, **point it toward your existing `.context/` structure rather than allowing Codex to create a second competing source of truth**.

That gives you something close to:

```text
AGENTS.md
 │
 ├── .context/
 │ ├── project.md
 │ ├── architecture.md
 │ ├── domain.md
 │ ├── data.md
 │ └── ...
 │
 └── docs/
 └── adr/
 ├── 001-neo4j-knowledge-graph.md
 ├── 002-vector-retrieval-role.md
 └── 003-language-neutral-profile.md
```

The `.context/` files tell agents **what EchoQuery currently is**; ADRs explain **why consequential architecture decisions were made**.

For your current stage, I'd run **`Terra High + /grill-with-docs` first**. Don't use xhigh or `/implement` yet. Once the Neo4j/Qdrant/retrieval/schema boundaries are settled, turn that into a spec and only then start implementation.

## User

i want to use it globally

## Assistant

Yep — if you want **Matt Pocock's skills available globally in Codex**, don't install them inside the EchoQuery repo.

From PowerShell, you can run this from anywhere:

```powershell
npx skills@latest add mattpocock/skills --global
```

That installs the skills globally so they can be used across **EchoQuery, OCR-GST, Audora, Statskill**, and your future repositories.

urlMatt Pocock / skillshttps://github.com/mattpocock/skills

Then go into EchoQuery:

```powershell
cd "D:\ALL Programming\Hacker_House\EchoQuery-RAG-based-STT"
```

and initialize/configure Matt's workflow **for this repository**:

```text
/setup-matt-pocock-skills
```

The important distinction is:

```text
GLOBAL
~/.agents/skills/
 │
 └── Matt Pocock skills
 │
 ├── available in EchoQuery
 ├── available in OCR-GST
 ├── available in Audora
 └── available in other repos

PER PROJECT
EchoQuery/
├── .context/ ← EchoQuery-specific knowledge
├── docs/adr/ ← EchoQuery architecture decisions
└── AGENTS.md ← EchoQuery-specific agent instructions
```

So **skills = global**, while **project context/configuration = local**. That's the setup I'd use.

For EchoQuery specifically, after global installation I'd start with:

```text
/setup-matt-pocock-skills
```

then use:

```text
/grill-with-docs
```

for the Neo4j architecture discussion, followed by:

```text
/to-spec
/to-tickets
/implement
```

Don't put EchoQuery-specific architecture into the global skill itself; keep that in your `.context/`/ADRs so the same global skills remain reusable across all your projects.

## User

there is no codex? then what to select

## Assistant

It **is there**. In your screenshot, under **“Which agents do you want to install to?”**, I can see:

> `• Codex`

It’s the **third item**, immediately below `Amp` and `Cline`.

Your screen currently says:

> `Selected: Amp, Cline, Codex +11 more`

So you’ve accidentally selected a bunch of agents.

Since you want these globally for **Codex**, I’d do this:

1. Use **↑ / ↓** to move through the list.
2. Press **Space** to deselect everything you don't use.
3. Keep **Codex** selected.
4. **Universal (`.agents/skills`)** says *always included*, so that's expected.
5. Press **Enter** to confirm.

You should ideally end up with something like:

```text
Selected: Codex
```

plus the automatically included **Universal `.agents/skills`** location.

You **do not need** to select Cursor, Cline, Amp, Gemini CLI, etc. just because they're available. If you also actively use Claude Code, scroll/check whether **Claude Code** is among the additional agents and select that too; otherwise just Codex is enough.

## User

oh ok got it

## Assistant

Perfect 👍

## User

@Notion write notes for me in notion giving me step by step guide to use this skill not only for echoquery but for everything in the future, to make me better coder.

and then in that add sub page specifically for guide for EchoQuery, to use these skills 

first give me confirmation that u can use my notion to write

## Assistant

Worked for 18s

## Assistant

Yes — I can access your connected **Notion workspace** and I have permission to **create pages and sub-pages** there. fileciteturn6file0L1-L1

I can create exactly what you described:

- a main page like **“Matt Pocock Skills — Personal Coding Playbook”** with a reusable, step-by-step guide for using the skills across future projects;
- inside it, a dedicated **EchoQuery** sub-page covering the recommended flow for that project: setup → architecture/domain modelling → spec → tickets → implementation → review/refactor;
- practical guidance on **when to use each skill, which model/reasoning level to pair with it, prompts to paste, mistakes to avoid, and a repeatable workflow** so it becomes a long-term coding system rather than an EchoQuery-only note.

I can write this directly into your Notion now.

## User

ok do it

## Assistant

Worked for 1m 45s

## Assistant

Done — I created both pages directly in your Notion:

**🧭 Main page:** urlMatt Pocock Skills — Personal Coding Playbookhttps://app.notion.com/p/3ddba935a9db818eb958cd7f157eb8ba?pvs=204

It covers the reusable workflow for future projects: `setup → domain-modeling → grill-with-docs → to-spec → to-tickets → implement → code-review → architecture improvement`, plus when to skip skills, Terra High vs xhigh, reusable prompt templates, coding habits, and anti-patterns.

**🕸️ EchoQuery sub-page:** urlEchoQuery — Using the Skills for the Neo4j Migrationhttps://app.notion.com/p/3ddba935a9db81a19ba3cf2d11f46b79?pvs=204

That one specifically covers the **Neo4j transition**, current-vs-target architecture, KG domain modelling, ADRs, migration specification, suggested tracer-bullet tickets, implementation/review workflow, responsibility boundaries, graph reasoning, and EchoQuery-specific guardrails.

I also deliberately made the first meaningful Neo4j milestone an **end-to-end vertical slice**, rather than simply “install Neo4j.” memcite

## Resources

### Local attachments
- [HERFIT NOVELTY.pdf](../../../Raw/Export/file_0000000074d8820685105806e9ff2f2d.dat)
- [EchoQuery_Final_Year_Project_Abstract.pdf](../../../Raw/Export/file_00000000bdcc82119d0ff59e4aea95b5.dat)
- [d175b040-dd93-430f-b2f8-42ecb719b00f.png](../../../Raw/Export/file_00000000ca4c81f5aa5f1a08053b3697.dat)

### External references
- [National Skills Qualification Framework - National Council for Vocational Education and Training](https://ncvet.gov.in/national-skills-qualification-framework/)
- [NSQF Notification - National Council for Vocational Education and Training](https://ncvet.gov.in/national-skills-qualification-framework/nsqf-notification/)
- [Policies and Guidelines - National Council for Vocational Education and Training](https://ncvet.gov.in/guidelines)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2297199&lang=1&reg=3)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2223183&lang=1&reg=6)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2247756&lang=1&reg=3)
- [About NSQF | Government of India : National Institute of Electronics & Information Technology](https://www.nielit.gov.in/kolkata/content/nsqf)
- [About NSQF | Government of India : National Institute of Electronics & Information Technology](https://www.nielit.gov.in/srinagar/content/nsqf)
- [About NSQF | Government of India : National Institute of Electronics & Information Technology](https://www.nielit.gov.in/chandigarh/content/nsqf)
- [SIH26097 · AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY | SIH 2026 Problem Statements](https://sih2026.vuce.in/ps/SIH26097)
- [National Qualification Register](https://www.nqr.gov.in/nsqf)
- [NITI Aayog](https://www.niti.gov.in/node/2397)
- [FAQ's | Department of Empowerment of Persons with Disabilities (DEPwD) | India](https://depwd.gov.in/en/faqs-3/)
- [Skill Development Programmes | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/content/skill-development-programmes)
- [Income Generating Schemes | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/content/income-generating-schemes)
- [About Scheme | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/content/about-scheme)
- [Illustrative list of domain under GIA | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/illustrative-list)
- [Circulars | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/Circulars)
- [Sanction Orders | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/Sanction-Orders)
- [About Scheme | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/About-Scheme)
- [Home | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/)
- [Infrastructure Development | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/content/infrastructure-development)
- [Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY) | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/schemes/104)
- [SIH26097 · AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY | SIH 2026 Problem Statements](https://sih2026.vuce.in/ps/SIH26097?utm_source=chatgpt.com)
- [Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY) | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/schemes/104?utm_source=chatgpt.com)
- [Skill Development Programmes | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/content/skill-development-programmes?utm_source=chatgpt.com)
- [National Skills Qualification Framework - National Council for Vocational Education and Training](https://ncvet.gov.in/national-skills-qualification-framework/?utm_source=chatgpt.com)
- [NSQF Notification - National Council for Vocational Education and Training](https://ncvet.gov.in/national-skills-qualification-framework/nsqf-notification/?utm_source=chatgpt.com)
- [Policies and Guidelines - National Council for Vocational Education and Training](https://ncvet.gov.in/guidelines?utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2297199&lang=1&reg=3&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2223183&lang=1&reg=6&utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2247756&lang=1&reg=3&utm_source=chatgpt.com)
- [Income Generating Schemes | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/content/income-generating-schemes?utm_source=chatgpt.com)
- [About Scheme | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/content/about-scheme?utm_source=chatgpt.com)
- [Illustrative list of domain under GIA | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/illustrative-list?utm_source=chatgpt.com)
- [Circulars | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/Circulars?utm_source=chatgpt.com)
- [Sanction Orders | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/Sanction-Orders?utm_source=chatgpt.com)
- [About Scheme | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/About-Scheme?utm_source=chatgpt.com)
- [Home | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/?utm_source=chatgpt.com)
- [Infrastructure Development | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/content/infrastructure-development?utm_source=chatgpt.com)
- [What's New | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/whats-new?utm_source=chatgpt.com)
- [Flow Chart | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/Flow-Chart?utm_source=chatgpt.com)
- [Flow Chart | Pradhan Mantri Anusuchit Jaati Abhyuday Yojna (PM-AJAY)](https://pmajay.dosje.gov.in/Flow-Chart-State?utm_source=chatgpt.com)
- [About NSQF | Government of India : National Institute of Electronics & Information Technology](https://www.nielit.gov.in/kolkata/content/nsqf?utm_source=chatgpt.com)
- [About NSQF | Government of India : National Institute of Electronics & Information Technology](https://www.nielit.gov.in/srinagar/content/nsqf?utm_source=chatgpt.com)
- [About NSQF | Government of India : National Institute of Electronics & Information Technology](https://www.nielit.gov.in/chandigarh/content/nsqf?utm_source=chatgpt.com)
- [National Qualification Register](https://www.nqr.gov.in/nsqf?utm_source=chatgpt.com)
- [News / Events (What's New) | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/whats-new/1493?utm_source=chatgpt.com)
- [DoSJE](https://www.socialjustice.gov.in/social-audit/schemes?utm_source=chatgpt.com)
- [News / Events (What's New) | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/index.php/whats-new/1493?utm_source=chatgpt.com)
- [Meta Data | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/whats-new/77898?utm_source=chatgpt.com)
- [Scheme For Residential Education For Students in High Schools in Targeted Areas (SHRESHTA) | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/schemes/41?utm_source=chatgpt.com)
- [DoSJE](https://socialjustice.gov.in/social-audit/download-report?utm_source=chatgpt.com)
- [Scheme For Residential Education For Students in High Schools in Targeted Areas (SHRESHTA) | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/schemes/41/archive?utm_source=chatgpt.com)
- [DoSJE](https://www.socialjustice.gov.in/social-audit/download-report?utm_source=chatgpt.com)
- [Central Sector Scholarship of Top Class Education for SC Students | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/schemes/27?utm_source=chatgpt.com)
- [Schemes | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/schemes?utm_source=chatgpt.com)
- [FAQs | Department of Social Justice and Empowerment - Government of India](https://socialjustice.gov.in/common/74591?utm_source=chatgpt.com)
- [NITI Aayog](https://www.niti.gov.in/node/2397?utm_source=chatgpt.com)
- [FAQ's | Department of Empowerment of Persons with Disabilities (DEPwD) | India](https://depwd.gov.in/en/faqs-3/?utm_source=chatgpt.com)
- [Problem Statements | Smart India Hackathon 2026](https://sih-lemon-eight.vercel.app/problem-statements?utm_source=chatgpt.com)
- [SIH 26097 (SIH26097): AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY — Datasets, Tech Stack & Solution Strategy | SIH 2026 | SIH ONE](https://sihone.pages.dev/ps/26097?utm_source=chatgpt.com)
- [SIH 2026 Problem Statements Explorer | CodeHunters Academy](https://www.codehuntersacademy.com/sih-2026-ps?utm_source=chatgpt.com)
- [sih-2026-problem-statements/CHANGELOG.md at main · vedantchalke36/sih-2026-problem-statements · GitHub](https://github.com/vedantchalke36/sih-2026-problem-statements/blob/main/CHANGELOG.md?utm_source=chatgpt.com)
- [Smart-India-Hackathon-SIH-2026-Problem-Statements/README.md at main · NoBugNinja/Smart-India-Hackathon-SIH-2026-Problem-Statements · GitHub](https://github.com/NoBugNinja/Smart-India-Hackathon-SIH-2026-Problem-Statements/blob/main/README.md?utm_source=chatgpt.com)
- [GitHub - Rajkumar-Porandla/SIH-2026-Problem-Statements: 🚀 Complete dataset of all 231 Smart India Hackathon (SIH) 2026 Problem Statements (CSV, JSON, TXT) with full descriptions, organizations, themes, and Python scraper. · GitHub](https://github.com/Rajkumar-Porandla/SIH-2026-Problem-Statements?utm_source=chatgpt.com)
- [sih-winning-presentations/manifest.json at master · JoysonBeera/sih-winning-presentations · GitHub](https://github.com/JoysonBeera/sih-winning-presentations/blob/master/manifest.json?utm_source=chatgpt.com)
- [GitHub - RajnishPuri/Voco_World: A web/app based solution required for vocational training for persons with visual impairment. It would have greater accessibility support and a better user interface. · GitHub](https://github.com/RajnishPuri/Voco_World?utm_source=chatgpt.com)
- [GitHub - JoysonBeera/sih-winning-presentations: Curated archive of Smart India Hackathon (SIH) winning team presentations (PPTX/PDF), categorized by year and domain (2020–2026). · GitHub](https://github.com/JoysonBeera/sih-winning-presentations?utm_source=chatgpt.com)
- [sih-winning-presentations/README.md at master · JoysonBeera/sih-winning-presentations · GitHub](https://github.com/JoysonBeera/sih-winning-presentations/blob/master/README.md?utm_source=chatgpt.com)
- [Ministry of Education, Department of Higher Education](https://www.education.gov.in/technical-education-15?utm_source=chatgpt.com)
- [Samagra Shiksha](https://samagra.education.gov.in/vocational.html?utm_source=chatgpt.com)
- [Thematic Session | Government of India, Ministry of Education](https://www.education.gov.in/nep/aqeg-se?utm_source=chatgpt.com)
- [Consultation Process | Government of India, Ministry of Education](https://www.education.gov.in/nep/consultation-process?utm_source=chatgpt.com)
- [Samagra Shiksha](https://samagra.education.gov.in/about.html?utm_source=chatgpt.com)
- [education.gov.in](https://www.education.gov.in/docs/background_note_Reimagining_Vocational_Education_Skill_building_revised.pdf?utm_source=chatgpt.com)
- [Samagra Shiksha](https://samagra.education.gov.in/inclusive.html?utm_source=chatgpt.com)
- [Constitutional Provision | Government of India, Ministry of Education](https://www.education.gov.in/seventh_schedule_list-3?utm_source=chatgpt.com)
- [education.gov.in](https://www.education.gov.in/docs/Reimagining%20Vocational%20Education%20and%20Skill%20Building%2017%20sept%202021.pdf?utm_source=chatgpt.com)
- [education.gov.in](https://www.education.gov.in/nep/nep2020_final_eng.pdf?utm_source=chatgpt.com)
- [PRASHAST](https://prashast.education.gov.in/?utm_source=chatgpt.com)
- [Special Recruitment Drive to fill up of vacancies for Persons with Disabilities (PwDs) reg. | Government of India, Ministry of Education](https://www.education.gov.in/special-recruitment-drive-fill-vacancies-persons-disabilities-pwds-reg?utm_source=chatgpt.com)
- [Home | Ministry of Skill Development and Entrepreneurship](https://www.msde.gov.in/?wpmobileexternal=true&utm_source=chatgpt.com)
- [Home | Ministry of Skill Development and Entrepreneurship](https://www.msde.gov.in/?trk=public_post-text&utm_source=chatgpt.com)
- [msde.gov.in](https://www.msde.gov.in/offerings/schemes-and-services/details/jan-shikshan-sansthan-jsscjM4ATMtQWa?utm_source=chatgpt.com)
- [msde.gov.in](https://www.msde.gov.in/media/photo-gallery/skill-india-partners-crpf-jawans-skill-development-agenda-30th-august-2016?utm_source=chatgpt.com)
- [SANKALP INDIA](https://sankalp.msde.gov.in/?trk=public_post-text&utm_source=chatgpt.com)
- [msde.gov.in](https://www.msde.gov.in/offerings/schemes-and-services/details/initiatives-in-the-north-east-and-lwe-regions-MjM4ATMtQWa?utm_source=chatgpt.com)
- [PSCMR Smart Internal Hackathon 2026](https://pscmr.ac.in/PSCMR/sih/index.html?utm_source=chatgpt.com)
- [PSCMR Smart Internal Hackathon 2026](https://www.pscmr.ac.in/PSCMR/sih/index.html?utm_source=chatgpt.com)
- [Smart Education - SIH 2026 Problem Statements (11) | SIH 2026 Problem Statements](https://sih2026.vuce.in/themes/smart-education?utm_source=chatgpt.com)
- [SIH 2026 Problem Statement Research Explorer](https://sih26ps.vercel.app/?utm_source=chatgpt.com)
- [Problem Statements Explorer | OUCE SIH 2026](https://sih-ouce.meetthealtezza.tech/problem-statements?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC009?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC036?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC043?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC021?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC015?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC012?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC039?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/login?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC033?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC051?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC050?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC026?utm_source=chatgpt.com)
- [Customer Care Executive (Call Centre) | National Skill Development Corporation (NSDC)](https://nsdcindia.org/customer-care-executive-call-centre-0?utm_source=chatgpt.com)
- [Curriculum & Content Availability | National Skill Development Corporation (NSDC)](https://www.nsdcindia.org/contentavailability/1409?utm_source=chatgpt.com)
- [| National Skill Development Corporation (NSDC)](https://nsdcindia.org/nos-listing/38?utm_source=chatgpt.com)
- [Curriculum & Content Availability | National Skill Development Corporation (NSDC)](https://www.nsdcindia.org/contentavailability/1410?utm_source=chatgpt.com)
- [Packer | National Skill Development Corporation (NSDC)](https://nsdcindia.org/packer-1?utm_source=chatgpt.com)
- [National Occupational Standards and Model Curriculum | National Skill Development Corporation (NSDC)](https://www.nsdcindia.org/national-occupational-standards-and-model-curriculum?utm_source=chatgpt.com)
- [Curriculum & Content Availability | National Skill Development Corporation (NSDC)](https://www.nsdcindia.org/contentavailability/1562?utm_source=chatgpt.com)
- [Curriculum & Content Availability | National Skill Development Corporation (NSDC)](https://nsdcindia.org/contentavailability/1411/sites/default/files/files/contentavailability-exp/1411?utm_source=chatgpt.com)
- [Curriculum & Content Availability | National Skill Development Corporation (NSDC)](https://nsdcindia.org/contentavailability/1492?utm_source=chatgpt.com)
- [Retail Trainee Associate | National Skill Development Corporation (NSDC)](https://nsdcindia.org/retail-trainee-associate-0?utm_source=chatgpt.com)
- [Curriculum & Content Availability | National Skill Development Corporation (NSDC)](https://nsdcindia.org/contentavailability/1562?utm_source=chatgpt.com)
- [Curriculum & Content Availability | National Skill Development Corporation (NSDC)](https://www.nsdcindia.org/contentavailability/1492?utm_source=chatgpt.com)
- [(PDF) Assessment of Blindness Among Women in Mumbai](https://www.researchgate.net/publication/410828004_Assessment_of_Blindness_Among_Women_in_Mumbai?utm_source=chatgpt.com)
- [Vocational Training – Blind Relief Association](https://blindrelief.org/vocational-training/?utm_source=chatgpt.com)
- [NAB Unit Maharashtra | State Learning Centre](https://nabunitmaharashtra.org/disability-centre/state-learning-centre?utm_source=chatgpt.com)
- [niepvd.in](https://niepvd.in/?utm_source=chatgpt.com)
- [Activities](https://scd.tn.gov.in/activities.php?utm_source=chatgpt.com)
- [About Department | NIEPVD RC CHENNAI | India](https://niepvdrcchennai.nic.in/about-department/?utm_source=chatgpt.com)
- [ali yavar jung national institute for the hearing handicapped, mumbai](https://studylib.net/doc/7356248/ali-yavar-jung-national-institute-for-the-hearing-handica...?utm_source=chatgpt.com)
- [FAQ | NIEPVD Dehradun | India](https://niepvd.nic.in/faq/?utm_source=chatgpt.com)
- [SIH26097 — AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY | SIH Buddy](https://www.sihbuddy.in/ps/SIH26097)
- [SIH26097 roasted — Mild 🙂 | SIH Buddy](https://www.sihbuddy.in/roast/SIH26097)
- [SIH26097 — AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY | Zaid Sayyed](https://zaidsayyed.in/tools/sih-problem-statements/sih26097)
- [National Qualification Register](https://www.nqr.gov.in/aboutus)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/11035)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/12190)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/3198)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/2277)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/4116)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/11071)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/12127)
- [SIH 26097 (SIH26097): AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY — Datasets, Tech Stack & Solution Strategy | SIH 2026 | SIH ONE](https://sihone.pages.dev/ps/26097)
- [National Qualification Register](https://nqr.gov.in/qualifications/3223)
- [National Qualification Register](https://www.nqr.gov.in/aboutus?utm_source=chatgpt.com)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/11035?utm_source=chatgpt.com)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/12190?utm_source=chatgpt.com)
- [SIH26097 — AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY | SIH Buddy](https://www.sihbuddy.in/ps/SIH26097?utm_source=chatgpt.com)
- [SIH26097 roasted — Mild 🙂 | SIH Buddy](https://www.sihbuddy.in/roast/SIH26097?utm_source=chatgpt.com)
- [SIH26097 — AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY | Zaid Sayyed](https://zaidsayyed.in/tools/sih-problem-statements/sih26097?utm_source=chatgpt.com)
- [Ministry of Social Justice and Empowerment (MoSJE) Problem Statements (8 PS) — SIH 2026 | SIH ONE | SIH ONE](https://sihone.pages.dev/organization/ministry-of-social-justice-and-empowerment-mosje?utm_source=chatgpt.com)
- [Smart Education Problem Statements (13 PS) — SIH 2026 | SIH ONE | SIH ONE](https://sihone.pages.dev/theme/smart-education?utm_source=chatgpt.com)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/3198?utm_source=chatgpt.com)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/2277?utm_source=chatgpt.com)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/4116?utm_source=chatgpt.com)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/11071?utm_source=chatgpt.com)
- [National Qualification Register](https://nqr.gov.in/qualifications/3223?utm_source=chatgpt.com)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/12127?utm_source=chatgpt.com)
- [National Qualification Register](https://nqr.gov.in/qualifications/11072?utm_source=chatgpt.com)
- [National Qualification Register](https://nqr.gov.in/qualifications/14250?utm_source=chatgpt.com)
- [National Qualification Register](https://www.nqr.gov.in/qualifications/2671?utm_source=chatgpt.com)
- [SIH-2026-/ps_2026/README.md at main · jeevansai-hub/SIH-2026- · GitHub](https://github.com/jeevansai-hub/SIH-2026-/blob/main/ps_2026/README.md?utm_source=chatgpt.com)
- [Sign In | PM-AJAY](https://pm-ajay.dosje.gov.in/?utm_source=chatgpt.com)
- [SIH Navigator | Smart India Hackathon Prep Platform](https://sih-gitam.vercel.app/?utm_source=chatgpt.com)
- [Press Release Page | Press Information Bureau](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2298226&lang=1&reg=1&utm_source=chatgpt.com)
- [Find PS For Your Team | SIH 2026 Explorer](https://sih-explorer.amanuniyal47.workers.dev/explore?utm_source=chatgpt.com)
- [SMART INDIA](https://www.sih.gov.in/letters/Guidelines-College-SPOC.pdf?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC030?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NCS007?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC028?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC025?utm_source=chatgpt.com)
- [Smart India Hackathon 2024 - Senior Edition Finale](https://finale.sih.gov.in/event/NC049?utm_source=chatgpt.com)
- [Smart India Hackathon | Junior Edition](https://junior.sih.gov.in/?utm_source=chatgpt.com)
- [Managing usage with GPT-6 Astra in Work and Codex | OpenAI Help Center](https://help.openai.com/bs-ba/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex?utm_source=chatgpt.com)
- [Reasoning Effort Tuning: Minimal to xhigh for Cost and Speed | Codex Knowledge Base](https://codex.danielvaughan.com/2026/03/27/reasoning-effort-tuning/?utm_source=chatgpt.com)
- [`VALID_REASONING_EFFORTS` rejects `max` and `ultra` locally, so the flagship model's top two reasoning tiers are unreachable from the plugin · Issue #751 · openai/codex-plugin-cc · GitHub](https://github.com/openai/codex-plugin-cc/issues/751?utm_source=chatgpt.com)
- [codex-dev-skills/docs/main-agent-and-subagent-settings.md at main · jeffery777/codex-dev-skills · GitHub](https://github.com/jeffery777/codex-dev-skills/blob/main/docs/main-agent-and-subagent-settings.md?utm_source=chatgpt.com)
- [Codex limits spark frustration among subscribers - #76 by Joao_Martins - Codex - OpenAI Developer Community](https://community.openai.com/t/codex-limits-spark-frustration-among-subscribers/1390408/76?utm_source=chatgpt.com)
- [I just want a guideline. GPT-5.6 Sol/Terra/Luna Comparison | Estimating Credit Consumption by Codex Reasoning Level｜おとっこ](https://note.com/otokko/n/n0444d81f0ca0?hl=en&utm_source=chatgpt.com)
- [Model Selection in Codex CLI: Current Models and When to Use Each | Codex Knowledge Base](https://codex.danielvaughan.com/2026/03/26/codex-cli-model-selection/?utm_source=chatgpt.com)
- [ReasoningEffort](https://javadoc.io/static/com.openai/openai-java/4.23.0/com/openai/models/ReasoningEffort.html?utm_source=chatgpt.com)
- [Full Code of skills-directory/skill-codex for AI - Complete Repository Source | GitExtract](https://gitextract.com/skills-directory/skill-codex?utm_source=chatgpt.com)
- [model_reasoning_effort — Codex config — Codex Insider](https://www.codexinsider.com/config/model-reasoning-effort/?utm_source=chatgpt.com)
- [Models And Reasoning — Codex SDK v0.19.0](https://codex-sdk.hexdocs.pm/07-models-and-reasoning.html?utm_source=chatgpt.com)
- [Managing Context | Arantic Documentation](https://docs.arantic.com/codex/context?utm_source=chatgpt.com)
- [skills/README.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/README.md?utm_source=chatgpt.com)
- [skills/skills/engineering/README.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/skills/engineering/README.md?utm_source=chatgpt.com)
- [GitHub - mattpocock/skills: Skills for Real Engineers. Straight from my .agents directory. · GitHub](https://github.com/mattpocock/skills?utm_source=chatgpt.com)
- [skills/docs/engineering/setup-matt-pocock-skills.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/docs/engineering/setup-matt-pocock-skills.md?utm_source=chatgpt.com)
- [skills/docs/engineering/domain-modeling.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/docs/engineering/domain-modeling.md?utm_source=chatgpt.com)
- [skills/skills/engineering/to-spec/SKILL.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/skills/engineering/to-spec/SKILL.md?utm_source=chatgpt.com)
- [skills/docs/engineering/improve-codebase-architecture.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/docs/engineering/improve-codebase-architecture.md?utm_source=chatgpt.com)
- [skills/ARCHITECTURE.md at main · chann/skills · GitHub](https://github.com/chann/skills/blob/main/ARCHITECTURE.md?utm_source=chatgpt.com)
- [skills/skills/in-progress/README.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/skills/in-progress/README.md?utm_source=chatgpt.com)
- [skills/agent-skill-best-practices.md at main · nyosegawa/skills · GitHub](https://github.com/nyosegawa/skills/blob/main/agent-skill-best-practices.md?utm_source=chatgpt.com)
- [skills/docs/productivity/writing-great-skills.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/docs/productivity/writing-great-skills.md?utm_source=chatgpt.com)
- [skills/skills/engineering/setup-matt-pocock-skills/SKILL.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/skills/engineering/setup-matt-pocock-skills/SKILL.md?utm_source=chatgpt.com)
- [skills/docs/engineering/ask-matt.md at main · mattpocock/skills · GitHub](https://github.com/mattpocock/skills/blob/main/docs/engineering/ask-matt.md?utm_source=chatgpt.com)
- [GitHub - chriscox/agent-skills: Reusable skills for AI coding agents — Claude Code, Codex, Gemini CLI, and OpenClaw · GitHub](https://github.com/chriscox/agent-skills?utm_source=chatgpt.com)
- [GitHub - shane9coy/Agent-Skill-Architecture-Guide: A comprehensive reference for building and organizing AI agent skills across Claude Code, KiloCode, OpenClaw, and OpenAI Codex. Covers SKILL.md specifications, folder structures, mode-scoped skills, agent orchestration, and self-hosted model configuration. · GitHub](https://github.com/shane9coy/Agent-Skill-Architecture-Guide?utm_source=chatgpt.com)
- [skills/README.md at main · robjsliwa/skills · GitHub](https://github.com/robjsliwa/skills/blob/main/README.md?utm_source=chatgpt.com)
- [codex-skills/CLAUDE.md at main · am-will/codex-skills · GitHub](https://github.com/am-will/codex-skills/blob/main/CLAUDE.md?utm_source=chatgpt.com)
- [claude-skills/docs/guides/agent-skills-for-codex.md at main · alirezarezvani/claude-skills · GitHub](https://github.com/alirezarezvani/claude-skills/blob/main/docs/guides/agent-skills-for-codex.md?utm_source=chatgpt.com)
- [claude-skills/README.md at main · OneWave-AI/claude-skills · GitHub](https://github.com/OneWave-AI/claude-skills/blob/main/README.md?utm_source=chatgpt.com)
- [agent-skills-claude/docs/comparison.md at main · demystify-systems/agent-skills-claude · GitHub](https://github.com/demystify-systems/agent-skills-claude/blob/main/docs/comparison.md?utm_source=chatgpt.com)
- [skills/README.md at main · sean2077/skills · GitHub](https://github.com/sean2077/skills/blob/main/README.md?utm_source=chatgpt.com)
- [GitHub - snepraj2709/system-design-first-principles-skill · GitHub](https://github.com/snepraj2709/system-design-first-principles-skill?utm_source=chatgpt.com)
- [skills/ARCHITECTURE.md at main · b1tank/skills · GitHub](https://github.com/b1tank/skills/blob/main/ARCHITECTURE.md?utm_source=chatgpt.com)
- [GitHub - britt/agent-skills: Some skills for Claude and his buddies · GitHub](https://github.com/britt/agent-skills?utm_source=chatgpt.com)
