---
type: social-topic-report
date: '2026-06-15'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-15T04:24:31+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 242
salience: 0.25
sentiment: mixed
confidence: 0.5
tags:
- local-llm
- llama.cpp
- model-merging
- offline-tools
- cost-economics
- low-signal
thumbnail: https://pbs.twimg.com/media/HKyzi0WXwAAn7BS.jpg
translated_by: claude-sonnet-4-6
---

# ข่าว AI & ทักษะใหม่ — 2026-06-15

## TL;DR
- วันนี้ artifact ที่ใช้ได้จริงมีน้อย สองอันที่มีคุณค่าโดยตรง: คู่มือ llama.cpp ฉบับมิถุนายน 2026 สำหรับรัน local LLM บน consumer GPU ด้วย one-line command ไม่ต้องใช้ Docker/Python [16], และ Kage เครื่องมือ Show HN ที่ snapshot เว็บไซต์ใดก็ได้ลงใน offline binary ไฟล์เดียว [32]
- model-merging ปรากฏสองครั้ง: LLM "โฮมเมด" จาก Rio de Janeiro ถูก flag บน GitHub ว่าเป็น merge ของโมเดลที่มีอยู่แล้ว [49], และ meme เกี่ยวกับการรัน merged GGUF (gemma-4 + แท็ก 'coder'/'fable5'/'composer') บน 8GB VRAM ที่ความเร็ว 20+ tok/s [36]
- สัญญาณต้นทุน: SemiAnalysis อ้างว่า subscription ChatGPT $200/เดือน อาจทำให้ OpenAI แบกต้นทุนสูงถึง $14,000 หากถูกใช้งานเต็มที่ [5]
- รายการที่ได้ engagement สูงส่วนใหญ่ไม่เกี่ยวข้อง: ดาราศาสตร์ ('Gemini new moon'), กีฬา, และการกล่าวถึง 'Claude'/'Gemini' ในบริบทสัตว์เลี้ยงและจิตรกร [6][7][20][23][51] เรื่องเล่า 'Anthropic Fable 5 / Mythos export-ban / White House' ขนาดใหญ่ [9][15][26][29][59] ใช้ชื่อโมเดลที่ไม่ตรงกับ release จริงใดๆ และอ่านแล้วเหมือนข่าวลือ/satire — ถือว่ายังไม่ verified

## สิ่งที่เกิดขึ้น
สำหรับโฟกัสที่ระบุไว้ (AI tools, frameworks, plugins, repos, research drops ใหม่) signal ที่ชัดเจนมีน้อย artifact ที่ชัดที่สุด: คู่มือ llama.cpp สำหรับ local inference บน consumer GPU พร้อม one-liner แบบ copy-paste [16], และ Kage เครื่องมือ open-source สำหรับ mirror เว็บไซต์ลงใน offline binary ไฟล์เดียว [32] model-merging ในชุมชนปรากฏสองรูปแบบ — GitHub issue สาธารณะที่อ้างว่าโมเดล 'โฮมเมด' ระดับชาติ/ภูมิภาคเป็นแค่ merge ที่ rebadge [49], และมุกตลกเกี่ยวกับ GGUF หลาย merge ที่รันได้เร็วบน 8GB VRAM [36] ด้านเศรษฐศาสตร์ ตัวเลขจาก SemiAnalysis ที่ถูกอ้างถึงระบุต้นทุนการใช้งานหนักของแผน ChatGPT $200 สูงถึง $14,000 [5]

## ทำไมจึงสำคัญ (เหตุผล)
รายการที่ใช้ได้จริงชี้ทิศทางเดียวกัน: local, low-cost inference พัฒนาขึ้นเรื่อยๆ เส้นทาง llama.cpp แบบไม่ต้อง Docker บน consumer GPU [16] บวกกับ merged GGUF เร็วบนการ์ด 8GB [36] ลดเกณฑ์การเข้าถึง offline/on-device AI ในเกม, XR, และ edutech ซึ่ง privacy และไม่มีค่าใช้จ่ายต่อ call เป็นเรื่องสำคัญ ข้อโต้แย้งเรื่อง merge [49] คือต้นทุนลำดับที่สอง: provenance และ licensing ของโมเดลในชุมชนไม่ชัดเจน โมเดล local 'ฟรี' จึงมีความเสี่ยงทางกฎหมายและคุณภาพแฝงอยู่ ตัวเลขต้นทุนจาก SemiAnalysis [5] อธิบายแรงกดดันของ vendor ต่อ rate limit และเรื่องร้องเรียน 'nerf' [40] — ผู้ใช้งานหนักทำให้ขาดทุน ซึ่งทำให้งบประมาณ hosted API ไม่แน่นอนและเสริมเหตุผลให้ self-host workload ประจำ

