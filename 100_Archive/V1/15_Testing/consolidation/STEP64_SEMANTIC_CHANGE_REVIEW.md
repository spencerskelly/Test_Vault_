# Step 64 — Semantic source change review (2026-10-14)

Status: **read-only review completed; retain candidate improvements; no release approval.**

Original commit: `b0c4e2c6bdfb96d36f51d8152b17be22592ef174`; current validation branch: `integration/p03-legacy-compat-tests-20261013`. Compared historical `src/` content directly with consolidated `55_Workbench/src/`.

## Per-file findings

| File | Semantic difference observed | Disposition |
| --- | --- | --- |
| `core/cache.ts` | Serialize/read `variantOfFormatError` and contextual `quantity`/`unitOfMeasure` | Retain; regression-test cache roundtrip |
| `core/localmodel-edit.ts` | Structured 0.5 reciprocal Interface `equals` plan with atomic note-snapshot edit; reject unsafe linked targets | Retain; test apply/undo/redo and invalid edits |
| `core/localmodel.ts` | Read schema 0.5/0.6; **write still 0.5**; read-only 0.6 part quantity/unit fields; expanded allowed-field checks | Retain; ensure 0.6 cannot be written inadvertently |
| `core/model.ts` | `variantOfFormatError` on notes | Retain |
| `core/review.ts` | New `variantOf` category, finding conversion and counts | Retain |
| `obsidian/assurance.ts` | Adds `validateVariantOf` to review pipeline | Retain |
| `obsidian/indexer.ts` | Raw metadata format checker attaches `variantOfFormatError` | Retain |
| `obsidian/review.ts` | New variant family guidance | Retain |
| `core/variantof.ts` (new) | Read-only variant relationship finding validation (invalid endpoints, duplicates, missing target, cycles) | Retain |
| `core/variantof-format.ts` (new) | Read-only scalar wikilink shape checker | Retain |

## Assessment

These changes are coherent feature additions, not demonstrated accidental corruption. **Do not revert them simply to match the historical `main.js` hash.** Historical binary exact reproduction already passed in run 38604566786; the newer consolidated source is a distinct candidate and its fresh-build hash need not match the older governed release artifact.

Important governance distinction: source validation and hash consistency are not release authorization. The checked-in historical bundle and `artifact-sha256.txt` must remain unchanged until a separately approved new release candidate is created.

## Step 65

1. Review test coverage for reciprocal Interface `equals` atomicity, 0.6 read-only behavior, quantity/unit parsing and cache roundtrips, and `variantOf` safety.
2. If gaps exist, add synthetic tests only on the validation branch and run them.
3. Refactor CI reporting into two **separate** gates: historical governed artifact integrity and new candidate build determinism. Do not call the candidate release-equivalent or waive hash failures.
4. Preserve PR #39/#41 reviewer holds, real-QEAX/macOS/Windows GUI acceptance and release governance before merging or branch deletion.

No source edits, model rewriting, hash manifest alteration, release, branch deletion or merge performed in Step64.
