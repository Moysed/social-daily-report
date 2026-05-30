// Small display helpers shared across pages.

export function cleanInline(s: string): string {
  return s
    .replace(/\[(\d+(?:,\s*\d+)*)\]/g, "")
    .replace(/!?\[([^\]]+)\]\([^)]+\)/g, "$1")
    .replace(/`([^`]+)`/g, "$1")
    .replace(/\s{2,}/g, " ")
    .trim();
}

export function extractTldr(body: string): string[] {
  const lines = body.split(/\r?\n/);
  let inTldr = false;
  const bullets: string[] = [];
  for (const raw of lines) {
    const line = raw.trim();
    if (/^##\s+(TL;DR|TL;?DR|สรุป)/i.test(line)) { inTldr = true; continue; }
    if (inTldr && /^##\s/.test(line)) break;
    if (inTldr && /^[-*]\s+/.test(line)) {
      bullets.push(cleanInline(line.replace(/^[-*]\s+/, "")));
    }
  }
  return bullets;
}

const TOPIC_TITLES: Record<string, string> = {
  "ai-devtools": "AI Devtools",
  "ai-news": "AI News",
  "game-dev": "Game Dev",
  xr: "XR / VR / AR",
  "web-frontend": "Web & Frontend",
  edtech: "EdTech",
  "ai-research": "AI Research",
  "3d-graphics": "3D & Graphics",
  "devops-cloud": "DevOps & Cloud",
  "multimodal-ai": "Multimodal AI",
  "audio-ai": "Audio AI",
  "thai-tech": "Thai Tech",
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

// e.g. 2026-05-20 -> "20 May" (brief line / prev-next edition labels). Localizes for Thai.
export function shortDate(iso: string, lang: string = "en"): string {
  const d = new Date(iso + "T00:00:00Z");
  if (Number.isNaN(d.getTime())) return iso.slice(5);
  const locale = lang === "th" ? "th-TH-u-ca-gregory" : "en-GB";
  return d.toLocaleDateString(locale, { day: "numeric", month: "short", timeZone: "UTC" });
}

// Split a bullet into a bold lead-in clause + the rest (Axios pattern).
// Shared by Home.astro (R1) and the report page (R2). NOTE: Home.astro still keeps
// a local copy — keep these identical if you touch either.
export function boldLeadIn(s: string): { lead: string; rest: string } {
  const dmIdx = s.indexOf(" — ");
  if (dmIdx > 0) return { lead: s.slice(0, dmIdx + 3), rest: s.slice(dmIdx + 3) };
  const colIdx = s.indexOf(": ");
  if (colIdx > 4 && colIdx < s.length * 0.55) return { lead: s.slice(0, colIdx + 2), rest: s.slice(colIdx + 2) };
  const words = s.split(/\s+/);
  const k = Math.min(5, Math.max(3, Math.floor(words.length * 0.35)));
  return { lead: words.slice(0, k).join(" ") + " ", rest: words.slice(k).join(" ") };
}

// Reading time: EN words/200. Thai chars/1600 — calibrated so a report reads in
// roughly the same time as its EN translation (these reports are ~40% English
// terms/names/numbers + structured post-stream data, not pure Thai prose, so a
// literary chars/350 rate badly overstates them). Floor at 1 min.
export function readingMinutes(body: string, lang: string): number {
  if (!body) return 1;
  if (lang === "th") {
    return Math.max(1, Math.ceil([...body].length / 1600));
  }
  return Math.max(1, Math.ceil(body.trim().split(/\s+/).length / 200));
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
