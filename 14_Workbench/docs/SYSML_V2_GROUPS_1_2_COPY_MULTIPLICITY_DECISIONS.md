# Group 1/2 approval and v1 Copy / part multiplicity mapping
Date: 2026-10-17
Status: Approved policies; implementation and exact source-data audit pending.
Normative baseline: OMG SysML v2.0 and KerML 1.0.

## Group 1 approved
Native namespace membership, imports, alias memberships, feature chaining, typed metadata application, documentation/comments, typed feature values, and multiplicity restrictions. Model membership, alias, and annotations as distinct native constructs (not generic edges).

### EA v1 Copy -> v2 Alias plus note consolidation
User-approved intent: map an EA v1 Copy to native v2 alias, consolidate *one canonical Markdown note*, and merge source relationships and content into that note.
Critical semantic guard: native AliasMembership makes another name for the **same model element**. An EA Copy is not necessarily identical in semantics or content. Before consolidation confirm source-copy identity and compatibility; unresolved collisions/independent ownership/different meaningful definitions are flagged instead of silently conflated. Preserve each original EA element GUID, notes, tags, outgoing/incoming connector identities, original endpoint roles and provenance in canonical note/source ledger. Deduplicate truly equivalent native relationships by semantic identity with many-source trace links; do not silently sum, discard, or conflate incompatible relationships. Alias labels and source locations remain navigable.
EA importer work: source copy chain resolver; cycle detection; identity reconciliation; content section merging with conflict markers; connector remapping to canonical ID; idempotency; record one-to-many source-to-target provenance. Workbench: alias redirects to canonical note, aliases searchable, all merged relationships queryable, show original source metadata. BOM: canonical part identity remains stable; copies do not create new BOM parts or erase revision-specific BOM evidence.

### Multiplicity from part relationship
EA importer reads explicit multiplicity from the **part/aggregation/composition connector end** (correct owner/end orientation), maps to native multiplicity on the resulting part usage when valid. Multiplicity describes cardinality, NOT necessarily a BOM quantity with UOM; keep earlier quantity/unit rules distinct, retain source values and flags for malformed or unspecified multiplicity. BOM transformer gets multiplicity/quantity/UOM from its authoritative parent assembly BOM lines in accordance with previous decisions and reconciles with EA connector-end values without blind overwrite.

## Group 2 approved as native modeling capabilities, translation deferred
- KerML Unioning: owning type classifies values classified by any listed types (type union).
- KerML Intersecting: owning type classifies values classified by all listed types.
- KerML Differencing: owning type classifies values classified by first listed type and none of subsequently listed types.
These are TYPE relationships, not generic 'union of feature lists' or a BOM set operation. Verify exact typing, ownership and grammar before implementation.
- Advanced feature membership semantics and related valid KerML expressions: require individually named, normative definition entries with eligible contexts, ownership and visibility; no generic unspecified 'advanced' editor.
No inferred EA/BOM mappings until specific source constructs and conformance rules separately approved. Support native Workbench creation via typed contextual operation and help panel, distinct from arbitrary connectors.

## Group 2 definition management requirements
Each of Unioning, Intersecting, Differencing and subsequently enumerated feature membership operations gets vault-local machine-readable rule plus Markdown definition:
canonical metaclass, exact short meaning, set/type-classification interpretation, eligible source and target, ownership, native notation (conformance-checked), differences vs Specialization/Subsetting/Redefinition/Disjoining, examples/nonexamples, EA/BOM non-inference rules, Workbench editing/rendering, validation constraints, normative reference, provenance, implementation status and follow-up.
Definitions menu uses same registry as translator/editor; all help displayed in-place; searchable, comparable, collapsible. No claim of complete native coverage from a grouped policy.

## Follow-up register
GRP-01 enumerate and validate all Group 1 metaclasses and normative v2.0 examples.
COPY-01 inventory source EA Copy relationships and duplicated objects, classify same-identity vs meaningful divergence.
COPY-02 implement safe canonicalization, merged notes/relationships, alias redirects, provenance and collision review.
COPY-03 EA + BOM import order, where-used, original GUID and duplicate connector test fixtures.
MULT-01 identify EA connector-end multiplicity storage and orientation, verify across actual source export.
MULT-02 reconcile multiplicity vs BOM quantity/unit and preserve source-level conflicts.
GRP2-01 separate detailed reference entries for Unioning, Intersecting, Differencing.
GRP2-02 audit other advanced feature membership kinds and create specific reference entries.
GRP2-03 Workbench eligibility queries, native edit/preview and per-type visualization filters.
GRP2-04 native parser/semantic tests and no inferred EA/BOM translation tests.
GRP3-01 review variation/variant semantics individually against MDSE product families and BOM variantOf.
GRP3-02 separately review causation/occurrence semantics and analysis/trade-study operations.

## Status note
Group 1/2 APPROVED for native support; Group 3 not yet approved.
