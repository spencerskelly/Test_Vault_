# Golden Import — Component-to-component Realization

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation and parser validation pending.

- An explicit EA Realization between two compatible components maps to native SysML v2 **allocation** semantics, representing implementation mapping (for example physical controller implementing a logical control component).
- Do not translate this source relationship to specialization, physical containment, satisfaction or verification by default.
- Preserve exact EA source/target endpoints, original direction, type/stereotype, source identity and provenance; normalize allocation roles only from trusted evidence.
- If either endpoint or its role is ambiguous or incompatible, flag for review rather than invent a native allocation.
- Reusable components remain one PartDefinition/MDSE note each. Relationship usages do not create additional notes.
- Verify emitted allocation syntax and model semantics with the pinned native SysML v2 parser.
