---
type: social-topic-report
date: '2026-06-07'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-06-07T15:04:44+00:00'
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
post_count: 285
salience: 0.7
sentiment: mixed
confidence: 0.55
tags:
- ai-devtools
- agent-skills
- coding-agents
- mcp
- openai
- security
thumbnail: https://pbs.twimg.com/media/HKHQJ4LaUAAdo9i.jpg
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-06-07

## TL;DR
- Vercel เปิดตัว Skills API ในฐานะ "npm registry สำหรับ agent capabilities" แบบเปิดและฟรี; Garry Tan จาก YC ระบุว่า skills คือสิ่งที่มาแทน prompts [26][28]
- FT รายงานว่า OpenAI กำลังเตรียม ChatGPT overhaul ครั้งใหญ่ที่สุด โดยรวม ChatGPT, Codex และ web browser เข้าไว้ใน desktop platform เดียว [22][29]
- เรื่องราวการใช้ coding agent ครองพื้นที่: Cursor สร้าง landing page จาก voice note [9], "real-life pokedex" ด้วย Claude Code [16], และการใช้ Codex หนักรายวัน [6][52]; async dual-agent workflow รายงานว่าเพียงพอสำหรับการสร้าง app [44]
- MCP ขยายตัวต่อเนื่องในกลุ่ม web stack — รองรับ MCP ใน TanStack AI แล้ว (server pooling, typegen CLI, managed lifecycle) [47]
- ประเด็นความปลอดภัย: Meta ยืนยันบัญชี Instagram หลายพันบัญชีถูกแฮกโดยอาศัยช่องโหว่ AI chatbot [19]

## What happened
ธีมหลักในเชิงปฏิบัติคือ agent "skills" ในฐานะ portable capability layer Vercel ปล่อย Skills API ที่เรียกว่า open, free registry สำหรับ agent capabilities [26] สอดคล้องกับที่ Garry Tan กล่าวว่า "the skills are the prompts" [28] พร้อมกับ skill repos และ installer ที่ออกมาพร้อมกัน — taste-skill [13], last30days-skill [14], และเครื่องมือที่ติดตั้ง skills ให้ตรงกับ tech stack [54] — และรายงานจากทีม Codex ว่า skills ที่อัปเดตแล้วทำให้ one-shot Nitro Module ได้ [46] นอกจากนี้ รายงานจาก FT (อ้างถึงใน [22][29]) ระบุว่า OpenAI วางแผนรวม ChatGPT, Codex และ browser เป็น desktop superapp เดียว Coding-agent usage anecdotes มีมาก: Cursor เสร็จ landing page จาก voice note 10 นาที [9], Codex ได้รับการยกย่องด้าน reverse-engineering และการครอบคลุม task ที่หลากหลาย [6][52][57], และ async two-agent app building [44] MCP รองรับใน TanStack AI แล้ว [47] ด้าน infrastructure, Vercel อธิบาย agent filesystem state ที่ mount ได้อิสระจาก sandbox lifecycle [39], turbovec นำเสนอ Rust vector index พร้อม Python bindings [10], และ Microsoft เผยแพร่ pg_durable สำหรับ in-database durable execution [42]

