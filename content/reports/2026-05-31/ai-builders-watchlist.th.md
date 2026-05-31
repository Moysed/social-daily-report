---
type: social-topic-report
date: '2026-05-31'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-05-31T16:31:18+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.35
sentiment: mixed
confidence: 0.55
tags:
- indie-hackers
- ai-agents
- codex
- video-gen
- devtools
- openclaw
thumbnail: https://pbs.twimg.com/media/HJo95BoXIAsVniK.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-05-31

## TL;DR
- สัปดาห์นี้ dominated ด้วยโพสต์รายได้ indie: marclou รายงาน $87,507 สำหรับ May 2026 [2], jackfriks $59,347 [4]; joint venture ร่วม Ship or Die แบ่ง 50/50 ทำรายได้รวมประมาณ $40K [31][34].
- steipete ย้ายไป San Francisco ช่วง MS Build และกำลังพัฒนา OpenClaw อย่างต่อเนื่อง ซึ่งเป็น personal agent framework แบบ modular/lean ที่ยึดหลัก "เพิ่มเฉพาะสิ่งที่จำเป็น" [1][11].
- signal ใช้งานจริงด้าน coding agent: steipete รายงานว่า Codex เขียน codemods แบบ ad-hoc สำหรับ TypeScript migration ขนาดใหญ่ และใช้ 'autoreview' ร่วมกับ spec ใน agents.md เพื่อควบคุม model ให้ครอบคลุม edge case [21][17][23].
- การเปรียบเทียบ video-gen เป็น live thread ในกลุ่มนี้: Seedance 2.0 vs Gemini Omni Flash โดยมีการโต้แย้งว่าข้อได้เปรียบของ Omni อยู่ที่ distribution/access ไม่ใช่คุณภาพ output โดยตรง [24][25][40][41].
- TrustMRR ของ marclou ตรวจสอบ metrics ของ startup (MRR, churn, visitors) จาก Stripe/GSC/GA และ levelsio เตือนว่าการ claim '$1M ARR in a month' ส่วนใหญ่เป็นการปั่น [18][10].

## What happened
นี่คือ feed ที่ติดตามตัวบุคคล ไม่ใช่ข่าว รายการ engagement สูงส่วนใหญ่เป็นรายงานรายได้รายเดือนของ indie hacker: marclou $87,507 จากหลายโปรเจกต์ (TrustMRR $27K, DataFast $20K, Ship or Die $20K, CodeFast $8K, ShipFast $7K) [2], jackfriks $59,347 [4] และ levelsio รายงานว่าโปรเจกต์หนึ่งถึง $16K MRR ในเวลา 4 เดือน [3]. marclou และ jackfriks ยืนยันว่า Ship or Die เป็น joint venture แบบ 50/50 ดังนั้นแต่ละคนรายงานครึ่งหนึ่งของยอดรวม ~$40K [31][34]. TrustMRR ของ marclou อ้างว่าตรวจสอบ MRR/churn/visitors จาก Stripe, Google Search Console และ Google Analytics [18] ในขณะที่ levelsio เตือนสาธารณะว่าเรื่องเล่าการเติบโต '$1M ARR in a month' ส่วนใหญ่เป็นการสร้างภาพหรือปั่นตัวเลข [10]. นอกจากนี้ steipete ประกาศย้ายไป San Francisco ช่วง MS Build และทำงาน OpenClaw ต่อเนื่อง ซึ่ง frame ไว้เป็น personal agent แบบ modular, minimal [1][11].

