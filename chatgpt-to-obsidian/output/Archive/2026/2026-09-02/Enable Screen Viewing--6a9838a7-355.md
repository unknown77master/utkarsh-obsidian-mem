---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a9838a7-3550-83e8-a635-91a8c98cafe1"
created: 1788360977.808185
updated: 1788361797.312283
resource_section: true
---

# Enable Screen Viewing

## User

I understand you're asking, but I still can't directly view your screen—even as Openwiper, I'm designed to help through conversation, notes, calendar, and web searches rather than screen-sharing.
If you'd like, you can describe what you're seeing, share a note or document, or I can search for information about your topic. What would be most helpful?
I don't have direct access to your screen, but if you describe what you're seeing or share a note/snippet, I can help you work through it. What's on your mind?

this is the message i get i want it to view my screen
i want openwisper to view my screen
using minmax m3:free on openrouter which has image as input

## Assistant

Worked for 7s

## Assistant

Yes — MiniMax M3 itself is capable of seeing the screenshot. The problem is almost certainly **OpenWhisper’s request path/configuration**, not the model.

Your screenshot shows:

- **Share screen context = ON**
- **Separate vision model = ON**
- OpenRouter selected
- You’re trying to use `minimax/minimax-m3:free`

And OpenRouter currently lists MiniMax M3 as accepting **text + image + video input**. citeturn754627search1turn754627search8

The response:

> “I still can't directly view your screen…”

strongly suggests the screenshot is **not actually reaching MiniMax M3 as an image attachment**. The model is probably receiving only a text prompt saying something like “look at my screen”.

### First thing I would change

Turn **Separate vision model OFF**.

Since MiniMax M3 itself is multimodal, you don't need OpenWhisper to route the screenshot to some second vision model. With that setting enabled, OpenWhisper may be trying to use a separately configured/default vision provider which isn't set up correctly.

Keep:

**Share screen context:** ON 
**Separate vision model:** **OFF**

Then select:

```text
minimax/minimax-m3:free
```

as your main language model and test with something explicit like:

```text
What application is visible on my screen right now?
```

If that works, you've found the issue.

---

### If it still says it can't see the screen

Then we need to verify whether OpenWhisper is sending the screenshot in the correct OpenRouter format.

For OpenRouter `/api/v1/chat/completions`, a screenshot has to appear inside `messages\[\].content` as an image content block, for example:

```json
{
 "model": "minimax/minimax-m3:free",
 "messages": \[
 {
 "role": "user",
 "content": \[
 {
 "type": "text",
 "text": "Describe what is currently visible on my screen."
 },
 {
 "type": "image_url",
 "image_url": {
 "url": "data:image/png;base64,iVBORw0KGgo..."
 }
 }
 \]
 }
 \]
}
```

OpenRouter explicitly supports local images this way using base64 data URLs. citeturn754627search0turn754627search9

If OpenWhisper instead sends:

```json
{
 "role": "user",
 "content": "Describe my screen"
}
```

then MiniMax obviously has nothing visual to inspect and will give exactly the kind of refusal you're seeing.

### One important detail

Your screenshot shows this setting:

> **Separate vision model — Route commands that include a screenshot to a different, vision-capable model.**

That means OpenWhisper likely has **two routing paths**:

```text
Voice
 ↓
STT
 ↓
Normal LLM
```

and when vision routing is enabled:

```text
Voice
 ↓
STT
 ↓
Screenshot captured
 ↓
Separate Vision Model
```

If that second model isn't explicitly configured, or OpenWhisper doesn't recognize `minimax/minimax-m3:free` as a valid vision model through OpenRouter, the screenshot can get dropped.

Because M3 already supports images, the simpler path is:

```text
Voice
 \
 → MiniMax M3
 /
Screenshot
```

rather than maintaining a separate vision model.

### There's another possible OpenRouter compatibility issue

OpenRouter supports several API styles, including:

```text
/api/v1/chat/completions
/api/v1/responses
/api/v1/messages
```

