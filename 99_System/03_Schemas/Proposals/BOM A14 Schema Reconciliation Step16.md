# Step 16 — BOM A-14 schema reconciliation (PROPOSAL ONLY)

**Status:** For methodology review. **Not an approved W-decision, active schema revision, plugin release or writer upgrade.**
**Staged source:** `integration/bom-a14-source-step15-2026-10-09` at `5d34b3898d7c0a56719435c75b2993b876fca3d6`.
**Governing authority:** `Test_Vault_/99_System/03_Schemas/` and controlled `Base Vault/Definition/mdse-release.yaml`.
**Proposal files:** `bom-local-model-06-readonly.yaml` and `bom-variantof-oneway.yaml` in this folder. They are intentionally outside active schema filenames and not included in the generated runtime Base.

## 1. Current authority versus proposed behavior

| Topic | Active contract | Verified BOM implementation | Decision |
|---|---|---|---|
| Local Model record format | `local-model.yaml` **0.5**, readable 0.1–0.5, writes 0.5 | Workbench reads 0.1–0.6, **writes 0.5**; 0.6 recognizes new Part amount fields | Keep canonical **0.5**, isolate 0.6 reader proposal |
| `quantity` + `unitOfMeasure` | **Not legal** under 0.5 Part records | 0.6-only Part reader and provisional validator | Read-only trial; **never** emit under 0.5 marker |
| `multiplicity` | Existing `positiveIntegerOrSourceMultiplicity`; interchangeability count | BOM distinguishes per-occurrence amount | Preserve legacy source grammar; do not tighten historical versions without migration |
| `variantOf` | **Absent** from `relationships.yaml` **1.36** | Workbench's read-only Object graph validator resolves link shapes, self/cycles/duplicates | Propose **oneWay Object→Object**, no stored inverse |
| Object family subtype omission | `element-types.yaml` **1.18** lists Object subtypes without an explicit omission grant | A-09 proposes family/type Objects without invented subtype | Separate, prerequisite Object-schema decision |
| Release | `mdse-release.yaml` **pre-release**, localModel 0.5 | Step 15 source-level CI passed, no controlled 0.6 release | Do not alter manifest, runtime plugin lock or live templates |

The original BOM artifacts (A-01–A-14) are fully retained and checked by a **31/31 SHA-256** GitHub audit. The Step 15 isolated non-squashed candidate passed **462 Workbench tests**, **30 BOM-focused tests**, and original release checker **0 FAIL/4 expected WARN**; this does not approve ungoverned schema writing.

## 2. Proposed quantity / UOM semantics

**Owner:** One authoritative Part occurrence in the parent assembly's managed Local Model region; where-used and aggregate totals are **derived** from parents, not persisted as child `partOf` or `usedBy` lists.

- `multiplicity` counts interchangeable *instances* represented by this Part record. No silent multiplication of a single `ea` source row into both fields.
- `quantity` is a **positive exact decimal amount per interchangeable occurrence**, with matching required `unitOfMeasure`. The pair is optional but **all-or-nothing**.
- Canonical number writing proposed: ASCII plain decimal, no sign/exponent, zero or negative values. Preserve lexeme in an immutable raw-source evidence ledger. All totals use **exact decimal arithmetic**: with distinct reviewed factors, `total = multiplicity × quantity` in the same approved unit.
- Provisional reader vocabulary `ea`, `in`, `m`, `kg` is **not an authorized UOM registry**; case matters. Conversion factors, alias handling, dimensions, `ea` counted-item policy, precision and writer descriptor grammar still need explicit governance. Do not silently convert `in` to `m`, coerce zero to one, normalize ambiguous units, or infer UOM.
- The A-05 document illustrates a **future 0.6 writer**. It is a *separate gated proposal*, not what the existing BOM code actually implements. The Workbench code's `WRITABLE_VERSION` must remain `0.5` at this stage. The importer must not produce `quantity` / `unitOfMeasure` in a `schema=0.5` block.

### Needed before a governed 0.6 writer

