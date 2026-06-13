---
type: social-topic-report
date: '2026-06-13'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-13T03:33:57+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 42
salience: 0.55
sentiment: mixed
confidence: 0.55
tags:
- gaussian-splatting
- photogrammetry
- unity
- houdini
- image-to-3d
- xr-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065400058565079040/img/K_mHR8IT0VE_qxwT.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-13

## TL;DR
- Gaussian Splatting กำลังเคลื่อนจากงานวิจัยสู่ pipeline จริง: Gracia VR + Meta Reality Labs ทดสอบ GS และ volumetric video กับ scene ยากอย่างอาคารกลางแจ้งแสงแดดจัด [9] และสตูดิโอรีโนเวทสแกนอสังหาริมทรัพย์ด้วย GS แล้วส่ง walkthrough แบบ floor-by-floor ผ่าน PlayCanvas [13]
- งานวิจัย GS ก้าวหน้าสองด้าน: แนวทาง multi-GPU PyTorch สำหรับ scale การ reconstruct ไปสู่ความละเอียดสูงขึ้นและ scene ใหญ่ขึ้น [15] และ Wild3R ซึ่งเป็น feed-forward 3DGS จากภาพ sparse ที่ไม่มีเงื่อนไข พร้อม dataset ใหม่สำหรับ finetune AnySplat [20]
- Houdini 22 keynote กำหนดวันที่ 17 มิถุนายน ที่ลอนดอน (Curzon Soho) [10]
- Image-to-3D tools ถูกรวมบน GPU cloud: TripoSR, Microsoft TRELLIS, Hunyuan3D 2.1, Nerfstudio และ 3DGS [29]
- Unity asset tooling ออกใหม่: 'Real Fake Interiors' bake ห้องตกแต่งจำลองไว้หลังพื้นผิว window แบน [6] และ mask tool ในตัว editor จัดการ contrast/thresholds/channel packing/ramps เพื่อลดการวนกลับ Photoshop [11]

## สิ่งที่เกิดขึ้น
เส้นเรื่องหลักของวันนี้คือ Gaussian Splatting และ capture-to-3D ความร่วมมือ Gracia VR / Meta Reality Labs ทดสอบ GS และ volumetric video ใน condition ยาก [9]; ทีมแยกต่างหากสแกนอาคารด้วย GS สร้างงานรีโนเวทใหม่เป็น 3D แล้ว deploy scene ที่เดินสำรวจได้แบบ floor-by-floor ใน PlayCanvas [13] ฝั่งวิจัย มี multi-GPU PyTorch GS abstraction สำหรับความละเอียดสูงและ scene ใหญ่ [15] และ Wild3R นำเสนอ feed-forward 3DGS จากภาพ sparse ที่ไม่มีเงื่อนไขพร้อม dataset finetune AnySplat [20] การ capture แบบ photogrammetry+splat ยังคงมีต่อเนื่อง [30] และ image-to-3D toolchain (TripoSR, TRELLIS, Hunyuan3D 2.1, Nerfstudio) ถูก package ลงบน GPU cloud [29]

## ทำไมถึงสำคัญ (เหตุผล)
หลายรายการชี้ไปทิศทางเดียวกัน: การสแกน environment จริงให้ได้ scene พร้อมใช้ใน engine ราคาถูกลงและ deploy ทางเว็บได้มากขึ้น PlayCanvas walkthrough [13] แสดงว่า GS รันใน browser engine ได้ ซึ่งตรงกับ XR และ web delivery โดยตรง; งานของ Meta Reality Labs [9] บ่งชี้การลงทุนจากฝั่ง platform เมื่อรวมกับ image-to-3D generators [29] และ feed-forward GS จากภาพธรรมดา [20] ผลที่ตามมาคือ greybox และ environment prototyping เร็วขึ้นโดยใช้ manual modeling น้อยลง การเปิดตัว Houdini 22 [10] ยังคง procedural generation อยู่บน roadmap สำหรับสตูดิโอที่รับ pipeline นั้นได้ AI-assisted mesh/rig generation (เช่น Claude 'Fable 5' สร้าง mesh ที่มีชื่อและ hierarchy ใน ไม่กี่นาที [26], three.js game [19], งาน realtime [17]) มีให้เห็นซ้ำแต่ยังเป็น single-demo, self-reported และยังไม่ได้รับการยืนยันคุณภาพ production

