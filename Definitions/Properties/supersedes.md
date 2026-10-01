---
uid: 20260930133525643skellyspencer
id: INFO-00040
status: Active
property: supersedes
usedOn: see relationships.yaml
required: No
setBy: Translator (translated notes) or by hand; the inverse is generated
canChange: 
---
# supersedes

supersedes/supersededBy is for a note that has been replaced by another note: supersedes is written on the replacing note and points at the note it replaces; supersededBy is generated on the replaced note (W-191). Nothing in the import writes it.

## Direction

Written on the note that holds the field. The inverse `supersededBy` is generated on the other note and kept out of the way (W-126).

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126). It may hold several values.

## Inverse

`supersededBy`
