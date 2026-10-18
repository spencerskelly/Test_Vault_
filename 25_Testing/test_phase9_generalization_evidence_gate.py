import pathlib,sys,unittest
from unittest.mock import patch
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import phase9_generalization_evidence_gate as gate
class GateTests(unittest.TestCase):
 def test_failed_replay_blocks(self):
  with patch.object(gate,'check',return_value={'valid':False,'source_count':2,'ledger_count':2}):
   r=gate.gate('source','ledger','registry')
   self.assertFalse(r['review']);self.assertEqual(r['native_certified'],0)
 def test_count_mismatch_blocks(self):
  with patch.object(gate,'check',return_value={'valid':True,'source_count':2,'ledger_count':1}):
   self.assertFalse(gate.gate('source','ledger','registry')['review'])
 def test_consistent_replay_is_review_only(self):
  with patch.object(gate,'check',return_value={'valid':True,'source_count':2,'ledger_count':2}):
   r=gate.gate('source','ledger','registry')
   self.assertTrue(r['review']);self.assertEqual(r['native_certified'],0)
if __name__=='__main__':unittest.main()
