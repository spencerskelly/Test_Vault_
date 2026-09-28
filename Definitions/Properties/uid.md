---
type: Info
subtype: Property Definition
status: Active
property: uid
appliesTo: Every note created in the vault
required: Always
setBy: Template (hand-made notes) or translator (translated notes)
canChange: Never
---
# uid

The permanent identity of a note. It never changes, even if the note is renamed, moved or retired.

## Format

30 characters: a 17-digit timestamp followed by a 13-character author code.

`yyyyMMddHHmmssSSS` + author code, for example `20260928101530123skellyspencer`.

- The timestamp is local time, not UTC.
- The author code is the person's last name followed by first name, lowercase letters only, cut to 13 characters and padded with hyphens if shorter.

## How it is determined

- **Note created in the vault:** filled in automatically when the template is applied, from the creator's clock and their author code.
- **Note translated from EA:** the creation time recorded in EA, exactly as stored, and the EA author mapped to their author code. An EA element with no usable author gets `sparxeaauthor`.
- **Two notes with the same second and author:** one millisecond is added until the `uid` is unique. Ties are ordered by the old EA identifier, so translating the same data always gives the same `uid`.

## What it impacts

- Tools and AI use it to refer to one specific note, whatever its title.
- It shows when a note was created and by whom.
- Sorting by `uid` puts notes in creation order (approximately, since it uses local time).
- The validator checks that every `uid` is unique and correctly formed.

## What blank means

It is never blank. A note without a `uid` is an error.

## Not to be confused with

- `id`: the short number people quote, such as `REQ-00042`.
- The old EA identifier (`eaGUID`): kept only as a line at the bottom of translated notes, for tracing back to EA. It is not used for anything else.

## Decisions

W-06, W-09, W-10, W-11, W-12, W-13 in the Workspace Decision Log.
