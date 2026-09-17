---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a8c386d-9e68-83e8-856b-1304160734a4"
created: 1787574398.110555
updated: 1787578834.835551
resource_section: true
---

# Find AI Projects

## User

@TinyFish Use tinyfish search and fetch to find newly released or rapidly growing AI developer projects this week, fetch their documentation and READMEs, and explain what each is useful for.

## Assistant

Worked for 3m 13s

## Assistant

I searched specifically for **AI developer projects that are either newly appearing or showing unusually strong growth during the week of Aug 17–24, 2026**, then fetched their GitHub READMEs/documentation where I could identify the repository.

One caveat: GitHub's own trending data is not directly exposed cleanly through search, so I treated **recent star growth + current activity + developer relevance** as the signal rather than claiming an exact ranking.

### 1. Superpowers — `obra/superpowers`

urlobra/superpowers on GitHubhttps://github.com/obra/superpowers

**What it is:** 
An **agentic software-development methodology** that gives coding agents a structured set of reusable skills instead of letting the agent immediately start writing code. Its README describes it as a complete development methodology built from composable skills. fileciteturn8file0L1-L1

**Why it is interesting:**

- Works with multiple coding agents, including Claude Code, Codex, Copilot, Gemini, Pi and others. fileciteturn7file1L11-L14
- Provides skills for activities such as:
 - requirements clarification
 - planning
 - implementation
 - debugging
 - code review
 - testing
- The agent is encouraged to **understand the task before coding**, rather than simply generating code immediately. fileciteturn8file0L1-L1
- It has reached roughly **277k GitHub stars** and 24.8k forks in the fetched repository state. fileciteturn8file0L1-L1

**Useful for you:** 
This is particularly relevant if you're using **Claude Code/Codex-style agents to build large projects**. Instead of repeatedly telling an agent *"first analyze the architecture, then implement..."*, Superpowers turns that methodology into reusable agent skills.

**The important idea:** 
> Don't make the LLM smarter; make the **development process around the LLM** better.

---

### 2. Waku Agent — `ShenSeanChen/waku-agent`

urlShenSeanChen/waku-agent on GitHubhttps://github.com/ShenSeanChen/waku-agent

This one is considerably smaller but **architecturally very interesting**.

The README describes Waku as a **local-first personal AI assistant** designed so that the codebase is small enough to understand in an afternoon. It explicitly focuses on four components:

**Harness → Loop → Memory → Eval/LLM-Ops**. fileciteturn8file1L15-L15

Current fetched state:

- ~**1.5k stars**
- 283 forks
- 308 commits fileciteturn8file1L15-L15

The project emphasizes:

- **Local-first execution**
- Persistent memory stored in **SQLite**
- Agent loop
- Evaluation
- LLM operations
- Minimal framework abstraction fileciteturn8file1L15-L15

**What it is useful for:**

You could use its architecture as a reference for building your own:

```text
User
 ↓
Agent Harness
 ↓
Reasoning / Tool Loop
 ↓
Tools
 ↓
Memory
 ↓
Evaluation
```

This is especially relevant to your **EchoQuery / agent-oriented projects**, because it demonstrates the principle of keeping the agent architecture explicit instead of hiding everything behind a large framework.

There is also a dedicated document explaining **loop vs. graph architectures**, which is useful when deciding whether your agent needs a workflow graph or simply an iterative tool loop. fileciteturn4file3L27-L31

---

### 3. AI Agent Skills — `Aradotso/ai-agent-skills`

urlAradotso/ai-agent-skills on GitHubhttps://github.com/Aradotso/ai-agent-skills

This project is particularly interesting because it is almost a **meta-tool for discovering AI-agent capabilities**.

Its repository describes a bot that:

> scans GitHub every 30 minutes for trending repositories in the AI-agent niche, ranks them by stars/day, and generates an installable `SKILL.md` for the top new project. fileciteturn4file7L59-L63

So the project is essentially:

```text
GitHub
 ↓
Find trending AI-agent repos
 ↓
Rank by growth
 ↓
Analyze repository
 ↓
Generate SKILL.md
 ↓
Make capability installable by an agent
```

The fetched repository currently contains skills covering things such as:

- Agent Skills specification
- Open multi-agent orchestration
- Agent-browser
- Persistent agent memory
- Agentic AI research
- Coding-agent architecture
- Internet access for agents fileciteturn8file2L25-L35

**What it is useful for:**

Instead of manually discovering:

> "What new AI-agent tool appeared this week?"

you could have an automated pipeline continually discovering new projects and converting them into **agent-consumable skills**.

That is a surprisingly powerful concept for an AI developer workflow.

---

## What I think is actually worth paying attention to

The three projects represent **three different directions** emerging in AI development:

| Project | Core idea | Useful when |
|---|---|---|
| **Superpowers** | Give coding agents a development methodology | You want agents to build software more reliably |
| **Waku Agent** | Keep the agent architecture tiny, explicit and local | You want to understand/build your own agent |
| **AI Agent Skills** | Automatically discover and package new agent capabilities | You want agents that continuously gain new capabilities |

### The bigger trend

The interesting thing isn't another "AI coding assistant."

The emerging layer is:

**LLM → Agent → Skills → Harness → Evaluation → Continuous capability discovery**

Superpowers focuses on **skills/workflow**. 
Waku focuses on the **agent harness + memory + evaluation**. 
AI Agent Skills focuses on **discovering and distributing those capabilities**.

That's much closer to where I would look for **new project ideas worth building in 2026** than another generic RAG chatbot.

One particularly interesting signal is that a recent AI-agent trend report identified **Waku Agent at ~1,458 stars with +261 stars in a week**, indicating unusually rapid growth for such a small project. fileciteturn3file3L29-L33

And the broader developer ecosystem is clearly moving toward agent infrastructure: current discussions are increasingly centered on **coding-agent harnesses, skills, MCP, evaluation, memory and agent workflows**, rather than merely model APIs. fileciteturn2file3L27-L33

**If your goal is to find projects you could actually learn from or build on, I'd prioritize them:**

**1. Waku Agent → study the architecture** 
**2. Superpowers → study the skills/harness methodology** 
**3. AI Agent Skills → study automated capability discovery**

These three are much more technically interesting than simply chasing another newly released AI wrapper.

## Resources

No structured attachments or external references were present in this conversation.
