---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "refine"
sourcePattern: "Requirement → Requirement"
targetMapping: "refines / refinedBy"
disposition: "Direct"
---
# refine - Requirement to Requirement

## Rule

Source adds precision/detail to destination Requirement.

## Source

- EA relationship: [[EA Relationship - refine]]
- Endpoint pattern: `Requirement → Requirement`

## Target

`refines / refinedBy`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
