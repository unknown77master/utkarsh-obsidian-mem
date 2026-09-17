---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a8c3be2-f9c0-83ee-bbe5-8997b3242a2b"
created: 1787575289.632808
updated: 1787577286.790268
resource_section: true
---

# Fix Windows Popup Issue

## User

this pop up does not appear on screen and i am stuck here

## Assistant

Worked for a few seconds

## Assistant

Yes — from your screenshot, **ChatGPT is waiting for the Windows UAC (User Account Control) confirmation**, but the UAC dialog itself is not appearing. The ChatGPT window is therefore stuck at **“Finish Windows setup” → `config_load`**.

This is usually a Windows/UAC focus issue rather than something you need to do inside ChatGPT.

### Try these in order

**1. Press `Alt + Tab`**

Look through all open windows for a dialog titled **“User Account Control”**.

If you see it, select **Yes**.

---

**2. Press `Win + Ctrl + Shift + B`**

This resets the Windows graphics driver. Your screen may briefly flicker/beep.

Then return to ChatGPT and click **Try Windows setup again**.

---

**3. Check whether UAC is actually enabled**

Press:

`Win + R`

Type:

```text
UserAccountControlSettings
```

Press **Enter**.

Make sure the slider is **not at “Never notify”**. Set it to the default level, then click **OK**.

Restart ChatGPT and try the setup again.

---

### If it is still stuck — do this

Completely close ChatGPT:

1. Press `Ctrl + Shift + Esc`
2. Open **Task Manager**
3. Find **ChatGPT**
4. Right-click → **End task**
5. Start ChatGPT again **as a normal user** — don't use “Run as administrator”.
6. Try **Try Windows setup again**.

The Windows app is distributed through the Microsoft Store, and OpenAI's current documentation confirms that Windows-specific app setup/reset is supported. citeturn0search12turn0search8

### If the UAC popup still never appears

There is a useful reset option:

**Windows Settings → Apps → Installed apps → ChatGPT → ⋯ → Advanced options → Reset**

OpenAI specifically documents **Reset** as the Windows-app recovery procedure. citeturn0search8

Then reopen ChatGPT and retry the setup.

**I would start with `Alt + Tab` first.** If the UAC window is being created on a different virtual desktop/behind another window, that often exposes it immediately.

If you tell me **what happens when you click “Try Windows setup again”** (nothing happens, screen flashes, or it returns to the same `config_load` error), I can take you through the next step without reinstalling anything.

## User

no i tried all

## Assistant

Worked for 18s

## Assistant

Got it. Then **don't repeat the UAC/repair/reinstall steps**. I found an issue that matches your screenshot almost exactly.

The important part is: **the UAC popup shown in your screenshot is only an illustration**. In the reported bug, clicking “Try Windows setup again” never actually triggers a Windows UAC request, and the app immediately returns to `config_load`. This is a currently reported Windows-app issue. citeturn1view0turn1view1

### Let's fix the actual cause

The first thing I want you to check is the ChatGPT/Codex configuration.

**1. Completely close ChatGPT.**

Make sure it is not running in Task Manager.

**2. Open PowerShell normally** — don't run it as administrator.

**3. Run this:**

```powershell
Test-Path "$HOME\.codex\config.toml"
```

Tell me whether it returns:

```text
True
```

or

```text
False
```

**Don't delete anything yet.**

There are reports that a malformed or incompatible `config.toml` can cause exactly this `Finish Windows setup` → `Windows setup didn't finish` loop. Renaming the configuration file has fixed it for some users. citeturn1view1

However, since you've already tried several fixes, **I don't want you blindly deleting your config**—especially if you use Codex configuration/MCP/project settings.

Send me the output of that one command first, and we'll diagnose it from there.

## User

true

## Assistant

Worked for 8s

## Assistant

Good. That confirms the **`.codex\config.toml` file exists**.

And I found a report that is almost exactly your situation: **no UAC popup appears at all, and `Try Windows setup again` immediately fails with `Windows setup didn't finish`**. In one case, an invalid entry in `config.toml` caused the loop, and renaming that file fixed it. citeturn0search2turn0search3

So let's test that **without deleting your configuration**.

### Step 1 — Close ChatGPT completely

Close the ChatGPT window.

Then open **Task Manager → Details** and make sure there is no ChatGPT/Codex process running.

### Step 2 — Back up `config.toml`

Open **PowerShell** and run:

```powershell
Rename-Item "$HOME\.codex\config.toml" "config.toml.backup"
```

This **does not delete your file**. It simply changes:

```text
config.toml
```

to:

```text
config.toml.backup
```

Your original configuration is therefore preserved.

### Step 3 — Start ChatGPT again

Open ChatGPT normally.

Then click:

**Try Windows setup again**

### What should happen

If `config.toml` was causing the problem, ChatGPT should now be able to proceed with the Windows setup and the **actual UAC popup should appear**.

This isn't a random workaround—the same `Finish Windows setup` / no-UAC symptom has been reported specifically with the Windows Codex/ChatGPT desktop app, including cases where renaming `config.toml` resolved it. citeturn0search2turn0search6