MiniMax M3 is exposed through those OpenRouter interfaces. citeturn754627search4

If OpenWhisper uses OpenAI-style Chat Completions, it should send:

```json
{
 "type": "image_url",
 "image_url": {
 "url": "data:image/png;base64,..."
 }
}
```

If the application accidentally uses an Anthropic-style payload while talking to the OpenAI endpoint, or vice versa, vision can fail. This exact kind of formatting incompatibility has already appeared with MiniMax M3 integrations. citeturn754627search3

So your debugging order should be:

1. **Disable `Separate vision model`.**
2. Leave **Share screen context ON**.
3. Select `minimax/minimax-m3:free`.
4. Click **Refresh** after selecting the OpenRouter key/model.
5. Restart OpenWhisper if necessary.
6. Ask: **“Read the text in the top-left corner of my screen.”**

Don't ask simply:

```text
Can you see my screen?
```

because some assistant system prompts are written to reflexively answer that they don't have screen access. Ask a visual question that can only be answered from the screenshot.

For example:

```text
Look at the attached screen context and tell me which browser tabs are currently open.
```

or:

```text
Using the screen image included with this request, what website is currently open?
```

That will tell us immediately whether the image is arriving.

Based on the second screenshot you sent me, **MiniMax M3 should absolutely be capable of interpreting that screen**. OpenRouter explicitly marks it as an image-input model; the missing piece is getting OpenWhisper to attach the captured screenshot to the API request. citeturn754627search1

If disabling **Separate vision model** still doesn't work, send me the **OpenWhisper GitHub repo/link** you're using. I can inspect exactly how its screen-context request is built and tell you which config/code needs changing.

## User

I'm unable to access or view your screen directly. If you can describe what you're seeing — apps, windows, error messages, etc. — I'd be happy to help you interpret it or guide you through next steps.
no after **Disable** **`Separate vision model`****\*\*\*\*.**

1. Leave **Share screen context ON**.
2. Select `minimax/minimax-m3:free`.
3. Click **Refresh** after selecting the OpenRouter key/model.
4. Restart OpenWhisper if necessary.

not able to view my screen. use firescrape to get details about this issue is common or has it been resolved or raised

## Assistant

Worked for 24s

## Assistant

Yes — I found something important. **This is a real OpenWhispr failure mode, and the project has already added fixes specifically around screenshots being rejected by models/providers.**

OpenWhispr added screen context in merged PR **#1195**. On Windows it captures the monitor under your cursor, resizes it to at most 1568 px on the long edge, converts it to base64 JPEG, and attaches it to the Voice Agent request. So on Windows, there is **no extra screen-recording permission requirement**. The feature itself should work with your setup.

More importantly, OpenWhispr later merged **#1566**, which explicitly mentions:

> **“Selection edits survive rejected screenshots”**

and their own smoke-test scenario is essentially:

> Screen Context ON + **a model that rejects images** → fall back to text-only and show **“Screen Context Skipped”**.

That is extremely relevant to what you're seeing. It means OpenWhispr already knows that some selected model/provider combinations can reject the screenshot even though the rest of the LLM request works.

There is also a very recent OpenWhispr issue, **#1958**, where a maintainer confirmed on **Aug 31, 2026** that screen viewing already works through Voice Assistant:

1. Settings → AI Models → Voice Assistant
2. Enable Voice Assistant
3. Enable **Share screen context**
4. Use a vision-capable model or a separate vision model

They explicitly state that **Windows requires no additional permission**.

So the problem is **not that OpenWhispr cannot see Windows screens**.

### What I think is happening in your case

Your exact combination is:

```text
OpenWhispr
 ↓
OpenRouter
 ↓
minimax/minimax-m3:free
 ↓
image + text
```

MiniMax M3 itself supports vision, but there are already reports elsewhere of **MiniMax M3 multimodal requests failing through intermediary/provider integrations** even though text requests work.

For example, there is currently an OpenCode issue involving MiniMax M3 where:

