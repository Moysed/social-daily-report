---
type: social-topic-report
date: '2026-06-05'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-05T03:32:24+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 37
salience: 0.68
sentiment: mixed
confidence: 0.58
tags:
- gaussian-splatting
- photogrammetry
- blender
- shaders
- asset-pipeline
- webxr
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2062164703879540736/img/YjSQE5hPP5vo0ERh.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-05

## TL;DR
- SuperSplat ของ PlayCanvas (ฟรี, open source) สตรีม Gaussian scan 24 ล้านจุดไปยังเว็บเบราว์เซอร์แบบ live พร้อม load แทบทันที [3] — ส่งผ่าน web-native ไม่ใช่แค่ desktop viewer
- งานวิจัย Gaussian Splatting มาพร้อมกันหลายชิ้น: HiGS hierarchical real-time rendering [21], FreeStreamGS feed-forward จาก unposed streaming input [31], ZipSplat แบบ pose-free ใต้หนึ่งวินาที [33], และ TripoSplat image-to-3D Gaussian [32]
- เครื่องมือ photogrammetry ฝั่ง capture พัฒนาขึ้น: KIRI Engine เปิดตัว Featureless Object Scan Mode สำหรับวัตถุมันวาว/โมโนโครมที่ทำให้ feature matching พัง [14] และ node setup ใน Blender 20 วินาทีเพื่อ render scan ได้สมจริงขึ้น [30]
- Pipeline มาตรฐาน scan-to-game-ready (decimate, re-UV, bake details) ยังคงเป็น workflow หลัก [1]; มีเกม AAA เปิดเผยการใช้ laser scanning + photogrammetry ในการผลิต [4]
- สัญญาณย้อนทาง: โพสต์ดังตำหนิ photogrammetry ว่าทำให้เกมมีขนาด 130GB [7] — ต้นทุนจริงสำหรับเกม mobile หรือที่จำกัดขนาด

## สิ่งที่เกิดขึ้น
3D Gaussian Splatting ครองวันนั้นทั้งฝั่งเครื่องมือและงานวิจัย SuperSplat (PlayCanvas) สาธิตการสตรีม scan ขนาด 24M Gaussians ไปยังเบราว์เซอร์แบบ live พร้อม load แทบทันที [3] และบริษัทอสังหาริมทรัพย์สร้างโครงการที่ยังไม่ได้ก่อสร้างขึ้นมาใหม่เป็น splat ที่เดินสำรวจได้สำหรับผู้ซื้อ [11] งานวิจัย/release หลายชิ้นผลักดัน splatting ไปสู่การ capture ที่เร็วขึ้นและไม่ต้องใช้ pose: HiGS two-scale hierarchical rendering [21], FreeStreamGS online feed-forward จาก unposed streaming input [31], ZipSplat (Gaussian น้อยลง, pose-free, ต่ำกว่าหนึ่งวินาที) [33], และ TripoSplat image-to-3D [32] พร้อม demo การสร้าง GS แบบ interactive [13] ด้าน photogrammetry, KIRI Engine เพิ่ม Featureless Object Scan Mode สำหรับพื้นผิวมันวาว/ไม่มีลวดลาย [14] และ node setup เพื่อเพิ่มความสมจริงใน Blender [30]; pipeline scan-to-game-ready ด้วย decimation, UV ใหม่, และการ bake detail ถูกหยิบยกขึ้นมา [1] ขณะที่โปรเจกต์ AAA ยืนยันการใช้ laser scanning + photogrammetry [4]

