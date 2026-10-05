---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6ab3c023-5bd8-83ee-9a9c-e9f9302cfcd6"
created: 1790165027.935279
updated: 1790177840.817781
resource_section: true
---

# List Mattpocock Skills

## User

list all mattpocock skills

## Assistant

Worked for 5s

## Assistant

I can currently see **38 Matt Pocock skills** exposed through the connected `mattpocock` skill repository, plus one helper for reading supporting files.

1. `ask-matt` — routes your situation to the most suitable skill/flow.
2. `claude-handoff` — hands the current conversation to a fresh background agent.
3. `code-review` — reviews changes against both repo standards and the originating spec.
4. `codebase-design` — designs/improves module boundaries, interfaces, seams, and deep modules.
5. `diagnosing-bugs` — systematic debugging for bugs and performance regressions.
6. `domain-modeling` — develops terminology, domain models, `CONTEXT.md`, and ADRs.
7. `git-guardrails-claude-code` — blocks dangerous Git commands in Claude Code.
8. `grill-me` — aggressively questions a plan/design to expose weaknesses.
9. `grill-with-docs` — does the same while producing ADRs and glossary documentation.
10. `grilling` — general-purpose stress-testing/interview flow for decisions and ideas.
11. `handoff` — creates a compact handoff document for another agent.
12. `implement` — implements work from a spec or ticket set.
13. `implement-spec` — directly implements a specification in code.
14. `improve-codebase-architecture` — scans a codebase for architectural/deep-module improvements and produces a visual report.
15. `loop-me` — repeatedly grills you to develop specifications for workspace workflows.
16. `migrate-to-shoehorn` — migrates TypeScript test assertions to `@total-typescript/shoehorn`.
17. `pr` — writes a pull-request body.
18. `prototype` — builds disposable prototypes to test architecture, state, logic, or UI ideas.
19. `research` — researches technical questions from high-trust primary sources and saves findings into the repo.
20. `resolving-merge-conflicts` — helps resolve active Git merge/rebase conflicts.
21. `retro` — conducts a retrospective on a coding session.
22. `scaffold-exercises` — creates structured course/exercise directories, problems, solutions, and explainers.
23. `setup-matt-pocock-skills` — initializes a repo for the Matt Pocock engineering workflow.
24. `setup-pre-commit` — configures Husky, lint-staged, formatting, type checking, and tests.
25. `setup-ts-deep-modules` — configures `dependency-cruiser` to enforce deep-module boundaries in TypeScript repos.
26. `tdd` — test-driven development using red → green → refactor.
27. `teach` — teaches a skill or concept in the context of the current workspace.
28. `to-questionnaire` — converts unresolved decisions into a questionnaire for another person.
29. `to-spec` — converts the existing conversation into a formal spec and publishes it to the project tracker.
30. `to-tickets` — breaks a plan/spec into tracer-bullet tickets with dependency relationships.
31. `triage` — categorizes, verifies, and prepares issues/PRs for agents.
32. `wait-what` — re-explains/re-pitches the previous response when it didn't make sense.
33. `wayfinder` — plans very large multi-session projects using decision tickets and dependencies.
34. `wizard` — generates an interactive Bash wizard for steps a human must perform, such as credentials or cloud dashboards.
35. `writing-beats` — organizes writing material into a logical sequence of conceptual beats.
36. `writing-for-agents` — writes/edits agent instructions such as `AGENTS.md`, `CLAUDE.md`, and skills.
37. `writing-fragments` — explores and collects raw writing ideas before imposing structure.
38. `writing-shape` — turns raw material into a structured article or long-form piece.

There is also a supporting utility, **`read-skill-file`**, which isn't really a workflow skill itself. It reads files referenced by a skill, such as `references/GUIDE.md` or scripts bundled with it.

For the kind of development you do, the particularly useful chain is:

`domain-modeling → grill-with-docs → to-spec → to-tickets → implement → code-review → retro`

And for a project such as **EchoQuery/KaushalVaani**, I'd add `codebase-design`, `research`, `tdd`, and `writing-for-agents` around that workflow. memcite

## User

there is other repo on which i am working, i want to aks agent to what skill should use, like u suggested for this one, i want for that one

## Assistant

Worked for 6s

## Assistant

Yes — for a different repo, **don’t reuse the EchoQuery chain blindly**. Use Matt Pocock’s `ask-matt` as the router and make the agent inspect that repository first.

Paste this **from inside the other repo**:

:::writing{variant="document" id="48217" title="Matt Pocock Skill Selection Prompt"}
Inspect this repository and understand what I am building before recommending any workflow.

Use the Matt Pocock `ask-matt` skill to determine which skills from the Matt Pocock skills repository are actually useful for this project.

First inspect:
- repository structure
- README and existing documentation
- AGENTS.md / CLAUDE.md / CONTEXT.md if present
- package/config files
- architecture and important modules
- current git state and recent work if useful
- tests and development tooling
- TODOs, issues, specs, or planning documents available in the repo

Then recommend a project-specific Matt Pocock skill workflow.

I do NOT want every available skill. Select only the skills that materially help this repository.

For each recommended skill, explain:
1. Why it is useful specifically for this repo.
2. When I should invoke it.
3. What should happen before and after it.
4. Whether it is a one-time setup skill or something I should use repeatedly.

Then give me:

**Primary workflow**
`skill → skill → skill → ...`

**Use when needed**
- `skill` — trigger/condition
- `skill` — trigger/condition

**Initial setup**
- skills I should run once at the beginning

**Avoid for now**
- skills that exist but add unnecessary complexity to this project

