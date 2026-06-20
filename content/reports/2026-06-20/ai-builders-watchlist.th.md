---
type: social-topic-report
date: '2026-06-20'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-06-20T15:56:52+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.45
sentiment: mixed
confidence: 0.55
tags:
- ai-builders
- model-selection
- design-agents
- vibe-coding
- indie-hacking
- agentic-workflows
thumbnail: https://pbs.twimg.com/media/HLNHoQhXMAANhKP.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-06-20

## TL;DR
- theme หลักสัปดาห์นี้คือ model specialization: ผู้ใช้จริงรายงานว่า Opus 4.8 (ใน Claude Code) นำด้าน business/marketing/writing ส่วน GPT-5.5 (ใน Codex) นำด้าน coding [9]; builder คนหนึ่ง ship general-agent iOS app บน GPT-5.5 โดยมี GLM-5.2 ทำงานอยู่เบื้องหลัง [11]
- GLM-5.2 ได้รับการตอบรับแบบผ่าสอง — ฝั่งหนึ่งโปรโมตว่าใกล้เคียง Fable-5 benchmark ผ่าน setup แบบ 'council of models' [8] แต่อีกฝั่งในวงเดียวกันบอกว่าอ่อนแอใน agent loop จริง [47]
- Design agent กำลังแทนที่ Figma/Photoshop สำหรับ marketing asset: AmirMushich แสดง carousel/Instagram template generation ผ่าน trymoda/Moda พร้อม reusable brand kit [10][48][54][55][57]; MengTo แชร์ 'giant prompt' สำหรับสร้าง landing page จากคลัง template 5,009 หน้า [13][30]
- thesis ที่ builder พูดซ้ำ: ทักษะสำคัญตอนนี้คือ agent setup/management + การรัน local model บวกกับ distribution [1]; steipete มอง infra ว่า 'ทุกอย่างคือ fast หรือ slow API' [4] และเริ่มตั้งคำถามว่าต้องการ 'model picker' แล้ว [25]
- items ส่วนใหญ่เป็น lifestyle/personal noise (โรงแรม, อาหาร, หุ่นยนต์ท่องเที่ยว) [2][7][37][22]; signal ด้าน dev/AI จริงๆ มีปานกลาง กระจุกอยู่ใน ~8 จาก 60 items

## What happened
จาก 15 account ที่ติดตามในสัปดาห์นี้ thread ที่มีเนื้อหาจริงจังจับกลุ่มอยู่สามพื้นที่ แรก — model selection: EXM7777 บอกว่า Opus 4.8 ใน Claude Code รู้สึก 'นำหน้าหลายเดือน' ด้าน business/marketing/writing ส่วน GPT-5.5 ใน Codex คือ specialist ด้าน coding [9] และแชร์ setup แบบ 'council of models' ที่เล็งใกล้ Fable 5 benchmark [8]; ผู้เขียนคนเดียวกันกลับมาปัด GLM-5.2 ว่าเป็นแค่ hype จาก benchmark card ที่ล้มเหลว 'ใน real agent loop' [47] ขณะที่ rileybrown demo general-purpose agent iOS app ที่สร้างบน GPT-5.5 โดยให้ GLM-5.2 เป็นตัวขับเคลื่อน agent [11] steipete เพิ่ม framing ด้าน infra ว่า 'ทุกอย่างคือ fast หรือ slow API' [4] และ 'ตอนนี้เกือบต้องการ model picker แล้ว' [25] สอง — design automation: AmirMushich รัน multi-post thread เรื่องการสร้าง marketing carousel และ Instagram/brand template ซ้ำได้ด้วย design agent (trymoda/Moda, Claude MCP) [10][41][48][54][55][57] พร้อมอ้าง Slack-native creative tool ที่ทำ $20M ARR [42]; MengTo แสดง landing-page creation ผ่าน 'giant prompt' ที่ copy ได้จากคลัง template 5,009 หน้า — ตัวอย่างหนึ่ง recreate ไซต์ 'VR Game Agency' โดยตรง [13][30] สาม — builder-skills meta-thesis จาก gregisenberg: ผู้เชี่ยวชาญด้าน agent, distribution marketer, และ robotics engineer คือ skill set ที่มีค่าที่สุด [1] ที่เหลือเป็น lifestyle, ท่องเที่ยว, และ content แนวสร้างแรงบันดาลใจ [2][5][7][12][37]

