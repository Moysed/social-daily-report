---
type: social-topic-report
date: '2026-05-24'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-24T15:10:32+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- reddit
- rss
- x
regions:
- global
post_count: 75
salience: 0.55
sentiment: neutral
confidence: 0.6
tags:
- godot
- unity
- hdrp
- indie-gamedev
- rendering
- steam
thumbnail: https://external-preview.redd.it/bDhieGF1amY3eDJoMRIhTtrPaTzJQdAEkB6mIxD6SBrKpfWFk8yB5u1XNXWA.png?format=pjpg&auto=webp&s=f13a18d0ec204875d5991f167e6f0daefb40bd59
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-24

## TL;DR
- Godot ครองปริมาณโพสต์ใน indie showcase วันนี้ — fishing mechanics [1], Gravity Gun clones [2], survival horror [3], Parkour FPS [6] — สะท้อน momentum ของ community ที่ยังเติบโตต่อเนื่องเมื่อเทียบกับโพสต์ Unity/Unreal
- showcase เชิงเทคนิคของ Unity เน้นหนักไปที่ advanced rendering: HDRP real-time scene voxelization สำหรับ GI [8], procedural zero-texture shader NPCs ที่รัน 500/100FPS [22], stylized billboard foliage [5]
- เนื้อหา Unreal เบาบางและเน้นระดับเริ่มต้น (UE5.7 low-end optimization [26], Blueprint array gating [33]) — สัญญาณ pro-pipeline น้อยมากในวันนี้
- สัญญาณด้าน production/marketing: ปุ่ม Steam Playtest เปิดใช้งานได้ที่ 230 wishlists [19], milestone 5000 wishlists [24], scam ที่มุ่งเป้า indie รายเล็กเพิ่มสูงขึ้น [16]
- ไม่พบรายการ AI-in-pipeline ในวันนี้ — generative tools ไม่ปรากฏใน top 40 แสดงว่า community ให้ความสนใจกับ craft และ rendering tech มากกว่า

## What happened
Reddit r/godot ครองการมีส่วนร่วมด้วยโพสต์ WIP gameplay ที่ขัดเกลาแล้ว [1][2][3][6][11][17][30] รวมถึงการแชร์ tooling/plugin [13][15][27] เนื้อหาของ Unity3D เอียงไปทาง technical-rendering: HDRP GPU voxelization สำหรับ real-time GI ในโลก procedural [8], ระบบ shader-based NPC ที่ render agent 500 ตัวที่ 100fps โดยไม่ใช้ texture เลย [22], และ workflow ของ stylized billboard-card foliage [5][13] Unreal มีเพียงสามรายการ ทั้งหมดเป็นระดับ support: UE5.7 low-end GPU optimization [26], Blueprint dialogue gating [33], และ tutorial series turn-based combat 64 ตอน [35] Bluesky #ScreenshotSaturday เติมเต็มส่วนท้ายด้วย WIP ของ solo-dev [20][24][29][31][32][36][37][39][40] สัญญาณด้าน production: solo dev ที่สะท้อนถึงการเปลี่ยนเกมจากข้อความของผู้เล่นคนเดียว [10], scam ที่มุ่งเป้า indie ที่มีคนรู้จักน้อย [16], และ milestone wishlist/playtest บน Steam [19][24]

## Why it matters (reasoning)
สัดส่วนโพสต์ที่ Godot ได้รับ engagement สูงยังคงเพิ่มขึ้นเทียบกับ Unity/Unreal ใน indie community space — มีความเกี่ยวข้องเพราะ stack ที่เน้น Unity ของ NDF DEV ไม่ใช่ตัวเลือกหลักของ indie อีกต่อไป แม้ Unity ยังคงครอง heavy-rendering conversation [8][22] HDRP voxel-GI port [8] มีความสำคัญในเชิงเทคนิค: real-time GI สำหรับ scene แบบ procedural/dynamic เป็นจุดอ่อนที่ Unity เสียเปรียบ Unreal Lumen มาอย่างยาวนาน และ solution ที่ขับเคลื่อนโดย community ช่วยลดช่องว่างนั้นสำหรับ studio ที่ไม่สามารถ justify การย้ายไป Unreal ได้ ระบบ shader-NPC [22] เป็น pattern ที่ใช้งานได้จริงสำหรับ scene ที่มีฝูงชนใน XR/edutech ซึ่ง draw-call budget มีข้อจำกัด รายงาน scam-targeting [16] เป็นผลกระทบทางอ้อมจากการ publish บน Steam ที่มีขั้นตอนน้อย — studio เล็กที่มี public devlog กลายเป็น attack surface

