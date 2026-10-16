# MDSE v2 — BOM Integration

**Status:** Proposed translation design. Source ideas: BOM Work and v1 proposed A-02, A-07 and A-12 contracts. Do not claim existing v1 proposal as approved schema.

## Model concepts
- One reusable note/definition per normalized internal part number; revisions and occurrences do not duplicate that definition.
- The *parent* assembly/configuration owns BOM usages, including counts, quantities and applicability. Where Used is a reverse query; never materialize a child-side parent inventory.
- Separate discrete multiplicity from measured quantity and units. Preserve raw values; do not guess units or double count.
- A family similarity grouping is **not** automatically SysML specialization, SysML variation, or guaranteed substitutability.
- One effective BOM per parent and selected configuration/revision. Competing simultaneous effective BOMs block automatic interpretation; historical revisions remain in source ledger.
- SysML owns structural part usages and allowed formal alternatives. BOM source ledgers retain manufacturing revisions, source row evidence and effectivity.

## BOM-ALT-001 — Alternate manufacturing part on continuation row
When a row has **blank internal Part Number** but populated **Manufacturing Part Number**, interpret it as an alternate of the preceding applicable primary BOM line **within the same parent assembly, revision, configuration and BOM group**. Consecutive matching continuation rows attach to that same primary line. Preserve manufacturer identity and source-row provenance. Do **not** count the alternate as another required child usage or increase total assembly quantity.

If there is no unambiguous preceding qualifying primary line, create a review finding and do not infer a selected part. An alternate is **not** necessarily an engineering subtype (`subtypeOf`) or a family similarity (`variantOf`). Determine whether native SysML v2 variation usage is appropriate after validating interchangeability and effectivity.

**Example:**

| Internal part | Mfg part | Qty | Interpretation |
|---|---|---:|---|
| PC-100 | MFG-100 | 2 | Primary requirement |
| *(blank)* | MFG-101 | | Alternate for PC-100, not an extra two |
| *(blank)* | MFG-102 | | Another alternate for PC-100 |
| PC-200 | MFG-200 | 1 | New primary requirement |

**Review questions:** Are manufacturing alternates independently numbered definitions or approved supplier options on a single internal part? Does substitution apply per occurrence or whole line? How do restrictions, revisions and effective dates control selection?

## Acceptance tests
- Three lines above yield **2 required PC-100 occurrences**, not 4 or 6.
- A blank primary with manufacturing number before any primary is review-only.
- An alternate cannot cross an assembly/revision/configuration/group boundary.
- Where Used shows actual parent-owned selected structure; alternate candidates can be displayed separately.
- Re-import preserves revisions and source provenance.
