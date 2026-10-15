#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src=fs.readFileSync(importer,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": "+t);}
function forbid(t,m){if(src.includes(t))throw new Error(m+": "+t);}
need("prefer the stronger Connection.exposes topology only when one boundary Interface","planner exposure precedence contract");
need("if(aBoundary&&!bBoundary){outer=a;inner=b;}","boundary/internal detection A");
need("else if(bBoundary&&!aBoundary){outer=b;inner=a;}","boundary/internal detection B");
need("if(candidates.length===1){","single internal Connection requirement");
need("conn.exposesRefs.push(outer)","Connection owns exposes");
need("- exposes: ","render exposes");
need("exposes target is not an assembly-boundary Interface","exposes validator");
need("otherwise preserve an explicit same-owner BindingConnector as one canonical symmetric","canonical equals fallback");
need("cross-owner/unresolved bindings remain review-only","cross-owner binding guard");
forbid("temporary equals/review evidence retained.","temporary equals semantics removed");
const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0)throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.19 exposes regression: PASS");
