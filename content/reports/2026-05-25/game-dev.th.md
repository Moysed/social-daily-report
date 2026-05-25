---
type: social-topic-report
date: '2026-05-25'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-25T08:22:01+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- reddit
- x
regions:
- global
post_count: 55
salience: 0.78
sentiment: mixed
confidence: 0.72
tags:
- unreal-engine-6
- godot
- unity
- stylized-shaders
- on-device-ai
- indie-pipeline
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2058183587891974144/img/_QzMhINWZd4ePI3H.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-25

## TL;DR
- Epic ปล่อยตัวอย่าง Unreal Engine 6 พร้อมยืนยัน Rocket League เป็นเป้าหมาย upgrade แรก [9][16][19]
- Godot ecosystem ครองฟีด weekend — shaders, NPC AI, plugins, TCG/RPG demos [2][3][6][15]
- Unity Graph Toolkit 6.5 เปิดตัว tooling สำหรับ node-graph ที่ใช้งานได้จริงกับ mesh/VFX [26]
- Stylized rendering (single-tilable-texture, painterly, cloud, caustics) คือแนวทาง art direction ที่กำลังมาแรง [2][6][47][51]
- Offline neural translation plugin สำหรับ UE5 เป็นสัญญาณของ on-device AI ใน game pipeline [49]

## สิ่งที่เกิดขึ้น
ฟีดนักพัฒนา weekend ถูกครองโดยสองกระแสหลัก อย่างแรกคือ Epic ปล่อยตัวอย่าง Unreal Engine 6 พร้อมประกาศให้ Rocket League เป็น flagship upgrade target [9][19] ซึ่งก่อให้เกิดปฏิกิริยาในชุมชนแบบสองทาง — ภาพสวยงาม แต่มีความกังวลว่า UE5 ยังไม่ 'เสร็จสมบูรณ์' [16] อย่างที่สองคือ Godot ยังคงเติบโตจากรากหญ้า: cloud shaders [6], optimized NPC AI [15], stylized one-texture rendering pipelines [2], TCG/RPG projects [3], cozy demo launches [18], และการถกเถียงเรื่อง GDScript struct ที่ยังคงดำเนินอยู่ [21] Unity ยังคงมั่นคงพร้อม Graph Toolkit 6.5 [26], VFX/impact-frame shaders [1][5], และโพสต์ WIP ของ solo dev จำนวนมาก [13][40][45] การสังเกตจาก Bluesky [55] ชี้ให้เห็น cadence gap ที่ชัดเจน: UE5/Godot ออก quarterly ส่วน Unity 6 ออก monthly สำหรับ AI ใน pipeline นั้น สิ่งที่โดดเด่นที่สุดคือ offline on-device neural MT plugin สำหรับ UE5 [49]

## เหตุผลที่สำคัญ
การส่งสัญญาณของ UE6 รีเซ็ต horizon 5 ปีของ AAA tooling และยืนยันการลงทุนด้าน backwards-compat (เส้นทาง upgrade ของ Rocket League) [19] — แต่สำหรับ studio ขนาด indie/XR นั้นเป็นสัญญาณ 'จับตาดู-ยังไม่นำมาใช้' โดย UE5 ยังคงเป็น production target ที่เหมาะสม [16] ความหนาแน่นของ content บน Godot (shaders, AI, plugins, shipped demos) แสดงให้เห็นว่ามันข้ามจาก 'งานอดิเรก' สู่ 'พัฒนาได้จริง' สำหรับ scope แบบ 2D/stylized 3D ขนาดเล็ก [2][3][6][18] ซึ่งเกี่ยวข้องโดยตรงกับ mini-games edutech ของ NDF DEV ที่ Unity อาจใหญ่เกินความจำเป็น cadence รายเดือนของ Unity [55] บวกกับความก้าวหน้าของ Graph Toolkit [26] หมายความว่า pipeline ของ Unity-LTS ต้องการงบประมาณ maintenance ที่ active Offline UE5 MT plugin [49] คือสัญญาณ 'AI ใน pipeline' ที่จับต้องได้มากที่สุด — local inference สำหรับ localization นำไปใช้ได้โดยตรงกับ edutech ภาษาไทย/อังกฤษ

