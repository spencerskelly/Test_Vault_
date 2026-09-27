---
uid:
type: EA Relationship
status: Working
eaConnector: "allocate"
translationStatus: "Endpoint dependent"
---
# allocate

## Current mapping

Function→Thing becomes Thing performs Function; Design→Thing becomes designOf/hasDesign; others review

## Rule

The connector name alone is not sufficient when endpoint semantics change meaning. Endpoint-specific deterministic behavior belongs in Translation Rule notes.

## Unresolved handling

When no approved semantic mapping applies, preserve source direction with the current `map*Out / map*In` migration-evidence convention rather than inventing MDSE semantics.
