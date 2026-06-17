---
type: social-topic-report
date: '2026-06-17'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-06-17T15:05:15+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- hackernews
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 197
salience: 0.82
sentiment: mixed
confidence: 0.6
tags:
- ai-devtools
- coding-agents
- open-weights-llm
- mcp
- vercel
- cursor
thumbnail: https://pbs.twimg.com/media/HK80XzjbQAA2TsL.jpg
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-06-17

## TL;DR
- GLM-5.2 (open weights) รายงานว่าทำคะแนนเกิน 80% บน Terminal-Bench และขึ้นนำ Artificial Analysis open-weights index โดยอ้างว่าเหนือกว่า Gemini และ Opus 4.x ในราคาประมาณหนึ่งในสิบ [11][27][43][34]
- Vercel เปิดตัว 'eve' ซึ่งเป็น agent framework แบบ file-convention พร้อม 'Agent Stack' (AI SDK, AI Gateway, Workflow SDK, Sandbox, Chat SDK, Vercel Connect) รองรับการรัน function นาน 30 นาทีและ sandbox อายุ 24 ชั่วโมง [1][46][60][59]
- Tomas Reimers จาก Cursor/Graphite ประกาศ 'Origin' ซึ่งเป็นทางเลือกแทน Git สำหรับ agent workloads พร้อม MCP/API extensibility และจัดการ merge conflict ในตัว [3]; ขณะเดียวกัน Reuters รายงานดีล SpaceX–Anysphere (Cursor) มูลค่า $60B [10]
- Figma MCP server ขยายความสามารถให้สร้าง/แก้ Figma Slides, สร้าง FigJam data boards, และทำ roundtrip code-to-canvas พร้อมรองรับ custom fonts และ image export [16]
- Repos ประเภท agent 'skills' กำลังมาแรง: agent-skills (60,800+ stars), obra/superpowers, mattpocock/skills [23][9][6]; code-graph MCP servers (Gortex, codebase-memory-mcp) อ้างว่าลด token ได้มากสำหรับ coding agents [50][33]

## What happened
สัญญาณ AI devtools วันนี้รวมตัวอยู่รอบสามเรื่อง แรกสุดคือแรงส่งของ open-weights: หลาย item รายงาน GLM-5.2 นำ Artificial Analysis open-weights index, ทำคะแนนเกิน 80% บน Terminal-Bench และถูกวางตำแหน่งสู้กับ Gemini กับ Opus 4.x ในราคาประมาณหนึ่งในสิบ [11][27][43][34]; โพสต์แยกโต้แย้งว่า local models ตอนนี้ดีพอสำหรับงานจริงแล้ว [8] สองคือ agent tooling จาก Vercel: agent framework 'eve' ที่จำลองแบบ file convention ของ Next.js [1][13], 'Agent Stack' ที่รวม AI SDK, AI Gateway, Workflow SDK, Sandbox, Chat SDK และ Vercel Connect [46], scoped short-lived tokens ผ่าน Vercel Connect [59][32], และ execution limits ที่ยาวขึ้น (functions 30 นาที, sandboxes 24 ชั่วโมง) [60] สามคือ infrastructure รอบ coding agents: 'Origin' ทางเลือกแทน Git ของ Cursor/Graphite ที่สร้างสำหรับ agent workloads [3] บวกกับข่าวลือ SpaceX เข้าซื้อ Anysphere ผู้สร้าง Cursor มูลค่า $60B [10]

