# MDSE v0.8 Cross-Repository Reconciliation — 2026-10-02

## Purpose

This document is the authoritative continuation contract for the MDSE v0.8 base vault, EA native importer and MDSE Workbench after the 2026-10-02 cross-repository review.

It reconciles the settled model decisions with the current state of:
- `spencerskelly/Test_Vault_` — authoritative methodology/importer workspace;
- `spencerskelly/MDSE_Workbench` — standalone Workbench implementation;
- `spencerskelly/Test_Vault_-base-vault-2026-09-30-rel133-v051` — obsolete clean-base reference;
- `spencerskelly/20260930` — assessment/reference artifact;
- `spencerskelly/261001` — partial/reference import artifact.

Where older files conflict with this document and the decisions appended to the Workspace Decision Log on 2026-10-02, the newer decisions govern.

## Repository authority

### Test_Vault_
This is the authority for MDSE semantics, schemas, importer rules and release instructions.

Current target:
- MDSE release: `0.8.0`;
- relationships: `1.35`;
- element types: `1.17`;
- Local Model: `0.2`;
- importer target: `EA_to_MDSE_Native_Importer_v0.8.0.html`.

### MDSE_Workbench
This is the live plugin implementation. It remains independently versioned from MDSE releases.

The current 0.1.14 implementation is a pre-Local-Model spike. It is not the keepability build. WB-106 is the next implementation gate.

### Old base-vault repository
`Test_Vault_-base-vault-2026-09-30-rel133-v051` is reference only. It must not be issued as the v0.8 base.

### 20260930 and 261001
These are assessment/reference artifacts only. Their generated content, older schemas and importer versions are not continuation baselines and must not be patched into a v0.8 accepted model.

## Settled identity rules

### Global identity namespace
Every independently referenceable MDSE entity draws its 30-character identity token from one globally unique namespace.

A first-class note stores the token as:

`uid: <30-character-token>`

A Local Model record stores the same token inside a kind-prefixed native block ID:

- `part-<token>`
- `ep-<token>`
- `conn-<token>`
- `flow-<token>`

The kind prefix identifies the current local representation. The 30-character token is the persistent identity. A token may never be reused by a note or another local record in the destination vault.

If a local entity is later promoted to a first-class note by an explicit modeling decision, the note retains the same 30-character token. Promotion is not an importer inference.

### EA8647 first-import identity
The current source model lineage identifier is:

`sourceModelId: EA8647`

The authoritative EA source key is:

`EA8647 + EA GUID`

The source model identifier is importer provenance only. It is not written into normal engineering notes or Local Model records.

For first allocation in this import:
1. use the EA creation timestamp exactly as written; do not convert time zones;
2. normalize only to `yyyyMMddHHmmssSSS`;
3. if EA has no millisecond precision, use `000`;
4. use the existing 13-character normalized EA element author code;
5. if the author is missing or unusable for this import, use `skellyspencer`;
6. if no usable creation timestamp exists, start allocation at `20260911000000001`;
7. collisions increment by 1 ms;
8. records competing for one seed are ordered by EA GUID lexical order.

Derived local records inherit the UID seed of the EA source record that causes them to exist. When one source record causes several local records, deterministic ordering is:
1. source GUID;
2. local occurrence kind;
3. owning-context GUID;
4. definition GUID.

The identity allocator checks all existing note UIDs and all existing Local Model identity tokens before assigning anything.

### Rerun identity
`Local Model Source Map.csv` is authoritative for Local Model rerun identity. Once an identity is assigned, reruns reuse it exactly and do not regenerate it from timestamp/author.

A Source Map identity conflict is a hard error for the affected records. The importer never silently repairs, replaces or reassigns identity.

## Source ownership and reruns

EA-owned translated fields may refresh from EA. MDSE-owned content is preserved.

EA-owned:
- mechanically translated source fields;
- source-backed relationships;
- other fields explicitly declared importer-owned.

MDSE-owned:
- `uid` and local identity;
- filename and path after first creation;
- MDSE-only relationships;
- manually added narrative/model content;
- review decisions and later governed model edits unless explicitly returned to EA ownership.

If a person edits an EA-owned field, the next rerun may restore the EA value, but the overwrite is recorded in import evidence.

If an EA-owned relationship disappears from EA, the importer removes that source-provenanced relationship and logs the removal. An independently created MDSE relationship remains.

If a source entity disappears from EA, the MDSE entity is preserved and flagged for explicit disposition. If the source later returns, the existing Source Map identity is reused.

Existing MDSE filenames and paths are never automatically renamed or moved by a rerun.

## Local Model 0.2

Local Model 0.2 advances 0.1 additively.

Workbench must read 0.1 and 0.2. New importer/authoring output writes 0.2 only.

Part and endpoint occurrences may carry:

`usage: standard | variant | option`

Omission means `standard`.

- `standard`: required; effective definition is exactly the stated concrete definition.
- `variant`: required; resolves to one concrete definition in the transitive specialization family rooted at the stated definition.
- `option`: may be absent; when present resolves to the concrete root or a concrete specialization.

Candidate definitions come from `subtypeOf`; lists are not duplicated on occurrences.

Connections and flows do not receive `usage`.

Reusable definitions may carry sparse optional frontmatter `abstract: true`.
- absence means false;
- `abstract: false` is valid but canonical writing omits it;
- abstractness is not inherited;
- an abstract definition may organize a family but cannot be an effective occurrence definition.

