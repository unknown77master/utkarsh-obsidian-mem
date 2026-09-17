---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a8febb2-853c-83ee-91a2-42544b24c129"
created: 1787816955.781771
updated: 1787828628.351543
resource_section: true
---

# Configure Codex Plus Subscription

## User

i bougth plus subscription but codex is configured for model = "combo"
model_provider = "omniroute"

notify = \[ "C:\\Users\\ASUS\\AppData\\Local\\OpenAI\\Codex\\runtimes\\cua_node\\57937f104cca4dc5\\bin\\node_modules\\@oai\\sky\\bin\\windows\\codex-computer-use.exe", "turn-ended" \]
\[model_providers.omniroute\]
name = "OmniRoute"
base_url = "http://localhost:20128/v1"
env_key = "OMNIROUTE_API_KEY"
wire_api = "responses"

i wnat to load everything in this account to codex and use plus subscription of openai

## Assistant

Worked for 5s

## Assistant

Yes. Right now your Codex is **not using your ChatGPT Plus subscription**. This line overrides normal OpenAI/ChatGPT authentication:

```toml
model_provider = "omniroute"
```

and your requests are being sent to:

```toml
base_url = "http://localhost:20128/v1"
```

So OmniRoute is currently acting as the model backend.

Your **ChatGPT Plus plan includes Codex usage**, and OpenAI supports signing into Codex CLI/IDE directly using the same ChatGPT account. citeturn128214search0turn128214search4

### 1. Back up your current config

On Windows, your config should normally be here:

```powershell
notepad $env:USERPROFILE\.codex\config.toml
```

Save your OmniRoute configuration somewhere because you may want it again.

### 2. Remove the OmniRoute override

For using your Plus subscription, I recommend reducing `config.toml` to something like:

```toml
notify = \[ "C:\\Users\\ASUS\\AppData\\Local\\OpenAI\\Codex\\runtimes\\cua_node\\57937f104cca4dc5\\bin\\node_modules\\@oai\\sky\\bin\\windows\\codex-computer-use.exe", "turn-ended" \]
```

Specifically remove:

```toml
model = "combo"
model_provider = "omniroute"

\[model_providers.omniroute\]
name = "OmniRoute"
base_url = "http://localhost:20128/v1"
env_key = "OMNIROUTE_API_KEY"
wire_api = "responses"
```

You **do not need an OpenAI API key** to consume your included Plus Codex allowance. You want **ChatGPT sign-in**, not API-key billing. OpenAI explicitly distinguishes Codex configured with ChatGPT sign-in from API/provider configurations. citeturn128214search0turn128214search2

### 3. Log out of the existing Codex authentication

Run:

```powershell
codex logout
```

Then:

```powershell
codex
```

Codex should offer a sign-in flow. Choose:

**Sign in with ChatGPT**

A browser window should open. Sign in using **the exact OpenAI account on which you bought Plus**.

Do **not** choose API-key authentication if your goal is to consume your Plus Codex allowance.

### 4. Verify it

Inside Codex, run:

```text
/status
```

You want the status to indicate that you're authenticated through your ChatGPT/OpenAI account rather than `omniroute`.

You can also check:

```powershell
codex --version
```

I'd update Codex first if you're running an older version:

```powershell
npm install -g @openai/codex@latest
```

Then restart your terminal/IDE.

### About "load everything in this account to Codex"

There's an important distinction here. Signing Codex into this ChatGPT account will give Codex access to the **Codex capabilities and usage included with your Plus subscription**. It does **not mean every normal ChatGPT conversation/memory automatically becomes part of every local Codex session**.

Your local repositories, `AGENTS.md`, Codex instructions, plugins/integrations available to Codex, and Codex-specific account features can be used there. OpenAI now supports Codex across the CLI, IDE extension, web and desktop through the same ChatGPT login. citeturn128214search0

So your desired setup should essentially become:

```text
ChatGPT Plus account
 │
 │ Sign in with ChatGPT
 ▼
 Codex CLI
 │
 ├── OpenAI models
 ├── Plus Codex allowance
 ├── local repositories
 ├── AGENTS.md / skills
 └── Codex account features
```

instead of:

```text
Codex
 │
 ▼
OmniRoute localhost:20128
 │
 ▼
Third-party/provider routing
```

And yes — **you can completely stop using OmniRoute for Codex now and use your Plus subscription directly.** citeturn128214search0

## User

