---
type: social-topic-report
date: '2026-06-02'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-06-02T03:05:20+00:00'
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
post_count: 160
salience: 0.82
sentiment: mixed
confidence: 0.68
tags:
- coding-agents
- llm-models
- agent-skills
- mcp
- supply-chain-security
- evals
thumbnail: https://pbs.twimg.com/media/HJspkEsbkAAACqT.jpg
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-06-02

## TL;DR
- Anthropic ยื่นร่าง S-1 ต่อ SEC อย่างลับๆ ส่งสัญญาณว่าอาจ IPO และกดดันให้แสดงรายได้กับความยั่งยืน — สำคัญสำหรับใครที่ผูก toolchain ไว้กับ Claude/Claude Code [1][27]
- MiniMax-M3 เปิดตัว: context 1M token, multimodal, agentic coding ผ่าน sparse attention; ขึ้นอันดับ 1 open model บน Next.js agent evals ตามหลัง Opus และ GPT5 แต่ถูกกว่า ~10x (20x บน Vercel AI Gateway) [11][30][43][47] Qwen-3.7 Plus ก็อ้างสมรรถนะ coding/agent ใกล้ SOTA เช่นกัน [51]
- ระบบนิเวศ 'agent skills' กำลังรวมตัว: ผู้ชนะ Anthropic hackathon open-source 'Everything Claude Code' (183 skills, 48 sub-agents, 79 commands) [12][49][55], NVIDIA ส่ง skills catalog สำหรับ CUDA-X/Omniverse/Physical-AI [13] และ SkillSpector scanner ของ NVIDIA (64 checks/16 categories) ปรากฏขึ้นเพื่อตรวจสอบ skills ก่อนติดตั้ง [18]
- เหตุการณ์ด้าน supply-chain และ agent security สะสมขึ้น: พบ npm packages อันตรายใน Red Hat Cloud Services [19] และ AI support bot ของ Meta ถูกใช้ยึดบัญชี Instagram [9]
- OpenAI frontier models และ Codex พร้อมใช้งานบน AWS แล้ว [54]; MCP ขยายเข้าสู่ dev tooling เพิ่มขึ้น (TablePlus DB workflows) [58]

## สิ่งที่เกิดขึ้น
สองกลุ่มหลักครองพื้นที่ กลุ่มแรก — models และ platforms: Anthropic ยื่น draft S-1 ต่อ SEC อย่างลับๆ เปิดทางเลือก IPO ไว้ [1][27]; MiniMax ปล่อย M3, model multimodal context 1M ที่มี agentic coding ขึ้นอันดับ 1 ใน open-model agent evals ของ Next.js ขณะที่ราคาต่ำกว่า Opus และ GPT5 ราว 10x [11][30][43][47]; Qwen-3.7 Plus ของ Alibaba อ้างผล coding/agent ใกล้ SOTA [51]; และ OpenAI นำ frontier models พร้อม Codex เข้า AWS [54] กลุ่มสอง — 'agent skills' และ tooling layer โตขึ้น: ผู้ชนะ Anthropic hackathon open-source skill bundle ขนาดใหญ่สำหรับ Claude Code [12][49][55], NVIDIA เผยแพร่ official skills catalog สำหรับ CUDA-X/Omniverse/Physical AI [13] และปล่อย SkillSpector สำหรับสแกน skills แบบ static ก่อนติดตั้ง [18] MCP integrations ขยายกว้างขึ้น (TablePlus [58]; crypto servers ต่างๆ [34][40]) และ microsoft/markitdown (files→Markdown) ติด trend ในฐานะ ingestion glue [3] ควบคู่กับนี้ ความล้มเหลวด้าน security โผล่ขึ้น — npm packages อันตรายใน Red Hat Cloud Services [19] และการยึดบัญชี Instagram ผ่าน AI support bot ของ Meta [9] บทวิเคราะห์ชี้ว่า eval/observability startups กำลังเปลี่ยนโฉมสู่ 'continual learning' platforms [36][57] และมีการวิจารณ์ว่า swe-bench ไม่น่าเชื่อถือ โดยมี DeepSWE ถูกเสนอเป็น agentic benchmark ที่สมเหตุสมผลกว่า [20] ตัวเลขบางอย่าง เช่น '163k stars' [55] กับกรอบ $15K-credit [12] ขัดแย้งกัน ควรตีความอย่างระวัง

