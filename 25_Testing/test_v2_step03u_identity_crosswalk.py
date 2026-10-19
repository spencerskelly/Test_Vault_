import importlib.util,json,tempfile,unittest
from pathlib import Path

PATH=Path(__file__).resolve().parents[1]/"21_Importer"/"v2_step03u_identity_crosswalk.py"
spec=importlib.util.spec_from_file_location("crosswalk",PATH)
tool=importlib.util.module_from_spec(spec);spec.loader.exec_module(tool)

class IdentityCrosswalkTests(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup)
        self.root=Path(tmp.name);self.vault=self.root/"vault"
        (self.vault/"10_Elements").mkdir(parents=True)
        (self.vault/"10_Elements"/"EA-1.md").write_text("# A")
        self.manifest=self.root/"manifest.jsonl";self.output=self.root/"crosswalk.jsonl"
    def write(self,rows):
        self.manifest.write_text("".join(json.dumps(r)+"\n" for r in rows))
    def test_folder_disposition_preserved_without_renames(self):
        self.write([{"eaObjectID":1,"eaGUID":"g1","sourceNote":"EA-1.md","disposition":"folder_only"}])
        result=tool.build(self.vault,self.manifest,self.output)
        self.assertEqual(result["statuses"]["folder_mapping_pending"],1)
        self.assertEqual(result["moves"],0)
        self.assertIsNone(json.loads(self.output.read_text())["targetPath"])
    def test_missing_note_refused(self):
        self.write([{"eaObjectID":2,"eaGUID":"g2","sourceNote":"EA-2.md","disposition":"native_candidate"}])
        with self.assertRaisesRegex(ValueError,"Missing source note"):
            tool.build(self.vault,self.manifest,self.output)
    def test_duplicate_identity_refused(self):
        self.write([{"eaObjectID":1,"eaGUID":"g1","sourceNote":"EA-1.md","disposition":"native_candidate"}]*2)
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            tool.build(self.vault,self.manifest,self.output)
if __name__=="__main__":unittest.main()
