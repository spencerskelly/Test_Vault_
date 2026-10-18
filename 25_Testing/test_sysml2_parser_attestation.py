"""Synthetic parser-result attestation tests; no claim parser was run."""
import pathlib,sys,tempfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from sysml2_parser_attestation import fixture_digest,parser_attestation
class TestParserEvidence(unittest.TestCase):
 def setUp(self):
  tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup)
  self.fixture=pathlib.Path(tmp.name)/"example.sysml"
  self.fixture.write_text("package Synthetic {}")
 def test_acceptance_not_native_certification(self):
  r=parser_attestation(self.fixture,"synthetic-parser","0.0",0)
  self.assertEqual(r["status"],"PARSER_ACCEPTED")
  self.assertFalse(r["nativeCertified"])
 def test_rejection_recorded(self):
  r=parser_attestation(self.fixture,"synthetic-parser","0.0",1)
  self.assertEqual(r["status"],"PARSER_REJECTED")
 def test_missing_parser_identity_rejected(self):
  with self.assertRaisesRegex(ValueError,"PARSER_IDENTITY_REQUIRED"):
   parser_attestation(self.fixture,"","0.0",0)
 def test_modified_fixture_changes_fingerprint(self):
  original=fixture_digest(self.fixture)
  self.fixture.write_text("package Changed {}")
  self.assertNotEqual(original,fixture_digest(self.fixture))
if __name__=="__main__":unittest.main()
