"""Validate the v2 recovery trace register against actual repository paths.

A path exists != executable, tested, parser-accepted or released.
"""
import json
import pathlib
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
MANIFEST=ROOT/"26_Definitions/v2_recovery_traceability.v0.1.json"
EXPECTED={f"V2-{i:02d}" for i in range(1,15)}

class RecoveryRegisterTest(unittest.TestCase):
    def test_schema_unique_coverage_and_local_paths(self):
        payload=json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(payload["schema"],"mdse-v2-recovery-trace/1")
        records=payload["records"]
        ids=[r["id"] for r in records]
        self.assertEqual(len(ids),len(set(ids)),"duplicate trace ID")
        self.assertEqual(set(ids),EXPECTED,"missing or unexpected trace IDs")
        referenced=set()
        for r in records:
            self.assertIn(r["phase"],("first","later"))
            self.assertEqual(r["evidence_level"],"path_inventory_unverified")
            for field in ("authority","implementation","test"):
                path=r[field]
                if path is None:
                    self.assertNotEqual(field,"authority","missing contract authority")
                    continue
                self.assertIsInstance(path,str)
                self.assertNotIn("..",pathlib.PurePosixPath(path).parts)
                self.assertTrue((ROOT/path).is_file(),f"missing {r['id']} {field}: {path}")
                referenced.add(path)
            for flag in ("native_certified","ui_accepted","release_accepted"):
                self.assertIs(r[flag],False)
        self.assertGreaterEqual(len(referenced),15)

if __name__=="__main__":
    unittest.main()
