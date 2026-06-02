---
type: social-topic-report
date: '2026-06-02'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-02T03:09:56+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 232
salience: 0.5
sentiment: mixed
confidence: 0.6
tags:
- ai-tools
- codex
- aws-bedrock
- gemini
- claude-code
- agent-guidelines
thumbnail: https://pbs.twimg.com/media/HJwjcVPa0AAbIDS.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-02

## TL;DR
- frontier models และ Codex ของ OpenAI พร้อมให้ใช้งานแบบ generally available บน Amazon Bedrock แล้ว พร้อม security/compliance/governance controls ของ AWS [5][36][43]
- OpenAI จัด livestream วันนี้ (อังคาร 6/2, 8:30am PT) preview Codex และ OpenAI platform updates [26]
- Google ประกาศ Gemini Omni สำหรับ conversational video editing — แก้ action ในวิดีโอด้วยการพิมพ์คำสั่ง [45]; Gemini API เพิ่ม usage breakdown แบบแยกรายเดือน per-API-key [55]
- Stanford CS336 'Language Modeling from Scratch' เปิดสาธารณะแล้ว และ repo มี CLAUDE.md รวม AI-agent guidelines ที่นำไปใช้ต่อได้ [46][54]
- Anthropic reset rate limits ของ Pro/Max ทั้งหมดพร้อมกัน; สาเหตุที่อ้าง (Opus 4.8 'spawning parallel agents') ยังไม่ได้รับการยืนยัน [52][35]

## สิ่งที่เกิดขึ้น
มี platform release ที่จับต้องได้สองรายการ OpenAI นำ frontier models และ Codex ขึ้น Amazon Bedrock แบบ generally available เพื่อเปิดทางให้องค์กรที่ใช้ AWS governance อยู่แล้วสร้าง agent และ software-engineering workflows ได้ [5][36][43] พร้อมมี OpenAI livestream วันนี้เพื่อ preview Codex/platform updates เพิ่มเติม [26] ฝั่ง Google มีการ demo Gemini Omni ทำ conversational video editing [45] และ Gemini API ได้รับ per-API-key usage filtering [55] ด้าน artifacts และการเรียนรู้ Stanford CS336 เปิดสาธารณะแล้ว [46] และ assignment repo มี CLAUDE.md ที่กำหนด AI-agent guidelines สำหรับนำไปใช้เป็น pattern ได้ [54] marketing site ของ Anthropic ถูก rewrite ด้วย TanStack พร้อม data precaching [21] และ Anthropic reset rate limits ของ Pro/Max พร้อมกันทั้งหมด [52][35] ส่วน item ที่มี engagement สูงส่วนใหญ่วันนี้ไม่ใช่ tooling ได้แก่ คดี Florida ฟ้อง OpenAI/Altman [1][24][33][51][59] ข่าว IPO และ valuation ของ Anthropic/OpenAI [15][20][23][37][53] การเปิดตัว Stargate data center [25][38][39] รวมถึง noise จากดูดวงและ gaming leak [12][17][29][6][7][8][32]

## ทำไมถึงสำคัญ (เหตุผล)
Bedrock GA สำคัญเพราะทีมสามารถใช้ OpenAI models และ Codex ภายใน AWS account ที่มีอยู่ได้เลย พร้อม IAM, logging และ compliance posture ของ account นั้น แทนที่จะทำสัญญาแยกกับ OpenAI [5][36][43] — เกี่ยวข้องถ้า NDF DEV host อยู่บน AWS อยู่แล้ว Gemini API per-key breakdown เป็นการปรับปรุงการจัดสรรค่าใช้จ่ายขนาดเล็กแต่จริง: แยก spend ตาม project/key ได้แล้ว [55] ซึ่งช่วยป้องกันบิลเกินโดยไม่รู้ตัวจากหลาย client app CLAUDE.md ของ CS336 คือ artifact ที่นำไปใช้ต่อได้ตรงที่สุด: ตัวอย่าง agent guardrails สำหรับ codebase ที่ทีมนำไปปรับใช้กับ Unity/web repos ของตัวเองได้ [54] การ reset rate limit เป็นสัญญาณเตือนเชิงปฏิบัติการ — ถ้า studio พึ่งพา Claude Pro/Max สำหรับ coding รายวัน การเปลี่ยน quota ฝั่ง vendor สามารถขัดจังหวะการทำงานได้ และสาเหตุที่ระบุยังเป็นแค่ข่าวลือ [52][35] ส่วน second-order: noise เรื่องกฎหมายและ IPO [1][53] บ่งชี้ความเข้มข้นของการตรวจสอบและแรงกดดันด้านราคาต่อ model vendors ซึ่งจะส่งผลต่อต้นทุน API และเงื่อนไขในระยะยาว แต่ไม่มี item ใดวันนี้ที่ quantify ได้

