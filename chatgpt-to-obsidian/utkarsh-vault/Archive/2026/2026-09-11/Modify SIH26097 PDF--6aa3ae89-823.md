---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6aa3ae89-8230-83ee-944b-49974d284f05"
created: 1789111946.163452
updated: 1789126629.462751
resource_section: true
---

# Modify SIH26097 PDF

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

## Resources

### Local attachments
- [HERFIT NOVELTY.pdf](../../../Raw/Export/file_0000000074d8820685105806e9ff2f2d.dat)

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