## Why it matters (reasoning)
สัญญาณที่ควรให้น้ำหนักคือ skills/MCP convergence: ถ้า capabilities กลายเป็น packaged, versioned units ที่ agent หรือ IDE ใดก็โหลดได้ [26][47] studio หนึ่งก็สามารถ encode conventions ของตัวเอง (Unity patterns, XR rigs, Next.js/Shopify storefronts) ครั้งเดียวแล้วนำกลับมาใช้ข้าม Cursor, Codex และ Claude Code ได้เลย โดยไม่ต้อง re-prompt ทุกโปรเจกต์ ต้นทุนการสลับ agent ลดลง และลด lock-in — มีประโยชน์สำหรับทีมที่ติดตาม landscape กว้างแทนที่จะผูกกับ vendor เดียว ผลกระทบรอง: OpenAI superapp ที่รวม Codex กับ browser [22][29] จะดึง dev loop มาไว้ใน walled product มากขึ้น — สะดวกในระยะสั้น แต่ผูกมัดในระยะยาว agent เดียวกับที่ ship features ได้เร็ว [9][44] ก็ขยาย attack surface ด้วย: การแฮกผ่าน Instagram chatbot [19] แสดงให้เห็นว่า AI feature ใน product ที่ ship แล้วคือ exploit vector โดยตรง — เกี่ยวข้องโดยตรงกับ edutech และ mobile app ที่ NDF ship ควรระวังรายการที่ดังที่สุด — claim เรื่อง model version (Opus 4.8, GPT 5.5/5.6, "Mythos") ใน [24][49] มาจาก unsourced tweets และ claim ที่ Google จ่าย SpaceX $1B/เดือน [4] ดูเหมือน engagement bait ไม่ใช่ข้อเท็จจริงที่ verified

## Possibility
น่าจะเกิด: agent skills ลงเอยเป็น portable cross-tool format เมื่อ platform ใหญ่ (Vercel) ผลักดัน open registry พร้อม YC endorsement [26][28] และ skill repos อิสระหลายชิ้นออกมาวันเดียวกัน [13][14][54] เป็นไปได้: OpenAI ship ChatGPT/Codex/browser desktop merge แต่ scope และ timing ยังไม่แน่นอน เพราะแหล่งคือรายงานสื่อ ไม่ใช่ release จริง [22][29] เป็นไปได้: การ scaffold app routine เปลี่ยนมาใช้ agent ต่อเนื่อง สอดคล้องกับ shipping anecdotes [9][44] และ claim ของ Anthropic ว่า Claude เขียน production code 80% ของตัวเอง [21] แม้ตัวเลขนั้นมาจาก vendor statement [21] ไม่น่าเชื่อถือ: ชื่อ/version model เฉพาะ และตัวเลข Google-SpaceX compute ที่วนใน tweet [4][24][49] — ถือว่าเป็นข่าวลือจนกว่า primary source จะยืนยัน ไม่มีแหล่งใดในชุดนี้ระบุความน่าจะเป็นเป็นตัวเลข

## Org applicability — NDF DEV
1) Pilot agent skills สำหรับ stack ของ NDF — encode conventions ด้าน Unity, XR และ Next.js เป็น reusable skills เพื่อให้ Cursor/Codex/Claude Code โหลดแทนการ re-prompt; เริ่มจากทดสอบ Skills API และ stack-matched installer (effort med) [26][54][46]. 2) Standardize tool integrations บน MCP ในส่วนที่ใช้ TanStack/Next.js อยู่แล้ว เพื่อหลีกเลี่ยง bespoke glue ต่อ agent (effort med) [47]. 3) สำหรับงาน commerce-facing web/mobile ประเมิน path prompt-to-store ของ v0 บน Next.js + Shopify ใช้เป็น prototyping shortcut (effort low) [11]. 4) นำ async two-agent workflow มาใช้กับ app features ก่อนลงทุน heavy orchestration layers (effort low) [44][9]. 5) เพิ่ม abuse/threat review สำหรับทุก AI chatbot หรือ agent feature ที่ ship โดยเฉพาะใน edutech (effort med) [19]. 6) ทดลอง open-notebook สำหรับ research content e-learning ภายใน (effort low) [25]. ข้ามไปก่อน: smart glasses สำหรับ coding agents [8], chemistry/NMR model [5], Nvidia/Windows CPU hardware [43], และการเดิมพันกับ model version ที่ยังไม่ verified [24][49] — และเพิกเฉยต่อ VC/political และ giveaway noise ที่ไม่เกี่ยวข้อง [2][15][30]