now i want to add .claude plugins in codex, either from marketplace or from:
{
 "permissions": {
 "defaultMode": "auto"
 },
 "model": "combo",
 "hooks": {
 "SessionStart": \[
 {
 "matcher": "startup|resume",
 "hooks": \[
 {
 "type": "command",
 "command": "\"C:\\Users\\ASUS\\AppData\\Local\\jcode\\bin\\jcode.exe\" setup-hotkey --notify-cli-launch claude",
 "timeout": 5
 }
 \]
 }
 \]
 },
 "worktree": {
 "baseRef": "head"
 },
 "enabledPlugins": {
 "frontend-design@claude-plugins-official": true,
 "superpowers@claude-plugins-official": true,
 "skill-creator@claude-plugins-official": true,
 "feature-dev@claude-plugins-official": true,
 "chrome-devtools-mcp@claude-plugins-official": true,
 "firecrawl@claude-plugins-official": true,
 "swift-lsp@claude-plugins-official": true
 },
 "alwaysThinkingEnabled": false,
 "effortLevel": "xhigh",
 "modelSettings": {
 "combo": {
 "effortLevel": "high"
 }
 },
 "askUserQuestionTimeout": "never",
 "autoUpdatesChannel": "latest",
 "skipWorkflowUsageWarning": true,
 "theme": "dark",
 "editorMode": "normal",
 "preferredNotifChannel": "terminal_bell",
 "autoCompactEnabled": true,
 "autoContinueAtUsageLimit": true,
 "crossSessionInbound": "accept",
 "useAutoModeDuringPlan": true
}

## Assistant

Worked for a couple of seconds

## Assistant

Yes — but Claude’s `enabledPlugins` block cannot be copied into Codex config as-is. Claude Code and Codex use different plugin systems.

As of August 2026, Codex has its own **Plugin Directory**, and Codex plugins can bundle skills, apps/MCP-backed tools, instructions, and workflows. Your Plus plan can access plugins, though availability can still depend on the plugin and surface. citeturn208644search0turn208644search4

For your Claude list:

```json
"enabledPlugins": {
 "frontend-design@claude-plugins-official": true,
 "superpowers@claude-plugins-official": true,
 "skill-creator@claude-plugins-official": true,
 "feature-dev@claude-plugins-official": true,
 "chrome-devtools-mcp@claude-plugins-official": true,
 "firecrawl@claude-plugins-official": true,
 "swift-lsp@claude-plugins-official": true
}
```

think of the migration like this:

| Claude plugin | Best Codex equivalent |
|---|---|
| `frontend-design` | Codex plugin/skill |
| `superpowers` | Codex plugin/skills |
| `skill-creator` | Codex skill/plugin authoring |
| `feature-dev` | Codex plugin/skill |
| `chrome-devtools-mcp` | MCP/app integration |
| `firecrawl` | MCP/app integration |
| `swift-lsp` | MCP/tool integration |

### Easiest route: Codex Plugin Directory

Since you're now logged into Codex using the same Plus account, open Codex and go to:

**Plugins → Plugin Directory**

or, in supported Codex task views:

**Sources → Use plugins**

Then search for equivalents such as:

```text
frontend
design
browser
Chrome DevTools
Firecrawl
Swift
GitHub
```

OpenAI says installed plugins can be invoked in Codex, and plugins may contain only skills or combine skills with external apps/tools. citeturn208644search0

This is the route I'd use whenever the equivalent exists.

### For Claude plugins that are just skills

This is the interesting part: Claude's skill-based plugins can often be **ported**, because they're largely instructions/workflows rather than executables.

You don't need the exact Claude marketplace mechanism.

For example, instead of:

```text
frontend-design@claude-plugins-official
```

you can create a Codex-local plugin/skill containing the corresponding frontend-design instructions.

Conceptually:

```text
Claude

.claude/
 plugins/
 frontend-design/
 feature-dev/
 superpowers/

 ↓ port instructions/workflows

Codex

plugin / skills
 frontend-design
 feature-development
 superpowers
```

OpenAI explicitly supports **local/Codex-specific plugins**, including plugins that are usable only within Codex. citeturn208644search0

### MCP plugins are different

For:

```text
chrome-devtools-mcp
firecrawl
```

don't convert their prompts into skills.

Those should remain actual MCP/tool integrations:

```text
Codex
 │
 ├── Skill
 │ └── tells Codex HOW to use the tool
 │
 └── MCP/App
 └── actually executes the tool
```

So `chrome-devtools-mcp` should ultimately expose browser/DevTools operations to Codex, while Firecrawl should expose crawl/search/scrape operations.

Codex's plugin architecture explicitly supports this combination of **skills + apps/tools**. citeturn208644search0turn208644search3

