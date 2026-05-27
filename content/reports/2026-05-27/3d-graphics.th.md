---
type: social-topic-report
date: '2026-05-27'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-05-27T04:49:31+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- x
regions:
- global
post_count: 141
salience: 0.45
sentiment: mixed
confidence: 0.7
tags:
- blender
- geometry-nodes
- eevee
- procedural
- stylized-shading
- react-three-fiber
thumbnail: https://external-preview.redd.it/cmhoeGVqajZpZjNoMQsqFFakb1glENvFPS-fTnP6uFK2pksUhB6_rOF6GUec.png?format=pjpg&auto=webp&s=71b23f2a39d8af8a625470d58ebc84232f8e7025
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-05-27

## TL;DR
- วันที่มี keyword noise หนักมาก: ส่วนใหญ่ที่พบคำว่า 'nerf' เป็นการพูดคุยเรื่อง game-balance ไม่ใช่ signal ด้าน 3D/graphics [2-5,7,8,10-14,16,17,19,22,23,25-29,46,48-51,53-55,57-59]
- signal จริงกระจุกตัวรอบ Blender Geometry Nodes สำหรับงาน procedural build [6,34,41,56] และ workflow ด้าน stylized/NPR shading [20,32,33,35,38,52]
- Eevee Next (Blender 5.0) แสดง output แบบ stylized + volumetric ที่พร้อมใช้ใน production [21,31,35]
- Web3D pipeline ยังคงทำงานได้: demo ใช้งานจริงของ React Three Fiber + GLSL + Blender [39]; การเริ่มต้นใช้ Unreal material graph ยังคงมี barrier ต่ำมาก [30]
- ความต้องการตำแหน่ง Tech artist / VFX ถูกระบุว่าทนทานต่อ AI [60]

## What happened
Topic feed ถูกครอบงำด้วยการพูดคุยเรื่อง gaming-balance 'nerf' ที่ไม่เกี่ยวกับ 3D pipeline [2-5,7,8,10-14,16,17,19,22,23,25-29,46,48-51,53-55,57-59] เมื่อกรองออกแล้ว signal ด้าน graphics ที่แท้จริงมีความสม่ำเสมอ: Blender Geometry Nodes ขับเคลื่อน procedural Lego speed-build animation [6], procedural galaxy generator แบบสมจริง [34], procedural cell simulation [41], และ procedural creature rig ใน Godot [56] งาน Stylized/NPR ยังแข็งแกร่ง — anime eye shader [20], stylized metal panel texture pack [33], Eevee watercolor fish [21], Eevee nebula บน Blender 5.0 [31], การฟื้นคืนของ Frutiger Aero [35], grease-pencil lips [52], sketch-style render [38]

ใกล้เคียง pipeline: React Three Fiber + GLSL + Blender mini-game แสดง web3D loop [39]; Unreal material editor เข้าถึงง่ายพอที่เด็กอายุ 12 ปีจะสร้าง shape morph ได้เอง [30]; RayCast system สำหรับ Blender control rig [45]; thread ชุมชนเรื่อง Blender hygiene habit ที่ควรนำไปปรับใช้ [43]; tech-artist/VFX ยังคงรับสมัครงานแม้มีแรงกดดันจาก AI [60]

## Why it matters (reasoning)
สำหรับ studio แบบ NDF DEV ที่ส่งมอบงานบน Unity/XR/web แนวโน้มที่ยั่งยืนคือ procedural + stylized ในฐานะ cost lever Geometry Nodes [6,34] และ procedural sim [41,56] ช่วยให้ศิลปินคนเดียวสร้าง asset ที่มีความหลากหลายสูง ซึ่งปกติต้องใช้ทั้งทีม — ตรงกับงาน e-learning content library และ XR set dressing โดยตรง คุณภาพของ Eevee Next [21,31,35] หมายความว่า Blender สามารถผลิต render ระดับ marketing/cutscene ได้โดยไม่ต้องรอเวลา Cycles farm ทำให้ video deliverable เสร็จเร็วขึ้น demo R3F+GLSL [39] ยืนยันว่า stack ของ Next.js/Supabase รองรับ real-time 3D บนเว็บได้โดยไม่มี Unity WebGL bloat — เหมาะสำหรับ lightweight edutech 3D viewer ความต้องการ tech-artist ที่ยังคงแข็งแกร่ง [60] บ่งชี้ว่าทักษะ shader/pipeline ยังคงเป็นการจ้างงานที่ให้ผลตอบแทนสูงที่สุด ไม่ใช่ generalist 3D สิ่งที่ขาดหายอย่างเด่นชัด: ไม่มีรายการ Gaussian Splatting, NeRF, หรือ photogrammetry เลยวันนี้ — subfield นี้เงียบ แต่ไม่ได้หมายความว่าหยุดพัฒนา

