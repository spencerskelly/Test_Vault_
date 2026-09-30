---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 77
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 77 — Abstraction — allocate — Requirement ↔ Activity

## Source pattern

- **EA Connector:** Abstraction
- **EA Stereotype / Pattern:** allocate — Requirement ↔ Activity
- **Source Endpoint Semantics:** Activity (either EA endpoint)
- **Target Endpoint Semantics:** Requirement (other endpoint)

## MDSE relationship

- **Source YAML Relationship:** satisfies
- **Target YAML Inverse:** satisfiedBy

## Transformation rule

Normalize EA orientation: Activity satisfies Requirement; Requirement satisfiedBy Activity.

## Body detail rule

Preserve connector notes/roles/multiplicity/constraints in endpoint bodies when meaningful.

## Status

Settled

## Review trigger

Other endpoint is not Activity/Requirement

## Source basis / notes

18 observed Requirement↔Activity allocate connectors.
