---
type: social-topic-report
date: '2026-05-25'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-25T03:13:37+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- reddit
- x
regions:
- global
post_count: 79
salience: 0.55
sentiment: mixed
confidence: 0.7
tags:
- gamedev
- godot
- unreal-engine-6
- unity
- shaders
- ai-pipeline
thumbnail: https://preview.redd.it/l785g6fxv43h1.jpg?width=1948&format=pjpg&auto=webp&s=31a16c3d3c685e0d6bd332c8d4834dccd22e0e2e
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-25

## TL;DR
- Epic ปล่อยตัวอย่าง Unreal Engine 6 พร้อมยืนยันว่า Rocket League จะเป็นเป้าหมายอัปเกรดรายใหญ่รายแรก [8][13][14]
- Godot ครองส่วนแบ่งเสียงในฝั่ง indie วันนี้: มากกว่า 13 จาก 40 รายการ ส่วนใหญ่เป็น stylized rendering, shaders, และ RPG ทีมเล็ก [1][2][5][6][7]
- Unity Graph Toolkit 6.5 ออกอัปเดตการสร้าง node-based ที่ใช้งานได้จริงในระดับ production [18]
- สัญญาณ AI-in-pipeline มีน้อยแต่ชัดเจน: offline NMT plugin สำหรับ UE5 รองรับ localization โดยไม่ต้องใช้ API [30]
- กระทู้ตรวจสอบความเป็นจริงของ solo-dev (ความคาดหวังระดับ AAA, จำนวน wishlist, การเซ็นสัญญากับ publisher) ครองการถกเถียงฝั่ง business [10][22]

## สิ่งที่เกิดขึ้น
Epic ปล่อยตัวอย่าง Unreal Engine 6 และยืนยันว่า Rocket League จะเป็นหนึ่งใน migration รายแรกสู่ UE6 ซึ่งสร้างปฏิกิริยาผสมในชุมชน — ตื่นเต้นกับภาพกราฟิก แต่กังวลว่าฟีเจอร์ใน UE5 (Nanite/Lumen workflow, ความเสถียรของ editor) ยังไม่สมบูรณ์ [8][13][14] Godot ยังคงท่วม r/godot ด้วยผลงาน stylized-rendering (single tileable texture + tinting [1]), การทดลอง shader (เมฆ [6], ใต้น้ำ [20]), และโปรเจกต์ indie หลายแนว (TCG RPG [2], survival horror [5], เกมถ่ายภาพหลักฐาน [7]) รวมถึงการผลักดัน structs ใน GDScript อีกครั้ง [16] ฝั่ง Unity มีบทความรีวิว Graph Toolkit 6.5 แบบลงมือทดลอง [18] และ shader/VFX demos หลายชิ้น [4][29] ข่าว AI-in-pipeline มีน้อยแต่น่าสนใจ: offline neural MT plugin สำหรับ UE5 [30] ช่วยตัด dependency ด้าน API key และอินเทอร์เน็ตออกจากกระบวนการ localization ภายใน editor

## ทำไมถึงสำคัญ (เหตุผล)
การปล่อยตัวอย่าง UE6 รีเซ็ตบทสนทนาเรื่อง roadmap ของ engine ในระยะยาว ในช่วงเวลาที่หลาย studio กำลังอยู่ระหว่างการ adopt UE5 — กดดัน planning horizon และเสี่ยงทำให้เกิดการ 'รอ UE6' จนโปรเจกต์ UE5 ใหม่หยุดชะงัก [8][13][14] โมเมนตัมต่อเนื่องของ Godot ในงาน 2D/stylized 3D และ shader ยืนยันว่ามันคือ engine อันดับสามที่น่าเชื่อถือสำหรับทีมเล็กที่ต้องการ zero licensing risk และ iteration ที่รวดเร็ว [1][2][5][6]; การถกเถียงเรื่อง structs-in-GDScript [16] คือข้อจำกัดด้าน performance/architecture ที่แท้จริงสำหรับงานที่เกินระดับ prototype การพัฒนาของ Unity Graph Toolkit [18] สำคัญสำหรับผู้สร้างเครื่องมือที่ขยาย editor มากกว่าการทำงาน runtime ของเกม offline-NMT plugin [30] เป็น pattern เล็กแต่มีความหมาย: การ ship local ML model ภายใน engine plugin แทนการเรียก cloud API — ดีกว่าในแง่ต้นทุน, ความเป็นส่วนตัว, และ build สำหรับ offline edutech/XR

