# EA to MDSE Native Importer v0.8.2

This version preserves v0.8.1 unchanged and addresses the first real whole-model path-length failure.

## Changes from v0.8.1

- When the deepest generated folder repeats the complete engineering note name as its trailing label, the redundant folder level is removed before filename shortening.
- Examples covered:
  - `Folder / Note.md`
  - `Context - Note / Note.md`
  - `Context: Note / Note.md`
  - `Context / Note / Note.md`
- This is a navigation-only normalization. The note keeps its full engineering name and the alteration remains visible in the path-review evidence.
- The 212-character hard limit remains unchanged.
- The importer still refuses an irreducible path if the folder hierarchy itself leaves no readable filename space after this redundancy removal.

## Acceptance evidence leading to this version

Real EA8647 run:
- preflight: PASS, 0 fail / 0 warn
- whole-model plan: PASS
- source: 35,969 elements and 21,822 connectors
- first path failure:
  `00 Product Abstract/02 Module/04 IPC Accessory & Option/PCOM 1.0/Gen IV Control-Comms Use Case~a/Access Control - Authorization & Deauthorization/Access Control - Authorization/Access Control - Authorize from List/Authorize from List.md`
- failing path length: 236 characters
- after removing the redundant deepest folder: 199 characters

## Retained fixes from v0.8.1

- Local Model part occurrences are emitted only when their reusable definition is an Object.
- Output base selection checks required marker files before reading them.
- Mechanical folder subdivision over 75 generated files remains enabled.
