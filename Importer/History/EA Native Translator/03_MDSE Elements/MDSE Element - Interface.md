---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Interface"
mdseSubtypes: ["electrical & material","data","mechanical","generic physical","environmental"]
---
# Interface

## Definition

Meaningful boundary through which modeled elements interact or must remain compatible.

## Approved subtypes

- `electrical & material`
- `data`
- `mechanical`
- `generic physical`
- `environmental`

## Nomenclature

Engineering notes use:

```yaml
type: Interface
subtype: electrical & material
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
