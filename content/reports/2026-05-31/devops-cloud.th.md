---
type: social-topic-report
date: '2026-05-31'
topic: devops-cloud
lang: th
pair: devops-cloud.en.md
generated_at: '2026-05-31T16:18:20+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- x
regions:
- global
post_count: 85
salience: 0.45
sentiment: mixed
confidence: 0.5
tags:
- vercel
- supabase
- cloudflare
- cost-control
- security
- observability
thumbnail: https://pbs.twimg.com/media/HJgHDctXcAcja_F.png
translated_by: claude-sonnet-4-6
---

# DevOps & Cloud — 2026-05-31

## TL;DR
- ประเด็นค่าใช้จ่ายพุ่งเกินงบครองพื้นที่: โพสต์เตือนบิล Supabase $200 ข้ามคืนบนแอปที่ vibe-coded [52], ล้อเลียน '$30k Vercel invoice' [30], และมุมมอง '$5 VPSification of Vercel' [12] — เทียบกับ Cloudflare ที่ผู้ใช้รายงานบิล $0 บน free tier [55][29].
- ความเสี่ยงด้านความปลอดภัยบนแอปที่ใช้ Supabase ถูกหยิบยกตรงๆ — เงินหาย overnight, spam ท่วม, และหนังสือ cease-and-desist จากการขาด protection [52][41]; Ghost CMS SQL injection แยกต่างหากเปิดช่องให้ขโมย admin API keys และ inject JS [27].
- Vercel ส่ง Docker-in-Sandbox (รัน container, database, test suite แบบ isolated, persist ข้ามเซสชัน) [14][32], Data Pipeline 5GB/s พร้อม fanout/dedup/at-least-once delivery [21], และ Slack integration [39].
- Cloudflare ดัน agent-oriented primitives — Web Search สำหรับ Workers/agents [16], Browser Run quick actions (ดึง markdown/screenshot) [48][53] — พร้อมกันนั้นตัดพนักงาน ~20% [34].
- Observability ถูกมองว่าเป็น production bottleneck: เชื่อม Claude เข้า trace data เจอ slow path 5 วินาทีที่ Platzi [10]; Expo เปิด mobile observability beta [20].

## สิ่งที่เกิดขึ้น
ไอเทมที่ engagement สูงส่วนใหญ่เป็น meme (Railway 'shupo' [2][4][8][9], honeycomb [17][23][28][42]) หรือ poll [49][56] ที่แทบไม่มีเนื้อหาเชิงเทคนิค signal ที่มีประโยชน์กระจุกอยู่สี่กลุ่ม: **Cost** — เตือนบิล Supabase ที่ไม่ทันตั้งตัวและ security drain บนแอป vibe-coded [52], '$30k invoice' viral ที่แทง Vercel [30], คำว่า '$5 VPSification of Vercel' [12], การเรียกร้อง Vercel EC2 alternative [37] — เทียบกับรายงาน Cloudflare $0 bill [55][29]. **Platform moves** — Vercel เพิ่ม Docker ใน Sandbox [14][32], บรรยาย Data Pipeline 5GB/s พร้อม multi-fanout, dedup และ at-least-once delivery [21], และ Slack integration [39]; Cloudflare เพิ่ม Web Search สำหรับ Workers/agents [16] และ Browser Run quick actions [48][53] พร้อมประกาศเลิกจ้าง ~20% [34]. **Security** — Ghost CMS SQL injection เปิดเผย admin API keys และเปิดช่องให้ JS injection [27], และแอป Supabase ถูกชี้ว่าถูก ship ออกไปโดยไม่มี protection [52][41]. **Observability** — Claude เชื่อม trace data เจอ bottleneck 5 วินาทีที่ Platzi [10], และ Expo เปิดตัว mobile observability beta [20]. Supabase Postgres best-practice skill ตอนนี้ bundle มาใน Codex plugin 'Build Web Apps' [24].

