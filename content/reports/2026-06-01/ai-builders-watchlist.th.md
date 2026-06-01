---
type: social-topic-report
date: '2026-06-01'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-06-01T04:32:18+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.45
sentiment: positive
confidence: 0.55
tags:
- agentic-dev
- ai-qa
- prompt-engineering
- ai-video
- realtime-voice
- indie-builders
thumbnail: https://pbs.twimg.com/media/HJpy1sAa8AABRYW.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-06-01

## TL;DR
- steipete กำลัง ship agent framework ชื่อ OpenClaw — modular/lean, 'only add what you need,' พร้อม OpenRouter integration ใน onboarding [7][17] และกำลังย้ายไป SF ช่วง MS Build [1].
- แนวทาง agentic-dev workflow ในทางปฏิบัติ: steipete ให้ Codex ทำหน้าที่ QA อัตโนมัติ — เขียน user-test scenario ต่อ commit แล้วขับ browser/computer-use tools (crabbox/peekaboo/mcporter) ทดสอบในฐานะผู้ใช้จริง [4], พร้อม TypeScript codemod แบบ ad-hoc [11]; 'autoreview keeps GPT honest' [15].
- godofprompt ระบุว่า temperature tuning กำลังถูกถอดออกจาก reasoning models — OpenAI ถอดออกจาก o1/o3/GPT-5 และ Google เตือนไม่ให้แก้บน Gemini 3 [38].
- AI video ข้าม usability threshold สำหรับ creator กลุ่มนี้: 0xROAS clone วิดีโอได้ใน ~15 นาทีด้วย 'V3 AI UGC' [32][36], Grok Imagine Video 1.5 [21] และการเปรียบ Gemini Omni Flash กับ Seedance 2.0 [27][40].
- gregisenberg มอง GPT Realtime 2.0 ว่าเปิดทาง real-time, on-call voice agents (เช่น live contract negotiation) [3]; vasuman เสนอ model consulting แบบ forward-deployed custom-agent [9].

## What happened
feed builder สัปดาห์นี้โฟกัสที่ agentic development tooling steipete กำลัง build OpenClaw แบบ public — agent framework ที่ pitch ตัวเองว่า modular และ lean — 'fewer skills, fewer tools = your agent can work more efficiently' [7] — พร้อม OpenRouter onboarding integration ที่เสนอไว้ [17] เขาอธิบายการใช้ Codex เป็น QA agent ที่ generate user-test scenario ต่อ commit แล้ว exercise app ผ่าน web/VNC และ browser/computer-use tooling [4], เขียน codemod แบบ ad-hoc สำหรับ TypeScript migration [11] และพึ่ง 'autoreview' เพื่อควบคุม model output [15] เรื่องส่วนตัว (ย้ายไป SF, MS Build) เป็น context ไม่ใช่ signal [1].

## Why it matters (reasoning)
ด้าน prompting practice — godofprompt รายงานว่า provider กำลังถอด temperature knob ออกจาก reasoning models (o1/o3/GPT-5) และไม่แนะนำให้ใช้บน Gemini 3 [38]; ถ้าถูกต้อง วิธีที่ทีม tune model behavior จะต้องเปลี่ยน gregisenberg และ vasuman ชี้ที่ productized agents: voice agents แบบ real-time ที่นั่งฟัง live call [3] และ custom agent build แบบ forward-deployed [9] ด้าน media — creator หลายคนรายงานว่า AI video cloning เร็วพอสำหรับ production UGC แล้ว [21][32][36][27] สิ่งที่ทะลุผ่านคือ operational ไม่ใช่ theoretical: คนเหล่านี้รัน agent ใน build/test/QA loop จริง [4][11][13] ไม่ใช่แค่ demo.

