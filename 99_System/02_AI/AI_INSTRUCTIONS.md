# MDSE AI Instructions

For every AI tool that creates or edits notes in this vault (Claude, ChatGPT, Rovo, Gemini, or any other). AI tools cannot run Templater, so you do by hand exactly what the template snippets do. The result must look the same as a note created from a template.

Before substantial work: if `99_System/10_Docs/00 - Current State.md` exists, read it first (this is the methodology workspace). A lean generated engineering vault intentionally omits that registry; there, start with `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md`, `99_System/03_Schemas/relationships.yaml`, `99_System/03_Schemas/element-types.yaml`, `99_System/03_Schemas/authors.yaml` (AI codes and the default time zone) and the person notes in `99_System/04_People` (each person's author code and time zone). Property meanings are in `Definitions/Properties`.

## Creating a note

1. **Classify first.** Choose the class, then copy the matching template from `99_System/05_Templates` (for example `Requirement.md`). Keep its properties, their order (`type`, `subtype`, `id`, `uid`, `status`, `tags`, W-97) and its headings exactly. Do not add or drop properties except governed sparse optional properties declared by `element-types.yaml` and relationship fields from `relationships.yaml`. Optional properties follow `tags` and precede relationship fields; omit a default-valued sparse property when its schema says `omitWhenDefault`. Only `tags` and the relationship fields may hold more than one value. If no class fits, ask the user.
2. **Fill in `uid`** yourself. It is 30 characters, no spaces: `yyyyMMddHHmmssSSS` followed by a 13-character author code.
   - **Time:** local time now, to the millisecond, not UTC. Use the `timezone` in the directing person's note in `99_System/04_People` if it has one; otherwise `defaultTimezone` in `authors.yaml`.
   - **Author code, if a user directed the note:** that user's `code`, from their note in `99_System/04_People`. This applies even if you wrote every word. If you do not know who the user is, ask. A person may have `previousCodes` in their note: notes carrying those codes are also theirs.
   - **Author code, if you created the note on your own with no direct instruction:** your own code from `ai_authors` in `authors.yaml`. If your tool is not listed, add it: tool name (lowercase letters, at most 11), then `ai`, then hyphens to 13 characters.
   - **If another note or Local Model record already uses that 30-character identity token,** add one millisecond until it is globally unique in the vault.
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

- Do not edit generated release files: `99_System/06_Fileclasses/`, `.obsidian/plugin-lock.yaml`, `.obsidian/community-plugins.json` or any plugin `data.json`. They come from the schemas through the release scripts (W-322). Never add, update or remove plugins.

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
- Keep model-content folders at or below 75 generated model files. When a folder would exceed 75, create a meaningful semantic or navigational subdivision based on actual engineering/source structure; never create arbitrary numbered overflow buckets.

## Local occurrences

- Reuse the authoritative Object/Port/Item Flow definition rather than duplicating it for each contextual use (W-293, W-294).
- When a reusable Object/assembly is used inside another Object/system and that specific use must be distinguished, model the use as a local part occurrence owned by the containing context. Its reusable semantic source is `definition`, not `subtypeOf`.
- A contextual endpoint occurrence belongs to the Object/part occurrence on which it exists. A local connection belongs to the lowest meaningful common configuration context that brings its endpoint occurrences together. Local flows belong to that connection.
- A Requirement may keep `appliesTo` when its true target is an addressable local occurrence. Do not invent a new relationship solely because the target is contained.
- Local endpoint/flow roles are `transmit`, `receive`, `exchange` or `unspecified`.
- Use `local-model.yaml` as the canonical contained-record contract. New Local Model writing uses schema 0.2. Local IDs are native block IDs `part-<token>`, `ep-<token>`, `conn-<token>`, or `flow-<token>`, where `<token>` is a globally unique 30-character identity token. Part/endpoint `usage` may be `standard`, `variant`, or `option`; omission means `standard`. Do not put `usage` on connections or flows.
- Do not create a standalone note merely to preserve a contextual occurrence if stable local addressability is sufficient; promotion of a local occurrence to a note is an explicit modeling decision, never an importer inference.



## Sparse optional properties

`element-types.yaml` may declare governed sparse optional properties. Currently:
- `abstract: true` may be used on a reusable definition when the definition organizes/generalizes a specialization family but is not itself a selectable effective definition.
- absence means false;
- explicit `abstract: false` is valid but canonical writing omits it;
- abstractness is not inherited.

## Identity namespace

The 30-character token used by a note `uid` and by a Local Model block ID belongs to one global identity namespace. Never allocate a token already used by any note or Local Model record. The local kind prefix is representation metadata, not a separate uniqueness namespace.
