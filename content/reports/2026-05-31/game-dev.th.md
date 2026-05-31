---
type: social-topic-report
date: '2026-05-31'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-31T04:09:00+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 32
salience: 0.55
sentiment: neutral
confidence: 0.6
tags:
- unity
- ai-pipeline
- 3d-generation
- godot
- tooling
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060606108763295745/img/-oeMxhDSxmtuOXkf.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-31

## TL;DR
- Microsoft ปล่อย Trellis.2 โมเดล open-source ขนาด 4B แปลงภาพเป็น GLB mesh 3D พร้อม texture ใน ~3 วินาที (ต่ำกว่า 100ms บน CUDA) output พร้อมใช้ใน Blender/Unity/Unreal [3]
- Godot 4.7 beta 4 ออกแล้ว โดย Release Candidate ใกล้มาถึง [5]
- Unity AI แบ่งเป็นสามโหมด — Ask, Plan, Agent — สำหรับตอบคำถาม วางแผน และ automate งานซ้ำ [19]; Unity ยังโปรโมต Unity Studio ซึ่งเป็น web editor แบบ no-code สำหรับแอป 3D ภาคอุตสาหกรรม [26]
- ด้านธุรกิจ: Playstack ผู้จัดจำหน่าย Balatro กำลังถูกขายให้ parent company ของ GameSpot/Fandom ที่ราคา ~$169M [30]; 007 First Light ยอดขายทะลุ 1.5M แล้ว [31]
- มี open-source Unity character controller ปล่อยโดย thesquirrelyjones รองรับ moving platforms และ edge case ชนกำแพง [2]

## สิ่งที่เกิดขึ้น
วันนี้ tooling และ AI ครองวง Microsoft ปล่อย Trellis.2 โมเดล open-source image-to-3D ขนาด 4B สร้าง GLB mesh ในไม่กี่วินาที พร้อม output ที่ใช้กับ engine ได้เลย [3] Godot ขยับสู่ 4.7 beta 4 ก่อนถึง RC [5] Unity อธิบายสามโหมดของ AI assistant (Ask/Plan/Agent) [19] และโปรโมต Unity Studio ซึ่งเป็น 3D editor บน web แบบ no-code [26] มี Unity character controller แบบ open-source ปล่อยฟรี ครอบคลุม edge case ที่พบบ่อย [2] Unreal ปล่อย learning content UE5 ฟรีเรื่อง cinematic environments และ Substrate glass [7] Carmack ตั้งข้อสังเกตว่า writing suggestions ของ Gmail ทำให้ข้อความดีขึ้นแต่ลบ voice ของผู้เขียนทิ้ง [1]

ด้านธุรกิจ Playstack (Balatro) กำลังถูก acquire ที่ราคา ~$169M [30] 007 First Light ผ่าน 1.5M ยอดขาย [31] และ Patch Notes #54 รายงาน indie micro-grants, ราคา hardware ขึ้นอีกรอบ และ Witcher 3 expansion [32] ส่วนที่เหลือเป็น craft content: shaders [6][21], VFX [4][12], procedural/spline tools [13][16], texturing workflows [22] และประกาศ indie release [8][11][15][25]

## ทำไมถึงสำคัญ
สัญญาณชัดสุดคือ AI กำลังเข้าสู่ pipeline ของ asset และ code การที่ Trellis.2 เป็น open-source เร็ว และ emit GLB ที่ใช้กับทั้งสาม engine หลักได้เลย ช่วยลดต้นทุนขั้น first-pass ของ 3D asset [3] ซึ่งสำคัญสำหรับ studio เล็กที่ทำ Unity/XR กรอบ Ask/Plan/Agent ของ Unity แสดงว่าตัว engine vendor เองกำลังสร้าง assistant workflows ฝังเข้า editor [19] ส่วน Unity Studio มุ่งเป้าลูกค้า industrial/AR/VR แบบ no-code บน web [26] ซึ่งเชื่อมกับสาย edutech และ XR ของ NDF โดยตรง ข้อสังเกตของ Carmack [1] เป็นคำเตือนจริง: output ของ AI ลู่เข้าหา voice กลางๆ ใช้ได้กับทั้ง asset ที่ generate และ copy ที่เขียน — เร็วแต่เสี่ยงต่อความโดดเด่น ด้านธุรกิจยืนยันตลาดที่ตึงตัวขึ้น (ราคา hardware ขึ้น [32]) ที่ IP ที่พิสูจน์แล้วยังขายได้ [31] และการ consolidation ดำเนินต่อ [30] ยิ่งชัดว่า studio เล็กต้องคุม cost และพึ่ง tooling ที่ถูกกว่า

