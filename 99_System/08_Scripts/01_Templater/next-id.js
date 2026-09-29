module.exports = async function nextId(tp, prefix, width = 4) {
  const used = new Set();
  const pattern = new RegExp(`^${prefix}-(\\d+)$`, "i");
  for (const file of tp.app.vault.getMarkdownFiles()) {
    const frontmatter = tp.app.metadataCache.getFileCache(file)?.frontmatter;
    const candidates = [frontmatter?.id];
    for (const candidate of candidates) {
      const match = String(candidate ?? "").match(pattern);
      if (match) used.add(Number(match[1]));
    }
  }
  let next = 1;
  while (used.has(next)) next += 1;
  return `${prefix}-${String(next).padStart(width, "0")}`;
};
