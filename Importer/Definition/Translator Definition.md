---
id: INFO-00023
uid: 20260930120336279skellyspencer
status: Draft
---
# Translator Definition

What the stage 1 translator must do, in one place. It is kept current: any decision that changes a stage 1 rule updates this file in the same commit (W-247). Rules are stated once and cite their decision number. The tables live in the YAML files in `99_System/03_Schemas`, which stay the machine-readable authority; this file says which file holds what and does not copy the tables, so there is one place to change. Where this file and a YAML file disagree, that is a fault to fix, not a choice.

[[Importer Operating Contract]] defines the Stage-1 operational pipeline, trust boundaries, run-state terminology and release-hardening invariants without duplicating the detailed mappings here. [[Importer Issue Register]] tracks observed implementation/authority gaps against that pipeline. Neither document overrides a mapping/schema decision; any disagreement among current authorities is a fault to resolve explicitly.

Current through W-394. (W-325 and W-326 change no stage 1 rule; they align the release chain and the documents.) Release target 0.8.0; the registry of current files is [[00 - Current State]].

## 1. Purpose and scope

- The translator reads Sparx EA and writes the MDSE vault. EA is being retired; the vault becomes the single source of engineering knowledge (handoff, W-01).
- Two stages (W-30). **Stage 1** is direct and mechanical: it applies only approved, deterministic rules, decides no meaning, and loses nothing. The EA type stays in `eaType` and stage 2 corrects it. **Stage 2** applies meaning (reclassification, folding, cleanup) as separate reviewed git commits. The work list for stage 2 is `Post-Import Tasks.md`.
- **Canonical vs review relationship boundary (W-376).** Preserving an EA connector does not require asserting an uncertain MDSE relationship. Connector mappings marked for review and any relationship that fails the current endpoint rules remain source/review evidence and are not written into canonical frontmatter relationship fields.
- Every run goes into a fresh vault. It never imports over an existing vault (W-36, W-37). Only validated runs are committed (W-35).
- The translator fills a generated lean runtime base. Runtime plugins are governed by `.obsidian/plugin-lock.yaml`; the translator does not install plugins. The base ships every runtime plugin pinned, hashed and configured, and MDSE Bootstrap checks it (W-322).
- Path to a testable vault (W-249): a script builds a base vault once from the workspace; the tool fills a copy of it and does not create the vault, the plugin settings or Bootstrap; the tool reads the person notes, `authors.yaml` and the templates from that base vault, not from the workspace. Each test run is a disposable copy, checked by section 10, opened in Obsidian and discarded. The tool takes a package filter (W-252): it opens the `.qeax` read-only, numbers every note from the whole model (W-14) and writes only the selected packages, so a slice keeps its final ids and its numbers have gaps. A full run is the same tool with no filter. Links that leave the slice are written as in a full run (W-253). A fold follows the note that receives it: an element that folds into a note outside the slice is not written in that run (W-254). Packages are selected by a list of package paths given at run time; each path includes every package below it, a path may name any package, and the tool rejects a path that matches no package or more than one (W-255). A path is written `Name > Name > Name`, with `>` as the separator and optional spaces around it; each name is matched against the EA package name after trimming leading and trailing spaces, with case kept; no escaping is needed (W-266). A path starts at one of the ten packages under `IPC !` (my reading of W-117, not confirmed). The first test slice is `02 Product Context` (W-267). Not decided: what the ledger holds for a slice beyond the outcome `outside slice` (W-254).
- The result must be usable by people and AI together. Every review line must be resolvable from the vault alone (W-156). The vault is not released until stage 2 is complete (W-55).
- Stage 1 output is a vault, a ledger, a run manifest and review tables (section 3).
- **Resolvable contextual-endpoint review evidence (W-380).** A definitionless contextual endpoint review row retains the EA source Object_ID used by `localendpoint:<Object_ID>` planning keys, and semantic connector review persists the planner detail explaining why a W-377 connector was withheld. Review evidence must be joinable back to the exact source endpoint without inferring from display names.
- **Fresh-base initialization boundary (W-381).** `vault_uid: UNINITIALIZED` is valid only as a pre-import fresh-base state. The importer may validate/select it, but no model content may be written until explicit initialization allocates a unique governed vault UID and strict base validation passes again.
- **Output placement and naming (W-382).** The importer has no total generated-path-length cap and no generated-file-count limit per folder. It never creates mechanical `folder_N` buckets for capacity. Nested emitted elements are placed under folders named for their emitted parent element while preserving the parent note beside that folder. Generated note filenames are globally unique case-insensitively across the vault namespace, with existing base/system note basenames reserved first; established readable naming and deterministic collision markers still govern the final name. The filesystem component limit remains a physical write constraint.

## 2. Input

