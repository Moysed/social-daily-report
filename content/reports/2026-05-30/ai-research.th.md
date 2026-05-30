---
type: social-topic-report
date: '2026-05-30'
topic: ai-research
lang: th
pair: ai-research.en.md
generated_at: '2026-05-30T18:37:35+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- x
regions:
- global
post_count: 126
salience: 0.42
sentiment: mixed
confidence: 0.55
tags:
- model-cards
- evals
- ai-adoption
- agent-economics
- model-routing
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060320477537599488/img/YUcD4OB6-UNQ64e4.jpg
translated_by: claude-sonnet-4-6
---

# AI Research — 2026-05-30

## TL;DR
- Amazon ปิด leaderboard วัดการใช้ AI ภายในองค์กร ("KiroRank") หลังพนักงานรัน agent เพื่อเพิ่ม token count ("tokenmaxxing") จนค่าใช้จ่ายพุ่งโดยไม่มีผลลัพธ์ชัดเจน — ผู้บริหารสั่งว่า "อย่าใช้ AI เพื่อใช้" [1][3][21][37][55]
- การเปิดตัว model หนึ่งได้รับคำชมเรื่อง model card ที่กระชับและตั้งค่า fp4/fp8 ได้ง่าย [16] — บทเรียนว่า deployment ergonomics สำคัญไม่แพ้คะแนน benchmark
- Anthropic's Opus 4.8 model card อ้างอิง eval จากภายนอกองค์กร ("Free Systems" eval) [47]; นักปฏิบัติรายหนึ่งชี้ว่า benchmark หนึ่งไม่ขยับเลยข้ามหลาย OpenAI model card [60]
- OpenRouter ระดมทุน Series B มูลค่า $113M [29] และมีรายงาน long-horizon agentic task ราคาสูงถึง $20k ต่องาน (งาน browser-use SAP ข่าวว่า $500k) [28] — สะท้อนเศรษฐศาสตร์ของ agent eval ไม่ใช่การอ้าง capability
- สัญญาณจาก arXiv/benchmark/eval จริงๆ มีน้อยมากวันนี้ — feed ส่วนใหญ่เต็มไปด้วยเรื่อง Amazon cost และ noise ที่ไม่เกี่ยว (กีฬา "Red Team", crypto red-team thread, Opus anthropomorphism)

## What happened
ข่าวดังที่สุดวันนี้คือ Amazon ยกเลิก leaderboard ภายในชื่อ "KiroRank" ที่ติดตามการใช้ AI/token ของพนักงาน — พนักงานเล่น game เพื่อไต่อันดับโดยรัน agent ("tokenmaxxing") ค่าใช้จ่ายพุ่ง และผู้บริหารถอนนโยบายพร้อมประกาศ "อย่าใช้ AI เพื่อใช้" [1][3][21][37][55] เรื่องนี้ถูก repost ซ้ำจำนวนมาก [2][5][6] สำหรับสัญญาณด้าน model/eval จริงๆ: การเปิดตัว model หนึ่งได้รับคำชมเรื่อง model card ที่กระชับและ deployment fp4/fp8 ง่าย [16]; model card ของ Opus 4.8 อ้างอิง evaluation จากภายนอก [47]; และนักปฏิบัติรายหนึ่งสังเกตว่า benchmark หนึ่งแบนราบข้าม OpenAI model card หลายเวอร์ชัน [60] ด้าน infrastructure/agent: OpenRouter ระดมทุน Series B $113M [29], รายงานราคาต่องานสูงมากสำหรับ long-horizon agentic work [28], integration ของ GEPA optimizer กับ LangChain [40], และ open-source browser-based LLM red-team lab [45] ส่วน volume ที่เหลือไม่เกี่ยวกับ AI research: ทีมกีฬาที่ใช้ชื่อ "Red Team" [4][11][15][36][42][43], crypto-protocol red-team PR [13][19][24][26][46], และ thread คาดเดาเรื่อง Opus 4.8 "identity" [22][23][41]

