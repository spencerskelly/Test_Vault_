---
uid:
type: Translation Rule
status: Settled
sourceRelationship: "Any unresolved connector"
sourcePattern: "unapproved endpoint pattern"
targetMapping: "map<EAConnectorName>Out / map<EAConnectorName>In"
disposition: "Preserve Evidence"
---
# Unresolved connector preservation

## Rule

Store Out on original EA source and In on original target. Preserve direction exactly; replace once semantics are approved.

## Source pattern

- EA relationship: Any unresolved connector
- Endpoint pattern: `unapproved endpoint pattern`

## Target

`map<EAConnectorName>Out / map<EAConnectorName>In`

## Implementation expectation

Apply after semantic endpoint classification. If the endpoint pattern does not match, do not force this rule; use the connector-family fallback/review behavior.