## ทำไมถึงสำคัญ (เหตุผล)
เรื่องค่าใช้จ่ายและความปลอดภัยตรงกับ stack Next.js + Supabase ของ studio โดยตรง รายงาน surprise bill [52][30][12] สะท้อน usage-based pricing ที่ misconfiguration หรือ query ไม่มีขอบเขตทบต้นเงียบๆ — failure mode เดียวกับที่ทำให้โดน page ตี 3 และบิล runtime บวม คำเตือน Supabase drain [52][41] ชี้ root cause ที่ชัดเจนและเกิดซ้ำ: row-level security กับ rate limit ที่ไม่ได้ตั้งบนแอป ship เร็ว ทำให้ database เปิดโล่ง Ghost SQLi [27] เตือนว่า self-hosted CMS ใดๆ ใน stack คือ attack surface สำหรับขโมย key ในฝั่ง platform Docker-in-Sandbox [14][32] ลด gap ระหว่าง local กับ CI test environment ซึ่งช่วยลด deploy failure แบบ 'works on my machine' เศรษฐศาสตร์ $0 bill ของ Cloudflare [55][29] เป็นจริงสำหรับ internal tool traffic ต่ำ แต่การเลิกจ้าง 20% [34] เป็น second-order signal ที่ควรจับตาเรื่อง support และ roadmap ของสิ่งที่ mission-critical อยู่บนนั้น เรื่อง observability [10][20] ยืนยันว่า reliability win ที่ถูกที่สุดคือ trace-level visibility เข้า slow path ก่อนมันจะ page ใคร

## ความเป็นไปได้
**Likely:** bill shock แบบ usage-based บน Supabase/Vercel ยังคงเป็นความเสี่ยงที่มีชีวิตสำหรับแอปที่ ship โดยไม่มี spend cap และ RLS ดูจากปริมาณและความเฉพาะเจาะจงของ complaint [52][30][12]. **Plausible:** Vercel ขยายต่อเนื่องเข้าสู่ container/long-running-compute (Docker Sandbox วันนี้ [14][32], EC2-style requests [37]) ลดเหตุผลที่ต้องเพิ่ม VPS แยก. **Plausible:** Cloudflare free tier กับ agent primitives [16][48][53][55] จะกลายเป็น default ที่ถูกกว่าสำหรับ internal tool และ edge task. **Unlikely short-term:** layoff Cloudflare [34] กระทบความเสถียรของบริการ — ไม่มีไอเทมไหนแสดง operational impact เป็นแค่ headline เรื่องพนักงาน ไม่มีแหล่งข้อมูลใดให้ตัวเลข probability; ไม่มีการแต่งขึ้นที่นี่

## การนำไปใช้กับ NDF DEV
1) Audit Supabase project production ทุกตัวว่า RLS เปิดครบทุก table บวก rate limit ต่อ route — แก้ปัญหา drain/bill pattern ที่มีหลักฐานโดยตรง [52][41]. Effort: med. 2) ตั้ง hard spend cap / billing alert บน Vercel และ Supabase เพื่อกัน overrun เงียบ [30][12][52]. Effort: low. 3) นำ Supabase Postgres best-practice skill จาก Codex plugin มาใช้เป็น review checklist สำหรับ schema ใหม่ [24]. Effort: low. 4) เชื่อม trace/observability data ที่มีอยู่เข้า AI assistant เพื่อสแกน slow path ก่อนถูก page ตาม Platzi 5s find [10]. Effort: low-med. 5) สำหรับ internal tool traffic ต่ำ ให้ default ไป Cloudflare free tier แทน Vercel compute แบบจ่ายเงิน [55][29]. Effort: med (migration). 6) ใช้ Vercel Docker Sandbox จัดให้ CI test environment ตรงกับ prod container [14][32]. Effort: med. 7) ถ้ามี Ghost CMS instance อยู่ใน stack ให้ patch SQLi ทันที [27]. Effort: low. ข้าม: Railway memes [2][4][8][9], honeycomb/quantum/watch noise [17][23][28], free-hosting list-bait [35], และโพสต์ VC/culture [5][6][45] — ไม่มีคุณค่าเชิงปฏิบัติ

