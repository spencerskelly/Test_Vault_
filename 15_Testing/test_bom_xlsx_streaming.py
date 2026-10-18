"""Synthetic streaming-XLSX regression cases; no private BOM material."""
import pathlib
import sys
import tempfile
import unittest
import zipfile
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from bom_xlsx_reader import rows_from_xlsx
M="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
P="http://schemas.openxmlformats.org/package/2006/relationships"

def fixture(path,rows):
    with zipfile.ZipFile(path,"w") as z:
        z.writestr("xl/workbook.xml",f'<workbook xmlns="{M}" xmlns:r="{R}"><sheets><sheet name="BOM" sheetId="1" r:id="rId1"/></sheets></workbook>')
        z.writestr("xl/_rels/workbook.xml.rels",f'<Relationships xmlns="{P}"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
        z.writestr("xl/worksheets/sheet1.xml",f'<worksheet xmlns="{M}"><sheetData>{rows}</sheetData></worksheet>')

class Streaming(unittest.TestCase):
    def setUp(self):
        tmp=tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.p=pathlib.Path(tmp.name)/"synthetic.xlsx"
    def test_many_rows_and_last_record(self):
        rows="".join(f'<row r="{i}"><c r="A{i}" t="inlineStr"><is><t>SYN-{i}</t></is></c></row>' for i in range(1,1501))
        fixture(self.p,rows)
        source=rows_from_xlsx(self.p,"BOM")
        self.assertEqual(next(source),(1,{0:"SYN-1"}))
        remaining=list(source)
        self.assertEqual(len(remaining),1499)
        self.assertEqual(remaining[-1],(1500,{0:"SYN-1500"}))
    def test_formula_cell_is_refused(self):
        fixture(self.p,'<row r="1"><c r="A1"><f>1+1</f><v>2</v></c></row>')
        with self.assertRaisesRegex(ValueError,"FORMULA_CELL"):list(rows_from_xlsx(self.p,"BOM"))
    def test_duplicate_row_is_refused(self):
        fixture(self.p,'<row r="1"/><row r="1"/>')
        with self.assertRaisesRegex(ValueError,"DUPLICATE"):list(rows_from_xlsx(self.p,"BOM"))
    def test_empty_rows_preserve_excel_positions(self):
        fixture(self.p,'<row r="2"/><row r="7"><c r="C7"><v>2</v></c></row>')
        self.assertEqual(list(rows_from_xlsx(self.p,"BOM")),[ (2,{}),(7,{2:"2"}) ])
if __name__=="__main__":
    unittest.main()
