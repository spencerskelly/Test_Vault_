# MDSE v0.8 Design Check — 2026-10-01

## Purpose

This is the release-design check for the first potentially keepable complete EA → MDSE import. It reconciles the current MDSE methodology, Local Model design, native importer, relationship/element schemas, and MDSE Workbench.

The check distinguishes:
- **model authority** — what the MDSE should mean;
- **import behavior** — how EA evidence is carried mechanically;
- **Workbench behavior** — how engineers navigate, review and edit the model;
- **current code** — what v0.7 / Workbench 0.1.14 actually do today.

## Executive result

The model architecture is sound and is simpler than the EA structure it replaces:

1. reusable engineering definitions remain first-class notes;
2. contextual uses become owner-scoped Local Model occurrences;
3. each assembly owns the connections formed below its boundary;
4. connection-specific flows are stored once on their carrying connection;
5. higher-level integration uses exposed boundary interfaces rather than reaching through a child assembly;
6. Requirements may target an addressable local occurrence through an ordinary Obsidian block link;
7. folders are navigation only;
8. Obsidian-native Markdown, wikilinks and block IDs are preferred over plugin-private representations.

The current code is **not yet release-conformant**. v0.7 is an assessment prototype and Workbench 0.1.14 is still primarily note/path based. The next implementation must bring both tools up to the settled model rather than changing the model to fit the prototypes.

## Canonical structural model

### Definition versus occurrence

- A first-class **Object** note defines reusable invariant assembly/component structure.
- A first-class **Port** note defines a reusable interface/port concept.
- A first-class **Item Flow** note defines reusable information/energy/material carried through interfaces.
- A Local Model **part occurrence** identifies one contextual use of an Object.
- A Local Model **endpoint occurrence** identifies one contextual use of a Port/interface.
- A Local Model **connection** identifies the binding between two endpoint occurrences in one assembly context.
- A Local Model **flow** allocates one Item Flow occurrence to one specific connection.

No new first-class element type is required for a local occurrence, connection or flow.

### Assembly ownership

Every assembly owns the connections formed among the occurrences below that assembly boundary.

Invariant child wiring stays in the reusable child assembly definition. A parent assembly does not reach through a child assembly to connect directly to an internal endpoint.

When an internal endpoint must be available to the next level, the assembly exposes it through a boundary endpoint:

```text
Parent Assembly
    |
    +-- Child Assembly occurrence
            |
            +-- boundary endpoint
                    exposes
                       |
                       v
                internal endpoint
```

The parent connects to the child boundary endpoint. Workbench may traverse exposure to show what lies behind the boundary, but connection ownership does not move.

### EA BindingConnector / temporary equals

EA BindingConnector evidence is not automatically interpreted as exposure.

During Stage 1:
- preserve the contextual endpoint occurrences involved;
- preserve the BindingConnector as temporary `equals` evidence at the local endpoint level when its assembly context can be reconstructed;
- retain candidate containment/inner/outer evidence in the review output;
- do not convert to `exposes` merely because structural direction is derivable.

During review:
- confirmed boundary exposure becomes `exposes` / `exposedBy`;
- a BindingConnector that actually means a peer connection is resolved to the appropriate local connection/interface meaning;
- ambiguous cases remain visible until a person resolves them.

### Multiplicity

`multiplicity: N` means N copies are intentionally interchangeable in the modeled context.

Separate local occurrences are required as soon as any copy needs its own:
- connection;
- Requirement applicability;
- state;
- local attribute/override;
- flow allocation;
- maintenance/configuration identity;
- other semantic reference.

Repeated note-level relationship targets are never quantity.

## Canonical Local Model representation

Local Model content is a governed Markdown region:

```markdown
## Local Model

<!-- MDSE:LOCAL-MODEL START schema=0.1 -->

...records...

<!-- MDSE:LOCAL-MODEL END -->
```

Each record has:
- an engineering-readable heading;
- named Markdown fields;
- a native Obsidian block ID equal to its stable local ID.

All references between local records use ordinary Obsidian block links. Bare local IDs are not persisted as relationship/reference values when a native block link can be used.

Example:

