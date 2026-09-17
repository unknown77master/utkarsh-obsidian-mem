---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a9b351a-f734-83e8-a01e-0fc1a52a6fbb"
created: 1788556592.629227
updated: 1788556709.825954
resource_section: true
---

# Install Firecrawl CLI

## User

The Firecrawl CLI is not installed in this environment, how do i install it

## Assistant

Worked for a couple of seconds

## Assistant

If you mean the **Firecrawl CLI for your Windows/PowerShell setup**, install it globally with npm:

```powershell
npm install -g firecrawl-cli
```

Then verify:

```powershell
firecrawl --version
```

If PowerShell says `firecrawl` is not recognized, check where npm global binaries are installed:

```powershell
npm prefix -g
```

On Windows, it is commonly something like:

```text
C:\Users\ASUS\AppData\Roaming\npm
```

Make sure that directory is in your `PATH`, then restart PowerShell.

You can also try it without a global install:

```powershell
npx firecrawl-cli --help
```

Since you're using Node/npm already, npm is the simplest route for your environment.

## Resources

No structured attachments or external references were present in this conversation.