- **The import reads the `.qeax` file directly** (W-247). The CSV files in `99_System/CSV_EA` were used to define the rules; they are not an input to the import. Reading the source file avoids a translation error in an extraction step.
- **Source checkpoint requirement (W-373).** A source whose SQLite header indicates WAL mode is rejected. The importer reads only the selected `.qea/.qeax` file and does not merge a companion WAL; use a closed/checkpointed EA snapshot.
- **Exact source fingerprint (W-375).** A viable source is SHA-256 hashed as a complete byte stream before planning. The digest is written into preflight metadata, the Run Manifest and the import transaction state so the exact EA snapshot can be identified independently of filename or size.
- **Source profile authority (W-393, W-394).** Source-shape policy is machine-readable data, not importer-engine code. The active profile is declared by `Base Vault/Definition/mdse-release.yaml` and currently resolves to `Importer/Definition/Source Profiles/EA8647-2026-09-06-v1.json` (`mdse-ea-source-profile/1`). It owns `sourceModelId`, expected table/type counts, and an executable disposition for every discovered QEAX table. `imported` tables are exact-count gated; `ignored_nonempty_approved` tables are explicitly approved as present but not consumed by Stage 1; `ignored_must_be_empty` tables are allowed only while empty. Any discovered table with no disposition, any missing governed table, or any newly non-empty `ignored_must_be_empty` table fails preflight. The self-contained HTML carries an embedded canonical copy for offline use; `sync_source_profile.py` updates/checks that copy, the generic engine validates it at runtime, and CI requires the embedded copy to equal the external authority. Legitimate source-model evolution creates/updates a versioned profile and rebuilds the embedded data; it does not require editing source-count logic.
- The CSV files are an evidence bundle that an earlier tool build (2.6.0) extracted from `EA_2026_09_06_endgame.qeax`. They keep EA's table and column names, and the rules cite those names (`t_object.Object_Type`, `t_connector.Connector_Type`). The rules apply to the same tables in the `.qeax`.
- Tables the import uses, with the rule file that decides each field: `t_object` and `t_package` (elements and packages), `t_connector` (connectors), `t_objectproperties` (tags, including the `Notes` column, which only the `t_objectproperties_raw.csv` extract kept as a separate file), `t_xref` (relationship kinds such as `conveyed`, `trigger`, `entry`, `doActivity`, `represents`, `target`), `t_operation` and `t_operationparams` (operation/state-action evidence; the accepted EA8647 snapshot currently has 0 operation-parameter rows), `t_attribute` (Class attributes, W-86, W-108), `t_diagram`, `t_diagramobjects`, `t_diagramlinks` (diagrams), `t_document` (linked documents as attachments).
- **Base vault contents (W-321).** The exact runtime-base file set is defined once, machine-readably, in `99_System/03_Schemas/mdse-release.yaml` under `runtimeBase`; this document does not duplicate that list. `99_System/09_Tools/build-base.py` builds the clean base from that positive include list, and `check-release.py --base <path>` verifies exact copies and forbids workspace-only material. The deployed base is intentionally lean: it does **not** copy `00 - Current State.md`, `mdse-release.yaml`, the Decision Log, Translator Definition, EA evidence, archives or the Workbench design workspace. Its generated `.vault.yaml` ships `vault_uid: UNINITIALIZED` and `mdse_release: "0.8.0"`; initialization changes the vault identity/name but must preserve `mdse_release`. The old base repository remains reference only. The planned v0.8 importer is copied into the base when it exists; during pre-release development its absence is allowed and reported. The final issued base must pin a WB-106-capable Workbench release. MDSE Bootstrap is not part of the v0.8 runtime baseline while its source/release is unavailable (W-321).
- **Initialized destination gate (W-374).** `vault_uid: UNINITIALIZED` is valid only in the packaged clean base before first-use initialization. The native semantic importer refuses that value (or a missing vault UID); initialize the base first.
- Every source field/tag has a semantic disposition (`property`, `body`, `structure`, `archive` or `drop`, W-33) in the mapping authorities such as `ea-field-dispositions.yaml` and `ea-tag-dispositions.yaml`. Separately, every discovered SQLite table has an executable source-profile disposition (W-394). This prevents an EA feature from beginning to store data in a previously empty table without forcing a governed decision. `t_connectortag` remains intentionally dropped at the semantic layer (W-85) and is explicitly approved as a known non-empty ignored table in the current source profile.
- **Source counts for check 5 (W-257, W-393, W-394).** The values shown here remain human-readable evidence: `t_object` 35,969 (of these 1,386 are Packages), `t_connector` 21,822, `t_package` 1,387, `t_diagram` 2,924, `t_diagramobjects` 42,966, `t_diagramlinks` 37,955, `t_objectproperties` 249,892, `t_xref` 42,052, `t_document` 397, `t_operation` 23, `t_operationparams` 0, `t_attribute` 5; diagram counts are Custom 1,230, Logical 1,038, Use Case 267, CompositeStructure 151, Statechart 109, Activity 95, Sequence 24, Package 10. **The machine authority is the active source profile, not these prose numbers.** The importer reads all 100 discovered table counts needed to enforce the profile dispositions, exact-count gates the 12 `imported` tables, and writes preflight evidence plus the profile identity to the Run Manifest.
- The initial profile values originated in the CSV evidence bundle and were verified directly against `EA_2026_09_06_endgame.qeax` (W-273, W-394): all 12 importer-used table counts (including empty `t_operationparams`), all 31 EA object-type counts, all 15 connector-type counts and all 8 diagram-type counts match exactly. The same accepted snapshot contains 100 SQLite tables total: 12 `imported`, 34 `ignored_nonempty_approved`, and 54 `ignored_must_be_empty`. The tool compares every run against the **active versioned source profile** and fails on any difference (W-268, W-393). The 254–255-character question is also closed: `User Story`, `Product Management Comment`, `Sales Comment` and `Engineering Comment` already stop at that boundary in the QEAX itself and have no continuation in tagged-value Notes. Stage 1 preserves those values exactly, never reconstructs missing text, and reports the condition only as a source-data advisory (W-273).

## 3. Output

All in `99_System/11_Import`, regenerated on every run, read-only evidence (W-35, W-215, W-216).

- `Ledger.csv`: one row per element, connector, diagram and package, sorted by EA GUID. Columns `ea_guid, source_kind, ea_type, ea_name, outcome, rule, uid, id, folded_into_uid`. `outcome` is `note`, `folded`, `link`, `canvas` or `not carried`, and in a slice run only also `outside slice` (W-254); `rule` is the decision number.
- `Run Manifest.md`: date, importer release, base-vault `mdse_release`, relationship-schema version, element-schema version, Local Model schema version, source-profile id/schema, input identity (file name, size and SHA-256), the source counts read from the `.qeax` beside the profile-expected ones (W-257, W-393) and counts by outcome; for a slice run, also the links that leave the slice (W-253). Importer/base release mismatch is blocking from W-299 onward. For v0.8.0 initial import, the manifest also reports all source diagrams as deferred by scope and records that no diagram files were written (W-300).
- `Import State.json`: persistent filesystem transaction state (W-371). It is written as `IMPORT_IN_PROGRESS` before the first model file, becomes `IMPORT_FAILED` on a caught write failure when the filesystem remains writable, and becomes `IMPORT_COMPLETE` only after every required note, attachment and evidence file plus the Run Manifest has been written. The Run Manifest is non-authoritative unless this state is `IMPORT_COMPLETE`. A destination that already contains this file is not a clean base for another semantic import.
- **Run status dimensions (W-372):** the manifest reports source, plan, write, semantic and acceptance status separately. `WRITE_PASS` means the filesystem transaction completed; it does not mean semantic review is clear or the imported vault is accepted/release-ready. `ACCEPTANCE_PENDING` remains until the external acceptance gates complete.
- `Local Model Source Map.csv`: import evidence mapping each imported local record back to EA without putting EA provenance in engineering notes. Minimum columns are `source_model_id,source_key,owner_uid,local_id,local_kind,ea_guid,ea_source_kind,ea_owner_guid`. It is not engineering-model authority, but after first allocation it **is authoritative for importer rerun identity**; reruns reuse assigned local identities from this map and never regenerate or silently repair them (W-304, W-317, W-319).
- Four review tables, each starting `ea_guid, ea_type, ea_name, category`, with no status column (decisions go in `Review Changes Log.md` by the same GUID, W-38): `Review - Block-Level Flow Connectors.csv` (W-217), `Review - Definitionless Local Endpoints.csv` (W-377; supersedes the v0.8.0 `Review - Added Ports.csv` W-218 output), `Review - Nesting Direction.csv` (W-219), `Review - Equals Direction.csv` (W-220).
- Settled (W-319): the four header-only files `Identity Registry.csv`, `Model Checks.csv`, `Pending Relationships.csv` and `Transformation Log.csv` are retired and are not written by v0.8.0. The copies in this workspace are archived under `99_System/archive/11_Import retired/`.

