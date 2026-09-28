---
uid: 20260928090456001skellyspencer
id: INFO-00006
type: Info
subtype: Specification
status: Active
---
# MDSE Bootstrap: Author Registration

What MDSE Bootstrap must do so every person has an author code before creating a note, and so AI tools can find it. Decision W-24 in the Workspace Decision Log. The plugin's source is not in this repository, so this note is the specification for whoever maintains it.

## When

On install of the vault on a new computer, after the plugins are installed and before the person creates a note.

## Steps

1. If `.obsidian/author-code.txt` already exists and holds a valid code, keep it. Never overwrite it. Go to step 6 to make sure the person is registered.
2. Ask for first name and last name.
3. Derive the code: last name followed by first name, accents removed (ß becomes ss), lowercase letters only, cut to 13 characters, padded on the right with hyphens to 13.
4. Show the code and let the person accept it or type a different one. A code must match `^[a-z-]{13}$`. Reject a code that is already used by anyone in `99_System/03_Schemas/authors.yaml`, whether as `code`, in `previousCodes`, or as an AI code, and ask for another.
5. Write the code to `.obsidian/author-code.txt`. This file is local and git-ignored.
6. Register the person in `99_System/03_Schemas/authors.yaml`: `code`, `name` (first and last), and `timezone` (the computer's time zone, for example `America/Los_Angeles`). If the person is already listed by name or code, do nothing.
7. Save the change so it reaches the shared vault (commit and push, or leave it for Obsidian Git). Until it does, AI tools working from the shared vault will not know the person's code.

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
