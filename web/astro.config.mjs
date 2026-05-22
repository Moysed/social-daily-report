import { defineConfig } from "astro/config";

// Static site. Build output is committed-free (gitignored); deploy host
// (Vercel) runs `npm run build` on push. `site` controls absolute URLs in
// RSS feeds and og:url tags — override via SITE env var if the production
// domain differs from the default Vercel preview URL.
const site = process.env.SITE || "https://social-daily-report.vercel.app";

export default defineConfig({
  site,
  trailingSlash: "ignore",
});
