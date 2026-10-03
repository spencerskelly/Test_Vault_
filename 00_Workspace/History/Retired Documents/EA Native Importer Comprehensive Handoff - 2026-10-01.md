> [!NOTE] ARCHIVED 2026-10-03 (W-326). Moved to `99_System/archive/10_Docs retired/`; no current file depends on it. See [[00 - Current State]].

> [!WARNING]
> **SUPERSEDED AS THE CONTINUATION ENTRY POINT.** Retained as detailed 2026-10-01 evidence. Continue from [[MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02]] and [[Handoff Prompt - MDSE v0.8 Implementation]]. W-315 through W-319, Ruleset 1.23, element-types 1.17 and Local Model 0.2 govern where this handoff differs.

---
id: INFO-00069
uid: 20261001170000000skellyspencer
status: Draft
---
# EA Native Importer Comprehensive Handoff - 2026-10-01

## Purpose

This is the continuation document for the next chat working on the native Sparx EA -> MDSE/Obsidian importer.

It consolidates:
- the approved local-occurrence/interface/flow modeling decisions made after W-292;
- the experimental v0.6/v0.6.1 implementation work;
- every real-run fault exposed in this session;
- the repository-wide audit performed across every GitHub repository currently accessible;
- the exact authority/baseline to continue from;
- the work that must be merged before another accepted full import.

This file does not replace the historical Workspace Decision Log. The new approved decisions are also recorded there as W-293 through W-297. The Translator Definition and Ruleset are updated in the same work so this is not a parallel ruleset.

## 1. Authoritative continuation point

Continue from:

- Repository: `spencerskelly/Test_Vault_`
- Branch: `main`
- Reviewed head before this handoff update: `a2b9094ff2a84e9431b7ba8a4c6cc9b0352e2688`
- Relationship schema: **1.35**
- Element schema: **1.16**
- Current accepted native importer baseline: **v0.5.2**
- Current Workbench: **0.1.14**, in separate repo `spencerskelly/MDSE_Workbench` (predates W-298 Local Model indexing/edit separation)

`Test_Vault_` is the translator/methodology workspace, not an import output target.

The current clean base-vault repository is:

- Repository: `spencerskelly/Test_Vault_-base-vault-2026-09-30-rel133-v051`
- Branch: `main`
- Reviewed head: `f2d7f165931b10ae2c42c8bced167e18f3a6d776`
- Actual contents: relationship schema **1.35**, importer **v0.5.2**
- The repository name is stale: `rel133-v051` no longer describes its content.

Do not use the historical base branches in `Test_Vault_` as the current baseline:
- `base-vault-2026-09-30-rel132-v04` -> schema 1.32 / v0.4
- `base-vault-2026-09-30-rel133-v05` -> schema 1.33 / v0.5
- `base-vault-2026-09-30-rel133-v051` -> schema 1.33 / v0.5.1

## 2. Critical continuation rule

**Do not continue by extending experimental v0.6.1 directly.**

The next importer should be created by taking **v0.5.2 + relationship schema 1.35 as the baseline** and merging forward the approved occurrence/interface/flow implementation from experimental v0.6.1.

Reason:
- v0.5.2 contains W-291/W-292 `hasState/stateOf` behavior and the stronger clean-base-vault checks.
- v0.6/v0.6.1 were built from the older v0.5 / relationship-1.33 line.
- v0.6.1 therefore regressed the state-ownership rule and weakened the base-vault identity check even though it added the new occurrence model.

The target merger can be called v0.7 (recommended), but the version number itself is not a semantic decision.

### 2.1 Implementation update after handoff

`99_System/09_Tools/EA_to_MDSE_Native_Importer_v0.7.html` now exists on `spencerskelly/Test_Vault_` main as the first merge candidate built from v0.5.2/schema 1.35. The merge carries forward the W-293/W-294 local part, endpoint, connection and flow implementation from the experimental v0.6.1 code while preserving W-291/W-292 `hasState/stateOf`, `ownerField()`, the v0.5.2 clean-base README/workspace rejection checks, source/plan stale-state invalidation, and output-folder handle hardening. Static JavaScript syntax and merge-invariant checks passed. This does **not** promote v0.7 to the accepted importer baseline: real-QEAX validation is still required, and the remaining W-297 acceptance mechanisms (including the still-open hard repository-relative path limit) must be completed before an accepted full import.

### 2.2 Interface and release-pair update

Two additional approved decisions now govern the next accepted build.

- **W-298 — Local Model interface boundary.** Local part/endpoint/connection/flow/applicability records remain structured addressable Markdown in the containing note, but they are a governed Local Model region rather than ordinary narrative text. Workbench presents that content in its own **Local Model** dropdown/surface. Ordinary text editing must not rewrite the Local Model. Read-only parsing/indexing may precede the final authoring contract; structured Local Model editing waits until the canonical body schema/markers are frozen.
- **W-299 — synchronized importer/base release.** The next newly issued importer and clean base vault use one shared release number, **v0.8.0**. The importer is `EA_to_MDSE_Native_Importer_v0.8.0.html`; the clean base declares `mdse_release: "0.8.0"` in `.vault.yaml`. The importer refuses a version mismatch before planning/writing. Relationship schema and element schema retain independent versions and are recorded separately in the Run Manifest.

This does not promote v0.7 or retroactively rename historical base artifacts. v0.7 remains the current merge candidate until the remaining acceptance work is completed.

