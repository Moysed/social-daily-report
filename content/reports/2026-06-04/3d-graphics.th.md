---
type: social-topic-report
date: '2026-06-04'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-04T03:41:42+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 43
salience: 0.62
sentiment: positive
confidence: 0.58
tags:
- gaussian-splatting
- photogrammetry
- blender
- shaders
- ai-asset-generation
- xr-pipeline
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2061575218749943808/img/_SuSRfmf6GjLa7q2.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-04

## TL;DR
- SuperSplat (ฟรี, open source) สตรีม Gaussian scan ขนาด 24 ล้าน Gaussian ไปยัง web browser แบบ live พร้อม load เกือบทันที [3] — สัญญาณชัดที่สุดว่า Gaussian Splatting กำลังมุ่งสู่การส่งมอบผ่าน web/XR
- ความก้าวหน้าด้าน Gaussian Splatting หลายชิ้นมาพร้อมกัน: HiGS hierarchical real-time rendering [20], FreeStreamGS online feed-forward splatting จาก unposed streaming inputs [31], TripoSplat image-to-3D ที่ปรับจำนวน Gaussian ได้ [32] และ real-estate pre-construction walkthrough ที่สร้างจริง [12]
- Unity tooling ฟรีในเครื่องมือ: VFX Texture Lab ทำ mask cleanup, gradient mapping และ channel packing โดยไม่ต้องออกจาก Unity [4]
- Photogrammetry พัฒนาต่อเนื่อง — pipeline scan-to-game-asset ผ่าน decimation/re-UV/bake [2] และ KIRI Engine's Featureless Object Scan Mode สำหรับพื้นผิวมัน/ไม่มีรายละเอียด [14] — พร้อมเสียงบ่นว่า photogrammetry ทำให้เกมพองไปถึง 130GB [8]
- Unreal Engine 5.8 เพิ่ม Niagara memory และ speed optimizations สำหรับ real-time VFX simulations ขนาดใหญ่ขึ้น [11]; AI asset generators (Meshy สร้างเมืองสไตล์คอนซิสเทนต์ [22], one-prompt 3D world agent [28]) ยังโพสต์ demo ต่อเนื่อง

## What happened
เส้นเรื่องหลักคือ 3D Gaussian Splatting SuperSplat แสดง scan ขนาด 24M Gaussian สตรีมไปยัง browser แบบ live พร้อม load เกือบทันที [3], นักพัฒนา real-estate สร้างโปรเจกต์ใหม่เป็น pre-construction splat walkthrough [12] และงานวิจัยมาพร้อมกัน: HiGS สำหรับ hierarchical real-time rendering [20], FreeStreamGS สำหรับ online feed-forward splatting จาก unposed streaming inputs [31] และ TripoSplat สำหรับ controllable single-image-to-3D Gaussians [32] นอกจากนี้ยังมีการพูดเรื่อง splatting ที่ Techweek [30] แยกออกมา เทรนด์ AI camera-path/trajectory ได้รับความสนใจแพร่หลาย [1][9]

## Why it matters (reasoning)
สำหรับสตูดิโอที่ ship Unity games และ XR/VR demo web-streaming splat [3] สำคัญเพราะชี้ทางสู่การ deliver สภาพแวดล้อมที่ถ่ายมาผ่าน browser แทนที่ native build ขนาดหนัก — เกี่ยวข้องทั้งกับ XR portfolio และ web/mobile delivery และ real-estate walkthrough [12] คือต้นแบบเชิงพาณิชย์ที่จับต้องได้ กลุ่มงานวิจัย splatting [20][31][32] บ่งชี้ว่าทั้ง capture และ rendering ดีขึ้นพร้อมกัน ลดต้นทุนการแปลง scene จริงเป็น navigable assets ในฝั่ง production เครื่องมือฟรีในเครื่องมือ (VFX Texture Lab [4]) และ photogrammetry refinements [2][14] ลด asset cleanup เชิงมือ ขณะที่เสียงบ่น 130GB [8] คือต้นทุนลำดับสองที่จริง: รายละเอียดจาก scan ทำให้ build size พองขึ้น กระทบ mobile และ web targets และบังคับให้มีวินัยด้าน decimation/baking [2] AI asset generators [22][28][32] สัญญาความเร็วแต่รายการเหล่านี้ยังเป็น demo ที่ยังไม่พิสูจน์ใน production

