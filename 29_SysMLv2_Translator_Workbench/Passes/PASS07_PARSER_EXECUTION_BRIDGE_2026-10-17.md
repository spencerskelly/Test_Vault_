# Native SysML v2 parser execution bridge — first increment

Date: 2026-10-17. Official pilot release: https://github.com/Systems-Modeling/SysML-v2-Release/releases . Its latest 2026-08 installation instructions require an environment-specific installation; do not assume a command-line parser binary exists.

Added `15_Testing/sysml2_parser_runner.py` for an explicitly configured external executable command with exactly one `{fixture}` argument substitution, subprocess timeout and status `ACCEPTED`, `REJECTED`, or `TIMEOUT`. Records SHA-256 of the exact fixture and only the process name/exit code; suppresses captured stdout/stderr from reports because diagnostics may expose private source. Importantly this is only process-level acceptance, not validated SysML semantics. `nativeCertified` remains false.

Four synthetic tests are in `15_Testing/test_sysml2_parser_runner.py`; they exercise a dummy Python interpreter process, not an actual SysML parser. No independent parser has been executed so far. The parser launch command must be established from official pilot documentation after choosing a compatible installation, and its version recorded with the existing `sysml2_parser_attestation.py` schema.

Mac synthetic check (from repository root): `python3 -m unittest discover -s 15_Testing -p 'test_sysml2_parser_*.py' -v`. This should run attestation and runner tests; success remains pending actual user/local execution.

Next: choose the pilot installation method, explicitly identify its validation command, parse the synthetic part definition/usage fixture in `29_SysMLv2_Translator_Workbench/Fixtures`, capture exit status and parser version, introduce negative syntax fixture, and integrate independent semantic checks before native emission. Keep QEAX, BOM and private ledgers local. Pass 6 source validation not the same as SysML v2 parser qualification.