## ความเป็นไปได้
UE6 GA น่าจะอยู่ในช่วงปี 2027+ พร้อม migration window ยาวจาก UE5→UE6 (สูง) Godot 4.x ยังคงแย่งส่วนแบ่งจาก indie ระดับกลางต่อไป โดย structs ใน GDScript ยังคงค้างอยู่ในระยะสั้น (ปานกลาง, [21]) Unity ยังคง release รายเดือนอย่างคล่องตัว [55] — มีความเสี่ยง breaking changes สำหรับ studio ที่ใช้ LTS เก่า (ปานกลาง) on-device AI plugins สำหรับ translation/voice/NPC behavior จะแพร่หลายมากขึ้นใน 12 เดือนข้างหน้า (สูง) — คาดว่าจะมี equivalent ฝั่ง Unity ของ [49] และ [15] ตามมา

## การนำไปใช้สำหรับ NDF DEV
การใช้งานโดยตรง: (1) สำหรับ edutech/e-learning ให้ประเมิน Godot 4 สำหรับ 2D mini-games ภาษาไทย — ความเสี่ยงด้าน license ต่ำกว่า และ shippable ตาม [3][18] (2) นำ pattern 'one tilable texture + vertex tint' แบบ stylization [2] มาใช้กับ Unity edutech assets เพื่อ art direction ที่ cost ต่ำ — ประหยัด texture memory บน mobile/XR (3) สำหรับ localization ของ Enggenius/edutech ศึกษา pattern ของ offline MT plugin [49] และสร้าง prototype Unity Sentis equivalent — รองรับ content ไทย/อังกฤษแบบ offline สำหรับโรงเรียน (4) จับตา UE6 [9] แต่ยังไม่ต้อง migrate — XR pipeline ยังอยู่บน Unity (5) Painterly/stylized shaders [47] และ procedural impact VFX [1] เป็น reference ที่นำมาใช้ซ้ำได้สำหรับมาตรฐานคุณภาพ game jam สิ่งที่ควรข้าม: การ adopt UE6 ในระยะต้น, กระทู้เปรียบ AAA ที่ก่อความวิตกสำหรับ solo dev [13] สิ่งที่คุ้มค่า: stylization patterns + offline AI MT ยังไม่คุ้มค่าตอนนี้: การเปลี่ยน engine

