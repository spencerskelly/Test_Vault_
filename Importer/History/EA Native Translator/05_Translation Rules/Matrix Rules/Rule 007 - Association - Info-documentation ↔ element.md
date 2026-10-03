---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 7
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 7 — Association — Info/documentation ↔ element

## Source pattern

- **EA Connector:** Association
- **EA Stereotype / Pattern:** Info/documentation ↔ element
- **Source Endpoint Semantics:** Info / Document
- **Target Endpoint Semantics:** Described element

## MDSE relationship

- **Source YAML Relationship:** describes
- **Target YAML Inverse:** describedBy

## Transformation rule

Use only when source actually describes the target.

## Body detail rule

Preserve connector text if meaningful.

## Status

Settled

## Review trigger

If another approved relationship is clearly stronger; Requirement→Requirement refinement uses refines

## Source basis / notes

Default descriptive relation. `defines/definedBy` is retired into `describes/describedBy`; `refines/refinedBy` is reserved for Requirement→Requirement.
