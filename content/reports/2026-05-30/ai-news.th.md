---
type: social-topic-report
date: '2026-05-30'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-05-30T18:19:06+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 154
salience: 0.25
sentiment: neutral
confidence: 0.55
tags:
- ai-tooling
- api-pricing
- mcp
- coding-assistants
- low-signal
- noise-polluted
thumbnail: https://pbs.twimg.com/ext_tw_video_thumb/2060703402305454080/pu/img/fgtYUQc_UorZFdOJ.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-05-30

## TL;DR
- Feed เต็มไปด้วยโพสต์ K-pop/Thai BL เกี่ยวกับนักแสดงชื่อเล่น 'Gemini' (GeminiFourth, #TicketToHeavenEP1) และดวงดาว — signal จริงด้าน AI tooling วันนี้น้อยมาก [1][3][5][24]
- การจัดอันดับ coding model ส่วนตัวพบว่า Codex GPT-5.5 อันดับ 1, Claude Opus 4.8 อันดับ 2, Composer 2.5 อันดับ 3 นำหน้าการโค้ดมือและ Gemini [11]
- สงครามราคา API ในจีนร้อนขึ้น: DeepSeek ประกาศลดราคา API 75% ถาวร และ Xiaomi ลดได้ถึง 99% เพื่อสู้ [39]
- บล็อก 'MCP is dead?' ดึง 336 ความคิดเห็น สะท้อนการถกเถียงเรื่องบทบาทของ Model Context Protocol ใน agent stack [40]
- มุม market: Anthropic มี valuation สูงกว่า Walmart และ OpenAI สูงกว่า JPMorgan; Jim Cramer เตือนความเสี่ยง volatility จาก index rebalancing [50][34]

## What happened
ส่วนใหญ่ใน feed ไม่ใช่ AI tooling — เป็นโปรโมตซีรีส์/นักแสดง (Gemini–Fourth, #TicketToHeavenEP1) กับเนื้อหาดูดวง [1][2][5][7][24][25] signal AI จริงมีน้อย นักพัฒนารายหนึ่งโพสต์อันดับ coding assistant ส่วนตัวโดยให้ Codex GPT-5.5 นำ Claude Opus 4.8 และ Composer 2.5 [11] ด้านราคา DeepSeek ประกาศลด API 75% ถาวร และ Xiaomi ลดได้ถึง 99% [39] บล็อก 'MCP is dead?' สร้างการอภิปรายหนักเรื่อง Model Context Protocol [40] โพสต์ฝั่งการเงินระบุว่า Anthropic และ OpenAI มี valuation เกิน Walmart และ JPMorgan พร้อมเตือนความเสี่ยง volatility จาก index rebalancing [50][34] และ Musk ยืนกรานเรื่อง truthfulness ของ Gemini และ ChatGPT อีกครั้ง [56]

## Why it matters (reasoning)
สำหรับ studio AI workflows วันนี้ content ที่นำไปทำอะไรได้จริงมีแค่เรื่องราคาและทิศทาง protocol ไม่มี repo หรือ skill ใหม่ที่ชัดเจน การที่ provider จีนลดราคา API 75–99% [39] กดต้นทุนต่อ token ของรายหลักและอาจลดค่าใช้จ่ายงาน background/agentic task ถ้าคุณภาพยังอยู่ — เกี่ยวข้องกับงาน batch ที่ sensitive ด้านงบ การถกเถียง 'MCP is dead?' [40] สำคัญเพราะการเลือก tool integration ของ studio (Claude/Cursor plugins, agent connectors) ขึ้นอยู่กับว่า MCP จะยังเป็น integration layer หลักหรือไม่ thread 336 ความคิดเห็นบ่งชี้ว่าทิศทางยังไม่นิ่ง ลงทุนกับ MCP-specific plumbing ตอนนี้มีความเสี่ยงต้องแก้ทีหลัง อันดับ model อย่าง [11] เป็นความเห็นส่วนตัว ไม่ใช่ benchmark ไม่ควรใช้ตัดสินใจเปลี่ยน tool มูลค่า valuation/ตลาด [34][50] เป็นบริบทระดับ macro เท่านั้น

## Possibility
เป็นไปได้สูง: ราคา API จะยังถูกลงต่อเนื่องเพราะ DeepSeek และ Xiaomi เป็น anchor ต่ำ กดให้รายอื่นต้องตอบสนองด้านราคาหรือ tier [39] เป็นไปได้: MCP จะยังพัฒนาต่อไปมากกว่าตาย — ปริมาณการถกเถียง [40] แสดง engagement ไม่ใช่การทิ้ง แต่คาดว่าจะมี integration pattern ทางเลือกเกิดขึ้น ไม่น่าเป็นไปได้ (จาก feed นี้): อันดับ coding model ใน [11] จะสะท้อนคุณภาพที่วัดซ้ำได้คงเส้นคงวา เป็นแค่ความชอบส่วนตัว ไม่มีแหล่งข้อมูลใดให้ตัวเลขความน่าจะเป็น จึงไม่อ้างไว้

## Org applicability — NDF DEV
1) อ่านบทความ 'MCP is dead?' ก่อนขยาย integration ที่อิง MCP เพื่อตัดสินใจว่าจะ standardize บน MCP หรืออยู่แบบ adapter-agnostic — effort: low [40] 2) ประเมินราคา DeepSeek/Xiaomi สำหรับงานที่ไม่ critical แต่ volume สูง (เช่น bulk asset captioning, test generation) พร้อม spot-check คุณภาพเล็กน้อย อย่าย้ายงาน code ที่ production-critical — effort: med [39] 3) ใช้อันดับ coding model เป็นแรงบันดาลใจให้รัน A/B ของตัวเองบน studio task จริง แทนที่จะเชื่อตามนั้น — effort: low [11] ข้าม: content นักแสดง/ดูดวง [1][2][5][7][24][25] (ไม่เกี่ยว), ลิงก์ '20k free credits' [38] (ยังไม่ผ่านการตรวจสอบ น่าจะเป็น scam — ห้ามกรอก credentials) และ $GOBLIN/crypto lore [21]

