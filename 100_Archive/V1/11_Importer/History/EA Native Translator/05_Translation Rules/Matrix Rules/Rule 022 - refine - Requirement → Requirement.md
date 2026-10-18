---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 22
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 22 — refine — Requirement → Requirement

## Source pattern

- **EA Connector:** refine
- **EA Stereotype / Pattern:** Requirement → Requirement
- **Source Endpoint Semantics:** Requirement
- **Target Endpoint Semantics:** Requirement

## MDSE relationship

- **Source YAML Relationship:** refines
- **Target YAML Inverse:** refinedBy

## Transformation rule

Retain explicit refinement only when one Requirement adds precision/detail to another Requirement.

## Body detail rule

Preserve connector notes if useful.

## Status

Settled

## Review trigger

Either endpoint is not a Requirement

## Source basis / notes

Approved narrow use: Requirement→Requirement only.