## Signals ที่ต้องจับตา
- Vercel เข้าสู่ container และ pipeline [14][32][21] — ติดตามว่ามันลบความจำเป็นของ VPS/EC2 แยกสำหรับ long-running job ของ studio [37] ได้หรือเปล่า.
- Cloudflare เลิกจ้าง ~20% [34] — ดู support responsiveness และ roadmap ของสิ่งที่พึ่งพาอยู่.
- ความถี่ของเรื่องบิล/ความปลอดภัย Supabase [52][41] — เป็น proxy ว่า RLS-by-default tooling ดีขึ้นหรือเปล่า.
- Mobile observability tooling (Expo beta [20]) — เกี่ยวข้องถ้า app work ของ studio ต้องการ crash/perf visibility หลัง release.

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Railway | ^13435 c228 | [https://t.co/PLdn2N1GK8 https://t.co/nHw363jtqc](https://x.com/Railway/status/2060411091725832643) |
| x | Railway | ^1251 c3 | [@zeroxdayz Not hacked- shupo Hikari is the name of one of the high-speed Shinkan](https://x.com/Railway/status/2060566138522599464) |
| x | theo | ^935 c53 | [First donation is up, just gave $2,000 to @heyandras to support open source alte](https://x.com/theo/status/2060494740433571955) |
| x | Railway | ^913 c0 | [@rv32e shupo](https://x.com/Railway/status/2060486690351812987) |
| x | 31Carlton7 | ^640 c51 | [just wrapped up my first week at @vercel and @aisdk initial thoughts: - pace is ](https://x.com/31Carlton7/status/2060804842868908427) |
| x | immad | ^568 c25 | [Every VC had a reason Vercel shouldn't exist. Guillermo Rauch heard a different ](https://x.com/immad/status/2060466505251197435) |
| x | arpit_bhayani | ^491 c26 | [Everyone talks about agent intelligence. Then agents reach production - or face ](https://x.com/arpit_bhayani/status/2060717906296803457) |
| x | Railway | ^485 c0 | [@disk_writes shupo](https://x.com/Railway/status/2060486704427848062) |
| x | Railway | ^477 c4 | [We're in good company https://t.co/RdcAnhDKnZ](https://x.com/Railway/status/2060473943799062840) |
| x | freddier | ^409 c24 | [Claude made Platzi 10x faster. Platzi's dev team connected Claude to our observa](https://x.com/freddier/status/2060481390874148878) |
| x | xai | ^394 c19 | [It's also available via OpenRouter and Vercel AI Gateway, as well as in Cursor, ](https://x.com/xai/status/2060392251520594105) |
| x | jacobmparis | ^372 c10 | [the $5 VPSification of vercel is well underway](https://x.com/jacobmparis/status/2060447494924902547) |
| x | freeCodeCamp | ^360 c2 | [Building a basic RAG system is one thing. Making it secure, scalable, and produc](https://x.com/freeCodeCamp/status/2060572170988761187) |
| x | vercel_dev | ^357 c14 | [Run Docker inside Vercel Sandbox. ▪︎ Build and run containers in full isolation ](https://x.com/vercel_dev/status/2060443240902627388) |
| x | ai_trade_pro | ^351 c2 | [Worth remembering as next week's macro data starts hitting: In February, a singl](https://x.com/ai_trade_pro/status/2061083295568232656) |
| x | CherryJimbo | ^347 c20 | [Cloudflare is working on Web Search, giving AI agents and Workers real-time acce](https://x.com/CherryJimbo/status/2060717359979958513) |
| x | CharlesMullins2 | ^305 c19 | [🚨 SCIENTISTS MAY HAVE FOUND A CHEAPER PATH TO QUANTUM COMPUTERS AND IT LOOKS LIK](https://x.com/CharlesMullins2/status/2060424341268164706) |
| x | jerryjliu0 | ^276 c4 | [Parse PDFs in the browser, or the edge, in milliseconds Our LiteParse WASM packa](https://x.com/jerryjliu0/status/2060395856860455265) |
| x | vivekgalatage | ^242 c1 | [If low-level systems excite you, then you will enjoy reading this branch predict](https://x.com/vivekgalatage/status/2060952271845031972) |
| x | expo | ^237 c7 | [🆕 Today we open up the beta for our new mobile Observability service. If you've ](https://x.com/expo/status/2060423327781700091) |
| x | tobiaslins | ^231 c7 | [We've been using similar concepts when building Vercel Data Pipeline - Processin](https://x.com/tobiaslins/status/2060782772461973622) |
| x | QuinnyPig | ^168 c2 | [So @cloudflare has been saying they're an agentic cloud. Let's test the theory. ](https://x.com/QuinnyPig/status/2060523529494569023) |
| x | Rainmaker1973 | ^154 c7 | [Tibet's Donggar and Piyang Grottoes are a massive, X century archaeological comp](https://x.com/Rainmaker1973/status/2060978575688298616) |
| x | supabase | ^142 c7 | [The official "Build Web Apps" plugin for Codex ships with the Supabase Postgres ](https://x.com/supabase/status/2060732268696555549) |
| x | llama_index | ^132 c8 | [When we say "LiteParse runs everywhere," we mean it. Our WASM package is lightwe](https://x.com/llama_index/status/2060392729910116830) |
| x | pythontrending | ^131 c1 | [awesome-harness-engineering - Awesome list for AI agent harness engineering: too](https://x.com/pythontrending/status/2060395787901702207) |
| x | Playerinthgame | ^129 c3 | [What does this mean? Ghost is a widely used CMS. A SQL injection flaw lets remot](https://x.com/Playerinthgame/status/2060397849305575536) |
| x | GlobalWatchClub | ^105 c7 | [The Rolex Land-Dweller Do you like the honeycomb dial? https://t.co/lWxeCHjvGl](https://x.com/GlobalWatchClub/status/2061043647252947280) |
| x | unk_data | ^104 c5 | [I actually did last week, but don't want to pay for backend to keep it alive. Ma](https://x.com/unk_data/status/2060576950750716205) |
| x | AvgDatabaseCEO | ^102 c1 | [Vercel CEO would spend the time in the corner posting selfies then send you a $3](https://x.com/AvgDatabaseCEO/status/2060530275336003604) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Railway</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 13435 · 💬 228</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Railway/status/2060411091725832643">View @Railway on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/PLdn2N1GK8 https://t.co/nHw363jtqc”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Railway ออก Summer 2026 update สรุปสิ่งที่ ship แล้ว — distributed multi-cloud routing, HA Postgres one-click บน Patroni, real SSH ใน CLI — พร้อม roadmap agent-native sandbox, frontend CDN, และ self-healing deployments</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>HA Postgres one-click และ self-healing deployments ลด ops overhead ได้จริงสำหรับทีมเล็ก; remote MCP server ใน roadmap รองรับ agent-driven deploy pipeline โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง Railway HA Postgres แทน DB ที่ manage เองอยู่ และ track feature remote MCP server สำหรับ agent-driven deploy workflow ในอนาคต</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Railway/status/2060411091725832643" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Railway</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1251 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Railway/status/2060566138522599464">View @Railway on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@zeroxdayz Not hacked- shupo Hikari is the name of one of the high-speed Shinkansen Hikari is also the codename of our fleet of CDN POPs around the world that makes our website super fast pic maybe re”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Railway ชี้แจงว่า 'Hikari' คือชื่อ codename ของ CDN POP fleet ทั่วโลกของพวกเขา ไม่ใช่การถูก hack — ตั้งชื่อตามรถไฟ Shinkansen Hikari</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Railway/status/2060566138522599464" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 935 · 💬 53</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2060494740433571955">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“First donation is up, just gave $2,000 to @heyandras to support open source alternatives to Codex App and Claude Desktop 🫡 Also pumped that this can help with Coolify, the coolest open source hosting ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Theo บริจาค $2,000 ให้ @heyandras สร้าง open-source alternatives แทน Codex App และ Claude Desktop พร้อมชู Coolify เป็น self-hosted deployment platform ทางเลือกแทน Vercel</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Coolify เป็น open-source PaaS ที่ self-host ได้ ช่วยทีมเล็กลด cost จาก Vercel ทั้ง per-seat และ bandwidth</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม web stack ลอง deploy Coolify บน VPS สำรองก่อน project หน้าที่จะใช้ Vercel</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2060494740433571955" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Railway</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 913 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Railway/status/2060486690351812987">View @Railway on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@rv32e shupo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Account ทางการของ Railway โพสต์ข้อความ '@rv32e shupo' ซึ่งไม่มีเนื้อหาหรือประกาศใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Railway/status/2060486690351812987" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@31Carlton7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 640 · 💬 51</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/31Carlton7/status/2060804842868908427">View @31Carlton7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“just wrapped up my first week at @vercel and @aisdk initial thoughts: - pace is insane. onboarding was only two days then they get us working in prod codebase immediately after - you don’t wait for pe”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>พนักงานใหม่ของ Vercel เล่าว่า onboarding แค่ 2 วันแล้ว work ใน production codebase เลย วัฒนธรรมองค์กรเน้น bias-toward-action และ build in public</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โมเดล onboarding 2 วันแล้วลง prod สะท้อนว่าทีมเร็วๆ คาดหวังให้ ship ได้เลย ไม่รอ ramp-up นาน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมลองใช้แนวเดียวกัน: dev ใหม่รับ task จริงใน codebase จริงวันที่ 3 ไม่ใช่แค่ทำ sandbox</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/31Carlton7/status/2060804842868908427" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@immad</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 568 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/immad/status/2060466505251197435">View @immad on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Every VC had a reason Vercel shouldn't exist. Guillermo Rauch heard a different reason from every investor he spoke to when building Vercel, and he kept going anyway. He joined us live at Mercury HQ i”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Mercury VC จัด founder event และโปรโมต podcast ที่ Guillermo Rauch (CEO, Vercel) เล่าถึงการถูก investor ปฏิเสธก่อน Vercel จะสำเร็จ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/immad/status/2060466505251197435" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@arpit_bhayani</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 491 · 💬 26</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/arpit_bhayani/status/2060717906296803457">View @arpit_bhayani on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Everyone talks about agent intelligence. Then agents reach production - or face even the slightest bit of load - and suddenly the hard problems are: - memory management - concurrency - backpressure - ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Arpit Bhayani ชี้ว่า AI agent ใน production พังเพราะปัญหา backend คลาสสิก เช่น memory, concurrency, backpressure, retry, timeout, observability ไม่ใช่เรื่อง AI</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ทำ agentic feature ต้องวาง reliability infrastructure แบบเดียวกับ distributed system ทั่วไป — AI layer ไม่ได้แทนงาน engineering พวกนี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อนขยาย agent workflow ใด ๆ ให้ใส่ structured logging, timeout budget, และ retry policy — ดูเป็น microservice ไม่ใช่แค่ prompt</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/arpit_bhayani/status/2060717906296803457" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Railway</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 485 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Railway/status/2060486704427848062">View @Railway on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@disk_writes shupo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Railway โพสต์ข้อความ '@disk_writes shupo' ซึ่งไม่มีเนื้อหาทางเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Railway/status/2060486704427848062" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
