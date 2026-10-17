# BOM → SysML v2 → MDSE element and relationship integration review

Date: 2026-10-17. Status: review and implementation plan; not authorization to activate pending schema proposals.

## Reviewed existing BOM work
- `26_Definitions/BOM Integration.md`
- `14_Workbench/docs/bom/a01-a14/BOM_SEMANTIC_DECISION_RECORD_A-02.md`
- `BOM_VARIANTOF_CONTRACT_A-07.md`
- `BOM_RULESET_AMENDMENT_A-12.md`
- `BOM_A14_Validation_Checkpoint.md`
- Existing Workbench core localmodel and variantOf search results.
The A-series docs explicitly mark proposed changes, and A-14 describes partial validation. Do not assume approval or production writer availability.

## Target element crosswalk
| BOM source entity | Canonical SysML v2 element | MDSE note / ownership |
| --- | --- | --- |
| Unique normalized numbered product/assembly/part | reusable PartDefinition | one note per part number and stable UID |
| Meaningful family/type with no part number | reusable PartDefinition | one governed family definition note |
| Actual occurrence in an effective parent BOM | typed PartUsage | one distinct usage line owned by parent definition, no separate usage note |
| Historical revision/effectivity | source evidence/metadata | ledger plus note summary, not one note per revision |
| Non-primary manufacturer alternate | source alternate-selection evidence; native variation only if substantiated | do not count as extra required usage |
| Questionable relationships | not native | MDSE YAML flagLink on relevant note plus human-readable reason in body |

## Relationship crosswalk
1. Parent assembly to installed component → owned typed PartUsage; repeat rows/roles can be independent usages. Do not write child-side partOf/usedBy. Where Used is computed as reverse query.
2. Explicit discrete count → PartUsage multiplicity; missing multiplicity remains unspecified. Distinct source usage lines may not be merged merely because they reference the same child definition.
3. Measured amount and unit → usage-associated quantity and unit (separate from multiplicity). Preserve exact source decimals and dimensions. Native quantity-typed attribute representation and synchronization to MDSE Local Model remain a required design/conformance gate.
4. Family similarity → optional MDSE one-way variantOf for evidence-supported grouping, **not native specialization**, redefinition, substitutability or ownership. Approved native specialization only on affirmative subtype evidence.
5. Manufacturer alternate → per-line, same assembly/revision/configuration/group, no increase to required child count. Native variation is *not automatic*.
6. Replacement/supersedes → requires affirmative different-part-number replacement evidence; archive flag alone is insufficient.
7. Legacy/ambiguous relationship → YAML flagLink plus note-body explanation; source provenance and review disposition retained.
8. Revision configuration → one effective BOM per owning assembly and configuration; competing concurrent sources block automated selection; preserve historical ledger.

## Cross-import identity contract — critical integration point
- BOM canonical key: normalized internal part number with source namespaces and collision checks; EA canonical key: EA GUID.
- Add an **evidence-backed mapping layer** from both identifiers to a shared MDSE UID / PartDefinition. Never merge purely by display-name similarity.
- If EA and BOM both assert the same specific parent-owned usage, match on parent identity, child definition, role/occurrence identity, configuration and source evidence before choosing whether these are corroborating assertions or independent usages. Default is preserve independently; never merge merely by identical endpoints.
- Keep both source connectors/rows attached as provenance references when an explicit approved match is made.

## Implementation gates in order
1. Approve canonical joint identity and cross-source conflict policy.
2. Normalize BOM source rows, source manifests, primary/alternate continuations, revisions, configuration/effectivity and units; retain local-only raw ledger.
3. Build deterministic PartDefinition notes and family references; keep one note per normalized number.
4. Build effective per-parent PartUsage declarations with distinct stable usage identifiers, roles, multiplicity, quantity, UOM and provenance.
5. Reconcile EA-owned usages and BOM-owned usages without automatic endpoint-only deduplication.
6. Introduce quantity/UOM read-write schema only via approved version migration; verify quantity-kind and unit correctness with native syntax validation.
7. Implement one-way variantOf as governed MDSE-only grouping; assert subtype/variation/supersedes only with positive evidence.
8. Generate unresolved YAML flagLink plus explanatory note body and review queue.
9. Workbench structural/visual display: definitions versus usages, owner containment, where-used reverse queries, revision/alternate selection, flagged links, visual quantity/multiplicity distinctions, provenance navigation.
10. Execute synthetic fixtures, native SysML v2 parser, roundtrip/reimport, idempotence, collisions, unit conversion, alternate counting and no-data-in-repo CI. Commit only aggregate findings.

