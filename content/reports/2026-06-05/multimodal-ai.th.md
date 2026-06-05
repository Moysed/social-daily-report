---
type: social-topic-report
date: '2026-06-05'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-05T03:40:32+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 176
salience: 0.7
sentiment: mixed
confidence: 0.58
tags:
- multimodal-ai
- image-generation
- video-generation
- open-weights
- comfyui
- asset-pipeline
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2062331873305759744/img/xIyH77VNCyxnAPUR.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-05

## TL;DR
- Ideogram 4.0 เปิดตัวเป็น open-weight text-to-image model ขนาด 9.3B พร้อม native ComfyUI support; ดาวน์โหลด weights และ fine-tune ได้ ฝึกบน structured JSON caption datasets [5][6][46][59]
- Grok Imagine Video 1.5 ให้บริการผ่าน Vercel AI Gateway เป็น hosted API สำหรับ image-to-video พร้อม synced audio ในรอบเดียว [1][28]
- โมเดลใหม่อีกหลายตัวออกมาในช่วงเดียวกัน: Reve 2 (image) [38], NVIDIA Cosmos 3 (embodied/world-model foundation model) [19], Runway Aleph 2.0 (targeted video editing) [21] และ Kling 3.0 Omni [51]
- NVIDIA open-source Flashdreams เป็น Apache-2.0 acceleration library สำหรับ world model [55]
- โพสต์ที่ engagement สูงส่วนใหญ่เป็น tool listicle และ income-claim thread ไม่ใช่ technical signal [12][29][45][49]; สแต็ก multimodal ฟรีชื่อ 'Agnes' [16][24] มีสัญญาณของ scam ('ฟรี, ไม่มีวันหมดอายุ')

## สิ่งที่เกิดขึ้น
โมเดล image/video หลายตัวปรากฏในช่วงนี้ Ideogram 4.0 วางจำหน่ายในรูป open-weight text-to-image foundation model ขนาด 9.3B พร้อม native ComfyUI integration โดยระบุว่ารันและ fine-tune บน hardware ของตัวเองได้ [5][6][46][59] Grok Imagine Video 1.5 เปิดเป็น hosted image-to-video API บน Vercel AI Gateway สร้าง synced audio ได้ใน pass เดียว [1][28] Reve 2 (image) [38], Kling 3.0 Omni 4K [51] และ Runway's Aleph 2.0 targeted-edit tool [21] ก็ปรากฏเช่นกัน รวมถึงโมเดลวิดีโอไม่ทราบชื่อ ('PURPLE') ที่ถูก benchmark บน Artificial Analysis [10] ด้านโครงสร้างพื้นฐาน NVIDIA ปล่อย Cosmos 3 ซึ่งเป็น embodied AI foundation model ที่รวม prediction, domain transfer, reasoning และ action generation เข้าด้วยกัน [19] และ open-source Flashdreams เป็น Apache-2.0 world-model acceleration library [55] pattern ที่ practitioner ใช้ซ้ำๆ คือ pipeline Midjourney v8.1 → GPT Image 2 (character sheet) → Seedance 2.0 (animation) [2][34][42] CEO ของ Runway อ้างว่า ad agency รายหนึ่งสามารถ reproduce แคมเปญมูลค่า $300K–$600K ได้ในราคาประมาณ $3K [15] — ตัวเลขนี้มาจากฝ่ายการตลาดของ vendor เอง ส่วนใหญ่ของรายการตาม engagement เป็น listicle 'top 100 AI tools' [12][23][29][36][45][49][50][60] และ faceless-content income thread [11][17][18][25][48] ซึ่งให้ technical signal น้อยมาก

