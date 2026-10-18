"""Ensure the v2 master MOC resolves and indexes the principal program areas."""
import pathlib,re,unittest,urllib.parse

ROOT=pathlib.Path(__file__).resolve().parents[1]
MOC=ROOT/"MOC_MDSE_V2.md"
REQUIRED=("20_Base Vault","21_Importer","23_Bootstrap","24_Workbench","25_Testing",
          "26_Definitions","29_SysMLv2_Translator_Workbench","55_Workspace","66_Cross-Vault",
          "99_System","88_Reference")
PATTERN=re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

class MasterMocTests(unittest.TestCase):
 def test_links_and_coverage(self):
  text=MOC.read_text(encoding="utf-8")
  links=[urllib.parse.unquote(x.split("#",1)[0]) for x in PATTERN.findall(text)]
  self.assertGreaterEqual(len(links),40)
  errors=[]
  for link in links:
   if not link or "://" in link or link.startswith("#"):continue
   path=(ROOT/link).resolve()
   if not path.is_relative_to(ROOT) or not path.exists():
    errors.append(link)
  self.assertEqual(errors,[],"Broken local MOC references")
  for directory in REQUIRED:
   self.assertTrue((ROOT/directory).exists(),f"Missing expected area: {directory}")
   self.assertTrue(any(link==directory or link.startswith(directory+"/") for link in links),
                   f"Unindexed area: {directory}")
 def test_program_contracts(self):
  text=MOC.read_text(encoding="utf-8")
  for marker in ("## 00","## 10","## 20","## 30","## 40","## 50","## 60","## 70",
                 "Find before creating","Known missing coverage"):
   self.assertIn(marker,text)

if __name__=="__main__":unittest.main()
