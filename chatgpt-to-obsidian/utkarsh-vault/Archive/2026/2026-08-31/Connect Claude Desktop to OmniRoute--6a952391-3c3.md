---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a952391-3c3c-83e9-b94a-1b6e710a1a75"
created: 1788158877.207344
updated: 1788205766.46105
resource_section: true
---

# Connect Claude Desktop to OmniRoute

## User

how can i connect claude code desktop to onmiroute, it is live on 
\[http://localhost:20128/api/v1\](http://localhost:20128/api/v1)

## Assistant

You can connect Claude Code to a local router, but the key question is whether OmniRoute exposes an **Anthropic-compatible Messages API** or only an OpenAI-compatible `/v1` API. I’ll map the exact config for your `localhost:20128` endpoint and show you how to test it before changing Claude Code.

## Assistant

I found the important detail: **Claude Code Desktop does support the same gateway settings as the CLI**, and on Windows you can set them directly in the Desktop app’s **Local environment editor**. Also, don’t use `http://localhost:20128/api/v1` as `ANTHROPIC_BASE_URL`—Claude appends `/v1/messages` itself.

## Assistant

Worked for 39s

## Assistant

Yes — **Claude Code Desktop → OmniRoute works**, but configure the **Code tab's Local environment**, not the normal Claude chat settings.

### 1. Make sure OmniRoute itself works

In PowerShell:

```powershell
$OMNI_KEY = "YOUR_OMNIROUTE_API_KEY"

Invoke-RestMethod `
 -Uri "http://localhost:20128/v1/models" `
 -Headers @{ Authorization = "Bearer $OMNI_KEY" }
```

You should get the available models. OmniRoute's standard API is exposed at `/v1`. citeturn145137search3turn500203search5

### 2. Open Claude Code Desktop

In Claude Desktop:

**Code → Environment dropdown → Local → ⚙ gear**

Claude's docs specifically say the Local environment editor is where you can configure environment variables for Desktop Code sessions on Windows. citeturn670145search0

Add these:

```text
ANTHROPIC_BASE_URL=http://localhost:20128
ANTHROPIC_AUTH_TOKEN=YOUR_OMNIROUTE_API_KEY
ANTHROPIC_MODEL=auto/coding
```

Optionally also add:

```text
CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1
```

Then **fully close Claude Desktop and reopen it**.

### Important: don't use `/api/v1`

For Claude Code, this is wrong:

```text
ANTHROPIC_BASE_URL=http://localhost:20128/api/v1
```

and this is also wrong:

```text
ANTHROPIC_BASE_URL=http://localhost:20128/v1
```

Use:

```text
ANTHROPIC_BASE_URL=http://localhost:20128
```

Claude Code speaks the Anthropic Messages protocol and automatically adds:

```text
/v1/messages
```

So the final request becomes:

```text
http://localhost:20128/v1/messages
```

OmniRoute explicitly documents this behavior. If you put `/v1` into `ANTHROPIC_BASE_URL`, Claude can end up requesting `/v1/v1/messages`. citeturn933341search2turn500203search2

### 3. Why `auto/coding`?

OmniRoute supports:

```text
auto
auto/coding
auto/cheap
auto/fast
auto/smart
```

For Claude Code, I'd start with:

```text
ANTHROPIC_MODEL=auto/coding
```

because OmniRoute biases the route toward models suited for coding. citeturn500203search4

If you've already created your own OmniRoute combo, you can instead do:

```text
ANTHROPIC_MODEL=my-combo-name
```

or force a particular provider/model:

```text
ANTHROPIC_MODEL=cc/claude-opus-4-7
```

depending on what your `/v1/models` endpoint exposes.

### 4. Alternative: configure it globally

Since Desktop and CLI share `~/.claude/settings.json`, you can instead edit:

```text
C:\Users\ASUS\.claude\settings.json
```

Claude confirms that `%USERPROFILE%\.claude` is the Windows equivalent of `~/.claude`, and Desktop and CLI share this configuration. citeturn670145search0turn670145search1

Put:

```json
{
 "env": {
 "ANTHROPIC_BASE_URL": "http://localhost:20128",
 "ANTHROPIC_AUTH_TOKEN": "YOUR_OMNIROUTE_API_KEY",
 "ANTHROPIC_MODEL": "auto/coding",
 "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1"
 }
}
```

If your existing `settings.json` already contains things such as plugins, permissions, hooks, etc., **don't replace the whole file**—just merge those entries into its existing `"env"` object.

### 5. Use a Local session

This is important in Claude Code Desktop:

```text
Environment: Local ✅
```

not:

```text
Environment: Remote ❌
```

A Remote session runs on Anthropic's infrastructure, so its `localhost:20128` would mean the remote machine, **not your Windows PC**. citeturn670145search0

So your flow becomes:

```text
Claude Code Desktop
 │
 │ Anthropic Messages API
 ▼
http://localhost:20128/v1/messages
 │
 ▼
 OmniRoute
 │
 ├─ Claude
 ├─ GPT
 ├─ Gemini
 ├─ Kimi
 └─ your configured combos/providers
```

For your setup, I'd use the **Local environment editor method** rather than Windows global environment variables. It's cleaner and isolates the OmniRoute configuration to Claude Code Desktop. memcite

## User

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

setting.json

## Assistant

Worked for 17s

## Assistant

Yep. Keep your existing settings and just add an `"env"` block.

Use this as your `C:\Users\ASUS\.claude\settings.json`:

```json
{
 "permissions": {
 "defaultMode": "auto"
 },
 "model": "combo",
 "env": {
 "ANTHROPIC_BASE_URL": "http://localhost:20128",
 "ANTHROPIC_AUTH_TOKEN": "YOUR_OMNIROUTE_API_KEY",
 "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1"
 },
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
 }
}
```

Your `"model": "combo"` can stay exactly where it is. Claude Code supports `model` directly in `settings.json`, and it also supports environment variables such as `ANTHROPIC_BASE_URL` for routing through an LLM gateway. citeturn770897view0turn732496view0

### One important thing

Don't put:

```json
"ANTHROPIC_BASE_URL": "http://localhost:20128/api/v1"
```

or:

```json
"ANTHROPIC_BASE_URL": "http://localhost:20128/v1"
```

Start with:

```json
"ANTHROPIC_BASE_URL": "http://localhost:20128"
```

Claude Code will construct the Messages API path from the base URL.

### If OmniRoute doesn't require an API key

You can use a dummy token:

```json
"ANTHROPIC_AUTH_TOKEN": "omniroute"
```

Some Claude Code authentication flows expect a credential to exist even when the local gateway itself doesn't care about it.

Then completely close/reopen Claude Desktop and start a **Local Code session**.

Inside Claude Code run:

```text
/status
```

Claude's docs specifically recommend `/status` to verify which provider/base URL the current session is using. citeturn732496view0

You should see the base URL pointing to:

```text
http://localhost:20128
```

Also, your pasted JSON was missing the final closing `}`; the version above is valid JSON. Claude settings files are strict JSON, so even a trailing comma or missing brace will cause a Settings Error. citeturn770897view0

If `combo` is the OmniRoute combo you already created, this should give you:

```text
Claude Code Desktop
 ↓
model = combo
 ↓
localhost:20128
 ↓
OmniRoute
 ↓
your combo routing
```

memcite

## User

i want to use auto/coding" although i have combo setup

## Assistant

Worked for a few seconds

## Assistant

Yes — then just change the Claude Code model from `"combo"` to `"auto/coding"`.

Use:

```json
{
 "permissions": {
 "defaultMode": "auto"
 },
 "model": "auto/coding",
 "env": {
 "ANTHROPIC_BASE_URL": "http://localhost:20128",
 "ANTHROPIC_AUTH_TOKEN": "omniroute",
 "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1"
 },
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
 }
}
```

So this:

```json
"model": "combo"
```

becomes:

```json
"model": "auto/coding"
```

Your existing OmniRoute `combo` can remain configured inside OmniRoute; Claude Code simply won't explicitly request it.

The flow becomes:

```text
Claude Code
 ↓
model = auto/coding
 ↓
localhost:20128
 ↓
OmniRoute
 ↓
automatically chooses coding-appropriate model/provider
```

After saving, **fully restart Claude Desktop**, open a new Local Code session, then run:

```text
/status
```

You should see `auto/coding` as the requested model. memcite

## Assistant

Worked for 18s

## Assistant

Your Claude Code → OmniRoute connection is actually **working correctly**.

The screenshot shows:

> **Model discovery — found 74 models** ✅

and Claude is correctly calling:

```text
http://localhost:20128/v1/messages
```

The failure is happening **inside OmniRoute**, after Claude reaches it.

The important error is:

```text
\[502\]: Auggie CLI exited with code 1:
'auggie' is not recognized as an internal or external command
```

So `auto/coding` selected your **Auggie provider**, but OmniRoute can't find the `auggie` executable. OmniRoute's `auto/*` routing dynamically considers active connected providers, which is why this can happen even though you didn't explicitly choose Auggie. citeturn390780search0turn634650search1

### Best fix if you don't care about Auggie

Go into the **OmniRoute dashboard → Providers / Connections**, find:

```text
Augment / Auggie
```

and **disable that connection**.

Then keep Claude exactly like this:

```json
{
 "permissions": {
 "defaultMode": "auto"
 },
 "model": "auto/coding",
 "env": {
 "ANTHROPIC_BASE_URL": "http://localhost:20128",
 "ANTHROPIC_AUTH_TOKEN": "YOUR_OMNIROUTE_KEY",
 "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1"
 },
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
 }
}
```

Then restart OmniRoute and hit **Check again** in Claude.

### If you actually want Auggie included

OmniRoute's Auggie provider expects the Auggie CLI to be installed and authenticated locally. The documented setup is:

```powershell
npm install -g @augmentcode/auggie@latest
```

Then check:

```powershell
where.exe auggie
auggie --version
```

and authenticate:

```powershell
auggie login
```

OmniRoute normally looks for `auggie` on `PATH`, and it also supports an explicit `AUGGIE_BIN` environment variable if you need to point it directly to the executable. citeturn634650search0turn634650search3

However, Augment's current documentation lists **Windows through WSL**, rather than native Windows, as the supported Windows setup. Since your OmniRoute process is clearly spawning through native Windows—the `'... is not recognized as an internal or external command'` message confirms that—I wouldn't install Auggie just to fix this unless you specifically want that provider. citeturn634650search5

### So for your setup

I would do:

```text
Claude Code Desktop
 ↓
auto/coding
 ↓
OmniRoute :20128
 ↓
all healthy active coding providers
 ↓
EXCLUDE Auggie
```

Your **Claude settings do not need changing**. The `localhost:20128` base URL is right, `/v1/messages` is right, and model discovery is already succeeding. The thing to fix is the broken **Auggie connection inside OmniRoute**. memcite

## Resources

### External references
- [Use Claude Code Desktop - Claude Code Docs](https://code.claude.com/docs/en/desktop?utm_source=chatgpt.com)
- [OmniRoute/docs/guides/CLAUDE-CODE-CONFIGURATION.md at release/v3.8.50 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.50/docs/guides/CLAUDE-CODE-CONFIGURATION.md?utm_source=chatgpt.com)
- [omniroute - npm](https://www.npmjs.com/package/omniroute?activeTab=readme&utm_source=chatgpt.com)
- [OmniRoute Setup Guide — Install & Connect in 5 Minutes](https://www.omniroute.site/setup/?utm_source=chatgpt.com)
- [error using Claude desktop · diegosouzapw OmniRoute · Discussion #8130 · GitHub](https://github.com/diegosouzapw/OmniRoute/discussions/8130?utm_source=chatgpt.com)
- [omniroute/docs/guides/USER_GUIDE.md at main · ourines/omniroute · GitHub](https://github.com/ourines/omniroute/blob/main/docs/guides/USER_GUIDE.md?utm_source=chatgpt.com)
- [Claude Code settings - Claude Code Docs](https://code.claude.com/docs/en/settings?utm_source=chatgpt.com)
- [omniroute/docs/reference/CLI-TOOLS.md at main · robotjaol/omniroute · GitHub](https://github.com/robotjaol/omniroute/blob/main/docs/reference/CLI-TOOLS.md)
- [omniroute/README.md at main · ourines/omniroute · GitHub](https://github.com/ourines/omniroute/blob/main/README.md)
- [error using Claude desktop · diegosouzapw OmniRoute · Discussion #8130 · GitHub](https://github.com/diegosouzapw/OmniRoute/discussions/8130)
- [CLI Tools · diegosouzapw/OmniRoute Wiki · GitHub](https://github.com/diegosouzapw/OmniRoute/wiki/CLI-Tools/a5470ab85e5bdac8dd8ac2faed513ed152fb0b23)
- [OmniRoute/docs/reference/CLI-TOOLS.md at release/v3.8.51 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/reference/CLI-TOOLS.md)
- [Setup Guide · diegosouzapw/OmniRoute Wiki · GitHub](https://github.com/diegosouzapw/OmniRoute/wiki/Setup-Guide)
- [omniroute/docs/guides/USER_GUIDE.md at main · funcodingdev/omniroute · GitHub](https://github.com/funcodingdev/omniroute/blob/main/docs/guides/USER_GUIDE.md)
- [omniroute/docs/guides/USER_GUIDE.md at main · ourines/omniroute · GitHub](https://github.com/ourines/omniroute/blob/main/docs/guides/USER_GUIDE.md)
- [omniroute/docs/reference/CLI-TOOLS.md at main · renatobardi/omniroute · GitHub](https://github.com/renatobardi/omniroute/blob/main/docs/reference/CLI-TOOLS.md)
- [\[BUG\]\[Windows\] Desktop app ignores defaultMode: bypassPermissions in settings.json — mode picker missing "Bypass permissions" option · Issue #60541 · anthropics/claude-code · GitHub](https://github.com/anthropics/claude-code/issues/60541)
- [OmniRoute/docs/guides/USER_GUIDE.md at release/v3.8.50 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.50/docs/guides/USER_GUIDE.md)
- [claude-code-docs/content/en/docs/claude-code/desktop.md at main · thevibeworks/claude-code-docs · GitHub](https://github.com/thevibeworks/claude-code-docs/blob/main/content/en/docs/claude-code/desktop.md)
- [omniroute/docs/guides/CLAUDE-CODE-CONFIGURATION.md at main · Slazee/omniroute · GitHub](https://github.com/Slazee/omniroute/blob/main/docs/guides/CLAUDE-CODE-CONFIGURATION.md)
- [OmniRoute/docs/guides/CLAUDE-CODE-CONFIGURATION.md at release/v3.8.50 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.50/docs/guides/CLAUDE-CODE-CONFIGURATION.md)
- [omniroute-claude-windows/README.md at master · 51Vinay/omniroute-claude-windows · GitHub](https://github.com/51Vinay/omniroute-claude-windows/blob/master/README.md)
- [GitHub - SudhirRathore/omniroute-claude-code: Step-by-step guide to connecting OmniRoute to Claude Code with dynamic model selection, auto-fallback combos, and macOS launcher app. · GitHub](https://github.com/SudhirRathore/omniroute-claude-code)
- [Claude Code/Desktop works through OmniRoute gateway, but all tools fail (websearch, webfetch, bash, read, MCP tools). Anyone fixed this?](https://www.reddit.com/r/mcp/comments/1w1loaw/claude_codedesktop_works_through_omniroute/)
- [OmniRoute Setup Guide — Install & Connect in 5 Minutes](https://www.omniroute.site/setup/)
- [omniroute - npm](https://www.npmjs.com/package/omniroute?activeTab=versions)
- [omniroute - npm](https://www.npmjs.com/package/omniroute?activeTab=code)
- [omniroute - npm](https://www.npmjs.com/package/omniroute)
- [omniroute - npm](https://www.npmjs.com/package/omniroute?activeTab=readme)
- [Set up Claude Code - Anthropic](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- [Use Claude Code Desktop - Claude Code Docs](https://code.claude.com/docs/en/desktop)
- [Claude Code settings - Claude Code Docs](https://code.claude.com/docs/en/settings)
- [Model configuration - Claude Code Docs](https://code.claude.com/docs/en/model-config)
- [Claude Code: Desktop app: Code-tab sessions are never regist... · #84502](https://claudeissues.com/issue/84502-bug-desktop-app-code-tab-sessions-are-never-registered-for-remote-control-despit)
- [GitHub - v1tusha/life-support: agentrouter.org / New API gateways don't forward event: ping, so Claude Code kills the stream after ~18s of silence and retries forever. This local proxy injects the pings, retries transient errors, pre-commits SSE headers and hedges stalled requests — plus a terminal panel. One file, zero deps. · GitHub](https://git.hubp.de/v1tusha/life-support)
- [Enterprise deployment overview - Claude Code Docs](https://code.claude.com/docs/en/third-party-integrations)
- [claude-code/CHANGELOG.md at main · anthropics/claude-code · GitHub](https://code.claude.com/docs/id/changelog?utm_source=chatgpt.com)
- [claude-code/CHANGELOG.md at main · anthropics/claude-code · GitHub](https://code.claude.com/docs/ko/changelog?utm_source=chatgpt.com)
- [claude-code/CHANGELOG.md at main · anthropics/claude-code · GitHub](https://code.claude.com/docs/ja/changelog?utm_source=chatgpt.com)
- [claude-code/CHANGELOG.md at main · anthropics/claude-code · GitHub](https://code.claude.com/docs/fr/changelog?utm_source=chatgpt.com)
- [claude-code/CHANGELOG.md at main · anthropics/claude-code · GitHub](https://code.claude.com/docs/pt/changelog.md?utm_source=chatgpt.com)
- [claude-code/CHANGELOG.md at main · anthropics/claude-code · GitHub](https://code.claude.com/docs/zh-CN/changelog?utm_source=chatgpt.com)
- [Model deprecations - Claude Platform Docs](https://docs.anthropic.com/en/docs/about-claude/model-deprecations?utm_source=chatgpt.com)
- [Prompting best practices - Claude Platform Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-templates-and-variables?utm_source=chatgpt.com)
- [网页搜索工具 - Claude Platform Docs](https://docs.anthropic.com/zh-CN/docs/agents-and-tools/tool-use/web-search-tool?utm_source=chatgpt.com)
- [Claude on Amazon Bedrock (Opus 4.6 and earlier) - Claude Platform Docs](https://docs.anthropic.com/en/api/claude-on-amazon-bedrock?utm_source=chatgpt.com)
- [Soporte para PDF - Claude Platform Docs](https://docs.anthropic.com/es/docs/build-with-claude/pdf-support?utm_source=chatgpt.com)
- [Guida alla migrazione - Claude Platform Docs](https://docs.anthropic.com/it/docs/about-claude/models/migrating-to-claude-4?utm_source=chatgpt.com)
- [文档 - Claude Platform Docs](https://docs.anthropic.com/zh-CN/home?utm_source=chatgpt.com)
- [MCPコネクター - Claude Platform Docs](https://docs.anthropic.com/ja/docs/agents-and-tools/mcp-connector?utm_source=chatgpt.com)
- [탈옥 및 프롬프트 인젝션 완화 - Claude Platform Docs](https://docs.anthropic.com/ko/docs/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks?utm_source=chatgpt.com)
- [减少幻觉 - Claude Platform Docs](https://docs.anthropic.com/zh-CN/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations?utm_source=chatgpt.com)
- [Kundensupport-Agent - Claude Platform Docs](https://docs.anthropic.com/de/docs/about-claude/use-case-guides/customer-support-chat?utm_source=chatgpt.com)
- [用語集 - Claude Platform Docs](https://docs.anthropic.com/ja/docs/about-claude/glossary?utm_source=chatgpt.com)
- [Auto Combo · diegosouzapw/OmniRoute Wiki · GitHub](https://github.com/diegosouzapw/OmniRoute/wiki/Auto-Combo?utm_source=chatgpt.com)
- [OmniRoute/docs/reference/PROVIDER_REFERENCE.md at release/v3.8.50 · diegosouzapw/OmniRoute · GitHub](https://ithub.global.ssl.fastly.net/diegosouzapw/OmniRoute/blob/release/v3.8.50/docs/reference/PROVIDER_REFERENCE.md?utm_source=chatgpt.com)
- [GitHub - augmentcode/auggie: An AI agent that brings Augment Code's power to the terminal. · GitHub](https://github.com/augmentcode/auggie?utm_source=chatgpt.com)
- [OmniRoute/docs/reference/ENVIRONMENT.md at release/v3.8.50 · diegosouzapw/OmniRoute · GitHub](https://ithub.global.ssl.fastly.net/diegosouzapw/OmniRoute/blob/release/v3.8.50/docs/reference/ENVIRONMENT.md?utm_source=chatgpt.com)
- [Install Auggie CLI - Augment](https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli?utm_source=chatgpt.com)
- [omniroute/docs/guides/CLI-INTEGRATIONS.md at main · CarlaSalles-AI/omniroute · GitHub](https://github.com/CarlaSalles-AI/omniroute/blob/main/docs/guides/CLI-INTEGRATIONS.md?utm_source=chatgpt.com)
- [GitHub - saharmor/auggie-mcp: Run Augment Code as a coding agent via the Auggie CLI · GitHub](https://github.com/saharmor/auggie-mcp?utm_source=chatgpt.com)
- [omniroute/docs/reference/CLI-TOOLS.md at main · robotjaol/omniroute · GitHub](https://github.com/robotjaol/omniroute/blob/main/docs/reference/CLI-TOOLS.md?utm_source=chatgpt.com)
- [omniroute/docs/reference/CLI-TOOLS.md at main · renatobardi/omniroute · GitHub](https://github.com/renatobardi/omniroute/blob/main/docs/reference/CLI-TOOLS.md?utm_source=chatgpt.com)
- [agentmanager/catalog.json at main · kevinelliott/agentmanager · GitHub](https://github.com/kevinelliott/agentmanager/blob/main/catalog.json?utm_source=chatgpt.com)
- [OmniRouter/docs/guides/SETUP_GUIDE.md at release/v3.8.50 · alif2815/OmniRouter · GitHub](https://github.com/alif2815/OmniRouter/blob/release/v3.8.50/docs/guides/SETUP_GUIDE.md?utm_source=chatgpt.com)
- [fix(providers): Auggie (Augment CLI) provider fails with spawn EINVAL on Windows · Issue #6304 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/6304?utm_source=chatgpt.com)
- [Features · diegosouzapw/OmniRoute Wiki · GitHub](https://github.com/diegosouzapw/OmniRoute/wiki/Features?utm_source=chatgpt.com)
- [GitHub - diegosouzapw/OmniRoute: Never stop coding. Free MIT AI gateway: one endpoint, 290+ providers (90+ free), 500+ models — Kimi, Claude, GPT, OpenAI, Gemini, GLM, DeepSeek, MiniMax. Works with Claude Code, Codex, Cursor, OpenCode, Cline & Copilot. Quota-aware auto-fallback, RTK+Caveman compression saves 15-95% tokens, MCP/A2A, Desktop/PWA. Built by 500+ contributors · GitHub](https://github.com/diegosouzapw/OmniRoute/?utm_source=chatgpt.com)
- [OmniRoute/docs/guides/FEATURES.md at main · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/main/docs/guides/FEATURES.md?utm_source=chatgpt.com)
- [Features · diegosouzapw/OmniRoute Wiki · GitHub](https://github.com/diegosouzapw/OmniRoute/wiki/Features/a5470ab85e5bdac8dd8ac2faed513ed152fb0b23?utm_source=chatgpt.com)
- [fix(providers): auto/coding:pro + auto/reasoning + nvidia/google/diffusiongemma-26b-a4b-it return 15s timeouts · Issue #6458 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/6458?utm_source=chatgpt.com)
- [OmniRoute/docs/routing/AUTO-COMBO.md at release/v3.8.49 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.49/docs/routing/AUTO-COMBO.md?utm_source=chatgpt.com)
- [OmniRoute/docs/getting-started/AUTO-COMBO-GUIDE.md at release/v3.8.50 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.50/docs/getting-started/AUTO-COMBO-GUIDE.md?utm_source=chatgpt.com)
- [\[Feature\] Zero-config auto-routing: built-in auto combos via auto/ prefix · Issue #2099 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/2099?utm_source=chatgpt.com)
- [fix(api): auto/* routing aliases bypass API-key allowedConnections/disableNonPublicModels · Issue #9057 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/9057?utm_source=chatgpt.com)
- [fix(providers): oc/nemotron-3-ultra-free upstream 404 · Issue #11486 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/11486?utm_source=chatgpt.com)
- [Feature Flags · diegosouzapw/OmniRoute Wiki · GitHub](https://github.com/diegosouzapw/OmniRoute/wiki/Feature-Flags?utm_source=chatgpt.com)
- [fix(backend): credential health scheduler never retries failed connections after first check · Issue #9289 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/9289?utm_source=chatgpt.com)
- [fix(providers): Custom compatible providers excluded from auto/ routing by REGISTRY gate · Issue #5873 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/5873?utm_source=chatgpt.com)
- [\[Feature\] Enhanced `auto/*` combos · Issue #4235 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/4235?utm_source=chatgpt.com)
- [fix(providers): credential health check tests disabled (is_active=false) connections, causing unnecessary timeouts and scheduler latency · Issue #9180 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/9180?utm_source=chatgpt.com)
- [\[Feature\] Auto-disable API key on \[402\]: Insufficient account balance · Issue #5239 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/5239?utm_source=chatgpt.com)
- [\[BUG\] Combo model substitution forwards client thinking:{type:"disabled"} to a model that rejects it → upstream 400 · Issue #3554 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/3554?utm_source=chatgpt.com)
- [OmniRoute/src/app/api/provider-nodes/route.ts at release/v3.8.50 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.50/src/app/api/provider-nodes/route.ts?utm_source=chatgpt.com)
- [Router Backends · diegosouzapw/OmniRoute Wiki · GitHub](https://github.com/diegosouzapw/OmniRoute/wiki/Router-Backends?utm_source=chatgpt.com)
- [\[BUG\] Combo routing/failover completely broken in v3.8.8 and v3.8.9 (ignoring provider removal, missing fallbacks, and phantom models · Issue #3147 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/3147?utm_source=chatgpt.com)
- [OmniRoute/docs/architecture/ROUTER_BACKENDS.md at release/v3.8.50 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.50/docs/architecture/ROUTER_BACKENDS.md?utm_source=chatgpt.com)
- [Disable builtin "auto-routing catalog"? · diegosouzapw OmniRoute · Discussion #5862 · GitHub](https://github.com/diegosouzapw/OmniRoute/discussions/5862?utm_source=chatgpt.com)
- [fix(resilience): auto/* combos swallow upstream auth failure — empty finish:stop with no error when tools attached · Issue #8649 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/8649?utm_source=chatgpt.com)
- [omniroute/docs/routing/AUTO-COMBO.md at main · Gods-light/omniroute · GitHub](https://github.com/Gods-light/omniroute/blob/main/docs/routing/AUTO-COMBO.md?utm_source=chatgpt.com)
- [GitHub - Morgatinha/omniroute: Never stop coding. Free AI gateway: one endpoint, 231+ providers (50+ free), connect Claude Code, Codex, Cursor, Cline & Copilot to FREE Claude/GPT/Gemini. RTK+Caveman stacked compression saves 15-95% tokens, smart auto-fallback, MCP/A2A, multimodal APIs, Desktop/PWA. · GitHub](https://github.com/Morgatinha/omniroute?utm_source=chatgpt.com)
- [GitHub - NFTHiKe/OmniRoute: Never stop coding. Free AI gateway: one endpoint, 231+ providers (50+ free), connect Claude Code, Codex, Cursor, Cline & Copilot to FREE Claude/GPT/Gemini. RTK+Caveman stacked compression saves 15-95% tokens, smart auto-fallback, MCP/A2A, multimodal APIs, Desktop/PWA. · GitHub](https://github.com/NFTHiKe/OmniRoute?utm_source=chatgpt.com)
- [omniroute/README.md at main · Revmagi/omniroute · GitHub](https://github.com/Revmagi/omniroute/blob/main/README.md?utm_source=chatgpt.com)
- [OmniRoute/docs/routing/AUTO-COMBO.md at release/v3.8.51 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/blob/release/v3.8.51/docs/routing/AUTO-COMBO.md?utm_source=chatgpt.com)
- [GitHub - azazelpy/omniroute-sdk: 🔀 Multi-provider LLM gateway SDK (TS/Python/Go) — 200+ models, 16 providers, auto-routing · GitHub](https://github.com/azazelpy/omniroute-sdk?utm_source=chatgpt.com)
- [fix(api): Messages API returns synthetic `<block>no</block>` — claudeClassifierCompat trigger too broad · Issue #8189 · diegosouzapw/OmniRoute · GitHub](https://github.com/diegosouzapw/OmniRoute/issues/8189?utm_source=chatgpt.com)
- [Introducing Auggie CLI - Augment](https://docs.augmentcode.com/cli/overview?utm_source=chatgpt.com)
- [Auggie CLI - AI Coding Agent for Your Terminal | Augment Code](https://www.augmentcode.com/product/cli?utm_source=chatgpt.com)
- [Install Auggie CLI - Augment](https://augment-mtje7p526w.mintlify.app/cli/setup-auggie/install-auggie-cli?utm_source=chatgpt.com)
- [Auggie CLI by Coder Labs | Coder Registry](https://registry.coder.com/modules/coder-labs/auggie?utm_source=chatgpt.com)
- [@augmentcode/auggie - npm](https://www.npmjs.com/package/%40augmentcode/auggie?activeTab=versions&utm_source=chatgpt.com)
- [@augmentcode/auggie - npm](https://www.npmjs.com/package/%40augmentcode/auggie?activeTab=dependents&utm_source=chatgpt.com)
- [@augmentcode/auggie-sdk - npm](https://www.npmjs.com/package/%40augmentcode/auggie-sdk?activeTab=readme&utm_source=chatgpt.com)
- [omniroute - npm](https://www.npmjs.com/package/omniroute?activeTab=versions&utm_source=chatgpt.com)
- [omniroute - npm](https://www.npmjs.com/package/omniroute?activeTab=dependents&utm_source=chatgpt.com)
- [CLI Not Found Errors | aj47/auggie-context-mcp | DeepWiki](https://deepwiki.com/aj47/auggie-context-mcp/7.3-cli-not-found-errors?utm_source=chatgpt.com)
- [diegosouzapw--omniroute/README.md at 1bda6c15dc885b645243f6cc198688ba6bb7480c - diegosouzapw--omniroute - Wehub](https://wehub.plus/github-featured/diegosouzapw--omniroute/src/commit/1bda6c15dc885b645243f6cc198688ba6bb7480c/README.md?display=source&utm_source=chatgpt.com)
- [github-featured/diegosouzapw--omniroute - diegosouzapw--omniroute - Wehub](https://wehub.plus/github-featured/diegosouzapw--omniroute/commits/branch/release/v3.8.50/CHANGELOG.md?utm_source=chatgpt.com)
- [github-featured/diegosouzapw--omniroute - diegosouzapw--omniroute - Wehub](https://wehub.plus/github-featured/diegosouzapw--omniroute/commits/branch/release/v3.8.50/electron/package-lock.json?utm_source=chatgpt.com)
- [github-featured/diegosouzapw--omniroute: diegosouzapw/OmniRoute｜GitHub 镜像 ⭐ 54.4k · 🍴 7.4k - diegosouzapw--omniroute - Wehub](https://wehub.plus/github-featured/diegosouzapw--omniroute/src/commit/e8950ded397aa25bd7bd45a4d2e62e3dc74eb7b5?utm_source=chatgpt.com)
- [diegosouzapw--omniroute/README.md at c9d4a45f1883d7daf150bbff631f3e83b41aa5b4 - diegosouzapw--omniroute - Wehub](https://wehub.plus/github-featured/diegosouzapw--omniroute/src/commit/c9d4a45f1883d7daf150bbff631f3e83b41aa5b4/README.md?utm_source=chatgpt.com)
- [github-featured/diegosouzapw--omniroute - diegosouzapw--omniroute - Wehub](https://wehub.plus/github-featured/diegosouzapw--omniroute/blame/commit/e8950ded397aa25bd7bd45a4d2e62e3dc74eb7b5/README.md?utm_source=chatgpt.com)
- [cli-providers — diegosouzapw/omniroute](https://www.skills.sh/diegosouzapw/omniroute/cli-providers?utm_source=chatgpt.com)
- [OpenCode, OmniRoute, and Ponytail Installation - Apuntes de eduardófilo](https://apuntes.eduardofilo.es/en/2026-07-26_opencode_omniroute.html?utm_source=chatgpt.com)
- [Instalación OpenCode, OmniRoute y Ponytail - Apuntes de eduardófilo](https://apuntes.eduardofilo.es/2026-07-26_opencode_omniroute.html?utm_source=chatgpt.com)
- [pi-omniroute-sync · Packages · Pi](https://pi.dev/packages/pi-omniroute-sync?name=context7&utm_source=chatgpt.com)
- [OmniRoute — Free AI Gateway for Multi-Provider LLMs](https://omniroute.online/?utm_source=chatgpt.com)
- [pi-omniroute-sync | npm.io](https://npm.io/package/pi-omniroute-sync?utm_source=chatgpt.com)
