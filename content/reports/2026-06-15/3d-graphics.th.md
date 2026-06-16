---
type: social-topic-report
date: '2026-06-15'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-15T04:54:27+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 28
salience: 0.5
sentiment: positive
confidence: 0.6
tags:
- gaussian-splatting
- blender
- unity-shaders
- photogrammetry
- geospatial-3d
- procedural-generation
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065879491843346432/img/Bg2eywsphAzYdYmZ.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-15

## TL;DR
- Google ปล่อย browser flight sim ฟรีที่รันบน Photorealistic 3D Tiles ตัดปัญหาค่า API credit สำหรับ web geospatial 3D [1]
- Gaussian Splatting โผล่หลายงานอิสระ: product viz ที่รักษาเส้นใยผ้าไว้ได้ (Blender → Lichtfeld Studio) [2], splat ระดับเมืองจาก Apple Maps [10], composite ประติมากรรมใน Blender [21], และสแกนเร็วด้วย iPhone [3]
- Unity URP shader tutorial มาต่อเนื่อง: snow coverage บน mobile [5], gem [7], painterly post-process [15], black hole gravitational-lensing [17], พร้อม beginner VFX class [19]
- Meshy AI โปรโมต 'DDC Bridge' สำหรับ export mesh ที่ AI สร้างไปยัง Blender พร้อม animation ติดตามไปด้วย [28]
- คำอ้าง AI procedural ยังเป็นแค่ demo: 'Fable 5' real-time Unreal world generator ที่อ้างว่าสร้างได้ 'สองสามชั่วโมง' [12]

## สิ่งที่เกิดขึ้น
cluster ที่เด่นที่สุดคือด้าน capture/visualization Google เปิด web flight simulator ฟรีบน Photorealistic 3D Tiles โดยระบุว่าตัดค่า API credit ออกสำหรับงาน 3D-tiles บนเว็บ [1] ขณะที่ Apple Maps city-scale Gaussian splat ได้รับเสียงชม [10] Gaussian Splatting ปรากฏซ้ำหลายครั้ง: Blender-to-Lichtfeld product visualization ที่รักษารายละเอียดผ้าละเอียดได้ [2], composite ประติมากรรมด้วย Blender + GS [21], และสแกน iPhone ที่ tracking ความเร็วสูง [3] มีการสแกนคนจริงเพื่อทำ game outfit (EVE) ด้วย [4] ส่วน Blender ยังเป็นศูนย์กลาง production สำหรับ VFX และ shader — VFX Stargate กับ VDB explosions [9], hull shader ของ Halo ที่ rework ใหม่ [14], การดู emote [6], และ tutorial ต่าง ๆ [11][13]

Unity URP shader content เป็นอีก theme ที่วนซ้ำ: snow coverage บน mobile [5], gem ใน Shader Graph [7], painterly post-process [15], black-hole lensing shader [17], และ beginner VFX class สด [19] ด้าน AI-assisted content Meshy โปรโมต DDC Bridge สำหรับ export asset ที่มี animation ไปยัง Blender [27][28] และมีการอ้าง procedural Unreal world generator 'Fable 5' [12] รายการ engagement สูงหลายอันนอกเรื่อง — AI video-editor repo list [8], productivity-tools thread [20], โพสต์ LLM/satire [16], และ reply banter [18][22][23][24][25][26]

