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

A State that an Object or a State Machine has. Written on the Object or State Machine, pointing at the State (W-291, restoring the pair removed in W-185). Nothing in the import writes it yet: States placed under an owner stay `hasChild` (W-149) until the placement rule is decided.

## Direction

Written on the note that holds the field, an Object or a State Machine. The inverse `stateOf` is generated on the State and kept out of the way (W-126).

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126). It may hold several values.

## Inverse

`stateOf`
