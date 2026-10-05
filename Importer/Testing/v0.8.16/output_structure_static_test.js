#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.16/EA_to_MDSE_Native_Importer_v0.8.16.html");
const src=fs.readFileSync(importer,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": "+t);}
function forbid(t,m){if(src.includes(t))throw new Error(m+": "+t);}
need('version: "0.8.16"',"version");
need('function buildEntityContext(ctx,reservedIdentityTokens,existingStems)',"existing vault names participate in naming");
need('const usedFileNames=new Set();',"global filename namespace");
need('usedFileNames.add(base.toLowerCase())',"existing base/system basename reservation");
need('function elementParentChain(e,entities)',"nested parent chain");
need('for(const p of parents){outSegs.push(p.fileName);changed=true;}',"parent-element folder placement");
need('e.linkTarget=e.fileName',"filename-only imported links");
need('Importer-defined total path limit: none',"manifest path policy");
need('Generated-file-count limit per folder: none',"manifest folder policy");
need('Imported note filenames globally unique:',"manifest global naming policy");
need('const FS_COMPONENT_MAX_BYTES=255;',"physical component guard retained");
forbid('const MAX_GENERATED_PATH=',"artificial total-path cap");
forbid('const LONG_PATH_REVIEW_THRESHOLD=',"long-path review threshold");
forbid('const MAX_MODEL_FILES_PER_FOLDER=',"folder file-count cap");
forbid('function applyMechanicalFolderCapacity(items)',"mechanical folder splitting");
forbid('Review - Long Paths.csv',"long-path review artifact");
forbid('folder_1',"mechanical folder bucket");
forbid('Duplicate numbering is scoped to the target folder.',"folder-scoped duplicate naming");
forbid('function assignLinkTargets(entities,existingStems)',"path-qualified imported-link fallback");
const scripts=[...src.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/gi)].map(m=>m[1]);
if(scripts.length!==1)throw new Error("expected one embedded script");
new Function(scripts[0]);
console.log("v0.8.16 output-structure regression: PASS");
