---
type: social-topic-report
date: '2026-05-31'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-31T15:59:03+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 18
salience: 0.45
sentiment: neutral
confidence: 0.6
tags:
- gamedev
- unity
- unreal
- godot
- ai-tooling
- 3d-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060606108763295745/img/-oeMxhDSxmtuOXkf.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-31

## TL;DR
- Microsoft ปล่อย Trellis.2 โมเดล open-source ขนาด 4B ที่แปลงภาพเดียวเป็น textured GLB 3D asset ใน ~3 วินาที (mesh ต่ำกว่า 100ms บน CUDA) output ใช้ได้กับ Blender, Unity, และ Unreal ทันที [4]
- Godot 4.7 beta 4 ออกแล้ว และ Release Candidate กำลังจะตามมา [5]
- Unity AI เปิดสามโหมด — Ask, Plan, และ Agent — สำหรับ Q&A, ลำดับงานที่มี safeguard, และ automation งานซ้ำซาก [14]
- มีการปล่อย open-source Unity character controller รองรับ moving platforms และ wall collisions [1] พร้อม rain-drip shader node setup (Unity HDRP, พอร์ตได้กับ Unreal) [3]
- John Carmack ระบุว่า AI writing suggestions ของ Gmail ปฏิเสธได้ยากว่าไม่ดีขึ้น แต่ลบเสียงเฉพาะตัวของผู้เขียน [2] — ปัญหาที่วนซ้ำในงาน AI-assisted content

## What happened
อัปเดต engine/tooling สองรายการชัดเจน: Godot 4.7 ถึง beta 4 โดย RC ใกล้มาแล้ว [5], และ Unity เปิดเผยรายละเอียดสามโหมดของ AI assistant (Ask, Plan, Agent) สำหรับตอบคำถาม, สร้าง task plan ที่มี safeguard, และ automate งานซ้ำ [14] ด้าน asset generation, Microsoft ปล่อย Trellis.2 โมเดล open-source 4B แปลงภาพใดก็ได้เป็น textured GLB ใน ~3 วินาที (textured mesh ต่ำกว่า 100ms บน CUDA) ใช้ได้กับ Blender, Unity, และ Unreal [4] contribution จากชุมชนมี open-source Unity character controller สำหรับ edge cases อย่าง moving platforms และ wall collisions [1] และ rain-drip shader node graph ที่แชร์สาธารณะ (Unity HDRP, พอร์ตได้กับ Unreal) [3] Unreal ปล่อย free learning content ประจำเดือนพฤษภาคมครอบคลุม cinematic UE5 environments และ translucent glass ใน Substrate [6] ที่เหลือเป็น indie showcase และ itch.io/Godot release posts [7–13, 15–18] บวกกับโน้ตของ Carmack เรื่อง Gmail AI ที่ปรับปรุงงานเขียนแต่ลบเสียงส่วนตัว [2]

## Why it matters (reasoning)
Image-to-3D generation ในความเร็วและต้นทุนที่ Trellis.2 อ้าง [4] เปลี่ยนจุดที่ cost ของ asset อยู่: rapid prototyping, greyboxing, และ background props ถูกลง ขณะที่ topology, UV, และ optimization สำหรับ real-time ยังต้องการคนทำความสะอาด — generated mesh แทบไม่ ship as-is เป็น open source และ GLB-native จึงเสียบเข้า pipeline Unity/Unreal/Blender ที่มีอยู่แล้วได้โดยไม่ติด vendor lock-in [4] Unity Agent mode [14] ชี้ทิศทาง automation เดียวกันภายใน editor แต่ 'automate repetitive tasks' ยังคลุมเครือและยังไม่พิสูจน์ตัว คุณค่าขึ้นกับความเชื่อถือได้และ oversight ที่แต่ละ action ต้องการ ข้อสังเกตของ Carmack [2] นำไปใช้ได้กว้างกว่า email: AI assistance ดึงผลลัพธ์ไปทาง homogenized ซึ่งเกี่ยวกับทีมที่ใช้ AI สำหรับ narrative, marketing copy, หรือ code style Godot 4.7 ใกล้ RC [5] สืบทอด cadence ที่สม่ำเสมอในฐานะตัวเลือกไร้ค่า license สัญญาณส่วนใหญ่วันนี้เป็น routine community showcase ไม่ใช่การเปลี่ยนแปลงเชิงโครงสร้าง

