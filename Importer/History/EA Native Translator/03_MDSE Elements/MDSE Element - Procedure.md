---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Procedure"
mdseSubtypes: ["test","assembly","configuration","commissioning","calibration","maintenance","repair","decommissioning"]
---
# Procedure

## Definition

Ordered reusable procedure.

## Approved subtypes

- `test`
- `assembly`
- `configuration`
- `commissioning`
- `calibration`
- `maintenance`
- `repair`
- `decommissioning`

## Nomenclature

Engineering notes use:

```yaml
type: Procedure
subtype: test
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