## Possibility
Likely: agent-driven QA/codemod workflow (commit-triggered test generation + browser/computer-use execution) จะ mature ต่อเนื่องและกลายเป็นส่วนปกติของ dev pipeline เพราะ steipete รันอยู่ทุกวันแล้ว [4][11]. Plausible: การเปลี่ยน 'temperature is dead' บังคับให้แก้ prompt/config ถ้า depend บน temperature เพื่อ determinism หรือ creativity — verify กับ official docs ก่อนลงมือ เพราะนี่เป็น framing ของ practitioner คนเดียว [38]. Plausible: real-time voice agents ก้าวจาก concept ไปสู่ product ที่ ship จริงเมื่อ GPT Realtime 2.0 mature [3]. Unlikely (ระยะใกล้): OpenClaw จะกลายเป็น standard ที่ต้อง adopt — มันคือ framework ต้นแบบของคนคนเดียว ยัง opinionated อยู่มาก [7]; ใช้เป็น pattern source ไม่ใช่ dependency.

## Org applicability — NDF DEV
1) Pilot agent-as-QA loop สำหรับ web/mobile: ให้ Codex/Claude generate per-commit test scenario แล้วขับ browser-use tool ชน staging — ใช้ได้ตรงกับ web & mobile apps ของ NDF DEV (effort med) [4][15]. 2) Audit prompt/config code ที่ hardcode temperature บน reasoning models และยืนยัน provider behavior ก่อน rely (effort low) [38]. 3) ทดสอบ GPT Realtime 2.0 กับ use case e-learning/edutech ด้านเสียง (เช่น ฝึกพูดภาษาหรือ tutoring) เป็น spike แบบ scoped (effort med) [3]. 4) ทดลอง AI-video tool หนึ่งตัว (Omni Flash / Grok 1.5 / UGC cloner) สำหรับ marketing/short-form content แล้วเทียบกับการตัดต่อมือ (effort low) [27][32]; สังเกตว่า rileybrown เดินสวนทางด้วยการจ้าง human editor ที่เข้าใจ AI tools [23][42] — quality ยังต้องมีคนดูแล. 5) ลอง prompt-to-editable-design agent สำหรับ UI mockup เร็ว (effort low) [20][52]. Skip: logistics SF/MS Build [1], โพสต์ creatine และ lifestyle [5][58] และการอวด MRR/revenue [22][33] — ไม่มี content ที่ actionable.

