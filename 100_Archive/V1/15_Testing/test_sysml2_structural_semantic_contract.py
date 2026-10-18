import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from sysml2_structural_semantic_contract import validate,workbench_view
class StructureContractTests(unittest.TestCase):
 def setUp(self):
  self.nodes=[{"id":"sys","kind":"PartDefinition"},{"id":"pt","kind":"PortDefinition"},
              {"id":"p","kind":"PartUsage","owner":"sys"},
              {"id":"port","kind":"PortUsage","owner":"p","typed_by":"pt"}]
 def test_valid_part_and_port(self): self.assertEqual(validate(self.nodes,[]),[])
 def test_port_remains_distinct_from_part(self):
  self.assertNotEqual(workbench_view("PortUsage"),workbench_view("PartUsage"))
 def test_bad_port_typing(self):
  self.nodes[-1]["typed_by"]="sys"
  self.assertIn("INVALID_TYPE",validate(self.nodes,[]))
 def test_missing_endpoint(self):
  self.assertIn("MISSING_ENDPOINT",validate(self.nodes,[{"owner":"sys","source":"p","target":"absent"}]))
 def test_definition_not_endpoint(self):
  self.assertIn("INVALID_ENDPOINT",validate(self.nodes,[{"owner":"sys","source":"sys","target":"port"}]))
 def test_connection_view(self): self.assertEqual(workbench_view("ConnectionUsage")[1],"endpoint_edge")
 def test_ownership_cycle(self):
  self.nodes[2]["owner"]="port"
  self.assertIn("OWNERSHIP_CYCLE",validate(self.nodes,[]))
 def test_invalid_multiplicity(self):
  self.nodes[2]["multiplicity"]=[3,1]
  self.assertIn("INVALID_MULTIPLICITY",validate(self.nodes,[]))
 def test_valid_unbounded_multiplicity(self):
  self.nodes[2]["multiplicity"]=[0,"*"]
  self.assertEqual(validate(self.nodes,[]),[])
 def test_unapproved_direction(self):
  self.assertIn("INVALID_DIRECTION",validate(self.nodes,[{"owner":"sys","source":"p","target":"port","direction":"guessed"}]))
 def test_blank_provenance(self):
  self.nodes[2]["source_ref"]="  "
  self.assertIn("INVALID_PROVENANCE",validate(self.nodes,[]))
 def test_invalid_connection_owner_kind(self):
  self.assertIn("INVALID_CONNECTION_OWNER_KIND",validate(self.nodes,[{"owner":"pt","source":"p","target":"port"}]))

if __name__=="__main__":unittest.main()