```text
text → works
image → fails
```

despite MiniMax M3 supporting multimodality. The problem there is the integration/API formatting/routing rather than the model itself.

I also found another OpenRouter-related vision integration warning specifically about **`:free` routes**: a model can advertise image support globally while the particular free endpoint you get routed to may not accept the image request. That can produce exactly this kind of behavior:

```text
OpenWhispr captures screenshot ✅
 ↓
OpenWhispr attaches screenshot ✅
 ↓
OpenRouter route rejects / cannot use image ❌
 ↓
OpenWhispr's image retry/fallback activates
 ↓
request continues WITHOUT image
 ↓
MiniMax receives only text
 ↓
"I'm unable to access or view your screen."
```

That last part matches your symptoms extremely well.

## There is one very useful diagnostic in OpenWhispr now

PR **#1566** also added debug logging specifically for this feature:

```text
ROUTE_RESOLVED
AGENT_IMAGE_TARGET
```

The maintainers added those logs precisely so screen-context routing problems can be diagnosed.

So instead of randomly changing settings now, we should check the logs.

Trigger one command such as:

```text
Look at the screenshot attached to this request.
What website is currently open on my screen?
```

Then inspect the OpenWhispr log for:

```text
ROUTE_RESOLVED
```

and:

```text
AGENT_IMAGE_TARGET
```

Also look for:

```text
Screen Context Skipped
```

or anything containing:

```text
image
vision
screenshot
400
OpenRouter
retry
```

If you get **Screen Context Skipped**, that basically confirms it: **OpenWhispr captured the screen, tried MiniMax M3, the image request was rejected, and OpenWhispr silently retried without the screenshot.**

## The fastest experiment

Don't change anything except the model.

Keep:

```text
Share screen context = ON
Separate vision model = OFF
Provider = OpenRouter
```

Temporarily change:

```text
minimax/minimax-m3:free
```

to a known OpenRouter vision model.

It doesn't need to be your permanent model. We're using it as a control test.

Then say:

```text
Read the title of the browser tab I'm currently looking at.
```

There are only two meaningful outcomes:

| Result | Meaning |
|---|---|
| Other vision model sees screen | **MiniMax M3 `:free` / OpenRouter route is the problem** |
| Other vision model also can't see it | **OpenWhispr screenshot attachment/routing is broken on your installation/version** |

That test will tell us far more than toggling Separate Vision Model repeatedly.

### Also check your OpenWhispr version

Screen context was reported as available starting around **OpenWhispr 1.8.3**, and several fixes affecting this flow were merged afterward.

So if you're running an older build, upgrade before digging into API payloads.

The most interesting detail from the repository is that newer builds actually contain explicit **screenshot rejection → text-only retry logic**. Therefore the polite response you're receiving does **not necessarily mean OpenWhispr failed to capture your screen**. It may mean the image was captured, rejected downstream, stripped, and then MiniMax was called again as text-only.

If you paste the OpenWhispr debug log from **one failed screen question**, especially the lines around `ROUTE_RESOLVED` and `AGENT_IMAGE_TARGET`, I can tell you which exact stage is dropping the screenshot. memcite

## User

for stt i am using local modal

## Assistant

Worked for a couple of seconds

## Assistant

That’s fine. Your **local STT model is not the issue**.

Your pipeline is effectively:

```text
Your voice
 ↓
Local Whisper Turbo
 ↓
transcript text
 ↓
Voice Assistant / Agent
 ├── transcript text
 └── screenshot
 ↓
 OpenRouter → MiniMax M3
```

So **Speech-to-Text and screen vision are separate stages**. Local Whisper Turbo only converts your voice into text. It does not need multimodal/vision capability.

Your screenshot confirms a sensible setup:

```text
STT
Local → OpenAI Whisper Turbo ✅

Language Model / Voice Assistant
OpenRouter → minimax/minimax-m3:free

Screen Context
Share screen context → ON ✅
```

