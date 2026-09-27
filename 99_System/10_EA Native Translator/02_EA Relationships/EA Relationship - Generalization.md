---
uid:
type: EA Relationship
status: Working
eaConnector: "Generalization"
translationStatus: "Direct for compatible semantic families"
---
# Generalization

## Current mapping

specific subtypeOf general; inverse supertypeOf

## Rule

The connector name alone is not sufficient when endpoint semantics change meaning. Endpoint-specific deterministic behavior belongs in Translation Rule notes.

## Unresolved handling

When no approved semantic mapping applies, preserve source direction with the current `map*Out / map*In` migration-evidence convention rather than inventing MDSE semantics.
