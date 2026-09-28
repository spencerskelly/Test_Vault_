---
uid: 20260928090456000skellyspencer
id: INFO-00005
type: Info
subtype: Guide
status: Active
---
# Changing Your Author Code

Your author code is the last 13 characters of every `uid` you create. It is made once, when you first start (by MDSE Bootstrap during install, or by the popup the first time you apply a template), from your last name followed by your first name. It is recorded in your person note in `99_System/04_People`.

Change it only if something went wrong: a misspelled name, the wrong person's name, or a code that clashes with someone else's.

## What changing it does

- It affects only notes you create from now on.
- **Notes you already created keep their old code.** A `uid` never changes, even when it is wrong. Do not edit old `uid` values.
- The old code stays on record as yours, so people and tools know those notes are also yours.

## How to change it

1. **Choose the new code.** Exactly 13 characters, lowercase letters and hyphens only, and not used by anyone else. Standard form: last name then first name, letters only, cut to 13 or padded with hyphens on the right. Accents are dropped (Müller becomes muller).
2. **Update your person note.** Open your note in `99_System/04_People` and, in Properties, put the new value in `code` and add your old code to `previousCodes`.
3. **Update your local file.** Open `.obsidian/author-code.txt` in your vault folder and replace its contents with the new code. Or delete the file, and the popup will ask again the next time you apply a template.
4. **Tell any AI tool you work with** to use the new code, or point it at your person note.

## Check

Create a test note from a template. The end of its `uid` should be your new code. Delete the test note if it was only a test, or set its `status` to Retired if it was already saved to the vault.

Related: [[uid]]
