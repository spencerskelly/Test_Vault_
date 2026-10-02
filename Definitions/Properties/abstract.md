---
uid: 20261002113100000skellyspencer
id: INFO-00069
status: Active
property: abstract
usedOn: Reusable model definition notes when applicable
required: No
setBy: A person or governed tool
canChange: A person or governed tool
---
# abstract

Marks a reusable definition as an organizing/generalizing definition that is not itself a valid effective definition for a contextual occurrence.

## Rules

- Write `abstract: true` only when the definition itself is intentionally non-selectable.
- Absence means false.
- `abstract: false` is valid when encountered, but canonical writing omits it.
- Abstractness is not inherited.
- Candidate discovery traverses through abstract definitions to concrete descendants.
- A non-abstract family root remains selectable alongside its concrete descendants.
- `abstract` does not mean optional and does not make an occurrence a variant.
- `subtypeOf` remains reusable definition-level specialization.
- Local `usage: variant` or `usage: option` remains occurrence-level configuration semantics.

## Decisions

W-314 and W-319 in the Workspace Decision Log.
