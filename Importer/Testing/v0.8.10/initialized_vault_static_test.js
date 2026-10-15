#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path");
const importer=path.resolve(__dirname,"../../Tools/v0.8.10/EA_to_MDSE_Native_Importer_v0.8.10.html");
const src=fs.readFileSync(importer,"utf8");
if(!src.includes("function vaultUidFromText"))throw new Error("vault UID parser missing");
if(!src.includes('vaultUid.toUpperCase()==="UNINITIALIZED"'))throw new Error("UNINITIALIZED destination is not rejected");
console.log("v0.8.10 initialized-vault static checks: PASS");
