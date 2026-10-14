# Step 76 — Durable preservation and retirement approval register (2026-10-14)

Status: **decision-ready preservation proposal; no irreversible action approved or executed.**

## Fresh exact ref-tip freeze

Fetched GitHub commit at each live branch name and compared with Step22. Every branch still exists.

| Branch | Exact tip SHA | Unique commits vs Step22 | Step22-only commits | Candidate classification |
|---|---|---:|---:|---|
| `integration/bom-a14-reconciliation-2026-10-09` | `92a466df64b485b2f396a380593cc79ff161300f` | 2 | 128 | Historical BOM rehearsal |
| `integration/importer-reconciliation-2026-10-09` | `28215a58ff4757ad833ff54a4edf67dd35f13eb0` | 6 | 644 | Historical importer rehearsal; executable checker separately preserved |
| `integration/workbench-monorepo-rehearsal-2026-10-09` | `79dac2f69f97c3ac9ae8a1735640666e4047badb` | 1 | 1806 | Historical Workbench migration rehearsal |
| `recovery/repository-consolidation-2026-10-09` | `ffca1a2b8e8fe54da2191309f52a34286ad34648` | 19 | 1804 | Historical recovery ancestry; 15 document blobs already present on Step22 |

These ancestry counts are *not* missing-file counts; no deletion is authorized solely by matching content.

## Non-executable archival candidates

Preserve these historical workflow definitions as archival text (not under `.github/workflows` in a branch used for operations):
- `.github/workflows/bom-a14-merge-rehearsal.yml` — Git blob `cdee24fbcf33fea71f1fd297208f7467539cd5bb`.
- `.github/workflows/importer-monorepo-merge-rehearsal.yml` — Git blob `612cc78ee5c839def7dae9b343ef9c2f8dd9b8d2`.
- `.github/workflows/workbench-monorepo-rehearsal.yml` — Git blob `253722a1273e9d0f30255e25299c7ec56c18684b`.

Archive plan: Copy exact contents by verified blob into `66_Testing/consolidation/Archive/Historical_Workflows/` with `.yml.txt` extension, include source branch+tip+blob+historical date and explicit DO NOT ACTIVATE notice in separate manifest. File copies preserve readable configuration, **not unique Git commit ancestry**; retaining an immutable approved tag/ref for each tip addresses ancestry while allowing branch reduction. Any tags/ref operations require owner approval and commit-level protection review.

## Preservation and deletion approval gates

1. Re-fetch each branch tip immediately before any operation and abort if SHA differs.
2. Produce a file checksum report for archived source versus original Git blob, and verify reader access from intended durable destination.
3. Determine whether the currently active CI satisfies the original rehearsal's *unique* assertions; do not assert full parity merely from green candidate CI.
4. Capture exact historic PR head/base and any still-open dependents; agree whether closed PR and CI evidence should be retained.
5. Select approved durable ancestry refs or retention mechanism and verify they resolve to original tip SHAs independently of source branch.
6. Only after an explicit owner decision naming branch and exact tip SHA, delete in small batches with post-delete ref verification; never delete main, Step22 or active PR43 as part of these historical ref batches.

## Decision status

**HOLD all four branches.** We have exact original SHAs and file-level archival source IDs. We have NOT created archival copies or tags, moved main, merged or deleted refs, or changed governed artifacts.

## Next Step 77

Create non-executable byte-preserving copies of the three workflows and a provenance manifest on the PR43 validation branch; verify identical content hashes using Git blob SHA once committed. This does not replace immutable ancestry refs. Continue requiring owner approval before tag/merge/branch deletion.
