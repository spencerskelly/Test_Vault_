# Branch Cleanup — Checkpoint BR-46: Release CI Inventory Boundary

**Date:** 2026-10-12
**Repository:** spencerskelly/Test_Vault_
**Audit PR:** #41
**Candidate:** consolidation/step22-single-repo-cutover-2026-10-11 @ 58ab10870f11757cf1bf367ecd5868be9b60933d
**Status:** PARTIAL SOURCE INVENTORY — full workflow enumeration remains unverified

## Verified evidence

1. The Step22 workflow `.github/workflows/consolidation-step22-cutover.yml` has a narrow path-filtered, branch-scoped retirement-integrity job; it calls the 14-test `66_Testing/consolidation/test_step22_retirement.py`, not the full release checker. Its historical CI run was successful (see BR-41).
2. Direct fetch on Step22 confirms `Base Vault/Testing/Candidate Model Repository Preparation.md` (blob `77525b687b20127f07bb02f74ea9e582fde5e98f`) defines **three stages**: deterministic clean artifact; initialized/imported candidate repository; accepted operational/golden repository. Stage 1 specifically calls `Base Vault/Tools/v0.8.0-r2/build-base.py` and `Base Vault/Testing/check-release.py --base <folder>`, with zero failures and `vault_uid: UNINITIALIZED`. Stage 2 was explicitly deferred at that document's 2026-10-03 checkpoint pending importer/Workbench alignment. It must be re-evaluated, not blindly overridden.
3. The existing checker supports `--workbench` and `--base` source/fixture/payload parity and controls (BR-43/44); source implementation is verified, but test execution on a final promotion SHA is not.
4. GitHub search for `check-release.py` finds Base Vault, Bootstrap, workspace and importer documentation/script references in the **default branch search index**. It does **not** provide a complete inventory of `.github/workflows` on Step22 and did not prove existence of an exact-SHA full-release CI job.
5. The following *hypothesized conventional workflow names* were probed directly at Step22 and absent: `.github/workflows/mdse-release-check.yml`, `release-check.yml`, `ci.yml`, `base-vault-ci.yml`, `importer-workbench-compatibility.yml`, and `consolidation-step18-registry.yml`. Their absence **does not** imply other named workflows or relevant CI runs are absent.

## Current evidence map

| Coverage type | Source/procedure confirmed | CI on final promotion SHA confirmed? | Next treatment |
|---|---|---|---|
| Step22 Workbench retirement / inventory integrity | YES; historical job passed | Historical Step22 SHA job only | Preserve, do not duplicate |
| Base r2 builder + controlled release checker | YES; source and stage 1 procedure | NO | Reuse existing builder/checker on exact SHA |
| Workbench fixture/user-guide parity | YES; checker `--workbench` | NO | Exercise existing optional flag |
| Clean Base file set, plugin payload integrity | YES; checker `--base` | NO | Build disposable artifact, run checker |
| Real importer/Workbench/Bootstrap behavior | Existing project test architecture; exact active CI inventory not established | UNKNOWN | Enumerate actual workflow files and test suites before new CI |
| QEAX whole-model / attachment regression | Requires private data-owner decision | NO, cannot run without approval | Hold pending security classification |
| Mac and Windows Obsidian GUI acceptance | Separate documented operator process | NO | Real operator evidence required |

## No-duplication decision

Do not invent a new `mdse-release-check.yml` or broaden the Step22 retirement workflow without first enumerating the true current workflow set. Once names and triggers are verified, add the **minimum missing invocation** of already-existing `build-base.py` / `check-release.py` through a separate reviewed proposal. Preserve the historical retirement/audit job scope.

## Handoff / needed next evidence

- Obtain an exact Step22 Git tree listing for `.github/workflows/` and test-suite locations through a trusted Git checkout or a connector tree/list action with full SHA scope; inspect all real workflow triggers and commands.
- Map each CI job to required release tests and spot genuinely missing tests only after that exhaustive inventory.
- Remain blocked on QEAX owner decision, contributor-local work, W/document approvals, current release checks and Mac/Windows GUI acceptance.

**BR-46 output:** Honest coverage boundary, directly fetched stage-1 preparation contract and absence of six named conventional workflow paths; **not** an exhaustive workflow audit and **not** execution of release tests.

**NEXT BR-47:** Enumerate actual Step22 workflow tree and create a complete non-duplicative CI wiring map if tooling permits; otherwise focus on a supported end-to-end acceptance artifact without guessing paths.

**No operations:** No merge, PR closure, branch deletion, workflow edits, release promotion, model download or archival.