## ความเป็นไปได้
มีแนวโน้มสูง: livestream OpenAI วันนี้จะ ship Codex/platform updates ที่เป็นรูปธรรม เนื่องจากประกาศอย่างเป็นทางการแล้ว [26] คาดรายละเอียดตามมาภายในไม่กี่ชั่วโมง มีแนวโน้มสูง: model provider รายอื่นจะรวมตัวเข้า hyperscaler marketplace ต่อไป เพราะ OpenAI-on-Bedrock เป็น pattern เดียวกับที่ AWS มีให้ Anthropic อยู่แล้ว [5][43] เป็นไปได้: Gemini Omni video editing จะใช้งานได้จริงสำหรับ content การตลาด/edutech ถ้าถึง general availability แต่ item ปัจจุบันแสดงแค่ demo ยังไม่มีรายละเอียดการเข้าถึง [45] เป็นไปได้: มี model drop ใกล้ ๆ นี้ จาก dev account ที่น่าเชื่อถือ tease ไว้ [28] แต่ยังไม่ยืนยัน ไม่น่ากระทบ tooling ระยะใกล้: คดี Florida และข่าว IPO ครอง engagement แต่เป็นเรื่องกฎหมาย/การเงิน ไม่ใช่ product [1][53]

## การประยุกต์ใช้กับองค์กร — NDF DEV
1) ถ้า NDF DEV host อยู่บน AWS ให้ประเมิน OpenAI-on-Bedrock สำหรับ internal coding/agent task หนึ่งงาน เพื่อเปรียบต้นทุนและ governance กับ direct API — effort: med [5][36] 2) Copy CLAUDE.md ของ CS336 เป็น template เริ่มต้นสำหรับ agent guidelines ใน Unity และ web/mobile repos — effort: low [54]; จับคู่กับ CS336 สำหรับ team member ที่ต้องการ upskill ด้าน LLM internals [46] 3) ติดตาม OpenAI livestream วันนี้และบันทึก Codex changes ที่กระทบ coding workflow — effort: low [26] 4) ถ้าใช้ Gemini API ข้ามหลาย client project ให้เปิด per-API-key usage filtering เพื่อจัดสรรค่าใช้จ่าย — effort: low [55] 5) บันทึก Codex voice/notify-when-blocked trick สำหรับ agent run ที่ใช้เวลานาน — effort: low [40] 6) ถือว่า Claude Pro/Max quota เปลี่ยนแปลงได้และเตรียม fallback ไว้ถ้า coding พึ่งพาอยู่ [52][35] — effort: low ข้ามได้เลย: คดีความ, IPO/valuation, Stargate, Jensen quote, ดูดวง/gaming [1][24][53][25][9][29]

