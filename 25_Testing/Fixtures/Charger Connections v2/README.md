# Charger Connections v2 — Parser fixture

The independent SysML parser accepted [`connection_candidate.sysml`](connection_candidate.sysml) in [GitHub Actions run 38931726868](https://github.com/spencerskelly/Test_Vault_/actions/runs/38931726868). The workflow completed with success, including parser provisioning, validation and evidence upload. Evidence artifact: `v2-can-connection-candidate-evidence`, ID `12058722824`.

This result establishes **candidate acceptance only**. Unresolved endpoints, incompatible port types, incorrect ownership, and negative rejection controls remain unverified. Do not present a successful CLI exit as complete connection semantics certification.

The fixture is isolated under `25_Testing/Fixtures/Charger Connections v2/`, separate from the previously verified Golden Charger fixture and all v1 files. Runner warnings include deprecated `actions/setup-java@v4` and `actions/upload-artifact@v4`; upgrading these is a separate CI maintenance task.

Next validation: add deliberate negative connection cases, run under the same pinned parser, and inspect actual error classifications. Keep known-good sources unchanged.
