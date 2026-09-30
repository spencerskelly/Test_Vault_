---
id: INFO-00023
uid: 20260930120336279skellyspencer
status: Draft
---
# Translator Definition

What the stage 1 translator must do, in one place. It is kept current: any decision that changes a stage 1 rule updates this file in the same commit (W-247). Rules are stated once and cite their decision number. The tables live in the YAML files in `99_System/03_Schemas`, which stay the machine-readable authority; this file says which file holds what and does not copy the tables, so there is one place to change. Where this file and a YAML file disagree, that is a fault to fix, not a choice.

Current through W-274.

## 1. Purpose and scope

- The translator reads Sparx EA and writes the MDSE vault. EA is being retired; the vault becomes the single source of engineering knowledge (handoff, W-01).
- Two stages (W-30). **Stage 1** is direct and mechanical: it applies only approved, deterministic rules, decides no meaning, and loses nothing. The EA type stays in `eaType` and stage 2 corrects it. **Stage 2** applies meaning (reclassification, folding, cleanup) as separate reviewed git commits. The work list for stage 2 is `Post-Import Tasks.md`.
- Every run goes into a fresh vault. It never imports over an existing vault (W-36, W-37). Only validated runs are committed (W-35).
- The fresh vault has MDSE Bootstrap and the plugins installed and enabled before the run (W-248). The translator does not install plugins (my reading of W-248). Once the tool works, that vault is set up for testing (W-248).
- Path to a testable vault (W-249): a script builds a base vault once from the workspace; the tool fills a copy of it and does not create the vault, the plugin settings or Bootstrap; the tool reads the person notes, `authors.yaml` and the templates from that base vault, not from the workspace. Each test run is a disposable copy, checked by section 10, opened in Obsidian and discarded. The tool takes a package filter (W-252): it opens the `.qeax` read-only, numbers every note from the whole model (W-14) and writes only the selected packages, so a slice keeps its final ids and its numbers have gaps. A full run is the same tool with no filter. Links that leave the slice are written as in a full run (W-253). A fold follows the note that receives it: an element that folds into a note outside the slice is not written in that run (W-254). Packages are selected by a list of package paths given at run time; each path includes every package below it, a path may name any package, and the tool rejects a path that matches no package or more than one (W-255). A path is written `Name > Name > Name`, with `>` as the separator and optional spaces around it; each name is matched against the EA package name after trimming leading and trailing spaces, with case kept; no escaping is needed (W-266). A path starts at one of the ten packages under `IPC !` (my reading of W-117, not confirmed). The first test slice is `02 Product Context` (W-267). Not decided: what the ledger holds for a slice beyond the outcome `outside slice` (W-254).
- The result must be usable by people and AI together. Every review line must be resolvable from the vault alone (W-156). The vault is not released until stage 2 is complete (W-55).
- Stage 1 output is a vault, a ledger, a run manifest and review tables (section 3).

## 2. Input

