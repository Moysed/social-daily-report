---
type: social-topic-report
date: '2026-05-31'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-05-31T04:24:21+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 30
salience: 0.6
sentiment: positive
confidence: 0.55
tags:
- gaussian-splatting
- xr
- blender
- asset-pipeline
- ai-3d
- unity
thumbnail: https://pbs.twimg.com/media/HJi506gbMAAFWVc.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-05-31

## TL;DR
- glTF มี extension อย่างเป็นทางการสำหรับ 3D Gaussian Splatting แล้ว รองรับ 3DGS ระดับเมืองที่บีบอัด, แบ่ง tile และ stream ได้ [4]; standards leads จาก Niantic Spatial และ Khronos พูดถึงทิศทางต่อไปของ 3DGS [22]
- SplatBox รัน Gaussian splats กว่า 2,000,000 จุดพร้อม real-time relighting บน Quest 3 standalone ไม่ต้องต่อสาย [16] — ตรงกับงาน XR/VR ของสตูดิโอโดยตรง
- Blender geometry-nodes procedural workflows [15] และ cloth-physics-bake-to-bones rig ที่ถ่าย sim เข้า game engine ได้ [6][11] บ่งชี้ว่า pipeline Blender→engine สุกขึ้นมาก
- Meshy เปิด beta 'Meshy 3D Agent' สำหรับ 3D generation แบบ chat-driven [10][30]; อีกโพสต์อ้างว่า Claude Opus 4.8 เชื่อมกับ Blender แทนงานศิลปิน ซึ่งอ่านแล้วเป็น hype ยังไม่มีการยืนยัน [14]
- Unreal 5.8 เพิ่ม skeletonize/weight สำหรับ mesh ซับซ้อน (ต้นไม้) และ Control Rig Dynamics แบบ experimental [17]; CoStar กำลังนำ 3DGS เข้า 1,700 ชานเมืองในออสเตรเลีย [24]

## สิ่งที่เกิดขึ้น
Gaussian Splatting เป็นสัญญาณหลักที่ชัดเจนที่สุด glTF ได้รับ extension 3DGS อย่างเป็นทางการ และ city-scale splats บีบอัด, แบ่ง tile และ stream ได้แล้ว [4] พร้อมบทสนทนาเชิงลึกระหว่าง CTO ของ Niantic Spatial กับประธาน Khronos เรื่องทิศทางของ format [22] รวมถึงบริบทการ capture ด้วย aerial oblique-imagery [27] ฝั่ง on-device: SplatBox render ได้ 2M+ splats พร้อม real-time relighting บน Quest 3 standalone [16] และ CoStar กำลังสร้าง 3D ชานเมืองออสเตรเลีย 1,700 แห่ง [24] ฝั่ง DCC/pipeline มีเนื้อหา Blender เกี่ยวกับ procedural geometry-nodes assets [15], cloth-physics-to-bones rig สำหรับ engine [6][11] และ shader/texturing workflows สำหรับ Unity/Unreal [5][9][20] Unreal 5.8 preview mesh skeletonization และ Control Rig Dynamics [17] ส่วน Unity's Infinite Lands แสดง spline-based procedural road system [18] AI-3D tooling ปรากฏผ่าน Meshy 3D Agent beta แบบ chat [10][30] และการอ้างที่ยังไม่ยืนยันว่า Claude Opus 4.8 ขับ Blender ได้ [14] เนื้อหาที่ engagement สูงสุดส่วนใหญ่เป็น anime/fan render art [2][9] หรือโพสต์กีฬาที่ไม่เกี่ยว [1][3] ไม่ใช่ข่าว tooling

