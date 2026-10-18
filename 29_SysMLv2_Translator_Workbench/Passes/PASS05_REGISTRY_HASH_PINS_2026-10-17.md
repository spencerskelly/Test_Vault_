# Pass 5 — Registry SHA256 pinning, 2026-10-17

**Result:** exact candidate registry hashes pinned; read-only verification tool and synthetic tests committed. Native emission still disabled.

## Deliverables

- `14_Workbench/registry/sysml_v2_registry_pins.v0.1.json` (commit `01df97d`), SHA256 for all three current registry files: family dispositions v0.2, candidate v2 semantics v0.2, and decision register v0.1.
- `15_Testing/verify_sysml_v2_registry_pins.py` (commit `5ae1404`): rejects missing, drifted or empty pin sets and reports file hashes.
- `15_Testing/test_sysml_v2_registry_pins.py` (commit `779cf3f`): four synthetic regression cases for valid files, modified files, missing files and empty pin list.

## Local commands

```sh
python3 15_Testing/verify_sysml_v2_registry_pins.py .
python3 -m unittest discover -s 15_Testing -p test_sysml_v2_registry_pins.py -v
python3 -m unittest discover -s 15_Testing -p test_sysml_v2_semantic_decisions.py -v
```

These exact commands **have not been executed against a complete repository checkout**. SHA256 digests were computed from retrieved UTF-8 GitHub contents and compared to a known SHA256 reference vector; hash verification by the committed Python tool remains pending. Modifying any registry requires a deliberate new pin file version or approved update, with tests and review. Do not silently repin to conceal drift.

This stage is a consistency/integrity gate, not native SysML v2 syntax validation. Remaining open: checkout-level tests, independent parser, end-to-end first-run kit, release base and workflow repairs.
