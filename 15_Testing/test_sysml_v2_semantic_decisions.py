"""Cross-check approved family vocabulary against the deferred decision register."""
import json
from pathlib import Path
import unittest

REGISTRY=Path(__file__).resolve().parents[1]/"14_Workbench/registry"
def load(name):
    return json.loads((REGISTRY/name).read_text(encoding="utf-8"))

class SemanticDecisionContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source=load("family_disposition_registry.v0.2.json")
        cls.rules=load("sysml_v2_semantic_rules.v0.2.json")
        cls.decisions=load("sysml_v2_semantic_decisions.v0.1.json")

    def test_registry_versions_and_coverage(self):
        self.assertEqual(self.source["schema_version"],"0.2.0")
        self.assertEqual(self.rules["version"],"0.2.0")
        self.assertEqual(self.decisions["version"],"0.1.0")
        source={r["family"] for r in self.source["families"]}
        target={r["family"] for r in self.rules["relationshipRules"]}
        self.assertEqual(source,target)
        self.assertEqual(len(source),26)

    def test_exact_discrepancy_set(self):
        needed={r["family"] for r in self.rules["relationshipRules"]
                if r.get("existingCandidateDifference")}
        found=[r["family"] for r in self.decisions["records"]]
        self.assertEqual(len(found),len(set(found)))
        self.assertEqual(set(found),needed)
        self.assertEqual(len(found),11)

    def test_no_native_emission(self):
        self.assertFalse(self.rules["automaticNativeEmission"])
        self.assertEqual(self.rules["defaultDisposition"],"deferred_review")
        self.assertTrue(all(not r["nativeEmissionAuthorized"]
                            for r in self.decisions["records"]))
        self.assertTrue(all(r["emission"]=="deferred_pending_evidence_and_parser"
                            for r in self.rules["relationshipRules"]))

    def test_evidence_only_distinction(self):
        for family in ("Connector:","NoteLink:"):
            row=next(r for r in self.decisions["records"] if r["family"]==family)
            self.assertEqual(row["reviewState"],"evidence_only")

    def test_workbench_obligations(self):
        for r in self.decisions["records"]:
            self.assertTrue(r["requiredEvidence"])
            self.assertTrue(all(r["workbench"].get(k) for k in
                ("structural","visual","navigation","validation","roundTrip")))

if __name__=="__main__":
    unittest.main()