## ความเป็นไปได้
น่าจะเกิด: tooling สำหรับ local/edge LLM พัฒนาต่อเนื่องและใช้ได้จริงสำหรับงาน studio ที่ไม่ critical แล้วตอนนี้ [16][36] เป็นไปได้: การตรวจสอบ provenance ของ merged model เติบโตเป็นปัญหา licensing ที่ทีมต้องตรวจก่อน ship [49] ไม่น่าจะเชื่อถือได้ตามที่ระบุ: เรื่องเล่า 'Anthropic/Fable 5/Mythos export ban' [15][26][59] — ชื่อโมเดลและรายละเอียดยังไม่ verified และไม่สอดคล้องกับ release ที่รู้จัก อย่านำไปปฏิบัติจนกว่า primary source (เช่น Reuters/Axios รายงานตรง) จะยืนยัน [52] ไม่มี source ใดให้ probability ที่ defend ได้ จึงไม่ระบุไว้ที่นี่

## ความเกี่ยวข้องกับองค์กร — NDF DEV
1) ทดลอง setup llama.cpp local-LLM [16] บน dev GPU สำหรับ offline prototyping (NPC dialogue, draft content edutech, tagging asset) ที่ต้องการ data privacy หรือไม่มีค่าใช้จ่ายต่อ call — effort: ต่ำ 2) ทดสอบ Kage [32] สำหรับ package offline docs/demos หรือ kiosk/XR build ที่ต้องการ site แบบ self-contained — effort: ต่ำ 3) หากใช้ community/merged GGUF ให้เพิ่มขั้นตอนตรวจ provenance + license ใน eval step ก่อน ship ทุกครั้ง [36][49] — effort: กลาง 4) จัดทำ cost model คร่าวๆ สำหรับ hosted API เมื่อแรงกดดัน unit economics ของ vendor เพิ่มขึ้น [5] แล้ว route งาน bulk/low-stakes ไปยัง local model — effort: ต่ำ ข้ามได้: เรื่องเล่า Anthropic/White House/Fable [15][26][29][59] และรายการดาราศาสตร์/กีฬา/meme ทั้งหมด [6][7][20][23] — ไม่มีคุณค่าด้าน engineering

## สัญญาณที่ต้องจับตา
- ข้อโต้แย้ง provenance ของ model-merge ที่เคลื่อนมาสู่ GitHub issue สาธารณะ [49]
- คู่มือ local inference บน consumer GPU แบบ one-line setup [16] และ merged GGUF เร็วบน [36]
- Unit economics ของ vendor: ต้นทุนการใช้งานหนักเทียบกับราคาคงที่ [5] โยงกับเรื่องร้องเรียน rate-limit/quality [40]
- มุมมองคนสงสัยว่า AI ไม่ได้เพิ่มจำนวน app ที่ ship ออกมา [22] — counter-signal ต่อ tooling hype

