---
type: social-topic-report
date: '2026-05-30'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-05-30T18:42:27+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 38
salience: 0.7
sentiment: positive
confidence: 0.6
tags:
- gaussian-splatting
- blender
- xr-pipeline
- procedural
- ai-3d-tools
- unity-unreal
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060157376410402819/img/rppvxJmTxDY9hS9X.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-05-30

## TL;DR
- glTF มี extension อย่างเป็นทางการสำหรับ 3D Gaussian Splatting แล้ว รองรับ splat ระดับเมืองที่สามารถบีบอัด, แบ่ง tile, และ stream ได้ [5][27]
- SplatBox รัน Gaussian splats กว่า 2M splat พร้อม real-time relighting บน Quest 3 แบบ standalone ไม่ต้องใช้สาย [18]
- Meshy เปิดตัว 'Meshy 3D Agent' รุ่น beta — agent ที่ใช้ chat สำหรับระดมไอเดีย, สร้าง 3D asset แบบ batch, และปรับแต่งผลลัพธ์ [10][38]
- tooling สำหรับ pipeline Blender→engine ก้าวหน้า: cloth physics bake ลงบน bone เพื่อส่งไป engine [7][11], workflow ของ trim-sheet/Substance/Unity shader [23], และ Unreal 5.8 เพิ่ม dataflow skeletonize + Control Rig Dynamics แบบ experimental [24]
- CoStar กำลัง deploy Gaussian Splatting reconstruction ครอบคลุม 1,700 ย่านทั่วออสเตรเลีย [29]; เครื่องมือสร้างโลก Unity แบบ procedural (Infinite Lands splines, Voronoi islands) ยังพัฒนาต่อเนื่อง [17][21]

## สิ่งที่เกิดขึ้น
สัญญาณที่ชัดเจนที่สุดของวันนี้คือ Gaussian Splatting กำลังเติบโตจาก research demo ไปสู่ production format อย่างจริงจัง glTF ได้รับ extension อย่างเป็นทางการสำหรับ 3DGS และ splat สามารถบีบอัด, แบ่ง tile, และ stream ได้ในระดับเมือง [5] โดยมีการสนทนาเพิ่มเติมกับ Brian McClendon จาก Niantic Spatial และ Neil Trevett ประธาน Khronos [27] SplatBox แสดงให้เห็นว่า splat กว่า 2M จุดพร้อม real-time relighting ทำงานได้บน Quest 3 แบบ standalone [18], CoStar deploy การ reconstruct ระดับย่านทั่ว 1,700 พื้นที่ในออสเตรเลีย [29], และงานจาก CVPR 2026 มุ่งเป้าที่การปรับ pose ภายใต้ความไม่แน่นอนทางเรขาคณิต [16] ในด้าน AI-driven 3D authoring: Meshy ประกาศ '3D Agent' ระบบ chat-based ในรุ่น beta [10][38] และมีโพสต์อ้างว่าเชื่อม Claude Opus 4.8 เข้ากับ Blender เพื่อสร้าง animation จาก prompt [12]

## ความสำคัญ (เหตุผล)
มีสองเส้นทางที่สำคัญต่อ studio แรกคือ splat standardization: extension อย่างเป็นทางการของ glTF [5] บวกกับ on-device playback บน Quest 3 พร้อม relighting [18] ทำให้ 3DGS เปลี่ยนจาก capture แบบ one-off ไปสู่ asset type ที่เข้า pipeline ของ engine/XR ที่มีอยู่ได้ real-time relighting [18] แก้จุดอ่อนหลักของ splat สำหรับ interactive XR ที่แสงถูก bake ไว้ตายตัวและพังเมื่อ scene เปลี่ยนแปลง ผลต่อเนื่องคือ photogrammetry และการ capture (portable scanner [20], aerial oblique imagery [35], GeoTracker matchmove ใน Houdini [26]) ช่วย feed pipeline นี้ ลดต้นทุนการสร้าง content สำหรับ location-based และ digital twin เส้นทางที่สองคือ production tooling ที่ลดแรงงานด้วยมือ: procedural geometry nodes [15], Unity spline/Voronoi world generator [17][21], และ workflow ของ Blender-to-engine สำหรับ physics/texture [7][11][23][24] การอ้างถึง AI agent [10][12] ชี้ไปในทิศทางเดียวกัน แต่อิงกับประกาศจากผู้ขายและ hype ที่ยังไม่ผ่านการวัดผล ไม่ใช่ผลลัพธ์จริง