## ทำไมจึงสำคัญ (เหตุผล)
มีสองแนวโน้มที่มาบรรจบกันสำหรับ portfolio ของสตูดิโอ อย่างแรก splatting กำลังเคลื่อนจาก research demo สู่ web-deliverable assets [3][11]: การสตรีม 24M Gaussians ไปยังเบราว์เซอร์ทำให้ 3D photoreal ใช้งานได้จริงบนเว็บและ XR โดยไม่ต้องพึ่ง client ขนาดใหญ่ อย่างที่สอง method feed-forward แบบ pose-free ใหม่ [31][33] เล็งไปที่ pain point ที่ใหญ่ที่สุดใน capture pipeline — ขั้นตอน pose-estimation/COLMAP ที่ช้าและเปราะ — ซึ่งอาจย่นระยะจาก phone scan ถึง asset ที่ใช้งานได้ น้ำหนักที่ฉุดอยู่คือน้ำหนัก asset: การวิจารณ์เรื่อง photogrammetry bloat [7] เป็นต้นทุนลำดับสองที่เป็นจริง เพราะ raw scan detail ที่มากเกินไปทำให้ขนาดติดตั้งพองโต ซึ่งเป็นข้อจำกัดโดยตรงสำหรับเกม mobile Splatting และ workflow scan-to-game-ready bake [1] ตอบโจทย์นี้บางส่วนด้วยการแปลง capture เป็น geometry ที่ควบคุมได้, ถูก decimate แล้ว หรือ Gaussian representation แบบ compact [33] แทนที่จะเป็น 4K texture set ทุกที่

## ความเป็นไปได้
**น่าจะเกิด:** web-based splat viewer อย่าง SuperSplat พัฒนา streaming/scale ต่อเนื่อง ทำให้ 3D photoreal เป็น format ส่งมอบทาง web/XR ที่ใช้งานได้จริงภายในไม่กี่เดือน [3][11] **เป็นไปได้:** pose-free feed-forward splatting [31][33] และ image-to-3D [32][24] ถึงคุณภาพระดับ production สำหรับการสร้าง background/prop แต่ส่วนใหญ่ยังเป็น demo หรืองานวิจัยที่ยังไม่ได้ benchmark ดังนั้นคุณภาพและ licensing ยังพิสูจน์ไม่ได้ **เป็นไปได้:** Featureless Object Mode ของ KIRI [14] ปิดช่องว่างที่รู้จักกันดีสำหรับการสแกน glossy props ที่เป็นประโยชน์สำหรับ hard-surface assets **ไม่น่าเกิด (ระยะใกล้):** splatting แทนที่ mesh-based pipeline สำหรับตัวละครเกมที่มีการ animate ทั้งหมด — หลักฐานปัจจุบันคือการ capture และ render scene แบบ static ไม่ใช่ rigged deformable assets แหล่งข้อมูลไม่มีการให้ตัวเลขความน่าจะเป็น

## การนำไปใช้กับ NDF DEV
1) ทดลอง SuperSplat/PlayCanvas สำหรับ 3D scan ที่ส่งผ่านเว็บในโปรเจกต์ XR และ web; รูปแบบ real-estate walkthrough [11] map ตรงกับงาน client visualization — effort ต่ำ/กลาง [3][11] 2) เพิ่ม KIRI Engine ใน capture toolkit: ทดสอบ Featureless Object Scan Mode กับ glossy props [14] และนำ Blender scan-render node setup มาใช้ [30] — effort ต่ำ 3) กำหนดมาตรฐาน scan-to-game-ready bake (decimate → re-UV → bake) เป็น pipeline step ที่มีเอกสาร [1] และวางงบ install size ไว้รับมือกับความเสี่ยง photogrammetry bloat สำหรับ mobile title [7] — effort ต่ำ/กลาง 4) นำ shader reference ใน Unity URP/ShaderGraph (dissolve [10], potion [26]) และ Blender Shaders Plus addon [9] มาใช้กับงาน VFX — effort ต่ำ 5) ถ้าโปรเจกต์ไหนใช้ Unreal ให้จด UE5.8 Niagara memory/speed gains สำหรับ VFX [8] — effort ต่ำ ข้ามไปก่อน: feed-forward GS papers ในฐานะ production tool (ติดตามเฉยๆ ยังไม่ได้ benchmark) [31][33]; generative video/image hype items [25][29][34]; และโพสต์ที่ไม่เกี่ยว (OSINT ceiling [2], furry art [23], NYC meetup [35])

