# Golden Import — EA Realization to Requirement allocation

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation and native parser validation pending.

- When an EA Realization explicitly connects a component/part implementation with a Requirement, translate the relationship using native SysML v2 **allocation** semantics, **not satisfy**.
- Allocation represents assignment/responsibility or mapping; it does not assert that a requirement has been satisfied or verified.
- Preserve original EA connector type, direction, endpoints, stereotype and provenance; resolve actual allocation roles and target identity from trusted source evidence.
- Do not infer satisfaction from Realization. Explicit EA `satisfy` and `verify` relationships remain separate approved semantics and must not be collapsed into allocation.
- If endpoints or source meaning are incompatible or ambiguous, retain evidence with a review disposition rather than fabricate a native allocation.
- One MDSE note per reusable definition; relationship/usages do not create extra notes.
- Check emitted native allocation syntax against pinned official SysML v2 implementation before import acceptance.
