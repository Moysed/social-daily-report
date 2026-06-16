---
type: social-topic-report
date: '2026-06-14'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-14T15:39:43+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 33
salience: 0.55
sentiment: mixed
confidence: 0.55
tags:
- gaussian-splatting
- photogrammetry
- image-to-3d
- blender
- unity-urp
- procedural-generation
thumbnail: https://pbs.twimg.com/ext_tw_video_thumb/1856725024968753153/pu/img/k_Non4U2lQsIvWE1.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-14

## TL;DR
- Google เปิดตัว flight sim บนเว็บแบบฟรี สร้างบน Photorealistic 3D Tiles โดยอ้างว่าไม่ต้องจ่าย API credits สำหรับ 3D-tile simulator อีกต่อไป [1]; Apple Maps กำลัง ship city-scale Gaussian splats [29]
- เครื่องมือที่เรียกว่า 'Fable 5' ถูกใช้สร้าง procedural worlds render ใน Unreal Engine แบบ real-time อ้างว่าใช้เวลา 'สองสามชั่วโมง' [2][7][12] — เป็น demo claim ยังไม่ผ่านการยืนยัน
- Gaussian Splatting ขยับเข้าสู่ product visualization ผ่าน Blender → Lichtfeld Studio path ที่คงรายละเอียดละเอียดอย่างเส้นใยผ้าได้ [5] และงาน sculpture/scene [23]
- Image-to-3D model stack กำลังรวมศูนย์: TripoSR, Microsoft TRELLIS, Hunyuan3D 2.1, Nerfstudio และ 3DGS เข้าถึงได้ผ่าน GPU cloud tooling [13]; สแกนด้วย iPhone แบบ high-frame-rate tracking [3][10]
- Unity URP shader techniques พร้อม production: snow coverage บน mobile แบบ real-time [15] และ painterly post-process look [16]

## สิ่งที่เกิดขึ้น
signal ที่มี engagement สูงสุดคือ geospatial: Google ประกาศปล่อย web flight simulator ฟรีบน Photorealistic 3D Tiles เพื่อให้ developer ไม่ต้องเผา API credits [1] สอดคล้องกับโพสต์ Google Earth และ throwback ที่เกี่ยวข้อง [20][24][27] รวมถึง Apple Maps ที่ ship city-scale 3D Gaussian splats [29] กลุ่มที่สองคือเครื่องมือชื่อ 'Fable 5' สำหรับ procedural world generation render ใน Unreal Engine โดยมีหลายโพสต์อธิบายการสร้าง landscape, lighting และรายละเอียดแบบเต็มรูปแบบในเวลาสั้น [2][7][12][18] กลุ่มที่สามคือ asset capture และ generation: Gaussian Splatting สำหรับ product viz จาก Blender [5] และงาน sculpture [23]; image-to-3D pipeline (TripoSR, TRELLIS, Hunyuan3D 2.1, Nerfstudio, 3DGS) ผ่าน GPU cloud [13]; และ iPhone photogrammetry แบบเร็ว [3][10] Blender ยังคงเป็น DCC หลักสำหรับ VFX และ shader [4][8][9][11][14] ขณะที่ Unity URP shader breakdown ครอบคลุม mobile snow [15] และ painterly post-processing [16] พร้อมโฆษณา Unity VFX class สำหรับผู้เริ่มต้น [19] รายการที่เหลือเป็น noise นอกหัวข้อ: LLM fine-tune [17], AI video-editor และรายการ productivity [6][21] และข่าวไม่เกี่ยวข้อง [22]