### Don't migrate the whole JSON

A lot of this Claude config is Claude-specific:

```json
"permissions": {
 "defaultMode": "auto"
}
```

```json
"alwaysThinkingEnabled": false
```

```json
"effortLevel": "xhigh"
```

```json
"askUserQuestionTimeout": "never"
```

```json
"autoContinueAtUsageLimit": true
```

```json
"useAutoModeDuringPlan": true
```

These should **not** be dumped into `~/.codex/config.toml`.

Likewise this:

```json
"hooks": {
 "SessionStart": \[...\]
}
```

is specifically invoking:

```text
jcode.exe setup-hotkey --notify-cli-launch claude
```

so it is explicitly tied to Claude startup and isn't useful unchanged for Codex.

Your `worktree.baseRef = head` behaviour can instead be reproduced through Codex instructions/workflows if you still want that development pattern.

### What I would build for your Codex

I'd keep Codex itself relatively clean and put workflow behaviour into plugins/skills:

```text
Codex + ChatGPT Plus
│
├── Core Codex
│
├── AGENTS.md
│
├── Plugins / Skills
│ ├── frontend-design
│ ├── feature-dev
│ ├── superpowers
│ └── skill-creator
│
├── MCP / Apps
│ ├── Chrome DevTools
│ └── Firecrawl
│
└── language tooling
 └── Swift / LSP
```

That is much better than trying to replicate every Claude setting one-for-one.

And there's another useful benefit: OpenAI's new plugin model is shared across **ChatGPT and Codex**. A plugin can package instructions, skills and connected tools together rather than you maintaining separate giant configs for each environment. citeturn208644search0turn208644search3

For your specific seven Claude plugins, I would first try to install native Codex equivalents from the Plugin Directory; for whatever is missing, we can **port the original Claude plugin folders into native Codex skills/plugins**, and configure Chrome DevTools + Firecrawl as actual tool/MCP integrations rather than fake prompt replacements.

## User

ok i have installed plugin, i want to point them such that codex can use them in codex application

## Assistant

Worked for 8s

## Assistant

If you installed the plugins through the **ChatGPT/Codex Plugin Directory on this same Plus account**, you generally do **not** need to point Codex at a filesystem path manually. Installed plugins are account-level capabilities, and supported Codex views can use them directly. citeturn186995search0turn186995search3

In the **Codex application**, open your task/project and look for:

**Sources → Use plugins**

Then select the installed plugin(s) you want Codex to use for that task. OpenAI also supports invoking installed plugins with an `@plugin-name` mention where that surface supports it. citeturn186995search0

For example, if you installed a frontend skill/plugin, you can prompt Codex along the lines of:

```text
@frontend-design

Implement the dashboard UI in this repository.
Follow the existing design system and component structure.
```

The important distinction is:

```text
Plugin Directory install
 ↓
Your ChatGPT account
 ↓
Codex application
 ↓
Sources → Use plugins
```

You **do not** need something like this in `~/.codex/config.toml`:

```toml
plugins_path = "C:\\Users\\ASUS\\.claude\\plugins"
```

and you should not add Claude's:

```json
"enabledPlugins": {
 "frontend-design@claude-plugins-official": true
}
```

to Codex. That configuration belongs to Claude Code.

If what you actually installed are **physical Claude plugin folders under `.claude`**, rather than plugins from OpenAI's Plugin Directory, that's a different case. Codex won't automatically treat `.claude/plugins/...` as installed Codex plugins. Claude skills can often be imported/ported because OpenAI Skills follow the Agent Skills open standard, but they need to be installed into the OpenAI/Codex skill system rather than merely referenced from Claude's config. citeturn186995search6

So there are two cases:

| What you installed | What to do |
|---|---|
| Installed from **Codex/ChatGPT Plugin Directory** | Use **Sources → Use plugins**; no path configuration |
| Files exist under **`.claude/plugins`** | Import/port them as Codex Skills/plugins |
| MCP plugin such as Chrome DevTools | Configure the actual MCP/tool integration |
| Skill-only plugin | Install/import it as a Codex Skill |

If you're referring specifically to the `.claude/plugins` folders you already have on Windows, send me the output of:

```powershell
Get-ChildItem "$env:USERPROFILE\.claude\plugins" -Recurse -Depth 2 |
 Select-Object FullName
```

and I can map those exact folders into the Codex-compatible locations/config instead of making you reinstall everything.

## User

