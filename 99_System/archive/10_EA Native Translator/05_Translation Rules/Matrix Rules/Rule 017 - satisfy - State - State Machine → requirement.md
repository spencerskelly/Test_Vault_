---
uid:
type: Translation Rule
status: "Deferred"
matrixRuleId: 17
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 17 — satisfy — State / State Machine → requirement

## Source pattern

- **EA Connector:** satisfy
- **EA Stereotype / Pattern:** State / State Machine → requirement
- **Source Endpoint Semantics:** State / State Machine
- **Target Endpoint Semantics:** Requirement

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Do not auto-map in the new native importer until current satisfaction scope is reconfirmed against the latest metamodel.

## Body detail rule

Preserve connector evidence in body/source.

## Status

Deferred

## Review trigger

Any occurrence

## Source basis / notes

Older translator allowed it; later project direction restricted satisfaction to Function/Design.
