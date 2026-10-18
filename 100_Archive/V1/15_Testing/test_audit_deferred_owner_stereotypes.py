"""Synthetic stereotype boundaries for deferred aggregation audit."""
import pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from audit_deferred_owner_stereotypes import broad,typed
class TestDeferredScope(unittest.TestCase):
 def test_physical_context_is_broad_only(self):
  self.assertTrue(broad(("Class","Physical Context")))
  self.assertFalse(typed(("Class","Physical Context")))
 def test_software_component_is_not_physical_part(self):
  self.assertTrue(broad(("Class","Software Component")))
  self.assertFalse(typed(("Class","Software Component")))
 def test_system_partner_deferred(self):
  self.assertFalse(typed(("Class","System Partner")))
 def test_platform_deferred(self):
  self.assertFalse(typed(("Class","Platform")))
 def test_hardware_in_both(self):
  self.assertTrue(broad(("Class","Hardware Component")))
  self.assertTrue(typed(("Class","Hardware Component")))
 def test_interface_excluded_from_baseline(self):
  self.assertFalse(broad(("Class","Proxy Interface")))
 def test_business_line_excluded(self):
  self.assertFalse(broad(("Class","Business Line")))
if __name__=="__main__":unittest.main()
