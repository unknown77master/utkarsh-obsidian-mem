---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6967a2da-2428-8321-8b44-0b490f528633"
created: 1768399579.707355
updated: 1768399730.235897
resource_section: true
---

# Reset cursor in VSCode

## User

how to reset cursor in vscode

## Assistant

**Answer (student-style, concise and exam-appropriate):**

In Visual Studio Code, the cursor can be reset to a normal single cursor using the following methods:

1. **Press `Esc`** 
 This removes all multiple cursors and returns to one cursor.

2. **Click once anywhere in the editor** 
 A single mouse click resets the cursor to that position.

3. **Undo multiple cursors shortcut** 
 If created by keyboard, press `Esc` or use `Ctrl + U` to undo the last cursor.

4. **Reload VS Code window (if stuck)** 
 Press `Ctrl + Shift + P` → type **Reload Window** → press Enter.

**Conclusion:** 
The standard and fastest way to reset the cursor in VS Code is by pressing **Esc**.

If you want, I can also explain how multiple cursors are created and managed.

## User

no my cursor is not creating space when i am writing between brackets, it is erasing them and overwriting on <> brackets

## Assistant

**Answer (student-style, clear and practical):**

Your VS Code cursor is in **Overwrite Mode**, not in normal Insert Mode. 
In this mode, typing replaces existing characters instead of creating space — so it overwrites `< >`, `( )`, etc.

### How to fix it

1. **Press the `Insert (Ins)` key once on your keyboard.** 
 This switches back to **Insert Mode**.

2. Check the bottom-right of VS Code:
 - If it shows **OVR** → Overwrite mode (problem).
 - If it shows **INS** → Insert mode (correct).

### If you don’t have an Insert key (laptop users)

Go to:
- `File → Preferences → Settings`
- Search: **overwrite**
- Disable: **Editor: Overwrite Mode**

### Conclusion

The issue is not with brackets — it is due to **Overwrite Mode being enabled**. 
Pressing **Insert** will permanently solve the problem.

If you want, I can also explain how VS Code auto-pairs brackets and how to configure it properly.

## User

done

## Assistant

Good. 
Your editor is now back in **Insert Mode**, so typing will no longer overwrite brackets.

If you face any further VS Code, programming, or academic issues, you may ask freely. I will guide you properly.

## Resources

No structured attachments or external references were present in this conversation.
