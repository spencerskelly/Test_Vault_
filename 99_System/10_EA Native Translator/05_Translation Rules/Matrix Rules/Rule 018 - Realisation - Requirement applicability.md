---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 18
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 18 — Realisation — Requirement applicability

## Source pattern

- **EA Connector:** Realisation
- **EA Stereotype / Pattern:** Requirement applicability
- **Source Endpoint Semantics:** Requirement
- **Target Endpoint Semantics:** Applicable semantic element

## MDSE relationship

- **Source YAML Relationship:** appliesTo
- **Target YAML Inverse:** applies

## Transformation rule

Convert Thing/Document/Firmware→Requirement Realisation into Requirement appliesTo endpoint.

## Body detail rule

Preserve connector detail in bodies if present.

## Status

Settled

## Review trigger

Realisation is clearly implementation rather than applicability

## Source basis / notes

Current conservative mapping.
