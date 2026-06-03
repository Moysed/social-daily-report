---
type: social-topic-report
date: '2026-06-03'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-03T07:02:53+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 130
salience: 0.8
sentiment: mixed
confidence: 0.6
tags:
- multimodal-ai
- image-to-3d
- video-generation
- open-weights
- comfyui
- world-models
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2061412305766645760/img/AIwo6_dR1c055x0i.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-03

## TL;DR
- NVIDIA Cosmos 3 ซึ่งเป็นกลุ่ม open-weights omnimodal world models สำหรับ Physical AI ขึ้นอันดับ 1 ทั้ง Text-to-Image และ Image-to-Video บน Artificial Analysis leaderboards [8]
- ByteDance ปล่อย Bernini ออกมาเป็น open-source — framework สำหรับ video generation และ editing ที่รองรับ text-prompt edits และอ้างอิง image/video พร้อม code พร้อมใช้ [6]
- TripoAI's TripoSplat (open-source image-to-3D Gaussian model) รองรับ ComfyUI ตั้งแต่วันแรก: ป้อนภาพ 2D เข้าไป ได้ 3D Gaussian asset ออกมา [24]
- Runway ขยาย Aleph 2.0 (compositing mattes, multi-shot edits ยาวถึง 30 วินาที ที่ 1080p) เข้าสู่ API และประกาศเปิด London world-models hub พร้อม UK investment มูลค่า $100M [10][20][15]
- ประเด็นด้านชื่อเสียงและ IP โผล่ขึ้น: Scorsese เป็นที่ปรึกษาให้ Black Forest Labs ซึ่งก่อตั้งโดยทีมที่เคยเทรน Stable Diffusion บนภาพที่มีลิขสิทธิ์ [5][9]

## What happened
มีการปล่อย release จริงหลายชิ้นในฝั่ง image/video/3D generation NVIDIA Cosmos 3 omnimodal world models ขึ้นอันดับ 1 ใน open-weights Text-to-Image และ Image-to-Video [8] และ NVIDIA กำลังจัดตั้ง 'Cosmos Coalition' ร่วมกับ Runway [51] ByteDance เปิด source Bernini เป็น video gen+editing framework พร้อม code [6] TripoAI's TripoSplat นำ open-source image-to-3D Gaussian generation เข้า ComfyUI ตั้งแต่วันแรก [24] พร้อมกับ pipelines อื่นใน ComfyUI (storyboard→Seedance 2.0 animation [32], Qwen Image 2512 [56] และ Nexus BTA local studio ที่รองรับ SD 1.5/SDXL/Flux/Qwen/Z-Image Turbo/Lumina/WAN [35]) Runway ผลัก Aleph 2.0 editing เข้า API [20][10] และเปิด London research hub ที่มุ่งเน้น general world models พร้อมงบ UK $100M [15] Adobe เพิ่มความลึกของ partnership กับ NVIDIA ครอบคลุม Photoshop, Premiere และ Substance 3D [17][38] และทีม Morpheus AI (video world-model architectures) เข้าร่วม Roblox [7]

## Why it matters (reasoning)
Layer ที่ใช้งานได้จริงในระดับ production กำลังเคลื่อนมาหา open weights และ local ComfyUI pipelines ซึ่งตรงกับแนวทางของ studio ที่ให้ความสำคัญกับ open weights และ API ราคาประหยัดมากกว่า closed demos TripoSplat ทำให้ single-image→3D-Gaussian asset generation เข้าถึงได้ภายใน node graph ที่มีอยู่แล้ว [24] และ Cosmos 3 'Physical AI' world models มุ่งเป้าที่ spatial/scene use cases ซึ่งตรงกับงาน XR โดยตรง [8] การที่ world-model bets กระจุกตัว — Cosmos Coalition [51], Runway's London hub [15], Morpheus→Roblox [7] — บ่งชี้ว่าการแข่งขันรอบถัดไปคือ interactive scene/world generation ไม่ใช่แค่ clip output อีกต่อไป แต่ก็มีน้ำหนักถ่วง: คุณภาพยังไม่สม่ำเสมอ (text-to-video transformation ยังมี artifact หนึ่งหรือสองจุดแม้บน model ที่เร็วกว่าอย่าง Seedance 2.0/Google Omni [3]) และ copyright lineage ของ BFL/Stable Diffusion [5][9] ยังเป็นความเสี่ยงทางกฎหมายและชื่อเสียงสำหรับงาน commercial ที่สร้างบน model เหล่านั้น ส่วน volume ส่วนใหญ่ของวันนี้คือ noise — listicles '80+ AI tools' ที่วนซ้ำ [18][40][42][49] และ pitch สร้างรายได้จาก AI influencer [27][29][60] — ซึ่งทำให้ดูเหมือน activity มาก แต่ไม่ได้เพิ่ม production signal จริง

