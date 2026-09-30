---
uid: 20260928123124000skellyspencer
id: INFO-00020
type: Info
subtype: Guide
status: Active
---
# Handoff: Continue Here

Rewritten 2026-09-29 (W-183), updated through W-226 for a new AI chat continuing the work on this vault. Read this note first, then the Workspace Decision Log.

## What this vault is

`Test_Vault_` is a workspace, not the vault that will be built. It defines the EA-to-Obsidian (MDSE) translator and the conventions the real vault will follow. The real vault will be generated later by the translator, will hold only engineering notes plus a few definitions and diagrams, and will not contain the raw EA export or the methodology notes. EA is being retired, and the vault becomes the single source of engineering knowledge. The goal of the translation is a direct, mechanical stage 1 that loses nothing, so refinements can follow in stage 2 (W-30). The result must be usable by people and AI together.

## Read in this order

1. `99_System/10_Docs/Workspace Decision Log.md`: every decision (W-01 to W-226) and the Open list at the bottom. It is the authority for what has been decided.
2. `Definitions/Note Layout.md` and `Definitions/EA Source Section.md`.
3. `99_System/03_Schemas/`: `ea-element-mapping.yaml` (all 31 EA object types), `ea-connector-mapping.yaml` (all 15 connector types, W-151 to W-179), `relationships.yaml` (schemaVersion 1.23), `element-types.yaml` (26 classes, `Diagram` added in W-212), `ea-field-dispositions.yaml`, `ea-tag-dispositions.yaml`, `ea-package-rules.yaml`.
4. `99_System/10_Docs/Post-Import Tasks.md` (Tasks 1 to 8; Task 7 has 12 items).
5. `99_System/02_AI/AI_INSTRUCTIONS.md` and `MDSE Modeling Ruleset 1.21` (its section 3 is out of date, see the Open list).
6. The EA export is in `99_System/CSV_EA` (`t_objectproperties_raw.csv` is the tag source, because only it has the Notes column; `t_xref.csv` holds the `conveyed`, `trigger` and other relationship rows). The `.qeax` and the translator source (v2.6.0) are not in the repository; ask for `EA_to_MDSE_Consolidated_v2_6_0.zip` if the earlier tool's rules are needed. The r12 relationship matrix notes in `99_System/10_EA Native Translator` are evidence only; the connector mapping replaces them.

## How to work with Spencer

- One topic at a time, and one question per turn. End each turn with a single question. When he asks, walk him through it plainly ("like I'm 12").
- Give a recommendation with the reason. Say about any problem it creates before going on. Use numbers from the data, and say plainly what you are unsure of or could not check. Correct your own figures in the open when they turn out wrong. When you read his answer one way and apply it, say it is your reading.
- Show a real example from the export when a rule is hard to picture; he often asks for one.
- Short and direct, no praise. Tell him if there is a more efficient way to work.
- Nothing is applied until he approves it. If you apply consequences of an approved decision, say so and list them.
- Log every decision as the next W number (next is W-222) in the Decision Log, update the worklist YAML and this handoff, then commit and push to `main`. He allows pushing to `main` and pulls each change into Obsidian.
- Commit only when every edit applied and every YAML and JSON file parses. Make each scripted edit fail on an anchor that matches zero or several times, and stop the commit if any edit failed (twice in the last chat a commit went out missing an edit; once an anchor matched Task 5 instead of Task 7). Quote long YAML text values (a colon followed by a space has broken a file twice). Use quoted heredocs (`<<'EOF'`). Check that a referenced source file or column exists before relying on it. Stay with EA names until after the import (W-93).
- Never write an access token into a file. After cloning, reset the remote URL to the token-free form and push with the token in the command only. Set a repo-local git identity before the first commit. Check `git log` for commits you did not make before adding a decision number.

## Decisions in one place

