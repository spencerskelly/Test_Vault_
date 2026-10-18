---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 34
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12; terminology amended 2026-09-27"
---
# Rule 34 — Association / Actor link — Actor / element participation in Use Case

## Source pattern

- **EA Connector:** Association / Actor link
- **EA Stereotype / Pattern:** Actor / element participation in Use Case
- **Source Endpoint Semantics:** Use Case
- **Target Endpoint Semantics:** Actor / participating element

## MDSE relationship

- **Source YAML Relationship:** participants
- **Target YAML Inverse:** none

## Transformation rule

Store participation only on the owning Use Case. Do not write reciprocal participation YAML to the Actor/Object note.

## Body detail rule

Preserve role or connector detail in the Use Case body when meaningful.

## Status

Settled

## Review trigger

If the connector represents another approved semantic relationship rather than participation
