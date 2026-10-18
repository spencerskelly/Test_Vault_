# Pass 7 — macOS Java launcher detection correction (2026-10-17)

User executed six preflight unit tests successfully, but reported preflight `javaAvailable=true`, `jupyterAvailable=false`, and manual `java -version` emitted `Unable to locate a Java Runtime.` The `java` command was present only as the macOS launcher stub; `jupyter` was not found. This exposed a false-positive in the previous `shutil.which('java')` check.

Corrected `15_Testing/sysml2_pilot_preflight.py` to execute `java -version` read-only, require a successful process and parseable Java major version >=21, and distinguish `javaCommandPresent` from `javaAvailable`. It continues to probe Jupyter presence independently and never certifies native semantics. Added tests for the macOS launcher stub, legacy Java 8, and Java 21, retaining previous Jupyter/kernel tests.

The revised tests have been committed but **have not yet been executed on the user's Mac**. Recommended commands from the repository root:

```sh
git pull --ff-only origin main
python3 -m unittest -v 15_Testing/test_sysml2_pilot_preflight.py
python3 15_Testing/sysml2_pilot_preflight.py
```

Prefer a Linux GitHub Actions validation environment over system-wide installations on this older Mac. Parser/kernel must still actually execute the positive and negative synthetic `.sysml` fixtures before any native conformance claim. No private model data committed. `nativeCertified=0`.
