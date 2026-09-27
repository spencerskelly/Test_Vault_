---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 41
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 41 — Connector — Physical/logical interaction

## Source pattern

- **EA Connector:** Connector
- **EA Stereotype / Pattern:** Physical/logical interaction
- **Source Endpoint Semantics:** Source endpoint
- **Target Endpoint Semantics:** Target endpoint

## MDSE relationship

- **Source YAML Relationship:** interfaces
- **Target YAML Inverse:** interfaces

## Transformation rule

Write `interfaces` on both endpoint notes. The relationship is symmetric even though EA stores source and target.

## Body detail rule

Preserve port-to-port naming, endpoint roles, multiplicity, constraints, connector name, and notes in endpoint bodies when meaningful.

## Status

Settled

## Review trigger



## Source basis / notes

Direct native-import mapping. Plain EA Connector is represented by symmetric `interfaces`.
