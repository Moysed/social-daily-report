---
type: social-topic-report
date: '2026-06-12'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-06-12T16:02:20+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.6
sentiment: mixed
confidence: 0.5
tags:
- claude-fable-5
- agentic-coding
- codex
- indie-hacking
- monetization
- prompt-engineering
thumbnail: https://pbs.twimg.com/media/HKnP03yWYAE8Hpp.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-06-12

## TL;DR
- การเปิดตัว Claude Fable 5 ครองฟีดที่คัดสรรมาทั้งสัปดาห์: นักพัฒนาอ้างว่าสร้าง Kyoto 3D แบบ walkable ในเบราว์เซอร์ด้วย Three.js [26], สร้าง spec สำหรับแปลง web app ซับซ้อนเป็น native iOS+Android [49], และ clone layout/typography/chart จากรายงาน McKinsey PDF [13] — ล้วนเป็นโปรโมชัน ยังไม่มีการยืนยันอิสระ
- Agentic coding loop คือ workflow หลักของสัปดาห์: prompt '/goal refactor until happy' และ '/loop' ของ steipete ทำ auto-test, auto-review และรายงานว่า merge แล้ว close PR โดยไม่มีคนดูแล [2][18][27], และ Codex บน mac/win สามารถ spawn thread ได้แล้ว [42]
- ความจริงของธุรกิจ indie สวนทางกับกระแส: MengTo เล่าว่า vibe-code มาหลายเดือนแต่ยอดขายแทบเป็นศูนย์ [24][47], levelsio กำลังจะย้ายออกจาก Wise Business เพราะถูก hold เงินโอนก้อนใหญ่นาน 10–14 วัน [1], และ jackfriks บอกว่าการประหยัด $600/เดือนน่าตื่นเต้นกว่า $50K MRR [28]
- สัญญาณด้านต้นทุนและการ monetize: Skill หนึ่งอ้างว่าลดการใช้ Fable token ได้ 60% [20]; rileybrown คาดว่าจะมีโฆษณาแม้ในระดับ power-user เพื่อแลกกับ model ระดับ 'Mythos' [16]; Mythos ยังจำกัดเฉพาะ org ที่ได้รับความไว้วางใจ ส่วน Fable 5 คือ tier สาธารณะ [51]
- ปัญหาด้าน distribution: godofprompt ระบุว่า Microsoft บล็อก product ที่ขับเคลื่อนด้วย Claude เรื่อง data retention แม้จะมีการลงทุนใน Anthropic หลายพันล้านดอลลาร์ [36]

## สิ่งที่เกิดขึ้น
จาก 15 account ที่ติดตาม สัปดาห์นี้มีสองเส้นเรื่องมาบรรจบกัน แรกคือ model ใหม่ของ Anthropic 'Claude Fable 5' ขับเคลื่อนโพสต์ส่วนใหญ่: มีการอ้างว่าสร้าง Kyoto 3D grid แบบ walkable ในเบราว์เซอร์ด้วย Three.js [26], สร้าง spec แปลง web app ซับซ้อนเป็น native iOS และ Android [49], clone ดีไซน์จากรายงาน McKinsey PDF ได้ถูกต้อง [13], pipeline จากเอกสารเดียวออกมาเป็น promo video ผ่าน MCP [34], และ Skill ที่ลดการใช้ token ลงราว 60% [20] โดยมีการอธิบายว่า tier 'Mythos' ที่แรงกว่าถูก lock ไว้สำหรับ org ที่ได้รับความไว้วางใจ ส่วน Fable 5 คือ public release [51] และ rileybrown โต้แย้งว่าโฆษณาในระดับ power-user เป็นสิ่งที่หลีกเลี่ยงไม่ได้ [16] สองคือ agentic coding loop กลายเป็น practice หลัก: steipete แชร์ prompt '/goal refactor until happy' พร้อม auto-test/auto-review/commit [2][14][27], รายงานว่า loop ทำการ merge และ close PR [18], และพบว่า Codex app สามารถ spawn thread ได้แล้ว [42]; marclou ก็แสดงความกระตือรือร้นกับ Codex เช่นกัน [43]

