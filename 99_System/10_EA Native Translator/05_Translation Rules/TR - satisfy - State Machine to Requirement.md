---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "satisfy"
sourcePattern: "State Machine → Requirement"
targetMapping: "Requirement appliesTo State Machine"
disposition: "Direct"
---
# satisfy - State Machine to Requirement

## Rule

State Machine does not satisfy Requirements. Preserve the EA trace as applicability/scope.

## Source pattern

- EA relationship: [[EA Relationship - satisfy]]
- Endpoint pattern: `State Machine → Requirement`

## Target

`Requirement appliesTo State Machine`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