```markdown
## Local Model

<!-- MDSE:LOCAL-MODEL START schema=0.1 -->

### Part Occurrences

#### Power Board
- definition: [[Power Board]]

^part-power-board

#### Logic Board
- definition: [[Logic Board]]

^part-logic-board

### Local Interfaces

#### Power Board J2
- part: [[#^part-power-board|Power Board]]
- definition: [[CAN Interface]]

^ep-power-j2

#### Logic Board J4
- part: [[#^part-logic-board|Logic Board]]
- definition: [[CAN Interface]]

^ep-logic-j4

#### CAN
- definition: [[CAN Interface]]
- exposes: [[#^ep-logic-j4|Logic Board J4]]

^ep-can

### Connections

#### Power Board J2 to Logic Board J4
- endpointA: [[#^ep-power-j2|Power Board J2]]
- endpointB: [[#^ep-logic-j4|Logic Board J4]]

^conn-internal-can

##### CAN_H
- definition: [[CAN_H]]
- endpointA: transmit
- endpointB: receive

^flow-can-h

##### CAN_L
- definition: [[CAN_L]]
- endpointA: transmit
- endpointB: receive

^flow-can-l

<!-- MDSE:LOCAL-MODEL END -->
```

A boundary endpoint has neither `part` nor `parent`. A part endpoint uses `part`. A nested pin/contact/sub-interface uses `parent`. An inherited interface member is not materialized until the local context needs its own address.

### Cross-note local targets

A note-level semantic relationship may target a local record using the same native block link:

```yaml
appliesTo:
  - "[[Charger Controller Assembly#^ep-can|CAN]]"
```

The note UID + local ID is the durable semantic address. File path and visible heading are current navigation/display metadata.

## Native-Obsidian principle

Preference order:

1. core Obsidian primitive;
2. standard Markdown/YAML;
3. broadly used plugin-compatible representation;
4. custom Workbench behavior only where the engineering semantics cannot otherwise be preserved.

Workbench must add understanding, validation and views; it must not become a second model database.

## Current importer v0.7 conformance check

### Correct direction already present

- direct QEAX planning;
- relationship schema 1.35 baseline;
- first implementation of part/endpoint/connection/flow occurrence extraction;
- deterministic local IDs derived from EA identity;
- connection-owned conveyed flows;
- native block-link rendering exists in parts of the prototype;
- same-owner connection check prevents arbitrary endpoint ownership;
- state-placement/base-vault protections from the v0.5.2 line were merged.

### Required v0.8 corrections

1. **Managed region missing.** v0.7 writes `## Local Model` but does not write W-302 START/END markers.
2. **Record form is obsolete.** v0.7 uses bold record lines rather than the W-304/W-306 readable heading + named fields pattern.
3. **Block IDs are obsolete.** v0.7 writes derived `loc-...` anchors rather than block IDs equal to the stable `part-*`, `ep-*`, `conn-*`, `flow-*` IDs.
4. **EA provenance is in engineering records.** v0.7 writes source EA GUIDs into Local Model records; W-304 moves that evidence to `Local Model Source Map.csv`.
5. **Bare local addresses remain.** v0.7 persists textual addresses/parent occurrence strings. v0.8 should persist native block links for local references.
6. **Nested endpoint materialization is too eager.** v0.7 creates local records for source Ports broadly; W-305 requires inherited pins/contacts/sub-interfaces to stay implicit until context needs addressability.
7. **Assembly boundary/exposure is incomplete.** v0.7 excludes BindingConnector from local connections and does not preserve a contextual local temporary-`equals` representation suitable for later exposure review.
8. **Multiplicity is only copied, not governed.** v0.7 preserves source multiplicity but does not enforce W-310's interchangeable-copy meaning.
9. **Folder normalization is absent.** W-308 connector hierarchy compression and W-309 regulatory section-folder compression are not implemented.
10. **Path gate is incomplete.** W-307 requires the 88 Industrial connector >260-character offenders to reach zero before the global hard limit is chosen.
11. **Attachments are absent.** v0.7 explicitly does not extract `t_document`; v0.8 initial import must be complete for approved attachments.
12. **Diagram scope is outdated.** initial v0.8 must intentionally defer all diagrams and reconcile them as deferred, then support selectable additive diagram passes.
13. **Evidence is incomplete.** final review tables, complete terminal reconciliation and the Local Model Source Map are required.
14. **Release pairing is absent.** importer/base `mdse_release: 0.8.0` compatibility must block a mismatch.

