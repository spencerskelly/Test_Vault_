# Step 84 — Negative gate verified and PR42 integration preflight (2026-10-14)

## Verified
GitHub Actions run 38614959801, job 116027568046, completed SUCCESS. The compatible Local Model input passed and the disposable 0.7 schema case was rejected, completing positive and fail-closed coverage for `.github/workflows/step82-importer-workbench-contract.yml`.

## Important integration blocker

PR #42 (`integration/lean-test-infrastructure-20261013` to `main`) remains open/draft, tip `4eaddbd1364633ba21038dc85a51a76c374d354d`. Its changed files are limited to two CI workflows and two testing scripts. The main-based branch and main BOTH currently lack:
- `66_Testing/check_importer_workbench_localmodel.py`
- `55_Workbench/src/core/localmodel.ts`

A version of `99_System/03_Schemas/local-model.yaml` exists there but has a different blob from Step22/PR43. Therefore **DO NOT simply copy the Step82 job into PR42**: it would fail on absent inputs or, worse, give misleading results if paths were relaxed. The checker must become active only after a reviewed Workbench-and-importer source integration delivers all required files and correct release/schema contracts.

## Proposed safe route

1. Preserve Step82 workflow + checker on PR43; commit SHAs and passing CI recorded.
2. In PR42, document the future integration dependency (this note), rather than modify a workflow that cannot run correctly against its main-based source.
3. On an explicitly reviewed integrated candidate containing all four required inputs, migrate exact Step82 positive and disposable negative jobs into authoritative CI. Keep required paths and fail closed if absent; do not default to success.
4. Verify end-to-end checks on target merge SHA before retiring the temporary Step82 validation workflow.
5. Maintain independent release, real-QEAX, macOS/Windows GUI, ancestry, and branch-deletion approvals.

No edits to PR42, main, model/schema, historical artifacts, release pins or branch refs performed here.

## Step85
Review the actual Step22-to-main source integration candidate and release manifest/schema version changes, then propose an atomic promotion sequence that makes the compatibility checker runnable on the authoritative CI branch without transient false failures.
