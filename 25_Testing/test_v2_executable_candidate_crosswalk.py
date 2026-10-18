"""Verify approved family crosswalk against candidate selector runtime rules."""
import json,pathlib,unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
CROSS=ROOT/"26_Definitions/v2_executable_candidate_crosswalk.v0.1.json"
FAMILIES=ROOT/"26_Definitions/v2_mapping_family_recovery.v0.1.json"
RULES=ROOT/"24_Workbench/registry/sysml_v2_semantic_rules.v0.2.json"

class CandidateCrosswalkTests(unittest.TestCase):
 def test_recompute_selectors(self):
  cross=json.loads(CROSS.read_text(encoding="utf-8"))
  prior=json.loads(FAMILIES.read_text(encoding="utf-8"))
  registry=json.loads(RULES.read_text(encoding="utf-8"))
  self.assertEqual(len(cross["elements"]),60)
  self.assertEqual(len(cross["relationships"]),26)
  self.assertEqual({x["family"] for x in cross["elements"]},{x["family"] for x in prior["elements"]})
  self.assertEqual({x["family"] for x in cross["relationships"]},{x["family"] for x in registry["relationshipRules"]})
  for e in cross["elements"]:
   source_type,_,st=e["family"].partition(":")
   exact=[r for r in registry["elementRules"] if r["eaType"]==source_type and r["stereotype"].casefold()==st.casefold()]
   wildcard=[r for r in registry["elementRules"] if r["eaType"]==source_type and r["stereotype"]=="*"]
   selected=exact or wildcard
   status="exact_candidate" if exact else "wildcard_candidate" if wildcard else "not_covered_by_candidate_registry"
   self.assertEqual(e["selector_status"],status,e["family"])
   self.assertEqual(e["selector_target"],selected[0]["target"] if selected else None)
   self.assertFalse(e["native_emission_verified"])
  for r in cross["relationships"]:
   self.assertEqual(r["selector_status"],"exact_candidate_family")
   self.assertFalse(r["native_emission_verified"])

if __name__=="__main__":unittest.main()
