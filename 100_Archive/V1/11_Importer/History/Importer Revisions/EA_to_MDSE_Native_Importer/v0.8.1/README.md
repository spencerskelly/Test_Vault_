# EA to MDSE Native Importer v0.8.1

This version is the direct successor to v0.8.0 and preserves v0.8.0 unchanged for comparison.

## Changes from v0.8.0

1. **Local Model part typing**
   - v0.8.0 attempted to emit a Local Model `part` record for every folded EA Part.
   - Some EA Parts legitimately fold to Function/State/Item Flow definitions for note-level semantics.
   - Local Model 0.2 permits a part `definition` only to a reusable Object.
   - v0.8.1 therefore emits a Local Model part occurrence only when the folded definition is an Object.
   - Folded Parts resolving to non-Object definitions remain represented by the existing note-level/source-evidence rules and produce a diagnostic warning rather than an invalid Local Model record.

2. **Output-base selection**
   - The importer now checks for `.vault.yaml` and `README.md` before attempting to read them.
   - Selecting a non-base folder now returns the normal “not an initialized/unpacked base-vault copy” result instead of surfacing a filesystem read stack trace.

## Retained behavior

- MDSE release: 0.8.0
- relationships: 1.35
- element-types: 1.17
- Local Model: 0.2
- source model: EA8647
- 212-character generated path limit
- maximum 75 generated model files per folder
- deterministic mechanical `folder_1`, `folder_2`, … fallback subdivision when needed
- deferred diagram generation
- attachment reconciliation
- Run Manifest, Ledger, Source Map and review outputs
- WB-106 remains the keepability gate for the first retained whole-model import

## Acceptance status

The real EA8647 source passed v0.8.0 preflight and whole-model planning:
- 35,969 elements
- 21,822 connectors
- 1,387 packages
- 2,924 diagrams
- 42,966 diagram objects
- 37,955 diagram links
- 249,892 object properties
- 42,052 xrefs
- 397 documents
- 23 operations
- 5 attributes

v0.8.1 requires a fresh acceptance run from a freshly generated current base.
