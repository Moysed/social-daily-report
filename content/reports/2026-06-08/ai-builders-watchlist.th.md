---
type: social-topic-report
date: '2026-06-08'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-06-08T15:57:01+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.55
sentiment: mixed
confidence: 0.6
tags:
- ai-agents
- agent-orchestration
- indie-saas
- codex
- prompt-engineering
- devtools
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060985731988762627/img/Y8aOAYczKKJtuaHz.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-06-08

## TL;DR
- thesis ของ steipete — "หยุด prompt coding agents; ออกแบบ loop ที่ prompt agents แทน" — ดึง engagement 16,159 ครั้ง [1] และต่อยอดด้วยแนวคิด "fleets" ที่ออกแบบ loop [4] และ "claw" ที่ควบคุม Codex หลาย instance [17]
- Indie SaaS milestones ครองพื้นที่: marclou บันทึก 512 วันสู่ $20K MRR [3]; jackfriks ประกาศ $50K MRR พร้อมฉลอง [8][12] และย้าย infra ไป Cloudflare R2 ประหยัดได้ ~$1,000/เดือน [16][29]
- framing ของ marclou: "Taste is the only moat" [13] คู่กับ leaderboard $/LOC (ค่ากลาง 60k LOC, $0.005/LOC, n=178, revenue ยืนยันผ่าน Stripe) [18]
- Codex tooling momentum: iOS simulator plugin ทำงานใน Codex ให้เห็น [10]; steipete ยืนยัน "it's all codex and next-gen models" [36] และตัดทิ้ง VS Code [19] กับ Claude Code [22]; rileybrown กำลัง build skill ให้ agents ควบคุม text messages [48]
- สัญญาณความสงสัยจากกลุ่มเดียวกัน: tweet ที่ Claude สร้างพร้อมข้อมูลเท็จดึง 212 bookmarks [41]; claim "local SML สู้ LLM ส่วนใหญ่ได้" แพร่กระจายโดยไม่มีการยืนยัน [40][50]; มีการแซวว่า "it's a cult" ต่อวงการ prompt influencer [58]

## What happened
Watchlist สัปดาห์นี้รวมอยู่ที่สองกลุ่ม กลุ่มแรก agent-orchestration: steipete ผลักดันแนวคิดว่า unit of work กำลังเปลี่ยนจากการ prompt agent ไปสู่การสร้าง loop ที่ขับเคลื่อน agents [1] ขยายต่อเป็น "fleets" [4], supervisor pattern ที่ "claw" ดูแล Codex instances [17], shared cross-agent memory [56], OSS experiments ชื่อ clawsweeper และ crabfleet [6][54] รวมถึง VISION.md ที่ใช้เป็น agent context ระดับ project [14] เขา bearish ต่อ VS Code [19] และ Claude Code [22] โดยเดิมพันกับ Codex และ next-gen models [36] กลุ่มที่สอง indie-SaaS economics และ personal reflection: marclou เผยแพร่ video บันทึก 512 วันสู่ $20K MRR แบบตรงไปตรงมา [3][28][49], โต้แย้ง "taste is the only moat" [13], ส่ง leaderboard $/LOC [18] และเพิ่มการเซ็นบริษัทด้วย LOI/APA ใน acquisition marketplace ชื่อ trust_mrr [42] jackfriks ทะลุ $50K MRR [8][12][24] และย้าย file storage ไป R2 [16][29]

## Why it matters (reasoning)
สัญญาณที่ชัดเจนที่สุดคือการเปลี่ยนจาก one-shot agent prompting ไปสู่ programmatic loops และ supervision [1][4][17][56] หากรูปแบบนี้ยืนได้ ทักษะวิศวกรรมที่สำคัญจะเปลี่ยนไปสู่การออกแบบ control flow, verification, และ memory รอบ agents แทนที่การปั้น prompt ทีละตัว — ซึ่งตรงกับสิ่งที่ studio เล็กที่ ship งานข้าม Unity, XR, web, และ mobile ต้องการเพื่อขยาย output โดยไม่เพิ่มคน OSS repos ของ steipete [6][54] ทำให้รูปแบบนี้ตรวจสอบได้จริง ไม่ใช่แค่วาทกรรม ด้าน indie-SaaS เป็นส่วนใหญ่เพื่อแรงบันดาลใจและ self-promotion แต่สอง claim มีสาระส่งต่อได้: "taste is the moat" [13] และข้อมูล $/LOC [18] ชี้ทิศทางเดียวกัน — เมื่อการสร้าง code ถูกลง การสร้างความต่างย้ายไปที่ judgment, design, และ distribution ไม่ใช่ volume ของ code สัญญาณตรงข้ามคือคุณภาพ noise: สมาชิกกลุ่มเดียวกันชี้เนื้อหาเท็จที่ viral [41] และ hype framing [40][50][58] เป็นเครื่องเตือนว่า engagement rank ที่นี่ไม่ใช่ตัวชี้วัดความน่าเชื่อถือ

