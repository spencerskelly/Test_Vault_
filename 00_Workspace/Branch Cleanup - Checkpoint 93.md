# Step 93 — Local Model 0.5 Port edge fixtures

Source: frozen Step22 local-model.yaml 0.5 and ea-connector-mapping.yaml 1.1. Proposed tests, not release signoff.

1. Class-owned Port: create boundary Interface with no part/parent; preserve source GUID through Local Model Source Map.
2. Part-owned Port: create Interface with part reference to existing Part occurrence.
3. Typed Port: optional Interface definition targets Object/interface; untyped Interface omits definition and usage.
4. Ordinary Connector: exactly one Connection(endpointA, endpointB) when both endpoints resolve in one context; otherwise retain unresolved provenance.
5. BindingConnector exposure: use Connection.exposes only when unique owner, boundary Interface, internal Interface and internal Connection are deterministic. Negative: ambiguous multi-connection binding must not be promoted.
6. BindingConnector equality: persist symmetric Interface.equals only for explicit same-owner source bindings not already classified as exposure; never persist transitive closure. Cross-owner binding remains review-only.
7. InformationFlow: one Flow nested under carrying Connection, definition links to Item Flow, endpointA/B roles transmit/receive/exchange/unspecified.
8. Negative validation: references missing endpoints, malformed block IDs, equals across owners, non-boundary exposes, duplicated flows, contextual definitionless endpoint with usage, and exposure duplicated as equality must fail.
9. Regression: Local Model 0.1 to 0.4 loads without silent rewrite; 0.5 writes only on explicit migration.
10. Provenance: source_model_id, source_key, owner_uid, local_id, local_kind, ea_guid, ea_source_kind, ea_owner_guid; preserve one stable identity on rerun.

Acceptance gate: run fixtures and verify source-to-target links and no invented topology. Actual QEAX/Obsidian GUI and release approval remain separate.

No branch merge, deletion, or release promotion authorized.