## ความเป็นไปได้
UE6 น่าจะพร้อม production ภายใน 1-2 ปี (~70%); คาดว่าจะมีช่วง parallel ระหว่าง UE5→UE6 ยาวนาน คล้ายกับช่วง UE4→UE5 [8][14] Godot 4.x จะยังคงเพิ่มส่วนแบ่งในฝั่ง indie แต่จะไม่ลด share ของ Unity/Unreal ใน commercial 3D ในปีนี้ (~80%) offline-AI plugins เพิ่มเติม (translation, TTS, upscaling, NPC dialogue) จะ ship บน Fab และ Asset Store ในอีก 6 เดือนข้างหน้า เมื่อโมเดลขนาดเล็ก/Whisper-class กลายเป็นตัวเลือกที่ deploy ได้ (~60%) [30] เศรษฐกิจ wishlist ของ solo-dev ยังคงตึงตัว — threshold ของ publisher และแรงกดดันด้าน Steam discovery จะไม่ผ่อนคลาย (~75%) [22]

## การนำไปใช้ในองค์กร — NDF DEV
ส่วนที่ใช้ได้โดยตรงสำหรับ NDF DEV: (1) เทคนิค Godot stylized-rendering [1][6] ใช้กับ edutech/casual prototype งบน้อยที่ Unity license/perf ไม่คุ้มค่า — น่าลอง spike สั้น ความเสี่ยงต่ำ (2) Unity Graph Toolkit 6.5 [18] เกี่ยวข้องหากเราขยาย editor สำหรับ XR/Unity content pipeline ที่ทำซ้ำได้ — ROI ระดับกลางสำหรับ internal tooling (3) pattern ของ offline NMT plugin [30] เกี่ยวข้องสูงมาก — edutech/e-learning ของ NDF มักต้องการ localization ไทย↔EN และ XR build แบบ offline; เราสามารถนำ pattern เดียวกัน (local model ใน plugin) มาใช้กับ Unity content ของเรา (4) การปล่อยตัวอย่าง UE6 [8][14] — อย่าเปลี่ยนทิศ; เราไม่ได้ใช้ Unreal และเรื่องการ migrate ยังอีกหลายปี (5) ข้อมูล solo-dev wishlist/publisher [22] มีประโยชน์เป็น benchmark หากเราเผยแพร่เกมบน Steam เอง ข้ามได้: โพสต์ shader eye-candy บนคลาวด์ เว้นแต่จะเป็นแรงบันดาลใจสำหรับ art direction โดยตรง