**W-300 release scope:** the v0.8.0 keepable import is complete for semantic model content and linked-document attachments, but diagram creation is intentionally excluded from the initial run. All 2,924 source diagrams remain part of reconciliation evidence and are marked deferred by scope. A later additive diagram pass selects categories/types and adds only the requested diagram companion notes/Canvas artifacts without changing the accepted semantic model.

**W-302 Local Model boundary:** each note may contain at most one governed `## Local Model` region. It starts with `<!-- MDSE:LOCAL-MODEL START schema=0.1 -->` and ends with `<!-- MDSE:LOCAL-MODEL END -->`. The markers are not semantic data; they make the human-readable records safely parseable and protect them from ordinary body editing.

**W-303 local identity:** v0.8.0 uses stable type-prefixed local IDs (`part-*`, `ep-*`, `conn-*`, `flow-*`). Imported IDs are deterministically derived from immutable EA source identity/provenance rather than sequence position or mutable names, so a re-import preserves the address of the same source occurrence. Visible engineering identifiers remain separate display data.

**W-304 canonical records/source trace:** Local Model records use heading + named-field Markdown. Part occurrences reference reusable Object definitions. Nested/sub-interfaces are recursive endpoint records using the same endpoint schema with a `parent` address. Connections own flow records exactly once; Workbench/indexing surfaces those flows from each participating endpoint. EA GUIDs/source-only provenance are removed from engineering note records and written instead to `99_System/11_Import/Local Model Source Map.csv`, keyed by owner UID + local ID.

**W-305 inherited members:** reusable nested interface members are not expanded into local records automatically. They remain available through the reusable endpoint definition and are materialized locally only when connection, requirement scope, local override or another context-specific reference requires a stable local address.

**W-307 connector-path acceptance target:** the current 20260930 assessment has 89 model-note paths over 260 characters, 88 beneath `Connector ASM - Industrial`. v0.8.0 must drive that connector count to zero through corrected semantic placement, reusable-definition/local-occurrence handling and meaningful naming before the project chooses a global hard path limit. Blind truncation/hash renaming is not an acceptable fix.

**W-308 first remediation pass:** normalize only the connector navigation folders first: remove child wording already supplied by parent context (`Connector ASM`, `Industrial`, `Anderson`, etc.) and omit a model-number folder when the model note beneath already carries that identity and sibling ambiguity is not introduced. Then rerun path statistics before deciding which remaining items require Local Model conversion or other semantic restructuring.

**W-309 regulatory-folder normalization:** if a regulatory folder directly contains an element with the same section/title wording, retain the full title on the note and reduce the folder name to the section number/designator only. This is navigation compression, not a semantic change, and is allowed only when the resulting folder remains unambiguous among its siblings.

**W-310 multiplicity:** grouped local multiplicity is allowed only when copies are intentionally indistinguishable in the local context. Distinctly connected/configured/scoped copies are separate local part occurrences. If a grouped set later needs per-copy context, split/materialize it rather than overloading multiplicity.

## 3. Approved semantic model: reusable definition vs contextual occurrence

### 3.1 Reusable Object/assembly definitions

A reusable Object/assembly is defined once.

Invariant facts that are true every time it is used stay on the reusable definition:
- composition that is genuinely invariant;
- reusable interfaces/endpoints;
- reusable connector/pin/member definitions;
- internal connections that are invariant;
- reusable flow definitions;
- reusable requirements that apply to the definition.

Do not duplicate the reusable Object note merely because it is used by more than one product.

### 3.2 Local part occurrences

When a reusable Object/assembly is used inside another Object/system and the contextual use matters, create a **local part occurrence** in the containing context.

A local part occurrence:
- has a stable local ID separate from its visible engineering name;
- uses `definition` to point to the reusable Object/assembly;
- may carry a local identifier/name and multiplicity;
- inherits invariant structure/interfaces from its reusable definition;
- distinguishes two copies of the same reusable assembly in one system;
- does not require its own Markdown note solely because it is a contextual use.

Conceptual durable identity:

`owner note UID / part local ID`

This solves both:
1. the same reusable assembly used in Product 1 and Product 2 with different integration wiring;
2. two occurrences of the same reusable assembly used inside one product.

### 3.3 Local endpoints

A connector/Port/mating surface/proxy occurrence is owned by the Object/part occurrence on which it exists.

A local endpoint:
- has a stable local ID independent of a human-facing name such as J4;
- uses `definition` for the reusable interface/Port/connector concept;
- preserves source/local identifier, endpoint kind, multiplicity/quantity evidence when present, and EA provenance;
- may inherit nested addressable members from the reusable interface definition.

Conceptual durable identity:

`owner note UID / part occurrence path / endpoint local ID`

Renaming J4 must not change the stable local identity.

### 3.4 Nested interface members

Reusable interface definitions may contain nested addressable members such as:
- pins;
- terminal positions;
- contacts;
- mating features.

This is containment/decomposition, not `subtypeOf`.

A local endpoint occurrence inherits the reusable member structure from its `definition`. Do not create standalone Markdown notes for every inherited pin/contact solely because an occurrence exists.

Connections and flows may target a nested member, for example:

`Product UID / part-001 / ep-J4 / pin-2`

The exact persisted address syntax remains open.

### 3.5 Local connections

A local endpoint-to-endpoint connection has its own stable local ID.

The connection is owned by the **lowest meaningful common Object/system/configuration context** in which the participating endpoint occurrences are brought together.

This is semantic/configuration ownership:
- not folder ownership;
- not arbitrary endpoint ownership;
- not necessarily a standalone Interface note;
- not mechanically "deepest common folder."

