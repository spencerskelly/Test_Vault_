# Branch Cleanup — Checkpoint 126 (2026-10-14)

## Stalled importer-static-contract job
Requeried run [38645129012](https://github.com/spencerskelly/Test_Vault_/actions/runs/38645129012): `importer-static-contract` remains `in_progress` at `Checkout source contracts without archived QEAX`; its test steps are still pending. Seven other jobs are complete/success.

## Targeted mitigation committed
Updated `.github/workflows/mdse-integration-readonly.yml` on `integration/p03-legacy-compat-tests-20261013`, commit `60d9fb430a2d10c5b4bc0f21cbf9398adefd7052`. **Only** `importer-static-contract` checkout changed:
- Replaced broad non-cone sparse checkout (`/*` excluding source ZIP) with cone-mode sparse checkout of `Importer/Testing`, `Importer/Tools`, and `Base Vault/Tools`.
- Preserved `filter: blob:none`, `persist-credentials: false`, and all existing static checks and their commands.
- The checked commands reference importer testing/tools and Base Vault builder under these directories. Other jobs and workflow permissions are unchanged.

## Verification and limits
GitHub commit succeeded. Immediate workflow lookup for new commit returned no runs, so this mitigation is **not yet verified by CI**. Cause of original stalled checkout has not been established; narrower checkout is a risk-reduction candidate, not proven root-cause fix.

## Next Step 127
Verify GitHub Actions at commit `60d9fb430a2d10c5b4bc0f21cbf9398adefd7052`, with specific attention to `importer-static-contract` checkout and static tests. If failure, inspect missing paths or test dependencies before modifying workflow again. Real QEAX + generated-vault acceptance and GUI remain separate unverified gates.

No main commit, merge, branch deletion, release promotion or model signoff.
