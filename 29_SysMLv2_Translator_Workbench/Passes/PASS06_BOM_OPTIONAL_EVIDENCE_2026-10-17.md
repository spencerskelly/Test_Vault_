# Pass 6 — Optional BOM evidence

The read-only XLSX adapter now supports the original four mandatory mapped fields plus optional part_revision, parent_revision, variant_of, configuration, effectivity_start, effectivity_end, bom_revision and alternate_group. These are copied as **raw source evidence**, not accepted SysML v2 specialization, assembly containment, alternates, or resolved effectivity.

Changes: `15_Testing/bom_xlsx_reader.py` commit `ebb343a` and three synthetic tests in `15_Testing/test_bom_xlsx_optional_fields.py` commit `742c422`. Tests verify preserved variant/revision/alternate strings and provenance, compatibility with the original four fields, and rejection of unknown mapped fields. The exact test suite is committed, **not verified executed** in a complete checkout. No proprietary workbook rows were committed.

Additional model rules remain to implement: BOM-specific revision history, effectivity interpretation, distinction of variantOf candidate vs actual subtypeOf, assembly-defined where-used/quantity/units, alternate assembly choices, stable source-row identity independent of display order, and cross-source provenance. Do not merge EA and BOM records by matching names or part numbers without explicit reconciled evidence. Next pass should execute tests, review and add streaming for large XLSX, and produce local-only actual workbook aggregate findings.
