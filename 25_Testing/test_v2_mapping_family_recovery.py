"""Verify recovered V2 family decisions remain complete and uniquely keyed."""
import json,pathlib,re,unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
REC=ROOT/"26_Definitions/v2_mapping_family_recovery.v0.1.json"
DOC=ROOT/"24_Workbench/docs/GOLDEN_IMPORT_STEP2_60_FAMILY_DECISION_RECONCILIATION_2026-10-17.md"
REG=ROOT/"24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json"

class FamilyRecoveryTest(unittest.TestCase):
 def test_family_sets_and_status(self):
  data=json.loads(REC.read_text(encoding="utf-8"))
  rules=json.loads(REG.read_text(encoding="utf-8"))
  text=DOC.read_text(encoding="utf-8")
  section=False
  names=[]
  for line in text.splitlines():
   if line.startswith("### Native reusable") or line.startswith("### Native local") or line.startswith("### MDSE note"):
    section=True
   if section and line.startswith("- `"):
    names.extend(re.findall(r"`([^`]+)`",line.split(" -> ")[0]))
  elements=data["elements"]
  relationships=data["relationships"]
  self.assertEqual(len(elements),60)
  self.assertEqual(len(relationships),26)
  self.assertEqual({e["family"] for e in elements},set(names))
  self.assertEqual({r["family"] for r in relationships},{r["family"] for r in rules["relationshipRules"]})
  self.assertEqual(len(set(names)),60)
  self.assertEqual({g:sum(x["group"]==g for x in elements) for g in ("native_definition","native_usage","non_native")},
                   {"native_definition":40,"native_usage":7,"non_native":13})
  for r in elements+relationships:
   self.assertEqual(r["runtime_evidence"],"not_individually_verified")
   self.assertEqual(r["parser_status"],"not_verified")
   self.assertEqual(r["workbench_status"],"not_verified")

if __name__=="__main__":unittest.main()
