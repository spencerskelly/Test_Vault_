---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 27
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 27 — Dependency — Behavior dependency

## Source pattern

- **EA Connector:** Dependency
- **EA Stereotype / Pattern:** Behavior dependency
- **Source Endpoint Semantics:** Dependent behavior
- **Target Endpoint Semantics:** Prerequisite behavior

## MDSE relationship

- **Source YAML Relationship:** dependsOn
- **Target YAML Inverse:** dependencyOf

## Transformation rule

Use only when target is a true prerequisite/reliance.

## Body detail rule

Preserve connector notes/conditions in source body.

## Status

Settled

## Review trigger

Connector appears to mean execution sequence

## Source basis / notes

Execution order is not Dependency.
