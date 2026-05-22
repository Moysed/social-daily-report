// Small display helpers shared across pages.

const TOPIC_TITLES: Record<string, string> = {
  "ai-devtools": "AI Devtools",
  "game-dev": "Game Dev",
  xr: "XR / VR / AR",
  "web-frontend": "Web & Frontend",
  edtech: "EdTech",
};

export function prettyTopic(slug: string): string {
  return (
    TOPIC_TITLES[slug] ??
    slug
      .split("-")
      .map((w) => w.charAt(0).toUpperCase() + w.slice(1))
      .join(" ")
  );
}

export function langLabel(lang: string): string {
  return lang === "th" ? "ไทย" : "EN";
}

export function sentimentEmoji(sentiment: string | null): string {
  switch (sentiment) {
    case "positive":
      return "🟢";
    case "negative":
      return "🔴";
    case "mixed":
      return "🟡";
    default:
      return "⚪";
  }
}

// e.g. 2026-05-20 -> "Wed, 20 May 2026"
export function prettyDate(iso: string): string {
  const d = new Date(iso + "T00:00:00Z");
  if (Number.isNaN(d.getTime())) return iso;
  return d.toLocaleDateString("en-GB", {
    weekday: "short",
    day: "2-digit",
    month: "short",
    year: "numeric",
    timeZone: "UTC",
  });
}
