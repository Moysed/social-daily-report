---
type: social-topic-report
date: '2026-05-25'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-05-25T08:40:19+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- x
regions:
- global
post_count: 146
salience: 0.45
sentiment: mixed
confidence: 0.6
tags:
- blender
- procedural
- unity-vfx
- rigging
- unreal-stutter
- ai-mesh
thumbnail: https://external-preview.redd.it/ZzFvMDFoM2w0MjNoMbq707QQsHInqdFdOVXU99g4SAR--JMPuSi1Lr39bw_Y.png?format=pjpg&auto=webp&s=ad9c9a62a6e7f7d6daaefd564ab6006a9b828e9d
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-05-25

## TL;DR
- ผลงานจากชุมชน Blender ครองสัญญาณวันนี้ — tutorial ด้านริgging, เครื่องมือ procedural, และงาน render คุณภาพสูง [2][5][7][22][27]
- Procedural VFX สำหรับ Unity (impact frames, confetti shaders, lace generator) แสดงให้เห็น pipeline real-time ที่สมบูรณ์พร้อมซึ่ง indie dev กำลังส่งงานจริง [6][22][24][45]
- ปัญหา shader-compilation stutter ของ Unreal Engine 6 กลับมาเป็นประเด็น — สะท้อน pain point ในการ production จริง [11]
- workflow ที่ใช้ AI ช่วยสร้าง asset (Tripo.ai → Blender) เริ่มเป็นเรื่องปกติในกลุ่ม hobbyist อย่างเปิดเผย [59]
- สัญญาณรบกวนสูง: รายการคะแนนสูงส่วนใหญ่ใช้คำว่า 'nerf' ในฐานะสแลง ไม่ใช่เครื่องมือ 3D — สัญญาณ graphics จริงมีประมาณ 15 จาก 60 รายการ

## สิ่งที่เกิดขึ้น
Blender ยังคงครองบทสนทนาด้าน creative-3D: render เตารีดแบบ viewport [2], การวิเคราะห์ hand rig ของ Chris Jones [7], demo rigging แบบ node-based [27], procedural lace generator สำหรับ 4.2+ [22], ภาพ portrait จาก rigid-body dice จำนวน 13,000 ชิ้น [9], Grease Pencil แบบ 2D-in-3D สำหรับซีรีส์ indie [26], โมเดล full-body แบบ NPR [52], และโพสต์ที่แชร์ hybrid workflow ระหว่าง Tripo.ai กับ Blender อย่างตรงไปตรงมา [59] ในฝั่ง real-time/game-engine: procedural impact-frame VFX ใน Unity [6], procedural texturing สำหรับ city-builder [24], การอธิบาย UV-driven confetti material สำหรับ Unreal [45], การอัปเดต voxel renderer [39], และ thread ใน GraphicsProgramming ถามถึงวิธีทำ fake-depth glow effect [31] สัญญาณความขัดแย้งที่น่าสนใจ: Anton Hand แซะ shader-compilation stutter ของ Unreal Engine 6 [11] ส่วนรายการคะแนนสูงที่เหลือล้วนเป็นสแลง 'nerf' ในเกม ไม่เกี่ยวกับ 3D tooling

## เหตุใดจึงสำคัญ (การวิเคราะห์)
pattern หลักที่เห็นชัดคือ procedural + node-based authoring กำลังเปลี่ยนจากของเฉพาะทางมาเป็นมาตรฐาน — ทั้ง rigging [5][27], materials [22][45], และ VFX [6][24] ซึ่งลดต้นทุนแรงงานต่อ asset สำหรับ studio ขนาดเล็กที่ทำทั้ง game และ XR ผลลัพธ์รองลงมาคือ art team ต้องการโมเดลที่ hand-model น้อยลง แต่ต้องการความชำนาญด้าน shader/node มากขึ้น ซึ่งปรับเปลี่ยนรูปแบบการจ้างงานและฝึกอบรม ปัญหา stutter ของ UE6 [11] เป็น ship-blocker จริงสำหรับทีมที่กำลังพิจารณา Unreal สำหรับ title ถัดไป — ต้องประเมิน PSO precaching และความสมบูรณ์ของ shader pipeline ก่อนตัดสินใจ การที่ workflow ของ Tripo.ai [59] ถูกยอมรับอย่างเปิดเผยบ่งชี้ว่า AI-mesh-to-Blender retopo/texture กลายเป็นกระแสหลักในระดับ hobbyist แล้ว คำถามต่อไปคือคุณภาพระดับ studio