## Why it matters (reasoning)
signal ที่มีประโยชน์ที่สุดข้ามเรื่องเป็นเรื่อง operational ไม่ใช่ตัวเลขการเงิน: note ของ steipete เรื่อง Codex สร้าง codemods สำหรับ TypeScript migration [21], การใช้ 'autoreview' เพื่อควบคุม model [17] และการเข้ารหัส edge-case depth ไว้ใน agents.md spec [23] เป็น pattern ที่เป็นรูปธรรมสำหรับ agent-assisted refactoring ที่ทีม web/mobile ของ NDF DEV นำไปใช้ได้ทันที. thesis ของ OpenClaw ที่ว่า 'skills น้อยลง, tools น้อยลง = agent ที่มีประสิทธิภาพมากขึ้น' [11] สอดคล้องกับความกังวลด้าน context management ในทางปฏิบัติ. โพสต์รายได้ส่วนใหญ่เป็น noise สำหรับวัตถุประสงค์ของเรา — มันบ่งบอกว่า niche solo-SaaS/marketing-app ที่ builders กลุ่มนี้อยู่ยังแข็งแกร่ง แต่ตัวเลขเป็น self-reported และ specific กับ portfolio ของแต่ละคน [2][4] และ levelsio เองก็ชี้ว่าหลายอย่างใน genre นี้ถูกปั่น [10]. data point เชิงกลยุทธ์ที่ควรสนใจคือ framing ว่า 'ไม่มีใครต้องการสินค้าที่ดีที่สุดอันดับแปด' ที่อยู่เบื้องหลัง AI valuations อย่าง Anthropic ที่ $1T [32]: ใน AI tooling ตลาดกระจุกตัว ซึ่งสำคัญเมื่อต้องเลือก model/devtool vendor ที่จะ standardize.

## Possibility
**Likely:** agent-assisted codemods และ review loop (Codex/autoreview/agents.md) จะกลายเป็น standard practice สำหรับ migration ในกลุ่มนักปฏิบัติเหล่านี้ เพราะ steipete รายงานว่าใช้งานได้จริงใน production-scale TS work แล้ว [21][23]. **Plausible:** video-gen tooling (Seedance 2.0, Gemini Omni Flash) ยังคง churn ต่อไปโดยไม่มีผู้ชนะชัดเจนในระยะใกล้ — การถกเถียงเน้นที่ distribution vs raw quality ไม่ใช่ความได้เปรียบที่ชัดเจน [41]. **Plausible:** OpenClaw พัฒนาเป็น open personal-agent stack ที่ใช้งานได้จริง แต่ยังเร็วและผูกกับ momentum ของคนเดียว [1][11]. **Unlikely to matter operationally:** monthly MRR theater ยังดำเนินต่อแต่ได้ insight ที่ถ่ายทอดได้น้อยมาก [2][4].

## Org applicability — NDF DEV
1) ทดลองใช้ Codex (หรือเทียบเท่า) กับ TypeScript/Unity-tooling codemod ขอบเขตเล็กและรับ agents.md-style spec มาจำกัด edge-case behavior — low effort, high transfer [21][23]. 2) เพิ่ม 'autoreview' pass (model ตรวจ diff ตัวเองก่อน human review) ใน agent workflow ของ repo หนึ่งและวัดว่าลด review churn ได้หรือไม่ — low effort [17]. 3) ประเมิน Seedance 2.0 vs Gemini Omni Flash สำหรับคลิป marketing/promo ของ game หรือ edutech launch โดยดู access/cost ควบคู่กับคุณภาพ output — med effort [25][40][41]. 4) ติดตาม OpenClaw เป็น reference สำหรับ lean, modular agent design ก่อนเพิ่ม tools เข้า internal agents — low effort [11]. **Skip:** รายงาน MRR [2][4][3] และโพสต์ส่วนตัวที่ไม่เกี่ยวข้อง [9][15][19][25-personal] — ไม่มี action. อย่านำ self-reported revenue มาใช้ sizing market [10].

