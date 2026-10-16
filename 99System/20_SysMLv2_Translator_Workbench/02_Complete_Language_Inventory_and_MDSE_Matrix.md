# SysML v1 / SysML v2 / MDSE language inventory and directional MDSE matrix

Date: 2026-10-15

## Companion workbook
**SysML_v1_v2_MDSE_Complete_Inventory_and_Relationship_Matrix.xlsx** is supplied as a downloadable conversation artifact pending explicit binary-file upload to this repository.

## Workbook sheets
- SysML1 Elements — 124 concepts
- SysML1 Relationships — relationship vocabulary
- SysML2 Elements — 123 SysML v2 and KerML concepts
- SysML2 Relationships — semantic relationships and memberships
- MDSE Elements — 43 working vocabulary entries
- MDSE Relationships — 20 approved, derived, optional and proposed relationship families
- MDSE From-To Matrix — directional 43×43 table; rows FROM and columns TO
- Matrix Legend and Read Me — precision about matrix statuses, assumptions, sources

## Important qualifications
1. This inventory covers a broad set of user-facing constructs and lower-level concepts; it is **not** a machine-verified exhaustive extract of all normative UML/SysML v1 and SysML v2/KerML metaclasses, abstract types and association ends. The next standards audit should extract and compare machine-readable metamodel files.
2. The MDSE matrix uses documented prior engineering-model decisions, not a freshly machine-readable extract of live repository rules. It must not yet become hard-coded validation logic.
3. A blank cell means no authorized relation is yet documented. It is not a prohibition.
4. Asterisked relations are context-dependent and often require exact subtype/instance, endpoints, ownership, and acyclic checks.
5. 'Approved', 'Proposed' and 'Derived' are separate relationship statuses; do not treat a proposed or derived inverse as editable first-class model relationship.
6. The shared EA schema remains translation-agnostic, then independent MDSE/SysML v2 translation profiles map to respective vocabularies.

## Follow-up quality gates
- Check the complete SysML 1.7 normative XMI/UML profile, SysML 2.0/KerML normative machine-readable abstract syntax against workbook row lists.
- Enumerate **all** live MDSE element classes, properties, relationships and endpoint constraints from the repository ruleset.
- Split relationship matrix into **allowed**, **forbidden**, **conditional**, **not-defined** categories and record direction, multiplicity and semantics for each.
- Reconcile the worksheet elements against EA CSV export types/stereotypes and maintain source coverage and provenance counts.
- Put approved matrix in versioned machine-readable JSON alongside a spreadsheet for review.
 
## Standards
- https://www.omg.org/spec/SysML/1.7
- https://www.omg.org/spec/SysML/2.0
- https://www.omg.org/spec/KerML/1.0
