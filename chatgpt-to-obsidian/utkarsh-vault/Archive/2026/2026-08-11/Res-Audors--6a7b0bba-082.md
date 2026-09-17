---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a7b0bba-0828-83e8-9104-df626cfecf49"
created: 1786448881.301376
updated: 1786451035.956155
resource_section: true
---

# Res-Audors

## User

**craft resume for this role using Latex and add my project Audora also in projects section.**

**The Role**

We're hiring Tech Interns to build real, shipped features, not tickets picked off a backlog. You'll work across the stack as needed, sometimes backend, sometimes frontend, sometimes just wiring up an AI feature end to end. What matters more than which layer you're comfortable in is whether you can take a problem and actually ship a working solution.

This is a 6-month commitment aimed at 2026/27 grads. If it goes well, there's a real shot at converting to full-time. If you want to spend your first stretch out of college building things that actually get used in production, not shadowing someone else's codebase, keep reading.

You'll work closely with the product and engineering team, sitting in on discussions about what's broken and why, and turning that into code. AI-first, prototype-first, figure-it-out-yourself is how we work here, and that applies to how you build too.

**What You'll Do**

- Build and ship features across the stack, whatever the problem needs, backend logic, frontend UI, or both
- Write clean, working code and get comfortable shipping fast, then iterating based on real usage
- Debug and fix issues in the live product, not just in a sandboxed environment
- Work with AI/LLM APIs where relevant, our product runs on AI, so you'll likely touch this even if it's not your main focus
- Write basic technical documentation for what you build, so the team can maintain it after you
- Sit in on product and client conversations to understand what you're actually building for

**What We're Looking For:**

-
 **Solid programming fundamentals.** Comfortable in at least one language (Python, JavaScript, Java, whatever), and can pick up new stacks fast when needed
- **A builder's instinct.** You've built things outside class, projects, hackathon entries, personal tools, because you wanted them to exist, not because someone assigned it
- **Comfortable with ambiguity.** You don't need a fully scoped ticket to start, you can take a rough problem and figure out a path to a solution
- **High agency.** You debug your own blockers before asking for help, and you don't wait around for permission to try something
- **Clear communicator.** You can explain what you built and why, in a standup, a doc, or a quick Slack message
- **Curious about AI.** Not required to be an expert, but genuinely interested in how AI/LLMs fit into product, since it's core to what we're building

## Assistant

Worked for 18s

## Assistant

Absolutely. For this role, I’d position you as a **builder/full-stack + AI-oriented engineering student**, rather than as a pure Data Science candidate. The resume should emphasize **shipping products, debugging, backend/frontend work, AI integrations, Docker, and ownership**.

I’ve also added **Audora** as the strongest project because it demonstrates exactly what this role asks for: taking a rough problem, designing the architecture, integrating multiple systems, packaging it, and shipping releases.

Below is a **ATS-friendly one-page LaTeX resume** tailored to this role.

