export type Lang = "en" | "th";

export const LOCALES: Lang[] = ["en", "th"];

export const homePath: Record<Lang, string> = {
  en: "/",
  th: "/th/",
};

type Dict = {
  htmlTitle: string;
  description: string;
  siteNote: string;
  footer: string;
  switchLabel: string;
  dailyBrief: string;
  latestRun: string;
  leadSignal: string;
  leadDeck: string;
  allSignals: string;
  topics: (n: number) => string;
  posts: (n: number) => string;
  confidence: (pct: number | null) => string;
  salience: (pct: number | null) => string;
  sourcePosts: string;
  platforms: string;
  readReport: string;
  availableLanguages: string;
  metricGuideTitle: string;
  legendSalience: [string, string];
  legendConfidence: [string, string];
  archive: string;
  noReportsTitle: string;
  noReportsBody: string;
  backHome: string;
  reportMeta: string;
  model: string;
  translatedBy: string;
  switchReport: string;
  themeLabel: string;
  themeAuto: string;
  themeLight: string;
  themeDark: string;
  search: string;
  searchPlaceholder: string;
  searchEmpty: string;
  searchHint: string;
  filterTopic: string;
  filterDate: string;
  filterAll: string;
  filterClear: string;
};

export const UI: Record<Lang, Dict> = {
  en: {
    htmlTitle: "Social Daily Report",
    description: "AI-reasoned daily reports across social platforms for the NDF DEV team.",
    siteNote: "Daily social signal for NDF DEV",
    footer: "Opus synthesis and Thai translation pipeline. Built from static Markdown reports.",
    switchLabel: "ภาษาไทย",
    dailyBrief: "Daily intelligence brief",
    latestRun: "Latest run",
    leadSignal: "Lead signal",
    leadDeck: "Highest-salience topic from the latest run. Start here when time is short.",
    allSignals: "All signals",
    topics: (n) => `${n} ${n === 1 ? "topic" : "topics"}`,
    posts: (n) => `${n} ${n === 1 ? "post" : "posts"}`,
    confidence: (pct) => (pct == null ? "confidence n/a" : `${pct}% confidence`),
    salience: (pct) => (pct == null ? "salience n/a" : `${pct}% salience`),
    sourcePosts: "Source posts",
    platforms: "Platforms",
    readReport: "Read report",
    availableLanguages: "Available languages",
    metricGuideTitle: "How to read this",
    legendSalience: ["Salience", "how important or visible a topic was in the latest source posts."],
    legendConfidence: ["Confidence", "how strongly the collected evidence supports the summary."],
    archive: "Archive",
    noReportsTitle: "No reports have been published yet.",
    noReportsBody: "Generate the first bilingual report set from the pipeline, then rebuild the Astro site.",
    backHome: "All reports",
    reportMeta: "Report details",
    model: "model",
    translatedBy: "translated by",
    switchReport: "Switch report language",
    themeLabel: "Theme",
    themeAuto: "Auto",
    themeLight: "Light",
    themeDark: "Dark",
    search: "Search",
    searchPlaceholder: "Search reports",
    searchEmpty: "No matches",
    searchHint: "Press Esc to close, ↑↓ to navigate, ↵ to open",
    filterTopic: "Topic",
    filterDate: "Date",
    filterAll: "All",
    filterClear: "Clear filters",
  },
  th: {
    htmlTitle: "Social Daily Report",
    description: "รายงานสัญญาณโซเชียลรายวันสำหรับทีม NDF DEV",
    siteNote: "สัญญาณโซเชียลรายวันสำหรับ NDF DEV",
    footer: "วิเคราะห์ด้วย Opus และแปลไทยผ่าน pipeline สร้างจากรายงาน Markdown แบบ static",
    switchLabel: "English",
    dailyBrief: "บรีฟข่าวกรองรายวัน",
    latestRun: "รอบล่าสุด",
    leadSignal: "สัญญาณเด่น",
    leadDeck: "หัวข้อที่มี salience สูงสุดในรอบล่าสุด เริ่มอ่านตรงนี้เมื่อมีเวลาน้อย",
    allSignals: "สัญญาณทั้งหมด",
    topics: (n) => `${n} หัวข้อ`,
    posts: (n) => `${n} โพสต์`,
    confidence: (pct) => (pct == null ? "ไม่มีค่าความเชื่อมั่น" : `ความเชื่อมั่น ${pct}%`),
    salience: (pct) => (pct == null ? "ไม่มีค่า salience" : `salience ${pct}%`),
    sourcePosts: "โพสต์ต้นทาง",
    platforms: "แพลตฟอร์ม",
    readReport: "อ่านรายงาน",
    availableLanguages: "ภาษาที่มี",
    metricGuideTitle: "วิธีอ่านหน้านี้",
    legendSalience: ["Salience", "บอกว่าหัวข้อนั้นสำคัญหรือถูกพูดถึงมากแค่ไหนในโพสต์รอบล่าสุด"],
    legendConfidence: ["Confidence", "บอกว่าหลักฐานที่รวบรวมมาหนุนบทสรุปได้แน่นแค่ไหน"],
    archive: "คลังย้อนหลัง",
    noReportsTitle: "ยังไม่มีรายงานที่เผยแพร่",
    noReportsBody: "สร้างชุดรายงานสองภาษาชุดแรกจาก pipeline แล้ว build เว็บ Astro ใหม่",
    backHome: "รายงานทั้งหมด",
    reportMeta: "รายละเอียดรายงาน",
    model: "โมเดล",
    translatedBy: "แปลโดย",
    switchReport: "เปลี่ยนภาษารายงาน",
    themeLabel: "ธีม",
    themeAuto: "อัตโนมัติ",
    themeLight: "สว่าง",
    themeDark: "มืด",
    search: "ค้นหา",
    searchPlaceholder: "ค้นหารายงาน",
    searchEmpty: "ไม่พบผลลัพธ์",
    searchHint: "Esc ปิด · ↑↓ เลื่อน · ↵ เปิด",
    filterTopic: "หัวข้อ",
    filterDate: "วันที่",
    filterAll: "ทั้งหมด",
    filterClear: "ล้างตัวกรอง",
  },
};
