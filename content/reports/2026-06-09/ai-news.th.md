---
type: social-topic-report
date: '2026-06-09'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-09T03:09:16+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 233
salience: 0.4
sentiment: mixed
confidence: 0.55
tags:
- mcp
- anthropic
- openai-ipo
- model-release
- devtools
- ai-news
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2064117485624827904/img/6KXuyzRfh2pXEsRn.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-09

## TL;DR
- ฟีด AI engagement สูงวันนี้ส่วนใหญ่เป็น noise: มิวสิควิดีโอ 'Gemini Season' ของ Kanye West [1][13][18] และโพสต์ดาราศาสตร์ครองพื้นที่ ไม่มี artifact ที่ studio นำไปใช้งานได้จริง
- OpenAI ยื่น S-1 เป็นความลับเพื่อ IPO [8][34][58][52]; โน้ตที่อ้างว่าเป็นของ Altman ระบุว่ายังไม่ตัดสินใจเรื่อง timing และ 'อาจจะอีกนาน' [34] — เป็นข่าวองค์กร/การเงิน ไม่ใช่ tool
- Devtool ที่เป็นรูปธรรม: Anthropic เพิ่ม observability dashboard สำหรับ developer ที่สร้าง Claude connectors บน MCP [9]
- ข่าวลือที่ยังไม่ยืนยัน: Anthropic จะปล่อย 'Mythos' / 'Claude Fable 5' (model ระดับ Claude 5) 'พรุ่งนี้' [17][21][37][54] — มาจากบัญชี leak นิรนาม ถือเป็นข่าวลือ
- สัญญาณ model/infra: Xiaomi MiMo-v2.5-Pro-UltraSpeed อ้าง model 1T-param ที่ ~1000 tokens/sec [33]; Apple สร้าง AI architecture ใหม่รอบ Google Gemini models ตามรายงาน [53]

## What happened
ส่วนใหญ่วันนี้ไม่เกี่ยวกับ AI tooling ใหม่: กลุ่มใหญ่ครอบคลุมซิงเกิล 'Gemini Season' และมิวสิควิดีโอของ Kanye West [1][2][4][6][7][13][18][20][23][25][26][35][39][49][57][60] และโพสต์ดาราศาสตร์/โหราศาสตร์ [15][41][47] ซึ่งใช้คำว่า 'Gemini' ร่วมกันแต่ไม่มี AI artifact ใด กลุ่มใหญ่ที่สองคือการยื่น IPO เป็นความลับของ OpenAI [5][8][19][34][48][50][52][58][59] ซึ่งเป็นเหตุการณ์ด้านองค์กร/การเงิน ไม่ใช่ release ที่นำไปใช้ได้ ในส่วน artifact จริง: Anthropic ส่ง observability dashboard สำหรับ MCP connector developers [9] และจัดงาน Claude team event ที่โตเกียว [11] บัญชี leak อ้างว่า Anthropic จะปล่อย model ชื่อ 'Mythos'/'Claude Fable 5' พรุ่งนี้ [17][21][22][37][54] โดยโพสต์หนึ่งอ้างสิทธิ์ด้านความปลอดภัยที่ยังไม่ยืนยันว่า model นี้สามารถ 'weaponize ช่องโหว่ที่เพิ่งเปิดเผยได้เองภายในไม่กี่ชั่วโมง' [51]

