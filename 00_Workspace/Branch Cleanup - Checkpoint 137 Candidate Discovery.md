# Branch Cleanup — Checkpoint 137 Candidate Discovery Readiness

Date: 2026-10-14

## Change
Updated `66_Testing/consolidation/step136_discover_qeax_vault_candidates.py` on validation branch, commit `0848e60139ad267f4a793cba85da364d9e3671ff`. The earlier expression `[base, *base.rglob("*")]` eagerly enumerated every nested file before applying `--max-depth`, which could be extremely slow or memory-heavy in large vaults. It now uses top-down `os.walk` with depth pruning, skips symlinked directories and Git / node_modules / trash, and catches file-size stat failures. It remains strictly read-only and never claims to pair model and vault.

## Local operator next action
Run from a checkout containing the updated file:

```bash
python3 66_Testing/consolidation/step136_discover_qeax_vault_candidates.py "$HOME/Documents/Vaults" --max-depth 6 > "$HOME/Documents/qeax-candidate-inventory.json"
```

If the QEAX resides elsewhere, provide that directory as another root. Share the inventory paths (not the entire sensitive source) or supply the discovered paired model and vault through approved evidence exchange. A candidate vault must have both `99_System/11_Import/Review - Equals Direction.csv` and `99_System/11_Import/Local Model Source Map.csv`. If no vault is found, run one controlled importer v0.8.19 execution into a new empty output directory, not the approved vault, and then run `step120_real_qeax_operator_gate.py`.

## Acceptance boundary
No real-model candidate inventory was supplied in this conversation, and no local model/vault pair was available for acceptance. Thus no QEAX source integrity, generated-vault acceptance or GUI signoff can be asserted. Green CI remains the prior tested baseline; this discovery-script change is not yet CI-tested. No merge, main change, branch deletion or release promotion.
