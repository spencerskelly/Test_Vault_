---
uid: 20260930174529866skellyspencer
id: INFO-00066
status: Active
property: exposes
appliesTo: 
required: No
setBy: By hand (Post-Import Task 8 and new modeling); the inverse is generated
canChange: 
---
# exposes

exposes/exposedBy says one Port is also exposed at a higher level of the system: a circuit's antenna port, the PCBA's antenna port and the product's antenna port are the same port at three levels (W-281). Port to Port. Nothing in the import writes it; Post-Import Task 8 turns the temporary `equals` into `exposes`, or into `interfaces` when it is not an exposure.

## Direction

Written on the outer Port, pointing at the inner Port. The inverse `exposedBy` is generated on the inner Port and kept out of the way (W-126).

## Where it sits

After `tags`, in the order of `relationships.yaml` (W-126), after `hasFlow`. It may hold several values.

## Inverse

`exposedBy`
