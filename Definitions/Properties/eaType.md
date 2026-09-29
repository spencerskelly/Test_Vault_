---
uid: 20260928114132000skellyspencer
id: INFO-00018
type: Info
subtype: Property Definition
status: Active
property: eaType
appliesTo: Notes translated from EA, temporarily
required: Always on translated notes until review is complete
setBy: Translator
canChange: No, it records the source
---
# eaType

The classification the element had in EA. It is temporary: it stays while the imported model is being reviewed, so you can still filter by the original EA type after `type` has been set to an MDSE type.

## Format

Text, taken from EA. It is the EA stereotype when the element has one, otherwise the EA object type. Examples: `Regulatory Requirement`, `requirement`, `Activity`, `Class`.

This loses nothing: no stereotype is used on more than one EA object type, and the rule gives 72 distinct values for the 72 combinations found in the source.

## Where it sits

In the properties, directly below `status` and above `tags` (W-97).

## How it is determined

Set by the translator from the EA element. Nobody types it. Notes created in the vault, not translated from EA, do not have it.

## What it impacts

- Lets people and AI tools filter or group notes by their original EA classification while `type` and `subtype` are being reviewed.
- Gives the review a way to check that a note was classified correctly.

## What happens to it

When the full review is complete, it is either moved below the GUID as a line in the [[EA Source Section]] (`EA type: ...`) or removed entirely.

## What blank means

A note without it was not translated from EA.

## Not to be confused with

`type`, which is the MDSE type and is the one that matters for the model.

## Decisions

W-31 in the Workspace Decision Log.
