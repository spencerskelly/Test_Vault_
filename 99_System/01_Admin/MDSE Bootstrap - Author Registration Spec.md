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

1. If  already exists and holds a valid code, keep it. Never overwrite it. Go to step 6 to make sure the person is registered.
2. Ask for first name and last name.
3. Derive the code: last name followed by first name, accents removed (ß becomes ss), lowercase letters only, cut to 13 characters, padded on the right with hyphens to 13.
4. Show the code and let the person accept it or type a different one. A code must match . Reject a code that is already used by anyone in , whether as , in , or as an AI code, and ask for another.
5. Write the code to . This file is local and git-ignored.
6. Register the person in : ,  (first and last), and  (the computer's time zone, for example ). If the person is already listed by name or code, do nothing.
7. Save the change so it reaches the shared vault (commit and push, or leave it for Obsidian Git). Until it does, AI tools working from the shared vault will not know the person's code.

## Test cases

| First name | Last name | Code |
|---|---|---|
| Spencer | Skelly |  |
| Jesse | Rivera |  |
| Florian | Koerfer |  |
| Ray | Virzi |  |
| Jürgen | Müller |  |
| Anna | Weiß |  |

The first-use popup in  uses the same rule, so a person created either way gets the same code.

## If the person needs to change their code

See .