- **The import reads the `.qeax` file directly** (W-247). The CSV files in `99_System/CSV_EA` were used to define the rules; they are not an input to the import. Reading the source file avoids a translation error in an extraction step.
- The CSV files are an evidence bundle that an earlier tool build (2.6.0) extracted from `EA_2026_09_06_endgame.qeax`. They keep EA's table and column names, and the rules cite those names (`t_object.Object_Type`, `t_connector.Connector_Type`). The rules apply to the same tables in the `.qeax`.
- Tables the import uses, with the rule file that decides each field: `t_object` and `t_package` (elements and packages), `t_connector` (connectors), `t_objectproperties` (tags, including the `Notes` column, which only the `t_objectproperties_raw.csv` extract kept as a separate file), `t_xref` (relationship kinds such as `conveyed`, `trigger`, `entry`, `doActivity`, `represents`, `target`), `t_operation` (State actions, W-86), `t_attribute` (Class attributes, W-86, W-108), `t_diagram`, `t_diagramobjects`, `t_diagramlinks` (diagrams), `t_document` (linked documents as attachments).
- **Base vault contents (W-250).** The tool fills a copy of a base vault. For now the base vault is passed as a ZIP built from the workspace (W-270); a build script is not written. The base vault has: `.obsidian` without `workspace.json`, plugin `data.json` and `author-code.txt`; `.gitignore`, `.gitattributes`, `AGENTS.md`; `Definitions`; in `99_System`: `02_AI`, `04_People`, `05_Templates`, `08_Scripts`, `09_Tools`, the `Enabled Plugin Stack` note, the Bootstrap spec and Ruleset 1.22; in `03_Schemas` only `authors.yaml`, `element-types.yaml` and `relationships.yaml`. It does not have `CSV_EA`, `99_System/archive`, the Decision Log, the handoff, this file, the mapping and disposition YAML files (tool inputs), the import outputs, `MDSE Workbench`, the README or the cross-vault files. `.vault.yaml` is not copied from the workspace: a build script would write a fresh one with a new `vault_uid` and a name given at build time (W-269); in the ZIP it ships as `UNINITIALIZED` and is initialized after unzipping (W-270).
- Every field and every table has a disposition (`property`, `body`, `structure`, `archive` or `drop`, W-33): `ea-field-dispositions.yaml`. Empty tables are dropped (W-74). `t_connectortag` is dropped, since it holds five names and no values (W-85). Tags: `ea-tag-dispositions.yaml` (121 decided: 80 drop, 38 body, 3 structure).
- **Source counts for check 5 (W-257).** Rows in the CSV bundle's `extract_manifest.json`: `t_object` 35,969 (of these 1,386 are Packages), `t_connector` 21,822, `t_package` 1,387 (the root `Model` has no `t_object` row), `t_diagram` 2,924, `t_diagramobjects` 42,966, `t_diagramlinks` 37,955, `t_objectproperties` 249,892, `t_xref` 42,052, `t_document` 397, `t_operation` 23, `t_attribute` 5. Diagrams by EA diagram type (`diagram_type_summary.csv`): Custom 1,230, Logical 1,038, Use Case 267, CompositeStructure 151, Statechart 109, Activity 95, Sequence 24, Package 10. Counts by EA object type and connector type are in sections 5 and 6. The tool reads these counts from the `.qeax` and writes them to the run manifest beside the expected ones.
- The counts in this file originated in the CSV evidence bundle and were verified directly against `EA_2026_09_06_endgame.qeax` by native importer v0.1 (W-273): all 11 translator-used table counts, all 31 EA object-type counts, all 15 connector-type counts and all 8 diagram-type counts match exactly. The tool still compares every run against this baseline and fails on any difference (W-268). The 254–255-character question is also closed: `User Story`, `Product Management Comment`, `Sales Comment` and `Engineering Comment` already stop at that boundary in the QEAX itself and have no continuation in tagged-value Notes. Stage 1 preserves those values exactly, never reconstructs missing text, and reports the condition only as a source-data advisory (W-273).

## 3. Output

All in `99_System/11_Import`, regenerated on every run, read-only evidence (W-35, W-215, W-216).

- `Ledger.csv`: one row per element, connector, diagram and package, sorted by EA GUID. Columns `ea_guid, source_kind, ea_type, ea_name, outcome, rule, uid, id, folded_into_uid`. `outcome` is `note`, `folded`, `link`, `canvas` or `not carried`, and in a slice run only also `outside slice` (W-254); `rule` is the decision number.
- `Run Manifest.md`: date, tool version, input identity (file name and size), the source counts read from the `.qeax` beside the expected ones (W-257) and counts by outcome; for a slice run, also the links that leave the slice (W-253).
- Four review tables, each starting `ea_guid, ea_type, ea_name, category`, with no status column (decisions go in `Review Changes Log.md` by the same GUID, W-38): `Review - Block-Level Flow Connectors.csv` (W-217), `Review - Added Ports.csv` (W-218), `Review - Nesting Direction.csv` (W-219), `Review - Equals Direction.csv` (W-220).
- Not decided: what happens to the four header-only files `Identity Registry.csv`, `Model Checks.csv`, `Pending Relationships.csv` and `Transformation Log.csv` (W-215).

## 4. Notes

