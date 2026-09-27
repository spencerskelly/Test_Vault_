---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 10
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 10 — allocate — Function allocation

## Source pattern

- **EA Connector:** allocate
- **EA Stereotype / Pattern:** Function allocation
- **Source Endpoint Semantics:** Thing
- **Target Endpoint Semantics:** Function

## MDSE relationship

- **Source YAML Relationship:** performs
- **Target YAML Inverse:** performedBy

## Transformation rule

Reverse EA Function→Thing allocation into Thing performs Function.

## Body detail rule

Preserve connector metadata in body if present.

## Status

Settled

## Review trigger

Allocation endpoints do not read as performer/behavior

## Source basis / notes

Approved allocate semantic mapping.
