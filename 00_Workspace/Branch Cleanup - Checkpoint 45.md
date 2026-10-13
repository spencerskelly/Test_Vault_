# Branch Cleanup — Checkpoint BR-45: Existing CI Coverage and Non-Duplicate Release Test Plan

**Date:** 2026-10-12
**Repository:** spencerskelly/Test_Vault_
**Audit PR:** #41
**Candidate:** consolidation/step22-single-repo-cutover-2026-10-11 @ 58ab10870f11757cf1bf367ecd5868be9b60933d
**Status:** SOURCE COVERAGE REVIEW; exact-SHA complete release execution not verified

## Evidence inspected

1. Step22 workflow `.github/workflows/consolidation-step22-cutover.yml` (blob e23e950f81ea5dcdc88789fbd7a3eddfe05ad478): scoped to staging branch and four cutover files; read-only sparse checkout explicitly excludes `EA_2026_09_06_endgame.qeax.zip`. Invokes ONLY `python3 -m unittest discover -s 66_Testing/consolidation -p 'test_step22_retirement.py' -v` plus inventory assertions. It **does not invoke** `Base Vault/Testing/check-release.py`.
2. `66_Testing/consolidation/test_step22_retirement.py` (blob dc009e86bf411f682d65548cfdc2e0ac17780568): 14 `unittest` methods for provenance/inventory/source history, preserved SHA and explicit incomplete signoffs.
3. `Base Vault/Testing/check-release.py` (blob aae6d70357fbeea2c56aac7c3307604750dfdefe): comprehensive static source/manifest/lock checks and optional `--workbench` fixture parity and `--base` exact generated vault validation; exit 1 on any FAIL, warnings nonfatal. See BR-43/44.
4. The current default-branch `Base Vault/README.md` reports an earlier (2026-10-03) build of a Bootstrap-0.3.1 candidate Base and `check-release.py --base` yielding **0 fail / 4 expected pre-release warnings**. This is **documented historical result**, not a freshly executed test of the frozen Step22 candidate.
5. Current default-branch `Base Vault/Testing/Candidate Model Repository Preparation.md` calls for building an empty Base via `Base Vault/Tools/v0.8.0-r2/build-base.py` and checking it with `--base` prior to initialization.
6. Connected GitHub code search indexes default branch only; it was **not an exhaustive inventory of all workflows at the Step22 tip**. Other workflows may cover these tests. Do not conclude the repository has no additional coverage based on this bounded check.

## Coverage map

| Validation | Existing test/code | Verified Step22 CI run? | Proposed action |
|---|---|---|---|
| Standalone Workbench history coverage and controlled shutdown evidence | Step22 test module and workflow | YES — historical run 38192743995 job success; 14/14 reported | Preserve unchanged |
| Release metadata, schema alignment, source profile, doc registry, plugin lock/payload | `check-release.py` | NOT established by Step22 workflow | Run separately on authorized exact final SHA |
| Workbench fixtures, package/manifest version, user guide parity | `check-release.py --workbench '55_Workbench'` | NO in verified Step22 workflow | Invoke optional path on approved exact SHA |
| Deterministic uninitialized Base build and exact contents/hashes | `build-base.py` then `check-release.py --base <disposable-folder>` | NO in verified Step22 workflow; historical Base README describes prior passing candidate | Execute disposable test in governed CI |
| Full importer/Workbench/Bootstrap behavior and fail-closed negatives | Other test suites and runtime tests; not enumerated in this pass | NOT VERIFIED | Inventory existing suites and reuse rather than replicate |
| Real QEAX attachment/whole-model regression | Requires security-approved archive handling | NOT VERIFIED | Security decision first; use private authorized environment only |
| Real Mac/Windows Obsidian GUI operator cases | Human acceptance plans | NOT RUN based on available evidence | Execute separately; cannot be simulated by Python CI |
| Governance approvals, QEAX exposure decision, private local Git work signoff | Owner decisions, not automated tests | NOT AUTOMATABLE BY CODE | Keep independent hard HOLD |

## Minimal non-duplicative validation pipeline suggestion (PROPOSAL — no workflow changed)

1. Identify existing active release workflow jobs and their exact test calls before authoring new CI. Keep Step22 retirement job as a narrow, historically scoped check.
2. In security-approved environment at pinned exact commit, run basic checker `python3 'Base Vault/Testing/check-release.py'`; capture count of warnings and failures.
3. Run `python3 'Base Vault/Testing/check-release.py' --workbench '55_Workbench'`.
4. Build a **disposable** clean Base with the manifest-pinned r2 builder; run `python3 'Base Vault/Testing/check-release.py' --base '<output>'`. Run with both optional flags when practical.
5. Reuse existing importer and Workbench runtime tests; add only missing negative/contract coverage proven absent after test inventory.
6. Record test SHA, environment, checker warning dispositions, logs, and test names. Only the exact reviewed SHA can be considered for promotion.
7. Separately obtain Mac and Windows Obsidian GUI signoff, explicit W/document approvals, private QEAX owner decision, and contributor-local work preservation.

## Explicit limits / handoff

**BR-45 completed:** demonstrated that Step22 cutover CI does not call full release checker, identified existing broader checker/build tests and historical Base validation without falsely declaring current CI green. No exhaustive scan of every workflow on Step22 and no execution on frozen candidate occurred.

**NEXT BR-46:** Inspect named active controlled-release workflow(s) or current test inventory and close the remaining CI coverage uncertainty; keep output to evidence rather than adding duplicate jobs.

**NO ACTION:** No workflow updates, release, merge, deletion, public QEAX download or archival.
