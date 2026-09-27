---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Function"
mdseSubtypes: ["system","hardware","software","module"]
---
# Function

## Definition

Behavior controlled by the modeled product.

## Approved subtypes

- `system`
- `hardware`
- `software`
- `module`

## Nomenclature

Engineering notes use:

```yaml
type: Function
subtype: system
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
