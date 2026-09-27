---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Thing"
mdseSubtypes: ["electrical","circuit","mechanical","software","firmware"]
---
# Thing

## Definition

Reusable physical, software, firmware, or otherwise modeled engineering entity.

## Approved subtypes

- `electrical`
- `circuit`
- `mechanical`
- `software`
- `firmware`

## Nomenclature

Engineering notes use:

```yaml
type: Thing
subtype: electrical
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
