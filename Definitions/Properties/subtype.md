---
uid: 20260930133525628skellyspencer
id: INFO-00025
status: Active
property: subtype
appliesTo: Model notes whose class lists subtypes
required: No
setBy: Template (hand-made notes) or translator (translated notes)
canChange: No meaning given yet.
---
# subtype

An approved specialization within the `type` (Ruleset 1.22 section 1.1). It is not the relationship `subtypeOf`, which links two notes that are a true reusable specialization of each other.

## Format

One of the values listed for the class in `99_System/03_Schemas/element-types.yaml`. A class with no listed values leaves it blank (W-237, W-238). A Requirement takes it from the package it sits in (W-115, W-116, W-238).

## Where it sits

Second property of a model note, after `type` (W-97).

## Rules

- A note in `99_System` or `Definitions` carries no `subtype` (W-243, W-262).
