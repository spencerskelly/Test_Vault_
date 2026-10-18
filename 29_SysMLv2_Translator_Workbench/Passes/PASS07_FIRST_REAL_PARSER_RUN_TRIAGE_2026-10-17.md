# Pass 7 — First official parser CI run triage

Run: https://github.com/spencerskelly/Test_Vault_/actions/runs/39098371901/job/117589403003

Confirmed completed results: checkout PASSED; Java 21 setup PASSED; Conda setup PASSED; official SysML Jupyter kernel installation PASSED; positive fixture step FAILED; negative fixture step SKIPPED. Job log emitted status `REJECTED` for synthetic part definition/usage fixture (SHA256 `6c1c8ab627bdf814a6b85d0140e62a6de8f8c5cc691e2cfb0ca7884cb373f130`). The failure currently does not distinguish genuine SysML parse rejection from adapter protocol interpretation. In particular the old adapter treats any stream text containing `Error` as a failure, which is not sufficiently specific.

Commit `0daa666` adds aggregate-only diagnostic fields: counts of Jupyter IOPub message kinds, stream keyword hit count, whether a protocol error occurred, idle seen, shell reply type and status. It does not publish diagnostic text or any source rows. No native acceptance has been established; `nativeCertified=false`.

Next operator action: rerun the manual `sysml2-native-fixtures.yml` workflow on main and share run URL; inspect `diagnosticSummary` from the valid fixture. Then update the gate to require positive parse acceptance plus actual negative fixture rejection using authoritative native diagnostic evidence rather than guessing from text. The parser environment itself is available in Linux CI; no Mac installation needed.
