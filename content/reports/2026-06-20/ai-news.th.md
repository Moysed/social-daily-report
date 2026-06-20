---
type: social-topic-report
date: '2026-06-20'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-20T15:09:52+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 243
salience: 0.35
sentiment: mixed
confidence: 0.5
tags:
- ai-tooling
- open-models
- glm
- anthropic-pricing
- claude-code
- codegen
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2068306560569458688/img/SR1ke0qx6mBBzQ7Y.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-20

## TL;DR
- feed ส่วนใหญ่วันนี้เกิดจาก keyword collision: 'Gemini' ที่นี่หมายถึง solo stage ของ Vernon จาก SEVENTEEN [1][3][6] และ fanmeet ของนักแสดงไทย Gemini ในเวียดนาม [4][11][14] — ไม่ใช่ model ของ Google — signal จริงเรื่อง AI tooling มีน้อย
- GLM-5.2 (open weights ใบอนุญาต MIT) มีรายงานว่าเทียบ Codex ได้บน coding task จริงผ่าน OpenCode จากการใช้งาน 3 วัน [22] และอ้างว่า hallucinate น้อยกว่า GPT-5.5 ถึง ~3 เท่า [60]
- การเปลี่ยนระบบ billing แบบ usage-based ของ Anthropic ทำให้บิล AI ของบริษัทหนึ่ง (Workato) พุ่ง 700% ภายในวันเดียว จากเดิมที่จ่ายเป็น flat fee รายเดือน [32]
- Fable จะออกจาก Claude Code subscriptions ใน ~3 วัน ตาม Theo [9]
- GPT-5.6 Pro ถูกอ้างว่า one-shot เกมแนว Sims เป็นไฟล์ .html ไฟล์เดียวใน 48 นาทีโดยไม่ใช้ coding harness [49] — เป็น demo เดี่ยว ยังไม่ได้รับการยืนยัน

## What happened
Feed ถูกครอบงำด้วยเนื้อหาที่ไม่เกี่ยวกับ AI ซึ่ง match คำว่า 'Gemini' (stage Caratland ของ SEVENTEEN [1][3][6][19][28][35] และ fanmeet GeminiFourth [4][11][12][14][24][25]) และคำว่า 'Claude' (การเสียชีวิตของผู้ร่วมก่อตั้ง Ubisoft Claude Guillemot [20][26][38][46]) เมื่อกรองออกแล้ว เหลือ signal ด้าน AI tooling ที่ชัดเจนอยู่ไม่กี่ชิ้น นักพัฒนารายหนึ่งรายงานว่าใช้ GLM-5.2 กับ OpenCode แทน Codex 3 วันโดยไม่พบ regression ในการแก้ bug หรือ feature work [22] และมีโพสต์แยกที่อ้างว่า GPT-5.5 hallucinate มากกว่า GLM-5.2 (MIT-licensed) ถึง ~3 เท่า [60] ด้านต้นทุน มีรายงานว่าการเปลี่ยน billing ของ Anthropic ทำให้บิล Workato พุ่ง 700% ในวันเดียวหลังจากเคยจ่าย flat fee [32] และ Theo แจ้งว่า Fable จะออกจาก Claude Code subscriptions ใน ~3 วัน [9]

## Why it matters (reasoning)
สองประเด็นที่มีผลต่อ AI workflow ของ studio ได้แก่ ประการแรก open-weight models: ถ้า GLM-5.2 เทียบ Codex ได้จริงบน coding task [22] และ hallucinate น้อยกว่า model GPT-5.5/5.6-class [60] ต้นทุนและ lock-in ของ agentic coding จะลดลง — ใบอนุญาต MIT ยังตัดความเสี่ยงเรื่อง per-seat metering ออกด้วย ประการที่สอง ความผันผวนด้านต้นทุน: การเปลี่ยน billing ของ Anthropic กับบิลที่พุ่ง 700% [32] บวกกับการถอด Fable จาก Claude Code [9] แสดงให้เห็นว่าราคาและความพร้อมของ model สามารถเปลี่ยนได้โดยแทบไม่มีการแจ้งล่วงหน้า ซึ่งเป็นความเสี่ยงด้านงบประมาณและ continuity สำหรับทีมที่ build tooling บน vendor เดียว signal ด้าน edutech จากนอร์เวย์ที่เกือบห้ามใช้ AI ในโรงเรียนประถม [36] เป็นสัญญาณเชิงกฎหมายที่เกี่ยวข้องกับผลิตภัณฑ์ e-learning แม้จะเน้นเรื่องการ deploy ในชั้นเรียน ไม่ใช่ tooling ก็ตาม ข้อควรระวัง: claims ที่แรงที่สุดในที่นี้ ([22][49][60]) มาจากโพสต์ social เดี่ยวหรือ demo ครั้งเดียว ไม่ใช่ benchmark หรือ artifact ที่ reproduce ได้

