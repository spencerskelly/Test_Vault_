---
uid: 20260927191823000skellyspencer
id: INFO-00001
type: Info
status: Archived
---
# Archived Plugins

Plugins removed from the active stack. Kept here so the work behind them is not lost if we return to them.

Removed from `.obsidian/community-plugins.json` and `.obsidian/plugin-lock.yaml` on 2026-09-28. Reason: the vault is a single vault. Notes link to each other directly, and nothing needs cross-vault links or navigation.

Full original plugin folders (including the Multi-Vault Navigator binary) are in git history at commit `7c1dddd`, the last commit before removal.

## Ampure Cross-Vault Resolver

| Field | Value |
|---|---|
| Plugin ID | `ampure-cross-vault-resolver` |
| Version | 0.1.1 (the plugin-lock file said 0.1.0) |
| Author | Ampure (custom, in-house, not on the community list) |
| Desktop only | Yes |
| Archived copy | `ampure-cross-vault-resolver/main.js` and `manifest.json` in this folder |

**What it did.** Let a note in one vault link to a note in another vault by durable `uid`, so links survived renames and moves between vaults.

- Scanned sibling vault folders on the same computer, read each vault's `.vault.yaml`, and indexed notes that have a 30-character `uid` in frontmatter. The index refreshed every 60 seconds.
- Typing `[[` offered notes from other vaults in the suggestion list.
- Inserted links in the form `[[uid:<30-character uid>|Title]]`.
- Clicking a `uid:` link opened the target note in the other vault.
- Commands: "Rebuild cross-vault index" and "Insert cross-vault link".

**Why it existed.** The earlier plan was a company vault (`Ampure_Data`) plus engineering and product-line vaults, with UID-based links between them. Ruleset 1.21 sections 10, 11 and 13 and `Vault Architecture and Cross-Vault Rules.md` describe that design. It was an MVP.

**To restore.** Copy the archived folder to `.obsidian/plugins/ampure-cross-vault-resolver/`, add the ID back to `community-plugins.json`, and add a pin to `plugin-lock.yaml`. It needs notes with a `uid` and a `.vault.yaml` in each vault.

## Multi-Vault Navigator

| Field | Value |
|---|---|
| Plugin ID | `multi-vault-navigator` |
| Version | 2.3.3 (was not in the plugin-lock file) |
| Author | Hir43th (third-party community plugin) |
| Desktop only | Yes |
| Archived copy | None. Reinstall from the community plugin list. |

**What it did.** Navigate, search and open recent files across several vaults on the same computer.

**Why it existed.** It supported working across the multiple test vaults (Model, Ampure_Data, Import_Test, EA_Import and this one) during the vault-linking experiments.

**What was dropped with it.** `index-cache.json`, a 17 MB generated index of about 12,000 notes from those other vaults, including local file paths. It regenerates on demand and had no place in a shared repo. It remains in git history.

**To restore.** Install it from the community plugin list, add the ID back to `community-plugins.json`, and pin the version in `plugin-lock.yaml`.
