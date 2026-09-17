---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "698ce9df-182c-83a2-92b7-95344c14d42a"
created: 1770842665.569207
updated: 1770843018.085893
resource_section: true
---

# XSS Warning in HTML Sanitization

## User

i imported curl curl -X POST "https://api.kie.ai/api/v1/jobs/createTask" \ -H "Content-Type: application/json" \ -H "Authorization: Bearer YOUR_API_KEY" \ -d '{ "model": "sora-2-text-to-video", "callBackUrl": "https://your-domain.com/api/callback", "progressCallBackUrl": "https://your-domain.com/api/v1/jobs/progressCallBackUrl", "input": { "prompt": "A professor stands at the front of a lively classroom, enthusiastically giving a lecture. On the blackboard behind him are colorful chalk diagrams. With an animated gesture, he declares to the students: “Sora 2 is now available on Kie AI, making it easier than ever to create stunning videos.” The students listen attentively, some smiling and taking notes.", "aspect_ratio": "landscape", "n_frames": "10", "remove_watermark": true, "upload_method": "s3" }

getting error
Your `allowedTags` option includes, `style`, which is inherently
vulnerable to XSS attacks. Please remove it from `allowedTags`.
Or, to disable this warning, add the `allowVulnerableTags` option
and ensure you are accounting for this risk.

## Assistant

The error you are encountering is **not related to the curl request itself**. 
It is coming from a **backend HTML sanitization library** (most likely `sanitize-html` in Node.js).

---

# 📌 Why This Error Occurs

The message:

> Your `allowedTags` option includes `style`, which is inherently vulnerable to XSS attacks.

means:

- Your server is sanitizing incoming content.
- It has a configuration like:

```js
allowedTags: \['b', 'i', 'em', 'strong', 'style'\]
```

- The library is warning that allowing `<style>` tags can lead to **Cross-Site Scripting (XSS)** attacks.

This error is triggered **before or during processing of your API request**, not by the Kie AI API.

---

# 📌 Important Clarification

Your curl request is valid syntax-wise.

The issue is inside your application where:

- You receive data
- You sanitize HTML
- The sanitizer is configured incorrectly

---

# 📌 Root Cause (Most Likely Scenario)

Somewhere in your Node.js backend:

```js
sanitizeHtml(input, {
 allowedTags: \['style', ...\]
})
```

The `style` tag is dangerous because:

- It allows CSS injection
- CSS can be used for malicious behavior (data exfiltration, clickjacking tricks, etc.)

Modern versions of `sanitize-html` block it by default.

---

# ✅ Proper Fix (Recommended)

### Remove `style` from allowedTags

```js
sanitizeHtml(input, {
 allowedTags: sanitizeHtml.defaults.allowedTags
})
```

OR explicitly:

```js
sanitizeHtml(input, {
 allowedTags: \['b', 'i', 'em', 'strong', 'p', 'br'\]
})
```

This is the safest solution.

---

# ⚠️ Alternative (Not Recommended for Production)

If you truly need `<style>` tags:

```js
sanitizeHtml(input, {
 allowedTags: \['style', ...\],
 allowVulnerableTags: true
})
```

But this should only be used when:

- You fully trust input
- It is an internal system
- You understand XSS implications

---

# 📌 Why This Is Not a Kie AI Problem

Your curl request:

- Is JSON
- Contains no HTML
- Contains no `<style>` tag

Therefore:

The error is coming from your own server, not from:

- curl
- Kie AI
- Sora-2 model

---

# 📌 Debugging Steps

1. Search your backend project for:
 ```
 allowedTags
 ```
2. Locate sanitize-html configuration
3. Remove `'style'`
4. Restart server

---

# 🎯 Engineering-Level Understanding

From a security perspective:

Allowing `<style>` enables:
- CSS-based data exfiltration
- Overlay attacks
- UI redressing
- Token theft via CSS selectors

Therefore modern libraries intentionally block it.

---

If you want, tell me:

- What backend are you using? (Express? Next.js API route?)
- Where exactly the error appears? (terminal? browser? response JSON?)

I will give you a precise fix tailored to your stack.

## User

i am getting error on local hosted n8n

## Assistant

Good. Now we are narrowing the problem correctly.

Since the error is coming from **locally hosted n8n**, the issue is **inside n8n’s HTML sanitization layer**, not your curl request and not the Kie API.

---

# 📌 Why This Happens in n8n

n8n sanitizes HTML in certain nodes for security reasons (especially in):

- Webhook nodes 
- HTTP Request nodes 
- Respond to Webhook node 
- Markdown / HTML rendering in UI 

Internally it uses a sanitizer that blocks `<style>` because it is considered vulnerable to XSS.

Even if your payload is JSON, sometimes:

- n8n interprets part of the request as HTML
- Or a node is configured to expect HTML
- Or credentials / headers contain unexpected formatting

---

# 🎯 Most Likely Cause in Your Case

You are probably:

- Using a **Webhook node**
- Or sending raw body data
- Or copying curl directly into HTTP Request node

And n8n is sanitizing something that contains `style`.

---

# ✅ Proper Fix (Safe Method)

### 1️⃣ In HTTP Request Node

Make sure:

- Method → `POST`
- Send Body → `JSON`
- Content-Type → `application/json`
- Do NOT use "RAW" or "HTML"

Body should be added using JSON mode, not pasted as raw text.

---

# ✅ If You Are Using Webhook Node

In Webhook settings:

- Response Mode → `On Received`
- Or properly configure `Respond to Webhook`

Avoid returning raw HTML.

---

# 🚨 If Error Still Appears

This means your **n8n instance is configured with unsafe sanitizer settings**.

Since you're running locally, you can modify the environment variable:

Check your n8n `.env` or docker config.

Look for anything related to:

```
N8N_SANITIZE_HTML
```

If present, disable or adjust it.

---

# 🛠 If Running via Docker

Check your docker-compose file.

Add:

```yaml
environment:
 - N8N_SECURE_COOKIE=false
```

(only if testing locally)

Restart container after change.

---

# 🔎 Very Important Check

Are you pasting the entire curl command inside an n8n node?

If yes — that is wrong.

You must only extract:

- URL
- Headers
- JSON body

And configure them properly in the HTTP Request node.

---

# 📌 Correct n8n HTTP Node Setup

**URL**
```
https://api.kie.ai/api/v1/jobs/createTask
```