## Naming and path rules

### Duplicate and altered-name markers
The former ID-based duplicate-filename rule is superseded.

Within one target folder:
- first exact name: `Name.md`;
- duplicate names: `Name~2.md`, `Name~3.md`, ...;
- filesystem/path alteration: `Safe Name~a.md`, `~b`, ... using lowercase Excel-column sequencing `a..z, aa, ab...`;
- altered and duplicated: `Safe Name~a~2.md`.

The alphabetic alteration sequence is scoped to the sanitized base within the target folder. Deterministic ordering uses the authoritative EA source key.

The same rules apply to folders.

Every numeric-suffix case appears in the duplicate-name review. Every alphabetic-suffix case appears in the altered-name review.

### Folder shortening
Apply existing semantic shortening before touching filenames.

A folder whose primary purpose is to contain a note with the same engineering identity may use the shortest unambiguous identifier from that note; the note carries the full name.

Apply, in order:
1. remove wording already supplied by an ancestor;
2. remove generic structural wording already implied by the hierarchy;
3. shorten the folder before shortening its identically named authoritative note;
4. prefer stable designators/model numbers/section numbers;
5. omit redundant model-number folders when the note below carries the same identity and sibling ambiguity is not introduced;
6. collapse one-child intermediate folders only when they have no note, no independent semantic/navigation value and no sibling structure to preserve;
7. do not create empty folders for empty EA packages.

Industrial connector normalization removes repeated `Connector ASM`, `Industrial`, `Anderson` and redundant model-number wording where unambiguous.

Regulatory folders that directly contain a note with the same section/title retain the full title on the note and reduce the folder to the section/designator where unambiguous.

### Path limit
Maximum repository-relative generated path: **212 characters**.

After approved folder normalization, shorten only the filename if needed, preserving the leftmost human-readable portion and reserving room for alteration/duplicate markers and `.md`.

Any remaining path over 212 characters is a blocking preflight error.

Approved name/folder transformations are non-blocking and logged.

## BindingConnector rule

When BindingConnector context is reconstructable, preserve its contextual endpoints and temporary local `equals` evidence for review.

When the owning context or endpoints cannot be reconstructed deterministically, preserve the source connector in evidence and flag it for review. Do not invent `equals`, `exposes` or a local connection.

## Attachments and diagrams

An approved attachment that cannot be extracted or written is non-blocking. Record it as `failed attachment import` with source/error detail for post-import resolution.

Attachment reconciliation states include:
- written;
- intentionally skipped/out of scope;
- failed attachment import.

Initial v0.8 diagram creation is deferred. Every source diagram must nevertheless reconcile as either:
- `deferred by v0.8 scope`; or
- failed to reconcile.

An unreconciled source diagram is a blocking reconciliation error.

## Evidence package

Retire the four empty legacy artifacts unless a future unique use is demonstrated:
- `Identity Registry.csv`;
- `Model Checks.csv`;
- `Pending Relationships.csv`;
- `Transformation Log.csv`.

The v0.8 evidence set centers on:
- Run Manifest;
- Ledger / terminal reconciliation;
- Local Model Source Map;
- duplicate-name review;
- altered-name/path review;
- unresolved/review semantic and connector findings;
- attachment reconciliation;
- diagram deferral reconciliation.

## Base-vault/importer release gate

The first v0.8 base vault and importer are a matched pair:
- clean base declares `mdse_release: "0.8.0"`;
- importer declares the same release and refuses a mismatch;
- relationships 1.35;
- element-types 1.17;
- local-model 0.2.

The v0.8 importer is a clean-import tool. It does not migrate v0.7-generated model output in place.

The importer remains mechanical. It does not promote local occurrences into notes based on inferred future reuse.

## Workbench gate

Before a whole import is accepted/kept, WB-106 must provide:
- Local Model 0.1/0.2 reader;
- `ModelRef` identity for notes and local records;
- preservation/resolution of `#^local-id` block fragments;
- governed-region protection from ordinary body editing;
- Local Model dropdown/surface;
- local model-health findings;
- occurrence-aware Structure, Interfaces, Where Used and Requirements views.

Repeated note-level relationships are never engineering quantity. Quantity comes from Local Model `multiplicity`.

After WB-106, implement W-314 in this order:
1. read `abstract`;
2. read occurrence `usage`;
3. derive concrete candidates transitively from authored `subtypeOf`;
4. validate base variation semantics;
5. add read-only variation UI;
6. add temporary session configuration;
7. only later define persisted named-configuration syntax and editing.

## Deferred intentionally

Do not block the v0.8 base/importer for:
- persisted named configurations;
- model-number/product-code mapping;
- `allowedDefinitions`;
- cross-variant compatibility matrices;
- topology-specific variation;
- configuration-specific connection/flow syntax;
- new Function/Use Case/State occurrence kinds;
- local-record promotion heuristics.

## Implementation order

1. Keep this workspace as semantic authority.
2. Implement/validate schemas 1.17 and 0.2.
3. Build the canonical v0.8 importer writer and Source Map.
4. Implement the 212-character planner and naming/folder rules.
5. Complete attachments, diagram reconciliation and evidence.
6. Produce a new clean v0.8 base from the authority; do not repurpose the old base repo in place.
7. Validate representative real EA cases.
8. Complete WB-106.
9. Only then run a whole-model import eligible to keep.
