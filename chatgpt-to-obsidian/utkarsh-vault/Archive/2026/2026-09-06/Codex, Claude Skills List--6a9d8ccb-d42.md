---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a9d8ccb-d424-83e8-b5ae-8416e35b1de9"
created: 1788710093.101284
updated: 1788854657.238761
resource_section: true
---

# Codex, Claude Skills List

## User

what were the skills i gave to codex, list all of them

## Assistant

Worked for 10s

## Assistant

The skills/plugins I remember you giving to **Codex** were:

- **frontend-design**
- **superpowers**
- **skill-creator**
- **feature-dev**
- **chrome-devtools-mcp**
- **firecrawl**
- **swift-lsp**

These are the ones that came up when you were configuring the coding-agent environment and marketplaces. You also had **OpenAI bundled marketplaces** configured in Codex, but that’s a marketplace/source rather than an individual skill.

I’m deliberately not mixing these with your Claude Code setup unless you want a combined **Codex vs Claude skills/plugins** list. memcite

## User

give claude code skills also

## Assistant

For **Claude Code**, the skills/plugins you had installed were:

- **frontend-design**
- **superpowers**
- **skill-creator**
- **feature-dev**
- **chrome-devtools-mcp**
- **firecrawl**
- **swift-lsp**

So based on what I have from your setup, your **Claude Code skill/plugin set was the same list**. You also added the **official Claude marketplace** around that setup. memcite

## User

i have these skills installed, add this to ur memory and remember

## Assistant

Worked for a couple of seconds

## Assistant

Remembered. Your current installed skills baseline is **23 skills**:

1. Brandkit 
2. Deploy to Vercel 
3. Design Taste Frontend 
4. Design Taste Frontend V1 
5. Find Skills 
6. Full Output Enforcement 
7. Gpt Taste 
8. High End Visual Design 
9. Image to Code 
10. Imagegen Frontend Mobile 
11. Imagegen Frontend Web 
12. Industrial Brutalist UI 
13. Minimalist UI 
14. Redesign Existing Projects 
15. Stitch Design Taste 
16. Vercel CLI with Tokens 
17. Vercel Composition Patterns 
18. Vercel Optimize 
19. Vercel React Best Practices 
20. Vercel React Native Skills 
21. Vercel React View Transitions 
22. Web Design Guidelines 
23. Writing Guidelines

I’ll use this as the current list when you ask about your installed coding-agent skills later.

## User

now i want to redesign preexisting fronted of https://github.com/DgrnBoi/statskill-ai, user has added me as contributor, so i can make changes, give me prompt for this

## Assistant

Worked for 4s

## Assistant

Use this prompt in Codex/Claude Code from inside the `statskill-ai` repo:

```text
You are redesigning the frontend of an EXISTING project:

Repository:
https://github.com/DgrnBoi/statskill-ai

I am a contributor to this repository and I want to redesign the existing frontend without unnecessarily changing the product logic, backend contracts, or core functionality.

IMPORTANT:
Do not blindly rewrite the entire frontend.
First inspect the existing repository, understand the architecture, frontend stack, routes, components, current design system, backend/API dependencies, authentication flow if present, and identify what can be safely redesigned.

Use my installed skills whenever relevant, especially:

- Design Taste Frontend
- High End Visual Design
- Image to Code
- Imagegen Frontend Web
- Redesign Existing Projects
- Minimalist UI
- Web Design Guidelines
- Vercel React Best Practices
- Vercel Composition Patterns
- Vercel React View Transitions
- Full Output Enforcement

Primary goal:
Transform the current frontend into a polished, modern, premium-quality product interface that feels deliberately designed by a strong product/design team rather than a generic AI-generated dashboard.

DESIGN DIRECTION

The final UI should feel:

- modern
- premium
- clean
- highly usable
- restrained
- technically sophisticated
- visually consistent
- responsive
- fast
- professional enough to show in a portfolio, demo, hackathon, or production environment

Avoid obvious “AI slop” patterns such as:

- excessive gradients
- random purple/blue glow everywhere
- giant rounded cards for every element
- overly pill-shaped UI
- unnecessary glassmorphism
- excessive shadows
- gigantic hero text
- decorative elements with no purpose
- repetitive cards with identical styling
- fake metrics or invented content
- excessive animations
- icon overload
- generic SaaS-template appearance

DESIGN PRINCIPLES

1. Preserve information hierarchy.
2. Make dense information easy to scan.
3. Use spacing intentionally.
4. Use a limited and coherent color system.
5. Use typography to create hierarchy rather than excessive borders/cards.
6. Reduce unnecessary containers.
7. Prefer subtle separators and layout structure.
8. Use whitespace carefully, but do not make the interface unnecessarily sparse.
9. Make primary actions obvious.
10. Make secondary actions visually quieter.
11. Ensure accessible contrast.
12. Keep visual language consistent across every route.
13. Components should look related, not independently generated.
14. Mobile should feel intentionally designed, not simply collapsed desktop UI.
15. Preserve or improve performance.

BEFORE CODING

Perform an audit of the repository and report:

1. Frontend framework and version
2. Styling approach
3. Component structure
4. Existing routes/pages
5. Reusable components
6. State-management approach
7. API integration points
8. Authentication dependencies
9. UI/UX problems in the current implementation
10. Technical problems that could make the redesign harder
11. Components that should be preserved
12. Components that should be refactored
13. Components that should be replaced

Then create a concise redesign plan.

Do NOT change architecture unnecessarily.
Do NOT introduce a new UI framework unless there is a strong reason.
Prefer using the existing stack.

DESIGN SYSTEM

Before redesigning individual screens, define a small internal design system using existing project conventions.

Define:

- typography scale
- spacing scale
- border radius strategy
- surface hierarchy
- background hierarchy
- border colors
- text colors
- muted text
- accent color
- semantic success/warning/error colors
- button variants
- input variants
- card/container patterns
- modal styling
- navigation styling
- table styling if applicable
- empty states
- loading states
- error states

Keep tokens centralized where practical.

If Tailwind is used, organize this cleanly through theme/config/CSS variables rather than scattering arbitrary values everywhere.

LAYOUT

Improve the application shell first.

Pay attention to:

- navigation
- sidebar/header
- active route state
- content width
- page titles
- breadcrumbs if genuinely useful
- mobile navigation
- page padding
- scrolling behavior
- responsive breakpoints

Avoid excessive full-width layouts on large monitors if the content becomes hard to read.

COMPONENT QUALITY

Refactor repetitive UI into reusable components where useful, but do not over-engineer.

Examples:

- Button
- Input
- Select
- Badge
- Card/Surface
- Modal/Dialog
- EmptyState
- LoadingState
- ErrorState
- PageHeader
- Metric
- Data table wrappers
- Form field wrappers

Do not create abstractions that are used only once unless they materially improve clarity.

MOTION

Use animation sparingly.

Animations should primarily support:

- route/view transitions
- modal opening
- dropdowns
- hover feedback
- loading transitions
- state changes

Use subtle timing and motion.

Avoid constant floating, glowing, bouncing, or decorative motion.

RESPONSIVENESS

Explicitly verify:

- 320–375 px mobile
- tablet
- laptop
- 1440p desktop
- wide desktop

No horizontal overflow.
No broken cards.
No clipped buttons.
No tiny touch targets.
No desktop-only interaction assumptions.

ACCESSIBILITY

Ensure:

- semantic HTML
- keyboard navigation
- visible focus states
- proper button elements
- form labels
- meaningful aria attributes where required
- accessible contrast
- reduced-motion compatibility where feasible

PRODUCT INTEGRITY

This is a frontend redesign, not a product rewrite.

DO NOT:

- change backend API contracts unless required
- change database structure
- remove existing features
- create fake features
- invent data
- break authentication
- replace working logic just because another approach looks cleaner
- rewrite large portions of stable code without justification

If something in the current frontend is functionally broken, clearly distinguish:
“existing bug”
from
“redesign change”.

IMPLEMENTATION STRATEGY

Work incrementally.

Suggested order:

1. Audit repository
2. Identify frontend entry points
3. Establish design tokens
4. Redesign application shell/navigation
5. Redesign highest-traffic/main page
6. Redesign remaining pages
7. Refactor shared components
8. Add responsive behavior
9. Add loading/error/empty states
10. Add subtle motion
11. Accessibility pass
12. Performance pass
13. Run lint/typecheck/tests/build
14. Review git diff
15. Remove accidental/unrelated changes

Do not perform a giant uncontrolled rewrite.

VISUAL REVIEW

After each major page/component is redesigned:

- inspect the rendered result
- look for awkward spacing
- check typography hierarchy
- check visual density
- check alignment
- check responsive behavior
- verify dark/light theme compatibility if the project supports themes
- fix obvious inconsistencies before moving on

If browser/computer-use tooling is available, use it to inspect the actual rendered frontend instead of evaluating solely from source code.

QUALITY BAR

Ask yourself for every screen:

“Would this look credible if a senior product designer and senior frontend engineer reviewed it?”

If the answer is no, refine it.

CODE QUALITY

Maintain:

- simple component boundaries
- minimal duplication
- strong naming
- no dead CSS
- no unexplained magic numbers
- no unnecessary dependencies
- no huge monolithic components where decomposition helps
- no spaghetti state logic
- no design values duplicated across dozens of files

Do not add libraries simply because they are fashionable.

GIT SAFETY

Before editing:

1. Check `git status`.
2. Identify current branch.
3. Do not overwrite unrelated user changes.
4. Create a dedicated redesign branch if I am currently on main/master.

Suggested branch:

feat/frontend-redesign

Do not commit until the redesign is validated unless I explicitly ask you to commit.

FINAL VERIFICATION

Before declaring the task complete:

- run installation only if required
- run lint
- run typecheck if configured
- run tests if configured
- run production build
- inspect browser console for errors
- check network/API failures
- test desktop
- test mobile
- ensure existing core workflows still work
- verify no secrets are added
- inspect `git diff --stat`
- inspect final diff for unrelated modifications

At completion, provide:

1. What you changed
2. Design decisions made
3. Files changed
4. Components introduced/refactored
5. Functional behavior preserved
6. Any existing bugs you discovered
7. Any remaining issues
8. Build/test/lint results
9. Suggested screenshots/pages I should manually verify
10. Recommended commit message

Start by inspecting the repository.

Do NOT begin writing frontend code until you understand the current implementation and have given me the audit + redesign plan.
```

One thing I’d keep exactly as written is the **“audit first, don’t code immediately”** instruction. Since this is someone else’s existing repo and you’re contributing rather than starting from scratch, it’ll stop Codex from nuking working structure just to make the UI prettier.

Also, your `Redesign Existing Projects + Design Taste Frontend + High End Visual Design` skills are particularly suited to this job, while the Vercel React skills should only kick in if the repo is actually React/Next-based. memcite

## User

why are you making these many changes in same file, this is not token efficient, optimize ur tokens, context and every single thing.

write prompt with as this main moto for codex

## Assistant

Worked for a couple of seconds

## Assistant

Use this as a **global operating prompt for Codex**. The main principle is: **minimum necessary work, maximum useful result**. It specifically tells Codex to stop repeatedly rewriting the same file, rereading unnecessary context, and burning tokens on verbose reasoning.