## Why it matters (reasoning)
แรงกดด้านราคาเป็นเรื่องที่นำไปใช้งานได้ทันทีที่สุด: ถ้าการอ้างสิทธิ์ open-weights ของ GLM-5.2 เป็นจริง studio สามารถรัน coding/agent models ที่มีความสามารถแบบ self-hosted หรือผ่าน inference ราคาถูกกว่า ลดการพึ่งพาผู้ให้บริการ closed เพียงรายเดียว [11][27][43] ยิ่งสำคัญขึ้นเมื่อ vendor มีความไม่แน่นอน — ข่าวลือการซื้อ Cursor มูลค่า $60B [10] และการปิดตัวของ Fable [4][37][49] แสดงให้เห็นว่า tool หรือ model ที่ standardize ไว้อาจเปลี่ยนมือหรือหายไปได้รวดเร็วแค่ไหน Second-order: การรวมตัวของ MCP ในฐานะ integration layer (Figma [16], Lovable [48], Gortex/codebase-memory [50][33], cybersecurity tooling [56]) หมายความว่าการลงทุนใน MCP-based workflows กำลังกลายเป็น portable ข้ามระหว่าง editors และ agents แทนที่จะผูกกับ IDE เดียว ประเด็นซ้ำๆ เรื่อง 'ส่วนที่ยากคือ data/OAuth/tokens/scopes' [32] และ code-graph token-reduction tools [50][33] ต่างส่งสัญญาณว่าต้นทุนและ plumbing ไม่ใช่ raw model capability คือคอขวดการใช้งานจริงตอนนี้

## Possibility
มีแนวโน้มสูง: open-weights models จะยังปิดช่องว่างกับ closed frontier models บน coding benchmarks ต่อเนื่อง ทำให้ multi-model setups (closed + open fallback) กลายเป็นมาตรฐาน — หลาย item อิสระรายงาน GLM-5.2 ที่ระดับเดียวกับหรือเหนือกว่า closed models แล้ว [11][27][34][43] น่าจะเกิดขึ้น: MCP รวมตัวเป็น agent-integration standard เริ่มต้นข้าม editors และ design tools เมื่อดูจำนวน vendor ที่ส่ง MCP รอบนี้ [16][48][50][33][56] น่าจะเกิดขึ้นแต่ยังไม่ยืนยัน: ดีล SpaceX–Cursor [10] เป็นพาดหัวเดียว Reuters-style ไม่มี item อื่นยืนยัน ถือเป็นข่าวลือจนกว่าจะมีการยืนยัน ไม่น่าเกิดขึ้น (ระยะสั้น): Vercel 'eve'/Agent Stack กลายเป็น safe default — เป็น launch ที่ใหม่มากและมีการตลาดหนัก [1][13][18][28] ยังไม่มี maturity track record

## Org applicability — NDF DEV
1) Benchmark GLM-5.2 เทียบกับ coding-agent model ปัจจุบันบน Unity/web task จริงและด้านต้นทุน ถ้าตรงตามที่อ้างลดค่าใช้จ่ายได้ประมาณ 10x — effort med [11][27][43][34] 2) Pilot MCP server หนึ่งตัวใน editor ที่ใช้อยู่สำหรับ design-to-code: Figma MCP สำหรับงาน UI (Slides/FigJam/code roundtrip) เหมาะกับ edutech และ app screens — effort low/med [16] 3) ทดลอง code-graph MCP (Gortex หรือ codebase-memory-mcp) บน repo หนึ่งตัวเพื่อวัด token savings ก่อนตัดสินใจ — effort low [50][33] 4) นำ agent 'skills' ชุดที่ผ่านการคัดกรองแล้ว (obra/superpowers, agent-skills) มาใส่ใน .claude/agent config แทนการเขียนเอง — effort low [9][23][6] 5) สำหรับ web/mobile/edutech apps ประเมิน Vercel Connect scoped short-lived tokens เป็น pattern สำหรับ agent auth แม้ไม่ได้ adopt stack ทั้งชุด — effort med [59][32] ข้ามไปก่อน: commit กับ Vercel 'eve'/Agent Stack เป็น base (ใหม่เกินไป) [1][46]; react กับข่าวลือ SpaceX–Cursor [10]; Hermes/crypto-agent hackathon tooling [7][51] และรายงาน smart-contract exploitation [52] — ไม่เกี่ยวกับ stack ของเรา

