import type { APIContext } from "astro";
import { buildFeed } from "../rss.xml";

export const GET = (context: APIContext) => buildFeed(context, "th");
