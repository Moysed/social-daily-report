---
type: social-topic-report
date: '2026-06-02'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-06-02T03:55:30+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.5
sentiment: mixed
confidence: 0.58
tags:
- ai-agents
- codex
- agent-memory
- llm-tooling
- generative-video
- indie-hackers
thumbnail: https://pbs.twimg.com/media/HJpy1sAa8AABRYW.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-06-02

## TL;DR
- Codex คือเส้นเรื่องหลัก: steipete ใช้เป็น QA agent เขียน test scenario รายคอมมิตผ่าน browser-use tooling [2], ทำ TypeScript codemods แบบ ad-hoc [14], และให้แจ้งเตือนด้วยเสียงเมื่อ agent ติดขัด [11]; rileybrown clone setup ของ Codex เป็น cloud agent ถาวรที่คุยได้ผ่าน iMessage [20].
- Agent memory คือ cross-cutting idea ที่วนซ้ำ — knowledge graph แทน vector store [31], 'memory infra layer' [21], และ 'เราให้ tools agent ก่อน memory' [36].
- vasuman ชี้ว่า Opus 4.8 regression: 'พูดเหมือน 4o เป๊ะ, hallucinate หนัก' [15]; rileybrown ยืนยันว่า ship ไปแล้วสัปดาห์ที่แล้ว [35].
- godofprompt รายงานว่า frontier provider ถอด temperature parameter ออกแล้ว (OpenAI o1/o3/GPT-5; Google เตือนไม่ให้แตะ Gemini 3) [34].
- Generative media ราคาถูกลงต่อเนื่อง: 0xROAS อ้าง $0.004 ต่อวินาทีของ AI UGC video [40][42]; AmirMushich ดัน one-prompt editable design และ brand mockup [19][37][49].

## สิ่งที่เกิดขึ้น
การสนทนาระดับ practitioner สัปดาห์นี้หมุนรอบ OpenAI Codex. steipete สร้าง agentic dev workflow: QA assistant ที่ generate user-test scenario ต่อคอมมิตด้วย webVNC/computer-and-browser-use tooling [2], codemods ad-hoc สำหรับ TypeScript migration ขนาดใหญ่ [14], และ audio notification เมื่อ agent ติด [11] — รวมถึง modular agent ชื่อ OpenClaw ที่เน้น lean และ 'เพิ่มเฉพาะที่ต้องการ' [10][18][53]. rileybrown clone setup ของ Codex เป็น cloud agent ถาวรที่คุยผ่าน iMessage [20], ใช้ Codex Browser Use [17], และ Paper ใน Codex สำรวจ thumbnail [24]. Agent memory วนซ้ำเป็น bottleneck ที่รับรู้กัน: knowledge graph vs vector DB [31], 'memory infra layer' [21], และ framing ว่า tools มาก่อน memory [36].

## ทำไมถึงสำคัญ (เหตุผล)
สัญญาณที่เห็นคือการ consolidate: operator อิสระกำลังมุ่งหา Codex สำหรับ agentic coding (QA, codemods, cloud persistence) ซึ่งแสดงว่าเป็น pattern ที่ NDF DEV ลอกได้เลยแทนที่จะประดิษฐ์ใหม่ [2][14][20]. framing เรื่อง memory ที่วนซ้ำ [21][31][36] ชี้ว่า workflow เหล่านี้ยังพังตรงไหน — agent ที่ทำได้แต่ไม่จำ — ซึ่งเกี่ยวข้องถ้า NDF จะสร้าง AI feature แบบ persistent. รายงาน Opus 4.8 regression จาก voice ที่น่าเชื่อถือ [15][35] เป็นคำเตือนจากแหล่งเดียว ไม่ใช่ verdict แต่พอให้ทดสอบก่อน upgrade. การตัด temperature ออก [34] มีผลต่อ code จริงที่ tune LLM sampling. generative video/image ราคาถูก [40][37][19] ลดต้นทุน marketing และ concept asset แต่ตัวเลขเหล่านี้มาจากฝั่ง vendor ไม่ใช่ benchmark อิสระ.

