---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Aggregation"
sourcePattern: "Thing → Thing"
targetMapping: "partOf / hasPart"
disposition: "Direct"
---
# Aggregation - Thing to Thing

## Rule

Treat structural Thing aggregation as part-whole. Preserve multiplicity separately when meaningful.

## Source

- EA relationship: [[EA Relationship - Aggregation]]
- Endpoint pattern: `Thing → Thing`

## Target

`partOf / hasPart`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
