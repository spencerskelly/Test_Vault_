"""Synthetic, private-only Phase 8 input attestations."""
import hashlib,importlib.util,pathlib,tempfile,unittest
P=pathlib.Path(__file__).resolve().parents[1]/'24_Workbench/registry/runtime/normalize_qeax_phase8.py'
spec=importlib.util.spec_from_file_location('phase8_input_attestation',P)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
class InputAttestation(unittest.TestCase):
 def test_hash_matches_bytes_and_detects_change(self):
  with tempfile.TemporaryDirectory() as d:
   p=pathlib.Path(d)/'synthetic.sqlite';p.write_bytes(b'fixture-v1')
   original=mod.sha256_file(p)
   self.assertEqual(original,hashlib.sha256(b'fixture-v1').hexdigest())
   p.write_bytes(b'fixture-v2')
   self.assertNotEqual(original,mod.sha256_file(p))
 def test_registry_fingerprint_is_separate(self):
  with tempfile.TemporaryDirectory() as d:
   a=pathlib.Path(d)/'synthetic.sqlite';a.write_bytes(b'source')
   b=pathlib.Path(d)/'registry.json';b.write_bytes(b'{"families":[]}')
   v=mod.input_attestation(a,b)
   self.assertNotEqual(v['source_sha256'],v['registry_sha256'])
   self.assertEqual(v['native_certified'],0)
 def test_missing_input_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   with self.assertRaises(FileNotFoundError):
    mod.input_attestation(pathlib.Path(d)/'missing.sqlite',pathlib.Path(d)/'missing.json')
if __name__=='__main__':unittest.main()