## Signals to Watch
- DeepSeek/Xiaomi ลดราคาแล้ว provider สหรัฐฯ จะตามหรือไม่ [39]
- ผลลัพธ์การถกเถียง MCP และ integration pattern ทางเลือกที่อาจเกิดขึ้น [40]
- Benchmark อิสระสำหรับ Codex GPT-5.5 / Claude Opus 4.8 / Composer 2.5 นอกเหนือจากอันดับผู้ใช้คนเดียว [11]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **kristapsdz/openrsync** — Openrsync: An implementation of rsync, by the OpenBSD team | radar | <https://github.com/kristapsdz/openrsync> |
| **mplsllc/macsurf** — Macsurf, "modern" web browser for macOS 9 | radar | <https://github.com/mplsllc/macsurf> |
| **harry0703/MoneyPrinterTurbo** — 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. MoneyPrinterTurbo 💸 简体中文 / Engl | rss | <https://github.com/harry0703/MoneyPrinterTurbo> |
| **microsoft/markitdown** — Python tool for converting files and office documents to Markdown.MarkItDown Important MarkItDown pe | rss | <https://github.com/microsoft/markitdown> |
| **EveryInc/compound-engineering-plugin** — Official Compound Engineering plugin for Claude Code, Codex, Cursor, and moreCompound Engineering AI | rss | <https://github.com/EveryInc/compound-engineering-plugin> |
| **twentyhq/twenty** — The open alternative to Salesforce, designed for AI. The #1 Open-Source CRM Website · Documentation  | rss | <https://github.com/twentyhq/twenty> |
| **anthropics/claude-code** — Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and he | rss | <https://github.com/anthropics/claude-code> |
| **Leonxlnx/taste-skill** — Taste-Skill - gives your AI good taste. stops the AI from generating boring, generic slop Taste Skil | rss | <https://github.com/Leonxlnx/taste-skill> |
| **cursor/plugins** — Cursor plugin specification and official pluginsCursor plugins Official Cursor plugins for popular d | rss | <https://github.com/cursor/plugins> |
| **run-llama/liteparse** — A fast, helpful, and open-source document parserLiteParse / / / / / / Docs Looking for LiteParse V1? | rss | <https://github.com/run-llama/liteparse> |
| **galilai-group/stable-worldmodel** — A platform for reproducible world model research and evaluationstable-worldmodel A platform for repr | rss | <https://github.com/galilai-group/stable-worldmodel> |
| **byoungd/English-level-up-tips** — An advanced guide to learn English which might benefit you a lot 🎉 . 离谱的英语学习指南/英语学习教程/英语学习/学英语简体中文 / | rss | <https://github.com/byoungd/English-level-up-tips> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | geminiscity | ^5685 c10 | [4️⃣: [talks] ♊️: Keep going. I like listening to you talk. 4️⃣: [continues talki](https://x.com/geminiscity/status/2060703541661200394) |
| x | justalesky | ^3508 c7 | [https://t.co/0653ggwHBV P'Aof : "This is what Gemini and I had to deal with when](https://x.com/justalesky/status/2060734944792731708) |
| x | _iamjamila | ^3223 c70 | [Happy 30th Birthday to me the leader of the Gemini Supremacy Movement ♊️♊️♊️♊️ S](https://x.com/_iamjamila/status/2060698074972840192) |
| x | geminiscity | ^2881 c1 | [♊️: [talks about Tanrak who's reserved like Fourth when he first entered the ind](https://x.com/geminiscity/status/2060696629255274515) |
| x | mylifegemfourth | ^2084 c1 | [GEMINI CHANGED THE LYRICS FROM "that person must be you" TO "that person must be](https://x.com/mylifegemfourth/status/2060708154628002048) |
| x | aydellch | ^1984 c1 | [[ talking about how their feelings (while filming) coming from inside ] 🎤: And G](https://x.com/aydellch/status/2060698841205358890) |
| x | nongsiii | ^1878 c2 | [twenty years later, he comes back. from someone who once lost his faith in God, ](https://x.com/nongsiii/status/2060748869517144087) |
| x | aydellch | ^1847 c8 | [[ sing คนนั้นต้องเป็นเธอ by Win Metawin ] 4️⃣: That person must be... you~ ♊️: (](https://x.com/aydellch/status/2060707752729870807) |
| x | fotgems | ^1176 c3 | [gemini as barth is genuinely the best thing that has ever happened. #TicketToHea](https://x.com/fotgems/status/2060734775946887466) |
| x | aydellch | ^1145 c12 | [From giggling bcs Fourth could describe Gemini's golden body so detailed to feel](https://x.com/aydellch/status/2060700741665439981) |
| x | rezoundous | ^1095 c71 | [My personal ranking 1. Codex GPT-5.5 2. Claude Opus 4.8 3. Composer 2.5 4. Manua](https://x.com/rezoundous/status/2060707540795900216) |
| x | aydellch | ^1079 c13 | [I can't believe I got to see Gemini with gray hair 😭😭😭😭😭😭😭😭😭😭😭😭😭😭 GEMINIFOURTH T](https://x.com/aydellch/status/2060735782286139450) |
| x | nongsiii | ^1005 c3 | [4️⃣: Gemini is his golden form 😛😋 4️⃣: everyone's drooling 😝 ♊️: crazy 😹 #Ticket](https://x.com/nongsiii/status/2060740055665393785) |
| x | justalesky | ^1005 c0 | [https://t.co/Dd3bKMYPHV P'Aof: "We don't have much time left... Gemini and Fourt](https://x.com/justalesky/status/2060714469966442914) |
| x | justalesky | ^962 c2 | [https://t.co/frWvx6JhPo ♊: "Everything you say turns into a spoiler at this poin](https://x.com/justalesky/status/2060710188039221580) |
| x | CChang20970 | ^878 c2 | [♊️Gemini: We have been waiting for two years, and today is finally the day. We d](https://x.com/CChang20970/status/2060713001146274035) |
| x | wetneptune | ^866 c3 | [the full moon in sagittarius is in opposition to uranus in gemini. this is a ful](https://x.com/wetneptune/status/2060709658398990477) |
| x | gemnuna | ^835 c1 | [never see gemini with this expression before he truly like a different person as](https://x.com/gemnuna/status/2060739373268873477) |
| x | gemfot_smile | ^788 c2 | [Gem : I don't understand why they had to hurt Tanrak's feelings that much. The p](https://x.com/gemfot_smile/status/2060696319254208672) |
| x | nongsiii | ^776 c1 | [#TicketToHeavenEP1 Fourth to Gemini 🥹🤍 4️⃣: i feel that for this series, he dedi](https://x.com/nongsiii/status/2060709288755257538) |
| x | MarcellxMarcell | ^641 c25 | [Over the past 24 hours OpenAI and its developers have reaffirmed the $GOBLIN lor](https://x.com/MarcellxMarcell/status/2060723307088117774) |
| x | nongsiii | ^628 c0 | [#TicketToHeavenEP1 Gemini to Fourth 🥹🤍 ♊️: as everyone knows, Fourth is a playfu](https://x.com/nongsiii/status/2060712928593215505) |
| x | justalesky | ^621 c1 | [https://t.co/VOxH0DKBvE (Discussion about the 6 levels of heaven, meanwhile Gemi](https://x.com/justalesky/status/2060702949177991457) |
| x | OneLuckyGirl_28 | ^597 c8 | [JUNE✨ Aries: Attract Money Taurus: Manifest Wealth Gemini: Big Glow Up Cancer: M](https://x.com/OneLuckyGirl_28/status/2060714998821683340) |
| x | YogmayaAstro5 | ^587 c47 | [Jupiter in Cancer ♋ is going to be very beneficial for Cancer ♋ Virgo ♍ Pisces ♓](https://x.com/YogmayaAstro5/status/2060693961115918586) |
| x | astroinrealtime | ^586 c11 | [your laugh is unforgettable, gemini.](https://x.com/astroinrealtime/status/2060708307648627114) |
| x | justalesky | ^553 c0 | [https://t.co/3y5ghC4qWF Mae Godji: "You're really not going to do cheek kiss,fir](https://x.com/justalesky/status/2060740621506355487) |
| x | levelsio | ^520 c44 | [It's a disease all over Europe](https://x.com/levelsio/status/2060766986523553929) |
| x | mylifegemfourth | ^508 c1 | [the way gemini entered at the end then sing with fourth "good time with you" 🥺🥺 ](https://x.com/mylifegemfourth/status/2060706622939562279) |
| x | DoseofTarot | ^504 c4 | [Mutable Signs Gemini , Pisces , Sagittarius , Virgo Job opportunities coming in ](https://x.com/DoseofTarot/status/2060746897573212412) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@geminiscity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5685 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/geminiscity/status/2060703541661200394">View @geminiscity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“4️⃣: [talks] ♊️: Keep going. I like listening to you talk. 4️⃣: [continues talking] 👤: Gemini hasn't talked. 4️⃣: Come on, Gemini. Talk. ♊️: I like it~ No, I just listen to Fourth and I enjoy it. #Tic”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ fan account ตัดฉากซีรีส์ BL ไทย ตัวละครชื่อ Gemini บอกว่าชอบฟังมากกว่าพูด แท็ก hashtag ตอนแรกของซีรีส์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/geminiscity/status/2060703541661200394" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@justalesky</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3508 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/justalesky/status/2060734944792731708">View @justalesky on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/0653ggwHBV P’Aof : “This is what Gemini and I had to deal with whenever Fourth was trying to manage his stress.” GEMINIFOURTH TTH PREMIERE #TicketToHeavenEP1”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แอคเคาท์แฟนคลับโพสต์ caption ตลกเกี่ยวกับนักแสดงไทย Fourth กับ P'Aof โดยใช้ชื่อ Gemini ซึ่งไม่เกี่ยวกับ Google Gemini หรือเทคโนโลยีใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/justalesky/status/2060734944792731708" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@_iamjamila</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3223 · 💬 70</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/_iamjamila/status/2060698074972840192">View @_iamjamila on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Happy 30th Birthday to me the leader of the Gemini Supremacy Movement ♊️♊️♊️♊️ Siri, play GROWN WOMAN 💫 https://t.co/klkj2MRpA2”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Twitter โพสต์ฉลองวันเกิดอายุ 30 ปี อ้างอิงราศีเมถุน ไม่มีเนื้อหาด้านเทคโนโลยีใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/_iamjamila/status/2060698074972840192" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@geminiscity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2881 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/geminiscity/status/2060696629255274515">View @geminiscity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“♊️: [talks about Tanrak who's reserved like Fourth when he first entered the industry] 👤: Which meant Gemini likes Fourth since he entered the industry? ♊️: [coos] I just said like back then... 👤: So ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แอคเคาท์แฟนคลับซีรีส์ไทย post บทสนทนาเล่นๆ ระหว่างนักแสดง Gemini กับ Fourth เรื่องความสัมพันธ์ส่วนตัว ติด tag #TicketToHeavenEP1</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/geminiscity/status/2060696629255274515" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mylifegemfourth</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2084 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mylifegemfourth/status/2060708154628002048">View @mylifegemfourth on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“GEMINI CHANGED THE LYRICS FROM &quot;that person must be you&quot; TO &quot;that person must be FOURTH&quot; 😭😭😭😭😭😭😭😭😭😭😭😭😭🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍 GEMINIFOURTH TTH PREMIERE #TicketToHeavenEP1 https://t.co/owkb0U1PmJ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคลับรายงานว่า Gemini นักร้องไทยเปลี่ยนเนื้อเพลงให้เป็นชื่อ Fourth ระหว่างงาน premiere</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mylifegemfourth/status/2060708154628002048" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1984 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2060698841205358890">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“[ talking about how their feelings (while filming) coming from inside ] 🎤: And Gemini, do you feel it too? ♊️: Can you hear it my heart ♊️: It's saying 'love, love ter (you)' now [ ♊️4️⃣ looking at eo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคลับ live-tweet งาน premiere ของวง GeminiFourth พร้อมคำพูดบนเวที</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2060698841205358890" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1878 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2060748869517144087">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“twenty years later, he comes back. from someone who once lost his faith in God, he returns believing again. the way gemini portrayed old barth in this scene… there’s not a single trace of “gemini nora”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนซีรีส์ไทยชื่นชมการแสดงของ Gemini Norawit ในบท Barth จาก Ticket to Heaven EP1 ว่าเข้าถึงตัวละครมาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2060748869517144087" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1847 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2060707752729870807">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“[ sing คนนั้นต้องเป็นเธอ by Win Metawin ] 4️⃣: That person must be... you~ ♊️: (must be) Fourth~ // OMGGGGG, OKAY GEMINI GEMINIFOURTH TTH PREMIERE #TicketToHeavenEP1 https://t.co/DO6McqrrmE”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับตอบสนองต่อ Win Metawin ร้องเพลงในงาน premiere ของซีรีส์ ไม่มีเนื้อหาด้านเทคโนโลยีใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2060707752729870807" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
