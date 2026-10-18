"""Synthetic optional BOM evidence tests; no product or part records."""
import pathlib,sys,tempfile,zipfile,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from bom_xlsx_reader import iter_bom
M="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
P="http://schemas.openxmlformats.org/package/2006/relationships"
HEADERS=["Part","Parent","Qty","Unit","Revision","ParentRev","Variant","Config","EffectiveStart","EffectiveEnd","BomRev","Alternate"]
FIELDS=["part_number","parent_part_number","quantity","unit","part_revision","parent_revision","variant_of","configuration","effectivity_start","effectivity_end","bom_revision","alternate_group"]
class OptionalEvidenceTests(unittest.TestCase):
 def setUp(self):
  t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup)
  self.path=pathlib.Path(t.name)/"synthetic.xlsx"
  def inline(col,row,value):
   return f'<c r="{col}{row}" t="inlineStr"><is><t>{value}</t></is></c>'
  cols=list("ABCDEFGHIJKL")
  header="".join(inline(c,1,v) for c,v in zip(cols,HEADERS))
  vals=["P-A","A-A","2","pcs","B","A","P-Type","Config-1","2026-01-01","2026-12-31","4","Alt-1"]
  row="".join(inline(c,2,v) for c,v in zip(cols,vals))
  with zipfile.ZipFile(self.path,"w") as z:
   z.writestr("xl/workbook.xml",f'<workbook xmlns="{M}" xmlns:r="{R}"><sheets><sheet name="Items" sheetId="1" r:id="rId1"/></sheets></workbook>')
   z.writestr("xl/_rels/workbook.xml.rels",f'<Relationships xmlns="{P}"><Relationship Id="rId1" Target="worksheets/sheet1.xml"/></Relationships>')
   z.writestr("xl/worksheets/sheet1.xml",f'<worksheet xmlns="{M}"><sheetData><row r="1">{header}</row><row r="2">{row}</row></sheetData></worksheet>')
 def test_all_optional_values_retained_uninterpreted(self):
  mapping=dict(zip(FIELDS,HEADERS))
  record=next(iter_bom(self.path,"Items",mapping,"snap","synthetic.xlsx"))
  self.assertEqual(record.raw["variant_of"],"P-Type")
  self.assertEqual(record.raw["bom_revision"],"4")
  self.assertEqual(record.raw["alternate_group"],"Alt-1")
  self.assertEqual(record.disposition,"uninterpreted")
  self.assertEqual(record.provenance["row_number"],2)
 def test_essential_fields_only_still_supported(self):
  mapping=dict(zip(FIELDS[:4],HEADERS[:4]))
  record=next(iter_bom(self.path,"Items",mapping,"snap","synthetic.xlsx"))
  self.assertEqual(set(record.raw),set(FIELDS[:4]))
 def test_unknown_optional_mapping_rejected(self):
  mapping=dict(zip(FIELDS[:4],HEADERS[:4]))
  mapping["subtype_of"]="Variant"
  with self.assertRaises(ValueError):list(iter_bom(self.path,"Items",mapping,"snap","synthetic.xlsx"))
if __name__=="__main__":unittest.main()
