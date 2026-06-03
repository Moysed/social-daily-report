---
type: social-topic-report
date: '2026-06-03'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-03T06:53:43+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 33
salience: 0.45
sentiment: neutral
confidence: 0.6
tags:
- blender
- unity
- shaders
- gaussian-splatting
- photogrammetry
- asset-pipeline
thumbnail: https://pbs.twimg.com/media/HJu5g4-WoAAkc5f.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-03

## TL;DR
- Blender 5.2 เพิ่ม shader option "thin wall" สำหรับ mesh ที่มีความหนาน้อยหรือไม่มีเลย เช่น ใบไม้ กระดาษ ทิชชู่ และพลาสติกบาง [1]; engagement สูงสุดของวันด้วยยอดเกือบ 45k
- Ken Deng ปล่อย VFX Texture Lab เครื่องมือ Unity ฟรีสำหรับแก้ texture ใน engine: mask cleanup, gradient mapping, channel packing [4]
- การสร้าง camera path ด้วย AI จาก photogrammetry trajectory กลายเป็น creator trend [2][7][27] ต่อเนื่องจากงาน Gaussian splatting/spatial capture [26]
- FlippedNormals "FlipBox" bundle: Blender add-on 11 ตัว + asset กว่า 1500 ชิ้น ราคา $30 เน้น environment, procedural workflows, VFX, vegetation [13][18]
- เทคนิค shader ที่แชร์: reflection-based outline ที่ไม่ต้องทำ mesh ซ้ำหรือใช้ stencil [21]; Amplify Shader Editor trailing shader สำหรับ Unity [11]

## สิ่งที่เกิดขึ้น
ฟีด 3D ของวันนี้ถูกครองด้วย Blender release note เดียว — feature "thin wall" shader ใหม่ใน Blender 5.2 สำหรับ mesh ที่มีความหนาน้อยหรือไม่มีเลย เช่น ใบไม้ กระดาษ และพลาสติกบาง [1] นอกนั้นเป็นเรื่อง tooling: Unity texture utility ฟรี (VFX Texture Lab) สำหรับ mask cleanup, gradient mapping, channel packing โดยไม่ต้องออกจาก engine [4]; FlippedNormals add-on/asset bundle ราคา $30 สำหรับงาน environment และ procedural ใน Blender [13][18]; และเทคนิค real-time shader ที่แชร์กัน (reflection-based outline [21], Amplify trailing shader [11], stylized water shader [18], UE5 Niagara VFX [22])

## ความสำคัญ
ส่วนใหญ่เป็น tooling และการแชร์เทคนิคแบบ incremental ไม่ใช่การเปลี่ยน platform แต่ส่งผลตรงต่อต้นทุนการผลิต asset Blender thin-wall shader [1] กำจัด workaround เดิม (geometry สองด้าน/manual translucency) สำหรับ foliage และ thin prop ที่ใช้หนักทั้งใน game และ XR utility ใน engine อย่าง VFX Texture Lab [4] ลด round-trip ระหว่าง Photoshop/Substance กับ Unity ทำให้ iterate texture ได้เร็วขึ้น trend photogrammetry-camera-path [2][7][27] และ talk เรื่อง Gaussian splatting [26] อยู่ในส่วน capture-to-engine pipeline: วิธีถูกกว่าในการแปลง scene จริงและ trajectory ให้เป็น 3D ที่ใช้งานได้ ซึ่งสำคัญสำหรับ XR ที่ต้องการ environment จากโลกจริง ระดับ second-order: เมื่อ capture (splatting/NeRF/photogrammetry [24][26]) และ AI camera generation พัฒนาขึ้น bottleneck จะเลื่อนจากการ model ไปสู่ cleanup, retopo, และ engine integration — ซึ่งตรงกับ manual step ที่ utility เหล่านี้มุ่งแก้อยู่พอดี

## ความเป็นไปได้
Likely: thin-wall shading และ free in-engine texture tool จะกลายเป็น standard ใน foliage/prop pipeline เพราะทั้งคู่ลด manual step ที่รู้จักกันดี [1][4] Plausible: Gaussian splatting จะเคลื่อนจาก research/demo ไปสู่ production XR capture ต่อเนื่อง เห็นได้จาก conference attention [26] และงาน photogrammetry accuracy ที่เกี่ยวเนื่อง [24] — แต่ engine-native splat rendering และ editing ยังไม่ mature ดังนั้น adoption ยังอยู่ในขั้น exploratory Plausible: AI-generated camera path จะเข้าสู่ splat/video pipeline ในฐานะ creator workflow [2][7][27] แต่ signal ส่วนใหญ่ตอนนี้เป็น hype repost ยังไม่ใช่ tool ที่ ship แล้ว ไม่มี source ระบุตัวเลข probability จึงไม่ระบุ

