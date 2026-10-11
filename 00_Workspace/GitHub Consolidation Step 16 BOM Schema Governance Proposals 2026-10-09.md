# GitHub Consolidation — Step 16: BOM A-14 Schema Governance Proposals

**Date:** 2026-10-09 (PDT)
**Status:** **PASS — safe, isolated candidate schema contracts validated. Governance approval and release remain open.**
**Prior:** [[GitHub Consolidation Step 15 BOM Staged Source Integration 2026-10-09]]
**Review:** [Test_Vault_ draft PR #16](https://github.com/spencerskelly/Test_Vault_/pull/16)
**CI:** [Step 16 governance verification 38011837932](https://github.com/spencerskelly/Test_Vault_/actions/runs/38011837932)

## Source and change boundary

- From `integration/bom-a14-source-step15-2026-10-09` at `5d34b3898d7c0a56719435c75b2993b876fca3d6`.
- New proposal-only branch `integration/bom-governance-step16-2026-10-09`; its head at review creation was `bc1ade17f7e153d748ecd13a6d3b1d8655efd3a7`.
- Kept **actual active** `99_System/03_Schemas/local-model.yaml` (0.5 / blob `361dee8269f9fbdfd16bcee33a1b808015f7ba5a`), `relationships.yaml` (1.36 / `413fd5d32d12331413fda30653c7a3a38ac2d2ab`), `element-types.yaml` (1.18 / `3f694feadb2eafd41498aff5ebc24946b9715f6d`) and `Base Vault/Definition/mdse-release.yaml` (pre-release / blob `ce556ade56b5bd9650ccc659f1b41bf2ca411c10`) **byte-for-byte unchanged**. Those pinned SHA identities were proven in CI.
- None of the proposed new files is listed in the lean runtime Base copy list or loaded as the active tooling schema. No writer version change, plugin-lock regeneration, importer rewrite, or main branch merge.

## Artifacts committed on isolated Step 16 branch

1. `99_System/03_Schemas/Proposals/bom-local-model-06-readonly.yaml`: structured review contract for reading **0.6** Part occurrence `quantity` + `unitOfMeasure` with existing **0.5 writer**. Quantity/UOM are optional *together*; multiplicity counts interchangeable instances, quantity measures per instance, exact total `multiplicity × quantity` only when both factors have distinct evidence. Reader unit codes `ea,in,m,kg` explicitly marked **provisional and ungoverned**. Does not authorize new fields in `schema=0.5`.
2. `99_System/03_Schemas/Proposals/bom-variantof-oneway.yaml`: review candidate for Object→Object optional single forward `variantOf`, with no stored inverse, no substitution for `subtypeOf`, `partOf`, `copyOf` or `supersedes`, no self/cycle/multiple/dangling links, source evidence/review threshold. Object family missing-subtype allowance **requires independent governance** and is not implicitly approved.
3. `99_System/03_Schemas/Proposals/BOM A14 Schema Reconciliation Step16.md`: comparison and release decisions; discusses post-BOM read-only schema coexistence and writer activation prerequisites, exact decimals/UOM conversions/source ledger, family subtype omission, cardinality, Ruleset intro stale version references, canonical 0.5 BindingConnector equals/exposes semantics that must not regress.
4. `66_Testing/check_bom_step16_proposals.py`: fail-closed Python/YAML checker comparing **frozen Git blobs** of canonical authorities, release manifest pins and candidate-only markers, validating field list/decimal grammar/oneWay relationship/noninverse/cycle constraints, Workbench actual source reader/writer, model fixture, and **all 31 historical artifact SHA-256 checks**.
5. `.github/workflows/bom-step16-governance.yml`: read-only CI runs the proposal checker, existing importer/source compatibility, fresh Base and existing release checker, TypeScript, BOM focused tests, full Workbench suite and production build.

## Verifiable CI result

[GitHub Actions run 38011837932](https://github.com/spencerskelly/Test_Vault_/actions/runs/38011837932) completed **SUCCESS**. Evidence in logs:

- Both candidate proposals remain `proposal-only`; governing files and release pins unchanged; 0.6 reader/0.5 writer confirmed in actual Workbench source.
- `variantOf` remains proposed (not authorized to be emitted by the governed schema); no inverse semantics added. Legacy note `subtypeOf` and Local Model `usage: variant` retain their distinct meanings.
- **31/31** original historical BOM source files pass raw Git SHA-256 checks, including recovered binary ZIPs/run log.
- Importer source-profile and Local Model compatibility: PASS. Fresh Base Vault build: PASS. Original release checker: **0 fail / 4 expected pre-release warnings**.
- BOM/cache-focused **30/30 tests pass**, full Workbench **462/462 tests pass**, TypeScript typecheck and production build pass.
- Entire check is **non-mutating**; not a new mdseRelease or issued controlled schema.

## Engineering findings and approval gates

1. **Local Model 0.6 reader is ahead of governed readable versions**: active `0.5` schema lists only 0.1–0.5. Do not reinterpret this as approved 0.6. Formal upgrade requires decision/version allocation, reader/writer semantics, UOM registry, decimal validator descriptors, exact arithmetic, source evidence, importer and editor round-trip.
2. **0.6 implementation may not perfectly preserve 0.5 BindingConnector `equals` validation**: current 0.5 has same-owner reciprocal binding and `Connection.exposes` boundary semantics. Add explicit paired 0.5/0.6 topology and definitionless Interface fixtures *before* approving any 0.6 writer.
3. **`variantOf` Workbench review-only validator is not a governed YAML authoring contract**. Active relationship 1.36 lacks it, and the proposed family Object without subtype is not authorized under element-types 1.18. Need separate W-decision(s), schema and consumer migrations, and human evidence thresholds.
4. **Ruleset 1.23 introduction still cites superseded schema versions (relationships 1.35, Local Model 0.2)** even though active schemas are 1.36 and 0.5. Fix through an independent approved Ruleset version, not a hidden update on this proposal branch.
5. Source pairing on Step 15 passed component CI but **post-BOM full pinned QEAX determinism / real-vault candidate check and Obsidian UI startup/edit/restart** have not been rerun. This is the next critical acceptance gate.
6. Existing release warnings remain: Bootstrap 0.3.0 pin versus candidate lock 0.3.1, unissued importer and clean Base release, and unarchived earlier importer executable revisions.

**Proposed next Step 17:** Rehearse the full frozen 35,969-object / 21,822-connector QEAX import against the now-persisted Step 15/16 BOM source, including deterministic replay, Local Model 0.5 topology and Workbench candidate acceptance. Keep experimental 0.6 and variantOf separate from authorized 0.5 writes; if full model CI passes, plan a separate W-governance and manual Obsidian acceptance sequence.

**No main branches changed. Original Workbench/BOM history retained; all PRs remain draft.**
