# Pass 6 — CI acceptance operator gate (2026-10-17)

**Status: BLOCKED / not verified.** The tracked workflow exists at `.github/workflows/phase8-evidence-verification.yml`, and its job runs Python syntax validation plus all four exact checked-out Phase 8 test modules on `ubuntu-latest` with Python 3.11. Its `push` path filter includes the workflow file, and it supports manual `workflow_dispatch`.

## Independent status observations
- GitHub connected combined commit status for `c7947a23c6f2d491d37a4617579834b74bc13fd2`: 0 records.
- Available connected commit-workflow listing: 0 records, **but the connected action filters PR-triggered runs**, so it cannot prove the absence of a push-triggered job.
- Local container Git HTTPS checkout: unavailable because github.com DNS resolution failed.
- Public workflow page could not be fetched in this environment.
- Therefore **no CI pass and no CI failure are claimed**.

## Operator acceptance instructions

1. Open https://github.com/spencerskelly/Test_Vault_/actions/workflows/phase8-evidence-verification.yml and select **Run workflow** on `main`, or inspect the latest push-triggered execution.
2. Open its `synthetic` job. Verify checkout, Python 3.11 setup, source compilation and the `unittest -v` command all report completed/success.
3. Capture the **workflow run URL, commit SHA, test count, conclusion and UTC timestamp**, without uploading source model rows or artifacts.
4. If any step fails, preserve the job error text and apply the smallest tested patch on `main`; do not mark Pass 6 accepted until a rerun succeeds.
5. Run local QEAX and BOM content checks separately, without uploading them to GitHub Actions.

## Known scope limitations

The CI suite exercises **synthetic examples only** and cannot certify the 14,688-row private QEAX import, the central registry's semantics or native SysML v2 parser. The Phase 8 source ledger and all source identifiers stay local. **nativeCertified = 0; native emission disabled.**