## Possibility
Likely: tooling สำหรับ agent-loop/supervisor จะพัฒนาต่อและรวมศูนย์รอบ Codex-style harnesses ในกลุ่มนี้ภายในไตรมาสหน้า เพราะเสียงที่มีผู้ติดตามมากที่สุดกำลัง build และ open-source อยู่จริง [1][4][6][17][36] Plausible: "taste/design as moat" จะกลายเป็น positioning มาตรฐานของ solo และ small builders เมื่อ code output กลายเป็น commodity [13][18] steipete เองวาง timeline ใกล้ชิด — "3 months until" fleets ออกแบบ loop ของคุณ [4] — ซึ่งเป็นการประมาณของเขา ไม่ใช่ forecast ที่ยืนยันแล้ว Unlikely (near-term): claim เช่น local small model สู้ "most LLMs" ได้ [40] จะผ่านการตรวจสอบ เมื่อพิจารณาว่ากลุ่มเดียวกันกำลังล้อเลียนอยู่แล้ว [50] และชี้ fake viral posts [41]

## Org applicability — NDF DEV
1) ต้นแบบ agent-loop/supervisor pattern บน internal workflow หนึ่งชิ้น (เช่น asset pipeline หรือ test generation) แทน one-shot prompting — ศึกษา OSS clawsweeper/crabfleet ของ steipete ก่อน [6][54][1][17]; effort ปานกลาง 2) เพิ่ม VISION.md ทุก repo เป็น context anchor ประจำสำหรับ coding agents — ทำได้เลย cost ต่ำ [14]; effort ต่ำ 3) ทดลอง Codex iOS simulator plugin สำหรับสาย mobile/iOS [10]; effort ต่ำ 4) ทดสอบ Nano Banana 2 prompts สำหรับ logo/product mockups และ storyboard assets ที่เกี่ยวกับ marketing และ edutech content [11][27][46]; effort ต่ำ 5) หากใช้ cloud object storage อยู่ ให้ benchmark การย้ายไป R2 เพื่อตัด cost — jackfriks รายงานประหยัดได้ ~$1,000/เดือน ด้วยงานไม่กี่วัน [16][29]; effort ปานกลาง ทำเมื่อค่าใช้จ่าย storage ปัจจุบันคุ้มค่า ข้าม: MRR-milestone และ lifestyle content [3][8][12][21][45], claim "SML beats LLMs" ที่ไม่ผ่านการยืนยัน [40][50] และ framing McKinsey "replace 60% of dev teams" [30] — ถือเป็นแหล่งที่ไม่มีหลักฐาน

