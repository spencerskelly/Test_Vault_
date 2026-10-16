> [!NOTE] ARCHIVED 2026-10-03 (W-326). Moved to `99_System/archive/10_Docs retired/`; no current file depends on it. See [[00 - Current State]].

> [!WARNING]
> **SUPERSEDED PROCEDURE (W-261, W-320).** The ZIP steps below predate the base-vault path. A new vault now starts from the matched clean 0.8.0 base (not yet built; see [[00 - Current State]]) and is initialized with `99_System/09_Tools/Initialize-Vault.sh` or `Initialize-Vault.ps1`. Only the Git safety defaults and the tracked/untracked lists below remain valid.

# Git and New Vault Setup

## Purpose

Status (W-261): the ZIP procedure below predates the base vault path (W-249) and is not current. A script that builds the base vault will replace it; it is not written yet. The Git safety defaults and the tracked and untracked lists below still apply.

## Prerequisites

- Obsidian
- Git
- GitHub Desktop (current visible workflow)
- access to the target GitHub account/organization

## Procedure

1. Unzip into a new local folder.
2. Initialize vault identity.
3. Open the folder in Obsidian.
4. Confirm `.vault.yaml` no longer says `UNINITIALIZED`.
5. In GitHub Desktop, create/add the repository using this folder as the local repository.
6. Publish the repository to GitHub.
7. Confirm `main` is the default branch.
8. In Obsidian, verify Source Control / Obsidian Git sees a clean repository.
9. Commit and push any intentional initialization changes.

## Git safety defaults

```bash
git config pull.ff only
```

Do not solve divergence with force-push, `reset --hard`, or blind merges.

## Shared vs local Obsidian state

Tracked:
- `app.json`
- `appearance.json`
- `core-plugins.json`
- `community-plugins.json`
- `types.json`
- `templates.json`
- `plugin-lock.yaml`

Untracked:
- workspace files
- plugin `data.json` by default
- credentials
- local caches
- resolver SQLite index
