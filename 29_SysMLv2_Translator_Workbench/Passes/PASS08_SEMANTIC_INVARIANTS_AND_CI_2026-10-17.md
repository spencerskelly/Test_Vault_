# Pass 8 — Structural semantic invariant expansion

Scope: synthetic canonical structure guardrails only; does not read QEAX, assert native SysML semantic equivalence, or enable emission.

After the real-kernel structural syntax baseline succeeded, this increment added checks for recursive ownership cycles, explicit lower/upper multiplicity, recognized direction labels, nonblank supplied provenance, and connection owner kind. Six new synthetic test cases bring the structural contract suite to 12 tests.

Files: `15_Testing/sysml2_structural_semantic_contract.py`, `15_Testing/test_sysml2_structural_semantic_contract.py`, and `.github/workflows/sysml2-structural-semantics.yml`.

IMPORTANT limitations: `source_ref` is validated only when present, and is not a production provenance requirement. Direction label validation is vocabulary-only and does not certify EA direction normalization. Connection endpoint owner scope is not yet enforced. Multiplicity is a standalone guard, not a validated translation from EA part relationships. Existing synthetic Workbench labels are preliminary and require full structural/visual/navigation/round-trip rules.

The new suite has been committed to main; CI success has not yet been observed. No private source rows, GUIDs, or ledgers committed. Native emission remains disabled, nativeCertified=0.

Run locally:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_sysml2_structural_semantic_contract.py
```

Next priority: connect these guards to the typed canonical graph and trusted EA evidence schema rather than introducing a parallel independent representation, then enforce connection scope, direction provenance, and concrete Workbench behaviors. Parser success must remain a separate gate.