The local connection is the authoritative binding context for:
- endpoint A;
- endpoint B;
- all local flows carried across that binding;
- per-flow direction/role;
- connection/source provenance;
- an optional reusable connection/interface `definition` when one genuinely exists.

Conceptual durable identity:

`owner note UID / connection local ID`

### 3.6 Local flows

A local flow is **this occurrence of a reusable flow definition on this specific connection**.

A flow:
- has its own stable local ID;
- uses `definition` for the reusable Item Flow/information/energy/material concept;
- is owned by or allocated to one local connection;
- retains local identifier and EA conveyed-flow provenance;
- uses endpoint roles `transmit`, `receive`, `exchange`, or `unspecified`;
- may derive the opposite endpoint's complementary role when unambiguous.

Conceptual durable identity:

`owner note UID / connection local ID / flow local ID`

One connection may carry multiple flows.

### 3.7 Requirements targeting local occurrences

Existing Requirement `appliesTo` semantics remain unchanged.

A Requirement may apply to:
- a first-class note; or
- an addressable local occurrence such as a part occurrence, endpoint, nested pin/member, connection, or flow when that is genuinely the Requirement's scope.

Do not invent a new relationship just because the target is contained rather than file-backed.

`satisfies` remains restricted to Function and Design.

### 3.8 Body records vs frontmatter

Approved direction:
- first-class note semantics and note-level relationships remain in frontmatter;
- local contextual occurrences live as structured, addressable Markdown body records in their owning note;
- local body records are authoritative for exact occurrence/connection/flow allocation;
- body records must remain readable without a plugin;
- Workbench/importer will parse/index/validate/edit them.

The literal body-record syntax, local-ID token format, block-anchor syntax, promotion criterion, and manual-authoring contract are **not frozen**.

## 4. Why the part-occurrence layer was necessary

The key failure case was:

- reusable Assembly has endpoint J4;
- Product 1 uses Assembly and J4 connects to Part A;
- Product 2 uses the same Assembly and J4 connects to Part B.

Storing J4 -> Part A on the reusable Assembly would corrupt reuse.

Correct separation:
- reusable Assembly defines J4;
- Product 1 owns a local Assembly occurrence and its Product-1-specific J4 connection;
- Product 2 owns a separate local Assembly occurrence and its Product-2-specific J4 connection.

A second hard case:
- Product 3 contains two copies of the same Assembly.

A bare reusable `Assembly UID / J4` cannot distinguish them. The contextual part occurrence provides:
- `Product 3 / part-001 / J4`
- `Product 3 / part-002 / J4`

This is the reason local part occurrence identity is required.

## 5. Approved full-import usability and governance amendments

These decisions were made during the full-scale `20260930` review and are now adopted into the authoritative workspace as W-297.

### 5.1 Folder/navigation strategy

- Folder structure is navigation, not semantics.
- Do not split folders by count alone and do not create arbitrary overflow buckets.
- Aim for approximately 5–6 meaningful levels in ordinary model content.
- Preserve deeper hierarchy when formal/source structure genuinely needs it.
- Collapse a one-child intermediate folder only when it has no independent information/navigation value.
- Do not generate README/Base/Canvas scaffolding for every folder.
- Automatically generate the standard navigation set only for primary MDSE top-level domain folders; lower-level navigation artifacts are exception-based.
- Package notes are exception-based; packages normally become folders only.

### 5.2 Human naming and collision handling

- Soft target: about 40 characters for folder names.
- Soft target: about 80 characters for filenames.
- These are not truncation limits.
- Filename and visible engineering title are separate.
- Port filenames use `i<shortest unambiguous owner label> - <Port Name>`.
- Requirement `_r` is collision-specific, not universal.
- Use EA Name by default.
- Use EA Alias only when Name is clearly unsuitable/machine-noise; preserve the original Name as provenance.
- Reserved infrastructure prefixes: `Template -`, `Rule -`, `README_`, `BASE_`, `CANVAS_`.
- Collision checking covers imported/model content, system/infrastructure files, and user-authored notes.
- Prefer meaningful source/context discrimination before blind numeric suffixes.

### 5.3 Path preflight

Before any model write:
1. apply normal human naming;
2. use approved Alias substitution where justified;
3. remove repeated parent context;
4. strip source/package mechanics;
5. apply established readable abbreviations;
6. remove redundant structural wording;
7. shorten formal-navigation folders only where authoritative notes retain the full identifier/title;
8. recalculate repository-relative paths;
9. block the run if an unresolved path remains over the final hard limit.

The final hard repository-relative path limit remains open.

Do not create `unnamed/` for a known root package.

### 5.4 Housekeeping and run completion

Importer/bootstrap housekeeping should:
- initialize/validate `.vault.yaml`;
- remove tracked OS junk such as `.DS_Store`;
- enforce the reserved infrastructure namespace;
- update the root README appropriately;
- record housekeeping actions.

A run is complete only when every planned entity ends in one terminal state:
- written;
- intentionally transformed/suppressed;
- failed.

There must be zero unexplained remainder.

A partial writer is `INCOMPLETE / FAIL`, regardless of how many files exist.

Keep the Run Manifest concise and human-readable; detailed path/collision/naming/transformation/model-check evidence belongs in separate audit outputs.

Repeating the same semantic relationship target does not express quantity. Preserve occurrence/quantity evidence separately.

## 6. Experimental importer implementation

### 5.1 v0.6

Experimental source:
- Repository: `spencerskelly/20260930`
- Branch: `handoff/full-import-2026-10-01`
- File: `99_System/09_Tools/EA_to_MDSE_Native_Importer_v0.6.html`

v0.6 was created from the v0.5 / relationship-1.33 line to exercise the new occurrence architecture against the real EA model.

