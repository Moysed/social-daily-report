---
type: social-topic-report
date: '2026-06-02'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-02T03:33:36+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 20
salience: 0.45
sentiment: positive
confidence: 0.5
tags:
- blender
- gaussian-splatting
- xr
- photogrammetry
- shaders
- pipeline
thumbnail: https://pbs.twimg.com/media/HJu5g4-WoAAkc5f.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-02

## TL;DR
- Blender 5.2 รายงานว่าเพิ่ม shader 'thin wall' สำหรับ mesh ที่มีความหนาน้อยหรือเป็นศูนย์ เช่น ใบไม้ กระดาษ ทิชชู และพลาสติกบาง [1] (แหล่งเดียว ถือเป็น claim ยังไม่ยืนยัน)
- Gaussian splatting รันบน Quest 3 แบบ standalone ได้แล้ว โดยผู้สร้างแก้ปัญหา renderer ด้วย render-order key + depth tiebreak และ view-space distance sorting [6]; ยังปรากฏในรูปแบบ scene/memory capture [3] และ grayscale [18]
- Photogrammetry/3D scanning ถูกใช้เป็น character base ใน production pipeline จริง — scan ร่างกายเต็มตัวแล้ว sculpt ด้วยมือสำหรับ 'young Arnold' [13] และ head scan เป็น model base [15]
- Geometry-nodes VFX (stylized black hole) กำลัง port จาก Blender→Unreal [4]; FlippedNormals bundle มี Blender add-on 11 ตัว + asset กว่า 1500 ชิ้น ราคา $30 [16]
- ส่วนใหญ่เป็น showcase และ tutorial ของผู้สร้างรายบุคคล ไม่ใช่การเปลี่ยนแปลงระดับอุตสาหกรรม; signal ของ AI 3D-gen (Luma [14], Meshy [20]) ยังคลุมเครือ

## What happened
มีรายงาน shader ใน Blender เวอร์ชัน '5.2' ชื่อ 'thin wall' สำหรับ mesh ที่มีความหนาน้อยหรือเป็นศูนย์ เช่น ใบไม้ กระดาษ ทิชชู และพลาสติกบาง [1] ซึ่งได้ engagement สูงสุดในกลุ่มนี้ แต่มีแหล่งเดียว Gaussian splatting ปรากฏซ้ำหลายครั้ง: ในรูป standalone VR บน Quest 3 พร้อมการแก้ rendering ที่เป็นรูปธรรม (multi-renderer ordering ด้วย render-order key + depth tiebreak, view-space distance sorting) [6], การ capture ฉากทั้งหมดของบ้านครอบครัวในแนวคิด spatial memory [3], ในโหมด grayscale [18] และลิงก์ 'go deeper' ทั่วไป [19] Photogrammetry ปรากฏใน pipeline จริง — scan ร่างกายเต็มตัวของ Arnold แล้ว sculpt ย้อนอายุ ~20 ปี [13] และใช้ head scan ส่วนตัวเป็น character modeling base [15]

## Why it matters (reasoning)
Signal ที่มีประโยชน์และนำไปใช้ได้จริงสำหรับ XR/games studio คือ splatting ที่รันบน standalone headset [6]: คอขวดมาโดยตลอดคือการเรียง depth ที่ถูกต้องและ performance บน mobile GPU การที่ผู้สร้างแชร์แนวทาง render-order/depth-tiebreak แบบเปิดเผยช่วยลดอุปสรรคในการ capture สถานที่จริงและดูในแบบ 6DoF บนฮาร์ดแวร์ระดับ Quest [6][3] ซึ่งตอบโจทย์ content ประเภท environment และ 'spatial memory' สำหรับทั้ง XR experience และ edutech walkthrough โดยไม่ต้องสร้าง model ด้วยมือทั้งหมด Photogrammetry-as-base-mesh [13][15] ยืนยันแนวทาง hybrid ที่ใช้ได้จริง: scan เพื่อเก็บลักษณะใบหน้า/สัดส่วน แล้วตกแต่งด้วยมือ — เชื่อมโยงกับงาน character และ avatar โดยตรง ส่วน Blender 'thin wall' [1] หากข้อมูลถูกต้องจะช่วย offline rendering ของ foliage/thin asset แต่เป็น shader ระดับ Cycles/EEVEE จึงไม่ถ่ายทอดไปยัง Unity real-time shader โดยอัตโนมัติ คุณค่าในบริบท game pipeline จึงยังไม่ชัดจนกว่าจะได้รับการยืนยัน ส่วนที่เหลือ (geometry-nodes VFX [4][5], rigging demos [7][10][11][12], asset bundles [16]) เป็น craft และ learning resource ปกติ ไม่ใช่การเปลี่ยนแปลงระดับโครงสร้าง

