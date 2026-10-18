import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).parent))
from phase9_local_specialization_evidence_screen import audit
class GateTests(unittest.TestCase):
 def test_missing_inputs_are_not_implicitly_trusted(self):
  with self.assertRaises(FileNotFoundError):audit('/nonexistent-qeax-file','/nonexistent-ledger-file')
if __name__=='__main__':unittest.main()
