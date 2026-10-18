# Phase 9 — Source direction trust handoff

The complete Phase 8 QEAX ledger replay is verified for all 14,688 connectors, but the canonical graph currently accepts direction and sourceRef as caller-provided strings. Those strings are not source attestations.

**Fail-closed requirement:** Before writing any actual source generalization into the canonical graph, locally verify the exact QEAX, ledger and registry hashes; replay every connector; independently confirm source EA Generalization `Start_Object_ID` is the subtype and `End_Object_ID` is the supertype under an approved Sparx orientation rule; compare original direction to the ledger; and associate the exact source connector identity with the generated edge. Never publish model rows or identity mappings.

A synthetically valid canonical relationship is not a qualified native specialization. With no signed or otherwise trusted local issuer/verifier binding the evidence to a specific connector, leave real graph promotion gated and native emission disabled. This pass is a documented safety handoff rather than a claim that a trusted bridge exists.

Remaining tasks: add local read-only verifier with tamper tests for missing and duplicated connectors, reverse/unspecified directions, source snapshot swaps, false semantic approval flags, and graph provenance mismatches. Integrate through a read-only evidence-scoped API, not `directionEvidence:true` supplied by callers. Workbench must distinguish unqualified review links from approved specializations in structural and visual views and retain round-trip provenance.