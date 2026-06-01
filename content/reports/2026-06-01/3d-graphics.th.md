---
type: social-topic-report
date: '2026-06-01'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-01T04:14:06+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 18
salience: 0.35
sentiment: neutral
confidence: 0.5
tags:
- gaussian-splatting
- unreal-engine
- shaders
- blender
- xr-pipeline
- photogrammetry
thumbnail: https://pbs.twimg.com/media/HJi506gbMAAFWVc.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-01

## TL;DR
- Unreal Engine 5.8 เพิ่ม skeletonization/weighting แบบ dataflow สำหรับ mesh ซับซ้อน (เช่น ต้นไม้) และ plugin Control Rig Dynamics แบบ experimental สำหรับ sim-rigging [11]
- Gaussian Splatting กำลังเดินจาก demo สู่ deploy ได้จริง: creator รายหนึ่งรัน splat scene บน Quest 3 แบบ standalone VR พร้อม multi-renderer ordering แบบกำหนดเอง (render-order key + depth tiebreak, view-space distance) เพื่อแก้ splat sorting [13]
- ความรู้ shader ข้าม engine กำลังถูกแชร์เปิดเผย — rain-drip shader node graph ที่ระบุว่า port ไป Unreal ได้โดยตรง โดยความต่างของ Unity HDRP อยู่ที่การจัดการ mask [4]
- Three.js Water Pro สร้าง real-time water ที่สมจริงด้วย setup น้อยกว่า hand-built Blender shader-node lighting มาก ตามที่ creator เปรียบเทียบไว้ [15]
- item engagement สูงส่วนใหญ่เป็น showcase ของ artist รายบุคคล (snow shader [3], ripped game model [9], geometry-node VFX [7]) ไม่ใช่การปล่อย tool — สัญญาณวันนี้กระจาย

## What happened
item 3D/graphics วันนี้ถูกครอบงำด้วย post จาก creator รายบุคคลบน X มากกว่าประกาศจาก vendor ข่าว tooling ที่ชัดที่สุดคือ Unreal 5.8 ที่เปิดตัว skeletonization และ mesh-weighting ผ่าน dataflow พร้อม plugin Control Rig Dynamics แบบ experimental [11] Gaussian Splatting ปรากฏสองครั้งอย่างมีสาระ: ในฐานะวิธีจับภาพพื้นที่/สถานที่จากรูปสองสามร้อยใบ [5] และในฐานะ pipeline standalone-VR ที่ใช้งานได้จริงบน Quest 3 ที่แก้ splat draw-ordering ด้วย render-order key, depth tiebreak และ view-space distance [13] Shader และงาน procedural กำลังถูกแชร์เปิดเผย: rain-drip node setup พร้อมโน้ต porting สำหรับ Unreal/Unity HDRP [4], Blender snow shader [3], geometry-node black-hole VFX ที่วางแผน port ไป Unreal [7] และงาน particle/geonodes ของ Blender [8]

## Why it matters (reasoning)
สำหรับ asset pipeline ที่ป้อน Unity และ Unreal มีสองเรื่องสำคัญ แรกคือ Gaussian Splatting กำลังก้าวเข้าสู่ runtime XR: [13] แสดงให้เห็นว่าส่วนที่ยากไม่ใช่การจับภาพอีกต่อไป แต่คือการ integrate renderer และ splat sorting ที่ถูกต้องบน standalone headset ที่มี resource จำกัด — ตรงกับงาน XR บน Quest class โดยตรง สองคือ post shader [4][15] ยืนยันว่า real-time engine shader และ web stack (Three.js) สามารถทำคุณภาพที่เคยต้องใช้ Blender แบบ offline ได้แล้ว และ node graph ถ่ายโอนข้าม engine ได้มากขึ้นพร้อมข้อควรระวังเฉพาะ engine ที่รู้อยู่แล้ว (HDRP masking) [4] rigging/skeletonization tool ของ Unreal 5.8 [11] ลดแรงงานในการเตรียม organic mesh และ mesh ซับซ้อน ซึ่งเป็นส่วนที่แพงที่สุดในการเตรียม asset de-aging scan workflow [17] และ prop สีพื้นเหมาะกับ scan [1] เตือนว่าคุณภาพ photogrammetry ยังขึ้นกับสภาพการถ่ายและ cleanup ด้วยมือเป็นหลัก ไม่ใช่แค่ software

