---
type: social-topic-report
date: '2026-06-04'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-04T03:50:02+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 157
salience: 0.7
sentiment: mixed
confidence: 0.55
tags:
- multimodal-ai
- open-weights
- video-generation
- comfyui
- quantization
- copyright
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2062096072931971072/img/lg77Z-7uaTvV7SNC.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-04

## TL;DR
- Ideogram 4.0 เปิดตัวเป็น open-weight text-to-image model ขนาด 9.3B พารามิเตอร์ ฝึกด้วย structured JSON captions และรองรับใน ComfyUI แล้ว [12][29]
- Runway Aleph 2.0 API ตัดต่อวิดีโอ multi-shot ความยาวถึง 30 วินาทีที่ 1080p และสร้าง green-screen/clean plates โดยไม่ต้อง rotoscoping [13][41]; พร้อมกันนั้นยังฝังอยู่ใน Adobe Firefly [24]
- Intel AutoRound 4-bit (W4A16) quantization ถูกรวมเข้า vLLM-Omni สำหรับ Omni multimodal + diffusion image/video ลด Qwen3-Omni-30B จาก 66GB [43] — ช่วยประหยัดค่า local serving
- NVIDIA Cosmos 3 รวม prediction, domain transfer, reasoning และ action ไว้ใน embodied world model ตัวเดียว [33]; ทีม Morpheus video-world-model ย้ายไปร่วมงาน Roblox [3]
- ข้อพิพาทลิขสิทธิ์: มีโพสต์ระบุว่า Martin Scorsese กำลังให้คำปรึกษาบริษัท AI ที่ก่อตั้งโดยกลุ่มคนที่ฝึก Stable Diffusion บนภาพที่มีลิขสิทธิ์ ซึ่งเชื่อมโยงกับ Black Forest Labs [8][1][2]

## What happened
มีหลาย release ที่นำไปใช้งานจริงได้ Ideogram 4.0 คือ open-weight text-to-image model ขนาด 9.3B พารามิเตอร์ ฝึกด้วยข้อมูล structured JSON caption และรองรับใน ComfyUI [12] ผู้ใช้อิสระระบุว่าภาพผลลัพธ์คมชัด และชื่นชมที่มี open weights [29] Runway ปล่อย Aleph 2.0 ผ่าน API สำหรับตัดต่อวิดีโอ multi-shot ความยาวถึง 30 วินาทีที่ 1080p [13] พร้อม workflow ที่แปลงคลิปใดก็ได้ให้เป็น green-screen asset หรือ clean plate โดยไม่ต้อง rotoscoping [41]; model ประเภทเดียวกันนี้กำลังถูกฝังใน Adobe Firefly [24] ด้านการ serving Intel AutoRound post-training quantization ถูกรวมเข้า vLLM-Omni นำ 4-bit (W4A16) มาใช้กับ Omni multimodal และ diffusion image/video โดยลดขนาด Qwen3-Omni-30B จาก 66GB [43] รายการอื่น ๆ: Grok Imagine Video 1.5 ทำ image-to-video พร้อม synced audio ในขั้นตอนเดียวบน Vercel AI Gateway [6]; Seedance 2.0 มี ComfyUI storyboard-to-animation workflow [18]; Nexus BTA เป็น local ComfyUI studio สำหรับ image/video/3D ที่รองรับ SD 1.5, SDXL, Flux, Qwen, Z-Image Turbo, Lumina และ WAN [30]; NVIDIA ปล่อย Cosmos 3 [33]; และทีม Morpheus ที่อยู่เบื้องหลัง video world-model architectures ย้ายไป Roblox [3] ส่วนใหญ่ของ feed เป็นสัญญาณรบกวน: ลิสต์ "Top AI tools" ซ้ำซาก [23][35][36][37][38][47][49][50][53][57], โพสต์อ้างรายได้ [26][28][59] และ engagement bait [20][34][60]

