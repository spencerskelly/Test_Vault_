import pathlib,sys,unittest
from unittest.mock import patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import phase9_source_bound_specialization_review as gate
class SourceBoundGateTests(unittest.TestCase):
 def test_integrity_failure_blocks_graph_review(self):
  with patch.object(gate,'verify_rows',return_value={'verified':False,'source_count':14688}),patch.object(gate,'replay_normalization',return_value={'valid':True}),patch.object(gate,'inspect',side_effect=AssertionError('must not inspect')):
   r=gate.inspect_verified('q','l','r','a',{})
   self.assertFalse(r['review_valid']);self.assertEqual(r['native_certified'],0)
 def test_replay_failure_blocks_graph_review(self):
  with patch.object(gate,'verify_rows',return_value={'verified':True,'source_count':14688}),patch.object(gate,'replay_normalization',return_value={'valid':False}),patch.object(gate,'inspect',side_effect=AssertionError('must not inspect')):
   r=gate.inspect_verified('q','l','r','a',{})
   self.assertIn('NORMALIZATION_REPLAY_FAILED',r['blockers'])
 def test_clean_review_still_not_native(self):
  with patch.object(gate,'verify_rows',return_value={'verified':True,'source_count':14688}),patch.object(gate,'replay_normalization',return_value={'valid':True}),patch.object(gate,'inspect',return_value={'errors':{},'source_count':3735}):
   r=gate.inspect_verified('q','l','r','a',{})
   self.assertTrue(r['review_valid']);self.assertFalse(r['may_emit_native'])
 def test_expected_count_is_strict(self):
  with patch.object(gate,'verify_rows',return_value={'verified':True,'source_count':10}),patch.object(gate,'replay_normalization',return_value={'valid':True}),patch.object(gate,'inspect',side_effect=AssertionError('must not inspect')):
   self.assertIn('SOURCE_COUNT_MISMATCH',gate.inspect_verified('q','l','r','a',{})['blockers'])
if __name__=='__main__':unittest.main()
