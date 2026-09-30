---
type: Info
subtype: Guide
id: INFO-00022
uid: 20260928221439139skellyspencer
status: Active
tags:
---
# Note Layout

The order of everything in a note that was translated from EA. Every translated note follows it, so a person or an AI always knows where to look. Notes made by hand use the same order for the parts they have. The `Source: EA` section is described in [[EA Source Section]].

## Order

1. **Properties.** `type`, `subtype`, `id`, `uid`, `status`, `eaType`, `tags`, in that order (W-97), then the relationship fields, in the order they appear in `relationships.yaml` (W-126). `tags` and the relationship fields may hold more than one value; the other properties hold one each.
2. **Note.** The element's own description, as normal text (W-42). A package's or a diagram's Notes go here too.
3. **`text` wording.** Where EA held a `text` or `SysML1.4::text` value, it follows the Note after one blank line, with no label. Where the Note is empty, it is the Note (W-102, W-103).
4. **Comment texts.** `User Story`, `Sales Comment`, `Product Management Comment` and `Engineering Comment`, in that order, as normal text. Each has its own label (W-104, W-105, W-106).
5. **EA notes.** EA Notes that were linked to this element alone (W-161), under one label `**EA notes:**`, one bullet per note in EA creation order: `- <date>, <author>: <text>`. The date is the note's EA creation date (yyyy-MM-dd); the author is the person's name from their person note, found by the EA name, else the EA author as written, else `unknown`. A note of several lines continues as an indented block under its bullet; a note with no text is left out (W-162).
6. **User section.** Room for information people add: an empty `## Notes` heading, with nothing under it, written on every translated note (W-206).
7. **Aliases and `formerIds`.** Other names for the note and its earlier `id` values, directly below the user section (W-110, W-111). Their heading and line format are not decided.
8. **Multi-line `Priority` values.** A `Webasto MBDV Profile::Priority` value that contains a line break, as normal text with a label (W-106).
9. **`Source: EA`.** The traceability section, always last. Three empty lines come before it (W-99).

Attachments are files next to the note, not lines in it (W-76, W-77).

## Labels

A label is the EA tag name in bold with a colon, on its own line. The value starts on the next line and may run over several lines, written as it was in EA. A blank line separates one labeled text from the next.

```
**User Story:**
Airport operators need full-scale reports to:
- Analyze overall energy consumption patterns
- Justify future infrastructure expansion
```

Only real values are written. A tag that was empty or held a placeholder (`unassigned`, `<memo>`) writes nothing.

## Example

```
---
type: <MDSE type>
subtype: <MDSE subtype>
id: <id>
uid: <uid>
status: <status>
eaType: <EA stereotype, else EA object type>
tags:
<relationship fields, in the order of relationships.yaml, when the note has them>
---
<Note text>

<text wording, when both a Note and text exist>

**User Story:**
<value>

**Sales Comment:**
<value>

**EA notes:**
- 2025-01-29, Herman Montano: Use an installation file via the mobile app, or laptop.
- 2025-02-18, Herman Montano: Configure all common charger parameters at once,
  then configure the specific ones for each charger.

<user section, empty for now>

<aliases and formerIds>

**Webasto MBDV Profile::Priority:**
<first line>
<second line>



## Source: EA
Name: <original name, only when the file name differs>
EA GUID: {...}

- Part Number: <value>
- id: <value>
- MFG PN: <value>
```

## Tag lines in the `Source: EA` section

Below the `EA GUID` line, one line per value as `- <EA tag name>: <value>` (W-28, W-93), in this order, group by group (W-101, W-104). The order is stored as `order` in `ea-tag-dispositions.yaml`.

1. Identity: `Part Number (from PN and PartNumber)`, `PN Change Level`, `id`, `SysML1.4::id`, `Brand`, `MFG PN`
2. Requirements: `source`, `Webasto MBDV Profile::External Reference`, `Webasto MBDV Profile::Priority`, `Applicability Comment`, `Webasto MBDV Profile::Applicability Comment`, `verifyMethod`
3. Physical and cost: `Positions`, `Style`, `CMF`, `Material`, `Weight (g)`, `Quantity`, `Piece Cost`
4. Electrical: `PowerMax`, `Current Max`, `CurrentOutMax`, `VoltageInMin`, `VoltageInMax`, `VoltageOutMin`, `VoltageOutMax`, `Cable Compatibility`, `SignalType`
5. Failure mode: `Severity`, `Occurence`, `Detection`

`PN` and `PartNumber` share one `- Part Number:` line; they never occur on the same element.

## File names (W-196, W-197)

A note file name and a package folder name are the EA name with these changes, in order: `/` to `-`; `:` to ` -`; `?` and `*` removed; `"` to `''`; `<` to `(` and `>` to `)`; `|` and `\` to `-`; `[` to `(`, `]` to `)`, `#` to `no.`, `^` removed (W-205); each run of line breaks, control characters and spaces to one space; leading spaces and trailing spaces and periods trimmed. When the file name differs from the EA name, the `Name:` line keeps the original (W-48). Where two or more notes would get the same file name, case ignored, across the vault, every one of those notes adds its `id` after the name, one space between, for example `Start charge ACT-00456`; a note with a unique name keeps it (W-198, W-199). The `id` is whatever the note gets: always an internal one such as `ACT-00456` or `STD-00456` (W-203). Ports, pins and unnamed elements keep their own counters (W-134, W-138, W-145). Diagram names are not decided.

## Not decided yet

- The heading and line format of the aliases and `formerIds`.
- Where the `Default diagram` block (W-80) sits among the seven parts.
- The exact format of the `Name` line, and where it sits against the `Source: EA` heading (W-99).
- The order of other lines in `Source: EA` relative to the tag lines (connector values, `Alias`, `Designator`, `quantity of`, discussion posts, State and Class lines, `REVIEW port needed`).
- The `Definitions` of the kept body lines (W-93).

Related: [[EA Source Section]], [[id]], [[uid]], [[eaType]]
