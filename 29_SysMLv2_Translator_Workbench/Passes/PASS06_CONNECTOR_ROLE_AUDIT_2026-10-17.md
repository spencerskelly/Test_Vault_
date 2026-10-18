# Pass 6 — Connector endpoint role/ownership source audit

Date: 2026-10-17. Read-only reduced QEAX source analysis; evidence-only, no native SysML v2 certification.

## Aggregate local results

14,688 connectors audited. 433 have direction values other than explicit Source -> Destination (including missing, unspecified and reverse values); 44 have identical source/target element IDs. For 2,267 Aggregations, 1,670 mark destination composite and 597 mark a shared end; 1,948 lack explicit role names and 2,215 lack explicit cardinality. Categories overlap and must not be summed. All are source-evidence characteristics, not dispositions accepting SysML v2 ownership. Native certified = 0.

## Deliverables

- `15_Testing/audit_ea_connector_roles.py` commit `0d7b5c1`: aggregate-only direction, composite/shared end, explicit role/cardinality and self-reference audit.
- `15_Testing/test_audit_ea_connector_roles.py` commit `0b6bbfa`: four synthetic tests.
- A locally reproduced equivalent of these four tests was run and passed. The exact GitHub-committed test files have **not** been executed in a complete checkout.

## Semantic boundary and follow-up

- A destination composite flag is not by itself permission to emit owned part usage.
- Shared aggregations, roleless links, absent multiplicity and self-relations remain subject to typed eligibility, source provenance and review.
- `Direction=Unspecified` is not silently converted to Source -> Destination; EA family-specific orientation evidence must be attested independently.
- Follow-up: typed EA source/target endpoint eligibility and explicit owner context; compare Phase 8 provisional normalization to full semantic registry; parser-conformance gate; run exact committed tests and real-source end-to-end validation.
- No proprietary rows, IDs, GUIDs or full ledger were committed.

**Pass 6 remains open.** Continue only after user confirmation.
