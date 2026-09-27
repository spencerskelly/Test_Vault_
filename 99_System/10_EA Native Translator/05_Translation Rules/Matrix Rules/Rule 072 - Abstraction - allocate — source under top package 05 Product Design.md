---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 72
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 72 — Abstraction — allocate — source under top package 05 Product Design

## Source pattern

- **EA Connector:** Abstraction
- **EA Stereotype / Pattern:** allocate — source under top package 05 Product Design
- **Source Endpoint Semantics:** Any element under 05 Product Design
- **Target Endpoint Semantics:** Any allocated target

## MDSE relationship

- **Source YAML Relationship:** designOf
- **Target YAML Inverse:** hasDesign

## Transformation rule

Package-context rule takes precedence over EA source type/stereotype. Source designOf target; target hasDesign source.

## Body detail rule

Preserve connector notes/roles/multiplicity/constraints in endpoint bodies when meaningful.

## Status

Settled

## Review trigger

Source is not under 05 Product Design

## Source basis / notes

1003 observed allocate connectors in current export.
