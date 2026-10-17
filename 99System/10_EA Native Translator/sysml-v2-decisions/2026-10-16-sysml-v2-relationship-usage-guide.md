# SysML v2 Relationship Usage Guide — MDSE Translator and Workbench
Date: 2026-10-16
Status: Guidance baseline; validate syntax/semantic constraints against a conforming SysML v2 implementation.

## Model policy
EA Object → reusable `part def` by default. EA Generalization → specialization by default. These are *import conventions*, not blanket guarantees of correct source semantics. Keep separate source provenance and target model. Prefer native SysML v2 semantics; place unsupported MDSE-specific relationships in a separate extension/metadata section, never invent language keywords.

| Concept | Definition | Use when | Do not use when | Workbench structure | Workbench diagram |
|---|---|---|---|---|---|
| Specialization | A more specific definition/classifier inherits from a general one | “B is a kind of A” and compatible definitions | Sharing a part, ownership, a versioned occurrence, or configuration resemblance | Definitions and inherited features | Inheritance/generalization arrow |
| Subsetting | A feature constrains the values of another feature | A specialized feature's values are a subset of a broader feature's values | Defining a new type or replacing an inherited feature | Usage/feature and subsetted target | Distinct subsetting edge |
| Redefinition | A feature replaces/redefines inherited feature semantics in a specializing context | A variant changes an inherited part/feature | Two independent parts or simply similar definitions | Show inherited original and replacement | Redefinition mark and original link |
| Typing | A usage is typed by a definition | This assembly contains an instance/usage of reusable part type | It is a new subclass | Usage with definition reference | Usage annotated : Type |
| Composite part usage | An owning part contains its constituent part usage | A charger includes an owned controller occurrence | It only references a separately owned occurrence | Parent/child containment | Nested part |
| Referential part usage | A reference points to an already modeled part occurrence rather than composing it | Cross-context use/reference to same occurrence | Merely sharing the same reusable definition | Link to existing occurrence | Reference-marked part |
| Connection | Relationship connecting features or ends | Physical/logical connectivity | Equality of values | Typed connection and ends | Ordinary connector |
| Binding | Equality/identity constraint between two features | Must denote equivalence rather than physical linkage | Just linked by cable or communication | Binding usage and exactly two ends | Equality-specific connector |
| Interface | Specialized interaction connection with port ends | Defined interaction between compatible ports | Generic description of a port itself | Interface definition/usage and port ends | Distinct interface connector |
| Port | Boundary interaction feature of part/system | Specify interaction point | It is the entire physical device by default | Owned typed port usage | Boundary symbol |
| Exposure | Boundary port makes an internal interaction accessible; translation concept pending native mechanism | Boundary-to-internal trace genuinely needed | Assuming all exposures are bindings or inventing v2 `exposes` keyword | Source trace plus resolved native construct | Boundary port and drill-down trace |
| Succession | Ordering between actions/occurrences | One action occurs after another | Structural ownership | Occurrence/action ordering | Sequencing flow |
| Dependency | Named reliance when a conforming native relation supports intended semantics | Requires/depends-on semantics actually justified | Assuming any EA Dependency has one universal v2 equivalent | Typed semantic relation or source-only exception | Labeled dependency edge |
| Verification | Test case verifies requirement | Verification evidence is intended | Structural connection or generalization | Test-to-requirement trace | Traceability relationship |

## Examples
```sysml
part def Controller;
part def AdvancedController specializes Controller;
part def Charger {
  part controller : Controller;
}
part def ProCore specializes Charger {
  part redefines controller : AdvancedController;
}
```
Textual spellings and context restrictions must be verified in automated parser acceptance tests before production export.

## Import classification and correction
1. Retain original EA type/connector GUID/endpoints, source notes and stereotypes.
2. Apply approved baseline defaults. Mark target validity and provenance separately.
3. Allow reviewer to replace target relationship with a native, more specific construct; display before/after semantic preview, structural/visual impact, and dependent links.
4. Never rewrite the EA source record when updating target semantics.
5. Flag invalid native mappings instead of fabricating correct syntax.
6. Preserve an explicit list of out-of-language/MDSE-only properties for relationships with no corresponding native representation.

## Further catalog expansion
Coverage must ultimately include all imported EA relationship kinds, and the complete applicable SysML v2 relationship families, including allocations, requirement relationships, flows, succession, transitions, feature chains, calculations, and metadata. Add specification-backed canonical syntax, concrete valid/invalid examples, and Workbench shape rules before marking catalog complete.
