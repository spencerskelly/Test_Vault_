# Retired importers

> [!WARNING] ARCHIVED 2026-10-03 (W-326). SUPERSEDED by the current importer named in [[00 - Current State]]
> Nothing here may be used to generate a model. Kept as evidence of how the rules and the code developed.

| File | Role when current | Why retired |
|---|---|---|
| `EA_to_MDSE_Native_Importer_v0.1.html` | direct-QEAX preflight and source-count baseline (W-273) | superseded by later preflight |
| `EA_to_MDSE_Native_Importer_v0.2.html` | whole-model planner, passed on the real QEAX (W-274) | planner rebuilt in v0.8 |
| `v0.3`, `v0.4`, `v0.5`, `v0.5.1` | intermediate builds | superseded by v0.5.2 |
| `EA_to_MDSE_Native_Importer_v0.5.2.html` | accepted safety lineage and fallback (schema 1.35, release 0.5.x) | v0.8 carries its safety checks forward; it cannot produce a 0.8.0 model |
| `EA_to_MDSE_Native_Importer_v0.7.html` | occurrence/QEAX merge candidate, never accepted | v0.8 implements the governed Local Model 0.2 |
| `EA_to_MDSE_Native_Importer/v0.8.0` to `v0.8.5` | v0.8 candidates, each with its own README | superseded by v0.8.6 (W-323, W-324); v0.8.3 made the first whole-model semantic write, v0.8.5 the decode-only check |
