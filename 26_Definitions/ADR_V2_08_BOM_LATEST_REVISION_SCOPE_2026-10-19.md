# ADR-V2-08 — BOM scope: latest product revisions only

Date: 2026-10-19. Status: **ACCEPTED by owner** ("we're only concerned with the latest products right now").

## Decision

1. The vault holds **only the latest revision of each product** in scope. Superseded revisions stay in the PLM system of record and are not imported.
2. One note per part number (PN). A part's properties come from its latest revision. Revision history is not a set of notes.
3. A usage (parent → child line) records the **child revision pinned by the latest parent revision**. The pinned revision is read from the same export row (`Child CL1`, `Child CL2`).
4. Any PN whose latest revision cannot be determined from the export is reported and not imported. It is never guessed.

## Consequences

- Revision strings are stored exactly as exported (`-N99`, `-0 99`, `C04`, `A02`); they are not normalised.
- Redline exports (struck-out values) are treated as a change set against the latest revision, not as separate history. The unstruck text is current; struck text is kept only as a `previousValue` on that revision's `## Source` section.
- Parent PN + line number identifies a usage. Line numbers are never used positionally.
- Alternate-part rows (blank PN) attach as additional sources to the PN above them. They are not parts in their own right.

## Out of scope for now

- Historical revisions and their effectivity dates.
- Drawing-only lines (e.g. `01141-91 DWG …`, amount 0): recorded as document references, excluded from quantities.

## Open

- Whether "latest" is per PN or per top-level product family when a child PN's latest revision differs between parents. Recommendation: per PN; if parents pin different child revisions, report the conflict.