```latex
\documentclass\[10pt,a4paper\]{article}

% ---------- Packages ----------
\usepackage\[
 top=0.45in,
 bottom=0.45in,
 left=0.55in,
 right=0.55in
\]{geometry}

\usepackage{enumitem}
\usepackage{titlesec}
\usepackage\[hidelinks\]{hyperref}
\usepackage{tabularx}
\usepackage{xcolor}
\usepackage{fontawesome5}
\usepackage\[T1\]{fontenc}
\usepackage{lmodern}

% ---------- Formatting ----------
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}

\titleformat{\section}
 {\large\bfseries}
 {}
 {0em}
 {}
 \[\titlerule\]

\titlespacing{\section}{0pt}{6pt}{3pt}

\setlist\[itemize\]{
 leftmargin=1.25em,
 itemsep=1pt,
 topsep=1pt,
 parsep=0pt,
 partopsep=0pt
}

\newcommand{\resumeItem}\[1\]{
 \item \small #1
}

\newcommand{\projectHeading}\[2\]{
 \textbf{#1} \hfill \textit{#2}
}

% ---------- Document ----------
\begin{document}

% ---------- Header ----------
\begin{center}
 {\LARGE \textbf{Utkarsh Wadalkar}} \\\[3pt\]
 \small
 Pune, Maharashtra, India
 \,|\, 
 \href{mailto:YOUR_EMAIL}{YOUR_EMAIL}
 \,|\, 
 +91-XXXXXXXXXX
 \\\[2pt\]
 \href{https://github.com/utkarsh-wadalkar}{\faGithub\ github.com/utkarsh-wadalkar}
 \,|\, 
 \href{https://www.linkedin.com/in/utkarsh-wadalkar}{\faLinkedin\ linkedin.com/in/utkarsh-wadalkar}
\end{center}

% ---------- Summary ----------
\section{SUMMARY}

\small
Engineering student focused on building and shipping practical software products across the
\textbf{frontend, backend, cloud, and AI stack}. Experienced with \textbf{Python, JavaScript,
React, Node.js, FastAPI, Docker, AWS, and AI/LLM APIs}, with hands-on experience debugging
production-like systems, integrating services, and turning ambiguous problems into working
features. Strong builder mindset with a focus on rapid prototyping, iteration, and end-to-end
ownership.

% ---------- Education ----------
\section{EDUCATION}

\textbf{Bachelor of Engineering in Artificial Intelligence and Data Science}
\hfill \textit{2023 -- 2027} \\
\small
\textit{\[College Name\], Pune, Maharashtra}

% ---------- Technical Skills ----------
\section{TECHNICAL SKILLS}

\small
\textbf{Languages:} Python, JavaScript, C++, SQL \\

\textbf{Frontend:} React.js, Next.js, HTML, CSS, Tailwind CSS \\

\textbf{Backend:} Node.js, Express.js, FastAPI, REST APIs \\

\textbf{AI / ML:} LLM APIs, AI Application Development, RAG, Prompt Engineering,
Python, Pandas, NumPy, Scikit-learn \\

\textbf{Cloud / DevOps:} AWS, EC2, Docker, Docker Desktop, WSL2, Git, GitHub,
CI/CD fundamentals \\

\textbf{Databases / Tools:} MySQL, MongoDB, Firebase, Firestore, Power BI,
Tableau, Figma

% ---------- Projects ----------
\section{PROJECTS}

\projectHeading{Audora -- Desktop Apple Music Downloader}{Electron, React, FastAPI, Docker, Python}
\begin{itemize}
 \resumeItem{Built and shipped a cross-platform-style desktop application using
 \textbf{Electron + React} with a \textbf{FastAPI} backend for managing Apple Music downloads.}

 \resumeItem{Designed an end-to-end architecture connecting the desktop UI, backend services,
 Docker Manager, Docker Desktop, authentication wrapper, and the downloader container.}

 \resumeItem{Implemented a \textbf{setup wizard, download queue, history management, WebSocket-based
 live logs, diagnostics, offline detection, and container lifecycle management}.}

 \resumeItem{Built robust Docker integration with container reuse and runtime health checks,
 reducing setup friction and improving reliability during repeated application launches.}

 \resumeItem{Packaged the Python backend using \textbf{PyInstaller} and maintained iterative releases
 including setup-wizard fixes, live terminal improvements, offline handling, and UI redesigns.}

 \resumeItem{Took ownership of debugging issues across the frontend, backend, Docker environment,
 networking, packaging, and deployment rather than limiting development to a single layer.}
\end{itemize}

\projectHeading{AI Interview Question Generator}{Node.js, Express.js, OpenRouter, MySQL}
\begin{itemize}
 \resumeItem{Developing an AI-powered backend that generates technically relevant interview questions
 from structured user inputs using \textbf{LLM APIs}.}

 \resumeItem{Implemented prompt construction and structured JSON parsing to ensure AI-generated
 responses conform to application requirements.}

 \resumeItem{Built REST API endpoints using \textbf{Node.js and Express.js}, with centralized
 error handling, environment configuration, and database integration.}

 \resumeItem{Debugged API, SQL, timezone, environment-variable, and integration issues while
 iterating on the application backend.}
\end{itemize}

\projectHeading{Fake News Detection}{Python, Pandas, Scikit-learn, Matplotlib}
\begin{itemize}
 \resumeItem{Built a machine learning pipeline to classify news articles as real or fake using
 a publicly available Kaggle dataset.}

 \resumeItem{Performed data preprocessing, feature preparation, model training, and evaluation
 using Python and Scikit-learn.}
\end{itemize}

% ---------- Experience ----------
\section{EXPERIENCE}

\textbf{Software / AI Engineering Intern}
\hfill \textit{\[Company Name\] --- \[Dates\]} \\

\begin{itemize}
 \resumeItem{Built and maintained application features across the frontend and backend,
 working with JavaScript, React, Node.js, APIs, and databases.}

 \resumeItem{Integrated third-party services and AI APIs into application workflows and
 debugged issues across multiple layers of the stack.}

 \resumeItem{Collaborated through Git-based development workflows, debugging, code changes,
 and iterative feature delivery.}
\end{itemize}

% ---------- Certifications ----------
\section{CERTIFICATIONS}

\small
\textbf{Data Structures and Algorithms with C++} \\
\textbf{Data Science with Python} \\
\textbf{MySQL Bootcamp}

% ---------- Additional ----------
\section{ADDITIONAL}

\small
\textbf{Interests:} AI/LLM Applications, Full-Stack Engineering, Developer Tools,
Cloud Computing, Product Engineering

\end{document}
```

