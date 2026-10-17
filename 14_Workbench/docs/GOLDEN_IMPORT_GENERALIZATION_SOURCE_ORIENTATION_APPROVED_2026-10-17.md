# Golden Import — EA Generalization source orientation

Decision date: 2026-10-17. Status: APPROVED rule, fixture verification and parser conformance pending.

- For EA Generalization, interpret `t_connector.Start_Object_ID` as the **specific/child** definition and `t_connector.End_Object_ID` as the **general/parent** definition, subject to source-model verification.
- Native SysML v2 specialization proceeds **specific → general**, for compatible definitions only.
- Do not automatically reverse endpoints to make a relationship appear valid. Any exceptions, conflicting evidence, unresolved endpoints, incompatible kinds or cycles receive explicit review diagnostics and retain original source orientation/provenance.
- Do not infer variation or redefinition from generalization.
- Verify on the reduced QEAX and retain model-specific ledger locally; only aggregate results may be committed to the methods repository.
