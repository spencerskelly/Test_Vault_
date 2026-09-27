---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Document"
mdseSubtypes: ["standard","specification","report","drawing"]
---
# Document

## Definition

Document with reusable engineering identity.

## Approved subtypes

- `standard`
- `specification`
- `report`
- `drawing`

## Nomenclature

Engineering notes use:

```yaml
type: Document
subtype: standard
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
