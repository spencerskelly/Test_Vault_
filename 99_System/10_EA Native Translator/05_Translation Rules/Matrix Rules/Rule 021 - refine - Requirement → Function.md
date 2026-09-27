---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 21
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 21 — refine — Requirement → Function

## Source pattern

- **EA Connector:** refine
- **EA Stereotype / Pattern:** Requirement → Function
- **Source Endpoint Semantics:** Requirement
- **Target Endpoint Semantics:** Function

## MDSE relationship

- **Source YAML Relationship:** describes
- **Target YAML Inverse:** describedBy

## Transformation rule

Normalize non-Requirement refinement semantics to describes / describedBy.

## Body detail rule

Preserve connector notes if useful.

## Status

Settled

## Review trigger

If both endpoints are Requirements; then use refines / refinedBy

## Source basis / notes

Relationship simplification: Requirement→Function precision/detail uses describes rather than refines.
