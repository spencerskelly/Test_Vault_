#!/usr/bin/env python3
"""Source-faithful interim QEAX -> Obsidian notes; NO SysML-v2 certification or diagrams."""
import argparse, collections, hashlib, json, sqlite3
from pathlib import Path

def go(qeax, out):
    src, dst = Path(qeax).resolve(), Path(out).resolve()
    if src == dst or src in dst.parents or (dst.exists() and any(dst.iterdir())):
        raise ValueError("Output must be new/empty and outside source")
    with src.open("rb") as f: sha = hashlib.file_digest(f, "sha256").hexdigest()
    db = sqlite3.connect(src.as_uri()+"?mode=ro", uri=True)
    db.row_factory = sqlite3.Row
    try:
        objs = [dict(r) for r in db.execute("SELECT Object_ID,ea_guid,Name,Alias,Object_Type,Stereotype,Note,ParentID,Package_ID FROM t_object ORDER BY Object_ID")]
        edges = [dict(r) for r in db.execute("SELECT Connector_ID,ea_guid,Name,Connector_Type,Stereotype,Start_Object_ID,End_Object_ID,Notes FROM t_connector ORDER BY Connector_ID")]
        docs = [dict(r) for r in db.execute("SELECT ElementID,ElementType,DocType FROM t_document")]
    finally: db.close()
    by_id = {x["Object_ID"]: x for x in objs}
    if not by_id or len(by_id) != len(objs): raise ValueError("Empty or duplicate element identities")
    if len(set(x["Connector_ID"] for x in edges)) != len(edges): raise ValueError("Duplicate connector identities")
    if any(x["Start_Object_ID"] not in by_id or x["End_Object_ID"] not in by_id for x in edges):
        raise ValueError("Missing connector endpoint")
    graph = collections.defaultdict(list)
    for e in edges:
        graph[e["Start_Object_ID"]].append((e,"out",e["End_Object_ID"]))
        graph[e["End_Object_ID"]].append((e,"in",e["Start_Object_ID"]))
    elem = dst/"10_Elements"; review = dst/"90_Review"
    elem.mkdir(parents=True,exist_ok=True); review.mkdir(exist_ok=True)
    artifacts = [o for o in objs if o["Object_Type"] == "Artifact"]
    generated = [o for o in objs if o["Object_Type"] != "Artifact"]
    def ref(oid):
        o=by_id[oid]
        name=str(o["Name"] or o["Alias"] or o["Object_Type"] or "Unnamed").replace("|","/").replace("]","")
        return ("[[90_Review/Attachment_Ownership|Artifact "+str(oid)+": "+name+"]]" if o["Object_Type"]=="Artifact" else "[[EA-"+str(oid)+"|"+name+"]]")
    for o in generated:
        oid=o["Object_ID"]
        lines=["---","eaGUID: "+json.dumps(o["ea_guid"]),"eaObjectID: "+str(oid),
               "eaType: "+json.dumps(o["Object_Type"]),"eaStereotype: "+json.dumps(o["Stereotype"] or ""),
               "eaPackageID: "+str(o["Package_ID"] or 0),"eaParentID: "+str(o["ParentID"] or 0),
               "sysmlV2Certified: false","sourceRepresentation: interim","---","",
               "# "+str(o["Name"] or o["Alias"] or o["Object_Type"] or oid).replace("\n"," " ),""]
        if o["Note"]: lines += ["## EA description","",str(o["Note"]),""] 
        if o["ParentID"] in by_id: lines += ["## Parent","",ref(o["ParentID"]),""] 
        if graph[oid]:
            lines += ["## EA relationships (source-faithful; native mapping pending)",""]
            for e,direction,other in graph[oid]:
                family=str(e["Connector_Type"] or "")+(":"+str(e["Stereotype"]) if e["Stereotype"] else "")
                lines.append("- **"+family+"** ("+direction+"; EA connector "+str(e["Connector_ID"])+"): "+ref(other))
            lines.append("")
        (elem/("EA-"+str(oid)+".md")).write_text("\n".join(lines)+"\n",encoding="utf-8")
    parent_refs=0; unassigned=0
    for o in artifacts:
        parent=o["ParentID"]
        if parent in by_id and by_id[parent]["Object_Type"]!="Artifact":
            with (elem/("EA-"+str(parent)+".md")).open("a",encoding="utf-8") as f:
                f.write("\n## EA attachment candidate (metadata only)\n\n- Artifact "+str(o["Object_ID"])+": "+str(o["Name"] or "Unnamed")+" (GUID `"+str(o["ea_guid"])+"`)\n")
            parent_refs+=1
        else: unassigned+=1
    index=["# Artifact ownership review index","",
           "Artifact records are references, not new notes. Connector family is not proof of ownership.",""]
    for o in artifacts:
        oid=o["Object_ID"]
        index += ["## Artifact "+str(oid)+": "+str(o["Name"] or "Unnamed"),
                  "- GUID: `"+str(o["ea_guid"])+"`; kind: `"+str(o["Stereotype"] or "")+"`"]
        if o["ParentID"] in by_id and by_id[o["ParentID"]]["Object_Type"]!="Artifact":
            index.append("- Parent candidate: "+ref(o["ParentID"]))
        else:index.append("- Parent candidate: none")
        for e,direction,other in graph[oid]:
            index.append("- EA connector "+str(e["Connector_ID"])+", "+str(e["Connector_Type"] or "")+":"+str(e["Stereotype"] or "")+", "+direction+" -> "+ref(other))
        index.append("")
    (review/"Attachment_Ownership.md").write_text("\n".join(index)+"\n",encoding="utf-8")
    (review/"Embedded_Documents.md").write_text("# Embedded EA document references\n\n"+"\n".join("- ElementID `"+str(d["ElementID"])+"`, type `"+str(d["ElementType"])+"`, DocType `"+str(d["DocType"])+"`" for d in docs)+"\n",encoding="utf-8")
    summary={"status":"interim_navigable_notes_generated","source_sha256":sha,
             "source_elements":len(objs),"source_connectors":len(edges),"generated_element_notes":len(generated),
             "artifacts_total":len(artifacts),"artifacts_as_separate_notes":0,
             "artifacts_linked_to_parent_notes":parent_refs,"artifacts_in_review":unassigned,
             "embedded_document_records":len(docs),"diagram_imported":False,
             "sysml_v2_native_certified":False}
    (dst/"import_summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    (dst/"README.md").write_text("# Interim source-faithful MDSE note vault\n\nNot a golden import. Model notes in 10_Elements, artifact evidence in 90_Review. EA diagrams excluded. Package elements are temporarily represented as notes rather than validated folder structure. SysML v2 semantics are not certified.\n",encoding="utf-8")
    return summary

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("qeax");parser.add_argument("output_dir")
    a=parser.parse_args()
    print(json.dumps(go(a.qeax,a.output_dir),indent=2))
