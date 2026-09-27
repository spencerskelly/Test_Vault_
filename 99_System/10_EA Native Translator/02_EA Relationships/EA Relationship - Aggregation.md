---
uid:
type: EA Relationship
status: Working
eaConnector: "Aggregation"
translationStatus: "Endpoint dependent"
---
# Aggregation

## Current mapping

Thing→Thing: partOf; Function→Function: parent/hasChild; other patterns review/map evidence

## Rule

The connector name alone is not sufficient when endpoint semantics change meaning. Endpoint-specific deterministic behavior belongs in Translation Rule notes.

## Unresolved handling

When no approved semantic mapping applies, preserve source direction with the current `map*Out / map*In` migration-evidence convention rather than inventing MDSE semantics.
