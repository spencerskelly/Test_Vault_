---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 3
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 3 — Aggregation — Function decomposition

## Source pattern

- **EA Connector:** Aggregation
- **EA Stereotype / Pattern:** Function decomposition
- **Source Endpoint Semantics:** Child Function
- **Target Endpoint Semantics:** Parent Function

## MDSE relationship

- **Source YAML Relationship:** parent
- **Target YAML Inverse:** child

## Transformation rule

Function aggregation means decomposition, not physical partOf.

## Body detail rule

Preserve role/multiplicity/constraints if present.

## Status

Settled

## Review trigger

If child is actually specialization rather than decomposition

## Source basis / notes

Approved Function→Function aggregation rule.
