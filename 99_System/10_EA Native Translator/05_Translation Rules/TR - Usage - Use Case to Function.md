---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Usage"
sourcePattern: "Use Case → Function"
targetMapping: "realizedBy / realizes"
disposition: "Direct"
---
# Usage - Use Case to Function

## Rule

Current 2026-09-27 rule: approved Use Case→Function Usage maps to realization for this endpoint combination.

## Source pattern

- EA relationship: [[EA Relationship - Usage]]
- Endpoint pattern: `Use Case → Function`

## Target

`realizedBy / realizes`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
