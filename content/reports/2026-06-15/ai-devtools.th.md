---
type: social-topic-report
date: '2026-06-15'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-06-15T04:19:52+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- lobsters
- radar
- x
regions:
- global
post_count: 268
salience: 0.7
sentiment: mixed
confidence: 0.5
tags:
- coding-agents
- agent-skills
- local-llm
- open-weights
- devtools-security
- codex-claude-code
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2066172758736707584/img/Vqk45kTU-Km_Z0vE.jpg
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-06-15

## TL;DR
- หลายโพสต์อ้างว่า AMD Ryzen AI Max+ 395 mini PC รัน model 235B parameters ได้บนเครื่องราคา ~$1,499 โดยค่าไฟ ~$9/เดือน พร้อมเสนอว่าทดแทน sub Claude/OpenAI $200/เดือนได้ [1][24][37]; การนำเสนอแบบนี้คือ engagement-bait และ model ที่ใช้แทบแน่นอนว่าเป็น MoE ที่ quantize หนัก แต่ความสามารถ local-inference คือสัญญาณที่น่าจับตา [13]
- Coding agents กำลังเปลี่ยนจากการรับ prompt ไปสู่การกำหนดทิศทางตัวเอง: Codex เขียน /goal ให้ตัวเองและ sub-agents ที่ spawn ได้แล้ว [5][7] และผู้สร้าง Claude Code ระบุว่า 100% ของ PR และ 80–90% ของ code review ที่ Anthropic ผ่าน Claude Code โดยมี /loops เป็น workflow หลัก [8]
- agent skills สำหรับงาน game/XR เปิด source แล้ว ได้แก่ agent แปลง image → sprite-sheet 2D animation พร้อมใช้งานกับ Codex [34], skill 'game director' สำหรับ Three.js [45] และ skill แปลง codebase → architecture diagram [15]
- Open-weight coding models กำลังไล่ตาม frontier models อย่างรวดเร็ว — 'Fable-5/Composer-2.5' แบบ distilled รันบน 8GB VRAM ได้ 20+ tok/s ภายในไม่กี่วันหลัง launch [32] รวมถึง GLM 5.2 [40] และ Kimi K2.7 [35] ที่มีพัฒนาการต่อเนื่อง
- supply chain ของ agent skill กลายเป็น security surface แล้ว: NVIDIA ปล่อย SkillSpector สำหรับสแกน AI agent skills หาพฤติกรรมอันตราย [14] ขณะที่ setup router 'free Claude Code' แพร่กระจายอยู่ [10][41][56] และระบบนิเวศ skill รายงานว่าผ่าน 700,000 skills แล้ว [59]

## What happened
บทสนทนาด้าน AI devtools วันนี้แบ่งเป็นสี่กลุ่ม ฝั่ง Hardware: thread ของ influencer อ้างว่า AMD Ryzen AI Max+ 395 รัน model 235B ได้บนเครื่อง ~$1,499 ค่าไฟ ~$9/เดือน โดยชูว่าทำลาย cloud coding sub ได้ [1][24][37] พร้อม llama.cpp consumer-GPU guide แบบลงมือทำ [13] และรายงาน distilled coder models ที่รันบน 8GB VRAM ได้ 20+ tok/s [32] ฝั่ง Agents: Codex กำหนด /goal ให้ตัวเองได้ในฐานะการขยาย meta-prompting [5][7] และผู้สร้าง Claude Code รายงานว่าทีม Anthropic พึ่งพาเครื่องมือนี้เกือบทั้งหมดโดยใช้ /loops เป็น interface หลัก [8] ฝั่ง Skills/ecosystem: agent skills open-source มุ่งเป้า game และ studio workflows — sprite-sheet animation [34], Three.js game direction [45], architecture diagram [15], Codex-as-VFX [22] — และ skill catalog เปิดรายงานว่าผ่าน 700,000 แล้ว [52][59]

