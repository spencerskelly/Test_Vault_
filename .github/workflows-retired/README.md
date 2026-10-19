# Retired workflows

GitHub only runs `.github/workflows/`, so nothing here executes. Files are kept (not deleted) so the history and intent stay readable.

| Workflow | Why retired (2026-10-18) |
|---|---|
| `importer-candidate.yml` | Tests the archived **V1** importer. After the folder migration its builder expects the old repo-root layout (`99_System/08_Scripts`, `99_System/03_Schemas` beside the importer), which no longer exists; 7 of 22 steps fail even with every path repaired. V2 importer tests run from `v2-migration-executable-repair.yml`. |
| `mdse-monorepo-workbench-ci.yml` | References `55_Workbench/` and `66_Testing/consolidation/`, which do not exist in this repository. Transition-era gate for the retired consolidation branch. |
| `mdse-release-alignment-preflight.yml` | References `66_Testing/consolidation/` and `66_Testing/check_release_alignment.py`, which do not exist. Same transition-era gate. |
| `bootstrap-candidate.yml` | Builds from `Bootstrap/Tools/v0.3.1`, a pre-numbering v1 path that does not exist. It also commits a rebuilt artifact back to the branch, so leaving it live and broken was the safer failure, but it should not run at all. |
| `mdse-integration-readonly.yml` | 24 of 38 steps fail: `66_Testing/consolidation/`, `55_Workbench/`, `Importer/Tools/v0.8.19/`, `Base Vault/Tools/` do not exist. A transition-era aggregate of retired gates. |
| `package-imp009-base.yml` | Runs `Base Vault/Tools/v0.8.0-r2/build-base.py` and `Base Vault/Testing/check-release.py`, v1 paths that do not exist. |
| `v2-separation-staging.yml` | One-shot migration job, already executed (it produced the relocation commit). It runs `git switch -c`, `git push` and `gh pr create` with write permission whenever its own file or `stage_v2_archive_migration.py` changes on `main`, so it was a live footgun. |

To revive one: restore the tool paths first, move the file back to `.github/workflows/`, and confirm it passes locally before pushing, because a workflow whose own file changes triggers itself.
