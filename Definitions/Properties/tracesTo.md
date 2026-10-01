---
uid: 20260930133525645skellyspencer
id: INFO-00042
status: Active
property: tracesTo
usedOn: see relationships.yaml
required: No
setBy: Translator (translated notes) or by hand; the inverse is generated
canChange: 
---
# tracesTo

Migration/legacy escape hatch only. Prefer stronger semantic relationships.

## Direction

Written on the note that holds the field. The inverse `tracesFrom` is generated on the other note and kept out of the way (W-126).

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126). It may hold several values.

## Inverse

`tracesFrom`
