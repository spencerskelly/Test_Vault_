"""Preflight tests including the macOS Java launcher-stub case."""
import json, pathlib, sys, types, unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from sysml2_pilot_preflight import probe

def fake_run(java_version='openjdk version "21.0.4" 2024-07-16', java_code=0, kernels=None):
 def run(argv,**kw):
  if argv[:2]==["java","-version"]:
   return types.SimpleNamespace(returncode=java_code,stderr=java_version,stdout="")
  return types.SimpleNamespace(returncode=0,stderr="",stdout=kernels if kernels is not None else '{"kernelspecs":{}}')
 return run

class PreflightTests(unittest.TestCase):
 def test_missing_java(self):
  r=probe(which=lambda n: None if n=="java" else "/bin/jupyter")
  self.assertFalse(r["javaCommandPresent"])
  self.assertEqual(r["status"],"MISSING_DEPENDENCY")
 def test_missing_jupyter_reported_independently(self):
  r=probe(which=lambda n: "/bin/java" if n=="java" else None,run=fake_run())
  self.assertTrue(r["javaAvailable"])
  self.assertFalse(r["jupyterAvailable"])
 def test_missing_java_reports_jupyter_present(self):
  r=probe(which=lambda n: "/bin/jupyter" if n=="jupyter" else None)
  self.assertFalse(r["javaAvailable"])
  self.assertTrue(r["jupyterAvailable"])
 def test_registered_kernel(self):
  r=probe(which=lambda n:"/fake/"+n,run=fake_run(kernels=json.dumps({"kernelspecs":{"sysml":{}}})))
  self.assertEqual(r["status"],"KERNEL_FOUND")
  self.assertFalse(r["nativeCertified"])
 def test_no_kernel(self):
  r=probe(which=lambda n:"/fake/"+n,run=fake_run())
  self.assertEqual(r["status"],"KERNEL_NOT_FOUND")
 def test_invalid_kernel_json(self):
  r=probe(which=lambda n:"/fake/"+n,run=fake_run(kernels="not json"))
  self.assertEqual(r["status"],"KERNEL_QUERY_FAILED")
 def test_macos_launcher_stub(self):
  r=probe(which=lambda n:"/fake/"+n,run=fake_run("Unable to locate a Java Runtime",1))
  self.assertTrue(r["javaCommandPresent"])
  self.assertFalse(r["javaAvailable"])
  self.assertIsNone(r["javaMajorVersion"])
 def test_legacy_java_8_rejected(self):
  r=probe(which=lambda n:"/fake/"+n,run=fake_run('java version "1.8.0_392"'))
  self.assertEqual(r["javaMajorVersion"],8)
  self.assertFalse(r["javaAvailable"])
 def test_java21_detected(self):
  r=probe(which=lambda n:"/fake/"+n,run=fake_run())
  self.assertEqual(r["javaMajorVersion"],21)
  self.assertTrue(r["javaAvailable"])

if __name__=="__main__": unittest.main()
