#!/usr/bin/env python3
"""Build Bootstrap 0.3.1 in a checkout and check controlled release hashes.
Does not overwrite vendored payloads or promote versions. Requires Node/npm and dependencies access/cache.
"""
import argparse, hashlib, json, pathlib, subprocess, sys

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("root",type=pathlib.Path)
    ap.add_argument("--output",type=pathlib.Path,help="Optional local JSON report")
    a=ap.parse_args()
    root=a.root.resolve()
    src=root/"13_Bootstrap/Tools/v0.3.1"
    vend=root/"10_Base Vault/Runtime/Plugins/mdse-bootstrap"
    lock=root/".obsidian/plugin-lock.yaml"
    report={"candidate":"0.3.1","status":"BLOCKED","checks":[]}
    def check(name,passed,detail):
        report["checks"].append({"name":name,"passed":passed,"detail":str(detail)})
        return passed
    try:
        import yaml
        config=yaml.safe_load(lock.read_text())
        expected=config["plugins"]["mdse-bootstrap"]["sha256"]
        for f in ["package.json","package-lock.json","tsconfig.json","esbuild.config.mjs","src/main.ts","src/core.ts","test/core.test.ts"]:
            if not check("source:"+f,(src/f).is_file(),"present" if (src/f).is_file() else "missing"):
                raise RuntimeError("Missing build input: "+f)
        for f,digest in expected.items():
            target=vend/f
            passed=target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest()==digest
            if not check("vendored_lock:"+f,passed,"sha256 equals lock" if passed else "missing/drift"):
                raise RuntimeError("Vendored plugin hash mismatch")
        for args in (["npm","ci"],["npm","test"],["npm","run","build"]):
            run=subprocess.run(args,cwd=src,text=True,capture_output=True,timeout=180)
            detail="exit="+str(run.returncode)+" "+(run.stderr[-300:] if run.returncode else "")
            if not check(" ".join(args),run.returncode==0,detail):
                raise RuntimeError("Build/test failed: "+" ".join(args))
        built=src/"main.js"
        if not check("bundle_exists",built.is_file(),"bootstrap candidate main.js"):
            raise RuntimeError("Bundle missing")
        digest=hashlib.sha256(built.read_bytes()).hexdigest()
        locked=expected["main.js"]
        check("bundle_matches_vendored",digest==locked,"built="+digest+" locked="+locked)
        report["status"]="BUILD_AND_TEST_PASS"
        report["promotion"]="NOT_AUTOMATIC; Obsidian first-open and release manifest alignment still required"
    except Exception as ex:
        report["error"]=str(ex)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
    return 0 if report["status"]=="BUILD_AND_TEST_PASS" else 1

if __name__=="__main__":
    sys.exit(main())
