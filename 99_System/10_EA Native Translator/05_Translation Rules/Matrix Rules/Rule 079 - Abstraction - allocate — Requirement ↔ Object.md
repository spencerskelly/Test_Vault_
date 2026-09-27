---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 79
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 79 — Abstraction — allocate — Requirement ↔ Object

## Source pattern

- **EA Connector:** Abstraction
- **EA Stereotype / Pattern:** allocate — Requirement ↔ Object
- **Source Endpoint Semantics:** Requirement (either EA endpoint)
- **Target Endpoint Semantics:** Object (other endpoint)

## MDSE relationship

- **Source YAML Relationship:** appliesTo
- **Target YAML Inverse:** applies

## Transformation rule

Normalize EA orientation: Requirement appliesTo Object; Object applies Requirement.

## Body detail rule

Preserve connector notes/roles/multiplicity/constraints in endpoint bodies when meaningful.

## Status

Settled

## Review trigger

Other endpoint is not Object

## Source basis / notes

2 observed Requirement↔Object allocate connectors.
