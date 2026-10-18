# Pass 7 — Mac pilot preflight execution and diagnostic correction

On 2026-10-17, the user performed a successful `git pull --ff-only origin main`, ran `python3 -m unittest -v 15_Testing/test_sysml2_pilot_preflight.py` (4/4 passed, zero failures), then executed `python3 15_Testing/sysml2_pilot_preflight.py`. Report: `status=MISSING_DEPENDENCY`, `javaAvailable=false`, `jupyterAvailable=false`, `sysmlKernelRegistered=false`, `nativeCertified=false`.

**Qualification:** At that revision the tool short-circuited whenever Java or Jupyter was missing, leaving both Boolean fields false. Thus those results do **not** prove both packages were missing. Updated the probe to check availability independently (commit 8fda735), and added two synthetic tests (commit 42aefd3). These changes are committed but have **not yet** been executed on the user's Mac.

Next Mac commands after pulling main:

```sh
python3 -m unittest -v 15_Testing/test_sysml2_pilot_preflight.py
python3 15_Testing/sysml2_pilot_preflight.py
command -v java; java -version
command -v jupyter; jupyter --version
```

A detected Java binary is not proof of Java >=21. The Jupyter kernelspec and an actual parser acceptance/rejection run remain separate gates. Do not install system-wide packages without environment compatibility review; this user's Mac runs an older macOS release. No native model data committed. Native emission remains disabled.