## ความเป็นไปได้
**มีแนวโน้มสูง:** GS ไปต่อใน web/engine pipeline สำหรับ XR และ walkthrough เพราะ browser deployment ส่ง production แล้ว [13] และ platform vendor ลงทุนอยู่ [9] **เป็นไปได้:** image-to-3D tools [29] และ feed-forward GS [20] ใช้งานได้จริงสำหรับ prototype/background asset แต่คุณภาพ topology และ texturing ระดับ production ยังไม่ได้รับการพิสูจน์จากโพสต์เหล่านี้ **ยังไม่น่าเกิดในเร็วๆ นี้:** การสร้าง rigged mesh production-ready แบบ one-shot ด้วย AI [26] — claim นี้อ้างอิงจาก demo 5 นาทีเดียวโดยไม่มีการยืนยันอิสระ ไม่มีแหล่งข้อมูลใดระบุความน่าจะเป็นเป็นตัวเลข จึงไม่มีการอ้างอิง

## การนำไปใช้สำหรับ NDF DEV
1) ทดลอง GS-to-web pipeline สำหรับ XR/walkthrough asset โดยใช้แนวทาง PlayCanvas [13] และ GS capture [9][30] — effort ปานกลาง, ตรงกับ XR/VR portfolio โดยตรง 2) ทดสอบ image-to-3D tools (TRELLIS, Hunyuan3D 2.1, TripoSR) สำหรับ greybox/prototype asset ผ่าน GPU cloud [29] — effort ต่ำ/ปานกลาง; ประเมินว่า output clean-up เร็วกว่า model จากศูนย์หรือไม่ 3) นำ Unity tools ทั้งสองมาใช้ได้เลย: 'Real Fake Interiors' สำหรับ interior depth ราคาถูกบน window ของ mobile/web [6] และ in-editor mask tool เพื่อลดรอบ Photoshop ใน VFX [11] — effort ต่ำ ใช้กับงาน Unity ได้ทันที 4) ส่งคนหนึ่งดู Houdini 22 keynote 17 มิถุนายนเพื่อดู procedural feature ที่ประกาศ [10] ก่อนตัดสินใจทุ่มเวลา pipeline — effort ต่ำในการเข้าร่วม, effort สูงในการ adopt 5) รัน experiment เล็กๆ แบบกำหนดเวลาด้วย AI mesh/rig generation [26][19] เฉพาะ asset ที่ไม่ critical — effort ต่ำ, ถือว่า output เป็น draft ข้าม: $RENDER / crypto decentralized-GPU pitch [23], NFT 3D-scan sale [28][21], culture-war thread เรื่อง AI กับงานฝีมือ [8][22] และรายการนอกเรื่อง (telecom meeting [24], sports sensor replay [32][33])