- **Vault:** one vault, no cross-vault links (W-01). Old scaffolding removed, `99_System` kept (W-04). Plugins and the Obsidian Git exception (W-05).
- **Names:** MDSE things are `Object`; notes use `type` and `subtype` (W-02). `eaType` is a temporary property holding the EA stereotype, else the EA object type (W-31).
- **uid:** 17-digit local-time stamp plus a 13-character author code (W-13). Code is last name plus first name, accents removed, cut to 13, padded with hyphens (W-10, W-24). Translated notes use the EA creation time and author (W-09). Unknown EA authors are `sparxeaauthor` (W-12). AI codes are tool name, `ai`, hyphens (W-22); the AI's code is used only when no user directed the note (W-21). People are one note each in `99_System/04_People` (W-25).
- **id:** class prefix plus five digits, never reused, and notes are retired, not deleted (W-15, W-18). It is either an internal id or an external document-plus-section id such as `UL2594_13.1`, with `STD-` and `STK-` as fallbacks (W-17, W-27). Translated notes are numbered in EA creation order (W-14).
- **Templates and definitions:** templates serve hand-made and translated notes; Templater snippets fill `uid` and `id` (W-06, W-20). Every property gets a definition note in `Definitions/Properties` (W-08, W-19).
- **EA traceability:** the `EA GUID` line is first in a `Source: EA` section at the bottom of a translated note, and everything else kept from EA goes below it (W-03, W-28). The layout is described in `Definitions/EA Source Section.md`.
- **External documents:** one note per document edition with clause anchors; unconnected clauses fold into it (W-16).
- **Tags:** all 121 are decided (W-29 to W-95): 80 dropped, 38 body (36 tag lines under their EA tag names, and `text` and `SysML1.4::text` as normal text, W-102), 3 structure (W-93, W-102). Sequence-style EA `id` values are dropped (W-26). The `Stakeholder ID` tag holds clause numbers. When unsure, keep the value in the body and decide in the cleanup (W-27).
- **Default diagram line:** an element with a default diagram gets a marked `Default diagram: [[...]]` line, written only when the canvas is created, including by a diagrams-only run (W-80). **Requirements:** every one is imported as a note, folding is stage 2 (W-81).
- **Diagrams-only merge:** a new tool mode may add selected diagram types into an existing vault, additive only and through the accepted ledger (W-62). A diagram is a canvas file plus a companion note (W-73).
- **Import process:** two stages (W-30). Run into a fresh vault, review, then accept it or start fresh with better rules; never import over an existing vault (W-36, W-37). Review changes are the git diff against the baseline plus reasons in `99_System/10_Docs/Review Changes Log.md` (W-38). The source reference is a ledger keyed by EA GUID plus a run manifest, with no copied values (W-35).
- **Connectors and release:** connectors are imported where they were drawn; the 118 flow connectors attached to a block instead of a port are flagged `REVIEW port needed` and fixed in stage 2 (W-55). The vault is not released until stage 2 is complete. Tasks: `99_System/10_Docs/Post-Import Tasks.md`.
- **Field dispositions:** every field ends as `property`, `body`, `structure`, `archive` or `drop` (W-33). Element admin fields are settled (W-39), and so are the 21 empty element fields (W-40).

## Element mapping (W-113 to W-149, W-180, W-181): where it stands

All 35,969 EA elements have a rule, and a dry run applied every rule and passed (W-148): each row lands in exactly one outcome, none is unmapped. 30,545 notes result. The input is `eaType` (stereotype, else EA object type; 72 values).

| EA element | Becomes | Notes |
|---|---|---|
| Requirement (13,988) | Requirement | Subtype from the EA package path: standard, engineering (Engineering Requirements folder, all 2,469), design, functional, stakeholder (W-115, W-116). Every requirement is its own note; folding is stage 2 (W-81, Task 4). |
| InformationItem (2,825) | Requirement/standard (2,383 in the Regulatory Requirements folder) or Info (442) | W-115, W-145 |
| Port (4,387) | Port | Instance Ports of Parts and Objects merge into the block's Port by a one-hop rule (W-114): `PDATA3`, else exact name, else added, else stays. 2,589 Port notes. Subtype `proxy`, `full` or blank (W-128). |
| Class (2,737) | Port (423 interface Classes, subtype = the stereotype, W-120) or Object (2,314, blank subtype, W-139) | Physical Context and System Partner are not split out |
| Part (3,137) | Item Flow (760 FlowProperty pins, W-132), folded into the assembly as `hasPart` (2,055 typed by a Class, W-136), folded into the owner as `hasChild` (219, W-137, W-149), Object/`part` (103 with no block, W-138) | Role names, quantities and tags of a folded Part are kept as a source-section line |
| Object (545) | Object | `Classifier` is a temporary `hasClassifier` link (W-135) |
| Signal (623) | Item Flow | Blank subtype (W-131) |
| Activity (1,668) | Function (Function stereotypes to their subtype, no stereotype blank) or Verification/test (`testCase`) | W-141 |
| UseCase (1,667) | Use Case | Subtype from the folder: what, when, where, who (`who` was added), else blank (W-140) |
| State (1,112) | Design (954, in `05 Product Design`) or State (158) | Blank subtypes (W-142) |
| Artifact (459) | Artifact | document, image, or blank (W-143) |
| Issue 264, Actor 44, StateMachine 2 | Issue, Actor, State Machine | W-144 |
| Note 431, Text 61, Constraint 1 | Info | Blank subtype (W-145) |
| 13 small types (632): Action, StateNode, Change, Boundary, Decision, ActivityPartition, Trigger, Synchronization, Sequence, ActionPin, ProxyConnector, Event, ActivityParameter | `modelCheck`, subtype = the EA type | W-146 (amends W-100) |
| Package (1,386) | A folder; a `modelCheck`/`Package` note only for the 34 with a description | W-147 |

