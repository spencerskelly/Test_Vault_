---
uid:
type: Translation Rule
status: "Settled"
matrixRuleId: 75
source: "EA Native Import Relationship Mapping Matrix 2026-09-27 r12"
---
# Rule 75 — Abstraction — allocate — either endpoint is InformationItem

## Source pattern

- **EA Connector:** Abstraction
- **EA Stereotype / Pattern:** allocate — either endpoint is InformationItem
- **Source Endpoint Semantics:** InformationItem (either EA endpoint)
- **Target Endpoint Semantics:** Any other element

## MDSE relationship

- **Source YAML Relationship:** describes
- **Target YAML Inverse:** describedBy

## Transformation rule

Normalize EA orientation: InformationItem describes the other element; the other element is describedBy the InformationItem.

## Body detail rule

Preserve connector notes/roles/multiplicity/constraints in endpoint bodies when meaningful.

## Status

Settled

## Review trigger

Neither endpoint is InformationItem

## Source basis / notes

40 observed allocate connectors in current export.
