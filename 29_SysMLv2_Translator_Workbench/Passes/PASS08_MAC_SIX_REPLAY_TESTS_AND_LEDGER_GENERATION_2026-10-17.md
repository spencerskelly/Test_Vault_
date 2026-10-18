# Pass 8 — Mac replay tests passed and reduced QEAX located

2026-10-17: user ran all six synthetic `test_replay_phase8_local_normalization.py` tests on macOS; 6 passed, zero failures or errors. `git pull --ff-only origin main` reported already up to date.

User located reduced model at `/Users/spencerskelly/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax`. No `local_only_phase8_ledger.csv` was found under the user's Documents tree. Older September QEAX should not be substituted.

The documented registry is `14_Workbench/registry/family_disposition_registry.v0.2.json`; check it out with git and generate private ledger into `$HOME/Documents/MDSE_Local_Phase8` (outside Test_Vault_). Run `normalize_qeax_phase8.py --qeax ... --registry ... --out ...` then `replay_phase8_local_normalization.py --qeax ... --ledger ... --registry ...` and require 14688 source and ledger rows, `valid=true`, no discrepancy categories, `native_certified=0`. Report to chat only aggregate results. Source-model and ledger content must not enter the public repository. Replay shares implementation with the normalizer; it proves consistency, not independent semantic correctness. Native emission remains disabled.
