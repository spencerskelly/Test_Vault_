#!/usr/bin/env node
"use strict";
const fs=require("fs"),path=require("path"),vm=require("vm");
const importer=path.resolve(__dirname,"../../Tools/v0.8.11/EA_to_MDSE_Native_Importer_v0.8.11.html");
const src=fs.readFileSync(importer,"utf8");
const a=src.indexOf("function rotr32"),b=src.indexOf("class SQLiteReader",a);
if(a<0||b<a)throw new Error("embedded streaming SHA-256 block not found");
const sandbox={Uint8Array,Uint32Array,BigInt,Number,Array,Math};
vm.createContext(sandbox);
vm.runInContext(src.slice(a,b)+";this.Hash=SHA256Stream;",sandbox);
const H=sandbox.Hash;
const empty=new H().digestHex();
const abc=new H().update(new Uint8Array([97,98,99])).digestHex();
const split=new H().update(new Uint8Array([97])).update(new Uint8Array([98,99])).digestHex();
if(empty!=="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")throw new Error("empty SHA-256 vector failed");
if(abc!=="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")throw new Error("abc SHA-256 vector failed");
if(split!==abc)throw new Error("incremental SHA-256 update failed");
for(const token of ['sha256:sourceSha256','"- Source SHA-256: "+lastReport.source.sha256','sha256:lastReport.source.sha256'])if(!src.includes(token))throw new Error("fingerprint persistence missing: "+token);
console.log("v0.8.11 source fingerprint checks: PASS");
