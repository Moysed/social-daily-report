---
type: social-topic-report
date: '2026-06-03'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-06-03T07:13:51+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.55
sentiment: mixed
confidence: 0.5
tags:
- ai-agents
- codex-sites
- agent-native-apps
- openclaw
- ai-media-gen
- prompt-ops
thumbnail: https://pbs.twimg.com/media/HJ0pf9qWsAAmG9J.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-06-03

## TL;DR
- Riley Brown เสนอ thesis "agent-native app": ให้ pivot แอปแบบ standalone มาเป็น agent-driven [11][15] และสาธิต Codex Sites กับ Convex DB plugin สำหรับสร้าง hosted app และ internal tools ที่ agent เขียนได้ [16][18]; MengTo รายงานว่า ship แอปเว็บ 3 ตัวพร้อม Mac/iOS apps บน Codex [52]
- steipete (Peter Steinberger) กำลังนำ OpenClaw — agent gateway แบบ open-source, plugin-based — เข้าหา enterprise ผ่าน Microsoft [1][10][54] พร้อมเพิ่ม observability, security primitives, และ verifiable workspaces [6][56] หลังปิด ~1000 open issues [39]
- godofprompt แชร์ prompt-ops trick ที่ใช้ได้จริง: บรรทัดใน CLAUDE.md ที่บังคับให้โมเดลเรียกชื่อคุณเป็น canary ตรวจจับว่าโมเดลหยุดทำตาม instructions เมื่อใด [12]
- AI media-gen ยังคงอ้างสิ่งที่ escalate ขึ้นเรื่อย: คุณภาพภาพ Nano Banana 2 [5], brand mockups จาก Seedance [27], และรายงาน AI feature film เรื่องแรกที่ $500,000 [31]; godofprompt อ้าง Anthropic มี annual revenue ~$47B ใกล้ถึง profitable quarter แรก [45]
- ส่วนใหญ่ของ feed เป็น low-signal: thread เรื่องแอร์เครื่องบินและการเดินทาง [4][25][28][29], meta เรื่องนิสัย bookmark [2][23], และ gamification แนว "ship or die / market or die" [17][40][60]

## What happened
นี่คือ digest ของความเห็นและ anecdotes จาก builders 15 คนที่ติดตาม ไม่ใช่ข่าว thread หลักคือ agent-native development tooling Riley Brown โต้ว่าแอปแบบ standalone ควรกลายเป็น agent-native [11] อ้างว่า desktop app ที่รวม browser กับ agent ทำให้ design tools แยกต่างหากไม่จำเป็นอีกต่อไป [15] และสาธิต Codex Sites กับ Convex database plugin ที่เพิ่งปล่อยออกมาสำหรับสร้าง hosted, agent-writable apps และ internal tools [16][18]; รวมถึงรัน personal site ที่ auto-deploy ทุกสัปดาห์ผ่าน Codex automations [7] MengTo รายงานอิสระว่าสร้างแอปเว็บสามตัวและ Mac/iOS apps บน Codex [52] steipete กำลัง position OpenClaw — อธิบายว่าเป็น open-source, plugin-based agent gateway ไม่ใช่ clone [10][54] — สำหรับ enterprise ผ่าน Microsoft partnership [1] พร้อม observability, security, และ verifiable workspaces [6][56] หลังลด ~1000 issues [39]

## Why it matters (reasoning)
สิ่งที่ accounts เหล่านี้สื่อซ้ำๆ คือ unit ของซอฟต์แวร์กำลังเปลี่ยนจากแอปแบบ standalone ไปเป็นแอปที่ agent อ่าน เขียน และ host ได้ end-to-end [11][15][16][18] ถ้า Codex Sites + Convex ทำให้คนๆ เดียว stand up hosted, agent-writable backend ได้จริงอย่างรวดเร็ว [18] ต้นทุนของ internal tools และ prototypes จะลดลง ซึ่งสำคัญสำหรับ studio เล็กๆ ที่ทำ web/mobile และ edutech การที่ OpenClaw มุ่งสู่ enterprise [1][6] บ่งชี้ว่า agent harnesses กำลังถูก harden สำหรับ governance — observability และ security กลายเป็น selling points ไม่ใช่ afterthoughts CLAUDE.md canary [12] คือคำตอบที่ถูกและใช้งานได้จริงสำหรับ failure mode ที่มีอยู่จริง: instruction drift แบบเงียบในการรัน agent session นาน ด้าน media-gen, AI film $500k [31] และ tool claims [5][27] ชี้ว่าต้นทุนการผลิต content กำลังลดลง แม้จะเป็นแค่ single anecdotes จาก promotional accounts ตัวเลข revenue ของ Anthropic [45] ถ้าถูกต้อง จะ reframe ตลาดโมเดลรอบ revenue แทนการประเมินมูลค่า

