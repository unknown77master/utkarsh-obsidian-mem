---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6aaa276e-7d8c-83e8-81d6-23bc5a8a2e40"
created: 1789536112.293447
updated: 1789536136.31983
resource_section: true
---

# Move Docker To D Drive

## User

How to transfer docker desktop from c to d drive

## Assistant

Worked for a couple of seconds

## Assistant

On Windows 11, the best approach is to keep the small Docker Desktop application on `C:` and move the large Docker data—images, containers, volumes, build cache—to `D:`.

### Move Docker's storage to D:

1. Open **Docker Desktop**.
2. Go to **Settings → Resources → Advanced**.
3. Find **Disk image location**.
4. Click **Browse** and choose something like:

```text
D:\DockerData
```

5. Click **Apply & Restart**.

Docker Desktop should migrate its WSL2 virtual disk to the new location automatically.

You can verify afterward in:

```text
D:\DockerData
```

The large Docker virtual disk/VHDX should now live there instead of under your `C:\Users\<username>\AppData\Local\Docker\...` directory.

### If you mean Docker Desktop itself

The application binaries usually consume relatively little space. The storage problem is normally Docker's images/containers/volumes. For example, a Docker installation might look roughly like:

```text
C:\Program Files\Docker\ → ~1–3 GB
D:\DockerData\ → 20 / 50 / 100+ GB
```

So I recommend moving **Docker data only**.

Since you already have your **WSL Ubuntu on `D:\WSL\Ubuntu`**, putting Docker's data on something like `D:\DockerData` is also a clean setup. memcite

If **Disk image location isn't shown in your Docker Desktop**, tell me your Docker Desktop version or send a screenshot of **Settings → Resources**, and I'll give you the WSL/VHDX migration method instead.

## Resources

No structured attachments or external references were present in this conversation.