## ความเป็นไปได้
น่าจะเกิด: Codex-style agentic dev workflow โตต่อเนื่องเมื่อ operator ออกมาเผยแพร่ setup มากขึ้น [2][14][20]. เป็นไปได้: knowledge-graph memory กลายเป็น standard layer แทน vector store แบบ naive [21][31][36]. เป็นไปได้: ราคา AI video ต่อวินาทีลดต่อไปและคู่แข่งตาม 0xROAS ที่คาดไว้ [40]. ไม่น่ายืนยันได้จาก feed นี้: 'regression' ของ Opus 4.8 [15] — เป็นความเห็นของ practitioner คนเดียว ต้องทำ eval เองก่อนตัดสินใจ. ไม่มีแหล่งใดระบุ probability เป็นตัวเลข; ตัวเลขเงินและ session [40][44] ให้ถือว่าเป็นการอ้าง ไม่ใช่ตัวเลขที่ verify แล้ว.

## การนำไปใช้ใน NDF DEV
1) ทดลอง Codex เป็น QA/test-scenario generator และสำหรับ codemods ใน refactor หนัก TS ทั้ง web/mobile — ความพยายามระดับกลาง [2][14]. 2) ถ้าจะสร้าง AI feature ที่ต้องการ memory ให้ประเมิน knowledge-graph memory layer แทน vector store ล้วนๆ — ระดับกลาง [31][21][36]. 3) ทดลอง one-prompt image/video generation สำหรับ promo เกมและ marketing asset แต่ validate ราคาและคุณภาพด้วยตัวเองก่อนผูกมัด — ต่ำ/กลาง [40][37][19]. 4) ถ้า Claude อยู่ใน stack ให้ benchmark Opus 4.8 กับ model ปัจจุบันก่อน upgrade; จับตา regression ด้าน hallucination และเสียงที่รายงาน — ต่ำ [15][35]. 5) ตรวจ LLM call ทุกจุดที่ set temperature; frontier reasoning model กำลังตัด parameter นี้ออก — ต่ำ [34]. ข้าม: โพสต์ lifestyle/motivation [5][12][27][46], spam tactics YouTube shorts [16][30][60], funnel CPA/affiliate [25], marketing prompt-pack [28][57], และ branding CEO-as-app-icon [4] — ไม่มี signal ที่ใช้งานได้สำหรับ NDF.

