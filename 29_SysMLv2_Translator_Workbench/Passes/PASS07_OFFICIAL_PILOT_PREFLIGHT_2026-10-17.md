# Pass 7 — Official pilot installation preflight

The official SysML v2 Pilot Implementation is Eclipse/Xtext-based and documents an alternative Jupyter SysML kernel. The Jupyter kernel requires Java 21 or newer, a Jupyter environment, and registration of the `sysml` kernelspec. This is a verified deployment route, but a kernelspec is **not** a stand-alone CLI parser command, and registration does not establish that a fixture parses.

References:
- https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation
- https://github.com/Systems-Modeling/SysML-v2-Pilot-Implementation/blob/master/org.omg.sysml.jupyter.kernel/README.adoc
- https://github.com/Systems-Modeling/SysML-v2-Release/blob/master/install/jupyter/install.sh

Added `15_Testing/sysml2_pilot_preflight.py`: read-only checks for Java, Jupyter, and `jupyter kernelspec list --json` containing `sysml`. The JSON deliberately reports `nativeCertified: false`. Added four simulated-environment unit tests `test_sysml2_pilot_preflight.py`; these must be run on the Mac or GitHub CI before claiming success.

Mac commands (from Test_Vault_ after `git pull --ff-only origin main`):

```sh
python3 -m unittest -v 15_Testing/test_sysml2_pilot_preflight.py
python3 15_Testing/sysml2_pilot_preflight.py
java -version
jupyter kernelspec list
```

If the kernel is absent, first choose an installation matching macOS version and Java 21; do not install or upgrade packages automatically. The official release install script references Conda and may modify an existing environment; use a separate isolated environment. Next gate: capture actual kernel version and execute positive and invalid syntax fixtures via the Jupyter protocol or a verified official parser API; native semantics remain deferred.
