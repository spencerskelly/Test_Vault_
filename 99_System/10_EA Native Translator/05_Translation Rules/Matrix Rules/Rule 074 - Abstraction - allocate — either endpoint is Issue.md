---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 74
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 74 — Abstraction — allocate — either endpoint is Issue

## Source pattern

- **EA Connector:** Abstraction
- **EA Stereotype / Pattern:** allocate — either endpoint is Issue
- **Source Endpoint Semantics:** Issue (either EA endpoint)
- **Target Endpoint Semantics:** Any other element

## MDSE relationship

- **Source YAML Relationship:** affects
- **Target YAML Inverse:** affectedBy

## Transformation rule

Normalize EA orientation: Issue affects the other element; the other element is affectedBy the Issue.

## Body detail rule

Preserve connector notes/roles/multiplicity/constraints in endpoint bodies when meaningful.

## Status

Settled

## Review trigger

Neither endpoint is Issue

## Source basis / notes

259 observed allocate connectors in current export.
