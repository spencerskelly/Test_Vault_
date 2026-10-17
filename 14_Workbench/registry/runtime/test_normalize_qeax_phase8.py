import unittest
from normalize_qeax_phase8 import decide
class Phase8(unittest.TestCase):
 def row(self,**kw):
  x=dict(Connector_Type='Generalization',Stereotype='',Direction='Source -> Destination',Start_Object_ID=1,End_Object_ID=2,SourceIsAggregate=0,DestIsAggregate=0);x.update(kw);return x
 def test_general(self):self.assertEqual(decide(self.row(),('Class','block'),('Class','block'),set())['status'],'orientation_normalized')
 def test_reverse_composite(self):self.assertEqual(decide(self.row(Connector_Type='Aggregation',DestIsAggregate=2),('Class','block'),('Class','block'),set())['normalized_from'],2)
 def test_shared_not_composite(self):self.assertIn('SHARED_NOT_COMPOSITE',decide(self.row(Connector_Type='Aggregation',DestIsAggregate=1),('Class','block'),('Class','block'),set())['diagnostics'])
 def test_perform(self):self.assertEqual(decide(self.row(Connector_Type='Abstraction',Stereotype='allocate'),('Activity',''),('Class','block'),set())['rule'],'ALLOC-PERFORM')
 def test_exhibit(self):self.assertEqual(decide(self.row(Connector_Type='Abstraction',Stereotype='allocate'),('State',''),('Class','block'),set())['rule'],'ALLOC-EXHIBIT')
 def test_requirement_realization(self):self.assertEqual(decide(self.row(Connector_Type='Realisation'),('Class','block'),('Requirement',''),set())['normalized_from'],2)
 def test_non_part_aggregation(self):self.assertEqual(decide(self.row(Connector_Type='Aggregation',DestIsAggregate=2),('State',''),('State',''),set())['status'],'deferred_review')
 def test_unknown(self):self.assertIn('UNKNOWN_FAMILY',decide(self.row(Connector_Type='Mystery'),('Class',''),('Class',''),set())['diagnostics'])
if __name__=='__main__':unittest.main()
