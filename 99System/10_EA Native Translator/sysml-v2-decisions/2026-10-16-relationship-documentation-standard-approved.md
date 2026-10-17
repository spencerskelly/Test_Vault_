# APPROVED — Relationship Documentation Standard
Date: 2026-10-16
Status: APPROVED

## Rationale
If the reviewing engineering lead needed further explanation, future engineers and model authors will too. Every native SysML v2 relationship must have enough plain-language explanation to teach correct use, not only formal definitions or syntax fragments.

## Mandatory coverage per relationship
1. Official name and normative technical meaning; mention KerML vs SysML v2.
2. One-sentence meaning in ordinary language; then more thorough intuitive explanation.
3. What the relationship DOES NOT mean, with comparisons to likely confused relationships.
4. Valid endpoint categories, direction, owner/context, constraints.
5. At least one practical industrial-charger example and one counterexample.
6. Native v2 syntax, reference to specification, parser-validation status clearly marked.
7. Impact on modeled identity, ownership, typing, reuse and multiplicity, where relevant.
8. Structural tree behavior and visual diagram notation; clearly mark proposed Workbench conventions vs normative symbols.
9. Editing workflow: text ↔ structure ↔ diagram, authoritative note changes and validation.
10. EA import mapping status (mapped by rule / supported but not currently mapped / unresolved), plus current decision status.
11. Common authoring mistakes, diagnostic messages and correction guidance.
12. Cross-links to adjacent concepts and a succinct decision criterion ("use when…").
Documentation should be maintained as a browsable vault guide, not merely a terse decision ledger. Prior approved relationships will be expanded to this level; the current short decisions remain valid in the meantime.

## Architecture
The native SysML v2 syntax in notes is authoritative. The Workbench's structural and visual projections edit that syntax. One reusable definition for each distinct type, usages live in owning notes and generally do not require their own Markdown notes. EA is a migration source, not enduring authority.
