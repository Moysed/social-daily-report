---
type: social-topic-report
date: '2026-06-02'
topic: devops-cloud
lang: th
pair: devops-cloud.en.md
generated_at: '2026-06-02T03:38:09+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- x
regions:
- global
post_count: 135
salience: 0.4
sentiment: mixed
confidence: 0.5
tags:
- cloudflare
- supabase
- vercel
- cost-signal
- latency
- ai-gateway
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2061452121648865280/img/hS8gE8pxV4lWpSMx.jpg
translated_by: claude-sonnet-4-6
---

# DevOps & Cloud — 2026-06-02

## TL;DR
- Cloudflare ประกาศราคาสำหรับ Pipelines, R2 SQL, และ R2 Data Catalog; ยังไม่เริ่มเก็บเงิน และจะแจ้งล่วงหน้า 30 วันก่อนเปิดใช้งาน [30]
- benchmark หนึ่งบน app เดียวกันพบ Supabase free plan อยู่ที่ 1100ms เทียบกับ PlanetScale $5/mo ที่ 230ms [21] — เป็นสัญญาณเรื่อง latency/config ไม่ใช่บทสรุปขั้นสุดท้าย
- รายงานจาก indie app ที่ ship แล้วระบุ Supabase ใช้งบ $50 จากรายได้ $21k ซึ่งน้อยกว่าค่าโฆษณา ($6,500) และ Apple tax ($1,875) มาก [22] — Postgres บน Supabase ถูกมากในระดับ small scale
- MiniMax M3 เปิดตัวบน Cloudflare AI Gateway ในวันแรก พร้อมลด 50% สัปดาห์แรก [53][57]; OpenAI GPT-5.5/5.4/Codex พร้อมใช้งาน GA บน Amazon Bedrock แล้ว [17]
- ส่วนใหญ่ของวันนี้เป็น brand chatter, โพล deploy/database [28][59], และมุก; สัญญาณ reliability หรือ outage จริงมีน้อยมาก

## What happened
ข่าว infra-pricing ที่เป็นรูปธรรมเพียงอย่างเดียวคือ Cloudflare ประกาศอัตราค่าบริการสำหรับ Pipelines, R2 SQL, และ R2 Data Catalog โดยยังไม่เปิดเก็บเงิน และสัญญาว่าจะแจ้งล่วงหน้า 30 วัน [30] มีข้อมูล cost/performance สองจุดที่หมุนเวียนในกลุ่ม: benchmark เดียวที่แสดงให้เห็นว่า Supabase free plan ทำได้ 1100ms เทียบกับ PlanetScale plan $5/mo ที่ 230ms บน app เดียวกัน [21] และ revenue breakdown ที่ Supabase อยู่ที่ $50 จากต้นทุนทั้งหมดบนรายได้ $21k [22] ด้านพวก AI runtime นั้น MiniMax M3 เปิดตัวบน Cloudflare AI Gateway พร้อมส่วนลด 50% สัปดาห์แรก [53][57] และ OpenAI GPT-5.5/5.4/Codex ถึง GA บน Amazon Bedrock แล้ว [17]

## Why it matters (reasoning)
สำหรับ shop ที่ใช้ Next.js + Supabase สัญญาณที่ต้องสนใจคือ cost และ latency ไม่ใช่ความแปลกใหม่ ตัวเลข 1100ms ของ Supabase [21] เป็นเพียงตัวอย่างเดี่ยว แต่ชี้ให้เห็น failure mode จริงที่เกิดได้ — cold connections, region ไม่ตรง, หรือ unpooled queries บน tier ต่ำ — ซึ่งทำให้ production response ช้าได้จริง; ควรตรวจสอบตัวเองก่อน ไม่ใช่คิดเรื่อง migration ค่า Supabase $50 บนรายได้ $21k [22] ยืนยันว่า managed Postgres ยังถูกอยู่จนกว่า traffic จะโตขึ้น ดังนั้นบิลที่หนักกว่าอยู่ที่อื่น (ค่าโฆษณา, app-store tax, AI API calls ที่ $1,000) ราคา Cloudflare สำหรับ R2 SQL/Pipelines/Data Catalog [30] มีผลทางอ้อม: ทีมที่ใช้ R2 สำหรับ assets หรือ logs อยู่แล้วมี meter ที่ต้องคำนวณก่อนที่การเก็บเงินจะเริ่มต้น AI Gateway ที่เพิ่ม M3 [53][57] และ Bedrock ที่เพิ่ม OpenAI models [17] สะท้อน trend ของ routing/observability layer ที่นั่งอยู่หน้า model calls ซึ่งเป็นจุดที่ AI-feature runtime cost และ reliability ถูกจัดการมากขึ้นเรื่อยๆ

