# Branch cleanup — checkpoint BR-16

Date: 2026-10-12
Status: PARTIAL — CI probes classified, Base Vault branch contents require further review
Candidate head: consolidation/step22-single-repo-cutover-2026-10-11

## Comparisons (candidate as base)
| Branch | Branch-only commits | Candidate-only commits | Disposition |
|---|---:|---:|---|
| base-vault-2026-09-30-rel132-v04 | 1 | 2242 | HOLD; file listing truncated at 300 |
| base-vault-2026-09-30-rel133-v05 | 1 | 2232 | HOLD; file listing truncated at 300 |
| base-vault-2026-09-30-rel133-v051 | 1 | 2225 | HOLD; file listing truncated at 300 |
| ci-probe-bootstrap-031 | 3 | 1897 | HISTORICAL CI probe |
| ci-probe-bootstrap-artifact | 1 | 1896 | HISTORICAL CI probe |

## Direct source inspection
- Bootstrap/Tools/v0.3.1/CI_PROBE.md (blob 75e142e3e0af0396d5ccc412311eee471a604aec) explicitly identifies itself as temporary and says do not merge.
- Bootstrap/Tools/v0.3.1/CI_ARTIFACT_PROBE.md (blob c8714856165ace44fa0f388ff36ccf5d4816521f) explicitly identifies itself as temporary and says do not merge.
- .github/workflows/bootstrap-candidate.yml on ci-probe-bootstrap-031 (blob 57912ae1030bc0aa8bbf27358e7db7b95faaf4e1) has a trailing temporary PR probe line. Do not copy temporary variant into approved CI without diff review.

## Protection and next work
- Neither CI probe requires a bulk merge; retire only after PR, evidence, and local-unpublished-work checks.
- Keep all Base Vault branches until single exclusive commits and net tree impact have been reviewed with an untruncated comparison/diff.
- BR-15 source-doc copy remains blocked, so recovery branch remains protected; 15 original documents are NOT yet copied.
- No merge or deletion or release promotion performed.

NEXT: BR-17 — review Base Vault branch-only commits and exact delta using Git commit inspection or an approved local clone, then update deletion decision ledger.
