---
type: social-topic-report
date: '2026-06-04'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-04T03:19:51+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 227
salience: 0.55
sentiment: mixed
confidence: 0.58
tags:
- gemma4
- ollama
- claude-code
- agent-workflows
- ai-pricing
- local-models
thumbnail: https://pbs.twimg.com/media/HJ7Xa8yawAAAHgy.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-04

## TL;DR
- Google ปล่อย Gemma 4 12B โมเดล multimodal แบบ encoder-free รันได้บน local ผ่าน Ollama (`ollama run gemma4:12b-mlx`) และใช้เป็น backend ของ Claude Code ได้ [14][16]
- Anthropic เปลี่ยน trigger ของ Claude Code dynamic-workflow จาก "workflow" เป็น "ultracode" เพื่อลดการเรียกใช้โดยไม่ตั้งใจ โดย "use a workflow for this" ยังคงทำงานได้ [2]
- Anthropic เผย best practices สำหรับสร้าง Claude data-analysis agent ครอบคลุมเรื่อง skills, data foundations, และ evaluations [5]
- Claude "Mythos" รายงานว่าทำ METR 80%-task horizon ได้ที่ 3-4 ชั่วโมง ซึ่งตรงกับที่ superforecasters คาดไว้สำหรับสิ้นปีตั้งแต่ต้นพฤษภาคม [34]
- การกำหนดเพดานค่าใช้จ่าย AI กลายเป็นสัญญาณซ้ำๆ ในวันนี้: Uber $1,500/เดือน, T-Mobile พยายามลดเหลือ $30/เดือน (จาก $2,000) และผู้ใช้ภายในสูงสุดของ OpenAI ใช้ไปราว 100B tokens/เดือน [9][37][39][51]

## สิ่งที่เกิดขึ้น
Artifacts ที่จับต้องได้ในรอบนี้มีจำกัดแต่เป็นของจริง Google ส่ง Gemma 4 12B ซึ่งอธิบายว่าเป็น unified encoder-free multimodal model [14] พร้อมให้ใช้งานผ่าน Ollama ในวันเดียวกัน รวมถึง MLX build และ launch path สำหรับ Claude Code [16] Anthropic เคลื่อนไหวฝั่ง developer สองเรื่อง: เปลี่ยน trigger ของ Claude Code dynamic-workflow จาก "workflow" เป็น "ultracode" เพื่อลด false trigger [2] และเผย best practices สำหรับสร้าง Claude agent ที่ทำ business/data analysis โดยเน้นเรื่อง skills, data foundations, และ evaluations [5] ด้าน research/benchmark มีรายงานว่า Claude "Mythos" ทำ METR 80% task-completion horizon ได้ที่ 3-4 ชั่วโมง เร็วกว่าที่คาด [34] และ autonomous research agent ของ OpenAI ชื่อ "Aiden" รายงานว่ารันต่อเนื่อง 22 วัน และทำคะแนนเหนือผู้สมัครทั้ง 1,016 คนใน "Parameter Golf" hiring challenge [44] นอกจากนี้ยังมี prompt/agent pattern จาก Anthropic engineer แพร่กระจายออกมา: "สร้าง system ที่ prompt ตัวเอง" แทนที่จะ hand-prompt Claude [49]

## ทำไมถึงสำคัญ (เหตุผล)
สัญญาณที่ใช้ได้จริงสำหรับ studio คือ local + multimodal + ถูก Gemma 4 12B รันผ่าน Ollama พร้อม MLX build หมายความว่าโมเดล multimodal ระดับ 12B อยู่บน developer laptop ได้ พร้อม integration path กับ Claude Code [16] — เกี่ยวข้องโดยตรงกับการ prototype offline, ทำความเข้าใจ asset/image, และประหยัดค่า cloud token สิ่งนี้โยงตรงไปยังธีมที่สอง: สัญญาณที่ดังที่สุดในวันนี้ (ไม่นับ astrology และ finance) คือวินัยด้านค่าใช้จ่าย AI เพดาน $1,500/เดือนของ Uber, การพยายามลดเหลือ $30/เดือนของ T-Mobile, และผู้ใช้ 100B-token ของ OpenAI [9][37][39][51] ล้วนชี้ว่าผู้ซื้อกำลังคุม AI budget เข้มขึ้น ทำให้โมเดล local มีความหมายมากกว่าแค่ของเล่น การเปลี่ยนชื่อ workflow trigger [2] และ post เรื่อง analytics skills [5] ของ Anthropic แสดงให้เห็นว่า Claude tooling surface ยังขยับทุกเดือน จึงต้องดูแล prompt/skill setup ต่อเนื่อง กรอบคิด "system ที่ prompt ตัวเอง" [49] และผลลัพธ์ของ Aiden/Mythos [34][44] เป็นหลักฐานเบื้องต้นว่าหน่วยงานปฏิบัติจริงกำลังเลื่อนจาก single prompt ไปสู่ agent loop ที่รันนานขึ้น — เป็นทิศทางที่มีประโยชน์ แต่มาในรูปแบบ tweet ไม่ใช่ artifact ที่ reproduce ได้