**Don't delete `config.toml.backup`.** If this fixes it, we'll inspect the old configuration afterward and restore only the valid settings.

If it **still gives `Windows setup didn't finish` without showing UAC**, tell me that exact result. Then we'll move to the next diagnostic rather than changing random Windows settings.

## User

model = "qwen/qwen3-235b-a22b-2507"

model_provider = "openrouter"


web_search = "live"
notify = \[ "C:\\Users\\ASUS\\AppData\\Local\\OpenAI\\Codex\\runtimes\\cua_node\\dd584937042db7da\\bin\\node_modules\\@oai\\sky\\bin\\windows\\codex-computer-use.exe", "turn-ended" \]


\[model_providers.agentrouter\]
name = "OpenRouterAgent"
base_url = "https://openrouter.ai/api/v1/chat/completions" 
wire_api = "responses" 
bearer_token = "sk-......" 
 
\[marketplaces.openai-bundled\] 
source_type = "local" 
source = '\\?\C:\Users\ASUS\.codex\.tmp\bundled-marketplaces\openai-bundled'

## Assistant

Worked for 21s

## Assistant

Ah — **now we have the problem.** Your `config.toml` is not configured consistently.

The most important error is this:

```toml
model_provider = "openrouter"
```

but your provider section is:

```toml
\[model_providers.agentrouter\]
```

Those names **must match**. Codex expects `model_provider` to point to a key under `model_providers`. citeturn0search1turn1search4

You also have two other problems:

1. Your OpenRouter `base_url` includes `/chat/completions`, while you're using `wire_api = "responses"`. The current configuration examples use:
 ```toml
 base_url = "https://openrouter.ai/api/v1"
 wire_api = "responses"
 ```
 citeturn1search0turn1search1

2. `bearer_token` is not the normal current configuration mechanism. The documented approach is `env_key` or an appropriate authentication mechanism. citeturn0search1

### Your corrected config

**First, keep your backup. Then replace the contents of `config.toml` with this:**

```toml
model = "qwen/qwen3-235b-a22b-2507"
model_provider = "openrouter"

web_search = "live"

\[model_providers.openrouter\]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
wire_api = "responses"
env_key = "OPENROUTER_API_KEY"

\[marketplaces.openai-bundled\]
source_type = "local"
source = '\\?\C:\Users\ASUS\.codex\.tmp\bundled-marketplaces\openai-bundled'
```

Then set your API key as an environment variable rather than putting it directly into `config.toml`:

```powershell
\[Environment\]::SetEnvironmentVariable(
 "OPENROUTER_API_KEY",
 "YOUR_OPENROUTER_KEY",
 "User"
)
```

**Important:** Don't paste your actual API key here. The key you showed is redacted, but if the real key was ever exposed anywhere, rotate it in OpenRouter.

### But there's one more thing

Your `notify` entry is pointing to:

```text
C:\Users\ASUS\AppData\Local\OpenAI\Codex\runtimes\cua_node\dd584937042db7da\...
```

That runtime hash can change when Codex updates. **I would remove `notify` temporarily** while we're getting the desktop setup working.

So use the configuration above **without `notify`**.

---

### Why I think this is the actual culprit

Your configuration currently tells Codex:

> "Use provider **openrouter**"

but then defines:

> "Here is provider **agentrouter**."

There is no `model_providers.openrouter` definition.

That's a configuration-resolution failure, and it happens very early in Codex initialization. The current Codex documentation explicitly defines `model_provider` as the key that identifies the provider in the `model_providers` map. citeturn0search1

Also, there are current reports of **OpenRouter/custom providers interacting badly with Codex Desktop**, so once we get past the configuration error, there may be a separate Desktop-specific limitation. citeturn1search2

**Do this first: fix `config.toml` as above, restart ChatGPT, and click "Try Windows setup again."**

If the UAC popup still doesn't appear, **don't change anything else**. Tell me exactly what the screen says afterward, and we'll isolate whether we're dealing with the configuration failure or the separate Windows setup bug.

## Assistant

Worked for a couple of seconds

## Assistant

Yes — **this screenshot gives us the exact issue now.** The Windows UAC problem is no longer the primary blocker.

The red banner says:

> **“Fix config.toml: Model provider `agentrouter` not found.”**

That means Codex is currently reading:

```toml
model_provider = "agentrouter"
```

but it cannot find:

```toml
\[model_providers.agentrouter\]
```

### Do this first

Open:

```text
C:\Users\ASUS\.codex\config.toml
```

Make sure these two names **match exactly**.

Since your provider section is:

```toml
\[model_providers.agentrouter\]
```

your top-level setting should be:

```toml
model_provider = "agentrouter"
```

So, for now, use this structure:

```toml
model = "qwen/qwen3-235b-a22b-2507"
model_provider = "agentrouter"

web_search = "live"

\[model_providers.agentrouter\]
name = "OpenRouterAgent"
base_url = "https://openrouter.ai/api/v1/chat/completions"
wire_api = "responses"
bearer_token = "YOUR_KEY"

\[marketplaces.openai-bundled\]
source_type = "local"
source = '\\?\C:\Users\ASUS\.codex\.tmp\bundled-marketplaces\openai-bundled'
```

