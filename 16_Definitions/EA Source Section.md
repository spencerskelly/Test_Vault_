---
uid: 20260928101352000skellyspencer
id: INFO-00017
status: Active
---
# EA Source Section

The last section of every note that was translated from EA. It traces the note back to its original EA element and keeps source values that might still be useful. Notes created in the vault, not translated from EA, do not have it.

## Layout

The section starts with its heading. A `Name` line comes first when one is needed, then the `EA GUID` line. Everything else taken from EA goes below the GUID. Three empty lines separate the section from the rest of the note (W-99). The whole note is laid out in [[Note Layout]].

```
## Source: EA
Name: <original name>
EA GUID: {D2B8F0A4-...}

- Part Number: 4050030
- id: DG_0307_001_02
- SysML1.4::id: CC115
- Applicability Comment: Only for DC charging
```

## Rules

- The `Name` line is written only when a name has to be kept (for example, the file name differs from the EA name). Its exact format is not decided.
- The line `EA GUID:` comes next. It is for tracing back to the original element and is not used for anything else.
- Below it, one line per value in the form `- <EA tag name>: <value>`, using the tag name exactly as it was in EA, in the order set in [[Note Layout]] (W-101, W-104).
- A line is written only when EA had a real value. Placeholders such as `unassigned` and `<memo>`, and empty values, are left out.
- Values that were moved into a property of the note are not repeated here.
- Values that are written as normal text higher in the note are not repeated here: the Note, `text` wording, `User Story`, `Sales Comment`, `Product Management Comment`, `Engineering Comment`, and any multi-line `Priority` value (W-102, W-104, W-106). No tag line contains a line break.

## Order below the GUID (W-208)

1. The element's own EA values: the `Alias` line, then the tag lines in the order set in [[Note Layout]].
2. Values from EA structure on the element: `quantity of`, then the State action lines and the Class `Attribute:` lines, then the link lines (`Represents:`, `Target pin:` and the inverse forms), then the merged-Port lines (`Instance name in`, `Instance type in`, `Instance stereotype in`, `Instance redefinition in`).
3. Connector values.
4. Discussion posts.
5. `REVIEW port needed`, always the last line of the section.

## Lines decided since the layout was set

These are the kinds of line the translator writes in this section, or near it, as decided in the Workspace Decision Log. Each is written only when EA had a real value.

- `- Name: <original>` when the file name differs from the EA name, for example unsafe characters or a duplicate counter (W-48, W-71).
- `- Alias: <value>`, often a manufacturer part number (W-42).
- No `- Designator:` line is written; standards take `STD-#####` and the designator stays in the note name (W-203, replacing W-82).
- `quantity of <child> is: <value>` on an assembly, one line per Part or connector that gives a quantity (W-43, W-54).
- A discussion post on a requirement, one line each with author and date (W-75).
- `- Entry action:`, `- Do action:` or `- Exit action:` followed by the name, on a State (W-86), and `- Attribute: <name> (<type>)` on a Class (W-86). Links from `t_xref` are lines on both ends (W-194): `- Entry action:`, `- Do action:`, `- Represents:`, `- Target pin:` and the inverse forms `- Entry action of:`, `- Do action of:`, `- Represented by:`, `- Target pin of:`.
- On a block Port note, one line per real value that differed on a merged instance Port (W-121, W-211): `- Instance name in [[<assembly>]]: <value>`, `- Instance type in [[<assembly>]]: [[<Port note>]]`, `- Instance stereotype in [[<assembly>]]: <value>`, `- Instance redefinition in [[<assembly>]]: [[<Port note>]]`, with `(part <name>)` after the assembly link when the Part has a role name.
- Connector values (Name, Notes, trigger, guard, effect): on both end notes for Connector and InformationFlow, on the owner-side note for other types (W-55, W-56, W-61).
- `- REVIEW port needed: ...` on both ends of a flow connector that was drawn on a block instead of a port; it is deleted when the connector is moved to a port (W-55, Task 1 in `Post-Import Tasks.md`).

Some placements sit outside this section. An element's own description (its Note) is the main text at the top of the body, and a package's Notes and a diagram's Notes likewise (W-42, W-66, W-71). A `Default diagram: [[...]]` line sits in a marked block below the main text and above this section, and is written only when the diagram's canvas exists (W-80). Linked documents are attached as files next to the note, named `<note file name> asset <n>`, and are not lines in this section (W-76, W-77, W-78).

## Definitions of the kept body lines (W-93, W-209)

One table for the tag values kept in the model. The first 16 rows are inline lines below the GUID, written as `- <name>: <value>`; the last four are comment texts written as labeled normal text higher in the note (W-104, W-105). Counts are rows with a real value in `t_objectproperties_raw.csv` (empty values, `unassigned` and `<memo>` placeholders left out; for memo tags the text in `Notes`). The meaning column holds only what Spencer has said; the rest is blank until he gives it. The table is temporary: it is removed with the lines it defines when the review cleanup deletes them.

| Line | Meaning | Rows | Example value |
|---|---|---|---|
| `Webasto MBDV Profile::Priority` | MoSCoW priority of a requirement; some values also carry the MoSCoW legend (W-106). | 118 | This column categorizes requirements usi |
| `Applicability Comment` | No meaning given yet. | 45 | IP54, IP55 |
| `Webasto MBDV Profile::Applicability Comment` | No meaning given yet. | 11 | Is it one measure or all? |
| `source` | No meaning given yet. | 2 | UL 2594 |
| `Webasto MBDV Profile::External Reference` | No meaning given yet. | 2 | Annex A |
| `MFG PN` | No meaning given yet. | 101 | 6374G1 |
| `Part Number` | No meaning given yet. | 11 | 5910203 |
| `PN Change Level` | No meaning given yet. | 3 | A |
| `Brand` | No meaning given yet. | 6 | Anderson Power Product |
| `CMF` | No meaning given yet. | 15 | FASSON 72825T,50 MICRON WHITE PET TC/S33 |
| `Material` | No meaning given yet. | 1 | PC |
| `Weight (g)` | No meaning given yet. | 2 | 1 |
| `Piece Cost` | Cost of one piece, in US dollars (Spencer, W-93). | 6 | 15.99 |
| `Quantity` | Likely the number of pieces in a kit; 10 rows, not confirmed for each (Spencer, W-93). | 10 | 4 |
| `Positions` | No meaning given yet. | 1 | 6 |
| `Style` | No meaning given yet. | 13 | DV |
| `User Story` | No meaning given yet. | 118 | This column explains why the requirement |
| `Sales Comment` | No meaning given yet. | 4 | We'll want to add the ability for users  |
| `Product Management Comment` | No meaning given yet. | 37 | This objective aligns with market demand |
| `Engineering Comment` | No meaning given yet. | 10 | Maybe we can follow the ProCore edge dis |

## Why it is laid out this way

Everything below the GUID line is unreviewed source data. Once the values have been reviewed, the cleanup deletes what has no value, and the GUID line is left as the last line of the note (the `Name` line goes with the other reviewed values). Keeping it all in one place, below the GUID, makes that a simple, safe sweep for a person or an AI.

Related: [[Note Layout]], [[id]]
