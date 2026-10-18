---
uid: 20260930133525627skellyspencer
id: INFO-00024
status: Active
property: type
usedOn: Model notes
required: Always on a model note
setBy: Template (hand-made notes) or translator (translated notes)
canChange: In stage 2, when a note is reclassified
---
# type

The primary MDSE semantic class of a model note (Ruleset 1.23 section 1.1).

## Format

One of the classes in `99_System/03_Schemas/element-types.yaml`, for example `Requirement` or `Function`.

## Where it sits

First property of a model note (W-97).

## Rules

- A note in `99_System` or `Definitions` carries no `type` (W-243, W-262).
- On a translated note the translator sets it, and stage 2 corrects it (W-30). A note reclassified in stage 2 gets a new `id` and keeps the old one under `## Former ids` (W-181, W-207).
