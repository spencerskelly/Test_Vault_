import unittest
from unittest.mock import patch
import phase9_local_generalization_handoff as h

class GateTests(unittest.TestCase):
 def test_replay_failure_blocks(self):
  with patch.object(h,'check',return_value={'valid':False,'source_count':3,'ledger_count':3}):
   result=h.handoff('placeholder','placeholder','placeholder','1')
  self.assertFalse(result['ok'])
  self.assertFalse(result['nativeCertified'])
 def test_count_mismatch_blocks(self):
  with patch.object(h,'check',return_value={'valid':True,'source_count':3,'ledger_count':2}):
   result=h.handoff('placeholder','placeholder','placeholder','1')
  self.assertEqual(result['reason'],'FULL_LEDGER_REPLAY_FAILED')

if __name__=='__main__':unittest.main()