## ทำไมถึงสำคัญ (เหตุผล)
Gaussian Splatting คือทิศทางที่ชัดที่สุด: ผลลัพธ์ที่ดีจากหลายทีมอิสระ ตั้งแต่ product viz [2] ไปถึงสแกนโทรศัพท์ [3] และระดับเมือง [10][21] บ่งชี้ว่าฝั่ง capture กำลังสุกงอมสำหรับงาน asset และ environment ในบริบท XR/VR สิ่งนี้ลดต้นทุน photoreal scene และ product capture เทียบกับ manual modeling ประเด็นที่ยังขาด — และไม่มีรายการใดแตะ — คือการ integrate และ performance ของ splat ใน Unity/Unreal และบน mobile/headset ดังนั้นยังอยู่ในระดับ capture/visualization ไม่ใช่ interactive asset ที่ drop-in ได้ Google's free 3D-tiles web sim [1] สำคัญรองลงมา: ตัดค่า API ที่วนซ้ำและส่งสัญญาณว่า browser-based geospatial 3D เป็น path ที่ supported สำหรับ web/mobile Unity URP shader stream [5][7][15][17] คือ craft knowledge ที่นำไปใช้งานฝั่ง games/edutech ได้โดยตรง ต้นทุนต่ำ AI asset/world generation [12][28] อาจย่น prototyping time แต่รายการเหล่านี้ยังเป็น demo และ marketing ไม่ใช่ pipeline ที่ validate แล้ว

## ความเป็นไปได้
**มีแนวโน้มสูง:** Gaussian Splatting เคลื่อนจาก novelty ไปสู่ capture ปกติสำหรับ product viz และ environment scanning จากปริมาณและคุณภาพ demo อิสระ [2][3][10][21] **เป็นไปได้:** browser-based geospatial 3D app จะเพิ่มขึ้น เมื่อ Google เปิด path ฟรีไร้ credit บน 3D tiles [1] **เป็นไปได้แต่ยังไม่ verified:** AI procedural และ mesh tool (Fable 5 [12], Meshy DDC Bridge [28]) ลดเวลา setup asset/world ช่วงต้น — ถือ claim 'สองสามชั่วโมง' [12] เป็น demo จนกว่าจะมีคนทำซ้ำได้ **ไม่น่าเกิดในระยะใกล้:** splat แทน mesh-based pipeline สำหรับ interactive game content — ไม่มีรายการใดแสดง GS real-time ใน engine ที่ performance ระดับ production

## ความเกี่ยวข้องกับ NDF DEV
1) ทดลอง Gaussian Splatting capture workflow สำหรับ XR product/environment viz — ทดสอบ Blender → Lichtfeld path [2] และสแกน iPhone [3] กับ client asset จริงสักชิ้น แล้วตรวจว่า import เข้า Unity แล้วได้ผลแบบไหน ก่อน commit (med) 2) Prototype geospatial scene บน browser ด้วย Google's free 3D tiles สำหรับ web/mobile location-based feature ใด ๆ เพื่อเลี่ยงค่า per-call API [1] (low-med) 3) บันทึกและนำ URP shader technique ที่ใช้งาน Unity ปัจจุบันได้โดยตรง — painterly post-process สำหรับ stylized edutech/game [15], mobile-optimized snow [5], gem [7], lensing [17] (low) 4) ประเมิน Meshy's DDC Bridge สำหรับ AI-generated asset ที่มี animation import เข้า Blender เป็น prototyping shortcut [28] (med) **ข้ามได้:** AI video-editor repo list [8], productivity-tools thread [20], โพสต์ LLM/satire นอกเรื่อง [16], และ reply banter [18][22][23][24][25][26] อย่าวางแผนงบรอบ Fable 5 world-gen claim ที่ยังไม่ verified [12]

