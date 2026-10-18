# Phase 9 — Nested definition canonical Workbench contract

Added five Node.js synthetic assertions using the **existing** canonical graph validator. Both a lexical nesting edge and a subtype-to-supertype edge remain distinct, no PartUsage is invented, source provenance remains attached, and owner recursion is rejected. New GitHub CI workflow exercises this fixture on changes and manual dispatch.

This fixture represents Workbench **review semantics**, not an approved native SysML v2 translation. `relationships` is test metadata here; the canonical `validateGraph` method currently validates nodes and their owner IDs, **not the sample relationships array**. A production relationship validator with edge role, cycle, endpoint compatibility, native semantic checks and provenance is still required.

The official kernel fixture workflow was previously updated with two new nested native syntax fixtures but is **manual-dispatch only**. Its new jobs have not been observed passing; the existing parser baseline cannot be claimed as validating these new cases. GitHub connector currently exposes read-only workflow job results for known run IDs, not a workflow-dispatch action.

Mac test:

```sh
git pull --ff-only origin main
node --test 15_Testing/test_phase9_nested_definition_workbench_contract.mjs
```

For syntax verification, manually dispatch the [Native SysML v2 pilot fixture gate](https://github.com/spencerskelly/Test_Vault_/actions/workflows/sysml2-native-fixtures.yml) and inspect `Validate nested definition specialization of lexical owner` and `Validate contrast between nested usage and definition`.

Workbench: structural view keeps lexical parent hierarchy and generalization independently; visual view shows subtype→supertype without implying composition; navigate both endpoints and local EA records; preserve per-edge validation status and round-trip origin. Binding Port and ports-as-parts remain distinguishable. Native emitter disabled. No private QEAX rows committed.