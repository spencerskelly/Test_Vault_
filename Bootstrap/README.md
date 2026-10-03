# Bootstrap

Long-lived development area for MDSE Bootstrap.

## Folder intent
- **Definition/** — product behavior and setup specifications.
- **Tools/** — versioned Bootstrap source. The Base Vault release manifest identifies the active source; newer folders may be candidates.
- **Testing/** — first-open and candidate validation material.
- **History/** — retired revisions when they exist.

Current pinned runtime: **0.3.0**.
Current candidate: **0.3.1**, implementing W-330 safe activation repair. On 2026-10-03 it built successfully on the development Mac and all **9 tests passed**. The Base Vault candidate payload/lock also validated successfully.

Promotion remains blocked on integrated first-open persistence testing. Per W-337, test 0.3.1 in the next Workbench/importer-aligned integration candidate. Promotion then means first-open tests pass, 0.3.1 becomes the pinned runtime in the release manifest, the plugin lock is regenerated, and full release validation passes.
