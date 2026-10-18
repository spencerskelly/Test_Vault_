# Pass 6 — Mac checkout synthetic acceptance result (2026-10-17)

User-executed on macOS against `spencerskelly/Test_Vault_` after a successful `git pull --ff-only origin main`. Terminal output shows main fast-forwarded from `59aacb0d2` to `831e538ad`, then executed:

```sh
python3 15_Testing/run_pass06_acceptance.py --report "$HOME/Desktop/pass06-acceptance.local.json"
```

**Result:** 25 tests, 25 passed, 0 failures, 0 errors (0.039s). JSON status `PASS_SYNTHETIC_ONLY`; `nativeCertified: 0`. This is direct evidence of the exact repository checkout's synthetic test modules running on the user's Mac. Output report remains local on the user's Mac; no proprietary records or source model data were provided or committed.

**Acceptance decision:** close the *Mac checkout synthetic regression execution* gate. Do **not** close the full Pass 6 native-source import or release gate: source-to-ledger validation was not included in this particular command (`--qeax`/`--ledger` omitted); independent SysML v2 parser conformance, complete BOM workbook import, and GitHub Actions verification remain open. Connected GitHub combined status returned no statuses for commit `831e538ad...`; that is not proof of CI failure or success.

Next: execute the private QEAX/ledger fidelity command on the Mac with both explicit paths and a fresh local report destination, or continue parser-backed synthetic native SysML v2 fixture integration. Keep native emitter off until independent gates are satisfied.
