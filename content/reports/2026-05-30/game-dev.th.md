---
type: social-topic-report
date: '2026-05-30'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-30T18:23:38+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 39
salience: 0.55
sentiment: neutral
confidence: 0.6
tags:
- unity
- ai-pipeline
- image-to-3d
- godot
- tooling
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060606108763295745/img/-oeMxhDSxmtuOXkf.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-30

## TL;DR
- Microsoft ปล่อย Trellis.2 โมเดล open-source ขนาด 4B แปลงภาพเป็น textured 3D mesh ใน ~3 วินาที (mesh ต่ำกว่า 100ms บน CUDA) export เป็น GLB สำหรับ Blender, Unity และ Unreal [3].
- Unity AI เปิดตัวสามโหมดใน editor — Ask (Q&A), Plan (workback พร้อม safeguards) และ Agent (อัตโนมัติงานซ้ำ) [21].
- Godot 4.7 beta 4 ออกแล้ว คาด Release Candidate ใกล้มาถึง [5].
- มีการปล่อย open-source Unity character controller รองรับ moving platforms และ wall collisions [2]; Unity โปรโมต Unity Studio เว็บ editor แบบ no-code สำหรับ industrial 3D apps [29][31].
- ด้านธุรกิจ: Playstack สำนักพิมพ์ Balatro กำลังถูกขายในราคา ~$169M ให้บริษัทแม่ของ GameSpot/Fandom [35]; 007 First Light ทำยอดขายเกิน 1.5M ชุด [36].

## What happened
ฝั่ง tooling/AI: Microsoft ปล่อย Trellis.2 โมเดล open-source ขนาด 4B แปลงภาพเป็น textured GLB mesh ใน ~3 วินาที พร้อมใช้งานใน Blender, Unity และ Unreal [3]. Unity เปิดตัว in-editor AI สามโหมด: Ask, Plan และ Agent [21] พร้อมโปรโมต Unity Studio เว็บ editor แบบ no-code สำหรับ industrial/real-time 3D apps [29][31]. Godot 4.7 beta 4 ออกก่อน RC ที่วางแผนไว้ [5] และ Unreal เผยแพร่ learning material UE5 ฟรีเรื่อง cinematic environments และ Substrate glass [6]. ฝั่ง community/asset คึกคักตามปกติ: open-source Unity character controller สำหรับ moving-platform และ wall-collision edge cases [2], procedural Unity world tools โดยใช้ splines และ Voronoi grids [12][18][14] รวมถึงโพสต์ shader/VFX และ asset-store ต่างๆ [4][23][8][16].

## Why it matters (reasoning)
สิ่งที่เป็นรูปธรรมสำหรับ studio แบบ NDF DEV คือ Trellis.2 [3]: image-to-3D ที่เร็ว, open-source, license เป็นมิตรกว่า export ตรงเข้า Unity/Unreal pipeline ช่วยย่น early prototyping และงาน placeholder asset แม้คุณภาพ mesh ระดับ production ยังไม่มีการยืนยัน. กรอบ Ask/Plan/Agent ของ Unity AI [21] บ่งชี้ว่า editor กำลังกลายเป็น assistant surface ซึ่งสำคัญเพราะ AI assistants ของทีมเริ่มทับซ้อนกับของ engine vendor. Unity Studio แนว no-code industrial บนเว็บ [29][31] ชี้ว่า Unity มุ่งรายได้ enterprise/XR-visualization นอกเหนือเกม — เกี่ยวข้องกับงาน XR/edutech ของ NDF DEV โดยตรง. ความก้าวหน้าของ Godot 4.7 [5] ทำให้ทางเลือก open-source สุกงอมขึ้น ลดความเสี่ยง lock-in. รายการธุรกิจ [35][36][38][39] ส่วนใหญ่สะท้อนการควบรวมและความตึงเครียดด้านแรงงานในอุตสาหกรรมกว้าง ไม่มีการดำเนินการทางเทคนิคโดยตรง.

