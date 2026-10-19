# STEP-03V — EA UID allocation, governed placement still pending

Date: 2026-10-18.

## Authority and implementation

Read approved Ruleset 1.23 (sections 15 and 16) and `21_Importer/Definition/SysML v2 Single File Importers UID and Diagnostics Contract 2026-10-17.md`. V2 uses 30-character UID tokens (17 source-local creation timestamp digits + 13 lowercase author-code characters), source lineage `EA8647`, fallback `skellyspencer`, deterministic GUID ordering for collisions, and persistent source-key allocation. Filename is independently human-readable, globally unique case-insensitively; existing names reserved, duplicate `~2`, forced alteration `~a`; repository-relative paths hard limit 212 characters. EA Package containment must not become SysML ownership merely by folder placement.

Implemented `21_Importer/v2_step03v_uid_allocator.py` and three regression tests. The tool reads EA `CreatedDate` and `Author` from read-only QEAX, validates GUID against STEP-03U crosswalk, allocates unique timestamp-author candidate UIDs for standard notes, and marks Package and Boundary records held. It writes a new **private** allocation ledger, not the public repo. No note move or rename, no diagrams.

**Important remaining qualification:** This allocator cannot yet guarantee the globally governed identity namespace until it checks reserved existing note UIDs and local-model IDs, current authors-list overrides, prior source-key ledger, and format nuances of every real EA CreatedDate. Its output is a candidate first allocation, not authorization to write UID into notes on reimport. The ledger must be retained and reconciled before first use. Missing timestamps use the specified EA fallback. Source fields remain unchanged.

## Mac verification

```bash
git pull --ff-only origin main
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03v_uid_allocator.py' -v
python3 21_Importer/v2_step03v_uid_allocator.py \
 "/Users/spencerskelly/Documents/Vaults/Engineering_Data/EA_2026_10_15_endgame_mini.qeax" \
 "$HOME/Documents/MDSE_Local_STEP03S/identity_crosswalk.private.jsonl" \
 "$HOME/Documents/MDSE_Local_STEP03S/uid_allocation_candidate.private.jsonl"
```

Expected 11,303 input identities, 9,912 standard UID candidates, 1,388 Package records held for folder mapping, 3 Boundary records held for aggregation. No files changed in interim vault. On rerun, do not overwrite allocated ledger; use governed reconciliation.

## Next critical unit

Load already-governed UID reservations and source map; validate author normalization and timestamp precision against real QEAX; derive approved human-readable unique filenames and folder placement and perform atomic rewrite of all `[[EA-*]]` references on a fresh output vault. Audit source connector ID parity and zero broken paths. Keep unresolved semantic flags nonblocking. No EA diagrams.
