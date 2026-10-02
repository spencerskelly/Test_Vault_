# MDSE Modeling Ruleset 1.22

## Status

Current modeling ruleset for the MDSE vault. Reissued from 1.21 (W-260): the cross-vault sections, `instanceOf` and the `control` and `boundary` note are removed; section numbers are kept so that references still resolve. The rules the translator follows are in `Translator Definition.md`.

**2026-10-01 full-import/occurrence amendment:** Sections 9 and 15 incorporate the approved vault-usability/importer decisions from the full-import review plus W-293/W-294 local part/endpoint/connection/flow occurrence semantics. `relationships.yaml` schema 1.35 remains the note-level relationship authority. These amendments do not reopen unrelated semantic rules.

## 1. Model meaning before structure

Classify the concept semantically before choosing a type. Search for an existing authoritative definition before creating a new one. Prefer reuse, then instance, true specialization, decomposition, and only then a new independent concept.

Folder placement is navigation only.

## 1.1 Type and subtype nomenclature

The primary reusable engineering-entity type is **Object**. The former top-level type name `Thing` is deprecated.

`Object` may represent physical hardware, software, firmware, or other reusable engineering entities according to its approved subtype. In translator material, use **EA Object** for the Sparx EA metaclass and **MDSE Object** for the MDSE type whenever ambiguity is possible.


Every model note (a note made from a class template in `99_System/05_Templates`) uses `type` for its primary MDSE semantic class and `subtype` for an approved specialization/classification within that type.

Notes in `99_System` are reference and system notes and carry no `type` or `subtype` (W-243).

The former property name `kind` is deprecated and must not be used in new notes.

`subtype` as a property is distinct from the semantic `subtypeOf / supertypeOf` relationship. Use the relationship only for true reusable generalization between modeled elements.

## 2. Generalization

Use `subtypeOf` only for a reusable invariant semantic distinction. Where the difference is ordinary data or configuration, it is not a `subtypeOf`; there is no `instanceOf` field (W-184).

## 3. Product control

Removed in 1.22. `control` and `boundary` are not properties of a note (W-88, W-112).

## 4. Relationships

Author only the forward/owner-side relationship. Paired/symmetric inverses are generated derivative YAML and must be synchronized before handoff.

The same semantic relationship vocabulary applies across vault boundaries.

State ownership follows W-291/W-292: an Object `hasState` a State or State Machine; a State Machine `hasState` a State. Those pairs do **not** use `hasChild`. `stateOf` is the generated inverse.

## 5. Function vs Use Case

Function = behavior controlled by the modeled product.

Use Case = externally controlled behavior/scenario/actor goal.

Do not convert human/external-system steps into product Functions merely because they appear in a journey.

## 6. Evidence and uncertainty

Do not silently fill missing source information. Preserve ambiguity and create a model check when required.

## 7. Requirements

Requirement `appliesTo` defines scope. Function and Design may use `satisfies`. Verification uses `verifies`.

## 8. Verification

Verification defines reusable intent; Procedure orders activities; Setup defines capability; Plan selects campaign content; Result records execution evidence.

## 9. Navigation

Folder structure is for human navigation; it does not create semantic relationships.

Do not split a folder based on element count alone. Split only where a meaningful semantic or navigational subdivision exists. Do not create arbitrary overflow buckets such as numbered groups solely to reduce folder counts.

Aim for approximately 5–6 meaningful folder levels below the vault root for normal MDSE content. Deeper structure is allowed when it preserves useful formal/source structure, including regulatory hierarchies, document hierarchy, or real architecture.

An intermediate folder may be collapsed automatically only when it has exactly one meaningful child branch and has no independent note, content, or navigation value.

### 9.1 Automatic navigation artifacts

Do **not** generate README/Base/Canvas scaffolding for every folder.

Automatically generate the standard navigation set only for the primary MDSE top-level domain folders:

- `README_<folder>`
- `BASE_local_<folder>`
- `BASE_all_<folder>`
- `CANVAS_<folder>`

Lower-level navigation artifacts are exception-based and should be added only when a demonstrated navigation need exists.

The Local Base shows direct contents. The All Base is recursive. The Canvas is a map rather than an exhaustive inventory; a soft target of roughly 12–20 nodes is appropriate.