## Signal ที่ต้องจับตา
- รายงาน regression Opus 4.8 จาก voice ที่น่าเชื่อถือ — verify ด้วย eval ของตัวเอง [15][35].
- Temperature parameter ถูกตัดออกจาก frontier provider หลายราย; เช็คกับ code ที่ใช้งาน [34].
- Agent memory แบบ knowledge-graph layer ไม่ใช่ vector DB [21][31][36].
- Pattern Codex cloud-agent + messaging persistence (iMessage, voice-when-blocked) [20][11].

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | EXM7777 | ^2399 c41 | [this is the Hermes setup top 1% operators are using to get rid of AI slop... htt](https://x.com/EXM7777/status/2061086049326256356) |
| x | steipete | ^1582 c70 | [Been teaching codex to be my QA assistant. For every commit it creates a user-te](https://x.com/steipete/status/2061208638027395490) |
| x | vasuman | ^1034 c145 | [/goal has been running for 16 hours and we're in that sweet spot where I don't w](https://x.com/vasuman/status/2061203646449369497) |
| x | egeberkina | ^946 c44 | [CEOs are the new app icons https://t.co/W3jjrU027b](https://x.com/egeberkina/status/2061137275426165022) |
| x | marclou | ^928 c127 | [What I wanted at 20: - A fancy car - A lot of friends - A high-paid job - A craz](https://x.com/marclou/status/2061467056407708156) |
| x | gregisenberg | ^853 c121 | [Funny how the pendulum shifts 1. "GPT wrappers are worthless" → the value acrues](https://x.com/gregisenberg/status/2061484999153488082) |
| x | EXM7777 | ^573 c11 | [Matt has been shipping some incredible products lately... you should definitely ](https://x.com/EXM7777/status/2061301916324577401) |
| x | jackfriks | ^572 c62 | [years of nothing, and then everything all at once](https://x.com/jackfriks/status/2061442785253732851) |
| x | vasuman | ^537 c9 | [Incredible https://t.co/QqVOtcj5iN](https://x.com/vasuman/status/2061261104962244981) |
| x | steipete | ^471 c53 | [The idea of OpenClaw is always that it should be yours. It's modular and lean, o](https://x.com/steipete/status/2061072753998856696) |
| x | steipete | ^454 c31 | [I told codex to use https://t.co/oHS8ombQcW whenever I'm distracted and it needs](https://x.com/steipete/status/2061574752574283858) |
| x | jackfriks | ^425 c24 | [the best things this world has to offer cannot be bought. https://t.co/OqxMMk50d](https://x.com/jackfriks/status/2061480957522145750) |
| x | egeberkina | ^402 c2 | [Meet me on the green --sref 3662540287 568834969 --v 8.1 https://t.co/RIgGTHrlYx](https://x.com/egeberkina/status/2061465064243167678) |
| x | steipete | ^343 c33 | [Haven't seen codex writing ad-hoc codemods before, but it just did for a bigger ](https://x.com/steipete/status/2061115471760441692) |
| x | vasuman | ^306 c51 | [Something went very wrong in making Opus 4.8. Talks exactly like 4o. Hallucinate](https://x.com/vasuman/status/2061301288256823409) |
| x | eptwts | ^262 c17 | [there was a point in time where 99% of my traffic came from posting 5k youtube s](https://x.com/eptwts/status/2061454644115562533) |
| x | rileybrown | ^208 c13 | [Good morning everyone... I feel like it's going to be an awesome week. (Sent fro](https://x.com/rileybrown/status/2061464989307736118) |
| x | steipete | ^152 c8 | [@shashankgoyal95 @OpenRouter Integration with OpenClaw onboarding for a better s](https://x.com/steipete/status/2061182935957401658) |
| x | AmirMushich | ^142 c6 | [now you can create editable designs with 1 prompt save the tool 👇 https://t.co/f](https://x.com/AmirMushich/status/2061121201146060838) |
| x | rileybrown | ^140 c12 | [This prompt allows me to duplicate my codex setup to a persistent cloud agent th](https://x.com/rileybrown/status/2061452146864689545) |
| x | vasuman | ^139 c6 | [Memory infra layer for agents, massive unlock](https://x.com/vasuman/status/2061466097623376006) |
| x | levelsio | ^135 c48 | [@mitsuhiko I switched from 1Password to Bitwarden and it's so buggy more than ha](https://x.com/levelsio/status/2061517012271087725) |
| x | eptwts | ^132 c6 | [a beginner focusing on "building" instead of learning how to sell is incredibly ](https://x.com/eptwts/status/2061484103011061906) |
| x | rileybrown | ^131 c11 | [Wow Paper inside Codex is pretty wild. Especially with my youtube thumbnail skil](https://x.com/rileybrown/status/2061634840999448629) |
| x | 0xROAS | ^119 c9 | [say hello to $250 CPA](https://x.com/0xROAS/status/2061472119263772938) |
| x | rileybrown | ^115 c62 | [bro wispr flow went down for me... i'm so cooked lol i hate typing.](https://x.com/rileybrown/status/2061474913165148194) |
| x | jackfriks | ^114 c25 | [you are either mad at the world, or madly in love with the world pick your path.](https://x.com/jackfriks/status/2061427955427946844) |
| x | AmirMushich | ^100 c12 | [4807 folks to grab these prompts 👇 Just saw this reel on instagram: Mariah share](https://x.com/AmirMushich/status/2061360924233966022) |
| x | marclou | ^99 c25 | [✅ Startup Acquisition #96 on @trust_mrr ✅ $1.6K MRR voice-to-text startup sold f](https://x.com/marclou/status/2061428304826225077) |
| x | jackfriks | ^85 c6 | [kinda insane how you can get a youtube plaque by automating a YT channel using @](https://x.com/jackfriks/status/2061535413823504764) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2399 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2061086049326256356">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“this is the Hermes setup top 1% operators are using to get rid of AI slop... https://t.co/gbRRSx3sbM”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทวีตโปรโมต 'Hermes setup' ที่อ้างว่าช่วยลด AI slop โดยไม่อธิบายรายละเอียดใดๆ มีแค่ link กับ hype</dd>
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
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1582 · 💬 70</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061208638027395490">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Been teaching codex to be my QA assistant. For every commit it creates a user-test scenario and uses webVNC (crabbox), computer/browser use (peekaboo/mcporter) to test OpenClaw like a user/QA person w”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete ให้ Codex สร้าง user-test scenario ทุก commit แล้วรัน test ผ่าน webVNC + browser-use tools กับ app จริง พร้อมเปิด PR แก้บั๊กให้อัตโนมัติโดยไม่ต้องมีคนคอย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>QA loop แบบ agentic ที่รันทุก commit โดยไม่ต้องมี QA คน — apply ได้กับทุก web/mobile project ที่ studio ship ต่อเนื่อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง pilot ใน web project หนึ่งตัว: ให้ Codex gen test scenario ต่อ PR, รันผ่าน Playwright หรือ browser-use MCP, แล้วเปิด fix PR อัตโนมัติถ้าพัง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061208638027395490" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vasuman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1034 · 💬 145</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vasuman/status/2061203646449369497">View @vasuman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“/goal has been running for 16 hours and we're in that sweet spot where I don't want to stop it because it could be cooking but I also seriously doubt it. Please advise”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา @vasuman ปล่อย AI agent task (/goal) ทิ้งไว้ 16 ชั่วโมง ไม่มี progress signal ชี้ชัด — ติดอยู่กับ dilemma หยุด vs ปล่อยต่อ โดยไม่มีข้อมูลตัดสินใจ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Long-running agentic task ไม่มี observability built-in — ไม่มี checkpoint ทีมเผา compute โดยไม่รู้ว่า agent กำลังทำงานอยู่จริงหรือ stuck ค้างอยู่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">กำหนด timeout budget และ checkpoint prompt ชัดเจนสำหรับ long-running agent task ของ studio — ตัดสินใจด้วย policy ไม่ใช่ gut feeling</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vasuman/status/2061203646449369497" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@egeberkina</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 946 · 💬 44</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/egeberkina/status/2061137275426165022">View @egeberkina on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“CEOs are the new app icons https://t.co/W3jjrU027b”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์เขียนแค่ 'CEOs are the new app icons' ไม่มีข้อมูลเพิ่ม ลิงก์ก็ไม่มีเนื้อหาสนับสนุน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/egeberkina/status/2061137275426165022" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 928 · 💬 127</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2061467056407708156">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“What I wanted at 20: - A fancy car - A lot of friends - A high-paid job - A crazy social life - A lot of validation What I want at 30: - A fit body - A best friend - A peaceful mind - A meaningful wor”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Marc Lou โพสต์เปรียบเทียบสิ่งที่อยากได้ตอนอายุ 20 (รถ, เพื่อนเยอะ, งานเงินดี) กับตอนอายุ 30 (สุขภาพ, สงบ, งานที่มีความหมาย)</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2061467056407708156" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 853 · 💬 121</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2061484999153488082">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Funny how the pendulum shifts 1. &quot;GPT wrappers are worthless&quot; → the value acrues to application layer 2. &quot;AI will eliminate white collar jobs&quot; → someone needs to manage all these AI agents and everyon”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Greg Isenberg สรุป 8 narrative ใน AI ที่พลิกกลับ — model loyalty ตายแล้ว, open-source ครอบ 80% ของงาน, workflow engineering แทน prompt engineering, computer use ใช้จริงได้แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>จุด 'สลับ model ตาม task' และ 'workflow engineering แทน prompt engineering' ตรงกับวิธีที่ studio เล็กควรวาง AI tooling stack</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">กำหนด model ตาม task category (coding, docs, automation, design) ใน project ต่างๆ แทนการล็อคแค่ provider เดียว</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2061484999153488082" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 573 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2061301916324577401">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Matt has been shipping some incredible products lately... you should definitely equip your agents with: - /last30days - PrintingPress - Agent Cookie completely different experience with Hermes especia”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บัญชี anonymous แนะนำเครื่องมือ 3 ตัว (/last30days, PrintingPress, Agent Cookie) โดยอ้างว่าช่วยให้ Hermes ทำงานได้ดีขึ้น แต่ไม่มีคำอธิบายว่าแต่ละตัวทำอะไร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EXM7777/status/2061301916324577401" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jackfriks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 572 · 💬 62</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jackfriks/status/2061442785253732851">View @jackfriks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“years of nothing, and then everything all at once”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@jackfriks โพสต์ประโยคสั้นแสดงความรู้สึกเฉยๆ ไม่มีชื่อ tool, release, หรือ event ใดระบุ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jackfriks/status/2061442785253732851" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
