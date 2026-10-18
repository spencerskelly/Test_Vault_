import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from phase9_nested_profile_consistency import classify_payload
class ProfileTests(unittest.TestCase):
 def test_expected(self):
  self.assertEqual(classify_payload("@STEREO;Name=Hardware Component;FQName=Webasto MBDV Profile::Hardware Component;@ENDSTEREO;"),"EXPECTED_HARDWARE_PROFILE")
 def test_mismatched_profile(self):
  self.assertEqual(classify_payload("@STEREO;Name=Hardware Component;FQName=Other::Hardware Component;@ENDSTEREO;"),"OTHER_PROFILE_REVIEW")
 def test_missing_payload(self):
  self.assertEqual(classify_payload(""),"MISSING_OR_MULTIPLE_STEREOTYPES")
 def test_multiple_payloads(self):
  one="@STEREO;Name=Hardware Component;FQName=Webasto MBDV Profile::Hardware Component;@ENDSTEREO;"
  self.assertEqual(classify_payload(one+one),"MISSING_OR_MULTIPLE_STEREOTYPES")
if __name__=="__main__":unittest.main()