### 9.2 README purpose

A top-level README should explain:

1. what is in the folder;
2. what kinds of elements belong there;
3. where a user should start;
4. what related major areas may be useful next.

Do not put exhaustive generated inventories in the README; use Bases and Canvas for those views.

The root README is a human entry point first. It should briefly explain the vault, the primary MDSE folders, and relationship-based navigation before showing operational import/run information.

### 9.3 Package notes

EA packages normally become folders only. Do not generate a package note for every package. Create one only when it preserves meaningful information or adds genuine navigation/context value.

## 10. Company/domain authority

Removed in 1.22. The vault is one vault with no cross-vault links (W-01).

## 11. Cross-vault identity

Removed in 1.22 (W-01). Every note still has an immutable 30-character `uid` (W-13); its format is in `AI_INSTRUCTIONS.md`.

## 12. Vault creation and splitting

Users create new vaults; AI does not autonomously create or split them.

When scale, access, lifecycle, ownership, search quality, or AI context becomes problematic, AI may recommend that the user consider splitting a vault.

## 13. Cross-vault views

Removed in 1.22 (W-01).

## 14. Integrity before handoff

The checks a translator run must pass are in `Translator Definition.md` section 10. For hand-made work before handoff: YAML parses; ids and uids are unique; links resolve; inverses are synchronized; Functions have performers where applicable; requirement basis, satisfaction and verification gaps are visible.
## 15. Full-import usability and importer governance

These rules were approved from the 2026-10-01 full-scale native-import assessment. They govern importer output and vault usability without changing settled semantic type/relationship rules.

### 15.1 Human-oriented naming

Use the shortest human-readable name that remains unambiguous in context.

Soft targets:

- folder names: aim for ≤40 characters;
- filenames: aim for ≤80 characters.

These are not truncation limits. Longer names are allowed when shortening would remove important meaning. Do not invent opaque abbreviations solely to meet a soft target.

Semantic engineering name and filesystem locator are separate:

- UID remains the stable machine identity;
- filename may carry context needed for uniqueness;
- visible heading/title remains the engineering/source name unless an approved semantic rename exists.

Ports use the filesystem form `i<shortest unambiguous owner label> - <Port Name>.md`, while the visible heading remains the Port name. The `i<...>` convention is for Ports only.

Requirement filename suffix `_r` is collision-specific, primarily for same-named Function/Requirement collisions. It is not mandatory on all Requirements.

Generic repeated source headings such as `General` or `Normative references` may use the shortest useful source-document identifier in the filename while preserving the original heading.

Default to EA Name. EA Alias may become the human-facing name only when Name is clearly unsuitable for people, such as a URL, file path, generated machine string, punctuation-dominated text, or copied metadata. Preserve the original EA Name in provenance/source evidence.

If both Name and Alias are unsuitable, do not invent polished terminology without semantic evidence. A first-class element that still lacks a safe human name becomes a model-check/review item.

### 15.2 Reserved infrastructure namespace

Plain engineering names are reserved for model content.

Known infrastructure uses reserved naming, including:

- `Template - <Name>`
- `Rule - <Name>`
- `README_<folder>`
- `BASE_local_<folder>`
- `BASE_all_<folder>`
- `CANVAS_<folder>`

Known infrastructure collisions may be renamed automatically. A collision with an existing model or user-authored engineering note is blocking and must not be silently renamed.

Collision detection includes imported files, all pre-existing base-vault/system files, and existing model/user-authored notes. Do not solve collisions by blindly adding `_1`, `_2`, and similar suffixes when meaningful source/context can provide a human discriminator.

### 15.3 Approved automatic shortening

Before path evaluation, automatically apply approved human-readable shortening when it remains unambiguous:

- remove repeated parent context from child folder/file names;
- remove redundant generic structural wording when the parent path already establishes the role;
- strip source/package mechanics such as `SC_Pkg`;
- use established abbreviations such as `UBMID` for Universal BMID;
- compact or omit parenthetical engineering identifiers in folder names when authoritative notes retain them;
- shorten navigation folders for formal/regulatory hierarchy while preserving the exact source title/identifier in the authoritative note;
- remove redundant numeric source-placement prefixes in already-established Use Case navigation folders such as Who / What / When / Where / Why.

