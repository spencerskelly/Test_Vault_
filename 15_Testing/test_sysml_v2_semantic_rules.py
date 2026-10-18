"""Synthetic contract checks for provisional v2 ruleset; no model data."""
import json
import pathlib
import unittest
RULES=pathlib.Path(__file__).resolve().parents[1]/"14_Workbench/registry/sysml_v2_semantic_rules.v0.1.json"
class RulesetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(RULES.read_text(encoding="utf-8"))
    def test_nonrelease_and_fail_closed(self):
        self.assertFalse(self.data["automaticNativeEmission"])
        self.assertEqual(self.data["defaultDisposition"],"deferred_review")
        self.assertIn("not_parser_verified",self.data["releaseStatus"])
    def test_unique_rule_selectors(self):
        keys=[(x["eaType"],x["stereotype"]) for x in self.data["elementRules"]]
        families=[x["family"] for x in self.data["relationshipRules"]]
        self.assertEqual(len(keys),len(set(keys)))
        self.assertEqual(len(families),len(set(families)))
    def test_port_distinctions_not_collapsed(self):
        ports=[x for x in self.data["elementRules"] if x["eaType"]=="Port"]
        self.assertEqual({x["stereotype"] for x in ports},{"proxy","full"})
        self.assertEqual({x["target"] for x in ports},{"PortUsage","PartUsage"})
    def test_relationships_not_accepted_without_evidence(self):
        self.assertTrue(all(r["emission"]=="deferred_pending_evidence_and_parser" for r in self.data["relationshipRules"]))
    def test_workbench_and_provenance_obligations(self):
        self.assertTrue(self.data["workbenchContract"]["mustPreserveDistinctKinds"])
        self.assertIn("source_guid",self.data["provenance"])
if __name__=="__main__":unittest.main()