## Why it matters (reasoning)
signal ที่ควรดึงออกมาคือ practitioners ที่ NDF ติดตามหยุดมองว่า 'model' คือสิ่งเดียวแล้ว — ตอนนี้ route ตาม task: Opus สำหรับ prose/strategy, model ที่ tuned สำหรับ code ด้าน code [9][25] ซึ่งตรงกับ multi-provider/router architecture มากกว่าการ bet กับ vendor เดียว และบรรทัด 'fast or slow API' [4] สะท้อนว่า agent system ถูกประกอบจาก inference endpoint ที่เปลี่ยนแทนกันได้ ความขัดแย้งเรื่อง GLM-5.2 [11][47] เป็นคำเตือนที่มีประโยชน์: benchmark claim จากวงเดียวกันนี้แตกต่างจากผลลัพธ์จริงใน agent loop อย่างชัดเจน ดังนั้นการนำ model ใดมาใช้ควร validate บน workflow จริง ไม่ใช่ leaderboard อีกชั้นหนึ่ง thread ด้าน design agent [10][48][54][42] ชี้ให้เห็นว่า marketing/asset production (carousel, landing page, template ที่สอดคล้อง brand) คือจุดที่ apply agent ได้ถูกที่สุดตอนนี้ — ไม่ต้องใช้ engineering, ผลิต output ที่ ship ได้จริง และตัวอย่าง $20M ARR ใน Slack [42] แสดง pattern ที่ชนะคือส่ง result ภายใน tool ที่ team ใช้อยู่แล้ว ไม่ใช่ interface ใหม่ thesis เรื่อง skills [1] ยืนยันว่า leverage อยู่ที่ orchestration และ distribution ไม่ใช่ model access

## Possibility
น่าจะเกิด: task-based model routing กลายเป็น standard practice ใน cohort นี้ พร้อม tooling แบบ 'model picker' ชัดเจน [25][9] — framing กำลังรวมศูนย์แล้ว เป็นไปได้: GLM-5.2 และ model ต้นทุนต่ำคล้ายกันถูกใช้เป็น 'agent engine' ราคาถูกใต้ orchestrator model ที่แข็งแกร่งกว่า [11] แต่การนำมาใช้ยังขัดแย้งอยู่จนกว่าผล real-loop จะชัดเจน [47] เป็นไปได้: design agent ขยายจากการสร้าง social asset ไปสู่ landing page และ brand page เต็มรูปแบบเมื่อคลัง template โตขึ้น [13][30][54] โดยมีตัวอย่างหนึ่งที่เล็ง VR game-agency site อยู่แล้ว [30] ไม่น่าเกิด (จากข้อมูลนี้): model ใด model หนึ่งถูกมองว่าดีที่สุดสำหรับทุกอย่าง — commentary สัปดาห์นี้ argue ตรงข้ามโดยตรง [9][25] ไม่มีแหล่งข้อมูลใดให้ตัวเลข probability จึงไม่ระบุที่นี่

## Org applicability — NDF DEV
1) ทดลอง design agent สำหรับ marketing asset ของ game/app — carousel และ social template ผ่าน trymoda/Moda หรือ Claude MCP พร้อม NapLab brand kit (effort ต่ำ) [10][48][54][55] ตรงกับ marketing output ของ NDF โดยตรง 2) ทดสอบ 'giant prompt' landing-page generation สำหรับหน้า game หรือ XR product โดยปรับ template prompt ใน ChatGPT (effort ต่ำ) [13][30] — ตัวอย่างที่เผยแพร่ไปคือไซต์ VR agency [30] 3) นำ task-based model routing มาใช้ใน AI work ภายใน: model แข็งกว่าสำหรับ copy/strategy/decision, model ที่ tuned สำหรับ code ด้าน code (effort ต่ำ/กลาง) [9][25] — แต่ validate บน agent loop ของตัวเองก่อน เพราะ benchmark-vs-reality ของ GLM-5.2 แตกต่างกัน [11][47] 4) ให้ agent orchestration + distribution เป็น skills priority ของทีม [1] ข้าม: GLM-5.2 สำหรับ production agent loop จนกว่าจะรันทดสอบเอง [47]; setup แบบ 'council of models' [8] เป็น optional และยังไม่ได้รับการพิสูจน์บน stack ของเรา; ข้าม thread ด้าน lifestyle, motivation, และ X-revenue [2][5][12][23][37] — ไม่มี content ที่นำไปทำได้จริง