Other rules from this work: the `Interface` class is gone and `Port` replaced it (W-113). Folders start at the ten packages under `IPC !` (W-117). `hasPart`/`partOf` is for Object-to-Object only, and a permanent generic `hasChild`/`childOf` (written on the owner) carries every other `ParentID` nesting, about 19,600 links once the 781 that repeat a generalization are left out (W-149, W-178). Relationship fields follow `tags` in the properties and may hold lists (W-126). Stored link pairs added: `hasPort`/`portOf` (W-123), `copyOf`/`hasCopy` (W-124), `hasFlow`/`flowOf` (W-133), `hasChild`/`childOf` (W-149); temporary pair `hasClassifier`/`classifierOf` (W-125, W-127, W-135), resolved in stage 2 (Task 7). Differences on a merged Port are kept as lines on the block Port (W-121); four fixed `REVIEW` lines mark Port cases for review (W-130, Task 6), and a fifth marks the 252 nesting directions and a sixth the 88 mixed-type Generalization links (W-151, W-152, Task 7); `isConjugated` is a source-section line (W-129). Names: a Port note is `<owner> - <name>` and a pin note `<Port note> - <pin name>` (W-134); an unnamed element is its lowercase EA type and a counter, `note 1`, `part 1` (W-138, W-145). Nesting (W-151): the 836 drawn `Nesting` connectors add no notes; 584 repeat a `ParentID` link, and the 252 independent ones are written as `hasChild`/`childOf` with a `REVIEW nesting direction` line (checked in stage 2, Task 7) and the connector GUID inside each review line (W-152). Requirement nesting is bidirectional through W-149: every child carries `childOf`, every owner `hasChild`, Artifact notes included. Everything is mechanical on purpose: the EA type stays in `eaType` and stage 2 corrects it (Task 7).

Since W-150: `Classifier`, `Classifier_guid` and `PDATA1` are settled for every element type (W-180); `modelCheck` is a class with prefix `MC`, no folder, 14 subtypes (the 13 EA types and `Package`) and a plain template (W-181); a note reclassified in stage 2 is renumbered and keeps its `MC` id in `formerIds`. A NoteLink changes the Info count: an EA Note linked to one element folds into that element's body (250), so Info notes from Note, Text and Constraint are 243 and all notes about 30,295 (W-161). FlowProperty pin direction is now a field on the owning Port (W-177, below).

## Connector mapping (W-151 to W-179): where it stands

All 21,822 connectors have a rule, and a rebuild of the export with every rule puts each in exactly one (W-178); 9 have an end missing from the export and write nothing (W-57). The rules are in `ea-connector-mapping.yaml`. Part ends resolve to their block, Port ends to the merged Port (W-114, W-155); `Direction` decides which end is the source (W-51).