## Possibility
มีแนวโน้ม: เครื่องมือ image-to-3D อย่าง Trellis.2 จะถูกนำเข้า rapid prototyping และ concept pass เพราะ open-source license และเส้นทาง GLB→Unity/Unreal ตรง [3]. เป็นไปได้: in-editor AI agents (Unity's Agent mode) เริ่มจัดการงาน setup/refactor ซ้ำ แต่การใช้จริงขึ้นอยู่กับความน่าเชื่อถือที่โพสต์ยังไม่แสดง [21]. เป็นไปได้: Godot 4.7 ถึง RC แล้ว stable ในสัปดาห์ถัดไปตามที่ระบุ [5]. ไม่น่าเกิดขึ้น (จากรายการเหล่านี้): ดีลธุรกิจใดๆ [35][36] จะเปลี่ยนการตัดสินใจด้าน tooling ของ NDF DEV. ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น.

## Org applicability — NDF DEV
1) ทดลอง Trellis.2 บน throwaway branch สำหรับ placeholder/greybox 3D assets และตรวจ mesh quality, topology และ license terms ก่อนนำเข้า pipeline — effort ต่ำ [3]. 2) ประเมิน Unity AI Plan/Agent modes เทียบกับ AI assistants ที่ทีมใช้อยู่ เพื่อดูว่างาน editor ซ้ำอะไรที่ offload ได้ — effort ต่ำ/กลาง [21]. 3) จดบันทึก Unity Studio สำหรับงาน client ด้าน XR/edutech ที่ต้องการ no-code web 3D ในฐานะทางเลือกส่งมอบ — effort ต่ำในการประเมิน [29][31]. 4) ถ้า open-source character controller เหมาะกับ Unity prototype ปัจจุบัน ให้ดู [2] ก่อนสร้างใหม่เอง — effort ต่ำ [2]. ข้าม: รายการธุรกิจ/M&A และแรงงาน [35][36][38][39] (รับรู้เท่านั้น ไม่ต้องดำเนินการ) และโปรโมต asset-store sales และ screenshot [8][16][9][17].