## Acceptance criteria
- One definition note per part number, zero accidental duplicate notes from revision/source overlap.
- One effective BOM selected per parent/configuration; historical BOMs preserved.
- Separate source usage lines stay separate absent affirmative same-occurrence evidence.
- Multiplicity is unspecified when absent. Measured quantity/unit are not substituted for discrete count.
- Alternate continuation rows do not inflate structure or consumption.
- Where Used has no child-maintained parent inventories and is correct for selected configuration.
- No unsupported native specialization/variation inferred from variantOf, replacements, or similar names.
- All unmatched relations produce note YAML flagLink and an intelligible explanation.
- Source-only ledgers remain local and parser/Workbench conformance is required before release.

## Key still-open decision
What constitutes affirmative evidence that an EA usage and a BOM row describe **the same usage**, instead of two independently modeled usages? Prefer conservative separate usages until reviewed, because prior policy preserves multiple EA connectors for distinct use of the same part.

## Superseding approval — separate EA and BOM note identities (2026-10-17)

This section **supersedes** the earlier proposed automatic shared-UID identity reconciliation and the 'first decision' at the bottom of this review.

1. **Independent import first.** Every imported EA element note and every imported BOM part note receives its own unique, stable MDSE UID. Do not automatically coalesce notes/UIDs, even when an EA element alias equals a BOM part number.
2. **Cross-source discovery key.** EA `Alias` may contain the part number recorded in the BOM. Keep the exact EA alias and normalized BOM part number as independent provenance/search fields, never as proof that the two notes represent the same definition.
3. **SysML v2 first, BOM metadata retained.** Map recognized BOM structure into native SysML v2 definitions/usages and supported attributes where valid; put BOM-only fields that do not fit approved SysML v2 constructs into governed MDSE YAML, preserving values and source provenance. Do not invent native syntax for these fields.
4. **Post-import crossover review.** After both complete imports, build candidate matching reports (EA alias ↔ BOM part number, plus description, category, product context, relationships and revisions). Review possible overlaps and decide individually which notes, if any, should merge. No automatic note merge, deletion or UID rewriting.
5. **Merge governance.** A future merge requires an explicit reviewed decision, retention of all source identifiers and relationships, deterministic choice of surviving UID, a durable UID redirect/alias for the retired note identity, inbound link repair or resolution, audit trail, and reversible staged validation. Until approved, both notes persist.
6. **Distinct usage records.** EA aggregation usages and BOM owned usages remain independent on import, notwithstanding matching definitions or endpoints. A reviewed later merge of definitions does not automatically merge independent usage lines.
7. **Unresolved links.** When exact native semantics remain uncertain, retain MDSE YAML `flagLink` with an explanatory note section, including local evidence.

### Revised implementation order

A. Define UID allocation, separate EA/BOM namespaces, provenance and BOM metadata YAML schema.
B. Import EA and BOM independently while preserving source-defined relationships/usages and historical BOM evidence.
C. Validate each imported note/usage and native SysML v2 syntax; keep raw model data out of the methods repo.
D. Produce non-destructive post-import candidate overlap report with reason/confidence.
E. Review possible note merges individually; perform only approved staged migrations with link integrity and identity redirects.

**Acceptance:** A matching EA alias and BOM part number results in **two separate notes with two unique UIDs** until explicitly reviewed and merged. Both remain discoverable as possible crossovers. Original source identifiers remain in provenance and BOM metadata remains in YAML when no native v2 counterpart exists.
