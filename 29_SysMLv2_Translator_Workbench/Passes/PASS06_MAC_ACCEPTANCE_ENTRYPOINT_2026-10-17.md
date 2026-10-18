# Pass 6 — Mac-based acceptance entrypoint

Date: 2026-10-17. The user's macOS Git pull/commit/push is functioning; the assistant container's GitHub DNS restriction does not imply a user-side Git problem.

## Tools completed
- Fixed a malformed filename in `.github/workflows/phase8-evidence-verification.yml` and included the original-field mapping regression module (commit `dc413816`).
- Added `15_Testing/run_pass06_acceptance.py` (commit `1da8d6a`) to run all eight synthetic Phase 8 test modules using the local Mac's checkout. A private --report path **outside the repo** is mandatory. Optional --qeax and --ledger must be supplied together to run independent source fidelity. The script does not access the network, publish source records, or perform any native SysML v2 emission.

## Suggested Mac command (from Test_Vault_ checkout)
```sh
git pull --ff-only origin main
python3 15_Testing/run_pass06_acceptance.py --report "$HOME/Desktop/pass06-acceptance.local.json"
```
For a separate local-only QEAX/ledger check, provide `--qeax "/absolute/path/to/source.qeax" --ledger "/absolute/path/to/local_only_phase8_ledger.csv"` alongside a fresh `--report` path.

## Acceptance limitations
The runner's `revision` entry is deliberately `local-checkout-unattested`: successful tests require separate `git rev-parse HEAD` and clean-worktree capture before claiming a pinned checkout. Synthetic test pass alone does not establish full source coverage, semantics, CI success, or native parser certification. The private aggregate report stays outside GitHub and source-specific local ledgers must never be pushed. The Python module and workflow modifications have not yet been observed executing on the user's Mac or on GitHub Actions. **nativeCertified=0; Pass 6 open.**

Next gate: run exact checkout test entrypoint, collect pass/fail and checkout SHA, correct concrete failures, then proceed to independently parsed SysML v2 synthetic fixtures and native canonical graph implementation.
