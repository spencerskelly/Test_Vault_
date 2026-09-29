---
uid: 20260928123124000skellyspencer
id: INFO-00020
type: Info
subtype: Guide
status: Active
---
# Handoff: Continue Here

Written 2026-09-28 for a new AI chat continuing the work on this vault. Read this note first, then the Workspace Decision Log.

## What this vault is

`Test_Vault_` is a workspace, not the vault that will be built. It defines the EA-to-Obsidian (MDSE) translator and the conventions the real vault will follow. The real vault will be generated later by the translator, will hold only engineering notes plus a few definitions and diagrams, and will not contain the raw EA export or the methodology notes. EA is being retired, and the vault becomes the single source of engineering knowledge.

## Read in this order

1. `99_System/10_Docs/Workspace Decision Log.md`: every decision made here (W-01 to W-147) and the Open list at the bottom. It is the authority for what has been decided.
2. `99_System/02_AI/AI_INSTRUCTIONS.md`: how an AI creates notes (uid, id, status).
3. `99_System/03_Schemas/ea-field-dispositions.yaml`, `ea-tag-dispositions.yaml` and `ea-element-mapping.yaml`: the property and element worklists.
4. `Definitions/Properties`: the property definition notes (`uid`, `id`, `eaType` so far).

## How to work with Spencer

- One topic at a time, and one question per turn. End each turn with a single question.
- Give a recommendation with the reason. Say about any problem it creates before going on.
- Use numbers from the data. Say plainly what you are unsure of.
- Short and direct, no praise.
- When he says you decide, decide and log it.
- Log every decision in the Decision Log as the next W number, then commit and push to `main`. He allows pushing to `main` and pulls each change into Obsidian to check it.
- In shell commands use quoted heredocs (`<<'EOF'`). An unquoted one once stripped all the inline code out of two notes.
- Never write an access token into a file.

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

## Where the property work stands

Fields and tags are complete (W-33 to W-96), with one exception set aside for the element mapping.

Done: disposition vocabulary; all element, connector, package and diagram fields except three (W-33 to W-73); all subordinate tables (W-74 to W-86); all 121 tags (80 dropped, 38 body, 3 structure; W-29 to W-102); the W-88 property set (`uid`, `id`, `type`, `subtype`, `status`, `tags` on every note, `eaType` on translated notes; `aliases` and `formerIds` in the body; `control` and `boundary` not approved). Body lines use the exact EA tag name until after the import (W-93).

Set aside (W-96): `Classifier`, `Classifier_guid` and `PDATA1` on element types other than Part. They are marked `setAside` with counts by type in `ea-field-dispositions.yaml`. Decide them in the element mapping.

Applied in W-112: the property set and order in the templates, `element-types.yaml`, `types.json`, the `id` snippet, `next-id.js`, AI_INSTRUCTIONS and a note in Ruleset 1.21 section 3. Not applied: existing notes and the translator. Open rules found in the review: multi-line tag values on a body line, the order of lines in the `Source: EA` section, the line format for connector values on an end note, and where the definitions of kept body lines are written.

## Decided after the W-96 review (W-97 to W-100)

Property order at the top of every note: `type`, `subtype`, `id`, `uid`, `status`, `eaType`, `tags`; only `tags` and, after it, the relationship fields hold several values (W-97, W-126). The 36 body-line tags are reviewed first so Spencer can set their order (W-98). A `Name` line goes above `EA GUID`, and the `Source: EA` section starts three lines below the other body content (W-99). An element with no approved mapping gets `type: modelCheck` (W-100). The order of body lines is set in W-101 and changed by W-104 and W-105 (four comments become labeled normal text below the Note; the other 32 tag lines stay below the EA GUID) (`order` in `ea-tag-dispositions.yaml`). The `text` tag is kept as normal text below the Note (W-102). Open before the import: multi-line values, the 255-character cut. When a Note and `text` both exist they are separated by one blank line (W-103). None of this is applied yet to templates, snippets, schemas or the translator.

## Decided after W-112

W-113: the MDSE `Interface` class is removed and `Port` (prefix `PORT`, folder `20_Ports`, the five old Interface subtypes) is added. Intent: bring EA in as native as possible, lose no data, merge ports only as far as needed, resolve the rest in the second pass. The Port merge rule (one hop, PDATA3, then exact name, then add, else stay) is W-114. Next W number is W-148.

Port findings so far (from `t_object`, `t_connector`, `t_xref`; not yet decided): all 4,387 Ports have an owner (Part 1,956, Class 1,903, Object 485, ActivityPartition 42, Actor 1). `PDATA1` = the typing Class (3,432); `PDATA2` = redefinition, mostly a Port on an ancestor block (1,713 of 1,906); `PDATA3` = the Port on the block a Part or Object is typed by (1,697 of the Part-owned or Object-owned Ports match one on their own block); `Classifier` on Ports points at another Port (920). `isConjugated` exists only in `t_xref` CustomProperties for 31 Ports. Merge rule (approved, W-114), one hop only, never up the redefinition chain: an instance Port goes to the Port `PDATA3` names if that Port is on its owner's block, else to the Port with the exact same name on that block, else it is added to the block as a Port of its own; the connectors drawn in the assembly move with it and keep the assembly and Part as context. Modelled result: 4,387 Ports become 2,589, 0 self-loops, 45 connectors duplicate another. 26 Ports have no block and stay. Following the redefinition chain creates false self-loops (55) and must not be used.