## ความเป็นไปได้
น่าจะเกิด: 3DGS จะกลายเป็น XR asset format มาตรฐานภายในปีหน้า จาก glTF extension และ Quest 3 playback ที่ใช้งานได้จริง [5][18][27] — มีหน่วยงานมาตรฐานรองรับ ไม่ใช่แค่ demo ชิ้นเดียว เป็นไปได้: AI 3D agent อย่าง Meshy [10] จะมีประโยชน์สำหรับ blockout และ ideation แต่ไม่ถึงขั้น final game-ready asset เพราะหลักฐานยังเป็นแค่ประกาศ beta และ topology ยังมีความสำคัญ (การวิจารณ์ low-poly ใน [19] แสดงว่า artist ยังตัดสินคุณภาพ mesh อยู่) ไม่น่าเกิดในระยะสั้น: การอ้างว่า complex animation อัตโนมัติเต็มรูปแบบและ senior artist ถูก 'แทนที่' [12] — นั่นเป็นโพสต์ hype ที่ไม่มี workflow ที่ reproduce ได้แสดงให้เห็น AI short film มูลค่า $5,000 [14] เป็นการรายงานตัวเองและไม่ใช่การเปรียบเทียบที่ควบคุมตัวแปร

## ประโยชน์ต่อองค์กร — NDF DEV
1) รัน 3DGS test แบบ scoped สำหรับ portfolio XR/VR: capture สถานที่ขนาดเล็ก, export ผ่าน glTF 3DGS extension, และทดสอบ playback บน Quest 3 (effort ระดับกลาง) [5][18][27] 2) ประเมิน Blender cloth-bake-to-bones tool สำหรับงาน character ที่จะส่งไป Unity เพราะมุ่งเป้าที่ขั้นตอนส่งไป engine โดยตรง [7][11] (ต่ำ-กลาง) 3) นำ workflow ของ trim-sheet → Substance → Unity shader texturing มาใช้เป็นมาตรฐาน document ไว้สำหรับ game unit [23] (ต่ำ) 4) ทดลอง Meshy 3D Agent เฉพาะสำหรับ blockout/ideation ระยะต้น ไม่ใช่ final asset และกำหนด time-box ไว้ [10][38] (ต่ำ) 5) ติดตาม Unreal 5.8 Control Rig Dynamics หากโปรเจกต์ใดใช้ Unreal สำหรับ foliage/complex rig [24] (ต่ำ, monitor เท่านั้น) ข้าม: narrative ว่า AI แทนที่ artist [12] และ cost claim ของ AI short film [14] — ไม่มี workflow ที่ verified และ actionable ละเว้นโพสต์เกี่ยวกับ firearms/off-topic [1][22][32][34] ทั้งหมด