## Signals ที่ควรติดตาม
- UE6 official roadmap และเอกสาร UE5→UE6 compat จาก Epic
- Unity Sentis / on-device inference plugins สำหรับ localization และ NPC AI
- Godot 4.x struct RFC movement [21] — ส่งผลต่อ ports ที่ต้องการ performance สูง
- Painterly/stylized shader assets ที่ออกจำหน่ายบน FAB และ Asset Store [47][2]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | unity3dvfx | ^2520 c10 | [Procedurally generated impact frame with shader and particle system by @namutree](https://x.com/unity3dvfx/status/2058183630845874338) |
| reddit | Illustrious-Scratch7 | ^754 c14 | [Plenty of people asked how I did art style for my game, so here is my setup. Her](https://www.reddit.com/r/godot/comments/1tml8tz/plenty_of_people_asked_how_i_did_art_style_for_my/) |
| reddit | Rosehn | ^487 c22 | [I've been learning Godot over the past year to make an old-school trading card R](https://www.reddit.com/r/godot/comments/1tmj70x/ive_been_learning_godot_over_the_past_year_to/) |
| x | unity3dvfx | ^410 c7 | [This looks absolutely heavenly! ☁️✨ Procedural texturing + divine city-building ](https://x.com/unity3dvfx/status/2058598704488079660) |
| reddit | andre_mc | ^398 c13 | [Built a simple goal net effect that cansimulate back and forth! Shaders are trul](https://www.reddit.com/r/Unity3D/comments/1tmjo91/built_a_simple_goal_net_effect_that_cansimulate/) |
| reddit | Sea-Good5788 | ^298 c27 | [oh so fluffy!! im proud of it yes i AM that same guy who's obsessed with clouds ](https://www.reddit.com/r/godot/comments/1tmjhu7/oh_so_fluffy_im_proud_of_it/) |
| reddit | zacharieg14 | ^298 c11 | [Made a simple animation to my game's menu in 5 minutes, now it looks awesome! Hi](https://www.reddit.com/r/godot/comments/1tmchd1/made_a_simple_animation_to_my_games_menu_in_5/) |
| reddit | Equal_Money4055 | ^252 c22 | [Screenshots from my WIP Game the game is based on collecting photo evidence and ](https://www.reddit.com/r/godot/comments/1tmfu7j/screenshots_from_my_wip_game/) |
| reddit | Kudlattyy | ^232 c111 | [In case anyone missed it, Epic teased Unreal Engine 6. [https://www.youtube.com/](https://www.reddit.com/r/gamedev/comments/1tmktci/in_case_anyone_missed_it_epic_teased_unreal/) |
| x | RealtimeVFXMike | ^207 c7 | [Character controller update. Made a little sandbox in @ProdeusGame level editor ](https://x.com/RealtimeVFXMike/status/2058184636895772927) |
| x | thepixelform | ^175 c5 | [In unity there is strength. New formation orders: - Scatter, - Rally to Banner, ](https://x.com/thepixelform/status/2058450914592092302) |
| reddit | Soliloqu-You | ^167 c51 | [Have you ever changed your game because of one player's message? Hi everyone. I'](https://www.reddit.com/r/gamedev/comments/1tm8f61/have_you_ever_changed_your_game_because_of_one/) |
| reddit | Confident_Towel_8304 | ^158 c154 | [Solo dev here struggling with AAA comparisons and expectation management for my ](https://www.reddit.com/r/Unity3D/comments/1tm9kiv/solo_dev_here_struggling_with_aaa_comparisons_and/) |
| reddit | BenzFiveSix | ^116 c37 | [Someone played my game for 24,000 hours I'm the solo dev behind Vacuum Warrior, ](https://www.reddit.com/r/gamedev/comments/1tmh5iq/someone_played_my_game_for_24000_hours/) |
| reddit | ArmyOfChickens | ^108 c25 | [Npcs with advanced Ai Since starting my journey with godot 3 to being on 4.6 for](https://www.reddit.com/r/godot/comments/1tmutta7/npcs_with_advanced_ai/) |
| reddit | Unfair-Umpire-6826 | ^98 c105 | [Opinions on UE6 announcement? I have mixed opinions. on the one hand, it's cool.](https://www.reddit.com/r/unrealengine/comments/1tmkgnf/opinions_on_ue6_announcement/) |
| reddit | IamChipp | ^98 c8 | [I love how wild is this community here Sorry if this comes across as low effort ](https://www.reddit.com/r/godot/comments/1tmbl78/i_love_how_wild_is_this_community_here/) |
| reddit | tobiski | ^96 c10 | [Just released a demo for my cozy puzzle game, Paperlands Hey everyone! I've been](https://www.reddit.com/r/godot/comments/1tmllrf/just_released_a_demo_for_my_cozy_puzzle_game/) |
| reddit | TheFlamingLemon | ^95 c68 | [Rocket League will be upgraded to Unreal Engine 6 It was just revealed that Rock](https://www.reddit.com/r/unrealengine/comments/1tmgujh/rocket_league_will_be_upgraded_to_unreal_engine_6/) |
| x | OzgursAssets | ^94 c4 | [Kei Truck WIP I've started modeling this little friend. #gamedev #indiedev #ue5 ](https://x.com/OzgursAssets/status/2058179701747650697) |
| reddit | CoolStopGD | ^81 c46 | [Structs in GDscript progress Several times now I've hit moments where structs wo](https://www.reddit.com/r/godot/comments/1tmj0qg/structs_in_gdscript_progress/) |
| reddit | _IsItLucas | ^79 c4 | [I made the perfect Custom Window and I'm so proud of it After many, many, many a](https://www.reddit.com/r/godot/comments/1tmj40f/i_made_the_perfect_custom_window_and_im_so_proud/) |
| x | BadGameHOF | ^73 c3 | ['Air Control' released on this day in 2014. A Unity asset-mash with non-function](https://x.com/BadGameHOF/status/2058290193514533252) |
| x | 13z_game | ^68 c2 | [Wait till the end to see what a PERFECT PARRY feels like 🤭 #gamedev #indiedev #i](https://x.com/13z_game/status/2058201345010594162) |
| x | backtothedawn | ^68 c2 | [Well, this is your lawyer (and homie) 😭 Good luck 😉 #pixelart #gamedev #indiedev](https://x.com/backtothedawn/status/2058156065519235191) |
| reddit | PropellerheadViJ | ^67 c12 | [What's new and usable in Unity Graph Toolkit 6.5 (with code) I just moved a node](https://www.reddit.com/r/Unity3D/comments/1tmo0nb/whats_new_and_usable_in_unity_graph_toolkit_65/) |
| x | HitoriscanKOBO | ^62 c1 | [The relief model is now complete, and I've created a short demo animation. I've ](https://x.com/HitoriscanKOBO/status/2058547683363828042) |
| x | OzgursAssets | ^62 c1 | [Traffic Racer (2013) - Honda Civic Type-R Sedan (2007) #trafficracer #gamedev #i](https://x.com/OzgursAssets/status/2058165068932493543) |
| reddit | PensiveDemon | ^55 c10 | [[Convert Text Case] Built a plugin for myself - Should I share it to the Asset S](https://www.reddit.com/r/godot/comments/1tm9dew/convert_text_case_built_a_plugin_for_myself/) |
| x | realonepen | ^55 c4 | [Big update for my game! Added combat system and how player can interact with ene](https://x.com/realonepen/status/2058639356571910190) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@unity3dvfx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2520 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/unity3dvfx/status/2058183630845874338">View @unity3dvfx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Procedurally generated impact frame with shader and particle system by @namutree_04 #unity3d #gamedev #indiedev #madewithunity #unity #3dart #3d #unityengine #VFX #shader #RealTime #UE5 https://t.co/D”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev Unity โชว์ impact VFX แบบ procedural สร้างด้วย custom shader และ particle system ผลงานของ @namutree_04</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Impact frame แบบ procedural ด้วย shader+particle ตัดงาน hand-key frame-by-frame ออก ลด iteration time ได้มากสำหรับ action game</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ศึกษา pipeline shader+particle นี้แล้วสร้าง reusable impact VFX library มาตรฐานเดียวกันทุก project ที่ต้องการ hit-feel</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/unity3dvfx/status/2058183630845874338" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Illustrious-Scratch7</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 754 · 💬 14</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tml8tz/plenty_of_people_asked_how_i_did_art_style_for_my/" target="_blank" rel="noopener"><img src="https://preview.redd.it/l785g6fxv43h1.jpg?width=1948&amp;format=pjpg&amp;auto=webp&amp;s=31a16c3d3c685e0d6bd332c8d4834dccd22e0e2e" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Plenty of people asked how I did art style for my game, so here is my setup. Here is how I approached stylized rendering for my game: \- Most models are using only one tilable texture that is tinted b”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev ใน Godot อธิบาย stylized rendering pipeline: ใช้ tilable texture เดียว tint ด้วย vertex colors, toon lighting shader + DirectionalLight3D ตัวเดียว, base color ตั้งใจให้ flat แล้วค่อย boost ใน post-process, และ outline ด้วย inverted-normal geometry.</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค low-contrast base + post-process contrast boost แยก art authoring ออกจาก final look ทำให้ทีมเล็ก iterate ลุคได้โดยไม่ต้อง re-export texture ใหม่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ทำ pipeline นี้ได้ใน URP: ใช้ Shader Graph สำหรับ toon lighting, inverted-normal mesh สำหรับ outline, และ URP Volume สำหรับ post-process contrast — ลด texture work ต่อ asset ใน stylized project</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tml8tz/plenty_of_people_asked_how_i_did_art_style_for_my/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rosehn</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 487 · 💬 22</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tmj70x/ive_been_learning_godot_over_the_past_year_to/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/bDdvam55aHNpNDNoMdRlGGf7LJM8IJhjoJMg957xpDs5C6Tzcsrqn1p7SoPc.png?format=pjpg&amp;auto=webp&amp;s=c4248b042090570c9ef4ffaf5f064f8561169436" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I've been learning Godot over the past year to make an old-school trading card RPG! I've always wished there were more games like the classic yugioh or pokemon tcg games, so I decided to make one. Ste”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev ใช้เวลา 1 ปีเรียน Godot สร้าง trading card RPG สไตล์คลาสสิก แรงบันดาลใจจาก Yu-Gi-Oh และ Pokémon TCG ตอนนี้ขึ้น Steam แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>พิสูจน์ว่า solo dev สร้าง card game ที่มี AI, hand management และ turn logic ใน Godot ได้จริงภายใน 1 ปี — เป็น benchmark ด้าน scope และ timeline ที่จับต้องได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู architecture ของ Godot สำหรับ card game ได้ — state machine สำหรับ turn logic, resource file สำหรับ card data แล้วเทียบกับ tooling ของ Unity ในโปรเจกต์ลักษณะเดียวกัน</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tmj70x/ive_been_learning_godot_over_the_past_year_to/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@unity3dvfx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 410 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/unity3dvfx/status/2058598704488079660">View @unity3dvfx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This looks absolutely heavenly! ☁️✨ Procedural texturing + divine city-building is such a fresh combo. I love seeing indie devs push Unity in creative directions like this! #indiedev #gamedev #unity3d”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ยกย่อง indie game บน Unity ที่ผสม procedural texturing เข้ากับ theme เมืองสวรรค์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Procedural texturing ช่วยลด manual asset work ได้มาก — สำคัญสำหรับทีมเล็กที่มี artist จำกัด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลองใช้ procgen texture pipeline เพื่อเร่ง environment art ในโปรเจกต์เกม ลด dependency กับ hand-painted assets</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/unity3dvfx/status/2058598704488079660" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@andre_mc</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 398 · 💬 13</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/Unity3D/comments/1tmjo91/built_a_simple_goal_net_effect_that_cansimulate/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/ZHlodDlpYjBtNDNoMaiQIFGtgFloASNMB9EazzSc5fsuAbEBzKujilVTn1Li.png?format=pjpg&amp;auto=webp&amp;s=aa7e4d4ae12eaf0457aef638f8e85837b606b669" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Built a simple goal net effect that cansimulate back and forth! Shaders are truly magic!!!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา Unity สร้าง goal net effect ด้วย shader จำลองตาข่ายแกว่งไปมาได้จริงเมื่อลูกบอลถูกตี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แสดงให้เห็นว่าเอฟเฟกต์ตาข่ายที่ดูสมจริงทำได้ด้วย shader ล้วนๆ โดยไม่เปลือง CPU จาก Rigidbody หรือ cloth simulation</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity นำเทคนิคนี้ไปใช้ในซีน VR/XR ที่มีองค์ประกอบผ้าหรือตาข่ายได้ แทน cloth simulation ด้วย shader pass เพื่อรักษา frame budget</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1tmjo91/built_a_simple_goal_net_effect_that_cansimulate/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Sea-Good5788</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 298 · 💬 27</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tmjhu7/oh_so_fluffy_im_proud_of_it/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/dGRqZWFrM3JrNDNoMbd73V375KqV_CzKdI_MxZNkRo8Lxoq-cqIf_5otLKK0.png?format=pjpg&amp;auto=webp&amp;s=3862b580bbc94a639384b4750477633c5cc2623d" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“oh so fluffy!! im proud of it yes i AM that same guy who's obsessed with clouds on this sub.. still working on improving it, i want to make the BEST cloud shader for godot. and im STILL making the tut”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา Godot แชร์ cloud shader แบบฟูๆ ที่ตัวเองสร้าง พร้อมประกาศว่ากำลังทำ tutorial สอนเทคนิคนี้อยู่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cloud shader คุณภาพสูงจาก community พร้อม tutorial ฟรี ทีมเล็กๆ ได้ atmospheric visuals ระดับ production โดยไม่เสียค่าใช้จ่าย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ติดตาม developer คนนี้ไว้ — เทคนิค volumetric cloud แปลงข้าม engine ได้ พอ tutorial ออกให้แกะแนวคิดมาทำใหม่ใน ShaderGraph หรือ HLSL</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tmjhu7/oh_so_fluffy_im_proud_of_it/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@zacharieg14</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 298 · 💬 11</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tmchd1/made_a_simple_animation_to_my_games_menu_in_5/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/bzhyZGl0cWw4MzNoMY426Uwd8GWwg4dBiH67XbomPHpA8R8TTFqcbdC0IsWF.png?format=pjpg&amp;auto=webp&amp;s=e0b212748d7eed5c5fe5642353655386fe054339" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Made a simple animation to my game's menu in 5 minutes, now it looks awesome! Hi there ! For those who are interested in the planet, I made it with this tutorial : [https://www.youtube.com/watch?v=tPl”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer ใช้ Godot ทำ animation ดาวเคราะห์ใน menu หลักของเกมภายใน 5 นาที โดยอ้างอิง tutorial จาก YouTube ก่อนปล่อย wishlist บน Steam</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Animation ง่ายๆ บน menu สร้าง first impression ได้แรง — ROI สูงมากเทียบกับเวลาที่ใช้ โดยเฉพาะช่วงก่อน launch</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ใช้หลักการเดียวกันได้เลย — ลงทุน 30–60 นาทีทำ animation element เดียวใน main menu ก่อนโชว์ client หรือส่ง build</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tmchd1/made_a_simple_animation_to_my_games_menu_in_5/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Equal_Money4055</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 252 · 💬 22</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tmfu7j/screenshots_from_my_wip_game/" target="_blank" rel="noopener"><img src="https://preview.redd.it/p5z60p8kw33h1.png?width=1280&amp;format=png&amp;auto=webp&amp;s=33fe40355ad578aea96f80f58ca965c73de6f4d9" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Screenshots from my WIP Game the game is based on collecting photo evidence and proving your paranoia. so far how's the visuals?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev เดี่ยวแชร์ screenshot เกม WIP แนว paranoia ที่ผู้เล่นเก็บ photo evidence เพื่อพิสูจน์ความสงสัย ขอ feedback ด้านวิชวลใน r/godot</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Loop การเก็บ evidence เป็น core mechanic ที่ใช้ asset น้อยแต่สร้าง atmosphere ได้แรง — สัญญาณดีสำหรับทีมเล็กที่ budget จำกัด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง prototype mechanic เก็บ evidence แบบนี้สำหรับ pitch แนว mystery หรือ horror ได้เลย — design ไม่ติด engine ทำได้ใน sprint สั้น</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tmfu7j/screenshots_from_my_wip_game/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
</div>
