---
uid:
type: MDSE Element Definition
status: Working
mdseType: "Object"
mdseSubtypes: ["electrical","circuit","mechanical","software","firmware"]
---
# Object

## Definition

Reusable engineering entity representing modeled product structure or reusable technical content that is not better represented by another first-class MDSE type.

An Object may be physical or non-physical. The term does **not** imply only a tangible physical object.

## Approved subtypes

- `electrical`
- `circuit`
- `mechanical`
- `software`
- `firmware`

## Nomenclature

```yaml
type: Object
subtype: electrical
```

## EA source distinction

**EA Object** means the Sparx Enterprise Architect source metaclass whose `Object_Type = Object`.

**MDSE Object** means this MDSE semantic type.

Use the qualified names **EA Object** and **MDSE Object** in translator material whenever both could be confused.
