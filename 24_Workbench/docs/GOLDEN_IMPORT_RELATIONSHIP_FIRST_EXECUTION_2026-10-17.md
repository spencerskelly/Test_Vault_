# Golden Import — first approved-relationship reconciliation pass (2026-10-17)

Status: executable read-only audit; **not** native semantic acceptance.

Fixture: reduced QEAX SHA256 `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822`. Ran with a local copy of the committed audit implementation, 14,688 connector rows, all 26 approved exact families accounted for, zero unmapped.

| Exclusive disposition | Rows |
|---|---:|
| candidate_only | 10,419 |
| deferred_review | 3,856 |
| evidence_only | 413 |
| **Total** | **14,688** |

Native accepted: **0**. `candidate_only` means family recognized and preliminary endpoint checks passed, NOT direction/ownership, valid SysML v2 or approved native operation.

Overlapping diagnostic counts: `SOURCE_DIRECTION_UNATTESTED=431`; `SEMANTIC_EVIDENCE_REQUIRED=3696`; `ACTION_ENDPOINT_REVIEW=128`; `STATE_ENDPOINT_REVIEW=12`; `SPECIALIZATION_KIND_REVIEW=5`; `REQUIREMENT_ENDPOINT_REVIEW=14`; `VERIFY_ENDPOINT_REVIEW=1`.

The 413 evidence-only records are 220 NoteLinks + 193 Sequence reference interactions. The 3,856 deferred rows include 3,696 requiring semantic/source evidence under intentionally conservative family gates.

Implementation artifacts: `14_Workbench/registry/runtime/approved_relationship_audit.py` and `test_approved_relationship_audit.py`. Run: `python approved_relationship_audit.py --qeax /local/private/model.qeax --out /local/private/output`. Only the **aggregate summary** may be committed. Keep `PRIVATE_connector_reconciliation.csv`, model GUIDs, source identities and notes local. Synthetic tests are committed but have not been executed from the GitHub-hosted files or verified in CI.

Next exact gate: trusted EA orientation and role normalization, canonical element typing/owner resolution, specialized Realisation target selection, aggregation containment checks, and official SysML v2 parser. Do not promote this audit to native acceptance.
