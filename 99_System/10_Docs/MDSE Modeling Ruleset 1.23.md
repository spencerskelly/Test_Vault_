# MDSE Modeling Ruleset 1.23

## Status

Current modeling ruleset for the MDSE vault. Reissued from 1.22 after the 2026-10-02 v0.8 cross-repository reconciliation.

Ruleset 1.23 incorporates W-314 through W-319: Local Model usage/configuration semantics, globally collision-resistant reference-point identity, EA8647 first-import identity and rerun ownership, final naming/path conventions, Local Model schema 0.2, element schema 1.17 and the v0.8 evidence/keepability contract.

Where 1.22 or an older importer artifact conflicts with these amendments, 1.23 governs. `relationships.yaml` 1.35 remains the note-level relationship authority; `local-model.yaml` 0.2 governs Local Model records.

## 1. Model meaning before structure

Classify the concept semantically before choosing a type. Search for an existing authoritative definition before creating a new one. Prefer reuse, then instance, true specialization, decomposition, and only then a new independent concept.

Folder placement is navigation only.

## 1.1 Type and subtype nomenclature

The primary reusable engineering-entity type is **Object**. The former top-level type name `Thing` is deprecated.

`Object` may represent physical hardware, software, firmware, or other reusable engineering entities according to its approved subtype. In translator material, use **EA Object** for the Sparx EA metaclass and **MDSE Object** for the MDSE type whenever ambiguity is possible.


Every model note (a note made from a class template in `99_System/05_Templates`) uses `type` for its primary MDSE semantic class and `subtype` for an approved specialization/classification within that type.

Notes in `99_System` are reference and system notes and carry no `type` or `subtype` (W-243).

The former property name `kind` is deprecated and must not be used in new notes.

`subtype` as a property is distinct from the semantic `subtypeOf / supertypeOf` relationship. Use the relationship only for true reusable generalization between modeled elements.

## 2. Generalization

Use `subtypeOf` only for a reusable invariant semantic distinction. Where the difference is ordinary data or configuration, it is not a `subtypeOf`; there is no `instanceOf` field (W-184).

## 3. Product control

Removed in 1.22. `control` and `boundary` are not properties of a note (W-88, W-112).

## 4. Relationships

Author only the forward/owner-side relationship. Paired/symmetric inverses are generated derivative YAML and must be synchronized before handoff.

The same semantic relationship vocabulary applies across vault boundaries.

State ownership follows W-291/W-292: an Object `hasState` a State or State Machine; a State Machine `hasState` a State. Those pairs do **not** use `hasChild`. `stateOf` is the generated inverse.

## 5. Function vs Use Case

Function = behavior controlled by the modeled product.

Use Case = externally controlled behavior/scenario/actor goal.

Do not convert human/external-system steps into product Functions merely because they appear in a journey.

## 6. Evidence and uncertainty

Do not silently fill missing source information. Preserve ambiguity and create a model check when required.

## 7. Requirements

Requirement `appliesTo` defines scope. Function and Design may use `satisfies`. Verification uses `verifies`.

## 8. Verification

Verification defines reusable intent; Procedure orders activities; Setup defines capability; Plan selects campaign content; Result records execution evidence.

## 9. Navigation

Folder structure is for human navigation; it does not create semantic relationships.

Do not split a folder based on element count alone while it remains within the governed capacity. A model-content folder may contain at most **75 generated model files**. Prefer a meaningful semantic or navigational subdivision based on actual engineering or source structure. If no clear subdivision is available, deterministic mechanical subfolders such as `folder_1`, `folder_2`, etc. are allowed so import can continue; each generated subfolder must remain at or below the 75-file limit.

Aim for approximately 5–6 meaningful folder levels below the vault root for normal MDSE content. Deeper structure is allowed when it preserves useful formal/source structure, including regulatory hierarchies, document hierarchy, or real architecture.

An intermediate folder may be collapsed automatically only when it has exactly one meaningful child branch and has no independent note, content, or navigation value.

### 9.1 Automatic navigation artifacts

Do **not** generate README/Base/Canvas scaffolding for every folder.

Automatically generate the standard navigation set only for the primary MDSE top-level domain folders:

- `README_<folder>`
- `BASE_local_<folder>`
- `BASE_all_<folder>`
- `CANVAS_<folder>`

Lower-level navigation artifacts are exception-based and should be added only when a demonstrated navigation need exists.

The Local Base shows direct contents. The All Base is recursive. The Canvas is a map rather than an exhaustive inventory; a soft target of roughly 12–20 nodes is appropriate.

### 9.2 README purpose

A top-level README should explain:

1. what is in the folder;
2. what kinds of elements belong there;
3. where a user should start;
4. what related major areas may be useful next.

Do not put exhaustive generated inventories in the README; use Bases and Canvas for those views.

The root README is a human entry point first. It should briefly explain the vault, the primary MDSE folders, and relationship-based navigation before showing operational import/run information.

### 9.3 Package notes

EA packages normally become folders only. Do not generate a package note for every package. Create one only when it preserves meaningful information or adds genuine navigation/context value.

## 10. Company/domain authority

Removed in 1.22. The vault is one vault with no cross-vault links (W-01).

## 11. Cross-vault identity

Removed in 1.22 (W-01). Every note still has an immutable 30-character `uid` (W-13); its format is in `AI_INSTRUCTIONS.md`.

## 12. Vault creation and splitting

Users create new vaults; AI does not autonomously create or split them.

When scale, access, lifecycle, ownership, search quality, or AI context becomes problematic, AI may recommend that the user consider splitting a vault.

## 13. Cross-vault views

Removed in 1.22 (W-01).

## 14. Integrity before handoff

The checks a translator run must pass are in `Translator Definition.md` section 10. For hand-made work before handoff: YAML parses; ids and uids are unique; links resolve; inverses are synchronized; Functions have performers where applicable; requirement basis, satisfaction and verification gaps are visible.
## 15. Full-import usability and importer governance

These rules were approved from the 2026-10-01 full-scale native-import assessment. They govern importer output and vault usability without changing settled semantic type/relationship rules.

### 15.1 Human-oriented naming

Use the shortest human-readable name that remains unambiguous in context.

Soft targets:

- folder names: aim for ≤40 characters;
- filenames: aim for ≤80 characters.

These are not truncation limits. Longer names are allowed when shortening would remove important meaning. Do not invent opaque abbreviations solely to meet a soft target.

Semantic engineering name and filesystem locator are separate:

- UID remains the stable machine identity;
- filename may carry context needed for uniqueness;
- visible heading/title remains the engineering/source name unless an approved semantic rename exists.

Ports use the filesystem form `i<shortest unambiguous owner label> - <Port Name>.md`, while the visible heading remains the Port name. The `i<...>` convention is for Ports only.

Requirement filename suffix `_r` is collision-specific, primarily for same-named Function/Requirement collisions. It is not mandatory on all Requirements.

Generic repeated source headings such as `General` or `Normative references` may use the shortest useful source-document identifier in the filename while preserving the original heading.

Default to EA Name. EA Alias may become the human-facing name only when Name is clearly unsuitable for people, such as a URL, file path, generated machine string, punctuation-dominated text, or copied metadata. Preserve the original EA Name in provenance/source evidence.

If both Name and Alias are unsuitable, do not invent polished terminology without semantic evidence. A first-class element that still lacks a safe human name becomes a model-check/review item.

### 15.2 Reserved infrastructure namespace

Plain engineering names are reserved for model content.

Known infrastructure uses reserved naming, including:

- `Template - <Name>`
- `Rule - <Name>`
- `README_<folder>`
- `BASE_local_<folder>`
- `BASE_all_<folder>`
- `CANVAS_<folder>`

Known infrastructure collisions may be renamed automatically. A collision with an existing model or user-authored engineering note is blocking and must not be silently renamed.

Collision detection includes imported files, all pre-existing base-vault/system files, and existing model/user-authored notes. Do not solve collisions by blindly adding `_1`, `_2`, and similar suffixes when meaningful source/context can provide a human discriminator.

### 15.3 Approved automatic shortening

Before path evaluation, automatically apply approved human-readable shortening when it remains unambiguous:

- remove repeated parent context from child folder/file names;
- remove redundant generic structural wording when the parent path already establishes the role;
- strip source/package mechanics such as `SC_Pkg`;
- use established abbreviations such as `UBMID` for Universal BMID;
- compact or omit parenthetical engineering identifiers in folder names when authoritative notes retain them;
- shorten navigation folders for formal/regulatory hierarchy while preserving the exact source title/identifier in the authoritative note;
- remove redundant numeric source-placement prefixes in already-established Use Case navigation folders such as Who / What / When / Where / Why.

Formal/regulatory notes preserve exact source identifiers/titles where required for fidelity.

### 15.4 Blocking path preflight

Path checking happens before writing.

Preflight order:

1. apply normal naming;
2. substitute explicit Alias for clearly machine/noise Names;
3. remove repeated parent context;
4. strip source-mechanics suffixes;
5. apply approved established abbreviations;
6. remove redundant generic structural wording;
7. shorten navigation folders where authoritative notes retain the full formal title/identifier;
8. recalculate full repository-relative paths;
9. flag unresolved excessive paths.

After approved shortening, any path still over the final hard repository-relative limit is a blocking preflight error. The importer must not begin writing until every path has a deterministic human-readable destination.

**Amended by W-324.** No name or folder is shortened to fit a length. The approved shortening above is by meaning only. The hard repository-relative stop is **400 characters**; a planned path over 400 blocks the run and is never cut. The only forced cut is the filesystem component limit: a file name over 255 bytes cannot exist and is cut at a word boundary with `~a`; a folder name over 255 bytes blocks the run. Paths longer than 212 characters are listed for review in `Review - Long Paths.csv` and shortened after the import (Post-Import Tasks, Task 9).

### 15.4a Link targets (W-324)

A link written by the importer or by hand goes to the file name: `[[File name]]`. Only when that name is not unique in the vault (case-insensitive) is the shortest trailing path that is unique used, as Obsidian's shortest-path format writes it (`newLinkFormat: shortest`). A full path is never written unless it is the shortest unique one. Identity stays `uid`/`id` in the note, never in a link.

### 15.5 Root-package placement and housekeeping

Never create `unnamed/` as a fallback for a known root package. Known root packages with imported child content must receive intentional placement according to MDSE placement rules.

Before model write, importer/bootstrap should safely:

- remove tracked `.DS_Store`;
- initialize/validate `.vault.yaml`;
- enforce reserved infrastructure naming;
- rename known infrastructure files deterministically where needed;
- update the root README for the actual imported vault;
- record housekeeping actions in run diagnostics.

### 15.6 Reconciliation-based run completion

A run is complete only when every planned entity reconciles to an explicit terminal state:

- written;
- intentionally suppressed/collapsed/transformed by rule;
- explicitly failed.

There must be zero unexplained remainder. If the writer stops part-way, the run status is `INCOMPLETE / FAIL`; file creation alone never establishes completion.

The Run Manifest remains concise and human-readable. Detailed audit reports hold path exceptions, collision handling, naming substitutions, Alias use, transformations, suppressions, duplicate relationships, unresolved semantics, model checks, and other implementation diagnostics.

### 15.7 Repeated semantic relationships and Local Model occurrences

Do not repeat an identical note-level semantic relationship target to express quantity. Engineering quantity comes from Local Model `multiplicity`.

Reusable definitions remain first-class notes. Contextual uses are Local Model records owned by their engineering context:
- part occurrence -> reusable Object definition;
- endpoint occurrence -> reusable Port definition;
- connection -> contextual binding owned by the assembly/context that forms it;
- flow -> one occurrence of an Item Flow on one local connection.

Assembly ownership is authoritative: a parent connects to a child's boundary endpoint, not through the child to an internal endpoint. A boundary endpoint may `exposes` an internal endpoint. Temporary local `equals` preserves unresolved BindingConnector evidence until review.

Each Local Model record has a kind prefix plus a globally unique 30-character identity token:
- `part-<token>`
- `ep-<token>`
- `conn-<token>`
- `flow-<token>`

The token is drawn from the same global identity namespace as note UIDs and is never reused anywhere in the destination vault. The prefix identifies the current local representation; the token is the persistent identity.

