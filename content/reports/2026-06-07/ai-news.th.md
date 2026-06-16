---
type: social-topic-report
date: '2026-06-07'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-07T15:12:06+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 228
salience: 0.55
sentiment: mixed
confidence: 0.5
tags:
- openai
- chatgpt
- claude-code
- anthropic
- ai-tooling
- llm
thumbnail: https://pbs.twimg.com/media/HKL4iWbasAAdjLO.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-07

## TL;DR
- OpenAI กำลังวางแผน overhaul ครั้งใหญ่ที่สุดของ ChatGPT นับตั้งแต่เปิดตัว โดยรวม Codex, AI agents, image generation, web browser และบริการ third-party (payments, bookings) ไว้ใน 'superapp' เดียว ก่อน IPO ที่วางแผนไว้ โดย rollout จะเริ่มในอีกไม่กี่สัปดาห์ [16][22][24][37][58]
- ChatGPT ทะลุ 600M monthly active users เป็นครั้งแรกตาม Similarweb [60]; OpenAI CFO Sarah Friar ระบุว่า training run ครั้งใหญ่ถัดไปในฤดูใบไม้ร่วงนี้จะรันบน NVIDIA Vera Rubin platform และ compute จะขายหมดต่อเนื่องตลอดส่วนใหญ่ของปี 2027 [12]
- Anthropic รายงานว่า Claude เขียน production code ของตัวเองกว่า 80% แล้ว [14]; Claude Code Head Boris Cherny ระบุว่า 'transition ครั้งต่อไปจะมาในปีนี้' ในด้าน coding workflows [54]
- artifact ฟรีที่จับต้องได้: Anthropic เผยแพร่ prompt-engineering workshop ยาวประมาณ 24 นาที ไม่ต้องลงทะเบียน ไม่มี paywall [46]; โพสต์ 'free course' รอบข้าง [19][26][31] ส่วนใหญ่เป็น engagement bait
- AI content วันนี้ส่วนใหญ่เป็นข่าวและข่าวลือ ไม่ใช่ tools ที่ใช้งานได้จริง; repo/plugin ที่จับต้องได้มีน้อย สังเกตว่า: ความสับสนระหว่าง ChatGPT กับ Codex กับ Claude ในหมู่ working dev เป็นเรื่องจริง [56] และ Claude Code รายงานว่าทำคะแนน coding tests สูงกว่า GitHub Copilot [47]

## What happened
เรื่องหลักมาจากรายงานอ้างอิง FT ว่า OpenAI เตรียม redesign ChatGPT ครั้งใหญ่ที่สุดนับตั้งแต่เปิดตัว โดยแปลงเป็น 'superapp' ที่รวม Codex coding, AI agents, image generation และ browser ไว้ในแพลตฟอร์ม desktop/web/mobile เดียว พร้อม payments, bookings และบริการ third-party โดยจังหวะเวลาก่อน IPO; rollout จะเริ่มในอีกไม่กี่สัปดาห์ผ่านการเปลี่ยนแปลงเว็บและแอปที่ดัน users ไปหา coding และ image-generation [16][22][24][37][58][9][2][3] ข้อมูลสนับสนุน: ChatGPT แตะ 600M MAU ตาม Similarweb [60] และ CFO ของ OpenAI ยืนยันว่า training run ฤดูใบไม้ร่วงจะรันบน NVIDIA Vera Rubin โดย compute จะขายหมดตลอดส่วนใหญ่ของปี 2027 [12] ฝั่ง Anthropic มีสองประเด็นหมุนเวียน: Claude เขียน production code ของตัวเองกว่า 80% [14] และหัวหน้าทีม Claude Code บอกว่า 'transition' ของ workflow อีกครั้งจะมาในปีนี้ [54] มีการแชร์ prompt workshop ฟรีจาก Anthropic (~24 นาที) [46] ควบคู่กับโพสต์แบบ bait อย่าง '300 prompts' และ 'full course' [19][26][31] ประเด็นรอง: AgentRouter gateway non-profit จากจีนรองรับ 30+ models พร้อม free credits $100 [50], GitHub Copilot Pro promo ฟรี 2 ปี [45], บทวิเคราะห์ 'Claude Code เหนือกว่า Copilot ใน coding tests' [47], ตัวอย่าง prompt ของ GPT Image 2 [35] และเรื่องภูมิรัฐศาสตร์ที่ยังไม่ยืนยัน — อ้าง Pentagon blacklist บวกข่าวลือ NSA ใช้ 'Claude Mythos' [52] และข่าวลือแผน US ให้ประชาชนถือหุ้น OpenAI/Anthropic/xAI [25] เนื้อหาส่วนใหญ่ใน feed ไม่เกี่ยวข้อง เป็น noise จาก K-pop/โหราศาสตร์ [1][4][5][6][8][10][13][18][32][33][40][57]