It added:
- local part occurrence records for folded reusable EA Parts;
- contextual local endpoint records;
- hierarchical local addresses;
- local connection records;
- connection-owned conveyed flows;
- extraction of conveyed InformationFlow item GUIDs from `t_xref`;
- multiple flows per connection;
- flow roles `transmit/receive/exchange/unspecified`;
- local Requirement `appliesTo` evidence for local Part/Port targets;
- source Multiplicity rendering on local records;
- deduplication of repeated note-level Part relationships instead of using repeated identical links as quantity;
- interface-Class -> Port schema correction: interface-class stereotypes no longer become invalid Port subtypes;
- engineering/source heading preservation rather than using contextual filename as the visible heading;
- local scoped-ID collision diagnostics.

It also removed the old v0.5 limitation that silently acknowledged conveyed InformationFlow values were not rendered.

### 5.2 Synthetic occurrence validation

The v0.6 local model logic was executed in isolation against the exact reuse pattern:

- Product 1;
- local Control Assembly occurrence;
- local Harness occurrence;
- inherited/local J4;
- inherited/local P4;
- physical connection;
- bidirectional CAN InformationFlow with conveyed CAN definition;
- Requirement applying specifically to Product 1 / Control Assembly occurrence / J4.

Result:
- 2 local part occurrences;
- 2 local endpoint occurrences;
- 1 local connection;
- 1 conveyed local flow;
- 1 local Requirement applicability record;
- 0 unresolved conveyed xrefs;
- 0 local-model warnings.

This validates the core ownership/address logic, not the full importer.

### 5.3 v0.6.1

Experimental source:
- same repo/branch;
- file `EA_to_MDSE_Native_Importer_v0.6.1.html`.

v0.6.1 changed only output-folder handling:
- validates the output vault immediately at folder selection;
- clears the cached handle on `InvalidStateError` / `NotFoundError`;
- forces a new selection when Finder/macOS changes the folder behind the browser's File System Access handle.

The occurrence semantics are unchanged from v0.6.

### 5.4 Experimental branch status

Reviewed branch head before this handoff update:
- `c1dcb293cecdd41940ff0b810b3ea1b4edd2013e`

Open PR:
- `spencerskelly/20260930#1`
- title: `Document full-import review and handoff`
- base: `main`
- head: `handoff/full-import-2026-10-01`
- state: open
- not merged

Treat this branch as an implementation/evidence branch only.

## 7. Critical regression found by repository audit

v0.5.2 and relationship schema 1.35 contain W-291/W-292:

`hasState/stateOf` is restored.

Rules:
- Object -> Object uses `hasPart`;
- Object -> State uses `hasState`;
- Object -> State Machine uses `hasState`;
- State Machine -> State uses `hasState`;
- those state pairs must not use `hasChild`.

v0.5.2 centralizes this in `ownerField()`.

v0.6.1, because it was built from the 1.33 line:
- requires relationship schema 1.33;
- lacks `hasState/stateOf` in its relationship constants;
- falls back to `hasChild` for the W-292 state ownership cases.

Therefore v0.6.1 is **not** a valid successor to v0.5.2 as-is.

## 8. Base-vault validation difference

v0.5.2 has stronger base-vault identity checks than v0.6.1.

v0.5.2:
- requires `.vault.yaml`;
- reads root `README.md`;
- requires the README to start with `# MDSE Base Vault`;
- rejects a target containing `99_System/10_Docs/Workspace Decision Log.md`, so the translator workspace cannot be selected accidentally;
- requires relationship schema 1.35;
- identifies filesystem paths when reads/writes fail;
- invalidates old planner/output state on new source/preflight/plan operations.

v0.6/v0.6.1 retained only part of that logic and therefore should not replace it.

The next importer must preserve the v0.5.2 safety behavior and add the occurrence implementation to it.

## 9. Real QEAX validation results

Source tested repeatedly:

`EA_2026_09_06_endgame.qeax`

File size:
- 186,036,224 bytes

Repeated source counts:
- `t_object`: 35,969
- `t_connector`: 21,822
- `t_package`: 1,387
- `t_diagram`: 2,924
- `t_diagramobjects`: 42,966
- `t_diagramlinks`: 37,955
- `t_objectproperties`: 249,892
- `t_xref`: 42,052
- `t_document`: 397
- `t_operation`: 23
- `t_attribute`: 5

Observed result multiple times:
- Preflight: **PASS**
- 0 fail
- 0 warn
- Whole-model plan: **PASS**
- 35,969 elements classified
- 21,822 connectors classified

The EA source has not been the cause of the failed attempts in this session.

## 10. Faults exposed during real run attempts

### F-01 - schema/importer mismatch

Observed:
`v0.5.2 requires relationships.yaml 1.35`, but selected base had 1.33.

Result:
- writer stopped before model generation.

Meaning:
- expected and desirable safety behavior;
- exposed that multiple base-vault versions were being mixed.

### F-02 - existing model target

Observed with v0.6:
`Refusing to import over an existing model: output already contains folder '02 Product Context'.`

Result:
- stopped before writing.

Meaning:
- expected and desirable fresh-target gate;
- selected target was a populated model, not a disposable clean base copy.

### F-03 - wrong folder level / incomplete base target

Observed with v0.6:
`Selected output folder is not an initialized/unpacked base-vault copy: .vault.yaml is missing.`

Result:
- stopped before writing.

Likely cause:
- selected parent/inner folder rather than the actual vault root, or selected an incompletely extracted/recreated target.

### F-04 - stale File System Access handle

