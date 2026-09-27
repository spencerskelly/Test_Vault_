---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "NoteLink"
sourcePattern: "retained Info → Element"
targetMapping: "describes / describedBy"
disposition: "Direct"
---
# NoteLink - retained Info

## Rule

Retain reusable/multi-target knowledge as Info and use describes.

## Source pattern

- EA relationship: [[EA Relationship - NoteLink]]
- Endpoint pattern: `retained Info → Element`

## Target

`describes / describedBy`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
