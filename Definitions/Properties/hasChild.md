---
uid: 20260930133525635skellyspencer
id: INFO-00032
status: Active
property: hasChild
usedOn: see relationships.yaml
required: No
setBy: Translator (translated notes) or by hand; the inverse is generated
canChange: 
---
# hasChild

hasPart/partOf is for Object notes only, the assembly and block relationship (W-149). hasChild/childOf is the generic parent and child link for every other nesting, written on the owner; it carries the EA owner (ParentID) of an element (W-149) and the 252 independent Nesting connectors (W-151); no placement link is written where the child is subtypeOf its owner (W-178).

## Direction

Written on the note that holds the field. The inverse `childOf` is generated on the other note and kept out of the way (W-126).

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126). It may hold several values.

## Inverse

`childOf`
