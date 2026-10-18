---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 20
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 20 — refine — Use Case → Requirement

## Source pattern

- **EA Connector:** refine
- **EA Stereotype / Pattern:** Use Case → Requirement
- **Source Endpoint Semantics:** Use Case
- **Target Endpoint Semantics:** Requirement

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

Relationship simplification: Use Case→Requirement precision/detail uses describes rather than refines.
