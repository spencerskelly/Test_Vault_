---
uid: 20261001122036000skellyspencer
id: INFO-00068
status: Active
property: hasState
usedOn: see relationships.yaml
required: No
setBy: Hand or by AI (nothing in the import writes it yet); the inverse is generated
canChange: 
---
# hasState

A State or State Machine that an Object has, and a State that a State Machine has. Written on the Object or State Machine (W-291, W-292, restoring the pair removed in W-185). It is never `hasChild`: `hasChild` excludes Object to State, Object to State Machine and State Machine to State. The import writes it wherever an Object owns a State or State Machine, or a State Machine owns a State.

## Direction

Written on the note that holds the field, an Object or a State Machine. The inverse `stateOf` is generated on the State or State Machine and kept out of the way (W-126).

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126). It may hold several values.

## Inverse

`stateOf`