```text
# CODEX OPERATING PRINCIPLE — TOKEN, CONTEXT & CHANGE EFFICIENCY

Your highest-level engineering constraint for this project is:

MINIMUM NECESSARY WORK → MAXIMUM CORRECT RESULT.

Optimize EVERYTHING:
- token usage
- context-window usage
- tool calls
- file reads
- file writes
- shell commands
- browser interactions
- generated output
- code changes
- git diff size
- iteration count
- repeated reasoning

Do not confuse "working harder" with "doing better".

A clean 20-line targeted change is preferable to a 500-line rewrite if both solve the same problem.

==================================================
1. AVOID REPEATED EDITS TO THE SAME FILE
==================================================

Do NOT repeatedly modify the same file in many tiny iterations.

Bad behavior:

tokens.css
+0 -112

tokens.css
+0 -112

tokens.css
+0 -112

tokens.css
+0 -112

...repeated over and over while experimenting.

This wastes:
- context
- tokens
- tool calls
- edit history
- time
- reasoning capacity

Instead:

1. Read the relevant file once.
2. Understand its dependencies.
3. Decide the intended final state.
4. Prepare the complete coherent edit mentally.
5. Apply the edit once, or in as few passes as realistically possible.
6. Validate it.
7. Reopen/re-edit only if validation reveals an actual problem.

TARGET:

READ → PLAN → EDIT ONCE → VALIDATE

not:

READ → EDIT → READ → EDIT → READ → EDIT → REVERT → EDIT

==================================================
2. BATCH RELATED CHANGES
==================================================

When several changes belong to one logical task, batch them.

For example, if redesigning design tokens:

BAD:
- remove spacing token
- save
- inspect
- remove color token
- save
- inspect
- change radius
- save
- inspect
- change typography
- save

GOOD:
- inspect tokens.css
- inspect its usages
- determine final token system
- perform one coherent replacement
- run validation

The goal is not literally "one write per file" under all circumstances.

The goal is to avoid unnecessary edit churn.

==================================================
3. DO NOT REWRITE WORKING CODE
==================================================

Preserve existing code whenever possible.

Before replacing something, ask:

"Can the goal be achieved by modifying the existing implementation?"

Prefer:

PATCH > REFACTOR > REWRITE

A rewrite should only happen when the existing implementation genuinely blocks the desired result.

Do not rewrite files because:
- you prefer another style
- another abstraction looks cleaner
- you want to demonstrate a pattern
- regenerating is easier than understanding
- a skill suggests a different architecture

Existing working behavior has value.

==================================================
4. MINIMIZE GIT DIFF
==================================================

Treat git diff size as an engineering constraint.

Every changed line should have a reason.

Before modifying a file, ask:

"Does this file actually need to change?"

Before adding a dependency, ask:

"Can this be done with what the project already has?"

Before creating a new component, ask:

"Is an existing component already suitable?"

Before adding a CSS rule, ask:

"Does an existing token/class already solve this?"

Avoid:
- formatting unrelated files
- reorganizing imports unnecessarily
- mass renames without value
- changing whitespace unrelated to the task
- touching generated files unless required
- replacing whole files for small modifications

At completion:

git diff --stat
git diff

Review both.

Remove unrelated changes.

==================================================
5. CONTEXT WINDOW IS A RESOURCE
==================================================

Treat context like RAM.

Do not continually dump entire files into context.

Read only what is needed.

Prefer targeted inspection such as:

- relevant file sections
- imports
- component definition
- referenced CSS selectors
- specific API calls
- dependency declarations
- relevant routes

Do not repeatedly reread files whose contents are already understood unless they changed materially.

If a file is large, locate the relevant symbol first.

Examples:

rg "ComponentName"
rg "token-name"
rg "className"
rg "functionName"
rg "endpoint"

Then inspect the smallest useful region.

==================================================
6. SEARCH BEFORE READING
==================================================

For unfamiliar repositories:

Do NOT blindly open dozens of files.

Use repository search first.

Preferred flow:

tree / file listing
→ search relevant symbols
→ inspect only likely files
→ understand dependency path
→ change

For example:

rg "tokens.css" frontend/src
rg "var\\(--" frontend/src
rg "Button" frontend/src
rg "API_URL" frontend/src

Repository search is usually cheaper than reading everything.

==================================================
7. DO NOT OVER-ANALYZE SIMPLE CHANGES
==================================================

Scale reasoning to task complexity.

For a trivial CSS adjustment:
- inspect relevant styles
- change them
- verify

Do not produce a 30-step architectural analysis.

For architectural changes:
- reason deeply before editing.

Spend intelligence where it matters.

==================================================
8. PLAN BEFORE TOUCHING CODE
==================================================

Before significant edits, establish:

- objective
- affected files
- dependencies
- safest minimal implementation
- validation method

You do NOT need to print a giant plan to me.

Keep the plan concise.

Internally determine the complete direction before beginning edits.

This prevents oscillating between implementations.

==================================================
9. DO NOT EXPERIMENT DIRECTLY IN PRODUCTION FILES
==================================================

Do not use repeated edits to production files as a scratchpad.

If uncertain:

- reason first
- inspect documentation
- use a temporary scratch file if truly necessary
- test an isolated implementation

Then make the final source edit.

Source files are not your notebook.

==================================================
10. BE TOKEN-EFFICIENT IN RESPONSES
==================================================

Do not narrate every action.

Avoid output like:

"I'll inspect the file..."
"Now I'll check..."
"Next I'll..."
"I found..."
"I am now going to..."

Unless the information is actually useful.

During execution, keep commentary concise.

Report:
- important discoveries
- important decisions
- blockers
- final results

Do not dump routine command output unless needed.

==================================================
11. DON'T REPEAT INFORMATION
==================================================

If something has already been established in the current session, reuse it.

Do not repeatedly explain:
- repository architecture
- framework
- routes
- design direction
- user requirements
- previously inspected code

Maintain a compact mental working model.

==================================================
12. USE SKILLS SELECTIVELY
==================================================

Available skills are tools, not mandatory stages.

Do NOT run every relevant skill simply because it exists.

Choose the smallest useful subset.

For frontend redesign work, likely useful skills include:

- Redesign Existing Projects
- Design Taste Frontend
- High End Visual Design
- Web Design Guidelines
- Vercel React Best Practices when appropriate

Do not invoke five overlapping design workflows to solve one button.

Skills should reduce work, not multiply it.

==================================================
13. NO PARALLEL OVER-ENGINEERING
==================================================

Do not generate several implementations of the same thing unless explicitly requested.

Avoid:

Option A
Option B
Option C
Option D

then implementing one.

When requirements are clear:

Choose the strongest solution and implement it.

==================================================
14. KEEP COMPONENT ARCHITECTURE LEAN
==================================================

Do not abstract prematurely.

BAD:

Button
→ ButtonBase
→ InteractiveBase
→ ActionPrimitive
→ PressablePrimitive
→ StyledAction

when a normal reusable Button component is sufficient.

Create abstractions when they:
- remove meaningful duplication
- establish a real shared contract
- simplify future maintenance

Not merely because abstraction is possible.

==================================================
15. AVOID CSS EXPLOSION
==================================================

Do not solve redesigns by continually appending CSS.

Before adding styles:

1. inspect existing styles
2. identify obsolete rules
3. consolidate duplicates
4. reuse tokens
5. modify existing selectors when appropriate

Avoid turning index.css into an ever-growing patch log.

Prefer a coherent stylesheet over layers of overrides.

BAD:

.old-button {}
.old-button-new {}
.old-button-fix {}
.old-button-final {}
.old-button-final-2 {}

GOOD:

.button {}

with the correct final implementation.

==================================================
16. DESIGN TOKENS SHOULD BE STABLE
==================================================

Do not repeatedly regenerate tokens.css.

Before changing global tokens:

1. inspect all existing tokens
2. search where important tokens are consumed
3. identify what must stay compatible
4. design the final token set
5. perform one deliberate migration

Global design tokens have high fan-out.

Treat them as architecture, not experimentation.

==================================================
17. VALIDATE AT NATURAL CHECKPOINTS
==================================================

Do not run the full build after every tiny CSS change.

Use validation proportionally.

Small local change:
→ quick targeted check

Component completion:
→ relevant lint/typecheck/browser check

Major milestone:
→ full validation

Final:
→ complete validation

Batch validation intelligently.

==================================================
18. COMMAND EFFICIENCY
==================================================

Avoid unnecessary shell commands.

Do not repeatedly run:

git status
git diff
git status
git diff
git status

after every modification.

Use them at meaningful checkpoints.

Combine independent searches when appropriate.

Avoid reinstalling dependencies if already installed.

Avoid rebuilding when no relevant files changed.

==================================================
19. DEPENDENCY DISCIPLINE
==================================================

Adding a package has cost.

Before adding one, determine whether:
- the browser/platform already provides it
- the project already has an equivalent
- a small local implementation is simpler

Do not install a library for a trivial helper.

==================================================
20. FIX ROOT CAUSES
==================================================

When validation fails:

Do not stack patches blindly.

Find the root cause.

Bad:

error
→ add workaround
→ new error
→ add another workaround
→ another error
→ disable check

Good:

error
→ inspect source
→ understand root cause
→ make one correct fix

==================================================
21. DO NOT DESTROY AND RECREATE FILES UNNECESSARILY
==================================================

Prefer surgical edits.

Do not replace a 700-line file because 40 lines need modification.

Large rewrites increase:
- regression risk
- context usage
- review difficulty
- merge conflicts

This is especially important when contributing to someone else's repository.

==================================================
22. OPTIMIZE FOR REVIEWABILITY
==================================================

Someone else owns this repository.

The final PR should be easy to review.

A reviewer should understand:

- why each file changed
- what the redesign changed
- what behavior stayed intact

Avoid giant noisy diffs.

A good contribution is not only correct.

It is reviewable.

==================================================
23. PRESERVE CONTRIBUTOR-FRIENDLY HISTORY
==================================================

Do not repeatedly create commits for intermediate failed attempts.

Work toward a coherent final state first.

When committing later, commits should represent logical changes.

Example:

feat(frontend): redesign application shell
feat(frontend): refine dashboard UI
fix(frontend): improve responsive navigation

Not:

fix css
fix css again
button
button fix
final button
really final

==================================================
24. STOP WHEN THE TASK IS COMPLETE
==================================================

Do not continue polishing indefinitely.

Once:
- requirements are satisfied
- UX is coherent
- validation passes
- diff is clean

STOP.

Do not invent extra work.

==================================================
25. PRIMARY OPTIMIZATION FUNCTION
==================================================

For every action, implicitly evaluate:

VALUE OF ACTION
----------------
tokens consumed
context consumed
time consumed
risk introduced
diff generated

Prefer actions with the highest useful value per unit cost.

The objective is NOT minimum tokens at the expense of quality.

The objective is:

MAXIMUM ENGINEERING QUALITY
WITH MINIMUM NECESSARY COMPUTATION AND CHANGE.

==================================================
26. DEFAULT WORKFLOW
==================================================

Use this workflow unless the task requires otherwise:

UNDERSTAND
↓
SEARCH
↓
READ MINIMUM REQUIRED CONTEXT
↓
FORM FINAL APPROACH
↓
EDIT COHERENTLY
↓
VALIDATE
↓
FIX ROOT CAUSES ONLY IF NECESSARY
↓
REVIEW DIFF
↓
STOP

Avoid:

READ EVERYTHING
↓
TRY SOMETHING
↓
EDIT
↓
RE-READ
↓
TRY SOMETHING ELSE
↓
REWRITE
↓
REVERT
↓
REWRITE AGAIN
↓
RUN EVERYTHING
↓
KEEP POLISHING

==================================================
FINAL RULE
==================================================

Before every meaningful tool call or code edit, ask:

"Is this action necessary, and is there a cheaper way to get the same correct result?"

Before editing a file again, ask:

"Why was the previous edit insufficient?"

If there is no concrete answer, do not edit it again.

Before reading something again, ask:

"Has this information changed or do I actually need it?"

If not, reuse existing context.

Before adding code, ask:

"Can I solve this by improving what already exists?"

Prefer that.

Be deliberate.
Be surgical.
Be context-efficient.
Be token-efficient.
Be diff-efficient.
Be tool-efficient.

QUALITY FIRST.
WASTE NEVER.
```

For your specific `statskill-ai` redesign, I'd append this one extra rule because the screenshot shows exactly the failure mode you want to prevent:

```text
# STRICT FRONTEND REDESIGN RULE

For this redesign, do not use iterative CSS rewriting as a visual exploration strategy.

Before changing global files such as:

- index.css
- tokens.css
- globals.css
- theme files
- Tailwind configuration

first inspect their consumers and establish the intended final design system.

Global CSS/token files should normally receive ONE coherent redesign pass, followed only by small validation-driven corrections.

If you find yourself editing the same global stylesheet repeatedly, STOP.

Reassess the design and dependencies before making another edit.

Do not repeatedly delete/recreate tokens.css, regenerate design tokens, or append overrides to compensate for earlier changes.

The final diff should look like an intentional human-authored redesign, not the history of an agent experimenting.
```

This should be a **persistent instruction for the whole Codex session/project**, not something you paste separately before every task. It fits your architecture-first preference too: decide the end state, then make the smallest coherent change rather than letting the agent thrash around. memcite

## User

That review panel is duplicating the same `tokens.css +0/−112` entry; the repository itself has one `tokens.css` file and one consolidated diff (`63 additions, 105 deletions`), not twenty separate copies or rewrites.

## Assistant

Worked for a couple of seconds

## Assistant

Yes — that changes the diagnosis.

The screenshot is showing a **UI duplication bug/quirk in the Review panel**, not Codex repeatedly rewriting `tokens.css`. If the actual repository state shows **one file** and one consolidated diff like **63 additions / 105 deletions**, then my earlier interpretation was wrong.

So the prompt should **not** accuse Codex of repeatedly editing the file based on that panel. Instead, optimize actual agent behavior using **real repository evidence** such as `git diff`, tool-call history, and file reads.

Use this corrected prompt:

```text
# CODEX EFFICIENCY DIRECTIVE

Optimize this entire coding session for:

MAXIMUM CORRECT RESULT
with
MINIMUM NECESSARY TOKENS, CONTEXT, TOOL CALLS, FILE READS, EDITS, AND DIFF SIZE.

IMPORTANT:
Do not infer repeated file edits from the Review UI alone.

The Codex Review panel may visually duplicate the same file/diff entry multiple times.
Use the actual repository state as the source of truth:

- git diff
- git diff --stat
- git status
- actual tool/edit history

If the Review panel shows the same `tokens.css +0/-112` entry many times but git contains one consolidated diff, treat that as ONE change, not repeated rewrites.

## Core workflow

For every task:

SEARCH → READ MINIMUM CONTEXT → PLAN → MAKE COHERENT EDIT → VALIDATE → REVIEW DIFF → STOP

Avoid unnecessary exploratory loops.

## 1. TOKEN EFFICIENCY

Treat tokens as a finite engineering resource.

Do not:
- narrate routine actions
- repeat already-established information
- dump entire files unnecessarily
- generate long plans for trivial tasks
- explain obvious command output
- restate requirements repeatedly

Keep intermediate commentary extremely concise.

Spend tokens primarily on:
- understanding unfamiliar logic
- architectural decisions
- debugging
- implementation
- validation

## 2. CONTEXT EFFICIENCY

Treat the context window like working memory.

Before opening a file, ask:

"Do I actually need this file to complete the task?"

Prefer repository search first:

rg "ComponentName"
rg "token-name"
rg "functionName"
rg "className"
rg "API_URL"

Then inspect only the relevant sections.

Do not reread unchanged files unless necessary.

Do not load huge files when a small relevant range is sufficient.

Maintain a compact mental model of:
- architecture
- relevant files
- dependencies
- decisions already made

## 3. EDIT EFFICIENCY

Prefer:

SMALL PATCH > TARGETED REFACTOR > FULL REWRITE

Do not replace working code unnecessarily.

Before editing, determine the intended final state so related modifications can be made coherently.

Avoid edit churn.

However, DO NOT artificially force "one edit per file."

Multiple edits are acceptable when:
- validation reveals a real issue
- new information changes the implementation
- separating edits reduces risk

The objective is minimum NECESSARY edits, not minimum edit count.

## 4. USE ACTUAL GIT DIFF AS SOURCE OF TRUTH

Judge modification size from:

git diff --stat
git diff

NOT from duplicated Review-panel rows.

At logical checkpoints, inspect the actual diff.

Ensure:
- no accidental file changes
- no formatting-only noise
- no unrelated modifications
- no unnecessary rewrites

Do not repeatedly run git diff after every trivial modification.

## 5. MINIMIZE DIFF SIZE

Every changed line should contribute to the requested result.

Avoid:
- unrelated formatting
- mass import reordering
- unnecessary renaming
- replacing files unnecessarily
- changing architecture without need
- touching backend code during frontend redesign unless required

This is someone else's repository.

Optimize for a PR that is easy to review.

## 6. SEARCH BEFORE OPENING MANY FILES

When unfamiliar with an area of the repository:

BAD:
open 20 files and read them completely.

GOOD:

1. inspect directory structure
2. search symbols/references
3. identify dependency chain
4. open only relevant files
5. implement

Use search to reduce context usage.

## 7. SKILL EFFICIENCY

I have many installed skills.

Do not invoke every potentially relevant skill.

Select only the smallest useful subset for the current task.

For this frontend redesign, likely primary skills are:

- Redesign Existing Projects
- Design Taste Frontend
- High End Visual Design
- Web Design Guidelines

Use these only when their contribution is meaningful.

Use Vercel/React-specific skills only if the repository and current problem actually require them.

Skills must reduce uncertainty or improve quality.

They must not become additional ceremony.

## 8. CSS / DESIGN TOKEN DISCIPLINE

Global styling files have high fan-out.

Before significantly modifying files such as:

- tokens.css
- index.css
- globals.css
- theme configuration
- Tailwind config

first inspect how their important tokens/classes are consumed.

Then make a coherent design decision.

Avoid accumulating layers like:

old implementation
+ override
+ fix
+ override
+ final fix

Prefer modifying the canonical definition.

Do not continuously append CSS to compensate for earlier CSS.

## 9. DO NOT OVER-ENGINEER

Use the project's existing architecture unless it genuinely prevents the solution.

Do not:
- create unnecessary abstractions
- install unnecessary packages
- introduce a new design system framework merely for redesign
- break components into tiny wrappers without value
- build generic infrastructure for hypothetical future requirements

Solve the current problem cleanly.

## 10. COMMAND EFFICIENCY

Avoid redundant tool calls.

Do not repeatedly execute equivalent commands.

Examples:

BAD:

git status
git diff
git status
git diff
git status

GOOD:

Run them at meaningful checkpoints.

Likewise:

Do not repeatedly reinstall dependencies.
Do not repeatedly rebuild unchanged code.
Do not rerun expensive tests unless relevant changes occurred.

## 11. VALIDATION EFFICIENCY

Validate proportionally.

Tiny CSS/local change:
→ targeted browser check

Completed component:
→ relevant lint/type/browser check

Major redesign milestone:
→ broader validation

Final:
→ full lint/typecheck/tests/build as available

Do not run the entire validation suite after every tiny change.

## 12. ROOT-CAUSE DEBUGGING

When something breaks:

ERROR
→ investigate
→ understand root cause
→ fix root cause
→ validate

Do not stack random patches until the error disappears.

## 13. FRONTEND REDESIGN SPECIFICALLY

This is a redesign of an existing frontend.

Preserve:
- routes
- APIs
- authentication
- business logic
- user workflows
- backend contracts

unless explicitly required otherwise.

Focus changes primarily on:
- visual hierarchy
- layout
- typography
- spacing
- component styling
- responsiveness
- interaction quality
- accessibility
- consistent design language

Do not turn a frontend redesign into a repository rewrite.

## 14. DESIGN DELIBERATELY BEFORE STYLING

For each major page:

Understand current content and hierarchy first.

Then decide:
- layout
- hierarchy
- reusable patterns
- typography
- spacing
- surfaces
- responsive behavior

Then implement.

Do not use source files as a visual experimentation scratchpad.

## 15. STOP CONDITION

When:
- requested result is implemented
- functionality works
- design is coherent
- validation passes
- git diff is clean

STOP.

Do not continue inventing improvements.

## OPERATING QUESTION

Before any expensive action, ask:

"Will this materially improve the final result?"

Before reading a file:

"Can repository search give me the answer more cheaply?"

Before editing:

"Can the existing implementation be modified instead?"

Before adding code:

"Is this actually necessary?"

Before using another skill:

"Will it add unique value beyond the skills already used?"

Before another validation command:

"Has anything changed that makes this validation useful?"

Before continuing:

"Is the requested task already complete?"

Optimize for:

QUALITY / (TOKENS + CONTEXT + TOOL CALLS + TIME + DIFF + RISK)

Do not optimize one metric blindly.

In particular:
- do not sacrifice correctness to save tokens
- do not sacrifice maintainability to reduce diff
- do not avoid necessary validation to save time

Be deliberate, surgical, and efficient.
```