Conclusion: do not patch v0.7 output after generation. Implement the canonical Local Model writer before the keepable run.

## Current Workbench 0.1.14 conformance check

### Correct architecture already present

- vault files remain authoritative;
- schema is read from the vault;
- index is disposable;
- relationship writer validates against the schema;
- generated Canvas is a view rather than model truth;
- explicit edit mode and transaction/undo direction are sound;
- UI already separates Properties and Relationships and has the approved Local Model surface in product documentation.

### Required Local Model work before a keepable import

1. **Index identity is still path-only.** `NoteRecord`, edges and view traversal use file paths. Implement an addressable `ModelRef`:
   - note: UID + current path;
   - local: owner UID + local kind + local ID.
2. **Local Model is not parsed.** Add parser/index support for parts, endpoints, connections, flows and local endpoint relations.
3. **Block fragments are lost.** current frontmatter indexing resolves the containing note and does not preserve a `#^local-id` semantic target. Requirement `appliesTo` and other approved local targets must resolve to the local record.
4. **Body editing is unsafe.** current body replacement can rewrite the whole body. Until region-aware text editing exists, body editing must be disabled on notes containing a governed Local Model region. Then implement editing that preserves the region byte-for-byte.
5. **No local model-health checks.** Add findings for marker errors, duplicate IDs, invalid native block IDs, broken local links, missing definitions, invalid part/parent references, invalid connection endpoints, orphan flows and unresolved local Requirement targets.
6. **Views are note-only.** Structure, Interfaces, Where Used and Requirements must become occurrence-aware. Canvas may still use note/file cards where native Canvas requires it; local occurrences can be rendered as derived/textual view nodes without becoming separate vault notes.
7. **Writer is note-to-note only.** Read/navigation support is the v0.8 keepability gate; structured Local Model authoring can follow. When authoring is added, it must use the same schema/parser and native block-link representation.
8. **WB-091 quantity behavior conflicts with W-310.** repeated YAML relationship targets must not display as engineering quantity. Treat them as duplicate-source evidence/findings or deduplicate in import; true quantity comes from Local Model `multiplicity`.

## Schema check

### relationships.yaml 1.35

The relationship vocabulary is sufficient for the current design:
- `hasPart/partOf`;
- `hasPort/portOf`;
- `hasFlow/flowOf`;
- `exposes/exposedBy`;
- `interfaces`;
- temporary `equals`;
- Requirement `appliesTo`;
- Function/Design `satisfies`;
- Verification `verifies`;
- existing behavior/state/use-case relationships.

No new note-level relationship is required for assembly exposure.

### element-types.yaml 1.16

No new first-class element type is required for local part, endpoint, connection or flow records.

### Local Model schema

A machine-readable `99_System/03_Schemas/local-model.yaml` should define the 0.1 body contract so importer and Workbench cannot silently diverge. It is a format/tooling schema, not a new engineering metamodel.

## Folder/path design check

The path strategy remains semantic-safe because folders are navigation only.

Apply, in order:

1. eliminate repeated parent wording;
2. in Industrial connector hierarchy remove repeated `Connector ASM`, `Industrial`, `Anderson`, and redundant model-number folders when the note below carries the model identity;
3. for regulatory hierarchy, if folder and directly contained element repeat the same section title, reduce the folder to the section number;
4. use meaningful Alias for machine/noise names such as encoded URLs;
5. remeasure planned paths;
6. only then choose the vault-wide hard path limit.

Do not use blind truncation or opaque filename hashes as the normal solution.

## v0.8 keepability gates

The first import we might keep must satisfy all of these:

### Semantic completeness
- all Stage-1 source elements/connectors/packages reconcile;
- all approved attachments reconcile and write;
- all diagrams reconcile as intentionally deferred;
- no unexplained source remainder.

### Local Model
- canonical schema 0.1 markers/records;
- stable block IDs;
- native block links between local records;
- source map external to engineering records;
- correct occurrence/definition separation;
- correct assembly connection ownership;
- connection-owned flows;
- temporary local equals retained for exposure review where applicable;
- W-310 multiplicity semantics.

