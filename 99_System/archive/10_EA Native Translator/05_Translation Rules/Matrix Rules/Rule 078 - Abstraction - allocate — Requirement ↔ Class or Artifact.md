---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 78
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 78 — Abstraction — allocate — Requirement ↔ Class or Artifact

## Source pattern

- **EA Connector:** Abstraction
- **EA Stereotype / Pattern:** allocate — Requirement ↔ Class or Artifact
- **Source Endpoint Semantics:** Requirement (either EA endpoint)
- **Target Endpoint Semantics:** Class or Artifact (other endpoint)

## MDSE relationship

- **Source YAML Relationship:** appliesTo
- **Target YAML Inverse:** applies

## Transformation rule

Normalize EA orientation: Requirement appliesTo Class/Artifact; Class/Artifact applies Requirement.

## Body detail rule

Preserve connector notes/roles/multiplicity/constraints in endpoint bodies when meaningful.

## Status

Settled

## Review trigger

Other endpoint is not Class or Artifact

## Source basis / notes

25 observed Requirement↔Class/Artifact allocate connectors.
