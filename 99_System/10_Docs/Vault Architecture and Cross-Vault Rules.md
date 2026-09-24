# Vault Architecture and Cross-Vault Rules

## Repository model

Use independent sibling Git repositories. Do not nest repositories.

Each vault is independently permissioned and independently cloneable.

## Current organizational direction

- `Ampure_Data` — common company vault.
- Engineering import/staging vault — receives EA data before product-line separation.
- Product-line engineering vaults — EVSE, GSE, MHE, BMID, EMS.
- Engineering Common — shared engineering/product definitions that are genuinely cross-product.
- Additional vaults are created only when authority, confidentiality, workflow, lifecycle, scale, search, or AI-context quality justifies the boundary.

## Authority

Company/shared identities stay authoritative in `Ampure_Data`.

Engineering technical definitions stay authoritative in the responsible engineering vault.

A view/index does not become authoritative merely because it aggregates content from another vault.

## Stable identity

Each vault has `.vault.yaml`:

```yaml
vault_uid: <30-character UID>
name: <display name>
default_branch: main
```

Each durable note has immutable YAML `uid`.

Renames/moves do not change UID.

## Canonical reference

```text
uid:<note-uid>
```

Readable Markdown:

```text
[Title](uid:<note-uid>)
```

The resolver translates UID to the current accessible vault/path.

## Cross-vault UX target

Users should create cross-vault links with the normal `[[` interaction.

The resolver/plugin picker searches all locally registered accessible vaults, disambiguates duplicates, and inserts a readable UID-backed link.

Users should not need to type raw UID syntax.

## Current test limitation

Native Obsidian does not resolve `uid:` links across vaults by itself. Until the resolver plugin exists, `obsidian://open?vault=...&file=...` may be used only to test local cross-vault opening. It is not the production durable storage format.

## Access states

For discoverability/governance metadata, use:

- `open` — expected to be broadly available.
- `assigned` — available to specific groups; others may request access.
- `restricted` — only designated groups/users may access.

Repository permissions remain the real enforcement layer. The registry does not grant access.

The local resolver indexes only vaults the current user can access and must not reveal restricted vault names or paths to unauthorized users.

## Missing target behavior

- installed + accessible: open normally;
- previously known but not installed: show `Vault not installed`;
- unknown/unavailable: show `Referenced note unavailable`;
- never enumerate restricted remote repositories just to resolve an unknown UID.

## View linking

Cross-vault system/reference views should point to:

1. an authoritative Base in the target vault when available;
2. otherwise the target README/index.

Semantic relationships between notes point directly to the target note UID.

## Splitting

Vault boundaries are operational/security decisions, not semantic type rules.

When a vault becomes difficult to search, slow, too broad for AI context, or crosses authority/access/lifecycle boundaries, flag the pressure and recommend a user review of whether to split it.