| EA connector | Becomes |
|---|---|
| Nesting 836 | Nothing where it repeats placement (584); the other 252 `hasChild`, each with `REVIEW nesting direction: connector {GUID}` (W-151, W-152) |
| Generalization 3,974 | `subtypeOf`; mixed types flagged (W-152) |
| Connector 823 | `interfaces`; BindingConnector a temporary `equals` (Task 8 turns it into a directional pair); one link per pair; block-level ends `REVIEW port needed: ... connector {GUID}` (W-153 to W-158) |
| Aggregation 2,288 | Composite Object pairs `hasPart`, everything else `hasChild`; an existing link wins (W-159) |
| Realisation 950 | A requirement `appliesTo` an Object (either direction); Function realizes Use Case; else `realizedBy` flagged (W-160, W-167) |
| NoteLink 349 | A note on one element folds into its body under `**EA notes:**` with date and author; a note on several stays Info with `describes` (W-161, W-162) |
| Dependency 6,762 | `satisfy`: a Function or Design `satisfies`; `deriveReqt`: `derivedFrom`; `refine`: `refines`, a Use Case `drives`, Info `describes`; `trace`: `describes`, `affects`, `appliesTo`, requirements `references`; `verify`: `verifies`; no stereotype: Functions `dependsOn`; off-pattern pairs flagged (W-163 to W-169) |
| Abstraction 2,811 | `allocate`: an Object `performs` a Function and `hasDesign` a Design; else earlier rules or `tracesTo` flagged (W-170) |
| UseCase 1,258 | `extend` `optionOf`; `include` `hasChild` (W-171) |
| Association 603 | One-way `participants` on the Use Case; else earlier rules or `tracesTo` flagged (W-172) |
| Usage 239 | A Function or Design realizes a Use Case; requirements `dependsOn` requirements (W-173) |
| ControlFlow 407, StateFlow 200 | `precedes`/`follows`, with Guard, Trigger and Effect lines on the step before (W-174, W-175) |
| Sequence 199 | An ordered message list on the diagram companion note, no field (W-176) |
| InformationFlow 123 | `interfaces`, plus `transmits`/`receives` pointing at the conveyed Item Flow; a Port that does both `exchanges` (W-177, W-178) |

Principles that came out of this: only a Function or a Design satisfies a requirement; a requirement applies to an Object (W-160). Off-pattern pairs keep the EA meaning and get `REVIEW modelCheck: <stereotype> <source type> to <target type>` (W-160 onward). Every review line must be resolvable from the vault alone, with a review table in `99_System/11_Import` keyed by GUID where the notes cannot hold the evidence (W-156, W-157). Connector names use `- Connector name: <name> (to [[other end]])` (W-158). Where a placement child is `subtypeOf` its owner, no placement link is written (W-178). New fields since W-150: `interfaces`, `equals` (symmetric), `refines`/`refinedBy`, `drives`/`drivenBy`, `references`/`referencedBy`, `precedes`/`follows`, and one-way `participants`, `transmits`, `receives`, `exchanges`. Long generated lists (`applies` up to 133 on one Object) are judged after the import (W-179, Task 7 item 12). Flow elements (Actions, Decisions and the rest) stay `modelCheck` notes because most will be deleted and ids are never reused (W-174).

**Relationship review finished (W-184 to W-192).** 54 fields were removed in seven groups (117 before, 63 after), `supersedes`/`supersededBy` was defined and `conflictsWith` kept. `relationships.yaml` (schemaVersion 1.23) now has 63 fields: 25 paired pairs, 1 temporary pair, 3 symmetric and 8 one-way; `types.json` has 88 properties.

## Next steps, in Spencer's order (W-193: the blockers to the import first, the templates after them)