## Possibility
น่าจะเกิด: Gaussian Splatting ยังคงพัฒนาเป็น path จากจับภาพถึง runtime สำหรับ XR เพราะ standalone-VR integration ที่ใช้งานได้จริงพร้อมวิธีแก้ sorting เป็นรูปธรรมมีอยู่แล้ว [13][5] พอเป็นไปได้: เทคนิค shader/VFX ถูกปล่อยในรูป cross-engine-portable node graph พร้อมความต่างเฉพาะ engine ที่บันทึกไว้ ทำให้ใช้ความรู้ซ้ำข้าม Unity/Unreal/Three.js ง่ายขึ้น [4][15] พอเป็นไปได้: rigging feature ของ Unreal 5.8 ([11], ระบุว่า experimental) เสถียรในรุ่นถัดไป แต่ตอนนี้ควรถือว่ายังไม่เสถียร ไม่น่าจะเกิด (ไม่มีหลักฐาน): tool หรือมาตรฐานเดียวที่รวม workflow เหล่านี้ — สัญญาณวันนี้กระจายอยู่ใน creator รายบุคคล

## Org applicability — NDF DEV
รัน Gaussian Splatting test แบบ scoped สำหรับการจับภาพ XR location/environment และ validate splat sorting บน Quest 3 โดยเฉพาะ โดยใช้วิธี ordering ที่อธิบายไว้ (render-order key + depth tiebreak + view-space distance) (effort: med) [13][5] บันทึก rain-drip shader node setup ที่แชร์เปิดเผยเป็น reference และโน้ตความต่าง Unity HDRP mask ไว้ใน shader library ของทีม (effort: low) [4] ประเมิน Three.js Water Pro สำหรับ experience บน web/mobile ที่ต้องการ real-time water ก่อนสร้าง Blender shader เอง (effort: low) [15] ทดลอง Unreal 5.8 skeletonize/weighting และ Control Rig Dynamics กับ organic asset ซับซ้อน แต่อย่าใส่ใน production path ขณะยัง experimental (effort: med) [11] สำหรับ prop photogrammetry ใช้แนวทาง plain-color, scan-friendly เพื่อลด cleanup (effort: low) [1][17] ข้าม item engagement สูงที่ไม่เกี่ยว (cricket [2], AI short-film budget claim [10], VFX career anecdote [12]) — ไม่มีคุณค่า tooling

