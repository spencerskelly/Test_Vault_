"""Archive MOC coverage contract: all migrated V1 paths must be indexed."""
import json,pathlib,re,unittest,urllib.parse

ROOT=pathlib.Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/"100_Archive"
MANIFEST=ROOT/"26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json"
AREAS={"10_Base Vault":48,"11_Importer":666,"13_Bootstrap":28,"14_Workbench":217,"15_Testing":166,"16_Definitions":40}

class ArchiveMocTest(unittest.TestCase):
 def test_complete_archive_manifest_coverage(self):
  manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
  expected={p for p in manifest["path_moves"].values() if p.startswith("100_Archive/V1/")}
  self.assertEqual(len(expected),1165)
  for area,n in AREAS.items():
   self.assertEqual(sum(p.split("/")[2]==area for p in expected),n)
  indexed=[]
  index_files=sorted(ARCHIVE.glob("MOC_V1_*_[0-9]*.md"))
  self.assertEqual(len(index_files),12)
  for file in index_files:
   text=file.read_text(encoding="utf-8")
   for raw in re.findall(r"\]\((V1/[^)]+)\)",text):
    indexed.append("100_Archive/"+urllib.parse.unquote(raw))
  self.assertEqual(len(indexed),1165,"missing or duplicate links")
  self.assertEqual(set(indexed),expected,"archive MOC and manifest differ")
 def test_central_map_and_value_register(self):
  moc=(ARCHIVE/"MOC_V1_ARCHIVE.md").read_text(encoding="utf-8")
  self.assertIn("1,165",moc)
  for f in sorted(ARCHIVE.glob("MOC_V1_*_[0-9]*.md")):
   self.assertIn(f.name,moc)
  self.assertTrue((ROOT/"26_Definitions/V1_ARCHIVE_VALUE_RECOVERY_GAPS_2026-10-18.md").is_file())

if __name__=="__main__":unittest.main()