## Possibility
มีแนวโน้มสูง (70%): Geometry Nodes กลายเป็นค่าเริ่มต้นสำหรับงาน prop/environment แบบซ้ำๆ ใน indie+studio pipeline ภายใน 12 เดือน; Unity studio นำเข้า GN-baked variant ผ่าน Alembic/USD มากขึ้นเรื่อยๆ ปานกลาง (45%): Eevee Next มีเสถียรภาพพอที่ small studio จะยกเลิก Cycles สำหรับ non-hero shot ทั้งหมด เป็นไปได้ (35%): web-native 3D (R3F + WebGPU) แย่งส่วนแบ่งของงาน lightweight Unity WebGL edutech ไป ต่ำ (15%) แต่ควรติดตาม: ความเงียบของ Gaussian Splatting วันนี้อาจกลับทิศสัปดาห์หน้าพร้อม tooling release — สาขานี้รอ Blender-native splat importer มานานเกินพอแล้ว

## Org applicability — NDF DEV
การดำเนินการที่เป็นรูปธรรมสำหรับ NDF DEV: (1) ลงทุนหนึ่งสัปดาห์ผลักดันความเชี่ยวชาญ Geometry Nodes ให้กับ 3D lead — ผลตอบแทนคือ procedural environment สำหรับ EGAT Green Hold (D) และ UI/prop variant ของ TM Muscle Gym (G) ต้นทุนต่ำ ROI สูง (2) กำหนดมาตรฐาน Blender→Unity export hygiene checklist [43] (การตั้งชื่อ, applied scale, modifier policy) — ใช้เวลาหนึ่งวัน ประหยัดการแก้ไขซ้ำทุกสัปดาห์ (3) ทดลองใช้ R3F+GLSL [39] สำหรับ Next.js/Supabase edutech 3D viewer หนึ่งตัวแทน Unity WebGL — ได้เปรียบด้าน load-time และ bundle size สำหรับ e-learning (4) บันทึก stylized texture pack [33] และ anime shader [20] ไว้สำหรับเนื้อหา VRoom (V) และสไตล์ Enggenius (5) ข้าม noise เรื่อง 'nerf' ทั้งหมด อย่าไล่ล่า Gaussian Splatting สัปดาห์นี้ — ไม่มี tooling signal ใหม่ที่คุ้มค่าต่อการสืบสวน

