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

## Open (raised, not yet decided)

- Where the translator's source-of-truth ruleset lives.
- What happens to the existing methodology notes (rules, decisions, canvases, bases), including 99 canvas nodes that already point at note paths that do not exist.
- Disposition of the 121 EA tagged values, starting with where legacy IDs (`id`, `SysML1.4::id`) land.
- How the 13-character author code is derived from a person's name, and the rules for mapping EA author names, timezone and duplicate timestamps into `uid`.
- Whether original EA modified dates should also be kept (creation date and author go into `uid`).
- Where MDSE Bootstrap's source lives, so its install-time name entry can follow the same definition.
