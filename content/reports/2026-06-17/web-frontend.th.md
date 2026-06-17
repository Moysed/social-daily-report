---
type: social-topic-report
date: '2026-06-17'
topic: web-frontend
lang: th
pair: web-frontend.en.md
generated_at: '2026-06-17T15:23:48+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- hackernews
- lobsters
- x
regions:
- global
post_count: 221
salience: 0.55
sentiment: mixed
confidence: 0.6
tags:
- frontend
- ai-agents
- design-tokens
- tailwind
- open-weights
- vercel
thumbnail: https://pbs.twimg.com/media/HLAwEMhWMAAzipl.jpg
translated_by: claude-sonnet-4-6
---

# Web & Frontend — 2026-06-17

## TL;DR
- Vercel ปล่อย "eve" ในฐานะ "Next.js for agents" [1][7] และ Fred Schott จาก Astro ปล่อย "Flue 1.0 Beta" ในฐานะ "Astro for agents" [6] — วันเดียวกัน, framing แทบเหมือนกันทุกคำ จึงถือว่าเป็น marketing/satire บางส่วนจนกว่า docs จะยืนยันสาระจริง
- HN front-page: ผู้บริโภค US 60% บอกว่าคำว่า "AI" ใน brand messaging ทำให้ไม่อยากซื้อ [19] — ข้อมูลตรงสำหรับการ market สินค้า edutech/e-learning
- สถานะ default ของ Tailwind ถูกตั้งคำถาม: Polar ย้าย Tailwind→StyleX เพื่อจำกัด styling ที่ไม่ตรง brand [13]; peduarte จาก Radix ถามตรงๆ ว่า "Great Tailwind Migration" เริ่มแล้วหรือยัง [16]
- GLM-5.2 ขึ้นอันดับ 1 open-weights บน Artificial Analysis [24] รายงานว่าแซง Opus 4 [30]; โพสต์ที่อ่านกันมากโต้ว่า "running local models is good now" [3]
- Pattern สำหรับ AI-built UI: ล็อก LLM ไว้กับ shadcn + global design tokens [23] และรัน design-system linting ใน agent loop (Impeccable 3.7) [39]

## What happened
สองค่าย web framework เผยแพร่โปรเจกต์ "framework for agents" วันเดียวกัน: Vercel เปิดตัว "eve" พร้อม layout แบบ agent/instructions.md/tools/skills/sandbox/schedules ในชื่อ "Next.js for agents" [1] ซึ่ง Guillermo Rauch จาก Vercel ก็ echo ซ้ำ [7]; และ Fred Schott ผู้สร้าง Astro ปล่อย "Flue 1.0 Beta" ซึ่งเป็น TypeScript agent harness ที่ประกาศ "zero LLM lock-in" ในชื่อ "Astro for agents" [6] Rauch ยังผลัก Vercel AI SDK ว่าเกี่ยวข้องกว่าท่ามกลางการแข่งขันของ model โดยอ้าง GLM-5.2 ที่แซง Opus 4 [30] ด้าน styling, Polar ประกาศย้ายจาก Tailwind ไป StyleX เพื่อให้ค่าที่ไม่ตรง brand ทำได้ยากขึ้น [13] และ peduarte ตั้งคำถามว่า dominance ของ Tailwind กำลังจะสิ้นสุดหรือไม่ [16] นักพัฒนารายงานว่า LLM สร้าง UI ได้ผลดีขึ้นเมื่อจำกัดให้ใช้ shadcn กับ global design tokens [23] และ Impeccable 3.7 เพิ่ม design-system-aware linting ระหว่าง agent build [39]

