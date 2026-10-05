---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6ab0efec-b3f4-83e9-9508-2c76235cde45"
created: 1789980671.46877
updated: 1789980936.636488
resource_section: true
---

# Find All Sources

## User

I want to try it, give me all sources

## Assistant

I’ll verify what “Jev” actually is, then collect the official model/API, Andy Gao’s demo and code (if public), plus any setup guides needed to reproduce the voice-controlled Mac assistant. I’m using the Firecrawl search skill because these sources and launch details are live and recent.

## Assistant

The post is broadly accurate, with one important correction: Jev does not itself listen to audio, open apps, see the screen, or type. It receives text and returns a fast typed decision; speech-to-text and macOS automation do the actual work. I’m checking the public reproductions now so I can tell you which repo is closest to the demo and which sources are merely aggregators.

## Assistant

Worked for 1m 8s

## Assistant

The viral demo is real, but Andy Gao has not published its exact source code. The closest open-source recreation is currently macOS-only; since you use Windows 11, **Otto** is the project you should try first.

## Best option for your Windows PC

### 1. Otto — Windows + macOS

\[GitHub: NobleSpartan6/otto\](https://github.com/NobleSpartan6/otto)

It combines:

- TypeSafe Jev for rapid action selection
- Local OCR for observing the screen
- Native Windows/macOS automation
- Optional OpenAI-powered planning for complex tasks

Requirements:

- Windows 10/11
- Node.js 24+
- PowerShell 5.1+
- TypeSafe API key
- Optional OpenAI API key for hybrid mode

```powershell
git clone https://github.com/NobleSpartan6/otto.git
cd otto
npm install
npm run dev
```

Windows support is still experimental: it cannot control elevated applications or UAC dialogs, and publisher signing is not configured.

## Exact Mac-like voice implementation

### 2. Jev Voice

\[GitHub: kevinbadi/jev-voice\](https://github.com/kevinbadi/jev-voice)

This is the closest reproducible project to the video:

```text
Microphone
→ local VAD
→ local whisper.cpp transcription
→ Jev action selection
→ macOS automation
```

Capabilities include opening apps, typing, searching, scrolling, keyboard shortcuts, controlling media and executing compound commands.

It requires an Apple Silicon Mac. The repository reports approximately:

- Whisper transcription: 80–130 ms
- Jev decision: 170–420 ms
- Action execution: 50–100 ms

The repository is extremely new—it was created from a single initial commit on September 18—so inspect the automation code before granting Accessibility and Input Monitoring permissions.

### 3. Computer-use experiment

\[GitHub: awlevin/typesafe-computer-use\](https://github.com/awlevin/typesafe-computer-use)

A different macOS implementation that:

1. Captures the screen.
2. Extracts targets using OCR.
3. Gives Jev a bounded list of possible actions.
4. Executes the selected click/action.

Useful if you want actual screen-based computer use rather than only predefined voice commands.

## Original demo and claim

- \[Andy Gao’s original X post\](https://x.com/instantricecook/status/2100814590300889426)
- \[Archived demo page with source attribution\](https://systemonemodels.org/examples/discussions/voice-controlled-mac-computer-use/)
- \[Community archive of the post\](https://hermes-ai.net/jev/case/2100814590300889426/)

The original post says an application can open before he finishes speaking. That does **not** mean Jev directly processes streaming audio. A surrounding application must transcribe partial speech, send the text to Jev, and execute the returned decision.

## Official TypeSafe/Jev sources

- \[TypeSafe AI homepage\](https://typesafe.ai/)
- \[Create/manage API access\](https://console.typesafe.ai/)
- \[Jev introduction\](https://docs.typesafe.ai/introduction)
- \[Official quick start\](https://docs.typesafe.ai/introduction/quickstart)
- \[System One explanation\](https://docs.typesafe.ai/concepts/system-one)
- \[HTTP API reference\](https://docs.typesafe.ai/api)
- \[Python and JavaScript SDKs\](https://docs.typesafe.ai/sdk)
- \[Models, pricing and limits\](https://docs.typesafe.ai/models)
- \[How to build with System One\](https://docs.typesafe.ai/concepts/how-to-build-with-system-one)
- \[Confidence handling\](https://docs.typesafe.ai/confidence)
- \[Choice output\](https://docs.typesafe.ai/primitives/choice)
- \[Score output\](https://docs.typesafe.ai/primitives/score)
- \[Noul/yes-no output\](https://docs.typesafe.ai/primitives/noul)
- \[TypeSafe’s official agent skill\](https://github.com/typesafe-ai/skills)

The current official model is `jev-1.13.0`, while `jev-latest` points to it. It costs **$0.042 per million input tokens**, with output tokens free. Jev accepts only text—not audio, images or video.

## Additional useful implementations

- \[Voice-controlled browser\](https://github.com/moritzkremb/jev-voice-browser)
- \[Jev browser automation\](https://github.com/jkudish/jev-browser)
- \[macOS computer-use implementation\](https://github.com/paulsmith/computer-use-jev)
- \[Cua Driver + Jev guide\](https://cua.ai/docs/how-to-guides/driver/jev-use)
- \[Community project collection\](https://madewithjev.com/)
- \[Awesome Jev collection\](https://github.com/cobanov/awesome-jev)
- \[Pydantic AI integration\](https://ai.pydantic.dev/models/typesafe/)

My recommendation for you: first test the raw Jev API using its quick start, then run **Otto** on Windows. Don’t start with `jev-voice` unless you have access to an Apple Silicon Mac.

## User

https://github.com/awlevin/typesafe-computer-use and this
Even if this is for macOS don't u think I can make it for windows too, with my experience in making apps for windows, he'll I can even contribute to it, open a PR

## Assistant

Worked for 6s

## Assistant

Yes—you can absolutely port `typesafe-computer-use` to Windows and submit a PR. The clean approach is to preserve its Jev decision loop and replace the macOS-specific observation/action layer with a Windows adapter.

A sensible architecture would be:

```text
Voice/text command
 ↓
Screen capture + OCR
 ↓
Jev selects a bounded action
 ↓
Platform interface
 ├── macOS adapter
 └── Windows adapter
```

For Windows, likely replacements are:

| macOS capability | Windows implementation |
|---|---|
| Screenshot APIs | `mss`, `Pillow`, or Windows Graphics Capture |
| OCR | Existing project OCR, Windows OCR, or PaddleOCR |
| Mouse/keyboard | `pyautogui`, `pynput`, or Win32 `SendInput` |
| Window discovery | `pywin32` / Windows UI Automation |
| App launching | `subprocess`, Start Menu resolution |
| UI elements | `pywinauto` or Microsoft UI Automation |
| Permissions | Normal desktop access; elevated/UAC windows require special handling |

Your first PR should stay small:

1. Extract the existing macOS operations behind a `ComputerController` protocol/interface.
2. Move current behavior into `MacOSController`.
3. Add `WindowsController` for screenshots, clicks and keyboard input.
4. Select the implementation using `sys.platform`.
5. Add mocked platform tests.
6. Document Windows installation and limitations.

Avoid immediately adding voice control, application discovery and every Windows action. A focused PR supporting the existing workflow—capture → OCR → Jev decision → click—is much easier for the maintainer to review and merge.

A good contribution proposal:

> Hi! I’m interested in adding Windows support while preserving the existing Jev decision loop. My initial plan is to extract the macOS-specific screen capture and input operations behind a small platform interface, retain the current implementation as the macOS adapter, and add a Windows adapter supporting screenshots, mouse clicks, and keyboard input. I’ll include platform-specific tests and document known limitations such as UAC/elevated windows. Would you be open to this approach before I begin the PR?

One caveat: Windows automation libraries generally cannot interact with elevated applications when your process is non-elevated, and automation of the secure UAC desktop should remain out of scope. Otherwise, the port is completely practical—and aligns well with your existing Windows desktop/Electron/Python experience from Audora.

## Resources

### Local attachments
- [1000099477.jpg](../../../Raw/Export/file_00000000e1788211900aba1dd8cabfb1.dat)