Formal/regulatory notes preserve exact source identifiers/titles where required for fidelity.

### 15.4 Blocking path preflight

Path checking happens before writing.

Preflight order:

1. apply normal naming;
2. substitute explicit Alias for clearly machine/noise Names;
3. remove repeated parent context;
4. strip source-mechanics suffixes;
5. apply approved established abbreviations;
6. remove redundant generic structural wording;
7. shorten navigation folders where authoritative notes retain the full formal title/identifier;
8. recalculate full repository-relative paths;
9. flag unresolved excessive paths.

After approved shortening, any path still over the final hard repository-relative limit is a blocking preflight error. The importer must not begin writing until every path has a deterministic human-readable destination.

The exact hard repository-relative path threshold is **OPEN**. A 220-character value has been discussed but is not adopted.

### 15.5 Root-package placement and housekeeping

Never create `unnamed/` as a fallback for a known root package. Known root packages with imported child content must receive intentional placement according to MDSE placement rules.

Before model write, importer/bootstrap should safely:

- remove tracked `.DS_Store`;
- initialize/validate `.vault.yaml`;
- enforce reserved infrastructure naming;
- rename known infrastructure files deterministically where needed;
- update the root README for the actual imported vault;
- record housekeeping actions in run diagnostics.

### 15.6 Reconciliation-based run completion

A run is complete only when every planned entity reconciles to an explicit terminal state:

- written;
- intentionally suppressed/collapsed/transformed by rule;
- explicitly failed.

There must be zero unexplained remainder. If the writer stops part-way, the run status is `INCOMPLETE / FAIL`; file creation alone never establishes completion.

The Run Manifest remains concise and human-readable. Detailed audit reports hold path exceptions, collision handling, naming substitutions, Alias use, transformations, suppressions, duplicate relationships, unresolved semantics, model checks, and other implementation diagnostics.

### 15.7 Repeated semantic relationships and local occurrences

Do not repeat an identical semantic relationship target merely to express multiplicity.

However, do not discard evidence that several source occurrences may represent genuine engineering quantity or distinct local positions.

Approved local-endpoint ownership rule:

- a local connector, Port, mating surface, or proxy occurrence is owned by the MDSE Object/part on which that occurrence exists;
- the Interface references the participating local endpoints rather than owning those endpoint occurrences;
- the Interface owns the connection context and local flow context between the participating endpoints;
- the local endpoint must preserve its source/local identifier, reusable type/supertype, owning Object, and source provenance needed to distinguish it from other occurrences;
- a local flow must preserve its local identifier, reusable flow type/supertype, and endpoint/direction context.

A named EA occurrence does not require a standalone Markdown note merely to preserve endpoint identity, connection detail, flow detail, or engineering quantity if those facts can be represented as addressable local model data.

Every local endpoint and local flow receives a stable internal local identity separate from its visible engineering identifier/name. The stable local identity must remain unchanged when the human-facing identifier is renamed, so existing references can remain valid.

W-303 defines the v0.8.0 local-ID style for all local record kinds: `part-*`, `ep-*`, `conn-*`, and `flow-*` followed by an opaque stable token. Imported tokens are deterministic from immutable EA source identity/provenance. Do not use ordinal numbering or mutable engineering names as durable identity. Future Workbench-created local records follow the same prefixes with generated stable tokens.

Local identity is contextual rather than vault-global.

- A local **part occurrence** is durably identified by owning note UID + part local ID.
- A local **endpoint occurrence** is durably identified by owning note UID + its containing part-occurrence path (when applicable) + endpoint local ID.
- A local **connection** is durably identified by owning note UID + connection local ID.
- A local **flow** is connection-scoped and is durably identified by owning note UID + connection local ID + flow local ID.

Local IDs therefore need to be unique only within their approved semantic scope. Moving an occurrence to a different owning semantic element is a real ownership/model change and may require relationship/address updates.

Requirement `appliesTo` may directly target an addressable local occurrence inside its owning note. A local-target Requirement therefore retains the existing `appliesTo` semantic relationship; do not create a new relationship solely because the target is contained rather than file-backed.

