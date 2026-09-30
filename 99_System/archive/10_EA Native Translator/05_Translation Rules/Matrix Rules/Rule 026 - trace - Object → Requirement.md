---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 26
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12; terminology amended 2026-09-27"
---
# Rule 26 — trace — Object → Requirement

## Source pattern

- **EA Connector:** trace
- **EA Stereotype / Pattern:** Object → Requirement
- **Source Endpoint Semantics:** Requirement
- **Target Endpoint Semantics:** Object

## MDSE relationship

- **Source YAML Relationship:** appliesTo
- **Target YAML Inverse:** applies

## Transformation rule

Reverse semantic direction to Requirement applicability.

## Body detail rule

Preserve connector text in body if useful.

## Status

Settled

## Review trigger

Trace means something other than scope/applicability
