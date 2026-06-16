---
type: social-topic-report
date: '2026-06-12'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-12T15:38:38+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 46
salience: 0.58
sentiment: mixed
confidence: 0.6
tags:
- gaussian-splatting
- visionos
- unity
- threejs
- ai-3d
- procedural
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065400058565079040/img/K_mHR8IT0VE_qxwT.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-12

## TL;DR
- Gaussian splatting ครองคลัสเตอร์วันนี้: Apple visionOS 27 / Vision Pro รองรับ splat แบบ native [17], Apple Maps ดูเหมือนผสาน photogrammetry mesh กับ splat [20], และ Spark นำ 3D GS เข้า pipeline ของ three.js ควบคู่กับ mesh [26]
- Apple เปิด visionOS 27 และ Reality Composer Pro 3 API ให้นักพัฒนาเพิ่มขึ้น [19] แต่ Vision Pro culling splat ตัดภาพเมื่อเข้าใกล้ ทำให้ interior/walkthrough พัง [17]
- งานวิจัยลดต้นทุน GS capture: Wild3R ทำ feed-forward GS จากรูปถ่าย sparse ที่ไม่มีเงื่อนไข [32] และ multi-GPU PyTorch GS abstraction ขยาย reconstruction ไปยังฉากใหญ่/ความละเอียดสูง [18]
- Unity asset tooling: Real Fake Interiors เป็น baking tool + shader จำลองห้องที่มีเฟอร์นิเจอร์ซ่อนอยู่หลังหน้าต่างแบน [5]; Unity Editor tool จัดการ mask, channel packing, และ ramp โดยไม่ต้องวนกลับ Photoshop [12]
- AI-assisted 3D และ DCC releases: Claude Fable 5 รายงานว่าสร้าง rigged mesh พร้อม hierarchy ที่สะอาดและ metadata สำหรับ LLM [31] และขับ three.js scene สไตล์ GTA (shimmering ยังแก้ไม่ได้) [23]; Houdini 22 keynote วันที่ 17 มิถุนายนที่ลอนดอน [11] และ Unreal 5.8 รายงาน Niagara fluid ลื่นขึ้น [22]

## What happened
สัญญาณแรงที่สุดคือคลัสเตอร์ Gaussian splatting / radiance field ที่กระจายข้าม platform และ pipeline Apple เพิ่มรองรับ GS ใน Vision Pro แต่มี close-range culling เชิงรุกที่ทำให้ interior ด้อยลง [17]; ผู้สังเกตการณ์อนุมานว่า Apple Maps ใน visionOS 27 ผสาน photogrammetry mesh กับ splat [20] และ visionOS 27 รวมกับ Reality Composer Pro 3 ว่ากันว่าเปิด platform internal ให้นักพัฒนาเพิ่มขึ้น [19] บนเว็บ Spark ผนวก 3D GS เข้า three.js render pipeline และผสม splat กับ mesh ในฉากเดียวกัน [26] งานวิจัยผลักดันด้าน capture และ scale: Wild3R ทำ feed-forward GS จากรูปถ่าย sparse ไม่มีข้อจำกัด [32] และ multi-GPU PyTorch abstraction ขยาย GS reconstruction [18]; SIGGRAPH NeRF capture ของ Jensen Huang ผุดขึ้นอีกครั้ง [8][35] และ Meta Reality Labs collaboration ทดสอบ GS และ volumetric video ขั้นสุด [10]

