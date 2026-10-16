# Consolidation Step 04 — Repository authority and CI transition audit

**Date:** 2026-10-10  
**Status: REVIEW-ONLY AUTHORITY/CI AUDIT PERSISTED; NO CUTOVER, MERGE, PRODUCTION WRITER, OR ARCHIVAL APPROVAL.**  
**Exact inspection baseline:** `spencerskelly/Test_Vault_` / `consolidation/step03-classify-workbench-2026-10-10` commit `987e6a6b3a58a973ede5919364863d86d19108e4`.  
**Machine-readable evidence:** `00_Workspace/Consolidation Step 04 - CI Dependency Inventory 2026-10-10.json`.  

## 1. Confirmed architecture

The integrated candidate contains `55_Workbench/src`, `55_Workbench/test`, package metadata, committed historical ancestry, and the **root** `.github/workflows/mdse-monorepo-workbench-ci.yml`. That root job already runs `npm ci`, `npm run typecheck`, `npm test`, and `npm run build` with `working-directory: 55_Workbench`. It uploads build artifacts to Actions; it does **not** publish a release or mutate Git.

A separate root `mdse-release-alignment-preflight.yml` runs the read-only `66_Testing/check_release_alignment.py` report.

**The cutover is not accomplished**: `Test_Vault_/main` has not incorporated the consolidation staging branch; `MDSE_Workbench` remains active. Root Workbench CI has `push` restricted to old branch `integration/workbench-subtree-2026-10-09`; PR filters cover `main` and historical `recovery/repository-consolidation-2026-10-09`, not this step's draft PR target. Do not assert a green automatic CI check on this documentation-only branch.

## 2. Direct, active repository-authority references (must change at controlled promotion)

| Location | Current source-derived fact | Required controlled change |
|---|---|---|
| `Base Vault/Definition/mdse-release.yaml` | `tools.workbench.repo` and `repos.workbench` both name `spencerskelly/MDSE_Workbench` (lines 42, 69), although `repos.authority` names `spencerskelly/Test_Vault_` | Change both to `spencerskelly/Test_Vault_` as a coordinated *governed* authority update; document `55_Workbench/` as the in-repository source root in a backward-compatible or approved new manifest field. **Do not change pinned 0.1.18, plugin lock, localModel 0.5, or releaseStatus pre-release as a side effect.** |
| Root `README.md` | Says Workbench is a standalone repository (line 16) | Replace with integrated `55_Workbench/` source/testing location *after* authority decision; preserve historical repository as read-only reference. |
| `00_Workspace/MDSE Tool Definitions and Boundaries.md` | Declares standalone as authoritative for source and tests and as sole tool exception | Adopt one source authority in `Test_Vault_/55_Workbench/`; retain source-owned WB decisions and shared MDSE governing schema boundaries. Requires approved cross-tool/W decision. |
| `00_Workspace/00 - Current State.md` | Some interim status notes say source integrated (line 7), but source/implementation authority still names standalone (lines 54–55 and 81), and some baseline details predate the current LM 0.5 integration | Reconcile contradictions together; preserve historical dates and warnings instead of silently pretending old sections are fresh. |
| `Base Vault/Testing/check-release.py` | Workbench testing is already supplied with explicit `--workbench <path>`; it compares fixtures, version pins and controlled user guide (approx. lines 307–343) | Run with `--workbench 55_Workbench`; update instructions/callers where needed. Do not drop fixture parity, pinned artifact or guide checks. |
| `55_Workbench/README.md` | Still documents older 0.2 Local Model baseline and standalone release behavior in multiple sections | Reconcile against current approved 0.5 writer and 0.6 read-only proposal only after source integration, preserving historical notes separately. |
| `Base Vault/Tools/v0.8.0-r2/build-base.py` | Builds from pinned `mdse-release.yaml`/runtime plugin payload; this is not a Workbench git-clone builder | Preserve the existing release-payload/lock authority; do **not** replace it with `55_Workbench/main.js` on every development commit. |

## 3. GitHub Actions audit

All **22 root workflow files** on the Step 03 branch were inspected. **Eight root workflow files reference standalone `MDSE_Workbench`**, principally as pinned source checkouts or old tree-migration rehearsals:

- `.github/workflows/bom-a14-source-step15.yml`
- `.github/workflows/wb128-gate3-representative-views.yml`
- `.github/workflows/wb128-gate4-disposable-edits.yml`
- `.github/workflows/wb128-gate5-release-alignment.yml`
- `.github/workflows/wb128-real-vault-acceptance.yml`
- `.github/workflows/wb129-real-qeax-local-model-05.yml`
- `.github/workflows/wb129-rehearsal.yml`
- `.github/workflows/workbench-subtree-stage.yml`

Examples:
- `wb128-gate5-release-alignment.yml` checks out standalone exact commit `59fc6219...` to validate the historical 0.1.18 gate. This is a historical **pinned evidence check**; do not replace the source ref until defining a *new* baseline gate.
- `wb129-real-qeax-local-model-05.yml` pins standalone `8097f383...` and importer `b43c4d31...` for historical exact-source acceptance.
- `workbench-subtree-stage.yml`, `wb129-rehearsal.yml`, and `bom-a14-source-step15.yml` fetch old standalone branches to perform past import rehearsals. They should not be recycled as the day-to-day monorepo CI.
- `wb128-real-vault-acceptance.yml` checks out old `workbench/local-model-0.4`. Its historical evidence remains attributable to that old source.