## Why it matters (reasoning)
ถ้า OpenAI รวม coding (Codex), agents และ image generation ไว้ในแพลตฟอร์มเดียว [16][37] switching cost ของการอยู่ใน ChatGPT จะสูงขึ้น และการแข่งขันด้าน agent/coding tool ที่ NDF DEV เผชิญอยู่จะยิ่งดุเดือด — พื้นที่เดียวกับที่ Claude Code รายงานว่านำหน้า Copilot ใน coding tests [47] และที่ developer สับสนระหว่าง ChatGPT, Codex และ Claude [56] claim ที่ว่า Claude เขียน code ของตัวเอง 80% [14] และ frame 'transition ครั้งต่อไปในปีนี้' [54] ชี้ว่า coding assistants กำลังเคลื่อนจาก autocomplete ไปสู่งานแบบ delegated, loop-driven; สำหรับ studio ที่ ship Unity, XR และ web/mobile สิ่งนี้เปลี่ยน value จากความเร็วในการพิมพ์ไปสู่คุณภาพของ prompt/spec และ review discipline สัญญาณ compute ขายหมดถึงปี 2027 [12] คือ constraint ลำดับสอง: capacity และ pricing ของ models ที่ studio พึ่งพาอยู่กำลังตึงตัว ซึ่งสนับสนุนการทำ model-portability มากกว่าการ lock-in blog ด้านความกังวลเรื่องอาชีพ [44] และ 'hackathons are just Claude prompting battles' [49] สะท้อน labor shift ที่เกิดขึ้นจริงแต่เป็นแค่ sentiment ไม่ใช่ tooling

## Possibility
น่าจะเกิด: OpenAI จะ ship อย่างน้อยการเปลี่ยนแปลงที่มองเห็นได้ (ดัน users ไปหา coding/image features ในแอปและเว็บ) ภายในไม่กี่สัปดาห์ เพราะหลาย outlet อ้าง FT reporting เดียวกันพร้อม rollout window ระยะสั้น [22][37][16] เป็นไปได้: 'superapp' แบบเต็มรูปแบบที่มี payments, bookings และ third-party services จะมาทีละส่วนอย่างค่อยเป็นค่อยไป เพราะปัจจัยด้าน platform/regulatory และ timing ของ IPO ทำให้ launch พร้อมกันทุกอย่างยุ่งยาก [2][24][58] เป็นไปได้: Apple จะ reposition Siri รอบ custom Google Gemini model ใน WWDC 2026 ตาม leaks [39] ซึ่งจะเพิ่ม assistant platform หลักตัวที่สาม ไม่น่าเกิด (ระยะสั้น และยังไม่ยืนยัน): แผน US 'ให้ประชาชนถือหุ้น OpenAI/Anthropic/xAI' [25] และ claims Pentagon-blacklist/NSA-Mythos [52] — แหล่งเดียว ไม่มีการยืนยันซ้ำในชุดข้อมูล ไม่มีแหล่งใดระบุความน่าจะเป็นเป็นตัวเลข จึงไม่ระบุ