## Possibility
มีแนวโน้มสูง: เครื่องมือ image-to-3D อย่าง Trellis.2 กลายเป็นขั้นตอน early-pipeline มาตรฐานสำหรับ blockout และ non-hero asset เพราะเป็น open source + GLB output + sub-second mesh generation [4] เป็นไปได้: Unity Agent mode และ in-editor AI ทำนองเดียวกันถูก adopt อย่างระมัดระวังโดยมี trust และ human review เป็นประตู [14] สอดคล้องกับ tradeoff voice/quality ที่ Carmack ชี้ [2] เป็นไปได้: Godot 4.7 stable ออกตาม RC ที่กล่าวถึงใน [5] ไม่น่าเป็นไปตามหลักฐานนี้: generated 3D asset แทน hand-authored hero asset ใน production รอบนี้ — ไม่มีอะไรใน [4] แตะ topology, rigging, หรือคุณภาพ LOD ไม่มีแหล่งใดให้ตัวเลข adoption หรือคุณภาพเชิงปริมาณ

## Org applicability — NDF DEV
ทดสอบ Trellis.2 กับงาน NDF asset จริง — generate props สำหรับ Unity scene แล้วจับเวลา cleanup เทียบกับ modeling จากศูนย์ (effort: low; เป็น open source และ GLB-native) [4] ถ้าคุณภาพ output ผ่าน ให้รวมเข้า early prototyping สำหรับโปรเจกต์ Unity/XR (effort: med) [4] ทดลอง Unity AI โหมด Ask/Plan บนโปรเจกต์ที่ active อยู่เพื่อวัดความแม่นก่อนให้ Agent mode แตะงาน editor ซ้ำซาก (effort: low) [14] bookmark tutorial UE5 cinematic-environment และ Substrate glass ฟรีสำหรับงาน Unreal/XR ด้าน visual (effort: low) [6] ประเมิน open-source character controller [1] และ rain-drip shader setup [3] เป็น reference ไม่ใช่ drop-in code (effort: low) สำหรับ AI-assisted writing ใน docs, marketing, หรือ narrative ให้คน pass เพื่อรักษาเสียง — ถือ Carmack flattening point เป็น process note [2] ข้าม: indie showcase และ itch.io/Godot featured-game posts [7–13, 15–18] — ไม่มี signal ที่ actionable

