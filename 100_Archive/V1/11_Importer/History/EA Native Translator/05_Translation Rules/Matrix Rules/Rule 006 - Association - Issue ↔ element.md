---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 6
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 6 — Association — Issue ↔ element

## Source pattern

- **EA Connector:** Association
- **EA Stereotype / Pattern:** Issue ↔ element
- **Source Endpoint Semantics:** Issue
- **Target Endpoint Semantics:** Any affected semantic element

## MDSE relationship

- **Source YAML Relationship:** affects
- **Target YAML Inverse:** affectedBy

## Transformation rule

Use when association clearly represents impact/affected scope.

## Body detail rule

Preserve connector detail in endpoint bodies.

## Status

Settled

## Review trigger

If association meaning is not impact

## Source basis / notes

Issue impact relation.