**Headers**
```
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

**Body (JSON mode)**

```json
{
 "model": "sora-2-text-to-video",
 "callBackUrl": "https://your-domain.com/api/callback",
 "progressCallBackUrl": "https://your-domain.com/api/v1/jobs/progressCallBackUrl",
 "input": {
 "prompt": "A professor stands at the front...",
 "aspect_ratio": "landscape",
 "n_frames": "10",
 "remove_watermark": true,
 "upload_method": "s3"
 }
}
```

Do not paste it as raw string with quotes inside quotes.

---

# 🎓 Technical Explanation (As in Exam)

The error arises because n8n uses an HTML sanitization mechanism to prevent cross-site scripting attacks. When the configuration includes the `style` tag under allowedTags, the sanitizer flags it as vulnerable. This occurs even if the original request is JSON, due to internal content processing.

---

Now tell me:

- Are you running n8n via Docker or npm?
- Which node is throwing the error? (Webhook / HTTP Request / Function?)

Give me that detail and I will give you the exact correction.

## User

{
 "errorMessage": "JSON parameter needs to be valid JSON",
 "errorDetails": {},
 "n8nDetails": {
 "nodeName": "HTTP Request",
 "nodeType": "n8n-nodes-base.httpRequest",
 "nodeVersion": 4.4,
 "itemIndex": 0,
 "time": "2/12/2026, 2:18:43 AM",
 "n8nVersion": "2.6.4 (Self Hosted)",
 "binaryDataMode": "filesystem",
 "stackTrace": \[
 "NodeOperationError: JSON parameter needs to be valid JSON",
 " at ExecuteContext.execute (/usr/local/lib/node_modules/n8n/node_modules/.pnpm/n8n-nodes-base@file+packages+nodes-base_@aws-sdk+credential-providers@3.808.0_asn1.js@5_8da18263ca0574b0db58d4fefd8173ce/node_modules/n8n-nodes-base/nodes/HttpRequest/V3/HttpRequestV3.node.ts:447:15)",
 " at WorkflowExecute.executeNode (/usr/local/lib/node_modules/n8n/node_modules/.pnpm/n8n-core@file+packages+core_@opentelemetry+api@1.9.0_@opentelemetry+sdk-trace-base@1.30_ec37920eb95917b28efaa783206b20f3/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1069:31)",
 " at WorkflowExecute.runNode (/usr/local/lib/node_modules/n8n/node_modules/.pnpm/n8n-core@file+packages+core_@opentelemetry+api@1.9.0_@opentelemetry+sdk-trace-base@1.30_ec37920eb95917b28efaa783206b20f3/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1250:22)",
 " at /usr/local/lib/node_modules/n8n/node_modules/.pnpm/n8n-core@file+packages+core_@opentelemetry+api@1.9.0_@opentelemetry+sdk-trace-base@1.30_ec37920eb95917b28efaa783206b20f3/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:1685:38",
 " at /usr/local/lib/node_modules/n8n/node_modules/.pnpm/n8n-core@file+packages+core_@opentelemetry+api@1.9.0_@opentelemetry+sdk-trace-base@1.30_ec37920eb95917b28efaa783206b20f3/node_modules/n8n-core/src/execution-engine/workflow-execute.ts:2328:11"
 \]
 }
}

## Assistant

Excellent. Now this is a completely different error.

This is **not** about sanitizer anymore.

The real issue is:

> `"JSON parameter needs to be valid JSON"`

This means the **Body field in your HTTP Request node is not properly formatted JSON**.

---

# 🎯 Why This Happens in n8n

In n8n HTTP Request node (v4.4):

When you select:

- **Body Content Type → JSON**
- **Specify Body → Using JSON**

Then n8n expects:

✔ Pure JSON object 
❌ Not a string 
❌ Not escaped 
❌ Not copied curl format 
❌ No trailing commas 
❌ No single quotes 

---

# ❌ Most Common Mistake

You probably pasted something like this:

```json
'{ 
 "model": "sora-2-text-to-video",
 ...
}'
```

OR

```json
{
 "model": "sora-2-text-to-video",
 "n_frames": "10",
}
```

Notice:
- ❌ Wrapping JSON inside quotes
- ❌ Trailing comma
- ❌ Invalid syntax

That will trigger this exact error.

---

# ✅ Correct Way to Configure n8n HTTP Node

### Step 1

HTTP Request Node Settings:

- Method → `POST`
- URL → `https://api.kie.ai/api/v1/jobs/createTask`
- Authentication → None
- Send Headers → ON

Headers:

| Name | Value |
|------|-------|
| Authorization | Bearer YOUR_API_KEY |
| Content-Type | application/json |

---

### Step 2

Body Content Type → `JSON`

Specify Body → `Using JSON`

Paste this EXACTLY (no quotes around entire object):

```json
{
 "model": "sora-2-text-to-video",
 "callBackUrl": "https://your-domain.com/api/callback",
 "progressCallBackUrl": "https://your-domain.com/api/v1/jobs/progressCallBackUrl",
 "input": {
 "prompt": "A professor stands at the front of a lively classroom, enthusiastically giving a lecture. On the blackboard behind him are colorful chalk diagrams. With an animated gesture, he declares to the students: Sora 2 is now available on Kie AI, making it easier than ever to create stunning videos.",
 "aspect_ratio": "landscape",
 "n_frames": 10,
 "remove_watermark": true,
 "upload_method": "s3"
 }
}
```

---

# 🔎 Important Fix I Applied

1. Removed curly quotes inside prompt 
2. Changed `"n_frames": "10"` → `"n_frames": 10` 
 (should be number, not string)
