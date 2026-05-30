// Build-time thumbnail fetcher (web-only, pipeline untouched).
// Source posts hotlink media on pbs.twimg.com / redd.it which 404s once the post
// is deleted or the CDN expires. Hotlinking at runtime = broken images. Instead
// we snapshot every report's `thumbnail:` to public/thumbs/ at build time and
// emit a manifest mapping original-URL -> local path (or false if it 404'd).
// Home.astro reads the manifest and only renders an <img> when the local file
// exists — so the front page never shows a broken image, and what it does show
// is frozen in the repo. Cached across builds (skips already-downloaded files).
import { readdir, readFile, writeFile, mkdir, access, stat } from "node:fs/promises";
import { createHash } from "node:crypto";
import path from "node:path";

const REPORTS = path.resolve("../content/reports");
const OUT_DIR = path.resolve("public/thumbs");
const MANIFEST = path.resolve("src/lib/thumbs-manifest.json");
const UA = "Mozilla/5.0 (compatible; SDR-build/1.0)";

async function collectUrls() {
  const urls = new Set();
  let days;
  try { days = await readdir(REPORTS); } catch { return []; }
  for (const day of days) {
    const dir = path.join(REPORTS, day);
    let files;
    try {
      if (!(await stat(dir)).isDirectory()) continue;
      files = await readdir(dir);
    } catch { continue; }
    for (const f of files) {
      if (!f.endsWith(".md")) continue;
      const txt = await readFile(path.join(dir, f), "utf8");
      const m = txt.match(/^thumbnail:\s*(\S+)\s*$/m);
      if (m) urls.add(m[1].trim());
    }
  }
  return [...urls];
}

async function tryFetch(url) {
  const candidates = [url];
  // pbs.twimg.com/media/<id>.jpg often 404s but the ?format= variant can resolve.
  const tw = url.match(/^(https:\/\/pbs\.twimg\.com\/media\/[^.?]+)\.(jpg|png)$/);
  if (tw) candidates.push(`${tw[1]}?format=${tw[2]}&name=medium`);
  for (const u of candidates) {
    try {
      const res = await fetch(u, { signal: AbortSignal.timeout(15000), headers: { "user-agent": UA } });
      if (!res.ok) continue;
      const buf = Buffer.from(await res.arrayBuffer());
      if (buf.length > 800) return { buf, ct: (res.headers.get("content-type") || "").toLowerCase() };
    } catch { /* try next candidate */ }
  }
  return null;
}

const extFor = (ct, url) =>
  ct.includes("png") ? "png" : ct.includes("webp") ? "webp" :
  ct.includes("gif") ? "gif" : /\.png(\?|$)/.test(url) ? "png" : "jpg";

await mkdir(OUT_DIR, { recursive: true });

let prev = {};
try { prev = JSON.parse(await readFile(MANIFEST, "utf8")); } catch { /* first run */ }

const urls = await collectUrls();
const manifest = {};
let dl = 0, cached = 0, fail = 0;

for (const url of urls) {
  // Reuse a prior successful download if the file is still on disk.
  if (prev[url]) {
    try {
      await access(path.join("public", prev[url].replace(/^\//, "")));
      manifest[url] = prev[url];
      cached++;
      continue;
    } catch { /* file gone — refetch */ }
  }
  const got = await tryFetch(url);
  if (!got) { manifest[url] = false; fail++; continue; }
  const name = createHash("sha1").update(url).digest("hex").slice(0, 16) + "." + extFor(got.ct, url);
  await writeFile(path.join(OUT_DIR, name), got.buf);
  manifest[url] = "/thumbs/" + name;
  dl++;
}

await writeFile(MANIFEST, JSON.stringify(manifest));
const ok = dl + cached;
console.log(`[thumbs] ${ok}/${urls.length} available (${dl} new, ${cached} cached, ${fail} dead)`);
