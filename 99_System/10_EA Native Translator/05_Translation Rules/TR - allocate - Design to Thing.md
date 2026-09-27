---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "allocate"
sourcePattern: "Design → Thing"
targetMapping: "Design designOf Thing / Thing hasDesign Design"
disposition: "Direct"
---
# allocate - Design to Thing

## Rule

Translate allocation as design ownership when source element is semantically Design.

## Source pattern

- EA relationship: [[EA Relationship - allocate]]
- Endpoint pattern: `Design → Thing`

## Target

`Design designOf Thing / Thing hasDesign Design`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
