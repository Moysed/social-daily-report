---
type: social-topic-report
date: '2026-06-12'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-06-12T03:57:19+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- ai-coding
- claude-fable
- codex
- web-games
- indie-hackers
- agentic-workflows
thumbnail: https://pbs.twimg.com/media/HKhY9ykbAAAQzT2.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-06-12

## TL;DR
- "Claude Fable 5" ครองฟีดสัปดาห์นี้: levelsio พอร์ต Quake 1, Quake 2 และ Return to Castle Wolfenstein เป็น multiplayer บนเว็บ [8][9][36], godofprompt สร้างย่าน Kyoto แบบ walkable ด้วย Three.js ในเบราว์เซอร์ [21] และ clone layout/typography/charts จาก McKinsey PDF เป็น report ใหม่ [15], marclou ให้มันสร้าง DataEmpire บน analytics API ของตัวเอง (ผู้เยี่ยมชม 64 คนกลายเป็นชาวเมือง) [3][39]
- steipete รัน agentic maintenance loop: Codex ตื่นทุก ~5 นาที แล้วสั่งงานไปยัง threads ผ่าน orchestrator skill [2]; Codex app บน mac/win spawn threads ได้แล้ว [37] และเขาใช้ model setting สูงสุดเพราะ "ไม่ถูกจำกัดด้วย token" [59][18]
- OpenClaw hardening: media conversion ที่เคย shell out ไปหา ffmpeg กำลังย้ายไปใช้ ffmpeg-compiled-to-wasm ที่ performance ใกล้เคียงกันและลด surface risk [7][42]
- ถกเรื่อง access tier และ monetization: godofprompt นิยาม "Mythos" ว่าเปิดเฉพาะ org ที่ trusted ส่วน Fable 5 คือ public tier [50][5]; rileybrown คาดว่าผู้ใช้จะยอมรับโฆษณาเพื่อแลกกับ model ระดับสูง [19]
- ความคิดเห็นที่ engagement สูงสุด: "only boomers fix typos in prompts" (score 5,178) [1], "the moat is the original idea" [45] และ weighted-score decision prompt [25]; ข้อโต้แย้ง: "writing mac apps is still hard" [14]

## What happened
Watchlist สัปดาห์นี้รวมศูนย์อยู่ที่เหตุการณ์เดียว — การนำ Anthropic model ขีดความสามารถสูงที่เรียกว่า "Claude Fable 5" มาใช้ — พร้อมกับการผลักดัน agentic orchestration ไปพร้อมกัน builder อิสระหลายรายโพสต์ demo: game port บนเบราว์เซอร์แบบ multiplayer [8][9][36][20][55], เมือง 3D แบบ connected ด้วย Three.js [21], clone PDF เป็น branded report [15], pipeline MCP+Fable จากเอกสารหนึ่งชิ้นสู่ promo video [27] และ game บน analytics API [3][39] rileybrown ยืนยันอีกครั้งว่าตัวเอง "ไม่เคยเขียนโค้ดแม้แต่บรรทัดเดียว" [11] thread ของ steipete วนอยู่กับ Codex loop แบบ self-directing ผ่าน orchestrator skill [2], Codex app ที่ spawn threads ได้ [37] และ PR ที่ Codex ทำเสร็จให้ [4]

## Why it matters (reasoning)
กลุ่มนี้คือ early adopter ที่มักนำทิศทาง workflow ในหมู่ indie builder ดังนั้น demo ที่ซิงค์กันจากหลายรายส่งสัญญาณชัดว่าความสนใจกำลังเคลื่อนไปสู่: browser-native 3D/game generation, document/design cloning และรูปแบบ "ปล่อยให้ agent ทำงาน แล้วคอยบังคับทิศ" สำหรับการดูแล repo [2][8][21][15] การย้าย ffmpeg ไป wasm [7][42] ชี้ให้เห็นว่า client-side media processing กำลังแทน server shell-out ซึ่งลด deployment surface และ infra ต่อ request ผลทางอ้อม: การถกเรื่อง Mythos vs Fable 5 tiering [50] และการทำนายว่าจะมีโฆษณา [19] บ่งชี้ว่า capability กลายเป็น lever ที่ต้องจ่ายหรือเข้าถึงแบบ gated โดยต้นทุนเปลี่ยนจาก per-token billing ไปสู่ access tier และอาจมีโฆษณา — สิ่งนี้สำคัญสำหรับทีมที่ feature ใช้ AI หนัก สัญญาณสวนทางที่ต้องระวัง: หลักฐานเกือบทั้งหมดที่นี่คือ demo และความคิดเห็น ไม่ใช่ production report; "mac apps still hard" ของ steipete [14] และ "local models always behind cloud" ของ levelsio [54] คือข้อสงวนที่สำคัญที่สุด

