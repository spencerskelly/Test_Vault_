import tempfile
import unittest
from pathlib import Path
from localmodel_topology_index import parse_index

A = "ep-20261014130000001skellyspencer"
B = "ep-20261014130000002skellyspencer"
C = "conn-20261014130000003skellyspencer"


class LocalModelIndexTests(unittest.TestCase):
    def build(self, body):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        (root / "Assembly.md").write_text(body, encoding="utf-8")
        self.addCleanup(tmp.cleanup)
        return parse_index(root)

    def test_boundary_connection_and_equality(self):
        body = f"""<!-- MDSE:LOCAL-MODEL START schema=0.5 -->
### Interfaces
#### J1
- equals: [[#^{B}]]
^{A}
#### J2
- part: [[#^part-20261014130000004skellyspencer]]
- equals: [[#^{A}]]
^{B}
### Connections
#### C1
- endpointA: [[#^{A}]]
- endpointB: [[#^{B}]]
- exposes: [[#^{A}]]
^{C}
<!-- MDSE:LOCAL-MODEL END -->"""
        i = self.build(body)
        self.assertEqual([], i["errors"])
        self.assertIn(A, i["boundaries"])
        self.assertNotIn(B, i["boundaries"])
        self.assertEqual((A, B), i["connections"][C]["endpoints"])
        self.assertEqual([A], i["connections"][C]["exposes"])
        self.assertIn((A, B), i["equality"])
        self.assertIn((B, A), i["equality"])

    def test_duplicate_local_id_fails(self):
        body = f"""<!-- MDSE:LOCAL-MODEL START schema=0.5 -->
### Interfaces
#### J1
^{A}
#### J2
^{A}
<!-- MDSE:LOCAL-MODEL END -->"""
        self.assertTrue(any("duplicate endpoint" in e for e in self.build(body)["errors"]))

    def test_unclosed_region_fails(self):
        body = f"""<!-- MDSE:LOCAL-MODEL START schema=0.5 -->
### Interfaces
#### J1
^{A}"""
        self.assertTrue(any("unclosed" in e for e in self.build(body)["errors"]))


if __name__ == "__main__":
    unittest.main()