- **Classes:** 24, in `element-types.yaml` (schemaVersion 1.16): Object OBJ, Port PORT, Item Flow IFLOW, Function FUNC, Functional Flow FFLOW, State STATE, State Machine SM, Requirement REQ, Design DES, Use Case UC, Actor ACT, Failure Mode FM, Issue ISS, Info INFO, Step STEP, Verification VER, Procedure PROC, Setup SETUP, Plan PLAN, Result RES, Document DOC, Artifact ART, modelCheck MC, Diagram DIA. Context and Transition do not exist (W-237). Only Port, Item Flow, Requirement, Object, Use Case, Issue, Verification, Procedure, Diagram and modelCheck have subtypes; Function, Design, Info, Document and Artifact have none (W-237, W-238). Port subtypes are `proxy` and `full`.
- **Notes in `99_System`** carry no `type` or `subtype` and are not model elements (W-243). The translator makes none of them.
- **Properties, in order:** `type`, `subtype`, `id`, `uid`, `status`, `eaType`, `tags`, then the relationship fields in the order of `relationships.yaml` (W-97, W-126). `eaType` is the EA stereotype, else the EA object type (W-31); it is temporary. EA's own status, version, phase, complexity, effort and dates other than creation are dropped (W-39).
- **uid:** 17-digit local-time stamp plus a 13-character author code (W-13). Translated notes use the EA creation time and author (W-09). The code is last name plus first name, accents removed, cut to 13 and padded with hyphens (W-10, W-24). An EA author that is blank or not usable is `sparxeaauthor` (W-12, `authors.yaml`).
- **id:** class prefix, hyphen, five digits, numbered per prefix in EA creation order with ties by EA GUID, no gaps, permanent once final (W-14, W-15, W-18). Always internal (W-203): Requirement subtype `standard` takes `STD-#####` (10,918 notes), subtype `stakeholder` takes `STK-#####` (1,744), other Requirements `REQ-#####`. No designator is parsed. A note reclassified in stage 2 is renumbered and keeps its earlier id in `## Former ids` (W-181, W-207).
- **File names:** the EA name with the replacements in `Definitions/Note Layout.md` ("File names", W-196, W-197, W-205). A name that clashes vault-wide, case ignored, takes the `id` as a suffix on every note in the group (W-198, W-199). Ports, pins and unnamed elements have their own counters (W-134, W-138, W-145). When the file name differs from the EA name, a `Name:` line keeps the original (W-48).
- **Body:** the order is in `Definitions/Note Layout.md` (Note, `text` wording, comment texts, `**EA notes:**`, empty `## Notes`, `## Aliases` and `## Former ids` when needed, multi-line Priority, then `Source: EA`). The `Source: EA` section is in `Definitions/EA Source Section.md`: `EA GUID` first, everything else from EA below it, placeholders and empty values never written.

## 5. Elements

Every EA element has exactly one rule (W-148); the input is `eaType`. The rules are in `ea-element-mapping.yaml` (31 EA object types). Counts are from the CSV bundle.

| EA element | Becomes | Decision |
|---|---|---|
| Requirement 13,988 | Requirement. Subtype from the EA package path: standard, engineering (the Engineering Requirements folder), design, functional, stakeholder. Every requirement is its own note; folding is stage 2 | W-115, W-116, W-81 |
| InformationItem 2,825 | Requirement/standard (2,383, in the Regulatory Requirements folder) or Info (442, blank subtype) | W-115, W-145 |
| Port 4,387 | Port. Instance Ports of Parts and Objects merge into the block's Port by a one-hop rule (`PDATA3`, else exact name, else added, else stays); 2,589 Port notes; subtype `proxy`, `full` or blank from the stereotype | W-114, W-128 |
| Class 2,737 | Port (423 interface Classes, blank subtype, stereotype in `eaType`) or Object (2,314, blank subtype). A Physical Context stays an Object with its parts | W-120, W-139, W-237, W-239 |
| Part 3,137 | Item Flow (760 FlowProperty pins); folded into the assembly as `hasPart` (2,055 typed by a Class); folded into the owner as `hasChild` (219); Object, subtype `part` (103 with no block) | W-132, W-136, W-137, W-138, W-149 |
| Object 545 | Object, blank subtype; `Classifier` is a temporary `hasClassifier` link | W-135, W-180 |
| Signal 623 | Item Flow, blank subtype | W-131 |
| Activity 1,668 | Function (blank subtype, 1,141) or Verification, subtype `test` (527, stereotype `testCase`) | W-141, W-238 |
| UseCase 1,667 | Use Case; subtype from the folder (what, when, where, who), else blank | W-140 |
| State 1,112 | Design (954, under `05 Product Design`) or State (158); blank subtypes | W-142, W-237 |
| Artifact 459 | Artifact, blank subtype | W-143, W-237 |
| Issue 264, Actor 44, StateMachine 2 | Issue, Actor, State Machine; blank subtypes | W-144 |
| Note 431, Text 61, Constraint 1 | Info, blank subtype, except a Note linked to one unique element folds into that element's body. The accepted v0.2 plan folds 247 unique Note elements through 250 NoteLink connector rows; 184 Notes remain Info | W-145, W-161, W-274 |
| 13 small types, 632 (Action 323, StateNode 73, Change 65, Boundary 44, Decision 34, ActivityPartition 28, Trigger 27, Synchronization 14, Sequence 11, ActionPin 6, ProxyConnector 5, Event 1, ActivityParameter 1) | modelCheck, subtype = the EA type, `MC-#####` | W-146, W-181 |
| Package 1,386 | A folder; a modelCheck note, subtype `Package`, only for the 34 with a Notes description | W-147 |

