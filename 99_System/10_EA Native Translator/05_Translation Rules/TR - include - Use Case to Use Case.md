---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "include"
sourcePattern: "Use Case → Use Case"
targetMapping: "hasChild / parent"
disposition: "Direct"
---
# include - Use Case to Use Case

## Rule

Included Use Case is required constituent behavior when semantic decomposition is valid.

## Source pattern

- EA relationship: [[EA Relationship - include]]
- Endpoint pattern: `Use Case → Use Case`

## Target

`hasChild / parent`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
