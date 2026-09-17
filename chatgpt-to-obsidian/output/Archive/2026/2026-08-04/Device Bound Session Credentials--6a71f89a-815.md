---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a71f89a-815c-83e8-900d-6f2070d07a95"
created: 1785854125.866325
updated: 1785854277.439373
resource_section: true
---

# Device Bound Session Credentials

## User

Device Bound Session Credentials with software keys
Enables mock software-backed cryptographic keys for Google session credentials binding and Chrome refresh tokens binding (not secure). This is intended to be used for manual testing only. – Mac, Windows, Linux

#enable-bound-session-credentials-software-keys-for-manual-testing

Default
Device Bound Session Credentials (Standard)
Enables the official version of Device Bound Session Credentials. For more information see https://github.com/WICG/dbsc. – Mac, Windows, Linux

#enable-standard-device-bound-session-credentials

Default
Device Bound Session Credentials (Standard) - Federated Registrations
Enables federated session registration for the official version of Device Bound Session Credentials. – Mac, Windows, Linux

#enable-standard-device-bound-session-credentials-federated-sessions

Default
Device Bound Session Credentials (Standard) on Google
Enables Device Bound Session Credentials (Standard) to register sessions on Google sites – Mac, Windows, Linux

#enable-standard-device-bound-session-google

which one shoul i enable foe my windows pc

## Assistant

For a **normal Windows PC**, you generally **don't need to enable any of these flags**. Chrome enables stable security features automatically when they're ready.

Here's what each flag is for:

1. **Device Bound Session Credentials with software keys (Manual Testing)**
 - **Do not enable.**
 - This uses **software-backed mock keys** and is meant only for developers testing the feature.
 - It is **less secure** than the real implementation.

2. **Device Bound Session Credentials (Standard)** ✅
 - This is the **official implementation** of the feature.
 - It helps bind website sessions (such as login cookies) to your device, making stolen cookies much harder to reuse on another computer.
 - **If you want to try the feature early, this is the one to enable.**

3. **Device Bound Session Credentials (Standard) – Federated Registrations**
 - Used for federated login systems (e.g., Sign in with Google, Microsoft, etc.).
 - Intended mainly for compatibility testing.
 - **Leave at Default** unless you're specifically testing identity federation.

4. **Device Bound Session Credentials (Standard) on Google**
 - Applies the feature specifically to Google services.
 - **Leave at Default** unless you're testing Google's rollout.

### My recommendation

For everyday use on Windows:

- ✅ **Device Bound Session Credentials (Standard)** → Enable (optional)
- ❌ **Software keys for manual testing** → Do **not** enable
- ➖ **Federated Registrations** → Leave at Default
- ➖ **On Google** → Leave at Default

### Is it worth enabling?

If you're just browsing the web:
- There is **little noticeable benefit today**, because support is still being rolled out by websites.
- Enabling it won't make Chrome significantly faster or more secure immediately.
- If you prefer maximum stability, simply **leave everything at Default** and let Chrome enable the feature automatically when it's fully supported.

So unless you're interested in experimenting with new security features, **keeping all four flags at Default is the best choice**.

## Resources

No structured attachments or external references were present in this conversation.