## Why it matters (reasoning)
GS เคลื่อนจาก research demo สู่ production tooling ที่แตะ stack จริงของ studio: Unity, web (three.js), และ Vision Pro XR Spark ผสม splat กับ mesh ใน three.js [26] และ native Vision Pro support ของ Apple [17][20] หมายความว่า splat อยู่ภายในฉากปกติได้แทนที่จะจำกัดอยู่ใน viewer แยก feed-forward แบบ sparse input [32] และ multi-GPU scaling [18] โจมตีอุปสรรค production ใหญ่สุดสองอย่าง — ความพยายาม capture และต้นทุน reconstruction — ซึ่งเป็นเงื่อนไขที่ทำให้ splat กลายเป็น asset type ปกติแทนที่จะเป็น specialist capture สัญญาณตรงกันข้ามมีหลักฐาน: Apple culling ทำให้ splat ไม่น่าเชื่อถือสำหรับ interior XR ใกล้ๆ ตอนนี้ [17] และ geometry ที่ AI สร้างยังมี artifact เช่น shimmering materials [23] ดังนั้น ข้อจำกัดด้านคุณภาพและ platform ไม่ใช่ความสามารถ เป็นตัวกำหนดการนำไปใช้ ส่วน Unity micro-tool [5][12] และ DCC releases [11][22] เป็นการพัฒนา iteration-speed แบบ incremental ไม่ใช่การเปลี่ยนทิศทาง

## Possibility
Likely: GS รวมเข้า engine และ web runtime ที่มีอยู่ต่อเนื่องในฐานะ asset type ที่เข้ากับ mesh ได้ เนื่องจากมีการเคลื่อนไหวพร้อมกันใน three.js [26], Apple platforms [17][20], และ scaling research [18][32] Plausible: feed-forward sparse-photo capture [32] ทำให้ splat ใช้ได้จริงสำหรับ environment/asset reference capture ภายในไม่กี่เดือน Plausible แต่มีข้อจำกัด: Vision Pro interior experience ที่สร้างจาก splat ล้วนยังถูกบล็อกจนกว่า Apple จะเปลี่ยน culling behavior [17]; การสร้างบน photogrammetry-mesh + splat hybrid [20] เป็นทางเลือกที่ปลอดภัยกว่าในระยะใกล้ Unlikely จากหลักฐานนี้: AI mesh generation (Fable 5) แทนที่ production asset ที่ rig มือ/อัตโนมัติเร็วๆ นี้ — demo แสดงศักยภาพแต่ก็ยังมี artifact ที่ยังแก้ไม่ได้ [23][31] ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น

## Org applicability — NDF DEV
1) ประเมิน Real Fake Interiors สำหรับ interior อาคาร stylized ใน game/XR ที่ geometry เต็มรูปแบบสิ้นเปลือง — effort ต่ำ [5] 2) ต้นแบบ Spark ในฉากทดสอบ three.js เพื่อดูว่า splat+mesh mixing ทำงานอย่างไรบน web/mobile target ของ studio — effort กลาง [26] 3) ก่อน scope Vision Pro splat interior ใดๆ ให้ validate กับข้อจำกัด close-range culling และเลือก photogrammetry-mesh + splat hybrid แบบ Apple Maps แทน — effort ต่ำเพื่อยืนยัน กลางเพื่อออกแบบรอบ [17][20][19] 4) เพิ่ม Unity mask/channel-packing editor tool เข้า VFX/texture workflow เพื่อลด Photoshop round-trip — effort ต่ำ [12] 5) ดู Houdini 22 keynote (17 มิ.ย.) สำหรับฟีเจอร์ procedural pipeline ก่อนตัดสินใจเรื่อง tool version — effort ต่ำ [11] 6) รันการทดสอบ Fable 5 mesh/rig generation แบบ time-box เล็กๆ สำหรับ greyboxing และ prototype เท่านั้น โดยถือว่า output เป็น draft เนื่องจากข้อควรระวัง shimmering/คุณภาพ — effort กลาง [31][23] 7) ชี้ edutech/internal upskilling ไปยังหลักสูตร robotics/photogrammetry ฟรีของ Bonn สำหรับพื้นฐาน spatial capture — effort ต่ำ [2] ข้าม: รายการ crypto/NFT [30][39], radiance-field celebrity capture ในฐานะ production-relevant [8][35], Luma Cannes marketing [38][44], และโพสต์ off-topic politics/personal ทั้งหมด [7][9][15][28][29][33]

