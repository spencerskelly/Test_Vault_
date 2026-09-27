---
uid:
type: EA Relationship
status: Working
eaConnector: "satisfy"
translationStatus: "Endpoint dependent"
---
# satisfy

## Current mapping

Function or Design satisfies Requirement; State/State Machine become Requirement appliesTo; others review

## Rule

The connector name alone is not sufficient when endpoint semantics change meaning. Endpoint-specific deterministic behavior belongs in Translation Rule notes.

## Unresolved handling

When no approved semantic mapping applies, preserve source direction with the current `map*Out / map*In` migration-evidence convention rather than inventing MDSE semantics.