## Possibility
ระยะสั้น (3-6 เดือน, ~70%): Godot ยังคงดูดซับ mindshare ของ solo/small-team ในขณะที่ Unity ยึดครอง mid-tier production และ Unreal ยึดครอง AAA/arch-viz — การแบ่งส่วนสามฝ่ายนิ่งตัว ระยะกลาง (~50%): feature community-rendering ของ HDRP [8] ถูกรวมเข้าไปใน URP หรือ official Unity packages เมื่อ Unity ตอบสนองต่อแรงกดดันของ Lumen โอกาสต่ำกว่า (~25%): indie hit ที่โดดเด่นที่ shipped บน Godot ในปี 2026 กระตุ้นการเร่งตัวของ tooling/asset-store ที่ช่วยปิดช่องว่าง production-pipeline กับ Unity

## Org applicability — NDF DEV
นำไปใช้งานได้โดยตรง: ศึกษา [8] แนวทาง voxel-GI หากโปรเจกต์ XR/VR ของ NDF ใดๆ ต้องการ dynamic GI ในสภาพแวดล้อม procedural — แต่ HDRP รองรับเฉพาะ desktop/PC ไม่รองรับ Quest จึงมีประโยชน์จำกัดสำหรับ VR pipeline [22] pattern ของ shader-NPC ใช้งานได้โดยตรงกับ scene ฝูงชนใน edutech และ mobile Unity build ที่ texture memory มีข้อจำกัด — คุ้มค่ากับการ spike 1 วัน [5][13] workflow ของ billboard-foliage เป็น quick win สำหรับ Unity scene กลางแจ้งที่กำหนดเป้าหมาย low-end Android/Quest [16] ควรแจ้ง team เรื่อง scam หาก NDF title ใดขึ้น Steam ไม่คุ้มค่าที่จะดำเนินการ: การย้ายไป Godot (ไม่มี business case จากสัญญาณวันนี้), Unreal low-end optimization [26] (นอก stack)

