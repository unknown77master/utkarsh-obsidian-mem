---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a756f0f-0ea4-83ee-8507-e875d2ee23d5"
created: 1786081238.504394
updated: 1788264366.154586
resource_section: true
---

# Reddit Post

## User

i want people to join agentrouter, write a post which reddit wont remove using all this information and now they provide opus-5 and gpt-5.6-sol also:
Look I have found a website which provides 175$ ~ 1M worth of claude-code Opus 4.8 tokens in the form of api key. I needed it so much for my content creation and it actually works! The catch is simple, you must have a GitHub account which is at least few months old. I don't know when this demo might get ended. I can't call this a demo also, because 1M tokens is huge. (Use the link below to get extra 50$)

To get the API key:

Go to this link- https://shorturl.at/mI0eH
\[dont sign up!\] sign in -> continue with GitHub

Then once you get successfully logged in, go to create token (under api token tab)> enter any name > scroll down and check unlimited. Then submit.

Now refresh the page, check under the wallet tab you'll see the current balance as $175.

The setup for claude code:

Step 1: Create an AgentRouter account

You need a GitHub account that is at least few months old.

After creating your API key.

Step 2: Install Claude Code

Windows PowerShell:

irm https://claude.ai/install.ps1 | iex

Windows CMD:

curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd

Linux and macOS:

curl -fsSL https://claude.ai/install.sh | bash

Step 3: Configure API Key and Base URL

Linux and macOS:

echo 'export ANTHROPIC_API_KEY="YOUR_API_KEY"' >> ~/.bashrc

echo 'export ANTHROPIC_BASE_URL="https://agentrouter.org"' >> ~/.bashrc

source ~/.bashrc

Windows PowerShell:

\[System.Environment\]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "YOUR_API_KEY", "User")

\[System.Environment\]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://agentrouter.org", "User")

After completing the setup, restart your terminal and run Claude Code.

Your Claude Code installation is now connected through AgentRouter.

## Assistant

Worked for a second

## Assistant

If your goal is to post this on Reddit without looking like a referral-spam post, the safest approach is to **avoid exaggerated claims, fake scarcity, and aggressive “join now” language**. Be transparent that it is a third-party API service and that the balance may be promotional.

Here’s a Reddit-style version:

:::writing{variant="social_post" id="58321"}
**I found a pretty useful API router for Claude Code — sharing in case anyone else needs it**

I’ve been using AgentRouter recently because I needed access to larger Claude Code usage for development/content work without managing multiple API providers separately.

They currently show **$175 of API credit** on new accounts, and the platform supports models including **Claude Opus 5** and **GPT-5.6-Sol**. The available balance and model access may depend on the account/promotion, so I wouldn’t assume the offer will stay around permanently.

One requirement I noticed is that you need to sign in with a **GitHub account that has some account history**.

**How I set it up:**

1. Go to AgentRouter: https://shorturl.at/mI0eH
2. **Don't create a separate email/password account** — use **Continue with GitHub**.
3. After signing in, open **API Token** → **Create Token**.
4. Give the token any name.
5. Scroll down and enable **Unlimited** if you want the token to work without manually setting a limit.
6. Create the token.
7. Refresh the page and check the **Wallet** section. My account showed **$175** in balance.

### Using it with Claude Code

Install Claude Code first.

**Windows PowerShell**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**Windows CMD**
```cmd
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

**Linux / macOS**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Then configure the AgentRouter API key and endpoint.

**Linux / macOS**
```bash
echo 'export ANTHROPIC_API_KEY="YOUR_API_KEY"' >> ~/.bashrc
echo 'export ANTHROPIC_BASE_URL="https://agentrouter.org"' >> ~/.bashrc
source ~/.bashrc
```

**Windows PowerShell**
```powershell
\[System.Environment\]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "YOUR_API_KEY", "User")

