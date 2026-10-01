---
uid: 20260930174840943skellyspencer
id: INFO-00067
status: Active
property: triggeredBy
usedOn: see relationships.yaml
required: No
setBy: By hand; the inverse is generated
canChange: 
---
# triggeredBy

triggeredBy/triggers says what starts a behavior: a Function, Design or State is triggered by a Function, Design, State or Item Flow (a signal or event) (W-282). It is element-level and does not say which transition a trigger belongs to; the transition-level `Trigger`, `Guard` and `Effect` lines from EA stay in the source section of the state before (W-175). Nothing in the import writes it. It replaces the unused one-way field `trigger`.

## Direction

Written on the triggered note, pointing at what triggers it. The inverse `triggers` is generated on the other note and kept out of the way (W-126).

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126), after `precedes`. It may hold several values.

## Inverse

`triggers`
