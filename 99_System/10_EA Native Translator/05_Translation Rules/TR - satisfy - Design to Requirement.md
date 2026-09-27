---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "satisfy"
sourcePattern: "Design → Requirement"
targetMapping: "satisfies"
disposition: "Direct"
---
# satisfy - Design to Requirement

## Rule

Design may satisfy any Requirement type under the current amended rule.

## Source

- EA relationship: [[EA Relationship - satisfy]]
- Endpoint pattern: `Design → Requirement`

## Target

`satisfies`

## Implementation expectation

Apply deterministically when the source elements have already been semantically classified into the stated endpoint types. Otherwise fall through to the connector-family review rule rather than coercing endpoint types.