## ความเป็นไปได้
**น่าจะเกิด:** Gemma 4 12B จะได้รับ community tooling และ quantized variant อย่างรวดเร็วเมื่อมี Ollama day-one support และ MLX build [16] **เป็นไปได้:** การ churn ของ Claude Code config จะตามหลังการเปลี่ยนชื่อ "ultracode" ดังนั้น trigger word ใดๆ ที่เขียน script ไว้จะต้องตรวจสอบเป็นระยะ [2] **เป็นไปได้:** AI vendors และองค์กรจะยังเคลื่อนไปสู่การกำหนด hard per-seat token cap ต่อไป ดัน team ให้ผสม local model กับ cloud [9][37][39] **ยากจะยืนยันเร็วๆ นี้:** Mythos 3-4h horizon [34] และชัยชนะ 22 วันของ Aiden [44] — ทั้งสองเป็น single-source claim ไม่มี methodology ที่ link มาด้วย ใช้เป็นทิศทางเท่านั้น อย่าถือเป็นที่ยืนยัน ไม่มี source ใดให้ตัวเลข probability จึงไม่ระบุไว้

## ความเกี่ยวข้องกับ NDF DEV
1) ดึง Gemma 4 12B ลง local และ benchmark สำหรับการทำความเข้าใจ image/asset และ offline prototyping รวมถึง launch path ของ Claude Code — effort ต่ำ/กลาง [14][16] 2) อัพเดต script, docs, หรือ team notes ของ Claude Code ที่อ้างถึง trigger "workflow" เพราะ dynamic trigger เปลี่ยนเป็น "ultracode" แล้ว — effort ต่ำ [2] 3) อ่าน post analytics-agent ของ Anthropic ก่อนสร้าง e-learning/edutech data-analysis agent ใดๆ โดยเฉพาะส่วน skills + evaluations — effort ต่ำ [5] 4) ทดลอง pattern "system ที่ prompt ตัวเอง" กับงานภายในที่ทำซ้ำได้หนึ่งชิ้น เช่น build/QA summary แทน ad-hoc prompting — effort กลาง [49] 5) นำค่าใช้จ่าย AI tool เข้าไปใน budgeting review เมื่อเห็น cost cap จากหลาย vendor ที่ชัดเจน; เลือก local model สำหรับงาน volume สูงแต่ risk ต่ำ [9][37][39] ข้ามได้เลย: IPO/valuation และการถกเถียงเรื่อง AI-bubble [3][4][11][13][55], ทุก item เรื่อง astrology/tarot, และ post ศิลปะ Claude Monet — ไม่เกี่ยวกับ workflow เลย

