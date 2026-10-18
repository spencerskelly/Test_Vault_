# Pass 6 — Native SysML v2 decision gates for 213 deferred EA aggregations
Date: 2026-10-17
Status: **Review proposal only. No approved mapping or native eligibility expansion.**

## Authoritative interpretation
OMG SysML v2.0 Language Specification (September 2025), especially §7.11 Parts and §7.25 Use Cases:
https://www.omg.org/spec/SysML/2.0/Language/PDF

**Important correction:** SysML v2 PartDefinition/PartUsage may represent logical components, **software components**, external entities, and organizations; a Part is *not limited to hardware/BOM items*. Therefore the previous strict classifier's deferral of `Software Component` is a **policy/evidence gate**, not a native-language prohibition. An external System Partner may also be modeled as a part definition/reference, but an actor parameter in a case and an owned subsystem have different meanings.

## Decisions for source categories

| EA stereotype | Native alternative | Evidence and decision before enabling | Current disposition |
|---|---|---|---|
| Physical Context | `use case def` with `subject`/`actor` roles where a genuine use case is expressed; alternatively occurrence/part representation for actual environment entity | Determine if the EA element denotes a scenario/context, environment entity, or boundary; identify its subject and participant roles. Aggregation alone insufficient | deferred_review |
| System Partner | external `part def` and `ref part` as a separately typed external entity where appropriate, or `actor` in a case | Establish external participation vs structural membership, and definition vs usage; never silently grant ownership | deferred_review |
| Software Component | `part def`/`part` for modeled software system component (allowed by language), or other appropriate logical behavior item where only function is described | Explicit reusable software component and host/containment evidence, usage typing, cardinality and relationship semantics; software allocation must remain separate | deferred_review |
| Platform | `part def`/`part` only for actual reusable structural platform; specialization/subsetting/redefinition for actual variation | Distinguish product family vs deployment host vs variant/reference; check type/usage and original connector role | deferred_review |
| Unstereotyped Class | no automatic target; candidate definition/usage selected by reviewed source attributes and relations | Inspect source semantics first; reject stereotype-name guessing | deferred_review |

Native syntax constructs above are available **alternatives**, not a claim that a given EA row qualifies.

## Workbench implementation requirements (all categories)

- **Structural view:** distinguish definition vs usage, composite containment vs reference vs actor/context. Software components may be part-like at a logical layer without BOM membership. Show port as an independent PortUsage/PartUsage only when legitimately modeled; no collapse.
- **Visual view:** distinct stereotype/context/actor/software/platform rendering and separate containment, reference, generalization and behavioral edge types; ambiguity visibly deferred.
- **Containment/connection:** retain original EA connector as evidence until owner direction, role, multiplicity and nesting are approved. Context and actor links do not become part composition by default.
- **Navigation:** definition ↔ usages, source ↔ proposed mapping, original EA connector endpoints, alternatives and review decision.
- **Validation:** explicit rule-version and source evidence, endpoint eligibility, semantic family match, typed usage, multiplicity/ownership, full native SysML v2 parser checks; no automated acceptance.
- **Round-trip/provenance:** original EA GUIDs, source type/stereotype, source direction and role, proposed native construct, review status and reason; keep individual records local.

## Dependency gates and remaining work
1. Execute exact GitHub main tests in an independent checkout (pending).
2. Review five categories with operator on representative *local-only* EA data; make explicit semantic decisions, including logical software components as valid part candidates.
3. Version controlled taxonomy statuses after decision, with separate native parser conformance fixtures.
4. Rerun all 14,688 connectors and regenerate local-only provenance ledger; use aggregates in public repository.
5. Validate actual BOM workbook separately and never auto-join BOM and EA identities.

**Approved native relationships created by this review: 0.** A separate non-SysML extension section is permitted only if the approved native standard cannot express the meaning; no custom v2 relationship.