**Do not change anything else yet.**

### Then save the file

After saving:

1. Go back to the Codex window shown in your screenshot.
2. **Close the `HH rag` thread.**
3. Reopen `HH rag`.
4. If necessary, completely restart Codex and reopen the project.

The red error specifically says:

> “After saving the file, reopen the thread.”

So this part matters.

---

### One important correction to my previous message

I told you to change:

```toml
model_provider = "openrouter"
```

That was wrong **for the configuration you originally showed**, because your actual provider block is named:

```toml
\[model_providers.agentrouter\]
```

The correct relationship is:

```text
model_provider = "agentrouter"
 ↓
\[model_providers.agentrouter\]
```

Think of it like a dictionary lookup:

```text
model_provider → "agentrouter"

model_providers\["agentrouter"\] → provider configuration
```

If you put `openrouter` at the top but only define `agentrouter`, Codex can't resolve the provider.

### Don't worry about the UAC yet

Your screenshot shows that **Codex is now running far enough to load the project/thread**, but it is rejecting the configuration before the thread can resume.

Let's get `config.toml` loading correctly first. **Don't delete your backup and don't reinstall anything.**

Once the red `agentrouter not found` message disappears, we can deal with the original Windows setup/UAC issue if it still remains.

## Assistant

Worked for 12s

## Assistant

Now we have a **different and much more precise error**. Your `config.toml` is loading successfully, and Codex is reaching OpenRouter.

The screenshot shows:

> `401 Unauthorized: No cookie auth credentials found` 
> URL: `https://openrouter.ai/api/v1/responses`

So **the provider name problem is fixed**. The remaining problem is **authentication**.

### What is wrong

Your current provider configuration apparently still has:

```toml
bearer_token = "..."
```

That is not the correct current Codex configuration for a custom provider. Current Codex/OpenRouter documentation uses `env_key` to tell Codex which environment variable contains the API key. citeturn2search0turn2search2

OpenRouter itself expects:

```text
Authorization: Bearer <OPENROUTER_API_KEY>
```

for `/api/v1/responses`. citeturn0search0

### Do this exactly

#### 1. Change your `config.toml`

Use:

```toml
model = "qwen/qwen3-235b-a22b-2507"
model_provider = "agentrouter"

web_search = "live"

\[model_providers.agentrouter\]
name = "OpenRouterAgent"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"
wire_api = "responses"

\[marketplaces.openai-bundled\]
source_type = "local"
source = '\\?\C:\Users\ASUS\.codex\.tmp\bundled-marketplaces\openai-bundled'
```

**Remove this completely:**

```toml
bearer_token = "sk-..."
```

Notice that I also changed:

```text
https://openrouter.ai/api/v1/chat/completions
```

to:

```text
https://openrouter.ai/api/v1
```

because Codex's `responses` wire API handles the `/responses` endpoint itself. OpenRouter's current Codex configuration specifically uses this base URL with `wire_api = "responses"`. citeturn2search1turn2search0

---

#### 2. Put your API key in `.env`

This is particularly important because you're using the **Codex desktop app**.

Create/open:

```text
C:\Users\ASUS\.codex\.env
```

Put:

```text
OPENROUTER_API_KEY=sk-or-your-real-key-here
```

OpenAI's current Codex documentation notes that desktop apps may not inherit environment variables from your shell and supports putting required environment variables in `~/.codex/.env`. citeturn2search4

**Don't send me the key.**

---

#### 3. Completely restart Codex

Don't just reopen the thread.

Close Codex completely, then start it again.

After restarting, open a **new chat** and test:

```text
hi
```

### Why this should fix this particular error

Your flow currently looks like:

```text
Codex
 ↓
agentrouter
 ↓
https://openrouter.ai/api/v1/responses
 ↓
❌ no usable API credential
 ↓
401
```

After the change:

```text
Codex
 ↓
agentrouter
 ↓
OPENROUTER_API_KEY from ~/.codex/.env
 ↓
Authorization: Bearer sk-or-...
 ↓
OpenRouter /responses
 ↓
Qwen
```

And importantly, **we don't need to touch the Windows UAC setup anymore right now**. Your latest screenshot proves Codex has progressed past the configuration-loading stage and is actually attempting an OpenRouter request.

### One security point

You previously had a real-looking API key directly inside `config.toml`. If that was ever exposed anywhere outside your machine, **rotate the OpenRouter key** and use the new one in `.codex\.env`.

Try those three changes. The expected result is that the `401 No cookie auth credentials found` error disappears.

## Resources

### Local attachments
- [7d7a13c5-360d-44ef-bb00-0f14850bdc04.png](../../../Raw/Export/file_0000000028188230800ef2d57292b783.dat)

