---
uid:
type: EA Relationship
status: Working
eaConnector: "refine"
translationStatus: "Endpoint dependent"
---
# refine

## Current mapping

Use Case→Requirement: drives/drivenBy; Requirement→Requirement: refines/refinedBy; unresolved patterns use mapRefine*

## Rule

The connector name alone is not sufficient when endpoint semantics change meaning. Endpoint-specific deterministic behavior belongs in Translation Rule notes.

## Unresolved handling

When no approved semantic mapping applies, preserve source direction with the current `map*Out / map*In` migration-evidence convention rather than inventing MDSE semantics.
