---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 11
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 11 — allocate — Design allocation

## Source pattern

- **EA Connector:** allocate
- **EA Stereotype / Pattern:** Design allocation
- **Source Endpoint Semantics:** Thing
- **Target Endpoint Semantics:** Design

## MDSE relationship

- **Source YAML Relationship:** hasDesign
- **Target YAML Inverse:** designOf

## Transformation rule

Normalize Design↔Thing allocation to Thing hasDesign / Design designOf.

## Body detail rule

Preserve connector metadata in body if present.

## Status

Settled

## Review trigger

Source/target orientation differs; meaning unclear

## Source basis / notes

Approved designOf/hasDesign pair.