## ประยุกต์ใช้กับ NDF DEV
Low effort — ติดตั้งและทดลอง VFX Texture Lab สำหรับ Unity texture cleanup/channel packing ใน game project ปัจจุบัน; ฟรี [4] Low effort — ประเมิน FlippedNormals FlipBox bundle ราคา $30 สำหรับ environment/vegetation/procedural asset ถ้าช่วยเติม content gap ในระยะใกล้ [13][18]; ตรวจ license terms สำหรับ commercial use ก่อนซื้อ Low/med — ทดสอบ Blender 5.2 thin-wall shader กับ asset foliage/กระดาษ/พลาสติกบาง เพื่อเลิกใช้ double-sided-geometry [1] Med — prototype reflection-based outline [21] สำหรับ Unity title แนว stylized/toon เทียบ cost กับ inverted-hull outline Med/high (exploratory เท่านั้น) — จัด spike สั้นๆ เรื่อง Gaussian splatting สำหรับ XR environment capture โดยดู Techweek talk และติดตาม engine-import maturity ก่อนตัดสินใจลงทุน [26][24] ข้าม: tutorial rigging/character/personal [3][5][6][9][16][19][20], Amplify trailing shader ถ้าไม่ได้ license Amplify Shader Editor อยู่แล้ว [11], และ post นอกเรื่อง/novelty [25][29][33]

