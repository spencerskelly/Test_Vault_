---
uid:
type: EA Relationship
status: Working
eaConnector: "NoteLink"
translationStatus: "Transform"
---
# NoteLink

## Current mapping

EA Note becomes Info; collapse low-reuse one-to-one note into target body; retained Info describes target

## Rule

The connector name alone is not sufficient when endpoint semantics change meaning. Endpoint-specific deterministic behavior belongs in Translation Rule notes.

## Unresolved handling

When no approved semantic mapping applies, preserve source direction with the current `map*Out / map*In` migration-evidence convention rather than inventing MDSE semantics.