W-115: Requirement subtype comes from the EA package path (old rule R-01) with a new subtype `engineering` for the Engineering Requirements folder (2,469); the 2,383 InformationItems in the Regulatory Requirements folder become Requirement notes with subtype `standard`. 16,371 requirement notes in all. Confirmed in W-116: the functionalRequirement and designConstraint stereotype override does not apply inside the Engineering folder (all 2,469 are engineering). Still open for Requirement: the template default subtype and the designator parse rule.

W-117: the vault folder tree starts at the ten packages under `IPC !` (`Model` and `IPC !` are not folders). Working method (W-119): by element type again, each `eaType` settled once, Requirements skipped (their subtype follows the package, W-115/W-116). The package walk is paused after `01 System` was shown. Decided rules are kept in `99_System/03_Schemas/ea-package-rules.yaml`. Done: `Model`, `IPC !`, `00 Product Abstract` (folder only, W-118). Next: `01 System` (Package_ID 1244, first child of `00 Product Abstract`), then the rest of `00 Product Abstract`, then `00 Product Definition`, `01 Product Use Case`, `02 Product Context`, `03 Product Requirement`, `04 Product Function`, `05 Product Design`, `06 Product Validation`, `07 Product Assembly`, `09 Product in Progress`.

W-120: the 423 interface Classes become Port notes (subtype = the stereotype) and a Port's `PDATA1` becomes `subtypeOf` between Port notes. Still open for Port: the 104 typing links that do not reach a Port note (97 Hardware Component, 2 Physical Signal, 5 missing), the 752 FlowProperty Parts, `PDATA2`, `Classifier`, the owner link, the `ProxyPort` and `FullPort` stereotypes, and W-45 (archives `PDATA2` and `PDATA3`) for Ports. W-121: differences on a merged instance Port (164 instance Ports, 117 block Ports: name 101, typing Class 39, stereotype 8, redefinition 23) are kept as lines on the block Port note; the line format and place are not decided. W-122: a Port's `PDATA2` becomes `subtypeOf` (1,257 links; 146 that do not follow the block family are flagged, wording open). W-123: the owner link is a stored pair `hasPort` (on the owner) and `portOf` (generated), in `relationships.yaml` and `types.json`; 2,589 Port notes, 2,520 owned by a block note. W-124: a general stored pair `copyOf` (on the copy) and `hasCopy`, for tracing a copy back to its original; first use: the 2 merged Ports whose `Classifier` names a Port in a different note (the other 203 of the 205 become links from a note to itself, nothing written); W-125 supersedes the rest: `Classifier` on Ports is written as a temporary `hasClassifier`/`classifierOf` pair (441 surviving Ports, plus the 2 merged ones), resolved in a later stage. Settled in W-126: relationship fields follow `tags` in the properties and may hold lists (W-97 amended). W-127: the 104 Port typing links that do not reach a Port note: 99 (97 Hardware Component, 2 Physical Signal) use the temporary `hasClassifier`, 5 missing GUIDs are kept as a `Source: EA` line. W-128: Port subtypes `proxy` (ProxyPort) and `full` (FullPort) added; plain Ports have a blank subtype. W-129: `isConjugated` is a source-section line on the 21 surviving Port notes that have a recorded value. W-130: four fixed `REVIEW` lines for Port cases (831 notes) and Post-Import Task 6. W-131: the 623 Signal elements become Item Flow notes with a blank subtype. W-132: each of the 760 FlowProperty Parts becomes its own Item Flow note (direction as source/target, Signal link as the temporary `hasClassifier`); Item Flow then has 1,383 notes. W-133: a Port note points at its pin notes with the stored pair `hasFlow`/`flowOf` (752 pins on 214 Port notes). W-147: a package is a folder, and only the 34 with a description also get a `modelCheck`/`Package` note; every `eaType` now has a mapping. W-146: the 13 small behaviour and annotation types (632 elements) become `modelCheck` notes with subtype = the EA type. W-145: Note (431), Text (61), Constraint (1) and the 442 InformationItems outside Regulatory become Info notes (blank subtype); one naming rule for every unnamed element (lowercase EA type and a counter). 2,018 elements are still unmapped (Package 1,386 and 632 small behaviour and annotation types). W-144: Issue (264, blank subtype), Actor (44) and StateMachine (2) map straight to their MDSE classes. W-143: Artifact stays Artifact (Document to `document` 329, Image to `image` 129, CustomDocument blank 1). W-142: a State element in `05 Product Design` (954) becomes a Design note, every other State (158) a State note, blank subtypes. W-141: Activity becomes Function (Function stereotypes to their subtype 530; no stereotype 611, blank subtype) or Verification/test for `testCase` (527); the 142 Activity-typed Parts of W-137 can now be written. W-140: UseCase becomes Use Case (1,667) with the subtype from the package (`what` 983, `when` 21, `where` 74, `who` 232 added to the list, 357 blank). W-139: every Class that is not an interface Class becomes an Object note with a blank subtype (2,314; the stereotype stays in `eaType`, Physical Context and System Partner are not split out); the split is made after the import. W-136: the 2,055 Parts typed by a Class fold into the assembly as one `hasPart` entry per Part, plus a source-section line for the 515 with data of their own (role name, quantity, tags, style); W-137: the 219 Parts typed by an Activity (142), State (61) or Signal (16) become a `hasPart` entry on their owner (Activity and State ones wait for their mappings); W-138: the other 103 Parts (no usable block) become Object notes with subtype `part` (added to the Object subtype list), unnamed ones named `part 1`, `part 2`. W-135: each of the 545 EA Objects becomes its own Object note (blank subtype), `Classifier` as the temporary `hasClassifier` (498), 47 dangling blueprints and 6 odd `PDATA1` as source-section lines; the three set-aside fields are now decided for Ports and Objects, still open for other types. W-134: a Port note is named `<owner> - <port name>` and a pin note `<Port note name> - <pin name>`, with a counter for repeats and blank names and the EA name kept as a `- Name:` line. Still open for flows: the 8 pins with no interface owner, the line format for the W-121 differences and the W-114 connector context.

