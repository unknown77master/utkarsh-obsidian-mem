---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a6080e2-34e8-83ee-9c7c-2ae8d4c07ebb"
created: 1784709368.444029
updated: 1784709404.963843
resource_section: true
---

# Grok Imagine Pricing Clarification

## User

Pricing: 1.6 credits per second for 480p (≈ $0.008), 3 credits per second for 720p (≈ $0.015)— video generation is about 90% of official pricing.
this this true? model is grock imagine 1.5

## Assistant

No, **that statement is not true for the official xAI API pricing**.

The claim:

> **1.6 credits/sec for 480p (≈ $0.008), 3 credits/sec for 720p (≈ $0.015) — about 90% of official pricing**

does **not** match xAI's official documentation.

According to the official xAI docs for **Grok Imagine Video 1.5**:

| Resolution | Official API Price |
|------------|-------------------:|
| 480p | **$0.08 per second** |
| 720p | **$0.14 per second** |
| Input image | **$0.01 per image** | citeturn0search0

### Compare the numbers

| Claim | Official |
|-------|---------:|
| 480p: **$0.008/sec** | **$0.08/sec** |
| 720p: **$0.015/sec** | **$0.14/sec** |

The claimed prices are roughly **10× cheaper** than the official API prices—not "90% of official pricing." citeturn0search0

### So where do those "credits" come from?

The values like:

- **1.6 credits/sec**
- **3 credits/sec**

are **platform-specific credit systems** used by third-party providers (or self-hosted gateways). A "credit" has no universal dollar value.

For example:

- A provider might define **1 credit = $0.005**
- Another might define **1 credit = $0.02**
- Another might simply subsidize the model to attract users.

So you **cannot compare credits directly with xAI pricing** unless the provider explicitly states how much one credit is worth.

### If you're using an API provider (OpenRouter, Kie AI, FAL, Segmind, etc.)

That pricing may be **their own pricing**, not xAI's. They often:
- subsidize costs,
- charge different margins,
- or use an internal credit system.

If you tell me **which website or provider** showed:

> **1.6 credits/sec for 480p, 3 credits/sec for 720p**

I can verify whether those credits are legitimate and calculate the real dollar cost for that platform.

## User

ya kie ai

## Assistant

Yes, **for Kie AI specifically, that pricing appears to be correct**.

Kie AI currently advertises **Grok Imagine 1.5** at approximately:

- **480p:** **1.6 credits/second** (≈ **$0.008/sec**)
- **720p:** **3.0 credits/second** (≈ **$0.015/sec**) citeturn0search0

However, this is **Kie AI's own pricing**, **not xAI's official pricing**.

Here's the comparison:

| Provider | 480p | 720p |
|---------|------:|------:|
| **Kie AI** | ~$0.008/sec | ~$0.015/sec |
| **Official xAI API** | **$0.08/sec** | **$0.14/sec** | citeturn0search1

So Kie AI is charging roughly **10× less** than the official xAI API prices.

### How can they do that?

There are a few possibilities:

- They may have negotiated wholesale pricing.
- They may subsidize the model to attract developers.
- They could be absorbing some costs as a marketing strategy.
- They may impose other limits (queues, concurrency, rate limits, fair-use policies) that offset the lower price.

It's not unusual for API aggregators to have pricing that differs significantly from the original provider.

### Is Kie AI trustworthy?

From what you've shared in previous conversations, you've already used Kie AI successfully for video generation. It is a legitimate API gateway, but because they're reselling access, I'd keep an eye on:
- API uptime,
- generation speed,
- rate limits,
- and whether pricing changes over time.

For many developers, it's a much cheaper way to experiment than paying xAI's official API rates.

If you're planning to build your SaaS around Grok Imagine 1.5, Kie AI is currently one of the lowest-cost providers available, but I'd still recommend designing your backend so you can switch providers if their pricing or service changes.

## Resources

### External references
- [Grok Imagine Video 1.5 | SpaceXAI Docs](https://docs.x.ai/developers/models/grok-imagine-video-1.5?utm_source=chatgpt.com)
- [Grok Imagine Video 1.5 Pricing on ImagineArt and xAI](https://www.imagine.art/blogs/grok-imagine-video-1-5-pricing?utm_source=chatgpt.com)
- [Grok Imagine Video | SpaceXAI Docs](https://docs.x.ai/developers/models/grok-imagine-video?utm_source=chatgpt.com)
- [Grok Imagine Video | xAI Docs](https://docs.x.ai/developers/models/grok-imagine-video?cluster=eu-west-1&utm_source=chatgpt.com)
- [FAQ - Grok Website / Apps | SpaceXAI Docs](https://docs.x.ai/grok/faq?utm_source=chatgpt.com)
- [Grok Imagine Image | SpaceXAI Docs](https://docs.x.ai/developers/models/grok-imagine-image?utm_source=chatgpt.com)
- [Grok Imagine Video Cost in Credits: Official API Price vs Platform Credit Math | YingTu](https://yingtu.ai/en/blog/grok-imagine-video-cost-credits?utm_source=chatgpt.com)
- [Grok Imagine Video 1.5 (Preview) Pricing | Segmind](https://www.segmind.com/models/grok-imagine-video-1.5-preview/pricing?utm_source=chatgpt.com)
- [Grok Imagine 1.5: #1 on the Image-to-Video AI Leaderboard | ngram.com](https://www.ngram.com/blog/grok-imagine-1-5-ai-video-leaderboard?utm_source=chatgpt.com)
- [Grok Video API | Tikdek](https://tikdek.com/grok-video-api?utm_source=chatgpt.com)
- [Image-to-Video V2 / Text-to-Video / Omni Reference API Usage](https://docs.topview.ai/reference/image-to-video-v2-text-to-video-omni-reference-api-usage?utm_source=chatgpt.com)
- [Grok Imagine Video 1.5 AI Video Generator | Try Image-to-Video](https://grokimaginevideo.app/?utm_source=chatgpt.com)
- [Free Grok Imagine API on Kie.ai – Try Grok Imagine 1.5 Online](https://kie.ai/grok-imagine?utm_source=chatgpt.com)
- [Kostenlose Grok Imagine API auf Kie.ai – Grok Imagine 1.5 online testen](https://kie.ai/de/grok-imagine?utm_source=chatgpt.com)
- [Pricing | Grok Imagine - AI Video Generator | Spicy Mode | Free Credits](https://grokimagine.app/pricing?utm_source=chatgpt.com)
- [Grok Imagine 1.5 AI Pricing | Grok Imagine 1.5 AI — AI Video Generator](https://grokimagine15.ai/pricing?utm_source=chatgpt.com)
- [Grok Imagine Video 1.5 by xAI on Vercel AI Gateway, Specs, Pricing & API](https://vercel.com/ai-gateway/models/grok-imagine-video-1.5?utm_source=chatgpt.com)
- [Pricing | Grok Imagine - AI Video Generator | Spicy Mode | Free Credits](https://imagineai.studio/pricing?utm_source=chatgpt.com)