## 4. Notes

- **Classes:** 20, in `element-types.yaml` (schemaVersion 1.18): Object OBJ, Item Flow IFLOW, Behavior BEH, Functional Flow FFLOW, Condition COND, Requirement REQ, Use Case UC, Actor ACT, Failure Mode FM, Issue ISS, Info INFO, Verification VER, Procedure PROC, Setup SETUP, Plan PLAN, Result RES, Document DOC, Artifact ART, modelCheck MC, Diagram DIA. `Object` includes subtype `interface` for reusable interface definitions. `Behavior` subtypes are `function`, `activity`, `action`, and `step`. `Condition` subtypes are `state`, `state machine`, `mode`, and `design`. Port, Function, State, State Machine, Design and Step are no longer first-class note classes under W-384; EA Ports are Local Model Interface occurrences.
- **Notes in `99_System`** carry no `type` or `subtype` and are not model elements (W-243). The translator makes none of them.
- **Properties, in order:** `type`, `subtype`, `id`, `uid`, `status`, `eaType`, `tags`, governed sparse optional properties (currently `abstract` when true), then relationship fields in the order of `relationships.yaml` (W-97, W-126, W-319). `eaType` is the EA stereotype, else the EA object type (W-31); it is temporary. EA's own status, version, phase, complexity, effort and dates other than creation are dropped (W-39).
- **uid:** 17-digit local-time stamp plus a 13-character author code (W-13). Translated notes use the EA creation time and author (W-09). The code is last name plus first name, accents removed, cut to 13 and padded with hyphens (W-10, W-24). For the EA8647 v0.8 first import, an EA author that is blank or unusable uses `skellyspencer`; the generic historical `sparxeaauthor` fallback in `authors.yaml` does not apply to this import (W-316).
- **id:** class prefix, hyphen, five digits, numbered per prefix in EA creation order with ties by EA GUID, no gaps, permanent once final (W-14, W-15, W-18). Always internal (W-203): Requirement subtype `standard` takes `STD-#####` (10,918 notes), subtype `stakeholder` takes `STK-#####` (1,744), other Requirements `REQ-#####`. No designator is parsed. A note reclassified in stage 2 is renumbered and keeps its earlier id in `## Former ids` (W-181, W-207).
- **File names:** EA Name is the default; EA Alias may replace it only when Name is clearly machine/noise and Alias is non-empty, human-readable and sufficiently unique, with original Name preserved in provenance. After required filesystem sanitization, duplicate files/folders use `~2`, `~3`, ... and forced alterations use lowercase Excel-column suffixes `~a`, `~b`, ...; combined cases use forms such as `~a~2`. The old id/type/`_1` collision conventions are superseded for v0.8. Deterministic ordering uses the authoritative source key (W-289, W-318).
- **Links (W-324):** a link goes to the file name, `[[File name]]`. If that name is not unique in the vault (case-insensitive, base-vault notes included), the shortest trailing path that is unique is used instead. Identity stays in `uid` and `id`. The Run Manifest reports how many links use a name and how many use a path.
- **Full-import naming/path governance (W-297):** filename and visible title are separate; use EA Name by default and Alias only when Name is clearly machine/noise, preserving original Name in provenance. Soft targets are about 40 characters for folder names and 80 for filenames; do not truncate meaning just to hit them. Reserved infrastructure prefixes are `Template -`, `Rule -`, `README_`, `BASE_`, and `CANVAS_`. Collision detection covers imported/model, system/infrastructure, and user-authored content and should use meaningful context before blind numeric suffixes. Apply approved readable shortening before evaluating repository-relative paths. Path preflight happens before any model write; any path still over the final hard limit is a blocking error. W-382 removes the importer-defined total-path limit; only the physical filesystem component limit remains. Never create `unnamed/` for a known root package.
- **Connector path remediation (W-307):** the historical assessment identified 88 >260-character paths; v0.8.0 must normalize that connector branch under W-308 and then satisfy the path rules (W-382: no importer-defined total-path limit) under `Connector ASM - Industrial` by correcting semantic placement/reuse and Local Model occurrence handling, plus meaningful Alias naming for machine/noise names. Do not use blind truncation or opaque hash renaming. The corrected planner must report zero >260 model-note paths in that connector structure; then the remaining real paths are used to choose the global hard limit.
- **Connector folder normalization (W-308):** perform the least invasive correction first. Lower folders omit repeated parent context (`Connector ASM`, `Industrial`, `Anderson`, etc.) when unambiguous, and model numbers are omitted from connector subfolder names when the engineering note beneath already carries that model identity. Folder labels are navigation only; note identity/relationships remain unchanged. Remeasure paths after this pass before promoting additional records into Local Model or applying other shortening.
- **Regulatory folder normalization (W-309):** when a regulatory folder directly contains an element with the same section/title wording, keep the full title on the element and reduce the folder to the section number/designator only (for example `7.4.2 Electrical Properties/7.4.2 Electrical Properties.md` → `7.4.2/7.4.2 Electrical Properties.md`). Apply only when the section number is clear and unique in the parent context.
- **Body:** the order is in `Definitions/Note Layout.md` (Note, `text` wording, comment texts, `**EA notes:**`, empty `## Notes`, `## Aliases` and `## Former ids` when needed, multi-line Priority, then `Source: EA`). The `Source: EA` section is in `Definitions/EA Source Section.md`: `EA GUID` first, everything else from EA below it, placeholders and empty values never written.


### 4.1 Folder/navigation output (W-297)

Folder structure is for navigation and does not create semantics.