## เหตุผลที่สำคัญ
การ standardize 3DGS สำคัญที่สุดสำหรับสตูดิโอ extension glTF อย่างเป็นทางการ [4] บวกกับ streaming/tiling หมายความว่า splats เดินผ่าน asset pipeline และ engine ที่มีอยู่ได้แล้ว แทนที่จะต้องอยู่ใน viewer เฉพาะ และ Quest 3 standalone playback พร้อม relighting [16] ขจัดอุปสรรคเดิมที่ splats หนักหรือ static เกินสำหรับ standalone XR ทั้งสองสิ่งนี้เลื่อน Gaussian Splatting จาก demo ไปสู่ production capture format ที่ใช้ได้จริงสำหรับ XR อย่างเต็มตัว พัฒนาการใน Blender [6][11][15][20] ลด manual labor ในส่วน asset production ที่สตูดิโอถือเองอยู่แล้ว — procedural variation และการนำ sim/cloth เข้า engine เป็น baked bone animation AI-3D tools [10][14] เป็นพื้นที่ที่ noise มากที่สุด: Meshy agent เป็น real beta [10][30] แต่ framing 'แทนศิลปินได้ใน 5 prompts' [14] คือ marketing claim ที่ไม่มีการ reproduce ให้ดู ดังนั้นคุณภาพ output, topology และความพร้อม rig ยังไม่ได้รับการพิสูจน์

## ความเป็นไปได้
มีแนวโน้มสูง: การนำ 3DGS มาใช้ใน tooling เร็วขึ้นเมื่อ glTF มี extension อย่างเป็นทางการแล้ว และ engine/viewer มี format เดียวที่ target ได้ [4][22] เป็นไปได้: standalone-headset splat playback อย่าง SplatBox [16] กลายเป็น viable สำหรับ client XR demos ภายในปีหน้า เพราะรัน 2M splats พร้อม relighting บน Quest 3 ได้แล้ว เป็นไปได้: 3DGS ถูกนำไปใช้เป็น spatial-reasoning benchmarks สำหรับ AI video models ตามที่มีการพูดถึงใน 2 โพสต์ [7][26] — ยังเป็นการคาดเดา ยังไม่เป็น product ไม่น่าเกิดในระยะใกล้: AI agents ผลิต game assets ที่พร้อม rig และจบในตัวโดยไม่ต้องให้ศิลปิน cleanup [14][10]; หลักฐานปัจจุบันเป็นแค่ beta และการอ้างที่ยังไม่ยืนยัน คุณภาพระดับ production ยังไม่มีให้เห็น

## การใช้ในองค์กร — NDF DEV
1) ทดสอบ Quest 3 splat playback แบบ SplatBox สำหรับ XR portfolio ชิ้นเดียว โดยใช้ photogrammetry/aerial capture ของ location จริง — effort ปานกลาง, ยืนยันว่า 3DGS ใช้กับ client XR ได้จริงไหม [16][4] 2) นำ trim-sheet → Substance masks → Unity shader texturing workflow [20] และ procedural geometry-nodes assets [15] เข้าสู่การผลิต Unity asset ปัจจุบัน — effort ต่ำ/ปานกลาง, ลด repetitive authoring 3) Pilot Blender cloth-physics-bake-to-bones rig กับตัวละครหนึ่งตัวเพื่อถ่าย sim เข้า Unity เป็น baked animation — effort ปานกลาง [6][11] 4) ทดลอง Meshy 3D Agent กับ concept/blockout assets ที่ทิ้งได้เท่านั้น พร้อม artist review gate — effort ต่ำ, ไม่ commit กับ pipeline [10][30] ข้าม: การอ้างว่า 'Claude Opus แทนศิลปิน' ในฐานะ production plan [14]; Unreal 5.8 features [17] ถ้ายังไม่มี Unreal project ที่ active; โพสต์ cricket/anime fan [1][2][3][9] แม้ engagement สูงแต่ไม่มี tooling signal

