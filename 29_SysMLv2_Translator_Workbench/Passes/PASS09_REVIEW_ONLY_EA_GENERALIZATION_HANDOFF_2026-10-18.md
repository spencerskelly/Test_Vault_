# Phase 9 — EA generalization evidence to canonical graph handoff

Added `phase9-generalization-handoff.mjs`, which constructs a **review-only candidate** canonical specialization edge after checking family, EA source orientation, normalized endpoint consistency, role, and graph invariants. It never mutates the graph, certifies native emission, or exports local QEAX data. Seven synthetic regression tests were added.

**Critical trust limitation:** `verified` and `semantic_direction_verified` in the present interface are merely caller-supplied claims. No independently authenticated issuer or source-hash-to-specific-row binding yet exists. Therefore a `candidate` response is NOT evidence of verified direction, approval, or native semantics. Do not connect this function to automatic translator or Workbench mutation. The actual Phase 8 manifest does not currently attest semantic direction; it should fail closed until a trusted local verifier issues an independently checked record-specific result.

Future production gate must locally verify immutable QEAX and ledger hashes; bind connector identity, raw Start/End, direction, family, role and registry revision to an independently recomputed semantic verification result; prevent arbitrary caller booleans; enforce source snapshot consistency; preserve source provenance and never commit source rows.

Workbench contract: structural and visual specialization links remain distinct from lexical nesting; node navigation, original EA provenance, validation diagnostics and round trip must be supported before enabled use. PartUsage, port-as-part, and Binding Port remain distinct.

Mac check: `node --test 15_Testing/test_phase9_generalization_handoff.mjs`. Tests committed, execution not yet independently observed. Native emission remains disabled.