## ทำไมถึงสำคัญ (เหตุผล)
มีสองเทรนด์ที่สำคัญต่อ studio: แรก capture-to-asset ถูกลงต่อเนื่อง — image-to-3D และ phone-based splatting/photogrammetry [3][10][13] ลดต้นทุนสร้าง reference mesh และ prop, และ splatting ตอนนี้คงรายละเอียดพอสำหรับ product-grade visual [5] ทำให้แรงงานเปลี่ยนจาก modeling ไป cleanup (topology, UV, runtime rendering) ไม่ใช่หายไป สอง platform-owned 3D data กำลังเข้าถึงได้โดยตรงบนเว็บ — ถ้า Google 3D Tiles flight sim ฟรีจริง [1] และ Apple เปิด city-scale splats [29] งาน geospatial XR และ web/edutech demo สร้างได้โดยไม่มี per-call API cost แต่ 'ฟรี' ต้องตรวจ license ก่อนนำไปพึ่งพาใน product จริง claim ของ 'Fable 5' procedural-to-Unreal [2][7][12] ชี้ให้เห็น world prototyping ที่เร็วขึ้น แต่ tweet เชิงเสียดสี 'what moral lesson has this fable taught us' [18] จากผู้เขียนคนเดียวกันเป็นคำเตือนที่สมเหตุสมผล: demo เวลาสั้นแทบไม่เคยเท่ากับ asset ที่ควบคุมได้และ ship จริงได้

## ความเป็นไปได้
**มีแนวโน้มสูง:** Gaussian Splatting ขยับจาก novelty ไปสู่ production สำหรับ product viz และ environment capture อย่างต่อเนื่อง เห็นจาก Blender/studio-tool integration ที่ใช้งานได้จริง [5][23] และ platform adoption ของ Apple [29] **เป็นไปได้:** image-to-3D (TRELLIS, Hunyuan3D 2.1) กลายเป็นขั้นตอน greyboxing/prototyping มาตรฐาน [13] แม้ production ยังต้องการ retopo และ UV แบบ manual **เป็นไปได้:** web 3D Tiles ฟรีหรือต้นทุนต่ำเปิดทาง geospatial web/XR และ edutech demo [1][29] ขึ้นอยู่กับเงื่อนไข license **ไม่น่าเกิดในเร็วๆ นี้:** เครื่องมือเดียว ('Fable 5') ผลิต Unreal world ที่ ship ได้โดยไม่ต้อง rework manual [2][7][12]; หลักฐานปัจจุบันเป็นแค่ demo ที่ยังไม่ผ่านการยืนยัน และผู้เขียนคนหนึ่งส่งสัญญาณความไม่เชื่อ [18] ไม่มีแหล่งข้อมูลใดระบุตัวเลขความน่าจะเป็น

## การประยุกต์ใช้ใน NDF DEV
1) ทำ spike เร็วๆ สำหรับ image-to-3D เพื่อสร้าง prototype/XR prop โดยใช้ TRELLIS และ Hunyuan3D 2.1; วัด mesh quality และเวลา cleanup ก่อน commit — effort ต่ำ/กลาง [13] 2) Pilot Blender → Gaussian Splatting path สำหรับ product-viz หรือ XR capture deliverable และยืนยัน runtime playback (Unity 3DGS plugin) ก่อน quote ลูกค้า — effort กลาง [5][23][29] 3) เพิ่ม iPhone photogrammetry/scan ใน reference-capture workflow สำหรับ scene/prop reference แบบเร็ว — effort ต่ำ [3][10] 4) นำ Unity URP shader techniques ไปใช้ใน title ปัจจุบันได้เลย: mobile snow coverage และ painterly post-process เป็น URP-native และเพิ่มคุณค่า portfolio — effort ต่ำ [15][16] 5) ตรวจ license และเงื่อนไขค่าใช้จ่ายของ Google Photorealistic 3D Tiles ก่อนออกแบบ feature geospatial web หรือ edutech โดยอาศัย 'ฟรี' — effort ต่ำสำหรับการตรวจ, กลางสำหรับ build [1][29] ข้าม: การเดิมพันกับ 'Fable 5' procedural-to-Unreal สำหรับ production จนกว่า output จะทำซ้ำได้และตรวจสอบได้ [2][7][12]; เพิกเฉยต่อรายการนอกหัวข้อ [17][22][6][21]

