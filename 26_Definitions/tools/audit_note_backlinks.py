#!/usr/bin/env python3
"""Read-only preflight for consolidating a Markdown note without breaking references.

Use: python3 26_Definitions/tools/audit_note_backlinks.py "path/to/source.md"
This tool never moves, rewrites, retires or deletes files.
"""
import argparse,hashlib,json,pathlib,subprocess,urllib.parse

ROOT=pathlib.Path(__file__).resolve().parents[2]
TEXT_EXTS={".md",".yaml",".yml",".json",".jsonc",".canvas",".base",".py",".mjs",".js",".ts",".html",".css",".txt"}

def tracked(root):
    p=subprocess.run(["git","ls-files","-z"],cwd=root,capture_output=True,check=True)
    return [pathlib.Path(x.decode("utf-8")) for x in p.stdout.split(b"\0") if x]

def scan(root,source,files):
    source=pathlib.Path(source)
    if source.is_absolute() or ".." in source.parts:raise ValueError("SOURCE_MUST_BE_SAFE_REPOSITORY_RELATIVE")
    file=root/source
    if not file.is_file():raise ValueError("SOURCE_NOT_FOUND")
    raw=file.read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    source_rel=source.as_posix()
    encoded="/".join(urllib.parse.quote(part,safe="") for part in source.parts)
    name=source.name
    stem=source.stem
    exact_refs=[]
    possible_refs=[]
    duplicates=[]
    for rel in files:
        path=root/rel
        if not path.is_file() or rel==source:continue
        if rel.suffix.lower()==".md" and hashlib.sha256(path.read_bytes()).hexdigest()==digest:
            duplicates.append(rel.as_posix())
        if rel.suffix.lower() not in TEXT_EXTS:continue
        try:body=path.read_text(encoding="utf-8")
        except (UnicodeDecodeError,OSError):continue
        exact=[s for s in (source_rel,encoded) if s in body]
        if exact:exact_refs.append({"file":rel.as_posix(),"kind":"explicit_path","matched":exact})
        elif name in body or ("[["+stem in body) or ("[["+name in body):
            possible_refs.append({"file":rel.as_posix(),"kind":"basename_or_wikilink_review"})
    return {
        "schema":"mdse-v2-safe-note-consolidation-audit/1",
        "source":source_rel,
        "sha256":digest,
        "identical_content_candidates":sorted(duplicates),
        "explicit_inbound_references":exact_refs,
        "possible_inbound_references":possible_refs,
        "status":"REVIEW_REQUIRED_NO_AUTOMATIC_MUTATION",
        "limitations":[
            "Dynamic code references and external vaults are not exhaustively detectable",
            "YAML IDs/aliases, Obsidian resolutions, Canvas/Bases references and external links need manual confirmation",
            "An empty reference list is not permission to delete or rename"
        ]
    }

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("source",help="repo-relative note path")
    ap.add_argument("--root",type=pathlib.Path,default=ROOT)
    args=ap.parse_args()
    try:
        report=scan(args.root.resolve(),args.source,tracked(args.root.resolve()))
        print(json.dumps(report,indent=2))
    except (ValueError,subprocess.CalledProcessError,OSError) as e:
        print(json.dumps({"status":"BLOCKED","reason":str(e)}))
        raise SystemExit(1)
