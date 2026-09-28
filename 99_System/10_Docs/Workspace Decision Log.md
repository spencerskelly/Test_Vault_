---
type: Info
status: Active
---
# Workspace Decision Log

Decisions made while turning this vault into the workspace that defines the EA-to-MDSE translator and the working conventions for the final vault. Newest last. Each entry: what was decided, why, and where it landed.

This log covers workspace and convention decisions. Translation-rule decisions (element, property, relationship mappings) will get their own entries as we work through them.

## Decided

**W-01 · 2026-09-28 · Vault strategy.** One vault. No reference/working split and no cross-vault links, so any visual can be built without cross-vault connections. The final vault holds engineering notes plus a few definitions and diagrams for people working in it. Methodology and translation material stays out of it. This vault (`Test_Vault_`) is a workspace for defining the translator, not the vault that will be built.

**W-02 · 2026-09-28 · Nomenclature.** MDSE "things" are `Object` (replaces `Thing`). Note classification uses `type` plus `subtype` (replaces `kind`). EA's own metaclass is written "EA Object" so it is never confused with MDSE Object. The translator tool (v2.6.0) still uses the old terms and needs the rename.

**W-03 · 2026-09-28 · EA traceability.** The old `eaGUID` appears only at the bottom of the note body, for traceability to the original element. It is not a frontmatter property and is not used for anything else.

**W-04 · 2026-09-28 · Legacy scaffolding removed, `99_System` kept.** The 21 empty legacy model folders (10_Objects to 71_Artifacts, 00_Home, 90_Concept) were deleted; they held navigation files only and the final structure will follow the EA model's package structure. `99_System` stays and is edited topic by topic, because this vault defines plugins, templates and conventions. Commit `7c1dddd`.

**W-05 · 2026-09-28 · Plugin stack.** Cross-vault plugins archived (Ampure Cross-Vault Resolver, Multi-Vault Navigator); the resolver source and notes on both are under `99_System/01_Admin/Archived Plugins/`. Kept: MDSE Bootstrap (auto-installs the pinned plugins on a new machine for team rollout), Dataview (needed for some functions Bases lacks; the functions are still to be listed), and the rest of the stack. The Obsidian Git binary stays committed because it is in use on the Mac; pinned at 2.40.0. Commits `003a146`, `7af1132`.

**W-06 · 2026-09-28 · Templates and identity.** People create notes by hand, so templates serve both hand-authored and translated notes, and a template is the single definition of a note class.
- Every note created in the vault gets a `uid` and a human-readable `id`. Notes brought in from outside keep their own identification.
- `uid` and `id` are filled automatically when a template is applied.
- `uid` is the global identity and also records creation time and original author.
- Duplicate `id` values from concurrent work are an accepted risk, handled by a periodic AI sweep that finds and repairs overlaps.
- Templates will not all be identical; they get class-specific fields as the rules are built, and some subtypes will get their own templates.

**W-07 · 2026-09-28 · Working agreement.** Claude may push directly to `main` on `Test_Vault_`, so the team learns first-hand how AI participation works and where it goes wrong. Topics are decided one at a time.
**W-08 · 2026-09-28 · Property definitions.** Every property gets its own definition note, so someone new to the vault can look up what it means without guessing. Each note states what the property is, how its value is determined, and what it impacts, plus the other fields that remove ambiguity (see the property definition standard once written).

**W-09 · 2026-09-28 · uid from EA history and name entry.**
- For translated notes, `uid` should carry the original EA creation time and original author, instead of the import time and the person who ran the translator. Feasible: EA has a creation date on every element and an author on nearly all. Detailed rules still to be decided.
- Each person enters their name once, and the author code is generated from it according to one written definition. Entered through a popup the first time a note is created from a template, and also during install (MDSE Bootstrap) so the standard is followed from the start.

**W-10 · 2026-09-28 · Author code rule.** The 13-character author code is the person's last name followed by first name, lowercase letters only, truncated to 13 characters, and padded with hyphens on the right when shorter. Examples: Spencer Skelly gives `skellyspencer`, Chesca Legaspi gives `legaspichesca`, Florian Koerfer gives `koerferfloria`, Jesse Rivera gives `riverajesse--`. This fits the existing `uid` pattern (13 characters, lowercase letters and hyphens).

**W-11 · 2026-09-28 · Author registry.** Ten people are mapped from the EA Author values to their author codes, recorded in `99_System/03_Schemas/authors.yaml`. Login names and display names of the same person are treated as one author (for example `SpencerSkelly` and `skellys`). Jesse Rivera and Ray Virzi are different people. All ten codes follow the W-10 rule and are unique. Every EA author value is covered except 722 blank authors and one junk value (`7.1.0-2`).

**W-12 · 2026-09-28 · Unknown EA authors.** EA elements with no usable author (722 blank, 1 with the value `7.1.0-2`) get the author code `sparxeaauthor`, meaning "created in Sparx EA, author not recorded". It is not a person and is recorded in `authors.yaml`.

**W-13 · 2026-09-28 · uid time is local time.** The timestamp in a `uid` (`yyyyMMddHHmmssSSS`) is local time, not UTC, for every note. Translated notes carry EA's recorded creation time exactly as stored; notes created in the vault carry the creator's local time when the template is applied. Reason: simplicity and consistency, with no timezone conversion. Consequences accepted: `uid` order is only approximately chronological across people in different timezones, and a clock change (the repeated hour when daylight saving ends) could produce a duplicate for the same author, which the uniqueness check catches. The translator tool currently defines this as UTC and needs changing. Duplicate timestamps are resolved by advancing one millisecond until unique, with ties ordered by EA GUID so the same EA data always yields the same `uid`.

**W-14 · 2026-09-28 · id numbering for translated notes.** Every translated note gets an `id`, numbered per class prefix in original EA creation order, oldest first, with ties broken by EA GUID. Numbers are assigned after the translator has decided which elements become notes, so there are no gaps. Same EA data gives the same numbers. Once the migration is final the numbers are permanent; notes created later in the vault continue after the highest migrated number. The tool currently orders by EA GUID and needs changing.

**W-15 · 2026-09-28 · id format.** Every `id` uses a five-digit number, for example `REQ-00042`, for every class. An `id` is never reused once issued. Five digits leaves room for 99,999 notes per class and keeps text sorting correct. The migration itself needs less: after the tool's fold rules only about 3,936 Requirement notes are emitted.

**W-16 · 2026-09-28 · External documents.** An external document (standard, regulation, stakeholder document) is brought in as one note per document edition, with an anchor for each clause. Links go straight to the clause with the anchor. Clauses that have no relationships fold into the document note; clauses that are connected to other elements become their own notes and link back to the clause anchor. To revisit only if a document proves too large to read whole (the largest, UL 2594, is about 610 clauses, roughly 33,000 tokens).

## Open (raised, not yet decided)

- Where the translator's source-of-truth ruleset lives.
- What happens to the existing methodology notes (rules, decisions, canvases, bases), including 99 canvas nodes that already point at note paths that do not exist.
- Disposition of the 121 EA tagged values, starting with where legacy IDs (`id`, `SysML1.4::id`) land.
- Which `id` the 2,754 connected external requirements (905 standard, 1,849 stakeholder) receive.
- How "never reuse an id" is enforced: the current ID script takes the highest existing number plus one, so deleting the newest note would free its number.
- Whether original EA modified dates should also be kept (creation date and author go into `uid`).
- Where MDSE Bootstrap's source lives, so its install-time name entry can follow the same definition.
