"""Synthetic read-only QEAX preflight tests; no real source data is committed."""
import importlib.util,pathlib,sqlite3,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location("qeax_v2",ROOT/"21_Importer/qeax_v2_preflight.py")
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class SourcePreflight(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.file=pathlib.Path(self.tmp.name)/"fixture.qeax"
  with sqlite3.connect(self.file) as db:
   for name in mod.TABLES.values():db.execute("CREATE TABLE "+name+" (id INTEGER)")
 def test_drift_fails_closed(self):
  with self.assertRaisesRegex(ValueError,"SOURCE_PROFILE_DRIFT"):mod.inspect(self.file)
 def test_diagnostic_mode_never_emits(self):
  a=mod.inspect(self.file,strict=False)
  self.assertEqual(a["status"],"SOURCE_PROFILE_DRIFT")
  self.assertFalse(a["native_emission_authorized"])
  self.assertFalse(a["real_model_rows_exported"])
 def test_exact_synthetic_profile(self):
  original=mod.PROFILE
  try:
   mod.PROFILE={name:0 for name in original}
   r=mod.inspect(self.file)
   self.assertEqual(r["status"],"PASS")
  finally: mod.PROFILE=original
 def test_bad_file_rejected(self):
  self.file.write_text("invalid")
  with self.assertRaisesRegex(ValueError,"NOT_VALID_QEAX_SQLITE"):mod.inspect(self.file)
if __name__=="__main__":unittest.main()
