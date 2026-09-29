---
uid: 20260928101352000skellyspencer
id: INFO-00017
type: Info
subtype: Guide
status: Active
---
# EA Source Section

The last section of every note that was translated from EA. It traces the note back to its original EA element and keeps source values that might still be useful. Notes created in the vault, not translated from EA, do not have it.

## Layout

The EA GUID comes first. Everything else taken from EA goes below it.

```
## Source: EA
EA GUID: {D2B8F0A4-...}

- EA id: DG_0307_001_02
- SysML1.4 id: CC115
- Applicability Comment: Only for DC charging
```

## Rules

- The line `EA GUID:` is always the first line of the section. It is for tracing back to the original element and is not used for anything else.
- Below it, one line per value in the form `- <EA tag name>: <value>`, using the tag name exactly as it was in EA.
- A line is written only when EA had a real value. Placeholders such as `unassigned` and `<memo>`, and empty values, are left out.
- Values that were moved into a property of the note are not repeated here.

## Lines decided since the layout was set

These are the kinds of line the translator writes in this section, or near it, as decided in the Workspace Decision Log. Each is written only when EA had a real value.

- `- Name: <original>` when the file name differs from the EA name, for example unsafe characters or a duplicate counter (W-48, W-71).
- `- Alias: <value>`, often a manufacturer part number (W-42).
- `- Designator: <value>` on a requirement whose external designator is shared with another note and so could not be its `id` (W-82).
- `quantity of <child> is: <value>` on an assembly, one line per Part or connector that gives a quantity (W-43, W-54).
- A discussion post on a requirement, one line each with author and date (W-75).
- `- Entry action:`, `- Do action:` or `- Exit action:` followed by the name, on a State (W-86), and `- Attribute: <name> (<type>)` on a Class (W-86).
- Connector values (Name, Notes, trigger, guard, effect): on both end notes for Connector and InformationFlow, on the owner-side note for other types (W-55, W-56, W-61).
- `- REVIEW port needed: ...` on both ends of a flow connector that was drawn on a block instead of a port; it is deleted when the connector is moved to a port (W-55, Task 1 in `Post-Import Tasks.md`).

Two placements sit outside this section. An element's own description (its Note) is the main text at the top of the body, and a package's Notes and a diagram's Notes likewise (W-42, W-66, W-71). A `Default diagram: [[...]]` line sits in a marked block below the main text and above this section, and is written only when the diagram's canvas exists (W-80). Linked documents are attached as files next to the note, named `<note file name> asset <n>`, and are not lines in this section (W-76, W-77, W-78).

## Why it is laid out this way

Everything below the GUID line is unreviewed source data. Once the values have been reviewed, the cleanup deletes what has no value, and the GUID line is left as the last line of the note. Keeping it all in one place, below the GUID, makes that a simple, safe sweep for a person or an AI.

Related: [[id]]