## สัญญาณที่ต้องติดตาม
- การนำ glTF 3DGS extension ไปใช้ใน engine และ exporter — จับตา Unity/Unreal import support [4][22]
- Standalone-headset splat tools (SplatBox) ที่รองรับ splat count สูงขึ้นหรือ ship SDK สำหรับ Quest [16]
- Meshy 3D Agent ออกจาก beta และ independent topology/rig-quality tests [10][30]
- ว่า 3DGS captures ถูกนำไปใช้เป็น AI spatial-reasoning benchmarks หรือไม่ ซึ่งจะบ่งชี้การลงทุนในวงกว้าง [7][26]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | PXJOSHIMA | ^2989 c12 | [In 2024 I was approached on IG by someone from a games design studio about makin](https://x.com/PXJOSHIMA/status/2060601157240881492) |
| x | Nyaonyx09 | ^2509 c11 | [Welcome back.... Animations by me using Blender. Credits : Models : Hoyoverse BG](https://x.com/Nyaonyx09/status/2060277804470862196) |
| x | broskyxn | ^1556 c11 | [@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year stil](https://x.com/broskyxn/status/2060730034584015072) |
| x | bilawalsidhu | ^679 c21 | [i like big splats and i cannot lie. you can now compress, tile and stream city s](https://x.com/bilawalsidhu/status/2060518632547877359) |
| x | sean_gause | ^221 c2 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | EdwardUrena_h | ^195 c2 | [With this tool as a foundation, you will be able to bake the cloth physics onto ](https://x.com/EdwardUrena_h/status/2060338391380619716) |
| x | bilawalsidhu | ^176 c6 | [Larus went ham with this one! Love the synced highlighting on the camera path, s](https://x.com/bilawalsidhu/status/2060373038982459741) |
| x | AckroseEdits | ^154 c18 | [Vfx highlights from @StanBrowney's Fitness Island video 🏝️ -Premiere pro + After](https://x.com/AckroseEdits/status/2060352963986530678) |
| x | A_fan_of_Sonic | ^144 c2 | [Ripped, fixed and shaded Vegeta from Sparking Zero for Blender • Move eyes in sh](https://x.com/A_fan_of_Sonic/status/2060749070554001630) |
| x | MeshyAI | ^120 c9 | [Introducing Meshy 3D Agent 🚀 The world's first AI agent for 3D creation, now in ](https://x.com/MeshyAI/status/2060311322123014560) |
| x | EdwardUrena_h | ^110 c0 | [One of the advantages of this is that you can design your own control system for](https://x.com/EdwardUrena_h/status/2060397763632701921) |
| x | ZohaibAi__sf | ^106 c30 | [Day 5. It's finished. 20,000 credits. ~$5,000. A global story. VFX. Costumes. Wi](https://x.com/ZohaibAi__sf/status/2060670680329511122) |
| x | mattworkman | ^103 c19 | [I once OFFENDED the mentor that hand picked me up from the gutter and sat me at ](https://x.com/mattworkman/status/2060573070151078006) |
| x | polydao | ^96 c18 | [This guy connected Claude Opus 4.8 to Blender and now 3D artists are getting rep](https://x.com/polydao/status/2060311186546065552) |
| x | 3DxDEV7 | ^90 c0 | [Procedural leather sandals built entirely with geometry nodes in Blender by 3D a](https://x.com/3DxDEV7/status/2060277202214674661) |
| x | DSkaale | ^79 c2 | [🚀 SplatBox now runs 2M+ Gaussian splats — with real-time relighting — on a stand](https://x.com/DSkaale/status/2060476211193655419) |
| x | chasescooper | ^76 c3 | [We have some exciting stuff in Unreal 5.8 - Skeletonize and weight complex meshe](https://x.com/chasescooper/status/2060737891408515270) |
| x | jettelly | ^63 c1 | [Developer Sapra shared how the spline-based road system works in their tool, Inf](https://x.com/jettelly/status/2060360513335549985) |
| x | Creality3dP | ^48 c7 | [Pika is Coming. Your first portable 3D scanning companion. For many people, 3D s](https://x.com/Creality3dP/status/2060276880138461651) |
| x | Rustledust77 | ^34 c1 | [Texturing workflow for our @FracturedRTS units: -&gt; Assign trim sheet material](https://x.com/Rustledust77/status/2060279247491465611) |
| x | sidefx | ^29 c1 | [@keen_tools has released the Open Beta of GeoTracker for Houdini, a fully integr](https://x.com/sidefx/status/2060519060899782737) |
| x | bilawalsidhu | ^27 c0 | [i went deep on where 3DGS goes next with the two people who'd know -- brian mccl](https://x.com/bilawalsidhu/status/2060520050742702503) |
| x | LumaLabsAI | ^25 c5 | [The conversation was great. Now make sure the promo stops people in their tracks](https://x.com/LumaLabsAI/status/2060406509578981568) |
| x | RadianceFields | ^23 c1 | [gaussian splatting is coming to 1,700 Australian suburbs this summer. The CoStar](https://x.com/RadianceFields/status/2060415724665946412) |
| x | LumaLabsAI | ^18 c3 | [The blog post did the thinking. Now let the promo do the work. Drop in the conte](https://x.com/LumaLabsAI/status/2060461313713909783) |
| x | bilawalsidhu | ^16 c0 | [Omni's take on rendering the camera path, then the *actual* earth studio render ](https://x.com/bilawalsidhu/status/2060886445770870905) |
| x | bilawalsidhu | ^5 c1 | [@AIDSfinder Most of these are aerial capture platforms - multi camera oblique im](https://x.com/bilawalsidhu/status/2060556756611113164) |
| x | bilawalsidhu | ^5 c0 | [@seungwoo0197 Very cool](https://x.com/bilawalsidhu/status/2060481731019362494) |
| x | bilawalsidhu | ^5 c1 | [@lexsicarium "She can relax right there" :-)](https://x.com/bilawalsidhu/status/2060373513966399642) |
| x | MeshyAI | ^3 c0 | [🥳 It's just the beginning — share your feedback, every reply shapes what we ship](https://x.com/MeshyAI/status/2060311516092760293) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PXJOSHIMA</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2989 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PXJOSHIMA/status/2060601157240881492">View @PXJOSHIMA on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In 2024 I was approached on IG by someone from a games design studio about making them a replica of the ROK body armour, they wanted it in a plain colour because it's easier for them to 3D scan and th”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ช่างทำ prop เล่าว่าถูก games studio ว่าจ้างให้สร้างชุดเกราะ ROK สีพื้นเพื่อ 3D scan แล้วใส่ camo texture ทีหลัง แต่ดูเหมือน studio ยกเลิกไป</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PXJOSHIMA/status/2060601157240881492" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Nyaonyx09</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2509 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Nyaonyx09/status/2060277804470862196">View @Nyaonyx09 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Welcome back.... Animations by me using Blender. Credits : Models : Hoyoverse BG : 克里斯提亚娜 Shader : StellarToon #Danmarch #Phaistelle https://t.co/LWgrGJgG7j”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist @Nyaonyx09 โพสต์ fan animation ทำด้วย Blender โดยใช้ model จาก Hoyoverse และ shader ชื่อ StellarToon พร้อม credit เจ้าของ asset</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Nyaonyx09/status/2060277804470862196" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@broskyxn</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1556 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/broskyxn/status/2060730034584015072">View @broskyxn on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year still getting advantage of pitches, now everyone's playing against us, God jii, be kind to us one more time this season. htt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคริกเก็ตโพสต์บ่นเรื่องความไม่ยุติธรรมของสนามแข่ง — คำว่า 'Unreal rigging' ในที่นี้หมายถึงการล็อกผลแข่ง ไม่ใช่ rigging ใน 3D</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/broskyxn/status/2060730034584015072" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 679 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2060518632547877359">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i like big splats and i cannot lie. you can now compress, tile and stream city scale 3d gaussian splats -- glTF has an official 3DGS extension now too. this is what the future of google earth looks li”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>glTF ออก extension อย่างเป็นทางการสำหรับ 3D Gaussian Splats แล้ว รองรับ compress, tile และ stream ฉาก 3DGS ระดับเมืองใน toolchain มาตรฐาน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>glTF extension ทำให้ asset 3DGS ใช้กับ pipeline มาตรฐาน (Unity, web, XR) ได้โดยไม่ต้อง custom loader — สภาพแวดล้อม photorealistic จาก scan ใช้งานจริงได้แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ glTF 3DGS extension ใน Unity หรือ WebXR prototype เพื่อเทียบ streaming quality กับ mesh asset ปกติในงาน environment และ XR scene</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2060518632547877359" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 221 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Sean Gause แชร์ node graph ครบชุดของ rain drip shader ใน Unity HDRP อธิบาย mask map channel (metal, AO, detail, smoothness) และบอกว่า port ไป Unreal ได้ไม่ยาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Node setup rain drip ใน Unity HDRP พร้อมใช้ฟรี ตรงกับงาน environment art ที่ปกติต้องลองผิดลองถูกเยอะ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity เอา node graph นี้ใส่ project HDRP ที่ต้องการ wet-surface หรือ rain effect ได้เลยโดยไม่ต้องสร้างใหม่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EdwardUrena_h</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 195 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EdwardUrena_h/status/2060338391380619716">View @EdwardUrena_h on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“With this tool as a foundation, you will be able to bake the cloth physics onto the bones, allowing you to transfer it to game engines. #blender #b3d #rig #rigging #animation @BlenderDev @Blender http”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Tool ใน Blender สำหรับ bake cloth physics simulation ลงบน bone ทำให้ export cloth animation เข้า game engine อย่าง Unity ได้โดยตรง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cloth physics แบบ runtime ใน Unity กินทรัพยากรสูง การ bake ลง bone ช่วยให้ Unity team ได้ cloth animation สำเร็จรูปโดยไม่มี overhead</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง tool นี้กับ character ที่มี cloth ใน Blender แล้วตรวจสอบว่า baked bone animation export เข้า Unity pipeline ของ studio ได้ปกติ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EdwardUrena_h/status/2060338391380619716" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 176 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2060373038982459741">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Larus went ham with this one! Love the synced highlighting on the camera path, something I wanted to try myself. Makes me think these could end up as spatial reasoning benchmarks for ai video models, ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Larus สร้าง 3D camera-path animation พร้อม synchronized highlighting; ผู้โพสต์แนะนำว่า dataset 3D ของเมืองใช้เป็น ground-truth benchmark ประเมิน spatial reasoning ของ AI video model ได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Synchronized camera-path highlighting เป็นเทคนิค previsualization ที่ใช้ได้จริงกับงาน XR scene layout และ cinematic tooling ใน Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง prototype camera-path highlight visualizer เป็น scene-layout tool ในโปรเจกต์ XR หรือ cinematic ถัดไปได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2060373038982459741" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AckroseEdits</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 154 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AckroseEdits/status/2060352963986530678">View @AckroseEdits on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Vfx highlights from @StanBrowney's Fitness Island video 🏝️ -Premiere pro + After Effects -Higgsfield AI -Blender https://t.co/FleURGsWbG”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>VFX creator โชว์ breakdown เอฟเฟกต์จากวิดีโอ YouTube ฟิตเนส ใช้ Premiere Pro, After Effects, Higgsfield AI, และ Blender</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Higgsfield AI + Blender ใน production จริงเป็นตัวอย่าง hybrid workflow ที่ทีมเล็กทำ cinematic content ได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดลอง Higgsfield AI ร่วมกับ Blender pipeline ที่มีอยู่ สำหรับ XR trailer หรือ e-learning video</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AckroseEdits/status/2060352963986530678" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