Pay particular attention to:
- `ask-matt`
- `domain-modeling`
- `codebase-design`
- `grill-me`
- `grill-with-docs`
- `research`
- `prototype`
- `to-spec`
- `to-tickets`
- `implement`
- `implement-spec`
- `tdd`
- `diagnosing-bugs`
- `code-review`
- `retro`
- `writing-for-agents`
- `wayfinder`

Do not assume the workflow I use for another project is appropriate here. Base the recommendation on this repository's actual architecture, maturity, scope, and current state.

I prefer architecture-first development, stable decisions, clean contracts, minimal unnecessary complexity, and avoiding repeated changes in direction.
:::

The important part is that **`ask-matt` is exactly the skill designed for this question**. It acts as the router over the other Matt Pocock skills.

For an existing repo, I’d have the agent determine something like:

`inspect repo → ask-matt → \[repo-specific planning/design skills\] → implement → code-review → retro`

rather than automatically doing:

`domain-modeling → grill-with-docs → to-spec → to-tickets → implement ...`

because, for example, a small mature app may not need `domain-modeling` or `to-tickets`, while a large architecture-heavy repo may benefit heavily from them.

If you send me **the repo URL/name**, I can also inspect that particular project and tell you which Matt Pocock skills I would use there. memcite

## User

`compileall` and `git diff --check HEAD` passed. Pytest, Ruff, and mypy could not run because those packages are absent from the active Python environment. 
how do i activate them

## Assistant

Worked for a second

## Assistant

You don’t “activate” `pytest`, `ruff`, and `mypy` individually. You activate the project’s Python virtual environment, then run them from there.

On Windows PowerShell, from the repo root, first check whether you already have a virtual environment such as `.venv`:

```powershell
Get-ChildItem -Force
```

If you see `.venv`, activate it with:

```powershell
.\.venv\Scripts\Activate.ps1
```

Your prompt should then look something like:

```text
(.venv) PS D:\path\to\repo>
```

Now check:

```powershell
python -m pytest --version
ruff --version
mypy --version
```

If the environment exists but those packages are still missing, install the project’s development dependencies. Prefer whatever the repo already defines. For example:

```powershell
pip install -r requirements.txt
```

or, if it has a dev requirements file:

```powershell
pip install -r requirements-dev.txt
```

For a `pyproject.toml` project, it may instead be:

```powershell
pip install -e ".\[dev\]"
```

If the project has no dependency definition yet, install them directly:

```powershell
python -m pip install pytest ruff mypy
```

Then run:

```powershell
python -m pytest
ruff check .
mypy .
```

If there is **no `.venv` yet**, create one:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pytest ruff mypy
```

If PowerShell blocks activation with an execution-policy error, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Since this came from an agent working on an existing repo, I’d first inspect `pyproject.toml`, `requirements*.txt`, `uv.lock`, `poetry.lock`, or `Pipfile` before manually installing anything. That avoids creating a dependency setup different from what the repo expects.

## Assistant

Worked for 5s

## Assistant

Yep — your screenshot shows that the repo **already has a `.venv` folder**, so you should activate that environment rather than create another one.

In the VS Code PowerShell terminal, from the repo root, run:

```powershell
.\.venv\Scripts\Activate.ps1
```

You should then see:

```text
(.venv) PS D:\...\Agentic Fraud Investigation>
```

Now verify that VS Code/terminal is actually using the venv:

```powershell
python -c "import sys; print(sys.executable)"
```

It should print a path ending roughly like:

```text
Agentic Fraud Investigation\.venv\Scripts\python.exe
```

Then check the tools:

```powershell
python -m pytest --version
python -m ruff --version
python -m mypy --version
```

If those still say they're missing, install them **inside this `.venv`**:

```powershell
python -m pip install pytest ruff mypy
```

Then your agent/tests can run:

```powershell
python -m pytest
python -m ruff check .
python -m mypy .
```

### Also set VS Code to use this environment

Because otherwise your terminal might use `.venv` while VS Code/Codex uses your global Python.

Press:

```text
Ctrl + Shift + P
```

Search:

```text
Python: Select Interpreter
```

Choose:

```text
.\.venv\Scripts\python.exe
```

Then **close the current terminal and open a new one**.

Since I can also see `pyproject.toml` in your repo, before permanently adding `pytest`, `ruff`, and `mypy`, it's worth checking whether they're already defined there as development dependencies. If they are, install the project's dev dependencies rather than maintaining them manually.

## User

do

## Assistant

Worked for 5s

## User

es it have .venv

## Assistant

Worked for a couple of seconds

## Assistant

No — from this screenshot, I don’t see an actual `.venv` folder in the repo.

What you saw earlier was this line inside `.gitignore`:

```text
/.venv/
```

That only tells Git to ignore a `.venv` folder if one exists. It does **not** mean the virtual environment has been created.

Your PowerShell error confirms that:

```text
.\.venv\Scripts\Activate.ps1
```

doesn’t exist.

Create it now from the repo root:

```powershell
py -m venv .venv
```

Then activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, install the dev tools:

```powershell
python -m pip install --upgrade pip
python -m pip install pytest ruff mypy
```

Then verify:

```powershell
python -m pytest --version
python -m ruff --version
python -m mypy --version
```

And run the checks:

```powershell
python -m pytest
python -m ruff check .
python -m mypy .
```

Since your repo has a `pyproject.toml`, it would be better to check that file first for existing dependency groups before installing manually. If you paste its contents, I can tell you the exact install command.

## Resources

### Local attachments
- [698b1af6-47b4-4f92-881d-80a15ed6fd75.png](../../../Raw/Export/file_0000000025488211be8d27076f16d235.dat)
