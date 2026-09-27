---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Association"
sourcePattern: "Issue ↔ Thing"
targetMapping: "affects"
disposition: "Direct"
---
# Association - Issue and Thing

## Rule

Normalize to Issue affects Thing.

## Source pattern

- EA relationship: [[EA Relationship - Association]]
- Endpoint pattern: `Issue ↔ Thing`

## Target

`affects`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
