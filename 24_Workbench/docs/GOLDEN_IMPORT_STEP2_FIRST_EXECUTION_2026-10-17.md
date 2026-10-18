# Golden Import — Step 2 first executable audit (2026-10-17)

Status: **read-only family classification implemented and run; canonical model generation pending**.

Source: local-only QEAX SHA-256 `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822`. No source rows, element identities, or per-element ledger uploaded.

## Actual local execution
- 11,447 element rows processed exactly once; 60 of 60 exact EA type/stereotype families recognized; zero unknown.
- Family dispositions: `native_definition=8597`, `conditional_context=43`, `local_usage=135`, `local_behavior=15`, `mdse_note=1116`, `attachment=144`, `organization=1388`, `reference_only=3`, `reference_view=3`, `excluded_by_policy=3`. Sum = 11,447.
- Overlapping diagnostics: `CONTEXT_COMPOSITION_REVIEW=43`, `SPECIALIZATION_REQUIRES_TARGET_VALIDATION=341`, `UNRESOLVED_OWNER=28`, `UNRESOLVED_ACTION_TYPE=51`, `UNRESOLVED_PART_TYPE=1`, `UNRESOLVED_PORT_TYPE=16`, `PORT_OWNER_REVIEW=6`, `CONNECTION_ENDPOINT_REVIEW=3`. External designation flags: `EXTERNAL_PART=149`, `EXTERNAL_PARTICIPANT=36`.
- Eight synthetic unit tests passed in local Python 3. **No native parser or GitHub CI result is claimed.**

## Gaps to next runnable increment
1. Context composition and Object specialization must be independently validated from source relationships and resolved target kinds.
2. The 28 unresolved local owners and untyped usage flags require retained diagnostics; missing classifier is permitted by approved policy, missing owner is not automatically repaired.
3. This audit does not yet allocate stable MDSE IDs, generate native SysML v2, create notes or folders, or check repeat import. Per-row ledger stays local.
4. Add run manifest and deterministic stable-ID allocation with evidence from original EA GUID, separating PartDefinition from owned PartUsage.

Re-run local-only audit with `python element_audit.py --qeax /private/fixture.qeax --out /private/output`. Keep all output in a non-repository folder.