## Why it matters (reasoning)
มีสองการเปลี่ยนแปลงที่สำคัญสำหรับ studio ประการแรก จุดที่สร้าง leverage กำลังเคลื่อนจาก prompt แต่ละครั้งไปสู่ harnesses และ skills ที่ใช้ซ้ำได้: self-goaling agents [5][7] และ /loops [8] หมายความว่า output ขึ้นอยู่กับคุณภาพของ skill/context library ไม่ใช่ความแม่นยำของ prompt แต่ละครั้ง [52] ทีมที่ลงทุนสร้าง skill repo จะได้เปรียบกว่าทีมที่แค่คุยกับ model [12] ประการที่สอง local inference ที่ถูกลง [1][13][32] บวกกับ open weights ที่พัฒนาเร็ว (GLM 5.2 [40], Kimi K2.7 [35]) กดต้นทุนลงและลดการผูกติดกับ paid API เจ้าใดเจ้าหนึ่ง ต้นทุนลำดับที่สองคือ security: ระบบนิเวศ 700k skills [59] และ router 'free Claude Code' ที่แพร่กระจาย [10][41][56] คือ supply-chain และ credential-abuse vector ที่ชัดเจน ซึ่งเป็นเหตุผลที่ SkillSpector ถือกำเนิด [14] มุมมองเชิงวิพากษ์: framing 'AMD $9/เดือนสังหาร cloud' [1][24] คือการตลาด — throughput, context limits และคุณภาพ quantization ไม่มีการระบุ และสไตล์ tweet ตัวพิมพ์ใหญ่บอกว่านี่คือ hype ไม่ใช่ benchmark

## Possibility
เป็นไปได้สูง: agent-skill libraries จะกลายเป็น unit หลักของ devtool value เพราะทั้ง Codex และ Claude Code กำลังรวมศูนย์สู่ workflow แบบ self-directed ที่ขับเคลื่อนด้วย skill [5][7][8][52] เป็นไปได้สูง: open-weight coders จะยังไล่ตาม frontier models ทันภายในไม่กี่วันหลัง release แต่ละครั้ง ตามความเร็วของ distillation [32][58] และพัฒนาการต่อเนื่องของ GLM/Kimi [35][40] เป็นไปได้: studio จะรัน coding/inference ส่วนหนึ่งบน hardware ในบ้านอย่าง Ryzen AI Max+ 395 เพื่อต้นทุนและการทำงาน offline [1][13][24] แม้คุณภาพจริงที่ context ใช้งานได้ยังพิสูจน์ไม่ได้ เป็นไปได้: เหตุการณ์ด้าน security จาก third-party skill อันตรายจะผลักดันให้ใช้ scanner กันกว้างขึ้น [14] ไม่น่าเกิด (ระยะใกล้): setup router 'free Claude Code' [10][41][56] จะเสถียรหรือใช้พึ่งพาได้จริง — อ่านแล้วดูเหมือนละเมิด ToS หรือเสี่ยง abuse

## Org applicability — NDF DEV
แนวทางลงมือจริง: (1) ทดลอง agent 2D sprite-sheet animation open-source กับ Unity 2D asset pipeline — effort ต่ำ, open-source [34] (2) ทดลอง skill Three.js game-director กับ WebGL/browser game prototype และ edutech mini-game — ต่ำ/กลาง [45] (3) สร้าง shared skill.md / agent-skill repo ให้ทีม ให้ output ของ Codex/Claude Code ทำซ้ำได้ทุกคน — ต่ำ/กลาง [5][7][8][52] (4) ก่อนติดตั้ง third-party agent skill ใดก็ตาม ให้รัน SkillSpector หรือ tool เทียบเท่า — effort ต่ำ และควรทำเป็น hard rule เพราะ surface 700k skills [14][59] (5) ประเมิน spec (อย่าซื้อตาม hype) ของ local-inference box สำหรับ coding ราคาถูก/offline และ on-device edutech demo โดยต้องยืนยัน tok/s จริง, context และคุณภาพ model ก่อน — กลาง [1][13][24][37] (6) ติดตาม GLM 5.2 และ Kimi K2.7 เป็น option coding model ราคาถูกสำหรับงานไม่ critical — ต่ำ [35][40] ข้าม: router 'free Claude Code' [10][41][56] (เสี่ยง security/ToS), framing AMD-kills-cloud เป็นข้อเท็จจริง [1][24] และ Fable-5 trace dump ที่ scrape มา [58] (เสี่ยงทางกฎหมายและคุณภาพ)

