---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Use Case"
mdseSubtypes: ["what","where","why","when"]
---
# Use Case

## Definition

Externally controlled behavior, scenario, or actor goal.

## Approved subtypes

- `what`
- `where`
- `why`
- `when`

## Nomenclature

Engineering notes use:

```yaml
type: Use Case
subtype: what
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