- Do not split by element count alone; split only for a meaningful semantic/navigational subdivision.
- Aim for about 5–6 meaningful levels in normal model content; deeper formal/regulatory/source hierarchy is allowed.
- A one-child intermediate folder may be collapsed only when it has no independent note/content/navigation value.
- Do not generate README/Base/Canvas scaffolding in every folder.
- Automatically generate the standard navigation set only for primary MDSE top-level domain folders; lower-level navigation artifacts are exception-based.
- EA packages normally become folders only. Create a package note only when it preserves meaningful package information or adds real navigation/context value.


## 5. Elements

Every EA element has exactly one rule (W-148); the input is `eaType`. The rules are in `ea-element-mapping.yaml` (31 EA object types). Counts are from the CSV bundle.

| EA element | Becomes | Decision |
|---|---|---|
| Requirement 13,988 | Requirement. Subtype from the EA package path: standard, engineering (the Engineering Requirements folder), design, functional, stakeholder. Every requirement is its own note; folding is stage 2 | W-115, W-116, W-81 |
| InformationItem 2,825 | Requirement/standard (2,383, in the Regulatory Requirements folder) or Info (442, blank subtype) | W-115, W-145 |
| Port 4,387 | **Local Model Interface occurrence only; never a first-class Port note.** A Port directly owned by a reusable Class becomes a boundary Interface occurrence in that Object's Local Model; a contextual/part-owned Port becomes an Interface occurrence in the containing context. When deterministic EA classifier/redefinition evidence resolves a reusable Interface Class, `definition` points to that `Object / interface` note; otherwise the Interface remains definitionless. Stage 1 does not synthesize a reusable definition merely because an endpoint exists. | W-384 |
| Class 2,737 | Object. The 423 recognized Interface Classes become `Object / interface`; other Classes remain Object under their existing Object mapping. A Physical Context stays an Object with its parts. | W-139, W-384 |
| Part 3,137 | Item Flow (760 FlowProperty pins); typed reusable Parts still resolve/fold to their reusable Object definition for note reduction, but each contextual typed Part also preserves a stable local part occurrence owned by the containing context when identity/configuration matters; untyped Parts may remain Object subtype `part`. Repeated identical `hasPart` targets do not encode quantity | W-132, W-136, W-137, W-138, W-149, W-293, W-294 |
| Object 545 | Object. EA classifier evidence remains available in source provenance/review evidence where needed; W-384 removes the Port-era temporary `hasClassifier` relationship from the current relationship schema. | W-135, W-384 |
| Signal 623 | Item Flow, blank subtype | W-131 |
| Activity 1,668 | Verification / `test` for stereotype `testCase`; otherwise Behavior. If the Activity stereotype includes `function`, it is `Behavior / function` regardless of package location. An Activity under `04 Product Function` is also `Behavior / function`; remaining Activities are `Behavior / activity`. | W-141, W-384 |
| UseCase 1,667 | Use Case; subtype from the folder (what, when, where, who), else blank | W-140 |
| State 1,112 | Condition. A State under `05 Product Design` becomes `Condition / design`; a State identified as a mode becomes `Condition / mode`; remaining States become `Condition / state`. | W-142, W-384 |
| Artifact 459 | Artifact, blank subtype | W-143, W-237 |
| Issue 264, Actor 44, StateMachine 2 | Issue, Actor, and `Condition / state machine`, respectively. | W-144, W-384 |
| Note 431, Text 61, Constraint 1 | Info, blank subtype, except a Note linked to one unique element folds into that element's body. The accepted v0.2 plan folds 247 unique Note elements through 250 NoteLink connector rows; 184 Notes remain Info | W-145, W-161, W-274 |
| 13 small types, 632 (Action 323, StateNode 73, Change 65, Boundary 44, Decision 34, ActivityPartition 28, Trigger 27, Synchronization 14, Sequence 11, ActionPin 6, ProxyConnector 5, Event 1, ActivityParameter 1) | modelCheck, subtype = the EA type, `MC-#####` | W-146, W-181 |
| Package 1,386 | A folder; a modelCheck note, subtype `Package`, only for the 34 with a Notes description | W-147 |

The accepted v0.2 whole-model plan produces 30,298 element-derived MDSE entities, including 34 package notes; 2,924 diagram companion notes are separate (W-274). The difference from the earlier W-161 count is a bookkeeping correction: 250 folded NoteLink connector rows represent 247 unique Note elements.

## 6. Connectors

Every connector has exactly one rule (W-178); 9 have an end missing from the export and write nothing (W-57). The rules are in `ea-connector-mapping.yaml` (15 connector types, W-151 to W-179). `Direction` decides which end is the source (W-51). Part ends resolve to their reusable block definition for note-level semantics while W-293/W-294 additionally preserve the contextual part/endpoint occurrence path; Port ends resolve to the reusable/merged Port definition (W-114, W-155, W-294). Forward note-level fields are written on the owner side; paired inverses and symmetric mirrors are persisted in the same run under the W-275 trial. `relationships.yaml` schemaVersion **1.35** is the authority for allowed note-level endpoint classes, including W-291/W-292 `hasState/stateOf`. The translator remains mechanical: an imported note-level link outside an endpoint rule is kept and becomes a Review finding, not an import error (W-277). The next importer baseline is v0.5.2/1.35; experimental v0.6/v0.6.1 occurrence code must be merged onto that baseline (W-296).