### Path/naming
- zero >260 model-note paths in the Industrial connector branch after W-308 normalization;
- W-309 regulatory compression applied;
- no machine/noise URL filenames where a meaningful Alias exists;
- final global limit selected only from the corrected planner.

### Workbench read/navigation
- Local Model parser;
- ModelRef identity;
- native local-link resolution;
- Local Model dropdown;
- occurrence-aware Structure / Interfaces / Where Used / Requirements;
- governed-region protection from ordinary body editing;
- Local Model health findings.

Structured Local Model editing is not required for the first keepable import.

### Release/evidence
- importer + clean base both v0.8.0;
- relationship schema and element schema checked independently;
- complete Run Manifest;
- complete Ledger;
- Local Model Source Map;
- review outputs;
- terminal-state reconciliation;
- run is discarded if any blocking check fails.

## Acceptance model to inspect before keeping the full import

Select real source examples that collectively demonstrate:

1. one reusable assembly used in two product contexts;
2. two occurrences of one reusable assembly in one system;
3. one assembly with at least two internal parts;
4. internal endpoint-to-endpoint connection;
5. multiple flows on one connection;
6. one outward boundary interface tied to an internal endpoint through temporary `equals` and then reviewed to `exposes`;
7. parent assembly connected to that exposed child interface;
8. nested interface member/pin materialized only because it is addressed;
9. Requirement applying to a local part/endpoint;
10. both grouped multiplicity and separately addressable repeated parts;
11. connector/regulatory path normalization;
12. an approved attachment;
13. diagrams reconciled but absent from initial import.

## Remaining decisions that should not be guessed

These do not invalidate the architecture, but must be explicit before final release if encountered:

- exact local-ID token length/collision extension rule;
- final repository-relative hard path limit after corrected planning;
- first-class promotion criteria for a local record that later becomes reusable in its own right;
- exact handling of a BindingConnector whose assembly context cannot be reconstructed;
- disposition of the four legacy/header-only import CSVs if they remain redundant.

## Conclusion

Do not simplify the new model back toward the current prototypes.

The target is:

> reusable first-class definitions + contextual Local Model occurrences + assembly-owned connections + connection-owned flows + explicit boundary exposure + native Obsidian navigation.

The importer preserves this structure mechanically. Workbench makes it easy to understand and review. Obsidian Markdown remains the model.

## Local Model Usage and Configuration Theory (W-314)

### Purpose

The Local Model must represent not only **which reusable definition occupies a contextual position**, but also whether that position is fixed, configurable, or optional. This must be done without turning the reusable definition hierarchy into product-specific configuration data and without introducing a separate Variant Point element or configuration relationship vocabulary.

The governing separation is:

> **Definition = what an engineering concept is. Occurrence = how that definition is used in this context. Configuration = how configurable occurrences are resolved for one named or temporary product realization.**

This creates three layers that remain intentionally distinct.

### Layer 1 — reusable definitions

Reusable notes carry invariant engineering meaning. They may form true specialization hierarchies using the existing `subtypeOf / supertypeOf` relationship.

Example:

```text
Power Module [abstract]
├── 24–48 V Power Module
└── 48–96 V Power Module
```

`Power Module` expresses the common reusable family. `24–48 V Power Module` and `48–96 V Power Module` are reusable specializations.

A future optional frontmatter property `abstract: true` means that the reusable definition exists to organize/generalize other definitions but is not itself a valid effective definition for a contextual occurrence. Absence of `abstract` means false. Abstractness is not inherited: Workbench traverses through abstract descendants to find concrete descendants.

A non-abstract family root remains selectable alongside its concrete descendants. Therefore specialization and abstractness remain separate decisions.

### Layer 2 — contextual Local Model occurrences

An owning Object/system/assembly creates local positions. Each position has its own stable local block identity and a `definition` link to the reusable concept it uses.

W-314 adds the semantic field:

```yaml
usage: standard | variant | option
```

Omission means `standard`.

The values mean:

| usage | Presence | Effective definition |
|---|---|---|
| `standard` | required | exactly the stated `definition`; that definition must be concrete |
| `variant` | required | exactly one concrete candidate from the specialization family rooted at the stated `definition` |
| `option` | may be absent | when present, one concrete candidate from the stated definition's specialization family |