## ความเป็นไปได้
**เป็นไปได้สูง:** โมเดล image-to-3D อย่าง Trellis.2 จะกลายเป็นขั้นตอน prototyping/greybox มาตรฐานใน indie pipeline เพราะ license open-source และ output เป็น GLB พร้อมใช้กับ engine [3] **เป็นไปได้สูง:** Godot 4.7 stable ตามมาเร็ว เพราะ beta 4 ระบุชัดว่ากำลัง stage RC [5] **เป็นไปได้:** Unity Agent mode และ Unity Studio ขยายสู่ลูกค้า non-game/industrial ตามที่ Unity สื่อสารเรื่อง AR/VR-skills positioning [26][28] **ไม่น่าเกิดขึ้น (ระยะสั้น):** asset ที่ AI generate ทดแทน bespoke art ในระดับ shippable quality — craft content วันนี้ [6][21][22] แสดงว่า shader และ texturing แบบ hand-tuned ยังเป็นตัวกำหนด visual identity ที่ Carmack เตือนว่า AI ทำให้แบนลง [1] ไม่มีแหล่งใดให้ตัวเลขความน่าจะเป็น

## การนำไปใช้กับ NDF DEV
1) ทดลอง Trellis.2 สำหรับ 3D prototyping/greyboxing ใน Unity และ XR scenes อย่างรวดเร็ว — ตรวจ license และคุณภาพ mesh/topology ก่อนใช้งาน production — effort ต่ำ [3] 2) Pilot Unity AI ในโหมด Ask/Plan/Agent กับงาน Unity จริง เพื่อวัดเวลาที่ประหยัดได้จากงาน editor ซ้ำๆ — effort ต่ำ [19] 3) ทดสอบ open-source Unity character controller ใน prototype เพื่อประเมินการรับมือ moving platform และ wall-collision — effort ต่ำ [2] 4) ติดตาม Unity Studio ในฐานะ delivery path ที่เป็นไปได้สำหรับลูกค้า edutech/industrial XR ที่ต้องการ web 3D แบบ no-code — effort กลาง ประเมินอย่างเดียว [26] 5) ส่ง UE5 free learning content (cinematic environments, Substrate glass) ให้ทีมที่ใช้ Unreal — effort ต่ำ [7] ข้ามได้: item ประเภท indie release/screenshot [8][11][12][14][15][16][18][25], asset-bundle sale [9] และ business/IP [30][31] — NDF รับรู้ไว้แต่ไม่มี action โดยตรง

## สัญญาณที่ต้องติดตาม
- กำหนด RC/stable ของ Godot 4.7 — beta 4 ระบุไว้ชัดแล้ว [5]
- การ adopt Trellis.2 และ feedback คุณภาพ asset ใน pipeline จริงของ Unity/Unreal [3]
- ความสมบูรณ์ของ Unity Agent mode และความน่าเชื่อถือของ automation สำหรับงาน production [19]
- ราคา hardware ที่ขึ้นต่อเนื่อง [32] — แรงกดดันด้าน margin กับงาน XR/VR ที่พึ่งพา hardware