## Possibility
**มีโอกาสสูง:** Gaussian Splatting เดินหน้าสู่ XR/visualization ผ่าน web delivery เนื่องจากมี 24M-Gaussian browser stream ที่ใช้งานได้จริง [3], real-estate case ที่ ship แล้ว [12] และงานวิจัยที่บรรจบกัน [20][31] **เป็นไปได้:** image/prompt-to-3D (TripoSplat [32], Meshy [22], one-prompt world agent [28]) ใช้งานได้จริงสำหรับ greyboxing และ background props แต่ control และ quality ยังพิสูจน์ไม่ได้จาก demo เพียงอย่างเดียว **เป็นไปได้:** แรงกดเรื่อง build size ดัน team ไปสู่ leaner, baked photogrammetry pipelines แทน raw scans [2][8] **ไม่น่าจะเกิดขึ้นจากหลักฐานนี้:** AI 3D agents แทนงาน authored environment ในระยะใกล้ — claim อย่าง "entire worlds from one prompt" [28] ยังไม่ได้รับการพิสูจน์ เป็นแค่ marketing

## Org applicability — NDF DEV
1) ประเมิน SuperSplat สำหรับ demo XR/visualization แบบ browser — ฟรี open source และสตรีม scan ขนาดใหญ่ไปยัง web ได้แล้ว [3][12] (effort: med) 2) เพิ่ม VFX Texture Lab เข้า Unity pipeline สำหรับงาน mask/channel-pack/gradient ในเครื่องมือ [4] (effort: low) 3) ใช้ scan-to-game-asset routine (decimation, UV ใหม่, bake) เป็น standard เพื่อควบคุม build size สำหรับ mobile/web ตอบโจทย์ปัญหา 130GB โดยตรง [2][8] (effort: med) 4) ทดลอง KIRI Featureless Object Scan Mode สำหรับ prop ที่มัน/ไม่มีรายละเอียดและ photogrammetry ทั่วไปล้มเหลว [14] (effort: low) 5) สำหรับ VR avatars เส้นทาง VRoid+Blender พร้อม 52 ARKit blendshapes และ Perfect Sync คือ reference ที่พร้อมใช้ [26] (effort: med) **ข้ามไปก่อน:** Unreal 5.8 Niagara changes ถ้ายังไม่มี Unreal project ที่ active [11]; การถกเถียง generative media ใน film [18][35][16][23]; Apple U1/spatial-anchor speculation [15][29] — น่าสนใจแต่ยังไม่ actionable วันนี้ ถือ one-prompt 3D world claims [28] เป็น demo ไม่ใช่ฐานตัดสินใจจัดซื้อ

