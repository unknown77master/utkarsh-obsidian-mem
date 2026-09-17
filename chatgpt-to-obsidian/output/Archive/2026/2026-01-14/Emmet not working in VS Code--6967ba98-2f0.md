---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6967ba98-2f04-8322-9e3a-70378459db46"
created: 1768405678.994343
updated: 1768405690.38961
resource_section: true
---

# Emmet not working in VS Code

## User

div.input-container is not working in vs code when pressed enter\

## Assistant

**Answer (written in student style):**

When I type `div.input-container` in VS Code and press **Enter**, it does not work because **Emmet abbreviation expansion is not triggered**. This happens mainly due to settings, file type, or incorrect usage.

**Correct method:**

1. Make sure the file is saved as **.html**. 
2. Type:
 ```
 div.input-container
 ```
3. Press **Tab** (not Enter).

Then it will expand to:

```html
<div class="input-container"></div>
```

**If it still does not work, check the following:**

1. Open **Settings** → search **Emmet**. 
2. Enable: **Emmet: Trigger Expansion On Tab**. 
3. Ensure language mode is **HTML** (bottom right of VS Code).

**Reason:**

Enter is used to move to the next line, while Emmet uses **Tab** to expand abbreviations.

**Conclusion:**

Therefore, `div.input-container` works only when Emmet is enabled and the **Tab key** is used in an HTML file.

## Resources

No structured attachments or external references were present in this conversation.
