---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Dependency"
sourcePattern: "Behavior → prerequisite Behavior"
targetMapping: "dependsOn"
disposition: "Semantic"
---
# Dependency - behavior prerequisite

## Rule

Use only when the source relationship genuinely means prerequisite/reliance. Execution order belongs in Functional Flow topology.

## Source pattern

- EA relationship: [[EA Relationship - Dependency]]
- Endpoint pattern: `Behavior → prerequisite Behavior`

## Target

`dependsOn`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
