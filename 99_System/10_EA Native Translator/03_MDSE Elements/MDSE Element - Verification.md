---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Verification"
mdseSubtypes: ["test","analysis","inspection","demonstration"]
---
# Verification

## Definition

Reusable verification intent.

## Approved subtypes

- `test`
- `analysis`
- `inspection`
- `demonstration`

## Nomenclature

Engineering notes use:

```yaml
type: Verification
subtype: test
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