## Possibility
**Likely:** Cloudflare จะเปิดเก็บเงิน Pipelines/R2 SQL/R2 Data Catalog ภายในราวหนึ่งเดือนหลังแจ้ง 30 วัน ใครที่ prototype อยู่ควรคาดว่า meter จะเปิดเร็วๆ นี้ [30] **Plausible:** ช่องว่าง latency ระหว่าง Supabase กับ PlanetScale [21] มาจาก tier/region/pooling เป็นหลัก ไม่ใช่ตัว engine และสามารถปิดช่องได้เมื่อ config ถูกต้อง — ใช้ตัวเลขนี้เป็นแรงกระตุ้นให้วัด ไม่ใช่ proof **Plausible:** AI Gateway กลายเป็น default front door สำหรับ model calls เมื่อรองรับ M3 ตั้งแต่วันแรกพร้อมส่วนลด [53][57] **Unlikely:** รายการใดในวันนี้เป็นสัญญาณ reliability problem ของ Supabase หรือ Vercel — กระแสลบเป็นเรื่องมุก [8][46][52] และ stock/layoff talk [18][41] ไม่ใช่ incident

## Org applicability — NDF DEV
1) ตรวจ latency ของ production Supabase queries (region match, connection pooling/pgBouncer, indexed reads) ก่อนจะเชื่อหรือปัดทิ้งตัวเลข 1100ms — effort ต่ำ [21]. 2) ถ้าใช้หรือวางแผนใช้ R2 สำหรับ asset/log storage ให้คำนวณอัตรา Pipelines/R2 SQL/Data Catalog ใหม่ตอนนี้ขณะที่ billing ยังปิดอยู่และนาฬิกา 30 วันยังไม่เริ่ม — effort ต่ำ [30]. 3) คง Supabase เป็น Postgres layer ต่อไป; ข้อมูล $50-บน-$21k ยืนยันว่าเป็น cost line เล็กน้อยในระดับ scale ของเรา — effort ต่ำ ไม่ต้องเปลี่ยน [22]. 4) ถ้าเพิ่ม AI features ให้ route model calls ผ่าน Cloudflare AI Gateway (หรือ Bedrock) เพื่อ cost caps และ observability แทนการเรียก provider โดยตรง — effort กลาง [53][57][17][54]. 5) เสริม dev-ergonomics ไม่บังคับ: Cloudflare Tunnels menu-bar tool สำหรับ expose local dev servers — effort ต่ำ [26]. ข้ามได้: HydraDB และ agent-context products [1], stock/macro และ layoff threads [9][18][19][34][41], และโพสต์ Claude-Code-$1000 stunt [33][36] — ไม่มีคุณค่าเชิง operational