The failure therefore happens **after transcription**, when OpenWhispr constructs the Voice Assistant request.

There is one distinction that matters a lot: make sure you are invoking the **Voice Assistant hotkey**, not normal **Dictation**.

The OpenWhispr maintainer specifically says screen context is currently attached to the **Voice Assistant / Agent Mode** workflow. It is *not* automatically applied to ordinary dictation cleanup. The recent issue #1958 was actually asking for screen context to be added to normal dictation cleanup; the maintainer replied that users should use Voice Assistant for this today.

So if you press your ordinary dictation shortcut and say:

> “What is on my screen?”

you can end up with a model call that has **no screenshot at all**, regardless of that toggle.

Go to:

**Settings → Hotkeys**

and find the shortcut corresponding to **Voice Assistant**. Use that shortcut specifically.

Then test:

> “Using the screenshot attached to this request, tell me which application is currently in front.”

If you are already definitely using the Voice Assistant hotkey, then we can rule out STT completely. At that point, I’d focus on **`minimax/minimax-m3:free` being rejected or misdetected for image input by OpenWhispr/OpenRouter**.

A clean diagnostic would be:

```text
Local Whisper Turbo
 ↓
Voice Assistant hotkey
 ↓
Share screen context ON
 ↓
known-good OpenRouter vision model
```

If that model sees your screen, your entire OpenWhispr + Windows + local-STT setup is working and **MiniMax M3 `:free` is the only variable left**.

So don't change your local Whisper Turbo. **Keep it.**

Next, show me your **OpenWhispr → Settings → Hotkeys** page. I want to make sure you're actually triggering the Voice Assistant route rather than normal Dictation.

## User

I can't view attached images, but if you tell me the name of the app or any text you see in the screenshot, I can help you figure out what to do next or look up related info. What does it say?

this was the response from openwisper after agent hot key

## Assistant

Worked for 14s

## Assistant

That response is actually the clearest signal so far:

> **“I can't view attached images…”**

You are definitely hitting the **Voice Assistant route**, but MiniMax is behaving as though **no usable image reached it**.

I searched the current GitHub/developer index again, and there is stronger evidence that this is a **MiniMax M3 + intermediary routing problem**, not your local STT or Windows capture.

One recent integration report describes MiniMax M3 vision requests that returned **HTTP 200** but the model still received no image and simply behaved as text-only. Another OpenRouter integration successfully tested MiniMax M3 with PNG/JPEG, which means the model itself *can* work through OpenRouter; therefore the exact client payload/routing path matters. There are also reports that OpenRouter's upstream provider selection can matter: the model may advertise vision while a particular serving endpoint does not correctly accept that image form.

So at this point your likely pipeline is:

```text
Voice Assistant hotkey ✅
 ↓
Local Whisper Turbo ✅
 ↓
Screen capture probably succeeds ✅
 ↓
OpenWhispr builds image request
 ↓
OpenRouter / MiniMax M3 integration
 ↓
image missing / stripped / unsupported upstream ❌
 ↓
MiniMax receives text only
 ↓
"I can't view attached images"
```

### Best next test: use `Separate vision model` ON

My earlier suggestion to turn it off was reasonable because M3 is natively multimodal, but given what we've now found, **for your specific setup I would reverse that**.

Keep MiniMax M3 as your regular assistant model, but enable:

```text
Share screen context: ON
Separate vision model: ON
```

Then choose a **different known-good vision model** as the separate vision model.

That tests this architecture:

```text
 ┌─ MiniMax M3 → normal voice commands
Voice Assistant ────┤
 │
Screenshot ─────────┴─ dedicated vision model
```

If that works, you don't need to abandon MiniMax M3. You can use M3 for normal reasoning/tool use while routing screenshots through a more reliable vision endpoint.

### But there is an even better diagnostic

OpenWhispr added debug logs specifically for this:

```text
ROUTE_RESOLVED
AGENT_IMAGE_TARGET
```

We should look at those now rather than guessing.

On Windows, reproduce once:

