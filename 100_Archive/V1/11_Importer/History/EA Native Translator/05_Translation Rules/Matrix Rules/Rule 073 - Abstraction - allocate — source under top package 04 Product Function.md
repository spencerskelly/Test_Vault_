---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 73
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 73 — Abstraction — allocate — source under top package 04 Product Function

## Source pattern

- **EA Connector:** Abstraction
- **EA Stereotype / Pattern:** allocate — source under top package 04 Product Function
- **Source Endpoint Semantics:** Any element under 04 Product Function
- **Target Endpoint Semantics:** Any allocated target

## MDSE relationship

- **Source YAML Relationship:** performedBy
- **Target YAML Inverse:** performs

## Transformation rule

Package-context rule takes precedence over EA source type/stereotype. Source performedBy target; target performs source.

## Body detail rule

Preserve connector notes/roles/multiplicity/constraints in endpoint bodies when meaningful.

## Status

Settled

## Review trigger

Source is not under 04 Product Function

## Source basis / notes

1410 observed allocate connectors in current export.