3. Removed fancy quotes around the sentence

Smart quotes like:

```
“Sora 2 is now available...”
```

can break JSON parsing in some environments.

Replace them with normal quotes or remove them.

---

# 🎓 Conceptual Explanation (Exam Style)

The error occurs because JSON syntax requires strict formatting rules. If the body contains improperly escaped characters, trailing commas, or is wrapped as a string literal instead of an object, the parser throws a validation error. n8n enforces strict JSON compliance before sending the HTTP request.

---

# 🚀 Quick Validation Trick

Before pasting into n8n:

1. Go to https://jsonlint.com
2. Paste your JSON
3. Validate
4. Then paste into n8n

---

If it still fails, send me a screenshot of your HTTP node configuration (without API key). I will pinpoint the exact mistake immediately.

## User

Are you running n8n via Docker or npm?

Which node is throwing the error? (Webhook / HTTP Request / Function?)
docker, http

## Assistant

Good. Since you are running **n8n via Docker** and the error is coming from the **HTTP Request node**, the issue is strictly configuration-related — not Docker, not sanitizer, not Kie AI.

---

# 🎯 Clear Diagnosis

The error:

> `JSON parameter needs to be valid JSON`

means:

The **Body field in the HTTP Request node is not syntactically valid JSON**.

In n8n v2.x (HTTP Request v4), this happens when:

- JSON is wrapped in quotes
- There is a trailing comma
- There are smart quotes (“ ”)
- There is an unescaped character
- You pasted raw curl instead of structured JSON
- Expression mode is mixing with plain JSON

---

# ✅ Correct Configuration (Step-by-Step)

## 1️⃣ HTTP Request Node

- **Method** → `POST`
- **URL** → 
 ```
 https://api.kie.ai/api/v1/jobs/createTask
 ```

---

## 2️⃣ Headers

Enable “Send Headers”

Add:

| Name | Value |
|------|-------|
| Authorization | Bearer YOUR_API_KEY |
| Content-Type | application/json |

---

## 3️⃣ Body Configuration (VERY IMPORTANT)

- **Body Content Type** → `JSON`
- **Specify Body** → `Using JSON`

Then paste this **exactly**:

```json
{
 "model": "sora-2-text-to-video",
 "callBackUrl": "https://your-domain.com/api/callback",
 "progressCallBackUrl": "https://your-domain.com/api/v1/jobs/progressCallBackUrl",
 "input": {
 "prompt": "A professor stands at the front of a lively classroom, enthusiastically giving a lecture. On the blackboard behind him are colorful chalk diagrams. With an animated gesture, he declares to the students that Sora 2 is now available on Kie AI, making it easier than ever to create stunning videos.",
 "aspect_ratio": "landscape",
 "n_frames": 10,
 "remove_watermark": true,
 "upload_method": "s3"
 }
}
```

---

# 🚨 Critical Checks

### ✔ Do NOT:
- Wrap entire JSON in quotes
- Use single quotes `'`
- Leave trailing commas
- Use fancy quotes like “ ”
- Turn on Expression mode accidentally

---

# 🔎 If It Still Fails

Switch to this alternative method:

### Instead of "Using JSON"

Select:

- **Body Content Type** → `RAW`
- Then choose `JSON`

Paste the same object there.

Sometimes this bypasses parsing quirks in v4.

---

# 🧠 Why Docker Is Not the Issue

Docker only runs the n8n container. 
The JSON parsing happens inside the HTTP Request node before sending the request.

Therefore:

Container configuration is irrelevant in this case.

---

# 🎓 Conceptual Understanding (Exam Style)

The HTTP Request node validates JSON syntax before execution. If the body is not a properly formatted JSON object according to ECMAScript JSON specification (RFC 8259), the node throws a NodeOperationError and halts execution.

---

If you want, paste exactly what you have inside the Body field (remove API key). I will identify the syntax error immediately.

## Resources

No structured attachments or external references were present in this conversation.
