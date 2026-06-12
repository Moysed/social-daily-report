---
type: social-topic-report
date: '2026-06-12'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-12T03:43:14+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 154
salience: 0.62
sentiment: mixed
confidence: 0.55
tags:
- video-generation
- comfyui
- open-weights
- production-pipeline
- image-generation
- asset-consistency
thumbnail: https://pbs.twimg.com/media/HKcCFSIbUAARH9Z.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-12

## TL;DR
- สัญญาณที่แข็งแกร่งที่สุดคือ tooling สำหรับ production pipeline ไม่ใช่ flagship model ใหม่: workflow ใน ComfyUI สร้าง roto/matte utility pass จาก footage ได้แล้ว [4] แปลง Playblast ดิบให้เป็น finished shot ผ่าน Seedance 2.0 [52] และ emit bounding-box JSON อัตโนมัติ [57]
- open-weights และ video editing model ราคาถูกก้าวหน้าขึ้น: LTX 2.3 'Omni-Reference' อ้างอิงภาพได้สูงสุด 5 ภาพเพื่อ multi-subject consistency [54] และ Bernini (Wan 2.2) ของ ByteDance ทำ character swap และ background replacement แบบเฉพาะจุดได้ [53]
- Midjourney ตั้ง V8.1 เป็น default, จะ deprecate V8 ในสองสัปดาห์, และกำลังทดสอบ V8.2 [13]; ข้อมูลจากผู้ใช้ของตัวเองแสดง 20M registered เทียบ ~1M ที่จ่ายเงิน [22]
- ต้นทุน ไม่ใช่แค่คุณภาพ กำลังกลายเป็น axis การแข่งขันของ AI video โดยมี Seedance 2.0 ของ CapCut เป็นตัวจุดชนวน [47] และ UGC seller อ้างราคา $1/clip ที่ volume สูง [30][37]
- Runway ขยายความร่วมมือกับ Lionsgate ด้วยโปรแกรมพัฒนา original IP ร่วมกัน [10][31]; ส่วนที่เหลือในฟีดส่วนใหญ่เป็น monetization grift และ tool listicle ที่มี technical signal น้อย [5][8][19][21][32]

## What happened
ฟีดถูกครอบงำด้วย generative video และ image activity บนด้าน tooling มี ComfyUI workflow หลายชุดที่มุ่งเป้า production step จริง: สร้าง utility/matte pass จาก footage โดยไม่ต้องทำ rotoscoping ด้วยมือ [4], pipeline จาก Playblast ไปเป็น finished shot ด้วย Seedance 2.0 [52], การสร้าง bounding-box + JSON ด้วย LLM [57] และการทดลอง audio for video [58] ด้านโมเดล LTX 2.3 เพิ่ม multi-subject reference (ได้ถึง 5 ภาพ) [54], Bernini/Wan 2.2 ของ ByteDance ถูกนิยามว่าเป็น surgical video editor สำหรับ character swap และ background replacement [53] และมีข่าวลือที่ยังยืนยันไม่ได้เกี่ยวกับโมเดลใหม่ในตระกูล Dreamina/Seedance [33] Midjourney ยก V8.1 ขึ้นเป็น default, กำหนด V8 deprecation ในสองสัปดาห์, และแจ้งว่ากำลังทดสอบ V8.2 [13] ขณะที่โพสต์แยกอ้างจำนวนผู้ใช้ registered 20M เทียบ ~1M ที่จ่ายเงิน [22]

## Why it matters (reasoning)
จุดศูนย์ถ่วงกำลังเคลื่อนจาก 'โมเดลไหนดูดีที่สุด' ไปสู่ 'อะไรที่ป้อน pipeline ได้' รายการ ComfyUI ที่ซ้ำกัน [4][52][57][58] แสดงให้เห็นว่า generative step กำลังถูกแทรกเข้าไปใน VFX/asset workflow ที่มีอยู่แล้ว (roto, utility pass, pre-viz จาก Playblast) ไม่ใช่แทนที่ — นั่นคือรูปแบบที่เข้าถึง output ของ studio จริงๆ multi-subject reference [54] และ targeted editing [53] แก้จุดอ่อนเรื้อรังของโมเดลเหล่านี้: ความสม่ำเสมอของ character และ scene ระหว่าง shot ซึ่งสำคัญกว่า hero frame แบบ one-off สำหรับ edutech sequence และ game cinematic การกรอบเรื่องด้วยต้นทุน [47][30][37] บ่งชี้ commoditization ของการสร้าง clip ดิบ ผลักดันให้ความได้เปรียบอยู่ที่การควบคุม ความสม่ำเสมอ และการ integrate ตัวเลข churn ของ Midjourney [22] และการ turnover version รวดเร็ว [13] ตอกย้ำว่า closed subscription tool เผชิญแรงกดดันด้าน retention ซึ่งเสริมกรณีของ open-weight ในที่ที่มีให้ใช้

