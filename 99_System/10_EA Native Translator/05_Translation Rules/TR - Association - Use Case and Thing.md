---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Association"
sourcePattern: "Use Case ↔ Thing"
targetMapping: "hasParticipant"
disposition: "Direct"
---
# Association - Use Case and Thing

## Rule

Normalize direction to the Use Case participant relationship regardless of EA source/target orientation.

## Source pattern

- EA relationship: [[EA Relationship - Association]]
- Endpoint pattern: `Use Case ↔ Thing`

## Target

`hasParticipant`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