### Why this version fits the role

The important shift is that I **didn't make the resume primarily about AI/ML theory**. This job description repeatedly emphasizes:

- **Ship working features**
- **Frontend + backend**
- **AI/LLM APIs**
- **Debug production issues**
- **Ambiguous problems**
- **Builder mindset**
- **High agency**
- **Technical communication**

So Audora is deliberately the first project. Its architecture gives you strong evidence for almost every requirement:

> **Electron → React → FastAPI → Docker Manager → Docker Desktop → wrapper → downloader**

That is much more compelling for this role than simply saying you trained an ML model.

**One important thing:** replace the `YOUR_EMAIL`, phone number, `\[College Name\]`, and `\[Company Name\]` placeholders before submitting. Also, if you give me your **current resume PDF/text**, I can merge the exact education, internship, achievements, dates, and metrics into this version without inventing anything.

## User

give Aideo project also, dont rewrite entirely, just give this one

## Assistant

Add this under your **Projects** section:

:::writing{variant="document" id="58321"}
\textbf{AIdeo -- AI Video Generation SaaS} \hfill \textit{React, Next.js, Node.js, Express.js, Firebase, n8n}

\begin{itemize}
 \resumeItem{Built an AI-powered video generation SaaS that automates video creation through an end-to-end workflow integrating \textbf{React, Next.js, Node.js, Firebase, and n8n}.}

 \resumeItem{Developed frontend interfaces and backend REST APIs for managing user requests, AI generation workflows, and application data.}

 \resumeItem{Integrated \textbf{AI APIs and n8n automation workflows} to orchestrate multi-step video generation processes and connect external services.}

 \resumeItem{Implemented Firebase Authentication and Firestore for user management and persistent application data, while debugging API, environment, and integration issues across the stack.}

 \resumeItem{Designed the application with a product-focused approach, iterating on features and integrations to turn an AI prototype into a usable SaaS product.}
\end{itemize}
:::

## User

As u can see it became 2 page resume and i want inly 1 page, so short decription in every project, such that recruiter gets hint of what i did but he gets intrigued to ask me questions about my own projects. Dont overexplain or overwhelm recuiter with block of text which he is going to ignore, keep in sleek but intriguing 

\section{PROJECTS}

\projectHeading{Audora -- Desktop Apple Music Downloader}{Electron, React, FastAPI, Docker, Python}
\begin{itemize}
\resumeItem{Built and shipped a cross-platform-style desktop application using
\textbf{Electron + React} with a \textbf{FastAPI} backend for managing Apple Music downloads.}

