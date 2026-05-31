---
type: social-topic-report
date: '2026-05-31'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-05-31T16:14:35+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 21
salience: 0.55
sentiment: positive
confidence: 0.6
tags:
- gaussian-splatting
- gltf
- xr
- blender
- unreal
- shaders
thumbnail: https://pbs.twimg.com/media/HJi506gbMAAFWVc.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-05-31

## TL;DR
- glTF มี extension อย่างเป็นทางการสำหรับ 3D Gaussian Splatting แล้ว และ city-scale 3DGS สามารถบีบอัด แบ่ง tile และ stream ได้ [3][16]
- SplatBox รัน Gaussian splats กว่า 2M+ พร้อม real-time relighting บน Quest 3 แบบ standalone ไม่ต้องต่อสาย [9]
- CoStar Group กำลัง rollout การ reconstruct ด้วย Gaussian Splatting ครอบคลุม 1,700 ย่านในออสเตรเลีย โดยใช้ aerial oblique multi-camera platform [17][20]
- เนื้อหา shader/rig เชิงปฏิบัติหมุนเวียน: node setup สำหรับ rain-drip ที่พกพาได้จาก Blender→Unreal/Unity HDRP [4] และ Unreal 5.8 เพิ่ม dataflow skeletonization พร้อม Control Rig Dynamics แบบ experimental [10]
- KeenTools ปล่อย open beta ของ GeoTracker matchmove (object/camera tracking) ใน Houdini แบบ native [15]

## สิ่งที่เกิดขึ้น
กระแสหลักคือ Gaussian Splatting กำลังพัฒนาเป็น format มาตรฐานที่ stream ได้ Khronos เพิ่ม 3DGS extension อย่างเป็นทางการใน glTF รองรับการบีบอัด tiling และ streaming ของ splat ระดับ city-scale [3] พร้อมพูดคุยเพิ่มเติมกับ Neil Trevett ประธาน Khronos และ Brian McClendon CTO ของ Niantic Spatial [16] ฝั่ง runtime SplatBox สาธิต splats 2M+ พร้อม real-time relighting บน Quest 3 แบบ standalone [9] และ CoStar Group กำลัง deploy splat reconstruction ระดับย่านเมืองใน 1,700 พื้นที่ของออสเตรเลียจากภาพ oblique ทางอากาศ [17][20] รายการเครื่องมืออื่น: node graph สำหรับ rain-drip shader ที่พอร์ตจาก Blender ไป Unreal และ Unity HDRP ได้ โดยมี mask-map difference เป็นข้อแตกต่าง [4]; Unreal 5.8 dataflow skeletonization สำหรับ mesh ซับซ้อน เช่น ต้นไม้ พร้อม Control Rig Dynamics plugin แบบ experimental [10]; KeenTools GeoTracker matchmove open beta สำหรับ Houdini [15]; และ workflow Blender particle/geonodes กับ rigging [8][12]

## เหตุใดจึงสำคัญ
การมาตรฐานหน่วย (glTF 3DGS) บวกกับ relighting บน standalone VR [9] ผลักดัน splat จากการเป็น research demo ไปสู่ asset format ที่ engine pipeline นำไปใช้และ stream ต่อได้ ซึ่งสำคัญมากสำหรับ XR ที่การโมเดล environment แบบ photoreal ด้วยมือมีต้นทุนสูง [3][16] การ relighting บนอุปกรณ์ [9] แก้ปัญหาคอขวดหลักของ splat ในงาน production นั่นคือแสงที่ bake ตายตัวไม่โต้ตอบกับ scene การ capture ระดับย่านเมืองผ่าน aerial platform [17][20] ส่งสัญญาณว่าคอขวดกำลังเลื่อนจากการ capture ไปสู่ delivery และการ integration ผลลัพธ์ระดับที่สอง: สตูดิโออาจเลือก capture-and-stream แทนการโมเดล environment ด้วยมือสำหรับสถานที่จริงมากขึ้น ขณะที่ content ที่สร้างขึ้นเอง เช่น shader และ rig ยังเป็นจุดสร้างมูลค่าสำหรับงาน stylized/game [4][6] รายการ shader และ Unreal/Houdini [4][10][15] เป็นการพัฒนาแบบ incremental ไม่ใช่เชิงโครงสร้าง แต่ช่วยลด friction ใน DCC→engine pipeline ที่มีอยู่