## Repos & Tools ที่ควรลอง
| repo | source | url |
|---|---|---|
| **tamnd/kage** — Show HN: Kage – Shadow any website to a single binary for offline viewing | radar | <https://github.com/tamnd/kage> |
| **nex-agi/Nex-N2** — LLM "โฮมเมด" จาก Rio de Janeiro ที่ถูกพบว่าเป็น merge ของโมเดลที่มีอยู่แล้ว | radar | <https://github.com/nex-agi/Nex-N2> |
| **iptv-org/iptv** — Collection of publicly available IPTV channels from all over the world | rss | <https://github.com/iptv-org/iptv> |
| **freeCodeCamp/freeCodeCamp** — open-source codebase และหลักสูตรของ freeCodeCamp.org เรียน math, programming, และ computer science | rss | <https://github.com/freeCodeCamp/freeCodeCamp> |
| **pytest-dev/pytest** — pytest framework สำหรับเขียน test ขนาดเล็ก ขยายได้ถึง functional test ซับซ้อน | rss | <https://github.com/pytest-dev/pytest> |
| **swc-project/swc** — platform บน Rust สำหรับ Web เพื่อเพิ่มความเร็ว development SWC (Speedy Web Compiler) | rss | <https://github.com/swc-project/swc> |
| **chatwoot/chatwoot** — live-chat, email support, omni-channel desk แบบ open-source ทางเลือกแทน Intercom, Zendesk, Salesforce | rss | <https://github.com/chatwoot/chatwoot> |
| **NVIDIA/SkillSpector** — security scanner สำหรับ AI agent skills ตรวจ vulnerability, malicious pattern, และความเสี่ยงด้าน security | rss | <https://github.com/NVIDIA/SkillSpector> |
| **meshery/meshery** — cloud native manager หาก Meshery มีประโยชน์ ★ repository นี้เพื่อแสดงการสนับสนุน | rss | <https://github.com/meshery/meshery> |
| **cypress-io/cypress** — testing ที่เร็ว ง่าย และเชื่อถือได้สำหรับทุกอย่างที่รันใน browser | rss | <https://github.com/cypress-io/cypress> |
| **GorvGoyl/Clone-Wars** — clone แบบ open-source กว่า 100 รายการของไซต์ดัง เช่น Airbnb, Amazon, Instagram, Netflix, Tiktok, Spotify | rss | <https://github.com/GorvGoyl/Clone-Wars> |
| **Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots** — ตำราเรียน open-source เกี่ยวกับ Autonomous Robots เน้น computation | rss | <https://github.com/Introduction-to-Autonomous-Robots/Introduction-to-Autonomous-Robots> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | katwhetstone_ | ^4495 c0 | [re: Freddie Andersen I really hope that we, as a general sports media sphere, ca](https://x.com/katwhetstone_/status/2066323300293152868) |
| x | levelsio | ^2986 c47 | [I'm back in America My hotel room has: - AC that goes down to 18°C/64°F but my s](https://x.com/levelsio/status/2066262537965084785) |
| x | MrBeastInsights | ^2779 c69 | [MrBeast used Gemini AI for a short portion of his recent video, "50 YouTube Lege](https://x.com/MrBeastInsights/status/2066224212365259035) |
| x | charliebcurran | ^2591 c129 | [I used AI to explain the Anthropic drama to my girlfriend, with fruit. https://t](https://x.com/charliebcurran/status/2066297562244751614) |
| x | interesting_aIl | ^2176 c30 | [A $200 ChatGPT subscription can cost OpenAI $14,000 if utilized to its full pote](https://x.com/interesting_aIl/status/2066271768411595131) |
| x | astropriestesss | ^1928 c9 | [this gemini new moon is for the writers, teachers, speakers, storytellers, peopl](https://x.com/astropriestesss/status/2066224337061822795) |
| x | labrujxnegra | ^1517 c4 | [Today is the new moon in gemini, new moons are a great time to set intentions fo](https://x.com/labrujxnegra/status/2066268236526837791) |
| x | energyhealingjw | ^1253 c40 | [This Super New Moon arrives in 5 hours in electric Gemini. If this message finds](https://x.com/energyhealingjw/status/2066274614485901405) |
| x | PolymarketMoney | ^1223 c50 | [NEW IN: Anthropic is now projected to hit a $1,750,000,000,000 valuation this ye](https://x.com/PolymarketMoney/status/2066273639251456072) |
| x | mixereilish | ^1178 c0 | [Claude as a bridesmaid is the best 🥹 love their friendship https://t.co/7bNfXg95](https://x.com/mixereilish/status/2066235387496825093) |
| x | wooyofot | ^1143 c0 | [the size difference??? the way gemini staring at fourth like THAT...those veiny ](https://x.com/wooyofot/status/2066255241478316238) |
| x | Youssofal_ | ^1124 c43 | [OMG THEY ARE DROPPING IT! ANTHROPIC IS SCREWED! Scores higher than Fable in ever](https://x.com/Youssofal_/status/2066230597329072285) |
| x | DrIndyEinstein | ^1105 c4 | [if you want to shift your life, I highlyyy recommend working with the new moon e](https://x.com/DrIndyEinstein/status/2066286486060769610) |
| x | shakoistsLog | ^1092 c36 | [it's insane to me openai expects me to read two answers and pick the best one fo](https://x.com/shakoistsLog/status/2066291909891641498) |
| x | kimmonismus | ^1069 c58 | [Just now: Anthropic is flying senior technical staff to Washington to repair its](https://x.com/kimmonismus/status/2066240276075528533) |
| x | TraffAlex | ^973 c38 | [🖥️ Best Local LLMs for Consumer GPUs — llama.cpp Guide (June 2026) What I actual](https://x.com/TraffAlex/status/2066236717015728227) |
| x | chamath | ^957 c81 | [The CEOs of the Mags have each been in the seat for decades. Love them or hate t](https://x.com/chamath/status/2066229609373610473) |
| x | JoshuaDKaye_ | ^943 c5 | [You cannot make this astrology up. Two helicopters collided in mid-air. Two mach](https://x.com/JoshuaDKaye_/status/2066309353787789429) |
| x | KoronellukinhaC | ^908 c10 | [Claude the wolf 🐺 https://t.co/MGaeB0Jqef](https://x.com/KoronellukinhaC/status/2066297929053159777) |
| x | Sportsnet | ^787 c4 | ["It's tough to really describe how much he [Claude Lemieux] meant to me and how ](https://x.com/Sportsnet/status/2066365156720877897) |
| x | supermoongirl9 | ^721 c2 | [gemini new moon lesson: if there's one universal rule in this life is that bette](https://x.com/supermoongirl9/status/2066291347963716033) |
| x | antoniogm | ^696 c95 | [You can finally say this without being canceled: AI isn't creating a Cambrian ex](https://x.com/antoniogm/status/2066234772519874569) |
| x | Havenlust | ^671 c5 | [Claude Monet https://t.co/3mvTGLjD6J](https://x.com/Havenlust/status/2066232113922248766) |
| x | LokiJulianus | ^631 c7 | [Sucks to be Anthropic: you're flying to DC on a Sunday to get your model off an ](https://x.com/LokiJulianus/status/2066343056316432490) |
| x | GreenIrisTarot | ^590 c1 | [˚୨୧⋆｡˚⋆ what's coming in the next 7 days? 🤍🕊️✨ apply to s, m, r ♈︎ Aries: strong](https://x.com/GreenIrisTarot/status/2066222253772067018) |
| x | kimmonismus | ^584 c67 | [Keeps getting worse: It seems that the Chinese government ("China-linked group")](https://x.com/kimmonismus/status/2066259589381669169) |
| x | DoseofTarot | ^584 c3 | [Mutable Signs Gemini , Pisces , Sagittarius , Virgo Release your ex Yes , you're](https://x.com/DoseofTarot/status/2066321084014596323) |
| x | PromptLLM | ^560 c5 | [Claude May of discovered a new area of self help https://t.co/hFNEF3I51G](https://x.com/PromptLLM/status/2066251631570694558) |
| x | robj3d3 | ^545 c57 | [Update on Fable 5: > Anthropic staff have flown to Washington > Ongoing talks ar](https://x.com/robj3d3/status/2066239964346777912) |
| x | ryiacy | ^488 c29 | [My interpretation of this: Right now, Anthropic and OpenAI are making a killing ](https://x.com/ryiacy/status/2066260212772679864) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@katwhetstone_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4495 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/katwhetstone_/status/2066323300293152868">View @katwhetstone_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“re: Freddie Andersen I really hope that we, as a general sports media sphere, can get to a place where leading with empathy is the norm. Andersen played 12 playoff games. He lost his agent and close f”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจารณ์กีฬาเรียกร้องให้แสดงความเห็นอกเห็นใจต่อ Freddie Andersen ผู้รักษาประตู NHL ที่เพิ่งสูญเสีย agent และเพื่อนสนิท Claude Lemieux จากการฆ่าตัวตาย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/katwhetstone_/status/2066323300293152868" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2986 · 💬 47</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2066262537965084785">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm back in America My hotel room has: - AC that goes down to 18°C/64°F but my sensor shows it's 16°C/61°F! Ice cold means perfect sleep - $100 in free spending on anything + full minibar with beautif”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio เปรียบโรงแรม US vs เนเธอร์แลนด์ราคาเดียวกัน สรุปว่า US คุ้มกว่า — AC เย็นกว่า ทำความสะอาดทุกวัน มี minibar และ amenities ให้ครบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2066262537965084785" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MrBeastInsights</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2779 · 💬 69</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MrBeastInsights/status/2066224212365259035">View @MrBeastInsights on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“MrBeast used Gemini AI for a short portion of his recent video, “50 YouTube Legends Fight For $1,000,000.” The Gemini icon can be seen in the bottom right corner, apparently left in by accident. https”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>วิดีโอ '50 YouTube Legends Fight For $1,000,000' ของ MrBeast โชว์ Gemini AI interface ติดจอโดยไม่ตั้งใจระหว่าง edit</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MrBeastInsights/status/2066224212365259035" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@charliebcurran</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2591 · 💬 129</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/charliebcurran/status/2066297562244751614">View @charliebcurran on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I used AI to explain the Anthropic drama to my girlfriend, with fruit. https://t.co/8Lth4wRfrZ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้สร้าง analogy ผลไม้อธิบาย Anthropic drama ให้แฟนฟัง — เป็น content ตลกที่ viral</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/charliebcurran/status/2066297562244751614" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@interesting_aIl</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2176 · 💬 30</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/interesting_aIl/status/2066271768411595131">View @interesting_aIl on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A $200 ChatGPT subscription can cost OpenAI $14,000 if utilized to its full potential, per SemiAnalysis https://t.co/3laNcTRyBV”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>SemiAnalysis ประเมินว่า user ที่ใช้ ChatGPT Pro $200/เดือนเต็มที่ อาจทำให้ OpenAI แบกต้นทุน compute สูงถึง $14,000/เดือน ต่อคน — ขาดทุน 70 เท่า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>OpenAI กำลัง subsidize การใช้งานหนักในราคาขาดทุนหนัก — สัญญาณว่า flat-rate AI subscription แบบนี้อาจอยู่ไม่ได้นานโดยไม่มี usage cap</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอน budget AI tools ให้ทีม ให้คิดไว้ว่า flat-rate แบบนี้จะเปลี่ยนเป็น usage-based — อย่า build workflow ที่ assume ว่า limit ปัจจุบันจะอยู่ถาวร</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/interesting_aIl/status/2066271768411595131" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@astropriestesss</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1928 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/astropriestesss/status/2066224337061822795">View @astropriestesss on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“this gemini new moon is for the writers, teachers, speakers, storytellers, people wanting to grow on social media, people wanting to share their messages with the WORLD. time to get things in motion!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บัญชีดาราศาสตร์โหราศาสตร์โพสต์ว่าช่วง Gemini new moon เป็นสัญญาณทางจิตวิญญาณสำหรับนักเขียน ครู และคนทำ social media</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/astropriestesss/status/2066224337061822795" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@labrujxnegra</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1517 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/labrujxnegra/status/2066268236526837791">View @labrujxnegra on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Today is the new moon in gemini, new moons are a great time to set intentions for growth, prosperity and expansion! write down your manifestations, burn your bay leaves, light green and yellow candles”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แนะนำพิธีกรรมช่วงดวงจันทร์ใหม่ในราศีเมถุน เช่น เขียนความปรารถนา เผาใบกระวาน และจุดเทียนเพื่อดึงดูดความมั่งคั่ง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/labrujxnegra/status/2066268236526837791" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@energyhealingjw</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1253 · 💬 40</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/energyhealingjw/status/2066274614485901405">View @energyhealingjw on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This Super New Moon arrives in 5 hours in electric Gemini. If this message finds you on June 14 or 15 you’re receiving Divine alignment falling into place. The right love &amp;amp; relationship arriving s”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บัญชี X โพสต์เนื้อหาโหราศาสตร์เรื่อง Super New Moon ใน Gemini วันที่ 14–15 มิ.ย. ชวนให้ interact และ follow เพื่อ 'รับ' alignment และความสำเร็จในอาชีพ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/energyhealingjw/status/2066274614485901405" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