## Signals to Watch
- คุณภาพ/ความสุกงอมของ license image-to-3D open-source — Trellis.2 และรุ่นต่อๆ ไปที่เข้าสู่ pipeline จริง [3].
- ความน่าเชื่อถือและราคาของ Unity AI Agent mode ขณะเปลี่ยนจาก demo สู่การใช้งาน editor รายวัน [21].
- กำหนด RC/stable ของ Godot 4.7 ในฐานะ open-source engine [5].
- การผลักดัน enterprise/industrial ของ Unity (Unity Studio) สะท้อนลำดับความสำคัญที่เกินกว่า game tooling [29][31].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ID_AA_Carmack | ^1189 c135 | [I have difficulty arguing that most of the writing changes suggested in gmail no](https://x.com/ID_AA_Carmack/status/2060399696955195843) |
| x | jettelly | ^824 c3 | [Developer thesquirrelyjones released an open-source custom character controller ](https://x.com/jettelly/status/2060617205989965911) |
| x | RoundtableSpace | ^217 c20 | [Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D ](https://x.com/RoundtableSpace/status/2060477532537827633) |
| x | DAVFX_0 | ^203 c3 | [Anomaly with Illugen #vfx #realtimevfx #illugen #gamedev #unity3d https://t.co/j](https://x.com/DAVFX_0/status/2060306891687809144) |
| x | godotengine | ^190 c7 | [One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for ](https://x.com/godotengine/status/2060503643057496501) |
| x | UnrealEngine | ^163 c8 | [Free learning content for the 5th month of the year? Yeah, we May just have some](https://x.com/UnrealEngine/status/2060396306934436123) |
| x | itchio | ^149 c0 | [Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playa](https://x.com/itchio/status/2060511506815746558) |
| x | ushadersbible | ^139 c0 | [Hey guys, the Technical Art Unity Bundle is 70% OFF 🎁 https://t.co/1eA8907m5M #g](https://x.com/ushadersbible/status/2060220692675678422) |
| x | UnrealEngine | ^72 c19 | [We know that #ScreenshotSaturday is always out of this world So, show us what in](https://x.com/UnrealEngine/status/2060723065991131533) |
| x | itchio | ^65 c0 | [The Board Is Yours: A strategic chess-based incremental game. https://t.co/BHK6Y](https://x.com/itchio/status/2060360518469353950) |
| x | itchio | ^61 c2 | [Pitchfork (Game Boy/ PC): Discover a pitchfork, throw it to a wall and bounce of](https://x.com/itchio/status/2060149120296251856) |
| x | jettelly | ^60 c1 | [Developer Sapra shared how the spline-based road system works in their tool, Inf](https://x.com/jettelly/status/2060360513335549985) |
| x | itchio | ^55 c0 | [Trigwa: Statue pushing game with a narrative. Each puzzle tells part of a larger](https://x.com/itchio/status/2060405812057780236) |
| x | R2RGames | ^52 c0 | [Almost 300 followers! Here is more progress on my medieval builder, spline walls](https://x.com/R2RGames/status/2060462094802379049) |
| x | _vazgriz | ^47 c4 | [Learn how to write an autopilot for a flight sim game in my newest blog post (li](https://x.com/_vazgriz/status/2060061124456808885) |
| x | MalberShark | ^46 c0 | [🐶 Skye (Dog) #polyart version is NOW LIVE on the @AssetStore! Easily one of my f](https://x.com/MalberShark/status/2060145030518432219) |
| x | MortalCrux | ^45 c5 | [A mind-blowing magic finisher 🧙‍♀️ #indiegamedev #indiegame #unity3d #pcgamer #m](https://x.com/MortalCrux/status/2060702882001731819) |
| x | unity3dvfx | ^43 c0 | [This is so clean 🔥by @GbrosGames Procedural island generation with Voronoi grids](https://x.com/unity3dvfx/status/2060093851675541880) |
| x | MJF_game | ^43 c13 | [Modern Jet Fighters Online is now live in Canada 🇨🇦 #Multiplayer #JetFighters #O](https://x.com/MJF_game/status/2060349067666899320) |
| x | mazestalker | ^41 c1 | [I love going back to my pre-URP areas and updating them with 2 years of experien](https://x.com/mazestalker/status/2060495924523135169) |
| x | unitygames | ^40 c3 | [Meet Unity AI's three modes: Ask, Plan, and Agent. 1️⃣ Ask: Get your questions a](https://x.com/unitygames/status/2060435608732836007) |
| x | R2RGames | ^38 c1 | [Fluffy clouds, chill afternoon vibes! #unity3d #gamedev https://t.co/NbXBUTIAFK](https://x.com/R2RGames/status/2060120197311410405) |
| x | jettelly | ^35 c0 | [Check out this tree shader by Sqrek, going through the seasons by changing leaf ](https://x.com/jettelly/status/2060239719481405445) |
| x | Rustledust77 | ^34 c1 | [Texturing workflow for our @FracturedRTS units: -&gt; Assign trim sheet material](https://x.com/Rustledust77/status/2060279247491465611) |
| x | JasozzGames | ^33 c0 | [intellisense please stop this when have i *ever* used that property #gamedev #un](https://x.com/JasozzGames/status/2060361262064599358) |
| x | itchio | ^27 c0 | [Tango Zero: Space is a tough job (Buy now!) https://t.co/OGlGrTd3dz by @Remanenc](https://x.com/itchio/status/2060088722289492206) |
| x | FreyaHolmer | ^26 c0 | [@edmundmcmillen I would love to voice some cats!! @TylerGlaiel said I wasn't coo](https://x.com/FreyaHolmer/status/2060326276724916311) |
| x | itchio | ^23 c0 | [Dungeons of Freeport: An Extraction Roguelike Dungeon-Crawler https://t.co/2L6EX](https://x.com/itchio/status/2060451112503722298) |
| x | unity | ^22 c1 | [Think building interactive 3D apps for industry has to be slow and complicated? ](https://x.com/unity/status/2060345542803173429) |
| x | godotengine | ^13 c0 | [Featured game: Elfie: A Sand Plan https://t.co/JAOBcSXMGt](https://x.com/godotengine/status/2060503644617740388) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1189 · 💬 135</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2060399696955195843">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I have difficulty arguing that most of the writing changes suggested in gmail now aren’t improvements, but it does tend to wipe out my particular authorial voice.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>John Carmack สังเกตว่า AI ใน Gmail แนะนำการเขียนที่ดีกว่าในแง่เทคนิค แต่ลบเอกลักษณ์การเขียนของเขาออกไปด้วย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ID_AA_Carmack/status/2060399696955195843" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 824 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2060617205989965911">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer thesquirrelyjones released an open-source custom character controller for Unity, designed to handle edge cases like moving platforms and wall collisions. 🎮 See more: https://t.co/fpq8pSxsLi ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer thesquirrelyjones ปล่อย open-source character controller สำหรับ Unity ที่รองรับ edge cases อย่าง moving platforms และ wall collisions</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ประหยัดเวลาทีม Unity ไม่ต้องสร้าง character controller ใหม่ทุกโปรเจกต์ edge cases พวก moving platforms มาให้แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู repo นี้ก่อนเขียน locomotion code เองในโปรเจกต์ Unity ถัดไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2060617205989965911" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RoundtableSpace</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 217 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RoundtableSpace/status/2060477532537827633">View @RoundtableSpace on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D asset in 3 seconds. Textured mesh under 100ms on CUDA, outputs a GLB file ready for Blender, Unity, and Unreal. Open sou”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Microsoft ปล่อย Trellis.2 โมเดล open-source ขนาด 4B parameters แปลงภาพเป็น textured GLB mesh ใน ~3 วินาที บน CUDA ใช้งานได้ทันทีใน Blender, Unity, Unreal</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แปลงภาพเป็น GLB ใน 3 วินาที ลดเวลา prototype 3D assets ของทีม Unity จากชั่วโมงเหลือไม่กี่นาที</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">รัน Trellis.2 บนเครื่อง CUDA ป้อน concept art หรือรูป reference เพื่อสร้าง draft GLB สำหรับ prototype ใน Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RoundtableSpace/status/2060477532537827633" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DAVFX_0</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 203 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DAVFX_0/status/2060306891687809144">View @DAVFX_0 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anomaly with Illugen #vfx #realtimevfx #illugen #gamedev #unity3d https://t.co/jnd5t1LiAH”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>VFX artist @DAVFX_0 โชว์ real-time effect ชื่อ 'Anomaly' สร้างด้วย Illugen ซึ่งเป็น VFX tool ที่ใช้ใน Unity แสดง particle และ shader คุณภาพสูง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Illugen ทำ real-time VFX ใน Unity ได้ระดับนี้ — ทีม Unity ควรรู้จักไว้เป็น option สำหรับ environmental หรือ ability effects</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">หา Illugen แล้วทดสอบใน Unity sandbox ดูว่าเข้ากับ VFX pipeline ของ studio ได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DAVFX_0/status/2060306891687809144" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@godotengine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 190 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/godotengine/status/2060503643057496501">View @godotengine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for a Release Candidate in the near future https://t.co/af9vUd2qLQ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีม Godot ปล่อย Godot Engine 4.7 beta 4 แล้ว พร้อมประกาศว่า Release Candidate ใกล้ออกแล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Godot 4.7 stable ใกล้ออก — ทีมที่สนใจ open-source engine ทางเลือกควบคู่กับ Unity มี timeline ชัดขึ้นแล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เอา Godot project ที่มีอยู่ไป test กับ beta 4 ตอนนี้เลย จะได้แก้ breaking changes ก่อน stable ออก</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/godotengine/status/2060503643057496501" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 163 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2060396306934436123">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Free learning content for the 5th month of the year? Yeah, we May just have some here for you... Explore how to create cinematic environments in UE5, set up translucent glass in Substrate, and more. I”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine ปล่อย free learning content ประจำเดือนพฤษภาคม ครอบคลุม cinematic environment ใน UE5 และการตั้งค่า translucent glass ด้วย Substrate material system</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค cinematic environment และ material workflow ใน UE5 ใช้ได้จริงกับงาน XR/VR แม้ทีมจะใช้ Unity เป็นหลัก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ดู module cinematic environment และ Substrate glass เพื่อเอา reference ด้าน lighting และ material ไปใช้ใน workflow ของตัวเอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2060396306934436123" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@itchio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 149 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/itchio/status/2060511506815746558">View @itchio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playable Solo or GM-Less https://t.co/vGYtVXXzUe by @CrossedPathsRPG https://t.co/avSktXRORC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>'Ashes' คือ tabletop RPG แนว Souls-like สไตล์ OSR เล่นคนเดียวหรือไม่มี GM จาก CrossedPathsRPG วางขายบน itch.io</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/itchio/status/2060511506815746558" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ushadersbible</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 139 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ushadersbible/status/2060220692675678422">View @ushadersbible on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hey guys, the Technical Art Unity Bundle is 70% OFF 🎁 https://t.co/1eA8907m5M #gamedev https://t.co/KSY2xfp9ud”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@ushadersbible ประกาศลด Technical Art Unity Bundle 70% ครอบคลุม shaders, VFX และ tech-art ใน Unity</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ส่วนลด 70% เป็นโอกาสซื้อ resource สำหรับทีม Unity โดยเฉพาะสาย shader และ VFX ในราคาต่ำ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดูรายละเอียด bundle ก่อน ถ้า match กับงาน shader หรือ VFX ปัจจุบัน ก็ซื้อได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ushadersbible/status/2060220692675678422" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