## Possibility
Likely: ComfyUI ยังคงเป็น integration layer ที่ generative step ถูก bolt เข้ากับ production work โดยมี workflow อิสระสี่รายการในรอบนี้ [4][52][57][58] Plausible: การแข่งขันด้านต้นทุนรุนแรงขึ้นเมื่อ CapCut/Seedance 2.0 เปิดตัว กดราคา per-clip [47] Plausible: open/affordable editing model (LTX 2.3, Wan 2.2) ยังคงปิด consistency gap ที่ขวางการใช้งานแบบ multi-shot [53][54] Unlikely ตามที่นำเสนอ: DiffusionGemma-26B 'flipping' autoregressive text generation [7] — เป็นโพสต์ hype โพสต์เดียวที่ไม่มี benchmark และเป็น text diffusion ไม่ใช่ image/video/3D จึงถือว่าเป็น noise สำหรับหัวข้อนี้ ไม่มีแหล่งข้อมูลใดระบุตัวเลข probability ที่น่าเชื่อถือ; การอ้าง UGC '550 videos/day ที่ $1' เป็น marketing ไม่ใช่ข้อมูลที่ verified [30][37]

## Org applicability — NDF DEV
1) ทดลอง ComfyUI utility-pass และ Playblast workflow สำหรับ pre-viz และ edutech motion visual (effort: med) [4][52] — slot เข้ากับงาน Unity/render ที่มีอยู่แทนที่จะแทนที่ 2) ทดสอบ LTX 2.3 multi-subject reference และ Wan 2.2 editing สำหรับ character-consistent clip ข้าม lesson หรือ marketing series เนื่องจากทั้งคู่เป็น open/affordable แทนที่จะเป็น black-box (effort: med) [53][54] 3) ใช้ Midjourney V8.1 สำหรับ concept art และ moodboard ต่อไปแต่ถือว่าเป็นแบบ disposable เมื่อพิจารณา churn V8→V8.2 และการพึ่งพา subscription (effort: low) [13][35] 4) ติดตามราคา Seedance 2.0/CapCut ก่อนผูกพัน budget กับ hosted video API ใดๆ (effort: low) [47] ข้าม: creator-monetization thread [5][8][19][51], '100+ AI tools' listicle ทั่วไป [21][25][32][42][49], AI-art showcase post [17][20][36][43] และ Kingdom Hearts/Sora upscaling discourse [11][26][55] — ไม่มี signal ที่ใช้ได้สำหรับ NDF DEV

