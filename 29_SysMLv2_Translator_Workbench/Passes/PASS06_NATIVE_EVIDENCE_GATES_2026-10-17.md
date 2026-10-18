# Pass 6 — Machine-readable deferred native evidence requirements

Date: 2026-10-17. Gated and **non-emitting**.

Implemented versioned evidence checklist `14_Workbench/registry/deferred_native_evidence_gates.v1.json`, assessment `15_Testing/deferred_native_evidence_gate.py`, and five synthetic tests `15_Testing/test_deferred_native_evidence_gate.py`. Categories: software component, system partner, physical context, platform, and unstereotyped class. Common fields include EA and connector provenance, direction, endpoint roles, reviewer disposition, Workbench structural/visual/navigation/validation obligations, round-trip provenance, and independently reviewed native parser fixture/result. Category-specific fields prevent inferred ownership, actor semantics, BOM membership, or subtype relationships.

Acceptance boundary: even complete evidence produces `evidence_complete_not_certified`, never native certification. The central SysML v2 eligibility registry, original source semantic verification, and a real native syntax parser remain independent approvals. Unknown source categories and untyped Classes cannot automatically select a native construct. Never commit populated evidence envelopes or source GUIDs: keep source-specific row data local.

**Verification note:** tests have been committed, but not executed from an exact GitHub checkout. These test cases are synthetic and do not establish a native parser result. No EA connector promoted; nativeCertified=0.

Next: execute exact committed tests in isolated checkout, validate cross-schema compatibility with Phase 8 source ledger, and produce parser-backed examples for native PartDefinition/Usage, use case actor/subject, occurrences and platform variation. Do not lift emission gate automatically.