> **Using the screenshot attached to this request, tell me which application is currently in front.**

Then get the OpenWhispr logs and search for:

```text
ROUTE_RESOLVED
AGENT_IMAGE_TARGET
Screen Context Skipped
image
screenshot
vision
OpenRouter
400
422
retry
```

If you paste ~20–40 lines around `AGENT_IMAGE_TARGET`, I can tell whether:

```text
capture failed
 vs
capture succeeded but OpenWhispr didn't attach it
 vs
OpenRouter rejected it
 vs
OpenWhispr stripped it and retried
 vs
MiniMax accepted the API request but ignored the image
```

That is now the most useful thing to investigate.

Also, **keep Local Whisper Turbo exactly as it is**. We've effectively ruled STT out. Your voice is clearly getting transcribed and reaching the assistant correctly; only the image channel is broken.

## Resources

### Local attachments
- [869457b4-fe15-48e7-9b0b-1f2cf5590599.png](../../../Raw/Export/file_00000000a1c4820ba975ef6164da94c1.dat)
- [Screenshot 2026-09-02 201728.png](../../../Raw/Export/file_000000005cec8209b9ab9d288dc4274f.dat)
- [7a79d5f9-1128-447a-abfc-d9fe54483324.png](../../../Raw/Export/file_000000005de0820b90f80cbd3c3e5dee.dat)

