---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Design"
mdseSubtypes: ["characteristic","decision"]
---
# Design

## Definition

Engineering design characteristic, choice, or definition.

## Approved subtypes

- `characteristic`
- `decision`

## Nomenclature

Engineering notes use:

```yaml
type: Design
subtype: characteristic
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
