import rss from "@astrojs/rss";
import { getCollection } from "astro:content";
import type { APIContext } from "astro";
import { UI } from "../lib/i18n";
import { prettyTopic } from "../lib/format";

export const GET = (context: APIContext) => buildFeed(context, "en");

export async function buildFeed(context: APIContext, lang: "en" | "th") {
  const t = UI[lang];
  const all = await getCollection("reports");
  const items = all
    .filter((e) => e.data.lang === lang)
    .sort((a, b) => (a.data.date < b.data.date ? 1 : -1));

  const base = context.site ?? new URL("https://social-daily-report.local");
  const prefix = lang === "th" ? "/th/" : "/";

  return rss({
    title: t.htmlTitle + (lang === "th" ? " (ไทย)" : ""),
    description: t.description,
    site: new URL(prefix, base).toString(),
    items: items.map((entry) => {
      const d = entry.data;
      const pct = (v: number | null | undefined) =>
        v == null ? null : Math.round(v * 100);
      const meta = [
        t.posts(d.post_count),
        t.salience(pct(d.salience)),
        t.confidence(pct(d.confidence)),
      ].join(" / ");
      return {
        title: `${prettyTopic(d.topic)} — ${d.date}`,
        pubDate: new Date(d.generated_at),
        description: meta,
        link: `/report/${d.date}/${d.topic}/${d.lang}`,
        categories: [...new Set([d.topic, ...(d.tags ?? [])])],
      };
    }),
    customData: `<language>${lang === "th" ? "th" : "en"}</language>`,
  });
}
