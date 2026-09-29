---
uid: 20260928123124000skellyspencer
id: INFO-00020
type: Info
subtype: Guide
status: Active
---
# Handoff: Continue Here

Rewritten 2026-09-29 (W-150) for a new AI chat continuing the work on this vault. Read this note first, then the Workspace Decision Log.

## What this vault is

`Test_Vault_` is a workspace, not the vault that will be built. It defines the EA-to-Obsidian (MDSE) translator and the conventions the real vault will follow. The real vault will be generated later by the translator, will hold only engineering notes plus a few definitions and diagrams, and will not contain the raw EA export or the methodology notes. EA is being retired, and the vault becomes the single source of engineering knowledge. The goal of the translation is a direct, mechanical stage 1 that loses nothing, so refinements can follow in stage 2 (W-30). The result must be usable by people and AI together.

## Read in this order

1. `99_System/10_Docs/Workspace Decision Log.md`: every decision (W-01 to W-169) and the Open list at the bottom. It is the authority for what has been decided.
2. `Definitions/Note Layout.md` and `Definitions/EA Source Section.md`.
3. `99_System/03_Schemas/`: `ea-element-mapping.yaml` (the element rules, all 31 EA object types decided), `ea-field-dispositions.yaml`, `ea-tag-dispositions.yaml`, `element-types.yaml`, `relationships.yaml`, `ea-package-rules.yaml`.
4. `99_System/10_Docs/Post-Import Tasks.md` (Tasks 1 to 7).
5. `99_System/02_AI/AI_INSTRUCTIONS.md` and `MDSE Modeling Ruleset 1.21` (its section 3 is out of date, see the Open list).
6. The EA export is in `99_System/CSV_EA` (`t_objectproperties_raw.csv` is the tag source, because only it has the Notes column). The `.qeax` and the translator source (v2.6.0) are not in the repository; ask for `EA_to_MDSE_Consolidated_v2_6_0.zip` if the earlier tool's rules are needed.

## How to work with Spencer

- One topic at a time, and one question per turn. End each turn with a single question. When he asks, walk him through it plainly ("like I'm 12").
- Give a recommendation with the reason. Say about any problem it creates before going on. Use numbers from the data, and say plainly what you are unsure of or could not check. Correct your own figures in the open when they turn out wrong.
- Short and direct, no praise. Tell him if there is a more efficient way to work.
- Nothing is applied until he approves it. If you apply consequences of an approved decision, say so and list them.
- Log every decision as the next W number (next is W-170) in the Decision Log, update the worklist YAML and this handoff, then commit and push to `main`. He allows pushing to `main` and pulls each change into Obsidian.
- Validate every YAML and JSON file with a parser before each commit, and only commit and push if all of them parse (a colon followed by a space inside an unquoted YAML value has broken a file twice; quote long text values). Use quoted heredocs (`<<'EOF'`). Check that a referenced source file or column exists before relying on it. Stay with EA names until after the import (W-93).
- Never write an access token into a file. After cloning, reset the remote URL to the token-free form and push with the token in the command only. Set a repo-local git identity before the first commit. Check `git log` for commits you did not make before adding a decision number (a duplicate W-117 was found once).

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

## Element mapping (W-113 to W-149): where it stands

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

Other rules from this work: the `Interface` class is gone and `Port` replaced it (W-113). Folders start at the ten packages under `IPC !` (W-117). `hasPart`/`partOf` is for Object-to-Object only, and a permanent generic `hasChild`/`childOf` (written on the owner) carries every other `ParentID` nesting, 20,384 links (W-149). Relationship fields follow `tags` in the properties and may hold lists (W-126). Stored link pairs added: `hasPort`/`portOf` (W-123), `copyOf`/`hasCopy` (W-124), `hasFlow`/`flowOf` (W-133), `hasChild`/`childOf` (W-149); temporary pair `hasClassifier`/`classifierOf` (W-125, W-127, W-135), resolved in stage 2 (Task 7). Differences on a merged Port are kept as lines on the block Port (W-121); four fixed `REVIEW` lines mark Port cases for review (W-130, Task 6), and a fifth marks the 252 nesting directions and a sixth the 88 mixed-type Generalization links (W-151, W-152, Task 7); `isConjugated` is a source-section line (W-129). Names: a Port note is `<owner> - <name>` and a pin note `<Port note> - <pin name>` (W-134); an unnamed element is its lowercase EA type and a counter, `note 1`, `part 1` (W-138, W-145). Nesting (W-151): the 836 drawn `Nesting` connectors add no notes; 584 repeat a `ParentID` link, and the 252 independent ones are written as `hasChild`/`childOf` with a `REVIEW nesting direction` line (checked in stage 2, Task 7) and the connector GUID inside each review line (W-152). Requirement nesting is bidirectional through W-149: every child carries `childOf`, every owner `hasChild`, Artifact notes included. Everything is mechanical on purpose: the EA type stays in `eaType` and stage 2 corrects it (Task 7).

