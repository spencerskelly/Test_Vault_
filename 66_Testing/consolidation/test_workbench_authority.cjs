"use strict";
const test=require("node:test"),assert=require("node:assert/strict");
const fs=require("node:fs"),os=require("node:os"),path=require("node:path");
const {spawnSync}=require("node:child_process");
const {LEGACY,classify,classifyPaths,gitTrackedMatches,audit}=require("./audit_workbench_authority.cjs");
const cases=[
 ["Base Vault/Definition/mdse-release.yaml","blocking"],
 ["README.md","blocking"],
 ["00_Workspace/00 - Current State.md","blocking"],
 ["00_Workspace/MDSE Tool Definitions and Boundaries.md","blocking"],
 ["55_Workbench/README.md","blocking"],
 [".github/workflows/old-release.yml","blocking"],
 [".github/workflows/legacy-checkout.yaml","blocking"],
 ["Importer/Tools/v0.8.19/build.py","blocking"],
 ["55_Workbench/src/main.ts","blocking"],
 ["Bootstrap/Tools/v0.3.1/start.js","blocking"],
 ["66_Testing/unknown_rule.json","blocking"],
 ["00_Workspace/GitHub Consolidation Step 18 Obsidian UI Acceptance Handoff 2026-10-09.md","historical"],
 ["00_Workspace/Consolidation Step 04 - Repository Authority and CI Transition Audit 2026-10-10.md","historical"],
 ["00_Workspace/History/Retired Documents/old.md","historical"],
 ["Importer/History/old.js","historical"],
 ["55_Workbench/docs/Reference/ARCHIVE_WB106_RUNTIME_BUILD.yml","historical"],
 ["55_Workbench/docs/bom/a01-a14/BOM_RUN_LOG.md","historical"],
 ["66_Testing/check_release_alignment.py","detector"],
 ["66_Testing/consolidation/audit_workbench_authority.cjs","detector"],
 ["66_Testing/consolidation/test_workbench_authority.cjs","detector"],
 ["00_Workspace/Unexpected New SOP.md","needs_review"],
 ["55_Workbench/docs/Definition/Current Ownership.md","needs_review"],
 ["99_System/10_Docs/Current Modeling.md","needs_review"],
 ["foo\\bar\\manual.md","needs_review"],
];
for(const [p,k] of cases)test("classifies "+p,()=>assert.equal(classify(p),k));
test("deduplicates and orders results",()=>{const x=classifyPaths(["README.md","00_Workspace/History/old.md","README.md"]);assert.deepEqual(x.blocking,["README.md"]);assert.deepEqual(x.historical,["00_Workspace/History/old.md"]);});
function fixture(map){const root=fs.mkdtempSync(path.join(os.tmpdir(),"mdse-audit-"));const git=(...args)=>{const r=spawnSync("git",["-C",root,...args],{encoding:"utf8"});if(r.status!==0)throw Error(`${args.join(" ")}: ${r.stderr}`);};git("init","-q");git("config","user.email","audit@example.invalid");git("config","user.name","Audit Test");for(const [p,s]of Object.entries(map)){const f=path.join(root,p);fs.mkdirSync(path.dirname(f),{recursive:true});fs.writeFileSync(f,s);}git("add","-A");return {root,git,clean:()=>fs.rmSync(root,{recursive:true,force:true})};}
test("historical-only archive references are nonblocking",()=>{const f=fixture({"00_Workspace/History/history.md":LEGACY,"00_Workspace/Consolidation Step 06 - audit.md":LEGACY});try{const x=audit(f.root);assert.equal(x.strictReady,true);assert.equal(x.counts.historical,2);}finally{f.clean();}});
test("active CI reference fails strict readiness even alongside historical citation",()=>{const f=fixture({".github/workflows/wb.yml":LEGACY,"00_Workspace/History/old.md":LEGACY});try{const x=audit(f.root);assert.equal(x.strictReady,false);assert.equal(x.counts.blocking,1);assert.equal(x.counts.historical,1);}finally{f.clean();}});
test("unknown current guidance fails closed as needs_review",()=>{const f=fixture({"99_System/10_Docs/Current Guidance.md":LEGACY});try{const x=audit(f.root);assert.equal(x.strictReady,false);assert.equal(x.counts.needs_review,1);}finally{f.clean();}});
test("detector literal is not confused with execution dependency",()=>{const f=fixture({"66_Testing/check_release_alignment.py":LEGACY});try{const x=audit(f.root);assert.equal(x.strictReady,true);assert.equal(x.counts.detector,1);}finally{f.clean();}});
test("untracked file is outside declared Git-tracked scan",()=>{const f=fixture({"00_Workspace/History/archive.md":LEGACY});try{fs.mkdirSync(path.join(f.root,"untracked"));fs.writeFileSync(path.join(f.root,"untracked","new.py"),LEGACY);assert.equal(gitTrackedMatches(f.root).length,1);}finally{f.clean();}});
test("case-sensitive exact repo term does not match lookalikes",()=>{const f=fixture({"README.md":"spencerskelly/mdse_workbench"});try{assert.deepEqual(gitTrackedMatches(f.root),[]);assert.equal(audit(f.root).strictReady,true);}finally{f.clean();}});
test("positive tracked file containing full legacy repo name matched",()=>{const f=fixture({"README.md":"authority: "+LEGACY});try{assert.deepEqual(gitTrackedMatches(f.root),["README.md"]);}finally{f.clean();}});
test("leading dot relative path is normalized",()=>assert.equal(classify("./README.md"),"blocking"));
