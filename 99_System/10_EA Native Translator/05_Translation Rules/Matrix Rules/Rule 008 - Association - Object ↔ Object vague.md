---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 8
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12; terminology amended 2026-09-27"
---
# Rule 8 — Association — Object ↔ Object vague

## Source pattern

- **EA Connector:** Association
- **EA Stereotype / Pattern:** Object ↔ Object vague
- **Source Endpoint Semantics:** Object
- **Target Endpoint Semantics:** Object

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not create generic Association relationship.

## Body detail rule

If connector has meaningful name/notes, preserve body detail and flag review; otherwise explicit ignore.

## Status

Review

## Review trigger

Any non-empty label/notes/roles/constraints or meaningful endpoint pattern
