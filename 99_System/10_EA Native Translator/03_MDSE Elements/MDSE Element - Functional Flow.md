---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Functional Flow"
mdseSubtypes: []
---
# Functional Flow

## Definition

Contextual behavior topology using Functions and local sequencing/control.

## Approved subtypes

No predefined subtypes.

## Nomenclature

Engineering notes use:

```yaml
type: Functional Flow
subtype: 
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