A new W-decision and conflict-checked version; a versioned `positiveExactDecimal` and `controlledUOM` descriptor accepted by every schema consumer; an approved unit/alias registry and exact conversion specification; actual source S1/S2 profiling; import ledger and effective BOM policy; a canonical writer/editor round-trip that refuses invalid partial pairs; Base/Workbench/Importer regression including real QEAX and Obsidian interactions. Preserve 0.1–0.5 semantics under their original markers.

## 3. Proposed Object `variantOf` semantics

A `variantOf: "[[Object Family]]"` candidate is **one forward scalar link** from an Object to an Object. It describes family/similar builds, **not** inheritance, physical assembly, substitutability, configuration equivalence, copying or replacement. No `variants`, `variantOfInverse`, `subtypeOf` or target-side `partOf` fields are written as a side effect.

- Exactly one resolvable existing Object target; reject self-reference, duplicates, multiple targets, invalid note types and directed cycles, including multi-hop cycles.
- Reverse direct-family membership is an **ephemeral index query**; transitive descendants may be derived with path guards and must be distinguishable from direct links.
- Source-derived edges require traceable evidence and review. An uncertain or competing candidate goes in a ledger/finding, **not YAML**. Manual accepted relationships outrank weaker machine inferences.
- Existing Local Model `usage: variant` **continues to derive concrete choices from `subtypeOf`**, not `variantOf`.
- Family/type Objects with no governed subtype must **not** be generated merely because a grouping target would be useful. A-09's subtype-omission proposal needs its own Object-validator, template, serializer and release approval.

### Needed before authorization

New W-decision, collision-checked relationship version (candidate v1.37, **not assigned**), exact `oneWay` field declaration and guidance in active `relationships.yaml`, optional Object subtype-omission approval (candidate element-types v1.19, **not assigned**), Ruleset/AI instructions, templates/Fileclasses, deterministic UID resolution, resolver/cardinality/cycle acceptance, importer writer semantics and manual Obsidian check.

## 4. Differences that still need engineering resolution

1. **Declared readable set**: active Local Model v0.5 does not list 0.6 although the BOM Workbench parser can read it. This is intentionally treated as **experimental extra reader capability**, not a new governed format. Do not advertise active 0.6 schema support to importers/writers.
2. **Exact quantities**: Workbench's current 0.6 parser checks lexical validity and provisional units. It does **not** establish that every aggregation, cross-unit conversion, or BOM source mapping uses approved arbitrary-precision arithmetic and provenance. Keep quantities read-only until those checks exist.
3. **Canonical BindingConnector `equals`**: active 0.5 has same-owner symmetric binding semantics. The BOM reader's 0.6 branch has separate field/validation logic; a future 0.6 schema cannot accidentally regress canonical 0.5 equality, boundary `Connection.exposes`, or definitionless Interface validation. Add paired 0.5/0.6 regression fixtures before any writer promotion.
4. **Ruleset version drift**: the currently published Ruleset 1.23 introduction still refers to older relationship/Local Model versions (1.35/0.2). Resolve this through an **independently versioned Ruleset update**, not a silent edit of the active text during this proposal.
5. **Governance ownership**: `Test_Vault_` is source-schema authority. The 31 restored BOM files and existing Workbench read-only implementation are evidence, not an unrecorded W-decision. Verify latest decision-log head before assigning any number.
6. **No forward-only inverse normalization**: the global paired-field inverse generation in relationships 1.36 does not apply to proposed oneWay `variantOf`; ensure no regenerate script writes an inverse.

## 5. Acceptance and release boundaries

**This Step 16 branch may prove:** candidate specifications are consistent with current source versions and each other; canonical Git blob identities and release pins remain unchanged; all BOM original files match the frozen SHA list; canonical Base and original release checker pass; Workbench code, typecheck and full regression remain green.

**This Step 16 branch must not claim:** approved 0.6 writer/schema, complete UOM vocabulary, governed `variantOf` authoring, family subtype omission, post-BOM full real-QEAX acceptance, interactive Obsidian restart tests, a fixed Bootstrap lock/pin, or release promotion.

**Proposed next gate (Step 17):** Execute a fresh pinned full-QEAX import + deterministic replay and real-vault Workbench 0.5 acceptance **against the now-persisted BOM Step 15 source**; test read-only 0.6 fixtures separately. Do not promote BOM's 0.6/variantOf fields into existing source 0.5 notes without explicit governance approval.
