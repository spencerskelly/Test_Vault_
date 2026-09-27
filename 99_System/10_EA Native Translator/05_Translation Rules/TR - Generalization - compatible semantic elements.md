---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Generalization"
sourcePattern: "specific → general"
targetMapping: "subtypeOf / supertypeOf"
disposition: "Direct"
---
# Generalization - compatible semantic elements

## Rule

Preserve specialization semantics. EA source is the specific element; destination is the general element.

## Source

- EA relationship: [[EA Relationship - Generalization]]
- Endpoint pattern: `specific → general`

## Target

`subtypeOf / supertypeOf`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
