"""Synthetic, non-proprietary tests for the read-only QEAX table-disposition gate."""
import importlib.util
import pathlib
import sqlite3
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
MODULE = HERE / "reconcile_qeax_dispositions.py"
spec = importlib.util.spec_from_file_location("qeax_dispositions", MODULE)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

POLICY = {
    "expected": {"tables": {"t_object": 2, "t_connector": 1}},
    "tableDispositions": {
        "t_object": "imported",
        "t_connector": "imported",
        "t_taggedvalue": "ignored_must_be_empty",
        "t_connectortag": "ignored_nonempty_approved",
    },
}

class TestDispositionReconciliation(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.database = pathlib.Path(self.temp.name) / "synthetic.qeax"
        with sqlite3.connect(self.database) as db:
            for table in POLICY["tableDispositions"]:
                db.execute(f"CREATE TABLE {table} (value TEXT)")
            db.execute("INSERT INTO t_object VALUES ('synthetic')")
            db.execute("INSERT INTO t_connectortag VALUES ('approved')")

    def report(self, policy=POLICY):
        return gate.reconcile(self.database, policy)

    def test_valid_policy_passes(self):
        report = self.report()
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["issueCount"], 0)
        self.assertEqual(report["nonemptyTables"], 2)

    def test_unexpected_table_blocks(self):
        with sqlite3.connect(self.database) as db:
            db.execute("CREATE TABLE unexpected_model_data (value TEXT)")
        report = self.report()
        self.assertEqual(report["status"], "BLOCKED")
        self.assertIn("UNCLASSIFIED_TABLE", [x["category"] for x in report["issues"]])

    def test_forbidden_nonempty_blocks(self):
        with sqlite3.connect(self.database) as db:
            db.execute("INSERT INTO t_taggedvalue VALUES ('unexpected')")
        report = self.report()
        self.assertEqual(report["status"], "BLOCKED")
        self.assertIn("FORBIDDEN_NONEMPTY", [x["category"] for x in report["issues"]])

    def test_required_table_missing_blocks(self):
        with sqlite3.connect(self.database) as db:
            db.execute("DROP TABLE t_connector")
        report = self.report()
        self.assertEqual(report["status"], "BLOCKED")
        self.assertIn("EXPECTED_TABLE_MISSING", [x["category"] for x in report["issues"]])

    def test_legacy_full_count_mismatch_is_not_a_policy_error(self):
        # Table disposition is independent of historical source snapshot counts.
        self.assertEqual(self.report()["status"], "PASS")

if __name__ == "__main__":
    unittest.main()