## Layout and sweep (W-107, W-108)

The note layout is written in `Definitions/Note Layout.md`; `Definitions/EA Source Section.md` describes the last section. A sweep of all fields, tags and export files found no missing field; column dispositions for `t_attribute`, `t_operation`, `t_xref` and `t_document`, and a role for every file in `CSV_EA`, were added to `ea-field-dispositions.yaml`. `Object Type` (both), `Origin` and `In-Links` stay `drop` (W-109). Open from the sweep: the counter order for several attachments on one note.

## Next topic: element mapping

Element mapping: which MDSE type and subtype each EA object type becomes. The worklist is `ea-element-mapping.yaml` (31 object types, largest first, all `pending`), with what the earlier translator did as evidence (`oldToolRules`). It should also settle the three set-aside fields, the `type` value for elements with no approved mapping (handoff review item 1), whether Ports are notes or sections of the block note, the relationship vocabulary (`effect`, `entry`, `doActivity`, `represents`, `conveys`, `target`, and `direction` on flows), the fate of States, Classes and Packages, and the sequence-diagram rule. The chat needs `EA_to_MDSE_Consolidated_v2_6_0.zip` uploaded again, for the earlier tool's rules. The first proposal to fold unconnected requirements into document notes is replaced (W-81).

### Plan for the element mapping (proposal, nothing approved)

1. **Proposal sheet first.** Before asking anything, compute for all 72 `eaType` values: row count, sample names, connectors in and out, populated tags and fields, `Classifier` and `PDATA1` values, and a proposed `type` and `subtype` with the evidence. Approve by family with exceptions: requirements and specs; structure (Class, Part, Object, Port, InformationItem, Signal); behavior (Activity, Action, State, StateNode, Decision, ActivityPartition, Trigger, Synchronization, Sequence, ActionPin, StateMachine, Event, ActivityParameter); other (Package, Artifact, Note, Text, Issue, Change, Actor, Boundary, Constraint, UseCase, ProxyConnector).
2. **Ports (recommendation, not decided).** Each Port (4,387) becomes its own note with subtype Port, placed with its owning block, with a Dataview table on the block note listing its ports. Reasons: connectors end on port objects, so endpoints stay valid; it matches the requirement approach (own note in stage 1, fold in stage 2); `Classifier` (920 typed Ports) gives the type link. To check first: how the owner block is found (probably `ParentID`), Ports with no owner, `isConjugated` values, and consistency with Parts merging into blocks (W-43, W-44).
3. **Templates.** One per type, with a subtype variant only where fields or sections differ, generated from `element-types.yaml`; each follows `Definitions/Note Layout.md`.
4. **Dry run.** Every EA row lands in exactly one mapping row, none unmapped (unmapped gets `type: modelCheck`, W-100), and totals per type match the export.

## Not yet verified or still open

- The Templater snippets pass 21 tests against mock objects but have not been run in Obsidian. The core Templates plugin should be turned off so it does not compete with Templater.
- `next-id.js` is superseded (it filled gaps and used four digits) and should be removed once the snippets work.
- MDSE Bootstrap must implement `99_System/01_Admin/MDSE Bootstrap - Author Registration Spec.md`. Its source is not in this repository.
- Dataview is kept, but the functions that need it are not listed yet.
- The 79 methodology rule notes and their canvases are still in `99_System/10_EA Native Translator`, with 99 canvas nodes that point at notes that do not exist. Whether they are frozen, and where the translator's rules finally live, are open.
- The translator tool (v2.6.0) still uses `Thing`, `kind`, UTC time and GUID-ordered ids, and needs updating.
- The handoff package review (from another AI session) has items still to go through; they are listed in the Open list.

## Access

Give the new chat a new fine-grained GitHub token limited to `Test_Vault_` with Contents read and write and a short expiry, and revoke the one used in the previous chat.