## Signals to Watch
- Blender + Lichtfeld Studio เป็น Gaussian Splatting product-viz pipeline [2]
- Geospatial 3D ฟรีไร้ API credit บน Google Photorealistic 3D Tiles [1] และ Apple Maps city splat [10]
- Meshy DDC Bridge — AI mesh export ไปยัง Blender พร้อม animation [28]
- Fable 5 procedural Unreal world claim — ต้องทำซ้ำได้ก่อนเชื่อ [12]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^1160 c23 | [Google got tired of all the vibe coded simulators built on 3d tiles and said - s](https://x.com/bilawalsidhu/status/2065834228818866255) |
| x | msteevie3d | ^349 c10 | [Wow, product visualization via Gaussian Splatting is mind blowing. 🤯 From @Blend](https://x.com/msteevie3d/status/2065879965602603119) |
| x | SadlyItsBradley | ^316 c16 | [Say hello to my fishy friend in high frame rate tracking! This is pretty damn im](https://x.com/SadlyItsBradley/status/2065974984258818512) |
| x | ScrubSquad115 | ^298 c0 | [1 year ago today, we learned that @Bambi_jesuis2 was one of the 3D scan models f](https://x.com/ScrubSquad115/status/2066239676457811997) |
| x | Sakura_Rabbiter | ^293 c2 | [Real-Time Snow Coverage on Mobile with URP #unity #shader #gamedev #VFX😊 https:/](https://x.com/Sakura_Rabbiter/status/2066170153159819717) |
| x | Glacetomic | ^238 c6 | [Completely forgot I can literally view all the emotes in blender if I want to, s](https://x.com/Glacetomic/status/2065791001483174393) |
| x | ushadersbible | ^235 c0 | [A simple gem shader you can create with Shader Graph in Unity 💎 Shaders, Compute](https://x.com/ushadersbible/status/2066242990759186678) |
| x | KanikaBK | ^177 c15 | [Here are 10 AI video editor GitHub repos worth bookmarking: 1. Shotcut https://t](https://x.com/KanikaBK/status/2065780534148731148) |
| x | venturepictures | ^173 c10 | [Little STARGATE test animation for 1) new hyperspace VFX 2) new asteroid / plane](https://x.com/venturepictures/status/2065967983655071928) |
| x | bilawalsidhu | ^142 c2 | [City scale 3d gaussian splats just hit different - well done apple maps](https://x.com/bilawalsidhu/status/2066175946831348094) |
| x | AckroseEdits | ^106 c20 | [More vfx highlights for @StanBrowney 🔥 -Blender -Ae and Pr pro https://t.co/awQe](https://x.com/AckroseEdits/status/2065728382869045435) |
| x | n1neshards | ^81 c15 | [This guy just built a full procedural world generator with real time Unreal Engi](https://x.com/n1neshards/status/2065904409356243293) |
| x | DemNikoArt | ^60 c1 | [EXTENDED TUTORIAL 🚲 Would you like to know more? ⚔️🪐🎖️ I have long versions for ](https://x.com/DemNikoArt/status/2066202654162747670) |
| x | adiri_3d | ^59 c1 | [Another day's progress, and I reworked the hull shader, lots more detail now :) ](https://x.com/adiri_3d/status/2065748564299706829) |
| x | jettelly | ^56 c0 | [This painterly shader uses post-processing in Unity URP to give 3D scenes the lo](https://x.com/jettelly/status/2065690632782582120) |
| x | multimodalart | ^51 c4 | [The municipality of Rio de Janeiro released Rio 3.5, a Qwen fine-tune that is to](https://x.com/multimodalart/status/2065947636054569125) |
| x | jettelly | ^40 c0 | [Check out this real-time black hole shader by consentantaneity, simulating gravi](https://x.com/jettelly/status/2066113427551240331) |
| x | bilawalsidhu | ^40 c7 | [So kids… what moral lesson has this fable taught us? https://t.co/JUQMyvYqpy](https://x.com/bilawalsidhu/status/2065800911776063555) |
| x | VFX_Therapy | ^38 c0 | [I'm conducting live vfx class in Unity for beginners on this Tuesday 8:30pm EST.](https://x.com/VFX_Therapy/status/2065905873126621305) |
| x | AramideOyekunle | ^30 c1 | [Productivity AI Tools: 1. https://t.co/zB10zBY60B – Writing like a human 2. http](https://x.com/AramideOyekunle/status/2065861778353926644) |
| x | blue_nile_3d | ^24 c1 | [Life in the city - sculpture made with gaussian splatting and Blender https://t.](https://x.com/blue_nile_3d/status/2065771922743496865) |
| x | bilawalsidhu | ^20 c0 | [@DavidSacks https://t.co/yJNFNsHrWl](https://x.com/bilawalsidhu/status/2065857687800123752) |
| x | bilawalsidhu | ^11 c0 | [@codetaur Pure visual umami](https://x.com/bilawalsidhu/status/2066000036240953836) |
| x | bilawalsidhu | ^6 c0 | [@APompliano @DavidSacks A new world indeed](https://x.com/bilawalsidhu/status/2065871927994913262) |
| x | bilawalsidhu | ^5 c0 | [@southpolesteve @DanielleFong Banger](https://x.com/bilawalsidhu/status/2065879703743795633) |
| x | bilawalsidhu | ^5 c2 | [@HarksenNiels Same with my confidence that I will be able to fly an f-16 if need](https://x.com/bilawalsidhu/status/2065869718251004109) |
| x | MeshyAI | ^0 c0 | [@tom_krikorian We'll check and let you know soon. Thanks for the feedback!](https://x.com/MeshyAI/status/2066364603920244806) |
| x | MeshyAI | ^0 c1 | [@tom_krikorian You can use Meshy DDC Bridge! It allows you to export your file t](https://x.com/MeshyAI/status/2066353974547226695) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1160 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065834228818866255">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Google got tired of all the vibe coded simulators built on 3d tiles and said - screw it, flight sim on web, free for all - no need to burn api credits. The deeper lore here is that flight sim has long”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google เปิดตัว flight simulator บน browser ฟรี ใช้ Google Maps 3D Tiles โดยไม่ต้องใช้ API credits — เดิมฟีเจอร์นี้ซ่อนอยู่ใน Google Earth Pro desktop</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมใช้ Google Maps 3D Tiles สร้าง environment 3D สำหรับ web/XR ได้ฟรี ไม่ต้องห่วงเรื่อง API credits ตอน prototype</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดลอง flight sim ดูคุณภาพ 3D Tiles และ load performance เป็น reference สำหรับ project 3D world บน web</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2065834228818866255" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@msteevie3d</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 349 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/msteevie3d/status/2065879965602603119">View @msteevie3d on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow, product visualization via Gaussian Splatting is mind blowing. 🤯 From @Blender to @lichtfeldstudio , the details are crazy. It preserved everything so well, even the tiny hairs on the fabric! I ho”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปิน 3D ถ่าย 500 ภาพแล้วแปลงเป็น Gaussian Splat (2M splats, 50k iterations ผ่าน IGS+ ใน Lichtfeld Studio) ได้รายละเอียดพื้นผิวระดับเส้นขนผ้า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Gaussian Splatting สร้าง product viz คุณภาพสูงจากภาพถ่ายล้วน — เป็น pipeline ที่ใช้ได้จริงสำหรับงาน XR และ e-learning โดยไม่ต้อง model มือ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ: ถ่าย prop หรือ product 200–500 ภาพ แล้ว process ผ่าน IGS+ หรือ Luma AI เพื่อประเมินคุณภาพ splat สำหรับ asset ใน XR</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/msteevie3d/status/2065879965602603119" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SadlyItsBradley</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 316 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SadlyItsBradley/status/2065974984258818512">View @SadlyItsBradley on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Say hello to my fishy friend in high frame rate tracking! This is pretty damn impressive for such a quick 3D scan (from my iPhone) https://t.co/vzXlKsFRW5”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@SadlyItsBradley แชร์คลิป 3D scan ปลาที่ถ่ายด้วย iPhone พร้อม high frame rate tracking แสดงให้เห็นว่า mobile photogrammetry ให้ผลลัพธ์ที่ใช้งาน real-time ได้จริงในเวลาไม่นาน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การ scan ด้วย iPhone ได้คุณภาพพอใช้งาน real-time ได้แล้ว ลด barrier ด้านอุปกรณ์สำหรับ asset capture ใน XR/VR หรือ Unity prototype pipeline</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลองใช้ iPhone scan props เล็กๆ หนึ่งวัน เพื่อประเมินว่า workflow นี้ใช้ทำ rapid asset prototyping ได้จริงก่อนลงทุนอุปกรณ์ scan เฉพาะทาง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SadlyItsBradley/status/2065974984258818512" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ScrubSquad115</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 298 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ScrubSquad115/status/2066239676457811997">View @ScrubSquad115 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“1 year ago today, we learned that @Bambi_jesuis2 was one of the 3D scan models for EVE She shared Black Wave and Keyhole suit with us many other outfits were scanned in with Bambi but sadly didn't tak”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนเกมระลึกครบรอบ 1 ปีที่รู้ว่ามีการใช้ model คนจริงในการ 3D scan ตัวละคร EVE ในเกม Stellar Blade</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ScrubSquad115/status/2066239676457811997" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Sakura_Rabbiter</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 293 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Sakura_Rabbiter/status/2066170153159819717">View @Sakura_Rabbiter on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Real-Time Snow Coverage on Mobile with URP #unity #shader #gamedev #VFX😊 https://t.co/0txae8ebtw Come and subscribe to my Fanbox to download this project https://t.co/sT4MYw51yi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@Sakura_Rabbiter ปล่อย shader snow coverage แบบ real-time บน Unity URP สำหรับ mobile พร้อม project ให้โหลดบน Fanbox</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Shader snow coverage ที่ optimize สำหรับ mobile URP พร้อม project จริง — ใช้เป็น reference สำหรับ environment effect ใน Unity ได้เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team โหลด project จาก Fanbox มาศึกษา shader ก่อนทำ outdoor/seasonal scene</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Sakura_Rabbiter/status/2066170153159819717" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Glacetomic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 238 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Glacetomic/status/2065791001483174393">View @Glacetomic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Completely forgot I can literally view all the emotes in blender if I want to, so here's Remi without the heavy abstraction vfx. https://t.co/PHMwBbanoX”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator แสดงให้เห็นว่า emote ของ game character สามารถ import และดูใน Blender ได้โดยตรง ช่วยให้เห็น mesh และ animation ดิบโดยไม่มี VFX ของ engine บัง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ใช้ Blender ดู game asset แบบ raw นอก engine เป็น workflow ที่ practical โดยเฉพาะตอน debug rig หรือ animation</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ใช้วิธีเดียวกันได้ — export FBX/glTF แล้วดู rig หรือ blend shape ใน Blender ก่อน debug ใน Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Glacetomic/status/2065791001483174393" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ushadersbible</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 235 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ushadersbible/status/2066242990759186678">View @ushadersbible on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A simple gem shader you can create with Shader Graph in Unity 💎 Shaders, Compute Shaders, and Math for Graphics 🔗 https://t.co/MQP1nKiD0x #IndieDevSunday https://t.co/iHisMzpxRc”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@ushadersbible แชร์วิธีทำ gem shader ด้วย Unity Shader Graph พร้อม tutorial แบบ step-by-step ใน #IndieDevSunday</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ใช้ได้ตรงกับงาน Unity game และ XR — gem/collectible effects เพิ่ม visual polish โดยไม่ต้องเขียน shader code เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team เอา Shader Graph setup นี้ไปทำเป็น reusable asset สำหรับ gem/crystal ใน project ที่กำลังทำได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ushadersbible/status/2066242990759186678" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KanikaBK</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 177 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KanikaBK/status/2065780534148731148">View @KanikaBK on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here are 10 AI video editor GitHub repos worth bookmarking: 1. Shotcut https://t.co/avPrh2NmjC Most actively maintained open source video editor in 2026. 14K stars. Cross-platform with AI-assisted fea”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>รายการ open-source video editor 10 ตัวที่น่าติดตามในปี 2026 นำโดย Shotcut (14K stars), Blender VSE, Kdenlive และ Wan2.1 ของ Alibaba ที่ generate video 1080p แบบ text-to-video ใช้ license Apache 2.0</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Wan2.1 และ Blender VSE ให้ pipeline สร้างและ composite วิดีโอระดับ production ฟรี เหมาะกับงาน XR/VR และ e-learning โดยไม่มีค่า license</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Wan2.1 สำหรับ generate B-roll หรือ cutscene ใน e-learning และ XR พร้อมประเมิน Blender VSE เป็น compositing step ใน post-production pipeline โดยไม่เสียค่าใช้จ่าย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KanikaBK/status/2065780534148731148" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
