---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Setup"
mdseSubtypes: []
---
# Setup

## Definition

Reusable verification/procedure setup definition.

## Approved subtypes

No predefined subtypes.

## Nomenclature

Engineering notes use:

```yaml
type: Setup
subtype: 
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
