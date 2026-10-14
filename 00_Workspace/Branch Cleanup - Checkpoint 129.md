# Branch Cleanup — Checkpoint 129 (2026-10-14)

## Concurrency diagnosis
Read `.github/workflows/mdse-integration-readonly.yml` on `integration/p03-legacy-compat-tests-20261013`. Workflow concurrency is:

```yaml
concurrency:
  group: mdse-integration-readonly-${{ github.ref }}
  cancel-in-progress: true
```

The two pinned commit lookups show older consolidated run [38645129012](https://github.com/spencerskelly/Test_Vault_/actions/runs/38645129012) still `in_progress` and newer narrowed-checkout run [38646509833](https://github.com/spencerskelly/Test_Vault_/actions/runs/38646509833) still `pending`. Earlier job query returned no jobs for the newer run. Earlier inspection showed the older run's `importer-static-contract` job still in checkout.

## Interpretation
Both runs use the same integration validation branch and hence are expected to share a concurrency group. With `cancel-in-progress: true`, GitHub would ordinarily cancel a superseded running instance, but that outcome is **not reflected in current run status**. The presence of a pending newer run plus an in-progress older run is consistent with a scheduling/concurrency blockage, but is not sufficient to prove the root cause. Logs for the old job previously returned BlobNotFound. No new checkout code is running yet.

## Controls and next step
No cancellation, workflow modification, merge, release or branch removal was performed. Next Step 130: inspect workflow run metadata/queue and the stale checkout job; if still blocked, obtain authorization before any manual cancellation. If cancellation is approved, cancel only the superseded run ID, confirm new run progresses and that importer checkout/tests pass. The actual QEAX and generated vault acceptance remain separate.
