---
uid: 20260928122756000skellyspencer
id: INFO-00019
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


## 2026-10-02 — v0.8 cross-repository reconciliation

- Issued MDSE Modeling Ruleset 1.23.
- Advanced element-types to 1.17 and Local Model to 0.2.
- Added sparse optional `abstract` property definition.
- Settled one global 30-character reference identity-token namespace.
- Settled EA8647 source lineage, first-allocation and rerun identity rules.
- Replaced ID-based duplicate filename handling with `~2` and forced alteration with `~a` sequencing.
- Set repository-relative hard limit to 212 characters and expanded folder-shortening rules.
- Settled rerun field ownership, source deletion behavior and relationship removal.
- Made failed attachment import non-blocking but reconciled; kept diagram creation deferred with mandatory reconciliation.
- Retired four empty legacy import CSVs.
- Refreshed the v0.8 implementation handoff and translator definition.
- Added `MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md` as the continuation contract.


## 2026-10-02 — W-321 release-chain alignment

- Made `mdse-release.yaml` the one machine-readable authority for the lean runtime-base contents.
- Removed duplicate prose ownership of the base file list from Translator Definition.
- Added deterministic `build-base.py` and extended `check-release.py` with `--base`.
- Generated bases carry `mdse_release` in `.vault.yaml`; initialization preserves it.
- Current State and the release manifest remain methodology-workspace files and are not copied into engineering vaults.
- Corrected active Translator Definition drift: element-types 1.17, Local Model 0.2, EA8647 author fallback, W-318 naming, Source Map rerun authority, and runtime-base status.
- Corrected relationships.yaml Local Model guidance from 0.1 to 0.2.
- Deferred unavailable MDSE Bootstrap from the v0.8 runtime plugin baseline.
- Established the final-base gate that a WB-106-capable Workbench release must be pinned before issue.
- Made AGENTS/AI instructions work both in the methodology workspace and the lean runtime base.
