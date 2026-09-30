---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 62
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 62 — Unrecognized relationship type — Any source relationship not listed above

## Source pattern

- **EA Connector:** Unrecognized relationship type
- **EA Stereotype / Pattern:** Any source relationship not listed above
- **Source Endpoint Semantics:** Any
- **Target Endpoint Semantics:** Any

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not silently ignore. Capture in relationship traceability / exception output and require an explicit mapping, ignore rule, or deferral before final import.

## Body detail rule

Preserve raw relationship type, stereotype, direction, endpoint identities, and populated metadata.

## Status

Review

## Review trigger

Always

## Source basis / notes

Global completeness safeguard for relationship types not yet identified in the rule set.
