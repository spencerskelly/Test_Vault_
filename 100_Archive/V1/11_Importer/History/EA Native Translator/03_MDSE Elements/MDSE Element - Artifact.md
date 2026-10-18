---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Artifact"
mdseSubtypes: ["image","document"]
---
# Artifact

## Definition

Physical or digital artifact with independent engineering identity.

## Approved subtypes

- `image`
- `document`

## Nomenclature

Engineering notes use:

```yaml
type: Artifact
subtype: image
```

`subtype` replaces the former `kind` property.

## Translator principle

Source EA stereotypes do not automatically create new MDSE subtypes. Only approved subtype mappings may populate `subtype`; otherwise preserve the source stereotype as provenance and leave `subtype` blank pending semantic review.