## Signals to Watch
- ว่า Vercel Skills API จะได้รับ cross-agent adoption หรือจะอยู่แค่ใน Vercel [26]
- OpenAI desktop superapp ที่รวม ChatGPT/Codex/browser ตามรายงาน — ติดตามว่าจะ release จริงหรือแค่ press speculation [22][29]
- MCP ขยายสู่ mainstream web frameworks (TanStack AI แล้ว) ในฐานะ default integration layer [47]
- AI-feature abuse ในฐานะ attack class ที่ active หลังเหตุการณ์ Meta/Instagram [19]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **RyanCodrai/turbovec** — A vector index built on TurboQuant, written in Rust with Python bindings | radar | <https://github.com/RyanCodrai/turbovec> |
| **NousResearch/hermes-agent** — The agent that grows with you | radar | <https://github.com/NousResearch/hermes-agent> |
| **Leonxlnx/taste-skill** — Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop | radar | <https://github.com/Leonxlnx/taste-skill> |
| **mvanhorn/last30days-skill** — AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - th | radar | <https://github.com/mvanhorn/last30days-skill> |
| **lfnovo/open-notebook** — An Open Source implementation of Notebook LM with more flexibility and features | radar | <https://github.com/lfnovo/open-notebook> |
| **TapXWorld/ChinaTextbook** — 所有小初高、大学PDF教材。 | radar | <https://github.com/TapXWorld/ChinaTextbook> |
| **microsoft/pg_durable** — PostgreSQL in-database durable execution | radar | <https://github.com/microsoft/pg_durable> |
| **Crosstalk-Solutions/project-nomad** — Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowle | radar | <https://github.com/Crosstalk-Solutions/project-nomad> |
| **openai/plugins** — OpenAI Plugins | radar | <https://github.com/openai/plugins> |
| **aaif-goose/goose** — an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and  | radar | <https://github.com/aaif-goose/goose> |
| **refactoringhq/tolaria** — Desktop app to manage markdown knowledge bases | radar | <https://github.com/refactoringhq/tolaria> |
| **ValveSoftware/GameNetworkingSockets** — Valve P2P networking broken for more than 2 months | hackernews | <https://github.com/ValveSoftware/GameNetworkingSockets> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | theo | ^6456 c59 | [Credit where it's due](https://x.com/theo/status/2063168665525289237) |
| x | amasad | ^5817 c159 | [When I spoke out against the Gaza genocide, a bunch of midwit VCs ganged up on m](https://x.com/amasad/status/2063344460705288401) |
| x | theo | ^4813 c94 | [He just turned it on and the battery is already dead https://t.co/1x0EBiDGwt](https://x.com/theo/status/2063158974644629929) |
| x | theo | ^4149 c206 | [Google is now paying SpaceX nearly $1 billion every month for compute. Yes, Goog](https://x.com/theo/status/2063016208065327500) |
| x | AnthropicAI | ^3427 c232 | [New Anthropic Science Blog: Making Claude a chemist. To manipulate a molecule, c](https://x.com/AnthropicAI/status/2062979607448682731) |
| x | gdb | ^2596 c230 | [Whenever I don't use codex for a task, I ask myself why and usually realize that](https://x.com/gdb/status/2063437915347136554) |
| x | theo | ^1820 c207 | [Another solid payout, not bad considering how little I've been on here the last ](https://x.com/theo/status/2063046400095752358) |
| x | Polymarket | ^1744 c169 | [JUST IN: Chinese startup Monako unveils smart glasses built to run AI coding age](https://x.com/Polymarket/status/2063441528232501549) |
| x | leerob | ^1556 c133 | [Cursor (and coding agents generally) still blows my mind daily. Just today: 1. I](https://x.com/leerob/status/2063055479106879562) |
| radar | RyanCodrai_turbovec | ^1533 c0 | [RyanCodrai/turbovec A vector index built on TurboQuant, written in Rust with Pyt](https://github.com/RyanCodrai/turbovec) |
| x | rauchg | ^1124 c92 | [Vercel is partnering with and integrating Shopify. Starting with @v0, you can no](https://x.com/rauchg/status/2062931028579078430) |
| radar | NousResearch_hermes-agent | ^1117 c0 | [NousResearch/hermes-agent The agent that grows with you](https://github.com/NousResearch/hermes-agent) |
| radar | Leonxlnx_taste-skill | ^1104 c0 | [Leonxlnx/taste-skill Taste-Skill - gives your AI good taste. stops the AI from g](https://github.com/Leonxlnx/taste-skill) |
| radar | mvanhorn_last30days-skill | ^1097 c0 | [mvanhorn/last30days-skill AI agent skill that researches any topic across Reddit](https://github.com/mvanhorn/last30days-skill) |
| x | amasad | ^1002 c6 | [@sahouraxo Hardly a day goes by without horrific news coming from the genocide r](https://x.com/amasad/status/2063321514796294177) |
| x | om_patel5 | ^905 c29 | [SOMEONE VIBE CODED A POKEDEX FOR REAL LIFE WITH CLAUDE CODE point your phone at ](https://x.com/om_patel5/status/2063467264817479775) |
| x | Samaytwt | ^653 c167 | [Never touching cursor again 😭 https://t.co/ra0XND9o8i](https://x.com/Samaytwt/status/2063532244661321909) |
| x | akshay_pachaar | ^651 c34 | [The Hermes Desktop App is insanely good. It's now the best way to run AI agents ](https://x.com/akshay_pachaar/status/2062943995811307530) |
| hackernews | speckx | ^648 c237 | [Meta confirms 1000s of Instagram accounts were hacked by abusing its AI chatbot](https://this.weekinsecurity.com/meta-confirms-thousands-of-instagram-accounts-were-hacked-by-abusing-its-ai-chatbot/) |
| x | bigaiguy | ^645 c28 | [A kid from Shantou with no programming background got into Tsinghua University's](https://x.com/bigaiguy/status/2063224246831313339) |
| x | PeterDiamandis | ^630 c86 | [Anthropic reports Claude now writes over 80% of its own production code — meanin](https://x.com/PeterDiamandis/status/2063603307067879590) |
| x | mark_k | ^582 c52 | [According to FT, @OpenAI is preparing the biggest ChatGPT overhaul since launch.](https://x.com/mark_k/status/2063569543784468893) |
| x | WikiOoc | ^569 c3 | [have an unfinished section of an "aztec" codex about the backrooms i should simp](https://x.com/WikiOoc/status/2063494560085688816) |
| x | morganlinton | ^558 c68 | [For 99% of us, GPT 5.6 is going to be what we use, not Mythos. And it won't be b](https://x.com/morganlinton/status/2063445228821029188) |
| radar | lfnovo_open-notebook | ^555 c0 | [lfnovo/open-notebook An Open Source implementation of Notebook LM with more flex](https://github.com/lfnovo/open-notebook) |
| x | rauchg | ^539 c36 | [Use the Skills API to make all your agents and platforms smarter. Think of it as](https://x.com/rauchg/status/2062951924677128455) |
| x | amasad | ^533 c22 | [Vibecon https://t.co/ggY7LLaB8y](https://x.com/amasad/status/2063300737296400516) |
| x | Av1dlive | ^436 c27 | [Garry Tan (CEO of Y-Combinator): "when someone asks how I 'prompt' my AI, the an](https://x.com/Av1dlive/status/2063314381203738690) |
| x | coinbureau | ^428 c72 | [🚨HUGE: CHATGPT IS GETTING A COMPLETE OVERHAUL OpenAI is preparing its biggest Ch](https://x.com/coinbureau/status/2063523804874481881) |
| x | supabase | ^426 c179 | [We hit 200,000 followers 🎉 To celebrate, we're doing a Supabase swag challenge! ](https://x.com/supabase/status/2063269183924613409) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6456 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2063168665525289237">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Credit where it’s due”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Theo (t3.gg) quote tweet ของ Elon Musk ปี 2025 ที่แซวว่า 'ซื้อ GPU เยอะๆ → กำไร' พร้อมบอกว่าตอนนี้พิสูจน์แล้วว่าถูก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2063168665525289237" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amasad</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5817 · 💬 159</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amasad/status/2063344460705288401">View @amasad on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“When I spoke out against the Gaza genocide, a bunch of midwit VCs ganged up on me both in public and tried to hurt me in private too. Many of those who stood by me were also VCs. Just the better ones.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>CEO ของ Replit โพสต์เรื่องส่วนตัวว่าถูก VC กลุ่มหนึ่งโต้กลับหลังออกมาต้านสงคราม Gaza และมองว่าการยืนหยัดในจุดยืนช่วย filter คนออกเองตามธรรมชาติ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amasad/status/2063344460705288401" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4813 · 💬 94</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2063158974644629929">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“He just turned it on and the battery is already dead https://t.co/1x0EBiDGwt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@theo โพสต์มุกตลกหนึ่งบรรทัดว่า 'เพิ่งเปิดเครื่องแบตก็หมดแล้ว' ไม่มีบริบทหรือหัวข้อ technical ใดระบุ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2063158974644629929" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4149 · 💬 206</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2063016208065327500">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Google is now paying SpaceX nearly $1 billion every month for compute. Yes, Google is paying SpaceX for compute. They're that desperate.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google จ่ายเงิน SpaceX ราว $1B ต่อเดือนสำหรับ compute เพราะ infrastructure ตัวเองรองรับ AI demand ไม่ทัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2063016208065327500" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnthropicAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3427 · 💬 232</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnthropicAI/status/2062979607448682731">View @AnthropicAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New Anthropic Science Blog: Making Claude a chemist. To manipulate a molecule, chemists first need to understand its structure. Their main tool is NMR spectroscopy. We found Opus 4.7 matches—and on so”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Anthropic เผย blog ว่า Claude Opus 4.7 ทำได้เทียบเท่าหรือดีกว่า software NMR spectroscopy เฉพาะทาง สำหรับงานวิเคราะห์โมเลกุลทางเคมี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AnthropicAI/status/2062979607448682731" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gdb</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2596 · 💬 230</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gdb/status/2063437915347136554">View @gdb on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Whenever I don’t use codex for a task, I ask myself why and usually realize that there’s some missing context, I needed to write a skill, or I just didn’t think to use it. Rarely is it because the tas”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Greg Brockman (OpenAI) บอกว่าที่ไม่ใช้ Codex มักเป็นเพราะขาด context, ยังไม่มี skill หรือลืมใช้ — แทบไม่ใช่เพราะ model ทำไม่ได้ — และระบุว่า adoption overhang ยังสูงมาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>อุปสรรคของ AI coding คือ workflow และนิสัยการใช้ ไม่ใช่ความสามารถ model — แก้ด้วยการปรับ process ทีม ไม่ใช่รอ model ดีกว่านี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดูว่างานประจำใดในทีมยังรัน manual แล้วเขียน context/skill เพิ่มเพื่อส่งผ่าน Codex หรือ AI tool ที่ใช้อยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gdb/status/2063437915347136554" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1820 · 💬 207</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2063046400095752358">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Another solid payout, not bad considering how little I’ve been on here the last 2 weeks https://t.co/nlusuc1xLw”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@theo โพสต์ว่าได้รับ payout จาก X creator program ดีพอสมควร แม้จะแทบไม่ได้โพสต์ใน 2 สัปดาห์ที่ผ่านมา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2063046400095752358" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Polymarket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1744 · 💬 169</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Polymarket/status/2063441528232501549">View @Polymarket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“JUST IN: Chinese startup Monako unveils smart glasses built to run AI coding agents like Claude Code &amp;amp; Codex. https://t.co/nWiaPdjyhZ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>สตาร์ทอัพจีน Monako เปิดตัว smart glasses ที่รัน AI coding agents อย่าง Claude Code และ Codex ได้โดยตรงบนตัวอุปกรณ์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Hardware สวมใส่ที่รัน coding agents แบบ hands-free คือ form factor ใหม่สำหรับ developer — สัญญาณว่า AI devtools กำลังออกนอก desktop</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action — ติดตามความพร้อมวางจำหน่ายและรีวิวจริงก่อน ค่อยประเมินว่า form factor นี้เหมาะกับ workflow ของทีมหรือเปล่า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Polymarket/status/2063441528232501549" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
