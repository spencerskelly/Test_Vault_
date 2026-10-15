# EA to MDSE Native Importer v0.8.10

v0.8.10 builds on v0.8.9 and implements W-374 / IMP-005.

## Change

The destination base must have an initialized vault identity before the importer accepts it.

`requireBaseVault()` now reads `vault_uid` from `.vault.yaml` and rejects:
- a missing/blank vault UID;
- the literal packaged-base value `UNINITIALIZED`.

The governed initializer remains responsible for assigning the vault identity/name while preserving `mdse_release`.

## Why

A large semantic model should never be written into an identity-less base. This makes the documented initialization order mechanically enforced.

## Validation

- Embedded JavaScript syntax parse: PASS.
- Static assertion confirms `vaultUidFromText()` exists.
- Static assertion confirms literal `UNINITIALIZED` is rejected.

## Next hardening item

IMP-006: compute and persist a cryptographic fingerprint of the exact selected QEAX snapshot.
