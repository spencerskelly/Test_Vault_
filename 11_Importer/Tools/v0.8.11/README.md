# EA to MDSE Native Importer v0.8.11

v0.8.11 builds on v0.8.10 and implements W-375 / IMP-006.

## Change

Every otherwise viable source `.qea/.qeax` is fingerprinted with the standard SHA-256 digest before preflight can complete successfully.

The hash is recorded in:
- preflight source metadata;
- `Run Manifest.md`;
- `Import State.json`.

## Memory behavior

The importer keeps its streaming-source design. It does **not** load the complete QEAX into memory just to hash it.

A small incremental SHA-256 implementation reads the source in 8 MiB chunks with `File.slice()`, updates the hash state, yields to the UI between chunks, and retains only bounded hashing state.

## Validation

The exact SHA-256 implementation embedded in v0.8.11 was extracted and tested against standard vectors:
- empty input → PASS;
- `abc` → PASS;
- `a` + `bc` split across separate updates → same digest, PASS.

Full embedded JavaScript syntax parse also passes.

Real-QEAX acceptance still needs to confirm the digest is produced and copied identically into preflight, transaction and manifest evidence.

## First hardening group status

Implemented in candidate code:
- IMP-001 persistent transaction state;
- IMP-003 separated run-status dimensions;
- IMP-004 WAL source hard stop;
- IMP-005 initialized destination requirement;
- IMP-006 streaming source SHA-256.

The next systemic correction is IMP-002: prevent semantically invalid/provisional relationships from becoming canonical YAML merely because their EA connector was preserved.
