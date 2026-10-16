---
uid: 20260930133525642skellyspencer
id: INFO-00039
status: Active
property: precedes
usedOn: see relationships.yaml
required: No
setBy: Translator (translated notes) or by hand; the inverse is generated
canChange: 
---
# precedes

precedes/follows is the order of steps in a flow: precedes is written on the step before, pointing at the step after; follows is generated. Used for EA ControlFlow (W-174) and StateFlow (W-175); a guard, trigger or effect is a source-section line on the step before.

## Direction

Written on the note that holds the field. The inverse `follows` is generated on the other note and kept out of the way (W-126).

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126). It may hold several values.

## Inverse

`follows`
