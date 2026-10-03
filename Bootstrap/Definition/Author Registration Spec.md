---
uid: 20260928090456001skellyspencer
id: INFO-00006
status: Active
---
# MDSE Bootstrap: Author Registration

What MDSE Bootstrap must do so every person has an author code before creating a note, and so AI tools can find it. Decisions W-24 and W-25 in the Workspace Decision Log. Implemented by MDSE Bootstrap 0.3.0 (W-322); source in `MDSE Bootstrap/plugin/`, overview in [[README_MDSE Bootstrap]].

## When

On the first open of the vault on a computer, once Restricted mode is off (the plugins ship inside the vault, W-322), and before the person creates a note. A person can rerun it with **MDSE Bootstrap: Register author code**.

## Steps

1. If `.obsidian/author-code.txt` already exists and holds a valid code, keep it. Never overwrite it. Go to step 6 to make sure the person has a note.
2. Ask for first name and last name.
3. Derive the code: last name followed by first name, accents removed (ß becomes ss), lowercase letters only, cut to 13 characters, padded on the right with hyphens to 13.
4. Show the code and let the person accept it or type a different one. A code must match `^[a-z-]{13}$`. Reject a code that is already used by anyone: as `code` or in `previousCodes` in any note in `99_System/04_People`, or as an AI code in `99_System/03_Schemas/authors.yaml`. Ask for another.
5. Write the code to `.obsidian/author-code.txt`. This file is local and git-ignored.
6. Create the person's note in `99_System/04_People`, named `First Last.md`, from the `Person` template in `99_System/05_Templates`. Fill in `code`, `name` and `timezone` (the computer's time zone, for example `America/Los_Angeles`). The `uid` and `id` are filled the same way as any other note. If a note for the person already exists (same name or code), do nothing.
7. Save the change so it reaches the shared vault (commit and push, or leave it for Obsidian Git). Until it does, AI tools working from the shared vault will not know the person's code.

One file per person means several people registering on the same day do not conflict.

## Test cases

| First name | Last name | Code |
|---|---|---|
| Spencer | Skelly | `skellyspencer` |
| Jesse | Rivera | `riverajesse--` |
| Florian | Koerfer | `koerferfloria` |
| Ray | Virzi | `virziray-----` |
| Jürgen | Müller | `mullerjurgen-` |
| Anna | Weiß | `weissanna----` |

The first-use popup in `Snippet - uid` uses the same rule, so a person created either way gets the same code.

## If the person needs to change their code

See `Definitions/Changing Your Author Code.md`.

## Implementation notes (0.3.0)

- Step 4 accepts a code that already belongs to a person note with the same name: that is the same person on a new computer. The note is not recreated (step 6).
- Step 6 creates the note with Templater's create-from-template so `uid` and `id` come from `Snippet - uid` and `Snippet - id`; Bootstrap then sets `code`, `name` and `timezone` (the computer's IANA time zone).
- Step 7 is a notice asking the person to commit and sync; Bootstrap does not run Git itself.
