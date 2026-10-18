---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Item Flow"
mdseSubtypes: ["information","energy","material"]
---
# Item Flow

## Definition

Reusable item/energy/material/information transfer definition.

## Approved subtypes

- `information`
- `energy`
- `material`

## Nomenclature

Engineering notes use:

```yaml
type: Item Flow
subtype: information
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
