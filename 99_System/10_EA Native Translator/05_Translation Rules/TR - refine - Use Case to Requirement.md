---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "refine"
sourcePattern: "Use Case → Requirement"
targetMapping: "drives / drivenBy"
disposition: "Direct"
---
# refine - Use Case to Requirement

## Rule

Use Case explains why the Requirement exists. This intentionally does not use refines.

## Source

- EA relationship: [[EA Relationship - refine]]
- Endpoint pattern: `Use Case → Requirement`

## Target

`drives / drivenBy`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
