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

1. **Properties.** `type`, `subtype`, `id`, `uid`, `status`, `eaType`, `tags`, in that order (W-97). Only `tags` may hold more than one value.
2. **Note.** The element's own description, as normal text (W-42). A package's or a diagram's Notes go here too.
3. **`text` wording.** Where EA held a `text` or `SysML1.4::text` value, it follows the Note after one blank line, with no label. Where the Note is empty, it is the Note (W-102, W-103).
4. **Comment texts.** `User Story`, `Sales Comment`, `Product Management Comment` and `Engineering Comment`, in that order, as normal text. Each has its own label (W-104, W-105, W-106).
5. **User section.** Room for information people add. Its name and content are not decided; the translator writes nothing here.
6. **Aliases.** Other names for the note, directly below the user section (W-110). Its heading and line format are not decided.
7. **Multi-line `Priority` values.** A `Webasto MBDV Profile::Priority` value that contains a line break, as normal text with a label (W-106).
8. **`Source: EA`.** The traceability section, always last. Three empty lines come before it (W-99).

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
---
<Note text>

<text wording, when both a Note and text exist>

**User Story:**
<value>

**Sales Comment:**
<value>

<user section, empty for now>

<aliases>

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

## Not decided yet

- The name and content of the user section, and the heading and line format of the aliases.
- Where `formerIds` goes (W-88 moved it to the body; W-110 places only the aliases).
- Where the `Default diagram` block (W-80) sits among the seven parts.
- The exact format of the `Name` line, and where it sits against the `Source: EA` heading (W-99).
- The order of other lines in `Source: EA` relative to the tag lines (connector values, `Alias`, `Designator`, `quantity of`, discussion posts, State and Class lines, `REVIEW port needed`).
- The `Definitions` of the kept body lines (W-93).

Related: [[EA Source Section]], [[id]], [[uid]], [[eaType]]
