"use strict";
/* Step 11: verify byte-for-byte archival and absence of runnable legacy workflows.
 * Reads only eight small archived YAML files and git tree metadata; no QEAX. */
const test=require("node:test"),assert=require("node:assert/strict");
const fs=require("node:fs"),path=require("node:path"),crypto=require("node:crypto");
const {spawnSync}=require("node:child_process");
const root=path.resolve(__dirname,"../..");
const directory="55_Workbench/docs/Reference/ARCHIVE_CI_RETIRE_2026-10-10";
const originals=[
["bom-a14-source-step15.yml","b0a138ecdb46a3a74587aa0ba04997a06d930455"],
["wb128-gate3-representative-views.yml","0bdaa3b0feb5e6917f6cb42053f93ddbcac8cb06"],
["wb128-gate4-disposable-edits.yml","5afbcd3322f228889fd0ce57e66e14eb3c725598"],
["wb128-gate5-release-alignment.yml","abf0174b2af10d4f9974a584bfa12530f1721b47"],
["wb128-real-vault-acceptance.yml","44b4c93f413ccf0478b8cfb162692fc0f40b0004"],
["wb129-rehearsal.yml","7721087d6fc31cafd2390cdaa5ba8ae1fc97b09a"],
["workbench-subtree-stage.yml","3e51e09147179ffed9a24c3f19b38d8705fb6fe1"]
];
function git(...args){const p=spawnSync("git",["-C",root,...args],{encoding:"utf8"});assert.equal(p.status,0,"git "+args.join(" ")+": "+p.stderr);return p.stdout.trim();}
function blob(data){const prefix=Buffer.from("blob "+data.length+"\0");return crypto.createHash("sha1").update(prefix).update(data).digest("hex");}
for(const [name,sha]of originals) {
  test("archived original YAML SHA matches: "+name,()=>{
    const rel=directory+"/"+name,bytes=fs.readFileSync(path.join(root,rel));
    assert.equal(blob(bytes),sha);
    assert.equal(git("rev-parse","HEAD:"+rel),sha);
  });
  test("legacy workflow is absent from active Git tree: "+name,()=>{
    const listing=git("ls-tree","-r","--name-only","HEAD","--",".github/workflows");
    assert.ok(!listing.split("\n").includes(".github/workflows/"+name));
    assert.ok(!fs.existsSync(path.join(root,".github/workflows",name)));
  });
}
test("archive README marks material as nonexecutable reference",()=>{
  const body=fs.readFileSync(path.join(root,directory,"README.md"),"utf8");
  assert.match(body,/Reference-only/);
  assert.match(body,/not be copied back/);
});
test("retained root monorepo Workbench CI and release preflight exist",()=>{
  for(const name of ["mdse-monorepo-workbench-ci.yml","mdse-release-alignment-preflight.yml"])
    assert.ok(git("rev-parse","HEAD:.github/workflows/"+name).match(/^[0-9a-f]{40}$/));
});
test("root Git workflow tree contains no standalone Workbench repo checkout names",()=>{
  const legacy=["spencerskelly","MDSE_Workbench"].join("/");
  const live=git("ls-tree","-r","--name-only","HEAD","--",".github/workflows").split("\n").filter(Boolean);
  for(const p of live){
    const text=fs.readFileSync(path.join(root,p),"utf8");
    assert.ok(!text.includes(legacy),"Old repo reference remains in live workflow "+p);
  }
});
test("controlled plugin lock blob is unchanged",()=>{
  assert.equal(git("rev-parse","HEAD:.obsidian/plugin-lock.yaml"),
    "c430670577318457972a154012d08c6d28e6d11b");
});
test("pre-release target is not promoted",()=>{
  const m=git("show","HEAD:Base Vault/Definition/mdse-release.yaml");
  assert.ok(m.includes("releaseStatus: pre-release"));
  assert.ok(m.includes('  localModel: "0.5"'));
  assert.ok(m.includes('    version: "0.1.18"'));
});
