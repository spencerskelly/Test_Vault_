# Pass 7 — Structural SysML v2 real-kernel fixture baseline passed

GitHub Actions: https://github.com/spencerskelly/Test_Vault_/actions/runs/39100244556/job/117594868017

Observed completed success: checkout, Java 21, isolated Conda, official SysML Jupyter kernel, five diagnostic-classifier regression tests, four positive fixture checks, negative syntax rejection, cleanup.

| Fixture | Expected | Observed | SHA-256 |
|---|---|---|---|
| synthetic_part_definition_usage.sysml | ACCEPTED | ACCEPTED | 6c1c8ab627bdf814a6b85d0140e62a6de8f8c5cc691e2cfb0ca7884cb373f130 |
| synthetic_nested_part_usages.sysml | ACCEPTED | ACCEPTED | 0648e9cdbc40227edb9954a4576e4c9ba127d6b0c30c5ff504449ef9cc0444c0 |
| synthetic_port_as_part.sysml | ACCEPTED | ACCEPTED | b8c98f6956d977588ca513e409126b96d01332012514351e28c585016e018139 |
| synthetic_connection_usage.sysml | ACCEPTED | ACCEPTED | 4e8d44616c94166eaf9a76c399a4180766b57912aa6e5cd0590ceef4881f3b2a |
| synthetic_invalid_syntax.sysml | REJECTED | REJECTED | d0b0031d219f45a99cd8a3e014c55a4d14c3d9206e0d2cb83c40435c857bb0b6 |

All four positive runs: matched shell execute_reply=ok, no IOPub errors and no recognized diagnostic categories. Invalid run: three stream messages, error_marker=3, parser_recovery=3, runner status REJECTED.

Interpretation: This closes the **basic structural textual syntax fixture baseline** for exact fixture hashes and this official pilot kernel environment. It does not demonstrate that EA proxy/full port mappings, connection ownership, binding vs reference, redefinition, flow allocation, or IBD representation preserve intended semantics. In particular, a typed SysML port usage on a part is not the same assertion as the port being modeled as a part usage. Parser classification is still stream-pattern based.

Next priority: synthetic semantic fixtures and observable canonical graph checks for end-kind, port typing, ownership, endpoint direction and multiplicity; then state/action nested usages, redefinition, binding ports, requirements and verification. Expose Workbench structural/visual rendering contracts without erasing distinctions. Native emitter remains disabled; nativeCertified=false. No proprietary QEAX/BOM rows or ledgers committed.