```
\resumeItem{Designed an end-to-end architecture connecting the desktop UI, backend services,
Docker Manager, Docker Desktop, authentication wrapper, and the downloader container.}

\resumeItem{Implemented a \textbf{setup wizard, download queue, history management, WebSocket-based
live logs, diagnostics, offline detection, and container lifecycle management}.}

\resumeItem{Built robust Docker integration with container reuse and runtime health checks,
reducing setup friction and improving reliability during repeated application launches.}

\resumeItem{Packaged the Python backend using \textbf{PyInstaller} and maintained iterative releases
including setup-wizard fixes, live terminal improvements, offline handling, and UI redesigns.}

\resumeItem{Took ownership of debugging issues across the frontend, backend, Docker environment,
networking, packaging, and deployment rather than limiting development to a single layer.}
```

\end{itemize}

\projectHeading{AI Interview Question Generator}{Node.js, Express.js, OpenRouter, MySQL}
\begin{itemize}
\resumeItem{Developing an AI-powered backend that generates technically relevant interview questions
from structured user inputs using \textbf{LLM APIs}.}

```
\resumeItem{Implemented prompt construction and structured JSON parsing to ensure AI-generated
responses conform to application requirements.}

\resumeItem{Built REST API endpoints using \textbf{Node.js and Express.js}, with centralized
error handling, environment configuration, and database integration.}

\resumeItem{Debugged API, SQL, timezone, environment-variable, and integration issues while
iterating on the application backend.}
```

\end{itemize}

\textbf{AIdeo -- AI Video Generation SaaS} \hfill \textit{React, Next.js, Node.js, Express.js, Firebase, n8n}

\begin{itemize}
\resumeItem{Built an AI-powered video generation SaaS that automates video creation through an end-to-end workflow integrating \textbf{React, Next.js, Node.js, Firebase, and n8n}.}

```
\resumeItem{Developed frontend interfaces and backend REST APIs for managing user requests, AI generation workflows, and application data.}

\resumeItem{Integrated \textbf{AI APIs and n8n automation workflows} to orchestrate multi-step video generation processes and connect external services.}

\resumeItem{Implemented Firebase Authentication and Firestore for user management and persistent application data, while debugging API, environment, and integration issues across the stack.}

\resumeItem{Designed the application with a product-focused approach, iterating on features and integrations to turn an AI prototype into a usable SaaS product.}
```

\end{itemize}

\projectHeading{Fake News Detection}{Python, Pandas, Scikit-learn, Matplotlib}
\begin{itemize}
\resumeItem{Built a machine learning pipeline to classify news articles as real or fake using
a publicly available Kaggle dataset.}

```
\resumeItem{Performed data preprocessing, feature preparation, model training, and evaluation
using Python and Scikit-learn.}
```

\end{itemize}

## Assistant

Yes — your instinct is correct. **For this role, the projects section should create curiosity, not explain the entire architecture.** The recruiter should understand *what you built + what makes it technically interesting* in 5–10 seconds.

I would reduce it to **2 bullets for the major projects and 1 bullet for Fake News Detection**. This should save substantial vertical space.

Replace your entire `PROJECTS` section with this:

```latex
\section{PROJECTS}

\projectHeading{Audora -- Desktop Apple Music Downloader}{Electron, React, FastAPI, Docker, Python}
\begin{itemize}
 \resumeItem{Built and shipped a desktop application with \textbf{Electron + React + FastAPI}, integrating Docker to manage the complete download workflow.}
 \resumeItem{Engineered a custom \textbf{Docker lifecycle, setup wizard, live logs, diagnostics, and container health checks}, handling issues across the full stack.}
\end{itemize}

\projectHeading{AI Interview Question Generator}{Node.js, Express.js, OpenRouter, MySQL}
\begin{itemize}
 \resumeItem{Built an AI-powered backend that generates structured technical interview questions using \textbf{LLM APIs, Node.js, and Express.js}.}
 \resumeItem{Implemented \textbf{prompt engineering, structured JSON parsing, REST APIs, and centralized error handling} for reliable AI responses.}
\end{itemize}

\projectHeading{AIdeo -- AI Video Generation SaaS}{React, Next.js, Node.js, Express.js, Firebase, n8n}
\begin{itemize}
 \resumeItem{Built an AI video-generation SaaS connecting \textbf{AI APIs, React/Next.js, Node.js, Firebase, and n8n} into an end-to-end workflow.}
 \resumeItem{Designed the product around automated multi-step AI workflows, external service integrations, and persistent user data.}
\end{itemize}

\projectHeading{Fake News Detection}{Python, Pandas, Scikit-learn}
\begin{itemize}
 \resumeItem{Built a machine learning pipeline to classify news articles using \textbf{Python and Scikit-learn}, covering preprocessing, model training, and evaluation.}
\end{itemize}
```

### Why I prefer this version

The **Audora** bullets deliberately leave some unanswered questions:

> *"custom Docker lifecycle"* 
> *"setup wizard"* 
> *"live logs"* 
> *"container health checks"*

A technical interviewer can naturally ask:

- Why did you use Docker?
- How does your Docker lifecycle manager work?
- How do you detect container health?
- How are live logs streamed to Electron?
- Why FastAPI instead of Node?
- How did you package the Python backend?
- What was the hardest bug you encountered?

That's exactly the **intrigue** you want.

For **AI Interview Question Generator**, the interesting hooks are:

> *structured JSON parsing + LLM APIs + prompt engineering*

Rather than explaining the implementation, you're giving them reasons to ask **how you made unreliable LLM output usable by a backend**.

And for **AIdeo**, the phrase:

> *"automated multi-step AI workflows"*

is much stronger than listing every feature. It invites questions about your n8n architecture, API orchestration, Firebase, and AI generation pipeline.

### One more change I'd make

Since you're targeting this **Tech Intern** role specifically, I'd order them:

**1. Audora** → strongest engineering/project ownership signal 
**2. AIdeo** → strongest AI/product signal 
**3. AI Interview Question Generator** → strongest LLM/backend signal 
**4. Fake News Detection** → supporting ML project

So I'd actually use:

```text
Audora
AIdeo
AI Interview Question Generator
Fake News Detection
```

That ordering tells the recruiter in ~10 seconds:

**"This person builds products → works across the stack → works with AI → has ML fundamentals."**

That's a much better narrative for this particular job than giving every project equal space.

## User

use this instead of fake news 

# Sales-Forecasting-using-Machine-Learning

Developed an end-to-end sales prediction pipeline to forecast Item\_Outlet\_Sales for a retail dataset. Performed extensive data cleaning (handling missing values with mean/mode imputation, replacing zero values, consolidating categorical entries), feature engineering (creating New\_Item\_Type, Outlet\_Years, and encoding categorical features), and exploratory data analysis (distribution plots, count plots, and correlation heatmaps) to identify trends and relationships.

Implemented multiple regression algorithms — Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, Extra Trees, LightGBM, and XGBoost — and evaluated them using cross-validation, MSE, and R² scores. Conducted hyperparameter tuning via RandomizedSearchCV to optimize Random Forest, LightGBM, and XGBoost models. Visualized feature importances and residual distributions to assess model performance.

## Assistant

Yes. For the resume, I would **not use the full description** because it will bring back the same space problem. Compress it while retaining the technically interesting parts.

Replace the Fake News project with:

```latex
\projectHeading{Sales Forecasting using Machine Learning}{Python, Pandas, Scikit-learn, XGBoost, LightGBM}
\begin{itemize}
 \resumeItem{Built an end-to-end sales forecasting pipeline with \textbf{data cleaning, feature engineering, EDA, and categorical encoding} to predict retail outlet sales.}
 \resumeItem{Compared \textbf{8 regression models} and used cross-validation, RandomizedSearchCV, and feature-importance analysis to optimize and evaluate the best-performing models.}
\end{itemize}
```

