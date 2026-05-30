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
  // Friendly metric labels (replace jargon)
  activityLabel: string;
  evidenceLabel: string;
  activityHigh: string;
  activityMedium: string;
  activityLow: string;
  // Trend vs previous run of the same topic
  trendRising: string;
  trendEasing: string;
  trendSteady: string;
  trendNew: string;
  streakBadge: (n: number) => string;
  streakBadgeAria: (n: number) => string;
  sparklineLabel: string;
  rssShort: string;
  rssTopicAria: (topic: string) => string;
  subscribeTitle: string;
  subscribeAllFeed: string;
  subscribePerTopic: string;
  askTitle: string;
  askKicker: string;
  askPlaceholder: string;
  askButton: string;
  askHint: string;
  askEmpty: string;
  askAiSoon: string;
  // Home dashboard chrome
  morningBrief: string;
  todayOverview: string;
  todayHeading: (n: number) => string;
  archiveToggleShow: (n: number) => string;
  archiveToggleHide: string;
  // Report page nav
  prevReport: string;
  nextReport: string;
  alsoToday: string;
  onThisPage: string;
  // Phase 1 UX
  tldrTitle: string;
  readFullReport: string;
  leadSticker: string;
  // Phase 2 share
  shareTitle: string;
  shareX: string;
  shareLine: string;
  shareCopy: string;
  shareCopied: string;
  // Phase 3a
  unread: string;
  trendingTitle: string;
  trendingDays: (n: number) => string;
  // R1
  whyItMatters: string;
  minRead: (n: number) => string;
  newSince: (n: number) => string;
  scanAll: (n: number) => string;
  // R2 report page
  keyPoints: string;
  wordsUnit: string;
  // Friendly inline metric (replaces raw "salience .85" jargon on cards/metastrip)
  interest: (pct: number) => string;
  sourcesUnit: (n: number) => string;
  latestEdition: string;
  frontPage: string;
  // R3 ⌘K search palette
  searchRecent: string;
  searchBrowse: string;
  searchResultsCount: (n: number) => string;
  searchMatchesIn: string;
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
    activityLabel: "Activity",
    evidenceLabel: "Evidence",
    activityHigh: "High activity",
    activityMedium: "Steady",
    activityLow: "Quiet",
    trendRising: "Rising",
    trendEasing: "Easing",
    trendSteady: "Holding",
    trendNew: "New today",
    streakBadge: (n) => `trending ${n}d`,
    streakBadgeAria: (n) => `Topic carried for ${n} consecutive days`,
    sparklineLabel: "14-day salience",
    rssShort: "RSS",
    rssTopicAria: (topic) => `RSS feed for ${topic}`,
    subscribeTitle: "Subscribe",
    subscribeAllFeed: "All topics",
    subscribePerTopic: "Per topic",
    askTitle: "Ask the archive",
    askKicker: "Search across every report",
    askPlaceholder: "Ask anything (e.g. \"local LLM cost\", \"Antigravity\", \"agent eval\")",
    askButton: "Search",
    askHint: "Searches TL;DRs, signals, tags, and topics across every day on file.",
    askEmpty: "No matches across the archive yet — try a broader query.",
    askAiSoon: "AI synthesis arriving once the backend is live.",
    morningBrief: "Morning brief",
    todayOverview: "What's worth knowing today",
    todayHeading: (n) => (n === 1 ? "1 topic today" : `${n} topics today`),
    archiveToggleShow: (n) => (n === 1 ? "Show 1 earlier day" : `Show ${n} earlier days`),
    archiveToggleHide: "Hide earlier days",
    prevReport: "Older in this topic",
    nextReport: "Newer in this topic",
    alsoToday: "Also today",
    onThisPage: "On this page",
    tldrTitle: "TL;DR",
    readFullReport: "Read full report",
    leadSticker: "Top Signal Today",
    shareTitle: "Share",
    shareX: "Share on X",
    shareLine: "Share on LINE",
    shareCopy: "Copy link",
    shareCopied: "Copied",
    unread: "Unread",
    trendingTitle: "Trending this week",
    trendingDays: (n) => `${n} ${n === 1 ? "day" : "days"}`,
    whyItMatters: "Why it matters",
    minRead: (n) => `${n} min`,
    newSince: (n) => `${n} new since you last looked`,
    scanAll: (n) => `~${n} min to scan all`,
    keyPoints: "Key points",
    wordsUnit: "words",
    interest: (pct) => `${pct}% interest`,
    sourcesUnit: (n) => (n === 1 ? "source" : "sources"),
    latestEdition: "latest",
    frontPage: "front page",
    searchRecent: "Recent",
    searchBrowse: "Browse topics",
    searchResultsCount: (n) => `${n} ${n === 1 ? "result" : "results"}`,
    searchMatchesIn: "matches in",
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
    activityLabel: "ความเคลื่อนไหว",
    evidenceLabel: "หลักฐาน",
    activityHigh: "คุยกันหนาแน่น",
    activityMedium: "พอเหมาะ",
    activityLow: "เงียบ",
    trendRising: "กำลังมา",
    trendEasing: "ค่อย ๆ ซา",
    trendSteady: "ทรงตัว",
    trendNew: "เพิ่งเริ่มวันนี้",
    streakBadge: (n) => `ติดเทรนด์ ${n} วัน`,
    streakBadgeAria: (n) => `หัวข้อนี้อยู่ในรายงานติดต่อกัน ${n} วัน`,
    sparklineLabel: "salience 14 วัน",
    rssShort: "RSS",
    rssTopicAria: (topic) => `ฟีด RSS ของ ${topic}`,
    subscribeTitle: "สมัครรับ",
    subscribeAllFeed: "ทุกหัวข้อ",
    subscribePerTopic: "แยกตามหัวข้อ",
    askTitle: "ถามคลังรายงาน",
    askKicker: "ค้นข้ามรายงานทุกวัน",
    askPlaceholder: "ถามอะไรก็ได้ (เช่น \"local LLM\", \"Antigravity\", \"eval agent\")",
    askButton: "ค้นหา",
    askHint: "ค้นทั้ง TL;DR, signals, แท็ก และหัวข้อ ครอบคลุมทุกวันในคลัง",
    askEmpty: "ยังไม่พบในคลัง ลองคำกว้างขึ้น",
    askAiSoon: "สรุปด้วย AI กำลังมา ต่อ backend แล้วใช้ได้",
    morningBrief: "บรีฟเช้า",
    todayOverview: "วันนี้ควรรู้อะไร",
    todayHeading: (n) => `${n} หัวข้อวันนี้`,
    archiveToggleShow: (n) => `ดูย้อนหลังอีก ${n} วัน`,
    archiveToggleHide: "ซ่อนย้อนหลัง",
    prevReport: "เก่ากว่าในหัวข้อนี้",
    nextReport: "ใหม่กว่าในหัวข้อนี้",
    alsoToday: "วันนี้ยังมี",
    onThisPage: "หัวข้อในหน้านี้",
    tldrTitle: "สรุป",
    readFullReport: "อ่านฉบับเต็ม",
    leadSticker: "สัญญาณเด่นวันนี้",
    shareTitle: "แชร์",
    shareX: "แชร์บน X",
    shareLine: "แชร์ผ่าน LINE",
    shareCopy: "คัดลอกลิงก์",
    shareCopied: "คัดลอกแล้ว",
    unread: "ยังไม่อ่าน",
    trendingTitle: "มาแรงสัปดาห์นี้",
    trendingDays: (n) => `${n} วัน`,
    whyItMatters: "ทำไมถึงสำคัญ",
    minRead: (n) => `${n} นาที`,
    newSince: (n) => `${n} ใหม่ตั้งแต่คุณดูล่าสุด`,
    scanAll: (n) => `~${n} นาทีเพื่อสแกนทั้งหมด`,
    keyPoints: "ประเด็นสำคัญ",
    wordsUnit: "คำ",
    interest: (pct) => `น่าสนใจ ${pct}%`,
    sourcesUnit: () => "แหล่ง",
    latestEdition: "ล่าสุด",
    frontPage: "หน้ารวมของวัน",
    searchRecent: "ค้นล่าสุด",
    searchBrowse: "หัวข้อทั้งหมด",
    searchResultsCount: (n) => `${n} ผล`,
    searchMatchesIn: "พบใน",
  },
};