Observed:
`InvalidStateError: An operation that depends on state cached in an interface object was made but the state had changed since it was read from disk.`

Meaning:
- macOS/Finder changed, moved, replaced, or recreated the selected folder after the browser had cached its directory handle.

v0.6.1 was added to clear that stale handle and require reselection.

### F-05 - importer-version ambiguity

The local path in one failure showed:
`Test_Vault_/99_System/09_Tools/EA_to_MDSE_Native_Importer_v0.5.2.html`

Later tests used:
`Downloads/EA_to_MDSE_Native_Importer_v0.6.html`

Both were valid files, but they expect different relationship schemas and base behavior.

This exposed a workflow fault:
- file location/version was not unambiguous enough;
- base vault and importer must be treated as one versioned pair.

### F-06 - minimal v0.6 ZIP was not the canonical base vault

A small downloadable `MDSE_Importer_Test_Vault_v0.6.zip` was produced during this session.

It was a minimal disposable target with:
- relationship schema 1.33;
- element schema 1.16;
- root README titled `MDSE Importer Test Vault v0.6`.

It is **not** the canonical W-250 base vault and is not compatible with v0.5.2's stronger README/schema checks.

Do not use it as the next baseline.

### F-07 - experimental v0.6 baseline regression

Repository audit showed v0.6/v0.6.1 were based on 1.33 and therefore omitted W-291/W-292 `hasState/stateOf`.

This is a real implementation regression and must be fixed by rebasing/merging the occurrence work onto v0.5.2/1.35.

### F-08 - authority documents lagged implementation

Before this handoff update:
- `Handoff - Continue Here.md` said it was updated through W-290 while already describing W-291/W-292;
- `Translator Definition.md` said `Current through W-290` while its connector table already included W-292 behavior;
- its base-vault paragraph still described the older 1.33/v0.5 snapshot.

These are documentation faults being corrected with this handoff.

## 11. Repository audit - all currently accessible repositories

### 11.1 `spencerskelly/Test_Vault_`

Role: **authoritative translator/methodology workspace**.

Current main:
- relationship schema 1.35;
- element schema 1.16;
- accepted fallback importer v0.5.2 plus v0.7 assessment/merge candidate;
- complete EA evidence bundle;
- Workspace Decision Log through W-313;
- Translator Definition aligned to Local Model schema 0.1;
- `MDSE v0.8 Design Check - 2026-10-01.md`;
- `local-model.yaml` schema 0.1;
- Ruleset 1.22;
- archived older native-translator rule material;
- MDSE Workbench design workspace.

Branches also retain historical base-vault snapshots (1.32/v0.4, 1.33/v0.5, 1.33/v0.5.1).

Use this repo as the new-chat authority.

### 11.2 `spencerskelly/Test_Vault_-base-vault-2026-09-30-rel133-v051`

Role: **current clean disposable base-vault repository**.

Despite its name:
- relationship schema is 1.35;
- importer v0.5.2 is included;
- README explicitly says the name is stale.

Use a disposable copy, not the repo working copy itself.

### 11.3 `spencerskelly/20260930`

Role: first large populated assessment/reference artifact.

Main:
- partial generated model;
- relationship schema 1.33;
- importer files through v0.5;
- prior audit found 16,307 generated model Markdown notes vs 30,298 planned element-derived entities;
- no completed Run Manifest/Ledger reconciliation;
- known long-path and naming issues.

Branch `handoff/full-import-2026-10-01`:
- comprehensive full-import review;
- occurrence-model Ruleset amendments;
- experimental v0.6 and v0.6.1;
- open PR #1.

Do not treat main or the experimental branch as the current translator authority.

### 11.4 `spencerskelly/261001`

Role: **partial/reference import artifact, not an accepted v0.6 run**.

Audit:
- 16,305 model Markdown notes;
- no `99_System/11_Import` files;
- no Run Manifest;
- no Ledger;
- sampled notes contain no `## Local Model` occurrence section;
- root README says `MDSE Importer Test Vault v0.6`.

Conclusion:
- README/version claim is not sufficient evidence of a successful occurrence import;
- treat as incomplete/reference only.

### 11.5 `spencerskelly/MDSE_Workbench`

Role: Workbench plugin implementation.

Reviewed main:
- plugin version 0.1.14;
- relationship test fixture schema 1.35;
- element fixture schema 1.16;
- Structure view already follows `hasState`;
- Interface view is still based on note/frontmatter relationships;
- Workbench does **not** yet parse/index Local Model schema 0.1 records; WB-106 makes that read/navigation capability a v0.8 keepability gate.

Future requirement:
- after the real merged importer output validates the body record shape, extend Workbench indexing and Interface/Flow Canvas generation.

### 11.6 `spencerskelly/EA_Model_Evidence`

Role: source evidence repository.

Contains raw/enriched EA CSV evidence:
- `t_object`;
- `t_connector`;
- `t_xref`;
- `t_objectproperties`;
- diagram and connectivity audits;
- source integrity/evidence reports.

It is evidence, not semantic authority.

Keep using it to answer source-pattern questions.

### 11.7 `spencerskelly/EA_Model_Import`

Role: older generated-model/import artifact.

Contains the old `Model/...` hierarchy and generated files, not the current native-importer governance/schema stack.

Treat as historical evidence only.

### 11.8 `spencerskelly/EA_Import`

Role: older MDSE/import workspace.

Reviewed:
- Ruleset 1.19;
- relationships schema 1.2;
- element schema 1.2.

Historical only; do not use as the current translator baseline.

### 11.9 `spencerskelly/PosiBattery`