## Signals to Watch
- ว่า claim 'GLM-5.2 benchmark ดีแต่ agent loop อ่อน' [47] ยืนหยัดได้ไหมเมื่อ builder อื่นรันใต้ orchestrator มากขึ้น [11]
- การ hire และ framing 'fast/slow API' + 'model picker' ของ steipete [3][4][25] — สัญญาณต้นของ router/agent-infra tooling ที่กำลัง mature ในวงนี้
- Design agent ที่ทำ $20M ARR โดยอยู่ใน Slack [42] — pattern การ distribute (ส่ง result ใน tool เดิม) แทน interface ใหม่
- AI video/image quality ที่กระโดดของ egeberkina [45][46] — เกี่ยวข้องกับ game cinematics และ XR asset pipeline ถ้า trend นี้ต่อเนื่อง

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | gregisenberg | ^1054 c121 | [The most valuable skill sets on the planet right now: 1. people who can set up a](https://x.com/gregisenberg/status/2068325550603559402) |
| x | levelsio | ^817 c103 | [Why American hotels keep bringing me ice and water non-stop? What do people do i](https://x.com/levelsio/status/2068168031151485370) |
| x | steipete | ^599 c23 | [Hannes speaks both developer and agents. Blessed to have him on the team!](https://x.com/steipete/status/2068199277277401419) |
| x | steipete | ^462 c18 | [Everything's either a fast or slow API now.](https://x.com/steipete/status/2067821739556413651) |
| x | marclou | ^422 c54 | [Discipline puts you ahead of 99% of people.](https://x.com/marclou/status/2068161229760381189) |
| x | egeberkina | ^297 c2 | [Could stay here forever https://t.co/9Z2h8KXmiq](https://x.com/egeberkina/status/2068075701626978643) |
| x | marclou | ^279 c56 | [Korea airport has little robots 🤖 that show you the way to your flight departure](https://x.com/marclou/status/2068197519503557105) |
| x | EXM7777 | ^242 c10 | [here's the exact setup to build a council of models (get close to Fable 5 benchm](https://x.com/EXM7777/status/2067969663624208506) |
| x | EXM7777 | ^232 c51 | [Opus 4.8 inside Claude Code feels months ahead of everything else on the busines](https://x.com/EXM7777/status/2067684271431840210) |
| x | AmirMushich | ^227 c17 | [5 min to design pro carousels (with 0 skill) No Figma, or Photoshop Just one des](https://x.com/AmirMushich/status/2068057733505651037) |
| x | rileybrown | ^216 c32 | [One shot a general purpose agent iOS app with GPT 5.5… the general agent is powe](https://x.com/rileybrown/status/2068200276285161700) |
| x | jackfriks | ^203 c35 | [life is incredibly unfair and when you win it becomes much easier to keep winnin](https://x.com/jackfriks/status/2068341261749170653) |
| x | MengTo | ^153 c11 | [I get asked a lot for giant prompts to create insanely detailed landing pages. H](https://x.com/MengTo/status/2068272410646999059) |
| x | egeberkina | ^147 c2 | [Island mode https://t.co/nAX1eEdk55](https://x.com/egeberkina/status/2067730177317032112) |
| x | eptwts | ^147 c19 | [once you become very good at what you do, you can teach others how to do it & ta](https://x.com/eptwts/status/2068279446713348479) |
| x | levelsio | ^123 c4 | [I am not complaing btw, I like abundance](https://x.com/levelsio/status/2068193707464225031) |
| x | levelsio | ^97 c16 | [🤓 Another interesting milestone I was able to connect the modern WebGL Quake 1 m](https://x.com/levelsio/status/2068174430120079365) |
| x | jackfriks | ^89 c24 | [my monthly business goals: - MRR go up 📈 - customer support go down 📉 repeat for](https://x.com/jackfriks/status/2068339953071747411) |
| x | levelsio | ^87 c7 | [@e_c_t_o hey man, can you follow me for DM so I can pay you the prize? :D](https://x.com/levelsio/status/2068171841139786034) |
| x | eptwts | ^86 c24 | [i'm looking for a cracked dev to work on a project w/ me... must have a very goo](https://x.com/eptwts/status/2068305718327873918) |
| x | levelsio | ^75 c4 | [@yannschaub Bullshit Anyone should be able to have a platform, that's free speec](https://x.com/levelsio/status/2068079912703909953) |
| x | levelsio | ^63 c11 | [@Andercot Helicopters are a terrible idea](https://x.com/levelsio/status/2068094084258947143) |
| x | eptwts | ^62 c12 | [i don't see why people even care about X revenue sharing... if you're getting en](https://x.com/eptwts/status/2068335317493453310) |
| x | levelsio | ^60 c3 | [@jackfriks Ironically those are LESS complex than the overengineering of the ser](https://x.com/levelsio/status/2068092252979663225) |
| x | steipete | ^54 c1 | [@beyang @nicolaygerold it's almost like you need a model picker](https://x.com/steipete/status/2068133642426003475) |
| x | marclou | ^50 c10 | [✅ Startup Acquisition #104 on @trust_mrr ✅ AI startup sold for $2,000. It create](https://x.com/marclou/status/2068314177702424585) |
| x | marclou | ^45 c14 | [I built a tiny wardrobe for the @DataFast_ globe. You can now switch map styles:](https://x.com/marclou/status/2068352981041627436) |
| x | jackfriks | ^36 c13 | [there is something about making things where the more you make things the better](https://x.com/jackfriks/status/2068341029187531212) |
| x | EXM7777 | ^34 c1 | [https://t.co/YYx2w1E5An](https://x.com/EXM7777/status/2068032062351983032) |
| x | MengTo | ^32 c3 | [You can copy giant prompts from all 5,009 landing pages on https://t.co/Kpiogf2z](https://x.com/MengTo/status/2068272414551838787) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1054 · 💬 121</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2068325550603559402">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The most valuable skill sets on the planet right now: 1. people who can set up agents properly, manage them, and run local AI models 2. marketers who know how to build distribution 3. robotics enginee”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Greg Isenberg ระบุ 6 skill set ที่มีค่าที่สุดตอนนี้: คนที่ตั้งและจัดการ agent ได้, builder-distributor, วิศวกร robotics, นักการตลาดที่ใช้ AI เป็น, curator คลิปสั้น, และคนสร้าง community จริงๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>archetype builder-distributor คือแรงกดดันที่ studio เล็กรู้สึกอยู่แล้ว เพราะทีมน้อยแต่ต้องทั้ง ship และ market</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตรวจทีมว่ามีใครครอบ agent ops และ distribution บ้าง แล้วเติมช่องว่างด้วยการจ้างหรือ upskill</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2068325550603559402" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 817 · 💬 103</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2068168031151485370">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Why American hotels keep bringing me ice and water non-stop? What do people do in hotel rooms here?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Pieter Levels โพสต์ความสงสัยส่วนตัวเรื่องโรงแรมอเมริกันที่คอยเอาน้ำแข็งและน้ำมาให้ — ไม่มีเนื้อหาเชิงเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2068168031151485370" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 599 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2068199277277401419">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hannes speaks both developer and agents. Blessed to have him on the team!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ชมสมาชิกทีมชื่อ Hannes ว่าเข้าใจทั้งมุมมอง developer และ agent</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2068199277277401419" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 462 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2067821739556413651">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Everything’s either a fast or slow API now.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete สังเกตว่า API สมัยใหม่ โดยเฉพาะ AI API แบ่งออกเป็นสองแบบชัดเจน: fast (sync/streaming) กับ slow (async job queue) ไม่มีตรงกลาง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เลือก pattern ผิดตั้งแต่ออกแบบ = refactor เจ็บปวด — UI streaming ต่อกับ slow job endpoint (หรือกลับกัน) พัง UX และบังคับ retry logic ที่ไม่ได้วางแผนไว้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อน build AI feature ทุกตัว ประกาศ pattern ก่อนเลย — streaming สำหรับ output real-time, async job สำหรับ generation หนัก — ก่อนแตะ UI หรือ backend</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2067821739556413651" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 422 · 💬 54</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2068161229760381189">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Discipline puts you ahead of 99% of people.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Marc Lou โพสต์ quote แรงจูงใจทั่วไปเรื่อง discipline ไม่มี technical content, tool, หรือ announcement ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2068161229760381189" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@egeberkina</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 297 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/egeberkina/status/2068075701626978643">View @egeberkina on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Could stay here forever https://t.co/9Z2h8KXmiq”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Post ของ @egeberkina เป็นแค่ความรู้สึกส่วนตัว ('Could stay here forever') พร้อม link ที่ไม่มีเนื้อหาอธิบาย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/egeberkina/status/2068075701626978643" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 279 · 💬 56</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2068197519503557105">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Korea airport has little robots 🤖 that show you the way to your flight departure gate https://t.co/dI9lt4H386”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>มีคนแชร์คลิปหุ่นยนต์นำทางขนาดเล็กในสนามบินเกาหลี ทำหน้าที่พาผู้โดยสารไปยังประตูขึ้นเครื่อง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2068197519503557105" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 242 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2067969663624208506">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“here's the exact setup to build a council of models (get close to Fable 5 benchmarks): https://t.co/vEXGhIpWPg”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ X engagement ต่ำ อ้างว่ามี setup สำหรับทำ council of models ให้ใกล้เคียง Fable 5 benchmarks โดยแปะ link ออกไปโดยไม่มีรายละเอียดในโพสต์เลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EXM7777/status/2067969663624208506" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
