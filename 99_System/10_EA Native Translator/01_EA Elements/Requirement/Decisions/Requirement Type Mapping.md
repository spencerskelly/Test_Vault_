---
uid:
type: Translation Decision
status: Working
decisionArea: "Requirement Type Mapping"
---
# Requirement Type Mapping

## Purpose

Define how EA Requirement objects and stereotypes become MDSE Requirement elements without allowing stereotype names to silently expand the MDSE taxonomy.

## Baseline rule

Every EA element with `Object_Type = Requirement` imports as:

```yaml
type: Requirement
```

The EA stereotype is preserved as source provenance.

## Current proposed classification

| EA stereotype | MDSE type | MDSE requirementType | Decision |
|---|---|---|---|
| `functionalRequirement` | Requirement | Functional | Proposed Settled |
| `Functional` | Requirement | Functional | Proposed Settled |
| `designConstraint` | Requirement | Design Constraint | Proposed Settled |
| none | Requirement | blank | Preserve |
| `requirement` | Requirement | blank | Preserve |
| `extendedRequirement` | Requirement | blank | Review |
| `performanceRequirement` | Requirement | blank | Review |
| `physicalRequirement` | Requirement | blank | Review |
| `Regulatory Requirement` | Requirement | blank | Review |
| `Webasto Requirement` | Requirement | blank | Review |

## Rule

Unknown or organization-specific stereotypes do not create new MDSE Requirement types automatically.

## Why

This preserves EA source fidelity while allowing only explicitly approved semantic normalization.

## Open decisions

- Should `performanceRequirement` become Functional, Design Constraint, or a distinct classification?
- Should `physicalRequirement` remain generic or map to Design Constraint?
- Should `Regulatory Requirement` become a Requirement category or remain provenance?
- Is `Webasto Requirement` a source/ownership label rather than a requirement type?
