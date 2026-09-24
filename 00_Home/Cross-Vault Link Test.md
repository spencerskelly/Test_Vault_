---
uid:
type: Info
status: Draft
---

# Cross-Vault Link Test

## Goal

Verify that this new vault can reference content owned by another locally available vault without copying that content.

## Test 1 — current/native Obsidian behavior

Until the UID resolver plugin is implemented, use an Obsidian URI as a **temporary transport test**:

```text
[Open Ampure_Data README](obsidian://open?vault=Ampure_Data&file=README.md)
```

This proves that both vaults can be opened and addressed locally. It is **not** the durable production link format because vault names and paths can change.

## Test 2 — canonical durable format

Production cross-vault references use:

```text
[Readable title](uid:<30-character-note-uid>)
```

Optional section target:

```text
[Readable section](uid:<30-character-note-uid>#<section-anchor>)
```

The future resolver plugin will translate the UID to the current accessible vault/path.

## View-level rule

When a system/reference view needs to point into another vault:

- point to the target `.base` view when a relevant authoritative Base exists;
- otherwise point to the target vault/folder README or equivalent index.

When a note relates to a specific note in another vault, link directly to that note's UID.

## Expected result

- Native URI test can open `Ampure_Data` now.
- UID links remain the stored durable architecture, but will not navigate until the resolver layer is implemented.