## Possibility
น่าจะเกิด: output แบบ browser-based 3D/game และ rapid prototype จาก model class นี้จะต่อเนื่อง เพราะ builder อิสระหลายรายส่ง web demo ที่ใช้งานได้จริงภายในไม่กี่วัน [8][9][21][20] เป็นไปได้: agentic maintenance loop (scheduler + orchestrator + thread spawning) จะกลายเป็น pattern ทั่วไปในหมู่ indie builder [2][37][4] แม้ตอนนี้มีแค่ steipete ที่แสดงให้เห็นในเชิงลึก เป็นไปได้แต่ยังเป็นการคาดเดา: tiered/gated model access และ top tier แบบรองรับโฆษณา [50][19] — สิ่งเหล่านี้คือความเห็น ไม่ใช่นโยบายที่ประกาศแล้ว ไม่น่าเกิดในระยะใกล้: demo แบบ one-prompt จะแปลงตรงสู่ app ที่พร้อม production และ maintain ได้; ผู้เขียนคนเดียวกันระบุว่าพื้นผิวที่ยาก (native app, integration) ยังคงยากอยู่ [14][22] ไม่มี source ใดระบุ probability เป็นตัวเลข; ตัวเลขเดียวที่มีคือค่า correlation 0.44 ที่อ่อนแอของ marclou ระหว่าง revenue กับ domain rating [16]

## Org applicability — NDF DEV
1) ทดลอง Fable-class model สำหรับ browser 3D/game และ XR/web preview prototype เพื่อสร้าง demo client-facing ได้เร็ว — effort ต่ำ/กลาง [8][9][21][20] 2) ทดสอบ PDF-to-branded-report regeneration สำหรับเนื้อหา edutech/e-learning และใบเสนอราคา ต่อเข้ากับ paperwork pipeline ที่มีอยู่ — effort ต่ำ [15] 3) ประเมิน ffmpeg-compiled-to-wasm สำหรับ in-browser media conversion ใน web/mobile app เพื่อลด server load และ surface risk — effort กลาง [7][42] 4) นำร่อง agentic maintenance loop แบบ scoped (orchestrator skill + scheduled threads) บน repo ความเสี่ยงต่ำ โดยมีการควบคุมทิศทางอย่างใกล้ชิด ไม่ใช่ปล่อยให้ทำงานโดยไม่มีคนดู — effort กลาง [2][37] 5) นำ weighted-score decision prompt มาใช้ในการตัดสินใจด้าน design/architecture เพื่อให้ trade-off อธิบายได้ชัดเจน — effort ต่ำ [25] 6) พิจารณาระบบ automation สำหรับ content repurposing แบบ one-piece-in/many-out สำหรับการตลาด — effort ต่ำ [31] ข้ามได้: โพสต์เกี่ยวกับ personal finance และ lifestyle [12][35][33], ค่า 0.44 domain-rating correlation เป็น input ในการวางแผน [16] และ CapCut AI film festival ถ้าไม่ได้ทำงาน AI film [43] อย่าคาดหวังว่า demo เหล่านี้พร้อม production — ถือว่าทุกอย่างเป็น prototype [14][22]

