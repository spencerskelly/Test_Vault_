---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 31
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 31 — include — Required constituent Use Case

## Source pattern

- **EA Connector:** include
- **EA Stereotype / Pattern:** Required constituent Use Case
- **Source Endpoint Semantics:** Included Use Case
- **Target Endpoint Semantics:** Base Use Case

## MDSE relationship

- **Source YAML Relationship:** parent
- **Target YAML Inverse:** child

## Transformation rule

Use parent/child only when include is truly decomposition/required constituent behavior.

## Body detail rule

Preserve include context/condition in body.

## Status

Review

## Review trigger

Included element actually product Function or relation is not decomposition

## Source basis / notes

Include is semantic, not mechanical.
