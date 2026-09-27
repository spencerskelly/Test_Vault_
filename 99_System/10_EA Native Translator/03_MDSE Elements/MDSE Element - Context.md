---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Context"
mdseSubtypes: []
---
# Context

## Definition

Modeled external or situational context relevant to behavior or applicability.

## Approved subtypes

No predefined subtypes.

## Nomenclature

Engineering notes use:

```yaml
type: Context
subtype: 
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
