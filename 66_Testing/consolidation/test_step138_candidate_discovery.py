#!/usr/bin/env python3
"""Regression checks for bounded, read-only QEAX candidate discovery."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("step136_discover_qeax_vault_candidates.py")
REVIEW = Path("99_System/11_Import/Review - Equals Direction.csv")
MAP = Path("99_System/11_Import/Local Model Source Map.csv")

class CandidateDiscoveryTests(unittest.TestCase):
    def test_depth_boundary_and_vault(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "shallow.qeax").write_bytes(b"qeax")
            (root / "child").mkdir()
            (root / "child" / "boundary.qea").write_bytes(b"qea")
            (root / "child" / "deep").mkdir()
            (root / "child" / "deep" / "excluded.qeax").write_bytes(b"deep")
            vault = root / "vault"
            for p in (REVIEW, MAP):
                path = vault / p
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("header\n", encoding="utf-8")
            result = subprocess.run([sys.executable, str(SCRIPT), str(root), "--max-depth", "1"],
                                    text=True, capture_output=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(result.stdout)
            sources = {Path(x["path"]).name for x in data["sources"]}
            self.assertEqual(sources, {"shallow.qeax", "boundary.qea"})
            self.assertEqual(len(data["candidate_vaults"]), 1)
            self.assertFalse(data["pairing_verified"])

    def test_missing_root_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, str(SCRIPT), str(Path(tmp) / "absent")],
                                    text=True, capture_output=True, check=False)
            self.assertEqual(result.returncode, 2)
            self.assertTrue(json.loads(result.stdout)["errors"])

if __name__ == "__main__":
    unittest.main()
