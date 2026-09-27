---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Aggregation"
sourcePattern: "Function → Function"
targetMapping: "parent / hasChild"
disposition: "Direct"
---
# Aggregation - Function to Function

## Rule

Function aggregation is behavior decomposition, not physical structure.

## Source

- EA relationship: [[EA Relationship - Aggregation]]
- Endpoint pattern: `Function → Function`

## Target

`parent / hasChild`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