### External references
- [Using the ChatGPT Windows app | OpenAI Help Center](https://help.openai.com/en/articles/9982051-using-the-chatgpt-windows-app%25252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252525252523.ejs?utm_source=chatgpt.com)
- [ChatGPT Windows ऐप का उपयोग करना | OpenAI Help Center](https://help.openai.com/hi-in/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Admin controls, security, and compliance for plugins and apps | OpenAI Help Center](https://help.openai.com/en/articles/11509118?utm_source=chatgpt.com)
- [Apps in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-chatgpt-%E4%B8%AD%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%99%A8?utm_source=chatgpt.com)
- [ChatGPT app templates | OpenAI Help Center](https://help.openai.com/en/articles/20001247?utm_source=chatgpt.com)
- [Using the built-in browser in the ChatGPT desktop app | OpenAI Help Center](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app?utm_source=chatgpt.com)
- [Windows app | OpenAI Help Center](https://help.openai.com/en/collections/10670766-windows-?utm_source=chatgpt.com)
- [Microsoft Teams app for ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/12552368?utm_source=chatgpt.com)
- [Windows App - Release Notes | OpenAI Help Center](https://help.openai.com/en/articles/10003026-windows-app-release-notes?utm_source=chatgpt.com)
- [Plugins in ChatGPT and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001256?utm_source=chatgpt.com)
- [Moving to the new ChatGPT desktop app | OpenAI Help Center](https://help.openai.com/en/articles/20001276?utm_source=chatgpt.com)
- [SharePoint app in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/12143177-sharepoint-app-in-chatgpt?utm_source=chatgpt.com)
- [ChatGPT Windows ആപ്പ് ഉപയോഗിക്കുന്നത് | OpenAI Help Center](https://help.openai.com/ml-in/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275/?utm_source=chatgpt.com)
- [ChatGPT Windows యాప్‌ను ఉపయోగించడం | OpenAI Help Center](https://help.openai.com/te-in/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Plugins in ChatGPT and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001256/?utm_source=chatgpt.com)
- [Controlos de administrador, segurança e conformidade para plugins e apps | OpenAI Help Center](https://help.openai.com/pt-pt/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business?utm_source=chatgpt.com)
- [Windows app stuck on "Finish Windows setup" — sandbox setup never triggers a real UAC prompt, "Retry" fails instantly · Issue #32492 · openai/codex · GitHub](https://github.com/openai/codex/issues/32492)
- [Bug: Cannot access Chatgpt after new update - Bugs - OpenAI Developer Community](https://community.openai.com/t/bug-cannot-access-chatgpt-after-new-update/1386466)
- [Bug: Cannot access Chatgpt after new update](https://community.openai.com/t/bug-cannot-access-chatgpt-after-new-update/1386466?utm_source=chatgpt.com)
- [استفاده از اپ ChatGPT ویندوز | OpenAI Help Center](https://help.openai.com/fa-ir/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [ChatGPT Windows अॅप वापरणे | OpenAI Help Center](https://help.openai.com/mr-in/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Utilizarea aplicației ChatGPT pentru Windows | OpenAI Help Center](https://help.openai.com/ro-ro/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Përdorimi i aplikacionit ChatGPT për Windows | OpenAI Help Center](https://help.openai.com/sq-al/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Usar la app de ChatGPT para Windows | OpenAI Help Center](https://help.openai.com/es-419/articles/9982051-usar-la-app-de-chatgpt-para-windows?utm_source=chatgpt.com)
- [Korištenje aplikacije ChatGPT za Windows | OpenAI Help Center](https://help.openai.com/bs-ba/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [ChatGPT Windows ایپ استعمال کرنا | OpenAI Help Center](https://help.openai.com/ur-in/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Používání aplikace ChatGPT pro Windows | OpenAI Help Center](https://help.openai.com/cs-cz/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [ChatGPT Desktop App for Windows Won't Load After Update ...](https://community.openai.com/t/chatgpt-desktop-app-for-windows-wont-load-after-update-november-25/1032083?utm_source=chatgpt.com)
- [ChatGPT/Codex Windows app stuck on “Finish Windows setup”](https://www.reddit.com/r/codex/comments/1v56u0r/chatgptcodex_windows_app_stuck_on_finish_windows/?utm_source=chatgpt.com)
- [sandbox setup never triggers a real UAC prompt, "Retry" fails ...](https://github.com/openai/codex/issues/32492?utm_source=chatgpt.com)
- [Windows setup cannot complete (UAC never appears) #32995](https://github.com/openai/codex/issues/32995?utm_source=chatgpt.com)
- [Deploy the Windows app | ChatGPT Learn](https://learn.chatgpt.com/docs/enterprise/windows-deployment?utm_source=chatgpt.com)
- [How To Install ChatGPT On Windows 10 And Windows 11 Tutorial ...](https://www.youtube.com/watch?v=SSM8zi0TuSA&utm_source=chatgpt.com)
- [How To Fix ChatGPT Not Launching On Windows 11 - YouTube](https://www.youtube.com/watch?v=Pac1nKwOmrA&utm_source=chatgpt.com)
- [ChatGPT Windows App Not Working? Fix It Fast (2026) - AI Q&A Hub](https://www.aiqnahub.com/chatgpt-windows-app-not-working/?utm_source=chatgpt.com)
- [I can't install any app via the Microsoft store](https://learn.microsoft.com/en-us/answers/questions/5765763/i-cant-install-any-app-via-the-microsoft-store?utm_source=chatgpt.com)
- [Windows setup fails before the UAC prompt, and both setup options are non-functional · Issue #32149 · openai/codex · GitHub](https://github.com/openai/codex/issues/32149?utm_source=chatgpt.com)
- [Usar la aplicación ChatGPT para Windows | OpenAI Help Center](https://help.openai.com/es-es/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Nggunakake aplikasi ChatGPT Windows | OpenAI Help Center](https://help.openai.com/jv-id/articles/9982051-nggunakake-aplikasi-chatgpt-windows?utm_source=chatgpt.com)
- [How can I contact support? | OpenAI Help Center](https://help.openai.com/en/articles/6614161-h?utm_source=chatgpt.com)
- [使用 ChatGPT Windows 应用 | OpenAI Help Center](https://help.openai.com/zh-hans-cn/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Usando o aplicativo ChatGPT para Windows | OpenAI Help Center](https://help.openai.com/pt-br/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [Using the ChatGPT Windows app | OpenAI Help Center](https://help-lb.openai.com/en/articles/9982051-using-the-chatgpt-windows-app?utm_source=chatgpt.com)
- [\[Windows\] Setup hangs at “Complete configuration” after UAC approval on Windows 11 24H2 · Issue #34783 · openai/codex · GitHub](https://github.com/openai/codex/issues/34783?utm_source=chatgpt.com)
- [Windows native agent setup fails without displaying the required UAC prompt · Issue #36613 · openai/codex · GitHub](https://github.com/openai/codex/issues/36613?utm_source=chatgpt.com)
- [\[Windows\] "Finish Windows setup" loops with no UAC prompt; sandbox runner gets Access Denied on C:\Users\Default · Issue #37940 · openai/codex · GitHub](https://github.com/openai/codex/issues/37940?utm_source=chatgpt.com)
- [ChatGPT/Codex Windows Desktop App — Stuck in "Complete Windows Setup" one-time permission loop · Issue #37665 · openai/codex · GitHub](https://github.com/openai/codex/issues/37665?utm_source=chatgpt.com)
- [app-server: JSON-RPC `-32600` is overloaded across "no rollout found" and "failed to load configuration" — please make the two discriminable · Issue #28496 · openai/codex · GitHub](https://github.com/openai/codex/issues/28496?utm_source=chatgpt.com)
- [fstools/block.c at master · openwrt/fstools · GitHub](https://github.com/openwrt/fstools/blob/master/block.c?utm_source=chatgpt.com)
- [packages/net/stunnel/files/stunnel.init at master · openwrt/packages · GitHub](https://github.com/openwrt/packages/blob/master/net/stunnel/files/stunnel.init?utm_source=chatgpt.com)
- [UEVR/src/Mod.hpp at master · praydog/UEVR · GitHub](https://github.com/praydog/UEVR/blob/master/src/Mod.hpp?utm_source=chatgpt.com)
- [X-TCAS/src/xplane.c at master · skiselkov/X-TCAS · GitHub](https://github.com/skiselkov/X-TCAS/blob/master/src/xplane.c?utm_source=chatgpt.com)
- [gallery-dl/gallery_dl/option.py at master · mikf/gallery-dl · GitHub](https://github.com/mikf/gallery-dl/blob/master/gallery_dl/option.py?utm_source=chatgpt.com)
- [coova-chilli-openwrt/coova-chilli/files/chilli.init at master · openwisp/coova-chilli-openwrt · GitHub](https://github.com/openwisp/coova-chilli-openwrt/blob/master/coova-chilli/files/chilli.init?utm_source=chatgpt.com)
- [Don't use GetPrivateProfile* WinAPI functions for loading INI · Issue #468 · sfall-team/sfall · GitHub](https://github.com/sfall-team/sfall/issues/468?utm_source=chatgpt.com)
- [gargoyle/package/qos-gargoyle/files/qos_gargoyle.init at master · ericpaulbishop/gargoyle · GitHub](https://github.com/ericpaulbishop/gargoyle/blob/master/package/qos-gargoyle/files/qos_gargoyle.init?utm_source=chatgpt.com)
- [packages/net/nlbwmon/files/nlbwmon.init at master · openwrt/packages · GitHub](https://github.com/openwrt/packages/blob/master/net/nlbwmon/files/nlbwmon.init?utm_source=chatgpt.com)
- [packages/net/zerotier/files/etc/init.d/zerotier at master · openwrt/packages · GitHub](https://github.com/openwrt/packages/blob/master/net/zerotier/files/etc/init.d/zerotier?utm_source=chatgpt.com)
- [automlbenchmark/runbenchmark.py at master · openml/automlbenchmark · GitHub](https://github.com/openml/automlbenchmark/blob/master/runbenchmark.py?utm_source=chatgpt.com)
- [#34783 - \[Windows\] Setup hangs at “Complete configuration” after UAC approval on Windows 11 24H2 - openai/codex - upd.dev](https://upd.dev/openai/codex/issues/34783?utm_source=chatgpt.com)
- [Windows Desktop: "Finish Windows setup" never completes, preventing sandboxed edits · openai/codex #32808](https://codexissues.com/issue/32808-windows-desktop-finish-windows-setup-never-completes-preventing-sandboxed-edits?utm_source=chatgpt.com)
- [User Account Control settings | Microsoft Support](https://support.microsoft.com/en-US/Windows/security/user-account-control-settings?utm_source=chatgpt.com)
- [Configuration Reference - Codex CLI](https://www.mintlify.com/openai/codex/configuration/reference?utm_source=chatgpt.com)
- [GitHub](https://github.com/openai/codex/diffs/0?base_sha=e0303dbac06b6ead612107fa2144cf5b809bbe98&name=95abf99e718a8e6ad5155dda10e280f50912a847&pull_number=1848&sha1=e0303dbac06b6ead612107fa2144cf5b809bbe98&sha2=95abf99e718a8e6ad5155dda10e280f50912a847&short_path=b335630&w=false&utm_source=chatgpt.com)
- [codex-settings/configs/openrouter.toml at main · feiskyer/codex-settings · GitHub](https://github.com/feiskyer/codex-settings/blob/main/configs/openrouter.toml?utm_source=chatgpt.com)
- [OpenRouter model catalog parsing fails on startup · Issue #24286 · openai/codex](https://github.com/openai/codex/issues/24286?utm_source=chatgpt.com)
- [Desktop custom providers are unusable with existing chats and the model picker · Issue #29156 · openai/codex · GitHub](https://github.com/openai/codex/issues/29156?utm_source=chatgpt.com)
- [codex/codex-rs/app-server/tests/suite/v2/connection_handling_websocket.rs at main · openai/codex · GitHub](https://github.com/openai/codex/blob/main/codex-rs/app-server/tests/suite/v2/connection_handling_websocket.rs?utm_source=chatgpt.com)
- [Config.toml | Updated Keys · Issue #2760 · openai/codex](https://github.com/openai/codex/issues/2760?utm_source=chatgpt.com)
- [github.com](https://github.com/openai/codex/diffs/1?base_sha=b73426c1c40187ca13c74c03912a681072c2884f&head_user=cevatkerim&name=main&pull_number=1298&qualified_name=refs%2Fheads%2Fmain&sha1=b73426c1c40187ca13c74c03912a681072c2884f&sha2=2e1131d49cbea41ce1023d5548574c41123547e9&short_path=ed3b507&unchanged=expanded&w=false&utm_source=chatgpt.com)
- [codex-openai/docs/config.md at main · adhameldeeb/codex-openai · GitHub](https://github.com/adhameldeeb/codex-openai/blob/main/docs/config.md?utm_source=chatgpt.com)
- [openai-platform/codex/config-sample.md at main · llms-txt-archive/openai-platform · GitHub](https://github.com/llms-txt-archive/openai-platform/blob/main/codex/config-sample.md?utm_source=chatgpt.com)
- [codex-openai/docs/example-config.md at main · roshanemoraes/codex-openai · GitHub](https://github.com/roshanemoraes/codex-openai/blob/main/docs/example-config.md?utm_source=chatgpt.com)
- [github.com](https://github.com/openai/codex/diffs/2?base_sha=9f2ab97fbcaa18bcfbbe1cf342f6720a006baf9c&head_user=ibakaidov&name=main&pull_number=4261&sha1=9f2ab97fbcaa18bcfbbe1cf342f6720a006baf9c&sha2=3d75f7bf60274a3692ba099561b2d65de85f647b&short_path=77b3519&w=false&utm_source=chatgpt.com)
- [Codex CLI global config options. · GitHub](https://gist.github.com/SuperPauly/8df862018a2e481c55b5bf7c2c215f37?utm_source=chatgpt.com)
- [ZodError / Schema Validation Failure when using GPT-5.2 series via OpenRouter · Issue #9863 · openai/codex · GitHub](https://github.com/openai/codex/issues/9863?utm_source=chatgpt.com)
- [Error occurred when connecting to the OpenRouter model · Issue #7731 · openai/codex](https://github.com/openai/codex/issues/7731?utm_source=chatgpt.com)
- [Custom Responses provider intermittently fails with native `namespace` tool routing errors · Issue #32318 · openai/codex · GitHub](https://github.com/openai/codex/issues/32318?utm_source=chatgpt.com)
- [github.com](https://github.com/openai/codex/diffs/0?base_sha=b581498882377e4066fd7a31baee963108290167&head_user=illgitthat&name=main&pull_number=2408&sha1=b581498882377e4066fd7a31baee963108290167&sha2=cc12733cd98a51d3dd65d921f33ed16b7e4aa7a4&short_path=b335630&w=false&utm_source=chatgpt.com)
- [codex-remote-bridge/ProxySpec.md at main · YusenDu/codex-remote-bridge · GitHub](https://github.com/YusenDu/codex-remote-bridge/blob/main/ProxySpec.md?utm_source=chatgpt.com)
- [GitHub - feiskyer/codex-settings: OpenAI Codex CLI settings, configurations, skills and prompts for vibe coding · GitHub](https://github.com/feiskyer/codex-settings?utm_source=chatgpt.com)
- [Bug Report: `/compact` Command Fails in Chat Completions API Mode · Issue #2417 · openai/codex](https://github.com/openai/codex/issues/2417?utm_source=chatgpt.com)
- [Add GLM 5.2 To Codex Via OpenRouter · GitHub](https://gist.github.com/WolframRavenwolf/e6c3755cc9919e2d258335707090eebc?utm_source=chatgpt.com)
- [Configure Codex with Amazon Bedrock | OpenAI Help Center](https://help.openai.com/en/articles/20001253-configure-codex-with-amazon-bedrock?utm_source=chatgpt.com)
- [GPT-5.3-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.3-codex?utm_source=chatgpt.com)
- [Models | OpenAI API](https://developers.openai.com/api/docs/models?utm_source=chatgpt.com)
- [All models | OpenAI API](https://developers.openai.com/api/docs/models/all?utm_source=chatgpt.com)
- [GPT-5-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5-codex?utm_source=chatgpt.com)
- [GPT-5.2-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.2-codex?utm_source=chatgpt.com)
- [codex-mini-latest Model | OpenAI API](https://developers.openai.com/api/docs/models/codex-mini-latest?utm_source=chatgpt.com)
- [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model?utm_source=chatgpt.com)
- [Models | OpenAI API](https://developers.openai.com/api/docs/models/text?utm_source=chatgpt.com)
- [Codex use cases](https://developers.openai.com/codex/use-cases?category=automation&category=integrations&category=ios&category=knowledge-work&category=quality&task_type=analysis&team=engineering&team=finance&team=quality-engineering&team=research&team=sales&utm_source=chatgpt.com)
- [Retrieve model | OpenAI API Reference](https://developers.openai.com/api/reference/typescript/resources/models/methods/retrieve?utm_source=chatgpt.com)
- [Codex use cases](https://developers.openai.com/codex/use-cases?category=data&category=engineering&category=front-end&category=integrations&category=ios&category=macos&search=Automation&task_type=analysis&task_type=code&task_type=testing&team=engineering&team=operations&team=sales&utm_source=chatgpt.com)
- [Create a model response | OpenAI API Reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/create?utm_source=chatgpt.com)
- [Codex CLI Custom Model Providers: The Complete Configuration Guide | Codex Knowledge Base](https://codex.danielvaughan.com/2026/04/23/codex-cli-custom-model-providers-configuration-guide/?utm_source=chatgpt.com)
- [model_provider — Codex config — Codex Insider](https://codexinsider.com/config/model-provider/?utm_source=chatgpt.com)
- [model_providers.<id>.base_url — Codex config — Codex Insider](https://codexinsider.com/config/model-providers-base-url/?utm_source=chatgpt.com)
- [Codex config.toml (2026): Add Any Custom Provider in 6 Lines (OpenRouter, Azure, Ollama, DeepSeek)](https://www.morphllm.com/codex-provider-configuration?utm_source=chatgpt.com)
- [Integration with Codex CLI | OpenRouter | OpenRouter | Documentation](https://openrouter.ai/docs/cookbook/coding-agents/codex-cli?utm_source=chatgpt.com)
- [Custom AI Providers - Codex CLI](https://www.mintlify.com/openai/codex/configuration/custom-providers?utm_source=chatgpt.com)
- [GPT Chat Latest - API Pricing & Providers | OpenRouter](https://openrouter.ai/openai/gpt-chat-latest/api?utm_source=chatgpt.com)
- [Codex CLI with OpenRouter: config.toml Setup and Models — OpenRouter Blog](https://openrouter.ai/blog/tutorials/codex-cli-openrouter/?utm_source=chatgpt.com)
- [codex/codex-rs/core/src/config/mod.rs at main · openai/codex · GitHub](https://github.com/openai/codex/blob/main/codex-rs/core/src/config/mod.rs?utm_source=chatgpt.com)
- [CodexPlusPlus/crates/codex-plus-core/src/relay_config.rs at main · BigPizzaV3/CodexPlusPlus · GitHub](https://github.com/BigPizzaV3/CodexPlusPlus/blob/main/crates/codex-plus-core/src/relay_config.rs?utm_source=chatgpt.com)
- [apply_relay_injection fallback 和 save_relay_file 覆盖 config.toml 时丢失已有 MCP servers (如 node_repl) · Issue #994 · BigPizzaV3/CodexPlusPlus · GitHub](https://github.com/BigPizzaV3/CodexPlusPlus/issues/994?utm_source=chatgpt.com)
- [github.com](https://github.com/openai/codex/diffs/11?base_sha=774892c6d7ddbe55bf8862748f9507b03b75c92f&head_user=kierr&name=main&pull_number=5220&qualified_name=refs%2Fheads%2Fmain&sha1=774892c6d7ddbe55bf8862748f9507b03b75c92f&sha2=f39108eace356b0212a0315f7bc24403b44e8f43&short_path=77b3519&unchanged=expanded&w=false&utm_source=chatgpt.com)
- [openai-platform/codex/config-reference.md at main · llms-txt-archive/openai-platform · GitHub](https://github.com/llms-txt-archive/openai-platform/blob/main/codex/config-reference.md?utm_source=chatgpt.com)
- [openai-mirror/developers.openai.com/codex/config-reference.md at main · ai-native-engineer/openai-mirror · GitHub](https://github.com/ai-native-engineer/openai-mirror/blob/main/developers.openai.com/codex/config-reference.md?utm_source=chatgpt.com)
- [Responses API: reasoning items with content: null rejected by non-OpenAI providers like Openrouter · Issue #11834 · openai/codex · GitHub](https://github.com/openai/codex/issues/11834?utm_source=chatgpt.com)
- [Running Codex on top of OpenRouter · GitHub](https://gist.github.com/monperrus/8e79efefb3d149857df1f388bc14361f?utm_source=chatgpt.com)
- [ZodError- code 400 · Issue #7721 · openai/codex](https://github.com/openai/codex/issues/7721?utm_source=chatgpt.com)
- [GPT-5 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/openai/gpt-5/api?utm_source=chatgpt.com)
- [GPT-4 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/openai/gpt-4/apps?tab=parameters&utm_source=chatgpt.com)
- [GPT-5.2 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/openai/gpt-5.2/providers?utm_source=chatgpt.com)
- [GPT-4o (2024-05-13) - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/openai/gpt-4o-2024-05-13/overview?utm_source=chatgpt.com)
- [Llama 3.2 1B Instruct - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/meta-llama/llama-3.2-1b-instruct/providers?utm_source=chatgpt.com)
- [GPT-5.2 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/openai/gpt-5.2/api?utm_source=chatgpt.com)
- [OpenAI GPT Latest - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/~openai/gpt-latest/activity?utm_source=chatgpt.com)
- [gpt-oss-120b - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/openai/gpt-oss-120b%3Aexacto/api?utm_source=chatgpt.com)
- [Request Builder | OpenRouter](https://openrouter.ai/request-builder?utm_source=chatgpt.com)
- [o4 Mini Deep Research - API Pricing & Providers | OpenRouter](https://openrouter.ai/openai/o4-mini-deep-research/api?utm_source=chatgpt.com)
- [o3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/openai/o3/providers?utm_source=chatgpt.com)
- [Responses | OpenAI API Reference](https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses?utm_source=chatgpt.com)
- [Get a model response | OpenAI API Reference](https://developers.openai.com/api/reference/cli/resources/responses/methods/retrieve?utm_source=chatgpt.com)
- [GPT-5.1-Codex Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.1-codex?utm_source=chatgpt.com)
- [Responses | OpenAI API Reference](https://developers.openai.com/api/reference/java/resources/beta/subresources/responses?utm_source=chatgpt.com)
- [Model guidance | OpenAI API](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.2&utm_source=chatgpt.com)
- [Create a model response | OpenAI API Reference](https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/methods/create?utm_source=chatgpt.com)
- [model_providers.<id>.env_key — Codex config — Codex Insider](https://www.codexinsider.com/config/model-providers-env-key/?utm_source=chatgpt.com)
- [Codex · Hugging Face](https://huggingface.co/docs/inference-providers/integrations/codex?utm_source=chatgpt.com)
- [Codex · Hugging Face](https://huggingface.co/docs/inference-providers/main/integrations/codex?utm_source=chatgpt.com)
- [Automatic Code Review for Claude Code — Async Reviews via Hooks + OpenRouter](https://openrouter.darenbot.com/docs/cookbook/coding-agents/automatic-code-review?utm_source=chatgpt.com)
- [Codex CLI Integration - OpenRouter](https://openrouter.darenbot.com/docs/cookbook/coding-agents/codex-cli?utm_source=chatgpt.com)
- [Codex CLI Custom Model Providers: Azure, Vercel, Local LLMs and Dynamic Bearer Tokens | Codex Knowledge Base](https://codex.danielvaughan.com/2026/03/31/codex-cli-custom-model-providers/?utm_source=chatgpt.com)
- [Codex CLI Model Catalogue Architecture: Providers, Discovery, and Debugging Model Resolution | Codex Knowledge Base](https://codex.danielvaughan.com/2026/05/04/codex-cli-model-catalogue-architecture-providers-discovery-debug/?utm_source=chatgpt.com)
- [docs/example-config.md · GitHub Zoo/codex - Gitee](https://gitee.com/github_zoo/codex/blob/main/docs/example-config.md?utm_source=chatgpt.com)
- [OpenAI Codex · Cloudflare AI Gateway docs](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/openai-codex/?utm_source=chatgpt.com)
- [Codex CLI with OpenRouter: Configuration Guide](https://agents.iwebtools.net/connect/codex/openrouter/?utm_source=chatgpt.com)
- [Codex config.toml (2026): Add Any Custom Provider in 6 Lines (OpenRouter, Azure, Ollama, DeepSeek)](https://t.co/IItHkagzwF?utm_source=chatgpt.com)
- [Responses — Layer X1](https://www.layerx1.com/docs/api/responses?utm_source=chatgpt.com)