## Signals to Watch
- จับตาว่า Unity จะ ship คำตอบอย่างเป็นทางการสำหรับ community HDRP voxel-GI [8] ใน roadmap update ถัดไปหรือไม่
- ติดตาม adoption curve ของ Godot 4.x บน Steam — หาก breakout hit ขึ้นมา ecosystem ของ asset/tooling อาจเร่งตัว
- ติดตาม rendering trick ที่กำหนดเป้าหมาย Quest/mobile (shader NPCs [22], billboard foliage [5][13]) สำหรับ NDF VR backlog
- จับตา pattern ของ indie scam [16] — อาจต้องมี studio-side policy สำหรับการติดต่อที่ไม่ได้ร้องขอ

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | im_arseny | ^335 c20 | [working on a fishing mechanic in my game about a gopher catching stars from the ](https://www.reddit.com/r/godot/comments/1tlmda5/working_on_a_fishing_mechanic_in_my_game_about_a/) |
| reddit | Jeheno | ^234 c7 | [Half-Life 2's Gravity Gun recreation](https://www.reddit.com/r/godot/comments/1tlphly/halflife_2s_gravity_gun_recreation/) |
| reddit | erofamiliar | ^186 c29 | [working on a survival horror, it's still VERY early but it's slowly getting ther](https://www.reddit.com/r/godot/comments/1tm2e4h/working_on_a_survival_horror_its_still_very_early/) |
| reddit | EscapeDoodland | ^170 c6 | [Working on something new](https://www.reddit.com/r/Unity3D/comments/1tlkigm/working_on_something_new/) |
| reddit | craftymech | ^130 c4 | [Stylized Foliage Fun with stylized foliage! I've created 12 tree/bush species no](https://www.reddit.com/r/Unity3D/comments/1tllqgs/stylized_foliage/) |
| reddit | SSV-Interactive | ^112 c24 | [Showcasing My First Game "RUNFALL" RUNFALL is first person Parkour with world sh](https://www.reddit.com/r/godot/comments/1tlng2f/showcasing_my_first_game_runfall/) |
| reddit | Fabrix10 | ^98 c43 | [Is there a way to get squared edges instead of rounded edges for a Label outline](https://www.reddit.com/r/godot/comments/1tlu3rx/is_there_a_way_to_get_squared_edges_instead_of/) |
| reddit | artengame | ^84 c12 | [Finally managed to port real time scene voxelization natively in HDRP for Global](https://www.reddit.com/r/Unity3D/comments/1tln2yw/finally_managed_to_port_real_time_scene/) |
| reddit | BlastingBlaster | ^84 c8 | [Added colorful rainbow road like shader to my level!](https://www.reddit.com/r/godot/comments/1tltdj9/added_colorful_rainbow_road_like_shader_to_my/) |
| reddit | Soliloqu-You | ^68 c34 | [Have you ever changed your game because of one player's message? Hi everyone. I'](https://www.reddit.com/r/gamedev/comments/1tm8f61/have_you_ever_changed_your_game_because_of_one/) |
| reddit | Squirrelation_Games | ^63 c2 | [Oops. Someone forgot to hide the player model](https://www.reddit.com/r/godot/comments/1tlouby/oops_someone_forgot_to_hide_the_player_model/) |
| reddit | zacharieg14 | ^62 c2 | [Made a simple animation to my game's menu in 5 minutes, now it looks awesome! Hi](https://www.reddit.com/r/godot/comments/1tmchd1/made_a_simple_animation_to_my_games_menu_in_5/) |
| reddit | Planet1Rush | ^41 c0 | [Updated my foliage system: MultiMesh now supports LODs and collision in debug mo](https://www.reddit.com/r/godot/comments/1tlrdkj/updated_my_foliage_system_multimesh_now_supports/) |
| reddit | Aalzard | ^31 c6 | [Okay guys, look at this main menu for my game 👀 This is the main menu for my coo](https://www.reddit.com/r/Unity3D/comments/1tlsov6/okay_guys_look_at_this_main_menu_for_my_game/) |
| reddit | PensiveDemon | ^31 c5 | [[Convert Text Case] Built a plugin for myself - Should I share it to the Asset S](https://www.reddit.com/r/godot/comments/1tm9dew/convert_text_case_built_a_plugin_for_myself/) |
| reddit | ploxiar | ^30 c13 | [watch out for scammers Hello, there is a target on unreleased / released indie g](https://www.reddit.com/r/gamedev/comments/1tljjgd/watch_out_for_scammers/) |
| reddit | Shabaubi | ^30 c2 | [I made an environment based off the backrooms trailer shot Very excited for the ](https://www.reddit.com/r/godot/comments/1tlps6y/i_made_an_environment_based_off_the_backrooms/) |
| reddit | Krons-sama | ^29 c2 | [I tried applying parallax to the particles system](https://www.reddit.com/r/Unity3D/comments/1tlmzf4/i_tried_applying_parallax_to_the_particles_system/) |
| reddit | JetPoweredGames | ^29 c2 | [My Steam Playtest is Live! Big Saturday Update to Iron Dogs. Many tweaks, added ](https://www.reddit.com/r/godot/comments/1tlvjkm/my_steam_playtest_is_live/) |
| bluesky | projectsentinelgame.com | ^29 c0 | [I've been refining the roar and arrest mechanics. The Sentinel uses a cybernetic](https://bsky.app/profile/projectsentinelgame.com/post/3mmkbx7azzs2f) |
| reddit | alexwizardev | ^24 c12 | [Roast my game's look Hey everyone, I'm trying to nail the retro vibe for my game](https://www.reddit.com/r/Unity3D/comments/1tlvl0w/roast_my_games_look/) |
| reddit | SignificanceLeast172 | ^23 c5 | [I made a procedural zero-texture, shader-based NPC creation system that runs 500](https://www.reddit.com/r/Unity3D/comments/1tlvvu3/i_made_a_procedural_zerotexture_shaderbased_npc/) |
| reddit | yowanselvakumar | ^21 c0 | [we ready to make our first indie title hopefully we believe this prototype make ](https://www.reddit.com/r/Unity3D/comments/1tln7jq/we_ready_to_make_our_first_indie_title/) |
| bluesky | studioephua.bsky.social | ^20 c2 | [In Ashes has surpassed 5000 wishlists! Thank you for your support and patience t](https://bsky.app/profile/studioephua.bsky.social/post/3mmlovyasls2h) |
| reddit | Deimor_ | ^19 c7 | [transferring my game to Unity im converting my pixel art game to a 3D cartoon in](https://www.reddit.com/r/Unity3D/comments/1tlynmb/transferring_my_game_to_unity/) |
| reddit | Unusual-Newt-96 | ^18 c11 | [How do i optimize the engine for lower end hardware Hi there Currently on UE5.7 ](https://www.reddit.com/r/unrealengine/comments/1tlq6z1/how_do_i_optimize_the_engine_for_lower_end/) |
| reddit | Jadael | ^18 c1 | [Terrablox - Voxel 3D virtual tabletop For the past month, I've been prototyping ](https://www.reddit.com/r/godot/comments/1tlt44j/terrablox_voxel_3d_virtual_tabletop/) |
| reddit | IamChipp | ^17 c1 | [I love how wild is this community here Sorry if this comes across as low effort ](https://www.reddit.com/r/godot/comments/1tmbl78/i_love_how_wild_is_this_community_here/) |
| bluesky | ditheremotion.bsky.social | ^17 c0 | [Never posted anything for #ScreenshotSaturday until now but hey, better late tha](https://bsky.app/profile/ditheremotion.bsky.social/post/3mmk4c4p45k25) |
| reddit | Zany19 | ^15 c3 | [First look of my Godot game that I've been working on for 8 Months "Lilifel" The](https://www.reddit.com/r/godot/comments/1tlkaz8/first_look_of_my_godot_game_that_ive_been_working/) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@im_arseny</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 335 · 💬 20</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tlmda5/working_on_a_fishing_mechanic_in_my_game_about_a/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/bDhieGF1amY3eDJoMRIhTtrPaTzJQdAEkB6mIxD6SBrKpfWFk8yB5u1XNXWA.png?format=pjpg&amp;auto=webp&amp;s=f13a18d0ec204875d5991f167e6f0daefb40bd59" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“working on a fishing mechanic in my game about a gopher catching stars from the sky”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev สร้าง fishing mechanic ใน Godot — ตัวละคร gopher ตกดาวจากท้องฟ้าแทนปลา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เอา mechanic คุ้นเคย (ตกปลา) ใส่ context แปลก ๆ เป็นสูตรสร้าง virality ได้ดี — 335 likes ตอน WIP บอกว่า concept แข็งแกร่งมาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team เอาไปใช้ได้เลย: หยิบ mechanic มาตรฐาน แล้วเปลี่ยน semantic layer — code เหมือนเดิม แต่ feel ต่างสิ้น — prototype ไว, concept value สูง</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlmda5/working_on_a_fishing_mechanic_in_my_game_about_a/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Jeheno</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 234 · 💬 7</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tlphly/halflife_2s_gravity_gun_recreation/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/c2x1b2k5czR0eDJoMexf6Ifygwfa-FFy1AtzJb_WCmwM8crvquWNI3-_V3-C.png?format=pjpg&amp;auto=webp&amp;s=62898f9f70649ce07385d4d33b6762be96957996" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Half-Life 2's Gravity Gun recreation”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาสร้าง Gravity Gun จาก Half-Life 2 ขึ้นมาใหม่ใน Godot engine แล้วแชร์ใน r/godot</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ระบบจับ-ขว้างวัตถุแบบ physics เป็น mechanic ที่นำไปใช้ซ้ำได้ — การ implement ที่สะอาดใน Godot ให้ blueprint อ้างอิงสำหรับเกมที่เน้น physics</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดู logic ของระบบนี้เป็น reference ตอนสร้าง grab/throw mechanics ใน XR project เพราะ physics feel ของมือกับวัตถุสำคัญมากใน XR</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlphly/halflife_2s_gravity_gun_recreation/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@erofamiliar</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 186 · 💬 29</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tm2e4h/working_on_a_survival_horror_its_still_very_early/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/eTZ0bHAxNmZtMDNoMQva5I01QUlbb-O9g6b_pjJ3GUIIgHxvnIXI0cE---M2.png?format=pjpg&amp;auto=webp&amp;s=8ad8dffd610e27cb942a4bc3de58fede03b9ab71" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“working on a survival horror, it's still VERY early but it's slowly getting there, gameplay-wise I don't really have a title or anything, and the gameplay you're seeing is just about the extent of it,”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev คนเดียวโชว์ progress เกม survival horror ใน Godot ช่วง early มาก — ยังขาด level design, sound design และ mechanic kick ที่ตัดหัวศัตรูเพื่อทดสอบ locational damage จาก script แทน raycast</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การใช้ script ทดสอบ locational damage ก่อนล็อค raycast แสดง mindset iterate ไวที่ทีมเล็กควรยืมมาใช้ตอน prototype ระบบ combat</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง wire placeholder hit zone ใน script ก่อน แล้วค่อย swap เป็น raycast จริงตอน gameplay feel โอเคแล้ว ประหยัดเวลา rework</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tm2e4h/working_on_a_survival_horror_its_still_very_early/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@EscapeDoodland</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 170 · 💬 6</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/Unity3D/comments/1tlkigm/working_on_something_new/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/NzRqeHAwZHp0dzJoMWDB3wTLoVrePXTwSowOLksrWWOytGzGRym7NHqsTknw.png?auto=webp&amp;s=f3e28ad03b23ca24e9360b913cd237104ebed872" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Working on something new”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer บน r/Unity3D โพสต์ teaser ชื่อ 'Working on something new' น่าจะเป็น screenshot หรือ GIF ของ game ที่กำลังพัฒนา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>170 likes แต่ comment แค่ 6 — visual WIP บน r/Unity3D ดึง organic reach ได้ดีโดยไม่ต้องรอ content สมบูรณ์</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team โพสต์ WIP ระยะแรกบน r/Unity3D ได้เลย ไม่ต้องรอ polish — screenshot ดิบๆ ก็ reach ได้ดีพอกัน</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1tlkigm/working_on_something_new/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@craftymech</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 130 · 💬 4</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/Unity3D/comments/1tllqgs/stylized_foliage/" target="_blank" rel="noopener"><img src="https://i.redd.it/b5h62nqf2x2h1.jpeg" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Stylized Foliage Fun with stylized foliage! I've created 12 tree/bush species now using the rotating billboard technique and foliage cards that I draw in Photoshop. The foliage cards are really just a”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev สร้างต้นไม้/พุ่มไม้ stylized 12 สายพันธุ์ใน Unity โดยใช้ foliage card แบบ alpha cut-out palette 3 สี และ rotating billboard แล้วพัก workflow ไว้ใน Unity tool ของตัวเอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่าได้ foliage stylized สวยและ dense ด้วย flat card ง่ายๆ ซ้อนกัน โดยไม่ต้องใช้ geometry ซับซ้อน ต้นทุน polygon ต่ำมาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team สร้าง foliage card tool แบบ reusable ด้วย pipeline billboard+alpha-cutout นี้ เร่ง environment art ได้เลยสำหรับ project stylized ทุกโปรเจกต์</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1tllqgs/stylized_foliage/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@SSV-Interactive</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 112 · 💬 24</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tlng2f/showcasing_my_first_game_runfall/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/ZXppeDlnaHlleDJoMRe0JTZBc2IlAkUhTTl_8G4spqhx-a-bZQ1Kkeshgh83.png?format=pjpg&amp;auto=webp&amp;s=20368838876067fda66c783e79c4648cbd4cc715" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Showcasing My First Game &quot;RUNFALL&quot; RUNFALL is first person Parkour with world shifting mech like Titanfall 2 , wanted to do my version of something like that , huge fan of titanfall movement mech. Hop”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer เดี่ยวโชว์เกมแรก 'RUNFALL' ใน Godot — first-person parkour ที่มี world-shifting mechanic แบบ Titanfall 2</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ระบบ movement ของ Titanfall 2 ถูกยกย่องมาก การที่ solo dev ทำได้ใน Godot พิสูจน์ว่าไม่ต้องใช้ทีม AAA หรือ Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดู Titanfall 2-style world-shift เป็น pattern สำหรับ XR/VR locomotion — mechanic หมุน/เปลี่ยน space ใช้กับ headset ได้ดี</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlng2f/showcasing_my_first_game_runfall/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Fabrix10</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 98 · 💬 43</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tlu3rx/is_there_a_way_to_get_squared_edges_instead_of/" target="_blank" rel="noopener"><img src="https://preview.redd.it/srs8ba7spy2h1.png?width=1092&amp;format=png&amp;auto=webp&amp;s=91fc210eb60849dc81fd991f16270d3ef05ce6d3" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Is there a way to get squared edges instead of rounded edges for a Label outline? Hello, I was trying to create a Label using a pixel font(Jersey 10) and while the font renders correctly I'm strugglin”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer ใน Godot พบว่า outline ของ pixel font โค้งมนโดย default แก้ได้โดยแปลง font เป็น bitmap font ผ่านเว็บ Snowb.io แล้วตั้งค่า stroke ก่อน import</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Godot ไม่มี option squared outline ใน Label โดยตรง การ bake stroke ลง bitmap font ตอน export คือวิธีเดียวที่เชื่อถือได้สำหรับ pixel-art UI</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ที่ทำ 2D หรือ pixel-art UI ควรลอง bake bitmap font ผ่าน Snowb.io แทนการใช้ runtime outline shader ซึ่งมักให้ผลโค้งมนกับ font ขนาดเล็ก</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlu3rx/is_there_a_way_to_get_squared_edges_instead_of/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@artengame</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 84 · 💬 12</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/Unity3D/comments/1tln2yw/finally_managed_to_port_real_time_scene/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/bms4bTd2bWtieDJoMc8VuwnK_eXu-0d0e4QadjeAY4x_v2K247NwPfMfRfQh.png?format=pjpg&amp;auto=webp&amp;s=fcde5b1d7bf4c36f15805967742764d480603272" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Finally managed to port real time scene voxelization natively in HDRP for Global Illumination and other uses, using GPU for maximum performance and full support of procedural changing worlds.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev ทำ real-time scene voxelization ใน Unity HDRP สำเร็จ ใช้ GPU เต็มรูปแบบ รองรับ Global Illumination และ procedural world ที่เปลี่ยนแปลงได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>GPU voxelization ใน HDRP ทำให้ได้ dynamic GI โดยไม่ต้อง bake lightmap เลย สำคัญมากสำหรับเกมที่ generate หรือเปลี่ยน environment แบบ runtime</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดูเทคนิคนี้ได้เลยสำหรับ HDRP project ที่มี dynamic scene — เลิก bake GI ลด iteration time และรองรับการเปลี่ยน level แบบ real-time โดยไม่ต้อง re-light</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1tln2yw/finally_managed_to_port_real_time_scene/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
</div>
