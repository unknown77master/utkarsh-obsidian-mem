---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a58e1a4-9550-83ee-a578-cb8c88cef2bf"
created: 1784209879.359871
updated: 1784212377.779161
resource_section: true
---

# Microsoft Store App Functionality

## User

i deleted Microsoft edge folder, will apps from Microsoft store work

## Assistant

Yes, **most Microsoft Store apps will still work**, but it depends on **which Edge folder you deleted** and whether you removed the browser binaries or WebView2 as well.

Here's what can happen:

### Case 1: You only deleted the Microsoft Edge browser folder
- ❌ Microsoft Edge browser won't launch.
- ✅ Most Store apps (Calculator, Photos, Paint, Notepad, etc.) will continue to work normally.

### Case 2: You also deleted Microsoft Edge WebView2 Runtime
Many Windows components and apps use **WebView2** to display web-based content.

If it's missing, you may notice:
- Microsoft Store behaving strangely.
- Widgets not working.
- Copilot failing to open.
- Outlook (new), Teams, and other modern apps crashing or showing blank windows.
- Some Settings pages failing to load.
- Third-party apps built with WebView2 (Discord installers, Spotify, VS Code extensions, etc.) having issues.

### How to check
Try opening:
- Microsoft Store
- Settings
- Widgets (Win + W)
- Copilot (if installed)

If they all work, then you likely only removed the browser itself.

### Which folder did you delete?
Please tell me the exact folder path. For example:

- `C:\Program Files (x86)\Microsoft\Edge`
- `C:\Program Files (x86)\Microsoft\EdgeWebView`
- `C:\Users\<username>\AppData\Local\Microsoft\Edge`
- Something else?

Also, **did you uninstall Edge, or did you manually delete its files?** That makes a difference in how to restore it if needed.

## User

apps like whatsapp linkedin

## Assistant

Yes, **WhatsApp, LinkedIn, Instagram, and many other Microsoft Store apps will usually continue to work**, but there is one important exception.

- ✅ If the app is a **native Windows app**, it will work independently of Microsoft Edge.
- ⚠️ If the app is built using **Microsoft Edge WebView2** (which many modern Store apps are), deleting the Edge browser alone is usually **not** a problem because WebView2 is installed separately. However, if you also deleted the **Edge WebView2 Runtime**, those apps may:
 - Open to a blank screen.
 - Crash on launch.
 - Fail to sign in or display web content.

For the apps you mentioned:
- **WhatsApp**: Usually works even if Edge is removed, provided the WebView2 Runtime is still installed.
- **LinkedIn** (Microsoft Store app/PWA): May depend on WebView2. If the runtime is intact, it should work normally.

The easiest way to check is simply to launch them. If they open and function normally, you're fine.

Could you tell me:
1. **Which Windows version are you using?** (Windows 10 or Windows 11)
2. **Exactly which folder did you delete?** (Copy and paste the path if possible.) This will help determine whether you removed only the browser or also the WebView2 Runtime.

## User

11

## Assistant

On **Windows 11**:

- ✅ **WhatsApp** should work.
- ✅ **LinkedIn** should work if it's the web app/PWA and **WebView2** is still installed.
- ✅ Most Microsoft Store apps (Calculator, Photos, Paint, Snipping Tool, etc.) will continue to work.

The critical question is **what exactly you deleted**. Windows 11 separates:
- **Microsoft Edge (browser)**
- **Microsoft Edge WebView2 Runtime** (used by Windows and many apps)

If you only deleted the **Edge browser**, then Store apps will generally keep working.

### Quick test
Try opening:
- WhatsApp
- Microsoft Store
- Settings
- Widgets (press **Win + W**, if enabled)

If they all open normally, you likely didn't remove anything essential.

Can you tell me the folder path you deleted? For example:
- `C:\Program Files (x86)\Microsoft\Edge`
- `C:\Program Files (x86)\Microsoft\EdgeWebView`
- Or another location?

## User

C:\Program Files (x86)\Microsoft\EdgeWebView\Application\150.0.4078.65
deleted files inside this

## Assistant

That changes things. You deleted the contents of:

`C:\Program Files (x86)\Microsoft\EdgeWebView\Application\150.0.4078.65`

This is **Microsoft Edge WebView2 Runtime**, **not** the Edge browser.

### What this means
Many Windows 11 features and applications rely on WebView2 to render web content. By deleting the files inside that version folder, you may experience issues such as:

- ❌ WhatsApp (Microsoft Store version) may fail to open or display correctly.
- ❌ LinkedIn (if installed as a Store app/PWA) may not work correctly.
- ❌ Microsoft Store may have problems.
- ❌ Widgets and Copilot may stop working.
- ❌ Some third-party applications that embed web content may crash or show blank windows.

