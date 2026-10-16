# MDSE v2 — Structural Translation Matrix (first pass)

**Status:** Gate A draft; rule candidates not yet accepted as production translator behavior.  
**Scope:** High-impact EA/SysML v1 constructs and relationships.  
**Authority:** Formal SysML v2 output (not MDSE YAML).  
**Standards baseline:** OMG SysML v2.0 [Transformation](https://www.omg.org/spec/SysML/2.0/Transformation/PDF) and [Language](https://www.omg.org/spec/SysML/2.0/Language/PDF).  
**Date:** 2026-10-15.

| ID | EA / SysML v1 construct | OMG v2 transformation basis | Current v1 MDSE representation | V2 target | Treatment / review gate | Workbench presentation |
|---|---|---|---|---|---|---|
| STR-001 | «block» Class (reusable hardware) | Block mapping → PartDefinition | Object note | `part def` | **Standard candidate** if EA stereotype actually denotes a Block; do not treat every UML Class as a Block | Reusable definition with where-used |
| STR-002 | Ordinary UML Class | General classifier mapping; **not automatically a Block** | Object note | Evaluate `occurrence def` / other appropriate definition | **Review** classifier and stereotypes; no unconditional `part def` | Definition with semantic kind |
| STR-003 | Part property owned by Block | Property/part mapping → PartUsage | Local Model Part with hasPart/partOf conventions | Typed `part` usage owned by enclosing definition | **Standard candidate**; preserve type, aggregation, bounds, property identity, redefinitions | Assembly child line |
| STR-004 | Reference property / noncomposite usage | Property mapping preserving composite/reference semantics | Local reference / part links | Referential usage rather than fabricated owned component | **Review** EA aggregation and type evidence | Reference usage distinctly styled |
| STR-005 | «proxyPort» | Proxy port mapping → PortUsage | Local Interface endpoint | Typed or untyped `port` usage (as supported by source) | **Standard candidate**; preserve conjugation/direction/feature exposure evidence | Boundary port |
| STR-006 | «fullPort» | CommonFullPort mapping → PartUsage, FullPort metadata | Local Interface endpoint | `part` usage with full-port semantics/metadata | **Standard**; do not force into `port` | Full port / part boundary |
| STR-007 | «interfaceBlock» | InterfaceBlock mapping → PortDefinition | Object/interface note | `port def` | **Standard candidate**; distinguish port definition from `interface` connection | Reusable port contract |
| STR-008 | «flowProperty» on interface/block | Feature mapping, direction/type preserved | Often independent Item Flow note | Directed features on relevant definitions/usages | **Review** before emitting independent `flow` | Input/output feature |
| STR-009 | Connector (assembly topology) | Connector/association mappings conditioned on kind/endpoints | Connection / exposes in Local Model | Applicable `connection` / `interface` usage | **Review** connector stereotype, end roles and owner; topology isn't automatically power/data flow | Link between resolved endpoints |
| STR-010 | «bindingConnector» | Binding-related mappings; distinct from topology | `equals` or `exposes` in selected cases | Binding semantics supported by standard v2 model | **High-priority review**; existing exposes heuristic must not create non-equivalent formal semantics | Binding link with provenance |
| STR-011 | Generalization | Specialization mapping | subtypeOf | Native specialization | **Standard candidate** only if a true generalization; never inferred from family similarity | Type hierarchy |
| STR-012 | Package/nesting | Package and owning membership/namespace mapping | Folders, hasChild/childOf | `package`, namespace ownership / feature membership | **Review** ownership independent of note path; source packages don't imply physical partOf | Namespace browser |
| STR-013 | BOM parent-child part line | No generic SysML-v1 BOM transformation; engineering extension | Parent Local Model Parts | Contextual `part` usage on parent/configuration | **Approved MDSE variation needed**; preserve source ledger and effectivity | Multilevel BOM and Where Used |
| STR-014 | BOM alternate Mfg Part Number continuation | No generic v1 construct | BOM-ALT-001 | Conditional alternate selection; native variation only if semantics support | **Review** interchangeable versus supplier option; no additional consumption | Alternates nested under primary line |

## Mandatory source fields

Capture source type, stereotypes, owner, classifier, endpoint roles, connector stereotype, direction, multiplicity, aggregation, revisions, source GUID, imported UID and provenance before transforming. Do not rely on folder classification alone.

## Relationship ownership principles

1. **Containment** — owning namespace/feature membership is a formal SysML declaration, not filesystem nesting.
2. **Typing** — a usage references a definition; the usage is not its definition.
3. **Specialization** — retains formal type semantics; not inferred from `variantOf`.
4. **Connection and interface** — represent distinct semantics; source stereotypes and contextual endpoints determine the construct.
5. **Binding** — cannot be rewritten as a physical connection solely because two endpoints appear together.
6. **Reverse/where-used** — generated by Workbench querying authoritative usages; not duplicated as independent statements.
7. **BOM alternates** — candidates never increment assembly quantities.

## Verification checklist

- Extract actual EA metadata values for each mapping group (including cases with missing stereotypes).
- Tie each OMG claim to the precise normative mapping class/section; references above are document level until this check.
- Create synthetic pairwise fixtures for proxy port, full port, binding, part use, reference use, interface block, generalization and manufacturer alternate.
- Run an independent SysML v2 parser/validator; no fixtures are claimed validated yet.
- Compare generated structure, typing, multiplicity and ownership with original EA meaning and retain review evidence.

## Open questions for the next pass

1. Which EA plain Classes in our model are true reusable physical types versus UML classes or information types?
2. How are FullPorts and ProxyPorts stereotyped and represented in the CSV exports?
3. How do `exposes` and binding connector heuristics map when model intent differs from the OMG mapping?
4. How does formal SysML ownership compose when each primary MDSE element has its own Markdown note?
5. How will BOM line configurations and revision-selected usages be persisted without a parallel editable graph?

## Current numbered path references

- [Definition index](README.md)
- [Structural contract](Structural%20Mapping%20Contract.md)
- [Mapping and conformance](Mapping%20and%20Conformance.md)
- [BOM integration](BOM%20Integration.md)
- [Original v2 translator plan](../29_SysMLv2_Translator_Workbench/README_SysMLv2_Translator_Workbench.md)
- [Testing index](../25_Testing/README.md)