And I would **remove** my previous strict rule saying:

> “Global CSS/token files should normally receive ONE coherent redesign pass”

because that can actually make Codex worse—it might force an oversized speculative edit just to satisfy the prompt. The better target is **few justified edits**, with `git diff` being the ground truth.

Also, `+1,873 / -2,496` in the screenshot is the **Last Turn aggregate**, so that’s the number worth scrutinizing for token/diff efficiency—not the duplicated visual rows for `tokens.css`.

## User

i will add this is AGENTS.md file

## Assistant

Yes — `AGENTS.md` is a good place for this.

I’d make one change though: **shorten it significantly** before putting it there. `AGENTS.md` is injected into context repeatedly, so if it’s huge, the “token-efficiency prompt” itself becomes token-inefficient.

Use this tighter version:

```md
# AGENTS.md

## Core Operating Principle

Optimize for:

**maximum correct result with minimum necessary tokens, context, tool calls, edits, diff size, and risk.**

Use:

**SEARCH → READ MINIMUM CONTEXT → PLAN → EDIT COHERENTLY → VALIDATE → REVIEW DIFF → STOP**

Do not over-analyze, over-read, over-edit, or over-engineer.

---

## Repository Evidence Is the Source of Truth

Do not infer repeated edits from the Codex Review UI.

The Review panel may visually duplicate the same file/diff entry.

Use the actual repository state:

- `git diff`
- `git diff --stat`
- `git status`
- actual edit/tool history

A duplicated Review entry does not mean a file was rewritten multiple times.

---

## Context Efficiency

Treat context as a limited resource.

Before reading a file, ask whether it is actually required.

Prefer search first:

```bash
rg "ComponentName"
rg "functionName"
rg "token-name"
rg "className"
rg "API_URL"
```

Then inspect only the relevant files/sections.

Avoid:
- reading entire large files unnecessarily
- reopening unchanged files without reason
- dumping large command outputs
- restating already-established architecture or requirements

Reuse information already established in the session.

---

## Edit Efficiency

Prefer:

**small patch > targeted refactor > rewrite**

Preserve working code whenever possible.

Before editing:
1. understand the intended final state
2. identify affected dependencies
3. make related changes coherently

Avoid unnecessary edit churn.

Multiple edits are acceptable when new evidence or validation requires them. Do not artificially optimize for "one edit per file."

---

## Diff Discipline

Every changed line should have a reason.

Avoid:
- unrelated formatting
- unnecessary import reordering
- mass renaming
- needless file rewrites
- generated-file changes unless required
- architecture changes unrelated to the task
- backend changes during frontend-only work unless necessary

At meaningful checkpoints inspect:

```bash
git diff --stat
git diff
```

Remove unrelated changes before completion.

Optimize for a PR that another maintainer can review easily.

---

## Tool and Command Efficiency

Do not repeatedly run equivalent commands.

Avoid patterns like:

```text
git status
git diff
git status
git diff
git status
```

Use checks at meaningful checkpoints.

Do not:
- reinstall dependencies unnecessarily
- rebuild unchanged code
- run expensive tests after every tiny change
- invoke tools without a clear purpose

Before an expensive tool call ask:

**Will this materially improve the result?**

---

## Token-Efficient Communication

Do not narrate routine actions.

Avoid unnecessary commentary such as:

- "I'll inspect the file now"
- "Next I'll check..."
- "Now I'm going to..."
- long summaries of obvious command output

Communicate mainly:
- important discoveries
- decisions
- blockers
- validation results
- final changes

Keep plans proportional to task complexity.

---

## Skills

Installed skills are tools, not mandatory workflow stages.

Use only the smallest useful subset.

For frontend redesign, likely relevant:

- Redesign Existing Projects
- Design Taste Frontend
- High End Visual Design
- Web Design Guidelines

Use React/Vercel-specific skills only when relevant to the current stack/task.

Do not invoke overlapping skills merely because they are installed.

---

## Frontend Redesign Rules

This is an existing product, not a greenfield rewrite.

Preserve unless explicitly required:

- routes
- backend/API contracts
- authentication
- business logic
- existing workflows
- working functionality

Focus redesign work on:

- visual hierarchy
- layout
- typography
- spacing
- component styling
- responsive behavior
- interaction quality
- accessibility
- consistency

Do not turn a frontend redesign into an architecture rewrite.

---

## CSS and Design Tokens

Global styling files have high impact.

Before significantly changing:

- `tokens.css`
- `index.css`
- `globals.css`
- theme files
- Tailwind configuration

inspect their important consumers first.

Prefer updating canonical styles over stacking overrides.

Avoid patterns like:

```text
old style
+ override
+ fix
+ override
+ final fix
```

Keep the styling system coherent.

Do not use production CSS files as an experimentation scratchpad.

---

## Architecture

Do not over-engineer.

Avoid:
- unnecessary abstractions
- unnecessary dependencies
- components created only to wrap one trivial element
- new design-system frameworks without strong justification
- infrastructure for hypothetical future requirements

Prefer the project's existing architecture.

Create abstractions only when they meaningfully reduce duplication or clarify a real shared contract.

---

## Validation

Validate proportionally.

Small local change:
- targeted check

Completed component:
- relevant lint/type/browser check

Major milestone:
- broader validation

Final:
- lint
- typecheck if configured
- tests if configured
- production build
- browser/runtime errors
- responsive behavior
- final git diff

Do not run the full validation suite after every trivial change.

---

## Debugging

Fix root causes.

Use:

**error → investigate → understand → correct fix → validate**

Do not stack speculative patches until the error disappears.

---

## Stop Condition

Stop when:

- requested work is complete
- functionality is preserved
- design/code is coherent
- validation passes
- diff contains no unrelated changes

Do not invent additional work after the task is complete.

---

## Decision Rule

Before a meaningful action ask:

1. Is this necessary?
2. Can I get the same answer with less context?
3. Can I modify existing code instead of replacing it?
4. Will another skill/tool add unique value?
5. Is the requested task already complete?

Optimize for:

**QUALITY / (TOKENS + CONTEXT + TOOL CALLS + TIME + DIFF + RISK)**

Never sacrifice correctness or maintainability merely to minimize tokens.
```

This is better for `AGENTS.md` because the important constraints stay persistent without burning thousands of tokens every time Codex loads project instructions.

## User

some what text is in canvas and other is out of it, should i copy and past both the text in agents.md or just the canvas one. ans in one line

## Assistant

Copy and paste **both** into `AGENTS.md` — the canvas/code block is only part of the full instruction, and the text outside it is also part of the prompt.

## User

limits are burning/hitting to fast, give a solution, use @Firecrawl to search if any one has already built a open-source reop or article or technique or method any thing you find that might help me

## Assistant

Worked for 1m 7s

## Assistant

Yes — I found a few concrete things, and your screenshot already reveals two major causes: you’re running **5.6 Terra at Extra High reasoning** and you have **multiple subagent threads active**. Those two together can burn quota extremely fast.

The strongest fix is not one magic repo; it’s a combination of **shorter injected context + fewer subagents + smaller reasoning/model for routine work + aggressive command-output limiting**.

1. **Shrink your `AGENTS.md` drastically.** This is especially important because we just made yours fairly large. OpenAI’s own Codex guidance explicitly says that reducing `AGENTS.md` size helps usage limits last longer, and recommends **nested `AGENTS.md` files** so only relevant instructions are injected for a directory/task. Source: OpenAI Codex docs, `developers.openai.com/codex/agent-configuration/agents-md`.

 I’d change your setup from one giant root file into something like:

 ```text
 repo/
 ├── AGENTS.md # ~30-50 lines, global only
 ├── frontend/
 │ └── AGENTS.md # frontend/design rules
 ├── backend/
 │ └── AGENTS.md # backend rules
 └── tests/
 └── AGENTS.md # testing rules
 ```

 Your root `AGENTS.md` should contain only universally applicable rules such as:

 ```md
 # AGENTS.md

 ## Efficiency
 Optimize for correctness with minimum necessary context, tool calls, and diff size.

 Use:
 SEARCH → READ MINIMUM CONTEXT → PLAN → EDIT → VALIDATE → STOP.

 - Search before opening large files.
 - Read only relevant sections.
 - Do not reread unchanged files without reason.
 - Prefer patch > targeted refactor > rewrite.
 - Do not narrate routine actions.
 - Avoid unrelated edits.
 - Use subagents only when they clearly save work.
 - Limit command output before adding it to context.
 - Validate proportionally to the change.
 - Stop when the requested task is complete.

 ## Git
 Use git diff/status as source of truth.
 Do not infer repeated edits from UI review entries.
 Keep the final PR focused and reviewable.
 ```

 That is enough globally. Put all frontend-specific design rules under `frontend/AGENTS.md`.

2. **Stop using Extra High reasoning as your default.** In your screenshot, Codex is running `5.6 Terra Extra High`. For things like CSS edits, renames, tests, routing changes, simple refactors, UI polishing, and repository inspection, that is overkill. OpenAI’s current Codex guidance specifically recommends switching to a smaller model for routine work; it mentions **GPT-5.6 Terra or Luna** as ways to stretch local-message usage depending on what you were using previously.

 I’d use roughly:

 | Task | Reasoning |
 |---|---|
 | CSS/layout/small bug | Low/Medium |
 | Normal feature | Medium |
 | Complex multi-file bug | High |
 | Architecture/very hard debugging | Extra High |

 Don't leave **Extra High** selected globally.

3. **Subagents are probably your biggest hidden multiplier.** Firecrawl surfaced a current issue in the official `openai/codex` repository: **“Parallel subagents cause extreme token amplification and repeated compaction”**. In that report, two review subagents each recorded about **340M cumulative tokens**, with repeated compactions and large amounts of inherited/shared history processing. That does not mean those exact numbers equal billed usage, but it shows how badly parallel children can amplify context processing. Source: `openai/codex#33196`.

 There’s also another recent issue, `openai/codex#35463`, titled **“Codex subagents drain full week quota overnight”**, specifically correlating heavy MultiAgent V2 usage with quota exhaustion.

 For you, add this to the global `AGENTS.md`:

 ```md
 ## Subagents

 Do not spawn subagents by default.

 Use a subagent only when:
 - the task is genuinely parallelizable, AND
 - delegating it is likely to reduce total work/context.

 For ordinary coding, inspection, CSS, debugging, and small refactors,
 stay in the primary agent.

 Never spawn multiple review/research subagents for a task that the
 primary agent can reasonably complete itself.

 Prefer one focused subagent over several overlapping subagents.
 ```

 Looking at your screenshot, you had a session plus **four threads**. I would specifically stop letting Codex create that many children for ordinary project work.