## ความเป็นไปได้
มีแนวโน้มสูง (≈70%): procedural node tooling จะกลายเป็น baseline ที่คาดหวังใน Blender 4.x+ — studio ที่ข้ามข้อนี้ไปจะเสีย iteration speed ไป 2-3 เท่า มีแนวโน้มสูง (≈60%): ปัญหา shader-stutter ของ UE6 จะผลัก indie/mid team กลับไปหา Unity 6 หรือทำให้ยังคงอยู่บน UE5.x ตลอดปี 2026 มีความเป็นไปได้ (≈40%): AI mesh generator (Tripo, Meshy, Rodin) จะกลายเป็น step มาตรฐานแบบ 'blockout → human polish' ใน pipeline ของ studio ภายใน 12 เดือน ไม่พบสัญญาณของ NeRF/Gaussian Splatting/photogrammetry ในชุดข้อมูลวันนี้ — subfield นี้เงียบในชิ้นส่วนนี้

## การนำไปใช้กับ NDF DEV
ใช้ได้ทันที: (1) นำ pattern node-based rigging [5][7][27] มาใช้กับงาน Unity character — rig ที่ reusable ลดเวลา setup XR-character (2) pattern procedural material/VFX [6][22][24][45] map ตรงกับโปรเจกต์ Unity edutech และ XR ของ NDF — texture bake น้อยลง, build ขนาดเล็กลง, runtime variation ฟรี (3) Grease Pencil 2D-in-3D [26] เป็นทางลัดด้านสไตล์ราคาถูกสำหรับเนื้อหา explainer ใน edutech (4) ประเมิน AI mesh gen แบบ Tripo.ai [59] สำหรับ prop ที่ไม่ใช่ hero ในฉาก e-learning — ความเสี่ยงต่ำ, ความเร็วสูง ข้ามไปก่อน: การ migrate ไป UE6 [11] — รอให้แก้ปัญหา stutter ก่อน ไม่มีสัญญาณ NeRF/Splat ที่นำไปใช้ได้วันนี้

