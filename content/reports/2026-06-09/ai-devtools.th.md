---
type: social-topic-report
date: '2026-06-09'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-06-09T03:04:21+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 292
salience: 0.85
sentiment: mixed
confidence: 0.62
tags:
- coding-agents
- mcp
- agent-skills
- open-models
- evals
- on-device
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2064010372621737984/img/u0c0ovEguIx46u6Q.jpg
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-06-09

## TL;DR
- workflow ของ coding-agent กำลังเปลี่ยนจาก prompt แบบครั้งเดียวไปเป็น 'skills' และ 'loops' ที่ใช้ซ้ำได้: มี directory ของ workflow สำเร็จรูปสำหรับ Cursor/Claude Code/Codex [15], skill text-to-lottie [1], รวมถึง skill repo จาก Google [29] และ OpenAI plugins [57]; ผู้สร้าง Claude Code บอกว่าตอนนี้เขา 'สร้าง loops' แทนที่จะเขียน prompt และรัน agent พร้อมกันราว ~100 ตัว ส่วนใหญ่จากโทรศัพท์ [45][47]
- MCP กำลังกลายเป็น integration layer ข้ามเครื่องมือ: Figma's MCP server รองรับใน Xcode แล้ว [27] และ OptimAI ส่ง search MCP ที่ target Claude/Cursor/Copilot/Codex พร้อมกัน [23]
- ความไม่เชื่อถือ eval กำลังเพิ่มขึ้น — METR's FrontierCode อ้างว่ากว่าครึ่งของผลลัพธ์ SWEBench merge ไม่ได้จริง [26] พร้อมกับบทความ 'AI is slowing down' [34] และการมอง xAI ว่าเป็นแค่ datacentre REIT [35]
- สัญญาณ commercial scale: Cursor รายงาน annualized revenue $4B (เพิ่มเป็น 2 เท่าใน 4 เดือน) พร้อม option ถูก SpaceX/xAI เข้าซื้อ [37][48]; OpenAI ยื่น draft S-1 แบบปิดลับ [56]
- on-device/open model ก้าวหน้า: Gemma 4 QAT ลด memory ~4x (E2B เหลือ ~1GB) สำหรับ mobile [30], MiMo-v2.5-Pro ของ Xiaomi อ้าง 1T params ที่ 1000 tok/s [25], และ Nex-N2 open-source model สำหรับ agentic coding/tool-use [13]

## สิ่งที่เกิดขึ้น
ปริมาณข่าวของวันนี้หมุนรอบ coding agent และ ecosystem รอบข้าง tooling ใหม่ได้แก่ open-source skill text-to-lottie สำหรับ Codex/Claude Code [1], directory 'loops' ของ agent workflow สำเร็จรูป [15], research-agent skill ที่ sweep Reddit/X/YouTube/HN [2][40], และ skill/plugin repo ทางการจาก Google [29] และ OpenAI [57] Claude Code ผ่านไปราว 1 ปีนับจาก GA พร้อมบทสรุปเรื่อง auto vs plan mode [5] และผู้สร้างบรรยาย workflow ที่ใช้ loops และ agent พร้อมกัน ~100 ตัว โดยบางส่วนสั่งงานจากโทรศัพท์ [45][47] คำแนะนำสำหรับ Codex เน้น outcome-based prompting และ mode 'Approve for me' [50][54] และมีคำแนะนำด้าน design ที่ให้ model agent เป็น state machine แทน loop [10]

## ทำไมถึงสำคัญ
แรงสองทิศที่ขัดกันชัดเจน ด้านหนึ่ง tooling layer กำลัง standardize: MCP แพร่เข้า first-party IDE (Figma MCP ใน Xcode [27]) และ search/context provider รวมตัวข้ามทุก agent หลักพร้อมกัน [23] ขณะที่ format 'skills' และ 'loops' [1][15][29][57] ทำให้ agent behavior พกพาและใช้ซ้ำได้แทนที่จะ bespoke ต่อ prompt ซึ่งลด switching cost และเอื้อประโยชน์ต่อผู้ที่ครอง agent surface — นั่นจึงทำให้ revenue trajectory ของ Cursor [37][48] และ S-1 ของ OpenAI [56] สำคัญในฐานะสัญญาณ consolidation อีกด้านหนึ่ง ความกดดันด้านความน่าเชื่อถือเพิ่มขึ้น: ข้ออ้างของ METR ที่ว่า >50% ของผลลัพธ์ SWEBench merge ไม่ได้ [26] ทำลายตัวเลข benchmark headline และ 'AI is slowing down' [34] บวก framing xAI-as-REIT [35] ผลักกลับต่อ narrative ด้าน capability และ capex สำหรับ studio ผลสุทธิคือ agent workflow ใช้ได้จริงแล้ว แต่ benchmark และคำอ้างของ vendor ควรลด discount ไว้ก่อน