## Possibility
**Likely:** open-source image-to-3D (TripoSplat) บวก ComfyUI integration จะกลายเป็นขั้นตอนมาตรฐานใน indie asset prototyping เพราะได้รับ Day-0 support และรองรับ open model หลากหลาย [24][35] **Plausible:** world models จาก Cosmos/Runway/Morpheus จะเคลื่อนไปสู่ interactive scene generation ที่ใช้ใน game/XR engine ได้ภายใน 12–18 เดือน รองรับด้วย timeline การลงทุนที่ Runway ประกาศไว้ [15][7][8] **Plausible:** ข้อพิพาท copyright เกี่ยวกับ Stable-Diffusion-lineage tools (BFL) จะยกระดับและผลักดัน studio ไปหา weights ที่มี license สะอาดกว่าหรือ self-hosted [9][5] **Unlikely near-term:** text-to-video แบบ hands-off สำหรับงาน client โดยไม่ต้องแต่งด้วยมือ เพราะแม้แต่ model ที่เร็วในปี 2026 ยังมี artifact [3] ไม่มีแหล่งข้อมูลใดระบุตัวเลขความน่าจะเป็น จึงไม่มีการให้ตัวเลขในที่นี้

## Org applicability — NDF DEV
1) ทดสอบ TripoSplat ใน ComfyUI สำหรับ single-image→3D-Gaussian props/characters เป็น prototyping path สำหรับ Unity/XR assets — effort ต่ำ/กลาง [24] 2) ตั้ง local ComfyUI bench สำหรับ image/video/3D (Nexus BTA, Flux/Qwen/SDXL/WAN) เพื่อให้ generation อยู่ใน-house และ license อยู่ในการควบคุม — effort กลาง [35][56][32] 3) ประเมิน NVIDIA Cosmos 3 open weights สำหรับ image/video และ Physical-AI scene generation ที่เกี่ยวข้องกับ XR — effort กลาง [8][51] 4) ติดตาม Bernini สำหรับ prompt-based video editing เพราะ code เป็น public แล้ว — effort ต่ำในการ clone/ประเมิน [6] 5) กำหนด policy: หลีกเลี่ยง Stable-Diffusion-lineage/BFL models สำหรับงาน client ที่รับเงิน จนกว่า licensing จะชัดเจน — effort ต่ำ [9][5] พิจารณา Runway Aleph 2.0 API เฉพาะเมื่อมีงบ hosted เท่านั้น แต่ให้ priority ต่ำกว่า open weights เพราะเป็น closed/hosted [20] ข้ามไปได้เลย: listicles '80+ AI tools' ที่วนซ้ำ [18][40][42][49], AI-influencer monetization threads [27][29][60] และ waifu-art posts [14][46] — ไม่มี production value