## Possibility
น่าจะเกิด: gaussian splatting เคลื่อนไปสู่ consumer standalone VR ต่อเนื่อง เพราะมี Quest 3 demo และ ordering technique ที่แชร์แล้ว [6][3][18] เป็นไปได้: Blender 'thin wall' shader ช่วย thin-asset offline rendering ในรุ่นที่กำลังจะมา แต่ความเทียบเท่ากับ real-time engine ยังไม่มีหลักฐานจาก item เหล่านี้ [1] เป็นไปได้แต่หลักฐานอ่อน: AI-driven 3D generation (Luma framing [14], Meshy reactions [20]) พัฒนาจนใช้งานได้ใน asset workflow — item มีความคลุมเครือเกินกว่าจะฟันธง น่าจะยังไม่เกิดระยะใกล้: splat-based asset แทนที่ modeled geometry ใน game ที่ ship แล้ว หลักฐานปัจจุบันเป็นการ capture/playback ไม่ใช่ game-ready mesh ที่ optimize แล้ว [6] ไม่มีแหล่งใดระบุความน่าจะเป็นเป็นตัวเลข

## Org applicability — NDF DEV
1) ทดสอบ prototype gaussian-splatting capture→Quest 3 playback สำหรับ XR/edutech location-walkthrough โดยใช้แนวทาง render-order key + depth tiebreak ที่อธิบายไว้ [6][3] (effort: ปานกลาง) 2) รับ scan-as-base แล้ว hand-finish มาใช้ใน character/avatar production ที่ต้องการความถูกต้องของลักษณะใบหน้า [13][15] (effort: ปานกลาง) 3) ประเมิน FlippedNormals bundle (add-on 11 ตัว + asset กว่า 1500 ชิ้น, $30) สำหรับ studio asset/environment library — ต้นทุนต่ำ ความเสี่ยงต่ำ [16] (effort: ต่ำ) 4) ติดตาม Blender 5.2 'thin wall' แต่รอยืนยันก่อนนำเข้า pipeline และตรวจสอบว่า map ไปยัง Unity real-time shader ได้หรือไม่ก่อนพึ่งพาสำหรับ game asset [1] (effort: ต่ำ) ข้ามไปก่อน: Blender→Unreal geometry-nodes VFX port [4] (studio ใช้ Unity เป็นหลัก), rigging/animation showcase รายบุคคล [7][10][11][12], fan animation [2], โพสต์ court case ที่ไม่เกี่ยวข้อง [17] และ AI-3D-gen claim ที่ยังไม่ยืนยัน [14][20] นอกจากติดตามแบบไม่เร่งรีบ