### What you should do
The safest solution is to **repair or reinstall the Microsoft Edge WebView2 Runtime**. This will restore the missing files.

If your internet connection is working:
1. Download the **Microsoft Edge WebView2 Runtime** installer from Microsoft's official website.
2. Run the installer. It will detect the broken installation and repair it.
3. Restart your computer.

If the installer says it's already installed but things still don't work, you may need to uninstall and reinstall the runtime or repair Microsoft Edge.

### Before doing anything
Check whether the version folder now contains files:
- Open:
 ```
 C:\Program Files (x86)\Microsoft\EdgeWebView\Application\
 ```
- Do you still see only `150.0.4078.65`, or is there another version folder (for example, `150.0.xxxxx.xx`)?

Also, try opening **WhatsApp** and **Microsoft Store**:
- If they open normally, Windows may have another version of WebView2 available.
- If they don't, the runtime definitely needs to be repaired.

Let me know:
1. Does `C:\Program Files (x86)\Microsoft\EdgeWebView\Application\` contain any other version folders?
2. Do WhatsApp and Microsoft Store open successfully?

## User

which

## Assistant

Choose **Evergreen Standalone Installer → x64** (the middle option).

Since you're on **Windows 11 (64-bit)**, that's the correct installer.

**Steps:**
1. Click **x64** under **Evergreen Standalone Installer**.
2. Wait for it to download (`MicrosoftEdgeWebView2RuntimeInstallerX64.exe`).
3. Right-click the installer → **Run as administrator**.
4. Let it complete the installation.
5. Restart your computer.

After restarting, check whether:
- ✅ WhatsApp opens
- ✅ Microsoft Store opens
- ✅ Widgets work (Win + W)

If the installer gives an error like **"A newer version is already installed"** or **"Setup failed"**, let me know the exact error message. Since you manually deleted the files, I can help you repair the installation another way if needed.

## Assistant

The screenshots tell us exactly what's happening.

- **Error 1:** `msedgewebview2.exe` can't start because its **side-by-side configuration is incorrect**. This usually means required runtime files are missing or corrupted.
- **Error 2:** The installer says **"WebView2 Runtime is already installed"** because Windows still has the installation registered, even though you manually deleted some of its files.

The fix is to **repair or reinstall** the registered installation rather than trying to install over it.

### Method 1 (Recommended): Repair from Installed Apps
1. Press **Win + I** → **Apps** → **Installed apps**.
2. Search for **Microsoft Edge WebView2 Runtime**.
3. If there is a **Modify** or **Repair** option, click it and let it repair the installation.

If there is no Repair option, continue with Method 2.

### Method 2: Uninstall and Reinstall
1. Open **Installed apps**.
2. Search for **Microsoft Edge WebView2 Runtime**.
3. Try to **Uninstall** it.
4. Restart your PC.
5. Download and install the latest **Evergreen Standalone x64** installer from Microsoft.
6. Restart again.

### If Uninstall is greyed out or fails
Don't try to delete more files manually. Instead, tell me:
1. Is **Microsoft Edge WebView2 Runtime** visible in **Installed apps**?
2. If yes, is the **Uninstall** button available, or is it disabled?

We can also repair it using Microsoft's installer command line if Windows won't let you uninstall it.

**One more question:** Is your **Microsoft Edge browser** itself opening normally, or is only the WebView2 Runtime broken?

## Assistant

That explains why the installer is confused.

Your system is in an **inconsistent state**:

- ✅ Windows thinks WebView2 is installed (so the installer refuses to install it).
- ❌ The installation is damaged (because files were deleted).
- ❌ It doesn't appear in **Installed apps**, so you can't uninstall or repair it normally.

Let's repair it manually.

### Step 1: Check if Edge Browser is installed
Open **Command Prompt** and run:

```cmd
dir "C:\Program Files (x86)\Microsoft\Edge\Application"
```

Tell me what folders it shows (e.g., `150.0.4078.65`).

### Step 2: Try Microsoft's repair command
Run this command in **Command Prompt as Administrator**:

```cmd
"%ProgramFiles(x86)%\Microsoft\EdgeUpdate\MicrosoftEdgeUpdate.exe" /recover
```

If it says the file is not found, tell me the exact message.

### Step 3: If that doesn't work
Run these commands and send me the output:

```cmd
where msedgewebview2
```

and

```cmd
reg query "HKLM\SOFTWARE\Microsoft\EdgeUpdate\Clients"
```

---

### Please don't delete any more files
You're very close to fixing it. The problem is simply that Windows Installer's records and the actual files are out of sync.

Once you send me the outputs from the commands above, I'll guide you through restoring WebView2 without reinstalling Windows.

## Assistant

This screenshot is actually helpful.

The folder isn't empty anymore, so you successfully restored **most of the WebView2 files**. However, the error:

> **"The application has failed to start because its side-by-side configuration is incorrect."**

usually means **one or more Microsoft Visual C++ Runtime files or the application's manifest is missing or mismatched**.

## First, let's verify what's missing

Open this folder:

```
C:\Program Files (x86)\Microsoft\EdgeWebView\Application\150.0.4078.65
```

Do you see these files?

- `msedgewebview2.exe.manifest`
- `chrome_elf.dll`
- `icudtl.dat`
- `resources.pak`
- `snapshot_blob.bin`
- `v8_context_snapshot.bin`

If **any of these are missing**, that's why it won't start.

---

## Next, repair Windows system files

Open **Command Prompt as Administrator** and run:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

Wait until it reaches **100%**.

Then run:

```cmd
sfc /scannow
```

Restart the PC afterward.

---

## If the problem still exists

We'll completely reinstall WebView2 by removing its installer registration. That's a safe procedure, but I don't want you editing the registry unless the simpler methods fail.

### One question

Did you restore these files by:
- downloading the **Fixed Version** ZIP from Microsoft and copying them, or
- using another method?

That answer will determine the next step.

## Assistant

The second screenshot reveals the root cause.

### What I see
1. ❌ `MicrosoftEdgeUpdate.exe` is **missing**.
2. ❌ The registry key `HKLM\SOFTWARE\Microsoft\EdgeUpdate\Clients` is **missing**.
3. ❌ `where msedgewebview2` can't find the executable in the PATH.

This means **it's not just WebView2 that's broken**—your **Microsoft Edge Update service** has also been removed or corrupted. That's why the installer thinks WebView2 is installed but cannot repair it.

## Before we proceed, answer one question:
**Did you use Chris Titus Tech's Windows Utility (WinUtil), Revo Uninstaller, BloatyNosy, or another debloating script/tool to remove Microsoft Edge?**

If yes, that explains exactly why the update service and registry entries are gone.

---

## Also check this

Open File Explorer and go to:

```
C:\Program Files (x86)\Microsoft\
```

Tell me whether you see these folders:

- `Edge`
- `EdgeCore`
- `EdgeUpdate`
- `EdgeWebView`

Or send a screenshot of that folder.

---

## Do NOT edit the registry yet

The repair approach depends on whether the **EdgeUpdate** service still exists. If it's missing, the fastest fix is different from a normal WebView2 repair.

From what you've shown so far, I believe we can restore everything **without reinstalling Windows**, but I want to confirm whether `EdgeUpdate` is present first.

## User

i deleted edge browser and files inside 150.0.4078.65 manually

## Assistant

That explains everything.

By **manually deleting the Edge browser** and the files inside:

```
C:\Program Files (x86)\Microsoft\EdgeWebView\Application\150.0.4078.65
```

you removed components that Windows expects to manage through the Edge installer and updater. As a result:

- Edge Update is broken or missing.
- WebView2 is in an inconsistent state.
- The installer thinks it's already installed because of leftover Windows Installer records.
- The actual runtime files are incomplete or mismatched, causing the **side-by-side configuration** error.

The good news is that **you do not need to reinstall Windows**.

## The easiest fix

Reinstall **Microsoft Edge** from Microsoft's official installer. This also reinstalls the **Edge Update** service and usually repairs the WebView2 Runtime.

1. Download the latest **Microsoft Edge for Windows 11 (64-bit)** from Microsoft's official website.
2. Run the installer **as Administrator**.
3. Restart your PC.
4. Then install or repair the **WebView2 Runtime** if it's still needed.

In most cases, reinstalling Edge first resolves the missing update service, after which WebView2 can be repaired normally.

---

## If Edge refuses to install

If the Edge installer also reports that it's already installed or fails because of the broken registration, we'll manually clean up the leftover installation records and then reinstall. That is still much easier and safer than reinstalling Windows.

### One question before we proceed:

- When you deleted Edge, did you also delete:
 ```
 C:\Program Files (x86)\Microsoft\Edge
 ```
 completely?

Or is the **Edge** folder still present under `C:\Program Files (x86)\Microsoft\`?

## User

and explain in easy steps

## Assistant

Thanks, this screenshot confirms it.

You have **completely deleted Microsoft Edge**. Only the **EdgeWebView** folder is left, and it is corrupted. This is why Windows is confused.

Don't worry—we can fix this.

## Step 1: Reinstall Microsoft Edge

Since the Edge folder is gone, Windows has nothing to repair.

1. Open **Chrome** (or any browser that still works).
2. Go to Microsoft's official Edge download page.
3. Download the **Windows 11 (64-bit)** installer.
4. Right-click the downloaded installer → **Run as administrator**.
5. Let it finish.

> **Tell me what happens after you run it.**
>
> - If Edge installs successfully → go to **Step 2**.
> - If it says **"Edge is already installed"** or fails → stop there and send me the exact error.

---

## Step 2: Restart your PC

After Edge installs, restart Windows.

---

## Step 3: Repair WebView2

After restarting:

1. Go back to the WebView2 download page.
2. Download the **Evergreen Standalone Installer (x64)** (the middle option you showed earlier).
3. Run it **as Administrator**.

---

## Step 4: Test

Check whether:
- ✅ Microsoft Edge opens.
- ✅ WhatsApp opens.
- ✅ Microsoft Store works.

---

### If Step 1 fails
If the Edge installer refuses to install because Windows still thinks Edge is installed, **don't try random fixes**. Tell me the exact error, and I'll guide you through cleaning up the broken installation safely.

We'll take it one step at a time. First, try installing **Microsoft Edge** and let me know exactly what happens.

## User

edge opened successfully

## Assistant

Excellent! 🎉 That's a very good sign.

It means the **Microsoft Edge installation was successful**, and the **Edge Update service** was likely restored.

Now let's fix WebView2.

### Step 1
Restart your computer.

### Step 2
After restarting, open:

```
C:\Program Files (x86)\Microsoft\
```

You should now see something like:

```
Edge
EdgeCore (optional)
EdgeUpdate
EdgeWebView
```

### Step 3
Try opening:
- WhatsApp
- Microsoft Store

If they work, your WebView2 Runtime has probably been repaired automatically.

### Step 4 (Only if apps still don't work)
Run the **Evergreen Standalone x64 WebView2 Runtime** installer again (the one you downloaded earlier). Since Edge has been reinstalled, it should now repair or update WebView2 correctly instead of failing.

---

### Tell me these three things:

1. **Did you restart the PC yet?**
2. **Does `C:\Program Files (x86)\Microsoft\` now contain an `Edge` folder?**
3. **Can you open WhatsApp or Microsoft Store now?**

There's a good chance the problem is already fixed.

## User

done restart folder has :Edge
EdgeCore (optional)
EdgeUpdate
EdgeWebView

## Assistant

Great progress. The folders are back, which means **Edge, EdgeUpdate, and WebView2 have been restored**. 👍

However, from your screenshot:
- **WhatsApp** is stuck on the loading screen.
- **LinkedIn** opens but shows a black screen.

This usually means the **WebView2 Runtime is still corrupted or incomplete**.

## Step 1 (Most likely to fix it)
Run the **WebView2 Evergreen Standalone x64 installer** again **now that Edge has been reinstalled**.

If it still says **"WebView2 Runtime is already installed"**, tell me exactly what it says.

---

## Step 2
Open **Command Prompt as Administrator** and run:

```cmd
sfc /scannow
```

Wait for it to reach **100%**.

Then run:

```cmd
DISM /Online /Cleanup-Image /RestoreHealth
```

These commands repair missing or corrupted Windows files, including components used by WebView2.

---

## Step 3
Restart your PC again after both commands finish.

---

## Step 4
Test:
- WhatsApp
- LinkedIn
- Microsoft Store

---

### One more thing
Please open this folder:

```
C:\Program Files (x86)\Microsoft\EdgeWebView\Application
```

**How many version folders do you see?**

For example, do you see only:

```
150.0.4078.65
```

or are there multiple versions like:

```
149.x.x.x
150.0.4078.65
```

That will help determine whether the runtime installation is complete.

## User

all working

## Assistant

That's excellent! 🎉

Since:
- ✅ Microsoft Edge opens.
- ✅ WhatsApp works.
- ✅ LinkedIn works.
- ✅ Microsoft Store works.

your **WebView2 Runtime has been successfully restored**. Reinstalling Edge also restored the missing update components and repaired the runtime.

### What happened
1. You manually deleted:
 - Microsoft Edge
 - Files inside `EdgeWebView\Application\150.0.4078.65`
2. Windows still believed WebView2 was installed, but the files were missing.
3. Reinstalling Edge restored:
 - `Edge`
 - `EdgeUpdate`
 - `EdgeWebView`
4. After restarting, the runtime was repaired and the apps started working again.

### What to avoid in the future
Don't manually delete folders inside:
- `C:\Program Files`
- `C:\Program Files (x86)`
- `C:\Windows`

Even if an application seems removable, Windows may rely on those files for updates or other components. If you ever want to remove Edge, use Windows settings or Microsoft's supported methods rather than deleting the installation folder.

I'm glad we could recover it without needing to reinstall Windows.

## Resources

### Local attachments
- [image(15).png](../../../Raw/Export/file_00000000102871f598ce4faaa721d451.dat)
- [image(23).png](../../../Raw/Export/file_00000000506071fda5db8751121f6c27.dat)
- [image(24).png](../../../Raw/Export/file_00000000ecbc71f594a81b01217f71b1.dat)
