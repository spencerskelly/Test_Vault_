"""Synthetic tests for the Phase 8 vs typed-candidate taxonomy boundary."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from reconcile_ea_owner_candidates import phase8_part,typed_part
class Reconciliation(unittest.TestCase):
 def test_hardware_both(self):
  self.assertTrue(phase8_part(("Class","Hardware Component")))
  self.assertTrue(typed_part(("Class","Hardware Component")))
 def test_software_old_only(self):
  self.assertTrue(phase8_part(("Class","Software Component")))
  self.assertFalse(typed_part(("Class","Software Component")))
 def test_business_line_excluded_phase8(self):
  self.assertFalse(phase8_part(("Class","Business Line")))
 def test_interface_excluded_phase8(self):
  self.assertFalse(phase8_part(("Class","Electrical & Material Interface")))
 def test_physical_context_not_typed(self):
  self.assertTrue(phase8_part(("Class","Physical Context")))
  self.assertFalse(typed_part(("Class","Physical Context")))
 def test_state_activity_not_parts(self):
  self.assertFalse(phase8_part(("State","")))
  self.assertFalse(typed_part(("Activity","function")))
if __name__=="__main__":unittest.main()