## Why it matters (reasoning)
แนวโน้มที่ NDF DEV ใช้ประโยชน์ได้จริงคือการรวมศูนย์ไปที่ open weights และ local inference ที่ถูกลง Ideogram 4.0 open weights พร้อม ComfyUI [12][29] และ Nexus BTA local multi-model studio [30] ทำให้ทดลองงาน image และ 3D เบื้องต้นได้ใน-house โดยไม่เสียค่า API ต่อครั้ง และไม่ต้องส่ง client IP ไปยังบริการปิด AutoRound 4-bit ใน vLLM-Omni [43] ลดข้อกำหนด GPU สำหรับการ self-host multimodal และ diffusion models ซึ่งสำคัญสำหรับสตูดิโอที่ไม่มีงบ datacenter clean plates และ green-screen extraction แบบไม่ต้อง rotoscoping ของ Aleph 2.0 [41][13] ตอบโจทย์ต้นทุน VFX ที่เป็นรูปธรรมสำหรับ trailer และวิดีโอ edutech ในมิติรอง: ข้อพิพาท Scorsese/Black Forest Labs [8][1][2] บ่งชี้ความเสี่ยงด้านที่มาของข้อมูลอย่างแท้จริง — model ที่ข้อมูลฝึกไม่ชัดเจนคือภาระรับผิดสำหรับ assets ที่ใช้กับลูกค้าหรือเชิงพาณิชย์ใน game/edutech ดังนั้นการเลือก open-weight คือการจัดการความเสี่ยงทางกฎหมายไปพร้อมกัน ไม่ใช่แค่เรื่องต้นทุน Cosmos 3 world model [33] และการย้ายทีม Morpheus ไป Roblox [3] ชี้ว่า video/world models กำลังเคลื่อนเข้าสู่ interactive game platform ซึ่งเกี่ยวข้องกับ roadmap ด้าน Unity และ XR แต่ยังไม่ใช่ tooling ที่พร้อมใช้

## Possibility
มีแนวโน้มสูง: open-weight image models (Ideogram 4.0 [12][29], stack ใน Nexus BTA [30]) รวมกับ 4-bit local serving [43] จะทำให้การสร้าง asset แบบ self-hosted ใช้ได้จริงสำหรับสตูดิโอขนาดเล็กต่อเนื่อง เนื่องจากทั้งหมดปล่อยออกมาและรันได้แล้ว เป็นไปได้: การตัดต่อวิดีโอแบบ Aleph จะกลายเป็นขั้นตอนมาตรฐาน pre/post สำหรับวิดีโอ marketing และ edutech เมื่อขยายจาก Runway API เข้าสู่ Adobe Firefly [24][13] เป็นไปได้: world models (Cosmos 3 [33], Morpheus ที่ Roblox [3]) จะเข้าถึง game/XR engine แบบ interactive แต่ยังไม่ชัดเรื่อง timeline และปัจจุบันอยู่ในขั้น research/acquisition ไม่ใช่ Unity-ready SDK ไม่น่าจะชัดในเร็ว ๆ นี้: คำถามด้านลิขสิทธิ์/ที่มาข้อมูลจาก [8][1][2] — ยังเป็นข้อกล่าวหาและข้อพิพาทที่ยังดำเนินอยู่ ไม่ใช่ผลที่ตัดสินแล้ว ควรมองเป็นความเสี่ยงถาวรไม่ใช่สิ่งที่จะชัดเจนในระยะสั้น

## Org applicability — NDF DEV
1) ทดลอง Ideogram 4.0 ใน ComfyUI สำหรับ concept art และวิสต้า edutech — open weights ลดความเสี่ยงด้านที่มาและต้นทุนสำหรับงานลูกค้า (effort: low) [12][29]. 2) ทดสอบ Nexus BTA เป็น local front-end เดียวสำหรับทดลอง image/video/3D ข้ามโมเดล SDXL/Flux/Qwen/WAN (effort: low) [30]. 3) ทดลอง Aleph 2.0 สำหรับ clean plates/green-screen แบบไม่ต้อง rotoscoping บน trailer และ explainer footage ก่อนตัดสินใจทำ VFX แบบ manual (effort: med) [13][41]. 4) ประเมิน AutoRound 4-bit + vLLM-Omni เพื่อ self-host multimodal/diffusion model บน GPU ที่มีอยู่ โดยเทียบกับการลดขนาด Qwen3-Omni-30B [43] (effort: med/high). 5) ใช้ Seedance 2.0 ComfyUI storyboard workflow สำหรับ game-cinematic และ lesson pre-viz (effort: med) [18]. ข้าม: ลิสต์ "Top AI tools" [23][35][36][37][47][49][53][57], โพสต์อ้างรายได้/grift [26][28][59], Agnes stack "free no-expiration" [25] (ไม่ยืนยัน น่าจะเป็น bait) และโพสต์ NFT/engagement [52][20][60]. ติดตามแต่ยังไม่ดำเนินการ Cosmos 3 [33] และ Morpheus/Roblox [3] จนกว่าจะมี tooling ฝั่ง Unity

