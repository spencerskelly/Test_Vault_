---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Requirement"
mdseSubtypes: ["functional","design","standard","stakeholder"]
---
# Requirement

## Definition

Normative engineering requirement.

## Approved subtypes

- `functional`
- `design`
- `standard`
- `stakeholder`

## Nomenclature

Engineering Requirement notes use the common MDSE property:

```yaml
type: Requirement
subtype: functional
```

The former Requirement-specific idea of `requirementType` is not used. The former common property `kind` is renamed to `subtype`.

## Translation principle

Every EA `Object_Type = Requirement` becomes MDSE `type: Requirement`. An EA stereotype populates `subtype` only through an explicit approved mapping. Unknown/custom stereotypes are preserved as source provenance without expanding the MDSE taxonomy.

## Canvas

[[CANVAS - Requirement Translation]]
