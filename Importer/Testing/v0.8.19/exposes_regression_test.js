#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.19/EA_to_MDSE_Native_Importer_v0.8.19.html");
const src=fs.readFileSync(importer,"utf8");
function need(t,m){if(!src.includes(t))throw new Error(m+": "+t);}
function forbid(t,m){if(src.includes(t))throw new Error(m+": "+t);}
need("BindingConnector is resolved inside Local Model 0.4 as Connection exposes -> boundary Interface when deterministic","planner exposure contract");
need("if(aBoundary&&!bBoundary){outer=a;inner=b;}","boundary/internal detection A");
need("else if(bBoundary&&!aBoundary){outer=b;inner=a;}","boundary/internal detection B");
need("if(candidates.length===1){","single internal Connection requirement");
need("conn.exposesRefs.push(outer)","Connection owns exposes");
need("- exposes: ","render exposes");
need("exposes target is not an assembly-boundary Interface","exposes validator");
need("equals is temporary review evidence only for a genuine boundary-to-internal","equals scope");
need("no exposes or equals relationship invented","non-exposure binding guard");
forbid("could not be deterministically resolved to one internal Connection exposure; temporary equals/review evidence retained.","old broad equals fallback");
const s1=src.indexOf("<script>"),s2=src.lastIndexOf("</script>");
if(s1<0||s2<0)throw new Error("embedded script missing");
new Function(src.slice(s1+8,s2));
console.log("v0.8.19 exposes regression: PASS");
