import importlib.util,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def mod(path,name):
 s=importlib.util.spec_from_file_location(name,ROOT/path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
builder=mod("20_Base Vault/build_v2_test_base.py","b")
checker=mod("20_Base Vault/verify_v2_staged_runtime.py","c")
class RuntimeTests(unittest.TestCase):
 def test_integrity_and_honest_runtime_block(self):
  with tempfile.TemporaryDirectory() as tmp:
   base=Path(tmp)/"base";builder.build(base);report=checker.audit(base)
   self.assertEqual(report["files_checked"],8)
   self.assertEqual(report["hash_failures"],[])
   self.assertFalse(report["plugin_ready"])
   self.assertFalse(report["native_import_ready"])
   self.assertEqual(report["status"],"BLOCKED_RUNTIME")
 def test_tamper_is_reported(self):
  with tempfile.TemporaryDirectory() as tmp:
   base=Path(tmp)/"base";builder.build(base)
   (base/"99_System/README_Base_V2.md").write_text("tampered")
   report=checker.audit(base)
   self.assertEqual(report["status"],"FAIL_BASE_INTEGRITY")
   self.assertIn("99_System/README_Base_V2.md",report["hash_failures"])
if __name__=="__main__":unittest.main()
