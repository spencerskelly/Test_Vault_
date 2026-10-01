# MDSE AI Instructions

For every AI tool that creates or edits notes in this vault (Claude, ChatGPT, Rovo, Gemini, or any other). AI tools cannot run Templater, so you do by hand exactly what the template snippets do. The result must look the same as a note created from a template.

Before substantial work, read `99_System/10_Docs/MDSE Modeling Ruleset 1.22.md`, `99_System/03_Schemas/relationships.yaml`, `99_System/03_Schemas/element-types.yaml`, `99_System/03_Schemas/authors.yaml` (AI codes and the default time zone) and the person notes in `99_System/04_People` (each person's author code and time zone). Property meanings are in `Definitions/Properties`.

## Creating a note

1. **Classify first.** Choose the class, then copy the matching template from `99_System/05_Templates` (for example `Requirement.md`). Keep its properties, their order (`type`, `subtype`, `id`, `uid`, `status`, `tags`, W-97) and its headings exactly. Do not add or drop properties, except that relationship fields from `99_System/03_Schemas/relationships.yaml` follow `tags` (W-126). Only `tags` and the relationship fields may hold more than one value. If no class fits, ask the user.
2. **Fill in `uid`** yourself. It is 30 characters, no spaces: `yyyyMMddHHmmssSSS` followed by a 13-character author code.
   - **Time:** local time now, to the millisecond, not UTC. Use the `timezone` in the directing person's note in `99_System/04_People` if it has one; otherwise `defaultTimezone` in `authors.yaml`.
   - **Author code, if a user directed the note:** that user's `code`, from their note in `99_System/04_People`. This applies even if you wrote every word. If you do not know who the user is, ask. A person may have `previousCodes` in their note: notes carrying those codes are also theirs.
   - **Author code, if you created the note on your own with no direct instruction:** your own code from `ai_authors` in `authors.yaml`. If your tool is not listed, add it: tool name (lowercase letters, at most 11), then `ai`, then hyphens to 13 characters.
   - **If another note already has that exact `uid`,** add one millisecond until it is unique.
3. **Fill in `id`** yourself: the class prefix, a hyphen, and a five-digit number. Find the highest number used for that prefix across every note in the vault, including retired notes, and the earlier ids listed under `## Former ids` in any note (W-207), then add one. Prefixes are in `element-types.yaml`. Never reuse a number.
4. **Check before saving:** `uid` matches `^\d{17}[a-z-]{13}$`, and `id` matches `^[A-Z]+-\d{5}$`.

Examples of a filled note header:

```
id: REQ-00042
uid: 20260928101530123skellyspencer   (a user directed the note)
uid: 20260928101530123claudeai-----   (Claude created it on its own)
```

## Status and review

- Leave `status` at the template default. Never advance it or mark your own note reviewed or approved. A person does that.
- Never delete a note. To remove one, set `status` to Retired. The `id` stays reserved.

## Do not

- Change an existing note's `uid` or `id`.
- Stamp `uid` or `id` on material brought in from outside (standards, external documents). It keeps its own identification.
- Add an `eaGUID` to a new note. It appears only at the bottom of notes translated from EA.
- Invent missing source facts.
- Duplicate an existing concept. Reuse and link to it.
- Create or split vaults. Users create vaults. You may flag when scale or context quality suggests a split.

## Relationships

- Use only relationships defined in `relationships.yaml`.
- Create a relationship only between classes its endpoint rule in `relationships.yaml` allows (`from`, `to`, `sameClass`, `excludePairs`; W-272, W-277). A relationship with no rule yet is not restricted. Use `tracesTo` only when two notes are related and no relationship fits yet; it is provisional and comes back as a Review finding to be replaced (W-288).
- Author the forward (owner-side) relationship and, in the same edit, write its inverse per `relationships.yaml`: a paired field gets its inverse field on the other note; a symmetric field is written on both notes; a one-way field gets nothing. Inverse fields are derivative: the forward field wins when they disagree (W-275).
- Folder placement is navigation, not meaning.

## Local occurrences

- Reuse the authoritative Object/Port/Item Flow definition rather than duplicating it for each contextual use (W-293, W-294).
- When a reusable Object/assembly is used inside another Object/system and that specific use must be distinguished, model the use as a local part occurrence owned by the containing context. Its reusable semantic source is `definition`, not `subtypeOf`.
- A contextual endpoint occurrence belongs to the Object/part occurrence on which it exists. A local connection belongs to the lowest meaningful common configuration context that brings its endpoint occurrences together. Local flows belong to that connection.
- A Requirement may keep `appliesTo` when its true target is an addressable local occurrence. Do not invent a new relationship solely because the target is contained.
- Local endpoint/flow roles are `transmit`, `receive`, `exchange` or `unspecified`.
- Do **not** invent or manually standardize the contained-record Markdown syntax yet. The final local-ID token format, anchor/address syntax, canonical block fields and manual-authoring contract remain open. Until those are frozen, use the importer/Workbench-approved representation or ask.
- Do not create a standalone note merely to preserve a contextual occurrence if stable local addressability is sufficient; promote an occurrence only when an approved independent lifecycle/reuse/ownership/navigation need justifies it.

