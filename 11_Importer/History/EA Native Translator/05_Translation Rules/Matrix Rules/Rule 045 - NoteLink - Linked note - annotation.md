---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 45
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 45 — NoteLink — Linked note / annotation

## Source pattern

- **EA Connector:** NoteLink
- **EA Stereotype / Pattern:** Linked note / annotation
- **Source Endpoint Semantics:** Linked/owning element
- **Target Endpoint Semantics:** EA Note / annotation

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not create an MDSE relationship or connector note. Preserve recoverable note content in the linked/owning element body; report missing content.

## Body detail rule

Preserve note text in the linked/owning element body when recoverable; retain source traceability.

## Status

Settled

## Review trigger

Missing/unrecoverable note content

## Source basis / notes

Primary reference §6.14. NoteLink is source annotation, not an MDSE relationship.
