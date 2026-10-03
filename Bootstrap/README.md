# Bootstrap

Long-lived development area for MDSE Bootstrap.

## Folder intent
- **Definition/** — product behavior and setup specifications.
- **Tools/** — versioned Bootstrap source. The Base Vault release manifest identifies the active source; newer folders may be candidates.
- **Testing/** — first-open and candidate validation material.
- **History/** — retired revisions when they exist.

Current pinned runtime: **0.3.0**.
Current candidate: **0.3.1**, implementing W-330 safe activation repair.

Promotion means: candidate build/tests pass, first-open testing passes, its built files replace the Base Vault runtime payload, the plugin lock is regenerated, and the release manifest is updated.