This is much better than Fake News Detection for your current resume because it gives an interviewer several natural technical hooks:

- Why did you choose those regression models?
- Why XGBoost/LightGBM?
- How did you handle missing and zero values?
- What features did you engineer?
- Why RandomizedSearchCV?
- Which model performed best and why?
- How did you evaluate the models?

So your final **Projects** ordering should be:

1. **Audora** — strongest builder/full-stack signal
2. **AIdeo** — AI + SaaS/product signal
3. **AI Interview Question Generator** — LLM + backend signal
4. **Sales Forecasting** — ML fundamentals signal

That gives the recruiter a very clean progression: **Build → AI Product → LLM Backend → ML fundamentals.**

## User

give names of them

## Assistant

If you mean the **external services/APIs used in AIdeo**, based on your project, you can name them explicitly instead of saying “external service integrations.”

For example:

```latex
\resumeItem{Built an AI video-generation SaaS connecting \textbf{Kie.ai, Google Gemini, Firebase, and n8n} with React/Next.js and Node.js into an end-to-end workflow.}
```

And if you want to keep it slightly broader:

```latex
\resumeItem{Built an AI video-generation SaaS integrating \textbf{Kie.ai, Google Gemini, Firebase, and n8n} across the frontend, backend, and automated AI workflows.}
```

**I prefer the second one** for your resume—it gives the recruiter concrete technologies they can ask you about.

## User

add this in experience section and give me new section

## Assistant

Worked for a couple of seconds

## Assistant

Yes. Since this is a **30-hour Power BI Training Program conducted by Rubicon Skill Development**, I would include it in **Experience** as a training/industry exposure entry rather than presenting it as a formal internship.

Replace your current `EXPERIENCE` section with:

```latex
\section{EXPERIENCE}

\textbf{Power BI Trainee -- Rubicon Skill Development Pvt. Ltd.}
\hfill \textit{Dec 2025} \\

\begin{itemize}
 \resumeItem{Completed a \textbf{30-hour practical training program} focused on data analysis, visualization, and dashboard development using \textbf{Microsoft Power BI}.}
 
 \resumeItem{Worked with data transformation, interactive visualizations, and dashboard development to translate datasets into actionable insights.}
\end{itemize}
```

### If you want it even more resume-efficient

Since you're trying to keep everything to **one page**, I actually recommend this shorter version:

```latex
\section{EXPERIENCE}

\textbf{Power BI Trainee -- Rubicon Skill Development Pvt. Ltd.}
\hfill \textit{Dec 2025} \\

\begin{itemize}
 \resumeItem{Completed \textbf{30 hours of practical Power BI training} covering data analysis, visualization, data transformation, and interactive dashboard development.}
\end{itemize}
```

**I recommend the second version** for your resume. It is factual, compact, and doesn't consume valuable space that should go toward your projects and technical skills.

## Resources

### Local attachments
- [5ef3d90d-1b74-403c-b10d-da249935c863.png](../../../Raw/Export/file_00000000b8a882089c3cad6713b3093c.dat)
- [image(20260811-122323).png](../../../Raw/Export/file_0000000089c082119ccc71f447c9da5e.dat)

### External references
- [ATS-Friendly LaTeX Resume](https://chatgpt.com/c/6a4cf3ea-f630-83e8-a470-d4966e71ebd8)
- [SQL Dump Import Issue](https://chatgpt.com/c/6a75f201-083c-83e8-b57d-20145b792d41)
- [Apple Music ALAC Setup](https://chatgpt.com/c/6a4bdcbf-8ca0-83ee-9e01-f7d961f07879)
- [ai-interview-Qs](https://chatgpt.com/c/6a747601-01b4-83e8-a684-0477c0bcf5ea)
- [Mneme Memory Ownership](https://chatgpt.com/c/6a4a8ba2-5818-83ee-b816-c1dbcac25d8d)