## Signals to Watch
- OpenAI livestream วันนี้สำหรับ Codex/platform updates — ดูผลในวันเดียวกัน [26]
- Gemini Omni video-editing — รอประกาศ access/GA ก่อนวางแผนใช้กับ content [45]
- model drop ที่ tease ไว้จาก dev account ที่น่าเชื่อถือ — ยังไม่ยืนยัน [28]
- CLAUDE.md ของ CS336 ในฐานะ portable agent-guideline pattern ที่นำมา adopt และปรับแต่งได้ [54]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **stanford-cs336/assignment1-basics** — AI Agent Guidelines for CS336 at Stanford | radar | <https://github.com/stanford-cs336/assignment1-basics> |
| **cyberpapiii/chipotlai-max** — Chipotlai Max | radar | <https://github.com/cyberpapiii/chipotlai-max> |
| **microsoft/markitdown** — Python tool for converting files and office documents to Markdown.MarkItDown Important MarkItDown pe | rss | <https://github.com/microsoft/markitdown> |
| **nesquena/hermes-webui** — Hermes WebUI: The best way to use Hermes Agent from the web or from your phone!Hermes Web UI Hermes  | rss | <https://github.com/nesquena/hermes-webui> |
| **supermemoryai/supermemory** — Memory engine and app that is extremely fast, scalable. The Memory API for the AI era. State-of-the- | rss | <https://github.com/supermemoryai/supermemory> |
| **harry0703/MoneyPrinterTurbo** — 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. MoneyPrinterTurbo 💸 简体中文 / Engl | rss | <https://github.com/harry0703/MoneyPrinterTurbo> |
| **D4Vinci/Scrapling** — 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale  | rss | <https://github.com/D4Vinci/Scrapling> |
| **pbakaus/impeccable** — The design language that makes your AI harness better at design.Impeccable The vocabulary you didn't | rss | <https://github.com/pbakaus/impeccable> |
| **p-e-w/heretic** — Fully automatic censorship removal for language models Heretic: Fully automatic censorship removal f | rss | <https://github.com/p-e-w/heretic> |
| **EveryInc/compound-engineering-plugin** — Official Compound Engineering plugin for Claude Code, Codex, Cursor, and moreCompound Engineering AI | rss | <https://github.com/EveryInc/compound-engineering-plugin> |
| **TauricResearch/TradingAgents** — TradingAgents: Multi-Agents LLM Financial Trading Framework Deutsch / Español / français / 日本語 / 한국어 | rss | <https://github.com/TauricResearch/TradingAgents> |
| **revfactory/harness** — A meta-skill that designs domain-specific agent teams, defines specialized agents, and generates the | rss | <https://github.com/revfactory/harness> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | CultureCrave | ^10142 c121 | [Florida is suing OpenAI and CEO Sam Altman • The lawsuit alleges OpenAI exploite](https://x.com/CultureCrave/status/2061562509543547072) |
| x | BobbyBorkIII | ^3861 c64 | [The year is 2040. OpenAI has digitized Trump's brain to serve as President for a](https://x.com/BobbyBorkIII/status/2061527378757652524) |
| x | Vivek4real_ | ^3508 c44 | [JENSEN HUANG SAID THAT ELON MUSK WAS THERE FOR HIM AS A CUSTOMER AT A TIME WHEN ](https://x.com/Vivek4real_/status/2061503291457224757) |
| x | allenanalysis | ^3327 c81 | [🚨 THIS IS THE ENTIRE AI INDUSTRY'S NIGHTMARE IN ONE QUOTE. An author suing OpenA](https://x.com/allenanalysis/status/2061504329266176362) |
| x | OpenAI | ^3157 c183 | [OpenAI frontier models and Codex are now generally available on AWS, giving ente](https://x.com/OpenAI/status/2061564502160892138) |
| x | RevivalOfPotara | ^2983 c8 | [Not believing leaks because they involve sonic getting a new model they can't cr](https://x.com/RevivalOfPotara/status/2061560378602168792) |
| x | sgaygirlwhosafn | ^2874 c20 | [the leaker -had new unseen footage of jsr -screenshot of the new streets of rage](https://x.com/sgaygirlwhosafn/status/2061536911286530270) |
| x | Danny8bit | ^1842 c18 | [everyone collectively going "Sonic getting a new model?? Lmao hell nah, this dud](https://x.com/Danny8bit/status/2061557462013264046) |
| x | DeFiTracer | ^1754 c95 | [🚨 BREAKING: NVIDIA CEO JENSEN HUANG JUST SAID LIVE ON CNBC: "INVESTING IN SPACEX](https://x.com/DeFiTracer/status/2061557363971137567) |
| radar | ssiddharth | ^1392 c332 | [The newest Instagram "exploit" is the goofiest I've seen](https://www.0xsid.com/blog/meta-account-takeover-fiasco) |
| x | Sportsnet | ^1386 c8 | [Frederik Andersen speaks on Claude Lemieux reaching out to him before he accepte](https://x.com/Sportsnet/status/2061524267796246779) |
| x | hourIyhoroscope | ^1385 c36 | [stay calm, gemini.](https://x.com/hourIyhoroscope/status/2061501026931298700) |
| x | kevinroose | ^1252 c48 | [the first time i visited Anthropic it was a 160-person start-up in Jackson Squar](https://x.com/kevinroose/status/2061526831682236656) |
| x | sama | ^1232 c268 | [The OpenAI Foundation is doing a lot of wonderful things. Helping society become](https://x.com/sama/status/2061562575322492937) |
| x | unusual_whales | ^1185 c148 | [Salesforce, $CRM, has a stake in Anthropic worth about $5 billion, per Bloomberg](https://x.com/unusual_whales/status/2061527450723504375) |
| x | higgsfield | ^1157 c63 | [Claude is now your real estate marketing agency. Analyze listings from Airbnb, B](https://x.com/higgsfield/status/2061520692756332677) |
| x | GreenIrisTarot | ^1151 c4 | [˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — random upcoming predic](https://x.com/GreenIrisTarot/status/2061510590816747592) |
| x | jiewfritty | ^958 c0 | [forgetting the lyrics after making eye contact with fourth 😭 gemini norawit you'](https://x.com/jiewfritty/status/2061511107551101189) |
| x | _Crypto_Barbie | ^938 c30 | [⚠️ JUST IN: CRYPTO EXCHANGE GEMINI SAYS „CLARITY ACT IS VERY CLOSE TO GETTING DO](https://x.com/_Crypto_Barbie/status/2061535561261649979) |
| x | FocusedCompound | ^923 c11 | [Just got hold of the sell-side analysis for the eventual Anthropic IPO https://t](https://x.com/FocusedCompound/status/2061542585198366958) |
| x | theo | ^916 c46 | [Confirmed rewrite with Tanstack and a bunch of data precaching. Great work Anthr](https://x.com/theo/status/2061563106208432223) |
| x | AmonSyd | ^852 c9 | [New oc Claude SCP 049 🔥 He is the cure 👁️ https://t.co/t8vQOeqbYk](https://x.com/AmonSyd/status/2061588248292458650) |
| x | tenobrus | ^847 c23 | [buying into the anthropic IPO at $1T valuation would obviously be an incredible ](https://x.com/tenobrus/status/2061568991949381850) |
| x | ProudSocialist | ^847 c39 | [New: The state of Florida is suing OpenAI and its CEO Sam Altman for prioritizin](https://x.com/ProudSocialist/status/2061516106586615891) |
| x | Polymarket | ^831 c94 | [NEW: OpenAI officially breaks ground on its 1,000,000,000-watt Stargate data cen](https://x.com/Polymarket/status/2061546785823146185) |
| x | derrickcchoi | ^807 c17 | [Come join our livestream tomorrow where we'll preview some exciting updates to t](https://x.com/derrickcchoi/status/2061515948503269572) |
| x | Yuchenj_UW | ^761 c98 | [OpenAI slept on coding, so Anthropic stole the crown. Anthropic didn't secure en](https://x.com/Yuchenj_UW/status/2061505386797232209) |
| x | thdxr | ^712 c62 | [i don't usually do the whole "this new model changes everything" but i am very i](https://x.com/thdxr/status/2061606433292976613) |
| x | niyetsel | ^709 c1458 | [IF I WERE YOU, I WOULDN'T IGNORE THIS! Write your number according to your zodia](https://x.com/niyetsel/status/2061607124694868077) |
| x | Havenlust | ^648 c5 | [Claude Monet https://t.co/3RnSicJzSd](https://x.com/Havenlust/status/2061570484613841168) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CultureCrave</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 10142 · 💬 121</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CultureCrave/status/2061562509543547072">View @CultureCrave on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Florida is suing OpenAI and CEO Sam Altman • The lawsuit alleges OpenAI exploited users’ data and safety to boost the company’s market value at an 'unacceptable' cost • They want Altman personally lia”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Florida ฟ้อง OpenAI และ Sam Altman ข้อหาใช้ข้อมูลผู้ใช้และละเลยความปลอดภัยเพื่อเพิ่มมูลค่าบริษัท พร้อมเรียกให้ Altman รับผิดเป็นการส่วนตัว — รัฐแรกในสหรัฐฯ ที่ฟ้องด้านความปลอดภัย AI</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CultureCrave/status/2061562509543547072" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BobbyBorkIII</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3861 · 💬 64</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BobbyBorkIII/status/2061527378757652524">View @BobbyBorkIII on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The year is 2040. OpenAI has digitized Trump’s brain to serve as President for all eternity. Northern Virginia is one contiguous data center running the Trump simulacrum. The US-Iran peace deal collap”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์เสียดสีเชิง fiction จินตนาการปี 2040 ที่ OpenAI digitize สมองของ Trump เป็นประธานาธิบดีถาวร และ S&amp;P 500 แตะ 1,000,000</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BobbyBorkIII/status/2061527378757652524" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Vivek4real_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3508 · 💬 44</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Vivek4real_/status/2061503291457224757">View @Vivek4real_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“JENSEN HUANG SAID THAT ELON MUSK WAS THERE FOR HIM AS A CUSTOMER AT A TIME WHEN NO ONE ELSE WAS. AND HE CLAIMED THAT ELON MUSK IS THE ORIGINAL FOUNDER OF OPENAI AND CHATGPT. “WHEN I ANNOUNCED THIS PRO”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Jensen Huang ยกย่อง Elon Musk ว่าเป็นลูกค้ารายแรกในยุคที่ไม่มีใครสนใจ และอ้างว่า Musk คือผู้ก่อตั้ง OpenAI และ ChatGPT ตัวจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Vivek4real_/status/2061503291457224757" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@allenanalysis</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3327 · 💬 81</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/allenanalysis/status/2061504329266176362">View @allenanalysis on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 THIS IS THE ENTIRE AI INDUSTRY'S NIGHTMARE IN ONE QUOTE. An author suing OpenAI says AI companies didn't just buy books. They allegedly downloaded them from pirate sites. Then, according to his clai”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>คดีฟ้อง OpenAI ระบุว่าบริษัทโหลด training data หนังสือจากเว็บละเมิดลิขสิทธิ์ แล้วลบหน้า copyright และ ISBN ออกก่อนนำไปเทรน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้าพิสูจน์ได้ output จาก AI tools มีความเสี่ยง IP ต่อเนื่อง — studio ที่ ship งาน AI-assisted เชิงพาณิชย์ควรรู้ว่าตัวเองพึ่ง model ไหน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">บันทึก AI tools ที่ใช้ในแต่ละ project และตรวจ indemnification clause ใน ToS ของแต่ละ tool ก่อน ship งานให้ลูกค้า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/allenanalysis/status/2061504329266176362" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@OpenAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3157 · 💬 183</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/OpenAI/status/2061564502160892138">View @OpenAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“OpenAI frontier models and Codex are now generally available on AWS, giving enterprises a new way to build on Amazon Bedrock with OpenAI through the security, compliance, and governance workflows they”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>OpenAI frontier models และ Codex พร้อมให้ใช้งานบน Amazon Bedrock แล้ว ผ่าน security และ compliance workflow ของ AWS ที่องค์กรใช้อยู่แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า studio ใช้ AWS อยู่แล้ว เรียก OpenAI models ได้เลยผ่าน Bedrock โดยไม่ต้องแยก account OpenAI</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า studio มี AWS infra อยู่แล้ว ลองเปลี่ยน OpenAI API call ไปใช้ผ่าน Bedrock เพื่อรวม billing และ access control ในที่เดียว</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/OpenAI/status/2061564502160892138" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RevivalOfPotara</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2983 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RevivalOfPotara/status/2061560378602168792">View @RevivalOfPotara on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Not believing leaks because they involve sonic getting a new model they can't craft slander this good https://t.co/cFmoghOT8J”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ไม่เชื่อ leak เกมที่บอกว่า Sonic จะได้ model ใหม่ เพราะมองว่าเขียนได้แม่นเกินกว่าจะเป็นเรื่องจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RevivalOfPotara/status/2061560378602168792" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sgaygirlwhosafn</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2874 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sgaygirlwhosafn/status/2061536911286530270">View @sgaygirlwhosafn on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“the leaker -had new unseen footage of jsr -screenshot of the new streets of rage -screenshots of miku in p5x -teased p6 taking place in yokohama or whatever all the way back in febreuary but suddenly ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ถกเรื่องความน่าเชื่อถือของ leaker เกม โดยอิงจากประวัติการปล่อย leak JSR, Streets of Rage, Persona 5X, Persona 6 เทียบกับ claim ใหม่เรื่อง Sonic</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sgaygirlwhosafn/status/2061536911286530270" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Danny8bit</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1842 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Danny8bit/status/2061557462013264046">View @Danny8bit on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“everyone collectively going “Sonic getting a new model?? Lmao hell nah, this dude is absolutely a fucking liar” has gotta be the funniest shit I’ve seen in a while”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้คอมเมนต์ว่า community พากันหัวเราะเยาะข่าวที่ว่า Sonic จะได้ 'new model' และบอกว่ามันตลกมาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Danny8bit/status/2061557462013264046" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