## Why it matters (reasoning)
Frontend vendor กำลังนำ convention ของตัวเอง (file-based config, opinionated project structure) มาครอบบน AI agent [1][6][7] สัญญาณคือ agent tooling ถูก market หาผู้พัฒนา web โดยใช้ mental model ที่คุ้นเคยอยู่แล้ว ไม่ใช่เพราะสิ่งเหล่านี้พิสูจน์แล้ว framing "X for agents" พร้อมกันจากสองค่ายในวันเดียว [1][6] เป็นเหตุให้ skeptical ไม่ใช่ตื่นเต้น — อ่านแล้วเหมือน positioning มากกว่าอื่น thread ด้าน styling มีความเป็นรูปธรรมกว่า: StyleX [13] และ design-token discipline [23][39] แก้ปัญหาเดียวกัน — รักษา output ให้ตรง brand เมื่อทั้งมนุษย์และ LLM สร้าง UI เร็ว tokens ทำหน้าที่เป็น guardrail ที่ agent ฝ่าฝืนได้ยาก จึงเป็นเหตุที่ token-first setup ถูกรายงานว่าทำให้ UI จาก GPT-5.5/Claude ใช้งานได้จริง [23][39] ข้อมูลผู้บริโภค [19] เป็น constraint ลำดับสอง: ความเร็วของ AI feature shipping ชนกับความเบื่อหน่ายของผู้ซื้อ ดังนั้น naming และ messaging — ไม่ใช่แค่ความสามารถ — ส่งผลต่อ conversion ความก้าวหน้าของ open-weights [3][24][30] ลด cost floor ของการเพิ่ม model feature ซึ่งเกี่ยวข้องกับ edutech ที่ต้องคุมต้นทุน

## Possibility
น่าจะเกิด: design tokens กลายเป็น interface มาตรฐานระหว่าง AI codegen กับ brand consistency เพราะหลายกลุ่มที่ไม่เกี่ยวกันต่างมาลงที่จุดเดียวกันในสัปดาห์นี้ [13][23][39] เป็นไปได้: "eve" และ "Flue" เป็น promotional หรือล้อเล่นบางส่วน เนื่องจาก framing วันเดียวกันที่ประสานกัน [1][6][7] — ตรวจ docs/repos จริงก่อนสมมติว่า production ready เป็นไปได้: open-weights model (GLM-5.2) ยังปิดช่องว่างกับ closed frontier model สำหรับงานระดับ app [24][30] ทำให้ local/self-hosted inference ใช้ได้กับบาง feature [3] ไม่น่าเกิด (ระยะใกล้): การอพยพออกจาก Tailwind ครั้งใหญ่ — [16] ตั้งเป็นคำถาม และ [13] เป็นการตัดสินใจของบริษัทเดียว ไม่ใช่ trend ที่วัดได้ ไม่มี source ใดให้ตัวเลขความน่าจะเป็น ยกเว้น consumer survey [19] (60%)

## Org applicability — NDF DEV
1) Marketing copy สำหรับ edutech/e-learning และ app: หลีกเลี่ยงการนำด้วย "AI" ใน consumer-facing messaging ให้อธิบาย outcome แทน — effort ต่ำ [19] 2) ตั้ง global design-token layer และจำกัด AI-assisted UI ให้ใช้ shadcn ก่อนขยาย LLM codegen เพื่อให้ output ตรง brand และ review ได้ — effort กลาง [23][39][13] 3) ถ้าจะเพิ่ม agent/chat feature บน web หรือ mobile app ให้ประเมิน Vercel AI SDK เป็น integration layer แทนที่จะไปที่ "agent framework" ใหม่โดยตรง — effort กลาง [30][7] 4) ทดลอง open-weights model (GLM-5.2) กับ AI feature ที่ต้องประหยัดต้นทุนและไม่ critical แล้วเทียบกับ closed model — effort กลาง [24][3][30] ข้าม: อย่าย้าย Tailwind code ที่มีอยู่ไป StyleX ตอนนี้ — ไม่มีความเร่งด่วนใน items [16][13]; ข้าม "eve"/"Flue" จนกว่าจะยืนยันได้ว่าเป็นสินค้าจริงที่มี doc ชัดเจน [1][6]