## Signals to Watch
- การ adoption จริงของ GLM-5.2 และว่า benchmark wins จะรอดการ eval อิสระได้หรือไม่ [11][27][43]
- การแพร่กระจายของ MCP server ข้าม design/dev tools ในฐานะ portability standard [16][48][50][33]
- การยืนยันหรือปฏิเสธการซื้อกิจการ SpaceX–Anysphere/Cursor และผลกระทบต่อ tooling [10]
- ความสมบูรณ์ของ Vercel Agent Stack — execution limits, pricing, lock-in — ก่อนจะปลอดภัยใช้ production [46][60]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **Panniantong/Agent-Reach** — ให้ AI agent มองเห็นอินเทอร์เน็ตทั้งหมด อ่านและค้นหา Twitter, Reddit, YouTube, GitHub | radar | <https://github.com/Panniantong/Agent-Reach> |
| **mattpocock/skills** — Skills สำหรับวิศวกรจริง ตรงจาก .claude directory ของผู้เขียน | radar | <https://github.com/mattpocock/skills> |
| **obra/superpowers** — agentic skills framework และ software development methodology ที่ใช้งานได้จริง | radar | <https://github.com/obra/superpowers> |
| **freeCodeCamp/freeCodeCamp** — codebase และหลักสูตร open-source ของ freeCodeCamp.org สอนคณิตศาสตร์ การเขียนโปรแกรม และวิทยาการคอมพิวเตอร์ | radar | <https://github.com/freeCodeCamp/freeCodeCamp> |
| **Universal-Debloater-Alliance/universal-android-debloater-next-generation** — GUI ข้ามแพลตฟอร์มเขียนด้วย Rust ใช้ ADB debloat Android ที่ไม่ได้ root เพื่อความเป็นส่วนตัว | radar | <https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation> |
| **n0-computer/iroh** — IP address พัง dial keys แทน networking stack แบบ modular เขียนด้วย Rust | radar | <https://github.com/n0-computer/iroh> |
| **chatwoot/chatwoot** — live-chat, email support, omni-channel desk open-source ทางเลือกแทน Intercom, Zendesk, Salesforce | radar | <https://github.com/chatwoot/chatwoot> |
| **DeusData/codebase-memory-mcp** — code intelligence MCP server ประสิทธิภาพสูง index codebase เป็น persistent knowledge graph | radar | <https://github.com/DeusData/codebase-memory-mcp> |
| **meshery/meshery** — Meshery, cloud native manager | radar | <https://github.com/meshery/meshery> |
| **bytedance/UI-TARS-desktop** — Open-Source Multimodal AI Agent Stack เชื่อม AI models และ Agent Infra ล่าสุด | radar | <https://github.com/bytedance/UI-TARS-desktop> |
| **krahets/hello-algo** — 《Hello 算法》: บทเรียน data structures และ algorithms แบบ animation พร้อมรันได้ด้วยคลิกเดียว รองรับ Python, Java, C++, C, C#, JS, Go, Swift, Rust | radar | <https://github.com/krahets/hello-algo> |
| **penpot/penpot** — Penpot: design tool open-source สำหรับความร่วมมือระหว่าง design และ code | radar | <https://github.com/penpot/penpot> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | vercel | ^3309 c162 | [Introducing eve, an agent framework. 𝚊𝚐𝚎𝚗𝚝/ 𝚊𝚐𝚎𝚗𝚝.𝚝𝚜 𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝𝚒𝚘𝚗𝚜.𝚖𝚍 𝚝𝚘𝚘𝚕𝚜/ 𝚜𝚔𝚒𝚕](https://x.com/vercel/status/2067180054979936413) |
| x | theo | ^3109 c250 | [I hate to admit it but the loop people were right](https://x.com/theo/status/2067115748959682743) |
| x | swyx | ^2572 c112 | [Cursor/Graphite's @TomasReimers just announced Origin @cursor_ai's long awaited ](https://x.com/swyx/status/2066928345246470204) |
| x | simonw | ^2184 c143 | [If this really is the "jailbreak" that got Fable shut down I'm deeply unimpresse](https://x.com/simonw/status/2066722034491789720) |
| radar | Panniantong_Agent-Reach | ^2025 c0 | [Panniantong/Agent-Reach Give your AI agent eyes to see the entire internet. Read](https://github.com/Panniantong/Agent-Reach) |
| radar | mattpocock_skills | ^1849 c0 | [mattpocock/skills Skills for Real Engineers. Straight from my .claude directory.](https://github.com/mattpocock/skills) |
| x | NousResearch | ^1545 c107 | [The Hermes Agent Accelerated Business Hackathon presented by @NVIDIAAI × @stripe](https://x.com/NousResearch/status/2066921443548348436) |
| hackernews | jfb | ^1447 c555 | [Running local models is good now](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/) |
| radar | obra_superpowers | ^1109 c0 | [obra/superpowers An agentic skills framework & software development methodology ](https://github.com/obra/superpowers) |
| hackernews | itsmarcelg | ^1087 c1584 | [SpaceX to buy Cursor for $60B](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/) |
| x | cline | ^1024 c23 | [GLM-5.2 is the first open-weights model to cross 80% on Terminal-Bench, and beat](https://x.com/cline/status/2066951439793242193) |
| x | neogeo8man | ^1007 c4 | [the writing in these is like a mean parody of later Jones cartoons by one of his](https://x.com/neogeo8man/status/2066794474559213833) |
| x | rauchg | ^966 c92 | [https://t.co/uNXS9jEgpg is Next.js for agents. I built Next with a simple premis](https://x.com/rauchg/status/2067183015214584307) |
| hackernews | Cider9986 | ^909 c476 | [GrapheneOS has been ported to Android 17](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) |
| radar | freeCodeCamp_freeCodeCamp | ^764 c0 | [freeCodeCamp/freeCodeCamp freeCodeCamp.org's open-source codebase and curriculum](https://github.com/freeCodeCamp/freeCodeCamp) |
| x | figma | ^712 c27 | [Updates to the Figma MCP server: → Generate and edit decks in Figma Slides → Bui](https://x.com/figma/status/2066923337889305038) |
| x | AndroidDev | ^700 c24 | [Android 17 has arrived! 🎉 We're bringing together next generation tools, librari](https://x.com/AndroidDev/status/2066954030115352984) |
| x | rauchg | ^694 c44 | [Tomorrow https://t.co/hO8iYOkXYk some big announcements! https://t.co/wmn8ZHNQjz](https://x.com/rauchg/status/2066838428218486827) |
| x | rauchg | ^659 c89 | [New https://t.co/A1yfEM2Rig is live, highlighting the present and future of our ](https://x.com/rauchg/status/2067165617275256982) |
| x | finbarrtimbers | ^568 c45 | [Today was my second day at Microsoft Superintelligence, where I'll be working on](https://x.com/finbarrtimbers/status/2066647629979963541) |
| hackernews | pseudolus | ^503 c218 | [Calvin and Hobbes and the price of integrity](https://therepublicofletters.substack.com/p/calvin-and-hobbes-and-the-price-of) |
| hackernews | mrshu | ^497 c214 | [TIL: You can make HTTP requests without curl using Bash /dev/TCP](https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/) |
| x | sharbel | ^474 c25 | [Someone built a free collection of production-grade engineering skills that teac](https://x.com/sharbel/status/2066872849046933768) |
| hackernews | thm | ^467 c244 | [Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://wpvip.com/future-of-the-web-2026/) |
| radar | Universal-Debloater-Alliance_universal-android-debloater-next-generation | ^465 c0 | [Universal-Debloater-Alliance/universal-android-debloater-next-generation Cross-p](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation) |
| hackernews | dzonga | ^452 c264 | [Stop Using JWTs](https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452) |
| hackernews | himata4113 | ^451 c242 | [GLM-5.2 is the new leading open weights model on Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) |
| x | rauchg | ^428 c51 | [It's time to ship](https://x.com/rauchg/status/2067106499449565265) |
| radar | n0-computer_iroh | ^422 c0 | [n0-computer/iroh IP addresses break, dial keys instead. Modular networking stack](https://github.com/n0-computer/iroh) |
| radar | chatwoot_chatwoot | ^400 c0 | [chatwoot/chatwoot Open-source live-chat, email support, omni-channel desk. An al](https://github.com/chatwoot/chatwoot) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vercel</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3309 · 💬 162</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vercel/status/2067180054979936413">View @vercel on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing eve, an agent framework. 𝚊𝚐𝚎𝚗𝚝/ 𝚊𝚐𝚎𝚗𝚝.𝚝𝚜 𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝𝚒𝚘𝚗𝚜.𝚖𝚍 𝚝𝚘𝚘𝚕𝚜/ 𝚜𝚔𝚒𝚕𝚕𝚜/ 𝚜𝚊𝚗𝚍𝚋𝚘𝚡/ 𝚜𝚌𝚑𝚎𝚍𝚞𝚕𝚎𝚜/ Like Next.js, for agents. https://t.co/ezUIGLkSqG”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Vercel เปิดตัว 'eve' agent framework แบบ file-based convention มีโครงสร้าง tools/, skills/, sandbox/, schedules/ — ใช้แนวคิดเดียวกับที่ Next.js ทำกับ web routing</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่คุ้นกับ Next.js เข้าใจ pattern นี้ได้เร็ว ลดเวลาออกแบบ agent architecture เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู repo eve บน GitHub แล้วประเมินว่า structure ของมันเข้ากับ web project ของ studio ได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vercel/status/2067180054979936413" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3109 · 💬 250</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2067115748959682743">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I hate to admit it but the loop people were right”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Theo Browne (@theo) นักพัฒนา web ที่เคยสงสัย agentic loop ออกมายอมรับว่ากลุ่มที่เชื่อใน agentic coding loop นั้นพูดถูก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>คนที่เคย skeptic ยอมรับ agentic loop แปลว่า pattern นี้พ้นจาก hype แล้ว และให้ผลจริงในงาน dev</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เช็คว่า workflow AI ของทีมใช้ single-shot หรือ agentic loop — ถ้ายังเป็น single-shot ลอง loop-based agent กับ task เล็กใน sprint นี้ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2067115748959682743" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@swyx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2572 · 💬 112</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/swyx/status/2066928345246470204">View @swyx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Cursor/Graphite’s @TomasReimers just announced Origin @cursor_ai’s long awaited Git competitor, scalable for agent workloads, extensible with api and mcp, and built in merge conflicts and co failure a”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Tomas Reimers จาก Cursor/Graphite ประกาศ Origin ระบบ version control ใหม่แทน Git ที่รองรับ AI agent workloads, API/MCP extensibility และ auto-resolve merge conflict กับ CI failure</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>VCS ที่ออกแบบมาสำหรับ agent หมายความว่า branch, merge และ CI recovery วิ่งได้โดยไม่ต้องแตะมือ ตรงกับ multi-agent pipeline ที่ทีมกำลังใช้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม Origin ให้ออก public แล้ว pilot ใน project ที่ใช้ Cursor อยู่แล้ว เน้นทดสอบ agent-driven branch และ conflict resolution</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/swyx/status/2066928345246470204" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@simonw</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2184 · 💬 143</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/simonw/status/2066722034491789720">View @simonw on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If this really is the &quot;jailbreak&quot; that got Fable shut down I'm deeply unimpressed https://t.co/tRhzKcFHRX”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Simon Willison ดู jailbreak ที่อ้างว่าทำให้ AI model Fable โดน shut down แล้วบอกว่าไม่ได้ซับซ้อนอะไร — แปลว่าการตัดสินใจ shut down อาจเกินกว่าความเสี่ยงจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>AI product โดน shut down จาก exploit ง่ายๆ บอกว่า risk tolerance ต่ำมาก — ทีมที่ ship AI feature ต้องมี incident response policy ก่อน launch</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">กำหนด AI incident policy ให้ชัด: อะไรทำให้ kill feature, ใครตัดสินใจ, เร็วแค่ไหน — ทำก่อน feature AI ตัวไหนขึ้น live</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/simonw/status/2066722034491789720" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NousResearch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1545 · 💬 107</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NousResearch/status/2066921443548348436">View @NousResearch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Hermes Agent Accelerated Business Hackathon presented by @NVIDIAAI × @stripe × @NousResearch starts now, for builders making agents that can earn, spend, and run real operations at any scale. Our ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Nous Research, NVIDIA, และ Stripe เปิด hackathon (ปิดรับ 30 มิ.ย.) สร้าง autonomous business agent บน Hermes + Stripe Skills รางวัลที่ 1: $10k + DGX Spark + $5k Stripe credits</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Stripe Skills ให้ agent จัดการ payment และ provision SaaS ได้เอง — blueprint จริงสำหรับ agentic commerce ที่ studio นำไปปรับใช้ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เหลือ 13 วัน — สร้าง demo agent บน Hermes + Stripe Skills, อัดวิดีโอ 1–3 นาที, กรอกฟอร์มก่อน 30 มิ.ย.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NousResearch/status/2066921443548348436" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cline</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1024 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cline/status/2066951439793242193">View @cline on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“GLM-5.2 is the first open-weights model to cross 80% on Terminal-Bench, and beats every other open model available. It also beats Gemini, making it a frontier-level model for a fraction of the cost. O”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>GLM-5.2 เป็น open-weights model ตัวแรกที่ทำคะแนนเกิน 80% บน Terminal-Bench แซงทุก open model และ Gemini แล้ว ใช้งานได้ใน Cline ทันที</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>open model คะแนนสูงใน Cline ให้ทีมใช้ AI ช่วย coding ได้ในราคาต่ำกว่า proprietary API มาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ GLM-5.2 ใน Cline กับ terminal task เพื่อดูว่าแทน model ราคาสูงในงานประจำได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cline/status/2066951439793242193" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@neogeo8man</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1007 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/neogeo8man/status/2066794474559213833">View @neogeo8man on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“the writing in these is like a mean parody of later Jones cartoons by one of his critics, but to be fair he was 89 and dying very impressive Flash brush tool use tho, esp given this was 2001 https://t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้วิจารณ์ Flash animation ปี 2001 — ชม brush tool technique แม้ศิลปินอายุ 89 แต่ติคุณภาพ writing</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/neogeo8man/status/2066794474559213833" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 966 · 💬 92</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2067183015214584307">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/uNXS9jEgpg is Next.js for agents. I built Next with a simple premise: 𝚙𝚊𝚐𝚎𝚜/𝚒𝚗𝚍𝚎𝚡.𝚓𝚜 is all you need. Put some React in there and you’re good to go. Eve asks for even less. 𝚊𝚐𝚎𝚗𝚝/𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Guillermo Rauch (CEO Vercel) ปล่อย Eve — agent framework แบบ filesystem-based ที่ใช้ agent/instructions.md นิยาม agent และ tools/*.ts เป็น tool แต่ละตัว deploy บน Vercel ได้ทันที</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>convention แบบ file-based ของ Eve ทำให้โครงสร้าง agent อ่านได้และ version control ได้โดยไม่ต้องเรียนรู้ abstraction ใหม่ — ใครที่รู้จัก Next.js จับได้เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม web ลอง spin up Eve project ด้วย instructions.md + tools/*.ts ไฟล์เดียว เทียบ DX กับ agent setup ที่ใช้อยู่ก่อนตัดสินใจ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2067183015214584307" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
