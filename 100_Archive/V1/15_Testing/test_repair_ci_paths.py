import unittest
from repair_ci_paths import rewrite

class TestPaths(unittest.TestCase):
    def test_migrates_and_idempotent(self):
        s = 'paths:\n - "Importer/**"\n - "Base Vault/**"\n - "00_Workspace/**"\nrun: node "Importer/Testing/check.js"\nrun: python "Base Vault/Testing/check-release.py"\n'
        got = rewrite(s)
        self.assertIn('"11_Importer/**"', got)
        self.assertIn('"10_Base Vault/**"', got)
        self.assertIn('"55_Workspace/**"', got)
        self.assertEqual(rewrite(got), got)

    def test_missing_required_trigger_fails(self):
        with self.assertRaises(ValueError):
            rewrite('paths: ["Importer/**"]')

if __name__ == "__main__":
    unittest.main()
