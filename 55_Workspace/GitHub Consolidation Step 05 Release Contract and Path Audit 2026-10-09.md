# GitHub Consolidation — Step 5: Unified Release Contract and Path Audit

**Date:** 2026-10-09
**Status:** Completed diagnostic implementation; **not a release**.
**Plan source:** [[GitHub Consolidation Recovery Inventory 2026-10-09]]
**Prior:** [[GitHub Consolidation Step 04B Persisted Workbench Import 2026-10-09]]
**Active integration proposal:** [Test_Vault_ draft PR #8](https://github.com/spencerskelly/Test_Vault_/pull/8), branch `integration/workbench-subtree-2026-10-09`.

## What was implemented and verified

Created the first common testing directory using the user-approved numbered layout:

- `66_Testing/migration-path-plan.json` — explicit current-to-target folder map, unresolved `Cross-Vault` designation, version ownership, and acceptance gates;
- `66_Testing/check_release_alignment.py` — **read-only** standard-library diagnostic; reads existing release manifest and generated plugin lock, Workbench component metadata, schemas, registered workspace docs, and Git-tracked old-path references; emits structured JSON; offers a separate future `--strict` mode (not enabled for pre-release);
- `.github/workflows/mdse-release-alignment-preflight.yml` — read-only root GitHub Actions preflight on the integration branch. Publishes JSON findings; **does not change the release manifest, generated plugin lock, Git history or build artifacts**.

[Verified run #37971452217](https://github.com/spencerskelly/Test_Vault_/actions/runs/37971452217): **success**. Reports 12 warnings / 0 blocking check errors in diagnostic mode; the green CI job means the **audit ran**, not that the model is release-aligned. JSON artifact `mdse-release-path-audit-75eff6007af46e19f36f76b38df44658ac381ba5` is retained in Actions for the configured period. The earlier [first successful run #37971352743](https://github.com/spencerskelly/Test_Vault_/actions/runs/37971352743) also confirmed the detector and upload.

## Authority model — decisions to preserve

**One authoritative release manifest:** Existing `Base Vault/Definition/mdse-release.yaml` remains the release authority until the folder is deliberately renamed to `33_Base Vault/Definition/mdse-release.yaml` and all readers are patched as one reviewable migration. Do not introduce a competing canonical manifest.

**Separate three different truths:**

1. **Released/controlled pin** — manifest, generated `.obsidian/plugin-lock.yaml`, base/runtime payload and matching hashes must agree. Do not manually edit the generated lock.
2. **Development candidate** — imported Workbench source and unreconciled Importer/LM/BOM branches. Candidate version is **not** a release promotion.
3. **Verified integration** — one specific combined repository commit + checked hashes, approved schemas, importing/builder/Bootstrap startup/Workbench read/edit/reload acceptance. Workbench's 443 standalone tests alone do not establish this.

Each component may retain its own software version. The authoritative **integrated release ID + commit + artifacts** resolves which versions are compatible. A commit-level release snapshot must be reproducible.

## Observed version alignment (staged branch)

| Component | Declared controlled state | Other observed state | Status |
| --- | --- | --- | --- |
| MDSE release | 0.8.0, `pre-release` | No accepted combined candidate | Not promoted |
| Workbench | manifest pin and plugin lock: 0.1.16 | imported package + plugin manifest: 0.1.18; manifest candidate 0.1.17 | Candidate/pin mismatch, intentional until review |
| Bootstrap | manifest pin 0.3.0 | generated plugin lock 0.3.1 | **Pin/lock drift to reconcile**, no direct edit to generated lock |
| Importer | manifest candidate v0.8.6 | separate active PR #5 candidate v0.8.19 | Candidate history/source not yet integrated |
| Schemas | manifest relationships 1.35, element-types 1.17, Local Model 0.2 | current staged schema files match these declared versions | Baseline files matched; advanced LM 0.5 remains unmerged |

## Directory move map and counted textual dependencies

| Current root | Approved destination | Tracked files containing source-path text | Disposition |
| --- | --- | ---: | --- |
| `Definitions/` | `11_Definitions/` | 20 | Pending |
| `Importer/` | `22_Importer/` | 19 | Pending — account for PR #5 |
| `Base Vault/` | `33_Base Vault/` | 28 | Pending — builder, manifest, CI and generated paths |
| `Bootstrap/` | `44_Bootstrap/` | 18 | Pending — managed runtime startup |
| `Cross-Vault/` | Unresolved | 7 | Explicit manual classification; don't default into external resources |
| Standalone `spencerskelly/MDSE_Workbench` references | Now `55_Workbench/` within same repo where applicable | 24 | Update active tool authority references; keep historical provenance links |
| New `66_Testing/` | `66_Testing/` | n/a | **Established in staging** |
| New `88_Resources/` | `88_Resources/` | n/a | Pending; external information only |
| `99_System/`, `00_Workspace/`, root workflows, `.obsidian/` | Same paths | n/a | Retain |

Counts are **tracked files with the literal token**, not number of occurrences. Files may count in multiple rows. They are a lower-bound migration map, not proof every dynamic, generated, binary or Obsidian wikilink dependency is covered. The machine-readable audit artifact contains up to ten example paths per token.

## Document registry and important implementation hazard

The release manifest's `documents` registry is referenced by `Base Vault/Testing/check-release.py`. The audit reports **8 `00_Workspace/*.md` files currently absent from that registry**, including recent recovery records. Reconcile and register active planning documents as current/reference as appropriate when finalizing the manifest (do not claim existing full release checker is green solely because the new diagnostic passes).

The current `Base Vault/Tools/v0.8.0-r2/build-base.py` uses a source-relative root calculation and explicit `Base Vault/Definition/mdse-release.yaml` path. Its relative `ROOT` ascent remains valid at the same folder depth after renaming, but the hardcoded manifest name will not. The release include lists, runtime mappedFiles/forbiddenPaths, initialization scripts, generated references, CI working directories, `.obsidian/plugin-lock.yaml` generator comments and current-state/decision links also need review during the rename. Do **not** globally replace text within historical evidence.

## Approval gates to leave audit mode

1. Preserve workstation-local dirty/untracked/unpushed work and all remote feature branches, particularly Importer PR #5, LM 0.5, WB-129 and BOM.
2. Select and reconcile importer/Workbench candidate revisions; update canonical schemas and tool definitions together rather than mass-bumping version strings.
3. Stage numbered root migrations as atomic, path-audited work. Update **source references first or simultaneously**, never break the release builder on an intermediate protected main commit.
4. Generate pinned plugin artifact/lock through the approved release generator and verify checksum alignment; do not manually edit lock YAML or accept stale hashes.
5. Run strict release-checker and all component, integration, real-QEAX, base-build, first-open/Bootstrap and Workbench read/edit/reload acceptance on the same integration commit.
6. Only after all gates: change manifest to `release`, tag the integrated repository commit and approve PR promotion. Do not archive old tool repo before its standalone history and local-only work are accounted for.

## Current state / next bounded task

**Completed:** machine-readable path plan, executable audit, CI and machine-readable results, version-drift identification, directory-dependency reference counts. No root folder moved; no version promoted; no main branch changed.

**Next (Step 6):** compare importer PR #5's changes and path consumers against the combined integration branch, design an exact cherry-pick/merge/rebase strategy that retains its 475-commit history, and pick a first atomic directory migration with tests. The current staging's `Base Vault/` and `Importer/` paths should not be bulk-renamed while the large importer PR remains unresolved.
