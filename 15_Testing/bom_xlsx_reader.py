"""Read-only XLSX BOM row adapter, without inventing relationships or units."""
from decimal import Decimal, InvalidOperation
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zipfile import ZipFile, BadZipFile
from source_evidence_contract import bom_envelope

NS={"m":"http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r":"http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "p":"http://schemas.openxmlformats.org/package/2006/relationships"}
CELL=re.compile(r"^([A-Z]+)([0-9]+)$")

def column_index(reference):
    match=CELL.fullmatch(reference)
    if not match: raise ValueError("INVALID_CELL_REFERENCE")
    n=0
    for letter in match.group(1):n=n*26+ord(letter)-64
    return n-1

def text_cell(cell,strings):
    kind=cell.get("t")
    if cell.find("m:f",NS) is not None:
        raise ValueError("FORMULA_CELL_REQUIRES_EXPLICIT_CACHED_VALUE_REVIEW")
    if kind=="inlineStr":return "".join(t.text or "" for t in cell.findall(".//m:is/m:t",NS))
    v=cell.find("m:v",NS)
    if v is None:return None
    if kind=="s":
        idx=int(v.text)
        return strings[idx]
    return v.text

def rows_from_xlsx(path,sheet_name):
    """Yield (Excel row number, mapping of zero-based column indexes to original values)."""
    with ZipFile(Path(path),"r") as z:
        workbook=ET.fromstring(z.read("xl/workbook.xml"))
        rels=ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        targets={r.get("Id"):r.get("Target") for r in rels}
        sheet=next((s for s in workbook.findall("m:sheets/m:sheet",NS) if s.get("name")==sheet_name),None)
        if sheet is None:raise ValueError("WORKSHEET_NOT_FOUND")
        target=targets[sheet.get("{"+NS["r"]+"}id")]
        target=target.lstrip("/") if target.startswith("/") else "xl/"+target
        if ".." in Path(target).parts:raise ValueError("UNSAFE_WORKSHEET_TARGET")
        strings=[]
        if "xl/sharedStrings.xml" in z.namelist():
            root=ET.fromstring(z.read("xl/sharedStrings.xml"))
            strings=["".join(t.text or "" for t in si.findall(".//m:t",NS)) for si in root.findall("m:si",NS)]
        with z.open(target) as stream:
            # Stream one worksheet row at a time; do not construct a full sheet tree.
            # Shared strings remain workbook-scoped and may need a separate
            # large-workbook strategy if their table is itself enormous.
            row_tag="{"+NS["m"]+"}row"
            last_row=0
            for event,node in ET.iterparse(stream,events=("end",)):
                if node.tag!=row_tag:continue
                row_num=int(node.get("r"))
                if row_num<=last_row:raise ValueError("INVALID_OR_DUPLICATE_EXCEL_ROW")
                last_row=row_num
                vals={column_index(c.get("r")):text_cell(c,strings)
                      for c in node.findall("m:c",NS)}
                node.clear()
                yield row_num,vals

def iter_bom(path,sheet,columns,snapshot_id,workbook_id,header_row=1):
    """columns is explicit field name -> Excel header text, no guessed synonyms."""
    required={"part_number","parent_part_number","quantity","unit"}
    optional={"part_revision","parent_revision","variant_of","configuration","effectivity_start","effectivity_end","bom_revision","alternate_group"}
    if not required.issubset(columns) or set(columns)-required-optional:
        raise ValueError("INVALID_BOM_FIELD_MAPPING")
    if len(set(columns.values()))!=len(columns):raise ValueError("DUPLICATE_COLUMN_MAPPING")
    header=None
    for row_number,raw in rows_from_xlsx(path,sheet):
        if row_number<header_row:continue
        if row_number==header_row:
            header={str(v).strip():i for i,v in raw.items() if v is not None}
            missing=set(columns.values())-set(header)
            if missing:raise ValueError("BOM_HEADERS_MISSING: "+",".join(sorted(missing)))
            continue
        if header is None:raise ValueError("HEADER_ROW_NOT_FOUND")
        values={field:raw.get(header[title]) for field,title in columns.items()}
        # All optional fields remain uninterpreted original source strings.
        # A variant marker is evidence, NOT automatic subtypeOf/variantOf acceptance.
        if all(v is None or str(v).strip()=="" for v in values.values()):continue
        if not values["part_number"]:raise ValueError("BOM_PART_NUMBER_MISSING_ROW_"+str(row_number))
        quantity=values["quantity"]
        if quantity not in (None,""):
            try:
                if not Decimal(str(quantity)).is_finite():raise ValueError()
            except (InvalidOperation,ValueError):raise ValueError("INVALID_BOM_QUANTITY_ROW_"+str(row_number))
        yield bom_envelope(snapshot_id,"bom_line",f"{sheet}:{row_number}",values,
                           workbook_id,sheet,row_number)