## Signals to Watch
- ติดตามคุณภาพ mesh และ topology จริงของ Trellis.2 — asset ที่ generate ต้อง cleanup หนักหรือใช้ได้เลย [4]
- ติดตาม reliability ของ Unity AI Agent mode และ oversight ที่ต้องการก่อนเชื่อการ automation [14]
- ติดตาม Godot 4.7 Release Candidate แล้วตามด้วย stable [5]
- ติดตามปัญหา 'voice flattening' ของ AI ที่ขยายจากงานเขียนไปยัง code และ narrative content [2]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | jettelly | ^1375 c7 | [Developer thesquirrelyjones released an open-source custom character controller ](https://x.com/jettelly/status/2060617205989965911) |
| x | ID_AA_Carmack | ^1289 c142 | [I have difficulty arguing that most of the writing changes suggested in gmail no](https://x.com/ID_AA_Carmack/status/2060399696955195843) |
| x | sean_gause | ^685 c4 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | RoundtableSpace | ^351 c23 | [Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D ](https://x.com/RoundtableSpace/status/2060477532537827633) |
| x | godotengine | ^223 c9 | [One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for ](https://x.com/godotengine/status/2060503643057496501) |
| x | UnrealEngine | ^190 c8 | [Free learning content for the 5th month of the year? Yeah, we May just have some](https://x.com/UnrealEngine/status/2060396306934436123) |
| x | itchio | ^170 c1 | [Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playa](https://x.com/itchio/status/2060511506815746558) |
| x | UnrealEngine | ^101 c27 | [We know that #ScreenshotSaturday is always out of this world So, show us what in](https://x.com/UnrealEngine/status/2060723065991131533) |
| x | MortalCrux | ^77 c5 | [A mind-blowing magic finisher 🧙‍♀️ #indiegamedev #indiegame #unity3d #pcgamer #m](https://x.com/MortalCrux/status/2060702882001731819) |
| x | Plasmeo | ^69 c2 | [Who needs cover when you have shielder drones ? #indiedev #gamedev #FPS #Unity #](https://x.com/Plasmeo/status/2060742236816445564) |
| x | itchio | ^61 c0 | [Trigwa: Statue pushing game with a narrative. Each puzzle tells part of a larger](https://x.com/itchio/status/2060405812057780236) |
| x | R2RGames | ^57 c0 | [Almost 300 followers! Here is more progress on my medieval builder, spline walls](https://x.com/R2RGames/status/2060462094802379049) |
| x | mazestalker | ^45 c1 | [I love going back to my pre-URP areas and updating them with 2 years of experien](https://x.com/mazestalker/status/2060495924523135169) |
| x | unitygames | ^42 c3 | [Meet Unity AI's three modes: Ask, Plan, and Agent. 1️⃣ Ask: Get your questions a](https://x.com/unitygames/status/2060435608732836007) |
| x | OzgursAssets | ^35 c2 | [Modular alternative headlight design #keitruck #gamedev #indiedev #ue5 #Unity3d ](https://x.com/OzgursAssets/status/2060799257293000895) |
| x | DAVFX_0 | ^33 c2 | [Electric stuff in Illugen #vfx #realtimevfx #illugen #unity3d #gamedev https://t](https://x.com/DAVFX_0/status/2060866245482709002) |
| x | itchio | ^28 c0 | [Dungeons of Freeport: An Extraction Roguelike Dungeon-Crawler https://t.co/2L6EX](https://x.com/itchio/status/2060451112503722298) |
| x | godotengine | ^17 c0 | [Featured game: Elfie: A Sand Plan https://t.co/JAOBcSXMGt](https://x.com/godotengine/status/2060503644617740388) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1375 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2060617205989965911">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer thesquirrelyjones released an open-source custom character controller for Unity, designed to handle edge cases like moving platforms and wall collisions. 🎮 See more: https://t.co/fpq8pSxsLi ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer thesquirrelyjones ปล่อย open-source character controller สำหรับ Unity ที่จัดการ edge cases เช่น moving platforms และ wall collisions</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ประหยัดเวลา debug ฟิสิกส์ยากๆ ได้มาก — ทีม Unity เอาไปใช้ใน platformer หรือ 3D action ได้เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง review repo นี้แล้วเทียบกับ character controller ที่ใช้อยู่ก่อนเริ่ม project ใหม่ที่เน้น movement</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2060617205989965911" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1289 · 💬 142</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2060399696955195843">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I have difficulty arguing that most of the writing changes suggested in gmail now aren’t improvements, but it does tend to wipe out my particular authorial voice.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Carmack สังเกตว่า AI ใน Gmail แนะนำข้อความที่ดีขึ้นจริงในแง่คุณภาพ แต่ลบ voice เฉพาะตัวออกจนหมด</dd>
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
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 685 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@sean_gause แชร์ node graph เต็มๆ ของ rain drip shader ใน Unity HDRP พร้อมอธิบาย mask map ที่แพ็ค metallic, AO, detail, smoothness ไว้ในแต่ละ channel และมีโน้ต port ไป Unreal</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Node setup rain drip shader ใน HDRP พร้อม documentation — ทีม Unity ได้ reference ตรงๆ สำหรับงาน wet-surface หรือ weather effect โดยไม่ต้องเริ่มใหม่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดึง node graph นี้ใส่ HDRP project ที่ต้องการ wet-surface effect ได้เลย; ถ้างานรันบน Unreal ก็ใช้โน้ต port ที่แนบมาได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RoundtableSpace</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 351 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RoundtableSpace/status/2060477532537827633">View @RoundtableSpace on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D asset in 3 seconds. Textured mesh under 100ms on CUDA, outputs a GLB file ready for Blender, Unity, and Unreal. Open sou”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Microsoft ปล่อย Trellis.2 โมเดล open-source 4B parameters แปลงภาพเป็น 3D mesh มี texture เป็นไฟล์ GLB ภายใน 3 วินาทีบน CUDA ใช้ได้กับ Blender, Unity, และ Unreal</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>pipeline image-to-3D ฟรีและ self-host ได้ ตัด workflow สร้าง 3D asset จากชั่วโมงเหลือวินาที ตรงกับงาน Unity game และ XR ที่ต้อง iterate asset บ่อย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง Trellis.2 ในเครื่อง แปลง concept art หรือ reference photo เป็น draft GLB สำหรับ block scene ก่อน commit งาน 3D จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RoundtableSpace/status/2060477532537827633" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@godotengine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 223 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/godotengine/status/2060503643057496501">View @godotengine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for a Release Candidate in the near future https://t.co/af9vUd2qLQ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Godot Foundation ปล่อย Godot Engine 4.7 beta 4 แล้ว Release Candidate กำลังจะตามมา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>4.7 RC ใกล้ออก หมายความว่า feature ใหม่ด้าน rendering, GDScript, และ editor เกือบ stable แล้วสำหรับทีมที่ติดตาม open-source แทน Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลองรัน Godot 4.7 beta 4 กับ prototype เล็กหรือ minigame ใน e-learning เพื่อประเมินก่อน stable ออก</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/godotengine/status/2060503643057496501" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 190 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2060396306934436123">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Free learning content for the 5th month of the year? Yeah, we May just have some here for you... Explore how to create cinematic environments in UE5, set up translucent glass in Substrate, and more. I”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine ปล่อย learning content ฟรีประจำเดือน May ครอบคลุมการสร้าง cinematic environment ใน UE5 และการตั้งค่า translucent glass ด้วย Substrate material system</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค Substrate glass และ cinematic lighting ใช้ได้กับงาน XR/VR environment โดยตรง แม้ทีมจะไม่ได้ ship บน UE5 เป็นหลัก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ให้ทีม XR/VR คนนึงลองทำ Substrate glass tutorial แล้ว note ว่า approach นี้ map กับ Unity material workflow ได้แค่ไหน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2060396306934436123" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@itchio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 170 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/itchio/status/2060511506815746558">View @itchio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playable Solo or GM-Less https://t.co/vGYtVXXzUe by @CrossedPathsRPG https://t.co/avSktXRORC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>itch.io โปรโมต Ashes ซึ่งเป็น tabletop RPG แบบ solo/GM-less ที่ได้แรงบันดาลใจจาก Souls-like และ OSR design โดย CrossedPathsRPG</dd>
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
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 101 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2060723065991131533">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We know that #ScreenshotSaturday is always out of this world So, show us what in the universe of possibilities you're developing, perfecting or concepting! 📷: @karabardin https://t.co/tiV6Ao2Aq0”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine โพสต์ #ScreenshotSaturday ตามปกติ ชวนนักพัฒนาแชร์ภาพงานที่กำลังทำ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2060723065991131533" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
