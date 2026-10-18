---
uid: 20260927224829000skellyspencer
id: INFO-00003
status: Active
property: id
usedOn: Every note created in the vault, not notes brought in from outside
required: Always, for notes created in the vault
setBy: Template (hand-made notes) or translator (translated notes)
canChange: Never
---
# id

The short, readable identifier people use to talk about a note, for example `REQ-00042`.

## Format

- **Every note:** a class prefix, a hyphen, and a five-digit number, for example `OBJ-00042`.
- **Requirements:** by subtype, `STD-#####` for a standard, `STK-#####` for a stakeholder requirement, and `REQ-#####` for the others (W-203). No designator is read from the source: a designator such as `UL 2594 24.1.0-01` stays in the note's name.

An `id` is always an internal identifier defined here. Any other identifier found in the source is not an `id`. It is kept in the note body under the source identifiers at the bottom.

## How it is determined

- **Note created in the vault:** filled in automatically when the template is applied, using the next number for that class.
- **Note translated from EA:** numbered in original creation order within each prefix, oldest first, so `REQ-00001` is the oldest requirement that is neither a standard nor a stakeholder requirement. The same EA data always gives the same numbers.
- After migration the numbers are permanent. New notes continue after the highest migrated number.

## What it impacts

- It is how people cite a note in conversation, reviews and documents.
- The validator checks for duplicate `id` values. A gap in the numbering means a note may have been deleted by accident.

## What blank means

It is never blank on a note created in the vault. Notes brought in from outside keep their own identification and have no `id`.

## Rules

- An `id` is never reused.
- A note that is no longer valid is retired, not deleted, so its `id` stays reserved.
- Two people creating notes at the same time can end up with the same number. This is an accepted risk. A periodic AI sweep finds these overlaps so they can be repaired.

## Not to be confused with

- `uid`: the permanent 30-character identity, which also records creation time and author.
- The old EA identifier (`eaGUID`).

## Decisions

W-06, W-14, W-15, W-17, W-18 in the Workspace Decision Log.
