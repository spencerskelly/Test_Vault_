---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 5
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 5 — Association — Use Case / Context participation

## Source pattern

- **EA Connector:** Association
- **EA Stereotype / Pattern:** Use Case / Context participation
- **Source Endpoint Semantics:** Use Case or Context endpoint (source or target)
- **Target Endpoint Semantics:** Participating Thing / Actor / external element

## MDSE relationship

- **Source YAML Relationship:** participants
- **Target YAML Inverse:** none

## Transformation rule

Store the other endpoint as one-sided local membership on the owning Use Case/Context regardless of EA source/target orientation. Do not create `subject/subjectOf` during native import.

## Body detail rule

Preserve connector label, role, notes, multiplicity, or constraints in the owning Use Case/Context body when meaningful.

## Status

Settled

## Review trigger

If the connector clearly means a different approved global semantic relationship

## Source basis / notes

Subject versus participant distinction is intentionally deferred to post-import cleanup.