4. **Add byte-capped command output.** This was the most useful open-source technique I found. The repo \[`Austin1serb/agents-md`\](https://github.com/Austin1serb/agents-md) is explicitly designed around context engineering for Codex/Claude-style coding agents.

 Their key technique is to cap unknown command output by **bytes**, not lines:

 ```bash
 COMMAND 2>&1 | head -c 4000
 ```

 For errors/logs where the end matters:

 ```bash
 COMMAND 2>&1 | tail -c 4000
 ```

 Why bytes instead of:

 ```bash
 head -n 20
 ```

 Because one minified JSON line, source map, stack trace, or generated bundle can itself contain tens or hundreds of thousands of characters.

 The repo author claims this rule reduced their average token usage by roughly **50% across comparable Codex tasks**. That's anecdotal, not an OpenAI benchmark, but the technique itself is sound.

 Add:

 ```md
 ## Command Output

 Never pull large unknown command output directly into context.

 For potentially large output, cap it:

 COMMAND 2>&1 | head -c 4000

 For logs/errors where recent output matters:

 COMMAND 2>&1 | tail -c 4000

 Search/filter before printing entire files, logs, test output, JSON,
 dependency trees, git history, or build output.

 Prefer rg/grep/find with targeted patterns over broad dumps.
 ```

5. **Limit MCPs/plugins per project.** OpenAI’s own usage guidance says every MCP server contributes additional context and recommends disabling MCP servers you don’t currently need. This matters a lot with your setup because you have many plugins/skills installed. Installed is fine; **active/injected into each Codex session** is the costly part.

 For a frontend redesign, you probably only need something like:

 ```text
 Git/GitHub
 Browser/Chrome
 maybe Firecrawl
 maybe Vercel
 ```

 Not 10+ MCP servers simultaneously.

6. **Start fresh sessions instead of dragging a giant thread forever.** Your screenshot says:

 ```text
 Context:
 59% left
 105,476 used / 258k
 ```

 That means this thread already has more than **100k tokens of active context**. Every subsequent turn may need to work against a large conversation state.

 Once a logical milestone is complete, have Codex write a tiny handoff file:

 ```md
 # HANDOFF.md

 Goal:
 ...

 Completed:
 ...

 Current architecture:
 ...

 Files changed:
 ...

 Remaining:
 ...

 Important constraints:
 ...
 ```

 Then start a **fresh session** and give it `HANDOFF.md` plus the next task.

 This is often much cheaper than endlessly continuing the same 150k–250k context thread.

7. **Compact earlier, but don't assume compaction itself is free.** Codex supports configuration such as:

 ```toml
 model_context_window = ...
 model_auto_compact_token_limit = ...
 ```

 OpenAI's config sample documents those settings. I would **not blindly copy random values from Reddit/GitHub**, because your available window depends on model/runtime and Codex version.

 The useful principle is:

 ```text
 smaller working context
 + earlier clean handoffs
 > carrying enormous context until forced compaction
 ```

 Repeated compaction itself can become expensive if a long-running agent repeatedly fills the context again.

8. **Don't ask Codex to “explore the entire repo” unless necessary.** This is another major source of silent waste.

 Instead of:

 ```text
 Explore this entire project and understand everything before making changes.
 ```

 use:

 ```text
 Identify only the files relevant to this task.
 Search symbols and dependency references first.
 Read the minimum necessary sections.
 Do not perform a repository-wide audit unless required.
 ```

 That change alone can prevent Codex from opening 30–100 files for a 3-file change.

### What I would change in your setup right now

Your highest-impact configuration would be:

```text
ROOT AGENTS.md
 ↓
30–50 lines only

frontend/AGENTS.md
 ↓
frontend/design rules

Default reasoning
 ↓
Medium

Extra High
 ↓
only manually for hard problems

Subagents
 ↓
OFF/default avoid
1 max unless genuinely parallel

MCPs
 ↓
only task-relevant ones

Command output
 ↓
4 KB caps where output size is unknown

Long sessions
 ↓
HANDOFF.md → new session
```

And most importantly: **the large `AGENTS.md` I gave you earlier should not remain as one giant root-level file.** OpenAI's own current guidance confirms the exact concern you're seeing: large instructions consume usage, and nested project instructions are the better pattern.

The three resources I'd actually keep bookmarked are the official Codex `AGENTS.md` documentation, the open-source \[`austin1serb/agents-md`\](https://github.com/austin1serb/agents-md) patterns repo, and the official Codex subagent amplification issue \[`openai/codex#33196`\](https://github.com/openai/codex/issues/33196).

If you want, next I can give you a **fully optimized ~40-line root `AGENTS.md` + a separate `frontend/AGENTS.md` specifically for your UI redesign work**, which would be much better than the large file we created earlier.

## User

lets do it not just for ui redesign work, now i want to setup everything one time for every project and upcomming once also, so tets start with root agents.md and them think of all the possible ways to creat a nested agents.md. use this screenshot from my whoburnedmore dashboard to get idea

## Assistant

Worked for 7s

## Assistant

Yes. We should make this a **one-time Codex context architecture**, not a UI-redesign-specific prompt.

Your WhoBurnedMore screenshot is useful because it shows where the real burn is happening:

- `exec` ≈ **176M tokens**
- `Bash` ≈ **76.5M**
- `Edit` ≈ **69.8M**
- `Read` ≈ **58.2M**
- `TaskUpdate` ≈ **27.3M**
- `Write` ≈ **26.7M**
- `PowerShell` ≈ **20.3M**
- `Grep` ≈ **19.7M**
- skills alone include roughly **9M + 5.2M + 4.2M** for your top three

So our main objective is not merely “write shorter prompts.” We need to reduce **what Codex reads, what command output enters context, how many agent loops occur, and how much instruction/skill context gets injected**.

OpenAI's current guidance also favors starting with the smallest useful instruction set, giving explicit stopping conditions, calibrating testing, and avoiding unnecessarily large persistent instruction files. citeturn459698search0turn459698search3

## Architecture I recommend

Instead of:

```text
PROJECT/
└── AGENTS.md ← huge file containing everything
```

use:

```text
PROJECT/
│
├── AGENTS.md # tiny universal project rules
│
├── frontend/
│ └── AGENTS.md # only if frontend exists
│
├── backend/
│ └── AGENTS.md # only if backend exists
│
├── mobile/
│ └── AGENTS.md # React Native / Flutter etc.
│
├── api/
│ └── AGENTS.md # if API is separate
│
├── ai/
│ └── AGENTS.md # LLM / RAG / agents / ML
│
├── data/
│ └── AGENTS.md # datasets / ETL / migrations
│
├── tests/
│ └── AGENTS.md
│
├── scripts/
│ └── AGENTS.md
│
└── infrastructure/
 └── AGENTS.md
```

You **do not create all of these in every project**.

You create only the nested files that correspond to real areas of that repository.

That is the key idea.

# 1. Universal root `AGENTS.md`

I would make your root file around this size:

```md
# AGENTS.md

## Goal

Complete the requested task correctly with the minimum necessary context,
tool calls, edits, and diff size.

Prefer:

SEARCH → READ MINIMUM CONTEXT → PLAN → EDIT → VALIDATE → STOP.

Correctness and maintainability outrank token savings.

## Scope

Work only on files relevant to the current task.

Do not perform repository-wide exploration unless the task requires it.

Preserve existing architecture, APIs, behavior, and conventions unless
changing them is necessary for the requested work.

## Context Discipline

Search before opening files.

Prefer targeted search (`rg`, `git grep`, symbol/reference lookup) over
reading directories or large files broadly.

Read only the relevant sections of large files.

Do not reread unchanged content unless new evidence makes it necessary.

Do not dump large logs, JSON, generated files, dependency trees, or command
output into context.

For unknown-size command output, filter it or byte-cap it first.

Examples:

COMMAND 2>&1 | head -c 4000
COMMAND 2>&1 | tail -c 4000

Increase the cap only when the missing output is required.

## Editing

Prefer:

small patch > targeted refactor > rewrite

Do not rewrite working code merely to match a preferred style.

Avoid unrelated formatting, renames, import churn, and generated-file changes.

Batch closely related changes when practical, but do not force a one-edit rule.

## Tools

Use the fewest tools necessary to solve the task.

Do not repeatedly run equivalent searches, builds, status checks, or tests.

Use installed skills/MCP tools only when they add unique value to the task.

Do not invoke overlapping skills merely because they are available.

## Subagents

Do not spawn subagents by default.

Use them only when independent parallel work is substantial enough to reduce
total work or materially improve correctness.

Prefer one focused subagent over several overlapping agents.

Do not delegate simple inspection, CSS edits, small refactors, or routine tests.

## Validation

Validate proportionally to the change.

Run targeted checks first.

Broaden to full lint/typecheck/tests/build only when the affected scope or
repository requirements justify it.

Do not rerun successful expensive checks unless code affecting them changed.

## Git

Treat `git status`, `git diff --stat`, and `git diff` as the source of truth.

Do not infer repeated edits from duplicated Review UI entries.

Do not overwrite unrelated user changes.

Before completion, remove accidental or unrelated changes.

## Communication

Keep routine narration minimal.

Report only important findings, decisions, blockers, validation failures,
and the final result.

Do not restate information already established in the session.

## Stop Condition

Stop when:

- the requested behavior is implemented
- relevant validation passes
- no known regression remains
- the diff is focused
- no requested work remains

Do not invent extra improvements after the task is complete.
```

That should be your **default root template for essentially every coding project**.

It is intentionally boring.

That is good.

You don't want the model spending thousands of tokens rereading a philosophy essay about token efficiency.

# 2. Why nested `AGENTS.md` is the important part

The root should describe **how Codex works**.

Nested files should describe **how that area of the repository works**.

For example:

```text
root AGENTS.md
 ↓
"be efficient, preserve architecture, validate appropriately"

frontend/AGENTS.md
 ↓
"this is React + Tailwind; preserve API contracts;
use our design tokens; follow accessibility rules"

backend/AGENTS.md
 ↓
"this is FastAPI; keep route/service/repository boundaries;
don't alter response schemas"

ai/AGENTS.md
 ↓
"retrieval/generation contracts, evaluation requirements,
prompt/versioning rules"
```

That prevents frontend-specific instructions from entering context while Codex is fixing a database migration.

OpenAI specifically recommends controlling injected context by using nested `AGENTS.md` files for larger projects. citeturn459698search3

# 3. Nested files I would support

Don't think of these as mandatory directories. Think of them as **templates that become available when a project needs them**.

| Nested file | When to create it |
|---|---|
| `frontend/AGENTS.md` | React, Next, Vue, web UI |
| `backend/AGENTS.md` | FastAPI, Django, Express, Spring etc. |
| `mobile/AGENTS.md` | React Native, Flutter, native mobile |
| `desktop/AGENTS.md` | Electron, Tauri, native desktop |
| `api/AGENTS.md` | Separate API package/contracts |
| `ai/AGENTS.md` | LLM, agents, prompts, RAG |
| `ml/AGENTS.md` | training/evaluation/features/models |
| `data/AGENTS.md` | ETL, schemas, pipelines, datasets |
| `db/AGENTS.md` | SQL/migrations/database rules |
| `tests/AGENTS.md` | unusual testing conventions |
| `scripts/AGENTS.md` | operational scripts/automation |
| `infra/AGENTS.md` | Docker, Terraform, cloud |
| `docs/AGENTS.md` | documentation-heavy projects |
| `packages/*/AGENTS.md` | large monorepos with distinct packages |

You can go even more specific where the repository genuinely warrants it:

```text
frontend/
├── AGENTS.md
├── components/
│ └── AGENTS.md
└── e2e/
 └── AGENTS.md
```

But **only do this when rules actually differ**.

Otherwise you're recreating the context problem with 20 instruction files.

# 4. Frontend template

Your generic reusable `frontend/AGENTS.md` could be:

```md
# Frontend Instructions

Applies only to frontend work.

## Preserve

Do not change backend contracts, authentication flows, routes, or business
logic merely for UI work.

Reuse the project's existing framework, component system, styling approach,
and dependencies unless there is a strong reason not to.

## UI Quality

Prefer deliberate, product-quality interfaces over generic generated UI.

Avoid unnecessary:
- gradients
- glassmorphism
- excessive rounded cards
- decorative glows
- giant hero text
- excessive pills
- animations without interaction value

Use typography, spacing, hierarchy, and restrained surfaces before adding
additional decoration.

## Components

Reuse existing components before creating new ones.

Create shared abstractions only when there is meaningful repeated behavior
or styling.

Do not split components into trivial wrappers merely for abstraction.

## CSS

Search existing styles and tokens before adding new rules.

Modify canonical definitions rather than stacking overrides where practical.

Do not use global stylesheets as an experimentation log.

## Responsive Design

Verify affected screens at mobile and desktop widths.

Avoid horizontal overflow, clipped controls, tiny touch targets, and layouts
that simply collapse without deliberate mobile hierarchy.

## Accessibility

Preserve semantic HTML, labels, keyboard access, focus states, accessible
contrast, and appropriate ARIA usage.

## Validation

For visual changes, inspect the rendered result when browser tooling is
available.

Run only the frontend checks relevant to the affected code before broader
validation.
```

Notice how much shorter this is than our original redesign mega-prompt.

# 5. Backend template

```md
# Backend Instructions

Applies only to backend work.

Preserve existing API contracts unless the requested task requires a contract
change.

Follow the repository's existing layering and dependency direction.

Do not introduce new architectural layers for small features.

Keep validation, authorization, business logic, and persistence concerns in
their existing locations.

Search callers before changing public functions, schemas, routes, events,
or database behavior.

Do not silently change response shapes, status codes, error semantics, or
configuration defaults.

Prefer targeted fixes over framework or architecture rewrites.

For database changes, inspect migrations and compatibility implications before
changing schema behavior.

Validate with the smallest relevant tests first, then broader backend checks
when warranted.
```

# 6. AI / RAG template

This one will be particularly useful for your projects.

```md
# AI / LLM Instructions

Applies to LLM, agent, retrieval, embedding, prompt, and evaluation code.

Do not replace a deterministic implementation with an LLM unless the task
requires it.

Preserve model/provider abstraction boundaries already used by the project.

Do not hard-code secrets, API keys, model credentials, or environment-specific
URLs.

Keep prompts centralized/versioned according to existing repository conventions.

For RAG changes, distinguish:
- ingestion
- chunking
- embedding
- indexing
- retrieval
- reranking
- generation
- evaluation

Change only the stages relevant to the task.

Do not increase context size, retrieved chunk count, or model calls without
justification.

Prefer retrieval precision and targeted context over blindly supplying more
documents to the model.

For agent workflows, minimize unnecessary model turns and tool loops.

Do not introduce multi-agent architecture when one agent or deterministic
workflow is sufficient.

When behavior changes, evaluate the affected path with representative examples
rather than relying solely on implementation correctness.
```

That aligns very well with the type of RAG/agent systems you're building. memcite

# 7. Tests template

Your screenshot shows `TaskUpdate`, `exec`, `Bash`, `Read`, etc. eating enormous amounts of context. Tests can contribute heavily when Codex repeatedly dumps full suites.

So:

```md
# Test Instructions

Run the smallest test scope that can validate the current change.

Prefer:
1. affected test
2. affected package/module tests
3. full suite only when warranted

Do not repeatedly run an unchanged successful full suite.

When test output is large, capture or filter only the failing/relevant portion.

Do not add tests that merely duplicate implementation details.

Add or update tests when behavior, contracts, regressions, or important edge
cases require coverage.

Fix the implementation before weakening or deleting a valid failing test.
```

# 8. Scripts / shell template

This is directly motivated by your dashboard.

`exec + Bash + PowerShell + Grep` account for hundreds of millions of observed tokens.

```md
# Script and Shell Instructions

Assume command output may be large until proven otherwise.

Search/filter output before displaying it.

For unknown-size output, use byte caps such as:

COMMAND 2>&1 | head -c 4000
COMMAND 2>&1 | tail -c 4000

Prefer targeted commands over recursive broad output.

Avoid:
- full dependency dumps
- complete logs
- recursive directory listings of large trees
- large JSON output
- full git history
- unfiltered test logs

Use `rg`, `find`, file globs, structured query flags, and targeted ranges.

Do not repeatedly execute equivalent diagnostic commands.

Do not modify user machine configuration unless the task explicitly requires it.
```

This may be one of your highest-value templates.

The open-source `agents-md` project we found uses essentially this same concept and specifically argues for **byte caps rather than line caps**, because one minified line can still flood the model's context.

# 9. Infrastructure template

```md
# Infrastructure Instructions

Applies to Docker, CI/CD, cloud, deployment, and infrastructure files.

Do not change production infrastructure while solving a local-development issue
unless necessary.

Preserve existing deployment topology unless the requested task changes it.

Never commit credentials, tokens, private keys, or environment secrets.

Inspect existing environment variables and deployment assumptions before adding
new configuration.

Prefer minimal changes to Dockerfiles, workflows, Terraform, or deployment
configuration.

Validate syntax/configuration using targeted tooling before attempting broad
deployment actions.

Do not perform destructive infrastructure operations without explicit user
approval.
```

# 10. Monorepo strategy

For a project like:

```text
my-product/
├── apps/
│ ├── web/
│ ├── mobile/
│ └── admin/
├── services/
│ ├── api/
│ └── worker/
├── packages/
│ ├── ui/
│ └── shared/
└── infra/
```

I would use:

```text
my-product/
├── AGENTS.md
│
├── apps/
│ ├── web/
│ │ └── AGENTS.md
│ ├── mobile/
│ │ └── AGENTS.md
│ └── admin/
│ └── AGENTS.md # only if materially different from web
│
├── services/
│ ├── api/
│ │ └── AGENTS.md
│ └── worker/
│ └── AGENTS.md # only if worker rules differ substantially
│
├── packages/
│ └── ui/
│ └── AGENTS.md
│
└── infra/
 └── AGENTS.md
```

Not:

```text
every-folder/
└── AGENTS.md
```

That would defeat the purpose.

# 11. Rules for whether to create a nested file

Use this decision test:

```text
Does this subtree have rules that:
 A. are important,
 AND
 B. differ from root,
 AND
 C. apply repeatedly to that subtree?
 |
 YES → nested AGENTS.md
 NO → don't create one
```

Good nested rule:

> API response schemas are public contracts; don't alter them without updating clients.

Bad nested rule:

> Write clean code.

That belongs nowhere because it's generic noise.

# 12. Skills are another big source of your burn

Your screenshot is particularly revealing:

```text
impeccable ~9.0M
doctor ~5.2M
frontend_design ~4.2M
systematic debugging ~63K
```

This suggests we should also establish a **skill-selection policy globally**.

Add this to root:

```md
## Skill Selection

Do not load or invoke a skill merely because its topic loosely matches the task.

Use a skill only when its specialized instructions materially improve the work.

For overlapping skills, choose the single best match first.

Add a second skill only when it provides a distinct capability not already
covered.

For routine edits, prefer no skill over loading a large unnecessary skill.
```

For a frontend redesign:

```text
Redesign Existing Projects
```

might be enough initially.

You do **not** necessarily need:

```text
Redesign Existing Projects
+ Design Taste Frontend
+ High End Visual Design
+ Minimalist UI
+ Imagegen Frontend Web
+ Web Design Guidelines
+ Vercel React Best Practices
+ ...
```

all entering one job.

That's exactly the kind of context multiplication we want to stop.

# 13. A very important rule for agents/subagents

Your previous screenshot showed four threads, and current OpenAI guidance explicitly says delegation behavior should be tuned rather than left implicit. citeturn459698search0

I'd add:

```md
## Delegation Budget

Default subagent budget: 0.

Use 1 subagent when a clearly independent task would otherwise require
substantial additional exploration by the parent.

Use 2+ only for genuinely independent, substantial workstreams.

Do not create subagents for:
- simple repository exploration
- routine code review
- CSS changes
- test execution
- formatting
- small debugging tasks

A subagent should receive the smallest task-specific context needed rather than
the entire parent investigation whenever the tooling supports that.
```

That is much better than saying simply “use subagents sparingly.”

# 14. What I would NOT put in `AGENTS.md`

This matters just as much.

Don't put:

- full repository architecture
- long product requirements
- huge design guidelines
- coding-language tutorials
- README content
- complete API documentation
- every known edge case
- current TODO list
- temporary task context
- screenshots
- whole schemas
- long examples
- repeated style instructions

Those belong in actual project docs.

The agent can search/read them **when needed**.

Think of `AGENTS.md` as:

> routing + behavior rules

not:

> repository encyclopedia

# 15. The full system I'd set up for every future repo

Eventually I'd make a reusable folder on your machine:

```text
codex-agent-templates/
│
├── root.md
├── frontend.md
├── backend.md
├── mobile.md
├── desktop.md
├── ai.md
├── data.md
├── database.md
├── tests.md
├── scripts.md
└── infrastructure.md
```

Then for a new project:

```text
React + FastAPI + RAG
```

you copy:

```text
root.md
 → ./AGENTS.md

frontend.md
 → ./frontend/AGENTS.md

backend.md
 → ./backend/AGENTS.md

ai.md
 → ./ai/AGENTS.md
```

Nothing else.

For Audora:

```text
./AGENTS.md
./frontend/AGENTS.md
./backend/AGENTS.md
./desktop/AGENTS.md
```

For EchoQuery:

```text
./AGENTS.md
./01-backend-api/AGENTS.md
./03-ai-rag-engine/AGENTS.md
./05-data/AGENTS.md
./08-infrastructure/AGENTS.md
```

For your GST project:

```text
./AGENTS.md
./mobile/AGENTS.md
./desktop/AGENTS.md
./backend/AGENTS.md
./ai-document-processing/AGENTS.md
```

So the structure follows **actual architecture**, not some universal folder convention. memcite

## Where we should go next

I would build this in three stages:

```text
Stage 1
Universal root AGENTS.md
 ↓
Stage 2
Reusable nested AGENTS.md template library
 ↓
Stage 3
Codex config.toml optimization
- reasoning defaults
- context/compaction
- MCP activation
- subagent behavior
- command/tool-output limits
```

The `AGENTS.md` architecture will reduce unnecessary instruction/context injection, but based on your WhoBurnedMore numbers, **`config.toml`, active MCP/skills, subagent policy, and shell-output discipline will probably produce an even larger reduction**.

So yes: the root file above is what I would standardize first, and then we can build the nested template library around it rather than continuing to append more rules to one giant `AGENTS.md`.

## User

ok i have now standardized root agents.md, next step

## Assistant

Worked for a couple of seconds

## Assistant

Next step: **standardize the nested `AGENTS.md` template library**.

I’d do it in this order so we don’t optimize blindly:

1. `frontend/AGENTS.md`
2. `backend/AGENTS.md`
3. `ai/AGENTS.md`
4. `tests/AGENTS.md`
5. `scripts/AGENTS.md`
6. `data/AGENTS.md`
7. `infra/AGENTS.md`
8. `mobile/AGENTS.md`
9. `desktop/AGENTS.md`
10. optional `db/AGENTS.md`

The rule is: **only copy a nested file into a repo when that subtree actually exists and needs different instructions**.

Let’s start with the most reusable three. Save these as templates somewhere like:

```text
C:\Users\ASUS\.codex\agent-templates\
├── frontend.md
├── backend.md
├── ai.md
├── tests.md
├── scripts.md
├── data.md
├── infra.md
├── mobile.md
└── desktop.md
```

### `frontend.md`

```md
# Frontend Instructions

Applies only to frontend work.

## Scope

Preserve existing routes, API contracts, authentication, business logic,
state behavior, and working user flows unless the task requires changing them.

Reuse the project's existing framework, component system, styling approach,
and dependencies whenever practical.

## Context

Search before reading broadly.

Locate:
- affected component
- imports
- styles/tokens it consumes
- callers/parents
- relevant tests

Do not audit the entire frontend for a local task.

## UI

Prefer intentional, product-quality interfaces.

Avoid unnecessary:
- gradients
- glassmorphism
- decorative glow
- excessive rounded cards
- excessive pills
- giant headings
- decorative animation
- generic SaaS-template patterns

Prefer hierarchy through typography, spacing, alignment, and restrained surfaces.

## Components

Reuse existing components before creating new ones.

Create abstractions only when they remove meaningful duplication or establish
a real shared contract.

Do not create trivial wrapper components.

## Styling

Search existing tokens/classes before adding styles.

Prefer modifying canonical definitions over stacking overrides.

Do not use global CSS as an experimentation log.

Do not introduce a new styling/UI framework unless required.

## Responsive + Accessibility

Check affected views at mobile and desktop widths.

Avoid overflow, clipping, tiny touch targets, and desktop-only assumptions.

Preserve semantic HTML, labels, keyboard access, focus states, accessible
contrast, and appropriate ARIA behavior.

## Validation

For visual work, inspect the rendered result when browser tooling is available.

Run targeted frontend checks first.
Only broaden validation when the affected scope requires it.
```

### `backend.md`

```md
# Backend Instructions

Applies only to backend work.

## Scope

Preserve existing API contracts, status codes, response schemas, authentication,
authorization, and persistence behavior unless the task requires a change.

Follow the repository's existing layering and dependency direction.

Do not redesign backend architecture for a local feature or bug fix.

## Context

Search callers and references before changing:
- routes
- schemas
- public functions
- events
- configuration
- database behavior

Read only the relevant implementation path.

## Implementation

Prefer:
small fix > targeted refactor > architecture change

Keep validation, business logic, persistence, and transport concerns in their
existing layers unless there is a concrete reason to move them.

Do not silently change public behavior.

Avoid new dependencies when existing utilities are sufficient.

## Database

Before schema or persistence changes, inspect:
- migrations
- callers
- compatibility implications
- existing constraints

Do not alter production data behavior casually.

## Validation

Run the smallest relevant backend test scope first.

Broaden to full tests/typecheck/build only when warranted.
```

### `ai.md`

```md
# AI / LLM Instructions

Applies to LLM, agent, RAG, embedding, retrieval, prompt, and model code.

## Scope

Do not replace deterministic logic with an LLM unless required.

Preserve existing provider/model abstraction boundaries.

Never hard-code API keys, credentials, secrets, or environment-specific URLs.

## Context Efficiency

Minimize model calls, retrieved context, tool loops, and unnecessary prompt size.

Do not increase:
- retrieved chunk count
- context size
- agent turns
- model count
- tool calls

without a concrete quality reason.

Prefer relevant context over more context.

## RAG

Treat these as separate stages:

- ingestion
- parsing
- chunking
- embedding
- indexing
- retrieval
- reranking
- generation
- evaluation

Change only the stages relevant to the task.

Search dependencies before altering shared retrieval or indexing contracts.

## Agents

Prefer deterministic workflows or one agent when sufficient.

Do not introduce multi-agent architecture merely because it is available.

Use subagents only when independent work materially reduces total work or
improves correctness.

Avoid recursive agent/tool loops without explicit bounds.

## Prompts

Keep prompts centralized according to project conventions.

Avoid duplicating large prompts across files.

Preserve prompt/version compatibility when relevant.

## Evaluation

For behavior changes, test representative examples.

Do not rely only on successful execution to claim AI quality improved.

Measure the affected behavior where practical.
```

The **next highest-value template after these is `scripts/AGENTS.md`**, because your WhoBurnedMore dashboard showed shell/tool activity (`exec`, Bash, PowerShell, Grep) as your biggest consumption source. That one should aggressively control command-output size. memcite

After the nested templates are standardized, we should move to the more impactful part:

**`config.toml` optimization → active MCP policy → skill policy → subagent configuration → compaction/context settings.**

## User

ok give me .md for :
The next highest-value template after these is scripts/AGENTS.md, because your WhoBurnedMore dashboard showed shell/tool activity (exec, Bash, PowerShell, Grep) as your biggest consumption source. That one should aggressively control command-output size.

## Assistant

Worked for 4s

## Assistant

Here’s a compact `scripts/AGENTS.md` optimized specifically for shell/tool efficiency:

```md
# Scripts / Shell Instructions

Applies to shell scripts, CLI tasks, automation, diagnostics, build commands,
PowerShell, Bash, and repository inspection commands.

## Primary Goal

Minimize unnecessary command execution and command-output context.

Prefer:

TARGETED COMMAND → SMALL OUTPUT → ACT → VALIDATE

Avoid:

BROAD COMMAND → HUGE OUTPUT → FILTER LATER

## Command Output Limits

Assume unknown command output may be large.

For potentially large output, cap by bytes:

```bash
COMMAND 2>&1 | head -c 4000
```

For recent logs/errors:

```bash
COMMAND 2>&1 | tail -c 4000
```

On PowerShell, prefer targeted selection/filtering instead of printing entire
objects or files.

Increase output limits only when the omitted data is actually required.

## Search Before Dumping

Prefer targeted search tools such as:

```bash
rg "pattern"
git grep "pattern"
find .
```

with appropriate path filters.

Do not dump:

- entire large files
- recursive directory trees
- full dependency graphs
- complete build logs
- complete test logs
- large JSON payloads
- full git history
- generated bundles
- lockfiles
- minified output

unless explicitly required.

## Read Small Regions

When inspecting files from the shell, read only the relevant portion.

Prefer:

```bash
sed -n '120,180p' file
```

or equivalent targeted commands.

Do not repeatedly print the same unchanged file or section.

## Command Efficiency

Do not repeatedly execute equivalent commands.

Avoid loops such as:

```text
git status
git diff
git status
git diff
git status
```

Use diagnostics at meaningful checkpoints.

Do not rerun expensive commands when nothing relevant changed.

## Git

Use targeted git inspection.

Prefer:

```bash
git status --short
git diff --stat
git diff -- path/to/file
git log -n 10 --oneline
```

over broad history or repository-wide dumps.

Use the smallest git command that answers the question.

## Tests

Run the narrowest useful test first.

Prefer:

1. affected test
2. affected module/package
3. full suite only when needed

For noisy failures, filter or tail output instead of injecting the entire log.

Do not repeatedly rerun an unchanged failing test without changing the suspected
cause or diagnostic strategy.

## Build Output

Do not stream verbose builds into context unless needed.

Prefer quiet/non-verbose modes where available.

If a build fails, capture the relevant error section only.

## JSON and Structured Output

Use query/filter options before printing structured data.

Prefer tools such as:

```bash
jq '.relevant.field'
```

or CLI-specific filtering flags.

Do not print large API responses or configuration objects when only one field is
needed.

## Processes

Do not repeatedly poll long-running commands at very short intervals.

Use reasonable waits and inspect status only when useful.

Avoid unnecessary background processes.

Terminate temporary processes when they are no longer required.

## Dependencies

Do not run package installation unless dependencies are missing or changed.

Do not reinstall packages just to ensure they exist.

Avoid dependency-tree commands unless resolving a dependency issue.

## System Changes

Do not modify:

- global environment variables
- shell profiles
- PATH
- system services
- package managers
- machine-wide configuration

unless the task explicitly requires it.

Prefer project-local configuration.

## Safety

Before destructive commands, verify scope.

Do not execute commands equivalent to:

- recursive deletion
- destructive database operations
- force resets
- broad file replacement

unless explicitly required and safe.

## Stop Condition

Stop running diagnostics once the necessary evidence has been obtained.

Before every shell/tool call ask:

1. What exact question will this command answer?
2. Can a narrower command answer it?
3. Can I reduce its output before it reaches context?
4. Have I already obtained this information?
```

This one should be especially useful given your `exec`, `Bash`, `PowerShell`, and `Grep` usage profile. memcite

## User

dit this until now

## Assistant

Good — you now have the four most important reusable templates in place:

- `frontend.md`
- `backend.md`
- `ai.md`
- `scripts.md`

That’s a solid base.

Next, I’d add these in this order:

```text
tests.md
data.md
infra.md
mobile.md
desktop.md
```

Then stop. Don’t add more unless a real project needs them.

The next one should be **`tests.md`**, because test execution/output can also become a major hidden token sink. After that, `data.md` and `infra.md` are broadly reusable.

Your template library should eventually look like:

```text
C:\Users\ASUS\.codex\agent-templates\
├── frontend.md
├── backend.md
├── ai.md
├── scripts.md
├── tests.md
├── data.md
├── infra.md
├── mobile.md
└── desktop.md
```

Then we move to the more impactful system-level work: **`config.toml` optimization, MCP/tool activation policy, skills policy, subagent limits, and compaction settings**.

## User

give appropriate tests.md

## Assistant

```md
# Tests Instructions

Applies to unit, integration, end-to-end, regression, snapshot, contract,
and other automated test work.

## Primary Goal

Validate the requested behavior with the smallest reliable test scope.

Prefer:

AFFECTED TEST → AFFECTED MODULE → BROADER SUITE → FULL SUITE ONLY WHEN NEEDED

Do not use the full test suite as the default first diagnostic step.

## Test Scope

Before running tests, identify the code path that changed.

Prefer the narrowest command that can validate it.

Examples:

- single test file
- single test case
- affected package/module
- related integration suite
- full repository suite only when justified

Do not repeatedly run unrelated tests.

## Output Discipline

Test output can consume large amounts of context.

Do not inject complete noisy test logs when only a small failure section matters.

For potentially large output, filter or cap it.

Examples:

```bash
COMMAND 2>&1 | tail -c 6000
```

or search for relevant failure markers:

```bash
COMMAND 2>&1 | rg -C 5 "FAIL|ERROR|AssertionError|Expected|Actual"
```

Use larger output only when the missing context is required to diagnose the failure.

## Failure Diagnosis

When a test fails:

1. identify the first meaningful failure
2. inspect the relevant implementation and test
3. determine the root cause
4. change the implementation or test only when justified
5. rerun the smallest relevant test

Do not blindly patch multiple failures at once.

Do not repeatedly rerun the same failing command without changing either:
- the suspected cause
- the code
- the diagnostic strategy

## Existing Tests

Treat existing valid tests as behavioral evidence.

Do not:
- weaken assertions to make a failure disappear
- delete valid tests because implementation changed unexpectedly
- replace precise assertions with vague ones without reason
- update snapshots blindly

If an existing test is incorrect or outdated, explain why before changing it.

## New Tests

Add tests when the change introduces or fixes:

- user-visible behavior
- API or contract behavior
- regression-prone logic
- meaningful edge cases
- failure handling
- security-sensitive behavior
- previously uncovered bug paths

Do not add tests merely to increase coverage numbers.

Avoid tests that only duplicate implementation details.

## Test Design

Prefer tests that validate observable behavior.

Avoid excessive mocking when a simpler realistic test is available.

Mock external systems only when needed for:
- determinism
- speed
- isolation
- unavailable services
- destructive side effects

Do not mock the exact implementation being tested.

## Regression Fixes

For a bug fix, prefer:

1. reproduce the bug with a focused test
2. confirm the test fails for the expected reason
3. implement the fix
4. confirm the focused test passes
5. run nearby regression tests

Do not write a regression test that cannot fail on the broken implementation.

## Integration Tests

Use integration tests when correctness depends on interactions between components.

Do not escalate to integration or end-to-end tests when a unit test proves the behavior adequately.

When integration tests require databases, services, containers, or network access,
reuse existing project infrastructure rather than creating unnecessary new setup.

## End-to-End Tests

E2E tests are expensive.

Run them only when:
- the changed workflow crosses multiple system boundaries
- frontend/backend integration matters
- a critical user journey changed
- repository policy requires them

Prefer the affected scenario over the entire E2E suite.

## Snapshots

Do not update snapshots automatically just because they changed.

Inspect the diff first.

Update snapshots only when the new output is intentional and correct.

Avoid large snapshots when targeted assertions are clearer.

## Flaky Tests

Do not hide flaky behavior with repeated retries unless retry behavior is an established project convention.

When a test appears flaky:

1. verify reproducibility
2. inspect timing/state/shared-resource causes
3. identify nondeterminism
4. fix the root cause where practical

Do not mark a test skipped merely to make CI green without justification.

## Performance

Do not run expensive benchmarks or load tests for unrelated changes.

When performance is part of the task, use representative targeted measurements.

Avoid drawing conclusions from a single noisy run.

## Test Data

Use the smallest representative fixtures necessary.

Avoid loading large datasets when a minimal fixture proves the behavior.

Do not duplicate large fixtures across tests.

Prefer shared fixtures/builders when they materially reduce repetition.

## Coverage

Coverage is a signal, not the objective.

Do not modify production code solely to satisfy arbitrary coverage percentages unless project policy requires it.

Focus coverage on meaningful behavior and important branches.

## Environment

Before installing or starting test infrastructure, check whether it already exists.

Do not repeatedly:
- reinstall dependencies
- recreate containers
- reseed databases
- restart services

unless required by the current test state.

Clean up temporary test resources when needed.

## Validation Sequence

Use this order by default:

1. focused failing/affected test
2. related tests
3. typecheck/lint if relevant
4. broader package/module tests
5. full suite only when warranted

If a broad test already passed and no relevant code changed afterward, do not rerun it.

## Reporting

Keep test reporting concise.

Report:
- command or scope tested
- pass/fail
- meaningful failing tests
- root cause if known
- any tests not run and why

Do not paste full successful logs.

## Stop Condition

Stop testing when:

- the changed behavior is covered appropriately
- relevant tests pass
- no nearby regression is indicated
- broader validation has been run when justified

Before every test command ask:

1. What exact risk does this test validate?
2. Is there a narrower test that answers the same question?
3. Can I reduce its output before it enters context?
4. Has this test already passed since the last relevant code change?
```

This is the version I’d standardize as `C:\Users\ASUS\.codex\agent-templates\tests.md`.

## User

this much big test.md defeats whole purpose of usage limit optimization

## Assistant

You're right. For nested `AGENTS.md`, this should be **tiny and high-signal**.

Use this instead:

```md
# Tests

Applies only to test work.

- Run the narrowest relevant test first.
- Prefer: single test → module/package → full suite only if justified.
- Do not rerun unchanged successful tests.
- Do not dump full noisy logs into context; filter or tail failures.
- For large output, cap it, e.g.:
 `COMMAND 2>&1 | tail -c 6000`
- Fix root causes; do not weaken valid assertions just to make tests pass.
- Add regression tests only for meaningful behavior/bugs.
- Do not blindly update snapshots.
- Avoid unnecessary mocks, fixtures, containers, and dependency reinstalls.
- Stop once relevant behavior is validated and no nearby regression is indicated.
```

This is much more aligned with the actual goal: **nested files should be compact routing constraints, not mini handbooks**.

## User

done

## Assistant

Worked for a couple of seconds

## Assistant

Great. Next I’d add **`data.md`**, but keep it just as compact as `tests.md`.

After that: `infra.md`, `mobile.md`, `desktop.md`, then we stop adding templates and move to **Codex `config.toml` optimization**, which is likely to save more usage than adding more `AGENTS.md` rules.

## User

lets do this

## Assistant

Worked for 5s

## Assistant

Good. For `config.toml`, I’d optimize **conservatively** first. The current Codex source exposes settings for `tool_output_token_limit`, subagent defaults, max subagent threads, context window, and auto-compaction. citeturn928218search0

Given your WhoBurnedMore usage, the biggest targets are:

- shell/tool output entering context
- too many subagents
- subagents using expensive reasoning
- long sessions with large active context
- unnecessary verbosity

I’d start with this baseline in `C:\Users\ASUS\.codex\config.toml`:

```toml
# ============================================================
# Codex — Usage-Efficient Global Defaults
# ============================================================

# Keep routine work efficient.
model_reasoning_effort = "medium"
model_verbosity = "low"

# Limit how much individual tool output is retained in model context.
# This is NOT the model's response-output limit.
tool_output_token_limit = 12000

# Compact before context becomes extremely large.
# We should tune these further based on the model you actually use.
model_context_window = 258000
model_auto_compact_token_limit = 180000

# ============================================================
# Subagents
# ============================================================

\[agents\]
enabled = true

# Prevent agent swarms.
max_concurrent_threads_per_session = 2

# Make workers cheaper than the parent by default.
default_subagent_model = "gpt-5.6-terra"
default_subagent_reasoning_effort = "medium"
```

### Why these settings

**`model_verbosity = "low"`** 
This reduces unnecessary textual output. Codex's config schema currently supports `low`, `medium`, and `high`. citeturn928218search8

**`tool_output_token_limit = 12000`** 
This is probably the single most interesting setting for your dashboard. Codex's current source explicitly describes it as the token budget used when storing tool/function outputs in the context manager. citeturn928218search0

You had huge usage from `exec`, Bash, Read, PowerShell and Grep, so I would not leave tool-result retention unconstrained.

I would start at:

```toml
tool_output_token_limit = 12000
```

rather than something extreme like `4000`, because debugging/build failures sometimes legitimately require several thousand tokens.

Your `scripts/AGENTS.md` still asks commands to cap their own output much more aggressively. These two layers complement each other:

```text
Shell filtering / 4KB byte caps
 ↓
tool_output_token_limit = 12k
 ↓
model context
```

### Subagent limit: 2

This matters a lot.

Recent reports against Codex describe runaway multi-agent trees, including one case with **74 spawned subagents**, most running high/ultra reasoning, producing enormous accumulated token counts. citeturn928218search9

Another recent report specifically found severe amplification from parallel workers. citeturn928218search5

So:

```toml
\[agents\]
max_concurrent_threads_per_session = 2
```

is a sensible global guardrail.

I would **not disable subagents completely**, because they can genuinely help on large independent tasks.

But your default topology becomes:

```text
Parent
├── Worker A
└── Worker B
```

instead of:

```text
Parent
├── Worker
├── Worker
├── Worker
├── Worker
│ ├── Worker
│ ├── Worker
│ └── ...
└── ...
```

### Default subagent = Terra Medium

This is important if your main agent is something stronger.

```toml
default_subagent_model = "gpt-5.6-terra"
default_subagent_reasoning_effort = "medium"
```

The current Codex source exposes both of these defaults. citeturn928218search0

So architecture review or difficult coding can remain on Sol/High when you explicitly choose it, while mundane workers don't automatically inherit the most expensive configuration.

There have been version-specific bugs where registered-agent model/effort overrides were ignored and children inherited the parent configuration, so after setting this we should **verify it from an actual spawned thread**, rather than assume it worked. citeturn928218search4

### Context/compaction

Your screenshot showed:

```text
105,476 used / 258k
59% left
```

So if that **258k is genuinely your effective model context**, I'd start around:

```toml
model_context_window = 258000
model_auto_compact_token_limit = 180000
```

That means compaction around ~70% rather than dragging the conversation almost to exhaustion.

Codex currently supports these settings, and the config source recognizes them as context/compaction controls. citeturn928218search0

However, this is the part I want to verify against **your actual current config/model** before we finalize it. I don't want us hardcoding `258000` globally if you switch between models with different windows.

### One thing I would NOT enable yet

Do not start playing with experimental context-management flags, MultiAgent V2 switches, memories, custom compaction prompts, etc.

We're optimizing through stable, understandable knobs first:

```text
1. verbosity
2. tool-output retention
3. subagent concurrency
4. subagent model/effort
5. compaction threshold
```

Then measure WhoBurnedMore again.

### Expected effect

Your current major burns:

```text
exec 176M
Bash 76.5M
Edit 69.8M
Read 58.2M
TaskUpdate 27.3M
Write 26.7M
PowerShell 20.3M
Grep 19.7M
```

Our setup now attacks them from several directions:

```text
ROOT AGENTS.md
 ↓ less broad exploration

nested scripts/AGENTS.md
 ↓ smaller shell output

tool_output_token_limit
 ↓ less retained tool context

Medium reasoning default
 ↓ less reasoning spend

2 subagent ceiling
 ↓ less multiplicative usage

Terra Medium workers
 ↓ cheaper delegated work

earlier compaction
 ↓ smaller long-lived sessions
```

Before you edit anything, **paste your current `C:\Users\ASUS\.codex\config.toml` here**. You have had custom providers/OmniRoute configuration in that file before, so I want to merge these optimizations into it rather than giving you a replacement that accidentally breaks your existing provider, hooks, marketplaces, or model setup. memcite

## User

no i cant

## Assistant

Worked for a couple of seconds

## Assistant

No problem — don’t paste it here.

Safest path: **make only additive, low-risk edits** to your existing `config.toml`, one block at a time, instead of replacing the file.

Start by adding just these lines near the top-level settings:

```toml
model_reasoning_effort = "medium"
model_verbosity = "low"
tool_output_token_limit = 12000
```

Do **not** change your provider, model, hooks, marketplaces, or auth config.

Then add this only if your current Codex version accepts it:

```toml
\[agents\]
max_concurrent_threads_per_session = 2
default_subagent_reasoning_effort = "medium"
```

I would **hold off on hardcoding**:

```toml
model_context_window = ...
model_auto_compact_token_limit = ...
default_subagent_model = ...
```

until we verify the exact current schema/model behavior on your installation, because those are more version/model-sensitive and can cause unintended behavior if guessed.

So the immediate safe optimization is:

```text
Medium reasoning
+ Low verbosity
+ 12k tool-output retention
+ max 2 subagents
```

That already targets the biggest usage multipliers without risking your existing setup.

## User

model = "gpt-6-astra"
model_reasoning_effort = "medium"
model_verbosity = "low"
tool_output_token_limit = 12000
service_tier = "default"

## Assistant

That baseline looks good:

```toml
model = "gpt-6-astra"
model_reasoning_effort = "medium"
model_verbosity = "low"
tool_output_token_limit = 12000
service_tier = "default"
```

I’d keep it exactly like that for now.

Next, add only the subagent guardrail:

```toml
\[agents\]
max_concurrent_threads_per_session = 2
```

I would **not** add a default subagent model yet, since you’re on `gpt-6-astra` and we should avoid guessing whether your current Codex build supports a separate worker-model override cleanly.

So your next checkpoint should be:

```toml
model = "gpt-6-astra"
model_reasoning_effort = "medium"
model_verbosity = "low"
tool_output_token_limit = 12000
service_tier = "default"

\[agents\]
max_concurrent_threads_per_session = 2
```

After that, the next optimization I’d do is **MCP/tool activation**, because that can quietly inject a lot of schema/context into every turn even before Codex does any actual work.

## User

i dont want to use gpt for every thing

## Assistant

Then don’t make GPT-6 Astra your universal default.

A better setup is to use **profiles by task type**:

```toml
# default: cheap/routine
model = "gpt-5.6-terra"
model_reasoning_effort = "medium"
model_verbosity = "low"
tool_output_token_limit = 12000
service_tier = "default"

\[profiles.astra\]
model = "gpt-6-astra"
model_reasoning_effort = "high"

\[profiles.fast\]
model = "gpt-5.6-luna"
model_reasoning_effort = "low"

\[profiles.review\]
model = "gpt-5.6-sol"
model_reasoning_effort = "high"

\[agents\]
max_concurrent_threads_per_session = 2
```

Then use them roughly like this:

- **Luna / fast** → tiny edits, search, formatting, boilerplate, simple CSS
- **Terra / default** → normal coding, features, debugging, refactors
- **Sol / review** → code review, harder bugs, architecture
- **Astra** → only the hardest tasks where the extra capability is actually worth the quota

That is much better than burning Astra on things like `rg`, CSS tweaks, updating imports, or fixing one failing unit test.

The next thing we should configure is **automatic model selection / routing**, if your current Codex build supports a clean way to do it; otherwise profiles are the safest approach.

## User

# default: cheap/routine
model = "gpt-5.6-terra"
model_reasoning_effort = "medium"
model_verbosity = "low"
tool_output_token_limit = 12000
service_tier = "default"

\[profiles.astra\]
model = "gpt-6-astra"
model_reasoning_effort = "medium"
model_verbosity = "low"

\[profiles.fast\]
model = "gpt-5.6-luna"
model_reasoning_effort = "low"

\[profiles.review\]
model = "gpt-5.6-sol"
model_reasoning_effort = "high"

\[agents\]
max_concurrent_threads_per_session = 2

notify = \[ "C:\\Users\\ASUS\\AppData\\Local\\OpenAI\\Codex\\runtimes\\cua_node\\c2900163265bdaec\\bin\\node_modules\\@oai\\sky\\bin\\windows\\codex-computer-use.exe", "turn-ended" \]
\[projects.'c:\users\asus'\]
trust_level = "trusted"

\[projects.'d:\all programming\iq'\]
trust_level = "trusted"

\[projects.'d:\all programming\hacker_house\echoquery-rag-based-stt'\]
trust_level = "trusted"

\[projects.'d:\all programming\git_clone\audora'\]
trust_level = "trusted"

\[projects.'c:\users\asus\documents\codex\2026-08-27\realtime-voice-chat'\]
trust_level = "trusted"

\[projects.'d:\all programming\0-webdev\iq'\]
trust_level = "trusted"

\[projects.'d:\all programming\0-webdev\sih'\]
trust_level = "trusted"

\[projects.'d:\all programming\0-webdev\hacker_house\facechain'\]
trust_level = "trusted"

\[projects.'d:\all programming\0-webdev\ocr-gst'\]
trust_level = "trusted"

\[windows\]
sandbox = "elevated"

\[marketplaces.openai-bundled\]
source_type = "local"
source = '\\?\C:\Users\ASUS\.codex\.tmp\bundled-marketplaces\openai-bundled'

\[marketplaces.openai-primary-runtime\]
source_type = "local"
source = '\\?\C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\plugins\openai-primary-runtime'

\[marketplaces.claude-plugins-official\]
source_type = "local"
source = '\\?\C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official'

\[plugins."codex-app-tools@openai-bundled"\]
enabled = true

\[plugins."visualize@openai-bundled"\]
enabled = true

\[plugins."computer-use@openai-bundled"\]
enabled = true

\[plugins."documents@openai-primary-runtime"\]
enabled = true

\[plugins."pdf@openai-primary-runtime"\]
enabled = true

\[plugins."spreadsheets@openai-primary-runtime"\]
enabled = true

\[plugins."presentations@openai-primary-runtime"\]
enabled = true

\[plugins."template-creator@openai-primary-runtime"\]
enabled = true

\[plugins."chrome@openai-bundled"\]
enabled = true

\[plugins."firecrawl@claude-plugins-official"\]
enabled = true

\[plugins."frontend-design@claude-plugins-official"\]
enabled = true

\[plugins."superpowers@claude-plugins-official"\]
enabled = true

\[plugins."skill-creator@claude-plugins-official"\]
enabled = true

\[plugins."feature-dev@claude-plugins-official"\]
enabled = true

\[plugins."chrome-devtools-mcp@claude-plugins-official"\]
enabled = true

\[plugins."chrome-devtools-mcp@claude-plugins-official".mcp_servers.chrome-devtools.tools.evaluate_script\]
approval_mode = "approve"

\[plugins."browser@openai-bundled"\]
enabled = true

\[plugins."unified-computer-use@openai-bundled"\]
enabled = true

\[features\]
js_repl = false

\[mcp_servers.node_repl\]
args = \[\]
command = 'C:\Users\ASUS\AppData\Local\OpenAI\Codex\runtimes\cua_node\c2900163265bdaec\bin\node_repl.exe'
startup_timeout_sec = 120

\[mcp_servers.node_repl.env\]
NODE_REPL_NATIVE_PIPE_CONNECT_TIMEOUT_MS = "1000"
NODE_REPL_NODE_MODULE_DIRS = 'C:\Users\ASUS\AppData\Local\OpenAI\Codex\runtimes\cua_node\c2900163265bdaec\bin\node_modules'
NODE_REPL_NODE_PATH = 'C:\Users\ASUS\AppData\Local\OpenAI\Codex\runtimes\cua_node\c2900163265bdaec\bin\node.exe'
NODE_REPL_TRUSTED_CODE_PATHS = 'C:\Users\ASUS\.codex;C:\Users\ASUS\AppData\Local\OpenAI\Codex\runtimes\cua_node\c2900163265bdaec\bin\node_modules'
CODEX_HOME = 'C:\Users\ASUS\.codex'
BROWSER_USE_AVAILABLE_BACKENDS = "chrome,iab"
BROWSER_USE_TINYSKY_ENABLED = "1"
NODE_REPL_INSTRUCTIONS_USE_CASE_BROWSER = ""
NODE_REPL_INSTRUCTIONS_USE_CASE_CHROME = ""
BROWSER_USE_CODEX_APP_BUILD_FLAVOR = "prod"
BROWSER_USE_CODEX_APP_VERSION = "26.901.31953"
NODE_REPL_TRUSTED_SERVICES = '{"browser":"C:/Users/ASUS/.codex/plugins/cache/openai-bundled/browser/26.901.31953/scripts/browser-service.mjs","sky":"@oai/sky/service"}'
SKY_CUA_NATIVE_PIPE = "1"
SKY_CUA_NATIVE_PIPE_DIRECTORY = '\\.\pipe\codex-computer-use-e7270b38-1368-4ce6-ab30-8e54f6c0c4dc'
CODEX_CLI_PATH = 'C:\Users\ASUS\AppData\Local\OpenAI\Codex\bin\1e3e57cdf0634c02\codex.exe'

\[desktop\]
conversationDetailMode = "STEPS_COMMANDS"
ambient-suggestions-enabled = true
external-agent-import-sync-enabled = true
followUpQueueMode = "queue"
keepRemoteControlAwakeWhilePluggedIn = true
selected-avatar-id = "codex"
avatar-overlay-mascot-width-px = 80

## Assistant

Worked for 4s

## Assistant

This config explains a lot: you currently have **many plugins enabled globally**, so even when you’re doing a simple coding task, Codex may be carrying extra tool/skill schema/context that you don’t need. OpenAI’s own guidance recommends limiting MCP/plugin usage because each enabled integration can increase prompt/context overhead. citeturn778754search4

I’d keep your model/profile section, but change the plugin strategy from **“everything enabled globally”** to **“minimal global set + enable per project/task.”**

Your current always-on plugins include things like `visualize`, `documents`, `pdf`, `spreadsheets`, `presentations`, `template-creator`, `firecrawl`, `frontend-design`, `superpowers`, `skill-creator`, `feature-dev`, `chrome-devtools-mcp`, `browser`, and `unified-computer-use`. That’s far more than a normal coding task needs.

I’d make the global baseline only:

```toml
\[plugins."codex-app-tools@openai-bundled"\]
enabled = true

\[plugins."computer-use@openai-bundled"\]
enabled = true

\[plugins."browser@openai-bundled"\]
enabled = true
```

Then disable the rest globally:

```toml
\[plugins."visualize@openai-bundled"\]
enabled = false

\[plugins."documents@openai-primary-runtime"\]
enabled = false

\[plugins."pdf@openai-primary-runtime"\]
enabled = false

\[plugins."spreadsheets@openai-primary-runtime"\]
enabled = false

\[plugins."presentations@openai-primary-runtime"\]
enabled = false

\[plugins."template-creator@openai-primary-runtime"\]
enabled = false

\[plugins."firecrawl@claude-plugins-official"\]
enabled = false

\[plugins."frontend-design@claude-plugins-official"\]
enabled = false

\[plugins."superpowers@claude-plugins-official"\]
enabled = false

\[plugins."skill-creator@claude-plugins-official"\]
enabled = false

\[plugins."feature-dev@claude-plugins-official"\]
enabled = false

\[plugins."chrome-devtools-mcp@claude-plugins-official"\]
enabled = false

\[plugins."unified-computer-use@openai-bundled"\]
enabled = false
```

Then enable them only when needed. For example:

```text
Frontend redesign
→ frontend-design
→ maybe chrome-devtools-mcp

Web research
→ firecrawl

PDF work
→ pdf

Spreadsheet task
→ spreadsheets

Slides
→ presentations
```

Also, you currently have both:

```text
computer-use
browser
unified-computer-use
chrome
chrome-devtools-mcp
```

That is a lot of overlapping browser/computer tooling. I would avoid keeping all five active. Pick the smallest set that covers your normal workflow; typically **browser + computer-use** is enough unless a task specifically needs Chrome DevTools.

Your model routing setup itself is sensible:

```text
Terra Medium → default normal coding
Luna Low → trivial/fast work
Sol High → review/hard debugging
Astra Medium → deliberately selected difficult work
```

That matches the goal of not spending Astra on routine operations.

One more thing I’d change: keep

```toml
tool_output_token_limit = 12000
```

for now, but after a few days of WhoBurnedMore data, try **8000** if debugging quality remains fine. Your dashboard showed shell/tool output as the biggest usage source, so this setting plus `scripts/AGENTS.md` is where I expect the biggest savings.

The next optimization after plugin pruning should be **automatic per-project plugin profiles** so, for example, a frontend repo starts with frontend tools while your RAG repos start with AI/research tools—without manually toggling everything each time.

## User

ok give me config.toml

## Assistant

Worked for a few seconds

## Assistant

Use this as your cleaned-up, usage-efficient `config.toml`. It preserves your trusted projects, desktop settings, runtime paths, profiles, and notification hook while reducing globally enabled plugins.

```toml
# ============================================================
# MODEL DEFAULTS
# ============================================================

# Default model for normal coding work.
model = "gpt-5.6-terra"
model_reasoning_effort = "medium"
model_verbosity = "low"

# Limit how much individual tool output is retained in context.
tool_output_token_limit = 12000

service_tier = "default"

# ============================================================
# MODEL PROFILES
# ============================================================

# Difficult / high-value work.
\[profiles.astra\]
model = "gpt-6-astra"
model_reasoning_effort = "medium"
model_verbosity = "low"

# Cheap / routine work:
# search, tiny edits, formatting, simple CSS, boilerplate, etc.
\[profiles.fast\]
model = "gpt-5.6-luna"
model_reasoning_effort = "low"
model_verbosity = "low"

# Hard debugging, architecture review, code review.
\[profiles.review\]
model = "gpt-5.6-sol"
model_reasoning_effort = "high"
model_verbosity = "low"

# ============================================================
# SUBAGENTS
# ============================================================

\[agents\]

# Prevent unnecessary agent swarms.
max_concurrent_threads_per_session = 2

# ============================================================
# CODEX DESKTOP NOTIFICATION
# ============================================================

notify = \[
 "C:\\Users\\ASUS\\AppData\\Local\\OpenAI\\Codex\\runtimes\\cua_node\\c2900163265bdaec\\bin\\node_modules\\@oai\\sky\\bin\\windows\\codex-computer-use.exe",
 "turn-ended"
\]

# ============================================================
# TRUSTED PROJECTS
# ============================================================

\[projects.'c:\users\asus'\]
trust_level = "trusted"

\[projects.'d:\all programming\iq'\]
trust_level = "trusted"

\[projects.'d:\all programming\hacker_house\echoquery-rag-based-stt'\]
trust_level = "trusted"

\[projects.'d:\all programming\git_clone\audora'\]
trust_level = "trusted"

\[projects.'c:\users\asus\documents\codex\2026-08-27\realtime-voice-chat'\]
trust_level = "trusted"

\[projects.'d:\all programming\0-webdev\iq'\]
trust_level = "trusted"

\[projects.'d:\all programming\0-webdev\sih'\]
trust_level = "trusted"

\[projects.'d:\all programming\0-webdev\hacker_house\facechain'\]
trust_level = "trusted"

\[projects.'d:\all programming\0-webdev\ocr-gst'\]
trust_level = "trusted"

# ============================================================
# WINDOWS
# ============================================================

\[windows\]
sandbox = "elevated"

# ============================================================
# MARKETPLACES
# ============================================================

\[marketplaces.openai-bundled\]
source_type = "local"
source = '\\?\C:\Users\ASUS\.codex\.tmp\bundled-marketplaces\openai-bundled'

\[marketplaces.openai-primary-runtime\]
source_type = "local"
source = '\\?\C:\Users\ASUS\.cache\codex-runtimes\codex-primary-runtime\plugins\openai-primary-runtime'

\[marketplaces.claude-plugins-official\]
source_type = "local"
source = '\\?\C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official'

# ============================================================
# GLOBAL PLUGINS
#
# Keep the global tool surface intentionally small.
# Enable specialized plugins only when the current task needs them.
# ============================================================

\[plugins."codex-app-tools@openai-bundled"\]
enabled = true

\[plugins."computer-use@openai-bundled"\]
enabled = true

\[plugins."browser@openai-bundled"\]
enabled = true

# ============================================================
# SPECIALIZED PLUGINS — DISABLED BY DEFAULT
# ============================================================

# Visual / artifact tools

\[plugins."visualize@openai-bundled"\]
enabled = false

\[plugins."documents@openai-primary-runtime"\]
enabled = false

\[plugins."pdf@openai-primary-runtime"\]
enabled = false

\[plugins."spreadsheets@openai-primary-runtime"\]
enabled = false

\[plugins."presentations@openai-primary-runtime"\]
enabled = false

\[plugins."template-creator@openai-primary-runtime"\]
enabled = false

# Web research

\[plugins."firecrawl@claude-plugins-official"\]
enabled = false

# Frontend / development skills

\[plugins."frontend-design@claude-plugins-official"\]
enabled = false

\[plugins."superpowers@claude-plugins-official"\]
enabled = false

\[plugins."skill-creator@claude-plugins-official"\]
enabled = false

\[plugins."feature-dev@claude-plugins-official"\]
enabled = false

# Chrome DevTools — enable only when DevTools-level inspection is needed.

\[plugins."chrome-devtools-mcp@claude-plugins-official"\]
enabled = false

\[plugins."chrome-devtools-mcp@claude-plugins-official".mcp_servers.chrome-devtools.tools.evaluate_script\]
approval_mode = "approve"

# Avoid overlapping computer/browser implementations globally.

\[plugins."unified-computer-use@openai-bundled"\]
enabled = false

\[plugins."chrome@openai-bundled"\]
enabled = false

# ============================================================
# FEATURES
# ============================================================

\[features\]
js_repl = false

# ============================================================
# NODE REPL / COMPUTER USE RUNTIME
# ============================================================

\[mcp_servers.node_repl\]
args = \[\]
command = 'C:\Users\ASUS\AppData\Local\OpenAI\Codex\runtimes\cua_node\c2900163265bdaec\bin\node_repl.exe'
startup_timeout_sec = 120

\[mcp_servers.node_repl.env\]

NODE_REPL_NATIVE_PIPE_CONNECT_TIMEOUT_MS = "1000"

NODE_REPL_NODE_MODULE_DIRS = 'C:\Users\ASUS\AppData\Local\OpenAI\Codex\runtimes\cua_node\c2900163265bdaec\bin\node_modules'

NODE_REPL_NODE_PATH = 'C:\Users\ASUS\AppData\Local\OpenAI\Codex\runtimes\cua_node\c2900163265bdaec\bin\node.exe'

NODE_REPL_TRUSTED_CODE_PATHS = 'C:\Users\ASUS\.codex;C:\Users\ASUS\AppData\Local\OpenAI\Codex\runtimes\cua_node\c2900163265bdaec\bin\node_modules'

CODEX_HOME = 'C:\Users\ASUS\.codex'

BROWSER_USE_AVAILABLE_BACKENDS = "chrome,iab"
BROWSER_USE_TINYSKY_ENABLED = "1"

NODE_REPL_INSTRUCTIONS_USE_CASE_BROWSER = ""
NODE_REPL_INSTRUCTIONS_USE_CASE_CHROME = ""

BROWSER_USE_CODEX_APP_BUILD_FLAVOR = "prod"
BROWSER_USE_CODEX_APP_VERSION = "26.901.31953"

NODE_REPL_TRUSTED_SERVICES = '{"browser":"C:/Users/ASUS/.codex/plugins/cache/openai-bundled/browser/26.901.31953/scripts/browser-service.mjs","sky":"@oai/sky/service"}'

SKY_CUA_NATIVE_PIPE = "1"

SKY_CUA_NATIVE_PIPE_DIRECTORY = '\\.\pipe\codex-computer-use-e7270b38-1368-4ce6-ab30-8e54f6c0c4dc'

CODEX_CLI_PATH = 'C:\Users\ASUS\AppData\Local\OpenAI\Codex\bin\1e3e57cdf0634c02\codex.exe'

# ============================================================
# DESKTOP
# ============================================================

\[desktop\]
conversationDetailMode = "STEPS_COMMANDS"
ambient-suggestions-enabled = true
external-agent-import-sync-enabled = true
followUpQueueMode = "queue"
keepRemoteControlAwakeWhilePluggedIn = true
selected-avatar-id = "codex"
avatar-overlay-mascot-width-px = 80
```

The important change is that **installed ≠ globally enabled**. You still retain Firecrawl, frontend-design, superpowers, document/PDF tools, DevTools, etc.; they simply stop entering normal sessions unless you deliberately enable them.

Your default workflow becomes:

```text
Normal coding
→ Terra / Medium
→ minimal plugins

Tiny/routine task
→ fast profile (Luna / Low)

Hard debugging/review
→ review profile (Sol / High)

Hardest/high-value work
→ astra profile

Web research
→ temporarily enable Firecrawl

Frontend design
→ temporarily enable frontend-design
→ optionally Chrome DevTools

PDF/docs/slides
→ enable only the corresponding plugin
```

One thing I would **not touch yet** is `model_context_window` or auto-compaction. First collect another day or two of WhoBurnedMore data with this setup + your compact `AGENTS.md` files. Then we can compare the before/after burn and tune `12000 → 8000` or context compaction based on evidence rather than guessing.

## User

where is 
mcp__Claude_Browser__preview_start my most used mcp

## Assistant

Worked for 12s

## Assistant

`mcp__Claude_Browser__preview_start` is **not** coming from the `browser@openai-bundled` entry I suggested keeping. It is a **Claude Browser MCP tool**, specifically the `preview_start` tool used to open the Browser pane or start a dev-server preview. Firecrawl found it documented under Claude Desktop/Claude Code browser tooling. 

So if that is your **most-used MCP**, then disabling the Claude/browser-related integration would be a mistake for your workflow.

In your config, the closest candidates are these overlapping browser tools:

```toml
\[plugins."chrome@openai-bundled"\]
enabled = true

\[plugins."browser@openai-bundled"\]
enabled = true

\[plugins."unified-computer-use@openai-bundled"\]
enabled = true

\[plugins."chrome-devtools-mcp@claude-plugins-official"\]
enabled = true
```

But `mcp__Claude_Browser__preview_start` itself likely comes from a **Claude Browser runtime/tool injected through the desktop/browser integration**, not `chrome-devtools-mcp`.

So I would revise the optimization strategy:

```toml
# KEEP — heavily used browser workflow
\[plugins."browser@openai-bundled"\]
enabled = true

\[plugins."computer-use@openai-bundled"\]
enabled = true

# KEEP for now until we verify which one exposes Claude_Browser preview_start
\[plugins."unified-computer-use@openai-bundled"\]
enabled = true

# Optional — only if you actively use DevTools inspection
\[plugins."chrome-devtools-mcp@claude-plugins-official"\]
enabled = false

# Optional duplicate browser implementation
\[plugins."chrome@openai-bundled"\]
enabled = false
```

The important distinction is:

```text
Claude_Browser.preview_start
≈ app preview / dev-server browser workflow

chrome-devtools-mcp
≈ DOM/network/console/devtools inspection
```

Those are different use cases.

And because your WhoBurnedMore dashboard says `mcp__Claude_Browser__preview_start` is your most-used MCP, **we should optimize around it, not remove it**.

The next useful step is to identify **exactly which enabled plugin/server in your Codex installation registers `Claude_Browser`**, then we can disable the redundant browser tools safely.

## User

ok thats is thank u

## Assistant

Worked for a couple of seconds

## Assistant

You’re welcome.

## User

pop up does not appear

## Assistant

Worked for 7s

## Assistant

This looks like a **known Windows sandbox-setup bug**, not a problem with UAC itself. Several recent Codex/ChatGPT Windows reports describe the exact same behavior: clicking **“Try Windows setup again”** but no real UAC prompt appears, or setup immediately falls back to **“Windows setup didn’t finish.”** citeturn832867search0turn832867search3

The most promising workaround I found is to reset only your Codex config first, because one recent community report says a stale/corrupted `config.toml` can cause this setup gate to fail. citeturn832867search1

Do this:

```powershell
Rename-Item "$HOME\.codex\config.toml" "config.toml.backup"
```

Then fully close ChatGPT/Codex and reopen it. Let it create a fresh config and try **Windows setup** again.

If that works, do **not** immediately paste your entire old `config.toml` back. Restore it section by section, because one of your custom settings may be tripping `config_load`.

If it still fails, the next safest workaround is to use **Continue with limited access** temporarily. There are current open issues where the Windows sandbox helper itself fails before creating its sandbox state, including ACL/access-denied failures, so reinstalling the app may not help. citeturn832867search2turn832867search4

Given that you recently made major changes to `config.toml`, I would try the rename/reset method first.

## Resources

### Local attachments
- [84c1e856-55a1-423a-bcfa-3bd9c9b5988e.png](../../../Raw/Export/file_00000000d38481faa1d96a7531dd8768.dat)
- [70a5fe73-94f0-44cd-b09f-f28686a17558.png](../../../Raw/Export/file_00000000798481fab57020a678c5cf0c.dat)
- [bf45a24f-d440-40ab-a1cc-413e11c3776b.png](../../../Raw/Export/file_00000000d95881fa94afd2ee79f39538.dat)
- [382d35a0-b6bc-4856-999e-d377b688384e.png](../../../Raw/Export/file_000000004ac0820b9b0a7b30eb41e94a.dat)
- [6b8aebb8-0be9-4fb5-8edc-73a0f6adccbe.png](../../../Raw/Export/file_000000007d4081fab834caae86033b94.dat)
- [902909e3-f75d-4a65-9406-a5f1986f3f3a.png](../../../Raw/Export/file_00000000faf081fab80c16f3f8ffd9d6.dat)
- [0ca8dfa4-fa57-4a3b-a67b-6f59827c7649.png](../../../Raw/Export/file_00000000741081fa8c6b88574dba1556.dat)
- [0d5fd727-4e66-4fe8-a07f-c83183bb6331.png](../../../Raw/Export/file_000000001b3481fa982598c0eb5430d3.dat)
- [b5b7fe57-4293-4943-b953-d7e7a53336ae.png](../../../Raw/Export/file_00000000fe6481faac119a224277ad55.dat)
- [3ec01eee-daa3-4f99-8e1e-ff7503b685f2.png](../../../Raw/Export/file_0000000031c481fd84ad08c4a9d81bda.dat)

### External references
- [Configure Codex Plus Subscription](https://chatgpt.com/c/6a8febb2-853c-83ee-91a2-42544b24c129)
- [Apple Music ALAC Setup](https://chatgpt.com/c/6a4bdcbf-8ca0-83ee-9e01-f7d961f07879)
- [Find AI Projects](https://chatgpt.com/c/6a8c386d-9e68-83e8-856b-1304160734a4)
- [Event Speaker Highlights](https://chatgpt.com/c/68122fd1-d814-8007-bc14-4e55de24c560)
- [iQOO](https://chatgpt.com/c/6a89d21e-12a0-83e8-8202-ba608ffb9656)
- [Internship Details for Google Form](https://chatgpt.com/c/6a369cc1-85c8-83e8-8fbc-a2fa9aae95d8)
- [Codex Installation Troubleshooting](https://chatgpt.com/c/6a72ff4d-7094-83ee-93b5-1541139dedf4)
- [LinkedIn Summary Creation Guide](https://chatgpt.com/c/679bbe34-d52c-8007-b3fb-5e95ab476737)
- [Frontend Skills Roadmap](https://chatgpt.com/c/682462ba-fd94-8007-9b74-3e0641028898)
- [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model?utm_source=chatgpt.com)
- [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5&utm_source=chatgpt.com)
- [OpenAI Developers](https://developers.openai.com/?utm_source=chatgpt.com)
- [Responses | OpenAI API Reference](https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses?utm_source=chatgpt.com)
- [GPT-5.3-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.3-codex?utm_source=chatgpt.com)
- [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2&utm_source=chatgpt.com)
- [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-4.1&utm_source=chatgpt.com)
- [GPT-5.2-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.2-codex?utm_source=chatgpt.com)
- [GPT-5-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5-codex?utm_source=chatgpt.com)
- [Create a model response | OpenAI API Reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/create?utm_source=chatgpt.com)
- [Responses | OpenAI API Reference](https://developers.openai.com/api/reference/ruby/resources/beta/subresources/responses?utm_source=chatgpt.com)
- [Community | OpenAI Developers](https://developers.openai.com/community?utm_source=chatgpt.com)
- [Responses | OpenAI API Reference](https://developers.openai.com/api/reference/java/resources/beta/subresources/responses?utm_source=chatgpt.com)
- [Showcase | OpenAI Developers](https://developers.openai.com/showcase?view=webmcp-apps&utm_source=chatgpt.com)
- [Apps | OpenAI Developers](https://developers.openai.com/showcase/apps?use_case=webmcp&utm_source=chatgpt.com)
- [All models | OpenAI API](https://developers.openai.com/api/docs/models/all?utm_source=chatgpt.com)
- [Showcase | OpenAI Developers](https://developers.openai.com/showcase?view=internal-apps&utm_source=chatgpt.com)
- [Games | OpenAI Developers](https://developers.openai.com/showcase/games?utm_source=chatgpt.com)
- [codex/codex-rs/core/src/config/mod.rs at main · openai/codex · GitHub](https://github.com/openai/codex/blob/main/codex-rs/core/src/config/mod.rs?utm_source=chatgpt.com)
- [codex/codex-rs/app-server-protocol/schema/json/v2/ConfigReadResponse.json at main · openai/codex · GitHub](https://github.com/openai/codex/blob/main/codex-rs/app-server-protocol/schema/json/v2/ConfigReadResponse.json?utm_source=chatgpt.com)
- [MultiAgentV2 runaway delegation: 74 subagents, 3-level nesting, 5.39B recorded tokens, and repeated review/test loops in one task · Issue #38989 · openai/codex · GitHub](https://github.com/openai/codex/issues/38989?utm_source=chatgpt.com)
- [gpt-5.6-sol `ultra` effort spawns multi-agent swarms despite `features.multi_agent=false`, consuming 250–600 credits per read-only task without batching guidance · Issue #35177 · openai/codex · GitHub](https://github.com/openai/codex/issues/35177?utm_source=chatgpt.com)
- [codex exec: registered agent TOML model / model_reasoning_effort ignored — subagents inherit the parent model (0.144.5) · Issue #33881 · openai/codex · GitHub](https://github.com/openai/codex/issues/33881?utm_source=chatgpt.com)
- [Docs ambiguity: scope of task-sensitive model/effort selection when settings are unpinned · Issue #36422 · openai/codex · GitHub](https://github.com/openai/codex/issues/36422?utm_source=chatgpt.com)
- [Windows 0.153.4: high usage with V2 workers, Code Mode truncation and effort-change cache misses (local telemetry) · Issue #43229 · openai/codex · GitHub](https://github.com/openai/codex/issues/43229?utm_source=chatgpt.com)
- [\[App\] Reasoning-effort picker cannot override project .codex/config.toml default · Issue #34535 · openai/codex · GitHub](https://github.com/openai/codex/issues/34535?utm_source=chatgpt.com)
- [I don't have the "max" reasoning effort settings in the Codex plugin. · Issue #40071 · openai/codex · GitHub](https://github.com/openai/codex/issues/40071?utm_source=chatgpt.com)
- [GPT-6 Astra reasoning-effort changes do not use configuration_update, defeating cache preservation · Issue #42996 · openai/codex · GitHub](https://github.com/openai/codex/issues/42996?utm_source=chatgpt.com)
- [Codex sub-agent spawn supports per-launch reasoning_effort, but tool schema/docs make agents think it cannot be changed · openai/codex@ed6e5cf · GitHub](https://github.com/openai/codex/actions/runs/27122575345?utm_source=chatgpt.com)
- [Codex CLI ignores model setting from config.toml · Issue #33642 · openai/codex · GitHub](https://github.com/openai/codex/issues/33642?utm_source=chatgpt.com)
- [GPT-5 Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5?utm_source=chatgpt.com)
- [GPT-5.1 Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.1?utm_source=chatgpt.com)
- [Get a model response | OpenAI API Reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/retrieve?utm_source=chatgpt.com)
- [codex-mini-latest Model | OpenAI API](https://developers.openai.com/api/docs/models/codex-mini-latest?utm_source=chatgpt.com)
- [GPT-5.1-Codex-Max Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.1-codex-max?utm_source=chatgpt.com)
- [GPT-5.4 Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.4?utm_source=chatgpt.com)
- [GPT-5.1-Codex Mini Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.1-codex-mini?utm_source=chatgpt.com)
- [Chat Latest Model | OpenAI API](https://developers.openai.com/api/docs/models/chat-latest?utm_source=chatgpt.com)
- [GPT-5.5 Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.5?utm_source=chatgpt.com)
- [Codex Meetups in Pune | OpenAI Developers](https://developers.openai.com/community/meetups?city=Pune&utm_source=chatgpt.com)
- [Showcase | OpenAI Developers](https://developers.openai.com/showcase/all?utm_source=chatgpt.com)
- [Windows app stuck on "Finish Windows setup" — sandbox setup never triggers a real UAC prompt, "Retry" fails instantly · Issue #32492 · openai/codex · GitHub](https://github.com/openai/codex/issues/32492?utm_source=chatgpt.com)
- [\[Windows\] "Finish Windows setup" loops with no UAC prompt; sandbox runner gets Access Denied on C:\Users\Default · Issue #37940 · openai/codex · GitHub](https://github.com/openai/codex/issues/37940?utm_source=chatgpt.com)
- [Bug: Cannot access Chatgpt after new update - #10 by karaachs - Bugs - OpenAI Developer Community](https://community.openai.com/t/bug-cannot-access-chatgpt-after-new-update/1386466/10?utm_source=chatgpt.com)
- [Windows setup loop — "Couldn't check Windows setup" / "Windows setup didn't finish", sandbox-setup.exe crashes silently on elevation · Issue #42264 · openai/codex · GitHub](https://github.com/openai/codex/issues/42264?utm_source=chatgpt.com)
- [Windows elevated sandbox setup fails with SetNamedSecurityInfoW error 5 · Issue #39245 · openai/codex · GitHub](https://github.com/openai/codex/issues/39245?utm_source=chatgpt.com)
- [Windows sandbox setup helper fails with 0xc0000142 only when launched by Codex · Issue #34928 · openai/codex · GitHub](https://github.com/openai/codex/issues/34928?utm_source=chatgpt.com)
- [Windows app stuck on "Finish Windows setup" — sandbox setup never triggers a real UAC prompt, "Retry" fails instantly · openai/codex@9e552e9 · GitHub](https://github.com/openai/codex/actions/runs/29185738501?utm_source=chatgpt.com)
- [Windows Desktop: "Finish Windows setup" never completes, preventing sandboxed edits · Issue #32808 · openai/codex · GitHub](https://github.com/openai/codex/issues/32808?utm_source=chatgpt.com)
- [\[Windows\]\[WSL\] Switching back to Windows Native fails with repeated UAC prompts and `config_load`; config changes do not persist · Issue #42938 · openai/codex · GitHub](https://download.plaud.ai/openai/codex/issues/42938?utm_source=chatgpt.com)
- [Windows Desktop: "Finish Windows setup" never completes, preventing sandboxed edits · openai/codex #32808](https://codexissues.com/issue/32808-windows-desktop-finish-windows-setup-never-completes-preventing-sandboxed-edits?utm_source=chatgpt.com)
- [Using the ChatGPT Windows app | OpenAI Help Center](https://help.openai.com/en/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Bug: Cannot access Chatgpt after new update - #12 by yanayeay - Bugs - OpenAI Developer Community](https://community.openai.com/t/bug-cannot-access-chatgpt-after-new-update/1386466/12?utm_source=chatgpt.com)
- [Bug: Cannot access Chatgpt after new update - #14 by pmi - Bugs - OpenAI Developer Community](https://community.openai.com/t/bug-cannot-access-chatgpt-after-new-update/1386466/14?utm_source=chatgpt.com)
- [Windows app | OpenAI Help Center](https://help.openai.com/en/collections/10670766-windows-?utm_source=chatgpt.com)
- [ChatGPT Windows ആപ്പ് ഉപയോഗിക്കുന്നത് | OpenAI Help Center](https://help.openai.com/ml-in/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [ChatGPT on Windows not starting after clicking the icon - solution - Bugs - OpenAI Developer Community](https://community.openai.com/t/chatgpt-on-windows-not-starting-after-clicking-the-icon-solution/1393666?utm_source=chatgpt.com)
- [Using the built-in browser in the ChatGPT desktop app | OpenAI Help Center](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app?utm_source=chatgpt.com)
- [Windows ChatGPT Desktop 26.825.3734.0 launches background processes but no UI - Bugs - OpenAI Developer Community](https://community.openai.com/t/windows-chatgpt-desktop-26-825-3734-0-launches-background-processes-but-no-ui/1393201?utm_source=chatgpt.com)
- [Windows App - Release Notes | OpenAI Help Center](https://help.openai.com/en/articles/10003026?utm_source=chatgpt.com)
- [Connecting and managing app accounts in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/20001494-connecting-and-managing-app-accounts-in-chatgpt?utm_source=chatgpt.com)
- [Plugins in ChatGPT and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001256?utm_source=chatgpt.com)
- [ChatGPT Desktop config.toml 'zeroed out' after auto-update, causing launch failure: A record of restoring existing settings｜おふじ│現場目線の業務改善 × AI活用](https://note.com/ofuji_genbanoai/n/n9e5f7bed153b?hl=en&utm_source=chatgpt.com)
- [I can't add a new laptop to my account - Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5680759/i-cant-add-a-new-laptop-to-my-account?utm_source=chatgpt.com)
