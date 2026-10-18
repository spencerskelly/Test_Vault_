# Pass 8 — Canonical model structural guard integration

This increment updates the existing production graph validator `14_Workbench/registry/runtime/canonical-model.mjs`, rather than relying solely on the earlier standalone Python synthetic guard.

Added opt-in validation for: port usage owner must be a PartDefinition or PartUsage; node multiplicity as [lower,upper] with integer lower, integer upper or `*`; and nonblank `sourceRef` when supplied. Existing typed definition/usage and ownership-cycle checks remain in the canonical validator.

Added seven Node tests in `15_Testing/test_canonical_structural_invariants.mjs`, and a GitHub Actions workflow at `.github/workflows/sysml2-canonical-structure.yml`. CI results have not yet been checked; this work does NOT authorize native emission.

Scope limitations: This adds checks to canonical graph nodes only. Connector direction, ownership scope, source attestation, provenance completeness, visual rendering and native syntax emission remain separate open gates. Existing data without `multiplicity` or `sourceRef` is not blocked. Neither the Python parallel checks nor this patch certifies SysML semantic equivalence.

Verification: `node --test 15_Testing/test_canonical_structural_invariants.mjs`. No private model rows committed.