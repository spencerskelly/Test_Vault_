# Step 08 — Actual integrated staging reference audit and line-level cutover ledger

**Date:** 2026-10-10 (GitHub CI ran 2026-10-11 UTC).  
**Status:** Verified real-checkout preflight; **NO CUTOVER, RELEASE, OR STANDALONE REPO ARCHIVE**.  
**Checked branch commit:** `3fc47d9f2ae64e567268925c5d3a495a5bb9fd50`.  
**Evidence:** <https://github.com/spencerskelly/Test_Vault_/actions/runs/38107795084>; first successful aggregate-only run <https://github.com/spencerskelly/Test_Vault_/actions/runs/38107734743>.  
**Path disposition JSON:** `66_Testing/consolidation/STEP08_REFERENCE_DISPOSITIONS.json`.

## What ran on the actual staging checkout

- GitHub Actions checked out the integrated source tree (including tracked archive presence), ran **33/33** Node tests and the Step 07 candidate `git grep` audit against the tracked checkout.
- Actual tree: **15 blocking files, 13 files needing review, 36 explicitly historical files, and one detector self-reference**. The count refers to paths containing the exact old repository string, not the number of string occurrences.
- `--strict` returned its designed **exit status 2**, and the CI job positively asserted that the strict JSON exactly matched the audit JSON. That **successful CI conclusion is NOT archival readiness**.
- The job did **not upload model files or the complete audit JSON**; the second run emitted only previously public tracked file paths and aggregate counts to Actions logs. The job checkout operates on repository files, so do not claim the archive was not copied to the runner.
- The GitHub workflow and scanner do not change source, release pins, plugin lock or `main`.

## All 15 blocking paths and disposition

| Path | Action |
|---|---|
| `.github/workflows/bom-a14-source-step15.yml` | **legacy_ci_review** — Old BOM A-14 subtree pull: retain historical frozen workflow, remove from active current CI after review |
| `.github/workflows/wb128-gate3-representative-views.yml` | **legacy_ci_review** — Old pinned standalone Workbench checkout, historical acceptance |
| `.github/workflows/wb128-gate4-disposable-edits.yml` | **legacy_ci_review** — Old pinned standalone Workbench checkout, historical acceptance |
| `.github/workflows/wb128-gate5-release-alignment.yml` | **legacy_ci_review** — Old exact 0.1.18 Workbench release pin, historical acceptance |
| `.github/workflows/wb128-real-vault-acceptance.yml` | **legacy_ci_review** — Historical Local Model 0.4 acceptance; not replaceable as equivalent new test |
| `.github/workflows/wb129-real-qeax-local-model-05.yml` | **legacy_ci_review** — Pinned importer/Workbench pair; QEAX access and data classification must be addressed |
| `.github/workflows/wb129-rehearsal.yml` | **legacy_ci_review** — Old branch-specific Workbench migration/rehearsal |
| `.github/workflows/workbench-subtree-stage.yml` | **legacy_ci_review** — Old Workbench source migration and write-capable staging workflow |
| `.obsidian/plugin-lock.yaml` | **release_provenance_hold** — Pinned original 0.1.18 source artifact; generated lock must not be manually altered |
| `00_Workspace/00 - Current State.md` | **migrate_current_authority** — Current model ownership sections identify standalone despite staging integration |
| `00_Workspace/MDSE Tool Definitions and Boundaries.md` | **migrate_current_authority** — Current ownership decision map declares standalone authoritative |
| `Base Vault/Definition/mdse-release.yaml` | **migrate_current_authority** — tools.workbench.repo and repos.workbench currently name standalone |
| `Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py` | **release_provenance_hold** — Current lock generator source label is pinned artifact provenance, not live code checkout |
| `Base Vault/Tools/v0.8.0/update-plugin-lock.py` | **historical_generator** — Older generator source label; preserve as historical after checking no active caller |
| `README.md` | **migrate_current_authority** — Root onboarding directs developers to standalone source |

**Important discovery:** The pinned `.obsidian/plugin-lock.yaml` source field names an **immutable Workbench 0.1.18 artifact and validation runs**. Its active generator `Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py` has the matching provenance label. These are **not proof of a currently required separate Git checkout**. Do not edit the generated lock by hand or erase its historic provenance to make the scanner green. The earlier `v0.8.0/update-plugin-lock.py` label is a separate historical-generator review.

The eight root `.github/workflows/*.yml` references are historical pinned-source tests or migration rehearsals, not the primary current root CI. They still appear under the active GitHub Actions workflow directory and some support `workflow_dispatch`; quarantine or retire trigger behavior in a separately reviewed CI-governance change. Keep original commit/source evidence intact.

## All 13 previously unclassified paths and disposition