## Org applicability — NDF DEV
1) ให้ทีมดู Anthropic prompt workshop ฟรี [46] แล้วนำ patterns ไปรวมไว้ใน prompt/spec template กลาง — effort ต่ำ เป็น artifact ที่จับต้องได้และน่าเชื่อถือที่สุดตรงนี้
2) ใช้ Claude Code เป็น coding agent หลักสำหรับ Unity/web/mobile ต่อไป อิงจากการเปรียบเทียบกับ Copilot [47] และ self-code claim [14] แต่วัดผลจากงานของตัวเองแทนที่จะเชื่อตัวเลข 80% — effort ต่ำ
3) รักษา model-portability: เพราะ compute ขาดแคลน [12] และ model หมุนเวียนเร็ว อย่า hard-code API ของ vendor เดียวลงใน pipeline เพื่อให้สลับได้เมื่อ pricing/availability เปลี่ยน — effort กลาง
4) ทดลอง GPT Image 2 [35] สำหรับ concept art, marketing และ placeholder game assets — effort ต่ำ
5) ติดตาม OpenAI 'superapp'/Codex consolidation แบบ watch item; อย่าปรับ workflow จนกว่าจะ ship จริง [16][37] — effort ต่ำ
ข้าม: การ route API keys/data ผ่าน AgentRouter China gateway [50] (operator ไม่รู้จัก มีความเสี่ยงด้าน data handling); bait '300 prompts'/'full course' [19][26][31]; และ noise จาก crypto/โหราศาสตร์/K-pop ทั้งหมด อย่า act กับข่าวลือ nationalization [25] หรือ Pentagon/NSA [52] — ยังไม่ยืนยัน

