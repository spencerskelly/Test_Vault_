---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 2
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 2 — Aggregation — Composite/shared

## Source pattern

- **EA Connector:** Aggregation
- **EA Stereotype / Pattern:** Composite/shared
- **Source Endpoint Semantics:** Thing
- **Target Endpoint Semantics:** Thing

## MDSE relationship

- **Source YAML Relationship:** partOf
- **Target YAML Inverse:** hasPart

## Transformation rule

Collapse EA composite/shared distinction to structural containment.

## Body detail rule

Preserve role/multiplicity/constraints in endpoint bodies.

## Status

Settled

## Review trigger

Physical Context exception; endpoint semantics not structural

## Source basis / notes

Normal Thing structural aggregation.
