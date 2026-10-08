# Local memory dashboard

Requires Git, Python 3.10+, and working Git credentials for the private repository `unknown77master/utkarsh-obsidian-mem`. No packages, server account, or database are needed. The user explicitly approved automatic vault uploads to this remote.

Open the dashboard at **http://127.0.0.1:8765**. It shows pending files, local/remote commit counts, last successful check, errors, and recent activity. Pause/resume and check/sync controls are available. Closing the browser leaves the service running.

## Start

From this repository:

```powershell
# Preview without committing, pulling, or pushing:
python .\vault-sync.py --read-only

# Full two-way sync (stop preview with Ctrl+C or dashboard Stop service first):
python .\vault-sync.py

# Install hidden background startup at Windows login and start now:
powershell -NoProfile -ExecutionPolicy Bypass -File .\install-vault-sync.ps1

# Remove startup and stop its scheduled instance:
powershell -NoProfile -ExecutionPolicy Bypass -File .\install-vault-sync.ps1 -Remove
```

Before enabling full sync, review, commit, and push these service/setup files manually. The service deliberately refuses non-vault pending changes or outgoing commits. This session cannot execute Git commits, so setup changes may still be uncommitted. Cloud agents will receive the new AGENTS.md rules only after setup is pushed.

If a preview is already open, use **Stop service** in the dashboard before installing startup. The installer does not terminate a separately launched service.

The default interval is 120 seconds. `--interval 300` changes it; `--port 8766` changes the dashboard port. `--once` runs one cycle. Windows Task Scheduler starts it at login, runs on battery, and retries process failures. It works while the computer is awake and the account is logged in; it cannot sync while powered off. Only one service instance per checkout is allowed.

## Behavior

Every cycle fetches the configured upstream. Full sync runs on `main` only, for the exact approved fetch and push URL. It commits settled additions/modifications only inside `chatgpt-to-obsidian/utkarsh-vault/`, pulls remote updates with rebase, and pushes without force. The commit subject uses current IST time and changed note names, for example `06-oct-2026:2-58:AM (updated coding projects and preferences)`.

Staged work, unrelated changes, deleted notes, protected exports, and active Git operations block automatic sync. Changes must remain stable for three seconds before committing. Agents should pause the service while editing and doing Git operations, then resume when updates have been validated: the service cannot judge the semantic accuracy of a note. Cloud agents follow AGENTS.md and push completed edits; no local process can fetch unpushed cloud edits.

Conflicting rebase is aborted, leaving local commits intact. Pause the dashboard and wait until the active cycle has finished; resolve the conflict manually with Git, then resume. A rejected push or network outage retains local commits and retries on the next cycle. Git credentials are never displayed or collected by the dashboard; authenticate with your usual Git credential manager.

The dashboard binds only to loopback and requires a per-session token for controls. Do not expose it through a tunnel. Activity is logged in ignored `.vault-sync/activity.log`, rotated at 1 MB. The existing `sync-vault.ps1` is a separate manual pull helper; do not run it alongside an active service.
