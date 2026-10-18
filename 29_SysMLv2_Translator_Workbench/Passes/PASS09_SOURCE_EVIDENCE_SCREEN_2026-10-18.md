# Phase 9: Local generalization evidence screen

Added a read-only local QEAX-to-ledger source identity and specialization direction check. It reports aggregate diagnostics only and never grants native certification. This is not trusted attestation and does not authorize emission. Full synthetic tamper tests and actual Mac execution remain pending.

Run `python3 15_Testing/phase9_local_specialization_evidence_screen.py --qeax "$HOME/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" --ledger "$HOME/Documents/MDSE_Local_Phase8/run_20261017/local_only_phase8_ledger.csv"` from Test_Vault_. Keep inputs and output private.