## Possibility
Likely: open models อย่าง GLM ยังคงตามประชิด proprietary coding models ทำให้ dual-stack (proprietary + open ผ่าน harness แบบ OpenCode) เป็นตัวเลือก hedge ที่ใช้งานได้จริง [22][60] Plausible: ทีมอื่นจะเจอ cost spike แบบไม่คาดคิดมากขึ้นเมื่อ vendor ย้ายจาก flat เป็น usage-based pricing ส่งผลให้ต้องทำ usage audit และตั้ง cap [32] Plausible: ข้อจำกัดการใช้ AI ในชั้นเรียนจะขยายออกไปนอกนอร์เวย์ ซึ่งจะส่งผลต่อการวางตำแหน่งผลิตภัณฑ์ edutech [36] Unlikely บนหลักฐานปัจจุบัน: GPT-5.6 Pro สามารถ one-shot เกมเต็มรูปแบบใน production ได้อย่างน่าเชื่อถือ — [49] เป็นเพียง demo .html เดี่ยวที่ยังไม่ได้ reproduce

## Org applicability — NDF DEV
1) ทดสอบ GLM-5.2 ผ่าน OpenCode เทียบกับ Claude/Codex setup ปัจจุบันบน task จริงของ NDF ก่อนตัดสินใจใดๆ (effort: med) [22][60] 2) Audit การใช้งาน Claude Code / Anthropic และตั้ง spend alert ตอนนี้เลย เนื่องจากการเปลี่ยน billing และรายงานบิลพุ่ง 700% (effort: low) [32] 3) ถ้ามี workflow ที่ depend on Fable ใน Claude Code ให้วางแผนเอาออกภายใน ~3 วัน (effort: low) [9] 4) สำหรับสาย edutech/e-learning ให้บันทึกกรณีนอร์เวย์เป็น compliance signal และทำ AI features ให้เป็น optional/configurable สำหรับ school deployment (effort: low) [36] 5) ให้ถือว่า GPT-5.6 Pro one-shot codegen เป็นแค่ prototyping experiment ที่ยังพิสูจน์ไม่ได้ ไม่ใช่ pipeline (effort: low) [49] Skip: item ทั้งหมดเรื่อง Gemini ไอดอล การรายงานการเสียชีวิตของ Ubisoft และ crypto snapshot — ไม่มีความเกี่ยวข้องกับ workflow

