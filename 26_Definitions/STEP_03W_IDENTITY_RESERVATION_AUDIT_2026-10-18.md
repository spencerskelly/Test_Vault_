# STEP-03W — Destination identity reservation audit

Date: 2026-10-18. Committed code and four synthetic tests.

## Purpose

Validate the 9,912 STEP-03V *candidate* UIDs against independently existing note UIDs and Local Model identity tokens in a **selected reference vault** before attempting to write them. Confirm one-to-one source EA GUID/Object ID parity with STEP-03U. Record collisions for subsequent nonblocking investigation. This stage does **not** resolve existing source-map ownership, produce approved filenames or MDSE paths, move notes, or rewrite links. No diagram processing.

Implementation: `21_Importer/v2_step03w_identity_reservation_audit.py`. Synthetic tests: `25_Testing/test_v2_step03w_identity_reservation_audit.py`.

### Execute on Mac

The fourth argument below is the *real destination/base vault to reserve against*, not the temporary STEP-03S generated vault. Set it deliberately:

```bash
git pull --ff-only origin main
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03w_identity_reservation_audit.py' -v
python3 21_Importer/v2_step03w_identity_reservation_audit.py \
 "$HOME/Documents/MDSE_Local_STEP03S/uid_allocation_candidate.private.jsonl" \
 "$HOME/Documents/MDSE_Local_STEP03S/identity_crosswalk.private.jsonl" \
 "/ABSOLUTE/PATH/TO/DESTINATION_BASE_VAULT" \
 "$HOME/Documents/MDSE_Local_STEP03S/uid_reservation_audit.private.jsonl"
```

Choose a target vault without personal or sensitive content unless local-only scanning is acceptable. No data leaves the Mac and the output is a local-only per-note ledger. The tool refuses to overwrite it. Exclude private ledgers and QEAX from public GitHub.

### Governing rules and gaps

Authority: `99_System/10_Docs/MDSE Modeling Ruleset 1.23.md` sections 15–16, and `21_Importer/Definition/SysML v2 Single File Importers UID and Diagnostics Contract 2026-10-17.md`.

This reads literal `uid:` YAML lines, and `part-/ep-/conn-/flow-` Local Model tokens in Markdown/Base content. It does **not** replace exhaustive YAML/parser namespace scanning, existing authoritative source-key-to-UID mapping, or persisted source map reconciliation. Reservations from these other sources must be integrated prior to final UID acceptance.

Ruleset 1.23 section 15.4 was later amended by W-382 to remove a blanket total-path-length limit. Preserve global case-insensitive filename uniqueness and actual filesystem component limits. Do not enforce an outdated 212-character total-path rule.

Next: source-map reconciliation with existing authorized identity ledger; real EA Name/Alias filename generation and duplicate handling; governed folder mapping; atomic link rewrite in a new vault and navigation/connector parity acceptance. Keep Package as folder-only and aggregate Boundary when writing the final model. No EA diagrams.
