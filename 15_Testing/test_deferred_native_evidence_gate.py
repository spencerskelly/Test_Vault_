"""Synthetic gates: complete evidence never equals native certification."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from deferred_native_evidence_gate import assess
REG={"requiredCommon":["source_kind","candidate_native_construct","reviewer_decision","parser_result"],
     "acceptedReviewDecision":"approved","acceptedParserResult":"passed",
     "categories":{"Software Component":{"nativeCandidates":["PartDefinition"],"required":["host_usage_evidence"]},
                   "Unstereotyped Class":{"nativeCandidates":[],"required":["explicit_source_concept"]}}}
class GateTests(unittest.TestCase):
 def test_unapproved_is_deferred(self):
  x=assess(REG,"Software Component",{"source_kind":"EA","candidate_native_construct":"PartDefinition","host_usage_evidence":"synthetic"})
  self.assertIn("REVIEW_NOT_APPROVED",x["missing"])
 def test_complete_still_not_certified(self):
  x=assess(REG,"Software Component",{"source_kind":"EA","candidate_native_construct":"PartDefinition",
    "host_usage_evidence":"synthetic","reviewer_decision":"approved","parser_result":"passed"})
  self.assertEqual(x["status"],"evidence_complete_not_certified")
  self.assertFalse(x["nativeCertified"])
 def test_unknown_deferred(self):
  self.assertEqual(assess(REG,"Unknown",{})["status"],"deferred_review")
 def test_untyped_class_needs_explicit_review(self):
  x=assess(REG,"Unstereotyped Class",{"source_kind":"EA","candidate_native_construct":"PartDefinition",
     "explicit_source_concept":"synthetic","reviewer_decision":"approved","parser_result":"passed"})
  self.assertIn("UNSUPPORTED_NATIVE_CANDIDATE",x["missing"])
 def test_missing_parser_blocks(self):
  x=assess(REG,"Software Component",{"source_kind":"EA","candidate_native_construct":"PartDefinition",
    "host_usage_evidence":"synthetic","reviewer_decision":"approved"})
  self.assertIn("PARSER_NOT_PASSED",x["missing"])
if __name__=="__main__":unittest.main()