## Signals to Watch
- ขนาดและ load time ของ web-native splat streaming — demo 24M-Gaussian บนเบราว์เซอร์ของ SuperSplat ตั้งมาตรฐานใหม่ [3]
- Pose-free / feed-forward splatting ที่พัฒนาสู่การตัดขั้นตอน COLMAP ออก [31][33]
- การสร้าง image-to-3D asset สำหรับ game props (TripoSplat [32], Meshy style-consistent towns [24])
- วินัยด้านขนาด install เมื่อการใช้ photogrammetry/scan ขยายตัว โดยเฉพาะสำหรับ mobile [7]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | JasozzGames | ^1326 c16 | [I'm really addicted to this 3D-scan-to-game-ready-asset pipeline! Just a few rou](https://x.com/JasozzGames/status/2062165225588089172) |
| x | bilawalsidhu | ^1255 c34 | [Gosh I love the OSINT community. This project throws every plane flying overhead](https://x.com/bilawalsidhu/status/2062527676557001015) |
| x | playcanvas | ^698 c22 | [🚀 Major upgrades just landed in SuperSplat, the free and open source platform fo](https://x.com/playcanvas/status/2062165374120894862) |
| x | _YuriP__ | ^556 c4 | [• Development started in 2020 • Lead character designer is Yusuke Kozaki (Fire E](https://x.com/_YuriP__/status/2062605291485540393) |
| x | VFX_Therapy | ^361 c2 | [Amazing procedurally generated real-time cloud shader created by @HugoChenin. #u](https://x.com/VFX_Therapy/status/2062231883384258909) |
| x | jettelly | ^287 c2 | [Developer jakubiee made this simple head shader for Unreal Engine 5, experimenti](https://x.com/jettelly/status/2062081858154750016) |
| x | TheVicious_One | ^231 c22 | [Hot take incoming: Photogrammetry is why games are 130GB We don't need to see la](https://x.com/TheVicious_One/status/2062204594185228557) |
| x | RedefineFX | ^219 c4 | [Unreal Engine 5.8 brings memory and speed optimizations for Niagara, allowing fo](https://x.com/RedefineFX/status/2062144965472313446) |
| x | filip_animation | ^190 c1 | [My most used Blender addons #4: - Shaders Plus by SMOUSE Glass, water, oily meta](https://x.com/filip_animation/status/2062619776153764230) |
| x | VFX_Therapy | ^152 c0 | [Dissolve Shader = Interactive edge glow + world space control. Perfect for enemy](https://x.com/VFX_Therapy/status/2062607977186738307) |
| x | AurelienCa80656 | ^148 c7 | [A real estate project recreated in Gaussian Splatting. Future buyers can freely ](https://x.com/AurelienCa80656/status/2062053609102008532) |
| x | mweinbach | ^126 c6 | [I keep thinking about Apple's U1 chip and the idea of understanding 3D space wit](https://x.com/mweinbach/status/2062255347608236229) |
| x | tom_doerr | ^116 c0 | [Interactive 3D generation with Gaussian Splatting https://t.co/eKRLRxxvVN https:](https://x.com/tom_doerr/status/2062467994786099421) |
| x | KIRI_Engine_App | ^112 c2 | [Featureless objects break most photogrammetry pipelines. Glossy, monochrome, no ](https://x.com/KIRI_Engine_App/status/2062089405741854822) |
| x | DemNikoArt | ^111 c2 | [🚨 NEW TUTORIAL IS OUT NOW! How to rig a Bike Suspension in Blender. 🔗 below #b3d](https://x.com/DemNikoArt/status/2062589493710934176) |
| x | SciTechera | ^111 c10 | [Wow. That's cool. Researchers just released World, an open-source Unreal Engine ](https://x.com/SciTechera/status/2062554345087041916) |
| x | 3DxDEV7 | ^73 c2 | [Take a look at this 👀 A procedural robot character creator for Blender with pres](https://x.com/3DxDEV7/status/2062247832321417594) |
| x | Mix3Design | ^73 c1 | [I will have a big announcement in the upcoming hours all the blender 3d artists ](https://x.com/Mix3Design/status/2062654531888910756) |
| x | ChurchillModels | ^68 c1 | [As usual, this model was made using acrylic, styrene, brass, and 3D printed part](https://x.com/ChurchillModels/status/2062462671509709013) |
| x | Rahll | ^64 c3 | [I agree with your general sentiment, but to be clear, a lot of what you're descr](https://x.com/Rahll/status/2062272983499260229) |
| x | janusch_patas | ^62 c2 | [HiGS: A Hierarchical Rendering Architecture for Real-Time 3D Gaussian Splatting ](https://x.com/janusch_patas/status/2062064390136795517) |
| x | multimodalart | ^60 c5 | [Ideogram 4 not only revamped their model to the best they built yet, but also th](https://x.com/multimodalart/status/2062210597148930139) |
| x | FoxibikiN | ^58 c1 | [(HD) Chillet &amp; Chill 🩵Chillet made by @furromantic ❄️Beau OC made by @miauha](https://x.com/FoxibikiN/status/2062652783975608633) |
| x | MeshyAI | ^53 c5 | [Build a 3D tiny town, block by block. Meshy keeps the style consistent across as](https://x.com/MeshyAI/status/2062121498207563920) |
| x | auqibhabib | ^52 c18 | [Made with seedance 2.0 + GPT Image 2 on @yapper_so Prompt. @image1 mage1 fights ](https://x.com/auqibhabib/status/2062599264807833617) |
| x | jettelly | ^49 c1 | [Technical Artist Miriam Martin Sánchez showed the breakdown behind her recent re](https://x.com/jettelly/status/2062489553152180629) |
| x | nodesandnoodles | ^46 c0 | [Turbulent gives you detailed water effects from a simple plane and a material. D](https://x.com/nodesandnoodles/status/2062394985689874596) |
| x | mweinbach | ^39 c2 | [You can then extend to an ecosystem. If you want to know where your AirTags are ](https://x.com/mweinbach/status/2062255381645074904) |
| x | bilawalsidhu | ^38 c5 | [First Aronofsky, then Scorsese, and now Gareth Edwards. Generative media has bee](https://x.com/bilawalsidhu/status/2062358867510440354) |
| x | KIRI_Engine_App | ^31 c1 | [It only takes 20 seconds to make your 3D scan renders more realistic Save this B](https://x.com/KIRI_Engine_App/status/2062479019023765643) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@JasozzGames</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1326 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/JasozzGames/status/2062165225588089172">View @JasozzGames on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm really addicted to this 3D-scan-to-game-ready-asset pipeline! Just a few rounds of decimation, new UVs, and then bake the details #gamedev #blender https://t.co/bAmx8JlHlM”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev แชร์ pipeline แปลง 3D scan ให้เป็น game-ready asset โดยใช้ decimation, UV remap, และ bake ใน Blender</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>วิธีทำ high-fidelity asset สำหรับ Unity หรือ XR โดยไม่ต้อง sculpt เอง ต้นทุนต่ำ ใช้ได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง workflow scan-decimate-bake กับ prop จริงเพื่อเร่ง asset production สำหรับ game หรือ XR ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/JasozzGames/status/2062165225588089172" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1255 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2062527676557001015">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gosh I love the OSINT community. This project throws every plane flying overhead onto your ceiling in near real time – decoded from a cheap radio, w/ live stars and the ISS behind it. Falling asleep u”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โปรเจกต์ hobbyist รับสัญญาณ ADS-B จาก SDR ราคาถูก แล้ว project ตำแหน่งเครื่องบิน ดาว และ ISS แบบ real-time ขึ้นเพดานเป็น ambient sky map.</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>รูปแบบ ambient ceiling projection ที่ซ้อน live data บน star map เป็น interaction concept ที่แข็งแกร่งสำหรับงาน XR/VR installation หรือ interactive exhibit.</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ลอง prototype pattern นี้โดยใช้ ADS-B open feed + star map API เป็น XR installation demo แบบ ceiling-mounted.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2062527676557001015" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@playcanvas</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 698 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/playcanvas/status/2062165374120894862">View @playcanvas on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚀 Major upgrades just landed in SuperSplat, the free and open source platform for 3D Gaussian splatting. Here is a 24-MILLION-Gaussian scan streaming live to a web browser. Near instant load time. Sol”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>SuperSplat อัปเดต renderer ใหม่ใช้ WebGPU compute shader + LOD streaming อัตโนมัติ รัน 24 ล้าน Gaussian บน browser ได้ 60 fps โหลดเร็วมาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Gaussian splat บน browser ที่ 60 fps ใช้งานได้จริงแล้ว ตรงกับงาน XR/VR และ 3D scanning ของทีมโดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง SuperSplat WebGPU renderer กับโปรเจกต์ web 3D หรือ XR ของทีมที่ต้องใช้ real-world scan หรือ photorealistic scene</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/playcanvas/status/2062165374120894862" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@_YuriP__</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 556 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/_YuriP__/status/2062605291485540393">View @_YuriP__ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“• Development started in 2020 • Lead character designer is Yusuke Kozaki (Fire Emblem Awakening/Fates/Heroes) • Laser scanning and photogrammetry • Developed their own sound engine with 7.1.4 audio • ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โปรเจกต์เกม (เริ่มปี 2020, Yusuke Kozaki ดู character) ใช้ photogrammetry, laser scanning และ custom 7.1.4 spatial audio engine พร้อมใช้ Top Gun Maverick เป็น reference สำหรับ cockpit cutscene</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Photogrammetry สำหรับ character และ custom spatial audio engine เป็น technique ที่ใช้ได้ตรงกับงาน Unity และ XR ของทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง evaluate photogrammetry pipeline เช่น RealityCapture หรือ Metashape สำหรับ XR asset เพราะ AAA production นี้ยืนยันแล้วว่า workflow ใช้ได้จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/_YuriP__/status/2062605291485540393" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 361 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2062231883384258909">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazing procedurally generated real-time cloud shader created by @HugoChenin. #unreal #gamedev https://t.co/5cVXjkgd7J”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Hugo Chenin เผย procedural cloud shader แบบ real-time ที่สร้างใน Unreal Engine พร้อม demo clip บน X</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Procedural cloud real-time เป็นสิ่งที่ต้องการบ่อยใน open-world และ XR — มี Unreal implementation จริงยืนยันว่าทำได้โดยไม่ต้องพึ่ง baked textures</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดูแนวทาง procedural noise ของ Chenin แล้วนำ shader logic หลักมาปรับใน Unity Shader Graph หรือ HLSL สำหรับงาน sky/environment</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2062231883384258909" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 287 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2062081858154750016">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer jakubiee made this simple head shader for Unreal Engine 5, experimenting with ambient occlusion to create more interesting facial shading. 🎭 See more: https://t.co/3GacKh8pFn #UnrealEngine #”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer jakubiee สร้าง head shader ใน Unreal Engine 5 โดยใช้ ambient occlusion เพิ่ม depth ให้ facial shading ดูน่าสนใจขึ้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป็น reference ที่ดีสำหรับทีมที่ทำ character ใน UE5 — แสดงให้เห็นว่า single-pass AO shader ทำได้แค่ไหน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู shader source ของ jakubiee เพื่อนำ AO technique ไปใช้กับ NPC หรือ avatar material ใน UE5 project ของทีม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2062081858154750016" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheVicious_One</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 231 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheVicious_One/status/2062204594185228557">View @TheVicious_One on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hot take incoming: Photogrammetry is why games are 130GB We don't need to see laundry in 4k”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ความเห็นนักพัฒนาเกมว่า photogrammetry (การสแกนวัตถุจริงเป็น 3D asset ความละเอียดสูง) คือต้นเหตุหลักที่ทำให้เกมมีขนาด 100GB+ ไม่ใช่ gameplay</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีม Unity ที่ใช้ photogrammetry เจอ tradeoff เดียวกัน — ความละเอียดสูงทำให้ build ใหญ่ ส่งผลต่อ distribution, load time, และ storage บน mobile/XR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">กำหนด texture budget ต่อ asset category ใน Unity ตั้งแต่เนิ่นๆ และ flag photogrammetry asset ให้ review LOD กับ compression ก่อนสะสมใน build</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheVicious_One/status/2062204594185228557" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RedefineFX</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 219 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RedefineFX/status/2062144965472313446">View @RedefineFX on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Unreal Engine 5.8 brings memory and speed optimizations for Niagara, allowing for bigger and more detailed VFX simulations that run in real-time. https://t.co/YhsZW0v0zm”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>UE 5.8 ลด memory และเพิ่มความเร็ว Niagara ทำให้ VFX simulation ใหญ่ขึ้น ละเอียดขึ้น แบบ real-time</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ทำ XR/VR หรือ real-time 3D บน Unreal Engine รัน particle effect ซับซ้อนขึ้นได้โดยไม่ชนเพดาน performance เดิม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้ามี project บน Unreal Engine ทดสอบ UE 5.8 Niagara กับ scene ที่เคยต้อง bake หรือ simplify VFX ไว้ก่อน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RedefineFX/status/2062144965472313446" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
