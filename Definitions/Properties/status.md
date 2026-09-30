---
uid: 20260930133525629skellyspencer
id: INFO-00026
status: Active
property: status
appliesTo: Every note that has the property
required: Always
setBy: Template; a person changes it
canChange: A person
---
# status

The review state of a note.

## Rules

- A template sets the default (`Draft` for model notes, `Active` for the people and definition notes). An AI tool leaves it at the template default, never advances it and never marks its own note reviewed or approved; a person does that (AI_INSTRUCTIONS).
- A note that is no longer valid is set to `Retired`, not deleted, and its `id` stays reserved (AI_INSTRUCTIONS, W-18).
- EA's own status values are not carried over; the vault starts with its own (W-39).

## Values

No complete list of values has been given yet. `Draft`, `Active` and `Retired` are the ones used so far.