## สัญญาณที่ควรติดตาม
- glTF 3DGS extension จะถูก adopt โดย Unity/Unreal importer หรือแค่ viewer [5][27]
- คุณภาพ real-time relighting และ performance headroom ของ splat บน standalone headset เมื่อ scene ขยายเกิน 2M [18]
- topology ของ output จาก Meshy 3D Agent และว่า beta ผลิต mesh ที่พร้อมสำหรับ engine หรือต้องการ cleanup มาก [10][19][38]
- portable/consumer scanning (Pika, Creality) ที่ลดต้นทุนการ capture สำหรับ asset photogrammetry [20]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^3306 c116 | [bro putting a belt fed machine gun on a monitor arm is probably the most america](https://x.com/bilawalsidhu/status/2060157431057994021) |
| x | Nyaonyx09 | ^2428 c11 | [Welcome back.... Animations by me using Blender. Credits : Models : Hoyoverse BG](https://x.com/Nyaonyx09/status/2060277804470862196) |
| x | PXJOSHIMA | ^2426 c9 | [In 2024 I was approached on IG by someone from a games design studio about makin](https://x.com/PXJOSHIMA/status/2060601157240881492) |
| x | broskyxn | ^1341 c9 | [@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year stil](https://x.com/broskyxn/status/2060730034584015072) |
| x | bilawalsidhu | ^628 c22 | [i like big splats and i cannot lie. you can now compress, tile and stream city s](https://x.com/bilawalsidhu/status/2060518632547877359) |
| x | RyanLykos | ^547 c3 | [Zhu Yuan textures... Finally complete! It's been a long journey so far but i'm f](https://x.com/RyanLykos/status/2060136495319597136) |
| x | EdwardUrena_h | ^180 c2 | [With this tool as a foundation, you will be able to bake the cloth physics onto ](https://x.com/EdwardUrena_h/status/2060338391380619716) |
| x | bilawalsidhu | ^166 c6 | [Larus went ham with this one! Love the synced highlighting on the camera path, s](https://x.com/bilawalsidhu/status/2060373038982459741) |
| x | AckroseEdits | ^145 c16 | [Vfx highlights from @StanBrowney's Fitness Island video 🏝️ -Premiere pro + After](https://x.com/AckroseEdits/status/2060352963986530678) |
| x | MeshyAI | ^116 c9 | [Introducing Meshy 3D Agent 🚀 The world's first AI agent for 3D creation, now in ](https://x.com/MeshyAI/status/2060311322123014560) |
| x | EdwardUrena_h | ^100 c0 | [One of the advantages of this is that you can design your own control system for](https://x.com/EdwardUrena_h/status/2060397763632701921) |
| x | polydao | ^96 c18 | [This guy connected Claude Opus 4.8 to Blender and now 3D artists are getting rep](https://x.com/polydao/status/2060311186546065552) |
| x | mattworkman | ^90 c18 | [I once OFFENDED the mentor that hand picked me up from the gutter and sat me at ](https://x.com/mattworkman/status/2060573070151078006) |
| x | ZohaibAi__sf | ^89 c26 | [Day 5. It's finished. 20,000 credits. ~$5,000. A global story. VFX. Costumes. Wi](https://x.com/ZohaibAi__sf/status/2060670680329511122) |
| x | 3DxDEV7 | ^87 c0 | [Procedural leather sandals built entirely with geometry nodes in Blender by 3D a](https://x.com/3DxDEV7/status/2060277202214674661) |
| x | rsasaki0109 | ^72 c1 | [[CVPR 2026] Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior](https://x.com/rsasaki0109/status/2060194429286138037) |
| x | jettelly | ^60 c1 | [Developer Sapra shared how the spline-based road system works in their tool, Inf](https://x.com/jettelly/status/2060360513335549985) |
| x | DSkaale | ^55 c2 | [🚀 SplatBox now runs 2M+ Gaussian splats — with real-time relighting — on a stand](https://x.com/DSkaale/status/2060476211193655419) |
| x | TsukinoYueVT | ^49 c4 | [@SignaIbat9 @Kimagure31415 I'd accept the argument if it were a proper sculpture](https://x.com/TsukinoYueVT/status/2060093810936258772) |
| x | Creality3dP | ^47 c6 | [Pika is Coming. Your first portable 3D scanning companion. For many people, 3D s](https://x.com/Creality3dP/status/2060276880138461651) |
| x | unity3dvfx | ^43 c0 | [This is so clean 🔥by @GbrosGames Procedural island generation with Voronoi grids](https://x.com/unity3dvfx/status/2060093851675541880) |
| x | bilawalsidhu | ^36 c3 | [@SmileyGnome That's when you pull out your sig rattler from the center console 🙃](https://x.com/bilawalsidhu/status/2060193419838771234) |
| x | Rustledust77 | ^34 c1 | [Texturing workflow for our @FracturedRTS units: -&gt; Assign trim sheet material](https://x.com/Rustledust77/status/2060279247491465611) |
| x | chasescooper | ^33 c2 | [We have some exciting stuff in Unreal 5.8 - Skeletonize and weight complex meshe](https://x.com/chasescooper/status/2060737891408515270) |
| x | LumaLabsAI | ^30 c6 | [BTS: Career Finder First the characters, then the scenes, then the shots — every](https://x.com/LumaLabsAI/status/2060081566651711841) |
| x | sidefx | ^27 c1 | [@keen_tools has released the Open Beta of GeoTracker for Houdini, a fully integr](https://x.com/sidefx/status/2060519060899782737) |
| x | bilawalsidhu | ^26 c0 | [i went deep on where 3DGS goes next with the two people who'd know -- brian mccl](https://x.com/bilawalsidhu/status/2060520050742702503) |
| x | LumaLabsAI | ^24 c5 | [The conversation was great. Now make sure the promo stops people in their tracks](https://x.com/LumaLabsAI/status/2060406509578981568) |
| x | RadianceFields | ^23 c1 | [gaussian splatting is coming to 1,700 Australian suburbs this summer. The CoStar](https://x.com/RadianceFields/status/2060415724665946412) |
| x | LumaLabsAI | ^17 c3 | [The blog post did the thinking. Now let the promo do the work. Drop in the conte](https://x.com/LumaLabsAI/status/2060461313713909783) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3306 · 💬 116</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2060157431057994021">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“bro putting a belt fed machine gun on a monitor arm is probably the most america thing i've seen all week. shout out eric pettway. https://t.co/03UR7DVW9o”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ไวรัลแสดงคนติดปืนกล belt-fed บน monitor arm เป็น joke เชิงวัฒนธรรม ไม่มีเนื้อหาด้านเทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2060157431057994021" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Nyaonyx09</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2428 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Nyaonyx09/status/2060277804470862196">View @Nyaonyx09 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Welcome back.... Animations by me using Blender. Credits : Models : Hoyoverse BG : 克里斯提亚娜 Shader : StellarToon #Danmarch #Phaistelle https://t.co/LWgrGJgG7j”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist อิสระปล่อยคลิป animation ทำใน Blender ใช้ StellarToon shader แบบ NPR กับโมเดล HoYoverse ผลลัพธ์คุณภาพ toon rendering ระดับ production ด้วย tool ฟรี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>StellarToon เป็น Blender shader สำหรับ NPR แบบ anime ที่ใช้งานจริงได้ — เป็น reference ที่ดีสำหรับ art pipeline Blender-to-Unity สไตล์ toon</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ StellarToon ใน Blender สำหรับงาน asset baking หรือ pre-render สไตล์ toon ก่อน import เข้า Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Nyaonyx09/status/2060277804470862196" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PXJOSHIMA</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2426 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PXJOSHIMA/status/2060601157240881492">View @PXJOSHIMA on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In 2024 I was approached on IG by someone from a games design studio about making them a replica of the ROK body armour, they wanted it in a plain colour because it's easier for them to 3D scan and th”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ช่างทำ prop เล่าว่าปี 2024 มี game studio ติดต่อให้ทำชุดเกราะ ROK สีพื้น เพื่อนำไปสแกน 3D แล้วใส่ลาย camo ทีหลัง — สุดท้ายดูเหมือนโปรเจกต์ไม่ไปต่อ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า studio จริงใช้ prop สีพื้นเป็น scan target แล้วใส่ texture ทีหลัง — เป็น pipeline จริง ไม่ใช่แค่ทฤษฎี</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PXJOSHIMA/status/2060601157240881492" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@broskyxn</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1341 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/broskyxn/status/2060730034584015072">View @broskyxn on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year still getting advantage of pitches, now everyone's playing against us, God jii, be kind to us one more time this season. htt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคริกเกตบ่นเรื่องความไม่ยุติธรรมในการแข่งขันและขอพรให้ทีมชนะ — คำว่า 'Unreal' ในที่นี้เป็น slang ไม่ใช่ Unreal Engine</dd>
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
    <span class="ndf-engagement">♥ 628 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2060518632547877359">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i like big splats and i cannot lie. you can now compress, tile and stream city scale 3d gaussian splats -- glTF has an official 3DGS extension now too. this is what the future of google earth looks li”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>glTF ได้ extension 3D Gaussian Splat อย่างเป็นทางการแล้ว พร้อมรองรับ compress, tile และ stream ฉาก 3DGS ระดับเมืองได้จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>glTF extension มาตรฐานทำให้ Unity และ web runtime โหลด splat scene photorealistic ได้โดยตรง — ตรงกับงาน XR และ location-based ของทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ลอง import ฉากผ่าน glTF 3DGS extension ใน Unity เพื่อประเมินว่าใช้แทน traditional 3D asset ในงาน XR ได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2060518632547877359" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 547 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2060136495319597136">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Zhu Yuan textures... Finally complete! It's been a long journey so far but i'm finally at my favourite part! I can't wait to dive into rigging and animation. Gonna be awesome😁 Feedback appreciated! (I”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist เดี่ยวแชร์ความคืบหน้างาน texture ตัวละคร Zhu Yuan ใน Blender (fan art จาก Zenless Zone Zero) ก่อนเข้าสู่ขั้น rigging และ animation</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2060136495319597136" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EdwardUrena_h</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 180 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EdwardUrena_h/status/2060338391380619716">View @EdwardUrena_h on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“With this tool as a foundation, you will be able to bake the cloth physics onto the bones, allowing you to transfer it to game engines. #blender #b3d #rig #rigging #animation @BlenderDev @Blender http”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Tool ใน Blender ช่วย bake cloth physics simulation ลง bone เปลี่ยนเป็น bone animation ที่ game engine นำเข้าได้ตามปกติ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cloth sim ส่งออกไป Unity ตรงๆ ไม่ได้ การ bake ลง bone แก้ทั้งปัญหา compatibility และ runtime cost พร้อมกัน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง workflow นี้กับ character asset ที่ตอนนี้ใช้ rigid cloth แทน cloth sim จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EdwardUrena_h/status/2060338391380619716" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 166 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2060373038982459741">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Larus went ham with this one! Love the synced highlighting on the camera path, something I wanted to try myself. Makes me think these could end up as spatial reasoning benchmarks for ai video models, ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Larus สร้าง visualization เส้นทางกล้องใน 3D city พร้อม highlight แบบ sync; ผู้โพสต์ตั้งข้อสังเกตว่าวิดีโอแบบนี้อาจใช้เป็น spatial reasoning benchmark สำหรับ AI video model โดยมีข้อมูล 3D เมืองจริงเป็น ground truth</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>pattern camera-path + synced highlight ตรงกับงาน fly-through และ shot-sequence review ใน XR/VR บน Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลอง prototype camera-path highlight overlay ใน Unity ใช้ visualize shot sequence ตอน pre-production review</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2060373038982459741" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
