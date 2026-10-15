# Consolidation Step 10 — Provenance-aware Workbench reference preflight

**Date:** 2026-10-10 (Pacific). **Status:** review-only candidate; not merged, released, archived or approved by governance.
**Parent:** 9d2956a574904a65d1a13d7fb21e5d83d0efabbf (Step 09).

## Scope

- Added Python reference policy that distinguishes active repo dependencies, uncertain references, exact frozen source provenance, and historical citations.
- Integrated policy into 66_Testing/check_release_alignment.py while preserving previous dependencyReferences, findings, roots, versions and non-Workbench path checks.
- Root read-only preflight workflow runs new unittest coverage and asserts that old root GitHub Actions still block readiness.
- No changes to the actual plugin lock, generator scripts, Workbench code, importer, schema, model source, or historical W decision log.

## Immutable provenance whitelist (full Git blobs, not substring exceptions)

| Tracked file | Approved historical Git blob SHA |
|---|---|
| .obsidian/plugin-lock.yaml | c430670577318457972a154012d08c6d28e6d11b |
| Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py | 74f18af673263d87d123d31056251ddbab265d4b |
| Base Vault/Tools/v0.8.0/update-plugin-lock.py | e687515dad5215781df55a3cdfcb38008b0780f4 |

Any edit to a whitelisted file invalidates the provenance exemption and becomes blocking. An executable legacy workflow under .github/workflows is always blocking, even when its original evidence is historically important. Historical W decisions and verified BOM handoffs remain intact. Unknown current documents are flagged for review.

## Interpretation

Workbench-specific strict readiness is separate from the broader release --strict mode, which also rejects pre-release status and all other pending migration warnings. A passing pre-release audit-mode workflow means the test and report ran, NOT approval of repository archival. This scan covers literal references in the local tracked checkout only; dynamic URLs, external CI, unpushed developer work, and remote-only Git history still need review.

## Outstanding gates

1. Authorized QEAX public-data classification and any required exposure response.
2. All contributor local clones/branches/stashes signed off.
3. W-decision and controlled repo cutover approved and merged into the designated authority.
4. Legacy checkout workflows reviewed and made inert with source evidence preserved.
5. Full importer/Workbench release alignment, artifact hashes, and real Obsidian first-open/edit/restart acceptance.
6. Separate explicit approval before standalone Workbench is archived read-only.

**Next bounded step:** Review and safely retire legacy Workbench checkout workflow triggers, without destroying their frozen evidence or bypassing safety and provenance checks.
