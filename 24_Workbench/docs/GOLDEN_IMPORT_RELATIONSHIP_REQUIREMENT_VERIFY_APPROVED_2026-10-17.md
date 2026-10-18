# Golden Import — Requirement Verification

Decision date: 2026-10-17. Status: APPROVED translation policy; implementation and official SysML v2 parser verification pending.

- Explicit EA `«verify»` maps to native SysML v2 verification semantics linking the relevant `VerificationCaseDefinition` to the verified requirement.
- Preserve the source-defined verification case and requirement endpoint roles, relationship identity, orientation, stereotype, and EA provenance. Do not infer verification from generic Realisation, allocation, package nesting or proximity.
- Keep verification-case definitions separate from test execution instances and results. A verification link does not by itself mean the requirement passed a test.
- Reusable definitions retain one MDSE note each; local usages/relationships do not create additional notes.
- If endpoints or roles are ambiguous, flag for review instead of generating an incorrect native relationship.
- Validate native syntax, endpoint eligibility, traceability and stable reimport before acceptance.