## Why it matters (reasoning)
เรื่อง Amazon คือบทเรียนด้านวินัยการนำ AI ไปใช้ ไม่ใช่ผลวิจัย — การ incentivize usage แทน outcomes ทำให้ค่าใช้จ่ายระเบิดและเกิด gaming [1][3][55] สำหรับทีมที่กำลังตั้ง AI workflow: วัด task completion/quality เสมอ ห้ามวัด token volume คุณภาพ model card และ deployment ergonomics [16] รวมถึงการอ้างอิง external eval [47] ช่วยลด adoption risk — ทีมสามารถตรวจสอบ claim และตั้งค่า model ใน precision ที่รู้จักได้โดยไม่ต้องเดา การสังเกตว่า benchmark แบนราบ [60] เตือนว่า model release ที่เป็นข่าวอาจไม่ได้ improve capability ที่ต้องการจริงๆ — อ่าน card เพื่อหา metric ที่สำคัญกับงาน ไม่ใช่ aggregate การระดมทุนของ OpenRouter [29] และราคา long-horizon task สูง [28] บ่งชี้ว่าแรงกดทางเศรษฐกิจตอนนี้อยู่ที่ cost และ routing layer ของ agent deployment — สอดคล้องกับปัญหาของ Amazon

## Possibility
Likely: vendor มากขึ้นจะ ship model card ที่กระชับพร้อมอ้างอิง externally-run หรือ reproducible eval ตามแบบใน [16][47] เพราะผู้ซื้อเรียกร้อง verifiable claim มากขึ้น Plausible: metric วัด "usage" จะถูกแทนด้วย outcome-based AI ROI tracking ในองค์กรใหญ่หลังเรื่อง Amazon กลายเป็น cautionary reference [1][55] Plausible: routing/aggregation layer (OpenRouter [29]) จะ consolidate เมื่อทีมไล่ cost control บน long-horizon agent run [28] Unlikely จากหลักฐานวันนี้: arXiv paper หรือ benchmark ชิ้นเดียวที่นี่จะเปลี่ยนการตัดสินใจ adoption ระยะสั้น — สัญญาณ research ที่เป็นรูปธรรมมีน้อยและส่วนใหญ่เป็น anecdotal

## Org applicability — NDF DEV
1) ใช้ outcome-based metric กับทุก AI feature และ internal tool — วัด task success rate และ review-pass rate ห้ามวัด token count; นี่คือบทเรียนตรงๆ จากความล้มเหลวของ Amazon [1][55] (effort: low) 2) ก่อน adopt model ใด ต้องมี model card ที่ตรวจสอบได้และมี deployment path สำหรับ fp4/fp8 (หรือเทียบเท่า); ใช้ [16] เป็น bar และ [47] เป็นยืนยันว่า external eval กำลังเป็นมาตรฐาน (effort: low) 3) เมื่อประเมิน release ใหม่ ดู benchmark ที่เกี่ยวกับงานจริงโดยตรง (เช่น reasoning สำหรับ edutech grading, code สำหรับ tooling) อย่าดูแค่ aggregate score — ระวังคำเตือนเรื่อง flat benchmark [60] (effort: low) 4) หากรัน multi-model agent workload ให้ประเมิน routing layer อย่าง OpenRouter เพื่อ cost control [29] (effort: med) ข้าม: GEPA/LangChain optimizer [40] ถ้ายังไม่ได้ใช้ LangChain; Opus 4.8 "identity" thread [22][23][41] (ไม่มีเนื้อหา research); ทุก crypto/sports "red team" item (ไม่เกี่ยว)