## ทำไมถึงสำคัญ
account เหล่านี้คือ early adopter ที่ workflow ของพวกเขามักนำหน้าการนำมาใช้ในวงกว้าง การเปลี่ยนจาก chat-style prompting มาสู่ autonomous loop แบบกำหนดขอบเขต (ตั้งเป้าหมาย → auto-test → auto-review → auto-commit) [2][18][27] จึงเป็นสัญญาณชัดเจนว่า assisted coding กำลังมุ่งไปสู่ supervised agent แทน single completion เคลม Fable 5 ถ้าเป็นจริงแม้บางส่วน ชี้ให้เห็นการสร้างผลลัพธ์ข้ามรูปแบบ (web→native spec [49], PDF→report [13], doc→video [34]) ที่ช่วยร่น prototyping ให้เร็วขึ้น แต่รายการเหล่านี้เป็นโปรโมชันและเน้น engagement ('99% are using it wrong' [3], 'Game over Rockstar' [22]) จึงต้องถือว่าเป็นเคลมที่ยังพิสูจน์ไม่ได้ บทเรียนที่ยั่งยืนกว่าคือเรื่องธุรกิจ: MengTo สร้างผลิตภัณฑ์ที่ polish แล้วแต่ยอดขายแทบเป็นศูนย์ [24][47] และ levelsio ชี้ว่าติดขัดที่ payment rail และ platform [1][50] ซึ่งยืนยันว่าความเร็วในการสร้างโค้ดไม่ได้แก้ปัญหา distribution สัญญาณด้าน monetize และ control — โฆษณาที่ top tier [16], การ gate model [51], และ friction เรื่อง data retention ระหว่าง Microsoft กับ Anthropic [36] — บ่งชี้ว่าเงื่อนไขต้นทุนและการเข้าถึง model ระดับสูงยังไม่นิ่ง

## ความเป็นไปได้
มีแนวโน้มสูง: bounded autonomous loop (goal → test → review → commit) จะกลายเป็น pattern มาตรฐานที่ builder กลุ่มนี้ขัดเกลาและเผยแพร่ต่อ เนื่องจาก steipete ใช้ prompt ซ้ำได้และมีรายงาน unattended PR merge [2][18][27] เป็นไปได้: cross-format generation แบบ Fable 5 (web→native, doc→media) ถูกนำไปใช้สำหรับการ prototype เร็วโดยทีม indie แต่ความน่าเชื่อถือในการใช้งานจริงยังตามหลัง demo เพราะทุกเคลมที่นี่ยังไม่ผ่านการยืนยันและเป็นการโปรโมตตัวเอง [13][26][49] เป็นไปได้: model ที่จ่ายเงินจะเพิ่มโฆษณาหรือ gate ที่เข้มข้นขึ้นใน higher tier ตามที่ rileybrown คาดและตามโครงสร้าง Mythos/Fable [16][51] ไม่น่าเกิดขึ้นจากหลักฐานนี้: framing ว่า 'แทนที่ studio' [22] — ไม่มีรายการใดแสดงผลลัพธ์ที่ ship, ขายได้จริง หรือใช้งานในระบบจริง และสัญญาณสวนทางเรื่องยอดขายก็ชัดเจน [24][47] ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น จึงไม่มีการใส่ตัวเลขไว้

## การประยุกต์ใช้สำหรับ NDF DEV
1) ทดลอง bounded-loop workflow กับ refactor ที่ไม่วิกฤต: ตั้งเป้าหมาย, กำหนดให้ต้องผ่าน live/e2e test และ auto-review ก่อน commit, บันทึก progress ลง scratch file — ความพยายามระดับกลาง [2][27] โดยให้มนุษย์กำกับทิศทางก่อนสำหรับงานที่ไม่ trivial ตามที่ steipete เองแนะนำ [14] 2) ทดลองใช้ Fable 5 (หรือ model ระดับสูงปัจจุบัน) สำหรับ browser 3D prototyping ใน Three.js สำหรับแนวคิด web/XR โดยถือว่าเคลม Kyoto-grid เป็น test target ไม่ใช่สิ่งที่รับประกัน — ความพยายามระดับกลาง [26] 3) ประเมิน token-reduction Skill/config สำหรับงาน assisted-coding ปกติเพื่อควบคุมค่าใช้จ่าย — ความพยายามต่ำ [20] 4) รวม iOS platform friction (developer account, การอนุมัติทุกการเปลี่ยนแปลง, ค่าธรรมเนียม 30%) ไว้ใน mobile release planning — ความพยายามต่ำ รับรู้ไว้เท่านั้น [50] 5) สำหรับงาน edutech/client ให้พิจารณา friction เรื่อง data retention ระหว่างผู้ให้บริการรายใหญ่เมื่อเลือก AI tooling สำหรับข้อมูลที่ sensitive [36] — ความพยายามต่ำ ข้ามได้: thread prompt-pack และ 'X is dead' ที่มีสาระน้อยสำหรับ stack ของเรา [22][35][39]; รายการ banking/Wise ที่ไม่เกี่ยวข้อง [1][15]; และการตัดสินใจซื้อใดๆ ที่อิงจาก Fable demo ที่ยังไม่ผ่านการยืนยันจนกว่าจะทดสอบเอง

