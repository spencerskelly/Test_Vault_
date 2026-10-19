#!/usr/bin/env python3
"""Check resolved relative Markdown links in a local Git checkout. Read-only."""
from pathlib import Path
from urllib.parse import unquote
import argparse, csv, re
LINK=re.compile(r'(?<!!)\[[^\]\n]*\]\((<[^>]+>|[^)]+)\)')
def audit(root, include_archive=False):
    root=root.resolve()
    for file in sorted(root.rglob('*.md')):
        rel=file.relative_to(root)
        if not include_archive and ('100_Archive' in rel.parts or '.git' in rel.parts): continue
        try: content=file.read_text(encoding='utf8')
        except UnicodeError: continue
        for match in LINK.finditer(content):
            raw=match.group(1).strip().strip('<>')
            if raw.startswith(('http:','https:','mailto:','obsidian:','#','data:')): continue
            target=unquote(raw.split('#',1)[0].split('?',1)[0])
            if not target or '${' in target: continue
            dest=(root/target[1:] if target.startswith('/') else file.parent/target)
            yield {'file':str(rel),'line':content.count('\n',0,match.start())+1,
                   'target':raw,'status':'OK' if dest.exists() else 'BROKEN'}
def main():
    p=argparse.ArgumentParser();p.add_argument('repository');p.add_argument('--output',required=True)
    p.add_argument('--include-archive',action='store_true');a=p.parse_args()
    rows=list(audit(Path(a.repository),a.include_archive))
    with Path(a.output).open('w',encoding='utf8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=('file','line','target','status'));w.writeheader();w.writerows(rows)
    count=sum(r['status']=='BROKEN' for r in rows)
    print(f'{len(rows)} relative links checked; {count} unresolved')
    return bool(count)
if __name__=='__main__':raise SystemExit(main())