## Signals to Watch
- SuperSplat-style web splat streaming จะได้ export/runtime path ที่ stable เข้า Unity หรือ WebGL viewers หรือไม่ [3]
- TripoSplat และ image-to-3D tools ที่คล้ายกันผลิต topology ที่ clean และ riggable แทน raw Gaussians ได้หรือไม่ [32]
- คุณภาพ featureless-object scanning ของ KIRI บน production props [14]
- แรงกดเรื่อง build size ที่กำหนดงบประมาณ texture/resolution ใน scanned-asset pipelines [2][8]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^4284 c67 | [Well that escalated quickly 😂 Insane camera path generation harry! https://t.co/](https://x.com/bilawalsidhu/status/2061886480847450588) |
| x | JasozzGames | ^981 c9 | [I'm really addicted to this 3D-scan-to-game-ready-asset pipeline! Just a few rou](https://x.com/JasozzGames/status/2062165225588089172) |
| x | playcanvas | ^526 c17 | [🚀 Major upgrades just landed in SuperSplat, the free and open source platform fo](https://x.com/playcanvas/status/2062165374120894862) |
| x | jettelly | ^332 c0 | [Technical Artist Ken Deng released VFX Texture Lab, a free Unity tool that lets ](https://x.com/jettelly/status/2061749670075150362) |
| x | TOAnimate_ | ^259 c1 | [Little tip that might save you: Don't skip the basics if you don't want everythi](https://x.com/TOAnimate_/status/2061810071927923134) |
| x | jettelly | ^230 c1 | [Developer jakubiee made this simple head shader for Unreal Engine 5, experimenti](https://x.com/jettelly/status/2062081858154750016) |
| x | VFX_Therapy | ^208 c2 | [Amazing procedurally generated real-time cloud shader created by @HugoChenin. #u](https://x.com/VFX_Therapy/status/2062231883384258909) |
| x | TheVicious_One | ^208 c20 | [Hot take incoming: Photogrammetry is why games are 130GB We don't need to see la](https://x.com/TheVicious_One/status/2062204594185228557) |
| x | AIWarper | ^194 c19 | [Fun fact - I started this entire trend after seeing a fantastic post by @bilawal](https://x.com/AIWarper/status/2061884417757544600) |
| x | SD_F111 | ^176 c6 | [Niko N model update!! 3D work/rigging is done now to clean up weights and UV! Ni](https://x.com/SD_F111/status/2061918040850121207) |
| x | RedefineFX | ^170 c3 | [Unreal Engine 5.8 brings memory and speed optimizations for Niagara, allowing fo](https://x.com/RedefineFX/status/2062144965472313446) |
| x | AurelienCa80656 | ^135 c7 | [A real estate project recreated in Gaussian Splatting. Future buyers can freely ](https://x.com/AurelienCa80656/status/2062053609102008532) |
| x | K_enzo1 | ^104 c6 | [Practice VFX/Anim: Me Port: https://t.co/xnTwH5Im8S #RobloxDev #robloxvfx #MoonA](https://x.com/K_enzo1/status/2061964402270597596) |
| x | KIRI_Engine_App | ^101 c2 | [Featureless objects break most photogrammetry pipelines. Glossy, monochrome, no ](https://x.com/KIRI_Engine_App/status/2062089405741854822) |
| x | mweinbach | ^83 c6 | [I keep thinking about Apple's U1 chip and the idea of understanding 3D space wit](https://x.com/mweinbach/status/2062255347608236229) |
| x | FourBeats265635 | ^81 c2 | [@YottaMindset @mnolangray "Closely connected" seems like a real stretch. Being a](https://x.com/FourBeats265635/status/2061669439620215273) |
| x | cgboost | ^80 c0 | [Learn how Martin Klekner made this sequence in Blender on our YouTube Channel. h](https://x.com/cgboost/status/2061748624178999569) |
| x | bilawalsidhu | ^79 c12 | [I see videos like this and get excited… it's the old guard embracing new tech. T](https://x.com/bilawalsidhu/status/2061811752786944074) |
| x | FlippedNormals | ^70 c0 | [This stylized water shader by Casey Sheep is included in our new Blender Add-Ons](https://x.com/FlippedNormals/status/2061810123350106393) |
| x | janusch_patas | ^53 c2 | [HiGS: A Hierarchical Rendering Architecture for Real-Time 3D Gaussian Splatting ](https://x.com/janusch_patas/status/2062064390136795517) |
| x | multimodalart | ^52 c5 | [Ideogram 4 not only revamped their model to the best they built yet, but also th](https://x.com/multimodalart/status/2062210597148930139) |
| x | MeshyAI | ^44 c4 | [Build a 3D tiny town, block by block. Meshy keeps the style consistent across as](https://x.com/MeshyAI/status/2062121498207563920) |
| x | Rahll | ^40 c2 | [I agree with your general sentiment, but to be clear, a lot of what you're descr](https://x.com/Rahll/status/2062272983499260229) |
| x | ushadersbible | ^38 c1 | [This outline technique is achieved using reflection. What's the difference? For ](https://x.com/ushadersbible/status/2061663479300296851) |
| x | cghow_ | ^37 c0 | [Shadow Binding Curse in Unreal Engine 5 Niagara https://t.co/MNIt02YoVO https://](https://x.com/cghow_/status/2061808463727239678) |
| x | kariha_moon5 | ^35 c0 | [Made in VRoid Studio x Blender. Includes: ✧ 5 default expressions ✧ Jacket toggl](https://x.com/kariha_moon5/status/2061812031339319493) |
| x | 3DxDEV7 | ^32 c0 | [Take a look at this 👀 A procedural robot character creator for Blender with pres](https://x.com/3DxDEV7/status/2062247832321417594) |
| x | heyrobinai | ^32 c6 | [NO WAY THIS 3D AGENT BUILDS ENTIRE WORLDS FROM ONE PROMPT.. 3D environment build](https://x.com/heyrobinai/status/2061840822656499739) |
| x | mweinbach | ^29 c2 | [You can then extend to an ecosystem. If you want to know where your AirTags are ](https://x.com/mweinbach/status/2062255381645074904) |
| x | RadianceFields | ^24 c0 | [I'm doing a talk tomorrow for @Techweek_ about gaussian splatting. Come by if yo](https://x.com/RadianceFields/status/2061663277893972082) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4284 · 💬 67</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061886480847450588">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Well that escalated quickly 😂 Insane camera path generation harry! https://t.co/ML4I0e2J6m”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@bilawalsidhu รีแอคต่อ demo 3D ที่แสดงการสร้าง camera path อัตโนมัติที่โดดเด่น ตัวโพสต์ไม่ระบุ tool แต่ได้ 4k+ likes จากชุมชน 3D graphics</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Camera path automation เกี่ยวตรงกับ Unity cutscene tooling, in-engine cinematics, และ XR flythrough — engagement สูงบ่งชี้ว่า demo น่าดู</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เปิดลิงก์แล้วดูว่า technique นี้เข้ากับ Unity หรือ XR pipeline ได้ไหม ก่อนตัดสินใจ evaluate tool ต่อ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061886480847450588" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@JasozzGames</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 981 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/JasozzGames/status/2062165225588089172">View @JasozzGames on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm really addicted to this 3D-scan-to-game-ready-asset pipeline! Just a few rounds of decimation, new UVs, and then bake the details #gamedev #blender https://t.co/bAmx8JlHlM”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาแชร์ workflow จาก 3D scan ไปเป็น game-ready asset ใน Blender: decimation → UV ใหม่ → bake detail ได้ asset จากของจริงที่ optimised แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Pipeline นี้ลดเวลา model prop และ environment แบบ manual ตรงกับงาน Unity และ XR ที่ต้องการ real-world geometry ที่ poly count ต่ำ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ลอง pipeline นี้กับ prop สแกนจริงสักชิ้น แล้วเทียบเวลากับการ model เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/JasozzGames/status/2062165225588089172" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@playcanvas</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 526 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/playcanvas/status/2062165374120894862">View @playcanvas on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚀 Major upgrades just landed in SuperSplat, the free and open source platform for 3D Gaussian splatting. Here is a 24-MILLION-Gaussian scan streaming live to a web browser. Near instant load time. Sol”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>SuperSplat อัปเกรด renderer เป็น WebGPU แบบ compute-based พร้อม LOD streaming อัตโนมัติ — render ฉาก 24 ล้าน Gaussian ที่ 60 fps ใน browser โหลดเร็วเกือบทันที</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Gaussian splatting ที่ 60 fps ใน browser ผ่าน WebGPU เปิดทางให้ทำ environment 3D สมจริงสำหรับงาน web XR หรือ e-learning โดยไม่ต้องพึ่ง native plugin</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดลอง capture ฉาก 3D ผ่าน SuperSplat WebGPU renderer ดูว่าเข้ากับ pipeline web XR หรือ e-learning ของ studio ได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/playcanvas/status/2062165374120894862" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 332 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2061749670075150362">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Technical Artist Ken Deng released VFX Texture Lab, a free Unity tool that lets artists make common texture edits, like mask cleanup, gradient mapping, and channel packing, without leaving the engine.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Ken Deng ปล่อย VFX Texture Lab ฟรี — Unity Editor tool สำหรับแก้ texture ในเครื่องมือเดียว: mask cleanup, gradient mapping, channel packing ไม่ต้องออกจาก engine</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัด round-trip ไป Photoshop/Substance ออกได้ — ทีม Unity ที่ทำ real-time VFX หรืองาน stylized ได้ประโยชน์ตรงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง install VFX Texture Lab แล้วทดสอบกับ workflow texture ปัจจุบัน — ดูว่าตัดขั้นตอน external tool ออกได้แค่ไหน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2061749670075150362" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TOAnimate_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 259 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TOAnimate_/status/2061810071927923134">View @TOAnimate_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Little tip that might save you: Don’t skip the basics if you don’t want everything to feel confusing later 😹 Learn the basics so your rigs don’t break later #toanimate #rigging #blender https://t.co/I”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@TOAnimate_ โพสต์ tip เรื่อง rigging ใน Blender เตือนว่าถ้าข้าม fundamental ไป rig จะพังทีหลัง พร้อมวิดีโอประกอบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เกี่ยวกับทีมที่ทำ character ใน Blender ก่อน export เข้า Unity หรือ XR — rig พังทำให้เสียเวลา pipeline</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">แชร์คลิปนี้ใน art channel ให้ junior 3D artist ที่ทำ rigged asset ดูเป็น reference</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TOAnimate_/status/2061810071927923134" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 230 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2062081858154750016">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer jakubiee made this simple head shader for Unreal Engine 5, experimenting with ambient occlusion to create more interesting facial shading. 🎭 See more: https://t.co/3GacKh8pFn #UnrealEngine #”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer jakubiee สร้าง head shader ใน Unreal Engine 5 โดยใช้ ambient occlusion เพื่อให้การแรเงาใบหน้าดีกว่า material ค่าเริ่มต้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัวอย่างจริงที่แสดงว่าแค่ปรับ AO ใน shader ก็ทำให้ character face rendering ดีขึ้นชัดเจน — ใช้ได้กับงาน UE5 character โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดู shader breakdown ที่ลิงก์แล้วทดสอบแนวทาง ambient occlusion แบบเดียวกันกับ character face ในโปรเจกต์ปัจจุบันหรือที่กำลังจะมา</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2062081858154750016" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 208 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2062231883384258909">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazing procedurally generated real-time cloud shader created by @HugoChenin. #unreal #gamedev https://t.co/5cVXjkgd7J”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Hugo Chenin ปล่อย real-time procedural cloud shader สำหรับ Unreal Engine พร้อมคลิปสาธิต</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Procedural cloud shader ลดการพึ่ง static skybox และเทคนิคนี้ใช้ได้กับงาน outdoor และ VR scene ใน Unity โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ดู shader architecture ของ Chenin เป็น reference ตอนทำ dynamic sky system ใน scene outdoor หรือ VR</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2062231883384258909" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheVicious_One</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 208 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheVicious_One/status/2062204594185228557">View @TheVicious_One on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hot take incoming: Photogrammetry is why games are 130GB We don't need to see laundry in 4k”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev โต้เถียงว่า photogrammetry และการสแกน asset 4K คือสาเหตุหลักที่ทำให้ขนาดเกมพุ่งถึง 130 GB</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ชี้ trade-off จริงในสาย production — asset สแกนความละเอียดสูง vs. ต้นทุน storage และ download ที่ต้องคิดตอน scope pipeline Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอน scope งาน 3D ให้กำหนด texture resolution budget ตั้งแต่ต้น และประเมินว่า photogrammetry asset ต้องทำ LOD compression ก่อน ship หรือไม่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheVicious_One/status/2062204594185228557" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