## Possibility
**Likely:** ต้นทุน AI image/video generation ลดต่อลงและคุณภาพยังคงเพิ่มขึ้น จาก demo อิสระหลายรายการ [5][27][31] **Plausible:** Codex Sites + Convex เติบโตเป็น path ที่ใช้งานได้สำหรับ internal tools และ prototypes แบบรวดเร็ว [16][18] แต่ตอนนี้ยังเป็นแค่ early demos ของ practitioners กลุ่มเล็ก ยังไม่ proven ที่ scale **Plausible:** enterprise agent gateways ที่มี observability/security (OpenClaw) จะได้รับความสนใจเมื่อ governance กลายเป็น requirement [1][6][56] **Unlikely (near-term, บนหลักฐานนี้):** "standalone apps are over" [8][15] — นี่คือ provocations จาก creators ที่มีแรงจูงใจด้าน reach ไม่ใช่ข้อมูล ให้ถือเป็น directional bet ไม่ใช่ fact

## Org applicability — NDF DEV
**Low effort:** นำ CLAUDE.md fixed-name canary (หรือ marker ที่คล้ายกัน) มาใช้ตรวจจับ instruction drift ใน Claude Code / agent sessions นานทั่วทีม [12] **Low effort:** ประเมิน Nano Banana 2 และ Seedance สำหรับ marketing mockups และ concept assets ด้าน game/XR รวมถึง Claude Project brand-guideline kit สำหรับ branding ลูกค้า [5][27][33] **Med effort:** ทดลอง Codex Sites + Convex plugin สำหรับ internal tool หรือ e-learning prototype เพื่อวัดความเร็วเทียบกับ stack ปัจจุบัน [16][18][52] **Low effort (monitor only):** ติดตามงาน enterprise observability/security ของ OpenClaw เมื่อ agent tooling เติบโตขึ้น [1][6] **Skip:** thread เรื่องการเดินทาง/แอร์ [4][25][28][29], meta เรื่อง bookmark [2][23], hot takes เรื่องการยกเลิก free plan และ agent-economy [9][22], และ content แนว "ship or die" gamification [17][40][41][60]

