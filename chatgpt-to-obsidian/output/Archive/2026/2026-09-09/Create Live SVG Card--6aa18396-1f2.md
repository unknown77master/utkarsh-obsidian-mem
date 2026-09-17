---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6aa18396-1f20-83ee-a41a-c4b433c4f573"
created: 1788969879.268904
updated: 1789046283.450946
resource_section: true
---

# Create Live SVG Card

## User

\[!\[whoburnedmore\]\(\[https://api.whoburnedmore.com/v1/badge/utkarsh-wadalkar.svg)\\](https://whoburnedmore.com/u/utkarsh-wadalkar\](https://api.whoburnedmore.com/v1/badge/utkarsh-wadalkar.svg\)\]\(https://whoburnedmore.com/u/utkarsh-wadalkar))

i want to change this svg to like in picture, but it should be live, it should update automatically in by github readme.md

## Assistant

Worked for 18s

## Assistant

Yes — you can make the **large Landscape card from your second screenshot live inside your GitHub README**, but only if WhoBurnedMore exposes that card as a public image/SVG endpoint.

Your current code:

```md
\[!\[whoburnedmore\](https://api.whoburnedmore.com/v1/badge/utkarsh-wadalkar.svg)\](https://whoburnedmore.com/u/utkarsh-wadalkar)
```

uses their small `badge` SVG endpoint. The CLI/dashboard itself stays live because WhoBurnedMore background sync refreshes usage roughly every 15 minutes. citeturn699986search1

### What you want

Basically this:

```text
┌─────────────────────────────────────────────┐
│ @utkarsh-wadalkar TOTAL COST $1,825 │
│ #203 ALL-TIME TODAY +1.2M │
│ │
│ TOKENS BURNED 30-DAY BURN │
│ 804M ▃▂▁▃▂▇▁▂▃▂ │
│ codex █████ 59% │
│ 36 active days claude ████ 41% │
└─────────────────────────────────────────────┘
```

and have `804M`, `$1,825`, rank, streak, chart, Codex/Claude percentages etc. update automatically.

### Important problem

I checked WhoBurnedMore's current public docs/site. I can confirm the documented live badge endpoint and their automatic usage syncing, but I **couldn't find a documented public SVG endpoint for the Landscape share card**. The Landscape/Hero/Report options you see in the dashboard appear to be part of their share-card generator rather than the documented README badge API. citeturn699986search0turn699986search1

So changing:

```text
/v1/badge/...
```

to something guessed such as:

```text
/v1/card/...
/v1/card/.../landscape.svg
/v1/share/...
```

would not be reliable unless we find the actual internal endpoint.

## Best solution

Since WhoBurnedMore is open source, we can make **our own live SVG wrapper** that looks almost exactly like your screenshot.

Architecture:

```text
GitHub README
 ↓
your dynamic SVG endpoint
 ↓
WhoBurnedMore public stats/API
 ↓
Live generated landscape card
```

Your README would then be as simple as:

```md
<a href="https://whoburnedmore.com/u/utkarsh-wadalkar">
 <img
 src="https://YOUR-ENDPOINT.vercel.app/api/whoburnedmore/utkarsh-wadalkar"
 width="700"
 alt="WhoBurnedMore stats"
 />
</a>
```

Every time GitHub refreshes the image, your endpoint fetches the latest WhoBurnedMore numbers and produces SVG:

```text
TOTAL COST
TODAY
MESSAGES
STREAK
ALL-TIME RANK
TOKENS BURNED
ACTIVE DAYS
30-DAY BURN
CODEX %
CLAUDE %
```

No README commits required.

### I'd use Vercel for this

Because you're already comfortable with Vercel/TypeScript, I'd make it something like:

```text
whoburnedmore-card/
├── app/
│ └── api/
│ └── card/
│ └── \[username\]/
│ └── route.ts
├── lib/
│ ├── whoburnedmore.ts
│ └── card.ts
└── package.json
```

Then:

```text
https://your-domain.vercel.app/api/card/utkarsh-wadalkar
```

returns:

```http
Content-Type: image/svg+xml
Cache-Control: public, s-maxage=900, stale-while-revalidate=3600
```

A 15-minute cache would also line up nicely with WhoBurnedMore's background sync cadence. citeturn699986search1

### Result in your profile README

```md
<p align="center">
 <a href="https://whoburnedmore.com/u/utkarsh-wadalkar">
 <img
 src="https://your-domain.vercel.app/api/card/utkarsh-wadalkar"
 width="720"
 alt="Utkarsh's AI coding token usage"
 />
 </a>
</p>
```

So when you go from:

```text
804M → 850M → 1B
```

or your rank becomes:

```text
#203 → #180
```

the README card changes automatically without touching `README.md`.

One thing I'd do **before building our own version**: inspect the WhoBurnedMore source/network calls and see whether the exact Landscape card already has an undocumented live endpoint. If it does, you can use that directly and need **zero custom infrastructure**. If it doesn't, the Vercel SVG route above is the cleanest fallback. memcite

## User

Scaffold the empty repository as a Vercel-ready TypeScript service.

means what?

## Assistant

It means:

**“Set up the basic project structure and configuration so this empty repo can run as a TypeScript app/service on Vercel.”**

In practice, whoever does the scaffolding would create the starter files, for example:

```text
whoburnedmore-card/
├── app/
│ └── api/
│ └── card/
│ └── \[username\]/
│ └── route.ts
├── package.json
├── tsconfig.json
├── .gitignore
└── README.md
```

and install/configure things so that:

```bash
npm install
npm run dev
```

works locally, and pushing the repo to Vercel can deploy it without extra setup.

For your specific live SVG card project, “scaffold the empty repository as a Vercel-ready TypeScript service” basically means:

> Create the starter Next.js/TypeScript project, add a Vercel-compatible API route structure, configure TypeScript/package scripts, and leave it ready for us to implement the WhoBurnedMore API fetching and SVG generation.

It **does not mean build the whole feature yet**. It mainly means “prepare the foundation.”

## User

Documentation and deployment

- Scaffold the empty repository as a Vercel-ready TypeScript service.
- Add README snippets showing every style with a replaceable handle:

 ```md
 <img src="https://YOUR-DEPLOYMENT/api/card/YOUR-HANDLE/landscape.png" />
 ```

- Document Vercel deployment and update the README with the real production URL once deployed.

means

## Assistant

That section is basically saying: **prepare the project so anyone can deploy it, use it, and understand how to embed the cards.**

For your project, each line means this:

- **“Scaffold the empty repository as a Vercel-ready TypeScript service.”** 
 Set up the repo with the basic TypeScript/Vercel project files and API route structure so it can run locally and deploy to Vercel.

- **“Add README snippets showing every style with a replaceable handle.”** 
 In the `README.md`, show copy-paste examples for each card style, like:
 ```md
 <img src="https://YOUR-DEPLOYMENT/api/card/YOUR-HANDLE/landscape.png" />
 ```

 And similarly:
 ```md
 <img src="https://YOUR-DEPLOYMENT/api/card/YOUR-HANDLE/hero.png" />
 <img src="https://YOUR-DEPLOYMENT/api/card/YOUR-HANDLE/report.png" />
 ```

 `YOUR-HANDLE` is meant to be replaced with something like:
 ```text
 utkarsh-wadalkar
 ```

- **“Document Vercel deployment.”** 
 Add instructions in the README explaining how to deploy:
 ```text
 1. Fork/clone repository
 2. Import it into Vercel
 3. Deploy
 4. Copy production URL
 ```

- **“Update the README with the real production URL once deployed.”** 
 Before deployment, examples might use:
 ```text
 https://YOUR-DEPLOYMENT/api/card/...
 ```

 After deployment, replace that with the actual URL, for example:
 ```md
 <img src="https://whoburnedmore-card.vercel.app/api/card/utkarsh-wadalkar/landscape.png" />
 ```

So the final deliverable should look roughly like:

```text
Repository
│
├── TypeScript/Vercel service
├── API endpoint
│ └── /api/card/\[handle\]/\[style\].png
│
├── README
│ ├── Landscape example
│ ├── Hero example
│ ├── Report example
│ ├── GitHub README usage
│ └── Vercel deployment instructions
│
└── Production deployment
 └── https://something.vercel.app
```

One thing I would change in that requirement for your project: if you are actually returning an **SVG**, the endpoint should ideally be:

```text
/api/card/utkarsh-wadalkar/landscape.svg
```

instead of `.png`.

SVG is much better for GitHub README cards because it stays sharp at every resolution and is easy to generate dynamically.

## User

i want a website where users go and put their profile/handle username or link and it gives user card link or command to run in terminal to generate card or what ever the process is

## Assistant

Yes — that’s a better product than just exposing an API endpoint.

The website should act as a **card generator / onboarding UI** for WhoBurnedMore-style live cards.

A clean flow would be:

```text
User opens website
 ↓
Enters WhoBurnedMore handle or profile URL
 ↓
Website validates the profile
 ↓
Shows live preview of card styles
 ↓
User chooses:
Landscape / Hero / Report
 ↓
Website generates:
1. Direct image URL
2. GitHub README Markdown
3. HTML embed
4. Optional terminal command
```

For example, user enters:

```text
utkarsh-wadalkar
```

or:

```text
https://whoburnedmore.com/u/utkarsh-wadalkar
```

Then the site shows a preview and generates something like:

```md
\[!\[WhoBurnedMore\](https://yourdomain.com/api/card/utkarsh-wadalkar/landscape.svg)\](https://whoburnedmore.com/u/utkarsh-wadalkar)
```

And HTML:

```html
<a href="https://whoburnedmore.com/u/utkarsh-wadalkar">
 <img
 src="https://yourdomain.com/api/card/utkarsh-wadalkar/landscape.svg"
 alt="WhoBurnedMore stats"
 />
</a>
```

The terminal command is optional, but you could also support:

```bash
npx whoburnedmore-card utkarsh-wadalkar
```

which prints the Markdown snippet in the terminal.

A stronger product structure would be:

```text
/
├── Landing page
│ ├── Handle / profile URL input
│ ├── Generate button
│ └── Example card
│
├── /generate
│ ├── Live preview
│ ├── Style selector
│ │ ├── Landscape
│ │ ├── Hero
│ │ └── Report
│ ├── Copy card URL
│ ├── Copy Markdown
│ ├── Copy HTML
│ └── Copy CLI command
│
└── /api/card/\[handle\]/\[style\].svg
```

For your case, I would make the **website the primary experience** and the API just power it behind the scenes.

The UX could be as simple as:

```text
Create your live AI coding card

\[ utkarsh-wadalkar \]

or paste:
https://whoburnedmore.com/u/utkarsh-wadalkar

 Generate card
```

Then:

```text
┌────────────────────────────────────────────┐
│ │
│ LIVE CARD PREVIEW │
│ │
│ TOKENS BURNED $1,825 │
│ 804M +1.2M today │
│ │
└────────────────────────────────────────────┘

Style
\[ Landscape \] \[ Hero \] \[ Report \]

GitHub Markdown
┌────────────────────────────────────────────┐
│ \[!\[WhoBurnedMore\](https://...)\](...) │
└────────────────────────────────────────────┘
 \[ Copy \]

Direct image
https://yourdomain.com/api/card/...

 \[ Copy \]

CLI
npx whoburnedmore-card utkarsh-wadalkar

 \[ Copy \]
```

I would **not require users to run a terminal command just to get the card**. That's unnecessary friction. The ideal experience is:

> Paste handle → choose design → copy Markdown → paste into GitHub README.

The CLI can be an extra developer-friendly option.

For the README/project requirements, I would rewrite your earlier section as:

```md
## Website and card generation

- Build a public web interface where users can enter either:
 - their WhoBurnedMore handle, or
 - their full WhoBurnedMore profile URL.

- Normalize both inputs into a valid profile handle.

- Fetch the user's current public statistics and render live previews of all supported card styles:
 - Landscape
 - Hero
 - Report

- For the selected card, generate copyable outputs for:
 - Direct SVG URL
 - GitHub Markdown
 - HTML embed
 - CLI command

Example:

```md
\[!\[WhoBurnedMore\](https://YOUR-DOMAIN/api/card/YOUR-HANDLE/landscape.svg)\](https://whoburnedmore.com/u/YOUR-HANDLE)
```

- Cards must remain dynamic. Users should not need to regenerate the card when their statistics change.

- Expose public endpoints following:

```text
/api/card/:handle/landscape.svg
/api/card/:handle/hero.svg
/api/card/:handle/report.svg
```

- Add one-click copy buttons for every generated snippet.

- Deploy the frontend and API together on Vercel.

- After production deployment, replace placeholder domains in examples with the real production domain.
```

And architecturally, I'd keep it **stateless** initially. No login, database, or user accounts.

```text
WhoBurnedMore
 ↓
Your API
 ↓
SVG renderer
 ↓
GitHub README

 ↑
 Website
 Handle → Preview → Copy
```

That keeps the MVP extremely clean: **one website + one dynamic card API**. Later you can add themes, custom colors, hiding metrics, custom widths, badges, analytics, etc. memcite

## User

include it also, make it part of plan

## Assistant

Yes — I’d make the CLI a first-class part of the plan, not just an optional afterthought.

## Updated plan

### 1. Public website

Build a public website where users can enter either:

```text
utkarsh-wadalkar
```

or:

```text
https://whoburnedmore.com/u/utkarsh-wadalkar
```

The site should normalize the input, validate the profile, fetch the public stats, and show live previews.

Supported styles:

```text
Landscape
Hero
Report
```

### 2. Live card API

Expose dynamic endpoints such as:

```text
/api/card/:handle/landscape.svg
/api/card/:handle/hero.svg
/api/card/:handle/report.svg
```

Example:

```text
https://yourdomain.com/api/card/utkarsh-wadalkar/landscape.svg
```

The SVG should be generated dynamically from the latest profile data, so the user does not have to regenerate or edit their README when stats change.

### 3. Card generator UI

After entering the handle, show:

```text
Live Preview

\[ Landscape \] \[ Hero \] \[ Report \]
```

Then generate four outputs.

#### Direct card URL

```text
https://yourdomain.com/api/card/utkarsh-wadalkar/landscape.svg
```

#### GitHub Markdown

```md
\[!\[WhoBurnedMore\](https://yourdomain.com/api/card/utkarsh-wadalkar/landscape.svg)\](https://whoburnedmore.com/u/utkarsh-wadalkar)
```

#### HTML

```html
<a href="https://whoburnedmore.com/u/utkarsh-wadalkar">
 <img
 src="https://yourdomain.com/api/card/utkarsh-wadalkar/landscape.svg"
 alt="WhoBurnedMore stats"
 />
</a>
```

#### CLI

```bash
npx whoburnedmore-card utkarsh-wadalkar
```

Every output gets a **Copy** button.

---

## 4. CLI package

Create a small npm CLI package:

```text
whoburnedmore-card
```

Users can run:

```bash
npx whoburnedmore-card utkarsh-wadalkar
```

and receive something like:

```text
WhoBurnedMore Card

Handle: utkarsh-wadalkar
Style: landscape

Direct URL:
https://yourdomain.com/api/card/utkarsh-wadalkar/landscape.svg

GitHub Markdown:
\[!\[WhoBurnedMore\](https://yourdomain.com/api/card/utkarsh-wadalkar/landscape.svg)\](https://whoburnedmore.com/u/utkarsh-wadalkar)
```

The CLI should also support profile URLs:

```bash
npx whoburnedmore-card https://whoburnedmore.com/u/utkarsh-wadalkar
```

and style selection:

```bash
npx whoburnedmore-card utkarsh-wadalkar --style hero
```

```bash
npx whoburnedmore-card utkarsh-wadalkar --style report
```

I'd also support:

```bash
npx whoburnedmore-card utkarsh-wadalkar --format markdown
```

```bash
npx whoburnedmore-card utkarsh-wadalkar --format html
```

```bash
npx whoburnedmore-card utkarsh-wadalkar --format url
```

And a convenient copy option:

```bash
npx whoburnedmore-card utkarsh-wadalkar --copy
```

So the complete CLI interface can remain very small:

```text
whoburnedmore-card <handle-or-url>

--style landscape|hero|report
--format markdown|html|url
--copy
```

---

## 5. Website should generate CLI commands too

On the website, the CLI section can automatically reflect the selected style.

For example, if the user selects **Hero**:

```bash
npx whoburnedmore-card utkarsh-wadalkar --style hero
```

If they select **Report**:

```bash
npx whoburnedmore-card utkarsh-wadalkar --style report
```

So website users can choose either workflow:

```text
Paste into README
 or
Run in terminal
```

---

## 6. Recommended repository structure

I would use a monorepo:

```text
whoburnedmore-card/
│
├── apps/
│ └── web/
│ ├── app/
│ │ ├── page.tsx
│ │ ├── generate/
│ │ └── api/
│ │ └── card/
│ │ └── \[handle\]/
│ │ └── \[style\]/
│ │ └── route.ts
│ │
│ ├── components/
│ │ ├── HandleInput.tsx
│ │ ├── CardPreview.tsx
│ │ ├── StyleSelector.tsx
│ │ └── CopySnippet.tsx
│ │
│ └── lib/
│ ├── handle.ts
│ ├── stats.ts
│ └── svg/
│
├── packages/
│ ├── core/
│ │ ├── handle.ts
│ │ ├── urls.ts
│ │ └── types.ts
│ │
│ └── cli/
│ ├── src/
│ │ └── index.ts
│ └── package.json
│
├── package.json
├── tsconfig.json
└── README.md
```

The important part is having:

```text
packages/core
```

for shared logic.

Both the website and CLI should use the same functions for:

```text
handle normalization
profile URL parsing
style names
card URL generation
Markdown generation
HTML generation
```

That prevents duplicated logic.

---

## 7. Keep the MVP stateless

Initially, don't add:

```text
Login
User accounts
Database
Dashboard
Saved cards
OAuth
```

The whole system can work as:

```text
 WhoBurnedMore
 ↓
 Stats fetcher
 ↓
 Card renderer
 ↓
 Dynamic SVG endpoint
 ↙ ↘
 Website GitHub
 ↑
 User input

CLI
 ↓
Shared core package
 ↓
Card URL / Markdown / HTML
```

That gives you a genuinely useful product without unnecessary infrastructure.

## Final requirements section

You can put this directly into your implementation plan:

```md
## Website, CLI, documentation and deployment

- Scaffold the repository as a Vercel-ready TypeScript monorepo.

- Build a public card-generator website where users can enter either:
 - a WhoBurnedMore handle;
 - or a full WhoBurnedMore profile URL.

- Normalize and validate the provided profile input.

- Show live previews for all supported card styles:
 - Landscape
 - Hero
 - Report

- Expose dynamic SVG endpoints:

 /api/card/:handle/landscape.svg
 /api/card/:handle/hero.svg
 /api/card/:handle/report.svg

- Cards must remain live and automatically reflect updated public profile statistics without requiring users to regenerate the card or modify their README.

- For the selected card, generate copyable:
 - Direct SVG URL
 - GitHub Markdown
 - HTML embed
 - CLI command

- Add one-click copy controls for every generated output.

- Create an npm CLI package usable through:

 npx whoburnedmore-card YOUR-HANDLE

- The CLI must accept either a handle or full profile URL.

- Support CLI options:

 --style landscape|hero|report
 --format markdown|html|url
 --copy

- Example:

 npx whoburnedmore-card utkarsh-wadalkar --style landscape --format markdown

- Share handle parsing, URL generation, types, and snippet generation between the web application and CLI through a common core package.

- Keep the initial product stateless:
 - no login;
 - no database;
 - no saved cards;
 - no user accounts.

- Document all supported website, API, Markdown, HTML, and CLI usage in the README.

- Include README snippets for every style with a replaceable handle:

 <img src="https://YOUR-DEPLOYMENT/api/card/YOUR-HANDLE/landscape.svg" />

- Document local development, npm CLI usage, and Vercel deployment.

- Deploy the web application/API to Vercel.

- Publish the CLI package to npm when ready.

- After production deployment, replace placeholder URLs throughout the README with the real production domain.
```

This gives the project **three ways to use the same system**: website for normal users, direct API for embedding, and CLI for developers.

## User

ok, make these instruction which will be included in readme.md part of fronted of website , because repo will be private, not public

## Assistant

Yes — since the repo will be private, the public-facing usage instructions should live on the website itself, not depend on `README.md`.

I’d update that part of the plan to this:

```md
## Website documentation and user onboarding

- Treat the website as the primary public documentation surface because the source repository will remain private.

- Add a dedicated "How to use" / "Docs" section to the frontend explaining all supported ways to generate and use cards.

- The frontend must document:

 ### 1. Website flow
 - Enter a WhoBurnedMore handle or full profile URL.
 - Choose a card style:
 - Landscape
 - Hero
 - Report
 - Preview the live card.
 - Copy the desired output.

 ### 2. GitHub Markdown
 Show a copyable example generated using the user's current handle:

 \[!\[WhoBurnedMore\](https://YOUR-DOMAIN/api/card/YOUR-HANDLE/landscape.svg)\](https://whoburnedmore.com/u/YOUR-HANDLE)

 Explain that the card is live and updates automatically as the user's statistics change.

 ### 3. HTML embed
 Show a copyable HTML example:

 <a href="https://whoburnedmore.com/u/YOUR-HANDLE">
 <img
 src="https://YOUR-DOMAIN/api/card/YOUR-HANDLE/landscape.svg"
 alt="WhoBurnedMore stats"
 />
 </a>

 ### 4. Direct card URL
 Show the direct live card URL:

 https://YOUR-DOMAIN/api/card/YOUR-HANDLE/landscape.svg

 ### 5. CLI usage
 Document the CLI directly on the website.

 Basic usage:

 npx whoburnedmore-card YOUR-HANDLE

 Accept a full profile URL as well:

 npx whoburnedmore-card https://whoburnedmore.com/u/YOUR-HANDLE

 Style selection:

 npx whoburnedmore-card YOUR-HANDLE --style landscape
 npx whoburnedmore-card YOUR-HANDLE --style hero
 npx whoburnedmore-card YOUR-HANDLE --style report

 Output formats:

 npx whoburnedmore-card YOUR-HANDLE --format markdown
 npx whoburnedmore-card YOUR-HANDLE --format html
 npx whoburnedmore-card YOUR-HANDLE --format url

 Copy directly to clipboard:

 npx whoburnedmore-card YOUR-HANDLE --copy

- The website should generate these examples dynamically using:
 - the user's entered handle;
 - the currently selected card style;
 - the real production domain.

- Add one-click Copy buttons beside:
 - Direct SVG URL
 - GitHub Markdown
 - HTML embed
 - CLI command

- Add a short explanation such as:

 "Your card stays live. Add it to your GitHub README once and the displayed stats will update automatically."

- Add a visible API/usage reference for supported card URLs:

 /api/card/:handle/landscape.svg
 /api/card/:handle/hero.svg
 /api/card/:handle/report.svg

- Do not rely on access to the private GitHub repository for any end-user setup or documentation.

- Keep README.md focused on internal developer documentation:
 - project setup;
 - architecture;
 - environment variables;
 - local development;
 - deployment notes;
 - internal CLI publishing steps.

- Public user documentation, usage examples, and onboarding must all be available from the deployed website.
```

For the frontend, I’d make this a proper section rather than a huge wall of docs. Something like:

```text
Generate your card

\[ Enter handle or profile URL \]

\[ Landscape \] \[ Hero \] \[ Report \]

 LIVE PREVIEW

Use your card

\[ GitHub \] \[ HTML \] \[ Direct URL \] \[ CLI \]

┌─────────────────────────────────────────────┐
│ npx whoburnedmore-card utkarsh-wadalkar │
└───────────────────────────────────── \[Copy\]

How it works

1. Add the card once
2. We fetch your latest public stats
3. The card updates automatically
4. No README changes required
```

And I’d still keep the **CLI package public on npm**, even though the main source repo is private. Users only need:

```bash
npx whoburnedmore-card ...
```

They do not need access to your GitHub repository at all.

## User

whoburnedmore_card.vercel.app in this "_" is it valid will vercel allow to make this domain or should it be whoburnedmore-card.vercel.app and what is "-" this called by humans

## Assistant

Worked for a couple of seconds

## Assistant

Use:

`whoburnedmore-card.vercel.app`

not:

`whoburnedmore_card.vercel.app`

The reason is that `_` is called an **underscore**, and it is generally not valid in normal hostname/domain labels. `-` is called a **hyphen** or **dash**, and that is valid in domain names.

So:

- `_` = underscore
- `-` = hyphen
- `whoburnedmore_card.vercel.app` → not suitable
- `whoburnedmore-card.vercel.app` → correct format

For Vercel specifically, the generated `.vercel.app` hostname should use letters, numbers, and hyphens. So I’d name the project:

`whoburnedmore-card`

which gives you:

`https://whoburnedmore-card.vercel.app`

That also looks cleaner in your GitHub README card URLs, e.g.:

```md
https://whoburnedmore-card.vercel.app/api/card/utkarsh-wadalkar/landscape.svg
```

## User

I have a practical correction: store completed PNGs in Next’s shared Data Cache (the cards are only \~197 KB, well below the cache-item limit). Once any render finishes—even after GitHub’s first short timeout—later GitHub requests read the PNG immediately. The playground will also prewarm a card before it exposes its README URL.

Loaded a tool, ran a command

The current renderer also still depends on a remote Chromium download; Vercel logs show that source occasionally returns `500`. I’m replacing it with the full, deployment-bundled Chromium package and adding a shared card cache plus bounded asset waits. That removes the fragile remote dependency and makes both first renders and GitHub re-fetches substantially faster.

how about using database as cache to store images and when same user updates its card, then old card gets deleted and new one gets saved and used as cache

## Assistant

Worked for a couple of seconds

## Assistant

Yes, that can work, but I would not make the database itself the primary image store.

A better pattern is:

```text
User/card key
 ↓
Database metadata
 ↓
Object/blob storage for PNG
```

For example:

```text
card_key:
utkarsh-wadalkar:landscape

database row:
handle = utkarsh-wadalkar
style = landscape
image_url = ...
stats_hash = abc123
updated_at = ...
```

The actual ~197 KB PNG should live in blob/object storage, not inside PostgreSQL unless you have a specific reason.

When the same user's stats change, your flow can be:

```text
Request card
 ↓
Fetch current WhoBurnedMore stats
 ↓
Create deterministic stats hash
 ↓
Compare with cached hash

same hash
 → return existing PNG immediately

different hash
 → render new PNG
 → upload new PNG
 → update DB pointer/hash
 → delete previous PNG
 → return new PNG
```

That is a very solid architecture.

The important part is: **do not regenerate just because a request arrives**. Regenerate only when the source stats have actually changed.

A key could be:

```text
sha256({
 handle,
 style,
 relevantStats,
 rendererVersion
})
```

I would include `rendererVersion`, because if you redesign the card but the user's stats stay the same, you still want a new render.

Something like:

```text
handle: utkarsh-wadalkar
style: landscape
stats_hash: 4c6f...
renderer_version: 3
storage_key: cards/utkarsh-wadalkar/landscape/4c6f....png
```

Then the live README URL remains stable:

```text
https://whoburnedmore-card.vercel.app/api/card/utkarsh-wadalkar/landscape.png
```

but internally it can serve:

```text
cards/utkarsh-wadalkar/landscape/4c6f....png
```

That gives you two useful layers:

```text
Stable public URL
 ↓
DB/cache lookup
 ↓
Immutable versioned PNG
```

For your specific Vercel deployment, though, I would compare this against simply using Next's Data Cache.

Your current idea:

```text
Next Data Cache
```

is simpler and probably enough for the first version.

Database + blob storage gives you more control if you later want:

```text
persistent cards across deployments
cache analytics
manual invalidation
card history
CDN-backed immutable images
storage independent of framework cache behavior
multiple render workers
```

But it adds more infrastructure.

So I would use this progression:

1. **Now:** Next Data Cache for completed rendered PNGs.
2. Add a deterministic cache key based on handle/style/stats/version.
3. Only if you start hitting cache persistence/eviction/visibility problems, move the actual PNGs to object storage.
4. Keep metadata in a DB only when you genuinely need metadata/state.

If you do add persistence, I'd choose something like:

```text
Postgres / Supabase
 → metadata only

Vercel Blob / Cloudflare R2 / S3
 → PNGs
```

rather than:

```text
Postgres BYTEA
 → 197 KB image blobs
```

because storing images directly in relational DB rows works, but becomes clumsier for CDN delivery and storage management.

One more improvement: instead of deleting the previous image before the new image is ready, do this atomically:

```text
render new
→ upload new
→ update pointer
→ then delete old
```

not:

```text
delete old
→ render new
```

Otherwise a failed render can temporarily leave the user with no card.

For GitHub README reliability, the strongest design is therefore:

```text
GitHub
 ↓
stable card endpoint
 ↓
fast metadata/cache lookup
 ↓
already-rendered PNG
```

with rendering happening only on a cache miss or stats change.

So yes: your database-backed idea is good, but I'd refine it to **DB for metadata + blob/object storage for images**, with Next Data Cache still sitting in front as the fastest layer.

## User

The \[**TiDB Cloud Starter**\](https://www.pingcap.com/tidb-cloud-starter-pricing-details/) plan (formerly TiDB Cloud Serverless) offers a generous free tier with **no credit card required to start**. \[\[1\](https://docs.pingcap.com/tidbcloud/select-cluster-tier/), \[2\](https://www.srvrlss.io/provider/tidb/)\]

**Free Tier Limits Per Instance**

- **Row-based storage:** 5 GiB per instance
- **Columnar storage:** 5 GiB per instance
- **Request Units (RUs):** 50 million RUs per month per instance \[\[1\](https://www.pingcap.com/tidb-cloud-starter-pricing-details/)\]

**Organization Quotas**

- You can create up to **5 free instances** per organization by default (totaling up to 25 GiB row storage, 25 GiB columnar storage, and 250 million RUs per month if fully utilized). \[\[1\](https://www.srvrlss.io/provider/tidb/)\]
- Creating a 6th instance requires adding a credit card and setting a spending limit, converting it to a paid scalable model unless previous instances are deleted. \[\[1\](https://www.pingcap.com/tidb-cloud-starter-pricing-details/)\]

**Key Features**

- **MySQL-compatible:** Works as a drop-in relational database.
- **Built-in vector search:** Supports AI application development.
- **Auto-scaling:** Scales automatically on demand, including scale-to-zero capabilities. \[\[1\](https://www.pingcap.com/blog/beyond-planetscale-a-guide-to-choosing-your-next-free-dbaas/), \[2\](https://docs.pingcap.com/tidbcloud/select-cluster-tier/), \[3\](https://www.srvrlss.io/provider/tidb/)\]

i have used tidb and this is what it provides for free, how about we use this and tell me most optimal way to use it

## Assistant

Worked for 9s

## Assistant

Yes. Given that you already know TiDB and have a generous free Starter instance, I would use it — but **not as the thing GitHub hits for every image request**.

The most efficient architecture for your project is:

```text
 WhoBurnedMore
 ↓
 stats fetcher
 ↓
GitHub ──→ Stable API ──→ Next Data Cache
 ↓ miss
 TiDB
 ↓
 existing card state
 ↓
 PNG object/blob
```

### What TiDB should store

Use TiDB as the **persistent source of truth for rendered-card state**, not primarily as raw image storage.

One row per:

```text
handle + style
```

For example:

```text
utkarsh-wadalkar + landscape
utkarsh-wadalkar + hero
utkarsh-wadalkar + report
```

A table like:

```sql
CREATE TABLE card_cache (
 id BIGINT AUTO_RANDOM PRIMARY KEY,

 handle VARCHAR(100) NOT NULL,
 style ENUM('landscape', 'hero', 'report') NOT NULL,

 stats_hash CHAR(64) NOT NULL,
 renderer_version INT NOT NULL DEFAULT 1,

 image_url TEXT NOT NULL,
 image_etag VARCHAR(128),

 source_updated_at DATETIME,
 rendered_at DATETIME NOT NULL,
 last_requested_at DATETIME NOT NULL,

 UNIQUE KEY uniq_handle_style (handle, style)
);
```

Then have another small table for profile data if useful:

```sql
CREATE TABLE profile_cache (
 handle VARCHAR(100) PRIMARY KEY,

 stats_json JSON NOT NULL,
 stats_hash CHAR(64) NOT NULL,

 fetched_at DATETIME NOT NULL,
 expires_at DATETIME NOT NULL
);
```

That lets the three card styles share the same fetched WhoBurnedMore data.

---

## Your ideal request flow

Suppose GitHub requests:

```text
/api/card/utkarsh-wadalkar/landscape.png
```

First check Next's Data Cache.

```text
L1 — Next Data Cache
```

If the completed PNG is cached there:

```text
return image immediately
```

No Chromium.

No TiDB query.

No WhoBurnedMore request.

That's exactly what you want for the massive majority of GitHub requests.

If L1 misses, query TiDB:

```text
SELECT ...
FROM card_cache
WHERE handle = ?
 AND style = ?;
```

If TiDB says a previously rendered image exists, serve that image.

So your second level is:

```text
L2 — TiDB persistent cache metadata
```

And your actual persistent PNG can live in:

```text
L3 — Blob/object storage
```

such as Vercel Blob, R2, S3-compatible storage, etc.

---

# Most important optimization: stale-while-revalidate

Don't make GitHub wait for Chromium just because the stats might be stale.

Suppose the currently stored card says:

```text
Tokens: 804M
Rendered: 14 minutes ago
```

and your refresh interval is 15 minutes.

A request comes at minute 16.

**Bad architecture:**

```text
GitHub
 ↓
stats expired
 ↓
fetch WhoBurnedMore
 ↓
launch Chromium
 ↓
render
 ↓
wait...
 ↓
GitHub times out
```

Instead:

```text
GitHub
 ↓
Existing PNG available?
 ↓
YES
 ↓
return existing PNG immediately
 ↓
refresh asynchronously / next controlled refresh
```

The user sees a card that's perhaps 1–15 minutes old instead of a broken image.

Then:

```text
fetch latest stats
 ↓
stats changed?
 ↙ ↘
 NO YES
 ↓ ↓
nothing render new PNG
 ↓
 upload
 ↓
 update TiDB
 ↓
 invalidate L1
```

That is much more robust.

---

# Don't render unless the data actually changed

This is where TiDB becomes particularly useful.

Create a deterministic hash from the values displayed on the card.

For example:

```ts
const hashInput = JSON.stringify({
 handle,
 totalTokens,
 totalCost,
 todayTokens,
 rank,
 activeDays,
 streak,
 thirtyDayData,
 modelShares,
});

const statsHash = sha256(hashInput);
```

TiDB currently has:

```text
stats_hash = a84cfe...
```

New API response produces:

```text
stats_hash = a84cfe...
```

Same value means:

```text
DO NOT LAUNCH CHROMIUM
DO NOT RENDER
DO NOT UPLOAD
```

Just update:

```text
fetched_at
expires_at
```

That could drastically reduce your rendering workload.

---

# Include a renderer version

Make your actual cache identity:

```text
handle
+
style
+
stats_hash
+
renderer_version
```

For example:

```text
utkarsh-wadalkar
landscape
8912a9...
v3
```

Why `renderer_version`?

Imagine tomorrow you redesign the Landscape card.

The stats haven't changed:

```text
804M
$1,825
#203
```

Without renderer versioning, your backend thinks:

> Same stats → existing image is valid.

But it's actually using the old design.

Increment:

```ts
RENDERER_VERSION = 4;
```

and every card automatically becomes eligible for regeneration.

---

# Prevent duplicate Chromium renders

This is another thing I'd use TiDB for.

Imagine GitHub, your playground and two browsers simultaneously request the same uncached card.

Without protection:

```text
request 1 → launch Chromium
request 2 → launch Chromium
request 3 → launch Chromium
request 4 → launch Chromium
```

Wasteful.

Use a render lock.

Something like:

```text
card_render_lock

handle
style
locked_until
```

Or put it directly into `card_cache`:

```sql
render_status ENUM('ready', 'rendering', 'failed')
render_started_at DATETIME
```

Then:

```text
Request A
 ↓
claims render lock
 ↓
Chromium

Request B
 ↓
sees rendering
 ↓
serves previous card
```

This is particularly valuable on serverless infrastructure.

---

# What about putting the PNG directly in TiDB?

Technically, yes.

You could do:

```sql
image_data MEDIUMBLOB
```

and store the ~197 KB PNG directly.

At your stated 5 GiB row-storage limit:

```text
5 GiB / 197 KB ≈ 26,000 images
```

Ignoring indexes, metadata and storage overhead.

And because you would keep only the latest version:

```text
10,000 users × 3 styles × 197 KB
≈ 5.9 GB
```

So approximately a few thousand users with all three rendered styles could still fit fairly comfortably before approaching the free storage limit.

But storage isn't the main reason I wouldn't do it.

Every cache miss would require TiDB to transfer ~197 KB through a SQL query:

```text
SELECT image_data FROM card_cache ...
```

That consumes more database I/O/RUs and makes the database responsible for something object storage/CDNs are much better at.

I'd rather have TiDB return:

```json
{
 "image_url": "...",
 "stats_hash": "...",
 "rendered_at": "..."
}
```

which is tiny.

Then the image is served through storage/CDN infrastructure.

---

# Use your free TiDB storage for valuable data instead

A typical `card_cache` row might only be 1–3 KB.

Even:

```text
100,000 users
× 3 styles
× ~2 KB
```

is only roughly:

```text
600 MB
```

before indexes/overhead.

Your metadata therefore scales far better than storing PNG binaries.

And the 50M monthly RUs can go toward tiny keyed queries rather than repeatedly transporting image blobs.

---

# I'd structure your caching in 3 layers

```text
 REQUEST
 │
 ▼
 ┌───────────────────┐
 │ Next Data Cache │ L1
 │ completed PNG │
 └─────────┬─────────┘
 │ miss
 ▼
 ┌───────────────────┐
 │ TiDB │ L2
 │ metadata/state │
 │ hash │
 │ render locks │
 │ timestamps │
 └─────────┬─────────┘
 │
 ▼
 ┌───────────────────┐
 │ Blob/Object Store │ L3
 │ persistent PNG │
 └───────────────────┘
```

And separately:

```text
WhoBurnedMore API
 │
 ▼
profile_cache
 │
 ▼
stats changed?
 NO YES
 │ │
 reuse Chromium
 │
 ▼
 new PNG
 │
 ▼
 blob storage
 │
 ▼
 update TiDB
```

---

## For your playground, prewarming becomes excellent

Your existing idea becomes even stronger.

User enters:

```text
utkarsh-wadalkar
```

and chooses:

```text
Landscape
```

Don't immediately show them the README URL.

Do:

```text
Generate
 ↓
fetch stats
 ↓
check TiDB
 ↓
render if necessary
 ↓
store PNG
 ↓
populate Next cache
 ↓
verify image
 ↓
show README snippet
```

Only after that expose:

```md
\[!\[WhoBurnedMore\](https://whoburnedmore-card.vercel.app/api/card/utkarsh-wadalkar/landscape.png)\](...)
```

Therefore GitHub's **first ever request** should already be a cache hit.

That's much better than hoping GitHub waits for first-time Chromium rendering.

---

## Deleting old cards

Your idea here is good, but do it in the correct order:

```text
1. Render new PNG
2. Verify PNG
3. Upload new PNG
4. Update TiDB pointer atomically
5. Invalidate/repopulate Next cache
6. Delete previous PNG
```

Never:

```text
delete old
→ start rendering new
```

because Chromium/render/storage failure would leave a broken card.

You could even keep the previous version for a short grace period and clean it up later.

---

## My recommended MVP stack

For **this specific project**, I'd now settle on:

```text
Next.js + TypeScript
 │
 ├── Frontend playground
 │
 ├── /api/card/*
 │
 └── renderer
 │
 bundled Chromium
 │
 ┌─────┴──────┐
 │ │
 TiDB Blob storage
 metadata PNG
 │
 └──────┬─────┘
 │
 Next Data Cache
```

TiDB handles:

```text
profile cache
stats hashes
render metadata
image pointers
last refresh
render status
distributed rendering locks
```

Blob/object storage handles:

```text
PNG bytes
```

Next Data Cache handles:

```text
very fast hot-card delivery
```

And Chromium should be used **only when `stats_hash` or `renderer_version` changes**.

That gives you the benefits of TiDB's free tier without wasting it on repeated 197 KB image reads, while solving the exact GitHub timeout/re-render problem you're dealing with.

## User

and we can use tidb for instantly loading metadata of website too?

## Assistant

Yes — TiDB can also hold website metadata, and that’s a good use of it.

But for “instant loading,” I’d still avoid making every frontend render depend directly on a fresh TiDB query. Use TiDB as the persistent source, then cache frequently read metadata at the app/CDN layer.

For example, TiDB can store things like:

```text
site_metadata
- total_cards_generated
- total_profiles
- total_requests
- featured_handles
- latest_supported_styles
- renderer_version
- maintenance_flag
- announcements
```

And maybe per-profile metadata:

```text
profile_metadata
- handle
- display_name
- avatar_url
- last_synced_at
- available_styles
- total_card_views
```

Then your website flow becomes:

```text
Browser
 ↓
Next.js page / API
 ↓
Next Data Cache
 ↓ miss
TiDB
```

So common homepage metadata gets cached and loads very quickly.

For example:

```ts
const metadata = unstable_cache(
 async () => getSiteMetadataFromTiDB(),
 \["site-metadata"\],
 { revalidate: 300 }
);
```

Conceptually that gives you:

```text
TiDB = persistent truth
Next cache = fast reads
Vercel CDN = fast delivery
```

That’s better than:

```text
every page load
→ open DB connection
→ query TiDB
→ wait
```

For mostly static content like:

```text
supported card styles
docs text
CLI examples
feature descriptions
```

I would **not** store those in TiDB at all. Keep them in code, because they rarely change.

Use TiDB for metadata that actually changes, such as:

```text
card count
user/profile count
render statistics
recently generated cards
featured profiles
service status
last sync information
```

So the optimized setup is:

```text
Static website content
→ bundled with Next.js

Dynamic website metadata
→ TiDB
→ Next Data Cache

Rendered card metadata
→ TiDB

Rendered PNGs
→ Blob storage

Hot PNG responses
→ Next Data Cache / CDN
```

That gives you fast page loads without turning TiDB into a bottleneck.

One more useful thing: if you show stats like:

```text
12,481 cards generated
3,928 profiles
99.9% cache hit rate
```

don’t calculate those with expensive `COUNT(*)` queries on every page view. Maintain small aggregate rows instead, e.g.:

```text
metrics
- total_cards
- total_profiles
- total_requests
```

Then homepage loading is just a tiny single-row lookup.

So yes — **TiDB is a good fit for dynamic website metadata too**, especially since you already plan to use it for card state. I’d just put Next/Vercel caching in front of it rather than treating TiDB itself as the frontend cache.

## User

yes i want to showoff that users are actually using this service at a status endpoint of website

## Assistant

Yes — that’s a good use of TiDB, and a dedicated `/status` page can make the project feel active and credible.

I’d expose aggregated usage, not raw user data. Something like:

```text
/status
```

showing:

```text
WhoBurnedMore Card Status

Service
Operational

Usage
12,481 cards generated
3,928 unique profiles
184,220 card requests
96.4% cache hit rate

Rendering
Landscape 5,924
Hero 3,811
Report 2,746

Infrastructure
Renderer version v1.4
Last successful render 12 sec ago
Average render time 1.8 s
Average cached response 42 ms

Recent activity
+37 cards generated in the last hour
+412 cards generated today
```

That gives you the “people are actually using this” effect without exposing handles unless you explicitly want a public leaderboard.

I’d slightly change the schema from the earlier generic `site_metadata` idea and make it purpose-built.

```text
service_metrics
- total_cards_generated
- total_unique_profiles
- total_card_requests
- total_cache_hits
- total_cache_misses
- renders_landscape
- renders_hero
- renders_report
- renders_failed
- last_successful_render_at
- renderer_version
- updated_at
```

Then separately:

```text
profile_metadata
- handle
- display_name
- avatar_url
- first_seen_at
- last_seen_at
- last_synced_at
- total_card_views
```

And for time-based charts:

```text
usage_hourly
- bucket_hour
- requests
- unique_profiles
- cards_generated
- cache_hits
- renders
- render_failures
```

That last table is important if you want to show:

```text
Last 24 hours
████████▇▇▆▅▅▆▇████
```

instead of only lifetime counters.

### Don't update TiDB on every image request

This is the main optimization I'd make.

If GitHub hits your image 100,000 times, don't execute:

```sql
UPDATE service_metrics
SET total_card_requests = total_card_requests + 1;
```

100,000 times synchronously.

That would waste RUs and add latency.

Instead:

```text
request
 ↓
serve card immediately
 ↓
increment lightweight cached counter
 ↓
periodically flush aggregate counts → TiDB
```

Or, for the MVP, only record meaningful events:

```text
new profile discovered
new card rendered
cache miss
render failure
```

while keeping raw request counting sampled or aggregated.

### Status page architecture

I'd use:

```text
/status
 ↓
/api/status
 ↓
Next Data Cache
 ↓ every ~30–60 sec
TiDB aggregated metrics
```

So someone refreshing your status page repeatedly doesn't keep hitting TiDB.

For example:

```text
TiDB
 ↓
cache 60 seconds
 ↓
/api/status
 ↓
status UI
```

A one-minute delay is perfectly acceptable for public usage stats.

### Metrics worth showing publicly

I'd expose only the interesting numbers:

- total generated cards
- unique profiles using the service
- total card views/requests
- cards generated today
- requests in the last 24 hours
- cache-hit percentage
- average cached response time
- successful render percentage
- card-style distribution
- renderer/service version
- current operational status

You can also add a small live-looking activity section:

```text
Last 24 hours

Requests
18,291 ↑ 12.4%

Cards generated
412

New profiles
93
```

That will make the project feel much more established.

### I would avoid public handles by default

For example, I'd avoid:

```text
Most viewed users
1. userA
2. userB
3. userC
```

unless users knowingly opt into that.

Aggregated numbers are enough to show adoption:

```text
3,928 developers have generated cards
```

without turning usage into a public tracking system.

And because you're already planning TiDB for card metadata, this doesn't require another service. The clean final architecture becomes:

```text
 WhoBurnedMore
 ↓
 Stats fetch
 ↓
 TiDB
 ↙ ↘
 Card metadata Usage metrics
 ↓ ↓
 Blob / PNG cache /status
 ↓ ↓
 GitHub Public dashboard
```

I'd definitely include `/status` in the product plan. It gives you both operational visibility and a nice adoption/showcase page.

## User

from what we just fixed ans this

## Assistant

Worked for a few seconds

## Assistant

From what we just decided, pick **Vercel Blob**.

Your architecture should be:

```text
TiDB
→ metadata, hashes, render state, usage metrics, status-page data

Vercel Blob
→ persistent PNG files

Next/Vercel cache
→ hot responses for GitHub and website previews
```

So for that prompt, choose:

**1. Vercel Blob — Recommended**

That matches the design we settled on: keep the ~197 KB image bytes out of TiDB and use TiDB for the things databases are actually good at.

The render/update flow should be:

```text
Stats changed
 ↓
Render new PNG
 ↓
Upload → Vercel Blob
 ↓
Update TiDB with:
 image URL
 stats hash
 renderer version
 rendered_at
 ↓
Warm/invalidate Next cache
 ↓
Delete old Blob only after new one is safely active
```

And reads:

```text
GitHub README request
 ↓
Next cache
 ↓ cache miss
TiDB metadata
 ↓
Vercel Blob PNG
```

I would **not choose TiDB BLOB** here. We specifically want your free TiDB RUs/storage available for card metadata, profile state, counters, time-series usage aggregates, `/status` metrics, render locks, etc.—not 197 KB binary transfers.

Cloudflare R2 is worth considering later if image traffic becomes large enough that Vercel Blob pricing/egress becomes unfavorable. For the current Vercel-native MVP, **Vercel Blob is the cleanest choice**. memcite

## Assistant

Pick **1. Next-request refresh**.

That matches the architecture we just designed:

```text
GitHub / playground requests card
 ↓
serve existing PNG immediately
 ↓
check whether upstream stats changed
 ↓
if changed:
render new PNG in background
 ↓
upload to Vercel Blob
 ↓
update TiDB metadata
 ↓
future requests get the new PNG
```

Why this is better for your current MVP:

- no constant polling cost
- much lower TiDB/API usage
- lower load on WhoBurnedMore
- no unnecessary Chromium renders
- stale card is still served instantly
- only active users trigger refresh checks

**Frequent polling** is worth it later only if you need cards to update within a few minutes even when nobody is requesting them.

For now, choose **Next-request refresh**. It is the more efficient and stable option for a free-tier-oriented Vercel + TiDB + Blob setup.

## User

Deployment is currently blocked because the linked Vercel project has no environment variables—neither `DATABASE_URL` nor `BLOB_READ_WRITE_TOKEN` exists. Please connect TiDB and a public Vercel Blob store in Vercel’s Preview environment; don’t paste secrets here. 

step by step guide to do this

## Assistant

Worked for 6s

## Assistant

Do it in this order: **TiDB first, then Vercel Blob, then redeploy Preview**.

### 1. Connect TiDB to Vercel

Because you’re using TiDB Cloud Starter, the cleanest path is the official **TiDB Cloud → Vercel integration**. TiDB can automatically create the required environment variables for the linked Vercel project. citeturn821864search0

Go to your **Vercel Dashboard** → open your `whoburnedmore-card` project → **Integrations** and add **TiDB Cloud**. During setup, select your Vercel project, TiDB organization/project, choose **Cluster**, choose the correct TiDB Starter instance/database, and select the framework your app expects. If your code expects a single `DATABASE_URL`, choose the Prisma/serverless-driver style if offered, because that integration creates `DATABASE_URL` automatically. citeturn821864search0

After connecting, go back to:

```text
Vercel project
→ Settings
→ Environment Variables
```

You want to see:

```text
DATABASE_URL
```

and make sure it applies to **Preview**.

If the integration gives you separate values instead:

```text
TIDB_HOST
TIDB_PORT
TIDB_USER
TIDB_PASSWORD
TIDB_DATABASE
```

but your app specifically expects `DATABASE_URL`, you can manually add one using TiDB's connection details. TiDB documents the Vercel-compatible format as:

```text
mysql://USER:PASSWORD@ENDPOINT:PORT/DATABASE?sslaccept=strict
```

TiDB Starter requires TLS when using the public endpoint. citeturn821864search0turn821864search2

Do **not** send that value here.

---

### 2. Create the Vercel Blob store

Now in Vercel, open the same project and go to the **Storage** area.

Create a new **Blob** store and choose:

```text
Public
```

for this project, because these are public GitHub README card images.

Connect that Blob store to your `whoburnedmore-card` project.

When a Blob store is connected to a Vercel project, Vercel supplies the SDK authentication environment variable:

```text
BLOB_READ_WRITE_TOKEN
```

Vercel documents that this token is automatically added when the Blob store is linked to the project. citeturn821864search1

Then verify under:

```text
Project
→ Settings
→ Environment Variables
```

that you now have:

```text
BLOB_READ_WRITE_TOKEN
```

and that it is available to **Preview**.

---

### 3. Verify both variables are scoped to Preview

At this point, under **Settings → Environment Variables**, you should have:

```text
DATABASE_URL
BLOB_READ_WRITE_TOKEN
```

Both need **Preview** enabled.

Vercel lets each environment variable be scoped separately to Production, Preview, and Development. citeturn821864search3

For now I would configure:

```text
DATABASE_URL
✓ Preview
✓ Production ← optional now, but useful soon

BLOB_READ_WRITE_TOKEN
✓ Preview
✓ Production ← optional now, but useful soon
```

If you specifically want to test everything before production, Preview-only is fine initially.

---

### 4. Important: redeploy after adding the variables

Adding environment variables does **not** modify an already-running deployment.

Vercel requires a new deployment for newly added environment variables to take effect. citeturn821864search3

Go to:

```text
Project
→ Deployments
→ latest Preview deployment
→ ⋯
→ Redeploy
```

Or push another commit to the preview branch.

After redeploying, the function should see:

```ts
process.env.DATABASE_URL
process.env.BLOB_READ_WRITE_TOKEN
```

---

### 5. Verify from the deployment logs

Open the new Preview deployment:

```text
Deployments
→ Preview deployment
→ Logs
```

You should no longer see errors like:

```text
DATABASE_URL is missing
```

or:

```text
BLOB_READ_WRITE_TOKEN is missing
```

You should instead see database initialization/migration or Blob initialization succeeding.

Do **not** log the actual environment-variable values.

Good:

```ts
console.log("DATABASE_URL configured:", Boolean(process.env.DATABASE_URL));
console.log(
 "BLOB_READ_WRITE_TOKEN configured:",
 Boolean(process.env.BLOB_READ_WRITE_TOKEN)
);
```

Bad:

```ts
console.log(process.env.DATABASE_URL);
console.log(process.env.BLOB_READ_WRITE_TOKEN);
```

---

### 6. One thing to check with TiDB migrations

If your deployment runs something like:

```bash
prisma migrate deploy
```

or your own schema setup, verify the database actually exists in TiDB first.

In TiDB Cloud:

```text
My TiDB
→ your Starter instance
→ Connect
```

The connection dialog gives you the username, password, endpoint, port and database details. citeturn821864search5

Your app should then create/use the tables we discussed for things such as:

```text
card_cache
profile_cache
service_metrics
usage_hourly
```

depending on what your current implementation has actually created.

---

### 7. Final expected setup

You should end up with:

```text
Vercel Project
│
├── Preview deployment
│
├── Environment Variables
│ ├── DATABASE_URL
│ │ ↓
│ │ TiDB Cloud Starter
│ │
│ └── BLOB_READ_WRITE_TOKEN
│ ↓
│ Public Vercel Blob
│
├── Next.js app
│
├── TiDB
│ ├── card metadata
│ ├── hashes
│ ├── render state
│ └── status/usage metrics
│
└── Vercel Blob
 └── persistent PNG cards
```

For your architecture, **do not create a private Blob store**. The generated PNGs are intended to be fetched by GitHub READMEs, so public Blob storage is the appropriate choice. citeturn821864search1

One more useful check: after everything is connected, test the Preview URL by generating your own `utkarsh-wadalkar` Landscape card first. That should exercise **TiDB → renderer → Vercel Blob → cache → image endpoint** end-to-end before you point GitHub at it.

## User

1. Open TiDB Cloud’s SQL Editor and run:

```
CREATE DATABASE whoburnedmore_card;
```

2. Return to the integration form and select `whoburnedmore_card`.
3. Keep **Framework: General**.
4. Enable **Branching** for preview deployments.
5. Click **Add Integration and Return to Vercel**.

I updated the application to accept the integration’s `TIDB_HOST`, `TIDB_PORT`, `TIDB_USER`, `TIDB_PASSWORD`, and `TIDB_DATABASE` variables automatically. It now defensively refuses `sys` and other system schemas. All 14 tests, typecheck, and production build pass.

After connecting TiDB, connect a public Vercel Blob store too, then tell me to continue.

Skill used: `vercel:env-vars`.

## Assistant

Worked for 5s

## Assistant

That instruction is now aligned with your app changes. Since your code accepts the **General** TiDB integration variables, you do **not** need `DATABASE_URL` anymore.

Do exactly this:

1. In **TiDB Cloud**, open your Starter instance → **SQL Editor** and run:
 ```sql
 CREATE DATABASE whoburnedmore_card;
 ```
 Then confirm the database appears.

2. Go back to the **TiDB Cloud ↔ Vercel integration** form and select:
 - Connection type: **Cluster**
 - Database: `whoburnedmore_card`
 - Framework: **General**
 - Branching: **Enabled**

 With Framework = General, TiDB should inject these variables into Vercel automatically:
 ```text
 TIDB_HOST
 TIDB_PORT
 TIDB_USER
 TIDB_PASSWORD
 TIDB_DATABASE
 ```
 That is exactly what TiDB currently documents for the General integration. citeturn293453search0

3. Click **Add Integration and Return to Vercel**.

4. In Vercel, open:
 ```text
 Project
 → Settings
 → Environment Variables
 ```
 Verify those five `TIDB_*` variables exist. Do not copy their values here.

5. Because you enabled **Branching**, TiDB can create isolated database branches for Vercel Preview deployments, so preview code does not have to modify your main database. TiDB currently supports this for GitHub-connected Vercel projects, and Starter organizations have a limited number of branches, so remember to remove old preview branches eventually. citeturn293453search0turn293453search2

6. Next, create/connect the **Vercel Blob** store. For your README cards choose:
 ```text
 Public Blob
 ```
 because GitHub needs to fetch the generated PNG without authentication.

One correction to the earlier deployment message: Vercel Blob changed in 2026. **New Blob project connections now use OIDC authentication by default**, so you may not necessarily see a long-lived `BLOB_READ_WRITE_TOKEN`. The current `@vercel/blob` SDK can authenticate automatically on Vercel using the project's OIDC token. citeturn293453search3

So if your code currently explicitly checks:

```ts
process.env.BLOB_READ_WRITE_TOKEN
```

and refuses to start without it, I would change that before proceeding. Prefer letting the current `@vercel/blob` SDK use Vercel's OIDC authentication. A legacy/existing Blob setup can still use `BLOB_READ_WRITE_TOKEN`, but it should not be your hard requirement for a newly connected store. citeturn293453search3

Your final Vercel setup should therefore look like:

```text
TiDB
├── TIDB_HOST
├── TIDB_PORT
├── TIDB_USER
├── TIDB_PASSWORD
└── TIDB_DATABASE

Vercel Blob
└── OIDC authentication
 (BLOB_READ_WRITE_TOKEN only if using legacy/token auth)
```

After both integrations are connected, **redeploy the Preview deployment**. TiDB notes that Preview env vars created by Branching may occasionally require a redeploy because of Vercel deployment timing. citeturn293453search0

Then tell your coding agent:

> TiDB and the public Vercel Blob store are connected. Continue with the deployment and verify the Preview environment end-to-end.

That is the point where it should proceed with schema initialization, Blob writes, card prewarming, and the actual Preview card test.

## User

what should i do here

## Assistant

Worked for 4s

## Assistant

You’re on the correct TiDB Cloud page. You already have one active **Starter** instance, so **don’t create another instance**.

Click your existing instance:

**`ai-interview-qs-prod`**

Then inside that instance, look for **SQL Editor** / **SQL Console**. Open it and run:

```sql
CREATE DATABASE whoburnedmore_card;
```

After that, verify it exists with:

```sql
SHOW DATABASES;
```

You should see:

```text
whoburnedmore_card
```

Then go back to the **TiDB → Vercel integration** flow and choose:

```text
Cluster/Instance: ai-interview-qs-prod
Database: whoburnedmore_card
Framework: General
Branching: Enabled
```

Then click **Add Integration and Return to Vercel**.

Using the same TiDB Starter instance for both your older AIDEO database and this new `whoburnedmore_card` database is fine. They remain logically separate databases inside the same TiDB instance, and this avoids wasting one of your free-instance slots. memcite

## Assistant

Looks good. Your screenshot shows that:

- the `whoburnedmore_card` schema exists
- `USE whoburnedmore_card;` succeeded
- TiDB says **“Query OK. Database changed!”**

So the database side is ready.

Next do this:

1. Go to **Integrations** in the left sidebar.
2. Open/connect the **Vercel integration**.
3. Choose this TiDB instance:
 `wbm-card-Instance`
4. Choose database:
 `whoburnedmore_card`
5. Keep **Framework = General**
6. Enable **Branching** for Preview deployments
7. Finish with **Add Integration and Return to Vercel**

Then in Vercel, verify these environment variables were added for Preview:

```text
TIDB_HOST
TIDB_PORT
TIDB_USER
TIDB_PASSWORD
TIDB_DATABASE
```

After that, connect the **public Vercel Blob store** to the same Vercel project.

Once both TiDB and Blob are connected, redeploy the Preview deployment and continue with the app.

## User

this window is not closing

## Assistant

Worked for 6s

## Assistant

You can just close it manually. The important part is that it already says **Installation Complete**.

What likely happened is the popup’s auto-close callback got stuck or the browser blocked the close action. That does **not** necessarily mean the TiDB integration failed.

Do this:

1. Click the **X** in the top-right of that popup/window.
2. Go back to your Vercel project.
3. Open **Settings → Environment Variables**.
4. Check whether these now exist:
 ```text
 TIDB_HOST
 TIDB_PORT
 TIDB_USER
 TIDB_PASSWORD
 TIDB_DATABASE
 ```
5. Also check **Integrations** and confirm TiDB Cloud is listed as connected.

If those variables are present, the integration succeeded and you can ignore the stuck popup.

If they are **not** present, refresh Vercel once and check again. If still missing, then reopen the TiDB integration and retry the connection.

## Assistant

This confirms the TiDB ↔ Vercel integration is connected correctly.

I can see:

- Vercel project: `whoburnedmore-card`
- TiDB organization: `Utkarsh's Org`
- TiDB project: `wbm-card-final`
- Connection type: `Cluster / wbm-card-cluster`
- Branching: **Enabled**

So TiDB is done.

Now go back to Vercel and do the Blob part:

```text
Vercel Dashboard
→ whoburnedmore-card
→ Storage
→ Create Database / Create Store
→ Blob
```

Choose a **public Blob store** and connect it to the same project.

After that, check:

```text
Project
→ Settings
→ Environment Variables
```

You should see the TiDB variables, typically:

```text
TIDB_HOST
TIDB_PORT
TIDB_USER
TIDB_PASSWORD
TIDB_DATABASE
```

and Blob should also be connected through Vercel’s current Blob auth setup.

Then redeploy your latest Preview deployment.

At that point, you can tell your coding agent:

> TiDB is connected with Branching enabled, and the public Vercel Blob store is connected. Continue with deployment and verify the Preview environment end-to-end.

You do **not** need to click **Add Link** again on the TiDB page. The existing row already proves the link exists.

## Assistant

You’re at the right screen. Use these settings:

- **Store Name:** `whoburnedmore-card-blob` — good
- **Region:** leave the default unless you have a specific reason to colocate elsewhere
- **Access:** choose **Public**
- **Custom Environment Variable Prefix:** leave as `BLOB`

Most importantly, check:

**“Add a read-write token env var to this connection”**

Your app currently expects writable Blob access for uploading rendered PNGs, so you want Vercel to create the read/write credential in addition to the store ID/public key.

Then click **Create**.

After creation, go to:

```text
Vercel Project
→ Environment Variables
```

and verify Blob-related variables exist for both **Preview** and **Production**. Based on the prefix shown, you should see variables beginning with `BLOB_`, and if you enabled the checkbox, a read/write token variable as well.

Then redeploy the latest Preview deployment so the new variables are available to the app.

For your use case, **Public** is definitely correct because GitHub READMEs need to fetch those PNG URLs without authentication.

## User

i want to delete this

## Assistant

Worked for 11s

## Assistant

Yes. To delete that **Vercel Blob store**:

1. Click the `whoburnedmore-card-blob` store card you’re viewing.
2. Open its **Settings** page.
3. Scroll to the bottom for the **Danger Zone**.
4. Choose **Delete Store** / **Delete Blob Store**.
5. Confirm the store name if Vercel asks you to type it, then confirm deletion.

Deleting the store will also remove the blobs inside it, so only do this if you don’t need anything stored there. Vercel Blob data persists until you delete it, so this is the correct way to fully remove the store. citeturn326454search6

After deleting it, I’d create the replacement again as:

```text
Name: whoburnedmore-card-blob
Access: Public
Prefix: BLOB
```

and connect it to both **Preview** and **Production**.

## Assistant

This screenshot shows the Blob side is configured correctly, but there’s one important issue with TiDB.

Your Blob variables are good and available to both environments:

- `BLOB_WEBHOOK_PUBLIC_KEY` → Production and Preview
- `BLOB_STORE_ID` → Production and Preview
- `BLOB_READ_WRITE_TOKEN` → Production and Preview

That means the Blob connection is ready.

The problem is your TiDB variables are currently scoped only to:

`Production`

I can see:

- `TIDB_HOST` → Production
- `TIDB_PORT` → Production
- `TIDB_USER` → Production
- `TIDB_PASSWORD` → Production
- `TIDB_DATABASE` → Production

Since you want to test a **Preview deployment**, those variables need to be available in **Preview** too.

For each `TIDB_*` variable, click the `...` menu on the right, edit the environment scope, and change it from:

```text
Production
```

to:

```text
Production and Preview
```

Do that for all five TiDB variables.

After that, your environment list should effectively look like:

```text
BLOB_WEBHOOK_PUBLIC_KEY Production and Preview
BLOB_STORE_ID Production and Preview
BLOB_READ_WRITE_TOKEN Production and Preview

TIDB_HOST Production and Preview
TIDB_PORT Production and Preview
TIDB_USER Production and Preview
TIDB_PASSWORD Production and Preview
TIDB_DATABASE Production and Preview
```

Then redeploy the latest Preview deployment.

One caveat: because you enabled **TiDB Branching**, the integration may manage Preview credentials dynamically. If Vercel/TiDB does not let you simply enable Preview on those same five variables, don’t manually copy production DB credentials into Preview. In that case, go back to the TiDB integration and verify the branching configuration is creating Preview-specific variables automatically.

But based on this screenshot, the immediate issue is clear: **Blob is ready; TiDB is still Production-only.**

## Resources

### Local attachments
- [7600c75f-cd26-4ec0-bfaa-528730706d1a.png](../../../Raw/Export/file_0000000060a48243a1ea2a8508c00fff.dat)
- [2c0ccd93-9236-4611-a21b-312b15cbbe76.png](../../../Raw/Export/file_0000000089a081f4b842c2f31aaf5cf1.dat)
- [558d3cf6-194f-43ed-abba-a7cd27861b9a.png](../../../Raw/Export/file_00000000489881fa8a88d81d761b5ea5.dat)
- [44b50c73-6a24-43fe-b5f7-bf7b317aec4d.png](../../../Raw/Export/file_00000000deac8206b5e17b65d6cf0d0b.dat)
- [d2387095-63bd-4d8d-a8d0-6ec3c8449d7e.png](../../../Raw/Export/file_000000001008820696d580fd75c2ff63.dat)
- [63c09e1f-dd8c-47a6-a125-99f8925db44a.png](../../../Raw/Export/file_00000000416481f89f4ff6e99662d7f3.dat)

### External references
- [whoburnedmore - npm](https://www.npmjs.com/package/whoburnedmore?utm_source=chatgpt.com)
- [whoburnedmore — AI Token Leaderboard](https://whoburnedmore.com/?utm_source=chatgpt.com)
- [best-practices-badge/docs/api.md at main · ossf/best-practices-badge · GitHub](https://github.com/ossf/best-practices-badge/blob/main/docs/api.md?utm_source=chatgpt.com)
- [GitHub - specstoryai/badges: SVG badges for visualizing AI-assisted development activity in GitHub repositories using SpecStory · GitHub](https://github.com/specstoryai/badges?utm_source=chatgpt.com)
- [GitHub - pujux/badge-it: An API serving useful badges for your GitHub Profile README 🚀🎉 Formerly known as git-badges. · GitHub](https://github.com/pujux/badge-it?utm_source=chatgpt.com)
- [GitHub - home-operations/kromgo: Build badges and graphs from PromQL and share them in your READMEs · GitHub](https://github.com/home-operations/kromgo?utm_source=chatgpt.com)
- [GitHub - tluhk/counter-api: API for counting visits · GitHub](https://github.com/tluhk/counter-api?utm_source=chatgpt.com)
- [GitHub - Vermaarp/profile-views: Open-source profile view counter for GitHub READMEs. Glass-style SVG badges, unique/daily stats, per-repo sub-counters, bot filtering, hashed IPs. Deploys to Deno Deploy free tier. · GitHub](https://github.com/Vermaarp/profile-views?utm_source=chatgpt.com)
- [GitHub - LukenSkyne/Badges: a customizable badge api with the ability to fetch third-party data · GitHub](https://github.com/LukenSkyne/Badges?utm_source=chatgpt.com)
- [GitHub - cncf/landscapeapp: 🌄Upstream landscape generation application · GitHub](https://github.com/cncf/landscapeapp?utm_source=chatgpt.com)
- [GitHub - warengonzaga/github-repo-banner: URL-based repository banners. Think shields.io, but for headers. ✨ · GitHub](https://github.com/warengonzaga/github-repo-banner?utm_source=chatgpt.com)
- [Readme SVG Toolkit · GitHub](https://github.com/readme-SVG?utm_source=chatgpt.com)
- [shields/badge-maker/README.md at master · badges/shields · GitHub](https://github.com/badges/shields/blob/master/badge-maker/README.md?utm_source=chatgpt.com)
- [shields/README.md at master · badges/shields · GitHub](https://github.com/badges/shields/blob/master/README.md?utm_source=chatgpt.com)
- [GitHub - open-educational-badges/badgr-server: Open Badge issuing and management with Django · GitHub](https://github.com/open-educational-badges/badgr-server?utm_source=chatgpt.com)
- [Best Resources for Young AI Founders in India](https://aigrants.in/topics/best-resources-for-young-ai-founders-india?utm_source=chatgpt.com)
- [AI Startup Residency Program: Empowering Innovators](https://aigrants.in/topics/ai-startup-residency-program?utm_source=chatgpt.com)
- [AI Innovation Grants for Indian Student Developers](https://aigrants.in/topics/ai-innovation-grants-for-indian-student-developers?utm_source=chatgpt.com)
- [Aditya Pundir (@adipundir): AI Token Usage — whoburnedmore](https://whoburnedmore.com/u/adipundir?utm_source=chatgpt.com)
- [Codex Weekly Limit Reset: How to Plan — whoburnedmore](https://whoburnedmore.com/guides/codex-weekly-limit-reset?utm_source=chatgpt.com)
- [How to Check opencode Token Usage and Cost — whoburnedmore](https://whoburnedmore.com/guides/check-opencode-usage?utm_source=chatgpt.com)
- [How to Check Warp AI Usage & Cost — whoburnedmore](https://whoburnedmore.com/guides/check-warp-usage?utm_source=chatgpt.com)
- [How to Check Aider Token Usage & Cost — whoburnedmore](https://whoburnedmore.com/guides/check-aider-usage?utm_source=chatgpt.com)
- [How to Check Codex CLI Usage and Token Cost — whoburnedmore](https://whoburnedmore.com/guides/check-codex-cli-usage?utm_source=chatgpt.com)
- [Claude Code Usage Limit Reached? Here's Why — whoburnedmore](https://whoburnedmore.com/guides/claude-code-usage-limit-reached?utm_source=chatgpt.com)
- [Best AI Coding Token Tracker 2026 — whoburnedmore — whoburnedmore](https://whoburnedmore.com/guides/best-ai-coding-token-tracker-2026?utm_source=chatgpt.com)
- [How to Check Qwen Code Usage & Limits — whoburnedmore](https://whoburnedmore.com/guides/check-qwen-code-usage?utm_source=chatgpt.com)
- [OpenAI Codex Credit Billing in 2026 — whoburnedmore](https://whoburnedmore.com/guides/codex-credits-billing-2026?utm_source=chatgpt.com)
- [Most Popular AI Coding Models — Live Data — whoburnedmore](https://whoburnedmore.com/research/ai-model-adoption?utm_source=chatgpt.com)
- [AI Token Leaderboards for Teams — whoburnedmore](https://whoburnedmore.com/for-teams?utm_source=chatgpt.com)
- [做个游戏 (@ezgameworkplace): AI Token Usage — whoburnedmore](https://whoburnedmore.com/u/ezgameworkplace?utm_source=chatgpt.com)
- [Hermes Agent Token Usage: Cost & History — whoburnedmore](https://whoburnedmore.com/guides/check-hermes-agent-usage?utm_source=chatgpt.com)
- [API documentation](https://arkhamdb.com/api/doc?utm_source=chatgpt.com)
- [arhxam/whoburnedmore — GitHub trending stats & insights](https://trendshift.io/repositories/55233?utm_source=chatgpt.com)
- [RepoPulse - GitHub Intelligence Engine](https://repopulse-one.vercel.app/?utm_source=chatgpt.com)
- [Backend | star-history/star-history | DeepWiki](https://deepwiki.com/star-history/star-history/4-backend?utm_source=chatgpt.com)
- [GitHub - github/octocanvas: A web app that creates GitHub-themed collectibles from GitHub profiles · GitHub](https://download.plaud.ai/github/octocanvas?utm_source=chatgpt.com)
- [Academy of mine APIs | Academy of Mine](https://docs.academyofmine.com/api/?utm_source=chatgpt.com)
- [Integrate TiDB Cloud with Vercel | TiDB Docs](https://docs.pingcap.com/tidbcloud/integrate-tidbcloud-with-vercel/?utm_source=chatgpt.com)
- [Connect to TiDB | TiDB Docs](https://docs.pingcap.com/ai/connect/?utm_source=chatgpt.com)
- [Private storage for Vercel Blob, now available in public beta - Vercel](https://vercel.com/changelog/private-storage-for-vercel-blob-now-available-in-public-beta?utm_source=chatgpt.com)
- [Settings | Vercel Academy](https://vercel.com/academy/vercel-foundations/vercel-settings?utm_source=chatgpt.com)
- [TiDB Cloud Quick Start | TiDB Docs](https://docs.pingcap.com/tidbcloud/tidb-cloud-quickstart/?utm_source=chatgpt.com)
- [Connect to TiDB Cloud Starter or Essential via Public Endpoint | TiDB Docs](https://docs.pingcap.com/tidbcloud/connect-via-standard-connection-serverless/?utm_source=chatgpt.com)
- [Integrate TiDB Cloud with Netlify | TiDB Docs](https://docs.pingcap.com/tidbcloud/integrate-tidbcloud-with-netlify/?utm_source=chatgpt.com)
- [集成 TiDB Cloud 与 Vercel | TiDB 文档中心](https://docs.pingcap.com/zh/tidbcloud/integrate-tidbcloud-with-vercel/?utm_source=chatgpt.com)
- [Select a Plan | TiDB Docs](https://docs.pingcap.com/tidbcloud/select-cluster-tier/?utm_source=chatgpt.com)
- [TiDB Cloud Serverless Driver Prisma Tutorial | TiDB Docs](https://docs.pingcap.com/developer/serverless-driver-prisma-example/?utm_source=chatgpt.com)
- [Create a TiDB Cloud Starter Instance | TiDB Docs](https://docs.pingcap.com/developer/dev-guide-build-cluster-in-cloud/?utm_source=chatgpt.com)
- [Import Data into TiDB Cloud Starter or Essential via MySQL CLI | TiDB Docs](https://docs.pingcap.com/tidbcloud/import-with-mysql-cli-serverless/?utm_source=chatgpt.com)
- [Connect to TiDB with mysql2 in Next.js | TiDB Docs](https://docs.pingcap.com/developer/dev-guide-sample-application-nextjs/?utm_source=chatgpt.com)
- [Integrate TiDB Cloud with Vercel | TiDB Docs](https://docs.pingcap.com/ja/tidbcloud/integrate-tidbcloud-with-vercel/?utm_source=chatgpt.com)
- [Environment Variables UI - Vercel](https://vercel.com/blog/environment-variables-ui?utm_source=chatgpt.com)
- [Secure Marketplace credentials with Production-only access - Vercel](https://vercel.com/changelog/secure-marketplace-credentials-with-production-only-access?utm_source=chatgpt.com)
- [Environment Variables | Vercel Academy](https://vercel.com/academy/svelte-on-vercel/environment-variables?utm_source=chatgpt.com)
- [Vercel Blob now supports OIDC authentication - Vercel](https://vercel.com/changelog/vercel-blob-now-supports-oidc-authentication?utm_source=chatgpt.com)
- [Preview Deployments | Vercel Academy](https://vercel.com/academy/svelte-on-vercel/preview-deployments?utm_source=chatgpt.com)
- [Environments | Vercel Knowledge Base](https://vercel.com/kb/environments?utm_source=chatgpt.com)
- [Vercel Sandbox now accepts environment variables at creation - Vercel](https://vercel.com/changelog/vercel-sandbox-now-accepts-environment-variables-at-creation?utm_source=chatgpt.com)
- [Deploy to Production | Vercel Academy](https://vercel.com/academy/subscription-store/deploy-to-production?utm_source=chatgpt.com)
- [TRUSTED_SOURCES_ENVIRONMENT_MISMATCH](https://vercel.com/docs/errors/trusted_sources_environment_mismatch?utm_source=chatgpt.com)
- [Environments Variables per Git branch - Vercel](https://vercel.com/changelog/environments-variables-per-git-branch?utm_source=chatgpt.com)
- [ServerlessWP - Vercel](https://vercel.com/templates/template/serverless-wordpress?utm_source=chatgpt.com)
- [Can't check off Production Environment from Environment Variable Settings for Preview Project](https://community.vercel.com/t/cant-check-off-production-environment-from-environment-variable-settings-for-preview-project/571?utm_source=chatgpt.com)
- [Next.js Image Gallery Starter Template - Vercel](https://vercel.com/templates/template/image-gallery-starter?utm_source=chatgpt.com)
- [Create private blob stores with a single click in v0 - Vercel](https://vercel.com/changelog/create-private-blob-stores-with-a-single-click-in-v0?utm_source=chatgpt.com)
- [Remotion on Vercel - Vercel](https://examples.vercel.com/templates/next.js/remotion-on-vercel?utm_source=chatgpt.com)
- [Vercel Private Blob is now generally available - Vercel](https://vercel.com/changelog/vercel-private-blob-is-now-generally-available?utm_source=chatgpt.com)
- [Payload Website Starter - Vercel](https://vercel.com/templates/next.js/payload-website-starter?utm_source=chatgpt.com)
- [ServerlessWP - Vercel](https://vercel.com/templates/other/serverless-wordpress?utm_source=chatgpt.com)
- [Vercel Blob public URLs return 503 Service Unavailable while API is functional](https://community.vercel.com/t/vercel-blob-public-urls-return-503-service-unavailable-while-api-is-functional/36291?utm_source=chatgpt.com)
- [Vercel Blob: Any file, any format, on Vercel - Vercel](https://vercel.com/storage/blob?utm_source=chatgpt.com)
- [Vercel Blob now supports consistent reads on private storage - Vercel](https://vercel.com/changelog/vercel-blob-now-supports-consistent-reads-on-private-storage?utm_source=chatgpt.com)
- [TiDB Cloud Branching (PREVIEW) Overview | TiDB Docs](https://docs.pingcap.com/tidbcloud/branch-overview/?utm_source=chatgpt.com)
- [ServerlessWP](https://vercel.com/templates/cms/serverless-wordpress?utm_source=chatgpt.com)
- [Introducing Vercel Connect - Vercel](https://vercel.com/blog/introducing-vercel-connect?utm_source=chatgpt.com)
- [Manage TiDB Cloud Branches | TiDB Docs](https://docs.pingcap.com/tidbcloud/branch-manage/?utm_source=chatgpt.com)
- [Data Service (PREVIEW) | TiDB Docs](https://docs.pingcap.com/tidbcloud/data-service-concepts/?utm_source=chatgpt.com)
- [Quick Start Guide for the TiDB Database Platform - v7.5 | TiDB Docs](https://docs.pingcap.com/tidb/v7.5/quick-start-with-tidb/?utm_source=chatgpt.com)
- [Connect to Your TiDB Cloud Dedicated Cluster | TiDB Docs](https://docs.pingcap.com/tidbcloud/connect-to-tidb-cluster/?utm_source=chatgpt.com)
- [System Variables | TiDB Docs](https://docs.pingcap.com/tidb/stable/system-variables/?utm_source=chatgpt.com)
- [Get Started with Data Service | TiDB Docs](https://docs.pingcap.com/tidbcloud/data-service-get-started/?utm_source=chatgpt.com)
- [Features | TiDB Docs](https://docs.pingcap.com/tidbcloud/features/?utm_source=chatgpt.com)
- [Signed URLs are now available for Vercel Blob - Vercel](https://vercel.com/changelog/signed-urls-are-now-available-for-vercel-blob?utm_source=chatgpt.com)
- [Vercel Blob | Vercel Knowledge Base](https://vercel.com/kb/vercel-blob?utm_source=chatgpt.com)
- [Vercel Blob | Vercel Knowledge Base](https://domains.vercel.com/kb/vercel-blob?utm_source=chatgpt.com)
- [Vercel CLI now supports signing blob URLs - Vercel](https://vercel.com/changelog/vercel-cli-now-supports-signing-blob-urls?utm_source=chatgpt.com)