## Signals to Watch
- Blender 5.2 release notes — ยืนยัน 'thin wall' shader และตรวจสอบว่ามี real-time/Unity equivalent หรือไม่ [1]
- เทคนิค rendering สำหรับ standalone-VR splatting (depth ordering, mobile-GPU performance) เมื่อมีการเผยแพร่เพิ่มเติม [6]
- ทิศทาง 'physical AI'/3D generalization ของ Luma Labs สำหรับความเกี่ยวข้องใน asset generation [14]
- คุณภาพ output ที่เป็น game-ready ของเครื่องมือ AI mesh-generation อย่าง Meshy [20]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Tioaoa2 | ^27793 c49 | [Blender 5.2 has a new shader feature called "thin wall" which is designed for me](https://x.com/Tioaoa2/status/2061445532518653996) |
| x | AnimGaby | ^1396 c13 | [D4DJ as Murder drones some parts are off sync because daVinci is trolling me Som](https://x.com/AnimGaby/status/2061071305634627949) |
| x | bilawalsidhu | ^660 c24 | [We treat 3d scanning like a tech demo, but it's actually spatial memory capture.](https://x.com/bilawalsidhu/status/2061134940813611505) |
| x | ashlee3dee | ^499 c1 | [stylized black hole vfx with geometry nodes :3 i will port this to unreal engine](https://x.com/ashlee3dee/status/2061195779952275511) |
| x | VFX_Therapy | ^482 c3 | [When your Unreal VFX project hits different… @IgorPontes breakdown his Sasuke-le](https://x.com/VFX_Therapy/status/2061109917222920517) |
| x | DSkaale | ^306 c7 | [Just stepped inside my favorite movie locations on my Quest 3 🎬 Gaussian splatti](https://x.com/DSkaale/status/2061114844263117118) |
| x | DemNikoArt | ^285 c2 | [Bike Suspension Tutorial coming this week 😉 #b3d #blender #blender3d #rigging #t](https://x.com/DemNikoArt/status/2061498924473487814) |
| x | bilawalsidhu | ^79 c6 | [Honestly if we put this demo in a fancy XR headset, we'd call it jarvis. The fut](https://x.com/bilawalsidhu/status/2061450274011591084) |
| x | bilawalsidhu | ^78 c3 | [Fucking cool. Giving AR portal vibes - like watching volumetric video with full ](https://x.com/bilawalsidhu/status/2060943911363690875) |
| x | EdwardUrena_h | ^76 c0 | [I set out to see if it was possible to add a custom gizmo—and yes, it was; it to](https://x.com/EdwardUrena_h/status/2061539090198045116) |
| x | EdwardUrena_h | ^65 c0 | [One of the good things about this is that it allows you to display only the bone](https://x.com/EdwardUrena_h/status/2061559777575014798) |
| x | TopologicalBomb | ^59 c3 | [homelander nearly done. gotta do a bit of miscellaneous rigging and mesh joining](https://x.com/TopologicalBomb/status/2061386957444325399) |
| x | anishmoonka | ^52 c1 | [To build a young Arnold, the crew scanned an older one. They took a full-body 3D](https://x.com/anishmoonka/status/2061192494449152390) |
| x | LumaLabsAI | ^50 c6 | [To improve human life, AI systems must be able to help us improve the physical w](https://x.com/LumaLabsAI/status/2061460217616027961) |
| x | Arorea | ^39 c0 | [@Sphere_Deer For Toriel I used a 3d scan of my head to 3d model a base that was ](https://x.com/Arorea/status/2061392121232249247) |
| x | casey_sheep | ^38 c2 | [🔥 I've partnered with @FlippedNormals to launch a special FlipBox bundle! Get 11](https://x.com/casey_sheep/status/2061482329139532174) |
| x | corn724142 | ^24 c7 | [I am now 100% certain Michael Proctor planted taillight. I can also prove it wit](https://x.com/corn724142/status/2061567865535275124) |
| x | RadianceFields | ^20 c0 | [gaussian splatting can be black and white too https://t.co/UshqcIlDAo](https://x.com/RadianceFields/status/2061221116492861786) |
| x | bilawalsidhu | ^9 c0 | [go deeper into gaussian splatting: https://t.co/0LnbXw4oZo](https://x.com/bilawalsidhu/status/2061260973260865653) |
| x | MeshyAI | ^2 c0 | [@niftyisland 😍 This is soooooo cool 😍](https://x.com/MeshyAI/status/2061246669040369797) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Tioaoa2</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 27793 · 💬 49</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Tioaoa2/status/2061445532518653996">View @Tioaoa2 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Blender 5.2 has a new shader feature called &quot;thin wall&quot; which is designed for meshes which have no thickness (or very little). These can be anything from leaves, paper, tissues and some thin plastics ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Blender 5.2 เพิ่ม shader node 'thin wall' สำหรับ mesh ที่ไม่มีความหนา เช่น ใบไม้ กระดาษ พลาสติกบาง ให้แสงผ่านทะลุถูกต้องโดยไม่ต้อง model geometry หนา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ทำ asset ใบไม้ ผ้า หรือกระดาษใน Blender สำหรับ Unity/XR ได้ translucency ถูกต้องด้วย node เดียว แทน workaround SSS หรือ alpha card</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">รอบหน้าที่ทำ asset ใบไม้หรือ thin surface ใน Blender ลอง thin wall node เทียบกับ alpha/SSS workaround ที่ใช้อยู่ในแง่คุณภาพและเวลา render</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Tioaoa2/status/2061445532518653996" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnimGaby</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1396 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnimGaby/status/2061071305634627949">View @AnimGaby on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“D4DJ as Murder drones some parts are off sync because daVinci is trolling me Some part I didn't include the background character because It will just destroy my blender lol anyways snow shader by @Ash”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>animator แฟนคลับโพสต์งาน Blender + DaVinci Resolve ที่ผสม D4DJ กับ Murder Drones พร้อมบ่น sync หลุดและ background character ทำ Blender พัง</dd>
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
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 660 · 💬 24</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061134940813611505">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We treat 3d scanning like a tech demo, but it’s actually spatial memory capture. Damn near teleportation. A few hundred photos of my parent’s old home, and now it’s immortalized forever. 3d gaussian s”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev ใช้ RealityCapture + Luma AI (Litchfield) สร้าง 3D Gaussian splat จากรูปไม่กี่ร้อยภาพ โดยมองว่า photogrammetry คือการเก็บ spatial memory ระยะยาว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Pipeline RealityCapture → Gaussian splat ทำได้จริงในโปรเจกต์เดี่ยว weekend เดียว — บอก quality bar ที่ใช้ได้จริงสำหรับงาน XR/VR scene capture</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลอง workflow RealityCapture + Luma AI กับ location จริง เพื่อวัด scan quality และ export compatibility กับ Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061134940813611505" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ashlee3dee</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 499 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ashlee3dee/status/2061195779952275511">View @ashlee3dee on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“stylized black hole vfx with geometry nodes :3 i will port this to unreal engine... soon https://t.co/bu98xUEYuO”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist @ashlee3dee สร้าง stylized black hole VFX ด้วย Blender Geometry Nodes และมีแผนจะ port ไปยัง Unreal Engine</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Geometry Nodes ให้ workflow แบบ procedural ที่ port ไป game engine ได้ ตรงกับงาน VFX ใน Unity/XR ของทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">รอดู UE port เมื่อออก แล้วใช้ Geometry Nodes breakdown เป็น reference สำหรับงาน stylized VFX แนว sci-fi ใน Unity หรือ Unreal ของทีม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ashlee3dee/status/2061195779952275511" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 482 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2061109917222920517">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“When your Unreal VFX project hits different… @IgorPontes breakdown his Sasuke-level Katon 🔥 with insane stylized effects. #vfx https://t.co/j4wFOeAnBm”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Igor Pontes ปล่อย breakdown ใน Unreal Engine สำหรับ VFX ไฟสไตล์อนิเมะ (Katon) ครอบคลุม particle, shader, และ timing</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>หลักการ stylized VFX จาก Unreal ใช้อ้างอิงกับ Unity VFX Graph และ Shader Graph ได้โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดึง breakdown นี้เป็น reference ทำ anime-style elemental effect ใน VFX Graph ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2061109917222920517" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DSkaale</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 306 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DSkaale/status/2061114844263117118">View @DSkaale on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just stepped inside my favorite movie locations on my Quest 3 🎬 Gaussian splatting + Standalone VR — Multi-renderer ordering (render-order key + depth tiebreak) - View-space distance (length to splat ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนารัน Gaussian splat ของสถานที่ถ่ายทำหนังบน Quest 3 standalone ผ่าน SplatBox (Unity) แก้ splat sorting ด้วย view-space distance และ render-order key + depth tiebreak</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การใช้ view-space length แทน raw z แก้ปัญหา sorting accuracy ที่รู้จักกันดีใน splat renderer และยืนยันว่าใช้งานได้บน standalone Quest 3 โดยไม่ต้องต่อ PC</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity XR team นำ SplatBox render-order + view-space distance sort ไปใช้กับ scene photogrammetry หรือ location-capture ที่พัฒนาสำหรับ standalone headset ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DSkaale/status/2061114844263117118" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DemNikoArt</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 285 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DemNikoArt/status/2061498924473487814">View @DemNikoArt on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bike Suspension Tutorial coming this week 😉 #b3d #blender #blender3d #rigging #tutorial https://t.co/XekTbKmhOc”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@DemNikoArt จะปล่อย tutorial การ rig ระบบกันสะเทือนจักรยานใน Blender สัปดาห์นี้ เน้นการตั้งค่า mechanical rig</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค rig กลไก suspension ใช้ได้โดยตรงกับ asset ยานพาหนะและ props ใน Unity และ XR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม 3D/Unity ดู tutorial แล้วเอาเทคนิค suspension rig ไปใช้กับ asset ยานพาหนะหรือกลไกใน pipeline ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DemNikoArt/status/2061498924473487814" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 79 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061450274011591084">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Honestly if we put this demo in a fancy XR headset, we’d call it jarvis. The future of 3d doesn’t involve the death of autocad, maya and blender. It turns those tools into a shared canvas of collabora”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้เขียน react ต่อ demo 3D ที่ไม่ระบุชื่อ โดยมองว่า AI agents จะเป็น collaboration layer บน Blender, Maya และ AutoCAD ไม่ใช่มาแทนที่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061450274011591084" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