## Signals to Watch
- ทิศทาง modular/minimal agent ของ OpenClaw และ SF momentum รอบ steipete [1][11].
- Codex codemods + autoreview + agents.md ในฐานะ repeatable migration pattern [21][17][23].
- Seedance 2.0 vs Gemini Omni Flash — distribution-vs-quality framing สำหรับ video gen [40][41].
- verified-metrics model ของ TrustMRR และ pushback ของ levelsio ต่อ inflated growth claims [18][10].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | steipete | ^1239 c74 | [Finally got my visa sorted out and moving to San Francisco, just in time for MS ](https://x.com/steipete/status/2061031509088231640) |
| x | marclou | ^736 c106 | [I made $87,507 in May 2026. ⭐️ TrustMRR — $27K 📈 DataFast — $20K 🏴‍☠️ Ship or Di](https://x.com/marclou/status/2061065911394836861) |
| x | levelsio | ^657 c50 | [Update after 4 months he's at $16K MRR https://t.co/1MpJWnyP9N](https://x.com/levelsio/status/2061027867274674194) |
| x | jackfriks | ^575 c83 | [i made $59,347 in may 2026 ... ($81,919 CAD) 🌉 post bridge — $36K 🏴‍☠️ ship or d](https://x.com/jackfriks/status/2061072407608066353) |
| x | EXM7777 | ^494 c17 | [https://t.co/ip0CFHxG7R](https://x.com/EXM7777/status/2060736517564477901) |
| x | levelsio | ^408 c43 | [https://t.co/yHVz4TUlse](https://x.com/levelsio/status/2060836472958165167) |
| x | vasuman | ^329 c45 | [Imagine an AI company that forward deploys into your enterprise to first underst](https://x.com/vasuman/status/2060847258283999376) |
| x | vasuman | ^320 c46 | [If you're a software engineer that is down for a paid work trial (1-2 weeks, con](https://x.com/vasuman/status/2060866035067343240) |
| x | jackfriks | ^258 c30 | [wife appreciation post (she made me banana bread today) https://t.co/I5ZycalO7d](https://x.com/jackfriks/status/2060871445622796739) |
| x | levelsio | ^245 c17 | [P.S. this is how actual realistc growth looks like You see all these ecom bros n](https://x.com/levelsio/status/2061036511202603374) |
| x | steipete | ^219 c33 | [The idea of OpenClaw is always that it should be yours. It's modular and lean, o](https://x.com/steipete/status/2061072753998856696) |
| x | EXM7777 | ^176 c7 | [this is the Hermes setup top 1% operators are using to get rid of AI slop... htt](https://x.com/EXM7777/status/2061086049326256356) |
| x | marclou | ^155 c34 | [These have been the best 10 years of my life. Entrepreneurship has taught me so ](https://x.com/marclou/status/2061104163745075339) |
| x | rileybrown | ^133 c7 | [What mean? https://t.co/CODJszlnCY](https://x.com/rileybrown/status/2060908536549261320) |
| x | jackfriks | ^109 c18 | [does this look like i'm trolling? this brand new toyota corolla will last longer](https://x.com/jackfriks/status/2061089156374114449) |
| x | steipete | ^104 c2 | [@theo Yes! See ya around this week?](https://x.com/steipete/status/2061038721290400240) |
| x | steipete | ^99 c2 | [@theo @VictorTaelin gotta use autoreview, that keeps gpt honest and usually help](https://x.com/steipete/status/2061036923397845456) |
| x | marclou | ^95 c33 | [Heads up! TrustMRR doesn't just show startup MRR, but also: 📉 Churn 📈 Visitors 👀](https://x.com/marclou/status/2061021034631852295) |
| x | egeberkina | ^93 c0 | [@tervisscoot Average concert in Turkey https://t.co/tExymyP6Ab](https://x.com/egeberkina/status/2060830061381431780) |
| x | rileybrown | ^86 c8 | [@vansh22b Shut up](https://x.com/rileybrown/status/2060910981484622132) |
| x | steipete | ^81 c13 | [Haven't seen codex writing ad-hoc codemods before, but it just did for a bigger ](https://x.com/steipete/status/2061115471760441692) |
| x | steipete | ^68 c8 | [@iruletheworldmo very much depends on the skillset of the person driving the AI.](https://x.com/steipete/status/2060749955707351156) |
| x | steipete | ^67 c3 | [@segolovach parent codex is pretty good at rejecting review comments. You need t](https://x.com/steipete/status/2060794664521781466) |
| x | AmirMushich | ^66 c14 | [GPT-2 x Seedance 2.0 animated logo mockup smart workflow + prompts 👇 Get more de](https://x.com/AmirMushich/status/2060775801121816995) |
| x | egeberkina | ^64 c3 | [Tonight Turkey at Ye's concert 🇹🇷 Made with Omni Flash https://t.co/iHEwBZ5zlP](https://x.com/egeberkina/status/2060828495521976754) |
| x | godofprompt | ^59 c10 | [I pulled a full week of @OpenAI's X analytics without an API key, a scraper, or ](https://x.com/godofprompt/status/2060808562314772519) |
| x | egeberkina | ^56 c0 | [Off-White™ presents: impossible places https://t.co/Bvy2jIR8BD](https://x.com/egeberkina/status/2060705806891249691) |
| x | steipete | ^55 c1 | [@artee_49 charge more for your work](https://x.com/steipete/status/2060702497396650316) |
| x | steipete | ^52 c1 | [@dasPoppers @openclaw Did we had the same idea yesterday? Didn't see your propos](https://x.com/steipete/status/2060974727213027435) |
| x | steipete | ^51 c5 | [@macmatan private one, a few work work. Difference is mostly permissions.](https://x.com/steipete/status/2060750352127770860) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1239 · 💬 74</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061031509088231640">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Finally got my visa sorted out and moving to San Francisco, just in time for MS Build and OpenClaw’s after hours! https://t.co/agbyZ79kb1”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ได้วีซ่าสหรัฐแล้ว และกำลังย้ายไป San Francisco พร้อมกับช่วง MS Build และ after-hours ของ OpenAI</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061031509088231640" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 736 · 💬 106</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2061065911394836861">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I made $87,507 in May 2026. ⭐️ TrustMRR — $27K 📈 DataFast — $20K 🏴‍☠️ Ship or Die — $20K 🧑‍💻 CodeFast — $8K ⚡️ ShipFast — $7K 🐥 Twitter — $3.2K 🦐 SuperShrimp — $1K 🍜 Indie Page — $715 🛡️ ByeDispute — ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Marc Lou รายงานรายได้ $87,507 ในเดือน พ.ค. 2026 จาก 13 products โดย TrustMRR, DataFast และ Ship or Die เป็นตัวนำ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2061065911394836861" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 657 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2061027867274674194">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Update after 4 months he's at $16K MRR https://t.co/1MpJWnyP9N”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio แชร์ update ของ builder รายหนึ่งที่ทำรายได้ $16K MRR ภายใน 4 เดือน โดยไม่ระบุ product, stack หรือวิธีการใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2061027867274674194" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jackfriks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 575 · 💬 83</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jackfriks/status/2061072407608066353">View @jackfriks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i made $59,347 in may 2026 ... ($81,919 CAD) 🌉 post bridge — $36K 🏴‍☠️ ship or die — $20K 🐷 lovelee couples — $3K 📔 year pix — $45 this has become an insanely stupid amount of money to me and doesn't ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie maker @jackfriks รายงานรายได้ $59,347 USD ในเดือนพ.ค. 2026 จาก 4 product ที่สร้างเอง: Post Bridge ($36K), Ship or Die ($20K), Lovelee Couples ($3K), Year Pix ($45)</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jackfriks/status/2061072407608066353" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 494 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2060736517564477901">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/ip0CFHxG7R”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Post นี้มีแค่ลิงก์ X Premium article ที่ต้องสมัครสมาชิกถึงเปิดได้ ไม่มีข้อความหรือบริบทใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EXM7777/status/2060736517564477901" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 408 · 💬 43</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2060836472958165167">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/yHVz4TUlse”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>levelsio โพสต์รูป SUV 18 ยี่ห้อที่ดีไซน์แทบเหมือนกันทุกเจ้า พร้อม quote-tweet ว่าสาเหตุมาจากกฎระเบียบและนโยบายเศรษฐกิจ ไม่ใช่ความต้องการของผู้บริโภค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2060836472958165167" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vasuman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 329 · 💬 45</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vasuman/status/2060847258283999376">View @vasuman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Imagine an AI company that forward deploys into your enterprise to first understand how everything works, then architects what an agent solution looks like custom built for you, and only then builds t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@vasuman เสนอ model: AI firm เข้าฝังตัวในองค์กร เข้าใจ workflow ก่อน แล้ว architect และสร้าง custom agent — และระบุว่ายังไม่มีใครทำแบบนี้ครบวงจร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>model 'discover → architect → build' สำหรับ enterprise AI agents คือ gap ที่ studio เล็กเข้าได้ก่อนที่ big consulting จะมาตีตลาด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">จัด client AI engagement เป็น 3 phases ชัดเจน: audit workflow → architect agent → build agent แล้ว pitch เป็น enterprise service ที่ต่างจากคนอื่น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vasuman/status/2060847258283999376" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vasuman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 320 · 💬 46</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vasuman/status/2060866035067343240">View @vasuman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If you're a software engineer that is down for a paid work trial (1-2 weeks, converts to an internship or full-time offer), come by our office today or tomorrow. I'll interview everyone and get back t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บุคคลรายหนึ่ง (@vasuman) เปิดรับ software engineer ทำ paid work trial 1-2 สัปดาห์ ที่ออฟฟิศ โอกาสต่อเป็น internship หรือ full-time — รับ DM แค่ช่วงสุดสัปดาห์นี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vasuman/status/2060866035067343240" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