The accepted v0.2 whole-model plan produces 30,298 element-derived MDSE entities, including 34 package notes; 2,924 diagram companion notes are separate (W-274). The difference from the earlier W-161 count is a bookkeeping correction: 250 folded NoteLink connector rows represent 247 unique Note elements.

## 6. Connectors

Every connector has exactly one rule (W-178); 9 have an end missing from the export and write nothing (W-57). The rules are in `ea-connector-mapping.yaml` (15 connector types, W-151 to W-179). `Direction` decides which end is the source (W-51). Part ends resolve to their block, Port ends to the merged Port (W-114, W-155). Forward fields are written on the owner side; inverses are generated (`relationships.yaml`, 63 fields).

| EA connector | Becomes | Decision |
|---|---|---|
| Nesting 836 | Nothing where it repeats placement (584); the other 252 `hasChild` with `REVIEW nesting direction: connector {GUID}` | W-151, W-152 |
| Generalization 3,974 | `subtypeOf`; mixed types flagged | W-152 |
| Connector 823 | `interfaces`; BindingConnector a temporary `equals`; one link per pair; block-level ends `REVIEW port needed` | W-153 to W-158 |
| Aggregation 2,288 | Composite Object pairs `hasPart`, all else `hasChild`; an existing link wins | W-159 |
| Realisation 950 | A requirement `appliesTo` an Object; Function realizes Use Case; else `realizedBy` flagged | W-160, W-167 |
| NoteLink 349 | A note on one element folds into its body under `**EA notes:**`; a note on several stays Info with `describes` | W-161, W-162 |
| Dependency 6,762 | By stereotype: `satisfy` (`satisfies`), `deriveReqt` (`derivedFrom`), `refine` (`refines`, `drives`, `describes`), `trace` (`describes`, `affects`, `appliesTo`, `references`), `verify` (`verifies`); none: `dependsOn`; off-pattern flagged | W-163 to W-169 |
| Abstraction 2,811 | `allocate`: an Object `performs` a Function and has a Design (`hasDesign`); else earlier rules or `tracesTo` flagged | W-170 |
| UseCase 1,258 | `extend` is `optionOf`; `include` is `hasChild` | W-171 |
| Association 603 | One-way `participants` on the Use Case; else earlier rules or `tracesTo` flagged | W-172 |
| Usage 239 | A Function or Design realizes a Use Case; requirements `dependsOn` requirements | W-173 |
| ControlFlow 407, StateFlow 200 | `precedes`; Guard, Trigger and Effect as lines on the step before | W-174, W-175 |
| Sequence 199 | An ordered message list on the diagram companion note, no field | W-176 |
| InformationFlow 123 | `interfaces`, plus `transmits` and `receives` pointing at the conveyed Item Flow; a Port that does both `exchanges` | W-177, W-178 |

An off-pattern pair keeps the EA meaning and gets `REVIEW modelCheck: <stereotype> <source type> to <target type>` (W-160 onward). Connector names use `- Connector name: <name> (to [[other end]])` (W-158). Where a placement child is `subtypeOf` its owner, no placement link is written (W-178). A Function or a Design satisfies a requirement; a requirement applies to an Object (W-160).

## 7. Fields, tags, packages

- **Dispositions:** every EA field, tag, small table and `t_xref` kind has one (section 2). Values kept are the tag lines, the comment texts and the structure lines defined in `Definitions/EA Source Section.md` (W-93, W-101, W-102, W-104 to W-106, W-209).
- **Packages:** the vault tree starts at the ten packages under `IPC !`; `Model` and `IPC !` are not folders (W-117, `ea-package-rules.yaml`). Package names follow the file-name rules. A package without a Notes description is only a folder.
- **Relationship fields in templates:** `Port` `subtypeOf`, `interfaces`; `Item Flow` `subtypeOf`; `Use Case` `participants`; `Function` and `Design` `subtypeOf`, `satisfies`; `Verification` `verifies`; `Info` and `Artifact` `describes`; `Issue` and `Failure Mode` `affects`; `State Machine` `hasChild`; all other classes none (W-222 to W-241). The translator writes fields from the connector rules, not from the templates.

