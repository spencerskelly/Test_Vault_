---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 24
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 24 — trace — Info → element

## Source pattern

- **EA Connector:** trace
- **EA Stereotype / Pattern:** Info → element
- **Source Endpoint Semantics:** Info
- **Target Endpoint Semantics:** Described element

## MDSE relationship

- **Source YAML Relationship:** describes
- **Target YAML Inverse:** describedBy

## Transformation rule

Do not preserve trace mechanically; map only if descriptive meaning is clear.

## Body detail rule

Preserve original trace label/notes if needed.

## Status

Settled

## Review trigger

Meaning not clearly descriptive

## Source basis / notes

Approved trace semantic mapping.