## ความเป็นไปได้
น่าจะเกิด: format skill/loop และ MCP ยังคง consolidate เป็น integration standard ต่อเนื่อง เพราะมี adoption พร้อมกันข้าม Cursor/Claude Code/Codex/Copilot [15][23][27][29][57] เป็นไปได้: on-device/quantized open model (Gemma 4 QAT ~1GB [30], speed claims ของ MiMo [25], Nex-N2 [13]) จะมีคุณภาพพร้อมใช้สำหรับ offline mobile/edutech inference ภายในไม่กี่เดือน แม้ว่าข้ออ้าง 1000 tok/s และ 1T-param [25] ยังรอการทดสอบอิสระ เป็นไปได้: vendor consolidation รอบ Cursor และ OpenAI ดำเนินต่อ [37][48][56] ไม่น่าเกิด (ระยะใกล้): ความเชื่อถือใน benchmark ฟื้นตัวเร็ว ตราบที่บทวิจารณ์อย่าง FrontierCode [26] และบทความ slowdown [34] ยังวนเวียนอยู่ ไม่มีแหล่งใดระบุความน่าจะเป็นเป็นตัวเลข; context window GPT 5.6 'ราว 1.5M tokens' เป็นแค่ข่าวลือ [58]

## ประยุกต์กับ NDF DEV
1) ทดลอง skill text-to-lottie สำหรับ motion asset ของ UI บน Unity/web/mobile — effort ต่ำ ตรงกับ stack โดยตรง [1] 2) ปรับมาใช้ coding-agent แบบ loop/skill (outcome + exit conditions) กับงาน build ซ้ำๆ; เริ่มด้วย workflow เดียวกับ guardrail 'Approve for me' — effort ต่ำ/กลาง [15][45][47][50][54] 3) ประเมิน Gemma 4 QAT (~1GB E2B) สำหรับ on-device/offline ใน edutech และ mobile app — effort กลาง, validate คุณภาพเอง [30] 4) ถ้าส่ง iOS/macOS ให้ทดสอบ Figma MCP server ใน Xcode เพื่อย่อ design-to-code — effort ต่ำ/กลาง [27] 5) สำหรับ web/mobile UI ที่ขับเคลื่อนด้วย agent ให้ประเมิน CopilotKit/AG-UI — effort กลาง [44] 6) สำหรับ XR/CV pipeline ดู roboflow/supervision เป็น reusable vision tooling — effort กลาง [7] ข้าม: ตามข่าวลือ GPT 5.6/Cursor-SpaceX [37][48][58], noise เรื่อง macOS cursor และ eFootball [6][33][38], และการใช้ SWEBench leaderboard เป็นหลักฐานในการจัดซื้อหลังจาก [26] รัน eval เล็กๆ ของตัวเองก่อนใช้ model ใดก็ตาม

## Signals ที่ต้องจับตา
- การ adoption MCP ใน first-party IDE — ดูว่า editor อื่นจะตาม Figma MCP ใน Xcode ไหม [27]
- การยืนยันอิสระ claim 1000 tok/s / 1T-param ของ MiMo และ GPT 5.6 context ก่อนนำไปอ้างอิง [25][58]
- FrontierCode ของ METR จะกลายเป็น counter-benchmark มาตรฐานเทียบ SWEBench สำหรับการเลือกเครื่องมือหรือไม่ [26]
- on-device open model (Gemma 4 QAT, Nex-N2) ถึงคุณภาพที่ใช้ได้จริงสำหรับ offline edutech/mobile [13][30]

