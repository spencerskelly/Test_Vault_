# Charger Connections v2 — Parser fixture

The independent SysML parser accepted [`connection_candidate.sysml`](connection_candidate.sysml) in [GitHub Actions run 38931726868](https://github.com/spencerskelly/Test_Vault_/actions/runs/38931726868). The workflow completed with success, including parser provisioning, validation and evidence upload. Evidence artifact: `v2-can-connection-candidate-evidence`, ID `12058722824`.

This result establishes **candidate acceptance only**. Unresolved endpoints, incompatible port types, incorrect ownership, and negative rejection controls remain unverified. Do not present a successful CLI exit as complete connection semantics certification.

The fixture is isolated under `25_Testing/Fixtures/Charger Connections v2/`, separate from the previously verified Golden Charger fixture and all v1 files. Runner warnings include deprecated `actions/setup-java@v4` and `actions/upload-artifact@v4`; upgrading these is a separate CI maintenance task.

Next validation: add deliberate negative connection cases, run under the same pinned parser, and inspect actual error classifications. Keep known-good sources unchanged.

## Connection negative controls — awaiting execution

The manual [CAN connection workflow](https://github.com/spencerskelly/Test_Vault_/actions/workflows/v2-sysml-connection-candidate.yml) now runs [check_connection_semantics.py](check_connection_semantics.py). It requires acceptance of the unchanged candidate and rejection of unknown controller port, unknown module port, unknown part endpoint, and malformed connection syntax. A validator returning success on a negative model fails CI. These controls have **not yet run** in GitHub Actions. Port type incompatibility and deeper ownership semantics still need separate, specification-grounded fixtures; they are not claimed tested here.

## Negative endpoint verification — 2026-10-16

[Run 38936451965](https://github.com/spencerskelly/Test_Vault_/actions/runs/38936451965) succeeded with the pinned independent parser. The unchanged connection baseline was accepted (exit 0); nonexistent controller port, nonexistent module port, unknown endpoint owner, and malformed connection syntax were each rejected (exit 1). The runner logged `PASS: baseline accepted and invalid endpoint/syntax controls rejected`. Evidence artifact: `v2-can-connection-candidate-evidence`, ID `12061786024`.

**Scope limit:** endpoint name-resolution and syntax rejection only; do not infer port-type compatibility or nested ownership rules from these results. Existing v1 models and Golden Charger v2 baseline were not changed.
