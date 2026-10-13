# Branch Cleanup — Checkpoint BR-44: Complete Release Checker / Final Promotion Gate

**Date:** 2026-10-12
**Repository:** spencerskelly/Test_Vault_
**Audit PR:** #41
**Candidate ref:** consolidation/step22-single-repo-cutover-2026-10-11
**Candidate SHA:** 58ab10870f11757cf1bf367ecd5868be9b60933d
**Code source:** `Base Vault/Testing/check-release.py`, Git blob `aae6d70357fbeea2c56aac7c3307604750dfdefe`
**Status:** Entire checker source inspected, no execution performed.

## 1. Remaining importer/release checks

The final importer section prohibits old length-driven path logic, full-path link targets, old Local Model markers and malformed Source Map fields. It warns in a pre-release (fails when issued `release`) if importer release is null, clean Base repository is null, or old importer revisions remain outside the designated history directory. It requires the retired importer history directory and benchmark validation. These are static-source checks, not whole-model execution tests.

## 2. Optional `--workbench` checks

When invoked with `--workbench PATH`, the checker compares normalized `relationships.yaml`, `element-types.yaml` and `local-model.yaml` in Workbench test fixtures to authority in `99_System/03_Schemas`; requires the historic `local-model-0.1.yaml` fixture; matches `package.json` and `manifest.json` versions to pinned Workbench release or an explicitly declared pre-release candidate; and compares normalized Workbench `docs/User Guide/MDSE Workbench User Guide.md` to the Base Vault user-guide release copy.

**Without `--workbench`, none of these optional checks are run.**

## 3. Optional `--base` checks

With `--base PATH`, checker reads generated `.vault.yaml` for `mdse_release` and `UNINITIALIZED` vault UID; assembles an exact allowed-file set from manifest includeFiles, includeTrees, mapped, conditional, generated and packaged plugins; checks missing and extra files; SHA-256 compares Base files and plugin payloads against source; disallows forbidden workspace-only paths; checks Base README release identification, Workbench presence for issued release, Bootstrap pin+enable in plugin configs and governed `.gitignore` behavior.

**Without `--base`, generated Base completeness, extra-file exclusions and file parity are not checked.** Test only a safely generated disposable Base vault, never an operating vault.

## 4. Exit semantics

The implementation appends failures and warnings separately, prints `N fail, M warn`, then exits `1 if fails else 0`. **Warnings are not fatal for exit status.** Some pre-release inconsistencies are explicitly warnings but become failures for `releaseStatus: release`, including missing issued importer/clean base and importer revision cleanup. Capture both counts and warning text; do not treat exit 0 with warnings as final release approval.

## 5. Exact-SHA promotion execution matrix

| Stage | Action | Required evidence |
|---|---|---|
| 0 | Fix a reviewed, authorized exact SHA in secure disposable checkout, with QEAX handling approved | Git SHA, authority, safe checkout scope |
| 1 | Run `python3 'Base Vault/Testing/check-release.py'` | Exit, `N fail, M warn`, full log, manifest and lock refs |
| 2 | Run `python3 'Base Vault/Testing/check-release.py' --workbench '55_Workbench'` | Workbench fixture/version/user-guide parity, explicit warning disposition |
| 3 | Build a disposable Base with approved build command and run `python3 'Base Vault/Testing/check-release.py' --base '/path/to/generated-base'` | Exact allowed-file parity, hashes, excluded paths, Bootstrap enablement |
| 4 | Optionally combine both flags for final parity: `--workbench '55_Workbench' --base '/path/to/generated-base'` | Both optional code paths executed together |
| 5 | Run separate importer/Workbench/Bootstrap tests, including invalid inputs, fail-closed negatives and real-QEAX regression only if approved | CI logs, case counts, error handling and safe benchmark artifacts |
| 6 | Execute actual Mac and Windows Obsidian operator acceptance | Signed observed results and residual defects |
| 7 | Confirm document/W decisions, public QEAX exposure owner determination, contributor local Git inventory, PR reviews and branch protection | Explicit approval references for each independent gate |
| 8 | Obtain separate approval for `main` promotion, and separate approval for old repository archive or remote branch retirement | Decision record; no implicit action |

**Important:** Steps 1–4 are implemented checks but **not executed in this checkpoint**, and steps 5–8 are not replaced by their success. The manifest currently declares MDSE `0.8.0` `pre-release`, importer `release: null`, Bootstrap `0.3.0` active and Workbench `0.1.18`; release-authority status is unchanged.

## 6. Handoff

**BR-44 result:** Completed source review of `check-release.py`, filled the BR-43 missing optional-path and exit-semantics details, and specified an executable exact-SHA validation sequence.
**NEXT BR-45:** Check whether the existing Step22 CI or other workflow already invokes the full checker with both optional flags and whether any end-to-end acceptance evidence is linked. Avoid introducing duplicate CI or declaring unrun tests green.
**NO ACTION:** No merge, closure, branch deletion, generated-vault mutation, model download, release promotion or repository archive.