## ทำไมถึงสำคัญ (เหตุผล)
signal ที่นำไปใช้ได้จริงคือ open weights บวก ComfyUI integration: Ideogram 4.0 รันแบบ local ได้ fine-tune บน art style ของ studio เองได้ และเชื่อมเข้า node graph ที่มีอยู่แล้วได้ [5][6][59] — เหมาะกับการสร้าง asset และ edutech-visual โดยไม่ติด per-image API lock-in หรือส่ง IP ให้ black box การฝึกด้วย structured JSON caption [5] บ่งชี้ว่าควบคุม prompt-to-layout ได้ดีขึ้น มีประโยชน์สำหรับ game/UI mockup ที่ต้องการความสม่ำเสมอ ด้านวิดีโอ ตลาดกำลังกระจัดกระจายระหว่าง hosted API (Grok Imagine via Gateway [1][28], Kling [51], Runway [15][21]) แทนที่จะรวมศูนย์ จึงมีความเสี่ยงจาก churn หากเดิมพันกับ pipeline ใดตัวเดียว; claim เรื่อง single-pass synced audio [1] และ targeted-edit [21] ช่วยลดขั้นตอน post-production หากพิสูจน์ได้ Cosmos 3 และ Flashdreams [19][55] ชี้ไปที่ world model สำหรับ simulation/XR แต่ยังอยู่ในขั้น research ยังไม่ใช่ production tool สำหรับ studio เล็ก ผลรอง: ปริมาณ listicle/grift content [12][29][45] และ 'free' stack ที่น่าจะเป็น scam [16][24] กลายเป็น noise หลักที่เพิ่มต้นทุนในการแยก release จริงออกจากการ farm engagement

## ความเป็นไปได้
**น่าจะเกิด:** Ideogram 4.0 จะได้รับการยอมรับจาก community เร็ว เพราะ ComfyUI support และ open weights พร้อมใช้งานแล้ว [5][46][59] ดังนั้น LoRA/fine-tune สำหรับ style เฉพาะควรตามมาเร็ว **พอเป็นไปได้:** hosted video model จะเปิดตัวต่อเนื่องในอัตราสูง (Grok 1.5, Kling 3.0, Aleph 2.0, รายการ 'PURPLE') [1][10][21][51] หมายความว่าไม่มี video tool ตัวใดกลายเป็นมาตรฐานในไตรมาสนี้ — เลือกตาม quality ปัจจุบัน ไม่ใช่ความภักดี **พอเป็นไปได้:** world-model tooling [19][55] จะพัฒนาเป็น XR/sim asset generation ในระยะยาว แต่ยังไม่เร็วพอที่จะวางแผนรับ **ไม่น่าเกิด:** vendor claim เรื่องลดต้นทุน 99% อย่าง Runway [15] จะใช้ได้จริงกับ workflow ของ studio โดยไม่ต้องทำ manual cleanup มาก — ถือเป็น marketing ไว้ก่อน ไม่มีแหล่งใดให้ตัวเลขความน่าจะเป็น จึงไม่ระบุตัวเลขที่นี่

## ความเกี่ยวข้องกับองค์กร — NDF DEV
1) ทดลอง Ideogram 4.0 ใน ComfyUI สำหรับ concept art, edutech illustration และ UI/texture mockup; ทดสอบ fine-tune บน style set ของตัวเอง (ความพยายาม: กลาง) [5][6][59] 2) Prototype pipeline Midjourney→GPT Image 2→Seedance สำหรับ character reference และ turnaround ของตัวละครเกม (ความพยายาม: ต่ำ-กลาง) [2][34][42] 3) ทำ bake-off เล็กๆ สำหรับ image-to-video ด้าน marketing/edutech โดยเปรียบ Grok Imagine 1.5 (Gateway API), Kling 3.0 และ Runway Aleph 2.0; เลือกตาม output quality และ cost per clip โดยคาดว่าต้องมี manual cleanup (ความพยายาม: กลาง) [1][21][28][51] 4) จดบันทึก Cosmos 3 และ Flashdreams ไว้สำหรับการทดลอง XR/sim ในอนาคต แต่ยังไม่ต้องลง pipeline time (ความพยายาม: ต่ำ, monitor only) [19][55] ข้าม: 'top 100 AI tools' listicle ทุกรายการ [12][29][45][49][60], faceless-content income thread [11][17][18][25][48] และ 'Agnes' free stack [16][24] — ไม่มี provider ที่ตรวจสอบได้และมีสัญญาณ scam