Persisted references between Local Model records use native Obsidian block links. The block ID equals the local ID. EA-only provenance belongs in the Local Model Source Map, not the engineering record.

Local Model schema 0.2 is the canonical writer format. Workbench readers support 0.1 and 0.2. Part and endpoint records may carry `usage: standard | variant | option`; omission means `standard`. Connections and flows do not carry `usage`.

Reusable definitions may use sparse optional `abstract: true`. Absence means concrete. Abstractness is not inherited.

### 15.8 Synchronized importer/base releases

From W-299 onward, each newly issued native importer intended for use is paired with one clean base-vault release using the **same semantic release version**.

- the importer declares its release version;
- the clean base vault declares the same value in `.vault.yaml` as `mdse_release`;
- the importer checks the two values before planning or writing and refuses a mismatch;
- the Run Manifest records importer release, base release, relationship-schema version and element-schema version separately;
- relationship and element schemas keep their own independent version numbers.

Existing historical artifacts are not retroactively renamed. The first newly issued synchronized pair after the v0.7 merge candidate is v0.8.0.


### 15.9 Lean runtime base

The engineering/base vault is a runtime artifact, not a copy of the methodology workspace (W-321). Its exact positive file set is machine-defined in `mdse-release.yaml` and generated by `build-base.py`. Do not copy Current State, the release manifest, Translator Definition, Decision Log, EA evidence, archives or Workbench design notes into each engineering vault. The runtime base carries `mdse_release` in `.vault.yaml` and the actual runtime schemas; initialization preserves that release value. The final issued base must pin a WB-106-capable Workbench. Unavailable plugins are not part of the runtime baseline.

## 16. v0.8 identity, naming and rerun amendments — 2026-10-02

### 16.1 Global reference identity

Every independently referenceable model entity uses one globally unique 30-character identity token namespace. Notes store the token in `uid`; Local Model records embed the token in their kind-prefixed native block ID. Identity is persistent across representation changes.

For ordinary hand-created notes, continue using the existing timestamp + 13-character author-code rule. Before assigning a new token, tooling must also avoid every existing Local Model token, not only note UIDs.

### 16.2 EA8647 first-import allocation

For the current EA lineage, `sourceModelId` is `EA8647`; the authoritative source key is `EA8647 + EA GUID`.

Use the EA creation timestamp exactly as stored with no timezone conversion, normalized to 17 digits. Missing milliseconds become `000`. Use the normalized EA author code; missing/unusable author uses `skellyspencer` for this import. Missing creation timestamp allocation begins at `20260911000000001`. Collisions add 1 ms and are ordered by EA GUID lexical order.

Derived local records inherit the seed of the source record that caused them; multiple derived records from one source are ordered by source GUID, local kind, owning-context GUID and definition GUID.

After first allocation, the Source Map is authoritative. Never regenerate or silently repair an assigned identity.

### 16.3 Filename and folder markers

The old ID-based duplicate-filename rule is superseded.

- duplicate: `Name~2`, `Name~3`, ...
- forced alteration: `Name~a`, `Name~b`, ... with lowercase Excel-column sequencing;
- both: `Name~a~2`.

The same convention applies to folders. Numeric markers are duplicate-review items; alphabetic markers are altered-name review items.

A folder that exists primarily to contain an identically named authoritative note may be shortened to the shortest unambiguous engineering identifier/designator because the note retains the full name. Remove repeated ancestor wording and redundant structural terms before shortening filenames. Collapse one-child folders only when they have no note, independent meaning or sibling structure. Do not emit empty folders for empty EA packages.

### 16.4 Rerun ownership

EA-owned translated fields and source-provenanced relationships may refresh. MDSE identity, file path/name, MDSE-only relationships and human-added content are preserved.

A human edit to an EA-owned field may be replaced by EA on rerun but the overwrite is logged. A removed EA-owned relationship is removed and logged. A source entity that disappears is preserved and flagged, never automatically deleted.

### 16.5 Reconciliation severity

Approved naming/folder transformations are non-blocking and logged. Failed approved attachment extraction is non-blocking and logged as a failed attachment import. Every source diagram must reconcile even though initial diagram creation is deferred; an unreconciled diagram is blocking.

See `MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md` for the implementation contract.
