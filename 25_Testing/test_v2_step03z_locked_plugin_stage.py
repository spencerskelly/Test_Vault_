import hashlib,importlib.util,json,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("plugin_stage",R/"20_Base Vault/stage_v2_locked_plugins.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class PluginStageTests(unittest.TestCase):
 def setup_fixture(self,p):
  base=p/"base";base.mkdir();(base/".mdse_v2_test_base.json").write_text("{}")
  art=p/"art";pins={}
  for pid in m.IDS:
   f=art/pid;f.mkdir(parents=True)
   (f/"manifest.json").write_text(json.dumps({"id":pid,"version":"2.0.0-test"}))
   (f/"main.js").write_text("module.exports = {}")
   pins[pid]={"version":"2.0.0-test","sha256":{n:hashlib.sha256((f/n).read_bytes()).hexdigest() for n in m.REQUIRED}}
  e=p/"evidence.json";e.write_text(json.dumps({"schema":"mdse-v2-plugin-evidence/1","v2_editor_tests_passed":True,"bootstrap_tests_passed":True,"plugins":pins}))
  return base,art,e
 def test_stages_hash_locked_payload(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);b,a,e=self.setup_fixture(p)
   report=m.stage(b,a,p/"out",e)
   self.assertTrue(report["plugin_artifacts_verified"])
   self.assertFalse(report["runtime_observed_in_obsidian"])
   self.assertTrue((p/"out/.obsidian/plugins/mdse-workbench/main.js").is_file())
 def test_bad_hash_fails_without_output(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);b,a,e=self.setup_fixture(p)
   (a/"mdse-workbench/main.js").write_text("tampered")
   with self.assertRaisesRegex(ValueError,"Hash mismatch"):m.stage(b,a,p/"out",e)
   self.assertFalse((p/"out").exists())
 def test_missing_evidence_fails(self):
  with tempfile.TemporaryDirectory() as tmp:
   p=Path(tmp);b,a,e=self.setup_fixture(p)
   data=json.loads(e.read_text());data["v2_editor_tests_passed"]=False;e.write_text(json.dumps(data))
   with self.assertRaisesRegex(ValueError,"evidence"):m.stage(b,a,p/"out",e)
if __name__=="__main__":unittest.main()