## ความเป็นไปได้
มีแนวโน้ม: 3DGS ในฐานะ glTF-standard asset จะกลายเป็น input ที่ใช้งานได้จริงสำหรับ Unity/Unreal XR scenes ภายในปีนี้ เนื่องจากมี extension อย่างเป็นทางการและผู้สนับสนุนในฝั่ง engine [3][16] เป็นไปได้: splat ที่ relit บนอุปกรณ์จะถึง production use สำหรับ Quest-class XR แม้ว่า demo ของ SplatBox ยังเป็น claim จากผู้ขายรายเดียว ยังไม่ได้รับการยืนยันอิสระ [9] เป็นไปได้: dataset splat ตามสถานที่ (ย่านจริง) ป้อนให้ AR/spatial apps ตามรอย rollout ในออสเตรเลีย [17] ไม่น่าเกิดในระยะใกล้: splat แทนที่ mesh-based authored asset สำหรับ interactive games โดยสมบูรณ์ เนื่องจาก collision, animation, และ stylization ยังเหมาะกับ mesh มากกว่า [4][6][8] ไม่มีแหล่งข้อมูลใดระบุตัวเลขความน่าจะเป็น

## การประยุกต์ใช้กับ NDF DEV
1) ทำ spike เล็กๆ import glTF 3DGS asset เข้า Unity แล้วทดสอบบน Quest 3 สำหรับ XR scene — ประเมิน streaming และ relighting feasibility (effort: med) [3][9] 2) Capture สถานที่จริงแห่งหนึ่งด้วย photogrammetry/aerial-style oblique imagery แล้ว reconstruct เป็น splat เพื่อเปรียบเทียบกับต้นทุนการโมเดลด้วยมือสำหรับ XR pitch (effort: med) [17][20] 3) นำ rain-drip shader node pattern มาเป็น reference สำหรับงาน Blender→Unity HDRP material ที่พกพาได้ ตรวจสอบ mask-map difference ที่ระบุ (effort: low) [4] 4) เมื่อ upgrade Unreal ทดลอง 5.8 dataflow skeletonization และ Control Rig Dynamics สำหรับ vegetation/secondary motion แต่ให้ถือว่า experimental (effort: low ในการประเมิน) [10] ข้ามได้: KeenTools GeoTracker สำหรับ Houdini ยกเว้น matchmove อยู่ใน pipeline จริง [15]; Luma promo-asset agents [18][19] (เป็นงาน marketing ไม่ใช่ asset production); anecdote เกี่ยวกับ AI short film และ sports/scan [1][2][7] มี signal ต่ำ

