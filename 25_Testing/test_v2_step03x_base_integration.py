import importlib.util,json,tempfile,unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location("stage",R/"20_Base Vault/stage_v2_import_base.py")
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class StageV2BaseTests(unittest.TestCase):
 def test_stages_without_manual_base(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);led=p/"ledger.jsonl";cross=p/"cross.jsonl"
   uid="20261001123456000skellyspencer"
   led.write_text(json.dumps({"eaObjectID":1,"eaGUID":"{A}","uid":uid})+"\n")
   cross.write_text(json.dumps({"eaObjectID":1,"eaGUID":"{A}"})+"\n")
   out=p/"isolated_base";r=m.stage(led,cross,out)
   self.assertTrue((out/"99_System/step03x_readiness.json").is_file())
   self.assertFalse(r["plugin_ready"])
   self.assertFalse(r["native_import_ready"])
   self.assertEqual(r["candidate_identity_audit"]["identities"],1)
   with self.assertRaisesRegex(ValueError,"exists"):m.stage(led,cross,out)
 def test_failure_cleans_partial_base(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d);led=p/"broken";cross=p/"missing";led.write_text("invalid")
   out=p/"base"
   with self.assertRaises(Exception):m.stage(led,cross,out)
   self.assertFalse(out.exists())
if __name__=="__main__":unittest.main()
