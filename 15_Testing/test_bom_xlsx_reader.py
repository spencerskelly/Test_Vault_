"""Synthetic XLSX adapter checks with an in-memory minimal OOXML workbook."""
import pathlib,sys,tempfile,unittest,zipfile
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from bom_xlsx_reader import iter_bom, rows_from_xlsx
M="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
P="http://schemas.openxmlformats.org/package/2006/relationships"
C={"part_number":"Part Number","parent_part_number":"Parent","quantity":"Qty","unit":"UoM"}

class BomXlsxTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup)
  self.path=pathlib.Path(t.name)/"synthetic.xlsx"
  workbook=f'<workbook xmlns="{M}" xmlns:r="{R}"><sheets><sheet name="BOM" sheetId="1" r:id="rId1"/></sheets></workbook>'
  rels=f'<Relationships xmlns="{P}"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>'
  rows='<row r="1">'+''.join(f'<c r="{col}1" t="inlineStr"><is><t>{head}</t></is></c>' for col,head in zip("ABCD",C.values()))+'</row>'
  rows+='<row r="2"><c r="A2" t="inlineStr"><is><t>PART-001</t></is></c><c r="B2" t="inlineStr"><is><t>ASSEMBLY-001</t></is></c><c r="C2"><v>2.5</v></c><c r="D2" t="inlineStr"><is><t>m</t></is></c></row>'
  rows+='<row r="3"/>'
  rows+='<row r="4"><c r="A4" t="inlineStr"><is><t>PART-002</t></is></c></row>'
  with zipfile.ZipFile(self.path,"w") as z:
   z.writestr("xl/workbook.xml",workbook)
   z.writestr("xl/_rels/workbook.xml.rels",rels)
   z.writestr("xl/worksheets/sheet1.xml",f'<worksheet xmlns="{M}"><sheetData>{rows}</sheetData></worksheet>')
 def test_read_and_preserve(self):
  items=list(iter_bom(self.path,"BOM",C,"s","synthetic.xlsx"))
  self.assertEqual(len(items),2)
  self.assertEqual(items[0].raw["quantity"],"2.5")
  self.assertEqual(items[0].raw["unit"],"m")
  self.assertEqual(items[0].raw["parent_part_number"],"ASSEMBLY-001")
  self.assertEqual(items[1].provenance["row_number"],4)
 def test_missing_sheet(self):
  with self.assertRaises(ValueError):list(rows_from_xlsx(self.path,"Unknown"))
 def test_missing_header(self):
  with self.assertRaises(ValueError):list(iter_bom(self.path,"BOM",{**C,"unit":"Other"},"s","f"))
 def test_no_implicit_column_mapping(self):
  with self.assertRaises(ValueError):list(iter_bom(self.path,"BOM",{"part_number":"Part Number"},"s","f"))
 def test_empty_row_skipped(self):
  self.assertEqual([n for n,v in rows_from_xlsx(self.path,"BOM")],[1,2,3,4])
  self.assertEqual(len(list(iter_bom(self.path,"BOM",C,"s","f"))),2)
if __name__=="__main__":unittest.main()
