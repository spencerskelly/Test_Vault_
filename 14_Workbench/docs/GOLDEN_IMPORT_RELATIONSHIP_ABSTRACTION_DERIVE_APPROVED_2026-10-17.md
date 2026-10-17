# Golden Import — EA Abstraction:Derive

Decision date: 2026-10-17. Status: APPROVED translation policy; runtime and native SysML v2 library/parser conformance pending.

- Explicit EA `Abstraction:Derive` maps to native SysML v2 standard-library **requirement derivation** when both endpoints are valid requirements.
- Preserve derived requirement → source requirement semantics, validated against trusted EA source endpoint direction/roles; do not infer direction from diagram layout.
- Preserve EA connector type `Abstraction`, stereotype `Derive`, GUID, endpoints, and original/normalized orientation as provenance.
- Keep derivation distinct from requirement decomposition, refinement, satisfaction and allocation. A source relationship with incompatible endpoints or uncertain roles remains flagged for review, rather than forcing native derivation.
- No separate MDSE note for a relationship or local usage. Validate native syntax and repeat-import behavior before acceptance.