The durable semantic target is the owner's immutable MDSE UID plus the occurrence's stable local ID. The human/Obsidian link representation may use an address into the owning note, but the literal anchor/link syntax is still to be verified against Obsidian and MDSE tooling.

Authoritative local endpoint and local flow records live as **structured, addressable Markdown blocks in the body of their owning note**, not as nested frontmatter/YAML objects.

Frontmatter remains focused on note-level MDSE semantics and note-level relationships. Local occurrence detail remains human-readable without plugins and may be parsed/validated/edited by MDSE tooling.

The Local Model is a **governed body region**, distinct from ordinary narrative text (W-298). MDSE interfaces must present Local Model records separately from normal note text, Properties and note-level Relationships. General text editing must not replace or rewrite the governed Local Model region. W-302 fixes the v0.8.0 boundary: immediately below `## Local Model`, use `<!-- MDSE:LOCAL-MODEL START schema=0.1 -->`; close with `<!-- MDSE:LOCAL-MODEL END -->`. A note may contain at most one such region. Missing, duplicated, nested or mismatched markers are model-health errors and block structured Local Model editing. The markers are parser/editor boundaries only; the records inside remain the human-readable model content.

A local occurrence uses the field **`definition`** to reference its reusable semantic definition. This is intentionally distinct from `subtypeOf`: the local occurrence is an installed/contextual occurrence of that reusable definition, not a reusable specialization of it.

Examples:
- local endpoint `J4` may have `definition: [[8-Pin Circular Connector]]`;
- local flow `CAN_H` may have `definition: [[CAN]]`.

Reusable Object/assembly usage follows the same occurrence-vs-definition rule. When a reusable Object is used inside another Object/system and the contextual use matters, represent that use as a **local part occurrence** owned by the containing context rather than duplicating the reusable Object note.

A local part occurrence:

- has its own stable local ID;
- uses `definition` to reference the reusable Object/assembly definition;
- may carry a local engineering identifier/name and multiplicity;
- inherits invariant structure and interface definitions from its reusable definition;
- provides the context needed to distinguish two uses of the same reusable assembly in one product;
- does not require a standalone Markdown note solely because it is a contextual use.

Invariant structure and connections that are true for every use of the reusable assembly remain with the reusable definition. Integration-specific connections belong to the containing product/system/configuration context.

Therefore the same reusable assembly may be used in Product 1 and Product 2 while the same inherited endpoint (for example J4) connects to different partners in each product. A connection references the **part occurrence + inherited/local endpoint**, not merely the reusable assembly definition.

W-306 establishes an Obsidian-native-first rule for MDSE representations: core Obsidian/standard Markdown/YAML first, broad plugin compatibility second, Workbench-only storage or syntax only when necessary. Workbench should enhance the native vault, not be required for basic reading/navigation.

The local-ID format is settled by W-303, the managed-region boundary by W-302, and the canonical heading + named-field record pattern by W-304. Part occurrences reuse Object/assembly definitions; endpoint occurrences reuse Port/interface definitions. W-305 adds lazy materialization: nested pins/contacts/sub-interfaces remain implicit through the reusable definition until the local context needs to address one independently; only then is a recursive `ep-*` child record created with `parent`. Connection-scoped flows are authored once on the carrying connection and are indexed/displayed from every participating interface. EA source identifiers/provenance are not Local Model engineering fields; import traceability lives in `99_System/11_Import/Local Model Source Map.csv`. W-306 settles anchor/link rendering: each materialized Local Model record uses a native Obsidian block ID matching its stable local ID, while headings remain engineering-readable. Cross-note references use ordinary block links such as `[[Owner Note#^ep-42bd90|J4]]`. Remaining open items are first-class-note promotion criteria and structured-authoring UX.

#### 15.7.1 Port/flow preservation requirements from current-model audit

The 2026-10-01 Port audit found that the current v0.5 model is not sufficient to preserve connection-specific flow allocation.

Preserve these facts in the replacement local-occurrence model:

- a local endpoint retains its local engineering identifier, reusable `definition`, endpoint kind, and owning/context address; EA-only source provenance is retained in the Local Model Source Map rather than the engineering record;
- source Port multiplicity/quantity evidence must not be discarded merely because local occurrences are collapsed into body records;
- the connection between two local endpoints must be independently identifiable/addressable from either endpoint;
- each local flow is allocated to a **specific connection**, not merely to one of the participating endpoints;
- one connection may carry multiple flows, for example J4 ↔ P4 carrying 5 V, CAN, and pilot;
- each flow retains its own local identifier, reusable `definition`, direction where known, and provenance;
- EA conveyed InformationFlow items must be translated rather than silently omitted;
- importer output must validate against the current element schema. v0.5 currently maps EA interface-class stereotypes such as `Electrical & Material Interface` to `type: Port` with subtype values that are not allowed by the current Port subtype schema (`proxy`, `full` only); this is an importer/schema reconciliation defect, not an approved new Port subtype.

The existing note-level `interfaces`, `hasFlow`, `transmits`, `receives`, and `exchanges` relationships may remain useful for reusable/summary semantics, but they must not be treated as sufficient evidence of which local flow belongs to which local endpoint-to-endpoint connection.

Every local endpoint-to-endpoint connection receives its own **stable owner-scoped local ID**. Local flows are owned by or explicitly allocated to that connection, not directly by either endpoint. The connection is the authoritative binding context for:

- endpoint A;
- endpoint B;
- all local flows carried across that connection;
- per-flow direction where known;
- source provenance for the connection and conveyed-flow evidence.

The local connection record is owned by the **lowest meaningful common Object/system context** in which both participating endpoints are brought together. This is a semantic/configuration ownership rule, not a folder-placement rule and not a requirement to mechanically choose the deepest common parent. Neither endpoint arbitrarily owns the connection, and a standalone Interface/connection note is not required solely to represent the local binding.

A local connection may optionally use **`definition`** to reference a reusable interface/connection definition when one genuinely exists. The local connection remains valid without a definition; do not create reusable interface definitions merely to populate the field. As with endpoint and flow occurrences, `definition` indicates contextual use of a reusable semantic concept and is not `subtypeOf`.

A local flow therefore means “this occurrence of a reusable flow definition on this specific connection,” not merely “a flow associated with this Port.”

Local flow identity is **connection-scoped**. The durable flow address is the owning note's immutable MDSE UID + the connection's stable local ID + the flow's stable local ID. A flow local ID therefore needs to be unique only within its owning connection.

MDSE visualization tooling must be able to derive at least two selectable connection views from the same authoritative data:

- **Interface view** — shows participating parts/endpoints and their connection/interface relationships;
- **Flow view** — shows the flows allocated to those connections, including multiple flows on one connection.

For a local flow, endpoint participation uses the controlled roles **`transmit`**, **`receive`**, **`exchange`**, or **`unspecified`**. These roles are interpreted relative to the participating endpoints of the owning connection. `exchange` means bidirectional participation. Tooling may derive the opposite endpoint's complementary role where unambiguous rather than redundantly storing both ends.

Reusable interface definitions may contain **nested addressable interface members** such as connector pins, terminal positions, or mating features. This is containment/decomposition, not `subtypeOf`. A local endpoint occurrence that references the reusable definition inherits that reusable interface structure; do not duplicate every child member as a separate Markdown note or repeated local definition solely because an occurrence exists.

A connection or local flow may address a nested member of an endpoint occurrence (for example J4 / pin 2) when the engineering connection is made at that level. The durable occurrence path therefore may extend through the endpoint occurrence into its inherited nested interface member.

Local body records must therefore be indexed by MDSE tooling for navigation, validation, relationship exploration, and generated Canvas views; frontmatter-only indexing is insufficient for this model.




### 15.8 Synchronized importer/base releases

From W-299 onward, each newly issued native importer intended for use is paired with one clean base-vault release using the **same semantic release version**.

- the importer declares its release version;
- the clean base vault declares the same value in `.vault.yaml` as `mdse_release`;
- the importer checks the two values before planning or writing and refuses a mismatch;
- the Run Manifest records importer release, base release, relationship-schema version and element-schema version separately;
- relationship and element schemas keep their own independent version numbers.

Existing historical artifacts are not retroactively renamed. The first newly issued synchronized pair after the v0.7 merge candidate is v0.8.0.
