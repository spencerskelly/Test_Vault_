---
uid:
type: Translation Decision
status: Working
decisionArea: "Requirement Subtype Mapping"
---
# Requirement Subtype Mapping

## Purpose

Define how EA Requirement stereotypes populate the common MDSE `subtype` property without allowing stereotype names to silently expand the taxonomy.

## Baseline rule

Every EA element with `Object_Type = Requirement` imports as:

```yaml
type: Requirement
```

The EA stereotype is preserved as source provenance. `subtype` is populated only by an explicitly approved mapping.

## Current proposed mapping

| EA stereotype | MDSE type | MDSE subtype | Decision |
|---|---|---|---|
| `functionalRequirement` | Requirement | `functional` | Proposed Settled |
| `Functional` | Requirement | `functional` | Proposed Settled |
| `designConstraint` | Requirement | `design` | Proposed Settled |
| none | Requirement | blank | Preserve |
| `requirement` | Requirement | blank | Preserve |
| `extendedRequirement` | Requirement | blank | Review |
| `performanceRequirement` | Requirement | blank | Review |
| `physicalRequirement` | Requirement | blank | Review |
| `Regulatory Requirement` | Requirement | blank | Review |
| `Webasto Requirement` | Requirement | blank | Review |

## Approved MDSE Requirement subtypes available

- `functional`
- `design`
- `standard`
- `stakeholder`

## Rule

Unknown or organization-specific stereotypes do not create new MDSE subtypes automatically.

## Your decision area

Edit the table above directly. Change the **Decision** and **MDSE subtype** cells as you decide each mapping, and add rationale below when the choice needs explanation.