## Signals to Watch
- ทิศทาง OpenClaw และ OpenRouter onboarding integration — template สำหรับ lean, self-hosted agent setup [7][17].
- Codex ทำ real codemod และ computer-use QA จริง รวมถึง self-recovery ('call crabbox doctor if a screenshot fails') [4][11][59].
- Provider ถอด temperature controls บน reasoning models — ยืนยันกับ OpenAI/Google docs [38].
- ความเร็ว AI-video UGC cloning (~15 นาที) กับ counter-move การจ้าง human editor [32][23].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | steipete | ^2108 c117 | [Finally got my visa sorted out and moving to San Francisco, just in time for MS ](https://x.com/steipete/status/2061031509088231640) |
| x | EXM7777 | ^1465 c25 | [this is the Hermes setup top 1% operators are using to get rid of AI slop... htt](https://x.com/EXM7777/status/2061086049326256356) |
| x | gregisenberg | ^847 c58 | [GPT Realtime 2.0 is pretty incredible 17 startup ideas that ONLY work because of](https://x.com/gregisenberg/status/2061129813750915508) |
| x | steipete | ^784 c34 | [Been teaching codex to be my QA assistant. For every commit it creates a user-te](https://x.com/steipete/status/2061208638027395490) |
| x | levelsio | ^571 c53 | [Take your creatine!!! https://t.co/TyTIqEUFUq](https://x.com/levelsio/status/2061176892691017909) |
| x | gregisenberg | ^442 c60 | [I can't believe how fun building a company is right now is. The weird part is it](https://x.com/gregisenberg/status/2061241159213576367) |
| x | steipete | ^414 c47 | [The idea of OpenClaw is always that it should be yours. It's modular and lean, o](https://x.com/steipete/status/2061072753998856696) |
| x | marclou | ^367 c59 | [These have been the best 10 years of my life. Entrepreneurship has taught me so ](https://x.com/marclou/status/2061104163745075339) |
| x | vasuman | ^346 c46 | [Imagine an AI company that forward deploys into your enterprise to first underst](https://x.com/vasuman/status/2060847258283999376) |
| x | vasuman | ^338 c49 | [If you're a software engineer that is down for a paid work trial (1-2 weeks, con](https://x.com/vasuman/status/2060866035067343240) |
| x | steipete | ^277 c32 | [Haven't seen codex writing ad-hoc codemods before, but it just did for a bigger ](https://x.com/steipete/status/2061115471760441692) |
| x | levelsio | ^267 c27 | [Please report this guy thx @nikitabier](https://x.com/levelsio/status/2061162603586445505) |
| x | vasuman | ^224 c53 | [/goal has been running for 16 hours and we're in that sweet spot where I don't w](https://x.com/vasuman/status/2061203646449369497) |
| x | steipete | ^152 c3 | [@theo Yes! See ya around this week?](https://x.com/steipete/status/2061038721290400240) |
| x | steipete | ^151 c6 | [@theo @VictorTaelin gotta use autoreview, that keeps gpt honest and usually help](https://x.com/steipete/status/2061036923397845456) |
| x | egeberkina | ^141 c4 | [CEOs are the new app icons https://t.co/W3jjrU027b](https://x.com/egeberkina/status/2061137275426165022) |
| x | steipete | ^133 c7 | [@shashankgoyal95 @OpenRouter Integration with OpenClaw onboarding for a better s](https://x.com/steipete/status/2061182935957401658) |
| x | egeberkina | ^104 c0 | [@tervisscoot Average concert in Turkey https://t.co/tExymyP6Ab](https://x.com/egeberkina/status/2060830061381431780) |
| x | vasuman | ^104 c1 | [Incredible https://t.co/QqVOtcj5iN](https://x.com/vasuman/status/2061261104962244981) |
| x | AmirMushich | ^102 c5 | [now you can create editable designs with 1 prompt save the tool 👇 https://t.co/f](https://x.com/AmirMushich/status/2061121201146060838) |
| x | 0xROAS | ^101 c8 | [here's how Grok Imagine Video 1.5 looks like: https://t.co/7aB3qNCv91](https://x.com/0xROAS/status/2061139518795735271) |
| x | jackfriks | ^98 c15 | [it's been almost a year since i learned what a database index is also almost a y](https://x.com/jackfriks/status/2061275203607372178) |
| x | rileybrown | ^87 c13 | [I'm going in the opposite direction. I'm hiring HUMAN video editors in New York ](https://x.com/rileybrown/status/2061215449858072994) |
| x | gregisenberg | ^72 c12 | [@RaminNasibov CS 1.6](https://x.com/gregisenberg/status/2061148444765372745) |
| x | gregisenberg | ^69 c3 | [@OrevaZSN honestly, not a bad idea adding it to https://t.co/ptcEtGCCsV](https://x.com/gregisenberg/status/2061227827299561934) |
| x | godofprompt | ^68 c10 | [I pulled a full week of @OpenAI's X analytics without an API key, a scraper, or ](https://x.com/godofprompt/status/2060808562314772519) |
| x | egeberkina | ^67 c3 | [Tonight Turkey at Ye's concert 🇹🇷 Made with Omni Flash https://t.co/iHEwBZ5zlP](https://x.com/egeberkina/status/2060828495521976754) |
| x | steipete | ^65 c8 | [@_lopopolo *need*](https://x.com/steipete/status/2061036484975559132) |
| x | steipete | ^64 c2 | [@dasPoppers @openclaw Did we had the same idea yesterday? Didn't see your propos](https://x.com/steipete/status/2060974727213027435) |
| x | AmirMushich | ^44 c6 | [Ferrari Luce brand vision* *2026 trends https://t.co/iU5A8LYCnC](https://x.com/AmirMushich/status/2061175478061285576) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2108 · 💬 117</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061031509088231640">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Finally got my visa sorted out and moving to San Francisco, just in time for MS Build and OpenClaw’s after hours! https://t.co/agbyZ79kb1”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ประกาศย้ายไปอยู่ San Francisco ตรงกับช่วง MS Build และงาน after-hours ชื่อ OpenClaw</dd>
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
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1465 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2061086049326256356">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“this is the Hermes setup top 1% operators are using to get rid of AI slop... https://t.co/gbRRSx3sbM”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Tweet โปรโมต 'Hermes setup' อ้างว่าช่วยลด AI slop แต่ไม่มีข้อมูลในโพสต์ มีแค่ลิงก์ภายนอก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EXM7777/status/2061086049326256356" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 847 · 💬 58</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2061129813750915508">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“GPT Realtime 2.0 is pretty incredible 17 startup ideas that ONLY work because of what this model makes possible: 1. Real-time contract negotiation agent. Sits on a call between two parties, checks pri”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Greg Isenberg แจก 17 concept startup ที่ต้องใช้ GPT Realtime 2.0 โดยเฉพาะ — run parallel tool calls ดึงข้อมูลหลายแหล่งพร้อมกันขณะ voice conversation ยังดำเนินอยู่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การ run parallel tools ระหว่างพูดคือ primitive ใหม่ — voice agent query ข้อมูล 5 แหล่งพร้อมกันโดยไม่ต้องหยุดรอ เปิด category always-on voice agent ที่ streaming TTS เดิมทำไม่ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">งาน e-learning ของ studio เหมาะทดสอบตรงๆ — ลอง prototype voice tutor ด้วย GPT Realtime 2.0 ให้ดึง learner progress กับ quiz content แบบ parallel ระหว่าง session จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2061129813750915508" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 784 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061208638027395490">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Been teaching codex to be my QA assistant. For every commit it creates a user-test scenario and uses webVNC (crabbox), computer/browser use (peekaboo/mcporter) to test OpenClaw like a user/QA person w”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ฝึก Codex ให้สร้าง user-test scenario ต่อ commit แล้วรัน via webVNC และ browser computer-use กับ app ของตัวเอง จากนั้น open fix PR อัตโนมัติโดยไม่ต้องมีคนดู</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>รวม per-commit test generation กับ computer-use execution เป็น QA loop อัตโนมัติ ทีมเล็กได้ regression testing ต่อเนื่องโดยไม่ต้องมี QA เฉพาะ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ต่อ Codex หรือ Claude agent เข้า CI pipeline ของ studio ให้สร้างและรัน browser-use test scenario ต่อ commit บน web หรือ e-learning แล้ว auto-open fix PR</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061208638027395490" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 571 · 💬 53</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2061176892691017909">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Take your creatine!!! https://t.co/TyTIqEUFUq”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio โพสต์แนะนำให้กิน creatine พร้อมลิงก์ ไม่มีเนื้อหาด้านเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2061176892691017909" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 442 · 💬 60</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2061241159213576367">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I can't believe how fun building a company is right now is. The weird part is it doesn't feel like work anymore. New AI models/tools/repos keep coming out making the impossible possible. My ONLY anxie”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Greg Isenberg นักลงทุนและ startup builder เปรียบยุค AI ตอนนี้เหมือนยุค mobile app ช่วงแรก — หน้าต่างที่เปิดไม่นาน และต้องรีบใช้ให้เต็มที่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2061241159213576367" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 414 · 💬 47</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061072753998856696">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The idea of OpenClaw is always that it should be yours. It's modular and lean, only add what you need. Fewer skills, fewer tools = your agent can work more efficiently.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete อธิบาย OpenClaw ว่าเป็น agent framework แบบ modular — add เฉพาะสิ่งที่ต้องการ เพราะ tools/skills น้อยลง = agent ทำงานมีประสิทธิภาพมากขึ้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่สร้าง AI agent มักใส่ tool เกิน — แนวคิด trim-first นี้ช่วยให้ reasoning ดีขึ้นและลด token waste ได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อน deploy internal agent ให้ audit tool/skill list แล้วตัดทุกอย่างที่ไม่ได้ใช้จริงใน workflow นั้นออก</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061072753998856696" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 367 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2061104163745075339">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“These have been the best 10 years of my life. Entrepreneurship has taught me so much that it's hard to believe the person I am today is the same person who started 10 years ago. Most of those years we”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@marclou สรุป 10 ปีในฐานะผู้ประกอบการ — บอกว่าการเดินทางคือรางวัล แม้จะเต็มไปด้วยความไม่แน่นอนและอุปสรรค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2061104163745075339" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
