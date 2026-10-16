---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Issue"
mdseSubtypes: ["engineering issue","lifecycle risk"]
---
# Issue

## Definition

Problem, concern, defect, or risk requiring engineering attention.

## Approved subtypes

- `engineering issue`
- `lifecycle risk`

## Nomenclature

Engineering notes use:

```yaml
type: Issue
subtype: engineering issue
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