Role: older product vault/model.

Reviewed:
- Ruleset 1.18;
- relationships schema 1.1;
- element schema 1.1.

Historical/product-specific model; not current translator authority.

### 11.10 `spencerskelly/Ampure_Data`

Role: company/common organizational vault.

Its `Rules/MDSE` area is the organization-wide methodology framework, but it is not the live EA native-translator implementation workspace.

Current separation:
- `Test_Vault_` owns the active translator decisions and executable importer work;
- `Ampure_Data` owns company/common organizational knowledge and the modular organization-wide methodology framework.

Stable MDSE methodology changes may later need deliberate promotion into `Ampure_Data/Rules/MDSE`, but do not silently synchronize experimental importer syntax into it.

## 12. Current Workbench implication

Workbench 0.1.14 is still note/frontmatter/path based. The target architecture is now fully defined enough to implement read/navigation support without waiting for another Local Model syntax decision.

Read these authorities together:
- Workspace decisions W-298, W-302 to W-306, W-310 to W-313;
- `99_System/03_Schemas/local-model.yaml` schema 0.1;
- `MDSE v0.8 Design Check - 2026-10-01.md`;
- Workbench decision WB-106.

Required before the first potentially keepable v0.8 import is accepted:
- parse Local Model managed regions and schema 0.1 records;
- index a durable ModelRef for notes and local records;
- preserve `#^local-id` fragments in local-target links;
- show the Local Model dropdown;
- navigate occurrences to reusable definitions and back;
- make Structure, Interfaces, Where Used and Requirements occurrence-aware where needed;
- protect the governed Local Model region from ordinary body editing;
- add local model-health findings.

Structured Local Model editing is deliberately later.

The current plugin's repeated-relationship `×N` behavior is not engineering quantity and must be removed/relabelled as duplicate-source evidence. W-310 quantity comes from Local Model multiplicity.

## 13. Current canonical Local Model design

The canonical body contract is `local-model.yaml` 0.1.

Core rules:
- readable headings;
- stable local IDs as native Obsidian block IDs;
- native Obsidian block links for persisted local references;
- `definition` points to reusable first-class Object/Port/Item Flow notes;
- inherited interface members materialize only when independently addressed;
- each assembly owns the connections below its boundary;
- a parent connects to a child boundary endpoint, not to the child's internal endpoint;
- boundary `exposes` inner;
- EA BindingConnector/temporary local `equals` stays review evidence until meaning is confirmed;
- flows are connection-scoped and authored once;
- grouped multiplicity means contextually interchangeable copies only;
- EA provenance stays in `Local Model Source Map.csv`, not engineering records.

See `MDSE v0.8 Design Check - 2026-10-01.md` for the complete worked example and conformance matrix.

## 14. v0.7 code audit against the target

v0.7 is a merge/assessment candidate, not the v0.8 writer.

Useful code already present:
- direct QEAX read/planning;
- schema 1.35 line;
- local part/endpoint/connection/flow extraction;
- deterministic source-derived local IDs;
- conveyed InformationFlow allocation;
- source multiplicity preservation;
- some native block-link display behavior;
- v0.5.2 safety lineage.

Must change for v0.8:
- add W-302 managed markers;
- replace bold prototype records with canonical headings + fields;
- block ID must equal local ID, not a separate `loc-...` anchor;
- remove EA GUID/source fields from Local Model records;
- persist local references as native block links, not raw address strings;
- implement W-305 lazy inherited-member materialization;
- preserve BindingConnector context as temporary local `equals` evidence rather than only note-level collapsed meaning where reconstructable;
- enforce/report W-310 multiplicity semantics;
- implement W-308 connector and W-309 regulatory folder normalization;
- drive the 88 Industrial connector >260-character paths to zero before selecting the global hard limit;
- import approved `t_document` attachments;
- intentionally defer/reconcile diagrams and support later type-selectable additive diagram passes;
- generate final review/evidence outputs and Local Model Source Map;
- enforce v0.8.0 importer/base release pairing.

Do not patch an assessment vault after generation to simulate these rules. Change the planner/writer and rerun.

## 15. Required next implementation sequence

1. Read `MDSE v0.8 Design Check - 2026-10-01.md`.
2. Read Workspace Decision Log W-293 through W-313.
3. Read current Translator Definition.
4. Read `relationships.yaml` 1.35, `element-types.yaml` 1.16 and `local-model.yaml` 0.1.
5. Treat v0.5.2 as accepted fallback/safety baseline and v0.7 as code evidence/merge candidate.
6. Build `EA_to_MDSE_Native_Importer_v0.8.0.html`; do not issue another unsynchronized interim importer/base pair.
7. Implement the canonical Local Model writer and source map first.
8. Implement assembly-owned connections and contextual BindingConnector temporary-`equals` preservation.
9. Implement W-308/W-309 naming normalization in planning, then remeasure path statistics and confirm zero Industrial connector paths >260.
10. Implement attachments and final evidence/reconciliation.
11. Implement initial diagram deferral plus additive type-selectable diagram pass.
12. Produce a clean base vault with `mdse_release: "0.8.0"` and include `local-model.yaml`.
13. Run syntax/static checks and real QEAX preflight/plan.
14. Before a whole-model write, validate representative real source cases from section 16.
15. In parallel or immediately after the canonical output is stable, update Workbench to the WB-106 read/navigation gate.
16. Do not accept/keep the whole-model run until importer and Workbench gates both pass.

## 16. Acceptance cases

The real source acceptance sample must demonstrate:

