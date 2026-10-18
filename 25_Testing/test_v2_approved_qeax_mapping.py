import pathlib,sqlite3,sys,tempfile,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"21_Importer"))
from review_approved_qeax_mapping import inspect

class GroupingTests(unittest.TestCase):
 def test_rows_without_diagram_dependencies(self):
  with tempfile.TemporaryDirectory() as folder:
   file=pathlib.Path(folder)/"fixture.qeax"
   with sqlite3.connect(file) as db:
    db.execute("CREATE TABLE t_object (Object_Type TEXT,Stereotype TEXT)")
    db.execute("CREATE TABLE t_connector (Connector_Type TEXT,Stereotype TEXT)")
    db.execute("CREATE TABLE t_package (Package_ID INTEGER)")
    db.executemany("INSERT INTO t_object VALUES (?,?)",[("Class","block"),("InformationItem",""),("Boundary",""),("Class","strange")])
    db.executemany("INSERT INTO t_connector VALUES (?,?)",[("Generalization",""),("Realisation","deriveReqt"),("Sequence",""),("Alien","")])
    db.execute("INSERT INTO t_package VALUES (1)")
   first=inspect(file)
   self.assertEqual(first["counts"]["unknown_element_family_rows"],1)
   self.assertEqual(first["counts"]["unknown_connector_family_rows"],1)
   self.assertEqual(first["approved_family_counts"]["connector:Realisation:deriveReqt"],1)
   self.assertEqual(first["dispositions"]["element:aggregate_boundary_note"],1)
   self.assertEqual(first["native_declarations_emitted"],0)
   with sqlite3.connect(file) as db:
    db.execute("CREATE TABLE t_diagram (id INTEGER)")
    db.execute("INSERT INTO t_diagram VALUES (999)")
   self.assertEqual(inspect(file),first)

if __name__=="__main__":unittest.main()