## Signals to Watch
- Self-goaling agents (Codex /goal, Claude /loops) — การเปลี่ยนผ่านจากการ prompt ไปสู่การสร้าง harness [5][7][8]
- Open-weight coders ที่ไล่ทัน frontier models ภายในไม่กี่วันหลัง launch [32][58]
- Security ของ agent-skill supply-chain: การสแกนด้วย SkillSpector เทียบกับ setup router 'free' [14][41][56]
- Local inference ระดับ 235B บน hardware ~$1.5k — ยืนยัน throughput/context ก่อนเชื่อ framing [1][13][37]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **iptv-org/iptv** — รวม IPTV channels สาธารณะจากทั่วโลก | radar | <https://github.com/iptv-org/iptv> |
| **NVIDIA/SkillSpector** — Security scanner สำหรับ AI agent skills ตรวจหา vulnerabilities, malicious patterns และ security risks | radar | <https://github.com/NVIDIA/SkillSpector> |
| **tamnd/kage** — Show HN: Kage – Shadow เว็บไซต์ใดก็ได้เป็น single binary เพื่อดู offline | hackernews | <https://github.com/tamnd/kage> |
| **chatwoot/chatwoot** — open-source live-chat, email support, omni-channel desk ทางเลือกแทน Intercom, Zendesk, Salesforce | radar | <https://github.com/chatwoot/chatwoot> |
| **nex-agi/Nex-N2** — LLM "ในบ้าน" ของ Rio de Janeiro ที่ดูเหมือนเป็น merge ของ model ที่มีอยู่แล้ว | hackernews | <https://github.com/nex-agi/Nex-N2> |
| **Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots** — Introduction to Autonomous Robots | radar | <https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots> |
| **andrewyng/aisuite** — interface เดียวรวม Generative AI providers หลายเจ้า | radar | <https://github.com/andrewyng/aisuite> |
| **GorvGoyl/Clone-Wars** — open-source clones 100+ ของเว็บดัง เช่น Airbnb, Amazon, Instagram, Netflix, Tiktok, Spotify | radar | <https://github.com/GorvGoyl/Clone-Wars> |
| **shiyu-coder/Kronos** — Kronos: Foundation Model สำหรับภาษาของตลาดการเงิน | radar | <https://github.com/shiyu-coder/Kronos> |
| **music-assistant/server** — Music Assistant คือ Media library manager open-source ฟรีที่เชื่อมต่อกับ streaming services | radar | <https://github.com/music-assistant/server> |
| **swc-project/swc** — platform ฝั่ง Web ที่เขียนด้วย Rust | radar | <https://github.com/swc-project/swc> |
| **freeCodeCamp/freeCodeCamp** — codebase และหลักสูตร open-source ของ freeCodeCamp.org เรียนคณิตศาสตร์ programming และ computer science | radar | <https://github.com/freeCodeCamp/freeCodeCamp> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | adiix_official | ^8775 c456 | [AMD CEO Lisa Su just killed Nvidia's $4,000 AI box with a $1,499 lunchbox. She w](https://x.com/adiix_official/status/2066172819952566643) |
| x | theo | ^4305 c74 | [Oliver Tree will be mostly remembered for memes. I hope we don't forget that he ](https://x.com/theo/status/2066241450338295893) |
| x | amasad | ^2719 c76 | [This is the most inspiring positive-sum vision for AI in the enterprise.](https://x.com/amasad/status/2066195933969412098) |
| x | amasad | ^2413 c136 | [Feels like we're getting psyoped. The end-game here is something bigger.](https://x.com/amasad/status/2065838585358745653) |
| x | thsottiaux | ^1765 c126 | [Codex can see and set its own /goal. Everything we build, we build also as a too](https://x.com/thsottiaux/status/2066270561081454989) |
| x | simonw | ^1729 c86 | [I'm just glad nobody at the US government thought to try that Fable 5 "jailbreak](https://x.com/simonw/status/2066147375119556735) |
| x | skirano | ^1646 c93 | [I basically never write my own /goal anymore. I ask Codex to write one for itsel](https://x.com/skirano/status/2066225908202053818) |
| x | 0xMovez | ^1580 c43 | [Claude Code creator: "100% of our pull requests at Anrtopic are run by Claude Co](https://x.com/0xMovez/status/2066225922928181644) |
| radar | iptv-org_iptv | ^1528 c0 | [iptv-org/iptv Collection of publicly available IPTV channels from all over the w](https://github.com/iptv-org/iptv) |
| x | khushiirl | ^1241 c39 | [IT WORKED. I'm in love with free open claude code https://t.co/UDZ9qe2zqh](https://x.com/khushiirl/status/2066166949026160958) |
| x | rauchg | ^1048 c35 | [If you don't love her at her foggiest, you don't deserve at her sunniest https:/](https://x.com/rauchg/status/2065856253428179357) |
| x | rauchg | ^997 c104 | [There seem to be two main groups 1️⃣ Those who post all day long about using cod](https://x.com/rauchg/status/2066246159140798859) |
| x | TraffAlex | ^965 c38 | [🖥️ Best Local LLMs for Consumer GPUs — llama.cpp Guide (June 2026) What I actual](https://x.com/TraffAlex/status/2066236717015728227) |
| radar | NVIDIA_SkillSpector | ^964 c0 | [NVIDIA/SkillSpector Security scanner for AI agent skills. Detect vulnerabilities](https://github.com/NVIDIA/SkillSpector) |
| x | DataChaz | ^895 c19 | [MANUALLY DRAGGING BOXES FOR ARCHITECTURE DIAGRAMS IS FINALLY DEAD There is a new](https://x.com/DataChaz/status/2065735103163363427) |
| x | theo | ^812 c79 | [You guys will believe literally anything](https://x.com/theo/status/2066329392549335468) |
| x | rauchg | ^714 c40 | [My flight to London is Starlink-enabled 😭 The greatest advancement to air travel](https://x.com/rauchg/status/2066315273947500699) |
| x | boringmarketer | ^702 c40 | [if you want Fable level performance NOW, the answer is to build your own coding ](https://x.com/boringmarketer/status/2066185785204719769) |
| x | antoniogm | ^693 c95 | [You can finally say this without being canceled: AI isn't creating a Cambrian ex](https://x.com/antoniogm/status/2066234772519874569) |
| x | jeremyberman | ^692 c53 | [GPT 5.5 Pro is the best model for planning and research. Why isn't it available ](https://x.com/jeremyberman/status/2066223027151315200) |
| x | StockSavvyShay | ^662 c82 | [$MSFT 10 years ago: • $50/share (split-adjusted basis) • 21x earnings • Written ](https://x.com/StockSavvyShay/status/2066181893360611651) |
| x | EHuanglu | ^632 c19 | [hire codex as 3d vfx artist and work 24/7 https://t.co/Ts4S3bkOEo](https://x.com/EHuanglu/status/2066216538433294477) |
| x | chainlink | ^522 c27 | [With Chainlink, building an onchain @FIFAWorldCup prediction market is only a si](https://x.com/chainlink/status/2065956152609783836) |
| x | antisadh | ^503 c27 | [AN AMD ENGINEER SHIPS A PALM-SIZED MINI PC THAT RUNS 235B MODELS FOR $9/MONTH AN](https://x.com/antisadh/status/2066115131457888600) |
| hackernews | kingstoned | ^500 c1487 | [How to earn a billion dollars](https://paulgraham.com/earn.html) |
| x | yukichung96 | ^455 c4 | [✦Lucia: Inverse Crown / Cursors ✦ I designed my Vol. 2 PGR custom cursor set! 🥰 ](https://x.com/yukichung96/status/2066148495145554058) |
| hackernews | tamnd | ^452 c99 | [Show HN: Kage – Shadow any website to a single binary for offline viewing](https://github.com/tamnd/kage) |
| hackernews | yegg | ^441 c478 | [Not everyone is using AI for everything](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they) |
| x | jerryjliu0 | ^433 c15 | [My mayor Muslim My bagel's Jewish The US government took away my AI Knicks in fi](https://x.com/jerryjliu0/status/2065666222646288824) |
| x | prisma | ^417 c10 | [Bun's @rustlang rewrite now helps power Prisma Compute in production. On stable ](https://x.com/prisma/status/2065982990178828347) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@adiix_official</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 8775 · 💬 456</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/adiix_official/status/2066172819952566643">View @adiix_official on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“AMD CEO Lisa Su just killed Nvidia’s $4,000 AI box with a $1,499 lunchbox. She walked on stage, held it in one hand, and ran a 235 billion parameter model live. No data center. No cloud. No rented GPU”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>AMD Ryzen AI Max+ 395 ใช้ unified memory 128GB ร่วม CPU/GPU รัน model 235B parameters บนเครื่อง $1,499 — เร็วกว่า RTX 5080 ถึง 3x บน DeepSeek R1 inference</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>128GB shared VRAM สูงสุดในตลาด consumer ตอนนี้ — studio เล็กรัน open-source model ขนาดใหญ่ได้เองโดยไม่ต้องพึ่ง cloud หรือจ่าย subscription</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง price out AMD Ryzen AI Max+ 395 เป็น local inference server กลาง studio แทนหรือลดค่า AI subscription รายเดือนของทีม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/adiix_official/status/2066172819952566643" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4305 · 💬 74</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2066241450338295893">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Oliver Tree will be mostly remembered for memes. I hope we don't forget that he was a genuinely great artist too. Feels like a good time to share his debut track &quot;Forget It&quot; (w/ Getter). RIP Oliver. Y”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Theo โพสต์ไว้อาลัย Oliver Tree นักดนตรีที่เพิ่งเสียชีวิต พร้อมแชร์เพลง debut ของเขา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2066241450338295893" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amasad</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2719 · 💬 76</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amasad/status/2066195933969412098">View @amasad on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is the most inspiring positive-sum vision for AI in the enterprise.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@amasad โพสต์ความเห็นหนึ่งประโยคว่ามีบาง 'vision' น่าประทับใจ — ไม่บอกว่าคืออะไร ไม่มี link ไม่มีรายละเอียด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amasad/status/2066195933969412098" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amasad</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2413 · 💬 136</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amasad/status/2065838585358745653">View @amasad on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Feels like we’re getting psyoped. The end-game here is something bigger.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@amasad (CEO Replit) โพสต์ความเห็นคลุมเครือว่าวงการ AI devtools กำลังมุ่งไปสู่เป้าหมายที่ใหญ่กว่าที่เห็น โดยไม่ระบุรายละเอียด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amasad/status/2065838585358745653" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@thsottiaux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1765 · 💬 126</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/thsottiaux/status/2066270561081454989">View @thsottiaux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Codex can see and set its own /goal. Everything we build, we build also as a tool for the agent. This is a generalization of meta prompting, where you let the agent set its own task based on your inte”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Codex รองรับ /goal command ที่ให้ agent อ่านและกำหนด objective ของตัวเองได้ ขยายแนวคิด meta-prompting ให้ agent แตก subtask จาก intent ของ user แทนการรับคำสั่งตรงๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Agent กำหนด goal เองได้ ลด overhead ในการ prompt engineer ตอนมอบ task หลายขั้นตอนให้ AI</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ /goal ใน Codex กับ task ภายในที่กำหนดขอบเขตชัด แล้วเทียบว่า agent แตก subtask เองได้ดีกว่า prompt manual แค่ไหน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/thsottiaux/status/2066270561081454989" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@simonw</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1729 · 💬 86</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/simonw/status/2066147375119556735">View @simonw on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm just glad nobody at the US government thought to try that Fable 5 &quot;jailbreak&quot; against Opus 4.x or GPT 5.x, or I wouldn't be getting anything useful done this weekend at all”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Simon Willison โพสต์แนว sarcasm ว่าโชคดีที่รัฐบาลสหรัฐฯ ไม่เอา jailbreak จากเกม Fable 5 ไปลองกับ Opus 4.x หรือ GPT-5</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/simonw/status/2066147375119556735" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@skirano</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1646 · 💬 93</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/skirano/status/2066225908202053818">View @skirano on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I basically never write my own /goal anymore. I ask Codex to write one for itself, and one for each agent it spawns. Like this 👇 https://t.co/8ykoPJNLmC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Pietro Schirano หยุดเขียน /goal เอง แล้วให้ Codex generate goal ให้ตัวเองและ sub-agent แต่ละตัวแทน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การให้ agent generate /goal เองช่วยให้แต่ละตัวมี scope ชัดเจน ลด context drift ใน multi-agent pipeline</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใน agentic workflow ให้ orchestrator generate /goal ให้ตัวเองและ child agent แต่ละตัว แทนการ hardcode</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/skirano/status/2066225908202053818" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@0xMovez</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1580 · 💬 43</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/0xMovez/status/2066225922928181644">View @0xMovez on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Claude Code creator: &quot;100% of our pull requests at Anrtopic are run by Claude Code. 80–90% of code review too. The feature I’m using the most today is /loops. I’m not prompting Claude anymore - I’m bu”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Boris Cherny (ผู้สร้าง Claude Code) เผยว่า 100% ของ PR และ 80–90% ของ code review ที่ Anthropic ใช้ Claude Code แล้ว และ feature ที่ใช้บ่อยสุดคือ /loop — เขา build loops แทนการ prompt</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การเปลี่ยนจาก one-shot prompt เป็น /loop automation เป็น pattern ที่ช่วย compound output ของ Claude Code สำหรับทีมเล็กที่ทำ review cycle ซ้ำๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมลอง /loop ใน Claude Code เพื่อ automate code review, lint หรือ test run แทนการ prompt ซ้ำทุกรอบ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/0xMovez/status/2066225922928181644" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