## Signals to Watch
- การใช้งาน GLM-5.2 ผ่าน OpenCode เป็นตัวแทน Codex — ติดตาม benchmark ที่ reproduce ได้ ไม่ใช่แค่ anecdote เดี่ยว [22][60]
- ผลกระทบจาก usage-based billing ของ Anthropic — ติดตามรายงานบิลพุ่งแบบกะทันหันเพิ่มเติม [32]
- การถอด Fable จาก Claude Code subscriptions ตาม timeline ~3 วัน [9]
- กฎหมาย AI ในโรงเรียนที่อาจขยายออกนอกนอร์เวย์ ซึ่งเกี่ยวข้องกับการวางตำแหน่ง edutech [36]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **DeusData/codebase-memory-mcp** — MCP server ด้าน code intelligence ประสิทธิภาพสูง จัดทำ index codebase ลงใน persistent knowledge graph | rss | <https://github.com/DeusData/codebase-memory-mcp> |
| **google-research/timesfm** — TimesFM (Time Series Foundation Model) คือ pretrained foundation model สำหรับ time-series ที่พัฒนาโดย Google | rss | <https://github.com/google-research/timesfm> |
| **palmier-io/palmier-pro** — video editor สำหรับ macOS ที่ build มาเพื่อ AI โดยเฉพาะ ต้องการ macOS 26 (Tahoe) | rss | <https://github.com/palmier-io/palmier-pro> |
| **koala73/worldmonitor** — dashboard intelligence แบบ real-time ระดับโลก รวม AI-powered news aggregation, geopolitical monitoring และการวิเคราะห์ | rss | <https://github.com/koala73/worldmonitor> |
| **aishwaryanr/awesome-generative-ai-guide** — repository รวม research update ด้าน generative AI, interview resources, notebooks และอื่นๆ | rss | <https://github.com/aishwaryanr/awesome-generative-ai-guide> |
| **BuilderIO/agent-native** — framework สำหรับ build applications แบบ agent-native แบบ open-source | rss | <https://github.com/BuilderIO/agent-native> |
| **chopratejas/headroom** — compress tool output, log, file และ RAG chunk ก่อนส่งถึง LLM ลด token ได้ 60-95% | rss | <https://github.com/chopratejas/headroom> |
| **calesthio/OpenMontage** — ระบบ agentic video production แบบ open-source ระบบแรกของโลก มี 12 pipeline, 52 tool, 500+ agent skill | rss | <https://github.com/calesthio/OpenMontage> |
| **zai-org/GLM-5** — GLM-5: จาก Vibe Coding สู่ Agentic Engineering รวม GLM-5.2, GLM-5.1 และ GLM-5 | rss | <https://github.com/zai-org/GLM-5> |
| **withastro/flue** — sandbox agent framework — Flue คือ Agent Harness Framework ที่ไม่ใช่แค่ SDK อีกตัว | rss | <https://github.com/withastro/flue> |
| **n0-computer/iroh** — เมื่อ IP address ไม่เสถียร ให้ dial ด้วย key แทน — modular networking stack ที่เขียนด้วย Rust | rss | <https://github.com/n0-computer/iroh> |
| **obra/superpowers** — agentic skills framework และ software development methodology ที่ใช้งานได้จริง | rss | <https://github.com/obra/superpowers> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | vernonsource | ^5594 c0 | [[full] gemini (jun solo) by vernon at caratland 2026 d-1 https://t.co/wpz2iEjq80](https://x.com/vernonsource/status/2068307702271602696) |
| x | kwansources | ^4560 c0 | [THE TRANSITION OF SEUNGKWAN TRIGGER TO VERNON GEMINI https://t.co/ZejCbBXYX9](https://x.com/kwansources/status/2068302911936045494) |
| x | vernonsource | ^3604 c0 | [VERNON DOING GEMINI FOR CARATLAND WHAT THE HELL https://t.co/jMBvTkvQG0](https://x.com/vernonsource/status/2068302530170511465) |
| x | geminiscity | ^3106 c4 | [👥: Fourth suay mak! 4️⃣: Fourth suay? ♊️: 😎👍🏻 4️⃣: Fourth suay mak~ ♊️: [nods] G](https://x.com/geminiscity/status/2068255930610024765) |
| x | don_rickardo | ^2984 c29 | [Closing gemini season out w these https://t.co/TJ3StCo9tq](https://x.com/don_rickardo/status/2068257515138355609) |
| x | coupslovre | ^2957 c0 | [caratland 2026 solo stage switch! #세븐틴 scoups — Happy Virus joshua — Jungle jun ](https://x.com/coupslovre/status/2068307759716815147) |
| x | flamehanie | ^2766 c1 | [VERNON - GEMINI (JUN'S SOLO) 😭😭 HIS VOCALSSS https://t.co/Uegmlw3OJ6](https://x.com/flamehanie/status/2068303116353855708) |
| x | minghaocheoI_ | ^2693 c1 | [VERNON DOING JUN'S GEMINI STAGE OH MY GODDDDDD OH MY GOD THIS IS SO SHOCKINGJDMG](https://x.com/minghaocheoI_/status/2068303019675148559) |
| x | theo | ^2519 c130 | [3 days left of using Fable in your Claude Code sub! Better maximize that token u](https://x.com/theo/status/2068273183212638384) |
| x | KyeomsBaekery | ^2217 c0 | [THE TRANSITION FROM SEUNGKWAN'S TRIGGER TO VERNON'S GEMINI OH GOD?!!! Insane…. h](https://x.com/KyeomsBaekery/status/2068302428504727637) |
| x | hopyjoy | ^2106 c2 | [Gemini wears his bag with sunflower 🌻 #GeminiFourthFMinVietnam #geminifourth #ge](https://x.com/hopyjoy/status/2068293071922749612) |
| x | prettiest_to_GF | ^2055 c11 | [#GeminiFourthFMinVietnam BIRTHDAY CAKE FOR GEMINI AND CONGRATS CAKE FOR FOT ❤️🙇‍](https://x.com/prettiest_to_GF/status/2068245875462427114) |
| x | AmandaAskell | ^2026 c85 | [I had chronic pain for most of my life until a doctor did an MRI of the pain sou](https://x.com/AmandaAskell/status/2068218515723866477) |
| x | Geminint_family | ^2011 c2 | [Happy 22nd Birthday Gemini 🎂👦🏻❤️ GEMINIFOURTH VN FANMEET #GeminiFourthFMinVietna](https://x.com/Geminint_family/status/2068240510373044507) |
| x | YasmeenOne | ^1913 c0 | [VERNON AND JUNS HIGHNOTES IN GEMINI!!!! 🥹🪽🐻‍❄️🐱 OUR VERJUN https://t.co/XkhdpuAy](https://x.com/YasmeenOne/status/2068305007745605988) |
| x | aydellch | ^1857 c3 | [: From now on I hope you'll take a better care of him ♊️: Is Father a shipper? ♊](https://x.com/aydellch/status/2068297239353811345) |
| x | vernonsource | ^1625 c0 | [the transition from seungkwan trigger to vernon gemini 😯 https://t.co/Rmki3IjWk1](https://x.com/vernonsource/status/2068304999487258662) |
| x | itsgemfourth | ^1538 c0 | [gemini always watching fotfot performing from the backstage... look at him :((( ](https://x.com/itsgemfourth/status/2068248014389756017) |
| x | minghaocheoI_ | ^1406 c2 | [FULL SOLO REVERSE STAGES FOR CARATLAND OH MY GOD ❤️‍🔥 seungkwan - trigger vernon](https://x.com/minghaocheoI_/status/2068338131447996534) |
| x | Pirat_Nation | ^1398 c64 | [Claude Guillemot, one of the co-founders of Ubisoft, has died in a plane crash n](https://x.com/Pirat_Nation/status/2068291114977681664) |
| x | nongsiii | ^1144 c1 | [Gemini doing the love wins all🫣 GEMINIFOURTH VN FANMEET #GeminiFourthFMinVietnam](https://x.com/nongsiii/status/2068237621927768470) |
| x | burkov | ^1035 c86 | [For the last three days, I've been using GLM 5.2 with OpenCode instead of Codex ](https://x.com/burkov/status/2068258575315542352) |
| x | gemfourtty | ^1005 c0 | [gemini really just stays still and lets his baby say whatever he wants, even whe](https://x.com/gemfourtty/status/2068245150401212630) |
| x | itsgemfourth | ^993 c0 | [GEMINIFOURTH VN FANMEET #GeminiFourthFMinVietnam 4️⃣ fourth loves gemini a lot! ](https://x.com/itsgemfourth/status/2068246938261344736) |
| x | GeminiFourthsup | ^958 c0 | [So sweet with each other 🫠🫠 https://t.co/P4sawP8ML2 https://t.co/66cuZS4qYC GEMI](https://x.com/GeminiFourthsup/status/2068238348599033900) |
| x | Dexerto | ^930 c62 | [Claude Guillemot, one of Ubisoft's five co-founding brothers, has died in a priv](https://x.com/Dexerto/status/2068321361710211225) |
| x | g4loversclub | ^913 c0 | [fourth singing the lyrics to all in while gemini does the choreo instead theyre ](https://x.com/g4loversclub/status/2068252518648312063) |
| x | lovrehani | ^903 c0 | [SEUNGKWAN — TRIGGER VERNON — GEMINI DINO — FORTUNATE CHANGE MINGYU — SHINING STA](https://x.com/lovrehani/status/2068306816212353168) |
| radar | ck2 | ^889 c375 | [Hyundai buys Boston Dynamics](https://startupfortune.com/hyundai-takes-full-control-of-boston-dynamics-as-softbank-exits-for-325-million/) |
| x | minghaocheoI_ | ^860 c0 | [THIS TRANSITION FROM SEUNGKWAN'S TRIGGER TO VERNON'S GEMINI STAGE?/!/?/? https:/](https://x.com/minghaocheoI_/status/2068301904552362342) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vernonsource</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5594 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vernonsource/status/2068307702271602696">View @vernonsource on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“[full] gemini (jun solo) by vernon at caratland 2026 d-1 https://t.co/wpz2iEjq80”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>วิดีโอแฟนถ่าย Vernon (SEVENTEEN) เพอร์ฟอร์ม solo 'Gemini' ในงานคอนเสิร์ต Caratland 2026 — ไม่เกี่ยวกับ Google Gemini</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vernonsource/status/2068307702271602696" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kwansources</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4560 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kwansources/status/2068302911936045494">View @kwansources on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“THE TRANSITION OF SEUNGKWAN TRIGGER TO VERNON GEMINI https://t.co/ZejCbBXYX9”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แอคเคาท์แฟน K-pop โพสต์เรื่อง Seungkwan และ Vernon จาก SEVENTEEN ในบริบท persona chatbot — ไม่มีเนื้อหาเชิงเทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kwansources/status/2068302911936045494" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vernonsource</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3604 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vernonsource/status/2068302530170511465">View @vernonsource on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“VERNON DOING GEMINI FOR CARATLAND WHAT THE HELL https://t.co/jMBvTkvQG0”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับ reaction การแสดงของ Vernon ในงาน CaratLand — 'Gemini' หมายถึงเพลง/ธีมการแสดง ไม่ใช่ Google Gemini</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vernonsource/status/2068302530170511465" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@geminiscity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3106 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/geminiscity/status/2068255930610024765">View @geminiscity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“👥: Fourth suay mak! 4️⃣: Fourth suay? ♊️: 😎👍🏻 4️⃣: Fourth suay mak~ ♊️: [nods] Gemini agrees that Fourth is pretty 🙂‍↔️🙂‍↔️🙂‍↔️ GEMINIFOURTH VN FANMEET #GeminiFourthFMinVietnam https://t.co/ZIBfjR6LXR”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แอคเคาท์แฟนคลับโพสต์เกี่ยวกับ fanmeet ของนักแสดง 'Fourth' ในเวียดนาม ไม่เกี่ยวกับ Google Gemini AI</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/geminiscity/status/2068255930610024765" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@don_rickardo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2984 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/don_rickardo/status/2068257515138355609">View @don_rickardo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Closing gemini season out w these https://t.co/TJ3StCo9tq”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์กำกวมบอกว่า 'ปิด Gemini season' พร้อมลิงก์สั้นที่ไม่มีบริบทใด ๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/don_rickardo/status/2068257515138355609" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@coupslovre</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2957 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/coupslovre/status/2068307759716815147">View @coupslovre on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“caratland 2026 solo stage switch! #세븐틴 scoups — Happy Virus joshua — Jungle jun — Shake It Off minghao — Raindrops mingyu — Shining Star dk — Skyfall seungkwan — Trigger vernon — Gemini dino — Fortuna”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับแจ้งรายชื่อเพลง solo stage ของสมาชิก Seventeen ในคอนเสิร์ต Caratland 2026</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/coupslovre/status/2068307759716815147" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@flamehanie</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2766 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/flamehanie/status/2068303116353855708">View @flamehanie on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“VERNON - GEMINI (JUN’S SOLO) 😭😭 HIS VOCALSSS https://t.co/Uegmlw3OJ6”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับรีแอคต่อ VERNON และ JUN จาก SEVENTEEN พร้อมคลิปเพลง ไม่มีเนื้อหาเชิงเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/flamehanie/status/2068303116353855708" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@minghaocheoI_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2693 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/minghaocheoI_/status/2068303019675148559">View @minghaocheoI_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“VERNON DOING JUN'S GEMINI STAGE OH MY GODDDDDD OH MY GOD THIS IS SO SHOCKINGJDMGM WOAHHHH https://t.co/gpghwJqnW9”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคลับ react สดต่อ Vernon จาก SEVENTEEN ที่ขึ้น stage แสดงเพลง Gemini แทน Jun</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/minghaocheoI_/status/2068303019675148559" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