## Signals to Watch
- Codex Sites + Convex plugin ในฐานะ fast path สู่ agent-writable hosted apps และ internal tools [16][18]
- AI feature film เรื่องแรกที่รายงานว่าใช้งบ $500,000 — data point ด้านต้นทุนการผลิต AI video [31]
- Anthropic ถูกอ้างว่าใกล้ถึง profitable quarter แรกที่ annual revenue ~$47B [45]
- การที่ OpenClaw รุกสู่ enterprise ผ่าน Microsoft พร้อม observability และ security primitives [1][6]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | steipete | ^3351 c104 | [Such a privilege to work with Microsoft to bring claws to enterprises!](https://x.com/steipete/status/2061874084649025728) |
| x | gregisenberg | ^1738 c483 | [Bookmarking tweets and not going back to them has become an epidemic](https://x.com/gregisenberg/status/2061835266587869404) |
| x | steipete | ^1136 c59 | [I told codex to use https://t.co/oHS8ombQcW whenever I'm distracted and it needs](https://x.com/steipete/status/2061574752574283858) |
| x | levelsio | ^1049 c42 | [Is it really true the EU does not allow airlines to use AC when the plane is not](https://x.com/levelsio/status/2061885263547167122) |
| x | egeberkina | ^763 c7 | [Nano Banana 2 is ridiculously good at this https://t.co/5zoGQNFH9s](https://x.com/egeberkina/status/2061849907447701818) |
| x | steipete | ^622 c19 | [It's been great working with Omar to get observability and verifiable workspaces](https://x.com/steipete/status/2061877813053907083) |
| x | rileybrown | ^549 c35 | [I built my new personal site on codex and it auto updates and deploys every Frid](https://x.com/rileybrown/status/2061848340166221910) |
| x | rileybrown | ^482 c55 | [Codex is dead. https://t.co/IsJtJ79hsW](https://x.com/rileybrown/status/2061882022981771660) |
| x | gregisenberg | ^442 c81 | [There's probably $100+ billion up for grabs for people who build startup for AI ](https://x.com/gregisenberg/status/2061889033865978326) |
| x | steipete | ^417 c16 | [@alexeheath It's not OpenClaw-like, it is the OpenClaw gateway.](https://x.com/steipete/status/2061909136435016185) |
| x | rileybrown | ^390 c48 | [If you're building a standalone application pivot to making an agent native app.](https://x.com/rileybrown/status/2061832477425950924) |
| x | godofprompt | ^368 c40 | [The dumbest-looking line in my CLAUDE. md is the most useful thing in it. It tel](https://x.com/godofprompt/status/2061722755280810476) |
| x | jackfriks | ^286 c39 | [man, having a cofounder is so damn cool https://t.co/mju5862umr](https://x.com/jackfriks/status/2061926862285046118) |
| x | jackfriks | ^260 c40 | [just booked first ever business class flight using business credit card points c](https://x.com/jackfriks/status/2061818481658450379) |
| x | rileybrown | ^198 c33 | [As soon as you shove a full browser into a desktop app that works seamlessly wit](https://x.com/rileybrown/status/2061821779547394372) |
| x | rileybrown | ^187 c8 | [Wow very easy to create a Codex Site with a Convex DB that your agent can write ](https://x.com/rileybrown/status/2062011135797137776) |
| x | jackfriks | ^181 c42 | [update to my app that forces people to make internet businesses in 30 days [ship](https://x.com/jackfriks/status/2061838787077161248) |
| x | rileybrown | ^170 c12 | [Codex is now insane for internal tools. Any app you want, hosted with new Codex ](https://x.com/rileybrown/status/2061999322372145192) |
| x | rileybrown | ^160 c30 | [Google is trying to make all their apps into super-apps, and the result will be ](https://x.com/rileybrown/status/2061817491408531611) |
| x | EXM7777 | ^154 c21 | [starting today i'm killing most of my short-form strategy on X... here's what ch](https://x.com/EXM7777/status/2061810575391465870) |
| x | egeberkina | ^150 c2 | [This is exactly how i remember skiing --sref 3662540287 568834969 --v 8.1 https:](https://x.com/egeberkina/status/2061782896042459640) |
| x | marclou | ^116 c47 | [Remove your free plan. Free users are leeches. They increase support, server cos](https://x.com/marclou/status/2062057982876410140) |
| x | gregisenberg | ^112 c15 | [I suffer from long bookmark](https://x.com/gregisenberg/status/2061835618133446716) |
| x | vasuman | ^111 c13 | [CTOs of startups (YC or otherwise) that aren't going the way you hoped: let's ch](https://x.com/vasuman/status/2061651983824765430) |
| x | levelsio | ^100 c0 | [@thorswdn Yes all the time, US not, Brazil not, Asia not, Middle East not](https://x.com/levelsio/status/2061919555635581241) |
| x | marclou | ^96 c25 | [✅ Startup Acquisition #97 on @trust_mrr ✅ AI security SaaS sold for $2,000 in 28](https://x.com/marclou/status/2061828694709293392) |
| x | AmirMushich | ^90 c8 | [Nike, Uniqlo, DKNY & other brands look fresh on these mockups Seedance prompt: t](https://x.com/AmirMushich/status/2061542292092309733) |
| x | levelsio | ^89 c1 | [@RBoehme86 Nah it's cold af in Brazil and Asia when you board](https://x.com/levelsio/status/2061919063723344200) |
| x | levelsio | ^79 c11 | [This @flysas flight was extremely hot No AC in flight either Is this normal for ](https://x.com/levelsio/status/2061908179072455030) |
| x | levelsio | ^71 c4 | [@Adrien_B_A Also the center of fashion is moving to Asia now](https://x.com/levelsio/status/2061804971742335246) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3351 · 💬 104</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061874084649025728">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Such a privilege to work with Microsoft to bring claws to enterprises!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ประกาศ partnership กับ Microsoft เพื่อนำ Claude (Anthropic AI) เข้าสู่ enterprise ผ่าน Azure</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Claude เข้า enterprise ผ่าน Microsoft หมายความว่า Azure-hosted Claude จะมี SLA และ compliance รองรับมากขึ้น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า client ต้องการ enterprise compliance ลอง evaluate Azure AI Foundry เป็นช่องทาง Claude แทน Anthropic API ตรง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061874084649025728" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1738 · 💬 483</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2061835266587869404">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bookmarking tweets and not going back to them has become an epidemic”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@gregisenberg ตั้งข้อสังเกตว่าคนส่วนใหญ่ bookmark tweet แล้วไม่เคยกลับไปอ่าน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2061835266587869404" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1136 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061574752574283858">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I told codex to use https://t.co/oHS8ombQcW whenever I'm distracted and it needs my help to be unblocked, and ever once it a while I hear it talking to me, and it's the coolest thing ever. (e.g. for r”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ตั้ง OpenAI Codex ให้ใช้ TTS พูดออกเสียงเมื่อ agent ติดขัดและต้องการ human input เช่น ตอน release ผ่าน npm ที่ต้องยืนยันด้วย 1Password</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>agent มักหยุดเงียบๆ ตอนเจอขั้นตอน auth — audio alert ช่วยให้ dev ทำงานอื่นต่อและเข้ามาช่วยเฉพาะตอนที่ติดจริงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เพิ่ม TTS หรือ OS notification ใน agent instructions ให้แจ้งเมื่อติดที่ขั้นตอน auth เช่น npm publish หรือ code signing</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061574752574283858" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1049 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2061885263547167122">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Is it really true the EU does not allow airlines to use AC when the plane is not flying yet? Every EU plane I board is a sauna until it takes off?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio ตั้งคำถามว่า EU มีกฎห้ามสายการบินเปิด AC ตอนจอดอยู่บนพื้นหรือเปล่า เพราะทุกเที่ยวบินใน EU ร้อนมากก่อน takeoff</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2061885263547167122" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@egeberkina</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 763 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/egeberkina/status/2061849907447701818">View @egeberkina on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Nano Banana 2 is ridiculously good at this https://t.co/5zoGQNFH9s”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ @egeberkina ชมเครื่องมือชื่อ 'Nano Banana 2' โดยไม่บอกว่ามันทำอะไร — context ทั้งหมดอยู่ในลิงก์ที่ไม่ได้อธิบาย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/egeberkina/status/2061849907447701818" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 622 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061877813053907083">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It’s been great working with Omar to get observability and verifiable workspaces into OpenClaw.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer @steipete โพสต์ชมการทำงานร่วมกับ Omar เพื่อเพิ่ม observability และ verifiable workspaces ใน OpenClaw โดยไม่มีรายละเอียดว่า OpenClaw คืออะไรหรือ ship อะไรไปบ้าง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061877813053907083" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rileybrown</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 549 · 💬 35</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rileybrown/status/2061848340166221910">View @rileybrown on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I built my new personal site on codex and it auto updates and deploys every Friday with updated data and videos. (https://t.co/9xepzFj1Pq) Codex automations + this new sites feature will be huge for i”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้โพสต์สร้างเว็บไซต์ส่วนตัวด้วย OpenAI Codex โดยตั้ง automation ให้ดึงข้อมูลใหม่และ deploy อัตโนมัติทุกวันศุกร์ ผ่าน Codex automation + ฟีเจอร์ sites ใหม่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Codex automation + site hosting ช่วยให้ทีมสร้าง internal dashboard หรือ portal ที่ดึงข้อมูลใหม่และ redeploy อัตโนมัติตามรอบ โดยไม่ต้อง deploy เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองใช้ Codex scheduled automation กับ internal tool เล็กๆ เช่น หน้า stats รายสัปดาห์หรือ team showcase เพื่อประเมิน pipeline ก่อนนำไปใช้จริงในโปรเจกต์ใหญ่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rileybrown/status/2061848340166221910" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rileybrown</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 482 · 💬 55</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rileybrown/status/2061882022981771660">View @rileybrown on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Codex is dead. https://t.co/IsJtJ79hsW”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>OpenAI Codex กำลังถูกปิดตัว ตามโพสต์ของ @rileybrown ที่แนบ screenshot มาเป็นหลักฐาน โดยไม่มีข้อความทางการในโพสต์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Codex เป็น agentic coding tool ที่แข่งกับ Cursor และ GitHub Copilot โดยตรง การปิดตัวลดทางเลือกที่ทีมอาจกำลังใช้หรือประเมินอยู่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตรวจสอบว่ามีใครในทีมใช้ Codex อยู่ ถ้ามีให้ย้ายไป Cursor หรือ GitHub Copilot และอัปเดต Codex API calls ใน internal tooling</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rileybrown/status/2061882022981771660" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
