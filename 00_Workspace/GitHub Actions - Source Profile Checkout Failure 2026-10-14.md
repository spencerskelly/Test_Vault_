# Branch Cleanup — GitHub Actions Failure Diagnosis (2026-10-14)

## Confirmed cause from run logs
User supplied GitHub Actions pages for commit `60d9fb430a2d10c5b4bc0f21cbf9398adefd7052`: run 38646509833 (push) and 38646500230 (PR #43). Both failed only `importer-static-contract` at `Source profile and v0.8.19 headless compile-only`; all seven other jobs succeeded. The full job log for push run, job 116136562276, shows:

```
FileNotFoundError: [Errno 2] No such file or directory:
.../Importer/Definition/Source Profiles/EA8647-2026-09-06-v1.json
```

The Step126 sparse checkout omitted `Importer/Definition`, a runtime dependency of `Importer/Tools/v0.8.19/sync_source_profile.py --check`. The broader checkout stall was avoided, but this omission caused a deterministic test failure. GitHub HTML also displayed eight **warnings** about Node.js 20-based versions of `actions/checkout@v4`, `actions/setup-node@v4`, and `actions/setup-python@v5` being forced onto Node.js 24. They are not the cause of this exit-code-1 failure.

GitHub UI HTML additionally showed account/session and dynamic page loading warnings (e.g., 'You switched accounts on another tab' / 'Uh oh! There was an error while loading'). These appear to be GitHub UI notices and are not the source-profile missing-file exception.

## Remediation completed
Updated only `importer-static-contract` checkout in `.github/workflows/mdse-integration-readonly.yml` on `integration/p03-legacy-compat-tests-20261013`, commit `b7238e249cc9a3ab65f97cee6bdbb32f19620ab6`:

```yaml
sparse-checkout: |
  Importer/Testing
  Importer/Tools
  Importer/Definition
  Base Vault/Tools
```

Kept blobless fetch, read-only credentials, all validation commands, and all unrelated jobs unchanged. Verified the edited source with GitHub fetch_file. The new consolidated CI run 38647533105 was queued at first inspection; **passing has not yet been demonstrated**.

## Prevention
1. Enumerate local and runtime source dependencies before narrowing sparse checkouts; a static test's script can reference additional data files outside its own directory.
2. Add a cheap preflight that asserts required source-profile files are present before calling source-profile sync. Prefer error messages naming checkout dependencies, not unhandled FileNotFoundError.
3. Once this fix passes, separately review Action major versions to address Node.js 20 deprecation warnings; do not conflate warnings with test failures. Update versions across workflows in a separate coordinated PR with pinned compatibility verification.
4. Avoid redundant push + PR duplicate runs where feasible, while retaining required branch protections. Do not disable required gates just to eliminate red status.
5. Keep real QEAX/GUI acceptance, PR43 merge, branch deletion and release promotion gated.

No main modification, merge, branch retirement, source-model import or release promotion occurred.
