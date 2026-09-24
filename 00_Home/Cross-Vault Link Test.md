---
uid:
type: Info
status: Draft
---

# Cross-Vault Link Test

## Goal

Verify that `Test_Vault_` can reference content owned by `Ampure_Data` without copying that content.

## Resolver test

The lightweight resolver plugin is the current MVP.

1. Make sure `Test_Vault_` and `Ampure_Data` are sibling folders on the same computer.
2. Pull both repositories.
3. Reload Obsidian.
4. In this note, type:

```text
[[Cross-Vault Resolver Target
```

5. Choose the result labeled from **Ampure Data**.
6. The inserted link should be UID-backed and readable.
7. Click it.

Expected target:

```text
Cross-Vault Resolver Target
```

Expected behavior: Obsidian opens the target note in `Ampure_Data`.

## Canonical durable format

Stored cross-vault references use:

```text
[Readable title](uid:<30-character-note-uid>)
```

Optional section target:

```text
[Readable section](uid:<30-character-note-uid>#<section-anchor>)
```

The note UID is durable. Vault name and path are only current location metadata.

## View-level rule

When a system/reference view needs to point into another vault:

- point to the target `.base` view when a relevant authoritative Base exists;
- otherwise point to the target vault/folder README or equivalent index.

When a note relates to a specific note in another vault, link directly to that note's UID.
