"""Fail-closed Step120 runner regressions; all fixtures are disposable."""
import json
import sqlite3
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

RUNNER = Path(__file__).with_name("step120_real_qeax_operator_gate.py")

class OperatorGateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.results = self.root / "results"
        self.qeax = self.root / "source.qeax"
        self.vault = self.root / "vault"

    def run_gate(self, *extra):
        result = subprocess.run([sys.executable, str(RUNNER), "--qeax", str(self.qeax),
            "--vault", str(self.vault), "--results", str(self.results), *extra],
            capture_output=True, text=True)
        report = json.loads((self.results / "qeax_imp011_acceptance.json").read_text())
        return result, report

    def test_missing_inputs_fail_and_report(self):
        result, report = self.run_gate()
        self.assertEqual(2, result.returncode)
        self.assertEqual("FAIL", report["result"])
        self.assertTrue(report["failures"])
        self.assertEqual([], report["checks"])

    def test_invalid_sqlite_fails_without_running_validators(self):
        self.qeax.write_bytes(b"not sqlite")
        result, report = self.run_gate()
        self.assertEqual(2, result.returncode)
        self.assertTrue(any("QEAX database error" in e for e in report["failures"]))
        self.assertEqual([], report["checks"])

    def test_valid_sqlite_wrong_binding_count_rejected(self):
        with sqlite3.connect(self.qeax) as db:
            db.execute("CREATE TABLE t_connector(Connector_Type TEXT, Stereotype TEXT)")
        result, report = self.run_gate()
        self.assertEqual(2, result.returncode)
        self.assertEqual(0, report["binding_connector_count"])
        self.assertEqual("FAIL", report["result"])

    def test_invalid_zip_fails_and_reports_hash(self):
        self.qeax.write_bytes(b"not sqlite")
        z = self.root / "bad.zip"
        z.write_bytes(b"not zip")
        result, report = self.run_gate("--source-zip", str(z))
        self.assertEqual(2, result.returncode)
        self.assertTrue(any("ZIP validation error" in e for e in report["failures"]))
        self.assertIn(str(z), report["files"])
        self.assertEqual(64, len(report["files"][str(z)]["sha256"]))

if __name__ == "__main__":
    unittest.main()
