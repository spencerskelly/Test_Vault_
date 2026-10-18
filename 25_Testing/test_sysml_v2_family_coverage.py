"""Cross-registry family coverage, fail-closed emission, and source traceability."""
import json
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
def load(path):
    return json.loads((ROOT/path).read_text(encoding="utf-8"))
class FamilyCoverage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=load("14_Workbench/registry/family_disposition_registry.v0.2.json")
        cls.target=load("14_Workbench/registry/sysml_v2_semantic_rules.v0.2.json")
    def test_complete_exact_family_set(self):
        a={x["family"] for x in self.source["families"]}
        b={x["family"] for x in self.target["relationshipRules"]}
        self.assertEqual(len(a),len(self.source["families"]))
        self.assertEqual(len(b),len(self.target["relationshipRules"]))
        self.assertEqual(a,b)
        self.assertEqual(len(a),26)
    def test_dispositions_and_rule_ids_preserved(self):
        v={x["family"]:x for x in self.target["relationshipRules"]}
        for item in self.source["families"]:
            with self.subTest(item=item["family"]):
                self.assertEqual(v[item["family"]]["sourceDisposition"],item["disposition"])
                self.assertEqual(v[item["family"]]["sourceRuleIds"],item["rule_ids"])
    def test_all_emissions_deferred(self):
        self.assertFalse(self.target["automaticNativeEmission"])
        self.assertEqual(self.target["defaultDisposition"],"deferred_review")
        for item in self.target["relationshipRules"]:
            self.assertEqual(item["emission"],"deferred_pending_evidence_and_parser")
    def test_structural_port_distinction_retained(self):
        port={x["stereotype"]:x["target"] for x in self.target["elementRules"] if x["eaType"]=="Port"}
        self.assertEqual(port,{"proxy":"PortUsage","full":"PartUsage"})
if __name__=="__main__":
    unittest.main()
