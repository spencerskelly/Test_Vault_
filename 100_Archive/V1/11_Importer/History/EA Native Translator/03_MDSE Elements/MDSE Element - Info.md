---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Info"
mdseSubtypes: ["need","objective","concern","decision","assumption","rationale","finding","analysis","trade study","calculation","milestone","lesson learned"]
---
# Info

## Definition

Reusable engineering knowledge or rationale.

## Approved subtypes

- `need`
- `objective`
- `concern`
- `decision`
- `assumption`
- `rationale`
- `finding`
- `analysis`
- `trade study`
- `calculation`
- `milestone`
- `lesson learned`

## Nomenclature

Engineering notes use:

```yaml
type: Info
subtype: need
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
