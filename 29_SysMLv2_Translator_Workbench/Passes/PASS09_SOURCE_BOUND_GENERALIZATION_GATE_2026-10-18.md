# Phase 9 — Local source-bound generalization gate

Implemented `15_Testing/phase9_source_bound_generalization_gate.py`: on a local workstation, it first runs the complete Phase 8 normalization replay over the private QEAX, ledger and registry, requiring full and error-free source coverage. For a selected connector it then independently reads the original QEAX connector type, stereotype, direction and endpoints, verifies the subtype→supertype direction, and checks that the matching ledger row has qualified normalized role and endpoints.

The tool outputs only a boolean for **canonical review eligibility** plus diagnostic codes and `nativeCertified=false`. It does not expose model connector IDs in output, does not create a canonical graph edge, and never authorizes native emission. Five synthetic tests added (using a patched successful replay solely to isolate the connector gate); no independent Mac or CI execution has yet been observed.

**Strict limitations:** Passing the Phase 8 replay is consistency with Phase 8 normalization, not external independent semantic proof. The local Python result has no authenticated issuer or cryptographic binding to a JS canonical graph invocation; **do not treat it as a trusted token in the Workbench**, and do not set any implicit directionEvidence boolean from it. More work is needed to bind a source snapshot hash, ledger hash, rule version and selected connector evidence into a local signed/controlled staging transaction. The generalization family is only provisionally eligible for review, not native certification.

Run tests locally:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_phase9_source_bound_generalization_gate.py
```

Operator-only full check requires supplying an actual numeric connector ID and endpoint IDs from local private review; do not paste those identifiers into public GitHub. Other approved mappings and Workbench structural/visual contract remain unaffected. Native emitter disabled.