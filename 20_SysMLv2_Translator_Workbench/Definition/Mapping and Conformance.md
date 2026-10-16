# MDSE v2 — Mapping and Conformance

**Status:** Worklist, not a claim of exhaustive verification.

## Translation classification
- **Standard:** follow applicable OMG SysML v1-to-v2 meaning.
- **Approved variation:** documented MDSE source reinterpretation, with rule ID, source evidence, reason and standards-valid target construct.
- **Review required:** missing, ambiguous or incompatible mapping; keep source evidence outside canonical structure.

## Initial review priorities
1. Block/Class → definition; Part → contextual usage with multiplicity and composition.
2. FullPort/ProxyPort, InterfaceBlock, PortDefinition/PortUsage and connections.
3. FlowProperty/ItemFlow, binding versus connection/exposure.
4. State/action/transition ownership and behavior semantics.
5. Requirement subject, satisfaction, verification and dependency.
6. Namespaces, package nesting, feature membership and specialization.
7. BOM manufacturing substitutions, effective revisions and measured quantities.

Complete the one-row-per-concept mapping workbook, a source-target relationship matrix, and independent conformance fixtures before broad importer changes.

Reference: https://www.omg.org/spec/SysML/2.0
