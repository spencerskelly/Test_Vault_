# Pass 6 — CI evidence gate status and value checks

Date: 2026-10-17. GitHub commit status lookup returned zero status records and the available commit-workflow lookup returned zero runs for `c7947a2` (the latter exposes PR-triggered runs only). This is **not evidence of CI pass or failure**. Local container cannot resolve `github.com` for `git clone`, so exact checkout tests were not run here.

Added `raw_evidence_values` to distinguish present columns from valid original endpoint type/aggregation flag values. Unspecified direction, optional source roles and cardinalities remain source evidence and are not guessed. Four synthetic value tests added and included in the dedicated GitHub Actions workflow. Verified the workflow's tracked path strings and test command after amendment; CI completion is still unverified. No proprietary data committed.

Open acceptance gates: successful CI run with job logs, direct clean-checkout exact tests, source registry digest pin, native parser verification, and production BOM workbook input. `nativeCertified=0`; native emission disabled.