### External references
- [OpenRouter Multimodal Capabilities - Complete Documentation](https://openrouter.ai/docs/guides/overview/multimodal/overview)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/minimax/minimax-m3)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/minimax/minimax-m3/benchmarks)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/minimax/minimax-m3/apps)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/minimax/minimax-m3-20260531/benchmarks)
- [MiniMax API and Models | OpenRouter](https://openrouter.ai/minimax)
- [text chat: expose image input (enable multimodal M3, incl. multi-image) · Issue #224 · MiniMax-AI/cli · GitHub](https://github.com/MiniMax-AI/cli/issues/224)
- [MiniMax M3 Multimodal API: Images and Video](https://minimax-ai.chat/docs/minimax-m3-multimodal-api/)
- [Provider Integration - Add Your Models to OpenRouter](https://openrouter.darenbot.com/docs/guides/community/for-providers)
- [OpenRouter PDF Inputs - Complete Documentation](https://openrouter.darenbot.com/docs/guides/overview/multimodal/pdfs)
- [How to Send an Image to an LLM via API (Vision Guide) — OpenRouter Blog](https://openrouter.helicone.ai/blog/tutorials/send-image-to-llm/)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/minimax/minimax-m3?utm_source=chatgpt.com)
- [MiniMax API and Models | OpenRouter](https://openrouter.ai/minimax?utm_source=chatgpt.com)
- [OpenRouter Multimodal Capabilities - Complete Documentation](https://openrouter.ai/docs/guides/overview/multimodal/overview?utm_source=chatgpt.com)
- [How to Send an Image to an LLM via API (Vision Guide) — OpenRouter Blog](https://openrouter.helicone.ai/blog/tutorials/send-image-to-llm/?utm_source=chatgpt.com)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/minimax/minimax-m3/apps?utm_source=chatgpt.com)
- [text chat: expose image input (enable multimodal M3, incl. multi-image) · Issue #224 · MiniMax-AI/cli · GitHub](https://github.com/MiniMax-AI/cli/issues/224?utm_source=chatgpt.com)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/minimax/minimax-m3/benchmarks?utm_source=chatgpt.com)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/minimax/minimax-m3-20260531/benchmarks?utm_source=chatgpt.com)
- [How to Send an Image to an LLM via API (Vision Guide) — OpenRouter Blog](https://openrouter.ai/blog/tutorials/send-image-to-llm/?utm_source=chatgpt.com)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.ai/minimax/minimax-m3/uptime?utm_source=chatgpt.com)
- [OpenRouter API and Models | OpenRouter](https://openrouter.ai/openrouter?utm_source=chatgpt.com)
- [MiniMax M3 Multimodal API: Images and Video](https://minimax-ai.chat/docs/minimax-m3-multimodal-api/?utm_source=chatgpt.com)
- [Provider Integration - Add Your Models to OpenRouter](https://openrouter.darenbot.com/docs/guides/community/for-providers?utm_source=chatgpt.com)
- [OpenRouter PDF Inputs - Complete Documentation](https://openrouter.darenbot.com/docs/guides/overview/multimodal/pdfs?utm_source=chatgpt.com)
- [MiniMax M3 - API Pricing & Benchmarks | OpenRouter](https://openrouter.siluerp.cn/minimax/minimax-m3?utm_source=chatgpt.com)
- [GitHub - getpipher/vision: Capability-aware vision + paste extension for the pi coding agent. Delegates image analysis only when the active model is text-only; passes through natively for multimodal models (zero delegation). · GitHub](https://github.com/getpipher/vision?utm_source=chatgpt.com)
- [GitHub - zakcali/open-router: Gradio chat, image input, image output user interfaces to be used with openrouter api key · GitHub](https://github.com/zakcali/open-router?utm_source=chatgpt.com)
- [GitHub - ruby1304/dsh-vision-subagent: Vision for DeepSeek Harness agents — paste images in the Web composer, delegate reads to Kimi/MiniMax vision routes on isolated contexts; zero image bytes in the main session · GitHub](https://github.com/ruby1304/dsh-vision-subagent?utm_source=chatgpt.com)
- [openwhisper/STATUS.md at main · Razepriv/openwhisper · GitHub](https://github.com/Razepriv/openwhisper/blob/main/STATUS.md?utm_source=chatgpt.com)
- [GitHub - Arjunhg/onevision · GitHub](https://github.com/Arjunhg/onevision?utm_source=chatgpt.com)
- [GitHub - stabgan/openrouter-mcp-multimodal at explainx · GitHub](https://github.com/stabgan/openrouter-mcp-multimodal?ref=explainx&utm_source=chatgpt.com)
- [ouroboros/ouroboros/llm.py at main · razzant/ouroboros · GitHub](https://github.com/razzant/ouroboros/blob/main/ouroboros/llm.py?utm_source=chatgpt.com)
- [GitHub - SunnyLich/OpenWand at launches.uicomet.com · GitHub](https://github.com/SunnyLich/OpenWand?ref=launches.uicomet.com&utm_source=chatgpt.com)
- [minimax-m3 API - openrouter/minimax-m3 | inference shell](https://inference.sh/apps/openrouter/minimax-m3?utm_source=chatgpt.com)
- [MiniMax: MiniMax M3 · Models · Pi](https://pi.dev/models/openrouter/minimax-minimax-m3?utm_source=chatgpt.com)
- [ai-context-bridge/server.mjs at clean-main · ZahraAmiriCa/ai-context-bridge · GitHub](https://ithub.global.ssl.fastly.net/ZahraAmiriCa/ai-context-bridge/blob/clean-main/server.mjs?utm_source=chatgpt.com)
- [GitHub - stabgan/openrouter-mcp-multimodal: MCP server for OpenRouter — chat with 300+ LLMs (Claude, Gemini, GPT), analyze images / audio / video, generate images / speech / music / video (Veo 3.1, Sora, Seedance, Wan) from Claude Desktop, Cursor, Kiro, VS Code. · GitHub](https://ithub.global.ssl.fastly.net/stabgan/openrouter-mcp-multimodal?utm_source=chatgpt.com)
- [How to Send an Image to an LLM via API (Vision Guide) — OpenRouter Blog](https://openrouter.vitalitytex.com.cn/blog/tutorials/send-image-to-llm/?utm_source=chatgpt.com)
- [openrouter/ directory - github.com/shepard-labs/go-ai-sdk/examples/openrouter - Go Packages](https://pkg.go.dev/github.com/shepard-labs/go-ai-sdk/examples/openrouter?utm_source=chatgpt.com)
