# Golden Import — Generic EA Dependency

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation and official native parser verification pending.

- Map an explicit **generic** EA Dependency to native SysML v2 `Dependency`, preserving the EA client → supplier orientation from trusted endpoint/direction evidence.
- A generic Dependency expresses reliance; do not infer ownership, physical connection, allocation, satisfaction, verification, flow or execution order.
- Do not use this fallback for specialized EA dependencies such as `trace`, `refine`, `satisfy`, `verify`, or `deriveReqt`; evaluate them under their own specific rules.
- Preserve original connector GUID, type, stereotype, endpoints and source orientation in the local-only disposition ledger and model provenance.
- Reject/defer untrusted direction or unresolved/incompatible targets rather than guessing. One MDSE note per defined element; relationships do not generate separate usage notes.
