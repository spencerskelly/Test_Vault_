# MDSE AI Instructions

For every AI tool that creates or edits notes in this vault (Claude, ChatGPT, Rovo, Gemini, or any other). AI tools cannot run Templater, so you do by hand exactly what the template snippets do. The result must look the same as a note created from a template.

Before substantial work, read `99_System/10_Docs/MDSE Modeling Ruleset 1.21.md`, `99_System/03_Schemas/relationships.yaml`, `99_System/03_Schemas/element-types.yaml` and `99_System/03_Schemas/authors.yaml`. Property meanings are in `Definitions/Properties`.

## Creating a note

1. **Classify first.** Choose the class, then copy the matching template from `99_System/05_Templates` (for example `Requirement.md`). Keep its properties and headings exactly. Do not add or drop properties. If no class fits, ask the user.
2. **Fill in `uid`** yourself. It is 30 characters, no spaces: `yyyyMMddHHmmssSSS` followed by a 13-character author code.
   - **Time:** local time now, to the millisecond, not UTC. Use the `timezone` of the person who directed the note if `authors.yaml` lists one; otherwise `defaultTimezone` from `authors.yaml`.
   - **Author code, if a user directed the note:** that user's `code` from `authors.yaml`. This applies even if you wrote every word. If you do not know who the user is, ask. A person may have `previousCodes` in `authors.yaml`: notes carrying those codes are also theirs.
   - **Author code, if you created the note on your own with no direct instruction:** your own code from `ai_authors` in `authors.yaml`. If your tool is not listed, add it: tool name (lowercase letters, at most 11), then `ai`, then hyphens to 13 characters.
   - **If another note already has that exact `uid`,** add one millisecond until it is unique.
3. **Fill in `id`** yourself: the class prefix, a hyphen, and a five-digit number. Find the highest number used for that prefix across every note in the vault, including retired notes and any `formerIds`, then add one. Prefixes are in `element-types.yaml`. Never reuse a number.
4. **Check before saving:** `uid` matches `^\d{17}[a-z-]{13}$`, and `id` matches `^[A-Z]+-\d{5}$`.

Examples of a filled note header:

```
uid: 20260928101530123skellyspencer   (a user directed the note)
uid: 20260928101530123claudeai-----   (Claude created it on its own)
id: REQ-00042
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
- Author the forward (owner-side) relationship. Generated inverse fields are derivative.
- Folder placement is navigation, not meaning.
