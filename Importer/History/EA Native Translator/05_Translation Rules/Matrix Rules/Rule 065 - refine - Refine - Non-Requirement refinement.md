---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 65
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 65 — refine / Refine — Non-Requirement refinement

## Source pattern

- **EA Connector:** refine / Refine
- **EA Stereotype / Pattern:** Non-Requirement refinement
- **Source Endpoint Semantics:** Any element where both endpoints are not Requirements
- **Target Endpoint Semantics:** Any semantic element

## MDSE relationship

- **Source YAML Relationship:** describes
- **Target YAML Inverse:** describedBy

## Transformation rule

All explicit refinement outside Requirement→Requirement is normalized to describes / describedBy.

## Body detail rule

Preserve connector notes if useful.

## Status

Settled

## Review trigger

Both endpoints are Requirements; use rule 22

## Source basis / notes

Implements the approved vocabulary simplification across SysML and Standard Profile refine variants.
