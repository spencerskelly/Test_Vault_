---
uid:
type: Translation Rule
status: "Deferred"
matrixRuleId: 47
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 47 — StateFlow — State transition evidence

## Source pattern

- **EA Connector:** StateFlow
- **EA Stereotype / Pattern:** State transition evidence
- **Source Endpoint Semantics:** Source State
- **Target Endpoint Semantics:** Target State

## MDSE relationship

- **Source YAML Relationship:** none
- **Target YAML Inverse:** none

## Transformation rule

Identify as transition evidence. Do not write a direct State→State YAML relationship from the connector. Preserve enough data to create/resolve a Transition when the native state-transition rule is finalized.

## Body detail rule

Preserve trigger, guard, effect/action, connector name, notes, and source/target state identity.

## Status

Deferred

## Review trigger

Always until connector-to-Transition handling is explicitly approved for the native importer

## Source basis / notes

Primary reference §9.3. Older translator treated true StateFlow as Transition.
