# EA to MDSE Native Importer v0.8.7

v0.8.7 is the first release-hardening revision built from v0.8.6. It implements W-371 / IMP-001 so a partial filesystem write cannot be mistaken for a completed import.

## Changes from v0.8.6

- Adds `99_System/11_Import/Import State.json`.
- Rejects any destination that already contains an import-state file; semantic imports still require a fresh generated base.
- Writes `IMPORT_IN_PROGRESS` before the first generated model note or attachment.
- Writes all model notes and attachments, then all required evidence except the Run Manifest.
- Writes the Run Manifest after the other evidence.
- Writes `IMPORT_COMPLETE` last. This is the authoritative completion event.
- On a caught write failure after the transaction begins, attempts to write `IMPORT_FAILED` with the error message.
- If the filesystem is no longer writable and even the failure marker cannot be updated, the existing `IMPORT_IN_PROGRESS` marker remains. That state is intentionally invalid and cannot be mistaken for PASS.
- The Run Manifest now states that its PASS is authoritative only when `Import State.json` is `IMPORT_COMPLETE`.

## Transaction-state shape

The JSON records:
- schema version;
- transaction status;
- importer name/version;
- MDSE release;
- source name and byte size;
- scope;
- start/update/completion timestamps;
- planned note, attachment-file and evidence-file counts;
- failure message when available;
- governing authority (`Importer Operating Contract / W-371`).

## Safety properties

1. No model file is written before `IMPORT_IN_PROGRESS` exists.
2. `IMPORT_COMPLETE` is never written before the Run Manifest.
3. A caught write failure cannot be converted to PASS.
4. A destination with prior transaction state cannot be reused as a clean base.
5. Rollback is not required: interrupted candidate bases are disposable and must be discarded.

## Validation performed

- Full embedded JavaScript syntax parse: PASS.
- Source-level transaction ordering checks are in `Importer/Testing/v0.8.7/transaction_state_static_test.js`.
- Real browser fault-injection remains required before IMP-001 is closed: interrupt note writing and evidence writing, verify the state remains `IMPORT_FAILED` or `IMPORT_IN_PROGRESS`, and verify the same destination is refused on another run.

## Remaining high-priority work

IMP-003 (run-status separation), IMP-004 (WAL policy), IMP-005 (initialized vault requirement) and IMP-006 (source fingerprint) remain intentionally separate so this revision changes one failure boundary at a time.
