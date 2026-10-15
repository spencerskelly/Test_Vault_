import csv
import tempfile
import unittest
from pathlib import Path
from imp011_topology_acceptance import check

A = "ep-20261014130000001skellyspencer"
B = "ep-20261014130000002skellyspencer"
C = "conn-20261014130000003skellyspencer"
START = "<!-- MDSE:LOCAL-MODEL START schema=0.5 -->"
END = "<!-- MDSE:LOCAL-MODEL END -->"

class Imp011TopologySynthetic(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.csv = self.root/"99_System/11_Import/Review - Equals Direction.csv"
        self.csv.parent.mkdir(parents=True)
        self.rows = [
            dict(ea_guid="binding-equals", actual_relation="Interface.equals", owner_note="Assembly.md",
                 start_local=A, end_local=B, connection_local="", exposes_local="", candidate_connection_count="0"),
        ]
        self.write_notes()
        self.write_csv()

    def write_csv(self):
        fields = ["ea_guid","actual_relation","owner_note","start_local","end_local","connection_local","exposes_local","candidate_connection_count"]
        with self.csv.open("w", newline="", encoding="utf-8") as f:
            writer=csv.DictWriter(f,fieldnames=fields)
            writer.writeheader()
            writer.writerows(self.rows)

    def write_notes(self):
        (self.root/"Assembly.md").write_text(f"""{START}
### Interfaces
#### Boundary
- equals: [[#^{B}]]
^{A}
#### Internal
- part: [[#^part-20261014130000004skellyspencer]]
- equals: [[#^{A}]]
^{B}
### Connections
#### Wiring
- endpointA: [[#^{A}]]
- endpointB: [[#^{B}]]
- exposes: [[#^{A}]]
^{C}
{END}
""",encoding="utf-8")

    def test_valid_equals(self):
        self.assertEqual([], check(self.root))

    def test_reject_wrong_owner(self):
        self.rows[0]["owner_note"]="Other.md"
        self.write_csv()
        self.assertTrue(any("owner mismatch" in x for x in check(self.root)))

    def test_reject_missing_symmetry(self):
        content=(self.root/"Assembly.md").read_text()
        content=content.replace(f"- equals: [[#^{A}]]","- identifier: test")
        (self.root/"Assembly.md").write_text(content)
        self.assertTrue(any("symmetric" in x for x in check(self.root)))

    def test_valid_exposure(self):
        self.rows=[dict(ea_guid="binding-exposure",actual_relation="Connection.exposes",
                        owner_note="Assembly.md",start_local=A,end_local=B,
                        connection_local=C,exposes_local=A,candidate_connection_count="1")]
        self.write_csv()
        # Exposure and equality must not both be persisted; remove equality from fixture.
        text=(self.root/"Assembly.md").read_text()
        text="\n".join(line for line in text.splitlines() if not line.startswith("- equals:"))
        (self.root/"Assembly.md").write_text(text)
        self.assertEqual([], check(self.root))

    def test_reject_ambiguous_exposure(self):
        self.test_valid_exposure()
        self.rows[0]["candidate_connection_count"]="2"
        self.write_csv()
        self.assertTrue(any("ambiguous" in x for x in check(self.root)))

    def test_reject_duplicate_exposure_equals(self):
        self.rows=[dict(ea_guid="binding-exposure",actual_relation="Connection.exposes",
                        owner_note="Assembly.md",start_local=A,end_local=B,
                        connection_local=C,exposes_local=A,candidate_connection_count="1")]
        self.write_csv()
        self.assertTrue(any("also persisted" in x for x in check(self.root)))

if __name__=="__main__":
    unittest.main()
