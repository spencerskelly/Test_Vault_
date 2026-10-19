# STEP-04B — Conservative QEAX-to-ledger adapter

Date: 2026-10-18. Status: **read-only local source-accounting pass; canonical mapping and generated-target audit NOT completed**.

## Implementation
`24_Workbench/registry/runtime/v2_step04_source_adapter.py` creates a private JSONL ledger, one record per EA object or connector, then invokes `v2_step04_ledger_gate.py`. It reads no EA diagram tables. Source rows are not uploaded.

Local command:

```sh
python3 24_Workbench/registry/runtime/v2_step04_source_adapter.py \
  --qeax /private/EA_2026_10_15_endgame_mini.qeax \
  --out /private/step04b
```

The CLI's `source_disposition.jsonl` contains source identifiers and is **private**. Only the aggregate `aggregate_summary.json` is suitable for sanitized review. Do not commit either unreviewed output.

## Actual local-run aggregate
Fixture SHA-256: `69222c060a81b3e35a3e25f365f2a1f4c3dd6eaa19d77fbbd5ba9abdf365a822`.

- Objects: **11,447 / 11,447**
- Connectors: **14,688 / 14,688**
- Total: **26,135**, all accounted for; duplicate/count/schema gate passed
- Encountered source families: **86** (60 element + 26 connector families)
- Preliminary dispositions: 24,515 `deferred_review`, 232 `evidence_only`, 1,388 `excluded_by_policy`; zero falsely accepted native targets
- Gate failures: **0**

These counts are **provisional source accounting**, not evidence of 24,515 semantic defects. In particular `deferred_review` currently means *semantic output not yet connected* rather than manual review of each row. The existing Phase 2 mapping registry and Phase 8 connector engine must now replace this conservative category **in groups**. Do not put 24,515 individual flags in Obsidian.

## Next: STEP-04C
Wire the approved exact 60+26 family resolver and normalized connector evidence into the adapter. Preserve rule IDs, typed source endpoints and original row provenance; produce real native/evidence/alias projection destinations only where a writer output exists. Compare all emitted targets against the canonical graph and staged notes. Handle unsupported/outlier links as `flagLink` and notes as `flagNote`, keeping individual connector traceability. Validate an identical second run and document differences. EA diagrams remain excluded until golden import approval.

**Gate not yet met:** full source→native/MDSE-note→parser→Workbench output verification. No golden import certification is implied.