## Signals ที่ต้องติดตาม
- ยืนยันว่า Google web flight sim / 3D Tiles access ฟรีจริงหรือไม่ และเงื่อนไข license [1][29]
- Apple Maps city-scale 3D Gaussian splats — ติดตาม SDK/runtime access สำหรับ third-party app [29]
- Image-to-3D stack ที่กำลังพัฒนา (TRELLIS, Hunyuan3D 2.1) — ติดตาม production-readiness ของ topology/UV [13]
- 'Fable 5' procedural-in-Unreal claims — ดูผลลัพธ์ที่ทำซ้ำได้และควบคุมได้ vs. demo แบบ one-off [12][18]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^1088 c22 | [Google got tired of all the vibe coded simulators built on 3d tiles and said - s](https://x.com/bilawalsidhu/status/2065834228818866255) |
| x | bilawalsidhu | ^846 c18 | [Someone needs to throw fable 5 at the OG of procedural 3D generation (houdini) a](https://x.com/bilawalsidhu/status/2065457916405072127) |
| x | SadlyItsBradley | ^240 c12 | [Say hello to my fishy friend in high frame rate tracking! This is pretty damn im](https://x.com/SadlyItsBradley/status/2065974984258818512) |
| x | Glacetomic | ^235 c6 | [Completely forgot I can literally view all the emotes in blender if I want to, s](https://x.com/Glacetomic/status/2065791001483174393) |
| x | msteevie3d | ^221 c7 | [Wow, product visualization via Gaussian Splatting is mind blowing. 🤯 From @Blend](https://x.com/msteevie3d/status/2065879965602603119) |
| x | KanikaBK | ^169 c15 | [Here are 10 AI video editor GitHub repos worth bookmarking: 1. Shotcut https://t](https://x.com/KanikaBK/status/2065780534148731148) |
| x | _vmlops | ^152 c6 | [Fable 5 tackling procedural world generation and rendering in Unreal Engine is w](https://x.com/_vmlops/status/2065619237788586086) |
| x | venturepictures | ^137 c8 | [Little STARGATE test animation for 1) new hyperspace VFX 2) new asteroid / plane](https://x.com/venturepictures/status/2065967983655071928) |
| x | AckroseEdits | ^99 c17 | [More vfx highlights for @StanBrowney 🔥 -Blender -Ae and Pr pro https://t.co/awQe](https://x.com/AckroseEdits/status/2065728382869045435) |
| x | MiladKambari | ^90 c0 | [3d scan..... #animation #b3d #blender3d #UnrealEngine #SubstancePainter #gamedev](https://x.com/MiladKambari/status/2065454231717372276) |
| x | AKantemirov | ^84 c4 | [I should keep working on my model, but these procedural textures from @noaxdesig](https://x.com/AKantemirov/status/2065605342206058857) |
| x | n1neshards | ^75 c15 | [This guy just built a full procedural world generator with real time Unreal Engi](https://x.com/n1neshards/status/2065904409356243293) |
| x | clore_ai | ^63 c35 | [Create detailed 3D models from images using https://t.co/tS1YgkSXYM's GPU-powere](https://x.com/clore_ai/status/2065457183811092985) |
| x | adiri_3d | ^54 c1 | [Another day's progress, and I reworked the hull shader, lots more detail now :) ](https://x.com/adiri_3d/status/2065748564299706829) |
| x | Sakura_Rabbiter | ^49 c1 | [Real-Time Snow Coverage on Mobile with URP #unity #shader #gamedev #VFX😊 https:/](https://x.com/Sakura_Rabbiter/status/2066170153159819717) |
| x | jettelly | ^47 c0 | [This painterly shader uses post-processing in Unity URP to give 3D scenes the lo](https://x.com/jettelly/status/2065690632782582120) |
| x | multimodalart | ^45 c2 | [The municipality of Rio de Janeiro released Rio 3.5, a Qwen fine-tune that is to](https://x.com/multimodalart/status/2065947636054569125) |
| x | bilawalsidhu | ^40 c7 | [So kids… what moral lesson has this fable taught us? https://t.co/JUQMyvYqpy](https://x.com/bilawalsidhu/status/2065800911776063555) |
| x | VFX_Therapy | ^32 c0 | [I'm conducting live vfx class in Unity for beginners on this Tuesday 8:30pm EST.](https://x.com/VFX_Therapy/status/2065905873126621305) |
| x | bilawalsidhu | ^30 c0 | [@googleearth Now this is a real throwback! LFG](https://x.com/bilawalsidhu/status/2065452301121179709) |
| x | AramideOyekunle | ^29 c1 | [Productivity AI Tools: 1. https://t.co/zB10zBY60B – Writing like a human 2. http](https://x.com/AramideOyekunle/status/2065861778353926644) |
| x | SamuelBaker_B | ^25 c9 | [1/10: RDF/M23 ran two industrial-scale forced recruitment camps in occupied east](https://x.com/SamuelBaker_B/status/2065513894542520814) |
| x | blue_nile_3d | ^24 c1 | [Life in the city - sculpture made with gaussian splatting and Blender https://t.](https://x.com/blue_nile_3d/status/2065771922743496865) |
| x | bilawalsidhu | ^24 c10 | [We live in interesting times in the foothills of the singularity; this is perhap](https://x.com/bilawalsidhu/status/2065616112914505772) |
| x | EmpressTrash | ^20 c5 | [Cycladic Venus ~~~ 1 week open edition for @panelhausapp artist in residency on ](https://x.com/EmpressTrash/status/2065623586585383307) |
| x | bilawalsidhu | ^19 c0 | [@DavidSacks https://t.co/yJNFNsHrWl](https://x.com/bilawalsidhu/status/2065857687800123752) |
| x | bilawalsidhu | ^16 c1 | [Genuinely amazing to spend time with some of the foremost creative technologists](https://x.com/bilawalsidhu/status/2065565442983309560) |
| x | multimodalart | ^16 c1 | [Try it out here! 🤗https://t.co/SD2aiXQG0a](https://x.com/multimodalart/status/2065558377669742941) |
| x | bilawalsidhu | ^10 c2 | [City scale 3d gaussian splats just hit different - well done apple maps](https://x.com/bilawalsidhu/status/2066175946831348094) |
| x | bilawalsidhu | ^6 c0 | [@codetaur Pure visual umami](https://x.com/bilawalsidhu/status/2066000036240953836) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1088 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065834228818866255">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Google got tired of all the vibe coded simulators built on 3d tiles and said - screw it, flight sim on web, free for all - no need to burn api credits. The deeper lore here is that flight sim has long”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google เปิด flight simulator บน web ฟรี ใช้ 3D Tiles ของ Google Earth โดยไม่ต้องมี Maps API key — ฟีเจอร์นี้เคยซ่อนอยู่ใน Google Earth Pro desktop มาก่อน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า Google 3D Tiles รับ real-time interactive 3D บน browser ระดับ consumer ได้ — เป็นตัวชี้วัด ceiling สำหรับงาน web หรือ XR ที่ใช้ stack เดียวกัน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองรัน flight sim บน web เพื่อดู rendering performance และ UX — ใช้เป็น baseline ฟรีตอน scope งาน 3D หรือ XR บน web</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2065834228818866255" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 846 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065457916405072127">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Someone needs to throw fable 5 at the OG of procedural 3D generation (houdini) and render it all in unreal engine https://t.co/QvVuHNhll7”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ฝันเอาเองว่า Fable 5 ควรสร้าง asset ด้วย Houdini แบบ procedural แล้ว render ใน Unreal Engine — ไม่มีประกาศหรือข้อมูลเทคนิคจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2065457916405072127" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SadlyItsBradley</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 240 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SadlyItsBradley/status/2065974984258818512">View @SadlyItsBradley on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Say hello to my fishy friend in high frame rate tracking! This is pretty damn impressive for such a quick 3D scan (from my iPhone) https://t.co/vzXlKsFRW5”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>สแกน 3D ปลาด้วย iPhone LiDAR แบบรวดเร็ว ได้ผลเป็น 3D model ที่ track ได้ใน high frame rate โดยไม่ใช้อุปกรณ์สแกนเฉพาะ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ผลสแกน iPhone LiDAR นำเข้า Unity หรือ XR pipeline ได้เลย เหมาะสำหรับ organic asset แบบรวดเร็วโดยไม่ต้องมีสตูดิโอ photogrammetry</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ลองใช้ Polycam หรือ RealityScan บน iPhone ดูว่าคุณภาพ scan เพียงพอสำหรับสร้าง prop และ environment asset หรือไม่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SadlyItsBradley/status/2065974984258818512" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Glacetomic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 235 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Glacetomic/status/2065791001483174393">View @Glacetomic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Completely forgot I can literally view all the emotes in blender if I want to, so here's Remi without the heavy abstraction vfx. https://t.co/PHMwBbanoX”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist @Glacetomic พบว่า Blender ดู emote ของ character ได้โดยตรงโดยไม่มี VFX ซ้อนทับ แล้ว post render สะอาดของตัวละคร Remi ออกมา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Glacetomic/status/2065791001483174393" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@msteevie3d</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 221 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/msteevie3d/status/2065879965602603119">View @msteevie3d on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow, product visualization via Gaussian Splatting is mind blowing. 🤯 From @Blender to @lichtfeldstudio , the details are crazy. It preserved everything so well, even the tiny hairs on the fabric! I ho”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักสร้าง 3D ถ่าย 500 รูปจากสินค้าจริง แล้ว train 50k iterations ด้วย IGS+ ได้ Gaussian Splat 2M splats — รักษา detail ระดับเส้นขนผ้าได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Pipeline นี้ (ถ่ายรูป → IGS+ → Gaussian Splat) ให้ asset สินค้าสมจริงโดยไม่ต้อง model polygon เหมาะกับ XR product demo หรือ e-learning</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลอง IGS+ สำหรับถ่าย product — 500 รูปทำได้ด้วยกล้อง DSLR หรือ phone rig และ output ใส่ Unity ผ่าน Gaussian Splatting plugin ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/msteevie3d/status/2065879965602603119" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KanikaBK</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 169 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KanikaBK/status/2065780534148731148">View @KanikaBK on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here are 10 AI video editor GitHub repos worth bookmarking: 1. Shotcut https://t.co/avPrh2NmjC Most actively maintained open source video editor in 2026. 14K stars. Cross-platform with AI-assisted fea”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>รวม 10 open-source AI video editor repos ที่น่า bookmark ในปี 2026 ครอบคลุม Shotcut, Kdenlive, Blender VSE, Wan2.1 (text-to-video Apache 2.0 จาก Alibaba) และ HunyuanVideo จาก Tencent</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Wan2.1 (Apache 2.0) และ Blender VSE ใช้ได้เลยสำหรับงาน XR/VR cinematic และ e-learning video โดยไม่มีค่า license</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง Wan2.1 สำหรับ b-roll หรือ intro ใน e-learning และใช้ Blender VSE เป็น compositing layer สำหรับ XR trailer</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KanikaBK/status/2065780534148731148" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@_vmlops</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 152 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/_vmlops/status/2065619237788586086">View @_vmlops on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fable 5 tackling procedural world generation and rendering in Unreal Engine is wild to watch 🔥 https://t.co/fnRT5F5sWd”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Playground Games สร้าง Fable 5 ด้วย procedural world generation บน Unreal Engine โดยมี footage เริ่มหมุนเวียนให้เห็นผลจริงในระดับ open world</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Procedural gen ระดับ AAA ใน UE5 เผย pattern ของ terrain, foliage, biome pipeline ที่ทีม Unity เอามาศึกษาปรับใช้กับ open-world หรืองาน XR environment ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู footage จาก link แล้วจดว่า procedural system ไหนปรากฏ (terrain, scatter, LOD) จากนั้นเช็ค Unity equivalent ใน HDRP หรือ third-party tools</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/_vmlops/status/2065619237788586086" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@venturepictures</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 137 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/venturepictures/status/2065967983655071928">View @venturepictures on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Little STARGATE test animation for 1) new hyperspace VFX 2) new asteroid / planet / atmosphere shader 3) PDC / railguns / missles / VDB explosions All done in Blender 3D. To save the gate! #Stargate #”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@venturepictures ปล่อย test animation ใน Blender 3D สาธิต hyperspace VFX, shader ดาวเคราะห์/บรรยากาศ และ VDB explosion สำหรับโปรเจกต์แฟน Stargate</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค atmosphere shader และ VDB explosion ใช้ได้ตรงกับงาน Unity XR/VR หรือ game ที่ต้องการ visual แนว sci-fi หรืออวกาศ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดู breakdown shader/VFX นี้เป็น reference สำหรับ asset pipeline งานฉาก sci-fi หรืออวกาศ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/venturepictures/status/2065967983655071928" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
