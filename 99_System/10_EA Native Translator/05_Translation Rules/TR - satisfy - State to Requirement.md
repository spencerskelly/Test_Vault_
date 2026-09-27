---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "satisfy"
sourcePattern: "State → Requirement"
targetMapping: "Requirement appliesTo State"
disposition: "Direct"
---
# satisfy - State to Requirement

## Rule

State does not satisfy Requirements. Preserve the EA trace as applicability/scope.

## Source pattern

- EA relationship: [[EA Relationship - satisfy]]
- Endpoint pattern: `State → Requirement`

## Target

`Requirement appliesTo State`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
