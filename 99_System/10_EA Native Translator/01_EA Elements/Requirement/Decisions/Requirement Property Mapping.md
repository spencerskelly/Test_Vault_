---
uid:
type: Translation Decision
status: Working
decisionArea: "Requirement Property Mapping"
---
# Requirement Property Mapping

## Purpose

Define the disposition of EA Requirement fields and tagged values during native import.

## Required disposition vocabulary

Each source field must end as one of:

- Direct
- Transform
- Body
- Provenance
- Ignore
- Review

## Current baseline

| EA source field | MDSE destination | Disposition | Status |
|---|---|---|---|
| Name | note title | Direct | Proposed |
| Notes / description | note body | Direct | Proposed |
| Object_Type | `type: Requirement` | Direct | Proposed |
| Stereotype | `eaStereotype` provenance and optional approved `requirementType` | Transform | Proposed |
| eaGUID | `eaGUID` | Provenance | Settled |
| EA package | `eaPackage` | Provenance | Settled |
| Package hierarchy | none automatically | Ignore as semantic structure | Settled |
| Requirement status | normalized `status` | Transform | Review |
| External / legacy requirement ID | `formerIds` or source ID property | Transform | Review |
| Tagged values | individually mapped | Review | Open |
| Author | none unless engineering value is established | Ignore / Review | Open |
| Created / Modified timestamps | provenance only if needed | Review | Open |

## Rule

No EA property is silently dropped until it has an explicit disposition in this note or a linked field-specific rule.

## Next step

Inventory the actual Requirement properties and tagged values present in the EA source export, then replace the open rows with concrete mappings.
