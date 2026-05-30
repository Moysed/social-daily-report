import { getCollection } from "astro:content";
import { OGImageRoute } from "astro-og-canvas";
import { prettyTopic } from "../../lib/format";

const reports = await getCollection("reports");

type OGPage = { title: string; description: string };

const pages: Record<string, OGPage> = {
  "default.png": {
    title: "Social Daily Report",
    description: "AI-reasoned daily intelligence briefs for NDF DEV",
  },
};

for (const entry of reports) {
  const { date, topic, lang, salience } = entry.data;
  const saliencePct = salience != null ? Math.round(salience * 100) : null;
  const meta = saliencePct != null ? `${date}  ·  Salience ${saliencePct}%` : date;
  pages[`report/${date}/${topic}/${lang}.png`] = {
    title: prettyTopic(topic),
    description: `SOCIAL DAILY REPORT  ·  ${meta}`,
  };
}

export const { getStaticPaths, GET } = await OGImageRoute({
  param: "route",
  pages,
  getImageOptions: (_path, page: OGPage) => ({
    title: page.title,
    description: page.description,
    fonts: [
      "./public/fonts/Fraunces-650.ttf",
      "./public/fonts/NotoSansThai-400.ttf",
    ],
    font: {
      title: {
        families: ["Fraunces", "Noto Sans Thai"],
        size: 58,
        lineHeight: 1.1,
        color: [38, 28, 18],
        weight: "Bold",
      },
      description: {
        families: ["Fraunces", "Noto Sans Thai"],
        size: 26,
        lineHeight: 1.45,
        color: [100, 78, 58],
        weight: "Normal",
      },
    },
    bgGradient: [[247, 242, 232], [240, 234, 222]],
    border: {
      color: [175, 65, 30],
      width: 16,
      side: "inline-start",
    },
    padding: 60,
  }),
});
