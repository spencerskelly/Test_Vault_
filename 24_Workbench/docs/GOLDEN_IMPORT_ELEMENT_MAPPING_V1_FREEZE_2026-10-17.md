# Golden Import — Element Mapping v1 freeze

Decision date: 2026-10-17. Status: **APPROVED semantic mapping baseline**, not import/runtime release certification.

The model owner approved freezing the reconciled 60-family element translations from `GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md`, incorporating subsequent approved decisions in `GOLDEN_IMPORT_STEP2_*_APPROVED_2026-10-17.md`. Proceed to **relationships**, beginning with ownership and containment.

Key invariants: one MDSE note per definition; no extra note for local usages; native SysML v2 constructs only where approved, with `type`, `subtype`, original EA type/stereotype and provenance in YAML; EA packages become organizational folders, not semantic ownership. Untyped part/action/port usages allowed with explicit unresolved-type flags. Source relationships retain an independent evidence-based translation gate.

Carry-forward exceptions: validate Object classifier-to-specialization targets (341 candidates); distinguish composite vs external Physical Context (43); resolve or explicitly flag local usage ownership (28). These are source-record validation tasks, not a reopening of family-level decisions.

No QEAX model rows, identities or generated model notes are committed here. Element family completeness is not native parser acceptance or golden import completion. Changes to this baseline require concrete source evidence or native conformance failure, with a versioned amendment.

Next discussion: EA aggregation/composition and nested element ownership — distinguish physically owned typed usages from pure model organizational nesting; avoid inference from EA package folders.