PS C:\Users\ASUS> Get-ChildItem "$env:USERPROFILE\.claude\plugins" -Recurse -Depth 2 |
>> Select-Object FullName

FullName
--------
C:\Users\ASUS\.claude\plugins\cache
C:\Users\ASUS\.claude\plugins\data
C:\Users\ASUS\.claude\plugins\marketplaces
C:\Users\ASUS\.claude\plugins\.last_inuse_sweep
C:\Users\ASUS\.claude\plugins\blocklist.json
C:\Users\ASUS\.claude\plugins\installed_plugins.json
C:\Users\ASUS\.claude\plugins\known_marketplaces.json
C:\Users\ASUS\.claude\plugins\plugin-catalog-cache.json
C:\Users\ASUS\.claude\plugins\cache\claude-plugins-official
C:\Users\ASUS\.claude\plugins\cache\claude-plugins-official\chrome-devtools-mcp
C:\Users\ASUS\.claude\plugins\cache\claude-plugins-official\feature-dev
C:\Users\ASUS\.claude\plugins\cache\claude-plugins-official\firecrawl
C:\Users\ASUS\.claude\plugins\cache\claude-plugins-official\frontend-design
C:\Users\ASUS\.claude\plugins\cache\claude-plugins-official\skill-creator
C:\Users\ASUS\.claude\plugins\cache\claude-plugins-official\superpowers
C:\Users\ASUS\.claude\plugins\cache\claude-plugins-official\swift-lsp
C:\Users\ASUS\.claude\plugins\data\chrome-devtools-mcp-claude-plugins-official
C:\Users\ASUS\.claude\plugins\data\superpowers-claude-plugins-official
C:\Users\ASUS\.claude\plugins\data\superpowers-inline
C:\Users\ASUS\.claude\plugins\data\swift-lsp-claude-plugins-official
C:\Users\ASUS\.claude\plugins\data\vercel-claude-plugins-official
C:\Users\ASUS\.claude\plugins\data\vercel-inline
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official\.claude-plugin
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official\external_plugins
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official\plugins
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official\.gcs-sha
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official\.gitignore
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official\LICENSE
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official\README.md

## Assistant

Worked for 4s

## Assistant

Good — now we can see exactly where Claude has stored them.

The key folders are these:

```powershell
C:\Users\ASUS\.claude\plugins\cache\claude-plugins-official\
```

with:

```text
chrome-devtools-mcp
feature-dev
firecrawl
frontend-design
skill-creator
superpowers
swift-lsp
```

Codex will **not automatically scan `.claude\plugins`**. It needs those capabilities either as native Codex plugins/skills, or as MCP/tool integrations. OpenAI confirms Codex loads configured skills and project/user instructions separately from Claude’s plugin system. citeturn809018search4turn809018search3

For your setup, I would **not copy the entire Claude plugin cache blindly**. First classify what each plugin actually contains.

Run this:

```powershell
$base = "$env:USERPROFILE\.claude\plugins\cache\claude-plugins-official"

Get-ChildItem $base -Directory | ForEach-Object {
 Write-Host "`n========== $($_.Name) ==========" -ForegroundColor Cyan

 Get-ChildItem $_.FullName -Recurse -Depth 3 |
 Where-Object {
 $_.Name -match 'SKILL\.md|plugin\.json|package\.json|mcp|README|commands|agents'
 } |
 Select-Object FullName
}
```

What I expect:

```text
frontend-design
feature-dev
skill-creator
superpowers
 ↓
mostly skills / instructions

chrome-devtools-mcp
firecrawl
 ↓
MCP/tool integrations

swift-lsp
 ↓
language/tool integration
```

For the skill-type ones, the goal is effectively:

```text
C:\Users\ASUS\.claude\plugins\cache\...
 ↓
 extract SKILL.md + resources
 ↓
 Codex skills
```

Codex supports Skills, and OpenAI’s Skills follow the Agent Skills open standard, so compatible skills can be moved between products rather than rewritten from zero. citeturn809018search3

I would create a Codex skills directory first:

```powershell
New-Item -ItemType Directory `
 "$env:USERPROFILE\.codex\skills" `
 -Force
```

Then inspect one plugin, starting with `frontend-design`:

```powershell
tree "$env:USERPROFILE\.claude\plugins\cache\claude-plugins-official\frontend-design" /F
```

Also:

```powershell
Get-ChildItem `
"$env:USERPROFILE\.claude\plugins\cache\claude-plugins-official\frontend-design" `
-Recurse |
Select-Object FullName
```

If you see something like:

```text
frontend-design\
 skills\
 frontend-design\
 SKILL.md
