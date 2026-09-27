---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "satisfy"
sourcePattern: "Function → Requirement"
targetMapping: "satisfies"
disposition: "Direct"
---
# satisfy - Function to Requirement

## Rule

Function may satisfy any Requirement type when this is the best available trace.

## Source

- EA relationship: [[EA Relationship - satisfy]]
- Endpoint pattern: `Function → Requirement`

## Target

`satisfies`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
