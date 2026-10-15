# Step 85 — Atomic Step22-to-main integration sequence (2026-10-14)

Status: **read-only source/config inventory; no promotion performed**.

## Direct ref evidence

| Required input | main / PR42 (main-based) | Frozen Step22 |
|---|---|---|
| `55_Workbench/package.json` | absent | `2d4607eaf1ceaf0d2a822b3f75c957795de603a5` |
| `55_Workbench/src/core/localmodel.ts` | absent | `f7fd4d43bafb57f8b4b706689f4cf8d03bc1971c` |
| `66_Testing/check_importer_workbench_localmodel.py` | absent | `95c29b377ad8c7a0596e1c164db2e6bb66168b52` |
| `Base Vault/Definition/mdse-release.yaml` | `a1692487d555f20ae08c7595f7eea5902f391619` | `6d06db25ed50ff390460c567b8fa769981aacc9e` |
| `99_System/03_Schemas/local-model.yaml` | `04b8592d9faef48aa1c952747a26e1ee917e8b58` (**0.2**) | `361dee8269f9fbdfd16bcee33a1b808015f7ba5a` (**0.5**) |
| `.obsidian/plugin-lock.yaml` | `2039b5ddda42ed8d6f08b00c987f05d775671f0e` | `c430670577318457972a154012d08c6d28e6d11b` |

Main-based PR42 currently shares the above same inputs/blobs as main. It is a standalone lean CI proposal, NOT the full source integration destination.

## Atomic and approval-gated migration plan

1. Freeze main, PR42, Step22, and PR43 tip identities; inventory preservation/gov approvals and exact changed paths before proposing a main integration PR.
2. Select **one new reviewed integration branch based on current main**. Do not directly turn PR43 (validation-only) into a release PR.
3. Stage the source tree and historical Git ancestry from Step22 under `55_Workbench/`, plus required importer checker, schemas, release manifest, plugin lock and relevant Base tooling **as a single cohesive candidate**. Do not first advance manifest/schema to 0.5 on main without compatible parser/writer and acceptance.
4. Apply a curated, reviewable set of PR42 CI changes to this same integration candidate, resolving overlap with PR43 validation gates and preserving source provenance. Keep PR42 independent while its base is unchanged.
5. Add Step82/83 positive and negative compatibility checks on this candidate only after all required inputs are present; use strict missing-input failures, not skips.
6. Run exact-source, historic ancestry, schema/release/lock consistency, importer tests, Workbench deterministic build/controlled artifact integrity, and Base/bootstrap checks. Record expected historical/new-candidate bundle difference; require separate release review.
7. Capture real-QEAX import, macOS/Windows Obsidian GUI and manual owner/reviewer approval. Synthetic/Linux CI cannot substitute for these.
8. Merge **only explicitly approved** reviewed candidate to main after all merge-tip checks; verify committed contents on main and retain durable historic refs.
9. Retire temporary historical branches/PRs only after no open dependency, exact tip+tag preservation, and per-branch owner approval.

## Critical cutover principle

A green PR43 proves its validation state, not main readiness. Main currently governs Local Model 0.2 and has no Workbench source; Step22 governs 0.5 with Workbench parser/writer. Treat this as one **atomic semantic authority migration** to avoid unsupported mixed versions.

## Next Step86

Build a path-scope and collision manifest across main/Step22/PR42/PR43 for the atomic candidate (read-only comparison, not new source merge). Classify safe additions versus governed file conflicts. Then prepare reviewer-ready handoff.

No main changes, merges, tags, branch deletions, or release/model mutations in Step85.
