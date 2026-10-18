# Step 18 — Controlled document registry application rehearsal

**Status: ISOLATED CANDIDATE ONLY. Document classifications are unapproved; not a release or a public-main merge.**
**Source:** Step 17 PR #34, commit `72fd3ef25d882f3e304b14ae36f126fa2d812c16`.

## Scope and exact rollback

The candidate inserts the 32 Step 17 rows directly after `documents:` in `Base Vault/Definition/mdse-release.yaml`. Exactly **29 entries remain `reference` and 3 remain `proposal`**. No `current`, `historical`, `superseded` or `retired` status is added. Each candidate item still has `PENDING_DOCUMENT_CONTROL_APPROVAL` in `step17_registry_proposal.json`. This is a review candidate and cannot be used as a document-control signoff.

- Previous manifest Git blob: `29a05fc71c2f25108f07927870ac5d3d3bdd618b`.
- Exact candidate manifest Git blob: `6d06db25ed50ff390460c567b8fa769981aacc9e`.
- The `step18_registry_candidate.py` checker verifies full candidate SHA, each source note SHA, the exact 32-row insertion, no changed existing registry paths and zero unregistered top-level Markdown after the candidate.
- Removing exactly those 32 anchored rows reproduces the previous manifest byte-for-byte. Its current old handoff/reconciliation and Step 13 successor proposal remain as they were; no W decision has been approved.
- Legacy Step 13–17 regression tests may use the *exactly recovered previous manifest* to prove original promises and governance states are still intact. Any non-row manifest edit invalidates recovery and fails all such tests.

## Verification meaning

The branch-only CI must rerun the entire unmodified `Base Vault/Testing/check-release.py --workbench 55_Workbench` script. **Zero native FAILs** are required to establish that the 32 registration errors were closed without revealing new release failures. Existing pre-release WARNs may remain and explicitly do not indicate issued release. Check the actual run before citing its outcome.

The CI also reruns the latest Step 13/14/15/17 registry/provenance tests, Step 16 guide and Workbench version tests, and the eight historical CI definition preservation checks. The QEAX ZIP is excluded from the runner working tree; no model content should be accessed.

## Not changed, accepted, or authorized

- No modification of the generated plugin lock, Workbench source, Importer, Bootstrap, Local Model schema, released runtime payload, or original W decision log.
- No assignment of a new W identifier; Step 15 governance register still contains twelve unapproved gates.
- No permission to merge draft PRs to `Test_Vault_/main`, rewrite public model history, archive the standalone `MDSE_Workbench` repository or activate a Local Model 0.6 writer.
- Real user Obsidian Mac/Windows GUI acceptance and contributor local clone/stash/worktree audit remain pending.
- Native-checker zero FAIL only verifies the tested source/check scope, not the issue of QEAX data classification, a signed issued release, or actual generated-vault GUI behavior.

**Next bounded step:** document-control owner reviews the candidate classifications and remaining pre-release warnings; separately verify the disposable generated Base Vault guide/plugin payload and readiness for manual Obsidian GUI testing, without promoting public main.