For `variant` and present `option` occurrences, the candidate family is derived transitively from the existing `subtypeOf` hierarchy. It consists of the root when the root is non-abstract plus every non-abstract descendant. Candidate lists are not duplicated on the occurrence.

This is contextual configuration semantics, not generalization. A local occurrence is not a subtype of its definition. Its `definition` field means "this contextual position uses this reusable engineering definition/family."

### Example assembly

```markdown
---
type: Object
subtype: electrical
id: OBJ-00100
uid: 20261001140000000skellyspencer
status: Active
tags: []
---

# Industrial Charger

## Local Model

<!-- MDSE:LOCAL-MODEL START schema=0.2 -->

### Part Occurrences

#### Power Module
- definition: [[Power Module]]
- usage: variant

^part-power-module

#### Cold Weather Heater
- definition: [[Cold Weather Heater]]
- usage: option

^part-cold-weather-heater

<!-- MDSE:LOCAL-MODEL END -->
```

The assembly has one Power Module position, not a relationship to every Power Module subtype. The position is required but unresolved until a concrete candidate is selected. The heater position may be absent.

### Example abstract family definition

```markdown
---
type: Object
subtype: electrical
id: OBJ-00101
uid: 20261001140100000skellyspencer
status: Active
tags: []
abstract: true
supertypeOf:
  - "[[48–96 V Power Module]]"
---

# Power Module

Generic reusable definition for charger power modules.
```

`abstract: true` prevents `Power Module` itself from becoming the effective installed definition while still allowing it to be the family root stated by the local variant occurrence.

### Example concrete specialization

```markdown
---
type: Object
subtype: electrical
id: OBJ-00102
uid: 20261001140200000skellyspencer
status: Active
tags: []
subtypeOf:
  - "[[Power Module]]"
---

# 48–96 V Power Module
```

This note is concrete because `abstract` is absent. It is therefore a candidate for the Industrial Charger's Power Module occurrence.

### Example reusable option definition

```markdown
---
type: Object
subtype: electrical
id: OBJ-00103
uid: 20261001140300000skellyspencer
status: Active
tags: []
---

# Cold Weather Heater
```

Nothing on the heater definition says "optional." Optionality belongs only to the contextual occurrence:

```yaml
definition: [[Cold Weather Heater]]
usage: option
```

The same heater could be required elsewhere:

```yaml
definition: [[Cold Weather Heater]]
usage: standard
```

This prevents product-specific usage semantics from contaminating reusable definitions.

### Layer 3 — configuration resolution

The base reusable architecture should remain unresolved. Selecting a variant or excluding an option for exploration must not rewrite the assembly's Local Model.

Workbench therefore needs two configuration states:

1. **temporary configuration state** — selections held in Workbench memory while an engineer explores;
2. **persisted named configuration** — a future native Markdown artifact that records selections separately from the base architecture.

A persisted selection identifies the local configurable position by its stable native block link, for example:

```markdown
- occurrence: [[Industrial Charger#^part-power-module|Power Module]]
- definition: [[48–96 V Power Module]]
```

An omitted option is explicit:

```markdown
- occurrence: [[Industrial Charger#^part-cold-weather-heater|Cold Weather Heater]]
- present: false
```

No entry is **unresolved**, not absent. A completed configuration resolves every `variant` and explicitly includes or excludes every `option`.

The exact persisted-configuration document/schema is deliberately not frozen by W-314. It must be decided before Workbench writes named configurations. That design must remain native Markdown and must not become a second database.

### Applicability beyond parts

The semantics are intentionally general:

- **part occurrence** — choose which reusable Object/assembly fills a structural position;
- **endpoint/Port occurrence** — choose which reusable Port/interface definition fills an interface position;
- **Function occurrence** — choose which reusable Function specialization fills a behavioral position;
- **Use Case occurrence** — choose which reusable Use Case specialization applies in a scenario position;
- **State occurrence** — choose which reusable State specialization fills a state-context position.

This does **not** require all five occurrence record kinds to exist now. The Local Model should gain a new occurrence kind only when that kind is independently valuable for engineering traceability/context. Configurability alone is not sufficient reason to invent one.