## สัญญาณที่ควรติดตาม
- วันที่ใน UE6 official roadmap และคู่มือ migration UE5→UE6 จาก Epic
- ความคืบหน้าของ Godot 4.x structs RFC — ปลดล็อกโปรเจกต์ commercial ขนาดใหญ่ขึ้น [16]
- offline-AI engine plugins เพิ่มเติม (TTS, NPC dialogue, upscaling) บน Fab/Asset Store [30]
- อัตราการ adopt Unity Graph Toolkit ในเครื่องมือ/โปรเจกต์ที่ ship แล้ว [18]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| reddit | Illustrious-Scratch7 | ^555 c10 | [Plenty of people asked how I did art style for my game, so here is my setup. Her](https://www.reddit.com/r/godot/comments/1tml8tz/plenty_of_people_asked_how_i_did_art_style_for_my/) |
| reddit | Rosehn | ^346 c13 | [I've been learning Godot over the past year to make an old-school trading card R](https://www.reddit.com/r/godot/comments/1tmj70x/ive_been_learning_godot_over_the_past_year_to/) |
| reddit | zacharieg14 | ^279 c11 | [Made a simple animation to my game's menu in 5 minutes, now it looks awesome! Hi](https://www.reddit.com/r/godot/comments/1tmchd1/made_a_simple_animation_to_my_games_menu_in_5/) |
| reddit | andre_mc | ^274 c11 | [Built a simple goal net effect that cansimulate back and forth! Shaders are trul](https://www.reddit.com/r/Unity3D/comments/1tmjo91/built_a_simple_goal_net_effect_that_cansimulate/) |
| reddit | erofamiliar | ^260 c32 | [working on a survival horror, it's still VERY early but it's slowly getting ther](https://www.reddit.com/r/godot/comments/1tm2e4h/working_on_a_survival_horror_its_still_very_early/) |
| reddit | Sea-Good5788 | ^243 c23 | [oh so fluffy!! im proud of it yes i AM that same guy who's obsessed with clouds ](https://www.reddit.com/r/godot/comments/1tmjhu7/oh_so_fluffy_im_proud_of_it/) |
| reddit | Equal_Money4055 | ^191 c20 | [Screenshots from my WIP Game the game is based on collecting photo evidence and ](https://www.reddit.com/r/godot/comments/1tmfu7j/screenshots_from_my_wip_game/) |
| reddit | Kudlattyy | ^179 c89 | [In case anyone missed it, Epic teased Unreal Engine 6. [https://www.youtube.com/](https://www.reddit.com/r/gamedev/comments/1tmktci/in_case_anyone_missed_it_epic_teased_unreal/) |
| reddit | Soliloqu-You | ^152 c48 | [Have you ever changed your game because of one player's message? Hi everyone. I'](https://www.reddit.com/r/gamedev/comments/1tm8f61/have_you_ever_changed_your_game_because_of_one/) |
| reddit | Confident_Towel_8304 | ^127 c143 | [Solo dev here struggling with AAA comparisons and expectation management for my ](https://www.reddit.com/r/Unity3D/comments/1tm9kiv/solo_dev_here_struggling_with_aaa_comparisons_and/) |
| reddit | BenzFiveSix | ^86 c33 | [Someone played my game for 24,000 hours I'm the solo dev behind Vacuum Warrior, ](https://www.reddit.com/r/gamedev/comments/1tmh5iq/someone_played_my_game_for_24000_hours/) |
| reddit | IamChipp | ^86 c8 | [I love how wild is this community here Sorry if this comes across as low effort ](https://www.reddit.com/r/godot/comments/1tmbl78/i_love_how_wild_is_this_community_here/) |
| reddit | Unfair-Umpire-6826 | ^81 c85 | [Opinions on UE6 announcement? I have mixed opinions. on the one hand, it's cool.](https://www.reddit.com/r/unrealengine/comments/1tmkgnf/opinions_on_ue6_announcement/) |
| reddit | TheFlamingLemon | ^80 c62 | [Rocket League will be upgraded to Unreal Engine 6 It was just revealed that Rock](https://www.reddit.com/r/unrealengine/comments/1tmgujh/rocket_league_will_be_upgraded_to_unreal_engine_6/) |
| reddit | tobiski | ^74 c6 | [Just released a demo for my cozy puzzle game, Paperlands Hey everyone! I've been](https://www.reddit.com/r/godot/comments/1tmllrf/just_released_a_demo_for_my_cozy_puzzle_game/) |
| reddit | CoolStopGD | ^67 c45 | [Structs in GDscript progress Several times now I've hit moments where structs wo](https://www.reddit.com/r/godot/comments/1tmj0qg/structs_in_gdscript_progress/) |
| reddit | _IsItLucas | ^60 c4 | [I made the perfect Custom Window and I'm so proud of it After many, many, many a](https://www.reddit.com/r/godot/comments/1tmj40f/i_made_the_perfect_custom_window_and_im_so_proud/) |
| reddit | PropellerheadViJ | ^53 c12 | [What's new and usable in Unity Graph Toolkit 6.5 (with code) I just moved a node](https://www.reddit.com/r/Unity3D/comments/1tmo0nb/whats_new_and_usable_in_unity_graph_toolkit_65/) |
| reddit | PensiveDemon | ^50 c8 | [[Convert Text Case] Built a plugin for myself - Should I share it to the Asset S](https://www.reddit.com/r/godot/comments/1tm9dew/convert_text_case_built_a_plugin_for_myself/) |
| reddit | EternalColosseum | ^46 c4 | [That moment you spend days on a feature that's not even important for your game ](https://www.reddit.com/r/godot/comments/1tme9m5/that_moment_you_spend_days_on_a_feature_thats_not/) |
| reddit | Small_Sherbert2187 | ^39 c13 | [Why does every post feel pretextual? This subreddit is honestly just a crappier ](https://www.reddit.com/r/Unity3D/comments/1tmgar0/why_does_every_post_feel_pretextual/) |
| reddit | IncinerationGames | ^37 c43 | [How many wishlists did your game have when a publisher decided to sign it? Hey e](https://www.reddit.com/r/gamedev/comments/1tm76la/how_many_wishlists_did_your_game_have_when_a/) |
| reddit | ArmyOfChickens | ^32 c6 | [Npcs with advanced Ai Since starting my journey with godot 3 to being on 4.6 for](https://www.reddit.com/r/godot/comments/1tmtta7/npcs_with_advanced_ai/) |
| reddit | ElectricMachineGames | ^28 c16 | [Make sure you keep your distance from those prickle bombs! They are one of The C](https://www.reddit.com/r/Unity3D/comments/1tmfzhq/make_sure_you_keep_your_distance_from_those/) |
| reddit | Maxwellbundy | ^26 c2 | [Prototype of my Tower Defense where you need to build your own maze](https://www.reddit.com/r/godot/comments/1tmo8cj/prototype_of_my_tower_defense_where_you_need_to/) |
| bluesky | studioephua.bsky.social | ^23 c2 | [In Ashes has surpassed 5000 wishlists! Thank you for your support and patience t](https://bsky.app/profile/studioephua.bsky.social/post/3mmlovyasls2h) |
| reddit | lykenwel | ^21 c6 | [Finally finished my Painterly Shader for UE5 Been working on this Shader for qui](https://www.reddit.com/r/unrealengine/comments/1tmokyl/finally_finished_my_painterly_shader_for_ue5/) |
| reddit | Frank__West | ^18 c1 | [I added blackjack to Unity... In case you aren't aware, it's a reference to Futu](https://www.reddit.com/r/Unity3D/comments/1tmmdwi/i_added_blackjack_to_unity/) |
| reddit | tanetanetan | ^17 c4 | [Made a procedural underwater caustics shader for my 2D Unity game (no textures),](https://www.reddit.com/r/Unity3D/comments/1tm7muy/made_a_procedural_underwater_caustics_shader_for/) |
| reddit | GeraltTheBarbarian | ^16 c4 | [I built an offline neural machine translation plugin for UE5. No internet, no AP](https://www.reddit.com/r/unrealengine/comments/1tmcf1j/i_built_an_offline_neural_machine_translation/) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Illustrious-Scratch7</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 555 · 💬 10</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tml8tz/plenty_of_people_asked_how_i_did_art_style_for_my/" target="_blank" rel="noopener"><img src="https://preview.redd.it/l785g6fxv43h1.jpg?width=1948&amp;format=pjpg&amp;auto=webp&amp;s=31a16c3d3c685e0d6bd332c8d4834dccd22e0e2e" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Plenty of people asked how I did art style for my game, so here is my setup. Here is how I approached stylized rendering for my game: \- Most models are using only one tilable texture that is tinted b”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev ใน Godot อธิบาย stylized rendering pipeline: texture เดียวต่อ model ย้อมด้วย vertex color, outline จาก inverted normals, toon lighting shader, ตั้ง contrast ต่ำไว้ก่อนแล้วดึงกลับใน post process</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค low-contrast แล้วดึง contrast กลับใน post process ช่วยให้ artist คนเดียว unify assets ต่างกันโดยไม่ต้อง repaint ลด art production time ได้ชัดเจน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ทำแบบนี้ได้ใน URP: ใช้ vertex color tinting บน shared atlas, inverted-hull outline pass, DirectionalLight เดียว + toon HLSL shader — ลด per-asset art cost ใน project stylized ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tml8tz/plenty_of_people_asked_how_i_did_art_style_for_my/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rosehn</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 346 · 💬 13</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tmj70x/ive_been_learning_godot_over_the_past_year_to/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/bDdvam55aHNpNDNoMdRlGGf7LJM8IJhjoJMg957xpDs5C6Tzcsrqn1p7SoPc.png?format=pjpg&amp;auto=webp&amp;s=c4248b042090570c9ef4ffaf5f064f8561169436" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I've been learning Godot over the past year to make an old-school trading card RPG! I've always wished there were more games like the classic yugioh or pokemon tcg games, so I decided to make one. Ste”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev ใช้เวลา 1 ปีเรียน Godot เพื่อสร้าง trading card RPG สไตล์ retro ชื่อ 'Cardaire: Eternal Aces' มี Steam page แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>พิสูจน์ว่า solo dev สร้าง card-game RPG ด้วย Godot ได้ภายใน 12 เดือน — เป็น scope benchmark จริงสำหรับทีมเล็กที่สนใจ genre นี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู architecture ของ Cardaire ใน Godot เป็น cross-engine reference ได้เลย — mechanics เช่น deck, hand, battle state แปลง Unity ได้ตรงๆ และยังไม่มีใน portfolio ของ studio</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tmj70x/ive_been_learning_godot_over_the_past_year_to/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@zacharieg14</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 279 · 💬 11</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tmchd1/made_a_simple_animation_to_my_games_menu_in_5/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/bzhyZGl0cWw4MzNoMY426Uwd8GWwg4dBiH67XbomPHpA8R8TTFqcbdC0IsWF.png?format=pjpg&amp;auto=webp&amp;s=e0b212748d7eed5c5fe5642353655386fe054339" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Made a simple animation to my game's menu in 5 minutes, now it looks awesome! Hi there ! For those who are interested in the planet, I made it with this tutorial : [https://www.youtube.com/watch?v=tPl”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev คนนึงเพิ่ม animation ดาวเคราะห์ใน main menu เกม Godot ใช้เวลา 5 นาทีโดยทำตาม YouTube tutorial ผลลัพธ์ดูดีขึ้นมาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การลงทุนแค่ 5 นาทีกับ tutorial ช่วยยก perceived quality ของเกมได้ชัดเจน — proof ว่า polish เล็กๆ ส่งผลใหญ่ต่อ first impression</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง timebox สั้นๆ (ไม่เกิน 30 นาที) ก่อน milestone — ใช้ shader หรือ particle system ที่มีอยู่แล้วปั้น animation ให้ menu และ UI ดูมี polish ขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tmchd1/made_a_simple_animation_to_my_games_menu_in_5/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@andre_mc</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 274 · 💬 11</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/Unity3D/comments/1tmjo91/built_a_simple_goal_net_effect_that_cansimulate/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/ZHlodDlpYjBtNDNoMaiQIFGtgFloASNMB9EazzSc5fsuAbEBzKujilVTn1Li.png?format=pjpg&amp;auto=webp&amp;s=aa7e4d4ae12eaf0457aef638f8e85837b606b669" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Built a simple goal net effect that cansimulate back and forth! Shaders are truly magic!!!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev คนนึงสร้าง shader effect จำลองแห อย่างในเกมฟุตบอล ให้แกว่งไปมาได้ตามแรงที่กระทบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ได้ physics feel จาก shader ล้วนๆ ไม่ต้องใช้ Rigidbody หรือ cloth sim เลย ช่วยประหยัด performance มากโดยเฉพาะบน mobile และ XR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity นำแนวทาง shader-first นี้ไปใช้ทำ net, ผ้า, หรือธง ใน scene ที่ต้องการ physics feel โดยไม่จ่าย performance ค่า simulation</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1tmjo91/built_a_simple_goal_net_effect_that_cansimulate/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@erofamiliar</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 260 · 💬 32</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tm2e4h/working_on_a_survival_horror_its_still_very_early/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/eTZ0bHAxNmZtMDNoMQva5I01QUlbb-O9g6b_pjJ3GUIIgHxvnIXI0cE---M2.png?format=pjpg&amp;auto=webp&amp;s=8ad8dffd610e27cb942a4bc3de58fede03b9ab71" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“working on a survival horror, it's still VERY early but it's slowly getting there, gameplay-wise I don't really have a title or anything, and the gameplay you're seeing is just about the extent of it,”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev เดี่ยวแชร์ prototype survival horror ใน Godot ระยะแรกสุด มี locational damage ผ่าน script; ยังต้องทำ level design, sound และ polish อีกเยอะ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เลือก locational damage ผ่าน script แทน raycast แลก simplicity กับ flexibility — ต้อง benchmark ก่อน commit เมื่อ scale ขึ้น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง benchmark script-based vs. raycast locational damage ใน prototype ปัจจุบัน; โปสนี้ยัง normalize การหยุดพักแล้วกลับมา grind ต่อว่าเป็น pattern ปกติของ small team</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tm2e4h/working_on_a_survival_horror_its_still_very_early/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Sea-Good5788</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 243 · 💬 23</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tmjhu7/oh_so_fluffy_im_proud_of_it/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/dGRqZWFrM3JrNDNoMbd73V375KqV_CzKdI_MxZNkRo8Lxoq-cqIf_5otLKK0.png?format=pjpg&amp;auto=webp&amp;s=3862b580bbc94a639384b4750477633c5cc2623d" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“oh so fluffy!! im proud of it yes i AM that same guy who's obsessed with clouds on this sub.. still working on improving it, i want to make the BEST cloud shader for godot. and im STILL making the tut”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาบน r/godot แชร์ cloud shader ที่ดูฟูนุ่ม สร้างใน Godot โดยตั้งเป้าทำให้เป็น cloud shader ที่ดีที่สุด พร้อม tutorial ที่กำลังทำอยู่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การวิจัย shader จาก community พร้อม tutorial ฟรี หมายถึง cloud solution สำหรับ Godot ที่ผ่านการ iterate มาแล้ว — บอกว่า atmospheric visuals แบบ stylized ทำได้โดยไม่ต้องใช้ budget ระดับ AAA</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู approach ของ shader นี้เป็น reference ตอนทำ sky หรือ environment system — bookmark tutorial ไว้ พอออกใช้เป็น resource ตรงๆ สำหรับ visual polish ใน 3D scene</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tmjhu7/oh_so_fluffy_im_proud_of_it/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Equal_Money4055</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 191 · 💬 20</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tmfu7j/screenshots_from_my_wip_game/" target="_blank" rel="noopener"><img src="https://preview.redd.it/p5z60p8kw33h1.png?width=1280&amp;format=png&amp;auto=webp&amp;s=33fe40355ad578aea96f80f58ca965c73de6f4d9" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Screenshots from my WIP Game the game is based on collecting photo evidence and proving your paranoia. so far how's the visuals?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev โชว์ WIP screenshots เกม paranoia ที่ผู้เล่นต้องเก็บ photo evidence เพื่อพิสูจน์ความสงสัย ขอ feedback เรื่อง visuals</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ระบบเก็บ evidence เป็น mechanic ที่ scope เล็กแต่สร้าง tension สูง ไม่ต้องพึ่ง combat system หนักๆ เหมาะกับทีมเล็ก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team หยิบ mechanic camera raycast + evidence log ไปใส่ prototype horror หรือ mystery ได้เลย ต้นทุน asset ต่ำมาก</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tmfu7j/screenshots_from_my_wip_game/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Kudlattyy</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 179 · 💬 89</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/gamedev/comments/1tmktci/in_case_anyone_missed_it_epic_teased_unreal/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/9ZxT4u_u2fmEy77pWhkELckscwjSqJsrwdm7clcX_po.jpeg?auto=webp&amp;s=c8532ec3866ed47fa2fb6652355ded011b4166a6" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In case anyone missed it, Epic teased Unreal Engine 6. [https://www.youtube.com/watch?v=p5d7y1cbWIk](https://www.youtube.com/watch?v=p5d7y1cbWIk)”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Epic Games ปล่อย teaser ของ Unreal Engine 6 ทาง YouTube มีคนแชร์ใน r/gamedev เผื่อใครพลาด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>UE6 คือ major shift ครั้งต่อไปของ real-time rendering — รู้ roadmap ไว้ก่อนช่วยให้ทีมวางแผน migration หรือจังหวะ adopt ได้ทัน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ควรดู teaser เพื่อ benchmark ทิศทาง UE6 ด้าน XR และ visual fidelity — ช่วยประกอบการตัดสินใจเรื่อง engine สำหรับ pitch XR/VR ต่อไป</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/gamedev/comments/1tmktci/in_case_anyone_missed_it_epic_teased_unreal/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
</div>