## เหตุใดจึงสำคัญ (เหตุผล)
เส้นโค้งต้นทุนคือเรื่องหลักสำหรับ studio: M3 และ Qwen-3.7 ให้คุณภาพ coding/agent ใกล้ frontier ในราคาเศษเสี้ยวของ closed-model [30][51] ทำให้การ route งาน open model ราคาถูกสำหรับ agent งานหนัก (codegen, refactor, test scaffolding) คุ้มค่าเชิงเศรษฐกิจ ในขณะที่สงวน Opus/GPT5 ไว้สำหรับงานยาก S-1 ของ Anthropic [1][27] และ OpenAI/Codex ที่ลงจอดบน AWS [54] ล้วนชี้ไปที่การรวมศูนย์ vendor และการกระจายในองค์กร — ดีต่อการจัดซื้อและเสถียรภาพ แต่เตือนว่าอย่าผูก workflow แน่นกับ UI ของ provider รายใดรายหนึ่ง เพราะ feature อาจหายไปโดยไม่แจ้ง (Codex 'Copy as Markdown' ถูกลบแล้วคืนกลับหลังถูกต่อต้าน [8][45]) ความเฟื่องฟูของ skills/MCP [12][13][22][28][58] ลดต้นทุนในการมอบความสามารถให้ agent แต่เหตุการณ์เดียวกัน — npm supply-chain ถูกโจมตี [19], AI support bot ถูกต้มจนยึดบัญชี [9] — แสดงว่า attack surface ขยายตามไปด้วย นั่นคือเหตุผลที่ SkillSpector มีอยู่ [18]: การติดตั้ง skill หรือ MCP server จากบุคคลที่สามตอนนี้คือการตัดสินใจเรื่องความน่าเชื่อถือของ dependency ไม่ใช่แค่ความสะดวก

## ความเป็นไปได้
น่าจะเกิด: open coding models ราคาถูก (M3, Qwen-3.7) จะถูกนำมาใช้ผ่าน gateway สำหรับ agent workloads ที่ต้นทุนสำคัญภายในไม่กี่เดือน เมื่อพิจารณาช่องห่างราคา 10–20x และตำแหน่งบน eval ที่แข่งขันได้ [30][11][51] เป็นไปได้: agent-skill marketplaces โตเร็วพอให้ skill scanning/signing กลายเป็นขั้นตอนมาตรฐาน เพราะทั้ง catalogs [12][13], scanner [18] และเหตุการณ์ supply-chain [19][9] กำลังเกิดขึ้นพร้อมกัน เป็นไปได้: eval vendors จะปรับตัวเป็น continual-learning platforms ในปี 2026 พร้อม shakeout — แหล่งข่าวเองทำนายว่าหลายรายจะล้มเหลว [36] ไม่น่าจะชัดเจนเร็วๆ นี้: ความน่าเชื่อถือของ benchmark — การวิจารณ์ swe-bench และ DeepSWE ยังอยู่ในช่วงเริ่มต้น [20] จึงยังไม่มี agentic-coding benchmark ใดที่ตกผลึก ไทม์ไลน์ IPO ของ Anthropic ยังไม่แน่นอน; draft S-1 แบบลับคือตัวเลือก ไม่ใช่กำหนดการ [1][27] ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น จึงไม่อ้างที่นี่

