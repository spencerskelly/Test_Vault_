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

## Why it is laid out this way

Everything below the GUID line is unreviewed source data. Once the values have been reviewed, the cleanup deletes what has no value, and the GUID line is left as the last line of the note. Keeping it all in one place, below the GUID, makes that a simple, safe sweep for a person or an AI.

Related: [[id]]
