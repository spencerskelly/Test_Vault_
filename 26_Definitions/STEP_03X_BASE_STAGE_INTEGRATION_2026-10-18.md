# STEP-03X — Automated V2 Test Base and UID Reservation Staging

2026-10-18. The existing V2 test-base builder is integrated with the STEP-03W identity audit via `20_Base Vault/stage_v2_import_base.py`. The script generates a fresh isolated destination and reports candidate UID reservations in one operation; it requires no manual Base Vault setup. Synthetic integration tests verify build, audit, fail-closed existing destination and cleanup on failure.

## Run on Mac from Test_Vault_

```bash
git pull --ff-only origin main
python3 -m unittest discover -s 25_Testing -p 'test_v2_step03x_base_integration.py' -v
python3 "20_Base Vault/stage_v2_import_base.py" \
 "$HOME/Documents/MDSE_Local_STEP03S/uid_allocation_candidate.private.jsonl" \
 "$HOME/Documents/MDSE_Local_STEP03S/identity_crosswalk.private.jsonl" \
 "$HOME/Documents/MDSE_Local_STEP03X_Base"
```

Destination must not exist. The stage writes its private UID candidate ledger under `99_System/uid_audit.private.jsonl` and readiness JSON under `99_System/step03x_readiness.json`. Keep these files local. The builder imports only V2 repository runtime/reference files and excludes V1 archives; no user QEAX or model records are committed.

## Critical scope boundary

This is an **uninitialized test base**, not a release-ready production Base Vault. Both `plugin_ready` and `native_import_ready` are false. The committed release-readiness checkpoint `20_Base Vault/Testing/V2_IMPORT_KIT_RELEASE_READINESS_2026-10-17.md` records unresolved Workbench, Bootstrap, plugin lock, native serializer, parser and synchronized release requirements. This check cannot authorize production deployment, plugin resets, native SysML v2 certification, or final UID use.

The automated candidate audit detects present reserved UID fields and common Local Model tokens in the generated base, but an empty fresh base does not prove global uniqueness against an eventual different destination or preexisting source map. Future stages must reconcile source maps and reserve other global token holders before finalizing identities.

Next: synchronize V2 Base Vault runtime and plugin release, complete source-map/identity governance, and run the reduced-QEAX import into a fresh disposable copy with navigational and connector reconciliation. EA diagrams stay deferred. Do not alter the functional STEP-03S vault.
