# Native SysML v2 Conjugation — Approved; remaining constructs group proposal
Date: 2026-10-17
Status: Conjugation approved. Group 1 and Group 2 proposed, NOT YET APPROVED.

## Conjugation decision (approved)
- Support native SysML v2 port conjugation and applicable native conjugate forms. A conjugated port reverses effective in/out flow directions according to the standard's type and feature semantics.
- Retain previously accepted distinct Proxy Port, Full Port and Binding Port handling; do not conflate ports, interfaces or connectors.
- EA translation: import *explicit compatible* conjugation only; do not infer it from mere connection or opposing directions.
- BOM translation: physical mating and cable relationships do not automatically establish conjugation.
- Workbench: allow contextual conjugation operation and vault-defined port contracts, show effective directions and semantic help without leaving view; maintain separate presentation filters.
- Verification: ensure reversal works for input/output features, retains definition identity, does not alter original EA provenance, survives reimports and passes native metamodel validation.

## Candidate group A — default native modeling support (proposal)
- Namespace membership and model organization.
- Import membership and alias membership.
- Feature chaining.
- Metadata application and annotation/documentation.
- Typed feature value assignment and explicit multiplicity restrictions.
All items must remain distinct native metamodel constructs. Not all are binary connectors; Workbench editing UX must use context-correct operations.
EA import only when direct source evidence and valid semantics are present, otherwise no inference.

## Candidate group B — native support with automatic translation deferred (proposal)
- Feature union, intersection and difference patterns.
- Advanced feature membership and related KerML expressions.
No automatic EA/BOM mapping from common generalization, containment, variant, attribute or BOM data; manually modeled native usage after validation.

## Exclusions / individual review
- Do not bulk-approve semantics-changing satisfaction, verification, realization, allocation, dependency, succession, interface, binding, state transition, redefinition, subsetting, or other relationships already reviewed or pending.
- Normative inventory completeness must be checked against OMG SysML v2.0 and KerML; this shortlist is not an exhaustive list.
- Ensure type-specific Workbench documentation uses in-vault definition registry; official metamodel term, valid contexts and compatibility, syntax, comparable constructs, validation and translator impact.
- For every construct track decision status distinct from implementation and conformance-tested status.

## Follow-up work
CONJ-01 normative conjugation/port contract test fixtures.
CONJ-02 explicit EA conjugation inventory and exceptions.
CONJ-03 BOM identity preservation/non-inference tests.
CONJ-04 Workbench conjugation creation, effective direction inspector and definition panel.
GRP-01 inventory complete native v2+KerML operation metamodel and categorize already approved, proposed, deferred, and individual review.
GRP-02 define registry schema and per-construct normative reference; avoid unverified grammar examples.
GRP-03 after user approval implement group A reference entries and contextual Workbench operations.
GRP-04 after user approval put group B in native-support deferred-import register.
