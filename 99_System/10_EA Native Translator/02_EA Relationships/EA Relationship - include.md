---
uid:
type: EA Relationship
status: Working
eaConnector: "include"
translationStatus: "Endpoint dependent"
---
# include

## Current mapping

Use Case→Use Case required decomposition; Use Case→Function realizedBy; otherwise review

## Rule

The connector name alone is not sufficient when endpoint semantics change meaning. Endpoint-specific deterministic behavior belongs in Translation Rule notes.

## Unresolved handling

When no approved semantic mapping applies, preserve source direction with the current `map*Out / map*In` migration-evidence convention rather than inventing MDSE semantics.