\[System.Environment\]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://agentrouter.org", "User")
```

Restart your terminal after setting the variables and launch Claude Code.

**A couple of caveats:** this is a third-party API router, not Anthropic/OpenAI directly. I also don't know how long the $175 promotional credit will remain available, so treat the balance as a current offer rather than something guaranteed.

If anyone else has tried AgentRouter, I'd be interested in hearing how the latency and model reliability compare with using the providers directly.
:::

**Important for Reddit:** don't repeatedly repost this across multiple subreddits, don't use multiple accounts to promote it, and don't claim the $175 is guaranteed or “free $175” unless the service explicitly states that. Those are the kinds of things that can make an otherwise legitimate post look like referral spam.

## User

suggest me on which subreddit should i post and most of the people will join

## Assistant

If your main goal is **maximum legitimate reach**, I’d prioritize communities where people already discuss Claude Code, AI coding tools, and API providers.

### Best targets

1. **r/ClaudeAI** — probably the strongest audience match. 
 People there are already interested in Claude Code and Claude models.

2. **r/ClaudeCode** — highly targeted if promotional/referral posts are permitted by the current rules.

3. **r/LocalLLaMA** — large AI developer audience, but your post needs to be framed as a technical/API-routing discovery rather than “join this service.”

4. **r/ChatGPT** — potentially huge reach, but your post is less directly relevant and promotional content may be restricted.

5. **r/ArtificialIntelligence** — broad audience, but again, check the rules because referral-style posts are often removed.

6. **r/SideProject** — useful if you present AgentRouter as a tool/service you discovered and explain the technical use case rather than simply advertising it.

### For your specific post

I'd start with **r/ClaudeAI** and **r/ClaudeCode**, but **check each subreddit's current rules before posting**. Don't copy-paste the exact same promotional post into many communities; that can look like spam and get your account/posts filtered.

Also, because you're using a shortened referral link, I'd strongly recommend being transparent that **the link is a referral/affiliate link if you receive any benefit from signups**. That will make the post much safer from a trust perspective.

If you want, I can also **rewrite the post specifically for r/ClaudeAI** in a way that sounds like a genuine technical discovery rather than an advertisement.

## User

Rewrite the post specifically for r/ClaudeAI

## Assistant

For **r/ClaudeAI**, I’d make it much less promotional and more like a personal discovery. Avoid “everyone join,” “$175 free,” or urgency language, since those can make it look like referral spam.

:::writing{variant="social_post" id="74126"}
**Found a third-party API router that currently gives $175 in API credit — works with Claude Code**

I was looking for a way to use Claude Code without constantly worrying about API usage limits, and I came across **AgentRouter**.

After signing in with GitHub, my account showed **$175 in API credit** in the Wallet section. They currently list models including **Claude Opus 5** and **GPT-5.6-Sol**.

The interesting part is that it can be used as an Anthropic-compatible endpoint, so Claude Code can be configured to route requests through it.

**Setup I used:**

1. Create an AgentRouter account using GitHub:
 https://shorturl.at/mI0eH

2. Go to **API Token → Create Token**.

3. Give the token a name and create it. There is also an **Unlimited** option when creating the token.

4. Refresh the dashboard and check **Wallet** to see the available credit.

5. Install Claude Code if you haven't already.

**Windows PowerShell:**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**Then set the environment variables:**

```powershell
\[System.Environment\]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "YOUR_API_KEY", "User")

\[System.Environment\]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://agentrouter.org", "User")
```

Restart the terminal and launch Claude Code.

For Linux/macOS:

```bash
export ANTHROPIC_API_KEY="YOUR_API_KEY"
export ANTHROPIC_BASE_URL="https://agentrouter.org"
```

One important note: **AgentRouter is a third-party service, not Anthropic**, so I'd recommend avoiding sensitive/private code until you're comfortable with how the service handles requests. I also don't know how long the current $175 promotional balance will be available.

I'm sharing this because the setup worked for me and I thought it might be useful to other Claude Code users.

Has anyone here used AgentRouter for a longer period? I'm particularly interested in **latency, reliability, and whether the model routing behaves similarly to using Anthropic directly**.
:::

This version is more likely to fit the **r/ClaudeAI** audience because it leads with the actual Claude Code use case and includes a caveat about the third-party service rather than reading like an advertisement.

## Resources

No structured attachments or external references were present in this conversation.