## การประยุกต์ใช้สำหรับ NDF DEV
1) ทดลองใช้ MiniMax-M3 (และ Qwen-3.7 Plus) ผ่าน Vercel AI Gateway สำหรับงาน web/Next.js และ coding-agent ทั่วไป เปรียบเทียบต้นทุน/คุณภาพกับการใช้ Opus/GPT5 ปัจจุบัน — effort ต่ำ [30][11][51] 2) ปฏิบัติต่อ agent skill หรือ MCP server จากบุคคลที่สามเหมือน untrusted dependency: รัน SkillSpector (หรือ static + LLM scan เทียบเท่า) ก่อนติดตั้ง bundle อย่าง 'Everything Claude Code', compound-engineering plugin หรือ 'harness' — effort ต่ำ/กลาง [18][12][28][22][19][9] 3) สำหรับงาน XR/VR และ Unity ดู skills catalog ของ NVIDIA สำหรับ CUDA-X/Omniverse/Physical-AI ใน Hermes Skills Hub เพื่อดูว่าช่วยเร่ง rendering/sim pipeline ได้ไหม — effort กลาง [13] 4) ใช้ microsoft/markitdown นำ docs/office files เข้าสู่ Markdown สำหรับการเตรียมเนื้อหา edutech และ agent ingestion — effort ต่ำ [3] 5) วาง model/provider ไว้หลัง abstraction (gateway หรือ adapter ของตัวเอง) เพื่อให้การเปลี่ยน UI/feature หรือราคาของ vendor ไม่พัง workflow — effort กลาง [8][45][54][1] 6) เมื่อเชื่อม MCP เข้ากับ DB/admin tools ภายใน (เช่น TablePlus) ปิดกั้น write access และทดสอบ permission/data-handling quirks — effort กลาง [58][41] ข้ามไปก่อน: crypto/DeFi MCP servers [34][40], MoneyPrinterTurbo [2], TradingAgents [35] และการรับ repo แนว 'X skills/Y sub-agents' ที่ viral โดยไม่สแกนและพิสูจน์ก่อน [55]

## Signals ที่ควรจับตา
- Open coding models ไล่ตาม closed frontier ในราคา ~10x ถูกกว่า — ติดตาม M3 และ Qwen-3.7 บน agent evals [30][51]
- Security tooling สำหรับ Skill/MCP กำลังกลายเป็น mandatory เมื่อ catalog ขยายตัว — จับตา SkillSpector และมาตรฐาน signing/provenance [18][13][19]
- Eval/observability vendors ปรับทิศสู่ 'continual learning' ในปี 2026; คาดว่าจะมี consolidation [36][57]
- AI hardware ในพื้นที่ (NVIDIA RTX Spark, Surface Laptop Ultra) ลดต้นทุน on-device/private agent [31][53][38]