1. reusable assembly used in two product/system contexts;
2. two uses of one reusable assembly in one system where available;
3. assembly with at least two internal parts;
4. internal part-to-part endpoint connection;
5. multiple flows on one connection;
6. outward boundary endpoint linked to an internal endpoint by temporary `equals`, then reviewable to `exposes`;
7. parent assembly connected to the child's boundary endpoint;
8. nested pin/contact/sub-interface materialized only because it is independently addressed;
9. Requirement `appliesTo` a local part/endpoint via native block link;
10. grouped interchangeable multiplicity and independently addressable repeated parts;
11. connector and regulatory folder normalization;
12. meaningful Alias replacing a machine/noise URL name;
13. at least one approved linked-document attachment;
14. all EA diagrams reconciled as intentionally deferred in the initial run;
15. stable local IDs across a rerun with unchanged source identity;
16. zero silent loss of conveyed InformationFlow items;
17. state ownership still follows W-292;
18. no invalid Port subtype values;
19. no unexplained terminal-state remainder.

## 17. Remaining decisions

Do not silently decide these:
- exact opaque local-ID token length/collision-extension rule;
- final hard repository-relative path limit after corrected v0.8 planning;
- promotion rule if a previously local-only record later needs to become a reusable first-class definition;
- fallback preservation for a BindingConnector whose assembly context cannot be reconstructed;
- disposition of the four legacy/header-only import CSVs if final evidence makes them redundant.

These are narrower than the older open list; managed-region syntax, local record kinds, native block references, multiplicity, assembly connection ownership and exposure semantics are now settled.

## 18. Copy-ready continuation prompt

Use `Handoff Prompt - MDSE v0.8 Implementation.md`. It is the current concise prompt for a new chat and supersedes the older prompt that ended at W-297.

## 19. Bottom line

The target MDSE is now:

> reusable first-class definitions + contextual Local Model occurrences + assembly-owned connections + connection-owned flows + explicit boundary exposure + native Obsidian navigation.

The model design should not be weakened to match v0.7 or Workbench 0.1.14. Those implementations now need to catch up to the model.

## W-314 continuation — contextual usage and configuration

W-314 adds an accepted semantic layer on top of the Local Model occurrence architecture without changing the deployed importer/schema yet.

The key rule is:

> Reusable definitions describe engineering kinds; Local Model occurrences describe contextual positions; configurations resolve variant/optional positions without mutating either the reusable definition or the base occurrence.

Accepted occurrence field:

```yaml
usage: standard | variant | option
```

Omitted means `standard`. `variant` is required and resolves to one concrete definition from the transitive specialization family rooted at `definition`. `option` may be absent; when present it resolves the same way. A future reusable-definition property `abstract: true` makes a family/root definition non-selectable while still allowing it to organize concrete descendants.

The full theory and examples are in `MDSE v0.8 Design Check - 2026-10-01.md`, section **Local Model Usage and Configuration Theory (W-314)**.

### Impact status at this handoff

| Area | Status after W-314 | Required next implementation |
|---|---|---|
| Modeling semantics | accepted | preserve W-314 without reopening |
| `relationships.yaml` | no change required | none for W-314 |
| `local-model.yaml` | still 0.1 | plan 0.2 with optional `usage` on part/endpoint occurrences |
| managed Local Model marker | still `schema=0.1` | move with schema 0.2, not before |
| `element-types.yaml` | no `abstract` support yet | add optional definition-level property in a governed way |
| property dictionary | no `abstract` definition yet | add when property becomes implemented |
| native importer | no configuration inference | parse/write new schema only after shared contract changes |
| Workbench 0.1.14 | no W-314 implementation | implement after WB-106 Local Model foundation |
| persisted named configurations | concept accepted, exact format open | decide native Markdown representation before save/write support |
| model-number rules | deferred | add later as product/configuration knowledge |

### Next design/implementation sequence

1. Freeze the exact `local-model.yaml` 0.2 field contract and backward-compatibility behavior.
2. Freeze how `abstract` is declared in `element-types.yaml` and its property definition.
3. Update the shared Local Model schema/marker and importer contract together.
4. Update Workbench schema loading, Local Model parser/index and candidate resolver.
5. Add read-only variation-space information and validation.
6. Add temporary configuration selection in Workbench without base-model mutation.
7. Decide the persisted named-configuration Markdown format.
8. Add persisted configuration editing and configured/compare/filter views.
9. Only then consider product-specific model-number generation/reverse decoding.
10. Defer `allowedDefinitions` and cross-variant compatibility syntax until a real product case requires them.

Do not use configurability as a reason to create new top-level element types, new relationship types, or new occurrence kinds. Function/Use Case/State usage semantics can follow W-314 once those contextual occurrence records are independently justified.

## Copy/paste handover prompt after W-314

Continue the MDSE native EA → Obsidian and MDSE Workbench design from the authoritative `spencerskelly/Test_Vault_` main repository. Do not restart the methodology or reopen settled decisions unless current source evidence creates a real conflict.

Start by reading, in this order:

1. `99_System/10_Docs/MDSE v0.8 Design Check - 2026-10-01.md`, especially **Local Model Usage and Configuration Theory (W-314)**.
2. `99_System/10_Docs/EA Native Importer Comprehensive Handoff - 2026-10-01.md`, including the W-314 continuation.
3. `99_System/10_Docs/Workspace Decision Log.md` through **W-314**.
4. `99_System/10_Docs/Translator Definition.md`.
5. the current MDSE Modeling Ruleset.
6. `99_System/03_Schemas/relationships.yaml`.
7. `99_System/03_Schemas/element-types.yaml`.
8. `99_System/03_Schemas/local-model.yaml`.
9. `MDSE Workbench/01 - Workbench Product Definition.md`.
10. `MDSE Workbench/03 - Build Outline and Roadmap.md`.
11. `MDSE Workbench/04 - Architecture and Model Boundary.md`.
12. the standalone `spencerskelly/MDSE_Workbench` repository and its current code before proposing code changes.