## Repos & Tools ที่ควรลอง
| repo | source | url |
|---|---|---|
| **mvanhorn/last30days-skill** — AI agent skill สำหรับวิจัยทุกหัวข้อข้าม Reddit, X, YouTube, HN, Polymarket และเว็บ | radar | <https://github.com/mvanhorn/last30days-skill> |
| **RyanCodrai/turbovec** — vector index ที่สร้างบน TurboQuant เขียนด้วย Rust พร้อม Python bindings | radar | <https://github.com/RyanCodrai/turbovec> |
| **roboflow/supervision** — เครื่องมือ computer vision ที่ใช้ซ้ำได้ 💜 | radar | <https://github.com/roboflow/supervision> |
| **aaif-goose/goose** — open source AI agent แบบ extensible ที่ทำได้มากกว่าแค่แนะนำ code — install, execute, edit และอื่นๆ | radar | <https://github.com/aaif-goose/goose> |
| **Panniantong/Agent-Reach** — ให้ AI agent มองเห็นอินเทอร์เน็ตทั้งหมด อ่านและค้นหาจาก Twitter, Reddit, YouTube, GitHub และอื่นๆ | radar | <https://github.com/Panniantong/Agent-Reach> |
| **refactoringhq/tolaria** — desktop app สำหรับจัดการ markdown knowledge base | radar | <https://github.com/refactoringhq/tolaria> |
| **TapXWorld/ChinaTextbook** — 所有小初高、大学PDF教材。 | radar | <https://github.com/TapXWorld/ChinaTextbook> |
| **google/skills** — Agent Skills สำหรับ Google products และ technologies | radar | <https://github.com/google/skills> |
| **CopilotKit/CopilotKit** — Frontend Stack สำหรับ Agents & Generative UI รองรับ React, Angular, Mobile, Slack และอื่นๆ | radar | <https://github.com/CopilotKit/CopilotKit> |
| **luongnv89/claude-howto** — คู่มือ visual แบบ example-driven สำหรับ Claude Code ตั้งแต่แนวคิดพื้นฐานถึง advanced agent พร้อม copy-paste | radar | <https://github.com/luongnv89/claude-howto> |
| **santifer/career-ops** — ระบบค้นหางานขับเคลื่อนด้วย AI สร้างบน Claude Code มี 14 skill mode, Go dashboard, PDF generation และอื่นๆ | radar | <https://github.com/santifer/career-ops> |
| **openai/plugins** — OpenAI Plugins | radar | <https://github.com/openai/plugins> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | konstipaulus | ^5228 c91 | [Introducing text-to-lottie: an open source skill and harness for generating prod](https://x.com/konstipaulus/status/2064011863889788972) |
| radar | mvanhorn_last30days-skill | ^3558 c0 | [mvanhorn/last30days-skill AI agent skill that researches any topic across Reddit](https://github.com/mvanhorn/last30days-skill) |
| x | AnthropicAI | ^2210 c185 | [New Science Blog: Why has AI advanced faster in coding than in biology? To agent](https://x.com/AnthropicAI/status/2064054837294354677) |
| radar | RyanCodrai_turbovec | ^1729 c0 | [RyanCodrai/turbovec A vector index built on TurboQuant, written in Rust with Pyt](https://github.com/RyanCodrai/turbovec) |
| x | bcherny | ^1557 c98 | [When we first demoed Claude Code internally, it got two reactions on Slack. A ye](https://x.com/bcherny/status/2064034799711588805) |
| x | 1000kilobytes | ^1370 c27 | [THE BUTLER CURSOR IS BACK IN MACOS 27 https://t.co/MJ7ubLbQNG](https://x.com/1000kilobytes/status/2064069798846505034) |
| radar | roboflow_supervision | ^1288 c0 | [roboflow/supervision We write your reusable computer vision tools. 💜](https://github.com/roboflow/supervision) |
| x | edzitron | ^1244 c14 | [Fun watching the mainstream media repeat things I've said for months like they'r](https://x.com/edzitron/status/2064023464022073567) |
| x | schizothotep | ^1198 c12 | [CHALLENGE FOR YOU, LOGAN GRIMNAR, IF YOU READ ONE FULL PAGE OF CODEX ASTARTES, 𝓕](https://x.com/schizothotep/status/2064014968488329280) |
| x | dzhng | ^1037 c61 | [don't use loops, design state machines https://t.co/xQ1Ir6KlcJ](https://x.com/dzhng/status/2063931263312892406) |
| x | hosseeb | ^1001 c129 | [OK, so I became one of those people: Claude diagnosed my sleep disorder. Here's ](https://x.com/hosseeb/status/2064042451850121632) |
| hackernews | lizhang | ^808 c159 | [Show HN: Performative-UI – A react component library of design tropes hope you e](https://vorpus.github.io/performativeUI/) |
| x | ModelScope2022 | ^731 c25 | [Nex-N2 is now open source！An agentic model series from Nex AGI built for coding,](https://x.com/ModelScope2022/status/2063881896153543022) |
| radar | aaif-goose_goose | ^699 c0 | [aaif-goose/goose an open source, extensible AI agent that goes beyond code sugge](https://github.com/aaif-goose/goose) |
| x | elorm_elom | ^698 c32 | [introducing loops! a directory of pre-built agent workflows for Cursor, Claude C](https://x.com/elorm_elom/status/2064005518343995588) |
| x | thsottiaux | ^683 c105 | [@YashHustle_22 Codex at breakfast Codex in the morning Codex at lunch Codex in t](https://x.com/thsottiaux/status/2064039257392709683) |
| radar | Panniantong_Agent-Reach | ^679 c0 | [Panniantong/Agent-Reach Give your AI agent eyes to see the entire internet. Read](https://github.com/Panniantong/Agent-Reach) |
| radar | refactoringhq_tolaria | ^651 c0 | [refactoringhq/tolaria Desktop app to manage markdown knowledge bases](https://github.com/refactoringhq/tolaria) |
| radar | TapXWorld_ChinaTextbook | ^592 c0 | [TapXWorld/ChinaTextbook 所有小初高、大学PDF教材。](https://github.com/TapXWorld/ChinaTextbook) |
| hackernews | bobbiechen | ^589 c238 | [Stop the Apple Music app from launching](https://lowtechguys.com/musicdecoy/) |
| x | skirano | ^584 c29 | [Today we're introducing Builder, a new MagicPath plan for people working with Co](https://x.com/skirano/status/2064035120483352776) |
| hackernews | 1vuio0pswjnm7 | ^565 c418 | [Anti-social: It's fads, not friends, which now dominate social media feeds](https://www.bbc.com/worklife/article/20260520-how-social-media-ceased-to-be-social) |
| x | OptimaiNetwork | ^562 c88 | [OptimAI Search MCP brings live context to the agents people already use. Claude.](https://x.com/OptimaiNetwork/status/2064012781658009804) |
| x | ThePrimeagen | ^509 c27 | [I have to push back on 2 things as i think one is categorically incorrect and th](https://x.com/ThePrimeagen/status/2064142254579826716) |
| hackernews | gainsurier | ^506 c356 | [MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) |
| x | swyx | ^490 c58 | [It's finally out!!! @METR_Evals found that more than half of SWEBench results is](https://x.com/swyx/status/2064081945567580323) |
| x | figma | ^486 c10 | [The Figma MCP Server is now supported in Xcode #WWDC https://t.co/WDy9qFtkd8](https://x.com/figma/status/2064120455808888873) |
| x | amasad | ^479 c20 | [@REM__BEN From his perspective, it's stationary; from the perspective of someone](https://x.com/amasad/status/2063667850531999921) |
| radar | google_skills | ^461 c0 | [google/skills Agent Skills for Google products and technologies](https://github.com/google/skills) |
| x | _philschmid | ^454 c17 | [More Gemma 4! New QAT Gemma 4 checkpoints with similar performance while using ~](https://x.com/_philschmid/status/2063990553826439378) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@konstipaulus</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5228 · 💬 91</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/konstipaulus/status/2064011863889788972">View @konstipaulus on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing text-to-lottie: an open source skill and harness for generating production ready Lottie animations with codex/claude code. $ npx skills add diffusionstudio/lottie Prompts guide and repo in”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>diffusionstudio ปล่อย text-to-lottie เป็น open-source skill สำหรับ Claude Code ที่สร้าง Lottie animation พร้อม production จาก text prompt ติดตั้งผ่าน `npx skills add diffusionstudio/lottie`</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Lottie ใช้ทั่วไปใน e-learning และ mobile UI การ generate จาก prompt ตัด handoff ระหว่าง designer กับ developer ออกได้เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตั้ง skill นี้ใน Claude Code ของ studio แล้วทดลองใช้กับ animation ใน e-learning หรือ mobile app</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/konstipaulus/status/2064011863889788972" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnthropicAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2210 · 💬 185</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnthropicAI/status/2064054837294354677">View @AnthropicAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New Science Blog: Why has AI advanced faster in coding than in biology? To agents, bio databases are like cities built before cars—maddening to drive in because they're designed for different traffic.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Anthropic เผย blog วิเคราะห์ว่า AI ทำงานกับ code ได้ดีกว่า biology เพราะ infrastructure ของ code (APIs, CLIs, version control) ถูกออกแบบให้ machine อ่านได้ตั้งแต่แรก ต่างจาก bio database ที่ออกแบบมาสำหรับมนุษย์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>หลักการเดียวกันใช้กับ legacy data system ที่ agent ของ studio ต้องใช้ — ถ้าข้อมูลไม่ได้ออกแบบให้ machine อ่าน agent จะทำงานได้แค่ระดับนึงเท่านั้น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอนสร้าง internal tools หรือ pipeline สำหรับ agent ออกแบบ data schema และ API ให้ machine อ่านได้ตั้งแต่ต้น ไม่ใช่ค่อยมาแก้ทีหลัง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AnthropicAI/status/2064054837294354677" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bcherny</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1557 · 💬 98</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bcherny/status/2064034799711588805">View @bcherny on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“When we first demoed Claude Code internally, it got two reactions on Slack. A year after GA, @_catwu and I sat down to talk about what's changed: why I use auto mode instead of plan mode, how routines”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@bcherny ผู้สร้าง Claude Code แชร์ retrospective ครบ 1 ปีหลัง GA: auto mode ดีกว่า plan mode ในการใช้งานจริง, routines จัดการ bug ก่อนที่เขาจะเห็น, และ code จาก phone เป็นหลัก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Pattern 'routines จัดการ bug ก่อนเจอ' ยืนยันว่า scheduled agents ทำงานเป็น proactive quality layer ได้จริง ไม่ใช่แค่ demo feature</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมเซ็ต Claude Code routines รัน nightly checks บน active projects เพื่อจับ regression ก่อน standup ตอนเช้า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bcherny/status/2064034799711588805" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@1000kilobytes</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1370 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/1000kilobytes/status/2064069798846505034">View @1000kilobytes on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“THE BUTLER CURSOR IS BACK IN MACOS 27 https://t.co/MJ7ubLbQNG”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>macOS 27 นำ Butler Cursor กลับมา ซึ่งเป็น cursor feature ที่ถูกตัดออกไปก่อนหน้านี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/1000kilobytes/status/2064069798846505034" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@edzitron</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1244 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/edzitron/status/2064023464022073567">View @edzitron on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fun watching the mainstream media repeat things I’ve said for months like they’re brand new thoughts down to the GitHub copilot stuff lol”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@edzitron บ่นว่า mainstream media เอา take เรื่อง AI devtools และ GitHub Copilot ที่เขาพูดไปนานแล้วมานำเสนอใหม่เหมือนเป็นเรื่องสด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/edzitron/status/2064023464022073567" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@schizothotep</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1198 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/schizothotep/status/2064014968488329280">View @schizothotep on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“CHALLENGE FOR YOU, LOGAN GRIMNAR, IF YOU READ ONE FULL PAGE OF CODEX ASTARTES, 𝓕𝓤𝓡𝓡𝓨, I'LL GIVE A THOUSAND PSYKERS TO THE GOLDEN THRONE https://t.co/ZMHmeJHSV0”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์มีม Warhammer 40K ท้าตัวละครสมมติ ไม่มีเนื้อหาด้านเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/schizothotep/status/2064014968488329280" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@dzhng</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1037 · 💬 61</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/dzhng/status/2063931263312892406">View @dzhng on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“don't use loops, design state machines https://t.co/xQ1Ir6KlcJ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@dzhng ผู้สร้าง Agentic framework แนะว่า AI agent workflow ควรออกแบบเป็น state machine แทน loop — ดีกว่าในแง่ debug, resume, และความชัดเจนของ flow</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>State machine ทำให้รู้ว่า agent หยุดตรงไหนเมื่อ fail — loop ธรรมดาไม่บอกอะไร แต่ named state บอกจุดที่พังได้ทันที</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใน AI agent pipeline ของ studio ให้กำหนด state ชัดๆ (idle, planning, executing, retrying, done) แทนการ wrap LLM call ไว้ใน while loop</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/dzhng/status/2063931263312892406" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@hosseeb</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1001 · 💬 129</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/hosseeb/status/2064042451850121632">View @hosseeb on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“OK, so I became one of those people: Claude diagnosed my sleep disorder. Here's the story. I'd been sleeping worse and worse since hitting my mid-30s. I've been averaging 5:30-5:45 a night for a coupl”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้เขียนเล่าประสบการณ์นอนหลับน้อยเรื้อรังและใช้ Oura ring ติดตามผล แต่โพสต์ถูกตัดก่อนถึงส่วนที่ Claude วินิจฉัยจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/hosseeb/status/2064042451850121632" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