1. **Done (W-194):** the 4 unmapped `t_xref` kinds (12 rows) are body lines on both ends. No merge with the W-86 `t_operation` State lines (W-195): both are written as defined. Inverse wording still unconfirmed.
2. **Naming:** unsafe means only what the system rejects (W-196: `\ / : * ? " < > |`, control characters, trailing space or period); replacement rules settled (W-197, in `Definitions/Note Layout.md`); every note in a duplicate-name group takes the `id` as suffix (W-198, W-199); standards take `STD-#####` and stakeholder requirements `STK-#####`, with no designator parsing (W-203, W-204, replacing W-201 and W-202); `[ ] # ^` are also replaced (W-205); diagram duplicates take the `DIA` id (W-212).
3. **Layout gaps:** done: user section (W-206), aliases and `formerIds` format (W-207), order of the `Source: EA` lines (W-208), definitions of kept body lines (W-209). All done: attachment counter (W-210), merged Port lines (W-211). The connector context of W-114 was dropped in W-155; nothing is open on it.
4. **Diagrams:** companion note class `Diagram`, prefix `DIA` (W-212); body: a `Canvas:` link line after the Note (W-213); canvas text card for a folded note holds its text (W-214). Item 4 is done.
5. **Review tables and ledger:** review table names are final, read-only, and start with `ea_guid, ea_type, ea_name, category` (W-216); the Block-Level Flow Connectors (W-217) Added Ports (W-218), Nesting Direction (W-219) and Equals Direction (W-220) tables are set. Item 5 is done; the ledger and run manifest are settled (W-215: `Ledger.csv` and `Run Manifest.md` in `99_System/11_Import`).
6. **Templates.** Spencer chose to list only the few relationship fields each class nearly always has (W-182). The proposed list waits for his approval, one class at a time; Requirement (W-222) and Object (W-223) are decided: none; Port (W-224): `subtypeOf`, `interfaces`, written in `Port.md`; Item Flow (W-225): `subtypeOf`, written in `Item Flow.md`; Use Case (W-226): `participants`, written in `Use Case.md`. Next class to ask: Function, then the others one at a time. Proposed list as first written (Requirement none, W-222; Object none, W-223; Port as listed, W-224; Item Flow as listed, W-225; Use Case `participants` only, W-226): Requirement `derivedFrom`, `appliesTo`; Object `subtypeOf`, `hasPart`, `hasPort`; Port `interfaces`, `subtypeOf`; Item Flow `subtypeOf`; Use Case `participants`, `drives`, `optionOf`; Function `satisfies`, `subtypeOf`, `precedes`; Design `satisfies`, `subtypeOf`; Verification `verifies`; Info and Artifact `describes`; Issue `affects`; State `precedes`; Actor `subtypeOf`; State Machine `hasChild`; Transition `source`, `target`, `trigger`; Context `participants`; Failure Mode `affects`; none for Plan, Result, Step, Procedure, Setup, Document, Functional Flow and modelCheck; `hasChild` on none (it comes from placement). Then: `Port.md` defaults to `electrical & material` (translated Ports are `proxy`, `full` or blank); subtype variants only where fields or sections differ; the legacy `folder` values in `element-types.yaml` (W-04); the Person template's list properties.
7. **Schema and docs left out of date:** `Ruleset 1.21` section 3, the translator (v2.6.0), the `Definitions/Properties` notes for the relationship fields (only `uid`, `id` and `eaType` exist), `MDSE Element - Interface.md` and its canvas, the 18 unused properties in `types.json`, and whether `hasFlow` stays next to the pin direction fields (W-177).

## Layout and sweep (W-107, W-108)

The note layout is written in `Definitions/Note Layout.md`; `Definitions/EA Source Section.md` describes the last section. A sweep of all fields, tags and export files found no missing field. `Object Type` (both), `Origin` and `In-Links` stay `drop` (W-109).

## Not yet verified or still open

- Values of `User Story` (25 of 118), `Product Management Comment` (20 of 37) and three others stop at 254 to 255 characters; not known whether EA or the export cuts them (needs the `.qeax`).
- The handoff's 10,052 unconnected requirements against 9,788 from the audit file (W-81); W-26's count of 79 shared clauses could not be reproduced; `SubType` "Weak" (27 rows) and the 6 `t_operation` Behaviour values.
- The Templater snippets pass mock tests but have not been run in Obsidian. The core Templates plugin should be turned off so it does not compete with Templater. `next-id.js` is superseded and should be removed once the snippets work.
- MDSE Bootstrap must implement `99_System/01_Admin/MDSE Bootstrap - Author Registration Spec.md`. Its source is not in this repository.
- Dataview is kept, but the functions that need it are not listed yet.
- The 79 methodology rule notes and their canvases are still in `99_System/10_EA Native Translator`, with 99 canvas nodes that point at notes that do not exist. Whether they are frozen, and where the translator's rules finally live, are open.
- The translator tool (v2.6.0) still uses `Thing`, `kind`, UTC time and GUID-ordered ids, and needs updating.
- The handoff package review (from another AI session) has items still to go through; they are in the Open list.
- The Person template holds list properties (`previousCodes`, `eaNames`), against the rule that only `tags` and the relationship fields hold several values.
- The multi-level containment rule that derives 60 of the 64 `equals` directions (W-156) has not been spot-checked.
- The review tables of W-156 and W-157 have final names and four fixed first columns (W-216); the other columns are not set yet.
- 14 elements keep a `Classifier_guid` line whose GUID is not in the export (W-180).

## Access

Give the new chat a new fine-grained GitHub token limited to `Test_Vault_` with Contents read and write and a short expiry, and revoke the one used in this chat.
