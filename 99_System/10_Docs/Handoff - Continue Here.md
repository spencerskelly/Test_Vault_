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

1. `99_System/10_Docs/Workspace Decision Log.md`: every decision made here (W-01 to W-87) and the Open list at the bottom. It is the authority for what has been decided.
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
- **Tags:** 69 of the 121 tags are dropped (W-29). Sequence-style EA `id` values are dropped (W-26). The `Stakeholder ID` tag holds clause numbers. When unsure, keep the value in the body and decide in the cleanup (W-27).
- **Default diagram line:** an element with a default diagram gets a marked `Default diagram: [[...]]` line, written only when the canvas is created, including by a diagrams-only run (W-80). **Requirements:** every one is imported as a note, folding is stage 2 (W-81).
- **Diagrams-only merge:** a new tool mode may add selected diagram types into an existing vault, additive only and through the accepted ledger (W-62). A diagram is a canvas file plus a companion note (W-73).
- **Import process:** two stages (W-30). Run into a fresh vault, review, then accept it or start fresh with better rules; never import over an existing vault (W-36, W-37). Review changes are the git diff against the baseline plus reasons in `99_System/10_Docs/Review Changes Log.md` (W-38). The source reference is a ledger keyed by EA GUID plus a run manifest, with no copied values (W-35).
- **Connectors and release:** connectors are imported where they were drawn; the 118 flow connectors attached to a block instead of a port are flagged `REVIEW port needed` and fixed in stage 2 (W-55). The vault is not released until stage 2 is complete. Tasks: `99_System/10_Docs/Post-Import Tasks.md`.
- **Field dispositions:** every field ends as `property`, `body`, `structure`, `archive` or `drop` (W-33). Element admin fields are settled (W-39), and so are the 21 empty element fields (W-40).

## Where the property work stands

Done: disposition vocabulary; all element, connector, package and diagram fields except three (W-33 to W-73, listed below); all subordinate tables (W-74 to W-86); 69 tags dropped; the `id` tags; `Stakeholder ID` as clause source.

Next, in this order:
1. The three element fields still `pending` in `ea-field-dispositions.yaml` (`Classifier`, `Classifier_guid`, `PDATA1`): decided for Parts only (W-44), they wait for the Port and Object mapping for other types.
2. The 44 pending tags in `ea-tag-dispositions.yaml` (the `Status` and `Object Type` tags were dropped in W-87). Spencer wants a new analysis after the import (Task 5 in `Post-Import Tasks.md`). Groups: large low-variety tags, comments and knowledge, part and hardware data, FMEA, EA tool leftovers.
3. Which properties every translated note carries.
4. The open items listed in the Decision Log, chiefly the per-document designator parse rule, the duplicate-name and unsafe-character rules, and the ports question, all needed before the import.

## Parked for a separate chat

Element mapping: which MDSE type each EA object type becomes. The worklist is `ea-element-mapping.yaml` (31 object types, largest first, all `pending`), with what the earlier translator did as evidence. The first proposal was: every EA Requirement becomes an MDSE Requirement note, except unconnected standard and stakeholder requirements (10,052), which fold into their document note. That is replaced for this import: every requirement is imported as its own note (13,988) and folding happens in stage 2 (W-81, Task 4). That chat will need `EA_to_MDSE_Consolidated_v2_6_0.zip` uploaded again, for the earlier tool's rules.

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
