# Final Consolidation — Step 9 Release Lock and CI Trigger Review

Date: 2026-10-14
Candidate: `integration/final-preservation-stage-20261014`; unchanged by this review.

## Read-only exact-file findings
- `Base Vault/Definition/mdse-release.yaml`: `releaseStatus: pre-release`; Workbench version and WB106 pin both `0.1.18`; importer candidate `0.8.19`; Local Model `0.5`.
- `Base Vault/Runtime/Plugins/mdse-workbench/manifest.json`: `0.1.18`.
- `.obsidian/plugin-lock.yaml`: Workbench `0.1.18`. **These three Workbench version declarations agree.** The lock contains SHA-256 hashes, but this pass did not compute runtime artifact SHA-256 independently.
- Bootstrap manifest *declared pinned source* remains `0.3.0`, with candidate source `Bootstrap/Tools/v0.3.1`; actual locked packaged Bootstrap is `0.3.1`. `Base Vault/Testing/check-release.py` explicitly treats this as a **warning** rather than failure **only when** pre-release and lock matches the candidate manifest and package versions. We verified candidate manifest `0.3.1`; we have not executed the full Python checker against exact staging, so no pass claim.
- Workflow `.github/workflows/mdse-integration-readonly.yml` is still push-filtered to `integration/p03-legacy-compat-tests-20261013` and PR-targeted to Step22, not the staging branch / future stable branches. This explains why a documentation-only commit on the newly created staging branch did not automatically prove its CI status.

## CI migration recommendation
1. Keep synthetic/static checks and protected-branch gate intact.
2. In a *reviewed staging CI-change commit*, add appropriate `pull_request` coverage for target `main` and `develop`, `workflow_dispatch` for exact-ref audits, and choose whether to keep push checks for `develop`. Avoid unrelated broad action upgrades in the same change.
3. Remove obsolete branch-specific push targets only **after** exact-head validation/branch cutover; otherwise it may make the current PR validation unavailable.
4. Verify the lock hashes using `python3 'Base Vault/Testing/check-release.py'` on the checked-out staged tree. Any warnings must be retained in the report, including the intentional Bootstrap candidate state.
5. Run exact-head consolidated test suite and confirm test/check status against the candidate's final commit; previous passing ancestor alone is insufficient.

## Release and cleanup boundary
This candidate is pre-release and not real-QEAX or Mac/Windows GUI accepted. No promotion, release, merge, deletion, or main write occurred. Development baseline and production/release acceptance remain distinct gates.
