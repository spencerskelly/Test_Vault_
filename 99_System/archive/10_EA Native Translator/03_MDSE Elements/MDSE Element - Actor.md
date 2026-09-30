---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Actor"
mdseSubtypes: []
---
# Actor

## Definition

External living/person role participating in modeled behavior.

## Approved subtypes

No predefined subtypes.

## Nomenclature

Engineering notes use:

```yaml
type: Actor
subtype: 
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
