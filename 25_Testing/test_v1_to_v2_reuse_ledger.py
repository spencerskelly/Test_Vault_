"""Guard the v1-to-v2 reuse ledger against lost artifacts and false parity claims."""
import json,pathlib,re,unittest,urllib.parse

ROOT=pathlib.Path(__file__).resolve().parents[1]
LEDGER=ROOT/"26_Definitions/v1_to_v2_reuse_ledger.v0.1.json"
MIGRATION=ROOT/"26_Definitions/V2_FOLDER_MIGRATION_MANIFEST_2026-10-18.json"
INDEX=ROOT/"26_Definitions/V1_V2_REUSE_LEDGER_INDEX.md"
AUDIT=ROOT/"26_Definitions/V1_V2_DEEP_TECHNICAL_RECOVERY_AND_PLATFORM_ARCHITECTURE_2026-10-18.md"

class ReuseLedgerTest(unittest.TestCase):
 def test_coverage_paths_status(self):
  ledger=json.loads(LEDGER.read_text(encoding="utf-8"))
  move=json.loads(MIGRATION.read_text(encoding="utf-8"))
  archive=set(move["path_moves"].values())
  self.assertEqual(ledger["schema"],"mdse-v2-prior-work-reuse-ledger/1")
  rows=ledger["records"]
  self.assertEqual(len(rows),28)
  self.assertEqual({x["id"] for x in rows},{f"R{i:02d}" for i in range(1,29)})
  self.assertGreaterEqual(len({r["v1_source"] for r in rows}),20)
  for r in rows:
   self.assertIn(r["milestone"],("first","later"))
   self.assertIn(r["priority"],("P0","P1","P2"))
   self.assertTrue(r["v1_source"].startswith("100_Archive/V1/"))
   self.assertIn(r["v1_source"],archive)
   self.assertTrue((ROOT/r["v1_source"]).is_file(),r["id"]+" archived source missing")
   if r["v2_target"]:
    self.assertNotIn("100_Archive/V1/",r["v2_target"])
    self.assertTrue((ROOT/r["v2_target"]).is_file(),r["id"]+" active reference missing")
   self.assertEqual(r["port_status"],"not_ported_or_not_verified")
   self.assertIs(r["v2_behavior_verified"],False)
   self.assertIn("no_V1_runtime_imports",r["acceptance_required"])
 def test_human_index_links(self):
  text=INDEX.read_text(encoding="utf-8")
  rows=json.loads(LEDGER.read_text(encoding="utf-8"))["records"]
  for r in rows:self.assertIn(r["id"]+" —",text)
  self.assertIn("DEF-01",AUDIT.read_text(encoding="utf-8"))
  self.assertIn("DEF-02",AUDIT.read_text(encoding="utf-8"))
  self.assertIn("DEF-03",AUDIT.read_text(encoding="utf-8"))
  for raw in re.findall(r"\]\(([^)]+)\)",text):
   target=urllib.parse.unquote(raw.split("#")[0])
   if not target or "://" in target:continue
   path=(INDEX.parent/target).resolve()
   self.assertTrue(path.is_relative_to(ROOT) and path.exists(),target)

if __name__=="__main__":unittest.main()
