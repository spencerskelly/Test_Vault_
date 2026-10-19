import importlib.util,json,tempfile,unittest
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"21_Importer"/"v2_step03t_placement_manifest.py"
spec=importlib.util.spec_from_file_location("placement",p);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class ManifestTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);self.root=Path(t.name);self.vault=self.root/"vault";(self.vault/"10_Elements").mkdir(parents=True)
  self.out=self.root/"manifest.jsonl"
 def note(self,oid,kind,stereo=""):
  (self.vault/"10_Elements"/f"EA-{oid}.md").write_text("---\neaObjectID: "+str(oid)+"\neaGUID: \"{guid}\"\neaType: "+json.dumps(kind)+"\neaStereotype: "+json.dumps(stereo)+"\n---\n# Heading\n")
 def test_registry_proposals_preserve_notes(self):
  self.note(1,"Requirement");self.note(2,"Package")
  before=[p.read_text() for p in sorted((self.vault/"10_Elements").iterdir())]
  result=mod.build(self.vault,p.parents[1],self.out)
  records=[json.loads(s) for s in self.out.read_text().splitlines()]
  self.assertEqual(result["notes"],2)
  self.assertEqual([r["disposition"] for r in records],["native_candidate","folder_only"])
  self.assertFalse(any(r["noteRenameAuthorized"] for r in records))
  self.assertEqual(before,[p.read_text() for p in sorted((self.vault/"10_Elements").iterdir())])
 def test_duplicate_identity_rejected(self):
  self.note(1,"Requirement");self.note(2,"Requirement")
  f=self.vault/"10_Elements"/"EA-2.md";f.write_text(f.read_text().replace("eaObjectID: 2","eaObjectID: 1"))
  with self.assertRaisesRegex(ValueError,"duplicate"):mod.build(self.vault,p.parents[1],self.out)
 def test_refuses_existing_manifest(self):
  self.note(1,"Requirement");self.out.write_text("sentinel")
  with self.assertRaisesRegex(ValueError,"exists"):mod.build(self.vault,p.parents[1],self.out)
if __name__=="__main__":unittest.main()
