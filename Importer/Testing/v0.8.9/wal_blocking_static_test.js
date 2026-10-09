#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.9/EA_to_MDSE_Native_Importer_v0.8.9.html");
const src=fs.readFileSync(importer,"utf8");
if(!src.includes('severity:"fail",code:"SQLITE_WAL_MODE"'))throw new Error("WAL mode is not a hard failure");
if(src.includes('severity:"warn",code:"SQLITE_WAL_MODE"'))throw new Error("warning-only WAL behavior remains");
console.log("v0.8.9 WAL blocking static checks: PASS");
