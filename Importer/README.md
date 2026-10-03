# Importer

Long-lived development area for the EA → MDSE importer.

## Folder intent
- **Definition/** — current importer contract and behavior definition.
- **Tools/** — executable importer revisions. Each revision has its own version folder; the candidate version is named by the release manifest.
- **Testing/** — source evidence, import evidence, benchmarks and files actively used to validate a candidate.
- **History/** — superseded importer revisions and earlier translator work. History is evidence only and may not generate a current model.

Normal work occurs on `main`. New versions are folders, not long-lived branches.