## Next steps, in the order I recommend

1. **Connectors (21,822), decided by connector type.** They are imported where drawn (W-55). Settled: `Nesting` 836 (W-151, W-152) and `Generalization` 3,974 (W-152); `Connector` 823 is settled (W-153 to W-158: plain `interfaces`, BindingConnector a temporary `equals` with Task 8, one link per pair, no context line, block-level ends flagged `REVIEW port needed`, Part ends resolve to their block). Every review line must be resolvable from the vault alone, with a review table per task keyed by GUID (W-156); the audit of the review lines is done (W-157: three get a table and a GUID, four pass); the Name line is `- Connector name: <name> (to [[other end]])` for every type (W-158); `Aggregation` 2,288 is settled (W-159: composite Object pairs `hasPart`, everything else `hasChild`, an existing link wins, 450 new links); `Realisation` 950 is settled (W-160: a requirement `appliesTo` an Object, a Function realizes a Use Case, everything else `realizedBy` with `REVIEW modelCheck: realization`); only a Function or a Design `satisfies` a requirement (W-160, for the Dependency mapping); `NoteLink` 349 is settled (W-161, W-162: a note on one element folds into its body as a bullet under `**EA notes:**` with date and author, a note on several stays Info with `describes`); `Dependency` 6,762 is decided one stereotype at a time: `satisfy` 2,444 is settled (W-163: Function or Design `satisfies`, everything else `satisfies` with `REVIEW modelCheck: satisfy`); `deriveReqt` 1,416 is settled (W-164: `derivedFrom` between requirements, else with `REVIEW modelCheck: deriveReqt`); `refine` 1,114 is settled (W-165: `refines` between requirements, a Use Case `drives` a requirement with the new `drives`/`drivenBy` pair, Info and Artifact `describes`, else flagged); `trace` 770 is settled (W-166, W-167: Info, Artifact and reversed Object to Info `describes`, Issue `affects`, Object and Requirement pairs in either direction `appliesTo` (Realisation too), Requirement to Requirement `references` with the new `references`/`referencedBy` pair, else flagged); `verify`, `RecoveryRequirement` and `ASILDecompose` are settled (W-168); the 667 with no stereotype are settled (W-169: Function to Function and Function to Design `dependsOn`, the rest by earlier rules or flagged), so Dependency is done; next is Abstraction (2,811); the rules are in `99_System/03_Schemas/ea-connector-mapping.yaml`. Method: for each type show the endpoint pairs under the new element mapping with counts and the relationship each becomes, then Spencer approves or changes rows. Order proposed: Realisation (950), NoteLink (349), Dependency (6,762), Abstraction (2,811), UseCase (1,258), Association (603), then the Usage, ControlFlow, StateFlow, Sequence and InformationFlow types. The Review and Deferred rows in the r12 matrix (`10_EA Native Translator/02_EA Relationships`, about 4,400 and 2,800) get a stage-1 fallback per type. The r12 matrix predates the element mapping (it still names `System Function` and `requirement` stereotypes), so every Settled rule is re-read against the new types first. Still to do: the line format for a connector's values on an end note (Name goes above `EA GUID`, W-99; Notes, trigger, guard and effect are open), the assembly and Part context of the connectors moved by the Port merge (W-114), the relationship vocabulary for `effect`, `entry`, `doActivity`, `represents`, `conveys` and `target`, and the 107 connectors that touch 90 Parts. The translator's matrix is in `99_System/10_EA Native Translator/07_References/r12 Workbook`.
2. **The three set-aside fields on the other element types** (W-96): `Classifier` on UseCase 23, ActivityPartition 22, Action 18, Sequence 1; `PDATA1` on Requirement 12,089, Issue 264, State 253, Activity 118 and others.
3. **Templates** (plan step 3): one per type (`Artifact.md` and the others list no relationship fields yet, W-151), subtype variants only where fields or sections differ, following `Definitions/Note Layout.md`. `modelCheck` has none; `Port.md` still defaults to `electrical & material`; the `modelCheck` class needs a prefix and an entry in `element-types.yaml` (W-100, W-146). Decide whether the legacy `folder` values in `element-types.yaml` stay (W-04).
4. **Naming:** the unsafe-character replacement and the duplicate-name suffix (W-48, W-65), and the designator parse rule per source document (W-82).
5. **Layout gaps:** the user section's name and content, the aliases and `formerIds` format, the order of the other `Source: EA` lines against the tag lines, where the definitions of kept body lines go, the counter order for several attachments on one note.
6. **Schema and docs left out of date:** `Ruleset 1.21` section 3, the translator (v2.6.0), the `Definitions/Properties` notes for the new relationship fields, `MDSE Element - Interface.md` and its canvas, and unused properties in `types.json`.

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

## Access

Give the new chat a new fine-grained GitHub token limited to `Test_Vault_` with Contents read and write and a short expiry, and revoke the one used in this chat.
