# Branch Cleanup — Checkpoint 115 (2026-10-14)

## Focused regression correction
Inspection of Step114 `test_imp011_topology_v2_step114.py` found that it subclasses `Imp011TopologySynthetic`, thereby inheriting v1 test methods whose module-level `check` points to `imp011_topology_acceptance.py` (v1), not v2. The resulting test discovery can mix v1 and v2 assertions. Preserve this finding and avoid treating inherited tests as v2 evidence.

Added `66_Testing/consolidation/test_imp011_topology_v2_step115.py`, commit `db23b51d9f93063c087599e181b8c02fe6701eef`. It subclasses `unittest.TestCase` directly, reuses setup-only fixture utilities, and explicitly invokes `imp011_topology_acceptance_v2.check` for all five tests: valid equals, invalid owner path, broken symmetry, Flow-safe exposure, ambiguous exposure rejection.

Added read-only `.github/workflows/step115-imp011-v2.yml` at `4b816b81b5128fd7ce7b2c623aa5c78e6a93fbf4` to run these five tests on Python 3.12 with sparse checkout.

## Verification
GitHub commits confirmed. Immediate workflow lookup for commit `4b816b81b5128fd7ce7b2c623aa5c78e6a93fbf4` returned no runs, so no CI PASS claim. New test code has **not yet been locally executed**. Earlier v1 synthetic acceptance and owner-path-only tests remain separate passing evidence.

## Next Step 116
Verify Step115 CI execution at pinned commit and inspect job logs on failure; correct any fixture lifecycle or import issues. Then run duplicate-basename/nested-path cases against the full v2 checker, preserve baseline-failure propagation, and prepare real QEAX acceptance. No merging, branch deletion, main modification or release promotion.
