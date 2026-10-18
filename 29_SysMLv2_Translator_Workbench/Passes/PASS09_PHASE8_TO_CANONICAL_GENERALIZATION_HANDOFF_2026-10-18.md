# Phase 9 — Phase 8 source-to-canonical generalization review handoff

Implemented `14_Workbench/registry/runtime/phase8-generalization-review.mjs` as a **review-only** edge preflight. Requires agreement among local ledger source PK/GUID/raw endpoint identity and a separately provided raw EA connector record, explicit `Source -> Destination`, subtype→supertype role, correct normalized endpoints, Phase 8 orientation status, and typed Definition nodes in the canonical graph. Eight synthetic Node tests added.

Important trust limitation: both the ledger and raw record are supplied by the caller; a malicious or mistaken caller could fabricate both. This does **not** read the QEAX independently, verify snapshot fingerprints, check the 14,688-row ledger manifest, or establish native SysML v2 semantic validity. The only positive result is `reviewable=true`, always with `nativeCertified=false` and `mayEmitNative=false`. No graph mutation or native emission.

Required later connection: issue a local-only per-source verification result after read-only QEAX row comparison and full manifest verification, bind it to immutable QEAX/registry/ledger hashes, and make production eligibility consume that verified result rather than merely caller-supplied strings. Reject replayed or mismatched snapshots. The existing 14,688-row Phase 8 replay passed on the operator's Mac but did not prove semantic correctness.

Workbench rule: preserve lexical ownership, definition specialization, usage typing and redefinition as distinct; visual directed subtype→supertype, explicit review status, both-end navigation and local EA provenance for round-trip. Neither binding ports nor part-as-port may be collapsed. Native emitter remains disabled.

Mac check: `git pull --ff-only origin main && node --test 15_Testing/test_phase8_generalization_review.mjs`. GitHub CI has not been updated in this pass and these tests have not yet been independently executed.