## Signals to Watch
- Gaussian Splatting renderer ordering บน Quest 3 standalone-VR — ติดตามว่าวิธีแก้ sorting ที่ใช้ซ้ำได้จะถูกแพ็กเกจหรือไม่ [13]
- Unreal 5.8 Control Rig Dynamics และ dataflow skeletonization ที่จะเคลื่อนจาก experimental ไปสู่ stable [11]
- Cross-engine portability ของ shader node graph พร้อมความต่าง HDRP/Unreal ที่บันทึกไว้ [4]
- คุณภาพ Three.js real-time water เทียบกับ Blender แบบ offline สำหรับงาน web/mobile [15]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | PXJOSHIMA | ^3163 c12 | [In 2024 I was approached on IG by someone from a games design studio about makin](https://x.com/PXJOSHIMA/status/2060601157240881492) |
| x | broskyxn | ^1668 c13 | [@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year stil](https://x.com/broskyxn/status/2060730034584015072) |
| x | AnimGaby | ^939 c12 | [D4DJ as Murder drones some parts are off sync because daVinci is trolling me Som](https://x.com/AnimGaby/status/2061071305634627949) |
| x | sean_gause | ^841 c5 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | bilawalsidhu | ^447 c21 | [We treat 3d scanning like a tech demo, but it's actually spatial memory capture.](https://x.com/bilawalsidhu/status/2061134940813611505) |
| x | VFX_Therapy | ^340 c3 | [When your Unreal VFX project hits different… @IgorPontes breakdown his Sasuke-le](https://x.com/VFX_Therapy/status/2061109917222920517) |
| x | ashlee3dee | ^203 c1 | [stylized black hole vfx with geometry nodes :3 i will port this to unreal engine](https://x.com/ashlee3dee/status/2061195779952275511) |
| x | lightarchitect_ | ^190 c1 | [I just love particle systems in Blender. Ok I know its not even close to Houdini](https://x.com/lightarchitect_/status/2060838278505648401) |
| x | A_fan_of_Sonic | ^160 c3 | [Ripped, fixed and shaded Vegeta from Sparking Zero for Blender • Move eyes in sh](https://x.com/A_fan_of_Sonic/status/2060749070554001630) |
| x | ZohaibAi__sf | ^130 c37 | [Day 5. It's finished. 20,000 credits. ~$5,000. A global story. VFX. Costumes. Wi](https://x.com/ZohaibAi__sf/status/2060670680329511122) |
| x | chasescooper | ^126 c3 | [We have some exciting stuff in Unreal 5.8 - Skeletonize and weight complex meshe](https://x.com/chasescooper/status/2060737891408515270) |
| x | mattworkman | ^105 c19 | [I once OFFENDED the mentor that hand picked me up from the gutter and sat me at ](https://x.com/mattworkman/status/2060573070151078006) |
| x | DSkaale | ^98 c4 | [Just stepped inside my favorite movie locations on my Quest 3 🎬 Gaussian splatti](https://x.com/DSkaale/status/2061114844263117118) |
| x | bilawalsidhu | ^74 c3 | [Fucking cool. Giving AR portal vibes - like watching volumetric video with full ](https://x.com/bilawalsidhu/status/2060943911363690875) |
| x | SteveWarnerFL | ^38 c6 | [Why is Three.js Water Pro able to do this level of realism in real time but I st](https://x.com/SteveWarnerFL/status/2060800324911222931) |
| x | bilawalsidhu | ^36 c0 | [Omni's take on rendering the camera path, then the *actual* earth studio render ](https://x.com/bilawalsidhu/status/2060886445770870905) |
| x | anishmoonka | ^24 c1 | [To build a young Arnold, the crew scanned an older one. They took a full-body 3D](https://x.com/anishmoonka/status/2061192494449152390) |
| x | MeshyAI | ^1 c0 | [@niftyisland 😍 This is soooooo cool 😍](https://x.com/MeshyAI/status/2061246669040369797) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PXJOSHIMA</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3163 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PXJOSHIMA/status/2060601157240881492">View @PXJOSHIMA on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In 2024 I was approached on IG by someone from a games design studio about making them a replica of the ROK body armour, they wanted it in a plain colour because it's easier for them to 3D scan and th”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ช่างทำ prop เล่าว่าเคยรับงาน game studio ปี 2024 ให้สร้าง ROK body armour จริงสีทึบเพื่อ 3D scan แต่สุดท้ายไม่มีการติดต่อกลับ</dd>
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
    <span class="ndf-author">@broskyxn</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1668 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/broskyxn/status/2060730034584015072">View @broskyxn on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year still getting advantage of pitches, now everyone's playing against us, God jii, be kind to us one more time this season. htt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์บ่นเรื่องสภาพสนามคริกเก็ตที่รู้สึกว่าเอื้อประโยชน์ให้ทีมตรงข้าม — คำว่า 'Unreal' ในที่นี้คือสำนวนกีฬา ไม่ใช่ Unreal Engine</dd>
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
    <span class="ndf-author">@AnimGaby</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 939 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnimGaby/status/2061071305634627949">View @AnimGaby on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“D4DJ as Murder drones some parts are off sync because daVinci is trolling me Some part I didn't include the background character because It will just destroy my blender lol anyways snow shader by @Ash”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แอนิเมเตอร์สาย fan art โพสต์งาน crossover D4DJ × Murder Drones ทำใน Blender + DaVinci Resolve โดยตัด background character ออกเพราะ Blender รับไม่ไหว และใช้ snow shader จาก @Ashkap50</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AnimGaby/status/2061071305634627949" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 841 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@sean_gause แชร์ node graph ครบชุดสำหรับ rain drip shader ใน Unity HDRP โดย mask map ใช้ channel metal/AO/detail/smooth และ port ไป Unreal ได้โดยแก้นิดเดียว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Shader wet-surface จาก production ที่แชร์ฟรีนี้ให้ starting point ที่ verified สำหรับ environment ใน Unity project โดยไม่ต้องสร้างใหม่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team เอา node graph นี้ใส่ HDRP scene ได้เลย แล้วปรับ mask map channel ให้ตรงกับ texture pipeline ของ project</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 447 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061134940813611505">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We treat 3d scanning like a tech demo, but it’s actually spatial memory capture. Damn near teleportation. A few hundred photos of my parent’s old home, and now it’s immortalized forever. 3d gaussian s”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาถ่ายภาพบ้านหลายร้อยรูป แล้วประมวลผลผ่าน RealityCapture + Lichtfeld ได้ผลลัพธ์เป็น 3D Gaussian Splat — แสดงให้เห็น pipeline photogrammetry-to-splat ที่ทำได้จริงโดยไม่ซับซ้อน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Pipeline RealityCapture → Lichtfeld ใช้งานได้จริงสำหรับ capture environment จริง เหมาะกับงาน XR/VR scene reconstruction โดยไม่ต้องพึ่ง LiDAR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลอง workflow นี้ — RealityCapture + Lichtfeld — capture พื้นที่จริงเป็น Gaussian Splat แล้วทดสอบ import เข้า Unity XR</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061134940813611505" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 340 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2061109917222920517">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“When your Unreal VFX project hits different… @IgorPontes breakdown his Sasuke-level Katon 🔥 with insane stylized effects. #vfx https://t.co/j4wFOeAnBm”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@IgorPontes ปล่อย breakdown ของ stylized fire VFX สไตล์อนิเมะที่สร้างใน Unreal Engine โดย @VFX_Therapy แชร์ต่อบน X</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Technique การทำ stylized elemental VFX ใน breakdown นี้นำมาปรับใช้กับ particle work สไตล์อนิเมะใน Unity ได้ตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู breakdown แล้วดึง technique การ layer stylized fire มาทำใหม่ใน Unity VFX Graph หรือ Shader Graph</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2061109917222920517" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ashlee3dee</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 203 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ashlee3dee/status/2061195779952275511">View @ashlee3dee on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“stylized black hole vfx with geometry nodes :3 i will port this to unreal engine... soon https://t.co/bu98xUEYuO”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist @ashlee3dee สร้าง stylized black hole VFX ใน Blender ด้วย geometry nodes และวางแผนจะ port ไป Unreal Engine</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Geometry nodes VFX เป็น workflow ที่ transfer ได้ — logic เดียวกันใช้ทำ stylized space/portal effect ใน Unity VFX Graph ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เอา geometry nodes setup นี้เป็น reference ตอน Unity team ต้องทำ stylized singularity หรือ portal shader สำหรับ XR scene</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ashlee3dee/status/2061195779952275511" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@lightarchitect_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 190 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/lightarchitect_/status/2060838278505648401">View @lightarchitect_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I just love particle systems in Blender. Ok I know its not even close to Houdini but still you'd be amazed what you can do. And now with Geonodes as well there is even more! Blender Mega Add-on Bundle”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปิน Blender โปรโมต paid add-on bundle พร้อมชมความสามารถ particle systems และ Geometry Nodes ว่าใช้ได้แม้จะสู้ Houdini ไม่ได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/lightarchitect_/status/2060838278505648401" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
