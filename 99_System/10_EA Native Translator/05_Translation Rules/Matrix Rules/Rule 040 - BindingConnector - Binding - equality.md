---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 40
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 40 — BindingConnector — Binding / equality

## Source pattern

- **EA Connector:** BindingConnector
- **EA Stereotype / Pattern:** Binding / equality
- **Source Endpoint Semantics:** Endpoint A
- **Target Endpoint Semantics:** Endpoint B

## MDSE relationship

- **Source YAML Relationship:** equals
- **Target YAML Inverse:** equals

## Transformation rule

Write `equals` on both endpoint notes. BindingConnector is distinct from interaction; do not map it to `interfaces`.

## Body detail rule

Preserve bound-port naming, endpoint roles, multiplicity, constraints, connector name, and notes in endpoint bodies when meaningful.

## Status

Settled

## Review trigger



## Source basis / notes

Direct native-import mapping.