## Signals to Watch
- Ideogram 4.0 open weights จะมี commercial/training-data license ที่ชัดเจนและใช้ได้กับ edutech และ games สำหรับลูกค้าหรือไม่ [12][29]
- การขยาย Aleph 2.0 จาก Runway API เข้าสู่ Adobe Firefly และ editor อื่น ๆ ในฐานะ standard video-edit layer [13][24]
- คุณภาพและ throughput ของ AutoRound 4-bit quantization ใน vLLM-Omni สำหรับ diffusion video บน consumer GPU [43]
- ผลลัพธ์ของข้อพิพาทลิขสิทธิ์ Scorsese / Black Forest Labs เพื่อใช้เป็นแนวทางประเมินความเสี่ยงทางกฎหมายของ model [8][1][2]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | CCinephilia | ^2241 c19 | [Marty didn't just disappoint us; he betrayed the entire film community. Only a f](https://x.com/CCinephilia/status/2061930091903332735) |
| x | bippburger | ^1475 c9 | [See but I saw this movie and know it's not true. The lead VFX firm credited is "](https://x.com/bippburger/status/2061897983923572969) |
| x | xxunhuang | ^536 c84 | [I'm excited to announce that the Morpheus AI team is joining Roblox! Over the pa](https://x.com/xxunhuang/status/2061939239915528653) |
| x | Suhail | ^429 c25 | [It is astounding how much and how fast you can learn anything with LLMs. On one ](https://x.com/Suhail/status/2061846994356953130) |
| x | aimikoda | ^417 c34 | [Midjourney + GPT Image 2 + Seedance 2.0 - Prompt Share Zero Trace 1. Generate th](https://x.com/aimikoda/status/2062097934468919483) |
| x | vercel_dev | ^389 c95 | [Grok Imagine Video 1.5 on AI Gateway. Image-to-video generation with synced audi](https://x.com/vercel_dev/status/2062331926296641565) |
| x | lanxre | ^343 c11 | [At least you can see genshin is trying with their camera work but u see that hsr](https://x.com/lanxre/status/2062048715913740536) |
| x | ednewtonrex | ^341 c11 | [Martin Scorsese is advising an AI company founded by the people who trained Stab](https://x.com/ednewtonrex/status/2061824631028265368) |
| x | jimmytheanti | ^308 c2 | [@garegibb "AI" is part of normal production workflows. Many tools in programs li](https://x.com/jimmytheanti/status/2061947515906204064) |
| x | kellyeld | ^301 c14 | ['Just Slide'. Found this fun #Midjourney style ref code. Loving these characters](https://x.com/kellyeld/status/2062168142747734434) |
| x | icreatelife | ^244 c40 | [I can't stop laughing at this meme prompt 😆 Would love to see your experiments w](https://x.com/icreatelife/status/2062156977426374872) |
| x | ComfyUI | ^226 c17 | [Ideogram 4.0 is now natively supported on ComfyUI @ideogram_ai v4.0 is an open-w](https://x.com/ComfyUI/status/2062203744931168436) |
| x | runwayml | ^222 c17 | [Aleph 2.0 is now available via the Runway API. Bring precise video editing direc](https://x.com/runwayml/status/2061895998545244342) |
| x | Suhail | ^200 c28 | [1/ it all started w 2 8xB200s excited to be back in the game again](https://x.com/Suhail/status/2062015784281653591) |
| x | fofrAI | ^199 c4 | [I need to see a video of two of these playing each other in real life.](https://x.com/fofrAI/status/2062126493501723065) |
| x | Mapemaofweb3 | ^197 c142 | [🚨 HIRING AI VIDEO CREATORS 🚨 we're currently identifying AI video creators for u](https://x.com/Mapemaofweb3/status/2062233219752493393) |
| x | gh_marjan | ^194 c4 | [🚀 Hiring: Research Scientists at FAIR, Meta 🚀 We're looking for strong candidate](https://x.com/gh_marjan/status/2061842923923333222) |
| x | ComfyUI | ^191 c4 | [Generate a complete storyboard from a single prompt, then animate it in Seedance](https://x.com/ComfyUI/status/2061825461504872469) |
| x | Bonita07192263 | ^177 c0 | [@DiscussingFilm Kane Parsons when he sees a Midjourney prompt https://t.co/R9BIo](https://x.com/Bonita07192263/status/2062346867237630406) |
| x | icreatelife | ^177 c83 | [Drop your art and connect with everyone who dropped theirs https://t.co/W9pPcScZ](https://x.com/icreatelife/status/2061930852393574474) |
| x | __dolani | ^164 c27 | [Good morning, Tech Twitter. Here are some skills you can lock in on and make som](https://x.com/__dolani/status/2062079119160910214) |
| x | mehwishkiran07 | ^157 c39 | [AI can now help you build YouTube videos with MrBeast-level production... for fr](https://x.com/mehwishkiran07/status/2061765061841154161) |
| x | AuroraMar1eL | ^156 c57 | [Top 50 AI tools worth trying in 2026: 🤖 Chatbots & Research 1. ChatGPT 2. Claude](https://x.com/AuroraMar1eL/status/2062094424105226368) |
| x | icreatelife | ^155 c26 | [I played with Aleph 2 in Adobe Firefly. Thoughts: Everyone is adding AI models. ](https://x.com/icreatelife/status/2061883034719129710) |
| x | ElsaSofia__AI | ^153 c52 | [🚨 Found a multimodal AI stack that's completely FREE with no expiration. ✅ Agnes](https://x.com/ElsaSofia__AI/status/2062129366977728618) |
| x | 0xTria | ^150 c12 | [A 42-YEAR-OLD WOMAN MADE $135,000 ON ETSY WITH 6 AI PROMPTS No inventory. No pri](https://x.com/0xTria/status/2062122461374636374) |
| x | azed_ai | ^149 c16 | [Good morning, take today one small step at a time Newly created style on Midjour](https://x.com/azed_ai/status/2061673188405514614) |
| x | Nekt_0 | ^145 c28 | [A KID CAN TURN ONE TIKTOK LINK INTO A JUSTIN BIEBER CLIP IN 4 STEPS. THAT SAME P](https://x.com/Nekt_0/status/2061802227530940857) |
| x | fofrAI | ^139 c4 | [Ideogram v4 is really good, and open weights. Images are crisp and feel fresh. h](https://x.com/fofrAI/status/2062251438990930323) |
| x | SD_Tutorial | ^131 c4 | [Nexus BTA🤩 for ComfyUI -a local AI image, video, workflow and 3D experiment stud](https://x.com/SD_Tutorial/status/2061730549866323976) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CCinephilia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2241 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CCinephilia/status/2061930091903332735">View @CCinephilia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Marty didn't just disappoint us; he betrayed the entire film community. Only a few hours passed, and it was already revealed that he was advising an AI company founded by the people who trained Stable”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Martin Scorsese ถูกรายงานว่าให้คำปรึกษา AI company ที่ก่อตั้งโดยทีมที่เทรน Stable Diffusion บนภาพที่มีลิขสิทธิ์โดยไม่ได้รับอนุญาต</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CCinephilia/status/2061930091903332735" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bippburger</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1475 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bippburger/status/2061897983923572969">View @bippburger on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“See but I saw this movie and know it’s not true. The lead VFX firm credited is “ACME AI,” there’s some shots in this that straight up look like Sora. I keep thinking about it”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ชมสงสัยว่าหนังที่เครดิต VFX ให้ 'ACME AI' ใช้ shot จาก Sora โดยอ้างจากลักษณะภาพ — ไม่มีการยืนยันจากสตูดิโอ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bippburger/status/2061897983923572969" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@xxunhuang</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 536 · 💬 84</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/xxunhuang/status/2061939239915528653">View @xxunhuang on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm excited to announce that the Morpheus AI team is joining Roblox! Over the past two years, I’ve focused on developing the foundational architectures behind modern video world models, including Self”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Morpheus AI ทีมที่สร้าง architecture สำหรับ real-time video world model (Self Forcing, AR-DiT) เข้าร่วม Roblox เพื่อขับเคลื่อนโปรเจกต์ Roblox Reality</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Generative world model แบบ real-time เริ่มเข้ามาแทน pre-rendered pipeline ใน game engine กระทบโดยตรงต่อวิธีสร้าง environment สำหรับเกมและ XR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม Roblox Reality developer access — ถ้าเปิด API/tooling Unity team เริ่ม prototype AI-driven world generation ได้เลยโดยไม่ต้องสร้าง model layer เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/xxunhuang/status/2061939239915528653" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Suhail</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 429 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Suhail/status/2061846994356953130">View @Suhail on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It is astounding how much and how fast you can learn anything with LLMs. On one hand, you could devalue intelligence / sulk or you can just be some guy in a small room learning the absolute frontier o”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@Suhail มองว่า LLM ทำให้การเรียนรู้ด้วยตัวเองเร็วและกระจายตัวมากขึ้น และเลือกมองเป็นโอกาสแทนที่จะกังวลเรื่อง intelligence ถูก devalue</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Suhail/status/2061846994356953130" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aimikoda</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 417 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aimikoda/status/2062097934468919483">View @aimikoda on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Midjourney + GPT Image 2 + Seedance 2.0 - Prompt Share Zero Trace 1. Generate the character. - Midjourney v8.1: hacker girl --ar 2:3 --profile w9b13s1 --stylize 1000 2. Create a character sheet. 3. Cr”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>pipeline 4 ขั้น (Midjourney v8.1 → GPT Image 2 → Seedance 2.0) รักษา character consistency จาก still image ผ่าน character sheet และ storyboard จนถึง final video</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ได้ character-consistent video โดยไม่ต้องมี 3D rig — ช่วย prototype cutscene, e-learning persona, หรือ XR narrative ได้เร็วขึ้นมาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง run pipeline นี้ prototype scene ที่มีตัวละครสำหรับ e-learning หรือ game pitch ก่อนลงทุนทำ 3D จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aimikoda/status/2062097934468919483" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vercel_dev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 389 · 💬 95</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vercel_dev/status/2062331926296641565">View @vercel_dev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Grok Imagine Video 1.5 on AI Gateway. Image-to-video generation with synced audio in one pass. 𝚊𝚠𝚊𝚒𝚝 𝚐𝚎𝚗𝚎𝚛𝚊𝚝𝚎𝚅𝚒𝚍𝚎𝚘({ 𝚖𝚘𝚍𝚎𝚕: '𝚡𝚊𝚒/𝚐𝚛𝚘𝚔-𝚒𝚖𝚊𝚐𝚒𝚗𝚎-𝚟𝚒𝚍𝚎𝚘-𝟷.𝟻-𝚙𝚛𝚎𝚟𝚒𝚎𝚠', 𝚙𝚛𝚘𝚖𝚙𝚝: '𝚊 𝚛𝚊𝚋𝚋𝚒𝚝 𝚜𝚙𝚛𝚒𝚗𝚝𝚒𝚗𝚐 𝚝𝚑𝚛𝚘𝚞𝚐𝚑 𝚗𝚢”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Vercel AI Gateway รองรับ xAI Grok Imagine Video 1.5 แล้ว — สร้างวิดีโอจากภาพพร้อม audio sync ในการเรียก API เดียวผ่าน AI SDK</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ใช้ Vercel AI Gateway อยู่แล้วได้ video+audio generation เพิ่มทันที ไม่ต้องต่อ vendor ใหม่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Grok Imagine Video 1.5 ผ่าน AI Gateway ที่มีอยู่ สำหรับโปรเจกต์ที่ต้องสร้าง video asset อัตโนมัติ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vercel_dev/status/2062331926296641565" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@lanxre</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 343 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/lanxre/status/2062048715913740536">View @lanxre on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“At least you can see genshin is trying with their camera work but u see that hsr?? Dogshit ive seen sora Ai do better than the devs”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้วิจารณ์ cinematography ใน Honkai Star Rail เทียบกับ Genshin Impact โดยอ้าง Sora AI แค่เป็น rhetorical jab ไม่ใช่ข้อสังเกตเชิงเทคนิค</dd>
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
    <span class="ndf-author">@ednewtonrex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 341 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ednewtonrex/status/2061824631028265368">View @ednewtonrex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Martin Scorsese is advising an AI company founded by the people who trained Stable Diffusion on copyrighted images. I've seen nothing to suggest they take a different approach at Black Forest Labs. Ge”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Martin Scorsese เป็นที่ปรึกษาให้ Black Forest Labs (บริษัทก่อตั้งโดยทีม Stable Diffusion เดิม) ซึ่งยังไม่มีสัญญาณว่าเปลี่ยนแนวทางเรื่อง copyright training data</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ความเสี่ยงด้านกฎหมายและจริยธรรมของ image-generation models ยังไม่มีข้อยุติ — studio ที่ใช้ tools เหล่านี้แบกรับความเสี่ยงทางอ้อม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อนนำ image-gen tool ไปใช้งานจริง ตรวจ training data policy ของ vendor ก่อนตัดสินใจ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ednewtonrex/status/2061824631028265368" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