## Signals to Watch
- ComfyUI ในฐานะ integration hub สำหรับ open model ใหม่ (TripoSplat 3D, Seedance storyboards, Qwen) — ดู cadence ของ day-0 support [24][32][56]
- World-model consolidation: Cosmos Coalition, Runway London, Morpheus→Roblox — ดู interactive/engine-ready output [51][15][7]
- Copyright exposure ของ Stable-Diffusion-lineage tools (BFL) ในฐานะ sourcing constraint สำหรับงาน commercial [9][5]
- Open-weights leaderboard claims (Cosmos 3 #1) — verify เองก่อน adopt [8]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | TheDivineNigga | ^2030 c19 | [@lowtierrogdaily Cropped the video so we couldn't see that sora ai watermark😂](https://x.com/TheDivineNigga/status/2061615794241343848) |
| x | bippburger | ^1226 c5 | [See but I saw this movie and know it's not true. The lead VFX firm credited is "](https://x.com/bippburger/status/2061897983923572969) |
| x | underwoodxie96 | ^1083 c29 | [I created this video using GPT Image 2.0 and Kling 3.0. I also tested Seedance 2](https://x.com/underwoodxie96/status/2061414477120016873) |
| x | javilopen | ^792 c2 | [@bfl_ai Well, this meme didn't age well 😂😂😂 https://t.co/1X7xPrtg3U](https://x.com/javilopen/status/2061834346969882649) |
| x | CCinephilia | ^702 c10 | [Marty didn't just disappoint us; he betrayed the entire film community. Only a f](https://x.com/CCinephilia/status/2061930091903332735) |
| x | aisearchio | ^677 c13 | [Bytedance drops an open-source Gemini Omni!!! Bernini is a new AI video generati](https://x.com/aisearchio/status/2061572022074020174) |
| x | xxunhuang | ^396 c59 | [I'm excited to announce that the Morpheus AI team is joining Roblox! Over the pa](https://x.com/xxunhuang/status/2061939239915528653) |
| x | ArtificialAnlys | ^323 c19 | [NVIDIA's Cosmos 3 lands at #1 among open weights models in both Text to Image an](https://x.com/ArtificialAnlys/status/2061494719998546206) |
| x | ednewtonrex | ^318 c11 | [Martin Scorsese is advising an AI company founded by the people who trained Stab](https://x.com/ednewtonrex/status/2061824631028265368) |
| x | runwayml | ^284 c17 | [Create compositing mattes in seconds with Aleph 2.0 Mattes let you isolate a sub](https://x.com/runwayml/status/2061548752989753454) |
| x | jimmytheanti | ^255 c2 | [@garegibb "AI" is part of normal production workflows. Many tools in programs li](https://x.com/jimmytheanti/status/2061947515906204064) |
| x | EMostaque | ^222 c14 | [I wonder how many founders will pass on investors who passed on them in prior ro](https://x.com/EMostaque/status/2061824453122642400) |
| x | EMostaque | ^206 c98 | [Let's say half of OpenAI and Anthropic goes to the American people, $1 trillion ](https://x.com/EMostaque/status/2061461391303753992) |
| x | NoNameAIProject | ^203 c1 | [🌸 Asuna / Relaxing in Her Room 🌙 ✅ ALL CHARACTERS ARE 21+ ADULTS "Soft light… so](https://x.com/NoNameAIProject/status/2061584954707075122) |
| x | runwayml | ^199 c21 | [Today we're announcing London as Runway's new European headquarters and our newe](https://x.com/runwayml/status/2061450141614145621) |
| x | Suhail | ^196 c16 | [It is astounding how much and how fast you can learn anything with LLMs. On one ](https://x.com/Suhail/status/2061846994356953130) |
| x | icreatelife | ^196 c42 | [Excited to share with you Adobe where I work full time partners with NVIDIA 🎉 Ad](https://x.com/icreatelife/status/2061497655289926143) |
| x | 1005Alok85200 | ^182 c22 | [80+ AI tools to finish months of work in minutes. 1. Research - ChatGPT - Copilo](https://x.com/1005Alok85200/status/2061663273041432602) |
| x | ideogram_ai | ^179 c78 | [Tomorrow 12 noon ET. Reply with your ideogram username below for early access. h](https://x.com/ideogram_ai/status/2061855321690186089) |
| x | runwayml | ^176 c12 | [Aleph 2.0 is now available via the Runway API. Bring precise video editing direc](https://x.com/runwayml/status/2061895998545244342) |
| x | Kling_ai | ^151 c16 | [What if you could pack a cloud in a bag? ☁️ Here's how we made it with Kling AI.](https://x.com/Kling_ai/status/2061462779647725817) |
| x | mehwishkiran07 | ^147 c38 | [AI can now help you build YouTube videos with MrBeast-level production... for fr](https://x.com/mehwishkiran07/status/2061765061841154161) |
| x | rebeccajolam | ^147 c4 | [Image to video using AI... Why I can't do NSFW? https://t.co/GeZJSiyNp9](https://x.com/rebeccajolam/status/2061476032457380134) |
| x | ComfyUI | ^145 c6 | [TripoSplat, an open-source image-to-3D Gaussian model from @tripoai, has Day-0 s](https://x.com/ComfyUI/status/2061509306743398668) |
| x | azed_ai | ^143 c15 | [Good morning, take today one small step at a time Newly created style on Midjour](https://x.com/azed_ai/status/2061673188405514614) |
| x | gh_marjan | ^141 c4 | [🚀 Hiring: Research Scientists at FAIR, Meta 🚀 We're looking for strong candidate](https://x.com/gh_marjan/status/2061842923923333222) |
| x | betraidx | ^141 c8 | [She makes $14,500 a month. The other her makes nothing. Pause at 0:20 — that's t](https://x.com/betraidx/status/2061565192878624920) |
| x | javilopen | ^139 c74 | [Seriously, where is Apple?](https://x.com/javilopen/status/2061518758380765637) |
| x | Nekt_0 | ^134 c27 | [A KID CAN TURN ONE TIKTOK LINK INTO A JUSTIN BIEBER CLIP IN 4 STEPS. THAT SAME P](https://x.com/Nekt_0/status/2061802227530940857) |
| x | fofrAI | ^131 c32 | [stable diffusion](https://x.com/fofrAI/status/2061723550407340471) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheDivineNigga</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2030 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheDivineNigga/status/2061615794241343848">View @TheDivineNigga on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@lowtierrogdaily Cropped the video so we couldn't see that sora ai watermark😂”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้งานกล่าวหาว่า @lowtierrogdaily ตัด watermark ของ Sora AI ออกจากวิดีโอเพื่อปกปิดว่าเป็น AI-generated content</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheDivineNigga/status/2061615794241343848" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bippburger</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1226 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bippburger/status/2061897983923572969">View @bippburger on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“See but I saw this movie and know it’s not true. The lead VFX firm credited is “ACME AI,” there’s some shots in this that straight up look like Sora. I keep thinking about it”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ชมสงสัยว่า VFX ในหนังเชิงพาณิชย์บางช็อตสร้างด้วย AI video model อย่าง Sora โดยบริษัท VFX ที่เครดิตคือ 'ACME AI' — ไม่มีชื่อหนังหรือหลักฐานยืนยัน</dd>
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
    <span class="ndf-author">@underwoodxie96</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1083 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/underwoodxie96/status/2061414477120016873">View @underwoodxie96 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I created this video using GPT Image 2.0 and Kling 3.0. I also tested Seedance 2.0 and Google Omni. They're much faster for generating transformation videos, but in my tests there were often one or tw”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator ใช้ GPT Image 2.0 + Kling 3.0 แบบ start-frame/end-frame chaining แล้วตัดต่อใน CapCut แทน generate ทั้งคลิปครั้งเดียว ได้ transformation video ที่ดูเป็นธรรมชาติกว่ามาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Technique นี้แก้ปัญหา shot ที่ดู AI ชัดเกิน ตรงกับงาน XR walkthrough, e-learning intro, หรือคลิปโปรโมทของ studio พอดี</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง start-frame/end-frame chaining ใน Kling 3.0 งาน AI video ถัดไปของ studio เช่น XR demo หรือ e-learning opener</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/underwoodxie96/status/2061414477120016873" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@javilopen</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 792 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/javilopen/status/2061834346969882649">View @javilopen on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@bfl_ai Well, this meme didn't age well 😂😂😂 https://t.co/1X7xPrtg3U”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@javilopen โพสต์มีม reaction ถึง Black Forest Labs (@bfl_ai) แบบว่า meme เก่าที่เคยล้อไว้ตอนนี้ผิดพลาดแล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/javilopen/status/2061834346969882649" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CCinephilia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 702 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CCinephilia/status/2061930091903332735">View @CCinephilia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Marty didn't just disappoint us; he betrayed the entire film community. Only a few hours passed, and it was already revealed that he was advising an AI company founded by the people who trained Stable”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Martin Scorsese รับตำแหน่ง advisor ให้ AI company ที่ก่อตั้งโดยทีม Stable Diffusion ซึ่งเคย train โมเดลบนภาพที่มีลิขสิทธิ์โดยไม่ได้รับอนุญาต ทำให้วงการภาพยนตร์ออกมาวิจารณ์หนัก</dd>
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
    <span class="ndf-author">@aisearchio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 677 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aisearchio/status/2061572022074020174">View @aisearchio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bytedance drops an open-source Gemini Omni!!! Bernini is a new AI video generation + editing framework. &amp;gt; Edit videos with text prompts &amp;gt; Image/video references &amp;gt; Code available https://t.co/”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ByteDance ปล่อย Bernini โอเพ่นซอร์ส — framework สร้างและ edit วิดีโอด้วย text prompt และ image/video reference พร้อม code ให้ใช้งาน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Edit วิดีโอด้วย text โดยไม่ต้อง editor เต็มตัว ช่วยเร่ง pipeline ทำ e-learning content และ XR demo reel</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง run Bernini local และทดสอบกับ e-learning หรือ XR content ที่ทำอยู่ เพื่อดูว่าเข้า asset pipeline ได้หรือเปล่า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aisearchio/status/2061572022074020174" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@xxunhuang</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 396 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/xxunhuang/status/2061939239915528653">View @xxunhuang on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm excited to announce that the Morpheus AI team is joining Roblox! Over the past two years, I’ve focused on developing the foundational architectures behind modern video world models, including Self”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Morpheus AI ผู้พัฒนา real-time video world model อย่าง Self Forcing และ AR-DiT ถูก Roblox ซื้อกิจการ เพื่อสร้าง 'Roblox Reality' — ระบบ generative world simulation บนแพลตฟอร์มเกม live</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Real-time generative world model เข้าสู่ game platform ระดับ production จริง บ่งชี้ว่า AI-driven world generation กำลังจะเป็น pipeline มาตรฐาน ตรงกับงาน Unity และ XR ของทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ติดตาม technical disclosure ของ Roblox Reality — architecture ที่เปิดเผยเป็น reference สำหรับ prototype generative environment ใน game projects ของ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/xxunhuang/status/2061939239915528653" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ArtificialAnlys</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 323 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ArtificialAnlys/status/2061494719998546206">View @ArtificialAnlys on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NVIDIA's Cosmos 3 lands at #1 among open weights models in both Text to Image and Image to Video on the Artificial Analysis Leaderboards! Cosmos 3 is a family of omnimodal world models for Physical AI”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>NVIDIA Cosmos 3 (open weights, สูงสุด 64B params) ขึ้นอันดับ 1 ทั้ง Text-to-Image และ Image-to-Video บน Artificial Analysis leaderboards ด้วย architecture รวม autoregressive + diffusion Mixture-of-Transformers</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>อันดับ 1 open weights ทั้ง image และ video generation ในโมเดลเดียว — studio มี local pipeline สร้าง visual assets สำหรับ XR/e-learning โดยไม่เสียค่า API รายครั้ง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Cosmos 3 Super local สำหรับ gen concept art หรือ video clip ใน XR/e-learning — prompt ต้องเป็น structured JSON ไม่ใช่ plain text</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ArtificialAnlys/status/2061494719998546206" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
