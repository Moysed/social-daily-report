import { getCollection } from "astro:content";
import type { APIRoute } from "astro";

// Pull bullets from a named markdown section. Falls back to empty list.
function bullets(body: string, headers: RegExp): string[] {
  const lines = body.split(/\r?\n/);
  const out: string[] = [];
  let inSection = false;
  for (const raw of lines) {
    const line = raw.trim();
    if (line.startsWith("## ")) {
      const label = line.slice(3).toLowerCase();
      inSection = headers.test(label);
      continue;
    }
    if (inSection && /^[-*]\s+/.test(line)) {
      out.push(line.replace(/^[-*]\s+/, "").replace(/\[(\d+(?:,\s*\d+)*)\]/g, "").trim());
    }
  }
  return out.slice(0, 8);
}

export const GET: APIRoute = async () => {
  const all = await getCollection("reports");
  const en = all.filter((e) => e.data.lang === "en");
  const docs = en.map((e) => {
    const d = e.data;
    const body = e.body ?? "";
    const tldr = bullets(body, /^(tl;dr|tldr)/);
    const signals = bullets(body, /^signals?( to watch)?/);
    return {
      date: d.date,
      topic: d.topic,
      title: d.topic,
      salience: d.salience,
      sentiment: d.sentiment,
      tldr,
      signals,
      tags: d.tags ?? [],
      platforms: d.platforms ?? [],
      url: `/report/${d.date}/${d.topic}/en`,
    };
  });
  docs.sort((a, b) => (a.date < b.date ? 1 : -1));
  return new Response(JSON.stringify({ generated_at: new Date().toISOString(), docs }), {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=300, s-maxage=900",
    },
  });
};