**Proposed CI policy, not applied:** 
1. Root `mdse-monorepo-workbench-ci.yml` becomes sole authoritative Workbench typecheck/test/build workflow, with explicit `main` and approved PR/staging trigger coverage and `55_Workbench/**` paths. Continue to publish checksum-bearing CI artifacts **without Git pushes**.
2. Root release-alignment preflight runs for changes to manifest, lock, current contracts and Workbench metadata; do not confuse diagnostic warnings with approved releases.
3. Obsolete source-import and pinned historical workflows remain discoverable as history. Retire their *automatic* triggers only in a separate reviewed CI-governance PR. Do not run arbitrary historical `workflow_dispatch` jobs as evidence of new baseline acceptance.
4. Nested `55_Workbench/.github/workflows/` remains preserved as historical source, **not** treated as live root GitHub Actions. The imported `55_Workbench/ci-workflows/release.yml` similarly does not authorize new runtime publication.
5. Branch names and action permissions must be validated against the actual chosen promotion/PR workflow. The current CI is narrowly branch-filtered and cannot be assumed to run automatically on this draft PR.

### Illustrative review-only trigger diff (NOT APPLIED)

```diff
# .github/workflows/mdse-monorepo-workbench-ci.yml
 on:
   push:
     branches:
-      - integration/workbench-subtree-2026-10-09
+      - main
   pull_request:
     branches:
       - main
-      - recovery/repository-consolidation-2026-10-09
+# Preserve approved staging coverage only if required by the accepted merge plan.
```

Apply the analogous change to `mdse-release-alignment-preflight.yml` when promotion topology is approved. **Do not broaden push permissions or enable historical artifact-push workflows.**

### Illustrative review-only manifest/README changes (NOT APPLIED)

```diff
# Base Vault/Definition/mdse-release.yaml
 tools:
   workbench:
-    repo: "spencerskelly/MDSE_Workbench"
+    repo: "spencerskelly/Test_Vault_"
 repos:
   authority: "spencerskelly/Test_Vault_"
-  workbench: "spencerskelly/MDSE_Workbench"
+  workbench: "spencerskelly/Test_Vault_"
```

Retain legacy repository in an explicit historical/reference role only after determining how release consumers interpret `repos.referenceOnly`. Keep runtime pin/version/lock unchanged until validated together.

## 4. Critical release-preflight false-positive gap

`66_Testing/check_release_alignment.py` (lines ~190–205) uses a repository-wide `git grep -I -l -F "spencerskelly/MDSE_Workbench"` plus other old-path terms, and raises `OLD_PATH_REFERENCES` when **any** tracked file matches. That includes `docs/` and archived branch handoffs; the Step 02–03 *correctly preserved* historical documents will therefore continue to register as references.

**Required future change:** maintain two explicitly separated counts:
- **Blocking active dependency set:** approved current authority/manifest, root production workflows, executable tool code, current onboarding docs and runtime build/reference paths, with a reviewed allowlist; unresolved refs are actionable findings.
- **Nonblocking historical evidence set:** registered archives, frozen test fixtures, historical release notes, and old migration handoffs. Keep the audit visible without falsely requiring deletion of traceability.

Do not simply suppress all Git grep findings or change `--strict` to ignore legitimate live dependencies. Test that an injected active old repo path fails and a registered historical citation does not. Also register new `00_Workspace/` checkpoint documents in the manifest **as reference**, through a governed document-registry change; avoid changing the official manifest in this staging audit.

## 5. Safe execution order and stop conditions

1. Approve consolidation source authority + migration/W decision, with specific `55_Workbench/` path and historical standalone status.
2. **Security stop:** classify the already-public `EA_2026_09_06_endgame.qeax.zip` source data. Because a public Git history exists, a deletion commit is not a complete exposure remedy if restricted.
3. Audit each local contributor workstation for untracked and unpushed Workbench work. Remote-only checks cannot certify this.
4. Review/merge stacked documentation PRs #19, #20, and this Step 04 candidate into the intended **consolidation staging chain**, not directly into public `main`; keep an exact commit ledger.
5. In a *separate atomic code PR*, update the manifest repository fields, root README, current state, tool-boundary doc, active CI triggers, and release-preflight active/history classification. Pin original sha values and show a before/after diff. Keep schema 0.5 and runtime lock unchanged.
6. Run `python3 "Base Vault/Testing/check-release.py" --workbench "55_Workbench"`, `python3 66_Testing/check_release_alignment.py` in audit and future scoped-strict modes, root Workbench `npm ci; npm run typecheck; npm test; npm run build`, importer/root CI, and plugin artifact+lock comparisons.
7. Integrate and separately test A-15.1–A-15.4 changes on actual Workbench source; no 0.6 writer or scalar `variantOf` production activation without schemas and gates.
8. Perform controlled Obsidian GUI first-open, restart, editing and recovery acceptance. Recheck published artifact hashes and read-only release status.
9. Only then approve staged promotion and separately approve archiving standalone `MDSE_Workbench`; retain Git history and recovery records.

## 6. Result and next small step

**Step 04 outcome:** identified direct authority drift, scoped 22 active-root workflow definitions (8 external repo references), documented migration-safe CI policy, and identified strict-preflight history false positives. No active repo source/manifest/schemas, Workbench writer, plugin lock, release pin, or GitHub `main` changed by this checkpoint.

**Next Step 05 (recommended):** perform a targeted **QEAX source confidentiality and public-exposure inventory**, recording evidence without copying/uploading the archive; owner classification and remediation decision are required before public-main merge. In parallel, prepare the local workstation Git audit checklist as a small repeatable command script. Do not archive standalone yet.