## สัญญาณที่ต้องติดตาม
- Agent autonomy ที่พัฒนาขึ้น: Codex thread-spawning [42] บวกกับ loop ที่ merge และ close PR [18] — ติดตามว่า unattended commit ยังปลอดภัยเมื่อใช้ในระดับ scale หรือไม่
- Monetize ของ top model: โฆษณาที่คาดว่าจะมีใน power-user tier [16] และ Mythos ที่ gate ไว้เหนือ public Fable 5 [51] — ติดตามการเปลี่ยนแปลงเงื่อนไขต้นทุนและการเข้าถึง
- Vendor distribution friction: Microsoft บล็อก product ที่ใช้ Claude เรื่อง data retention [36] — ติดตามผลกระทบของ enterprise/data-policy ต่อการเลือก AI tooling
- ช่องว่าง build-vs-sell: ผลิตภัณฑ์ที่ polish ของ MengTo แต่ยอดขายแทบเป็นศูนย์ [24][47] — ติดตามบทเรียนซ้ำว่าความเร็วในการสร้างไม่ช่วยเรื่อง distribution

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | levelsio | ^1475 c67 | [I'm pretty excited to move off of Wise Business permanently after realizing I ca](https://x.com/levelsio/status/2065411033594753414) |
| x | steipete | ^1360 c18 | [@MatthewBerman /goal refactor until you are happy with the architecture. ensure ](https://x.com/steipete/status/2065357277880877413) |
| x | gregisenberg | ^1053 c66 | [99% of people are using Claude Fable 5 wrong. People don't know how to work with](https://x.com/gregisenberg/status/2065184897296146724) |
| x | marclou | ^1022 c98 | [https://t.co/Yju8RrWuOV](https://x.com/marclou/status/2065385672991752210) |
| x | steipete | ^1008 c42 | [Getting Chris to do a PR with Codex!](https://x.com/steipete/status/2065176989359808636) |
| x | steipete | ^460 c23 | [@unusual_whales huh nobody told me](https://x.com/steipete/status/2065352947215540465) |
| x | levelsio | ^272 c8 | [Per Aspera Ad Astra 🚀💫](https://x.com/levelsio/status/2065392245524623576) |
| x | rileybrown | ^267 c43 | [I've still never written a line of code lol. https://t.co/1y9JueY0ur](https://x.com/rileybrown/status/2065177813162901790) |
| x | rileybrown | ^210 c28 | [No Codex Updates this week?](https://x.com/rileybrown/status/2065185122995909120) |
| x | steipete | ^198 c13 | [writing mac apps is still hard.](https://x.com/steipete/status/2065132980398444945) |
| x | jackfriks | ^190 c39 | [was going to buy a QR code wedding photo gallary software for my wedding but the](https://x.com/jackfriks/status/2065158280993734833) |
| x | levelsio | ^159 c10 | [@anulagarwal @marclou Use a simple tech stack and automate everything 100% so it](https://x.com/levelsio/status/2065373943788093688) |
| x | godofprompt | ^139 c9 | [I uploaded a McKinsey PDF report to Claude Fable 5 and told it to build a new re](https://x.com/godofprompt/status/2065031957139034371) |
| x | steipete | ^135 c4 | [@MatthewBerman probs makes sense to first discuss direction and steer, but if it](https://x.com/steipete/status/2065357538842026196) |
| x | levelsio | ^111 c4 | [Okay I guess it's not about interest, more probably it's about this and they hav](https://x.com/levelsio/status/2065416518255440058) |
| x | rileybrown | ^104 c20 | [Ads seem inevitable even at the power-user level. People will GLADLY accept ads ](https://x.com/rileybrown/status/2065220325340533102) |
| x | jackfriks | ^91 c28 | [it's not fair at all but... those who are able to win once are much more likely ](https://x.com/jackfriks/status/2065416918740132227) |
| x | steipete | ^88 c12 | [@codingturk my loop merged and closed the PR.](https://x.com/steipete/status/2065359081750360179) |
| x | jackfriks | ^73 c46 | [wokeup to an empty customer support inbox AMA](https://x.com/jackfriks/status/2065419193684500768) |
| x | AmirMushich | ^68 c6 | [I saved 60% of Claude Fable tokens with this Skill. Here: https://t.co/RfHiPwNV5](https://x.com/AmirMushich/status/2065323550370586769) |
| x | rileybrown | ^63 c5 | [Bro what... 👀](https://x.com/rileybrown/status/2065163458128007327) |
| x | godofprompt | ^60 c8 | [Game over @RockstarGames https://t.co/9XF4GCGEQA](https://x.com/godofprompt/status/2065162384671437222) |
| x | AmirMushich | ^60 c9 | [This is my brother He worked w me on Warner's, Atlantic Records' &amp; other pro](https://x.com/AmirMushich/status/2065141652977602615) |
| x | MengTo | ^60 c8 | [I vibe-coded for months. The sales never came. A very personal livestream on me ](https://x.com/MengTo/status/2065374320202035608) |
| x | steipete | ^60 c0 | [@larryhaonlp It bugged me too! Just too much on my plate, really appreciate the ](https://x.com/steipete/status/2065335761969574254) |
| x | godofprompt | ^54 c8 | [I had Claude Fable 5 build a walkable 3D Kyoto neighborhood in Three.js. Runs in](https://x.com/godofprompt/status/2065105437259882845) |
| x | steipete | ^52 c0 | [@MatthewBerman live test should include computer use, browser use and/or keys an](https://x.com/steipete/status/2065358960513929418) |
| x | jackfriks | ^52 c19 | [for some reason saving $600/month feels more exciting then hitting $50K MRR... t](https://x.com/jackfriks/status/2065427521621971219) |
| x | steipete | ^51 c2 | [@msuiche This is personal oss and not finished/integrated yet. Feedback welcome!](https://x.com/steipete/status/2065163664253227036) |
| x | steipete | ^51 c1 | [@thorstenball I smell an amp feature that sends a "ping" at 4:50 once, even if y](https://x.com/steipete/status/2065355792644194605) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1475 · 💬 67</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2065411033594753414">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm pretty excited to move off of Wise Business permanently after realizing I can't just transfer my money out when I need to They keep my money hostage for 10-14 days at least for a big transfer, lik”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>levelsio เจอปัญหา Wise Business หน่วงการโอนเงินก้อนใหญ่ 10–14 วัน และกำลังย้ายไปใช้ Stripe Business banking แทน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สตูดิโอเล็กที่รับเงินต่างประเทศผ่าน Wise อาจเจอปัญหาเดียวกันตอนโอนเงินก้อนใหญ่ออกไปยัง broker หรือ account อื่น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าใช้ Wise Business รับเงินลูกค้า ลองทดสอบ Stripe Business banking เป็น account หลักก่อนมีโอนเงินก้อนใหญ่ครั้งต่อไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2065411033594753414" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1360 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2065357277880877413">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@MatthewBerman /goal refactor until you are happy with the architecture. ensure you live test after each significant step and autoreview/commit. track progress in /tmp/refactor-{projectname}.md”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>steipete แชร์ pattern prompt /goal ใน Claude Code สำหรับ refactor อัตโนมัติ บังคับ live test ทุก step, auto-commit, และ log progress ลง /tmp markdown file</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>pattern นี้ฝัง checkpoint (test → review → commit) ไว้ใน prompt เลย ให้ agent แก้ตัวเองได้ระหว่าง refactor โดยไม่ต้องคอย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เอา pattern /goal นี้ใช้ใน Claude Code ตอน refactor งานใหญ่ฝั่ง web หรือ Unity เพื่อลดเวลา babysit</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2065357277880877413" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1053 · 💬 66</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2065184897296146724">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“99% of people are using Claude Fable 5 wrong. People don't know how to work with it yet because nothing this powerful has ever existed. I'll show you 10+ use cases and startup ideas that can only exis”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@gregisenberg โพสต์ teaser วิดีโอ 34 นาที อ้างว่าคนส่วนใหญ่ใช้ Claude Fable 5 ผิด พร้อมสัญญาว่ามี 10+ use cases — แต่ไม่มี detail ในโพสต์เลย</dd>
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
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1022 · 💬 98</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2065385672991752210">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/Yju8RrWuOV”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>https://t.co/Yju8RrWuOV</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2065385672991752210" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1008 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2065176989359808636">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Getting Chris to do a PR with Codex!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete แชร์ภาพสั้นๆ ของ Chris ใช้ OpenAI Codex (autonomous coding agent) สร้าง PR แทน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า Codex ถูกใช้ submit PR จริงในทีม ไม่ใช่แค่ demo</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง Codex CLI กับ PR เล็กๆ ภายในก่อน เพื่อดูว่า fit กับ code review flow ของทีมแค่ไหน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2065176989359808636" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 460 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2065352947215540465">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@unusual_whales huh nobody told me”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ทวีตตอบ @unusual_whales แค่ว่า 'huh nobody told me' — ไม่มีเนื้อหาด้านเทคนิค เครื่องมือ หรือข่าวใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2065352947215540465" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 272 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2065392245524623576">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Per Aspera Ad Astra 🚀💫”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio โพสต์วลีภาษาละติน 'Per Aspera Ad Astra' (ฝ่าความยากสู่ดวงดาว) พร้อม emoji จรวด ไม่มีเนื้อหาเชิงเทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2065392245524623576" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rileybrown</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 267 · 💬 43</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rileybrown/status/2065177813162901790">View @rileybrown on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I’ve still never written a line of code lol. https://t.co/1y9JueY0ur”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@rileybrown โพสต์ว่าตัวเองไม่เคยเขียน code เลย พร้อม link ที่ไม่มีบริบทใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rileybrown/status/2065177813162901790" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
