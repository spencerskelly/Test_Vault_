---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 13
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 13 — allocate — Information Item to behavior

## Source pattern

- **EA Connector:** allocate
- **EA Stereotype / Pattern:** Information Item to behavior
- **Source Endpoint Semantics:** Info
- **Target Endpoint Semantics:** Function / Use Case

## MDSE relationship

- **Source YAML Relationship:** describes
- **Target YAML Inverse:** describedBy

## Transformation rule

Normalize definition/detail semantics to describes / describedBy; do not create defines / definedBy.

## Body detail rule

Preserve detail in bodies.

## Status

Settled

## Review trigger

If the relationship is not actually descriptive

## Source basis / notes

Earlier conditional defines mapping is superseded. Native relationship vocabulary uses describes / describedBy.
