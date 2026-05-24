import { getCollection } from "astro:content";
import type { APIContext } from "astro";
import { buildFeed } from "../../rss.xml";

export async function getStaticPaths() {
  const all = await getCollection("reports");
  const topics = new Set(all.map((e) => e.data.topic));
  return [...topics].map((topic) => ({ params: { topic } }));
}

export const GET = (context: APIContext) =>
  buildFeed(context, "th", context.params.topic as string);