Do not automatically put `usage` on connections, flows, transitions or topology. If a part or endpoint is absent in a configuration, topology involving that occurrence is naturally filtered from the configured view. If later evidence shows a connection itself must vary independently of its endpoint selections, model that case explicitly rather than pre-building a generalized topology-variation language.

### Relationship to existing semantics

These concepts must remain distinct:

- `subtypeOf` — reusable definition-level "kind of";
- `definition` — local occurrence references reusable engineering meaning;
- `usage: variant` — contextual required selection from a reusable specialization family;
- `usage: option` — contextual position may be omitted;
- Use Case `optionOf` — existing note-level Use Case semantic relationship; not Local Model optionality;
- EA `Usage` connector — source connector semantics; never interpreted as Local Model `usage` merely because the word is the same.

A definition having subtypes does **not** make every occurrence of it a variant. Variant/option semantics must be explicit or deterministically supported by source evidence.

### Base-model/schema impact

W-314 settles the semantics but does not silently change the currently deployed schemas.

Expected implementation work:

1. advance `local-model.yaml` from schema 0.1 to 0.2;
2. add optional `usage` to the occurrence records that are currently supported for configuration, beginning with part and endpoint occurrences;
3. default omitted `usage` to `standard`;
4. do not add `usage` to connection or flow records;
5. update the managed-region marker to `schema=0.2` when the schema implementation lands;
6. add optional definition-level `abstract` support to the element/property schema and write its property definition;
7. leave `relationships.yaml` unchanged;
8. preserve backward/read compatibility deliberately rather than silently interpreting 0.1 content as 0.2 when unsafe.

No new top-level Variant, Variant Point, Option, Configuration Position, or configuration relationship type is required by this design.

### Importer impact

The importer must preserve the same semantic boundary.

It must **not**:

- infer `usage: variant` solely because the reusable definition has `subtypeOf` descendants;
- infer `usage: option` from an EA Use Case `optionOf` relationship;
- equate an EA connector named `Usage` with Local Model `usage`;
- attach optional/variant meaning to the reusable definition when the meaning belongs to one local occurrence;
- connect an owning assembly to every candidate specialization.

Until a deterministic EA source rule is approved, imported local occurrences default to `standard` by omission. Any source evidence that appears to encode true configurability should be preserved for review rather than guessed.

### Workbench impact

Workbench's eventual configuration behavior is a view/editor over this native model, not a second model.

Required capabilities, in dependency order:

1. parse/index the Local Model and preserve stable local block identities;
2. read `usage` and definition-level `abstract`;
3. traverse incoming `subtypeOf` relationships transitively to derive candidate descendants because `subtypeOf` is authored specific → general;
4. reject abstract effective definitions;
5. expose read-only variation information before adding editing;
6. provide configuration mode with dropdown selection for `variant` and include/exclude behavior for `option`;
7. hold unsaved selections in session state without mutating the base Local Model;
8. define and then support a native Markdown persisted-configuration format;
9. generate configured architecture, variation-space, configuration-comparison and configuration-filtered Canvas views from the same authoritative model;
10. add product-specific model-number encoding/decoding only after configuration semantics work independently.

Useful validation findings include:

- `standard` occurrence references an abstract definition;
- configured `variant` has no selection;
- selected definition is outside the root specialization family;
- selected definition is abstract;
- abstract family root has no concrete descendants;
- configured `option` lacks explicit present/absent state in a completed configuration;
- a stored selection becomes invalid after the reusable specialization hierarchy changes.

The last case must become a finding. Workbench must never silently substitute a different candidate.

### Theory summary

The mechanism scales because each concern has one home:

```text
Reusable definition hierarchy
        │
        │ definition / specialization family
        ▼
Contextual Local Model position
        │
        │ usage = standard | variant | option
        ▼
Configuration resolution
        │
        ├─ temporary Workbench selection
        └─ persisted named configuration
```

This allows reusable engineering definitions, product architecture, product variants/options and later commercial configuration rules to coexist without duplicating definitions or overloading relationships.

A later user-facing procedure should explain how engineers create and resolve these positions through Workbench. That procedure is intentionally deferred until the underlying schema and Workbench interaction are implemented and tested.
