---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 29
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 29 — Usage — Use Case → Function dependency

## Source pattern

- **EA Connector:** Usage
- **EA Stereotype / Pattern:** Use Case → Function dependency
- **Source Endpoint Semantics:** Use Case
- **Target Endpoint Semantics:** Function

## MDSE relationship

- **Source YAML Relationship:** dependsOn
- **Target YAML Inverse:** dependencyOf

## Transformation rule

Use when Function is relied upon but does not implement the scenario.

## Body detail rule

Preserve connector detail in source body.

## Status

Settled

## Review trigger

Meaning unclear

## Source basis / notes

Usage requires semantic classification.