Treat those sources as authoritative over older generated vaults and historical translator documents.

### Settled Local Model architecture

- Reusable engineering definitions remain first-class notes.
- Contextual occurrences that need identity live in the owning note's Local Model.
- Local parts reference reusable Objects through `definition`.
- Local endpoints reference reusable Ports/interfaces through `definition`.
- Local flows reference reusable Item Flows through `definition`.
- Stable local IDs are native Obsidian block IDs.
- Contextual topology belongs to the context that creates it, not to reusable definitions.
- Structural and behavioral architecture should reuse definitions rather than duplicate them.
- `subtypeOf / supertypeOf` remains reusable definition-level generalization.
- The Local Model is native Markdown in a governed body region and Workbench remains a view/editor over that model, not a second database.

### Settled W-314 usage/configuration semantics

The contextual Local Model occurrence field is:

```yaml
usage: standard | variant | option
```

Omitted `usage` means `standard`.

- `standard`: occurrence is required and uses the stated concrete `definition`.
- `variant`: occurrence is required and resolves to exactly one allowable concrete definition from the specialization family rooted at the stated `definition`.
- `option`: occurrence may be absent; when present it resolves to the stated concrete definition or an allowable concrete specialization.
- Candidate definitions are derived transitively from the existing `subtypeOf` hierarchy; do not duplicate candidate lists on the occurrence.
- A non-abstract root is selectable along with its non-abstract descendants.
- `abstract: true` on a reusable definition means the definition may organize/generalize concrete definitions but cannot itself be the effective definition of an occurrence. Absence means false. Abstractness is not inherited.
- Optionality and variant behavior belong to the local occurrence, never intrinsically to the reusable definition.
- Do not connect an assembly to every subtype simply to express a variant position.
- Do not create top-level Variant, Variant Point, Option or configuration relationship types for this mechanism.
- The same usage concept may later apply to part, endpoint/Port, Function, Use Case and State occurrences when those contextual occurrence kinds are independently justified.
- Do not automatically extend `usage` to connections, flows, transitions or topology.
- The base reusable architecture stays unresolved and must not be mutated merely to explore a configuration.
- Temporary Workbench selections may be session state.
- Persisted named configurations, when implemented, must store selections separately from the base Local Model and identify occurrences by stable native block-link addresses.
- No persisted selection entry means unresolved. `present: false` explicitly omits an option.
- A completed configuration resolves every variant and explicitly includes/excludes every option.
- Product/model-number codes belong to product/configuration knowledge, not reusable component definitions.
- Defer `allowedDefinitions` and cross-variant compatibility syntax until a real engineering example requires them.

### Important current implementation state

W-314 is a settled semantic decision, but the executable schema/code changes have **not** yet been made.

- `local-model.yaml` is still the deployed 0.1 contract.
- The managed region is still `schema=0.1`.
- `element-types.yaml` does not yet implement definition-level `abstract`.
- `relationships.yaml` requires no W-314 change.
- The native importer does not yet read/write `usage` and must not infer configurability.
- Standalone Workbench does not yet implement W-314.
- The exact persisted named-configuration Markdown format remains open.

Do not silently treat the documentation examples using `schema=0.2` as already-deployed syntax.

### Importer constraints

The importer must not:

- infer `usage: variant` merely because a definition has subtypes;
- infer `usage: option` from EA Use Case `optionOf`;
- equate an EA connector named `Usage` with Local Model `usage`;
- place contextual optional/variant semantics on reusable definitions;
- connect the owner to every candidate specialization.

Until a deterministic source rule is approved, imported occurrences remain standard by omission and uncertain configuration evidence should be preserved for review rather than guessed.

### Workbench direction

Preserve the dependency order:

1. complete the WB-106 Local Model foundation: shared parser, ModelRef identity, block-fragment preservation, governed-region protection and occurrence-aware views;
2. advance the shared Local Model schema intentionally;
3. add `usage` and `abstract` reading/indexing;
4. derive candidate families by transitive specialization traversal;
5. add validation and read-only variation-space information;
6. add temporary configuration selection without mutating the base model;
7. decide the exact persisted named-configuration Markdown representation;
8. add persisted configuration editing;
9. add Generic Architecture, Variation Space, Configured Architecture, Configuration Comparison and configuration-filtered Canvas views;
10. add product-specific smart model-number generation/reverse decoding only after configuration resolution is reliable.

### Next task

First inspect the live schemas and standalone Workbench code for the smallest compatible implementation of W-314. Then propose the exact schema changes and migration/backward-compatibility behavior **before modifying code**.

Specifically resolve:

1. the exact `local-model.yaml` 0.2 representation of optional `usage` on currently supported occurrence records;
2. whether the marker version must move to `schema=0.2` at the same time and how 0.1 notes are read;
3. the exact `element-types.yaml` representation for optional definition-level `abstract`;
4. the property-definition documentation required by the vault's property-governance rules;
5. importer/parser behavior for old and new Local Model records;
6. Workbench candidate-resolution and validation behavior;
7. what must remain deferred until the persisted configuration format is separately approved.

Recommend the smallest approach that scales. Do not add new element types, relationships or persistence layers unless current semantics truly cannot express the engineering need.
