---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 4
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 4 — Aggregation — Context participation / aggregation

## Source pattern

- **EA Connector:** Aggregation
- **EA Stereotype / Pattern:** Context participation / aggregation
- **Source Endpoint Semantics:** Context endpoint (source or target)
- **Target Endpoint Semantics:** Participating element

## MDSE relationship

- **Source YAML Relationship:** participants
- **Target YAML Inverse:** none

## Transformation rule

Store the other endpoint in one-sided `participants` YAML on the Context element regardless of EA source/target orientation. Preserve the Context element's imported EA-derived `type`; do not convert it to Use Case / Where during native import.

## Body detail rule

If EA supplies role, multiplicity, constraint, connector name, or notes, preserve meaningful detail in the owning Context body with the participant identified.

## Status

Settled

## Review trigger

If the connector clearly represents structural containment or another stronger semantic relation rather than participation

## Source basis / notes

Intentional exception to bidirectional storage. Context→Use Case/Where conversion is a post-import model change.
