---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6984d96a-4414-8323-8479-7040d6975a7b"
created: 1770314108.172594
updated: 1770314126.518384
resource_section: true
---

# Resolve Issue Button Action

## User

what happens when i click reslove issue

## Assistant

When you click **“Resolve conversation”** on GitHub, the following happens:

1. **The comment thread is marked as resolved** 
 GitHub visually collapses the discussion and labels it as *resolved*. This signals to reviewers and collaborators that the feedback has been acknowledged and addressed.

2. **No code is changed automatically** 
 Clicking *Resolve conversation* does **not** modify your code, apply suggestions, or fix the issue by itself. It is purely a review-state action, not a code action.

3. **The comment remains in history** 
 The discussion is not deleted. It stays in the pull request history and can be reopened later if needed.

4. **Review status improves** 
 If all review comments are resolved, the pull request appears “cleaner” and closer to being merge-ready. Many teams require all conversations to be resolved before merging.

5. **You are asserting responsibility** 
 By resolving it, you are effectively saying one of the following:
 - The issue has been fixed in the code 
 - The concern has been addressed in another way 
 - You have reviewed the suggestion and decided not to act on it (and accept the risk)

---

### In the context of your screenshot
The bot flagged a **minor issue** about missing input validation. 
If you click **Resolve conversation without adding validation**, GitHub will still allow it, but you are implicitly accepting the feedback without implementing it.

**Best practice (as expected in professional code reviews):**
- First, implement the suggested validation (or justify why it’s unnecessary in a reply).
- Then click **Resolve conversation**.

This demonstrates accountability, technical rigor, and review discipline—qualities expected in industry-grade pull requests.

## Resources

### Local attachments
- [50da5d10-493d-4ff0-942f-f87037dad7bb.png](../../../Raw/Export/file_000000008f2471fa826ff4b99f9f9596.dat)
