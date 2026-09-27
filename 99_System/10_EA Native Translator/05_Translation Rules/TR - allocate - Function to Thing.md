---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "allocate"
sourcePattern: "Function → Thing"
targetMapping: "Thing performs Function"
disposition: "Direct"
---
# allocate - Function to Thing

## Rule

Normalize to the MDSE authoritative performer direction.

## Source pattern

- EA relationship: [[EA Relationship - allocate]]
- Endpoint pattern: `Function → Thing`

## Target

`Thing performs Function`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
