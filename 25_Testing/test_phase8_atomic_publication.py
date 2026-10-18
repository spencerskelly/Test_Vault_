"""Synthetic transactional output guarantees for Phase 8 CLI wrapper."""
import importlib.util,pathlib,tempfile,unittest
PATH=pathlib.Path(__file__).resolve().parents[1]/"24_Workbench/registry/runtime/normalize_qeax_phase8.py"
spec=importlib.util.spec_from_file_location("phase8_normalizer",PATH)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
class AtomicPhase8(unittest.TestCase):
 def test_existing_destination_preserved(self):
  with tempfile.TemporaryDirectory() as d:
   output=pathlib.Path(d)/"existing"
   output.mkdir()
   marker=output/"original.txt"
   marker.write_text("unchanged")
   with self.assertRaisesRegex(ValueError,"OUTPUT_ALREADY_EXISTS"):
    module.reconcile_atomic("not-read.sqlite","missing-registry.json",output)
   self.assertEqual(marker.read_text(),"unchanged")
 def test_failure_leaves_no_result_or_stage(self):
  with tempfile.TemporaryDirectory() as d:
   output=pathlib.Path(d)/"result"
   with self.assertRaises(Exception):
    module.reconcile_atomic("nonexistent.sqlite","missing-registry.json",output)
   self.assertFalse(output.exists())
   self.assertEqual(list(pathlib.Path(d).glob(".phase8-incomplete-*")),[])
if __name__=="__main__":unittest.main()