| Path | Action |
|---|---|
| `00_Workspace/GitHub Consolidation Recovery Inventory 2026-10-09.md` | **historical_evidence** — Recovery history; keep original statements |
| `00_Workspace/Handoff Prompt - MDSE v0.8 Implementation.md` | **update_or_supersede_handoff** — Current handoff still directs Workbench changes to standalone; replace via registered successor |
| `00_Workspace/MDSE v0.8 Cross-Repository Reconciliation - 2026-10-02.md` | **governance_review** — Prior cross-repo baseline; inspect release document registration before downgrading to reference |
| `00_Workspace/README.md` | **migrate_current_authority** — Current workspace orientation points to standalone |
| `00_Workspace/Workbench Performance and Stability Roadmap.md` | **historical_progress** — Historical implementation milestones; preserve dates and prior commit provenance |
| `00_Workspace/Workspace Decision Log.md` | **governance_addendum** — Original W-325/W-328/W-329/W-341/W-342 decisions must remain; append new superseding W decision |
| `55_Workbench/docs/Definition/03 - Build Outline and Roadmap.md` | **historical_progress** — Old WB-106 source coding handoff; preserve context |
| `55_Workbench/docs/Definition/04 - Architecture and Model Boundary.md` | **migrate_current_authority** — Current Workbench boundary doc explicitly declares standalone implementation source |
| `55_Workbench/docs/INDEX.md` | **migrate_current_authority** — Current Workbench navigation declares standalone authority |
| `55_Workbench/docs/README.md` | **update_or_supersede_handoff** — Outdated current-ish Workbench introduction; preserve historical version claims |
| `55_Workbench/docs/bom/A01-A14_ORIGINAL_HANDOFF_ARCHIVE_VERIFICATION_2026-10-09.md` | **historical_evidence** — Exact original BOM recovery verification; immutable provenance |
| `55_Workbench/docs/bom/A01-A14_RECOVERY_STATUS_2026-10-09.md` | **historical_evidence** — Old pull request and audit links are historic facts |
| `66_Testing/consolidation/STEP07_CONTROLLED_CUTOVER_PREVIEW.md` | **historical_proposal** — Prior review-only proposal; not live dependency |

`Workspace Decision Log.md` contains recorded historical authority decisions; **append a new superseding decision** instead of rewriting old W-decision text. Old cross-repo milestones, original BOM recovery reports and prior GitHub evidence should stay attributable to their original source.

## Precise future active-source cutover anchor

These checked blobs can be compared with latest source **before applying any edits**:

- `Base Vault/Definition/mdse-release.yaml` — Git blob `ce556ade56b5bd9650ccc659f1b41bf2ca411c10`
- `README.md` — Git blob `ccd627dc18000895a424d577d3615d16535c9f95`
- `00_Workspace/00 - Current State.md` — Git blob `4e661e075b500950d2aebbf9394fbb087d70242e`
- `00_Workspace/MDSE Tool Definitions and Boundaries.md` — Git blob `6664dd427952fcfac995fee99d2cdd18164719b7`
- `.github/workflows/mdse-monorepo-workbench-ci.yml` — Git blob `afddc15493d96fb35c39eb89e68ad992b64d9c3f`
- `.github/workflows/mdse-release-alignment-preflight.yml` — Git blob `1198601ad6849fdd0ed35e1a08a55f78349d8211`
- `.obsidian/plugin-lock.yaml` — Git blob `c430670577318457972a154012d08c6d28e6d11b`
- `Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py` — Git blob `74f18af673263d87d123d31056251ddbab265d4b`
- `66_Testing/check_release_alignment.py` — Git blob `3eaeae1fa5b6eb198b717b49cf78b79b556a3dce`

Proposed **atomic follow-up** after owner/governance approval:
1. In `mdse-release.yaml`, migrate exactly **two** current repo fields (`tools.workbench.repo`, `repos.workbench`) from the standalone name to `spencerskelly/Test_Vault_`. Record `55_Workbench/` as the owned source root through an approved manifest-compatible mechanism; **do not touch** release status, Workbench 0.1.18 version pin, Local Model 0.5, runtime payload hashes, or generated plugin lock.
2. Reconcile root `README.md`, `00_Workspace/00 - Current State.md`, `00_Workspace/MDSE Tool Definitions and Boundaries.md`, `00_Workspace/README.md`, `55_Workbench/docs/INDEX.md`, and `55_Workbench/docs/Definition/04 - Architecture and Model Boundary.md`. Append a superseding W authority decision and keep the old decisions for provenance.
3. In root `mdse-monorepo-workbench-ci.yml` and `mdse-release-alignment-preflight.yml`, update old **push/PR branch filters** to reviewed `main` and chosen consolidation approval branches. Preserve read-only permissions and no-Git-push build artifacts.
4. Separately review the eight historical workflow triggers. Do not repoint a frozen acceptance test to new code under the same name.
5. Upgrade reference preflight from naive path-only matching to **schema-aware provenance classification**; fail active clone URLs/owner fields while allowing *verified frozen artifact* labels in generated lock and historical reports. Add negative tests proving an unapproved active legacy reference still blocks.
6. After actual local workstation audits and public QEAX owner-security classification, test the full toolchain with `python3 "Base Vault/Testing/check-release.py" --workbench "55_Workbench"`, Workbench `npm ci/typecheck/test/build`, release preflight, runtime lock/hash integrity, full importer pair, and real Obsidian first-open/edit/restart. Only then request promotion and separately approve read-only archival.

## Stop/rollback

- The Step 08 workflow is a **candidate branch-only audit** and can be deleted or reverted without touching `main`; it has **no promotion or write-back** steps.
- Preserve the original two repo SHA/branch heads and reviewed migration commits, so a cutover PR can be reverted atomically without rewriting Git history.
- **Outstanding stop gates:** the public QEAX archive content is unassessed; active contributor local clones and PowerShell execution are not signed off; the controlled 0.5 runtime and new A-15 BOM proposals are not accepted together; manual Obsidian GUI acceptance is not complete.
- Historical GitHub code and archived repos remain available for tracing; do not remove their records to force a green scan.

**Next bounded step:** Step 09 should draft a separate reviewable atomic patch for current authority documents and root CI, together with targeted provenance-aware negative tests. Do not apply it to public `main` until the security and user-acceptance gates are resolved.