| EA connector | Becomes | Decision |
|---|---|---|
| Nesting 836 | Nothing where it repeats placement (584); the other 252 `hasChild` (`hasPart` for Object to Object, `hasState` for Object to State or State Machine and State Machine to State, W-292) with `REVIEW nesting direction: connector {GUID}` | W-151, W-152, W-292 |
| Generalization 3,974 | `subtypeOf`; mixed types flagged | W-152 |
| Connector 823 | A connector between Local Model Interface occurrences becomes a Local Model Connection rather than a note-level `interfaces` relationship. A BindingConnector is resolved mechanically to `Connection.exposes -> boundary Interface` only when one internal connection and one boundary Interface are deterministic in the same context. Otherwise, resolved same-owner BindingConnector endpoints persist canonical symmetric `Interface.equals`; cross-owner or unresolved cases remain review-only. No Connection is invented. | W-384 |
| Aggregation 2,288 | Composite: Object pairs `hasPart`, Object to State or State Machine and State Machine to State `hasState` (W-292), all else `hasChild`; shared: `includes`; an existing link wins | W-159, W-277 |
| Realisation 950 | A requirement `appliesTo` an Object; Behavior realizes Use Case where the existing direction/rule applies; else `realizedBy` is review evidence until endpoint semantics are valid. | W-160, W-167, W-384 |
| NoteLink 349 | A note on one element folds into its body under `**EA notes:**`; a note on several stays Info with `describes` | W-161, W-162 |
| Dependency 6,762 | By stereotype: `satisfy` (`satisfies`), `deriveReqt` (`derivedFrom`), `refine` (`refines`, `drives`, `describes`), `trace` (`describes`, `affects`, `appliesTo`, `references`), `verify` (`verifies`); none: `dependsOn`; off-pattern flagged | W-163 to W-169 |
| Abstraction 2,811 | `allocate`: Object-to-Behavior uses `performs`; Object/Document-to-`Condition / design` uses `hasDesign`; other accepted mappings retain their existing relationship names, with off-pattern cases held for review. | W-170, W-384 |
| UseCase 1,258 | `extend` is `optionOf`; `include` is `hasChild` | W-171 |
| Association 603 | One-way `participants` on the Use Case; else earlier rules or `tracesTo` flagged | W-172 |
| Usage 239 | Behavior or Condition realizes a Use Case where the governed endpoint rule permits it; requirements `dependsOn` requirements. | W-173, W-384 |
| ControlFlow 407, StateFlow 200 | `precedes`; Guard, Trigger and Effect as lines on the step before | W-174, W-175 |
| Sequence 199 | An ordered message list on the diagram companion note, no field | W-176 |
| InformationFlow 123 | Preserve occurrence-level topology only: the participating Interfaces belong to a Local Model Connection, and each conveyed Item Flow is a local Flow under that specific Connection with roles `transmit`, `receive`, `exchange` or `unspecified`. W-384 removes the former note-level Port `interfaces` / `transmits` / `receives` / `exchanges` summary. | W-177, W-294, W-384 |

An off-pattern pair keeps the EA meaning and gets `REVIEW modelCheck: <stereotype> <source type> to <target type>` (W-160 onward). Connector names use `- Connector name: <name> (to [[other end]])` (W-158). Where a placement child is `subtypeOf` its owner, no placement link is written (W-178). A Behavior or Condition may satisfy a requirement when permitted by `relationships.yaml`; a requirement applies to its governed target (W-384).


### 6.1 Local occurrence, connection and flow preservation (W-293, W-294)

Stage 1 must preserve the distinction between a reusable definition and a contextual use without forcing every contextual use into a standalone note.

- **Local part occurrence:** when a reusable Object/assembly is used inside another Object/system and the contextual use matters, the containing context owns a stable local part occurrence. It uses `definition` to reference the reusable Object. Invariant structure remains on the reusable definition; product/system-specific integration belongs to the containing context.
- **Local Interface occurrence:** every EA Port that survives Stage 1 is represented as an Interface occurrence with a stable local ID separate from its visible identifier. `definition` may point to a reusable `Object / interface` only when deterministic source evidence resolves one; otherwise it is omitted. An Interface directly owned by the containing reusable Class/Object is a boundary Interface; part-owned or nested Interfaces retain their contextual ownership. A definitionless Interface cannot carry `usage`.
- **Local Connection:** the binding between two Interface occurrences has its own stable local ID and is owned by the lowest meaningful common Object/system/configuration context that brings those occurrences together. It may optionally use `definition` for a reusable connection concept. In Local Model 0.4, `exposes` belongs to the Connection and points to the boundary Interface through which that internal/context-owned Connection is made externally available.
- **Local flow:** each conveyed information/energy/material occurrence is allocated to one specific local connection, not merely to a Port. One connection may carry multiple flows. Local flow identity is connection-scoped and the participating endpoint roles are `transmit`, `receive`, `exchange` or `unspecified`.
- **Part-terminated conveyed-flow exception:** when EA provides a conveyed InformationFlow with exactly one contextual Part endpoint and one Interface endpoint, and no deterministic Interface exists at the Part end, the importer must not synthesize an Interface or Connection. The source connector and conveyed Item Flow are retained in `99_System/11_Import/Review - Part-Terminated Conveyed Flows.csv` as governed import-review evidence. This is a semantic review finding, not a Local Model flow, and does not extend Local Model schema 0.4.
- **Requirements:** existing `appliesTo` semantics may target an addressable local occurrence when that occurrence is genuinely the requirement scope. No new relationship is introduced solely because the target is contained.
- **Storage direction:** first-class note semantics remain in frontmatter. Exact occurrence/connection/flow allocation is represented as structured, addressable, human-readable Markdown body records owned by the containing note. These records form a governed **Local Model** region distinct from ordinary narrative text (W-298). Canonical current writing uses `<!-- MDSE:LOCAL-MODEL START schema=0.4 -->` through `<!-- MDSE:LOCAL-MODEL END -->`. Schemas 0.1, 0.2 and 0.3 retain their historical meanings; readers must select syntax/semantics by the region version and never silently reinterpret an older region as 0.4. The comments are parser/editor boundaries only. Missing, duplicate, nested or mismatched boundaries are model-health errors. Canonical record fields, native block-ID/address syntax, identity-token rules and usage semantics are governed by `local-model.yaml` 0.4 and W-384. Promotion of a local occurrence to a note remains an explicit modeling decision and is not inferred by the importer.

Conceptual durable addresses use the same Workbench/Local Model seam for every local kind:
- local record = owner note UID + local ID.

The local ID already carries the persistent globally unique 30-character token. Part/parent nesting and the carrying connection are semantic/context links, not additional identity components (W-315, WB-106).

**Superseded by W-315 (Ruleset 1.23 section 16.1, Local Model 0.2):** the short tokens of W-303 (`part-a7c31f` and similar) are no longer used. Every local record takes one 30-character identity token from the same globally unique namespace as note `uid` values, wrapped in a kind prefix: `part-<token>`, `ep-<token>`, `conn-<token>`, `flow-<token>`. The kind prefix names the current representation; the token is the persistent identity and is never reused. Allocation, rerun reuse (Local Model Source Map) and collision rules are in `MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md`, section "Settled identity rules".

A named source occurrence alone does not require a standalone Markdown note if these facts can be retained and addressed reliably in the containing model.

### 6.1 Canonical Local Model record pattern (W-304, W-306, W-311 to W-313)

