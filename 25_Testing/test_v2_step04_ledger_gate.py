import importlib.util
import pathlib
import unittest

P = pathlib.Path(__file__).resolve().parents[1] / "24_Workbench" / "registry" / "runtime" / "v2_step04_ledger_gate.py"
spec = importlib.util.spec_from_file_location("step04_gate", P)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def row(pk, table="t_object", disposition="native", **extras):
    obj = dict(source_system="EA", fixture_hash="abc", source_table=table,
               source_pk=pk, rule_id="R", rule_version="1", disposition=disposition,
               evidence="synthetic", target_stable_id="MDSE-"+str(pk))
    obj.update(extras)
    return obj

class TestStep04Gate(unittest.TestCase):
    def test_valid_exact_coverage(self):
        result = module.audit([row(1), row(2, "t_connector")],
                              {"t_object": 1, "t_connector": 1})
        self.assertTrue(result["passed"])
    def test_duplicate_rejected(self):
        self.assertIn("DUPLICATE_SOURCE",
                      [x["code"] for x in module.audit([row(1), row(1)])["failures"]])
    def test_untraced_native_rejected(self):
        self.assertFalse(module.audit([row(1, target_stable_id="")])["passed"])
    def test_evidence_only_requires_explanation(self):
        self.assertFalse(module.audit([row(1, disposition="evidence_only")])["passed"])
        self.assertTrue(module.audit([row(1, disposition="evidence_only",
                                           diagnostic_code="BOUNDARY_GROUPED")])["passed"])
    def test_wrong_counts_rejected(self):
        self.assertFalse(module.audit([row(1)], {"t_object": 2})["passed"])
    def test_mixed_fixture_rejected(self):
        self.assertFalse(module.audit([row(1), row(2, fixture_hash="different")])["passed"])

if __name__ == "__main__":
    unittest.main()