## แหล่งข้อมูล
| platform | author | engagement | url |
|---|---|---|---|
| x | ID_AA_Carmack | ^1249 c140 | [I have difficulty arguing that most of the writing changes suggested in gmail no](https://x.com/ID_AA_Carmack/status/2060399696955195843) |
| x | jettelly | ^1160 c5 | [Developer thesquirrelyjones released an open-source custom character controller ](https://x.com/jettelly/status/2060617205989965911) |
| x | RoundtableSpace | ^291 c21 | [Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D ](https://x.com/RoundtableSpace/status/2060477532537827633) |
| x | DAVFX_0 | ^230 c3 | [Anomaly with Illugen #vfx #realtimevfx #illugen #gamedev #unity3d https://t.co/j](https://x.com/DAVFX_0/status/2060306891687809144) |
| x | godotengine | ^209 c7 | [One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for ](https://x.com/godotengine/status/2060503643057496501) |
| x | sean_gause | ^198 c2 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | UnrealEngine | ^174 c8 | [Free learning content for the 5th month of the year? Yeah, we May just have some](https://x.com/UnrealEngine/status/2060396306934436123) |
| x | itchio | ^161 c0 | [Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playa](https://x.com/itchio/status/2060511506815746558) |
| x | ushadersbible | ^143 c0 | [Hey guys, the Technical Art Unity Bundle is 70% OFF 🎁 https://t.co/1eA8907m5M #g](https://x.com/ushadersbible/status/2060220692675678422) |
| x | UnrealEngine | ^94 c26 | [We know that #ScreenshotSaturday is always out of this world So, show us what in](https://x.com/UnrealEngine/status/2060723065991131533) |
| x | itchio | ^67 c0 | [The Board Is Yours: A strategic chess-based incremental game. https://t.co/BHK6Y](https://x.com/itchio/status/2060360518469353950) |
| x | MortalCrux | ^65 c5 | [A mind-blowing magic finisher 🧙‍♀️ #indiegamedev #indiegame #unity3d #pcgamer #m](https://x.com/MortalCrux/status/2060702882001731819) |
| x | jettelly | ^63 c1 | [Developer Sapra shared how the spline-based road system works in their tool, Inf](https://x.com/jettelly/status/2060360513335549985) |
| x | Plasmeo | ^60 c2 | [Who needs cover when you have shielder drones ? #indiedev #gamedev #FPS #Unity #](https://x.com/Plasmeo/status/2060742236816445564) |
| x | itchio | ^57 c0 | [Trigwa: Statue pushing game with a narrative. Each puzzle tells part of a larger](https://x.com/itchio/status/2060405812057780236) |
| x | R2RGames | ^52 c0 | [Almost 300 followers! Here is more progress on my medieval builder, spline walls](https://x.com/R2RGames/status/2060462094802379049) |
| x | mazestalker | ^44 c1 | [I love going back to my pre-URP areas and updating them with 2 years of experien](https://x.com/mazestalker/status/2060495924523135169) |
| x | MJF_game | ^43 c13 | [Modern Jet Fighters Online is now live in Canada 🇨🇦 #Multiplayer #JetFighters #O](https://x.com/MJF_game/status/2060349067666899320) |
| x | unitygames | ^40 c3 | [Meet Unity AI's three modes: Ask, Plan, and Agent. 1️⃣ Ask: Get your questions a](https://x.com/unitygames/status/2060435608732836007) |
| x | JasozzGames | ^35 c1 | [intellisense please stop this when have i *ever* used that property #gamedev #un](https://x.com/JasozzGames/status/2060361262064599358) |
| x | jettelly | ^35 c0 | [Check out this tree shader by Sqrek, going through the seasons by changing leaf ](https://x.com/jettelly/status/2060239719481405445) |
| x | Rustledust77 | ^34 c1 | [Texturing workflow for our @FracturedRTS units: -&gt; Assign trim sheet material](https://x.com/Rustledust77/status/2060279247491465611) |
| x | OzgursAssets | ^30 c2 | [Modular alternative headlight design #keitruck #gamedev #indiedev #ue5 #Unity3d ](https://x.com/OzgursAssets/status/2060799257293000895) |
| x | FreyaHolmer | ^28 c0 | [@edmundmcmillen I would love to voice some cats!! @TylerGlaiel said I wasn't coo](https://x.com/FreyaHolmer/status/2060326276724916311) |
| x | itchio | ^25 c0 | [Dungeons of Freeport: An Extraction Roguelike Dungeon-Crawler https://t.co/2L6EX](https://x.com/itchio/status/2060451112503722298) |
| x | unity | ^22 c1 | [Think building interactive 3D apps for industry has to be slow and complicated? ](https://x.com/unity/status/2060345542803173429) |
| x | godotengine | ^15 c0 | [Featured game: Elfie: A Sand Plan https://t.co/JAOBcSXMGt](https://x.com/godotengine/status/2060503644617740388) |
| x | unity | ^5 c0 | [@eLAconference @moeghofficial @Proj_RESPECT We can't wait to help empower the ne](https://x.com/unity/status/2060342302732665263) |
| rss | Game Developer Podcast | ^0 c0 | [Crafting Clair Obscur: Expedition 33's mournful tale ft. Jennifer Svedeberg-Yen ](https://www.gamedeveloper.com/design/crafting-clair-obscur-expedition-33-s-mournful-tale-ft-jennifer-svedeberg-yen) |
| rss | Chris Kerr | ^0 c0 | [Balatro publisher Playstack is being sold to GameSpot and Fandom parent company ](https://www.gamedeveloper.com/business/balatro-publisher-playstack-sold-to-gamespot-and-fandom-parent-company) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1249 · 💬 140</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2060399696955195843">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I have difficulty arguing that most of the writing changes suggested in gmail now aren’t improvements, but it does tend to wipe out my particular authorial voice.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Carmack ระบุว่า AI writing suggestions ใน Gmail ปรับปรุงงานเขียนได้จริง แต่ลบ personal voice เฉพาะตัวออกจนหมด</dd>
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
    <span class="ndf-engagement">♥ 1160 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2060617205989965911">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer thesquirrelyjones released an open-source custom character controller for Unity, designed to handle edge cases like moving platforms and wall collisions. 🎮 See more: https://t.co/fpq8pSxsLi ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer thesquirrelyjones ปล่อย open-source character controller สำหรับ Unity ที่รองรับ edge cases เช่น moving platforms และ wall collisions</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Edge cases ของ character controller กิน debug time เยอะ — baseline ที่ผ่านการทดสอบมาแล้วช่วย Unity team ประหยัดเวลาได้มาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู repo นี้แล้วประเมินว่าใช้เป็น starting point สำหรับ project ที่ต้องการ custom character movement ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2060617205989965911" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RoundtableSpace</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 291 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RoundtableSpace/status/2060477532537827633">View @RoundtableSpace on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D asset in 3 seconds. Textured mesh under 100ms on CUDA, outputs a GLB file ready for Blender, Unity, and Unreal. Open sou”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Microsoft ปล่อย Trellis.2 โมเดล open-source 4B ที่แปลงรูปภาพเป็น textured GLB mesh ภายใน 3 วินาที (sub-100ms บน CUDA) ใช้ได้กับ Blender, Unity และ Unreal ได้โดยตรง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>GLB output นำเข้า Unity ได้โดยตรง ตัดขั้นตอน manual texture และ export ออกจาก 3D asset pipeline สำหรับ game และ XR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">รัน Trellis.2 local กับ concept art หรือ reference photo เพื่อสร้าง first-pass 3D asset สำหรับ Unity game และ XR</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RoundtableSpace/status/2060477532537827633" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DAVFX_0</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 230 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DAVFX_0/status/2060306891687809144">View @DAVFX_0 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anomaly with Illugen #vfx #realtimevfx #illugen #gamedev #unity3d https://t.co/jnd5t1LiAH”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@DAVFX_0 แชร์ demo real-time VFX ชื่อ 'Anomaly' สร้างด้วย Illugen ซึ่งเป็น VFX tool สำหรับ Unity แสดงเอฟเฟกต์ particle และ volumetric ในเครื่องจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Illugen ทำ real-time VFX คุณภาพสูงใน Unity ได้โดยตรง — ตรงกับงาน game และ XR ของ studio ที่ต้องการ in-engine effects ที่ดูดี</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team หา Illugen ใน Asset Store หรือเว็บตรง แล้วทดสอบกับ project ที่ใช้ particle system อยู่ตอนนี้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DAVFX_0/status/2060306891687809144" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@godotengine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 209 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/godotengine/status/2060503643057496501">View @godotengine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for a Release Candidate in the near future https://t.co/af9vUd2qLQ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Godot Foundation ปล่อย Godot Engine 4.7 beta 4 แล้ว โดย Release Candidate อยู่ใกล้แค่เอื้อม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ใช้ Unity เป็นหลักควรจับตา Godot 4.7 stable เป็น reference เผื่อ project ที่ต้องการ engine ที่เบากว่าหรือไม่มี royalty</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ให้ dev คนนึงทดลอง Godot 4.7 beta 4 บน prototype ภายในก่อน RC ออก เพื่อดู workflow 2D/3D ว่าเหมาะไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/godotengine/status/2060503643057496501" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 198 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@sean_gause ปล่อย node setup สำหรับ rain drip shader ใน Unity HDRP พร้อมอธิบายวิธี port ไป Unreal โดยความต่างหลักคือ HDRP ใช้ mask map แบบ packed channels (metal, AO, detail, smoothness)</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Reference shader graph สำหรับ rain/wet-surface ที่ใช้ได้ทั้ง Unity HDRP และ Unreal — ประหยัด R&amp;D ได้หลายชั่วโมงสำหรับงาน environment art</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity นำ node setup นี้ไปใช้ใน HDRP project ที่ต้องการ wet-surface หรือ weather shader ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 174 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2060396306934436123">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Free learning content for the 5th month of the year? Yeah, we May just have some here for you... Explore how to create cinematic environments in UE5, set up translucent glass in Substrate, and more. I”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine ปล่อยคอนเทนต์เรียนฟรีประจำเดือนพฤษภาคม ครอบคลุม cinematic environment ใน UE5 และการตั้งค่า translucent glass ด้วย Substrate material</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Substrate glass และ cinematic lighting ตรงกับงาน XR/VR และ architectural visualization ที่ทีมทำใน UE5 โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ส่ง tutorial Substrate glass ให้คนในทีมที่กำลังทำ UE5 scene ที่ต้องใช้ material สมจริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2060396306934436123" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@itchio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 161 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/itchio/status/2060511506815746558">View @itchio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playable Solo or GM-Less https://t.co/vGYtVXXzUe by @CrossedPathsRPG https://t.co/avSktXRORC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>itch.io โปรโมต 'Ashes' เกม tabletop RPG สไตล์ Souls-like จาก CrossedPathsRPG ออกแบบให้เล่นคนเดียวหรือไม่มี GM โดยได้แรงบันดาลใจจากแนว OSR</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/itchio/status/2060511506815746558" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