## Signals to Watch
- ว่า OpenAI rollout จะรวม Codex + agents + browser จริงในแอปเดียวตาม timeline 'อีกไม่กี่สัปดาห์' หรือไม่ [16][37]
- Apple WWDC 2026 (รายงานว่าใกล้ถึง) และว่า Siri จะถูก rebuild บน custom Google Gemini model หรือไม่ [39]
- กลุ่มข่าวลือ next-model — 'mythos, 5.6, gemini pro 3.5' — ว่าอะไรจะ release จริงกับอะไรแค่ speculation [42][52]
- แรงกดด้าน compute supply: 'sold out through 2027' ของ Friar [12] ในฐานะ leading indicator ของ pricing/availability ของ models สำหรับ studio

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **ValveSoftware/GameNetworkingSockets** — Valve P2P networking พังมากกว่า 2 เดือนแล้ว | radar | <https://github.com/ValveSoftware/GameNetworkingSockets> |
| **anthropics/claude-code** — ขอให้ Anthropic ship Claude Desktop อย่างเป็นทางการสำหรับ Linux | radar | <https://github.com/anthropics/claude-code> |
| **devenjarvis/lathe** — Show HN: Lathe – ใช้ LLMs เพื่อเรียน domain ใหม่ ไม่ใช่ข้ามมัน | radar | <https://github.com/devenjarvis/lathe> |
| **mvanhorn/last30days-skill** — AI agent skill สำหรับค้นคว้าหัวข้อใดก็ได้ข้าม Reddit, X, YouTube, HN, Polymarket และเว็บ | rss | <https://github.com/mvanhorn/last30days-skill> |
| **MemPalace/mempalace** — ระบบ AI memory open-source ที่ benchmark ดีที่สุด และฟรี MemPalace Local-first AI memory. | rss | <https://github.com/MemPalace/mempalace> |
| **Panniantong/Agent-Reach** — ให้ AI agent ของคุณมองเห็นอินเทอร์เน็ตทั้งหมด อ่านและค้นหาบน Twitter, Reddit, YouTube, GitHub... | rss | <https://github.com/Panniantong/Agent-Reach> |
| **openai/whisper** — Robust Speech Recognition ด้วย Large-Scale Weak Supervision Whisper [Blog] [Paper] [Model card] [Colab] | rss | <https://github.com/openai/whisper> |
| **PaddlePaddle/PaddleOCR** — แปลง PDF หรือเอกสารรูปภาพใดก็ได้เป็น structured data สำหรับ AI toolkit OCR ทรงพลังและเบา | rss | <https://github.com/PaddlePaddle/PaddleOCR> |
| **microsoft/VibeVoice** — Open-Source Frontier Voice AI 🎙️ VibeVoice: Open-Source Frontier Voice AI 📰 News 2026-03-06: 🚀 VibeV | rss | <https://github.com/microsoft/VibeVoice> |
| **khoj-ai/khoj** — AI second brain ของคุณ Self-hostable ค้นหาคำตอบจากเว็บหรือเอกสารของคุณ สร้าง custom agents... | rss | <https://github.com/khoj-ai/khoj> |
| **666ghj/MiroFish** — Swarm Intelligence Engine ที่เรียบง่ายและใช้ได้ทั่วไป สำหรับทำนายทุกสิ่ง 简洁通用的群体智能引擎，预测万物 | rss | <https://github.com/666ghj/MiroFish> |
| **agentscope-ai/agentscope** — สร้างและรัน agents ที่มองเห็น เข้าใจ และไว้วางใจได้ 中文主页 / Documentation / Roadmap | rss | <https://github.com/agentscope-ai/agentscope> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | GMMTV | ^4230 c39 | [แทนรัก (Tanrak) Ost.Ticket to Heaven เด็กชายไม่ไปสวรรค์ - Gemini Norawit 🎥 Offic](https://x.com/GMMTV/status/2063485065183797364) |
| x | Polymarket | ^2299 c196 | [JUST IN: OpenAI is reportedly planning its biggest ChatGPT overhaul yet, aiming ](https://x.com/Polymarket/status/2063477552170090816) |
| x | Cointelegraph | ^1342 c186 | [🚨 JUST IN: OpenAI is reportedly turning ChatGPT into an AI superapp ahead of its](https://x.com/Cointelegraph/status/2063493776111231040) |
| x | nongsiii | ^1199 c0 | [i'm crying bc gemini ytd tweeted TanRak is the most a head-over-heels in love so](https://x.com/nongsiii/status/2063617325539185065) |
| x | gemiieyy | ^1053 c1 | [someone pls hold gemini or he will end up twerking infront of the father 😭😭😭 #Ti](https://x.com/gemiieyy/status/2063513052499329224) |
| x | BRNarawins | ^960 c0 | [IMAGINE THE CHAOS 😃🆘 PHUWIN HANA WITH NEKKO #NEKKOxGeminiFourthPhuwin ♊️: There ](https://x.com/BRNarawins/status/2063622404702658624) |
| x | DarioCpx | ^953 c50 | [Something has gone badly wrong in both Anthropic and OpenAI in the past months d](https://x.com/DarioCpx/status/2063534039567646895) |
| x | aydellch | ^750 c1 | [OMG, "TANRAK" FIRST LIVE BY GEMINI 😭😭😭🤍🤍 #NEKKOxGeminiFourthPhuwin https://t.co/](https://x.com/aydellch/status/2063614869895885106) |
| x | DeItaone | ^748 c122 | [OPENAI INTENDS TO TRANSFORM CHATGPT INTO A "SUPERAPP" THAT COMBINES CODING TOOLS](https://x.com/DeItaone/status/2063489894412857617) |
| x | RRinda6 | ^734 c2 | [(1/2) 🐼: I still hadn't starred in Fish Upon The Sky ♌️: So you guys were still ](https://x.com/RRinda6/status/2063624616409715067) |
| x | dotkrueger | ^688 c65 | [Facts 1. We are in the 5% cheapest Bitcoin has ever been 2. Comparable valuation](https://x.com/dotkrueger/status/2063497627405300167) |
| x | StockSavvyShay | ^655 c78 | [OpenAI CFO Sarah Friar says its next major training run this fall will be on $NV](https://x.com/StockSavvyShay/status/2063571134994641245) |
| x | aydellch | ^645 c2 | [[ https://t.co/VAgunmFhB3 ] Is this realll??? #NEKKOxGeminiFourthPhuwin #GeminiF](https://x.com/aydellch/status/2063625011986911674) |
| x | PeterDiamandis | ^642 c88 | [Anthropic reports Claude now writes over 80% of its own production code — meanin](https://x.com/PeterDiamandis/status/2063603307067879590) |
| x | hourIyhoroscope | ^608 c19 | [they don't understand you, gemini.](https://x.com/hourIyhoroscope/status/2063478808699609463) |
| x | mark_k | ^595 c53 | [According to FT, @OpenAI is preparing the biggest ChatGPT overhaul since launch.](https://x.com/mark_k/status/2063569543784468893) |
| x | aditiraaaj | ^541 c172 | [Hey @grok can you do better than chatgpt and Gemini ?? https://t.co/B20VSCPlXW](https://x.com/aditiraaaj/status/2063494600552280246) |
| x | Childmoon77 | ^535 c4 | [🌟 JULY ENERGY 🌟 Aries: Big Opportunities Taurus: Manifest Wealth Gemini: Dreams ](https://x.com/Childmoon77/status/2063517383549935771) |
| x | itspriionly | ^528 c267 | [NO ONE teaches you how to use Claude with professional-level prompts. I gathered](https://x.com/itspriionly/status/2063497616290370041) |
| x | aydellch | ^525 c0 | [Gemini was bending left and right so he could feed Jumu, and Fourth applied some](https://x.com/aydellch/status/2063630051732840826) |
| x | ishmohit1 | ^455 c16 | [Have created an AI dashboard using Claude where you just need to enter companies](https://x.com/ishmohit1/status/2063566462284136453) |
| x | FT | ^449 c24 | [OpenAI plots biggest ChatGPT overhaul since launch https://t.co/4GwCtUDSEP](https://x.com/FT/status/2063476350329995423) |
| x | g4snara | ^432 c0 | [the way fourth keeps touching the eyebrow scar gem/barth has everytime he imitat](https://x.com/g4snara/status/2063586337283068409) |
| x | coinbureau | ^430 c73 | [🚨HUGE: CHATGPT IS GETTING A COMPLETE OVERHAUL OpenAI is preparing its biggest Ch](https://x.com/coinbureau/status/2063523804874481881) |
| x | cryptorover | ^409 c95 | [THE AI BOOM MAY GET NATIONALIZED IN USA 🇺🇸 Trump is reportedly discussing a plan](https://x.com/cryptorover/status/2063561449914712349) |
| x | Vivek4real_ | ^409 c10 | [ANTHROPIC PAYS $750,000 A YEAR FOR THIS SKILL. STANFORD IS GIVING IT AWAY FOR FR](https://x.com/Vivek4real_/status/2063534676665634865) |
| x | Trathoa | ^405 c221 | [Gm fam ... have a great weekend A few updates and news over the weekend @useTria](https://x.com/Trathoa/status/2063520970963612147) |
| x | aydellch | ^401 c1 | [Not Gemini standing there like someone who wants to be punished too 😭😭😭😭😭😭 HE WA](https://x.com/aydellch/status/2063626825872650713) |
| x | solana | ^388 c130 | [Mastercard introduced always-on stablecoin settlement on Solana, Backpack announ](https://x.com/solana/status/2063622007540035728) |
| radar | gregsadetsky | ^372 c112 | [Ntsc-rs – open-source video emulation of analog TV and VHS artifacts](https://ntsc.rs/) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GMMTV</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4230 · 💬 39</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GMMTV/status/2063485065183797364">View @GMMTV on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“แทนรัก (Tanrak) Ost.Ticket to Heaven เด็กชายไม่ไปสวรรค์ - Gemini Norawit 🎥 Official MV on YouTube GMMTV RECORDS : https://t.co/DVxqZQvhuv and available on all streaming platforms. #TanrakMV #TicketToH”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>GMMTV ปล่อย MV เพลง 'แทนรัก' เพลงประกอบซีรีส์ Ticket to Heaven ขับร้องโดย Gemini Norawit</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GMMTV/status/2063485065183797364" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Polymarket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2299 · 💬 196</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Polymarket/status/2063477552170090816">View @Polymarket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“JUST IN: OpenAI is reportedly planning its biggest ChatGPT overhaul yet, aiming to turn it into a “superapp” ahead of the company’s IPO.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Polymarket รายงานว่า OpenAI วางแผน redesign ChatGPT ครั้งใหญ่ในรูปแบบ 'superapp' โดยจับจังหวะก่อน IPO</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Polymarket/status/2063477552170090816" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Cointelegraph</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1342 · 💬 186</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Cointelegraph/status/2063493776111231040">View @Cointelegraph on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 JUST IN: OpenAI is reportedly turning ChatGPT into an AI superapp ahead of its planned IPO. https://t.co/uZYwoKnejr”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>OpenAI กำลังรีดีไซน์ ChatGPT ให้เป็น superapp รวมบริการต่างๆ ไว้ในที่เดียว โดยจังหวะนี้ตรงกับช่วงก่อน IPO</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Cointelegraph/status/2063493776111231040" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1199 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2063617325539185065">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i’m crying bc gemini ytd tweeted TanRak is the most a head-over-heels in love song of gemini 😭😭😭😭😭😭😭 #NEKKOxGeminiFourthPhuwin https://t.co/VVukW2H1eg”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคลับโพสต์ถึง Gemini (วงนักแสดงไทย) ที่ทวีตว่า TanRak คือเพลงที่รู้สึก head-over-heels มากที่สุด พร้อม hashtag แฟนด้อม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2063617325539185065" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gemiieyy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1053 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gemiieyy/status/2063513052499329224">View @gemiieyy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“someone pls hold gemini or he will end up twerking infront of the father 😭😭😭 #TicketToHeavenEP2 https://t.co/o6nmhogJfx”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ตลกเกี่ยวกับตัวละครในซีรีส์ไทย ไม่มีเนื้อหาด้านเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gemiieyy/status/2063513052499329224" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BRNarawins</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 960 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BRNarawins/status/2063622404702658624">View @BRNarawins on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“IMAGINE THE CHAOS 😃🆘 PHUWIN HANA WITH NEKKO #NEKKOxGeminiFourthPhuwin ♊️: There was supposed to be a boy band unit with only three members. Those members were Gemini, Phuwin Fourth 👤: Oh, really? Like”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Gemini, Phuwin และ Fourth เล่าถึง boy band unit ที่เคยซ้อมด้วยกันแค่ 2–3 ครั้งแล้วก็เลิก ก่อนที่แต่ละคนจะไปแสดงซีรีส์แทน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BRNarawins/status/2063622404702658624" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DarioCpx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 953 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DarioCpx/status/2063534039567646895">View @DarioCpx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Something has gone badly wrong in both Anthropic and OpenAI in the past months despite both companies raised a biblical amount of capital https://t.co/T0IB0himmf”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บัญชี commentary (@DarioCpx ไม่ใช่ CEO จริง) โพสต์ว่ามีบางอย่างผิดพลาดที่ Anthropic และ OpenAI ในช่วงนี้ แต่ไม่มีรายละเอียดใดเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DarioCpx/status/2063534039567646895" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 750 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2063614869895885106">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“OMG, &quot;TANRAK&quot; FIRST LIVE BY GEMINI 😭😭😭🤍🤍 #NEKKOxGeminiFourthPhuwin https://t.co/5vxaSnxojR”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับแสดงความตื่นเต้นที่ Gemini (นักแสดงไทย) ร้องเพลง 'ตัณหา' live ในงาน NEKKO x Gemini x Fourth Phuwin — ไม่เกี่ยวกับ Google Gemini</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2063614869895885106" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
