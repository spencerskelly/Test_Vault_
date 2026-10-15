# Step 59 — Historical reproduction execution status (2026-10-14)

## Verified

- At Step58 commit `9adcd5d0bf0632965b0f1235a1263575f50a1298`, the connected GitHub workflow-run lookup (PR-triggered only) returned three completed runs:
  - `38603965655`: MDSE consolidated read-only integration — success.
  - `38603965666`: P03 legacy compatibility synthetic tests — success.
  - `38603965698`: P04 Workbench read-only build and tests — failure (existing release-artifact equivalence gate; do not waive).
- No Step58 historical reproduction run appeared in that lookup. **Because the connector lists PR-triggered workflows only, this is not evidence that no push-triggered run occurred.**
- The Step58 workflow originally specified a push trigger and manual dispatch but no PR trigger. Added PR trigger against frozen Step22 for changes to `.github/workflows/step58-historical-reproduction.yml`, committed as `f2a120810a3443db126f57b3e5ad34471fcd1861`.
- The first immediate run lookup for the PR-trigger commit returned no runs. The historical reproduction experiment is **not yet proven to have executed**; no experimental hash should be reported.

## Gate

Release status: **HOLD** until historical source compile provides node/npm/dependency versions, fresh `main.js` SHA-256, and whether the governed SHA-256 `1690d32a0c05e496366199b8ead7247eab42314a940ada8de3a0a1f109fcb0a7` is reproduced.

## Required Step60

1. Retrieve workflow runs for Step58 PR-trigger commit `f2a120810a3443db126f57b3e5ad34471fcd1861`, and inspect job logs if any.
2. If still absent, verify GitHub Actions recognizes a workflow introduced only on the validation branch; inspect whether the default-branch registration or event semantics are blocking it. Do not change main solely to force registration.
3. If the historical experiment runs, extract exact SHA-256 and runtime versions and update this record.
4. If no automatic run is possible, retain a review-only fallback: local detached historical checkout or separately reviewed manual dispatch with no artifact promotion.

No model, QEAX, original bundle, release manifest, historical branch or main modification is authorized.