## Signals to Watch
- การกำหนด model access — "Mythos" gated vs Fable 5 public — และการถกเรื่อง ad-monetization; ติดตามว่า tiering/pricing จะได้รับการยืนยันหรือไม่ [50][19]
- Codex app thread-spawning บวกกับ wake-every-5-min orchestrator loop ที่กำลังพัฒนาเป็น workflow ที่ทำซ้ำได้ [2][37]
- Pattern ffmpeg-to-wasm ที่แพร่กระจายสำหรับ client-side media เพื่อแทน server shell-out [7][42]
- ช่องว่างระหว่างคำกล่าวอ้าง "ไม่เคยเขียนโค้ดแม้แต่บรรทัดเดียว" กับความเป็นจริง "native apps still hard" [11][14]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | steipete | ^5178 c349 | [@_ARahim_ @bcherny only boomers fix typos in prompts. llms perfectly understand ](https://x.com/steipete/status/2064824399061299642) |
| x | steipete | ^4524 c179 | [Here's a simple loop: Tell codex to maintain your repos, wake up every 5 minutes](https://x.com/steipete/status/2064998499780084154) |
| x | marclou | ^971 c136 | [I asked Claude Fable 5 to build a game on top of my web analytics API. It made D](https://x.com/marclou/status/2065029898243318093) |
| x | steipete | ^671 c36 | [Getting Chris to do a PR with Codex!](https://x.com/steipete/status/2065176989359808636) |
| x | gregisenberg | ^575 c33 | [99% of people are using Claude Fable 5 wrong. People don't know how to work with](https://x.com/gregisenberg/status/2065184897296146724) |
| x | jackfriks | ^484 c78 | [can't believe this was only 18 months and 8 weeks ago... https://t.co/uvQxrEIShj](https://x.com/jackfriks/status/2065091476028047635) |
| x | steipete | ^445 c24 | [Part of the OpenClaw hardening work is reducing surface risk; for some media con](https://x.com/steipete/status/2064999763397980286) |
| x | levelsio | ^265 c17 | [I have revived @javilopen's 28 year old custom map he made and made a web-based ](https://x.com/levelsio/status/2065079822632538126) |
| x | levelsio | ^217 c23 | [I have to stop boring all of you with my game ports but I ported another game to](https://x.com/levelsio/status/2065139944478093555) |
| x | rileybrown | ^181 c26 | [No Codex Updates this week?](https://x.com/rileybrown/status/2065185122995909120) |
| x | rileybrown | ^179 c28 | [I've still never written a line of code lol. https://t.co/1y9JueY0ur](https://x.com/rileybrown/status/2065177813162901790) |
| x | jackfriks | ^166 c61 | [if taxes didn't exist i think i would be a lot less frugal cause i made a lot of](https://x.com/jackfriks/status/2065081366178345456) |
| x | jackfriks | ^152 c32 | [was going to buy a QR code wedding photo gallary software for my wedding but the](https://x.com/jackfriks/status/2065158280993734833) |
| x | steipete | ^148 c13 | [writing mac apps is still hard.](https://x.com/steipete/status/2065132980398444945) |
| x | godofprompt | ^127 c8 | [I uploaded a McKinsey PDF report to Claude Fable 5 and told it to build a new re](https://x.com/godofprompt/status/2065031957139034371) |
| x | marclou | ^119 c28 | [Moderate correlation (0.44) between a startup's revenue and its website domain r](https://x.com/marclou/status/2065090686245077403) |
| x | rileybrown | ^51 c5 | [Bro what... 👀](https://x.com/rileybrown/status/2065163458128007327) |
| x | steipete | ^50 c5 | [@eskoropisov You ask the man with unlimited tokens?](https://x.com/steipete/status/2064999858780688660) |
| x | rileybrown | ^49 c17 | [Ads seem inevitable even at the power-user level. People will GLADLY accept ads ](https://x.com/rileybrown/status/2065220325340533102) |
| x | AmirMushich | ^46 c15 | [Arena shooter made with Claude Fable in 1 prompt the prompt + remix link👇 https:](https://x.com/AmirMushich/status/2064814705881780614) |
| x | godofprompt | ^45 c6 | [I had Claude Fable 5 build a walkable 3D Kyoto neighborhood in Three.js. Runs in](https://x.com/godofprompt/status/2065105437259882845) |
| x | steipete | ^42 c2 | [@msuiche This is personal oss and not finished/integrated yet. Feedback welcome!](https://x.com/steipete/status/2065163664253227036) |
| x | 0xROAS | ^42 c0 | [here's how it looks like: https://t.co/lisFcjuz7a](https://x.com/0xROAS/status/2065135547366928715) |
| x | godofprompt | ^36 c6 | [Game over @RockstarGames https://t.co/9XF4GCGEQA](https://x.com/godofprompt/status/2065162384671437222) |
| x | godofprompt | ^32 c2 | [A decision you can't explain is a decision you can't defend. That's why you stal](https://x.com/godofprompt/status/2065045645908652375) |
| x | steipete | ^31 c1 | [@princebansal94 I just did, including skills?](https://x.com/steipete/status/2065007624064729192) |
| x | AmirMushich | ^29 c5 | [1 doc to Claude promo video No edits One MCP + Fable full process below](https://x.com/AmirMushich/status/2065031141808124401) |
| x | godofprompt | ^29 c4 | [Here's a TLDR of the situation: Meme by @myhandle https://t.co/rqMpPksdNo](https://x.com/godofprompt/status/2064974391096832303) |
| x | 0xROAS | ^29 c1 | [https://t.co/OXulLk3wuL](https://x.com/0xROAS/status/2065132329870192848) |
| x | godofprompt | ^28 c4 | [Microsoft literally has Claude built into Copilot and M365. They invested billio](https://x.com/godofprompt/status/2065147920446619773) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5178 · 💬 349</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2064824399061299642">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@_ARahim_ @bcherny only boomers fix typos in prompts. llms perfectly understand you even if you mistype.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete บอกในการตอบโต้ว่าไม่จำเป็นต้องแก้ typo ใน prompt เพราะ LLM ปัจจุบันเข้าใจได้ปกติแม้สะกดผิด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2064824399061299642" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4524 · 💬 179</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2064998499780084154">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here's a simple loop: Tell codex to maintain your repos, wake up every 5 minutes and direct work to threads. That makes it easy to parallelize+steer work as needed. I use a orchestrator skill combined”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete รัน Codex ใน loop ทุก 5 นาที ผ่าน orchestrator+triage+autoreview+computer-use skill เพื่อ maintain repo แบบ autonomous ในหลาย thread พร้อมกัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>pattern นี้ — scheduled agent loop + orchestrator + parallel threads — เป็น template จริงสำหรับ automate PR triage, code review, และ issue routing โดยไม่ต้องคอยดูตลอด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดลองบน repo ที่ active หนึ่งตัว โดยใช้ /loop + /schedule skill ของ Claude Code จับคู่กับ triage orchestrator ให้ handle PR review และ issue routing แบบ autonomous</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2064998499780084154" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 971 · 💬 136</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2065029898243318093">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I asked Claude Fable 5 to build a game on top of my web analytics API. It made DataEmpire: Every visitor to your site is a villager. They chop trees 🌳 build houses 🏠 and turn a campfire 🔥🏕️ into an em”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Marc Lou ใช้ Claude Fable 5 สร้าง DataEmpire — browser game แนว city-building ที่ visitor แต่ละคนกลายเป็น villager โดยดึงข้อมูลจาก DataFast analytics API แบบ real-time</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Claude Fable 5 สร้างเกมที่ต่อ API ได้จริงจาก prompt เดียว — ชี้ให้เห็นศักยภาพในการ prototype งาน interactive อย่างเร็ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมลอง prompt Claude Fable 5 สร้าง gamified layer หรือ visual demo บน API โปรเจกต์ที่มีอยู่ใน session เดียว เพื่อ validate concept เร็วขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2065029898243318093" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 671 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2065176989359808636">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Getting Chris to do a PR with Codex!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete เล่าว่าให้ contributor ชื่อ Chris ส่ง pull request โดยใช้ OpenAI Codex เป็นตัวดำเนินการ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Codex ถูกใช้ขับเคลื่อน PR flow ทั้งกระบวนการ — ไม่ใช่แค่เขียน code — บ่งชี้ว่า AI agents กำลังเข้าสู่ git workflow จริงจัง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Codex CLI กับ PR ภายในจริงๆ เพื่อวัดว่า handle git/GitHub steps ได้ถึงจุดไหนโดยไม่ต้องมีคนช่วย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2065176989359808636" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 575 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2065184897296146724">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“99% of people are using Claude Fable 5 wrong. People don't know how to work with it yet because nothing this powerful has ever existed. I'll show you 10+ use cases and startup ideas that can only exis”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@gregisenberg โปรโมตวิดีโอ ~34 นาที อ้างว่าคนส่วนใหญ่ใช้ Claude Fable 5 ผิดวิธี พร้อม 10+ use cases และ startup ideas แต่โพสต์ไม่มีรายละเอียดใดเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2065184897296146724" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jackfriks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 484 · 💬 78</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jackfriks/status/2065091476028047635">View @jackfriks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“can't believe this was only 18 months and 8 weeks ago... https://t.co/uvQxrEIShj”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@jackfriks โพสต์ถึงอะไรบางอย่างเมื่อ ~20 เดือนก่อน โดยไม่มีบริบทหรือรายละเอียดใดเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jackfriks/status/2065091476028047635" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 445 · 💬 24</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2064999763397980286">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Part of the OpenClaw hardening work is reducing surface risk; for some media conversion we had to shell out to ffmpeg. In the next release that can now be done via wasm, with similar performance for o”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>OpenClaw เปลี่ยนจากการ shell out ไปหา ffmpeg มาใช้ ffmpeg.wasm แทนใน media conversion เพื่อลด attack surface โดย performance ใกล้เคียงเดิม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แทน subprocess ffmpeg ด้วย wasm ตัด shell-injection risk ใน server หรือ web pipeline ที่รับ media จาก user ได้ทันที</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">project ที่ shell out หา ffmpeg สำหรับ video/audio ลอง ffmpeg.wasm แทนเพื่อปิดช่องโหว่ subprocess</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2064999763397980286" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 265 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2065079822632538126">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I have revived @javilopen's 28 year old custom map he made and made a web-based Quake 2 with Fable on fast mode 🤓 You can now play it here: 👉 https://t.co/vkEhgC2jkg 👈 It took a bit of hacking because”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio ใช้ Claude Fable ปลุกแผนที่ Quake 2 อายุ 28 ปี แก้ texture ไม่โหลดด้วยการ repack PAK files แล้ว deploy เป็นเกมเล่นบนเว็บ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>AI แก้ binary format เก่า (PAK files) ได้โดยไม่ต้องมี tool เฉพาะ — ตรงกับงานขุด asset หรือ project เก่าของ studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าเจอ Unity หรือ game project เก่าที่ asset พัง ลอง Claude Fable วิเคราะห์และแก้ format ก่อน re-export เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2065079822632538126" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
