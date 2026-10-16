---
uid: 20260927224829001skellyspencer
id: INFO-00004
status: Active
property: uid
usedOn: Every note created in the vault
required: Always
setBy: Template (hand-made notes) or translator (translated notes)
canChange: Never
---
# uid

The permanent identity token of a first-class note. It never changes, even if the note is renamed, moved or retired. The same 30-character token format is also used inside kind-prefixed Local Model IDs, and the token is globally unique across all independently referenceable model entities.

## Format

30 characters: a 17-digit timestamp followed by a 13-character author code.

`yyyyMMddHHmmssSSS` + author code, for example `20260928101530123skellyspencer`.

- The timestamp is local time, not UTC.
- The author code is the person's last name followed by first name, lowercase letters only, cut to 13 characters and padded with hyphens if shorter.

## How it is determined

- **Note created in the vault:** filled in automatically when the template is applied, from the creator's clock and their author code.
- **Note translated from EA:** importer-specific source rules govern first allocation. For the EA8647 v0.8 import, use the EA creation time exactly as stored with no timezone conversion, normalize missing milliseconds to `000`, and map the EA author to the 13-character author code. Missing/unusable author uses `skellyspencer` for this import. If creation time is missing, allocation begins at `20260911000000001`.
- **Note written by an AI:** if a user directed the note, even when the AI wrote every word, the user's author code is used. If the AI created the note on its own with no direct instruction, the AI's code is used, so these notes can be told apart. The pattern is always the tool name, then `ai`, then hyphens to 13 characters, so a new tool follows the same rule: `claudeai-----`, `chatgptai----`, `rovoai-------`, `geminiai-----`. The `status` property then shows whether a person has reviewed it.
- **Identity collision:** the 30-character token must be unused by every note UID and Local Model identity token in the destination vault. Add one millisecond until unique. For EA8647 first allocation, ties are ordered by EA GUID lexical order.

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


## Local Model identity

A Local Model record does not gain a note `uid` property. It embeds the same 30-character identity token in its native block ID, such as `ep-<token>`. The kind prefix is representation metadata; the token is the persistent identity. If an explicitly reviewed modeling change later promotes that local entity into a first-class note, the note retains the token.
