---
uid: 20260928122756000skellyspencer
id: INFO-00019
type: Info
subtype: Log
status: Active
---
# Review Changes Log

Reasons for changes made to an imported vault during review (Workspace Decision Log W-37 and W-38). The changes themselves are not written here. They are the `git diff` between the baseline import commit and the reviewed vault. This file records why, so the reasons can become rule changes for the next fresh import.

## How to add a line

One row per reason, not one per note. If the same change was made on many notes, write it once and say how many.

- **Element:** the EA GUID of the element when there is one (it survives a fresh import), otherwise the `uid` of the note.
- **Change:** what you changed, in a few words.
- **Why:** the reason.
- **Rule to change:** the rule, property or mapping the next import should change, if you know it. Leave blank if unsure.

## Log

| Date | Element | Change | Why | Rule to change |
|---|---|---|---|---|