## Signals to Watch
- tooling loop/fleet/supervisor ของ steipete และ timeline ที่เขาระบุ ~3 เดือนสำหรับ fleet ที่ออกแบบ loop ได้ [4][17] — ติดตามว่า OSS repos [6][54] จะมี adoption จริงหรือไม่
- Codex แทนที่ VS Code/Claude Code ใน daily workflow ของกลุ่มนี้ [19][22][36][10]
- "Taste/design is the moat" + $/LOC economics ในฐานะ positioning ที่กำลังเกิดขึ้นของ solo builder [13][18]
- Reliability hygiene: เสียงกลุ่มเดียวกันที่ชี้ AI-generated fake-info posts และ hype [41][50][58] — เป็นตัวตรวจสอบก่อนรับ engagement feed นี้ที่ face value

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | steipete | ^16159 c1426 | [Here's your monthly reminder that you shouldn't be prompting coding agents anymo](https://x.com/steipete/status/2063697162748260627) |
| x | steipete | ^1972 c89 | [@matijaoe my slop is better than your slop.](https://x.com/steipete/status/2063714507558683109) |
| x | marclou | ^1298 c195 | [I documented my SaaS journey to $20K MRR. It took 512 days. I got excited, I cri](https://x.com/marclou/status/2063917952186061152) |
| x | steipete | ^997 c35 | [@gauthampai Don't worry it'll take 3 months until it's there. We'll be talking a](https://x.com/steipete/status/2063706136100933750) |
| x | jackfriks | ^515 c93 | [3 years ago i found @marclou online and saw him making $30,000/month 3 years ago](https://x.com/jackfriks/status/2063982406839775406) |
| x | steipete | ^422 c15 | [@heyandras You can look at clawsweeper and crabfleet where I explore these ideas](https://x.com/steipete/status/2063871863210852794) |
| x | steipete | ^384 c29 | [@ThiagoMot_ Don't expect me to solve all problems. 🙃](https://x.com/steipete/status/2063705239144825243) |
| x | jackfriks | ^381 c71 | [if i wake-up tomorrow to $50K MRR then i'm taking my fiancee out to taco bell (o](https://x.com/jackfriks/status/2063809444169851189) |
| x | steipete | ^319 c10 | [@weswinder welllllll](https://x.com/steipete/status/2063700503356231823) |
| x | MengTo | ^278 c14 | [Insane to see the iOS simulator in Codex. iOS dev is about to get way easier wit](https://x.com/MengTo/status/2063907419919647180) |
| x | AmirMushich | ^259 c14 | [Nano Banana / GPT-2 prompt: 3D Glass logo mockup Adidas, Nike or your logo .png ](https://x.com/AmirMushich/status/2063700272661029176) |
| x | jackfriks | ^237 c44 | [TACO BELL IS ON ME TONIGHT HONEY !!!!! 😎🤘🤘🤘 https://t.co/9lUk2s4Kg4](https://x.com/jackfriks/status/2063970388896252135) |
| x | marclou | ^235 c83 | [Taste is the only moat.](https://x.com/marclou/status/2063964510206210051) |
| x | steipete | ^222 c21 | [@mosyaseen I use a VISION.md for my projects](https://x.com/steipete/status/2063715936402813175) |
| x | steipete | ^221 c18 | [@ilias_yahia You need better friends!](https://x.com/steipete/status/2063732154811470027) |
| x | jackfriks | ^195 c43 | [many people may think that spending 1-2 days to migrate infrastructure that save](https://x.com/jackfriks/status/2063786952755753471) |
| x | steipete | ^166 c20 | [@InderosD I have my claw supervising my codex'es.](https://x.com/steipete/status/2063697398958813322) |
| x | marclou | ^142 c33 | [Introducing the leaderboard of $$$ per Lines Of Code: https://t.co/nNbgPZCRNR 🧑‍](https://x.com/marclou/status/2063856500704194717) |
| x | steipete | ^138 c20 | [@LexanderBrouwer Who still uses VS Code?](https://x.com/steipete/status/2063700405247242731) |
| x | steipete | ^124 c2 | [@felipebbonatto rude 🤣](https://x.com/steipete/status/2063726930998993219) |
| x | jackfriks | ^124 c33 | [i would have ordered a tesla model Y instead of my toyota corolla hybrid but at ](https://x.com/jackfriks/status/2063774235252695397) |
| x | steipete | ^120 c26 | [@wicus_g Who still uses Claude Code?](https://x.com/steipete/status/2063706730580652541) |
| x | steipete | ^104 c8 | [@MyMoonEnt Correct. Is your time really not worth more?](https://x.com/steipete/status/2063701336084955565) |
| x | jackfriks | ^102 c29 | [one of the things i am most proud of about myself... though i can't be sure if i](https://x.com/jackfriks/status/2063986417106063765) |
| x | jackfriks | ^100 c16 | [this guy deserves $100k MRR for this video alone](https://x.com/jackfriks/status/2063968937780326875) |
| x | vasuman | ^81 c12 | [A thank you to Varick's clients. When we started, our earliest clients would tel](https://x.com/vasuman/status/2063782601350119695) |
| x | AmirMushich | ^74 c16 | [In 2018, my creative agency was producing a lot of ad storyboards Brands like Ad](https://x.com/AmirMushich/status/2063901308722061546) |
| x | marclou | ^51 c13 | [I regret a lot of things I said in this video. I was emotional, arrogant, and sp](https://x.com/marclou/status/2063923672050549214) |
| x | jackfriks | ^51 c10 | [files writing to r2 now, i can feel the dollars being saved as i type this basic](https://x.com/jackfriks/status/2063785597580267947) |
| x | godofprompt | ^48 c10 | [Remember when people were posting "this one prompt replaces a McKinsey consultan](https://x.com/godofprompt/status/2063957974016778713) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 16159 · 💬 1426</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2063697162748260627">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here’s your monthly reminder that you shouldn’t be prompting coding agents anymore. You should be designing loops that prompt your agents.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete บอกว่าหยุด prompt coding agent ทีละครั้งได้แล้ว ให้ออกแบบ loop ที่ drive agent แทน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมเล็กที่ใช้ AI coding tools อยู่แล้ว การเปลี่ยนจาก ad-hoc prompt ไปเป็น agent loop คือ output ต่อคนที่เพิ่มขึ้นโดยไม่ต้องจ้างเพิ่ม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">สร้าง workflow script (เช่น Claude Code Workflows หรือ agent pipeline) ที่ chain งานอัตโนมัติแทนการ trigger ทีละขั้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2063697162748260627" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1972 · 💬 89</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2063714507558683109">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@matijaoe my slop is better than your slop.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>สอง developer แซวกันเรื่อง AI-generated output ของใครห่วยกว่า — ไม่มีเนื้อหาเชิงเทคนิค ไม่มี announcement</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2063714507558683109" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1298 · 💬 195</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2063917952186061152">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I documented my SaaS journey to $20K MRR. It took 512 days. I got excited, I cried, I laughed, I lost hope. I got literally every moment on camera. This video is the raw story of what building a start”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Marc Lou ปล่อยวิดีโอสไตล์สารคดีบันทึก 512 วัน สร้าง SaaS จากศูนย์จนถึง $20K MRR</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2063917952186061152" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 997 · 💬 35</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2063706136100933750">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@gauthampai Don’t worry it’ll take 3 months until it’s there. We’ll be talking about fleets that design your loops then.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ตอบ @gauthampai แบบคาดเดาว่าอีก 3 เดือน 'fleets' จะ design 'loops' ให้ — ไม่มี tool, release, หรือรายละเอียดอะไรเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2063706136100933750" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jackfriks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 515 · 💬 93</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jackfriks/status/2063982406839775406">View @jackfriks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“3 years ago i found @marclou online and saw him making $30,000/month 3 years ago people laughed when i mentioned that amount of money per month i didn't believe it would be possible either, not yet. i”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie developer @jackfriks แชร์ journey ส่วนตัวที่ไปถึง $50,000 MRR กับ SaaS ของตัวเอง Postbridge โดยอ้างถึงความพากเพียรหลายปีและแรงบันดาลใจจาก @marclou</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jackfriks/status/2063982406839775406" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 422 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2063871863210852794">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@heyandras You can look at clawsweeper and crabfleet where I explore these ideas, it’s all oss.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>steipete แนะนำ OSS สองตัว — clawsweeper และ crabfleet — เป็น reference implementation ของ concept ที่กำลังคุยกันเรื่อง AI agent tooling</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทั้งสอง repo เปิด source จาก builder ที่ active ใน AI tooling space — น่าจะมี pattern สำหรับ Claude/agent orchestration ที่ดูได้ตรงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เปิด repo clawsweeper และ crabfleet บน GitHub แล้วดู README กับ core files หา agent pattern ที่เอามาใช้ใน AI tooling ของ studio ได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2063871863210852794" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 384 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2063705239144825243">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@ThiagoMot_ Don’t expect me to solve all problems. 🙃”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ตอบ @ThiagoMot_ แบบสั้นๆ ว่าไม่ได้คาดหวังจะแก้ปัญหาทุกอย่าง — ไม่มีเนื้อหาเชิงเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2063705239144825243" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jackfriks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 381 · 💬 71</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jackfriks/status/2063809444169851189">View @jackfriks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“if i wake-up tomorrow to $50K MRR then i’m taking my fiancee out to taco bell (on me) https://t.co/aXUhWHDr7P”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Founder โพสต์ล้อเล่นว่าถ้า MRR ถึง $50K จะพาแฟนไปกิน Taco Bell ไม่มีข้อมูล product หรือ technical ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jackfriks/status/2063809444169851189" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