## Signals to Watch
- Engine-native ingestion ของ glTF 3DGS ใน Unity/Unreal — จับตา first-class importer [3][16]
- การยืนยันอิสระเรื่อง standalone-Quest splat relighting performance นอกเหนือจาก claim ของ SplatBox [9]
- Location-based splat dataset ขยายเกิน 1,700 ย่านในออสเตรเลีย [17]
- Unreal 5.8 Control Rig Dynamics เลื่อนจาก experimental เป็น stable [10]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | PXJOSHIMA | ^3169 c12 | [In 2024 I was approached on IG by someone from a games design studio about makin](https://x.com/PXJOSHIMA/status/2060601157240881492) |
| x | broskyxn | ^1669 c13 | [@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year stil](https://x.com/broskyxn/status/2060730034584015072) |
| x | bilawalsidhu | ^717 c21 | [i like big splats and i cannot lie. you can now compress, tile and stream city s](https://x.com/bilawalsidhu/status/2060518632547877359) |
| x | sean_gause | ^698 c4 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | AnimGaby | ^301 c8 | [D4DJ as Murder drones some parts are off sync because daVinci is trolling me Som](https://x.com/AnimGaby/status/2061071305634627949) |
| x | A_fan_of_Sonic | ^157 c2 | [Ripped, fixed and shaded Vegeta from Sparking Zero for Blender • Move eyes in sh](https://x.com/A_fan_of_Sonic/status/2060749070554001630) |
| x | ZohaibAi__sf | ^126 c36 | [Day 5. It's finished. 20,000 credits. ~$5,000. A global story. VFX. Costumes. Wi](https://x.com/ZohaibAi__sf/status/2060670680329511122) |
| x | EdwardUrena_h | ^113 c0 | [One of the advantages of this is that you can design your own control system for](https://x.com/EdwardUrena_h/status/2060397763632701921) |
| x | DSkaale | ^108 c2 | [🚀 SplatBox now runs 2M+ Gaussian splats — with real-time relighting — on a stand](https://x.com/DSkaale/status/2060476211193655419) |
| x | chasescooper | ^104 c3 | [We have some exciting stuff in Unreal 5.8 - Skeletonize and weight complex meshe](https://x.com/chasescooper/status/2060737891408515270) |
| x | mattworkman | ^104 c19 | [I once OFFENDED the mentor that hand picked me up from the gutter and sat me at ](https://x.com/mattworkman/status/2060573070151078006) |
| x | lightarchitect_ | ^93 c1 | [I just love particle systems in Blender. Ok I know its not even close to Houdini](https://x.com/lightarchitect_/status/2060838278505648401) |
| x | bilawalsidhu | ^55 c1 | [Fucking cool. Giving AR portal vibes - like watching volumetric video with full ](https://x.com/bilawalsidhu/status/2060943911363690875) |
| x | bilawalsidhu | ^31 c0 | [Omni's take on rendering the camera path, then the *actual* earth studio render ](https://x.com/bilawalsidhu/status/2060886445770870905) |
| x | sidefx | ^31 c1 | [@keen_tools has released the Open Beta of GeoTracker for Houdini, a fully integr](https://x.com/sidefx/status/2060519060899782737) |
| x | bilawalsidhu | ^28 c0 | [i went deep on where 3DGS goes next with the two people who'd know -- brian mccl](https://x.com/bilawalsidhu/status/2060520050742702503) |
| x | RadianceFields | ^26 c1 | [gaussian splatting is coming to 1,700 Australian suburbs this summer. The CoStar](https://x.com/RadianceFields/status/2060415724665946412) |
| x | LumaLabsAI | ^25 c5 | [The conversation was great. Now make sure the promo stops people in their tracks](https://x.com/LumaLabsAI/status/2060406509578981568) |
| x | LumaLabsAI | ^19 c3 | [The blog post did the thinking. Now let the promo do the work. Drop in the conte](https://x.com/LumaLabsAI/status/2060461313713909783) |
| x | bilawalsidhu | ^5 c1 | [@AIDSfinder Most of these are aerial capture platforms - multi camera oblique im](https://x.com/bilawalsidhu/status/2060556756611113164) |
| x | bilawalsidhu | ^5 c0 | [@seungwoo0197 Very cool](https://x.com/bilawalsidhu/status/2060481731019362494) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PXJOSHIMA</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3169 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PXJOSHIMA/status/2060601157240881492">View @PXJOSHIMA on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In 2024 I was approached on IG by someone from a games design studio about making them a replica of the ROK body armour, they wanted it in a plain colour because it's easier for them to 3D scan and th”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ช่างทำ prop เล่าว่าเคยรับงานจาก game studio ให้สร้าง replica เกราะ ROK สีเรียบ เพื่อ 3D scan แล้วเติม camo texture ทีหลัง แต่ดูเหมือน studio เลิกทำไปก่อน</dd>
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
    <span class="ndf-engagement">♥ 1669 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/broskyxn/status/2060730034584015072">View @broskyxn on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year still getting advantage of pitches, now everyone's playing against us, God jii, be kind to us one more time this season. htt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคริกเก็ตบ่นว่าการแข่งขันไม่ยุติธรรม สนามเอื้อคู่แข่ง — คำว่า 'Unreal rigging' ในที่นี้แปลว่าโกง ไม่ใช่ Unreal Engine</dd>
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
    <span class="ndf-engagement">♥ 717 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2060518632547877359">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i like big splats and i cannot lie. you can now compress, tile and stream city scale 3d gaussian splats -- glTF has an official 3DGS extension now too. this is what the future of google earth looks li”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>glTF ออก extension อย่างเป็นทางการสำหรับ 3D Gaussian Splats (3DGS) รองรับ compress, tile และ stream ฉากระดับเมืองได้แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>3DGS เข้า glTF pipeline มาตรฐานแล้ว งาน XR/Unity ดึง real-world scene มาใช้ได้โดยไม่ต้องทำ custom loader</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ทดสอบ glTF 3DGS extension ใน Unity build ปัจจุบันได้เลย ประเมินว่าพร้อมใช้กับ real-world scene capture แค่ไหน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2060518632547877359" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 698 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@sean_gause แชร์ node graph ครบสำหรับ rain drip shader ใน Unity HDRP พร้อมอธิบาย mask map channels (metal, AO, detail, smooth) และวิธี port ไป Unreal Engine</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Node setup wet-surface shader สำหรับ Unity HDRP พร้อมใช้ ประหยัดเวลาทีม Unity ที่ต้องทำ rain/drip effects ในฉาก environment หรืองาน XR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เซฟ node graph นี้เป็น shader asset ใน Unity HDRP project ของ studio ไว้ใช้กับฉากที่ต้องการ rain หรือ wet-surface</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnimGaby</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 301 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnimGaby/status/2061071305634627949">View @AnimGaby on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“D4DJ as Murder drones some parts are off sync because daVinci is trolling me Some part I didn't include the background character because It will just destroy my blender lol anyways snow shader by @Ash”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@AnimGaby โพสต์ fan animation ใน Blender ผสม D4DJ กับ Murder Drones พร้อมระบุว่าตัด background character ออกเพราะทำให้ Blender crash และมีปัญหา sync ใน DaVinci Resolve</dd>
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
    <span class="ndf-author">@A_fan_of_Sonic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 157 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/A_fan_of_Sonic/status/2060749070554001630">View @A_fan_of_Sonic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ripped, fixed and shaded Vegeta from Sparking Zero for Blender • Move eyes in shader editor • Facial expressions with shapekeys Enjoy! https://t.co/ANJzYDKTMQ https://t.co/xmDuZMTEje”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักทำ 3D rip โมเดล Vegeta จาก Sparking Zero แล้ว share ไฟล์ Blender พร้อม shader ควบคุมดวงตาและ shapekey สำหรับ facial expressions</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>combo shapekey + shader eye เป็น reference ดีสำหรับทำ facial rig ใน Blender ก่อน export เข้า Unity หรือ XR pipeline</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ศึกษา pattern shader eye + shapekey สำหรับ facial rig ใน Unity/XR — ไม่ใช้ asset ที่ rip มาเพราะติด IP</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/A_fan_of_Sonic/status/2060749070554001630" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ZohaibAi__sf</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 126 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ZohaibAi__sf/status/2060670680329511122">View @ZohaibAi__sf on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Day 5. It’s finished. 20,000 credits. ~$5,000. A global story. VFX. Costumes. Wild locations. Even a full one-take sequence. At this budget… for a short film? Unreal. But here’s the truth: It wasn’t p”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้สร้างทำหนังสั้นมี VFX, ชุดแต่งกาย, หลายโลเคชันด้วย Agent One AI ใน 5 วัน งบ ~$5,000 (20k credits) โดยบอกว่า 'การกำกับ' สำคัญกว่าทักษะ prompting</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ต้นทุน $5K และ framework 'directing &gt; prompting' ตรงกับงานที่ studio ทำ ไม่ว่าจะเป็น game trailer, XR demo, หรือ e-learning video</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Agent One กับ cinematic asset ภายใน (game trailer หรือ XR promo) สักชิ้น เพื่อดู cost-per-minute จริงก่อนนำไปใช้จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ZohaibAi__sf/status/2060670680329511122" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EdwardUrena_h</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 113 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EdwardUrena_h/status/2060397763632701921">View @EdwardUrena_h on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One of the advantages of this is that you can design your own control system for the bones. #blender #animation #rig #b3d #rigging https://t.co/18WTbaG7VA”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Blender สาธิตการสร้าง control system สำหรับ bone ของ character rig เอง แสดงให้เห็นความยืดหยุ่นของการ rig แบบ manual</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ทำ character animation ใน Unity หรือ XR ใช้ custom rig control ใน Blender เพื่อให้ bone hierarchy สะอาดก่อน export</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง custom rig controller ใน Blender กับ character asset ตัวถัดไปเพื่อลดปัญหาตอน import</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EdwardUrena_h/status/2060397763632701921" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