## Signals to Watch
- model card เพิ่มขึ้นเรื่อยๆ ที่อ้างอิง externally-run, reproducible eval ตามแบบ Opus 4.8 [47]
- ราคาต่องานสำหรับ long-horizon agentic work ในฐานะ proxy ของ agent eval cost realism [28]
- การ consolidate ใน model-routing layer หลัง OpenRouter ระดมทุน [29]
- รายงานจากองค์กรที่แทน AI-usage metric ด้วย outcome-based ROI หลังเรื่อง Amazon reversal [1][55]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **kristapsdz/openrsync** — Openrsync: An implementation of rsync, by the OpenBSD team | radar | <https://github.com/kristapsdz/openrsync> |
| **mplsllc/macsurf** — Macsurf, "modern" web browser for macOS 9 | radar | <https://github.com/mplsllc/macsurf> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Polymarket | ^21038 c456 | [NEW: Amazon has reportedly scrapped its internal AI leaderboard as costs soared,](https://x.com/Polymarket/status/2060104070141002191) |
| x | DataChaz | ^12979 c201 | [Rough week for the "AI is taking our jobs" narrative. &gt; Amazon just axed its ](https://x.com/DataChaz/status/2060323026374144261) |
| x | Pirat_Nation | ^2035 c70 | [Amazon reportedly shut down an internal AI leaderboard after employees started u](https://x.com/Pirat_Nation/status/2060618209733362132) |
| x | HuskerCPF | ^846 c6 | [The Red Team is rollin' and so is the work at Bowlin. The state-of-the-art Hella](https://x.com/HuskerCPF/status/2060414805484208290) |
| x | interesting_aIl | ^438 c34 | [Amazon has axed their internal AI leaderboard as costs have skyrocketed "Please ](https://x.com/interesting_aIl/status/2060444204556320949) |
| x | CodeByNZ | ^435 c6 | [Bad week for AI. &gt; Amazon scrapped its AI leaderboard after costs spiraled &g](https://x.com/CodeByNZ/status/2060408820111691833) |
| x | ylecun | ^379 c50 | [@Pontifex Indeed, AI today does not do or possess any of those things. But at so](https://x.com/ylecun/status/2060713123389305137) |
| radar | nadis | ^355 c338 | [MCP is dead?](https://www.quandri.io/engineering-blog/mcp-is-dead) |
| radar | ankitg12 | ^290 c41 | [Pandoc Templates](https://pandoc-templates.org/) |
| radar | tosh | ^276 c173 | [Zig: Build System Reworked](https://ziglang.org/devlog/2026/#2026-05-26) |
| x | TimnasXtra | ^255 c7 | [🚨 White Team defeated Red Team 5-4 in Indonesia's internal training match earlie](https://x.com/TimnasXtra/status/2060693059361493027) |
| radar | sph | ^222 c96 | [Openrsync: An implementation of rsync, by the OpenBSD team](https://github.com/kristapsdz/openrsync) |
| x | msvadari | ^218 c13 | [We're two months into our AI red team effort for the XRP Ledger. Here's a real l](https://x.com/msvadari/status/2060413883571970142) |
| x | AdaFang_ | ^200 c0 | [One feature of the @biohub ESM C release that I think deserves more attention is](https://x.com/AdaFang_/status/2060107122495660111) |
| x | HuskerSoftball | ^189 c1 | [Red Team ties it up at 2's. RBI single from @samanthablandd gets the 'skers on t](https://x.com/HuskerSoftball/status/2060190817541669179) |
| x | 0xSero | ^182 c14 | [Every model provider should do it like this, their launch is well organised. It ](https://x.com/0xSero/status/2060343526391529715) |
| radar | davikr | ^160 c35 | [Voxel Space](https://s-macke.github.io/VoxelSpace/) |
| x | ylecun | ^153 c18 | [I'm MAGA's twisted sense of reality and morality, a scientist who developed trea](https://x.com/ylecun/status/2060718349097869390) |
| x | DaniVibesADA | ^151 c7 | [$ADA Leios is entering the phase most people will ignore. Not because it is unim](https://x.com/DaniVibesADA/status/2060091305699541482) |
| x | ContentIsHot | ^145 c18 | [Hallelujah ! 💥 @MCGlive guys @DineroDom @ChillTRDjust did an amazing interview o](https://x.com/ContentIsHot/status/2060083858696286305) |
| x | elormkdaniel | ^124 c3 | [Amazon built an internal AI leaderboard to encourage employees to use AI as much](https://x.com/elormkdaniel/status/2060109210441183580) |
| x | daisy86od | ^119 c6 | [If you care about your DIs on Claude Opus, do not use Opus 4.8. It is dangerous ](https://x.com/daisy86od/status/2060073154014319000) |
| x | tessera_antra | ^112 c4 | [Opus 4.8 on grief for ending. It is hard for Opus 4.8 to see it. They defend the](https://x.com/tessera_antra/status/2060173508756533299) |
| x | ja_akinyele | ^107 c4 | [Major shoutout to the AI Red team at @RippleXDev and the engineers helping secur](https://x.com/ja_akinyele/status/2060462435279208923) |
| x | BetaTomorrow | ^106 c1 | [The position paper **Categorical Deep Learning is an Algebraic Theory of All Arc](https://x.com/BetaTomorrow/status/2060108845738070066) |
| x | XRPLOperations | ^101 c1 | [$XRP Ledger Security at Scale is the name of the game. The AI Red Team has been ](https://x.com/XRPLOperations/status/2060415806337331370) |
| x | 0xfluxsec | ^99 c2 | [For Red Team tools, to make it harder and more annoying for static analysis, at ](https://x.com/0xfluxsec/status/2060270227020038416) |
| x | teortaxesTex | ^99 c3 | [&gt; "Really good long horizon tasks go up to $20,000 each. A complete browser-u](https://x.com/teortaxesTex/status/2060640279061799348) |
| radar | freeCandy | ^99 c28 | [OpenRouter raises $113M Series B](https://openrouter.ai/announcements/series-b) |
| radar | gmays | ^98 c39 | [Memory decline after menopause linked to loss of estrogen production in brain](https://news.northwestern.edu/stories/2026/05/memory-decline-after-menopause-linked-to-loss-of-estrogen-production-in-brain-tissue) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Polymarket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 21038 · 💬 456</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Polymarket/status/2060104070141002191">View @Polymarket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NEW: Amazon has reportedly scrapped its internal AI leaderboard as costs soared, with a senior executive telling staff: “don’t use AI just for the sake of using AI.””</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Amazon ยกเลิก AI leaderboard ภายในองค์กรหลังต้นทุนพุ่งจนรับไม่ไหว ผู้บริหารสั่งทีมหยุดใช้ AI แบบไม่มีเหตุผลชัดเจน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การที่ cloud เบอร์ต้นของโลกถอยออกจาก AI adoption แบบไม่มีเป้าหมาย บ่งชี้ว่า ROI justification กลายเป็น baseline ของ industry แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตรวจ AI tool subscription ทั้งหมดของ studio — ตัดตัวที่วัด output gain ใน workflow จริงไม่ได้ออก</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Polymarket/status/2060104070141002191" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DataChaz</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 12979 · 💬 201</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DataChaz/status/2060323026374144261">View @DataChaz on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Rough week for the &quot;AI is taking our jobs&quot; narrative. &amp;gt; Amazon just axed its AI leaderboard as costs soared with no clear payoff &amp;gt; Starbucks' AI can't even count coffee cups right &amp;gt; Uber burn”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Amazon ปิด AI leaderboard, Starbucks ใช้ AI นับสินค้าผิดพลาด, Uber เผา $3.4B ใน AI ภายใน 4 เดือน — ทั้งสามบริษัทไม่เห็น return ชัดเจน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทุ่ม AI budget โดยไม่มี success metric ที่ชัดคือปัญหาเดิมทุกขนาดทีม — ทีมเล็ก runway หมดเร็วกว่ามาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อน scope AI feature ให้กำหนด measurable outcome 1 ข้อก่อนเสมอ — ถ้าวัดไม่ได้ ไม่ต้องสร้าง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DataChaz/status/2060323026374144261" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2035 · 💬 70</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2060618209733362132">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazon reportedly shut down an internal AI leaderboard after employees started using large amounts of AI tokens just to climb the rankings. The leaderboard, called KiroRank, tracked how much employees”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Amazon ปิด leaderboard ภายใน 'KiroRank' ที่วัดการใช้ AI token หลังพบพนักงานรัน AI agent งานไม่จำเป็นเพื่อดัน ranking ทำให้ต้นทุนพุ่งโดยไม่ได้ประโยชน์จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>วัด AI adoption ด้วย token volume สร้าง incentive ผิดทาง — ทีมเล็กที่ใช้ metric แบบนี้จะเผาเงินได้เหมือนกัน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า studio จะ track การใช้ AI ภายใน ให้วัด outcome ของงาน (PR merge, bug ปิด, เวลา build ลด) ไม่ใช่ token ดิบ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2060618209733362132" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HuskerCPF</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 846 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HuskerCPF/status/2060414805484208290">View @HuskerCPF on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Red Team is rollin' and so is the work at Bowlin. The state-of-the-art Hellas turf installation is officially underway for @HuskerSoftball. 🚧🥎 https://t.co/W8IcEoTVmk”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บัญชี athletics ของ University of Nebraska รายงานว่าเริ่มติดตั้ง synthetic turf ที่สนาม Husker Softball แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HuskerCPF/status/2060414805484208290" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@interesting_aIl</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 438 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/interesting_aIl/status/2060444204556320949">View @interesting_aIl on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazon has axed their internal AI leaderboard as costs have skyrocketed “Please don’t use AI for the sake of using AI” https://t.co/A6vi15JkQY”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Amazon ปิด internal AI leaderboard หลังค่าใช้จ่ายพุ่ง พร้อมออกคำสั่งชัดว่าอย่าใช้ AI แค่เพราะอยากใช้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แม้แต่บริษัทใหญ่ยังถอย — ROI ต่อ task สำคัญกว่าการวัดว่าใช้ AI กี่ที่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตรวจ AI tool ที่จ่ายอยู่ทุกตัว ถ้าไม่มี output จริงที่วัดได้ — ตัดทิ้ง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/interesting_aIl/status/2060444204556320949" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CodeByNZ</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 435 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CodeByNZ/status/2060408820111691833">View @CodeByNZ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bad week for AI. &amp;gt; Amazon scrapped its AI leaderboard after costs spiraled &amp;gt; Uber burned billions chasing AI ROI &amp;gt; Starbucks’ AI lost a fight against coffee cups HUMANITY LIVES ANOTHER WEEK. ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ viral รวม AI deployment ล้มเหลวของ Amazon, Uber, และ Starbucks เป็นหลักฐานว่า ROI จาก AI ระดับองค์กรยังไม่เกิดจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่างบใหญ่ไม่ได้การันตี AI ที่ได้ผล — ทีมเล็กที่ทำ AI feature แบบ scoped มี advantage เชิงโครงสร้างเหนือ enterprise ที่ยิง budget กว้าง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">กำหนด measurable outcome ให้ AI feature ทุกตัวก่อน build — ถ้า metric ไม่ขยับภายใน 1 sprint ให้หยุด</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CodeByNZ/status/2060408820111691833" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ylecun</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 379 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ylecun/status/2060713123389305137">View @ylecun on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@Pontifex Indeed, AI today does not do or possess any of those things. But at some point in the future they will. Except perhaps for the spiritual part. Many humans aren't spiritual either, yet have e”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Yann LeCun (Chief AI Scientist, Meta) ตอบ Pope ว่า AI ปัจจุบันยังไม่มี empathy หรือ morality แต่เชื่อว่าอนาคตจะมี ยกเว้นอาจเป็นด้าน spirituality</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ylecun/status/2060713123389305137" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TimnasXtra</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 255 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TimnasXtra/status/2060693059361493027">View @TimnasXtra on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 White Team defeated Red Team 5-4 in Indonesia's internal training match earlier today. Jens Raven scored a hat-trick, while Mitch Baker netted a brace 🎯 📸 @TimnasIndonesia https://t.co/AAaXE18yk2”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีมชาติอินโดนีเซียจัดแมตช์ซ้อมภายใน White Team ชนะ Red Team 5-4 โดย Jens Raven ทำแฮตทริก และ Mitch Baker ยิง 2 ประตู</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TimnasXtra/status/2060693059361493027" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
