---
uid: 20260930133525655skellyspencer
id: INFO-00052
status: Active
property: affects
usedOn: see relationships.yaml
required: No
setBy: Translator (translated notes) or by hand; the inverse is generated
canChange: 
---
# affects

affects/affectedBy: the source has an impact on a target that exists anyway, good or bad. Written by an Issue, a Failure Mode or a Use Case (normal use that loads or wears a part) on the element it affects (W-166, W-240, W-284). It differs from `drives`, where the target exists or happens because of the source.

## Direction

Written on the note that holds the field. The inverse `affectedBy` is generated on the other note and kept out of the way (W-126).

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126). It may hold several values.

## Inverse

`affectedBy`
