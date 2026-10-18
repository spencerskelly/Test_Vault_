# Step 74 — BOM / Workbench rehearsal and recovery preservation (2026-10-14)

## Verified file-level findings

- BOM rehearsal: `.github/workflows/bom-a14-merge-rehearsal.yml` exists on `integration/bom-a14-reconciliation-2026-10-09` as blob `cdee24fbcf33fea71f1fd297208f7467539cd5bb`; absent at same path from Step22 and audit PR #41 branch. **Historical CI evidence requires retention/archival; do not activate** its legacy trigger.
- Workbench rehearsal: `.github/workflows/workbench-monorepo-rehearsal.yml` exists on `integration/workbench-monorepo-rehearsal-2026-10-09` as blob `253722a1273e9d0f30255e25299c7ec56c18684b`; absent from Step22 and audit PR #41. **Retain as historical rehearsal** pending feature-equivalence review, not active CI.
- Recovery handoff: `00_Workspace/GitHub Consolidation Step 18 Obsidian UI Acceptance Handoff 2026-10-09.md`, blob `81a4978e0ddbc01d5ac36a27a4dada499f05a632`, is **byte-identical** on recovery branch and Step22. Missing from PR #41's audit branch at same path does not mean lost from Step22.
- GitHub compare recovery-vs-Step22 listed 15 recovery handoff documents (Steps 04B–18) as `added` in compare output, but that status cannot be interpreted as absence from the endpoint tree: the Step18 file demonstrably exists unchanged at both refs. File-level reconciliation must use exact endpoint path/blob IDs.

## Disposition

Do not retire any of the BOM, Workbench or recovery branches based on comparison file status alone. Preserve inactive workflow source under a non-triggering historical-doc/archival location or immutable retained Git ref before branch deletion; preserve exact blob provenance. For recovery, inventory each of the 15 endpoint document blobs rather than assuming all 15 are exclusive.

## Step 75

Finish per-path SHA equality check for Steps 04B–18 between recovery and Step22, then review whether BOM/Workbench historical rehearsal controls are fully superseded by currently passing consolidated CI. No merge, deletion, release or artifact replacement has been authorized.