## Signals ที่ต้องจับตา
- Engine-native Gaussian splatting import/edit สำหรับ Unity/Unreal — ขึ้นอยู่กับความ mature ของ tooling [26][24]
- Free in-engine art utility (texture, VFX) ใน Unity ที่ลด DCC round-trip [4]
- AI camera-path/trajectory generation ที่พัฒนาจาก repost ไปสู่ creator tool จริง [2][7][27]
- Blender 5.2 shader additions (thin wall) และ fidelity การ export ไป game engine [1]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Tioaoa2 | ^45314 c92 | [Blender 5.2 has a new shader feature called "thin wall" which is designed for me](https://x.com/Tioaoa2/status/2061445532518653996) |
| x | bilawalsidhu | ^2675 c47 | [Well that escalated quickly 😂 Insane camera path generation harry! https://t.co/](https://x.com/bilawalsidhu/status/2061886480847450588) |
| x | DemNikoArt | ^596 c8 | [Bike Suspension Tutorial coming this week 😉 #b3d #blender #blender3d #rigging #t](https://x.com/DemNikoArt/status/2061498924473487814) |
| x | jettelly | ^227 c0 | [Technical Artist Ken Deng released VFX Texture Lab, a free Unity tool that lets ](https://x.com/jettelly/status/2061749670075150362) |
| x | TOAnimate_ | ^192 c0 | [Little tip that might save you: Don't skip the basics if you don't want everythi](https://x.com/TOAnimate_/status/2061810071927923134) |
| x | EdwardUrena_h | ^137 c1 | [One of the good things about this is that it allows you to display only the bone](https://x.com/EdwardUrena_h/status/2061559777575014798) |
| x | AIWarper | ^131 c12 | [Fun fact - I started this entire trend after seeing a fantastic post by @bilawal](https://x.com/AIWarper/status/2061884417757544600) |
| x | bilawalsidhu | ^123 c8 | [Honestly if we put this demo in a fancy XR headset, we'd call it jarvis. The fut](https://x.com/bilawalsidhu/status/2061450274011591084) |
| x | EdwardUrena_h | ^122 c0 | [I set out to see if it was possible to add a custom gizmo—and yes, it was; it to](https://x.com/EdwardUrena_h/status/2061539090198045116) |
| x | SD_F111 | ^111 c3 | [Niko N model update!! 3D work/rigging is done now to clean up weights and UV! Ni](https://x.com/SD_F111/status/2061918040850121207) |
| x | VFX_Therapy | ^95 c1 | [Absolute stunner: Dynamic trailing shader by @MetallCore999 in Amplify Shader Ed](https://x.com/VFX_Therapy/status/2061535622368833762) |
| x | FourBeats265635 | ^81 c2 | [@YottaMindset @mnolangray "Closely connected" seems like a real stretch. Being a](https://x.com/FourBeats265635/status/2061669439620215273) |
| x | casey_sheep | ^78 c2 | [🔥 I've partnered with @FlippedNormals to launch a special FlipBox bundle! Get 11](https://x.com/casey_sheep/status/2061482329139532174) |
| x | cgboost | ^76 c0 | [Learn how Martin Klekner made this sequence in Blender on our YouTube Channel. h](https://x.com/cgboost/status/2061748624178999569) |
| x | bilawalsidhu | ^73 c12 | [I see videos like this and get excited… it's the old guard embracing new tech. T](https://x.com/bilawalsidhu/status/2061811752786944074) |
| x | TopologicalBomb | ^63 c3 | [homelander nearly done. gotta do a bit of miscellaneous rigging and mesh joining](https://x.com/TopologicalBomb/status/2061386957444325399) |
| x | LumaLabsAI | ^62 c9 | [To improve human life, AI systems must be able to help us improve the physical w](https://x.com/LumaLabsAI/status/2061460217616027961) |
| x | FlippedNormals | ^60 c0 | [This stylized water shader by Casey Sheep is included in our new Blender Add-Ons](https://x.com/FlippedNormals/status/2061810123350106393) |
| x | Arorea | ^49 c0 | [@Sphere_Deer For Toriel I used a 3d scan of my head to 3d model a base that was ](https://x.com/Arorea/status/2061392121232249247) |
| x | K_enzo1 | ^47 c5 | [Practice VFX/Anim: Me Port: https://t.co/xnTwH5Im8S #RobloxDev #robloxvfx #MoonA](https://x.com/K_enzo1/status/2061964402270597596) |
| x | ushadersbible | ^38 c1 | [This outline technique is achieved using reflection. What's the difference? For ](https://x.com/ushadersbible/status/2061663479300296851) |
| x | cghow_ | ^30 c0 | [Shadow Binding Curse in Unreal Engine 5 Niagara https://t.co/MNIt02YoVO https://](https://x.com/cghow_/status/2061808463727239678) |
| x | Gwamothy | ^24 c2 | [@agraybee You're telling me that you have devices that can, from a handheld devi](https://x.com/Gwamothy/status/2061541531094532147) |
| x | RemoteSens_MDPI | ^23 c1 | [Improving the Accuracy of #Forest #Structure Analysis by Consumer-Grade #UAV #Ph](https://x.com/RemoteSens_MDPI/status/2061442845597225332) |
| x | SoapIsTasty00 | ^21 c1 | [@passcoderonald Everyone should have to upload a 3D scan of their penis, both er](https://x.com/SoapIsTasty00/status/2061668092028346788) |
| x | RadianceFields | ^21 c0 | [I'm doing a talk tomorrow for @Techweek_ about gaussian splatting. Come by if yo](https://x.com/RadianceFields/status/2061663277893972082) |
| x | bilawalsidhu | ^8 c1 | [@kvickart This feels like an emergent behavior, but now that they know it I woul](https://x.com/bilawalsidhu/status/2061888185433461074) |
| x | bilawalsidhu | ^8 c0 | [@bfl_ai https://t.co/RvIs1vBT9s](https://x.com/bilawalsidhu/status/2061850142148313145) |
| x | bilawalsidhu | ^7 c0 | [@LKaci2721 Lol, these models are so smart yet sooo dumb](https://x.com/bilawalsidhu/status/2061974433347104800) |
| x | bilawalsidhu | ^6 c0 | [@xxunhuang @AlbyHojel Officially official; congrats Xun and team!](https://x.com/bilawalsidhu/status/2061971021465350525) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Tioaoa2</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 45314 · 💬 92</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Tioaoa2/status/2061445532518653996">View @Tioaoa2 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Blender 5.2 has a new shader feature called &quot;thin wall&quot; which is designed for meshes which have no thickness (or very little). These can be anything from leaves, paper, tissues and some thin plastics ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Blender 5.2 เพิ่ม shader node 'Thin Wall' สำหรับ mesh ไม่มีความหนา เช่น ใบไม้ กระดาษ พลาสติกบาง render สมจริงขึ้นโดยไม่ต้องเพิ่ม geometry</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>3D artist สร้าง asset เกมหรือ XR ใน Blender render ใบไม้ กระดาษ และผ้าได้สมจริงขึ้น ไม่ต้องใช้ double-sided mesh hack</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">3D artist ในทีมลอง Thin Wall กับ asset ใบไม้และวัสดุบาง เพื่อลด geometry complexity โดยคุณภาพ render ยังได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Tioaoa2/status/2061445532518653996" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2675 · 💬 47</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061886480847450588">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Well that escalated quickly 😂 Insane camera path generation harry! https://t.co/ML4I0e2J6m”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google Gemini Omni (พ.ค. 2026) แปลง sketch เส้น camera path ที่วาดบนรูปภาพหรือ map ให้เป็น drone POV video ได้เลย demo โดย Bilawal Sidhu อดีต engineer XR ของ Google</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Sketch camera path แล้วได้ previz video เลย ลดเวลาทำ XR fly-through และ game cinematic โดยไม่ต้อง setup 3D ก่อน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง Gemini Omni Flash โดย sketch camera path บน concept art หรือ reference ภาพสถานที่ แล้วใช้เป็น previz สำหรับงาน XR และ game cinematic</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061886480847450588" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DemNikoArt</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 596 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DemNikoArt/status/2061498924473487814">View @DemNikoArt on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bike Suspension Tutorial coming this week 😉 #b3d #blender #blender3d #rigging #tutorial https://t.co/XekTbKmhOc”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@DemNikoArt จะปล่อย tutorial การ rig suspension จักรยานใน Blender สัปดาห์นี้ ครอบคลุม mechanical rigging แบบ constraint-based สำหรับ vehicle asset</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค rig suspension แบบกลไกใน Blender ใช้ได้โดยตรงกับการสร้าง vehicle และ prop asset สำหรับ Unity และโปรเจกต์ XR/VR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR บุ๊กมาร์ก tutorial นี้ไว้เพื่อเพิ่มทักษะ mechanical rigging สำหรับ vehicle asset แบบ animated</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DemNikoArt/status/2061498924473487814" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 227 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2061749670075150362">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Technical Artist Ken Deng released VFX Texture Lab, a free Unity tool that lets artists make common texture edits, like mask cleanup, gradient mapping, and channel packing, without leaving the engine.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Ken Deng ปล่อย VFX Texture Lab ฟรี — tool ใน Unity Editor สำหรับทำ mask cleanup, gradient mapping, channel packing โดยไม่ต้องออกจาก engine</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ลด round-trip ระหว่าง Unity กับ external tools อย่าง Photoshop หรือ Substance ตอน iterate VFX texture</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลองเพิ่ม VFX Texture Lab เข้า workflow VFX/shader แล้วทดสอบกับ task particle art หรือ environment art ถัดไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2061749670075150362" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TOAnimate_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 192 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TOAnimate_/status/2061810071927923134">View @TOAnimate_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Little tip that might save you: Don’t skip the basics if you don’t want everything to feel confusing later 😹 Learn the basics so your rigs don’t break later #toanimate #rigging #blender https://t.co/I”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@TOAnimate_ โพสต์เตือนทั่วไปให้เรียน Blender rigging พื้นฐานก่อน ไม่มีเทคนิคหรือ resource ใดระบุไว้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TOAnimate_/status/2061810071927923134" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EdwardUrena_h</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 137 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EdwardUrena_h/status/2061559777575014798">View @EdwardUrena_h on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One of the good things about this is that it allows you to display only the bones you want. #blender #b3d #rig #rigging #animation https://t.co/9vlBmIQChg”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>เทคนิค Blender rig แสดงเฉพาะ bone ที่ต้องการ ช่วยให้ animator โฟกัสเฉพาะส่วนที่กำลังทำงานอยู่ได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ซ่อน bone ที่ไม่ต้องการลด clutter ใน rig ซับซ้อน ทำให้ animate character ก่อน export เข้า Unity เร็วขึ้น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม 3D ใช้ bone visibility ใน Blender แยก facial หรือ limb rig ตอนเตรียม character ก่อน import เข้า Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EdwardUrena_h/status/2061559777575014798" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AIWarper</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 131 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AIWarper/status/2061884417757544600">View @AIWarper on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fun fact - I started this entire trend after seeing a fantastic post by @bilawalsidhu using photogrammetry camera trajectories Now look at how far it’s gone 😂”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@AIWarper อ้างว่าตัวเองเป็นคนจุดกระแส AI generation ที่ใช้ camera trajectory แบบ photogrammetry ต่อยอดจากโพสต์ของ @bilawalsidhu</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AIWarper/status/2061884417757544600" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 123 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061450274011591084">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Honestly if we put this demo in a fancy XR headset, we’d call it jarvis. The future of 3d doesn’t involve the death of autocad, maya and blender. It turns those tools into a shared canvas of collabora”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา @bilawalsidhu มองว่า AI agents จะไม่ฆ่า AutoCAD, Maya, หรือ Blender แต่จะเปลี่ยนให้กลายเป็น canvas ร่วมที่ทำงานกับ AI ได้ โดยอ้างอิงจาก demo ที่เขาบอกว่าใส่ XR headset แล้วจะเรียกว่า Jarvis</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สำหรับทีม XR/VR และ Unity การมอง AI agents เป็นตัวเร่ง pipeline ภายใน tools เดิมอย่าง Blender/Maya ตรงกับทิศทางที่ studio ใช้อยู่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม AI agent plugins สำหรับ Blender และ Maya ที่กำลังออกมา แล้วทดลองใช้กับ XR asset งานเล็กๆ เพื่อวัดผลจริงก่อนนำมาใช้ใน pipeline หลัก</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061450274011591084" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
