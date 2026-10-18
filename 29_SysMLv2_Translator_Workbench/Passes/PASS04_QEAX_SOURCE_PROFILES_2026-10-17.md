# Pass 04 — Reduced and full QEAX source profiles (initial evidence)

Status: aggregate source inspection completed, local-only profile generator committed; importer integration pending.

## Aggregate source baselines

| Table | September full accepted v1 | October reduced local test |
|---|---:|---:|
| t_object | 35,969 | 11,447 |
| t_connector | 21,822 | 14,688 |
| t_package | 1,387 | 1,389 |
| t_diagram | 2,924 | 2,208 |
| t_diagramobjects | 42,966 | 25,402 |
| t_diagramlinks | 37,955 | 23,531 |
| t_objectproperties | 249,892 | 43,634 |
| t_xref | 42,052 | 17,825 |
| t_document | 397 | 120 |
| t_operation | 23 | 21 |
| t_attribute | 5 | 3 |
| t_operationparams | 0 | 0 |

Local October QEAX: read-only SQLite PRAGMA quick_check = ok; SHA256 69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822. No proprietary row data committed.

## Shape evidence

Observed October element kinds include Requirement 2,638; Class 2,381; Package 1,388; Activity 1,151; UseCase 857. Connector kinds include Generalization 3,735; Dependency 3,058; Abstraction 2,619; Aggregation 2,267; Realisation 884. These are EA source classifications, not accepted SysML v2 relationships.

## Repository updates

- The September full-model v1 profile remains unchanged: 11_Importer/Definition/Source Profiles/EA8647-2026-09-06-v1.json. DO NOT overwrite or globally bypass its counts.
- Fixed old directory defaults in 11_Importer/Tools/v0.8.19/sync_source_profile.py (commit 6460ba0). This remains a historical v1 sync tool.
- Added 15_Testing/profile_qeax_local.py (commits 831477d, df4cfe3), a source-specific read-only evidence generator using SQLite quick_check, table and type counts and streaming SHA-256; output must be outside the Test_Vault_ checkout.
- Generator execution from a complete GitHub checkout has NOT been verified; aggregates above were obtained with separate read-only local SQLite queries.

## Next bounded action

1. Validate all discovered EA tables for the reduced source and compare against September's tableDispositions rules (including ignored_must_be_empty); never silently ignore nonempty unexpected rows.
2. Record a separate reduced-source profile as LOCAL evidence with explicit release/profile selector, never as a replacement of the full-model accepted v1 contract.
3. Add synthetic tests for profile mismatch, unexpected nonempty tables and count drifts.
4. Preserve all element and connector dispositions in a local-only ledger; publish only aggregates.

Release is not cleared: full base build, CI, native v2 parser, importer and Workbench runtime remain outstanding. Require user y for next pass.

## Pass 04 continuation — full table-disposition verification (2026-10-17)

Executed read-only SQLite on the user's reduced October QEAX (`PRAGMA quick_check = ok`) and compared the complete set of **100** table names and their row counts against the **100** named dispositions in September's accepted full-model EA source profile. The source contains **45 nonempty** and **55 empty** SQLite tables.

**Result:** 100/100 source tables classified, zero unexpected tables, zero source policy table omissions, **zero nonempty tables where the old profile requires ignored_must_be_empty**. This passes table policy compatibility only, not source snapshot count matching: reduced data intentionally differs from the full-model profile.

Committed reusable read-only policy runner `15_Testing/reconcile_qeax_dispositions.py` (commit `7e9fe4c7e073135491d78bfd2764991afcf08255`). It compares every SQLite table to a passed JSON profile, reports unclassified/missing tables and forbidden nonempty counts, does not copy source rows, and returns failure on findings. This runner was **not run from a complete repo checkout**; the local SQLite comparison described above was executed independently against the same reference disposition lists.

Run in a full checkout as:
```bash
python3 15_Testing/reconcile_qeax_dispositions.py /private/EA_2026_10_15_endgame_mini.qeax "11_Importer/Definition/Source Profiles/EA8647-2026-09-06-v1.json" --out /private/qeax-disposition-report.json
```

### Next
Add isolated synthetic regression tests: a valid fixture, one unexpected table, one forbidden nonempty table, and a missing required table. Then produce a **separate reduced-source v2 candidate profile** with current table/type counts (locally) and explicit selector. Do not mutate v1 September profile or any previous v1 baked importer profile. No proprietary rows or source GUIDs were committed. Pass 04 ongoing until these tests and selection behavior are verified.

## Pass 04 continuation — synthetic table-disposition regression tests

Added `15_Testing/test_reconcile_qeax_dispositions.py` (commit `2f616857b3766d8ca81489be46082943aa2d3e90`), using a disposable four-table SQLite model and no enterprise data. Five tests cover valid dispositions, unknown table, nonempty forbidden table, absent required table and the deliberate separation of snapshot count matching from table-disposition matching. All **five passed locally** with Python unittest against the fetched checker source:

```text
Ran 5 tests in 0.048s
OK
```

Re-run from full Test_Vault_ checkout with:
```sh
python3 -m unittest discover -s 15_Testing -p test_reconcile_qeax_dispositions.py -v
```

**Not yet verified:** importing the reduced model with its own source profile, all element-type and connector-type distributions, and imported connector disposition completeness. The old September full profile is preserved unchanged. The table-disposition gate is a separate required gate; it does not supersede strict current-source counts.

**Next gated step:** generate the current source's full type/count evidence locally and introduce a separate reduced profile selection contract without embedding proprietary row-level data or silently replacing the old v1 profile.