## Why it matters (reasoning)
สำหรับ studio ที่มองหา tool มาต่อยอด AI workflow วันนี้มี item ที่ actionable จริงๆ น้อยมาก MCP connector observability dashboard [9] เป็นรูปธรรมที่สุด: ถ้า NDF DEV เปิด internal tools/data ให้ Claude ผ่าน MCP การมี debug visibility ลดต้นทุน integration ได้โดยตรง การอ้างสิทธิ์ MiMo 1T-ที่-1000-tps [33] และ architecture Gemini-based ของ Apple [53] ชี้ทิศทางของ inference latency และ mobile on-device AI — เกี่ยวข้องกับ in-app assistant และ agent loop ที่ต้องการ latency ต่ำ — แต่ทั้งสองไม่ใช่สิ่งที่ small studio จะ self-host ได้ (1T model ไม่สามารถรันภายในได้จริง; คุณค่าขึ้นอยู่กับ hosted endpoint) OpenAI IPO [8][34] และ meta-commentary ('AI is slowing down' [43], Anthropic pause talk [46], xAI as a datacentre REIT [45]) เป็น signal เกี่ยวกับทิศทางตลาด ไม่ใช่ input สำหรับ workflow ผลกระทบลำดับสอง: ข่าวลือ Mythos/Claude 5 [17][37] สำคัญเฉพาะเมื่อออก official; แหล่งที่มาอ่อนและการอ้างสิทธิ์ความสามารถที่โดดเด่น [51] ยังไม่ยืนยัน การดำเนินการตอนนี้จึงเป็นการรีบเกินไป

## Possibility
น่าจะเกิด: MCP connector tooling และ ecosystem จะพัฒนาต่อเนื่อง เห็นได้จาก Anthropic ที่ส่ง developer dashboard [9] และจัดงาน developer event โดยตรง [11] พอเป็นไปได้: model Claude-class ใหม่ ('Mythos'/'Fable 5') จะออกในเร็วๆ นี้ [17][21][37][54] แต่ timing 'พรุ่งนี้' และ capability claims [51] มาจากบัญชี leak ให้ถือว่าวันที่และรายละเอียดยังไม่ยืนยัน พอเป็นไปได้: Apple ออก Gemini-backed AI APIs ที่กระทบการพัฒนา iOS app [53] ซึ่งเกี่ยวข้องกับงาน mobile ของ NDF DEV ไม่น่าจะ immediately useful: OpenAI IPO [8][34] ไม่เปลี่ยน toolchain ของ studio ในระยะใกล้ และ 'AI is slowing down' [43] เป็นความเห็น ไม่ใช่ release ที่วัดได้ ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น จึงไม่ระบุ

## Org applicability — NDF DEV
1) ประเมิน MCP connector observability dashboard [9] หากและเมื่อต่อ internal tools (Unity build data, e-learning content) เข้า Claude ผ่าน MCP — effort ต่ำ, ใช้งานได้โดยตรงสำหรับ debug integrations 2) รอยืนยัน official ของ Claude 5-class model ก่อนเปลี่ยน model defaults ใดๆ [17][37][54] — ไม่ต้อง re-architect ตามข่าวลือ; effort ต่ำในการ monitor 3) ติดตาม AI architecture Gemini-based ของ Apple [53] สำหรับ on-device/mobile AI APIs ใหม่ที่เกี่ยวข้องกับ iOS apps — effort ปานกลาง, monitor เท่านั้น 4) จดบันทึก MiMo claim 1000-tps [33] เป็น latency benchmark สำหรับตัวเลือก hosted ในอนาคตสำหรับ interactive/agent features — effort ต่ำ, ยังไม่ต้อง action ข้าม: ทั้ง cluster Kanye 'Gemini Season' [1][2][4][6][13][18] (irrelevant), รายการการเงิน OpenAI IPO [5][8][34][52][58] (ไม่ actionable) และ security hype ที่ยังไม่ยืนยัน [51] Performative-UI repo [16] เป็น design-trope/parody React library ไม่ใช่ production UI — ข้ามสำหรับงาน shipping

