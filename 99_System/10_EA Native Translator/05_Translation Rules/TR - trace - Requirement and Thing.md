---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "trace"
sourcePattern: "Requirement ↔ Thing"
targetMapping: "Requirement appliesTo Thing"
disposition: "Direct"
---
# trace - Requirement and Thing

## Rule

Normalize direction to Requirement applicability rather than preserving generic trace.

## Source pattern

- EA relationship: [[EA Relationship - trace]]
- Endpoint pattern: `Requirement ↔ Thing`

## Target

`Requirement appliesTo Thing`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
