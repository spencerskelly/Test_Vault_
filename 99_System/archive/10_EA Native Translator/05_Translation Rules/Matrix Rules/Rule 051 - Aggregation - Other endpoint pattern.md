---
uid:
type: Translation Rule
status: "Review"
matrixRuleId: 51
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 51 — Aggregation — Other endpoint pattern

## Source pattern

- **EA Connector:** Aggregation
- **EA Stereotype / Pattern:** Other endpoint pattern
- **Source Endpoint Semantics:** Any
- **Target Endpoint Semantics:** Any

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

No automatic fallback mapping. Existing structural, Function decomposition, and Context participation rules take precedence; all other Aggregation patterns require review.

## Body detail rule

Preserve roles, multiplicity, constraints, name, notes, and endpoint identities.

## Status

Review

## Review trigger

No approved Aggregation pattern matches

## Source basis / notes

Catch-all prevents silent semantic coercion.