## Signals to Watch
- Cloudflare จะเปิด billing สำหรับ R2 SQL/Pipelines/Data Catalog เมื่อไร และ cost จริงต่อ GB เมื่อเปิดแล้ว [30]
- การทดลองซ้ำช่องว่าง latency ระหว่าง Supabase กับ PlanetScale — 1100ms มาจาก config หรือ engine? [21]
- การ adopt AI Gateway ในฐานะ routing/observability layer สำหรับ model calls [53][57][54]
- ความเหนือกว่าของ Vercel ในเชิง product เทียบกับ Cloudflare/Render/Netlify ที่กำลังตามทัน [42][59]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | contextkingceo | ^1475 c197 | [Introducing HydraDB. The graph native context infrastructure for agents. Purpose](https://x.com/contextkingceo/status/2061452631298752790) |
| x | rauchg | ^1432 c193 | [Unclear if a durable trend, but CEOs and CTOs are back to coding with a fury, th](https://x.com/rauchg/status/2061135404942974982) |
| x | pontusab | ^1107 c50 | [Introducing Caltext, open-source calorie tracking in iMessage. Built with: • Bun](https://x.com/pontusab/status/2061410279922282556) |
| x | NVIDIAGeForce | ^570 c28 | [DLSS 4.5 is powering today's hits &amp; tomorrow's releases including: 🟢 Phantom](https://x.com/NVIDIAGeForce/status/2061485433314250932) |
| x | vivekgalatage | ^551 c3 | [If low-level systems excite you, then you will enjoy reading this branch predict](https://x.com/vivekgalatage/status/2060952271845031972) |
| x | rauchg | ^504 c29 | [Beautiful example of a full-stack agent on @vercel. Great learning material!](https://x.com/rauchg/status/2061415178298937365) |
| x | theo | ^414 c11 | [@NoamTenne @Cloudflare In my case, it's largely because they listen. I always pr](https://x.com/theo/status/2061198227232506353) |
| x | thdxr | ^411 c10 | [@supabase i have better hair than this](https://x.com/thdxr/status/2061226764798398871) |
| x | ai_trade_pro | ^369 c2 | [Worth remembering as next week's macro data starts hitting: In February, a singl](https://x.com/ai_trade_pro/status/2061083295568232656) |
| x | _MaxBlade | ^367 c17 | [The most powerful combo right now is Hermes + Cloudflare agent token + Hetzner V](https://x.com/_MaxBlade/status/2061232496415514877) |
| x | GlobalWatchClub | ^349 c10 | [The Rolex Land-Dweller Do you like the honeycomb dial? https://t.co/lWxeCHjvGl](https://x.com/GlobalWatchClub/status/2061043647252947280) |
| x | ArthurMacwaters | ^325 c47 | [🚨 Excited to announce we're hosting the first Autonomous Healthcare Hackathon! S](https://x.com/ArthurMacwaters/status/2061188831165268200) |
| x | tomfgoodwin | ^309 c133 | [errmmmmm, not to be miserable but has anyone noticed that agentic AI doesn't rea](https://x.com/tomfgoodwin/status/2061081009580605483) |
| x | nexxeln | ^308 c10 | [every job i've had came from people finding me through my work / twitter / githu](https://x.com/nexxeln/status/2061150758922604798) |
| x | Rainmaker1973 | ^308 c7 | [Tibet's Donggar and Piyang Grottoes are a massive, X century archaeological comp](https://x.com/Rainmaker1973/status/2060978575688298616) |
| x | ai_trade_pro | ^292 c0 | [Quietly one of the most important AI updates of the month, and it's not a benchm](https://x.com/ai_trade_pro/status/2061479694361395504) |
| x | awscloud | ^287 c21 | [Now generally available, @OpenAI GPT-5.5, GPT-5.4, and Codex on Amazon Bedrock. ](https://x.com/awscloud/status/2061564484523524302) |
| x | PeterDiamandis | ^255 c44 | [Tech companies are laying off people by the thousands, doing so without an ounce](https://x.com/PeterDiamandis/status/2061484183441305965) |
| x | StockMKTNewz | ^232 c71 | [All these stocks hit new 52 WEEK HIGHS at some point today Micron $MU Broadcom $](https://x.com/StockMKTNewz/status/2061533276821479572) |
| x | delvieero | ^214 c195 | [Honeycomb uncapping 👏🏻 🍯 🐝 ❤️ https://t.co/9x3NdAz0rf](https://x.com/delvieero/status/2061576021405503791) |
| x | _skris | ^213 c13 | [tested the @supabase free plan and @PlanetScale $5/mo plan for a simple app supa](https://x.com/_skris/status/2061125813886431571) |
| x | athcanft | ^197 c27 | [cost breakdown on $21k rev: ad spend: $6,500 apple tax: $1,875 ai api costs: $1,](https://x.com/athcanft/status/2061319369494606054) |
| x | PopPunkOnChain | ^191 c19 | [Pumpcade is now a Tier 1 @Cloudflare startup. We just recieved $350,000 in credi](https://x.com/PopPunkOnChain/status/2061449233153057214) |
| x | NVIDIAGeForce | ^179 c9 | [Explore, adapt, and survive Sota7 with #RTXOn. Honeycomb: The World Beyond arriv](https://x.com/NVIDIAGeForce/status/2061531530514575769) |
| x | eastdakota | ^172 c15 | [I'm very confused by the @Cloudflare Lisbon Office common area soundtrack today.](https://x.com/eastdakota/status/2061397318734114883) |
| x | Mouxy | ^151 c8 | [Create and manage Cloudflare Tunnels from your macOS menu bar. Bind tunnels to l](https://x.com/Mouxy/status/2061220019950772308) |
| x | greenvibe | ^150 c8 | [Morel mushrooms are prized for their honeycomb texture and earthy flavor https:/](https://x.com/greenvibe/status/2061450946639708591) |
| x | adahstwt | ^144 c94 | [hey developers, which database are you using the most recently: 1) Supabase 2) P](https://x.com/adahstwt/status/2061435886437625982) |
| x | gudmundur | ^137 c10 | [After nearly 4.5 years at Vercel, this week was my last. When I joined, I came i](https://x.com/gudmundur/status/2061055564931600885) |
| x | _ashleypeacock | ^137 c9 | [Pricing has been announced for Cloudflare Pipelines, R2 SQL and R2 Data Catalog!](https://x.com/_ashleypeacock/status/2061512995256012990) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@contextkingceo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1475 · 💬 197</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/contextkingceo/status/2061452631298752790">View @contextkingceo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing HydraDB. The graph native context infrastructure for agents. Purpose built to deliver precise context &amp; observability into why agents act the way they do. We've always believed graphs are ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>HydraDB คือ context store แบบ graph-native สำหรับ AI agent รวม in-memory, NVMe, และ object storage ไว้ในชั้นเดียว เพื่อ context retrieval ที่เร็วและถูกกว่า graph DB ทั่วไป</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่สร้าง agent pipeline หลายขั้นตอนต้องการ context retrieval ที่มีโครงสร้างและ latency ต่ำ HydraDB เล็งแก้ bottleneck นั้นโดยตรงด้วย tiered storage architecture</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Benchmark HydraDB เทียบกับ vector หรือ relational store ที่ใช้อยู่ตอน scope agentic feature ถัดไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/contextkingceo/status/2061452631298752790" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1432 · 💬 193</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2061135404942974982">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Unclear if a durable trend, but CEOs and CTOs are back to coding with a fury, thanks to coding agents. I have public company CEOs sliding into my DMs (and “InMail”) telling me about falling in love wi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>CEO ของ Vercel รายงานว่า C-suite ในบริษัทใหญ่กลับมา coding เองผ่าน agents อย่าง Claude Code ทำให้ enterprise เลือก software จากการใช้งานจริงแทน top-down sales</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เมื่อ executive ของ client ประเมิน dev tools ได้เอง คุณภาพ stack จริงของ studio กลายเป็นตัวตัดสิน ไม่ใช่ความสัมพันธ์กับ vendor</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Studio ควร demo Vercel และ Claude Code ได้คล่องตอน pitch งาน enterprise เพราะ C-suite ที่ target อยู่ตอนนี้เป็น hands-on users ไม่ใช่แค่ผู้อนุมัติ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2061135404942974982" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@pontusab</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1107 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/pontusab/status/2061410279922282556">View @pontusab on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing Caltext, open-source calorie tracking in iMessage. Built with: • Bun + Turborepo • Hono on Nitro (Vercel) • Chat SDK + Sendblue • AI SDK + GPT-4.1 vision • Upstash Redis • Vercel Workflows”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Caltext คือ open-source calorie tracker ใน iMessage ใช้ Hono/Nitro บน Vercel, GPT-4.1 vision, Upstash Redis และ Vercel Workflows ประมวลผลรูปอาหารที่ส่งมาทาง SMS</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การรวม Hono + Nitro + Vercel Workflows + Upstash Redis เป็น pattern จริงสำหรับ serverless AI pipeline ที่เบาและ source เปิดดูได้เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">studio ใช้ repo นี้เป็น reference ดู Vercel Workflows + Upstash Redis สำหรับ async AI processing ใน web หรือ e-learning feature ในอนาคต</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/pontusab/status/2061410279922282556" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NVIDIAGeForce</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 570 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NVIDIAGeForce/status/2061485433314250932">View @NVIDIAGeForce on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“DLSS 4.5 is powering today's hits &amp;amp; tomorrow's releases including: 🟢 Phantom Blade Zero 🟢 CINDER CITY 🟢 Squad 🟢 Marvel Rivals 🟢 Gothic 1 Remake 🟢 NARAKA: Bladepoint 🟢 Honeycomb: The World Beyond 🟢”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>NVIDIA GeForce โปรโมต DLSS 4.5 โดยแสดงรายชื่อเกม 8+ ตัวที่รองรับ เช่น Marvel Rivals และ NARAKA: Bladepoint ในแคมเปญ #RTXON</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NVIDIAGeForce/status/2061485433314250932" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vivekgalatage</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 551 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vivekgalatage/status/2060952271845031972">View @vivekgalatage on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If low-level systems excite you, then you will enjoy reading this branch prediction blog from cloudflare. https://t.co/scdxmks3NJ https://t.co/GJT0OKjcj3”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Cloudflare เผยแพร่บทความเชิงลึกเรื่อง CPU branch prediction อธิบายการทำงานของ speculative execution และผลกระทบต่อ performance จริงๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เขียน code ที่ CPU branch-friendly ใน hot path ของ Unity เช่น game loop, physics, AI tick ช่วยลด frame time ได้จริงโดยไม่ต้องเปลี่ยน algorithm</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ส่งบทความนี้ให้ทีม Unity ใช้เป็น reference ตอน profile และ optimize loop ที่ performance-critical ในโปรเจกต์ปัจจุบันหรือที่กำลังจะมา</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vivekgalatage/status/2060952271845031972" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 504 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2061415178298937365">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Beautiful example of a full-stack agent on @vercel. Great learning material!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Guillermo Rauch (CEO Vercel) ยก full-stack AI agent บน Vercel เป็น learning material สะท้อนว่า Vercel กำลัง push agentic app patterns บน platform ของตัวเอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Vercel กำลัง position เป็น host หลักสำหรับ agentic web app — pattern ที่ CEO ชู มักกลาย first-class feature ใน 1-2 ไตรมาส</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดูตัวอย่างใน link แล้วเช็คว่า architecture (streaming, tool calls, API routes) match กับ Vercel/Next.js stack ที่ studio ใช้อยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2061415178298937365" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 414 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2061198227232506353">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@NoamTenne @Cloudflare In my case, it's largely because they listen. I always prefer private crash outs to public ones. Never underestimate the sheer number of people at CF who are eager to hear every”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@theo บอกว่า Cloudflare มีทีมที่พร้อมรับฟีดแบ็กแบบ private และพยายามแก้ปัญหาจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2061198227232506353" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@thdxr</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 411 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/thdxr/status/2061226764798398871">View @thdxr on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@supabase i have better hair than this”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@thdxr โพสต์ตลกขำขันหนึ่งบรรทัดถึง Supabase เกี่ยวกับรูปภาพ ไม่มีเนื้อหาเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/thdxr/status/2061226764798398871" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
