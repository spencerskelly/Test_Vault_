import unittest
from approved_relationship_audit import POLICIES,evaluate
class Synthetic(unittest.TestCase):
 def row(self,t,s='',direction='Source -> Destination'):
  return dict(Connector_Type=t,Stereotype=s,Direction=direction,Start_Object_ID=1,End_Object_ID=2)
 def test_all_families(self):self.assertEqual(len(POLICIES),26)
 def test_special_case_precedence(self):
  self.assertEqual(POLICIES['Realisation:deriveReqt'],'derivation_review')
  self.assertNotEqual(POLICIES['Realisation:deriveReqt'],POLICIES['Realisation'])
 def test_non_native(self):
  self.assertEqual(evaluate(self.row('NoteLink'),{1:('Class',''),2:('Class','')})[0],'evidence_only')
 def test_ambiguous_review(self):
  self.assertEqual(evaluate(self.row('Aggregation'),{1:('Class',''),2:('Class','')})[0],'deferred_review')
 def test_bad_derivation(self):
  self.assertIn('REQUIREMENT_ENDPOINT_REVIEW',evaluate(self.row('Dependency','deriveReqt'),{1:('Class',''),2:('Class','')})[2])
 def test_missing_direction(self):
  self.assertIn('SOURCE_DIRECTION_UNATTESTED',evaluate(self.row('Dependency',direction='Unspecified'),{1:('Class',''),2:('Class','')})[2])
if __name__=='__main__':unittest.main()