```

then copying just that skill is appropriate:

```powershell
Copy-Item `
"$env:USERPROFILE\.claude\plugins\cache\claude-plugins-official\frontend-design\skills\frontend-design" `
"$env:USERPROFILE\.codex\skills\frontend-design" `
-Recurse -Force
```

Eventually you want something roughly like:

```text
C:\Users\ASUS\.codex\
│
├── config.toml
├── AGENTS.md
└── skills\
 ├── frontend-design\
 │ └── SKILL.md
 │
 ├── feature-dev\
 │ └── SKILL.md
 │
 ├── skill-creator\
 │ └── SKILL.md
 │
 └── superpowers\
 ├── SKILL.md
 └── ...
```

Codex specifically incorporates configured skill metadata into its agent context, alongside `AGENTS.md` and your `config.toml` instructions. citeturn809018search4

I would **not copy these yet**:

```text
chrome-devtools-mcp
firecrawl
swift-lsp
```

because if they contain actual MCP/server configuration, merely placing them under `skills` will give Codex instructions but **not the executable tool**.

Those need to become:

```text
Codex
├── Skills
│ └── instructions for using tool
│
└── MCP server
 ├── chrome-devtools
 ├── firecrawl
 └── possibly Swift tooling
```

So first run this one command and send me its output:

```powershell
$base = "$env:USERPROFILE\.claude\plugins\cache\claude-plugins-official"

foreach ($plugin in @(
 "frontend-design",
 "feature-dev",
 "superpowers",
 "skill-creator",
 "chrome-devtools-mcp",
 "firecrawl",
 "swift-lsp"
)) {
 Write-Host "`n===== $plugin =====" -ForegroundColor Cyan
 tree "$base\$plugin" /F
}
```

Then I can tell you **exactly which folders to symlink/copy into `.codex`, and which ones must be configured as MCP servers**, rather than guessing and breaking the plugins.

One useful option here: instead of duplicating the skills, we can probably make Codex and Claude share the same skill directories using Windows junctions/symlinks, so updating a skill once updates both environments. memcite

## User

lets add marketplace of claude

## Assistant

Worked for 6s

## Assistant

Yes — in that dialog, try adding the **local Claude marketplace folder itself**.

In **Source**, enter:

```text
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official
```

Since this is a **local folder**, you should not need a Git ref. Leave **Git ref** empty. Also leave **Sparse paths** empty initially.

So the form should be:

```text
Source:
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official

Git ref:
\[empty\]

Sparse paths:
\[empty\]
```

Then click **Add marketplace**.

Your folder already contains:

```text
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official\
├── .claude-plugin\
├── external_plugins\
├── plugins\
├── README.md
└── ...
```

The catch is that **Codex and Claude do not necessarily use identical marketplace manifests**. Codex does support importing marketplaces from a GitHub repo, Git URL, or local folder—as your screenshot shows—but whether Claude’s official marketplace loads directly depends on whether Codex accepts its marketplace/plugin schema. OpenAI documents Codex plugins as packages that can contain skills, apps, and app templates, so compatibility with a Claude-specific marketplace is not guaranteed. citeturn981114search0

### If the local marketplace is rejected

Instead, point Codex at individual compatible plugin folders. For example, try:

```text
C:\Users\ASUS\.claude\plugins\marketplaces\claude-plugins-official\plugins\frontend-design
```

or, if Codex wants a repository-style marketplace rather than a single plugin, we can create a tiny **Codex marketplace wrapper** around the Claude plugins you actually care about:

```text
C:\Users\ASUS\.codex\claude-marketplace\
├── marketplace manifest
└── plugins\
 ├── frontend-design
 ├── feature-dev
 ├── skill-creator
 └── superpowers