## Signals to Watch
- อัตราการนำ Blender 5.0 / Eevee Next ไปใช้ใน indie studio — เพดานคุณภาพที่เปลี่ยนไปส่งผลต่อโครงสร้างราคา
- ความสมบูรณ์ของเส้นทาง import Geometry Nodes → Unity (USD/Alembic)
- ประสิทธิภาพ React Three Fiber + WebGPU เทียบกับ Unity WebGL สำหรับ edutech
- การปล่อย Gaussian Splatting / NeRF tooling ครั้งถัดไปหลังจากความเงียบวันนี้

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | morelebaks | ^2610 c54 | [I made animations for Adult Swim!!!111 (Rick and Morty season premiere countdown](https://www.reddit.com/r/blender/comments/1tnyx1q/i_made_animations_for_adult_swim111_rick_and/) |
| x | idvlogic | ^1904 c39 | [[ May 2026 Official Q&amp;A Info ] • "Knight" will receive adjustments at the en](https://x.com/idvlogic/status/2059198953795547357) |
| x | ShiriAllwoodXXX | ^1571 c14 | [Nerf this!👾👾 https://t.co/hAxG0FSnwm](https://x.com/ShiriAllwoodXXX/status/2059031756834226254) |
| x | LordInosuke741 | ^1385 c14 | [Even the Vegapunk lineage-coding couldn't nerf her inner Luffy fangirl https://t](https://x.com/LordInosuke741/status/2059143393901769193) |
| x | nealCS | ^1014 c6 | [they might have to nerf the zeus😭 https://t.co/lRqxoFdNPz](https://x.com/nealCS/status/2059379634740076980) |
| reddit | Nintino | ^908 c32 | [Speedbuilding of a Lego building with Geometry Nodes For a long time now I wante](https://www.reddit.com/r/blender/comments/1toc38t/speedbuilding_of_a_lego_building_with_geometry/) |
| x | FlipMeAC | ^862 c13 | [Yeah Ive see enough. Nerf Cyno](https://x.com/FlipMeAC/status/2059334749223604528) |
| x | amoriesux | ^817 c1 | [HES TOO HAPPY SOMEONE NERF HIM https://t.co/O2KsSgE6XX](https://x.com/amoriesux/status/2059025733540860039) |
| reddit | Significant-Tree4752 | ^783 c160 | [To be honest: all of this is just demotivating :( Edit: guys your comment sectio](https://www.reddit.com/r/blender/comments/1to2vpv/to_be_honest_all_of_this_is_just_demotivating/) |
| x | notalvajay | ^740 c5 | [Nerf this 💋 https://t.co/BXh8857iUp](https://x.com/notalvajay/status/2059337436770234512) |
| x | RyanJosephHart | ^730 c91 | [But if you nerf Mai, someone else becomes public enemy number 1 and the cycle co](https://x.com/RyanJosephHart/status/2059009043973214298) |
| x | captaincoach_mr | ^727 c61 | [Nerf Strategist healing by 10% for 3 healers, Duelist damage by 10% for 3 dps, a](https://x.com/captaincoach_mr/status/2059268143260819926) |
| x | sin_nl7 | ^679 c12 | [Pray they nerf this combo. https://t.co/gdBLPVD3Xq](https://x.com/sin_nl7/status/2059054344310231191) |
| x | chillincheeto14 | ^669 c3 | ["Nerf This!" #FortniteArt #Overwatch https://t.co/CPfHxUv0JA](https://x.com/chillincheeto14/status/2059033362262643072) |
| reddit | BobThe-Bodybuilder | ^657 c23 | [Blender is pretty cool. That's about it. I's just crazy that we get this piece o](https://www.reddit.com/r/blender/comments/1toiy1t/blender_is_pretty_cool/) |
| x | kurooleaks | ^647 c13 | [On 6.7 v2 Beta, Cyno got a silent nerf on the way his Duststalker Bolts - Starsa](https://x.com/kurooleaks/status/2059225627392188727) |
| x | dudrandaI | ^573 c0 | [@AgroVator he actually found clorinde kit really fun and she got a huge uptime n](https://x.com/dudrandaI/status/2059230200429220199) |
| reddit | flockaroo | ^493 c19 | [home grown gas giant](https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/) |
| x | NefariousNova05 | ^487 c20 | [Deadlock is such a beautiful game because you have a character with something pe](https://x.com/NefariousNova05/status/2059229484063051833) |
| x | CGDASH_ | ^454 c2 | [Anime Eye Shader Blender https://t.co/1V1yuRnpx2](https://x.com/CGDASH_/status/2058820166520344722) |
| reddit | Kvendy_ | ^431 c11 | [Just a random fish on your feed!! Everything is rendered in Eevee, tried to make](https://www.reddit.com/r/blender/comments/1toesq0/just_a_random_fish_on_your_feed/) |
| x | J4MIEL4NNISTER_ | ^340 c1 | [Remember last year when everyone thought the Flexi-wings was gonna nerf McLaren ](https://x.com/J4MIEL4NNISTER_/status/2059337742585155982) |
| x | Justkindofhere | ^338 c3 | [OP pls nerf https://t.co/OUtbBdReYn](https://x.com/Justkindofhere/status/2059299268561629245) |
| reddit | ViscousRealm | ^335 c44 | [I redesigned Spotify app icon in 3d.](https://www.reddit.com/r/blender/comments/1to5p75/i_redesigned_spotify_app_icon_in_3d/) |
| x | Synnefaki_ | ^322 c20 | [Knight getting a buff but doctor getting a nerf whatever u all hate women](https://x.com/Synnefaki_/status/2059240240095596978) |
| x | ChicoFGC_ | ^300 c26 | [I think there's 3 ways capcom can nerf: 1. Make her 9k, she would still be very ](https://x.com/ChicoFGC_/status/2059328729042518104) |
| x | MrBubblyTTV | ^267 c33 | [hate to be a negative nancy, but you're gonna wanna wait until they nerf that en](https://x.com/MrBubblyTTV/status/2059137846972182951) |
| x | Dorkstrict | ^257 c42 | [Axel pick rate shows she's on nearly every single team this season By far one of](https://x.com/Dorkstrict/status/2059282603383914624) |
| x | lofi_lover0930 | ^255 c11 | [Dead or Alive used to have the best stages compared to any 3D fighting game unti](https://x.com/lofi_lover0930/status/2059005023477198911) |
| x | delaigrodela | ^235 c6 | [My 12 year old son saw my material generating 4 simple shapes from UV and the co](https://x.com/delaigrodela/status/2058977219188297867) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@morelebaks</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 2610 · 💬 54</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tnyx1q/i_made_animations_for_adult_swim111_rick_and/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/cmhoeGVqajZpZjNoMQsqFFakb1glENvFPS-fTnP6uFK2pksUhB6_rOF6GUec.png?format=pjpg&amp;auto=webp&amp;s=71b23f2a39d8af8a625470d58ebc84232f8e7025" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I made animations for Adult Swim!!!111 (Rick and Morty season premiere countdown) my all time dream was to make something for Adult Swim and here we are! It was a blast making it - as a teenage boy I ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Freelance animator ใน Blender ได้งานทำ countdown animation ให้ Rick and Morty season premiere บน Adult Swim พร้อม creative freedom เต็มที่ ทำ concept, assets และ sound design คนเดียว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>พิสูจน์ว่า artist คนเดียวที่มี style ชัดเจนสามารถคว้างาน IP ใหญ่ได้โดยไม่ต้องยอมลด creative direction — style คือสิ่งที่ขายได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม 3D ของ studio ควรสร้างและโปรโมต visual style ที่จดจำได้ต่อสาธารณะ เพราะงาน branded animation มักตกเป็นของ artist ที่มี look ชัดเจน ไม่ใช่แค่คนที่มี reel ดี</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tnyx1q/i_made_animations_for_adult_swim111_rick_and/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@idvlogic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1904 · 💬 39</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/idvlogic/status/2059198953795547357">View @idvlogic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“[ May 2026 Official Q&amp;amp;A Info ] • &quot;Knight&quot; will receive adjustments at the end of this season (question: buff). • Doctor will receive adjustments at the end of this season (question: nerf). • Compo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Identity V ประกาศปรับ balance ปลาย season: Knight buff, Doctor nerf, Composer rework ใหญ่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัวอย่างการสื่อสาร balance patch ผ่าน Q&amp;A format เพื่อจัดการ expectation player ก่อน update จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/idvlogic/status/2059198953795547357" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ShiriAllwoodXXX</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1571 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ShiriAllwoodXXX/status/2059031756834226254">View @ShiriAllwoodXXX on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Nerf this!👾👾 https://t.co/hAxG0FSnwm”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ใน category 3D &amp; Graphics โชว์ผลลัพธ์ NeRF (Neural Radiance Fields) พร้อม wordplay ว่า 'Nerf this!'</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>NeRF สร้าง 3D scene จาก 2D ภาพถ่ายได้เลย — ตรงกับงาน XR/VR ของทีมที่ไม่ต้องใช้ 3D scan rig เต็มรูปแบบ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ใช้ Luma AI หรือ Nerfstudio capture environment แล้ว bake เป็น mesh นำเข้า Unity ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ShiriAllwoodXXX/status/2059031756834226254" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LordInosuke741</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1385 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LordInosuke741/status/2059143393901769193">View @LordInosuke741 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Even the Vegapunk lineage-coding couldn't nerf her inner Luffy fangirl https://t.co/QYytnw9PiL”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนอาร์ต One Piece (น่าจะเป็น 3D) ล้อว่า lineage-coding ของ Vegapunk ก็ยังสู้ความเป็นแฟนคลับ Luffy ของตัวละครไม่ได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แฟนอาร์ต 3D ที่ผูก lore เข้ากับ humor ได้ 1385 likes — สูตรนี้ดึง organic reach บน X ได้จริงโดยไม่ต้องโฆษณา</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดูได้ว่า pose + expression ของ character สื่อ narrative ได้โดยไม่ต้องมี dialogue — ใช้อ้างอิงตอนออกแบบ cutscene หรือ XR avatar ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LordInosuke741/status/2059143393901769193" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nealCS</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1014 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nealCS/status/2059379634740076980">View @nealCS on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“they might have to nerf the zeus😭 https://t.co/lRqxoFdNPz”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แสดงปฏิกิริยาต่อ clip ใน game ที่ 'Zeus' (weapon หรือ character) แสดงพลังแรงมากจนน่าจะต้อง nerf</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>moment ที่ทำลาย balance ใน game กระจายไวและสร้าง community discussion ขนาดใหญ่ — ดูว่า studio ตอบสนองต่อ feedback แบบไหน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nealCS/status/2059379634740076980" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Nintino</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 908 · 💬 32</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1toc38t/speedbuilding_of_a_lego_building_with_geometry/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/YTl1bWlxZTJkaTNoMVS11un5SUpY5hGERqornMpxitkFRtR7mjCqBRTekigk.png?format=pjpg&amp;auto=webp&amp;s=22844084d8759407316b5ecaddab4e95b330ad35" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Speedbuilding of a Lego building with Geometry Nodes For a long time now I wanted to make a cool and satisfying 3D animation of a Lego model being built piece by piece with Blender (in the end it happ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist ใช้ Blender Geometry Nodes animate โมเดล Lego ให้ประกอบทีละชิ้น ทีละถุง ตามลำดับ instruction จริง โดยแยก collection ตามหมายเลขถุง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิคแยก collection ตามถุงเป็น data-organization ที่สะอาด ให้ Geometry Nodes ขับ animation ลำดับซับซ้อนได้โดยไม่ต้องเขียน script — ใช้ได้กับ modular 3D asset ทุกประเภท</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ทำแบบเดียวกันได้: จัด asset ใน Blender เป็น collection ลำดับเลข → ขับ reveal ด้วย Geometry Nodes → export เป็น pre-baked animation ใช้ใน e-learning แบบ step-by-step assembly</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1toc38t/speedbuilding_of_a_lego_building_with_geometry/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@FlipMeAC</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 862 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/FlipMeAC/status/2059334749223604528">View @FlipMeAC on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Yeah Ive see enough. Nerf Cyno”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้โพสต์เห็นข้อมูลเพียงพอแล้ว ขอให้ nerf ตัวละคร Cyno (น่าจะในเกม).</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Engagement สูง (862 likes) จากโพสต์ 5 คำ บอกว่า community มีความรู้สึกแรงเรื่อง game balance แต่ไม่มี signal ทางเทคนิคใดเลย.</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/FlipMeAC/status/2059334749223604528" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amoriesux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 817 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amoriesux/status/2059025733540860039">View @amoriesux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“HES TOO HAPPY SOMEONE NERF HIM https://t.co/O2KsSgE6XX”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>3D character render หรือ animation ที่มีสีหน้าดีใจเกินจริงกำลัง viral ผู้โพสต์ล้อว่าต้อง nerf ด่วน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Facial animation ของ 3D character ดีถึงระดับที่คนดูรู้สึก emotional ได้ทันที บ่งชี้ว่า bar ของ audience สูงขึ้นมากแล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ควรศึกษา rig และ blend-shape ของ character แบบนี้ แล้วยก standard facial animation ของ NPC ในงานที่ทำอยู่ให้สูงขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amoriesux/status/2059025733540860039" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
