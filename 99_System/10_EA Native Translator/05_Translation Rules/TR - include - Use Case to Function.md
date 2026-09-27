---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "include"
sourcePattern: "Use Case → Function"
targetMapping: "realizedBy / realizes"
disposition: "Direct"
---
# include - Use Case to Function

## Rule

Included product-controlled behavior becomes Function and realizes the external Use Case.

## Source pattern

- EA relationship: [[EA Relationship - include]]
- Endpoint pattern: `Use Case → Function`

## Target

`realizedBy / realizes`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
