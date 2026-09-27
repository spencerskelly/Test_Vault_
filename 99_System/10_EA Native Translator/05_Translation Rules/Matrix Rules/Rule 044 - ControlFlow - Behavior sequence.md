---
uid:
type: Translation Rule
status: "Deferred"
matrixRuleId: 44
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 44 — ControlFlow — Behavior sequence

## Source pattern

- **EA Connector:** ControlFlow
- **EA Stereotype / Pattern:** Behavior sequence
- **Source Endpoint Semantics:** Behavior usage / control node
- **Target Endpoint Semantics:** Behavior usage / control node

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not create global YAML relationship between reusable Functions. Preserve local sequence/control detail in bodies until flow model is finalized.

## Body detail rule

Preserve guards/control constructs in source/target bodies.

## Status

Deferred

## Review trigger

Always

## Source basis / notes

Flow-control notes intentionally avoided.
