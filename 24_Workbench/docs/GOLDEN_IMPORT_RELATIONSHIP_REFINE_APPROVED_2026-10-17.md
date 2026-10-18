# Golden Import — EA Refine

Decision date: 2026-10-17. Status: APPROVED translation policy; official SysML v2 library and parser conformance still pending.

- Explicit EA `«refine»` maps to native SysML v2 `Dependency` annotated with the standard-library `Refinement` metadata, rather than an unqualified generic Dependency.
- The **refining (clarifying) element** is the client/source and points to the **element being refined** (supplier/target), subject to trusted EA endpoint orientation verification.
- Refinement communicates a more precise or detailed description. It does not imply specialization, redefinition, containment, allocation, satisfaction or verification.
- Preserve original EA stereotype `refine`, source connector type, GUID, direction and endpoints in provenance. The Workbench should display Refinement distinctly from ordinary Dependency and expose metadata and navigation.
- If source direction is ambiguous or standard-library annotation cannot be validated, retain a review disposition rather than stripping the metadata or silently lowering to generic Dependency.
- Validate generated syntax against pinned SysML v2 libraries and parser prior to native acceptance.