```

and have those reference/copy the actual Claude skills.

For `chrome-devtools-mcp`, `firecrawl`, and probably `swift-lsp`, we should handle them separately because they involve executable tools/MCP rather than just instructions.

First try the exact local path above. If Codex gives you an error after clicking **Add marketplace**, send me the error screenshot/text and I'll convert the Claude marketplace into the format Codex expects.

## Resources

### Local attachments
- [2ead6f93-de45-41d4-9c9d-1eb59b690f7e.png](../../../Raw/Export/file_00000000a9fc81fab3da5c8201952f58.dat)

### External references
- [Using Codex with your ChatGPT plan | OpenAI Help Center](https://help.openai.com/en/articles/11369540-usi)
- [Codex | OpenAI Help Center](https://help.openai.com/en/collections/14937394-codex)
- [Configure Codex with Amazon Bedrock | OpenAI Help Center](https://help.openai.com/en/articles/20001253-configure-codex-with-amazon-bedrock)
- [ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275)
- [Plugins in ChatGPT and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex)
- [Using Codex with your ChatGPT plan | OpenAI Help Center](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan%2525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252529.csv)
- [Using Codex with your ChatGPT plan | OpenAI Help Center](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan%252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252528.pdf)
- [Introducing the Codex app | OpenAI](https://openai.com/index/introducing-the-codex-app/)
- [Introducing upgrades to Codex | OpenAI](https://openai.com/index/introducing-upgrades-to-codex/)
- [Using Codex with your ChatGPT plan | OpenAI Help Center](https://help.openai.com/en/articles/11369540-usi?utm_source=chatgpt.com)
- [Introducing the Codex app | OpenAI](https://openai.com/index/introducing-the-codex-app/?utm_source=chatgpt.com)
- [Configure Codex with Amazon Bedrock | OpenAI Help Center](https://help.openai.com/en/articles/20001253-configure-codex-with-amazon-bedrock?utm_source=chatgpt.com)
- [Codex | OpenAI Help Center](https://help.openai.com/en/collections/14937394-codex?utm_source=chatgpt.com)
- [ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275?utm_source=chatgpt.com)
- [Introducing upgrades to Codex | OpenAI](https://openai.com/index/introducing-upgrades-to-codex/?utm_source=chatgpt.com)
- [Plugins in ChatGPT and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex?utm_source=chatgpt.com)
- [Using Codex with your ChatGPT plan | OpenAI Help Center](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan%2525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252529.csv?utm_source=chatgpt.com)
- [Using Codex with your ChatGPT plan | OpenAI Help Center](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan%252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252528.pdf?utm_source=chatgpt.com)
- [Admin controls, security, and compliance for plugins and apps | OpenAI Help Center](https://help.openai.com/en/articles/11509118?utm_source=chatgpt.com)
- [Configurar o Codex com o Amazon Bedrock | OpenAI Help Center](https://help.openai.com/pt-br/articles/20001253-configurar-o-codex-com-o-amazon-bedrock?utm_source=chatgpt.com)
- [Configurar Codex con Amazon Bedrock | OpenAI Help Center](https://help.openai.com/es-es/articles/20001253-configurar-codex-con-amazon-bedrock?utm_source=chatgpt.com)
- [Create a model response | OpenAI API Reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/create?utm_source=chatgpt.com)
- [Community | OpenAI Developers](https://developers.openai.com/community?utm_source=chatgpt.com)
- [OpenAI Developers](https://developers.openai.com/?utm_source=chatgpt.com)
- [Get a model response | OpenAI API Reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/retrieve?utm_source=chatgpt.com)
- [Models | OpenAI API](https://developers.openai.com/api/docs/models?utm_source=chatgpt.com)
- [GPT-5.3-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.3-codex?utm_source=chatgpt.com)
- [All models | OpenAI API](https://developers.openai.com/api/docs/models/all?utm_source=chatgpt.com)
- [GPT-5.2-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.2-codex?utm_source=chatgpt.com)
- [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model?utm_source=chatgpt.com)
- [Chat Latest Model | OpenAI API](https://developers.openai.com/api/docs/models/chat-latest?utm_source=chatgpt.com)
- [GPT-5-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5-codex?utm_source=chatgpt.com)
- [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.5&utm_source=chatgpt.com)
- [Codex for every role, tool, and workflow | OpenAI](https://openai.com/index/codex-for-every-role-tool-workflow/?utm_source=chatgpt.com)
- [Plugin use cases and prompts | OpenAI Help Center](https://help.openai.com/en/articles/12084614-app-use-cases-and-prompts?utm_source=chatgpt.com)
- [Apps in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt%2525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252529.zst?utm_source=chatgpt.com)
- ["Agents Plugins" by OpenAI, Vercel, et. al. - thoughts? - API - OpenAI Developer Community](https://community.openai.com/t/agents-plugins-by-openai-vercel-et-al-thoughts/1389419?utm_source=chatgpt.com)
- [Plugins en ChatGPT y Codex | OpenAI Help Center](https://help.openai.com/es-419/articles/20001256-plugins-in-codex?utm_source=chatgpt.com)
- [Plugins in ChatGPT en Codex | OpenAI Help Center](https://help.openai.com/nl-nl/articles/20001256-plugins-in-chatgpt-and-codex?utm_source=chatgpt.com)
- [Running Codex safely at OpenAI | OpenAI](https://openai.com/index/running-codex-safely/?utm_source=chatgpt.com)
- [Plugins in ChatGPT en Codex | OpenAI Help Center](https://help.openai.com/nl-nl/articles/20001256-plugins-in-codex?utm_source=chatgpt.com)
- ["Agents Plugins" by OpenAI, Vercel, et. al. - thoughts? - API - OpenAI Developer Community](https://community.openai.com/t/agents-plugins-by-openai-vercel-et-al-thoughts/1389419/1?utm_source=chatgpt.com)
- [Latest topics - OpenAI Developer Community](https://community.openai.com/latest?page=164&utm_source=chatgpt.com)
- [How do you preserve project context across Codex sessions in a large codebase? - Codex - OpenAI Developer Community](https://community.openai.com/t/how-do-you-preserve-project-context-across-codex-sessions-in-a-large-codebase/1387550?utm_source=chatgpt.com)
- [GPT-5.6 Sol can now delegate to Luna, plus other tips to save credits - #5 by Joao_Martins - Codex - OpenAI Developer Community](https://community.openai.com/t/gpt-5-6-sol-can-now-delegate-to-luna-plus-other-tips-to-save-credits/1390765/5?utm_source=chatgpt.com)
- [Tips and Tricks for using Codex - #19 by platypus - Codex - OpenAI Developer Community](https://community.openai.com/t/tips-and-tricks-for-using-codex/1373143/19?utm_source=chatgpt.com)
- [Can't find a way to delete my personal chatGPT plugins - Plugins / Actions builders - OpenAI Developer Community](https://community.openai.com/t/cant-find-a-way-to-delete-my-personal-chatgpt-plugins/1387440?utm_source=chatgpt.com)
- [Product Feature Request: Event-Driven Task Coordination for Voice-Led Multi-Agent Work - #2 by jromisher28 - Codex - OpenAI Developer Community](https://community.openai.com/t/product-feature-request-event-driven-task-coordination-for-voice-led-multi-agent-work/1389356/2?utm_source=chatgpt.com)
- [Extended Personal Memory for ChatGPT, ChatGPT Work & Codex — Build Prompt + Testers - Use cases and examples - OpenAI Developer Community](https://community.openai.com/t/extended-personal-memory-for-chatgpt-chatgpt-work-codex-build-prompt-testers/1391779?utm_source=chatgpt.com)
- [Topics tagged marketplace](https://community.openai.com/tag/marketplace/348?utm_source=chatgpt.com)
- [Topics tagged skills](https://community.openai.com/tag/skills/1101?utm_source=chatgpt.com)
- [Codex limits spark frustration among subscribers - Page 4 - Codex - OpenAI Developer Community](https://community.openai.com/t/codex-limits-spark-frustration-among-subscribers/1390408?page=4&utm_source=chatgpt.com)
- [Plugins in ChatGPT and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001256/?utm_source=chatgpt.com)
- [Using Codex with your ChatGPT plan | OpenAI Help Center](https://help.openai.com/en/articles/11369540/?utm_source=chatgpt.com)
- [Skills in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/20001066?utm_source=chatgpt.com)
- [Plugins in ChatGPT and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001256?utm_source=chatgpt.com)
- [Plugin use cases and prompts | OpenAI Help Center](https://help.openai.com/en/articles/12084614-plugin-use-cases-and-prompts?utm_source=chatgpt.com)
- [Apps in ChatGPT | OpenAI Help Center](https://help-lb.openai.com/en/articles/11487775-apps-in-chatgpt?utm_source=chatgpt.com)
- [ChatGPT apps with sync | OpenAI Help Center](https://help.openai.com/en/articles/10847137-chatgpt-apps-with-sync?utm_source=chatgpt.com)
- [Plugins in ChatGPT and Codex | OpenAI Help Center](https://help-lb.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex?utm_source=chatgpt.com)
- [ChatGPT Enterprise & Edu - Release Notes | OpenAI Help Center](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-%C3%A9s-edu-kiad%C3%A1si-megjegyz%C3%A9sek?utm_source=chatgpt.com)
- [Pluginy v ChatGPT a Codexu | OpenAI Help Center](https://help.openai.com/cs-cz/articles/20001256-plugins-in-codex?utm_source=chatgpt.com)
- [Using Codex with your ChatGPT plan | OpenAI Help Center](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan%2525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252528.pdf?utm_source=chatgpt.com)
- [ChatGPT और Codex में प्लगइन | OpenAI Help Center](https://help.openai.com/hi-in/articles/20001256-plugins-in-codex?utm_source=chatgpt.com)
- [Plugins en ChatGPT y Codex | OpenAI Help Center](https://help.openai.com/es-419/articles/20001256-plugins-en-chatgpt-y-codex?utm_source=chatgpt.com)
- [Unrolling the Codex agent loop | OpenAI](https://openai.com/index/unrolling-the-codex-agent-loop/?utm_source=chatgpt.com)
- [ChatGPT Workspace Agents for Enterprise and Business | OpenAI Help Center](https://help.openai.com/en/articles/20001143?utm_source=chatgpt.com)
- [ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275/?utm_source=chatgpt.com)
- [Harness engineering: leveraging Codex in an agent-first world | OpenAI](https://openai.com/index/harness-engineering/?utm_source=chatgpt.com)
- [Unrolling the Codex agent loop | OpenAI](https://openai.com/pa-IN/index/unrolling-the-codex-agent-loop/?utm_source=chatgpt.com)
- [Unrolling the Codex agent loop | OpenAI](https://openai.com/ga-IE/index/unrolling-the-codex-agent-loop/?utm_source=chatgpt.com)
- [Codex एजेंट लूप को खोलना | OpenAI](https://openai.com/hi-IN/index/unrolling-the-codex-agent-loop/?utm_source=chatgpt.com)
- [Unrolling the Codex agent loop | OpenAI](https://openai.com/gu-IN/index/unrolling-the-codex-agent-loop/?utm_source=chatgpt.com)
- [Introducing Codex | OpenAI](https://openai.com/mt-MT/index/introducing-codex/?utm_source=chatgpt.com)
- [Codex एजंट लूप उलगडणे | OpenAI](https://openai.com/mr-IN/index/unrolling-the-codex-agent-loop/?utm_source=chatgpt.com)
- [Codex for Builders - Resource | OpenAI Academy](https://academy.openai.com/en/public/clubs/builders-etkn1/resources/codex-for-builders?utm_source=chatgpt.com)
- [Using Codex with your ChatGPT plan | OpenAI Help Center](https://help-lb.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan?utm_source=chatgpt.com)
- [ChatGPT ও Codex-এ প্লাগইন | OpenAI Help Center](https://help.openai.com/bn-bd/articles/20001256-plugins-in-chatgpt-and-codex?utm_source=chatgpt.com)
- [Use Codex with Amazon Bedrock | OpenAI Help Center](https://help.openai.com/en/articles/20001252-use-codex-with-amazon-bedrock?utm_source=chatgpt.com)
- [Плагіни в ChatGPT і Codex | OpenAI Help Center](https://help.openai.com/uk-ua/articles/20001256-plugins-in-codex?utm_source=chatgpt.com)
- [Showcase | OpenAI Developers](https://developers.openai.com/showcase?app_type=app&app_type=landing-page&app_type=storefront&utm_source=chatgpt.com)
- [Mga plugin sa ChatGPT at Codex | OpenAI Help Center](https://help.openai.com/fil-ph/articles/20001256-plugins-in-codex?utm_source=chatgpt.com)
- [Showcase | OpenAI Developers](https://developers.openai.com/showcase?app_type=app&app_type=game&app_type=landing-page&tech_stack=Next.js&tech_stack=React&use_case=games&use_case=marketing-sites&utm_source=chatgpt.com)
- [ChatGPT と Codex のプラグイン | OpenAI Help Center](https://help.openai.com/ja-jp/articles/20001256-plugins-in-codex?utm_source=chatgpt.com)
- [Codex Meetups in Pune | OpenAI Developers](https://developers.openai.com/community/meetups?city=Pune&utm_source=chatgpt.com)
- [Showcase | OpenAI Developers](https://developers.openai.com/showcase?app_type=game&app_type=other&app_type=storefront&source=openai&use_case=creative-tools&use_case=documentation&use_case=games&use_case=marketing-sites&utm_source=chatgpt.com)
- [Codex Meetups | OpenAI Developers](https://developers.openai.com/community/meetups?utm_source=chatgpt.com)
- [Codex Meetups in New Delhi | OpenAI Developers](https://developers.openai.com/community/meetups?city=New+Delhi&utm_source=chatgpt.com)
- [Codex Meetups in Kodakara | OpenAI Developers](https://developers.openai.com/community/meetups?city=Kodakara&utm_source=chatgpt.com)
- [Codex Meetups in Bengaluru | OpenAI Developers](https://developers.openai.com/community/meetups?city=Bengaluru&utm_source=chatgpt.com)