## 8. Diagrams and attachments

- A diagram is a canvas file plus a companion note (W-73). The companion note is class `Diagram`, `DIA-#####`, subtype the EA diagram type (custom, logical, use case, composite structure, statechart, activity, sequence, package; W-212). It carries `Canvas: [[...canvas]]` when the canvas exists (W-213). A folded EA note drawn on a diagram becomes a canvas text card holding its text (W-214). A sequence diagram has no canvas; its companion note lists the messages (W-176).
- An element with a default diagram gets a `Default diagram: [[...]]` line, written only when the canvas exists (W-80). A diagrams-only run may add diagrams to an existing vault, additive and through the ledger (W-62).
- Linked documents in `t_document` become files next to the note, named `<note file name> asset <n>`, the counter from 1 on every note, in the order of the pictures in the source RTF (W-76 to W-78, W-210). Not checked: that the byte order of pictures in an RTF matches the page order.

## 9. Review lines and modelCheck

- modelCheck (`MC`) holds unmapped EA elements; the subtype is the EA type; nothing is lost (W-100, W-146, W-181).
- Review lines are written on the notes and in the review tables (section 3). The kinds: `REVIEW port needed`, `REVIEW nesting direction`, `REVIEW modelCheck: ...`. Each is resolvable from the vault alone (W-156).

## 10. Checks the tool must pass before a run is kept

1. Every element, connector, diagram and package lands in exactly one outcome and one rule; the ledger has one row each (W-148, W-178, W-215).
2. No two notes share an `id`, a `uid` or a file name.
3. Every `[[link]]` the tool writes resolves to a note or an attachment in the run. In a slice run, a link to a note outside the slice is accepted when its target is in the model; the run manifest lists those links (W-253).
4. Every YAML and JSON file in the vault parses; every relationship field written is in `relationships.yaml`.
5. The source counts the tool read from the whole `.qeax` match the counts in this file exactly: the table rows listed in section 2, the elements by EA object type (section 5), the connectors by EA connector type (section 6) and the diagrams by EA diagram type (section 2). Any difference fails the check and the run is discarded; the manifest lists the differences, a person updates the counts in this file from it, and the run is repeated. This applies to every run, full or slice (W-257, W-268).
6. A run that fails any check is discarded, not committed (W-35).

Checks 1 and 6 follow earlier decisions; checks 2 to 5 are approved (W-256). Check 5 compares whole-model source counts, so it holds for a slice run too (W-257).

## 11. What stage 1 does not do

Reclassify `modelCheck` notes, split Object, Design or State by `eaType`, fold requirements, resolve `hasClassifier` and `equals`, move block-level flow connectors to ports, or decide any meaning. These are stage 2: `Post-Import Tasks.md` (W-30).

## 12. Open, not yet a rule

Implementation status (W-271, W-273, W-274): the native tool is a developer-only local HTML application. v0.1 established the read-only direct-QEAX preflight. `99_System/09_Tools/EA_to_MDSE_Native_Importer_v0.2.html` keeps that preflight, fixes recognition of single-quoted EA SQLite column names, treats the verified 255-character source loss as advisory, and adds a read-only whole-model Stage-1 translation planner. Spencer ran v0.2 on the actual QEAX and the whole-model plan passed in 1,948 ms with no failures or warnings (W-274). It classified 35,969 elements, 21,822 connectors, 1,387 packages, 2,924 diagrams and 42,052 xrefs, producing 30,298 element-derived MDSE entities plus 2,924 diagram companion notes. v0.2 is now the accepted planning baseline and is not modified after that acceptance run; it still writes no MDSE notes. Its only informational finding is the 27 multi-source W-114 added-Port groups for which the canonical source identity is not yet decided. Settle that identity rule before final whole-model uid/id assignment, then add the `02 Product Context` note-producing slice.

The Open list at the end of `Workspace Decision Log.md` is the list. Relevant here: the package filter (the ledger for a slice; W-252, W-254), the four header-only import files, the canonical source identity for the 27 W-114 added-Port groups with several source Ports (W-273, W-274), the remaining unexplained audit-count differences that are not source-baseline counts, the W-272 relationship endpoint-rule format, and whether third-party standards content may stay in the vault.