v0.8.0 uses engineering-readable headings plus named-field Markdown records inside the W-302 managed region. Each materialized record ends with a native Obsidian block ID equal to its stable W-303 local ID. All persisted references between local records use native Obsidian block links under W-312; bare local-ID strings are not the canonical persisted reference form.

The machine-readable authority for this body format is `99_System/03_Schemas/local-model.yaml`. Schema 0.4 is the current writer contract (W-384); readers must accept 0.1, 0.2, 0.3 and 0.4, preserving each older version's semantics rather than silently upgrading it.

- **Part occurrence:** readable heading, `definition` to reusable Object/assembly, optional `identifier` and `multiplicity`, followed by `^part-*`. W-310 permits multiplicity only for contextually interchangeable copies.
- **Interface occurrence:** readable heading; optional `definition` to a reusable `Object / interface`; optional `part` link to a local part occurrence or `parent` link to a local Interface occurrence; optional canonical symmetric `equals`, identifier/multiplicity/kind; followed by `^ep-*`. `part` and `parent` are mutually exclusive. An Interface with neither is on the owning assembly boundary. A definitionless Interface is valid contextual topology but cannot carry `usage`.
- **Connection:** readable heading with `endpointA` and `endpointB` native block links, optional `exposes` pointing to one or more same-context boundary Interface occurrences, followed by `^conn-*`. The owning note is the assembly/context that forms the connection.
- **Flow:** readable nested heading under its carrying connection, `definition` to reusable Item Flow, endpoint role fields (`transmit`, `receive`, `exchange`, `unspecified`), followed by `^flow-*`. The authoritative flow occurrence exists once on the connection.

Example:

```markdown
### Parts

#### Power Board
- definition: [[Power Board]]
^part-power-board

#### Logic Board
- definition: [[Logic Board]]
^part-logic-board

### Interfaces

#### Power Board J2
- part: [[#^part-power-board|Power Board]]
- definition: [[CAN Interface]]
^ep-power-j2

#### Logic Board J4
- part: [[#^part-logic-board|Logic Board]]
- definition: [[CAN Interface]]
^ep-logic-j4

#### CAN
- definition: [[CAN Interface]]
^ep-can

### Connections

#### Internal CAN
- endpointA: [[#^ep-power-j2|Power Board J2]]
- endpointB: [[#^ep-logic-j4|Logic Board J4]]
- exposes: [[#^ep-can|CAN]]
^conn-internal-can

##### CAN_H
- definition: [[CAN_H]]
- endpointA: transmit
- endpointB: receive
^flow-can-h
```

W-384 distinguishes a Connection from the boundary Interface that exposes it. A parent assembly connects to a child assembly's boundary Interface; it does not reach through the child to an internal endpoint. When deterministic BindingConnector/context evidence identifies exactly one internal Connection and boundary Interface, Stage 1 writes `Connection.exposes -> boundary Interface`. Otherwise, if both BindingConnector endpoints resolve to Interface occurrences under the same Local Model owner, Stage 1 writes canonical symmetric `Interface.equals`. Cross-owner or unresolved bindings remain review-only. The importer never invents a Connection to satisfy a BindingConnector.

EA-only provenance does not appear in Local Model engineering records. The importer writes `99_System/11_Import/Local Model Source Map.csv`, keyed by owner note UID + local ID. Minimum columns remain `owner_uid,local_id,local_kind,ea_guid,ea_source_kind,ea_owner_guid`; additional source-only columns may be added when needed.


### 6.2 Representation policy (W-306)

Prefer core Obsidian mechanisms and standard Markdown/YAML whenever they preserve the required MDSE meaning. Prefer broad plugin compatibility next. Workbench-only syntax/storage is a last resort. Workbench may provide richer semantic interpretation and views, but basic reading and navigation must remain useful in core Obsidian wherever practical.

## 7. Fields, tags, packages

- **Dispositions:** every EA field, tag, small table and `t_xref` kind has one (section 2). Values kept are the tag lines, the comment texts and the structure lines defined in `Definitions/EA Source Section.md` (W-93, W-101, W-102, W-104 to W-106, W-209).
- **Packages:** the vault tree starts at the ten packages under `IPC !`; `Model` and `IPC !` are not folders (W-117, `ea-package-rules.yaml`). Package names follow the file-name rules. A package without a Notes description is only a folder.
- **Relationship fields in templates:** current first-class relationships are governed by `relationships.yaml` 1.36, not legacy Port/Function/State templates. Behavior and Condition use the retained semantic relationship names where their endpoint rules permit them; Interface occurrence topology, including Connection-owned `exposes` and canonical symmetric `equals`, is represented in Local Model 0.5 rather than frontmatter. The translator writes fields from the governed connector rules, not from legacy templates.

## 8. Diagrams and attachments

- A diagram is a canvas file plus a companion note (W-73). The companion note is class `Diagram`, `DIA-#####`, subtype the EA diagram type (custom, logical, use case, composite structure, statechart, activity, sequence, package; W-212). It carries `Canvas: [[...canvas]]` when the canvas exists (W-213). A folded EA note drawn on a diagram becomes a canvas text card holding its text (W-214). A sequence diagram has no canvas; its companion note lists the messages (W-176). **W-300 release scope:** the initial v0.8.0 keepable import does not create any diagram notes or Canvas files. All source diagrams are reconciled as intentionally deferred. After the semantic model + attachments import is accepted, an additive diagram pass may be run against that vault. **W-301 selection:** the user may choose one or more preserved EA diagram types—Custom, Logical, Use Case, CompositeStructure, Statechart, Activity, Sequence, and Package. Only selected diagrams are added; re-running must not duplicate diagrams already imported and must not alter accepted semantic model content.
- An element with a default diagram gets a `Default diagram: [[...]]` line, written only when the canvas exists (W-80). A diagrams-only run may add diagrams to an existing vault, additive and through the ledger (W-62).
- Linked documents in `t_document` become files next to the note, named `<note file name> asset <n>`, the counter from 1 on every note, in the order of the pictures in the source RTF (W-76 to W-78, W-210). Not checked: that the byte order of pictures in an RTF matches the page order. `BinContent` is a ZIP payload that is unwrapped and CRC-checked before extraction; every row ends in one outcome (W-323).

## 9. Review lines and modelCheck

- modelCheck (`MC`) holds unmapped EA elements; the subtype is the EA type; nothing is lost (W-100, W-146, W-181).
- Review lines are written on the notes and in the review tables (section 3). The kinds: `REVIEW port needed`, `REVIEW nesting direction`, `REVIEW modelCheck: ...`. Each is resolvable from the vault alone (W-156).