## Signals to Watch
- Apple เปลี่ยน Vision Pro splat culling — ปัจจุบันบล็อก interior splat ใกล้ๆ [17]; ติดตาม visionOS 27 API notes [19]
- Feed-forward sparse-photo GS (Wild3R / AnySplat finetune) พัฒนาสู่ capture tool ที่ใช้ได้จริง [32]
- Spark / three.js GS adoption ในฐานะเส้นทางสู่ splat ใน web และ mobile XR builds [26]
- Houdini 22 keynote (17 มิ.ย., London) feature set สำหรับ procedural content pipeline [11]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ItzFAILURE | ^1062 c9 | ["Keep moving forward." Our past should define us not hold us prisioner. TY for 6](https://x.com/ItzFAILURE/status/2065400456591937620) |
| x | IlirAliu_ | ^658 c1 | [One professor at the University of Bonn quietly put his entire robotics curricul](https://x.com/IlirAliu_/status/2064979957009285375) |
| x | afrotron | ^222 c2 | [Rig is done just ironing out some kinks. I'll put it up on my gumroad later this](https://x.com/afrotron/status/2064789451839049861) |
| x | RyanLykos | ^212 c2 | [Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv](https://x.com/RyanLykos/status/2065189214413611291) |
| x | 80Level | ^198 c1 | [Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo t](https://x.com/80Level/status/2065109302562422981) |
| x | VFX_Therapy | ^173 c0 | [Detailed breakdown of the flame vfx in one frame by @S_SerraMock in Unreal. #vfx](https://x.com/VFX_Therapy/status/2065397660119716179) |
| x | zephyyy7 | ^170 c6 | [@Will40746376 @Dexerto funny how last game this same crowd swore "no real woman ](https://x.com/zephyyy7/status/2065112542448374086) |
| x | RadianceFields | ^152 c8 | [In the summer of 2023, I cold emailed Jensen Huang and asked to capture a NeRF o](https://x.com/RadianceFields/status/2064766228866924681) |
| x | sachin_inc | ^148 c9 | [The action of the Returning Officer, who is also the Secretary of the Madhya Pra](https://x.com/sachin_inc/status/2064727133411475762) |
| x | gracia_vr | ^140 c3 | [We teamed up with researchers at Meta @RealityLabs to stress-test what's actuall](https://x.com/gracia_vr/status/2065106030539997345) |
| x | sidefx | ^132 c0 | [Houdini 22 launches in London next week! Join us at Curzon Soho Cinema for an ex](https://x.com/sidefx/status/2065141618509005226) |
| x | VFX_Therapy | ^106 c0 | [Tired of opening Photoshop for every tiny mask tweak? @KenDeng built a Unity Edi](https://x.com/VFX_Therapy/status/2065035196358094848) |
| x | bilawalsidhu | ^105 c13 | [Wow, this is really cool. Has anyone productized this? I would love to be able t](https://x.com/bilawalsidhu/status/2064865579547193788) |
| x | filicroval | ^101 c7 | [🤖time for another 4D tool! this tool turns videos into moving 3D places film a m](https://x.com/filicroval/status/2064731328210145625) |
| x | rmacdon627 | ^96 c3 | [✅ The SAVE America Act (proof of citizenship + photo ID for federal elections) i](https://x.com/rmacdon627/status/2064881931221602482) |
| x | AKantemirov | ^82 c3 | [Took a few days to get procedural materials from @noaxdesign onto my model and s](https://x.com/AKantemirov/status/2065233326386843944) |
| x | iBrews | ^71 c3 | [Apple's new gaussian splatting support is cool, but the culling is kind of ridic](https://x.com/iBrews/status/2064836100720394464) |
| x | janusch_patas | ^69 c1 | [A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting Abstract (excerp](https://x.com/janusch_patas/status/2064965130413048221) |
| x | xchester16 | ^69 c1 | [After spending some time with the new visionOS 27 APIs and Reality Composer Pro ](https://x.com/xchester16/status/2064900511116185939) |
| x | Azadux | ^69 c5 | [I believe that Apple Maps in visionOS 27 is a combination of photogrammetry mesh](https://x.com/Azadux/status/2064876849252225246) |
| x | multimodalart | ^69 c2 | [folks @liquidai trained a specialist tiny model to do one thing rly well: extrac](https://x.com/multimodalart/status/2064864942180679962) |
| x | RedefineFX | ^67 c2 | [Falcon 9 landing real-time VFX in Unreal 5.8, continuing with my space explorati](https://x.com/RedefineFX/status/2065047711477301342) |
| x | drashyakuruwa | ^64 c8 | [A minor graphics update to the initial version of my GTA V-style game with @thre](https://x.com/drashyakuruwa/status/2065055670496276601) |
| x | DillyWillyVR | ^62 c2 | [Texturing a commission for my friend @Lightning260493 and here is the process! 🐾](https://x.com/DillyWillyVR/status/2065214193511326082) |
| x | pablovelagomez1 | ^53 c4 | [There's been a few cool updates recently. In particular, @rerundotio 0.33 releas](https://x.com/pablovelagomez1/status/2065154703068193138) |
| x | GithubProjects | ^47 c3 | [Spark integrates 3D Gaussian splatting with the THREE.js rendering pipeline for ](https://x.com/GithubProjects/status/2064807319255515476) |
| x | Deathbymetal87 | ^41 c2 | [if 420 of you guys donated to my kofi i could get an original 3d printed model o](https://x.com/Deathbymetal87/status/2065150122489430375) |
| x | fistandilus12 | ^40 c2 | [Funny how people who spent 20 years defending Photoshop, CGI, motion capture, pr](https://x.com/fistandilus12/status/2064943228340535490) |
| x | GSAIGETOA | ^38 c0 | [Update on Meeting of Team BDM with JS (Admin), DoT Shri K. Balaji on 09.06.2026 ](https://x.com/GSAIGETOA/status/2064954292612764048) |
| x | EnochsDegenCrib | ^37 c1 | [⭕️ $RENDER = The Decentralized GPU Powerhouse AI Actually Needs ⭕️💻🚀 Everyone's ](https://x.com/EnochsDegenCrib/status/2065155872914035156) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1062 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2065400456591937620">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&quot;Keep moving forward.&quot; Our past should define us not hold us prisioner. TY for 600 followers over these last couple of days! Model: @Artstudious Rig: @cookie_sugar42 Shader: @LuminaryOfAges Textures: ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Fan animator ฉลอง 600 followers ด้วยการโพสต์ fanart animation RWBY ใน Blender โดย credit ศิลปินแยกกันสำหรับ model, rig, shader และ textures</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ItzFAILURE/status/2065400456591937620" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IlirAliu_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 658 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IlirAliu_/status/2064979957009285375">View @IlirAliu_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One professor at the University of Bonn quietly put his entire robotics curriculum on YouTube: SLAM. Sensor fusion. State estimation. Probabilistic robotics. Self-driving cars. Motion planning. Photog”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Cyrill Stachniss อาจารย์ Univ. of Bonn นักวิจัย mobile robotics ที่ถูกอ้างอิงสูง อัป lecture มหาวิทยาลัยเต็มหลักสูตรขึ้น YouTube ฟรี ครอบคลุม SLAM, photogrammetry, sensor fusion, state estimation และ motion planning</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>SLAM และ photogrammetry ตรงกับงาน XR/VR spatial tracking และ 3D reconstruction ที่ studio ทำใน Unity อยู่แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ใช้ playlist SLAM และ photogrammetry เป็น reference ตอน scope งาน spatial anchoring หรือ AR tracking</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IlirAliu_/status/2064979957009285375" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@afrotron</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 222 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/afrotron/status/2064789451839049861">View @afrotron on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Rig is done just ironing out some kinks. I'll put it up on my gumroad later this month #blender #rigging #anissa #invincible https://t.co/CGVgJltzLt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@afrotron ทำ rig ตัวละคร Anissa จาก Invincible ใน Blender เสร็จแล้ว เตรียมปล่อยบน Gumroad เดือนนี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/afrotron/status/2064789451839049861" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 212 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2065189214413611291">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>RyanLykos แชร์ face rig ของตัวละคร Zhu Yuan ที่กำลัง WIP ใน Blender โดยโพสต์เป็นคลิปสั้น ไม่มี breakdown เทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2065189214413611291" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@80Level</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 198 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/80Level/status/2065109302562422981">View @80Level on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo that lets you create the illusion of a furnished room behind a flat window surface. Get it here: https://t.co/w9rlA4b1an ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Real Fake Interiors โดย AmplifyCreates คือ baking tool + shader สำหรับ Unity จำลองห้องที่มีเฟอร์นิเจอร์และแสงไฟอยู่หลังกระจกแบน โดยใช้เทคนิค interior mapping</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Interior mapping ให้ความลึกของตึกที่น่าเชื่อถือโดยแทบไม่กิน runtime — ได้จริงสำหรับ Unity project ที่มี exterior architecture</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลองใช้กับ project ที่มีตึกก่อนตัดสินใจทำ geometry จริงหรือ lightmap แบบแพง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/80Level/status/2065109302562422981" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 173 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2065397660119716179">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Detailed breakdown of the flame vfx in one frame by @S_SerraMock in Unreal. #vfx https://t.co/i257Fz3YZt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@S_SerraMock เผยแพร่ breakdown เทคนิค flame VFX ทีละ frame ใน Unreal Engine พร้อมอธิบาย layer ต่างๆ ในช็อตเดียว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ดู layer ของ particle, shader, และ lighting จาก pro ใน frame เดียว — เป็น reference ตรงๆ ให้ Unity team ทำ fire effect ใน game หรือ XR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เอา breakdown นี้เป็น reference ตอนทำ fire/environment VFX ใน Unity — map logic จาก Unreal ไปหา VFX Graph หรือ Shader Graph แทน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2065397660119716179" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@zephyyy7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 170 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/zephyyy7/status/2065112542448374086">View @zephyyy7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@Will40746376 @Dexerto funny how last game this same crowd swore &quot;no real woman looks like that,&quot; then Eve turned out to be a 3D scan of an adult Korean model. now an adult Korean face &quot;must be&quot; a chi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X โต้แย้งว่านักวิจารณ์อ่านใบหน้าอ้างอิงจากนักแสดงเกาหลีผู้ใหญ่ผิด โดยยกตัวอย่างว่าตัวละครในเกมก่อนหน้าสแกน 3D มาจากนางแบบเกาหลีผู้ใหญ่จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/zephyyy7/status/2065112542448374086" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RadianceFields</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 152 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RadianceFields/status/2064766228866924681">View @RadianceFields on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In the summer of 2023, I cold emailed Jensen Huang and asked to capture a NeRF of him at SIGGRAPH. He responded in about an hour and said yes. A radiance field is, in the simplest terms, akin to a 3D ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจัยอิสระ capture Gaussian splat 360° ของ Jensen Huang ที่ SIGGRAPH 2023 และสามปีต่อมา NVIDIA ออก project radiance field หลายตัว — NuRec, fVDB, 3DGRUT, gsplat — ยืนยันว่า format นี้ใช้งานจริงได้ในระดับ production</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Gaussian splatting มี tooling จาก NVIDIA รองรับแล้ว ทำให้ capture scene จริงสำหรับ XR/VR ทำได้จริงโดยไม่ต้องพึ่ง photogrammetry pipeline ราคาแพง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ควรทดสอบ NVIDIA gsplat หรือ 3DGRUT สำหรับ capture environment จริงใน XR scene ที่จะทำ แทนการ model 3D ด้วยมือ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RadianceFields/status/2064766228866924681" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
