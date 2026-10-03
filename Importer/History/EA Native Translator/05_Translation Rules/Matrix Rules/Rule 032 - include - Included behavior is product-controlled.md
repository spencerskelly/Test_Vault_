---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 32
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 32 — include — Included behavior is product-controlled

## Source pattern

- **EA Connector:** include
- **EA Stereotype / Pattern:** Included behavior is product-controlled
- **Source Endpoint Semantics:** Use Case
- **Target Endpoint Semantics:** Function

## MDSE relationship

- **Source YAML Relationship:** realizedBy
- **Target YAML Inverse:** realizes

## Transformation rule

Reclassify included element as Function when it implements the scenario.

## Body detail rule

Preserve scenario/include detail in body.

## Status

Review

## Review trigger

Sequence/topology matters or relation is prerequisite only

## Source basis / notes

May need Functional Flow later.
