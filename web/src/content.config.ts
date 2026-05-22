import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

// Read the pipeline's output directly — no copy/symlink. Each topic report is
// `content/reports/<date>/<topic>.<lang>.md`. We skip the per-day index.*.md
// files (different schema); the blog builds its own day index.
const reports = defineCollection({
  loader: glob({
    pattern: ["**/*.{en,th}.md", "!**/index.*.md"],
    base: "../content/reports",
  }),
  schema: z.object({
    type: z.literal("social-topic-report"),
    date: z.string(),
    topic: z.string(),
    lang: z.enum(["en", "th"]),
    pair: z.string(),
    generated_at: z.string(),
    generator: z.string(),
    model: z.string(),
    platforms: z.array(z.string()).default([]),
    regions: z.array(z.string()).default([]),
    post_count: z.number().default(0),
    salience: z.number().nullable().default(null),
    sentiment: z.string().nullable().default(null),
    confidence: z.number().nullable().default(null),
    tags: z.array(z.string()).default([]),
    translated_by: z.string().optional(),
  }),
});

export const collections = { reports };
