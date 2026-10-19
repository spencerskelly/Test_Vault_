#!/usr/bin/env python3
"""STEP-03J approved-family annotation: source graph in, staged graph out.

No native SysML emission. No diagrams. Keeps every original row and connector.
"""
import argparse
import importlib.util
import json
from pathlib import Path

def load_resolver(repo_root):
    path=Path(repo_root)/"21_Importer/v2_approved_family_resolver.py"
    spec=importlib.util.spec_from_file_location("approved_family_resolver",path)
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def annotate(nodes_file, edges_file, output_dir, repo_root):
    src_paths=[Path(nodes_file).resolve(),Path(edges_file).resolve()]
    out=Path(output_dir).resolve()
    if out.exists() and any(out.iterdir()):
        raise ValueError("Output directory not empty")
    if any(out == p or out in p.parents for p in src_paths):
        raise ValueError("Output overlaps source")
    resolver=load_resolver(repo_root)
    registry=resolver.load_registry(Path(repo_root)/"24_Workbench/registry/sysml_v2_approved_family_resolver.v0.1.json")
    # Preserve no-auto-emission gate even if a registry is modified later.
    if registry["metadata"]["automatic_native_emission"] or registry["metadata"]["ea_diagrams_enabled"]:
        raise ValueError("Unsafe registry")
    staged=[]; counts={"nodes":0,"edges":0,"flagNote":0,"flagLink":0,"element_outliers":0,"relationship_outliers":0}
    for filename, is_edge in ((src_paths[0],False),(src_paths[1],True)):
        result=[]
        with filename.open(encoding="utf8") as stream:
            for line in stream:
                if not line.strip(): continue
                record=json.loads(line)
                raw=(record.get("sourceData") if is_edge else record.get("source")) or {}
                row=raw.get("row") or {}
                ea_type=str(row.get("Connector_Type" if is_edge else "Object_Type") or "")
                stereotype=str(row.get("Stereotype") or "")
                if not ea_type:
                    resolution={"status":"review_required","reason":"MISSING_EA_TYPE","emission_authorized":False}
                else:
                    resolution=(resolver.resolve_connector if is_edge else resolver.resolve_element)(ea_type,stereotype,registry=registry)
                record["approvedFamilyReview"]=resolution
                # All families are uncertified at row level; attach flags only for unknown families.
                if resolution["status"]=="review_required":
                    kind="flagLink" if is_edge else "flagNote"
                    previous=record.get(kind)
                    note={"reason":resolution["reason"],"sourceFamily":ea_type+(":"+stereotype if stereotype else "")}
                    record[kind]=(previous if isinstance(previous,list) else ([previous] if previous else []))+[note]
                    counts[kind]+=1
                    counts["relationship_outliers" if is_edge else "element_outliers"]+=1
                counts["edges" if is_edge else "nodes"]+=1
                result.append(json.dumps(record,ensure_ascii=False,default=str)+"\n")
        staged.append(result)
    out.mkdir(parents=True,exist_ok=True)
    for name, lines in zip(("nodes.jsonl","edges.jsonl"),staged):
        (out/name).write_text("".join(lines),encoding="utf8")
    (out/"annotation_summary.json").write_text(json.dumps({"status":"family_staged_native_uncertified",**counts},indent=2)+"\n",encoding="utf8")
    return counts

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("nodes_jsonl");parser.add_argument("edges_jsonl");parser.add_argument("output_dir")
    parser.add_argument("--repo-root",default=str(Path(__file__).resolve().parents[1]))
    args=parser.parse_args()
    print(json.dumps(annotate(args.nodes_jsonl,args.edges_jsonl,args.output_dir,args.repo_root),indent=2))