## 10. Checks the tool must pass before a run is kept

1. Every element, connector, diagram and package lands in exactly one outcome and one rule; the ledger has one row each (W-148, W-178, W-215). For the initial v0.8.0 import, every diagram must reconcile explicitly as intentionally deferred rather than written (W-300).
2. No two notes share an `id`, a `uid` or a path (case-insensitive). File names may repeat in different folders; within one folder a repeat takes `~2` (W-318), and links name the shortest unique path where a name repeats (W-324).
3. Every `[[link]]` the tool writes resolves to a note or an attachment in the run. In a slice run, a link to a note outside the slice is accepted when its target is in the model; the run manifest lists those links (W-253).
4. Every YAML and JSON file in the vault parses; every relationship field written is in `relationships.yaml`; every governed Local Model record validates against `local-model.yaml`. Paired inverses and symmetric mirrors must match before writing. From W-376 onward, reviewed connector mappings are evidence-only and any remaining endpoint-rule violation is recorded then suppressed (including its inverse/symmetric mirror) before Markdown is rendered; canonical YAML must therefore contain only currently legal endpoint combinations.
5. The source inventory the tool reads from the whole `.qeax` must satisfy the **active versioned source profile**. All `imported` table rows, EA object types, connector types and diagram types are exact-count gated. Every discovered table must also have a disposition; a missing governed table, an undispositioned new table, or a non-empty `ignored_must_be_empty` table fails preflight. `ignored_nonempty_approved` means the table is consciously present but outside Stage-1 consumption; changing that decision requires source-profile review. If source evolution is intentional, a person reviews that change, updates/version-controls the profile, regenerates the embedded profile data with the sync tool, and reruns acceptance; executable importer count logic is not edited. This applies to every run, full or slice (W-257, W-268, W-393, W-394).
6. Before any model write, validate that every planned output path is deterministic, collision-free and writable. W-382 imposes no importer-defined total repository-relative path-length cap and no per-folder file-count cap. Only physical filesystem component constraints remain; a component the selected filesystem cannot create must be deterministically adjusted or the write must fail.
7. Reconcile every planned entity to one terminal state: written, intentionally transformed/suppressed, or failed. There must be zero unexplained remainder. A partial writer is `INCOMPLETE / FAIL`; file creation alone is not completion. The filesystem transaction must follow W-371: `IMPORT_IN_PROGRESS` precedes the first model write, the Run Manifest is written only after the other required evidence, and `IMPORT_COMPLETE` is the final authoritative write. Any `IMPORT_FAILED`, lingering `IMPORT_IN_PROGRESS`, or missing transaction state makes the candidate vault invalid. Keep the Run Manifest concise and put detailed path/collision/transformation/model-check evidence in separate audit outputs (W-297, W-371).
8. Import/bootstrap housekeeping initializes or validates `.vault.yaml`, removes tracked OS junk such as `.DS_Store`, enforces the reserved infrastructure namespace and records its actions (W-297).
9. For synchronized releases, the importer's release version must exactly equal the clean base vault's `.vault.yaml` `mdse_release`; mismatch blocks planning/writing. Relationship and element schema versions are checked separately and are not required to equal the release version (W-299).
10. A run that fails any check is discarded, not committed (W-35).

Checks 1 and 10 follow earlier decisions; checks 2 to 5 are approved (W-256); checks 6 to 8 are the W-297 full-import amendments; check 9 is the W-299 matched-release gate. Check 5 compares whole-model source counts, so it holds for a slice run too (W-257).

## 11. What stage 1 does not do

Reclassify `modelCheck` notes, split Object, Design or State by `eaType`, fold requirements, resolve `hasClassifier` and `equals`, move block-level flow connectors to ports, or decide any meaning. These are stage 2: `Post-Import Tasks.md` (W-30).

## 12. Open, not yet a rule

Implementation status (W-271, W-273, W-274, W-276, W-287, W-288, W-289, W-290, W-291, W-292, W-295, W-296, W-297): the native tool is a developer-only local HTML application. v0.1 established direct-QEAX preflight; v0.2 added the whole-model planner and is the immutable accepted planning baseline after its 1,948 ms PASS on the actual QEAX (35,969 elements, 21,822 connectors, 1,387 packages, 2,924 diagrams, 42,052 xrefs; 30,298 element-derived entities). v0.3 added W-276 canonical identity and the first structural writer. v0.4 added relationship schema 1.32 and shared Aggregation → `includes`. `99_System/archive/09_Tools retired importers/EA_to_MDSE_Native_Importer_v0.5.2.html` (archived, W-326) is the next assessment build (v0.5.1 plus `hasState`/`stateOf`, schemaVersion 1.35, W-291, W-292; ownership placement writes `hasState` for an Object or State Machine that owns a State or State Machine): it carries W-288, reports provisional `tracesTo` links as Review findings, implements W-289 human filenames, and adds explicit slice/whole-model output. It rejects existing model root folders rather than importing over a generated model. W-290 also resets stale plan/output-directory state whenever a new preflight/source is used, forces output-folder reselection after a new plan, and rejects the `Test_Vault_` translator workspace as an output target. Its output remains assessment-only: diagrams/canvases, `t_document` attachments, the four final review tables, and all remaining EA source-evidence lines are not yet complete. Experimental v0.6/v0.6.1 on `spencerskelly/20260930` branch `handoff/full-import-2026-10-01` proves the W-293/W-294 occurrence approach in isolated code and adds conveyed-flow allocation, but it was built from the older relationship-1.33 line and regresses W-291/W-292 `hasState/stateOf` plus part of the v0.5.2 base-vault validation. Therefore the next importer must start from **v0.5.2/schema 1.35 and merge the occurrence code forward** (W-296); do not continue directly from v0.6.1.

Implementation update, 2026-10-01: `99_System/archive/09_Tools retired importers/EA_to_MDSE_Native_Importer_v0.7.html` (archived, W-326) is now the merge candidate created from v0.5.2/schema 1.35. It carries the W-293/W-294 local part/endpoint/connection/flow renderer and conveyed-flow extraction while retaining `ownerField()` W-291/W-292 state ownership, schema 1.35 relationship constants, the clean-base README/workspace rejection checks, source/plan stale-state invalidation, and immediate output-folder validation. Static JavaScript parsing and merge-invariant checks pass. v0.7 is not yet the accepted baseline: it still needs the actual QEAX run, and W-297 path-limit/housekeeping/terminal-reconciliation acceptance behavior is not fully implemented; the hard repository-relative path limit was open at that assessment point; W-318 now fixes it at 212 characters. W-298 also requires the Local Model to be treated as a governed body region separate from ordinary text editing. W-299 establishes that the first newly issued synchronized importer/base pair after this candidate will be v0.8.0; v0.7 is not retroactively paired or promoted by that numbering decision.