## Signals to Watch
- Quantization, fine-tune, และ Ollama agent recipe (Hermes/Claude Code) ของ Gemma 4 12B ในช่วงวันข้างหน้า [16]
- การเปลี่ยน trigger/config ของ Claude Code เพิ่มเติมหลังการเปลี่ยนชื่อ "ultracode" [2]
- METR Mythos horizon [34] และ Aiden benchmark [44] จะมี write-up ที่ reproduce ได้หรือยังคงอยู่แค่ใน tweet
- Enterprise AI per-seat token cap ในฐานะ pricing trend (Uber, T-Mobile, OpenAI) ที่กระทบ tool budget [9][37][39][51]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **duanebester/gooey** — Gooey: A GPU-accelerated UI framework for Zig | radar | <https://github.com/duanebester/gooey> |
| **chopratejas/headroom** — Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens | rss | <https://github.com/chopratejas/headroom> |
| **NousResearch/hermes-agent** — The agent that grows with you Hermes Agent ☤ The self-improving AI agent built by Nous Research | rss | <https://github.com/NousResearch/hermes-agent> |
| **microsoft/markitdown** — Python tool for converting files and office documents to Markdown | rss | <https://github.com/microsoft/markitdown> |
| **nesquena/hermes-webui** — Hermes WebUI: The best way to use Hermes Agent from the web or from your phone | rss | <https://github.com/nesquena/hermes-webui> |
| **D4Vinci/Scrapling** — 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale | rss | <https://github.com/D4Vinci/Scrapling> |
| **odoo/odoo** — Odoo. Open Source Apps To Grow Your Business | rss | <https://github.com/odoo/odoo> |
| **Open-LLM-VTuber/Open-LLM-VTuber** — Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D | rss | <https://github.com/Open-LLM-VTuber/Open-LLM-VTuber> |
| **HKUDS/Vibe-Trading** — "Vibe-Trading: Your Personal Trading Agent" English / 中文 / 日本語 / 한국어 / العربية | rss | <https://github.com/HKUDS/Vibe-Trading> |
| **0x4m4/hexstrike-ai** — HexStrike AI MCP Agents: advanced MCP server สำหรับ AI agent (Claude, GPT, Copilot ฯลฯ) | rss | <https://github.com/0x4m4/hexstrike-ai> |
| **interviewstreet/hiring-agent** — AI agent สำหรับประเมินและให้คะแนน resume — pipeline แบบ resume-to-score | rss | <https://github.com/interviewstreet/hiring-agent> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | duragactivitty | ^3406 c21 | [niggas get on claude and make any website](https://x.com/duragactivitty/status/2062272669211308046) |
| x | ClaudeDevs | ^3231 c183 | [We've changed the trigger word from "workflow" to "ultracode". You can still say](https://x.com/ClaudeDevs/status/2062257177788858398) |
| x | KobeissiLetter | ^2742 c151 | [BREAKING: Anthropic has picked Morgan Stanley and Goldman Sachs to lead its upco](https://x.com/KobeissiLetter/status/2062296014879383922) |
| x | rdd147 | ^2401 c116 | [🚨 Sam Altman warns OpenAi and Anthropic are experiencing severe pullback on Ai s](https://x.com/rdd147/status/2062253781438624051) |
| x | ClaudeDevs | ^1256 c33 | [How do we automate business analytics with Claude? New blog post covering our be](https://x.com/ClaudeDevs/status/2062274312363770064) |
| x | GreenIrisTarot | ^1132 c6 | [˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — blessings upcoming! 💝](https://x.com/GreenIrisTarot/status/2062238216258727991) |
| x | aleabitoreddit | ^1124 c225 | [Just some random notes about $AVGO earnings transcript - Revenue target reiterat](https://x.com/aleabitoreddit/status/2062322546809381094) |
| x | ThierryBorgeat | ^1105 c92 | [🚨 We may be looking at the rarest market setup in 50 years. The S&P 500's four h](https://x.com/ThierryBorgeat/status/2062261038662427125) |
| x | edzitron | ^1010 c34 | [Hearing that T-Mobile attempted to limit its Claude enterprise users to as littl](https://x.com/edzitron/status/2062226951054467276) |
| x | sunlithetarot | ^987 c0 | [mutable signs (gemini, virgo, sagittarius, pisces), stay devoted to your dreams,](https://x.com/sunlithetarot/status/2062238974790570211) |
| x | BullTheoryio | ^938 c99 | [BREAKING: Ray Dalio just said the AI market is a bubble and it will burst. "All](https://x.com/BullTheoryio/status/2062247647592018351) |
| x | JV_F1 | ^892 c36 | [I'm really happy to share with you all how we will be showing up in Monaco this](https://x.com/JV_F1/status/2062259853176037490) |
| x | edzitron | ^805 c24 | [OpenAI is absolutely cooked. This is loser language. You can't be four years int](https://x.com/edzitron/status/2062349145264828551) |
| radar | rvz | ^721 c296 | [Gemma 4 12B: A unified, encoder-free multimodal model](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) |
| x | Polymarket | ^703 c56 | [JUST IN: Anthropic has reportedly tapped Morgan Stanley & Goldman Sachs to l](https://x.com/Polymarket/status/2062233732770103624) |
| x | ollama | ^676 c32 | [.@GoogleDeepMind's Gemma 4 - 12B is available on Ollama! Chat: ollama run gemma4](https://x.com/ollama/status/2062250522598572345) |
| x | amitisinvesting | ^656 c83 | [A TON OF THINGS HAPPENED IN THE STOCK MARKET TODAY. Here's a full recap: 1. $BTC](https://x.com/amitisinvesting/status/2062356758069498362) |
| x | zerohedge | ^653 c71 | [*BROADCOM: WORK WITH APOLLO, BLACKSTONE SERVES OPENAI, ANTHROPIC Translation: Br](https://x.com/zerohedge/status/2062296977614778371) |
| x | kimmonismus | ^635 c44 | [Im confused. And excited at the same time. I got the feeling OpenAI is preparing](https://x.com/kimmonismus/status/2062258181624016927) |
| x | tszzl | ^621 c144 | [I think you can make an equally convincing argument that waymo, claude, and the](https://x.com/tszzl/status/2062309538548859153) |
| x | JRSmith42091575 | ^601 c11 | [Me and one of my boys share a Claude account and he is actually cooked in life #](https://x.com/JRSmith42091575/status/2062239605319954847) |
| radar | cloud8421 | ^591 c222 | [Elixir v1.20: Now a gradually typed language](https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/) |
| radar | Tomte | ^519 c161 | [I was recently diagnosed with anti-NMDA receptor encephalitis](https://burntsushi.net/encephalitis/) |
| x | buildincrisis | ^513 c7 | [if anthropic had dropped Mythos today, it still wouldn't have been the best mode](https://x.com/buildincrisis/status/2062279290377380050) |
| x | OxfordAnalytics | ^487 c70 | [The AI Bubble is being driven by the fantasy that AI can replace human labour co](https://x.com/OxfordAnalytics/status/2062245841839006112) |
| x | StockSavvyShay | ^475 c22 | [$AVGO said the company entered an agreement to give Anthropic access to another](https://x.com/StockSavvyShay/status/2062307814207598761) |
| x | sunlithetarot | ^472 c0 | [🔮🪄 • blessings in the next 48 hrs. ♈ aries: happiness ♉ taurus: extra money ♊ ge](https://x.com/sunlithetarot/status/2062238824529555849) |
| x | Layyenne | ^461 c37 | [Someone in the comments used Gemini Which one got it better between the two??? @](https://x.com/Layyenne/status/2062230083889225909) |
| x | astroinrealtime | ^453 c11 | [stop guessing how they feel, gemini. ask them directly.](https://x.com/astroinrealtime/status/2062278176512852248) |
| x | Havenlust | ^441 c4 | [Claude Monet https://t.co/OmCsKFV6co](https://x.com/Havenlust/status/2062310359508328464) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@duragactivitty</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3406 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/duragactivitty/status/2062272669211308046">View @duragactivitty on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“niggas get on claude and make any website”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ไวรัลชมว่า Claude สร้างเว็บได้ง่าย แต่ไม่มีรายละเอียดทางเทคนิคใด ๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/duragactivitty/status/2062272669211308046" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ClaudeDevs</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3231 · 💬 183</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ClaudeDevs/status/2062257177788858398">View @ClaudeDevs on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We've changed the trigger word from &quot;workflow&quot; to &quot;ultracode&quot;. You can still say &quot;use a workflow for this&quot;, but when you're clearly referring to something else, Claude won't kick off a dynamic workflo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Claude Code เปลี่ยน keyword trigger dynamic multi-agent workflow จาก 'workflow' เป็น 'ultracode' แล้ว — วลี 'use a workflow for this' ยังใช้ได้เหมือนเดิม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่เคยพิมพ์ 'workflow' เพื่อ trigger orchestration จะไม่ได้ผลอีกต่อไป — keyword เปลี่ยนแบบไม่มี warning</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ปรับ habit การ prompt Claude Code ในทีม — ใช้ 'ultracode' แทนเมื่อต้องการ trigger multi-agent workflow จริงๆ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ClaudeDevs/status/2062257177788858398" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KobeissiLetter</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2742 · 💬 151</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KobeissiLetter/status/2062296014879383922">View @KobeissiLetter on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“BREAKING: Anthropic has picked Morgan Stanley and Goldman Sachs to lead its upcoming IPO, per Bloomberg. Anthropic was valued at $965 billion in its latest funding round, officially surpassing OpenAI’”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Anthropic เลือก Morgan Stanley และ Goldman Sachs นำ IPO หลังถูกประเมินมูลค่า $965B แซง OpenAI เป็นครั้งแรก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KobeissiLetter/status/2062296014879383922" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rdd147</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2401 · 💬 116</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rdd147/status/2062253781438624051">View @rdd147 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 Sam Altman warns OpenAi and Anthropic are experiencing severe pullback on Ai spending as companies put significant restraints on spending to restrict costs. The company warns investors it’s the firs”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ที่ไม่มีแหล่งอ้างอิงอ้างว่า Sam Altman เตือนนักลงทุนว่า OpenAI และ Anthropic เจอ enterprise ลด AI spending เพราะ cost ไม่คุ้ม — โพสต์นี้เป็น stock market commentary ($SOXX $DRAM)</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rdd147/status/2062253781438624051" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ClaudeDevs</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1256 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ClaudeDevs/status/2062274312363770064">View @ClaudeDevs on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“How do we automate business analytics with Claude? New blog post covering our best practices for skills, data foundations, and evaluations when building agents to perform data analysis: https://t.co/m”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@ClaudeDevs ออก blog post ว่าด้วย best practices สำหรับสร้าง Claude agent วิเคราะห์ข้อมูล ครอบคลุม skills design, data foundations, และ evaluation</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Pattern ของ evaluation และ skills layering ใช้ได้กับ Claude agent ทุกตัวที่ studio สร้าง ไม่ใช่แค่ analytics</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">อ่าน blog post แล้วดึง evaluation framework มาวัด performance ของ Claude agent ที่ studio ใช้งานอยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ClaudeDevs/status/2062274312363770064" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GreenIrisTarot</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1132 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GreenIrisTarot/status/2062238216258727991">View @GreenIrisTarot on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — blessings upcoming! 💝 • lucky timing. being at the right place at the right time over and over again • invitations to celebrations, weddings, ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บัญชี tarot โพสต์คำทำนายดวงชะตาสำหรับราศีเมถุน, กันย์, ธนู, และมีน เรื่องโชคและการรวมตัว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GreenIrisTarot/status/2062238216258727991" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aleabitoreddit</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1124 · 💬 225</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aleabitoreddit/status/2062322546809381094">View @aleabitoreddit on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just some random notes about $AVGO earnings transcript - Revenue target reiterated ($100B+ 2027, pretty sure markets wanted that to be raised this earning, hence the drop) Remember $NVDA Jensen commen”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Broadcom รายงานผลประกอบการยืนเป้า $100B+ ปี 2027 (ไม่ปรับขึ้น) — margin ฝั่ง AI networking ยังสูง แต่ TPU margin หดลงตามสเกล ออร์เดอร์มองเห็นถึงปี 2028</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aleabitoreddit/status/2062322546809381094" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ThierryBorgeat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1105 · 💬 92</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ThierryBorgeat/status/2062261038662427125">View @ThierryBorgeat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 We may be looking at the rarest market setup in 50 years. The S&amp;P 500's four historic drawdowns since 1972: – 1973 Inflation: -43% – 1987 Liquidity: -30% – 2000 Tech: -47% – 2008 Credit: -55% Each o”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิเคราะห์ชี้ว่าปี 2026 มีปัจจัยเสี่ยงตลาดทั้ง 4 พร้อมกันครั้งแรกในรอบ 50 ปี ทั้ง inflation, liquidity shock, tech bubble, และ credit freeze</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ThierryBorgeat/status/2062261038662427125" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
