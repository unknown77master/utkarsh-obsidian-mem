---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "698da564-92fc-8320-b25d-5769eddef59f"
created: 1770890624.295653
updated: 1770890645.896612
resource_section: true
---

# Open Developer Console n8n

## User

how to open developer consloe in n8n

## Assistant

To open the **Developer Console** while using **n8n in the browser (Docker setup)**, follow these steps:

### Method 1: Keyboard Shortcut (Fastest Way)

If you are using:

- **Windows / Linux (Chrome, Edge, Brave)** → Press 
 `Ctrl + Shift + I` 
 or 
 `F12`

- **Mac (Chrome, Edge, Brave)** → Press 
 `Cmd + Option + I`

---

### Method 2: Using Right Click

1. Open your n8n web interface.
2. Right-click anywhere on the page.
3. Click **Inspect**.
4. Go to the **Console** tab.

---

### Why You Need It in n8n

In your screenshot, n8n shows:

> “You can view the raw requests this node makes in your browser's developer console.”

When you:
- Click **Execute Step**
- Open the **Console tab**
- You will see the exact HTTP request body being sent

This helps you debug errors like:
> `JSON parameter needs to be valid JSON`

---

### Extra (Important for Your Case)

Since you are using:
```
{{ $json }}
```

If the console shows something malformed, the issue is usually:
- The previous node is returning a string instead of an object
- Or the JSON contains invalid escape characters

After opening the console, execute the node and check:
- `Request Payload`
- `Response`
- Any red errors

If you want, send me a screenshot of the console tab after executing, and I will guide you step-by-step to fix it.

## Resources

### Local attachments
- [3a7d3364-1e04-45ed-b66c-326131b8e0ba.png](../../../Raw/Export/file_000000009edc7206b202c67b0f1329dd.dat)
