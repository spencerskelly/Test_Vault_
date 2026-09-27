---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Association"
sourcePattern: "Info ↔ Thing"
targetMapping: "describes"
disposition: "Direct"
---
# Association - Info and Thing

## Rule

Normalize to Info describes Thing.

## Source pattern

- EA relationship: [[EA Relationship - Association]]
- Endpoint pattern: `Info ↔ Thing`

## Target

`describes`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