## Signals ที่ต้องติดตาม
- Houdini 22 keynote 17 มิถุนายน ลอนดอน — ดู procedural feature ที่ประกาศ [10]
- Wild3R + AnySplat: feed-forward GS จากภาพ sparse ธรรมดา พร้อม dataset [20]; คู่กับ multi-GPU GS scaling [15]
- Meta Reality Labs ลงทุนใน GS/volumetric video — จับตา platform tooling [9]
- 'Fable 5' (Claude) ปรากฏซ้ำใน 3D-gen demo [26][19][17] — ยังไม่ verified, ติดตามผลที่ reproduce ได้

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ItzFAILURE | ^3000 c19 | ["Keep moving forward." Our past should define us not hold us prisioner. TY for 6](https://x.com/ItzFAILURE/status/2065400456591937620) |
| x | IlirAliu_ | ^747 c1 | [One professor at the University of Bonn quietly put his entire robotics curricul](https://x.com/IlirAliu_/status/2064979957009285375) |
| x | GameZoneHQ | ^642 c3 | [Have a look at this impressive Unity real-time physics, created by VFX Artist @S](https://x.com/GameZoneHQ/status/2065365759451148399) |
| x | bilawalsidhu | ^474 c13 | [Someone needs to throw fable 5 at the OG of procedural 3D generation (houdini) a](https://x.com/bilawalsidhu/status/2065457916405072127) |
| x | VFX_Therapy | ^365 c0 | [Detailed breakdown of the flame vfx in one frame by @S_SerraMock in Unreal. #vfx](https://x.com/VFX_Therapy/status/2065397660119716179) |
| x | 80Level | ^266 c2 | [Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo t](https://x.com/80Level/status/2065109302562422981) |
| x | RyanLykos | ^248 c3 | [Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv](https://x.com/RyanLykos/status/2065189214413611291) |
| x | zephyyy7 | ^187 c6 | [@Will40746376 @Dexerto funny how last game this same crowd swore "no real woman ](https://x.com/zephyyy7/status/2065112542448374086) |
| x | gracia_vr | ^167 c4 | [We teamed up with researchers at Meta @RealityLabs to stress-test what's actuall](https://x.com/gracia_vr/status/2065106030539997345) |
| x | sidefx | ^155 c0 | [Houdini 22 launches in London next week! Join us at Curzon Soho Cinema for an ex](https://x.com/sidefx/status/2065141618509005226) |
| x | VFX_Therapy | ^120 c0 | [Tired of opening Photoshop for every tiny mask tweak? @KenDeng built a Unity Edi](https://x.com/VFX_Therapy/status/2065035196358094848) |
| x | The_Genesis_0 | ^120 c4 | [HOW TO: Create Realistic 3D Food in Blender in 10 steps. 1) Get Multiple referen](https://x.com/The_Genesis_0/status/2065394214771253289) |
| x | AurelienCa80656 | ^107 c3 | [We scanned the existing property using Gaussian Splatting, rebuilt the entire re](https://x.com/AurelienCa80656/status/2065420062861733906) |
| x | AKantemirov | ^100 c4 | [Took a few days to get procedural materials from @noaxdesign onto my model and s](https://x.com/AKantemirov/status/2065233326386843944) |
| x | janusch_patas | ^73 c1 | [A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting Abstract (excerp](https://x.com/janusch_patas/status/2064965130413048221) |
| x | RedefineFX | ^71 c2 | [Falcon 9 landing real-time VFX in Unreal 5.8, continuing with my space explorati](https://x.com/RedefineFX/status/2065047711477301342) |
| x | pablovelagomez1 | ^70 c5 | [There's been a few cool updates recently. In particular, @rerundotio 0.33 releas](https://x.com/pablovelagomez1/status/2065154703068193138) |
| x | DillyWillyVR | ^68 c2 | [Texturing a commission for my friend @Lightning260493 and here is the process! 🐾](https://x.com/DillyWillyVR/status/2065214193511326082) |
| x | drashyakuruwa | ^63 c8 | [A minor graphics update to the initial version of my GTA V-style game with @thre](https://x.com/drashyakuruwa/status/2065055670496276601) |
| x | zhenjun_zhao | ^44 c1 | [Wild3R: Feed-Forward 3D Gaussian Splatting from Unconstrained Sparse Photo Colle](https://x.com/zhenjun_zhao/status/2065032225423274347) |
| x | Deathbymetal87 | ^43 c2 | [if 420 of you guys donated to my kofi i could get an original 3d printed model o](https://x.com/Deathbymetal87/status/2065150122489430375) |
| x | fistandilus12 | ^42 c2 | [Funny how people who spent 20 years defending Photoshop, CGI, motion capture, pr](https://x.com/fistandilus12/status/2064943228340535490) |
| x | EnochsDegenCrib | ^41 c1 | [⭕️ $RENDER = The Decentralized GPU Powerhouse AI Actually Needs ⭕️💻🚀 Everyone's ](https://x.com/EnochsDegenCrib/status/2065155872914035156) |
| x | GSAIGETOA | ^41 c0 | [Update on Meeting of Team BDM with JS (Admin), DoT Shri K. Balaji on 09.06.2026 ](https://x.com/GSAIGETOA/status/2064954292612764048) |
| x | artjomwan | ^38 c0 | [Hey there! I have made this laser VFX in Unity today. I'm going to finish it but](https://x.com/artjomwan/status/2065148257274077527) |
| x | Oluwaphilemon1 | ^37 c1 | [This took 5 minutes. No rigging, no keyframes. Claude Fable 5 + any AI agent = l](https://x.com/Oluwaphilemon1/status/2065019441478332684) |
| x | LumaLabsAI | ^29 c5 | [Partnership is the new power move. Luma is at Cannes Lions 2026 with the partner](https://x.com/LumaLabsAI/status/2065092649518780723) |
| x | HeinerBuhr | ^24 c8 | [Some roses vanish in a few days. But Garden Roses — a 3D scan of real roses from](https://x.com/HeinerBuhr/status/2065081086233690316) |
| x | clore_ai | ^23 c5 | [Create detailed 3D models from images using https://t.co/tS1YgkSXYM's GPU-powere](https://x.com/clore_ai/status/2065457183811092985) |
| x | artfletch | ^22 c0 | [New #photogrammetry capture of Glengall Stairs and causeway on the Isle of Dogs.](https://x.com/artfletch/status/2065353199888851288) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3000 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2065400456591937620">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&quot;Keep moving forward.&quot; Our past should define us not hold us prisioner. TY for 600 followers over these last couple of days! Model: @Artstudious Rig: @cookie_sugar42 Shader: @LuminaryOfAges Textures: ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Blender artist โพสต์ fan animation จาก RWBY ฉลอง 600 followers โดย credit ทีม rig, shader, และ texture</dd>
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
    <span class="ndf-engagement">♥ 747 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IlirAliu_/status/2064979957009285375">View @IlirAliu_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One professor at the University of Bonn quietly put his entire robotics curriculum on YouTube: SLAM. Sensor fusion. State estimation. Probabilistic robotics. Self-driving cars. Motion planning. Photog”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Prof. Cyrill Stachniss จาก Univ. of Bonn เผยแพร่ curriculum robotics ทั้งชุดบน YouTube ฟรี ครอบคลุม SLAM, sensor fusion, photogrammetry, motion planning และ state estimation</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>SLAM และ photogrammetry เป็นเทคนิคหลักของ XR/VR spatial tracking และ 3D reconstruction มี lecture ระดับ university ให้ดูฟรีตรงประโยชน์กับทีม XR โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR บุ๊กมาร์ก playlist photogrammetry และ SLAM ไว้เป็น technical reference สำหรับงาน spatial anchoring หรือ environment scanning</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IlirAliu_/status/2064979957009285375" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GameZoneHQ</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 642 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GameZoneHQ/status/2065365759451148399">View @GameZoneHQ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Have a look at this impressive Unity real-time physics, created by VFX Artist @Sakura_Rabbiter #unity3d #gamedev #indiedev #madewithunity #unity #3dart #3d #unityengine #VFX #shader #RealTime #UE5 #3d”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@Sakura_Rabbiter VFX artist ปล่อย demo physics real-time ใน Unity ที่ใช้ custom shader + particle effects ร่วมกัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เห็น ceiling จริงของ Unity real-time physics + shader ปัจจุบัน — ใช้เป็น reference ตั้ง visual target ให้ทีม Unity และ XR ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู clip ที่ลิงก์ แล้วจด shader + physics setup เป็น benchmark สำหรับ VFX pass ถัดไปของทีม Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GameZoneHQ/status/2065365759451148399" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 474 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065457916405072127">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Someone needs to throw fable 5 at the OG of procedural 3D generation (houdini) and render it all in unreal engine https://t.co/QvVuHNhll7”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้แสดงความเห็นส่วนตัวว่าอยากให้ Fable 5 ใช้ Houdini สร้าง procedural 3D แล้ว render ใน Unreal Engine ไม่มีข้อมูลใหม่</dd>
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
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 365 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2065397660119716179">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Detailed breakdown of the flame vfx in one frame by @S_SerraMock in Unreal. #vfx https://t.co/i257Fz3YZt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@S_SerraMock ปล่อย breakdown แบบ frame-by-frame ของ flame VFX ที่สร้างใน Unreal Engine โดยแสดง layer ของ particle, shader, และ compositing</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Breakdown แบบนี้เปิดเผย layer logic และ shader trick ที่เอาไปใช้ใน Unity VFX Graph หรือ Shader Graph ได้เลย ไม่ติด engine</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม VFX ใช้ breakdown นี้เป็น reference ตอนสร้าง fire/flame ใน Unity VFX Graph สำหรับ game หรือ XR ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2065397660119716179" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@80Level</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 266 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/80Level/status/2065109302562422981">View @80Level on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo that lets you create the illusion of a furnished room behind a flat window surface. Get it here: https://t.co/w9rlA4b1an ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Amplify Creations ปล่อย 'Real Fake Interiors' สำหรับ Unity — ใช้ baking tool + shader จำลองห้องที่มีเฟอร์นิเจอร์อยู่หลังกระจกแบน โดยไม่ต้องสร้าง mesh ห้องจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ประหยัด performance มากกว่าการทำ interior mesh จริง เหมาะกับ Unity project ที่มีฉากตึก หรือ architectural visualization</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลองประเมิน asset นี้สำหรับฉากที่มีตึกหรือหน้าต่าง ลด geometry และ draw call ได้ทันที</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/80Level/status/2065109302562422981" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 248 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2065189214413611291">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา @RyanLykos แชร์ face rig ระหว่างทำใน Blender สำหรับตัวละคร Zhu Yuan แสดง bone structure และ shape key สำหรับ facial animation</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค face rigging ใน Blender ใช้ได้โดยตรงกับ character pipeline ของ Unity game และ XR ที่ต้องการ avatar หรือ NPC ที่แสดงสีหน้าได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR นำ bone layout และ shape key approach ของ rig นี้มาใช้เป็น reference ตอนสร้าง character asset ที่ต้องแสดงอารมณ์</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2065189214413611291" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@zephyyy7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 187 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/zephyyy7/status/2065112542448374086">View @zephyyy7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@Will40746376 @Dexerto funny how last game this same crowd swore &quot;no real woman looks like that,&quot; then Eve turned out to be a 3D scan of an adult Korean model. now an adult Korean face &quot;must be&quot; a chi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Twitter โต้ว่านักวิจารณ์อ่านหน้า Korean adult ผิดว่าเป็นเด็ก โดยอ้างสองเกมที่ใช้ 3D scan จากนางแบบ Korean ผู้ใหญ่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/zephyyy7/status/2065112542448374086" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