## สัญญาณที่ควรติดตาม
- ติดตาม Ideogram 4.0 community LoRA/fine-tune และเงื่อนไข license สำหรับใช้เชิงพาณิชย์ด้าน game/edutech [5][59]
- ติดตาม ranking ของโมเดลวิดีโอ 'PURPLE' ที่ไม่ทราบชื่อบน Artificial Analysis เพื่อดูว่าเป็นของ vendor ใด [10]
- ติดตามว่า single-pass synced audio ของ Grok Imagine ยืนยันผลในการทดสอบจริงหรือเป็นแค่ API claim [1][28]
- ติดตาม world-model tooling (Cosmos 3, Flashdreams) ว่ามี path สำหรับ XR/sim asset ที่ใช้งานได้จริงหรือยัง [19][55]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | vercel_dev | ^845 c167 | [Grok Imagine Video 1.5 on AI Gateway. Image-to-video generation with synced audi](https://x.com/vercel_dev/status/2062331926296641565) |
| x | aimikoda | ^675 c42 | [Midjourney + GPT Image 2 + Seedance 2.0 - Prompt Share Zero Trace 1. Generate th](https://x.com/aimikoda/status/2062097934468919483) |
| x | lanxre | ^347 c11 | [At least you can see genshin is trying with their camera work but u see that hsr](https://x.com/lanxre/status/2062048715913740536) |
| x | kellyeld | ^340 c18 | ['Just Slide'. Found this fun #Midjourney style ref code. Loving these characters](https://x.com/kellyeld/status/2062168142747734434) |
| x | ComfyUI | ^332 c25 | [Ideogram 4.0 is now natively supported on ComfyUI @ideogram_ai v4.0 is an open-w](https://x.com/ComfyUI/status/2062203744931168436) |
| x | fofrAI | ^302 c10 | [Ideogram v4 is really good, and open weights. Images are crisp and feel fresh. h](https://x.com/fofrAI/status/2062251438990930323) |
| x | michaelrabone | ^277 c5 | [Exploring Style --sref 2045219822 Midjourney 8.1 Autopsy Prompt Autopsy infograp](https://x.com/michaelrabone/status/2062489602749841621) |
| x | Bonita07192263 | ^275 c1 | [@DiscussingFilm Kane Parsons when he sees a Midjourney prompt https://t.co/R9BIo](https://x.com/Bonita07192263/status/2062346867237630406) |
| x | Mapemaofweb3 | ^269 c160 | [🚨 HIRING AI VIDEO CREATORS 🚨 we're currently identifying AI video creators for u](https://x.com/Mapemaofweb3/status/2062233219752493393) |
| x | BrentLynch | ^250 c42 | [👀WHAT SECRET AI VIDEO MODEL IS THIS? IS IT HAILUO 3? IS IT SEEDANCE 2.1? IS IT K](https://x.com/BrentLynch/status/2062570878312010028) |
| x | __dolani | ^205 c34 | [Good morning, Tech Twitter. Here are some skills you can lock in on and make som](https://x.com/__dolani/status/2062079119160910214) |
| x | AuroraMar1eL | ^188 c68 | [Top 50 AI tools worth trying in 2026: 🤖 Chatbots & Research 1. ChatGPT 2. Claude](https://x.com/AuroraMar1eL/status/2062094424105226368) |
| x | icreatelife | ^186 c45 | [I brought 60 people from X into Adobe Firefly Ambassadors program. It wasn't eas](https://x.com/icreatelife/status/2062548985164836912) |
| x | hayalet_kadir | ^183 c3 | ["Prompt by Hayalet - Generated by Stable Diffusion DreamShaper XL" #SciFiArt #Sp](https://x.com/hayalet_kadir/status/2062451736883683802) |
| x | c_valenzuelab | ^168 c21 | [Another wild customer story: a major ad agency was able to replicate a $300K–$60](https://x.com/c_valenzuelab/status/2062503358011674630) |
| x | ElsaSofia__AI | ^159 c53 | [🚨 Found a multimodal AI stack that's completely FREE with no expiration. ✅ Agnes](https://x.com/ElsaSofia__AI/status/2062129366977728618) |
| x | gippp69 | ^158 c38 | [THIS DEVELOPER BOUGHT A $799 MAC MINI AND NOW RUNS 5 FACELESS YOUTUBE CHANNELS F](https://x.com/gippp69/status/2062593165337489717) |
| x | 0xTria | ^157 c12 | [A 42-YEAR-OLD WOMAN MADE $135,000 ON ETSY WITH 6 AI PROMPTS No inventory. No pri](https://x.com/0xTria/status/2062122461374636374) |
| x | cybernetic_lab | ^157 c11 | [NVIDIA released Cosmos 3. It merges four previously isolated systems for predict](https://x.com/cybernetic_lab/status/2062109622862008734) |
| x | Tanaypawar27 | ^154 c34 | [Best accounts to follow from each frontier lab to stay constantly up to date Ant](https://x.com/Tanaypawar27/status/2062174278012064162) |
| x | runwayml | ^154 c9 | [The edits you need, made easy. Aleph 2.0 changes just what you want edited, leav](https://x.com/runwayml/status/2062540015473721682) |
| x | chrisdadiva | ^153 c3 | [How To Create AI Podcasts video That Looks Real in 2026. In this video, you'll l](https://x.com/chrisdadiva/status/2062414047023415665) |
| x | Onil_coder | ^151 c51 | [Professionals won't tell you this 👀 They use these daily. 🪄⚡ 1. Ideas 🧠 - YOU - ](https://x.com/Onil_coder/status/2062177239601729662) |
| x | tussiwe | ^145 c18 | [I just came across Agnes, a surprisingly capable full-modal AI model from a top-](https://x.com/tussiwe/status/2062524171742330994) |
| x | Lummox_eth | ^141 c29 | [Just a girl + Claude + Sora 2 and already 37 videos for kids with 2.1M views for](https://x.com/Lummox_eth/status/2062479498063323166) |
| x | vibeman_0 | ^133 c73 | [if your a content creator, a writer or a designer this is for you which ai serve](https://x.com/vibeman_0/status/2062219184176599085) |
| x | betraidx | ^129 c14 | [She makes $24,000 a month from a podcast. She doesn't host one. Pause at 0:36 — ](https://x.com/betraidx/status/2062280720672763967) |
| x | rauchg | ^129 c12 | [Grok Imagine Video on @vercel AI Gateway – the top image-to-video model on https](https://x.com/rauchg/status/2062332963636060313) |
| x | Bhanusinghyede | ^128 c24 | [🚀 𝟏𝟐𝟎 𝐌𝐢𝐧𝐝-𝐁𝐥𝐨𝐰𝐢𝐧𝐠 𝐀𝐈 𝐓𝐨𝐨𝐥𝐬 𝐘𝐨𝐮 𝐒𝐡𝐨𝐮𝐥𝐝 𝐊𝐧𝐨𝐰 𝐢𝐧 𝟐𝟎𝟐𝟔 Most people know 5–10 tools…](https://x.com/Bhanusinghyede/status/2062135616033452386) |
| x | MilkRoadAI | ^128 c13 | [Meta is extremely UNDERVALUED and Jensen Huang just explained exactly why the ma](https://x.com/MilkRoadAI/status/2062022483948310985) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vercel_dev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 845 · 💬 167</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vercel_dev/status/2062331926296641565">View @vercel_dev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Grok Imagine Video 1.5 on AI Gateway. Image-to-video generation with synced audio in one pass. 𝚊𝚠𝚊𝚒𝚝 𝚐𝚎𝚗𝚎𝚛𝚊𝚝𝚎𝚅𝚒𝚍𝚎𝚘({ 𝚖𝚘𝚍𝚎𝚕: '𝚡𝚊𝚒/𝚐𝚛𝚘𝚔-𝚒𝚖𝚊𝚐𝚒𝚗𝚎-𝚟𝚒𝚍𝚎𝚘-𝟷.𝟻-𝚙𝚛𝚎𝚟𝚒𝚎𝚠', 𝚙𝚛𝚘𝚖𝚙𝚝: '𝚊 𝚛𝚊𝚋𝚋𝚒𝚝 𝚜𝚙𝚛𝚒𝚗𝚝𝚒𝚗𝚐 𝚝𝚑𝚛𝚘𝚞𝚐𝚑 𝚗𝚢”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Vercel AI Gateway รองรับ xAI Grok Imagine Video 1.5 แล้ว — สร้างวิดีโอจากภาพพร้อม audio sync ได้ในการ call เดียวผ่าน generateVideo()</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>API call เดียวจบทั้ง video + audio sync ลด pipeline ที่ปกติต้องต่อหลาย step — ตรงกับงาน e-learning หรือ XR content ที่ต้องการ animated asset</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง Grok Imagine Video 1.5 ผ่าน Vercel AI Gateway สำหรับงานที่ต้องการ clip สั้นพร้อม audio เช่น intro e-learning หรือ preview XR scene</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vercel_dev/status/2062331926296641565" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aimikoda</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 675 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aimikoda/status/2062097934468919483">View @aimikoda on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Midjourney + GPT Image 2 + Seedance 2.0 - Prompt Share Zero Trace 1. Generate the character. - Midjourney v8.1: hacker girl --ar 2:3 --profile w9b13s1 --stylize 1000 2. Create a character sheet. 3. Cr”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>workflow 4 ขั้น — Midjourney v8.1 → GPT Image 2 → Seedance 2.0 — สร้าง character ตั้งแต่ text prompt ไปถึง storyboard และ video สุดท้าย พร้อมแชร์ prompts ครบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค character sheet เป็น reference บังคับให้ visual ตรงกันข้าม tool — แก้ปัญหา consistency ในงาน game, XR, หรือ e-learning ได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้ pipeline นี้ prototype character ของ game หรือ e-learning ก่อนเข้า production จริง — ลดรอบแก้งาน art ได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aimikoda/status/2062097934468919483" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@lanxre</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 347 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/lanxre/status/2062048715913740536">View @lanxre on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“At least you can see genshin is trying with their camera work but u see that hsr?? Dogshit ive seen sora Ai do better than the devs”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้บ่นว่า camera work ใน Honkai Star Rail แย่ และอ้างว่า Sora AI ทำได้ดีกว่า dev ของเกม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/lanxre/status/2062048715913740536" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kellyeld</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 340 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kellyeld/status/2062168142747734434">View @kellyeld on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“‘Just Slide’. Found this fun #Midjourney style ref code. Loving these characters. Lyrics by me and Marshall Altman. Animation: #VEO3. Song made with #Suno #ai #aiart #music #surreal https://t.co/xfpom”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator @kellyeld แชร์ music video animation สั้นชื่อ 'Just Slide' สร้างด้วย AI ล้วน — Midjourney style ref, VEO3 animation, Suno สำหรับเพลง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kellyeld/status/2062168142747734434" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ComfyUI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 332 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ComfyUI/status/2062203744931168436">View @ComfyUI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ideogram 4.0 is now natively supported on ComfyUI @ideogram_ai v4.0 is an open-weight 9.3B text-to-image foundation model. It is exclusively trained on structured JSON caption datasets for precise sce”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Ideogram 4.0 โมเดล text-to-image open-weight ขนาด 9.3B เทรนด้วย JSON caption ถูก integrate เข้า ComfyUI แล้ว รองรับทั้ง open-source node และ API node</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Inference ได้ local พร้อม text rendering แม่นยำและ bounding box control ตอบโจทย์งาน e-learning graphic และ in-game UI asset โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดึง ComfyUI Ideogram 4.0 node มาทดลองใน pipeline งาน e-learning หรือ XR สำหรับ asset ที่ต้องมี text ในภาพ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ComfyUI/status/2062203744931168436" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@fofrAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 302 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/fofrAI/status/2062251438990930323">View @fofrAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ideogram v4 is really good, and open weights. Images are crisp and feel fresh. https://t.co/8S1P4Rz9FB”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Ideogram v4 โมเดล text-to-image ถูกปล่อยเป็น open weights ให้ภาพคมชัดและมีสไตล์เฉพาะตัว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Open weights ทำให้ self-host หรือรันในเครื่องได้ สร้าง asset โดยไม่มีค่า API และควบคุม data เองได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Ideogram v4 แบบ self-hosted สำหรับสร้าง concept art ใน game, ภาพ e-learning, หรือ UI mockup</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/fofrAI/status/2062251438990930323" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@michaelrabone</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 277 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/michaelrabone/status/2062489602749841621">View @michaelrabone on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Exploring Style --sref 2045219822 Midjourney 8.1 Autopsy Prompt Autopsy infographic of geometric low-polygon TIE Fighter hybrid, parts and labels, industrial mechanical design --ar 3:2 --raw --sref 20”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney 8.1 ออกแล้ว มี flag ใหม่ (--hd, --raw) และระบบ --sref ที่ใช้ตัวเลขล็อก visual style ให้สม่ำเสมอข้ามหลาย prompt</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>workflow --sref ช่วยทีมเล็กล็อก art style ครั้งเดียวแล้วนำกลับมาใช้ใหม่กับ concept art, e-learning, หรือ game asset ได้โดยไม่ต้อง prompt ใหม่ทั้งหมด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">จัด session ทดสอบ Midjourney 8.1 เพื่อสร้าง --sref seed library เล็กๆ ที่ตรงกับ art direction ของงานปัจจุบันของ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/michaelrabone/status/2062489602749841621" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Bonita07192263</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 275 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Bonita07192263/status/2062346867237630406">View @Bonita07192263 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@DiscussingFilm Kane Parsons when he sees a Midjourney prompt https://t.co/R9BIoOSmRs”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ตลกบน X ว่านักแสดง Kane Parsons ตื่นเต้นเมื่อเห็น Midjourney prompt พร้อมรูปภาพประกอบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Bonita07192263/status/2062346867237630406" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
