"""Tests of read-only pilot kernel installation preflight."""
import json,pathlib,sys,types,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from sysml2_pilot_preflight import probe

class PreflightTests(unittest.TestCase):
 def test_missing_java(self):
  self.assertEqual(probe(which=lambda name: None if name=="java" else "/bin/jupyter")["status"],"MISSING_DEPENDENCY")
 def test_missing_jupyter_reported_independently(self):
  r=probe(which=lambda name: "/bin/java" if name=="java" else None)
  self.assertTrue(r["javaAvailable"])
  self.assertFalse(r["jupyterAvailable"])
  self.assertEqual(r["status"],"MISSING_DEPENDENCY")
 def test_missing_java_reports_jupyter_present(self):
  r=probe(which=lambda name: "/bin/jupyter" if name=="jupyter" else None)
  self.assertFalse(r["javaAvailable"])
  self.assertTrue(r["jupyterAvailable"])
 def test_registered_kernel(self):
  run=lambda *a,**kw:types.SimpleNamespace(returncode=0,stdout=json.dumps({"kernelspecs":{"python3":{},"sysml":{}}}))
  r=probe(which=lambda name:"/fake/"+name,run=run)
  self.assertEqual(r["status"],"KERNEL_FOUND")
  self.assertTrue(r["readyForManualPilotValidation"])
  self.assertFalse(r["nativeCertified"])
 def test_no_kernel(self):
  run=lambda *a,**kw:types.SimpleNamespace(returncode=0,stdout='{"kernelspecs":{"python3":{}}}')
  self.assertEqual(probe(which=lambda name:"/fake/"+name,run=run)["status"],"KERNEL_NOT_FOUND")
 def test_invalid_kernel_json(self):
  run=lambda *a,**kw:types.SimpleNamespace(returncode=0,stdout="not json")
  self.assertEqual(probe(which=lambda name:"/fake/"+name,run=run)["status"],"KERNEL_QUERY_FAILED")

if __name__=="__main__":unittest.main()
