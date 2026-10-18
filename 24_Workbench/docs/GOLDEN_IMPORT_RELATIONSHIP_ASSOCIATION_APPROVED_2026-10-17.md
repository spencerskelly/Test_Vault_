# Golden Import — EA Association

Decision date: 2026-10-17. Status: APPROVED translation policy; source-level and native parser validation pending.

- Where an explicit EA Association between physical components genuinely establishes physical connectivity, translate to native SysML v2 `ConnectionUsage`, referencing typed endpoints in their applicable owning context.
- Do not assume that every Association or even every physical-component Association conveys actual connectivity; require adequate source role/connector evidence.
- Associations lacking evidence of physical connectivity remain references with explicit review disposition rather than invented native connections.
- Preserve original EA connector type, stereotype, direction, endpoints, roles and provenance; do not infer ownership, flow or interface semantics from Association alone.
- No additional MDSE note for the connection usage. Workbench must distinguish confirmed connections from unresolved source associations.
- Verify endpoint eligibility, ownership context and native grammar conformance before acceptance.