## Repos & Tools ที่ควรลอง
| repo | source | url |
|---|---|---|
| **harry0703/MoneyPrinterTurbo** — 利用AI大模型，一键生成高清短视频 สร้างวิดีโอสั้นด้วย AI LLM แบบคลิกเดียว | radar | <https://github.com/harry0703/MoneyPrinterTurbo> |
| **microsoft/markitdown** — Python tool สำหรับแปลงไฟล์และเอกสาร office เป็น Markdown | radar | <https://github.com/microsoft/markitdown> |
| **D4Vinci/Scrapling** — 🕷️ adaptive Web Scraping framework ที่รองรับทุกอย่างตั้งแต่ single request ถึง full-scale | radar | <https://github.com/D4Vinci/Scrapling> |
| **codecrafters-io/build-your-own-x** — เชี่ยวชาญการเขียนโปรแกรมด้วยการสร้าง technology ที่ชอบขึ้นมาใหม่จากศูนย์ | radar | <https://github.com/codecrafters-io/build-your-own-x> |
| **nesquena/hermes-webui** — Hermes WebUI: วิธีที่ดีที่สุดในการใช้ Hermes Agent ผ่านเว็บหรือโทรศัพท์ | radar | <https://github.com/nesquena/hermes-webui> |
| **OpenBMB/VoxCPM** — VoxCPM2: Tokenizer-Free TTS สำหรับ Multilingual Speech Generation, Creative Voice Design และ True-to-L | radar | <https://github.com/OpenBMB/VoxCPM> |
| **FareedKhan-dev/train-llm-from-scratch** — วิธี train LLM ที่ตรงไปตรงมา ตั้งแต่ดาวน์โหลดข้อมูลจนถึงสร้าง text | radar | <https://github.com/FareedKhan-dev/train-llm-from-scratch> |
| **RedHatInsights/javascript-clients** — ตรวจพบ npm packages อันตรายใน Red Hat Cloud Services | hackernews | <https://github.com/RedHatInsights/javascript-clients> |
| **supermemoryai/supermemory** — Memory engine และ app ที่เร็วและ scalable สุด Memory API สำหรับยุค AI | radar | <https://github.com/supermemoryai/supermemory> |
| **revfactory/harness** — meta-skill ที่ออกแบบ domain-specific agent teams, กำหนด specialized agents และสร้าง | radar | <https://github.com/revfactory/harness> |
| **pbakaus/impeccable** — design language ที่ทำให้ AI harness เก่งด้าน design ขึ้น | radar | <https://github.com/pbakaus/impeccable> |
| **EveryInc/compound-engineering-plugin** — Official Compound Engineering plugin สำหรับ Claude Code, Codex, Cursor และอื่นๆ | radar | <https://github.com/EveryInc/compound-engineering-plugin> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | AnthropicAI | ^18682 c768 | [Anthropic has confidentially submitted a draft S-1 registration statement to the](https://x.com/AnthropicAI/status/2061478052257841495) |
| radar | harry0703_MoneyPrinterTurbo | ^3375 c0 | [harry0703/MoneyPrinterTurbo 利用AI大模型，一键生成高清短视频 Generate short videos with one cli](https://github.com/harry0703/MoneyPrinterTurbo) |
| radar | microsoft_markitdown | ^3034 c0 | [microsoft/markitdown Python tool for converting files and office documents to Ma](https://github.com/microsoft/markitdown) |
| x | elonmusk | ^2078 c308 | [@yunta_tsai Tool use was a gamechanger](https://x.com/elonmusk/status/2061220941112451251) |
| x | theo | ^1639 c79 | [This is bigger than you probably think](https://x.com/theo/status/2061572633599394200) |
| radar | D4Vinci_Scrapling | ^1486 c0 | [D4Vinci/Scrapling 🕷️ An adaptive Web Scraping framework that handles everything ](https://github.com/D4Vinci/Scrapling) |
| x | rauchg | ^1432 c193 | [Unclear if a durable trend, but CEOs and CTOs are back to coding with a fury, th](https://x.com/rauchg/status/2061135404942974982) |
| x | simonw | ^1410 c136 | [I'm really upset about this: OpenAI's Codex Desktop had a "Copy as Markdown" opt](https://x.com/simonw/status/2061158636311958005) |
| hackernews | ssiddharth | ^1403 c334 | [The newest Instagram "exploit" is the goofiest I've seen <a href="https:&#x2F;&#](https://www.0xsid.com/blog/meta-account-takeover-fiasco) |
| radar | codecrafters-io_build-your-own-x | ^1212 c0 | [codecrafters-io/build-your-own-x Master programming by recreating your favorite ](https://github.com/codecrafters-io/build-your-own-x) |
| x | cline | ^1185 c49 | [The new MiniMax-M3 is their first model to have 1m context, multimodal, and agen](https://x.com/cline/status/2061287441575858253) |
| x | RoundtableSpace | ^1035 c33 | [THE WINNER OF THE ANTHROPIC HACKATHON JUST OPEN SOURCED HIS ENTIRE AI CODING SET](https://x.com/RoundtableSpace/status/2061255156323495949) |
| x | NousResearch | ^991 c56 | [We have worked with @nvidia to integrate their official Agent Skills catalog int](https://x.com/NousResearch/status/2061572272993751364) |
| radar | nesquena_hermes-webui | ^945 c0 | [nesquena/hermes-webui Hermes WebUI: The best way to use Hermes Agent from the we](https://github.com/nesquena/hermes-webui) |
| x | theo | ^912 c46 | [Confirmed rewrite with Tanstack and a bunch of data precaching. Great work Anthr](https://x.com/theo/status/2061563106208432223) |
| radar | OpenBMB_VoxCPM | ^888 c0 | [OpenBMB/VoxCPM VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, C](https://github.com/OpenBMB/VoxCPM) |
| radar | FareedKhan-dev_train-llm-from-scratch | ^861 c0 | [FareedKhan-dev/train-llm-from-scratch A straightforward method for training your](https://github.com/FareedKhan-dev/train-llm-from-scratch) |
| x | bibryam | ^744 c40 | [SkillSpector - a new security scanner for skills by NVIDIA • Scan AI agent skill](https://x.com/bibryam/status/2060940955084054634) |
| hackernews | kurmiashish | ^733 c418 | [Malicious npm packages detected across Red Hat Cloud Services](https://github.com/RedHatInsights/javascript-clients/issues/492) |
| x | theo | ^712 c40 | [swe-bench is kind of a shitshow, and it makes evaluating LLMs hard. DeepSWE is t](https://x.com/theo/status/2061368474132521392) |
| radar | supermemoryai_supermemory | ^647 c0 | [supermemoryai/supermemory Memory engine and app that is extremely fast, scalable](https://github.com/supermemoryai/supermemory) |
| radar | revfactory_harness | ^524 c0 | [revfactory/harness A meta-skill that designs domain-specific agent teams, define](https://github.com/revfactory/harness) |
| hackernews | speckx | ^523 c252 | [The Pirate Bay Remains Resilient, 20 Years After the Raid](https://torrentfreak.com/the-pirate-bay-remains-resilient-20-years-after-the-raid/) |
| x | leerob | ^512 c16 | [Some tips to help agents understand your codebase: 1. The source code either nee](https://x.com/leerob/status/2061557826787344781) |
| x | rauchg | ^501 c29 | [Beautiful example of a full-stack agent on @vercel. Great learning material!](https://x.com/rauchg/status/2061415178298937365) |
| radar | pbakaus_impeccable | ^485 c0 | [pbakaus/impeccable The design language that makes your AI harness better at desi](https://github.com/pbakaus/impeccable) |
| hackernews | surprisetalk | ^461 c376 | [Anthropic confidentially submits draft S-1 to the SEC <a href="https:&#x2F;&#x2F](https://www.anthropic.com/news/confidential-draft-s1-sec) |
| radar | EveryInc_compound-engineering-plugin | ^417 c0 | [EveryInc/compound-engineering-plugin Official Compound Engineering plugin for Cl](https://github.com/EveryInc/compound-engineering-plugin) |
| hackernews | kristianpaul | ^372 c43 | [CS336: Language Modeling from Scratch](https://cs336.stanford.edu/) |
| x | rauchg | ^357 c27 | [MiniMax M3 is now the leading open model on the Next.js agent evaluations (https](https://x.com/rauchg/status/2061593874498531707) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnthropicAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 18682 · 💬 768</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnthropicAI/status/2061478052257841495">View @AnthropicAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anthropic has confidentially submitted a draft S-1 registration statement to the Securities and Exchange Commission. Pending completion of SEC review, this gives us the option to pursue an initial pub”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Anthropic ยื่น draft S-1 แบบลับต่อ SEC แล้ว เปิดทางให้ IPO ได้หลัง review เสร็จ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AnthropicAI/status/2061478052257841495" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@elonmusk</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2078 · 💬 308</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/elonmusk/status/2061220941112451251">View @elonmusk on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@yunta_tsai Tool use was a gamechanger”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Elon Musk ตอบ tweet ว่า 'Tool use was a gamechanger' โดยไม่ระบุ tool ใด รุ่นใด หรือบริบทใดเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/elonmusk/status/2061220941112451251" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1639 · 💬 79</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2061572633599394200">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is bigger than you probably think”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ของ @theo มีแค่ประโยคว่า 'This is bigger than you probably think' ไม่มีหัวข้อ, ชื่อ tool, release หรือข้อมูลใดระบุ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2061572633599394200" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1432 · 💬 193</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2061135404942974982">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Unclear if a durable trend, but CEOs and CTOs are back to coding with a fury, thanks to coding agents. I have public company CEOs sliding into my DMs (and “InMail”) telling me about falling in love wi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>CEO ของ Vercel (Guillermo Rauch) บอกว่า CEO และ CTO องค์กรใหญ่กลับมา code เองด้วย agents อย่าง Claude Code ทำให้ C-suite กลายเป็นคนประเมิน dev stack โดยตรง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ลูกค้า enterprise ที่ใช้ coding agents เองประเมิน stack โดยตรง — การเลือก tech ของ studio ไม่มีชั้น IT กั้นอีกต่อไป</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เวลา pitch ลูกค้า enterprise เตรียม stack walkthrough ที่ CEO ลอง code เองแล้วเข้าใจได้ — ไม่ใช่แค่ slide สำหรับทีม IT</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2061135404942974982" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@simonw</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1410 · 💬 136</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/simonw/status/2061158636311958005">View @simonw on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm really upset about this: OpenAI's Codex Desktop had a &quot;Copy as Markdown&quot; option for exporting full chat transcripts, but the feature vanished in an update a couple of days ago Genuinely my single ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Simon Willison รายงานว่า OpenAI Codex Desktop เพิ่งลบ feature 'Copy as Markdown' สำหรับ export transcript ออกโดยไม่แจ้ง ซึ่งเขายกให้เป็นจุดเด่นเดียวที่เหนือกว่า Claude Code</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ปัญหานี้เผย workflow gap จริง — การ export AI coding session เป็น Markdown มีประโยชน์สำหรับ docs และ retro แต่ยังไม่มี tool ไหนทำได้ดีพอ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมเขียน script เล็กๆ ที่อ่าน transcript file ของ Claude Code แล้ว export เป็น Markdown ได้เลย ไม่ต้องรอ vendor</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/simonw/status/2061158636311958005" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cline</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1185 · 💬 49</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cline/status/2061287441575858253">View @cline on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The new MiniMax-M3 is their first model to have 1m context, multimodal, and agentic coding capability. Congratulations to @MiniMax_AI for the breakthrough in sparse-attention architecture cutting comp”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>MiniMax-M3 เปิดตัวพร้อม context 1M token, รองรับ multimodal และ agentic coding — ใช้ sparse-attention architecture ลด compute และต้นทุนเหลือ 1/20 ของรุ่นก่อน — ใช้ฟรีใน Cline แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Context 1M token ต้นทุนต่ำมาก ทำให้ agentic coding ระดับ full-repo ที่เคยแพงเกินไปกลายเป็นทำได้จริงใน Cline</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ MiniMax-M3 ใน Cline กับ project Unity หรือ web ขนาดใหญ่ เทียบคุณภาพและต้นทุนกับ model หลักที่ทีมใช้อยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cline/status/2061287441575858253" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RoundtableSpace</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1035 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RoundtableSpace/status/2061255156323495949">View @RoundtableSpace on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“THE WINNER OF THE ANTHROPIC HACKATHON JUST OPEN SOURCED HIS ENTIRE AI CODING SETUP FOR FREE. 183 AGENT SKILLS, 48 SUB-AGENTS AND 79 READY-MADE COMMANDS. He spent 10 months on it, won $15K in API credi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ชนะ Anthropic Hackathon open-source ระบบ agent coding ทั้งหมดภายใต้ MIT license — 183 skills, 48 sub-agents, 79 commands สร้างนาน 10 เดือน หลังได้รับ API credits $15K</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Framework MIT ระดับนี้ที่ผ่านการใช้จริงมาแล้ว fork ได้เลย — ทีมดูได้ว่า skills ไหนอุด gap ใน Claude Code setup ปัจจุบันได้บ้าง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Clone repo แล้วเทียบ skill/command list กับ Oracle skills ที่มีอยู่ — หาของที่ port มาได้จริง เน้น Unity, XR, หรือ content pipeline</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RoundtableSpace/status/2061255156323495949" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NousResearch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 991 · 💬 56</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NousResearch/status/2061572272993751364">View @NousResearch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We have worked with @nvidia to integrate their official Agent Skills catalog into the Hermes Skills Hub. These skills teach your agent how to use CUDA-X libraries, Omniverse and Physical AI workflows,”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Nous Research รวม Agent Skills catalog อย่างเป็นทางการของ NVIDIA เข้ากับ Hermes Skills Hub แล้ว ครอบคลุม CUDA-X, Omniverse, Physical AI และ NeMo</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Skills สำเร็จรูปสำหรับ Omniverse และ NeMo ช่วยให้ทีม XR/VR ใช้ NVIDIA platform ผ่าน agent ได้เลย ไม่ต้องเขียน integration เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู Hermes Skills Hub ว่า Omniverse หรือ NeMo skills ใช้กับ pipeline XR/VR หรือ AI training ของทีมได้ไหม ก่อนสร้าง agent tool เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NousResearch/status/2061572272993751364" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
