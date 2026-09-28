<%*
const letters = s => String(s || "").normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/ß/g, "ss").toLowerCase().replace(/[^a-z]/g, "");
const codeFrom = (first, last) => (letters(last) + letters(first)).slice(0, 13).padEnd(13, "-");
const codeFile = ".obsidian/author-code.txt";
const adapter = tp.app.vault.adapter;
let code = "";
try { if (await adapter.exists(codeFile)) code = (await adapter.read(codeFile)).trim(); } catch (e) {}
if (!/^[a-z-]{13}$/.test(code)) {
  const first = await tp.system.prompt("First name (asked once, to create your author code)");
  const last = await tp.system.prompt("Last name");
  if (!first || !last || !codeFrom(first, last).replace(/-/g, "")) throw new Error("A first and last name are needed to create your author code.");
  const suggested = codeFrom(first, last);
  const answer = await tp.system.prompt("Your author code. Press Enter to accept it.", suggested);
  code = (answer || suggested).trim();
  if (!/^[a-z-]{13}$/.test(code)) code = suggested;
  await adapter.write(codeFile, code);
}
const used = new Set();
for (const f of tp.app.vault.getMarkdownFiles()) {
  const u = tp.app.metadataCache.getFileCache(f)?.frontmatter?.uid;
  if (u) used.add(String(u));
}
const pad = (n, l = 2) => String(n).padStart(l, "0");
const stamp = d => `${d.getFullYear()}${pad(d.getMonth() + 1)}${pad(d.getDate())}${pad(d.getHours())}${pad(d.getMinutes())}${pad(d.getSeconds())}${pad(d.getMilliseconds(), 3)}`;
let t = new Date();
while (used.has(stamp(t) + code)) t = new Date(t.getTime() + 1);
tR += stamp(t) + code;
%>