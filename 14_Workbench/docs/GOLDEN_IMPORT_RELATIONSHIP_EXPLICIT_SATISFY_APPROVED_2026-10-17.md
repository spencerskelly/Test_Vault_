# Golden Import — Explicit EA Satisfaction

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation and native SysML v2 conformance pending.

- Explicit EA `«satisfy»` maps to native SysML v2 **satisfy** semantics, distinct from allocation and verification.
- Preserve the original EA source connector GUID, type, stereotype, endpoints, orientation and evidence; validate native client/requirement roles before generating syntax.
- This link makes a modeled satisfaction claim, not proof of verification or successful test execution.
- Generic EA Realization between component and requirement remains separately approved as **allocate**, not satisfy. Never silently upgrade allocation or generic dependency to satisfaction.
- Unresolved endpoints/roles stay flagged for review; no inferred relationships or extra MDSE usage notes.
- Confirm native serializer/parser validity and repeat-import stability before accepting the imported relationship.
