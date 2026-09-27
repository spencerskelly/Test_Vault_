---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Transition"
mdseSubtypes: []
---
# Transition

## Definition

State-to-state transition within a State Machine.

## Approved subtypes

No predefined subtypes.

## Nomenclature

Engineering notes use:

```yaml
type: Transition
subtype: 
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