## Signals to Watch
- ว่า "eve" [1] และ "Flue" [6] จะปล่อย repo/docs จริงหรือเงียบหายไปเป็น marketing — ยืนยันว่า agent framework จาก web vendor เป็น category จริงหรือไม่
- ถ้ามีทีมที่ระบุชื่อได้ย้ายออกจาก Tailwind มากกว่า Polar จะเปลี่ยนคำถามของ [16] เป็น trend [13]
- การนำ design-system linting ใน agent build loop [39] และ token-locked LLM UI [23] มาเป็น default workflow
- momentum ของ open-weights: อันดับ Artificial Analysis รอบถัดไปที่ขยับรอบ GLM-5.2 [24][30] กระทบการตัดสินใจ build-vs-buy สำหรับ AI feature

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **rxi/microui** — MicroUI – ไลบรารี UI แบบ immediate-mode ขนาดเล็ก พกพาได้ เขียนด้วย ANSI C | hackernews | <https://github.com/rxi/microui> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | vercel | ^3480 c171 | [Introducing eve, an agent framework. 𝚊𝚐𝚎𝚗𝚝/ 𝚊𝚐𝚎𝚗𝚝.𝚝𝚜 𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝𝚒𝚘𝚗𝚜.𝚖𝚍 𝚝𝚘𝚘𝚕𝚜/ 𝚜𝚔𝚒𝚕](https://x.com/vercel/status/2067180054979936413) |
| x | skzpopbase | ^1610 c1 | [Felix revealed he ate Bbokari😭 👤: felix, i saw your photos at bbq chicken restau](https://x.com/skzpopbase/status/2067205081674498488) |
| hackernews | jfb | ^1452 c558 | [Running local models is good now](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/) |
| x | amitisinvesting | ^1327 c55 | [A TON OF THINGS HAPPENED IN THE STOCK MARKET TODAY. Here's a full recap: 1. Tomo](https://x.com/amitisinvesting/status/2067074781476753884) |
| x | CartoonandFrie1 | ^1182 c11 | ["Extinction." Shed, but Shelly and Dandy sing it! CREDITS: (Art by Me!!) (instru](https://x.com/CartoonandFrie1/status/2066935831059710214) |
| x | FredKSchott | ^1119 c87 | [Just Shipped: Flue 1.0 Beta Flue is the TypeScript framework for building the ne](https://x.com/FredKSchott/status/2066962296119959581) |
| x | rauchg | ^993 c93 | [https://t.co/uNXS9jEgpg is Next.js for agents. I built Next with a simple premis](https://x.com/rauchg/status/2067183015214584307) |
| hackernews | Cider9986 | ^911 c476 | [GrapheneOS has been ported to Android 17](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) |
| x | tlepaew | ^762 c2 | [netjj and lattekim reaction to thipun nc scene is killing me😭 net: freaking out ](https://x.com/tlepaew/status/2067175000692674934) |
| x | franmirabella | ^732 c46 | [No free week... No sale price... No PVE special mode... for Marathon will "turn ](https://x.com/franmirabella/status/2067027227569709459) |
| x | markklfc | ^730 c11 | [Lionel Messi on Erling Haaland's Snapchat post calling him "a madman" after the ](https://x.com/markklfc/status/2067230807085678611) |
| x | luvlattekim | ^719 c0 | [🖤: youre so tinyyyy 🖤: WAIT THIS ONE IS LONG (talking abt the nc scene) 😭😭😭😭😭 PL](https://x.com/luvlattekim/status/2067181379708952626) |
| x | emilwidlund | ^603 c55 | [As a first blog post, I'm writing about how @polar_sh is steering away from Tail](https://x.com/emilwidlund/status/2066804861325217948) |
| x | wesyang | ^557 c26 | [Bible verses are the new blasphemy under the reign of the astro-turfed corporate](https://x.com/wesyang/status/2066881481180393766) |
| x | BRNarawins | ^548 c0 | [Our babies grew up, and now they're the seniors to GMMTV's noongs. 🥹 PONDPHUWIN ](https://x.com/BRNarawins/status/2067182372341035315) |
| x | peduarte | ^544 c39 | [uh oh has the Great Tailwind Migration started? if you've been in the game long ](https://x.com/peduarte/status/2066815577298014646) |
| x | naughtymars_ | ^521 c1 | [There it is, the Tamers redrawing I promised, I swear I'll make more cause you g](https://x.com/naughtymars_/status/2066906389633466608) |
| x | luvlattekim | ^519 c1 | [🐶: mwah mwah 🖤: is it starting?? IM— THEYRE SO UNSERIOUS IM CRYING 😭😭😭 #Reactภพเ](https://x.com/luvlattekim/status/2067169871880921153) |
| hackernews | thm | ^515 c263 | [Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://wpvip.com/future-of-the-web-2026/) |
| x | sillydrone | ^513 c7 | [Things I been working on :3 #dandysworld #astro #sprout #cosmo https://t.co/f5Qs](https://x.com/sillydrone/status/2066925542964605329) |
| hackernews | pseudolus | ^503 c219 | [Calvin and Hobbes and the price of integrity](https://therepublicofletters.substack.com/p/calvin-and-hobbes-and-the-price-of) |
| hackernews | mrshu | ^498 c215 | [TIL: You can make HTTP requests without curl using Bash /dev/TCP](https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/) |
| x | mweinbach | ^471 c23 | [You can really make GPT 5.5 good at UI if you just force it into shadcn only wit](https://x.com/mweinbach/status/2066941610256969983) |
| hackernews | himata4113 | ^466 c252 | [GLM-5.2 is the new leading open weights model on Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) |
| x | luvlattekim | ^463 c1 | [bare minimum really but i really loved how latte just let kim hide on his should](https://x.com/luvlattekim/status/2067174169272565934) |
| x | ParadisLabs | ^457 c29 | [Analysis & Signals on $SIVE x $JBL Earnings (tomorrow): Reminder: Sivers announc](https://x.com/ParadisLabs/status/2066855950527479949) |
| hackernews | dzonga | ^455 c264 | [Stop Using JWTs](https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452) |
| x | luvlattekim | ^450 c1 | [latte clapping during thipun kissing scene I JUST KNOW BOY IS SO PROUD RIGHT NOW](https://x.com/luvlattekim/status/2067170744765964331) |
| x | frog_holid25596 | ^411 c0 | [@ORoyalRules Why the fuck do you have figurines of Astro boy and Bart (they're k](https://x.com/frog_holid25596/status/2067049141910266066) |
| x | rauchg | ^402 c28 | [React → https://t.co/a4QDSs9wxd Next.js → https://t.co/nDDXqUmgw5 @aisdk is more](https://x.com/rauchg/status/2067242482190979186) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vercel</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3480 · 💬 171</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vercel/status/2067180054979936413">View @vercel on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing eve, an agent framework. 𝚊𝚐𝚎𝚗𝚝/ 𝚊𝚐𝚎𝚗𝚝.𝚝𝚜 𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝𝚒𝚘𝚗𝚜.𝚖𝚍 𝚝𝚘𝚘𝚕𝚜/ 𝚜𝚔𝚒𝚕𝚕𝚜/ 𝚜𝚊𝚗𝚍𝚋𝚘𝚡/ 𝚜𝚌𝚑𝚎𝚍𝚞𝚕𝚎𝚜/ Like Next.js, for agents. https://t.co/ezUIGLkSqG”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Vercel เปิดตัว 'eve' — agent framework ที่ใช้ file convention แบบเดียวกับ Next.js (agent.ts, instructions.md, tools/, skills/, sandbox/, schedules/)</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โครงสร้างแบบ opinionated ทำให้ทีม web ของ studio สร้าง agent ใน production ได้เลย ไม่ต้องออกแบบ architecture เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองใช้ eve กับ agent ภายในขนาดเล็ก เช่น report generator หรือ project assistant เพื่อดูว่า convention เข้ากับ web stack ของ studio แค่ไหน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vercel/status/2067180054979936413" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@skzpopbase</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1610 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/skzpopbase/status/2067205081674498488">View @skzpopbase on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Felix revealed he ate Bbokari😭 👤: felix, i saw your photos at bbq chicken restaurants. how is bbokari going to react to this? 🐥: he didn't have time to react😋 https://t.co/XHgb5pVwZg”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Felix (Stray Kids) โพสต์มุกว่าไก่เลี้ยงของตัวเอง Bbokari 'ไม่ทันได้ react' หลังแฟนเห็นเขาไปกินร้าน BBQ Chicken</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/skzpopbase/status/2067205081674498488" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amitisinvesting</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1327 · 💬 55</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amitisinvesting/status/2067074781476753884">View @amitisinvesting on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A TON OF THINGS HAPPENED IN THE STOCK MARKET TODAY. Here's a full recap: 1. Tomorrow’s FOMC meeting will be Kevin Warsh’s first as Fed Chair, and the market will be watching closely to see how he fram”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>SpaceX ประกาศซื้อ Anysphere (บริษัทแม่ของ Cursor IDE) ด้วยมูลค่า $60B โดยระบุว่าเป็น AI collaboration — ส่วนที่เหลือของโพสต์เป็นเรื่อง FOMC และ ETF volume</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า SpaceX เป็นเจ้าของ Cursor, roadmap และ pricing ของ IDE อาจเปลี่ยนทิศภายใต้ parent ที่เน้น space/defense — ควรติดตามก่อนตัดสินใจเรื่อง dev tooling</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ชะลอการสมัคร Cursor แบบระยะยาวหรือ integrate deep ไว้ก่อน จนกว่า acquisition จะปิดและ SpaceX ชี้แจง product direction</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amitisinvesting/status/2067074781476753884" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CartoonandFrie1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1182 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CartoonandFrie1/status/2066935831059710214">View @CartoonandFrie1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&quot;Extinction.&quot; Shed, but Shelly and Dandy sing it! CREDITS: (Art by Me!!) (instrumental by Orelover!) (cover by @pytholiusmogus ! ) (voice acting by lynniepoo &amp;amp; Vonphire!) #dandysworld #shed #shell”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนอาร์ตทำ music cover เพลง 'Extinction' ใช้ตัวละครจาก Dandy's World พร้อมเครดิต art, instrumental, ร้อง และพากย์เสียง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CartoonandFrie1/status/2066935831059710214" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@FredKSchott</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1119 · 💬 87</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/FredKSchott/status/2066962296119959581">View @FredKSchott on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just Shipped: Flue 1.0 Beta Flue is the TypeScript framework for building the next generation of agents, designed around an open agent harness with zero LLM lock-in. It’s like Astro, for agents. Flue ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Flue 1.0 Beta จาก creator ของ Astro คือ TypeScript agent framework บน Vite มี 3 primitive หลัก (Workflows, Agents, Channels) รองรับ LLM ทุกเจ้า, durable state recovery, และ integration พร้อมใช้กับ Slack, GitHub, Linear, Discord</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ฐาน Vite บวก channel integration พร้อมใช้ ตัด boilerplate infra ที่มักบล็อกทีมเล็กไม่ให้ ship production agent ได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง Flue เทียบกับ agent stack ปัจจุบันของ studio ใน task เดียว (e-learning หรือ web automation) เพื่อดูว่า durable Workflows ตัดโค้ด glue ออกได้จริงไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/FredKSchott/status/2066962296119959581" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 993 · 💬 93</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2067183015214584307">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/uNXS9jEgpg is Next.js for agents. I built Next with a simple premise: 𝚙𝚊𝚐𝚎𝚜/𝚒𝚗𝚍𝚎𝚡.𝚓𝚜 is all you need. Put some React in there and you’re good to go. Eve asks for even less. 𝚊𝚐𝚎𝚗𝚝/𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Guillermo Rauch (CEO Vercel) เปิดตัว Eve — agent framework แบบ filesystem เหมือน Next.js โดย `agent/instructions.md` คือ entry point และ `tools/*.ts` คือ tools แต่ละตัว deploy บน Vercel</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Eve เอา convention filesystem ของ Next.js มาใช้กับ agent — ไม่ต้องตั้ง orchestration ซับซ้อน แค่ไฟล์ markdown + TypeScript tools ก็พร้อมใช้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง spike Eve ใน Vercel project ที่มีอยู่ได้เลย — เพิ่ม `agent/instructions.md` และ `tools/*.ts` ไฟล์เดียวเพื่อทดสอบ pattern ก่อน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2067183015214584307" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@tlepaew</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 762 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/tlepaew/status/2067175000692674934">View @tlepaew on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“netjj and lattekim reaction to thipun nc scene is killing me😭 net: freaking out ALL THE TIME, covering jj’s eyes, 🙈🙉🙊 jj: 😁👁️👁️ kim: STOP WATCHING latte: 🫪 watch it i told you to watch, “you made the ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับเล่า reaction ของนักแสดงซีรีส์ไทย ภพเธอ ตอนสุดท้าย ไม่มีเนื้อหา tech</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/tlepaew/status/2067175000692674934" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@franmirabella</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 732 · 💬 46</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/franmirabella/status/2067027227569709459">View @franmirabella on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“No free week... No sale price... No PVE special mode... for Marathon will &quot;turn things around.&quot; The player base was set via the launch and first server slam. In PlayStation console terms, Marathon is ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิเคราะห์ชี้ Marathon ของ Bungie ยอดขายต่ำกว่าเป้า ใกล้เคียง exclusive PlayStation ระดับกลาง และ Bungie จะเจอรายได้ต่ำยาวหลายปี ต้องพึ่ง update ใหญ่ปี 2027 กับ live-service เพื่อประคองตัว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/franmirabella/status/2067027227569709459" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