The Open list at the end of `Workspace Decision Log.md` is the list. Still open and relevant to the importer: the package filter beyond one path (W-252, W-254), unexplained audit-count differences that are not source-baseline counts, the standalone inverse-regeneration workflow and the Nodian trial, and whether third-party standards content may stay in the vault (this decides which attachments are "approved"). Settled since and no longer open: naming, folder and path rules (W-318), the four header-only import files (W-319), the v0.5 assessment findings (carried into W-315 to W-319).

### Local Model configuration usage (W-314)

Local Model `usage` is contextual configuration semantics, not an EA connector-type mapping.

Schema support is now governed by local-model 0.2 / element-types 1.17, while importer code still has to implement it:

- omission means `standard`;
- `variant` means a required local position whose effective reusable definition must be one concrete member of the specialization family rooted at the stated `definition`;
- `option` means the local position may be absent and, when present, uses a concrete member of that same family;
- definition-level `abstract: true` excludes that reusable definition from being an effective occurrence selection.

Stage 1 import must not infer configurability from the mere existence of reusable subtypes. It must not map EA Use Case `optionOf`, an EA `Usage` connector, or ordinary generalization directly to Local Model `usage`. Until an approved deterministic source rule exists, imported occurrences remain `standard` by omission and ambiguous configurability evidence is retained for review.

The importer must never express one configurable position by relating the owning assembly to every candidate subtype. The local occurrence remains the single contextual position; candidates are derived from the reusable `subtypeOf` hierarchy.

W-314 is implemented in schema form by W-319: Local Model 0.2 adds `usage: standard | variant | option` on part and endpoint records (omission means `standard`) and element-types 1.17 adds sparse optional `abstract: true`. The importer writes 0.2 only; Workbench readers accept 0.1 and 0.2. Candidate definitions are derived from `subtypeOf`; persisted named configurations remain deferred.


Implementation update, 2026-10-02: `EA_to_MDSE_Native_Importer_v0.8.0.html` (archived in `99_System/archive/09_Tools retired importers/`, W-326) now exists as the release candidate implementation. It carries the v0.5.2 safety lineage and v0.7 occurrence work forward, validates the 0.8.0 controlled base plus relationships 1.35 / element-types 1.17 / Local Model 0.2, allocates global note/local identity tokens, writes canonical Local Model 0.2 records and Source Map evidence, enforces W-318 naming and 212-character path preflight, reconciles deferred diagrams, writes the final evidence/review views, and imports governed linked documents mechanically (ExtDoc images, ModelDocument RTF picture payloads in source order, and text-only RTF unchanged), with any unreadable/unknown payload explicitly reconciled as a failed attachment import. It is **not yet accepted/release-conformant**: it still requires a real QEAX run to verify attachment/result counts and the WB-106 keepability gate before the first whole-model import is kept.

## v0.8.0 implementation amendment — 2026-10-02

This section supersedes older translator details where they conflict.

### Release contract

The next accepted native importer is `EA_to_MDSE_Native_Importer_v0.8.0.html`, paired with a newly generated clean base declaring `mdse_release: "0.8.0"`.

Required schemas:
- relationships 1.35;
- element-types 1.17;
- local-model 0.2.

The import is clean. v0.8 does not migrate a v0.7-generated populated vault in place.

### EA lineage and identity

For this import, `sourceModelId = EA8647`. Authoritative source identity is `EA8647 + EA GUID`.

First allocation uses EA Created exactly as stored, no timezone conversion. Missing milliseconds are `000`; missing/unusable author uses `skellyspencer`; missing Created allocation begins at `20260911000000001`. Use +1 ms collision handling and EA GUID lexical tie-breaking. Every allocated 30-character token is checked against note UIDs and all Local Model tokens.

Derived local records inherit the causing source's seed. Source Map identity is authoritative on rerun.

### Rerun ownership

Refresh only declared EA-owned translated fields and source-provenanced relationships. Preserve MDSE identity, existing file path/name, MDSE-only relationships and human-added content. Log overwritten human edits in EA-owned fields. Remove and log EA-owned relationships removed from EA. Preserve and flag entities whose source disappears.

### Local Model

Write new governed Local Model regions as schema 0.3. Existing schema 0.2 semantics remain frozen/compatible. Definitionless contextual endpoints may omit reusable `definition` under W-377/W-378; standard part/endpoint usage is represented by omission of `usage`. Do not infer variant/option from specialization descendants. Do not infer `abstract` from EA without an approved deterministic source rule.

BindingConnector precedence is: deterministic same-context `Connection.exposes` when a unique internal Connection and boundary Interface are proven; otherwise canonical symmetric `Interface.equals` for two resolved same-owner Interface occurrences; otherwise review-only evidence. Do not synthesize a Connection from BindingConnector evidence alone.

### Naming/path

The duplicate filename rule based on MDSE `id` is superseded.

Use `~2`, `~3` for duplicates; `~a`, `~b`, ... for forced name alterations; and combined forms such as `~a~2`. Apply the same convention to folders.

Normalize/shorten redundant folders by meaning only when that improves navigation. W-382 removes the importer-defined total path-length cap and mechanical folder-capacity subdivisions. Nested emitted elements use parent-element folders, and generated/imported filenames must remain globally unique case-insensitively across the vault namespace.

### Attachments and diagrams

A failed approved attachment write is non-blocking and explicitly reconciled as a failed attachment import.

Attachment acceptance (W-323): a decode-only run on the real `.qeax` must report PASS against `attachment_benchmark.json` (376 approved documents, 376 decoded OK, 390 attachment files, zero residual) before a full run is kept for attachments. The same summary line is written to the Run Manifest of every full run.

Initial diagram artifacts are deferred, but every source diagram must reconcile. Any unreconciled source diagram blocks acceptance.

### Evidence

The v0.8 evidence package uses Run Manifest, Ledger/terminal reconciliation, Local Model Source Map, naming/path reviews, semantic/connector reviews, attachment reconciliation and diagram reconciliation.

Do not emit the four legacy empty CSVs unless a unique future need is approved.