## Signals to Watch
- ComfyUI กลายเป็น de facto glue สำหรับ generative-to-production step — ติดตาม matte/roto [4] และ Seedance 2.0 Playblast [52] workflow เพื่อหา reproducible recipe
- LTX 2.3 และ Wan 2.2 รักษา character/scene consistency ข้าม multiple shot ได้จริงหรือไม่ ซึ่งเป็น gap ที่ขวางการใช้ multi-clip edutech [53][54]
- ราคา CapCut/Seedance 2.0 ในฐานะ cost benchmark สำหรับ hosted video generation [47][33]
- โปรแกรม joint IP ของ Runway–Lionsgate ในฐานะสัญญาณของ studio-grade licensing และ rights expectation ที่กำลังก่อตัวรอบ AI video [10][31]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | heyrimsha | ^804 c13 | [An Australian mathematician from Perth who spent a decade at Meta building the f](https://x.com/heyrimsha/status/2064621247569502602) |
| x | tan_stack | ^638 c28 | [TanStack AI is now in Beta! TanStack AI is no longer just a text-generation libr](https://x.com/tan_stack/status/2065102675390189916) |
| x | ashay_sewlall | ^451 c9 | [Some core memories deserve to be more than a picture 🥹⚽️ The HONOR 600 Pro AI Im](https://x.com/ashay_sewlall/status/2064742373624562074) |
| x | ComfyUI | ^352 c8 | [Mattes and Utilities Demo: VFX artist @heydoughogan breaks down a ComfyUI workfl](https://x.com/ComfyUI/status/2064804378457096621) |
| x | 0xJamino | ^335 c12 | [She uploads cartoons made by AI and pulls in $11,000 a month doing it Most peopl](https://x.com/0xJamino/status/2064775551613596066) |
| x | icreatelife | ^328 c41 | [Fable 5 + Firefly Boards = a fully playable game starring my pet turtle Pablo 🤯 ](https://x.com/icreatelife/status/2064769830473912368) |
| x | analogalok | ^324 c16 | [Auto regressive LLMs are officially on notice. run Gemma 4 26B diffusion gguf wi](https://x.com/analogalok/status/2064865717875618057) |
| x | vladuah | ^323 c13 | [Day 1 of posting AI YouTube videos daily until hitting $6,700 a month The niche ](https://x.com/vladuah/status/2064695648985718785) |
| x | Suhail | ^280 c13 | [Priorities for high agency people are almost always communicated by the latency ](https://x.com/Suhail/status/2065127494014120056) |
| x | runwayml | ^273 c35 | [Today, we're deepening our partnership with Lionsgate with a slate of new initia](https://x.com/runwayml/status/2065072377596088525) |
| x | McSolsy | ^248 c2 | [Me lowkey adding the sora ai watermark to footage of clown dropping in the final](https://x.com/McSolsy/status/2064765277829484665) |
| x | kellyeld | ^244 c20 | ["Art In Motion". This song is about looking inward to protect the raw center of ](https://x.com/kellyeld/status/2064708573603742141) |
| x | midjourney | ^241 c24 | [We've made V8.1 the new default model for all users on Midjourney. V8 will now b](https://x.com/midjourney/status/2064921117618557292) |
| x | heyrimsha | ^231 c5 | [Best open source GitHub repos that replace hundreds of dollars in AI subscriptio](https://x.com/heyrimsha/status/2064694594357579847) |
| x | bull_bnb | ^227 c32 | [AI data was big because models needed the internet. Robot data will be bigger be](https://x.com/bull_bnb/status/2065131071252103412) |
| x | Gravantus | ^217 c2 | [&gt;Fan made &gt;worth billions IP copyright doesn't magically go away with the ](https://x.com/Gravantus/status/2064890176783179825) |
| x | icreatelife | ^204 c287 | [Post your art. No words. Only your art.](https://x.com/icreatelife/status/2065057837307265480) |
| x | Kling_ai | ^197 c38 | [In June 2024, a group of creators began creating with Kling AI. Besides "this is](https://x.com/Kling_ai/status/2064709166904594616) |
| x | xkaidus | ^190 c10 | [Brands pay this guy $2,800 a video for a fitness blonde who never existed and he](https://x.com/xkaidus/status/2064695037875683547) |
| x | gurniaiart | ^188 c0 | [Knight art #AIArt #AIイラスト #midjourney #AIgirl #knight #aiGallery https://t.co/20](https://x.com/gurniaiart/status/2065067622610145360) |
| x | MdRimon488484 | ^156 c52 | [120 Must-Use AI Tools. ✨ 120 Smart AI Tools for Work & Growth.🧠 1. Ideas - YOU -](https://x.com/MdRimon488484/status/2064643995607904513) |
| x | ekinoks_26 | ^154 c161 | [Midjourney has 20 million registered users. Roughly 1 million pay. The other 19 ](https://x.com/ekinoks_26/status/2064950762715951536) |
| x | Tanaypawar27 | ^153 c30 | [Best accounts to follow from each frontier lab to stay constantly up to date Ant](https://x.com/Tanaypawar27/status/2064920550418645252) |
| x | ButchersBrain | ^148 c26 | [In a town where color was outlawed three generations ago, an aging inspector fin](https://x.com/ButchersBrain/status/2064624385076433059) |
| x | Alexie_Ai | ^146 c27 | [120 + Mind blowing AI tools 🔥 1. Ideas - Claude - ChatGPT - Bing Chat - Perplexi](https://x.com/Alexie_Ai/status/2064759650252382593) |
| x | CouchPotato232 | ^144 c8 | [Ok after more research, I believe KH1 Sora and Mickey are drawn by Nomura, while](https://x.com/CouchPotato232/status/2064581853038751980) |
| x | Suhail | ^142 c10 | [I've enjoyed this prompt for learning more than I thought I would: Teach me this](https://x.com/Suhail/status/2065103647848157369) |
| x | treyisforever | ^140 c0 | [@cihywastaken @ctrlkugi ai image generation has been around publicly since 2020 ](https://x.com/treyisforever/status/2065118866943176709) |
| x | HeyGen | ^131 c32 | [Your AI agent can now add HeyGen to its own stack. With @Stripe Projects, it fin](https://x.com/HeyGen/status/2064729845767290940) |
| x | FynCas | ^129 c61 | [MakeUGC & Kling 3.0 = 550 videos/day Fully realistic UGC ads — cinematic lightin](https://x.com/FynCas/status/2065071656100298813) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@heyrimsha</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 804 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/heyrimsha/status/2064621247569502602">View @heyrimsha on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“An Australian mathematician from Perth who spent a decade at Meta building the framework half the AI world runs on, then moved to OpenAI, then co-founded a company with the former CTO of OpenAI, just ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Mark Zuckerberg จ้าง Andrew Tulloch ซึ่งเป็น core contributor ของ PyTorch และ co-founder จากฝั่ง OpenAI ด้วยสัญญารายงาน $1.5B ใน 6 ปี บันทึกเป็น individual hiring package ใหญ่สุดใน tech</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Meta ยอมจ่าย $1.5B สำหรับวิศวกร AI infrastructure คนเดียว สะท้อนว่า PyTorch คือ strategic asset ที่ Meta ไม่ยอมปล่อยให้คู่แข่ง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/heyrimsha/status/2064621247569502602" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@tan_stack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 638 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/tan_stack/status/2065102675390189916">View @tan_stack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“TanStack AI is now in Beta! TanStack AI is no longer just a text-generation library with extras bolted on. TanStack AI has first-class dev experience for: ✅ Text and Streaming Structured Data ✅ Tool C”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>TanStack AI เข้า Beta พร้อม multimodal ครบ — text/streaming, structured data, tool calls, image/video/audio generation, realtime voice, host-side MCP และ orchestration พร้อม per-model type-safety</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ใช้ TanStack Query/Router อยู่แล้วสามารถเพิ่ม AI features — streaming, tool calls, MCP — ใน ecosystem เดิมพร้อม isomorphic devtools โดยไม่ต้องเปลี่ยน stack</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองประเมิน TanStack AI Beta เป็น AI layer ใน web project หน้าที่ต้องการ streaming structured data หรือ MCP tool integration</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/tan_stack/status/2065102675390189916" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ashay_sewlall</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 451 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ashay_sewlall/status/2064742373624562074">View @ashay_sewlall on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Some core memories deserve to be more than a picture 🥹⚽️ The HONOR 600 Pro AI Image to Video 2.0 feature will let me relive my MOTM winning moment ❤️ Which memory would you want to relive? @HONORZA #H”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Influencer โปรโมต feature AI Image to Video 2.0 ของ HONOR 600 Pro ผ่าน sponsored post โดยใช้ภาพความทรงจำส่วนตัวเป็น use case</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ashay_sewlall/status/2064742373624562074" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ComfyUI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 352 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ComfyUI/status/2064804378457096621">View @ComfyUI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mattes and Utilities Demo: VFX artist @heydoughogan breaks down a ComfyUI workflow that generates production-ready utility passes directly from your footage. No manual rotoscoping. No guesswork. What'”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ComfyUI ปล่อย workflow ของ @heydoughogan ที่ auto-generate background removal (RMBG), SAM3 segmentation, face matte และ depth/normals passes จากฟุตเทจที่ native resolution โดยไม่ต้อง rotoscope มือ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Depth, normals และ matte pass ที่ generate อัตโนมัติจากฟุตเทจจริงใช้ใน XR compositing และ relighting ใน Unity ได้เลย ไม่ต้องมีทีม VFX แยก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Studio ทดสอบ workflow นี้กับวิดีโอ e-learning หรือ XR เพื่อ auto-generate matte และ depth pass จากฟุตเทจที่ถ่ายมา ลด post-production มือได้ทันที</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ComfyUI/status/2064804378457096621" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@0xJamino</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 335 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/0xJamino/status/2064775551613596066">View @0xJamino on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“She uploads cartoons made by AI and pulls in $11,000 a month doing it Most people grind a second job. She did the opposite. Found a viral channel like Doggyland and reverse engineered the format. Chat”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้สร้างคอนเทนต์ใช้ ChatGPT เขียน prompt แล้วส่งเข้า Picsart Flow (ขับเคลื่อนด้วย Sora 2) ผลิต cartoon 4K ลง YouTube ทุกวัน รายได้แตะ $11K/เดือนใน 6 เดือน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Sora 2 ผ่าน Picsart Flow ผลิต animated clip 4K จาก text prompt — pipeline ที่อาจลดต้นทุน animation ใน e-learning หรืองาน promo เกมได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Picsart Flow + Sora 2 เทียบกับ workflow animation ปัจจุบันของ studio ดูความเร็วและคุณภาพ output</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/0xJamino/status/2064775551613596066" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@icreatelife</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 328 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/icreatelife/status/2064769830473912368">View @icreatelife on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fable 5 + Firefly Boards = a fully playable game starring my pet turtle Pablo 🤯 Took me less than an hour Every asset made with Firefly Tutorial and my workflow 👇 https://t.co/vSiGlmau4g”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator ใช้ Fable 5 + Adobe Firefly Boards สร้างเกมที่เล่นได้จริง โดย asset ทุกชิ้น generate จาก AI ใช้เวลาไม่ถึง 1 ชั่วโมง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Fable 5 + Firefly ลด concept-to-playable-prototype เหลือไม่ถึงชั่วโมง — ตรงกับงาน game jam หรือทำ demo pitch ให้ client</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมเกมลอง pipeline Fable 5 + Firefly Boards สำหรับ prototype ไว ก่อนเริ่ม Unity production build จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/icreatelife/status/2064769830473912368" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@analogalok</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 324 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/analogalok/status/2064865717875618057">View @analogalok on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Auto regressive LLMs are officially on notice. run Gemma 4 26B diffusion gguf with llama.cpp Google just dropped DiffusionGemma-26B, and it completely flips how we generate text. instead of predicting”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google ปล่อย DiffusionGemma-26B ใช้ diffusion แทน autoregressive — generate 256 tokens พร้อมกัน เป็น MoE ที่ใช้จริงแค่ 3.8B params รัน local บน RTX 3090/4090 ผ่าน llama.cpp GGUF</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>LLM local ที่ self-correct reasoning ระหว่าง generate และรันบน GPU เดี่ยวได้ — ใช้งาน on-device ได้จริงโดยไม่ต้องจ่าย cloud API</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Q4_K_M GGUF บน GPU rig ของ studio ผ่าน llama.cpp diffusion branch เพื่อวัด throughput สำหรับ local AI inference</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/analogalok/status/2064865717875618057" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vladuah</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 323 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vladuah/status/2064695648985718785">View @vladuah on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Day 1 of posting AI YouTube videos daily until hitting $6,700 a month The niche came from a single video - a man begging to get inside to escape a tornado. 15,000,000 views. The format was the product”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>creator ใช้ ChatGPT เขียน prompt → Sora generate วิดีโอ → ViewMax ตัดต่อและใส่ voiceover ได้คลิปพร้อม publish ในไม่กี่นาที โดย copy format ที่เคยมี 15M views มาปรับตัวแปรเดียว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า Sora ใช้งานได้จริงใน pipeline ไม่ใช่แค่ demo — ตรงกับ e-learning explainer หรือ XR scene preview ที่ studio ทำอยู่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ ChatGPT → Sora กับ e-learning explainer 1 คลิป แล้วเทียบเวลาและคุณภาพกับ workflow screen recording ที่ใช้อยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vladuah/status/2064695648985718785" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
