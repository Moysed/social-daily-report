import { defineConfig } from "astro/config";

// Static site. Build output is committed-free (gitignored); deploy host
// (Vercel/Cloudflare Pages) runs `npm run build` on push.
export default defineConfig({
  site: "https://social-daily-report.local",
  trailingSlash: "ignore",
});
