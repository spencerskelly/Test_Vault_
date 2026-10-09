# Importer

Long-lived development area for the EA → MDSE importer.

## Start here
- **Definition/Importer Operating Contract.md** — pipeline, trust boundaries, run states, invariants and release-hardening baseline.
- **Definition/Translator Definition.md** — detailed Stage-1 translation rules and links to the machine-readable mapping authorities.
- **Definition/Importer Issue Register.md** — ranked systemic correction backlog grounded in the current implementation and real imported-model evidence.

## Current candidate
- **v0.8.13** — current hardening candidate.
- v0.8.7–v0.8.11 are incremental hardening references for transaction state, run-status separation, WAL blocking, initialized destination enforcement, and source fingerprinting.
- v0.8.12 implements the W-376 canonical-vs-review relationship boundary.
- v0.8.13 implements W-377/W-378: Local Model 0.3 contextual endpoints may omit a reusable Port definition; the importer no longer manufactures Port notes solely to satisfy Local Model storage.
- Workbench PR #4 passes CI for Local Model 0.3 compatibility. A fresh schema-0.3 base plus targeted browser/real-QEAX acceptance is still required before IMP-009 or the candidate is release-conformant.

## Folder intent
- **Definition/** — current importer contract, translation behavior and correction backlog.
- **Tools/** — executable importer revisions. Each revision has its own version folder; the candidate version is named by the release manifest.
- **Testing/** — source evidence, import evidence, benchmarks and files actively used to validate a candidate.
- **History/** — superseded importer revisions and earlier translator work. History is evidence only and may not generate a current model.

Normal work occurs on `main`. New versions are folders, not long-lived branches. Short-lived review branches may be used for controlled changes before merge.
