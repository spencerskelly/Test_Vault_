# Pass 6 — Phase 8 schema compatibility and native parser fixture

Date: 2026-10-17. This is an **incremental implementation**, not a Phase 6 release signoff.

## Confirmed structural mismatch

Inspected actual GitHub `main` files: `14_Workbench/registry/runtime/normalize_qeax_phase8.py` emits CSV columns `source_pk, source_guid, raw_from, raw_to, family, rule, role, status, normalized_from, normalized_to, source_kind, target_kind, diagnostics`. The deferred native evidence gate requires original `source_direction`, `source_role`, `target_role`, source type/stereotype and a reviewed source semantic assertion, none of which are present in that ledger. Its single normalized `role` is **not** equivalent to both original EA endpoint roles; source/target normalized kinds must not be substituted for actual source type/stereotype. Review decision, parser verification and Workbench obligations are also absent.

Added `15_Testing/phase8_deferred_evidence_compat.py` (`a23260b`): validates required CSV keys, explicitly identifies missing source attestation and requires independent manual evidence. It never claims native certification or infers missing fields. Added five synthetic compatibility tests (`6098a15`) for absent columns, missing snapshot, no direction synthesis, explicit review/parser gates and zero automatic approval.

## Candidate native fixture

Added `Fixtures/synthetic_part_definition_usage.sysml` (`5f90ddb`): a **synthetic** `part def` with a nested typed `part` usage. It is a parser **candidate**, not parser-validated syntax. Do not mark `parser_result=passed` until an independent conforming SysML v2 parser is executed with recorded version, exact fixture digest and parse diagnostics. No parser was run in this increment. No other constructs (use-case actor/subject, occurrence, redefinition/specialization) are claimed parser-covered yet.

## Acceptance and data boundaries

- No real source records, GUIDs, local disposition ledger or BOM content committed.
- No full checkout execution of the newly committed synthetic tests yet.
- No change to native eligibility or emission registry. `nativeCertified=0`.
- Next gate: run exact checkout synthetic tests and real parser, then extend the Phase 8 source ledger *at the point of ingestion* with untouched original direction/roles/type/stereotype plus full provenance, rather than filling missing evidence downstream. Record aggregate-only local validation.