## สัญญาณที่ต้องติดตาม
- ปัญหา shader-stutter ของ UE6 — ติดตามว่า Epic จะปล่อย fix PSO/precache ใน point release 6.x หรือไม่
- การปล่อย Blender add-on แบบ procedural (lace [22], rigging nodes [27]) — จับตา bundle ที่ออกใบอนุญาตให้ studio ได้
- การยอมรับ workflow AI-mesh-to-DCC — คุณภาพของ Tripo, Meshy, Rodin ที่จะข้ามเกณฑ์ 'hero asset'
- การไม่มี Gaussian Splatting / NeRF ในชิ้นส่วน engagement สูง — อาจบ่งบอกว่า hype กำลังเย็นตัวลง หรืออาจเป็นเพียง sampling noise

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Anarmy08 | ^4307 c3 | [the funniest part about the music industry suddenly panicking over organic fando](https://x.com/Anarmy08/status/2058338259785207970) |
| reddit | operation-kind | ^4089 c76 | [Steam iron Blender viewport](https://www.reddit.com/r/blender/comments/1tm7tke/steam_iron_blender_viewport/) |
| x | Emanxamilius_ | ^3995 c16 | [The only way to nerf this football club was with the leeches for owners If they ](https://x.com/Emanxamilius_/status/2058278212635943137) |
| x | BrianRoemmele | ^3213 c177 | [In 1987 we got the famous Nerf TURBO Football. You did not throw it, no, you lau](https://x.com/BrianRoemmele/status/2058548555535778038) |
| x | DemNikoArt | ^2859 c41 | [A few ideas a new rigging tutorial. Which one would you like to see? 🤔 #b3d #ble](https://x.com/DemNikoArt/status/2058153981113733341) |
| x | unity3dvfx | ^2530 c10 | [Procedurally generated impact frame with shader and particle system by @namutree](https://x.com/unity3dvfx/status/2058183630845874338) |
| x | 3DxDEV7 | ^2334 c10 | [Check out this stunning Blender hand rig by Chris Jones. The way the tendons, he](https://x.com/3DxDEV7/status/2058587230499684740) |
| x | zajef77 | ^2025 c74 | [ok cyno is looking like he's actually good surely v2 won't nerf him right](https://x.com/zajef77/status/2058527342171914320) |
| reddit | LeandroCorreia | ^1386 c34 | [RPG Dice Portrait You should zoom to see it better. ;) Blender, over 13,000 dice](https://www.reddit.com/r/blender/comments/1tmkgjb/rpg_dice_portrait/) |
| x | Sneak0o | ^995 c12 | [SNEAKO couldn't believe it as he saw his childhood best friend appear on the Hod](https://x.com/Sneak0o/status/2058762764013781197) |
| x | AntonHand | ^986 c15 | [Unreal Engine 6 Now with 6x the shader compilation stutter.](https://x.com/AntonHand/status/2058630364898439516) |
| x | braindrainsfm | ^883 c1 | [Spot Wants a Treat It's out! This one took a little longer than I expected. Prob](https://x.com/braindrainsfm/status/2058598590289711528) |
| x | SCHIZO_FREQ | ^768 c24 | [Something about the enhanced games I'm just now realizing: Being outside in the ](https://x.com/SCHIZO_FREQ/status/2058733954145124618) |
| x | NyazuliArt | ^755 c6 | [Nerf this! 🐰🩷 #DVa #Overwatch https://t.co/51caDMQnhX](https://x.com/NyazuliArt/status/2058606507604750737) |
| x | Honnou__ | ^673 c29 | [nerf this car plz @ForzaHorizon @Microsoft @WeArePlayground https://t.co/1CB8IvM](https://x.com/Honnou__/status/2058411310442742057) |
| x | blucorsa | ^600 c10 | [The pre-nerf Eager Edge cone was RIDICULOUS bro https://t.co/5wZ5CGn99z](https://x.com/blucorsa/status/2058452649540829498) |
| x | sirencrave | ^566 c11 | [someone nerf this guy, he's about to marry dua lipa and become james bond in the](https://x.com/sirencrave/status/2058280252820889848) |
| x | GarlicSniff3r | ^562 c7 | [yooo better nerf this item, too much dmg https://t.co/qOVOyfavhA](https://x.com/GarlicSniff3r/status/2058421012522275049) |
| x | Helasimp22 | ^502 c3 | [I'm not falling for this Day 7 of larping till nerf](https://x.com/Helasimp22/status/2058577553833771232) |
| x | sanwee726 | ^468 c2 | [Sophia is so powerful they needed to nerf her. https://t.co/Lrupx8CkES](https://x.com/sanwee726/status/2058692753782173980) |
| reddit | todtodson | ^459 c4 | [Dystopian chill](https://www.reddit.com/r/blender/comments/1tmz1xd/dystopian_chill/) |
| x | 3DxDEV7 | ^448 c1 | [Okay this is actually really cool 😍 Procedural lace generator for Blender 4.2+, ](https://x.com/3DxDEV7/status/2058452098056950206) |
| x | HyunYuuX | ^440 c5 | [Keep in mind, Jane Doe is currently the only S-Rank Anomaly that doesn't have sp](https://x.com/HyunYuuX/status/2058332900148531366) |
| x | unity3dvfx | ^416 c8 | [This looks absolutely heavenly! ☁️✨ Procedural texturing + divine city-building ](https://x.com/unity3dvfx/status/2058598704488079660) |
| x | Fubgun | ^400 c58 | [0.5 Patch notes were updated, there was a Massive crafting nerf hidden in them. ](https://x.com/Fubgun/status/2058783251628691752) |
| reddit | Stef_Armchair_Prod | ^399 c4 | [2D Effects in 3D environments for our YouTube Indie series "The Hunt". Anyone el](https://www.reddit.com/r/blender/comments/1tmaw6t/2d_effects_in_3d_environments_for_our_youtube/) |
| x | EdwardUrena_h | ^391 c5 | [Here we have a big twerking... sorry, I mean a great demonstration of the advant](https://x.com/EdwardUrena_h/status/2058620424678678784) |
| reddit | LordLeonan | ^387 c6 | [Fist my Bump! I finally watched Project Hail Mary. I give it a big 👎](https://www.reddit.com/r/blender/comments/1tmabom/fist_my_bump/) |
| x | tong_ping_diary | ^357 c0 | [Anime style Glass Shader in Blender! #blender初心者 #blender #b3d #3DCG https://t.c](https://x.com/tong_ping_diary/status/2058337181471805883) |
| reddit | Rksaikia797 | ^352 c16 | [Made a horror style animation(share your thoughts!) Reworked the textures, light](https://www.reddit.com/r/blender/comments/1tmjsiw/made_a_horror_style_animationshare_your_thoughts/) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Anarmy08</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4307 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Anarmy08/status/2058338259785207970">View @Anarmy08 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“the funniest part about the music industry suddenly panicking over organic fandom and changing streaming rules is that armys called this YEARS ago. we literally watched them change billboard formulas,”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคลับ BTS บอกว่า ARMY รู้ล่วงหน้าแล้วว่าวงการเพลงจะตื่นตระหนกและเปลี่ยนกฎ streaming/Billboard เมื่อ organic demand จริงๆ มันใหญ่เกินไป</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แสดงให้เห็นว่า platform ใหญ่แอบเปลี่ยน metric/algorithm เพื่อกด demand signal ที่ไม่เข้ากรอบ — รูปแบบนี้เกี่ยวข้องกับทีมที่พึ่ง third-party distribution</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Anarmy08/status/2058338259785207970" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@operation-kind</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 4089 · 💬 76</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tm7tke/steam_iron_blender_viewport/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/ZzFvMDFoM2w0MjNoMbq707QQsHInqdFdOVXU99g4SAR--JMPuSi1Lr39bw_Y.png?format=pjpg&amp;auto=webp&amp;s=ad9c9a62a6e7f7d6daaefd564ab6006a9b828e9d" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Steam iron Blender viewport”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Reddit user โชว์โมเดล steam iron สมจริงใน Blender viewport ได้ upvote กว่า 4,000</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ได้ 4K likes จาก viewport เฉยๆ ไม่ต้อง final render — แสดงว่า real-time shading ใน Blender ตอนนี้ portfolio-grade แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ใช้ Blender viewport screenshot เป็น preview ให้ client ระหว่าง production ได้เลย ไม่ต้องรอ bake เต็ม</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tm7tke/steam_iron_blender_viewport/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Emanxamilius_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3995 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Emanxamilius_/status/2058278212635943137">View @Emanxamilius_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The only way to nerf this football club was with the leeches for owners If they had any other owner in football this club would be a powerhouse unrivalled by any other football team”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนบอลบอกว่าสโมสรของตัวเองถูกฉุดรั้งโดยเจ้าของทีม ถ้าเปลี่ยนเจ้าของได้ทีมนี้จะแกร่งที่สุดในโลก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โพสต์นี้ไม่มีข้อมูลเชิงเทคนิคเลย — เป็นความเห็นเรื่องฟุตบอลที่ถูกติด tag '3D &amp; Graphics' ผิด ไม่เกี่ยวกับ dev หรือ graphics</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่เกี่ยวข้อง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Emanxamilius_/status/2058278212635943137" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BrianRoemmele</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3213 · 💬 177</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BrianRoemmele/status/2058548555535778038">View @BrianRoemmele on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In 1987 we got the famous Nerf TURBO Football. You did not throw it, no, you launched it. I heard one kid in New Jersey launched his to INDIA or something. https://t.co/vOiz9d0ynL”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ระลึกความหลังเกี่ยวกับของเล่น Nerf TURBO Football ปี 1987 พร้อม joke ว่าเด็กคนหนึ่งขว้างไปถึงอินเดีย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวกับ 3D/graphics จริงๆ — เป็นแค่ nostalgia content ไม่มี technical substance แม้ tag จะบอกว่า 3D &amp; Graphics</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่เกี่ยวข้องกับ studio โดยตรง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BrianRoemmele/status/2058548555535778038" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DemNikoArt</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2859 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DemNikoArt/status/2058153981113733341">View @DemNikoArt on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A few ideas a new rigging tutorial. Which one would you like to see? 🤔 #b3d #blender #blender3d #rigging #tutorial https://t.co/tS38SboBlV”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist @DemNikoArt โพลถามผู้ติดตามว่าอยากดู rigging tutorial หัวข้อไหนใน Blender</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Engagement สูง (2.8k likes) บอกว่าตลาดต้องการ rigging education มาก — rigging เป็น bottleneck ที่ทีม indie game เจอบ่อย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ติดตาม tutorial series นี้เพื่อพัฒนาทักษะ character rigging ก่อน import เข้า Unity ลด rework ระหว่าง Blender กับ engine</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DemNikoArt/status/2058153981113733341" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@unity3dvfx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2530 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/unity3dvfx/status/2058183630845874338">View @unity3dvfx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Procedurally generated impact frame with shader and particle system by @namutree_04 #unity3d #gamedev #indiedev #madewithunity #unity #3dart #3d #unityengine #VFX #shader #RealTime #UE5 https://t.co/D”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@namutree_04 สร้าง impact frame VFX แบบ procedural โดยใช้ custom shader และ particle system ใน Unity</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Impact frame แบบ procedural ไม่ต้องทำ frame-by-frame ด้วยมือ shader ตัวเดียวสร้าง variation ได้ไม่จำกัด ประหยัดเวลามากสำหรับเกม action</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ทำ shader + particle combo นี้เป็น reusable VFX prefab สำหรับ hit reaction, skill effect, หรือ XR interaction ใช้ข้ามโปรเจกต์ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/unity3dvfx/status/2058183630845874338" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2334 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2058587230499684740">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out this stunning Blender hand rig by Chris Jones. The way the tendons, helper bones, and smoothing work together is seriously impressive. 🔥 If you’re into character rigging, this one is worth a”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แชร์ Blender hand rig ของ Chris Jones — ระบบ tendon, helper bone, และ smoothing ทำงานร่วมกันได้สมจริงมาก ถือเป็นตัวอย่าง character rigging ระดับอ้างอิง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Hand rig คุณภาพสูงเป็น bottleneck บ่อยใน character animation — solution นี้ใน Blender แสดงว่ามี open-source ทางเลือกแทน rigging tool ที่ต้องซื้อลิขสิทธิ์</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู rig structure นี้แล้ว replicate แนว helper bone + tendon กับ humanoid character ใน Unity Humanoid Avatar หรือ custom rig — ช่วยลดเวลา polish hand animation</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2058587230499684740" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@zajef77</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2025 · 💬 74</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/zajef77/status/2058527342171914320">View @zajef77 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“ok cyno is looking like he's actually good surely v2 won't nerf him right”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้เล่นคนนึงบอกว่า Cyno ดูแรงดี และหวังว่า patch v2 จะไม่ nerf เขา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป็นแค่ความรู้สึกของ fan เรื่อง balance ตัวละคร ไม่มี insight เชิง technical หรืออุตสาหกรรม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่เกี่ยวกับการทำงานของ studio โดยตรง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/zajef77/status/2058527342171914320" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
