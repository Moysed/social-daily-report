import type { Lang } from "./i18n";

export function bangkokToday(): string {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Bangkok",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(new Date());
}

export function relativeDate(
  date: string,
  lang: Lang,
  today: string
): { label: string | null; kind: "today" | "yesterday" | "recent" | "older" } {
  if (date === today) {
    return { label: lang === "th" ? "วันนี้" : "TODAY", kind: "today" };
  }
  const [ty, tm, td] = today.split("-").map(Number);
  const [vy, vm, vd] = date.split("-").map(Number);
  const diffDays = Math.round(
    (Date.UTC(ty, tm - 1, td) - Date.UTC(vy, vm - 1, vd)) / 86400000
  );
  if (diffDays === 1) {
    return { label: lang === "th" ? "เมื่อวาน" : "YESTERDAY", kind: "yesterday" };
  }
  if (diffDays >= 2 && diffDays <= 6) {
    return {
      label: lang === "th" ? `${diffDays} วันก่อน` : `${diffDays} DAYS AGO`,
      kind: "recent",
    };
  }
  return { label: null, kind: "older" };
}