## Signals to Watch
- การ release (หรือไม่ release) อย่าง official ของ Anthropic 'Mythos'/'Claude Fable 5' และความสามารถจริงเทียบกับ leaked claims [17][37][51][54]
- MiMo 1T-ที่-1000-tps model จะ available ผ่าน hosted API ที่ใครนอก Xiaomi เรียกใช้ได้หรือไม่ [33]
- รายละเอียด AI architecture Gemini-backed ของ Apple และ mobile APIs ฝั่ง developer [53]
- momentum ของ MCP connector ecosystem — developer tooling และ event จาก Anthropic เพิ่มขึ้น [9][11]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **mvanhorn/last30days-skill** — AI agent skill ที่ค้นคว้าทุก topic ผ่าน Reddit, X, YouTube, HN, Polymarket และ web | rss | <https://github.com/mvanhorn/last30days-skill> |
| **RyanCodrai/turbovec** — vector index ที่สร้างบน TurboQuant เขียนด้วย Rust พร้อม Python bindings corpus 10 ล้าน document | rss | <https://github.com/RyanCodrai/turbovec> |
| **google/skills** — Agent Skills สำหรับ Google products และ technologies | rss | <https://github.com/google/skills> |
| **refactoringhq/tolaria** — Desktop app จัดการ markdown knowledge bases 💧 รองรับ macOS, Windows | rss | <https://github.com/refactoringhq/tolaria> |
| **Panniantong/Agent-Reach** — ให้ AI agent มองเห็นอินเทอร์เน็ตทั้งหมด อ่านและค้นหาบน Twitter, Reddit, YouTube, GitHub | rss | <https://github.com/Panniantong/Agent-Reach> |
| **danielmiessler/Personal_AI_Infrastructure** — Agentic AI Infrastructure เพื่อขยาย capabilities ของมนุษย์ | rss | <https://github.com/danielmiessler/Personal_AI_Infrastructure> |
| **santifer/career-ops** — ระบบหางานขับเคลื่อนด้วย AI บน Claude Code มี 14 skill modes, Go dashboard, PDF generation | rss | <https://github.com/santifer/career-ops> |
| **phuryn/pm-skills** — PM Skills Marketplace: skills, commands และ plugins 100+ รายการ ครอบคลุมตั้งแต่ discovery ถึง strategy และ execution | rss | <https://github.com/phuryn/pm-skills> |
| **openai/plugins** — OpenAI Plugins คอลเลกชัน Codex plugin examples แบบ curated | rss | <https://github.com/openai/plugins> |
| **Andyyyy64/whichllm** — หา local LLM ที่รันได้จริงและ perform ดีที่สุดบน hardware ของคุณ จัดอันดับตามข้อมูล real, recency-aware | rss | <https://github.com/Andyyyy64/whichllm> |
| **MemPalace/mempalace** — AI memory system open-source ที่ benchmark ดีที่สุด และฟรี Local-first AI memory | rss | <https://github.com/MemPalace/mempalace> |
| **roboflow/supervision** — เครื่องมือ computer vision แบบ reusable | rss | <https://github.com/roboflow/supervision> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | kanyewest | ^22012 c1234 | [GEMINI SEASON Directed by Bianca Censori Out Now https://t.co/JKreaXTID5](https://x.com/kanyewest/status/2064117715338469767) |
| x | Kurrco | ^6823 c186 | [YE GEMINI SEASON OUT NOW 🚨 https://t.co/3nk9qzxUEV](https://x.com/Kurrco/status/2064098385531998451) |
| x | sama | ^4802 c761 | [Here is our current plan for OpenAI: https://t.co/r29FUUee3A](https://x.com/sama/status/2064088940932641225) |
| x | Rap | ^2138 c31 | [YE GEMINI SEASON (NEW SONG) 🚨TONIGHT🚨 https://t.co/qj1EPCOQot](https://x.com/Rap/status/2064097997667860761) |
| x | unusual_whales | ^2097 c190 | [BREAKING: OpenAI has confidentially filled for an IPO.](https://x.com/unusual_whales/status/2064103581880578090) |
| x | Kurrco | ^1593 c49 | [Ye and Bianca Censori in the new music video for 'Gemini Season' https://t.co/5U](https://x.com/Kurrco/status/2064098985770397779) |
| x | yeunrlsd | ^1541 c51 | [GEMINI SEASON 🐄 OUT NOW ON SPOTIFY https://t.co/VFEHmcwVmC](https://x.com/yeunrlsd/status/2064098806044733851) |
| x | CNN | ^1380 c179 | [OpenAI has confidentially filed for an initial public offering, setting it up fo](https://x.com/CNN/status/2064098143533232555) |
| x | ClaudeDevs | ^1345 c63 | [We've added an observability dashboard for developers of connectors. Connectors ](https://x.com/ClaudeDevs/status/2064072801062121906) |
| x | hopes_revenge | ^1294 c31 | [my friend at anthropic just asked me what color dog collar i wanted . i asked th](https://x.com/hopes_revenge/status/2064125177894457647) |
| x | claudeai | ^1277 c60 | [Final stop: Tokyo. Register to hear directly from the teams behind Claude: https](https://x.com/claudeai/status/2064139073590104402) |
| x | levelsio | ^1209 c64 | [My friend went to an indie hacker meetup this week and said this: "i went to ind](https://x.com/levelsio/status/2064090312885273022) |
| x | PopCrave | ^1203 c102 | [Kanye West releases new single "GEMINI SEASON" alongside music video directed by](https://x.com/PopCrave/status/2064125820222795845) |
| x | drewhahn | ^919 c8 | [when your anthropic friend who has been single his whole life suddenly pulls up ](https://x.com/drewhahn/status/2064103391211753681) |
| x | hyrumpd | ^837 c7 | [25 years old.. damn I'm getting old!! Happy Gemini season!! 😝#june#gemini#25 htt](https://x.com/hyrumpd/status/2064100970821206528) |
| radar | lizhang | ^804 c156 | [Show HN: Performative-UI – A react component library of design tropes](https://vorpus.github.io/performativeUI/) |
| x | jukan05 | ^773 c69 | [SOURCES: ANTHROPIC WILL RELEASE THE PUBLIC VERSION OF MYTHOS TOMORROW](https://x.com/jukan05/status/2064170300452098183) |
| x | XXL | ^742 c60 | [🗣️YE 🎬 "GEMINI SEASON" (MUSIC VIDEO) 🚨OUT NOW https://t.co/cWy2m4CPtD](https://x.com/XXL/status/2064108398342234138) |
| x | Polymarket | ^715 c111 | [NEW: OpenAI files confidentially for IPO.](https://x.com/Polymarket/status/2064096176786260466) |
| x | big_business_ | ^673 c38 | [👤YE👤 💿GEMINI SEASON💿 ◻️NEW SINGLE AND MUSIC VIDEO◻️ ◻️DIRECTED BY BIANCA CENSORI](https://x.com/big_business_/status/2064098708719849711) |
| x | MTSlive | ^643 c26 | [SITUATION DETECTED: Anthropic to release Mythos tomorrow, per Sources.](https://x.com/MTSlive/status/2064171066298339788) |
| x | ChrissGPT | ^612 c37 | [Welcome to the world Mr Claude Fable 5 (mythos) Final checkpoint https://t.co/AQ](https://x.com/ChrissGPT/status/2064142408313352533) |
| x | GoodAssSub | ^604 c36 | ["GEMINI SEASON" Music Video is now out https://t.co/0f7mEAH9EV](https://x.com/GoodAssSub/status/2064097688941908310) |
| x | yzyjohnny | ^601 c13 | [Ye has spoke on his favorite adult content of all time having a scene where Fran](https://x.com/yzyjohnny/status/2064103693448798720) |
| x | Rap | ^598 c16 | [YE GEMINI SEASON (NEW SONG &amp; VIDEO) 🚨OUT NOW🚨 https://t.co/umfOdop13T](https://x.com/Rap/status/2064099142649942285) |
| x | HipHopAllDay | ^576 c33 | [YE GEMINI SEASON (NEW SONG) OUT NOW 🚨 https://t.co/mujoRUVFPD](https://x.com/HipHopAllDay/status/2064100642935746678) |
| x | MumuTheLion | ^565 c0 | [Time for your body check, Claude... before I give you away. https://t.co/hEaLrhC](https://x.com/MumuTheLion/status/2064143545519513610) |
| x | antibearthesis | ^562 c38 | [POV: OpenAI stock after IPO https://t.co/FyjXSdcrMj](https://x.com/antibearthesis/status/2064095870711103989) |
| radar | 1vuio0pswjnm7 | ^562 c416 | [Anti-social: It's fads, not friends, which now dominate social media feeds](https://www.bbc.com/worklife/article/20260520-how-social-media-ceased-to-be-social) |
| x | yzycrave | ^552 c107 | [Thoughts on 'Gemini Season'? 🤔 https://t.co/EXppd5FqQB](https://x.com/yzycrave/status/2064103009781461488) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kanyewest</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 22012 · 💬 1234</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kanyewest/status/2064117715338469767">View @kanyewest on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“GEMINI SEASON Directed by Bianca Censori Out Now https://t.co/JKreaXTID5”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Kanye West โพสต์โปรโมตโปรเจกต์ 'GEMINI SEASON' กำกับโดย Bianca Censori — ไม่เกี่ยวกับ Google Gemini หรือ AI ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kanyewest/status/2064117715338469767" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Kurrco</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6823 · 💬 186</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Kurrco/status/2064098385531998451">View @Kurrco on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“YE GEMINI SEASON OUT NOW 🚨 https://t.co/3nk9qzxUEV”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@Kurrco โพสต์ hype เกี่ยวกับ Kanye West (Ye) และ Gemini season ตามดาราศาสตร์ ไม่ใช่ Google Gemini หรือ tech release ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Kurrco/status/2064098385531998451" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sama</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4802 · 💬 761</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sama/status/2064088940932641225">View @sama on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here is our current plan for OpenAI: https://t.co/r29FUUee3A”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Sam Altman เผยแผน phase 3 ของ OpenAI — สร้าง AI researcher อัตโนมัติ, เร่งเศรษฐกิจ, และให้ทุกคนมี AGI ส่วนตัว โดยคาดว่า AI จะ run research ส่วนใหญ่ของ OpenAI ได้เองภายใน March 2028</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป้า March 2028 บ่งว่า AI dev tools จะก้าวหน้าอีกระดับภายใน 2 ปี — ส่งผลโดยตรงต่อ workflow และบทบาทของนักพัฒนาในทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม milestone OpenAI รายไตรมาส แล้ว review ว่า workflow ใดของ studio (testing, docs, research) พร้อม automate แล้วเมื่อใกล้ 2028</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sama/status/2064088940932641225" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rap</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2138 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Rap/status/2064097997667860761">View @Rap on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“YE GEMINI SEASON (NEW SONG) 🚨TONIGHT🚨 https://t.co/qj1EPCOQot”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Ye (Kanye West) ประกาศเพลงใหม่ชื่อ 'Gemini Season' ออกคืนนี้ — ไม่เกี่ยวกับ Google Gemini AI</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Rap/status/2064097997667860761" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@unusual_whales</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2097 · 💬 190</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/unusual_whales/status/2064103581880578090">View @unusual_whales on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“BREAKING: OpenAI has confidentially filled for an IPO.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>OpenAI ยื่นไฟล์ IPO แบบ confidential แล้ว เตรียมเข้าตลาดหลักทรัพย์สหรัฐ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/unusual_whales/status/2064103581880578090" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Kurrco</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1593 · 💬 49</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Kurrco/status/2064098985770397779">View @Kurrco on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ye and Bianca Censori in the new music video for 'Gemini Season' https://t.co/5UKZ2wfu1c”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Ye และ Bianca Censori ปล่อย music video ชื่อ 'Gemini Season' — เนื้อหาบันเทิงดาราล้วนๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Kurrco/status/2064098985770397779" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@yeunrlsd</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1541 · 💬 51</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/yeunrlsd/status/2064098806044733851">View @yeunrlsd on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“GEMINI SEASON 🐄 OUT NOW ON SPOTIFY https://t.co/VFEHmcwVmC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>User ประกาศปล่อยเพลงชื่อ 'Gemini Season' บน Spotify — ไม่เกี่ยวกับ Google Gemini หรือ AI/dev ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/yeunrlsd/status/2064098806044733851" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CNN</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1380 · 💬 179</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CNN/status/2064098143533232555">View @CNN on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“OpenAI has confidentially filed for an initial public offering, setting it up for what may be the most highly anticipated market debut in recent history and a massive payday for early investors. https”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>OpenAI ยื่นเอกสาร IPO แบบปิดลับต่อหน่วยงานกำกับดูแลแล้ว บ่งชี้ว่ากำลังเดินหน้าเข้าตลาดหลักทรัพย์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CNN/status/2064098143533232555" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
