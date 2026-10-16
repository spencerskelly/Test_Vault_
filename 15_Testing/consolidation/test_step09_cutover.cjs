"use strict";
/**
 * Step 09 cutover rehearsal contract.
 * Read-only Node tests. No GitHub state changes or QEAX inspection.
 * These pins describe this candidate, not a permanent release gate.
 */
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const crypto = require("node:crypto");
const path = require("node:path");
const root = path.resolve(__dirname, "../..");
const read = p => fs.readFileSync(path.join(root,p),"utf8");
const blobSha = p => {
  const b = fs.readFileSync(path.join(root,p));
  return crypto.createHash("sha1").update(Buffer.from("blob "+b.length+"\0")).update(b).digest("hex");
};
const manifest=read("Base Vault/Definition/mdse-release.yaml");
const legacy="spencerskelly/"+"MDSE_Workbench";
const target="spencerskelly/Test_Vault_";
const ci=read(".github/workflows/mdse-monorepo-workbench-ci.yml");
const preflight=read(".github/workflows/mdse-release-alignment-preflight.yml");
test("release manifest routes exactly two governing Workbench repo fields to consolidated source",()=>{
  assert.equal((manifest.match(/(?:^\s*repo:|^\s*workbench:)\s*"spencerskelly\/Test_Vault_"/gm)||[]).length,2,
    "tools.workbench.repo and repos.workbench are the two exact governed repository fields");
  assert.match(manifest,/  workbench:\n    repo: "spencerskelly\/Test_Vault_"/);
  assert.match(manifest,/repos:\n  authority: "spencerskelly\/Test_Vault_"\n  workbench: "spencerskelly\/Test_Vault_"/);
  assert.ok(!manifest.includes(legacy),"no current legacy implementation authority in release manifest");
});
test("controlled release flags and pins retain pre-release state",()=>{
  for(const required of [
    'releaseStatus: pre-release','mdseRelease: "0.8.0"',
    '  relationships: "1.36"','  elementTypes: "1.18"','  localModel: "0.5"',
    '    version: "0.1.18"','    wb106Version: "0.1.18"',
    '    candidateVersion: null','    version: "0.3.0"'
  ])assert.ok(manifest.includes(required),"Missing release constraint "+required);
});
test("generated plugin lock stays byte-identical to pre-cutover authority",()=>{
  assert.equal(blobSha(".obsidian/plugin-lock.yaml"),"c430670577318457972a154012d08c6d28e6d11b");
});
test("current lock generator remains byte-identical",()=>{
  assert.equal(blobSha("Base Vault/Tools/v0.8.0-r2/update-plugin-lock.py"),"74f18af673263d87d123d31056251ddbab265d4b");
});
test("historical workspace decisions remain byte-identical",()=>{
  assert.equal(blobSha("00_Workspace/Workspace Decision Log.md"),"49ab9bc513b27ce7e1c2beed6e039aad5c0bebbb");
});
test("current onboarding and boundary pages no longer direct changes to standalone repo",()=>{
  for(const p of ["README.md","00_Workspace/README.md","00_Workspace/MDSE Tool Definitions and Boundaries.md",
      "00_Workspace/00 - Current State.md","55_Workbench/docs/INDEX.md",
      "55_Workbench/docs/Definition/04 - Architecture and Model Boundary.md"]){
    const content=read(p);
    assert.ok(!content.includes(legacy),"Old repository still designated by "+p);
  }
});
test("source authority name present in current release navigation",()=>{
  for(const p of ["README.md","00_Workspace/MDSE Tool Definitions and Boundaries.md","55_Workbench/docs/INDEX.md"])
    assert.ok(read(p).includes("55_Workbench/"),p);
});
test("Workbench source, plugin id and npm version stay paired",()=>{
  const pkg=JSON.parse(read("55_Workbench/package.json"));
  const plugin=JSON.parse(read("55_Workbench/manifest.json"));
  assert.equal(pkg.version,"0.1.18");assert.equal(plugin.version,"0.1.18");
  assert.equal(plugin.id,"mdse-workbench");
});
test("root CI targets monorepo with read-only credentials and no Git pushes",()=>{
  assert.ok(ci.includes("working-directory: 55_Workbench"));
  assert.match(ci,/permissions:\n  contents: read/);
  assert.ok(ci.includes("persist-credentials: false"));
  for(const cmd of ["npm ci","npm run typecheck","npm test","npm run build"])
    assert.ok(ci.includes(cmd),"Missing "+cmd);
  assert.ok(!ci.includes("git push"));
});
test("root CI checks this migration contract after setup-node",()=>{
  const setup=ci.indexOf("      - uses: actions/setup-node@v4");
  const gate=ci.indexOf("node --test 66_Testing/consolidation/test_step09_cutover.cjs");
  assert.ok(setup>=0 && gate>setup);
  assert.ok(ci.includes("working-directory: .\n        run: node --test 66_Testing/consolidation/test_step09_cutover.cjs"));
});
test("both current root workflows cover main and the exact staged branch",()=>{
  for(const [n,workflow]of [["CI",ci],["preflight",preflight]]){
    assert.match(workflow,/push:\n    branches:\n      - main\n      - consolidation\/step09-authority-ci-rehearsal-2026-10-10/);
    assert.ok(workflow.includes("      - consolidation/step08-real-tree-audit-2026-10-10"),n);
    assert.ok(!workflow.includes("integration/workbench-subtree-2026-10-09"),n);
    assert.ok(!workflow.includes("recovery/repository-consolidation-2026-10-09"),n);
  }
});
test("release alignment preflight is non-mutating and read-only",()=>{
  assert.match(preflight,/permissions:\n  contents: read/);
  assert.ok(!preflight.includes("git push"));
  assert.ok(preflight.includes("66_Testing/check_release_alignment.py"));
});
test("existing path-only authority audit still fail-closed and unmodified",()=>{
  assert.equal(blobSha("66_Testing/consolidation/audit_workbench_authority.cjs"),"e7987b9f3c49826cc9257047a80681f4cbc6c249");
});
test("QEAX archive remains outside release test access",()=>{
  const source=fs.readFileSync(__filename,"utf8");
  assert.ok(!ci.includes("unzip -j EA_2026"));
  assert.ok(!preflight.includes("unzip -j EA_2026"));
  assert.ok(source.includes("QEAX archive remains outside release test access"));
});
