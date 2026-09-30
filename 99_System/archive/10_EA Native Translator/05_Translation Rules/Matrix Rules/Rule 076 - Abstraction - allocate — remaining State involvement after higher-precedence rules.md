---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 76
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 76 — Abstraction — allocate — remaining State involvement after higher-precedence rules

## Source pattern

- **EA Connector:** Abstraction
- **EA Stereotype / Pattern:** allocate — remaining State involvement after higher-precedence rules
- **Source Endpoint Semantics:** State (either EA endpoint)
- **Target Endpoint Semantics:** Any other element

## MDSE relationship

- **Source YAML Relationship:** stateOf
- **Target YAML Inverse:** hasState

## Transformation rule

Normalize EA orientation: State stateOf the other element; the other element hasState the State. Apply only after package-context Design/Function and Issue/InformationItem rules.

## Body detail rule

Preserve connector notes/roles/multiplicity/constraints in endpoint bodies when meaningful.

## Status

Settled

## Review trigger

Neither endpoint is State, or a higher-precedence allocate rule already applies

## Source basis / notes

1044 total State-involved allocate connectors observed; only residual unmatched cases use this rule.
