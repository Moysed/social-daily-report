---
type: social-topic-report
date: '2026-05-24'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-24T03:09:42+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- reddit
- rss
- x
regions:
- global
post_count: 76
salience: 0.35
sentiment: mixed
confidence: 0.6
tags:
- godot
- unity
- indie-gamedev
- graphics
- shaders
- monetization
thumbnail: https://i.redd.it/mmck6oidbv2h1.jpeg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-24

## TL;DR
- Godot ครองสัญญาณวันนี้ — 14+ จาก 40 อันดับแรกเป็น Godot showcase บ่งชี้ว่า tooling ของ indie กำลังเทียบเท่า Unity มากขึ้น [1][2][4][5][6][8][9]
- ไฮไลท์เชิงเทคนิค: HDRP real-time scene voxelization สำหรับ GI [18], compute-shader water interaction [17], Dijkstra map pathfinding viz [21], UE5 fluid sim wave breaks [22]
- thread ตรวจสอบความเป็นจริงด้าน indie monetization โผล่ขึ้นมา; ช่องว่างระหว่างความคาดหวังกับรายได้จริงคือบ่นซ้ำๆ [7]
- ไม่มี engine release ครั้งใหญ่หรือข่าว AI-pipeline ในชุดนี้ — เนื้อหาส่วนใหญ่เป็น WIP screenshots, VFX experiments, และ milestone ของ solo-dev
- มุมมองเชิงอารมณ์/ชุมชน: เกมของ Godot dev ช่วยให้ผู้เล่นในเขตสงครามรู้สึกดีขึ้น [1] — เตือนใจว่าเกมมีความหมายเกินกว่าแค่ mechanics

## สิ่งที่เกิดขึ้น
feed game-dev วันนี้หนักไปด้วย Godot indie showcase — destruction systems [2], split-screen multiplayer [5], การสร้าง gravity gun จาก Half-Life 2 ขึ้นมาใหม่ [8], multimesh stress test ระยะ draw-distance 100km [9], และ platformer แรกของเด็กอายุ 16 ปี [4] เนื้อหา Unity เน้นเทคนิค: HDRP real-time scene voxelization สำหรับ GI บน procedural worlds [18], compute-shader water interaction [17], stylized billboard foliage [14], และการทดสอบ volumetric fog atmospheric [13] Unreal ปรากฏเพียงครั้งเดียวผ่าน fluid-sim wave-break plugin [22] thread ถามความเห็น indie dev เรื่องรายได้จริงกับความคาดหวัง [7] — 163 comments, เป็นรายการที่มีคนแสดงความคิดเห็นมากที่สุด

ไม่มี engine version release, ไม่มีข่าว AI-in-pipeline, ไม่มีการเคลื่อนไหวครั้งใหญ่ของอุตสาหกรรม สัญญาณเป็น community/showcase ไม่ใช่การประกาศ หนึ่งรายการที่โดดเด่นด้านอารมณ์ [1] — เกมของ dev ที่ช่วยให้คนในเขตสงครามรู้สึกดีขึ้น — ดึง engagement score สูงสุด

## ทำไมถึงสำคัญ (เหตุผล)
ความเข้มข้นของ Godot สำคัญ: เมื่อปีที่แล้วรายการนี้คงเป็น Unity เป็นหลัก ความเท่าเทียมด้าน tooling (multiplayer, multimesh scale, shader effects, custom UI work [20]) กำลังแคบลงสำหรับ indie ขนาด 2D และ stylized-3D — ซึ่งตรงกับ wheelhouse ด้าน edutech/web-game ของ NDF DEV พอดี โพสต์เทคนิคของ Unity [17][18] แสดงให้เห็นว่า engine ยังนำหน้าด้าน AAA-grade graphics R&D (voxel GI, compute shaders) ตอกย้ำการแบ่งแยก: Unity สำหรับ high-fidelity XR/3D, Godot สำหรับเป้าหมาย 2D/web ที่คล่องตัว thread รายได้ [7] เป็นสัญญาณตลาดที่เกิดซ้ำ — solo-dev monetization ยังคงโหดร้าย ซึ่งยืนยันทิศทาง contract/edutech mix ของ NDF ดีกว่าการพนัน indie บริสุทธิ์ การไม่มีเนื้อหา AI-pipeline ในอันดับ top 40 วันนี้เป็นสัญญาณในตัวเอง — hype cycle เย็นลงแล้ว กลายเป็น 'tools ที่ dev ใช้อยู่เงียบๆ' ไม่ใช่ข่าวพาดหัว

## ความเป็นไปได้
น่าจะเกิด (70%): Godot กินส่วนแบ่ง 2D/hobbyist จาก Unity ต่อเนื่องตลอดปี 2026; คาดว่าจะมี commercial release ขนาด mid-scope ที่ ship บน Godot มากขึ้น เป็นไปได้ (40%): งาน HDRP voxel-GI ของ Unity [18] ไหลลงสู่ URP ภายใน 12 เดือน ช่วยเพิ่ม fidelity ด้าน mobile/XR น่าจะเกิดน้อย (20%): Godot title ที่ viral เพียงเกมเดียวในปีนี้บังคับให้มีการประเมินใหม่ในระดับ enterprise การสะท้อนอารมณ์ของชุมชน [1] ชี้ให้เห็นว่าเกม narrative ขนาดเล็กยังคงดึงความสนใจได้เกินมูลค่าที่ควร

## การนำไปใช้ใน Org — NDF DEV
ความเกี่ยวข้องโดยตรง: จำกัดวันนี้ ไม่มีรายการใดที่ต้องดำเนินการทันที สิ่งที่ควรสังเกตสำหรับ NDF: (a) split-screen ของ Godot [5] และ far-camera multimesh [9] ทำให้มันเป็น candidate ที่น่าเชื่อถือสำหรับ edutech prototype ขนาดเบาที่ Unity รู้สึกหนักเกินไป — คุ้มค่าทดลอง 1 วัน ไม่ใช่เปลี่ยน stack ทั้งหมด (b) Unity compute-shader water [17] และ HDRP voxel GI [18] เป็น reference material สำหรับเป้าหมาย VRoom/XR fidelity — bookmark ไว้ อย่านำมาใช้ตอนนี้ (c) เทคนิค stylized billboard foliage [14] ถูกและนำไปใช้ได้โดยตรงกับงาน open-world หรือ e-learning environment (d) thread รายได้ indie [7] ตอกย้ำ: ยึด client work เป็นกระดูกสันหลัง; มองเกม NDF original เป็น long-tail ไม่ใช่แหล่งรายได้หลัก ความเกี่ยวข้องโดยรวมต่ำ — สังเกตการณ์ อย่าเปลี่ยนทิศทาง

## สัญญาณที่ต้องติดตาม
- ติดตาม Godot 4.x adoption ใน commercial mid-scope release — ข้อกล่าวอ้างความเท่าเทียมจะพิสูจน์หรือล้มเหลว
- Unity HDRP→URP feature backports (โดยเฉพาะ voxel GI) เพื่อความเป็นไปได้ด้าน XR
- thread สำรวจรายได้ indie รายไตรมาสถัดไป — การเปลี่ยนแปลง sentiment = proxy สุขภาพตลาด
- AI-pipeline tooling ใดๆ (texture/animation/level-gen) ที่กลับมาปรากฏใน top engagement

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | Psychological-Road19 | ^1790 c26 | [My game gave someone comfort in an active warzone and it's stuck with me since. ](https://www.reddit.com/r/godot/comments/1tld9wx/my_game_gave_someone_comfort_in_an_active_warzone/) |
| reddit | Matiesus | ^822 c36 | [I added some destruction to my super "hero" game](https://www.reddit.com/r/godot/comments/1tlfd5o/i_added_some_destruction_to_my_super_hero_game/) |
| reddit | binbun3 | ^271 c9 | [Claw Effect From my Battle FX: [https://binbun3d.itch.io/battle-fx](https://binb](https://www.reddit.com/r/godot/comments/1tldrkm/claw_effect/) |
| reddit | Juaniesteban | ^257 c25 | [I'm a 16 Year Old developer making my first game! Would love to hear some feedba](https://www.reddit.com/r/godot/comments/1tlicub/im_a_16_year_old_developer_making_my_first_game/) |
| reddit | Fit-Hovercraft-7669 | ^231 c14 | [I've added multiplayer split-screen to my ArcadeRacer Recently my multiplayer re](https://www.reddit.com/r/godot/comments/1tlbrag/ive_added_multiplayer_splitscreen_to_my/) |
| reddit | im_arseny | ^224 c13 | [working on a fishing mechanic in my game about a gopher catching stars from the ](https://www.reddit.com/r/godot/comments/1tlmda5/working_on_a_fishing_mechanic_in_my_game_about_a/) |
| reddit | PrudentCombination38 | ^132 c163 | [How much did your indie game earn? Hi everyone, I'm curious about the real exper](https://www.reddit.com/r/gamedev/comments/1tl9ph3/how_much_did_your_indie_game_earn/) |
| reddit | Jeheno | ^130 c4 | [Half-Life 2's Gravity Gun recreation](https://www.reddit.com/r/godot/comments/1tlphly/halflife_2s_gravity_gun_recreation/) |
| reddit | derethdweller | ^127 c24 | [i was fully expecting godot to crash when i asked him to render that Camera far ](https://www.reddit.com/r/godot/comments/1tl849y/i_was_fully_expecting_godot_to_crash_when_i_asked/) |
| reddit | EscapeDoodland | ^100 c2 | [Working on something new](https://www.reddit.com/r/Unity3D/comments/1tlkigm/working_on_something_new/) |
| reddit | FederalProfessor7836 | ^98 c24 | [Quetoo, a love letter to the QUAKE series, released after 19 years This one has ](https://www.reddit.com/r/gamedev/comments/1tlivz7/quetoo_a_love_letter_to_the_quake_series_released/) |
| reddit | PrinceOnAPie | ^91 c4 | [Some before and afters of my game, trying to create a consistent artstyle If you](https://www.reddit.com/r/godot/comments/1tlfwig/some_before_and_afters_of_my_game_trying_to/) |
| reddit | halisavakis | ^87 c7 | [Made another atmospheric foggy scene to play around with lighting and colors Thi](https://www.reddit.com/r/Unity3D/comments/1tlfbru/made_another_atmospheric_foggy_scene_to_play/) |
| reddit | craftymech | ^79 c4 | [Stylized Foliage Fun with stylized foliage! I've created 12 tree/bush species no](https://www.reddit.com/r/Unity3D/comments/1tllqgs/stylized_foliage/) |
| reddit | BManx2000 | ^77 c2 | [Lowered the tickrate to test interpolation but instead I became an arm flailing ](https://www.reddit.com/r/godot/comments/1tl79jb/lowered_the_tickrate_to_test_interpolation_but/) |
| reddit | SSV-Interactive | ^57 c9 | [Showcasing My First Game "RUNFALL" RUNFALL is first person Parkour with world sh](https://www.reddit.com/r/godot/comments/1tlng2f/showcasing_my_first_game_runfall/) |
| reddit | 24Ronin | ^54 c0 | [Water Interaction via Compute Shader](https://www.reddit.com/r/Unity3D/comments/1tl7x9k/water_interaction_via_compute_shader/) |
| reddit | artengame | ^45 c10 | [Finally managed to port real time scene voxelization natively in HDRP for Global](https://www.reddit.com/r/Unity3D/comments/1tln2yw/finally_managed_to_port_real_time_scene/) |
| reddit | BlastingBlaster | ^39 c3 | [Added colorful rainbow road like shader to my level!](https://www.reddit.com/r/godot/comments/1tltdj9/added_colorful_rainbow_road_like_shader_to_my/) |
| reddit | Fabrix10 | ^37 c32 | [Is there a way to get squared edges instead of rounded edges for a Label outline](https://www.reddit.com/r/godot/comments/1tlu3rx/is_there_a_way_to_get_squared_edges_instead_of/) |
| reddit | Merlord | ^36 c12 | [Visualising Dijkstra's Map values used in enemy pathfinding](https://www.reddit.com/r/godot/comments/1tlg5im/visualising_dijkstras_map_values_used_in_enemy/) |
| reddit | Atomic_Lighthouse | ^35 c21 | [Been working so hard on getting the wave break effect working in my sim. This is](https://www.reddit.com/r/unrealengine/comments/1tlbf47/been_working_so_hard_on_getting_the_wave_break/) |
| reddit | Squirrelation_Games | ^31 c1 | [Oops. Someone forgot to hide the player model](https://www.reddit.com/r/godot/comments/1tlouby/oops_someone_forgot_to_hide_the_player_model/) |
| bluesky | lordwolfenstein.bsky.social | ^19 c0 | [This is the starting screen of Zombie Quest. There will be no animated #introseq](https://bsky.app/profile/lordwolfenstein.bsky.social/post/3mmjf7ozj222v) |
| bluesky | ruisilvagamedesign.bsky.social | ^19 c1 | [The different colours the wall can change to and what they represent. Rather tha](https://bsky.app/profile/ruisilvagamedesign.bsky.social/post/3mmiynz2af22g) |
| bluesky | ditheremotion.bsky.social | ^17 c0 | [Never posted anything for #ScreenshotSaturday until now but hey, better late tha](https://bsky.app/profile/ditheremotion.bsky.social/post/3mmk4c4p45k25) |
| reddit | Krons-sama | ^16 c1 | [I tried applying parallax to the particles system](https://www.reddit.com/r/Unity3D/comments/1tlmzf4/i_tried_applying_parallax_to_the_particles_system/) |
| bluesky | projectsentinelgame.com | ^16 c0 | [I've been refining the roar and arrest mechanics. The Sentinel uses a cybernetic](https://bsky.app/profile/projectsentinelgame.com/post/3mmkbx7azzs2f) |
| reddit | Aalzard | ^15 c4 | [Okay guys, look at this main menu for my game 👀 This is the main menu for my coo](https://www.reddit.com/r/Unity3D/comments/1tlsov6/okay_guys_look_at_this_main_menu_for_my_game/) |
| bluesky | thatfriendlydev.bsky.social | ^15 c0 | [I'm a solo dev making Backpack Guardian. Just added a new dangerous event: The S](https://bsky.app/profile/thatfriendlydev.bsky.social/post/3mmjefxx4w22n) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Psychological-Road19</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 1790 · 💬 26</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tld9wx/my_game_gave_someone_comfort_in_an_active_warzone/" target="_blank" rel="noopener"><img src="https://i.redd.it/mmck6oidbv2h1.jpeg" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“My game gave someone comfort in an active warzone and it's stuck with me since. I feel very touched. It was a while back now, someone popped into my Discord and told me about how the game is comfortin”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา Godot แชร์ว่ามีผู้เล่นส่งข้อความมาจากเขตสงครามบอกว่าเกมให้ความสบายใจ และ dev ส่ง ad-free pack ให้ฟรี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เกม indie เล็กๆ ให้ความสบายใจจริงๆ แก่คนในเขตสงคราม — ยืนยันว่า studio เล็กก็สร้าง impact ต่อชีวิตคนได้เกินกว่าตัวเลข download</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมควรเก็บ player impact story ไว้อย่างจริงจัง — ข้อความจริงจากผู้เล่นแชร์ภายในทีมสร้าง morale ได้มากกว่า dashboard ตัวเลขใดๆ และไม่เสียค่าใช้จ่าย</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tld9wx/my_game_gave_someone_comfort_in_an_active_warzone/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Matiesus</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 822 · 💬 36</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tlfd5o/i_added_some_destruction_to_my_super_hero_game/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/OGxoMWNqeG5zdjJoMdmbDslmZCFVSDpyLFWn28rqcfl7HJHTc2vqnwo6e7Ll.png?format=pjpg&amp;auto=webp&amp;s=c094b08ac084b354ad67c58cd8645e9b95da9171" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I added some destruction to my super &quot;hero&quot; game”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา Godot เพิ่ม destructible environment แบบ real-time ให้เกม superhero indie โชว์ physics-driven debris และการพัง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Destruction physics เพิ่ม player satisfaction ได้มากเทียบกับ effort — และโปรเจกต์นี้พิสูจน์ว่า indie dev คนเดียวทำได้โดยไม่ต้องใช้ทรัพยากร AAA</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ทดลอง destruction แบบเดียวกันด้วย Unity Fracture หรือ custom mesh-splitting — เพิ่ม production value ให้เกม action หรือ XR ที่กำลังพัฒนา</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlfd5o/i_added_some_destruction_to_my_super_hero_game/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@binbun3</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 271 · 💬 9</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tldrkm/claw_effect/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/aGI5OGF1MnQ5djJoMY3siOwDBpXLfsUQbvEbrXiWwjIyVBHHPhtQirBXT6Ym.png?format=pjpg&amp;auto=webp&amp;s=17875087dd92f443049bb4d361dd35d0837648b0" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Claw Effect From my Battle FX: [https://binbun3d.itch.io/battle-fx](https://binbun3d.itch.io/battle-fx) I also made swing effects and these claw effects are actually 3 swing effects with additional de”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา Godot แชร์ claw effect ที่ประกอบจาก swing effect 3 ชั้นบวก detail เพิ่ม วางขายเป็น Battle FX asset pack บน itch.io</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การแตก effect ซับซ้อนออกเป็น primitive ซ้ำได้ (swing × 3 + detail) คือ pattern VFX ที่ดี ทำให้ asset pack modular และขายต่อได้ง่าย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ใช้แนวคิดเดียวกันได้เลย — ประกอบ battle/skill VFX จาก sub-effect ย่อยที่ reuse ได้ ลด asset แต่ได้ variety เพิ่ม</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tldrkm/claw_effect/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Juaniesteban</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 257 · 💬 25</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tlicub/im_a_16_year_old_developer_making_my_first_game/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/cmpzbXpkcWxmdzJoMYlriZFskikFGvW9R-mqRZzaBGUpbK_DcINJyt3NkeE2.png?format=pjpg&amp;auto=webp&amp;s=28a16cce8a66991b2dbe834259363c55c36850f1" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm a 16 Year Old developer making my first game! Would love to hear some feedback! I'm developing a 2D fast paced platformer heavily inspired in Pizza Tower, Ultrakill and Speedrunning based games. T”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาอายุ 16 สร้าง 2D platformer ชื่อ Speedtickers ด้วย Godot แรงบันดาลใจจาก Pizza Tower และ Ultrakill core mechanic คือต้องชนะก่อน timer หมด — วางบน Steam wishlist แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โซโล่ทีนชิปเกมขึ้น Steam ได้ด้วย Godot โดยใช้ mechanic เดียว (timer pressure) บวก genre reference ที่ชัด — พิสูจน์ว่า scope ที่แน่นพอทำให้จบได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ใช้หลักเดียวกันได้: ล็อก mechanic เดียว อ้างอิง 2-3 เกมเป็น design north star และ freeze scope ก่อนเข้า production</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlicub/im_a_16_year_old_developer_making_my_first_game/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Fit-Hovercraft-7669</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 231 · 💬 14</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tlbrag/ive_added_multiplayer_splitscreen_to_my/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/MWk0N3Y1bTd2dTJoMa7p0FlN6O1BOj4ABt6rYhDkJyXz7EVpueeu4_lyojv9.png?format=pjpg&amp;auto=webp&amp;s=481449462d800b3883f321be4d16c00f8d998e13" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I've added multiplayer split-screen to my ArcadeRacer Recently my multiplayer received some love - now you can not only race against each other via network, but also on split-screen. (In this video, t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev คนเดียวเพิ่ม split-screen multiplayer แบบ local ให้ arcade racer ใน Godot ที่มี network multiplayer อยู่แล้ว โดยใช้ AI เป็น P2 ในการ demo</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทำ network และ split-screen multiplayer ใน Godot คนเดียวได้ทั้งคู่ — เป็น benchmark ที่ดีสำหรับการ plan scope โปรเจกต์ game ขนาดเล็ก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู pattern split-screen ของ Godot นี้ได้ตอน scope local co-op — SubViewport ของ Godot เทียบได้กับ Camera Rect ของ Unity ช่วย estimate effort ได้แม่นขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlbrag/ive_added_multiplayer_splitscreen_to_my/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@im_arseny</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 224 · 💬 13</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tlmda5/working_on_a_fishing_mechanic_in_my_game_about_a/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/bDhieGF1amY3eDJoMRIhTtrPaTzJQdAEkB6mIxD6SBrKpfWFk8yB5u1XNXWA.png?format=pjpg&amp;auto=webp&amp;s=f13a18d0ec204875d5991f167e6f0daefb40bd59" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“working on a fishing mechanic in my game about a gopher catching stars from the sky”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev กำลังทำ fishing mechanic ใน Godot สำหรับเกมแนว whimsical — gopher โยนสายตกดาวจากท้องฟ้า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เอา mechanic คุ้นเคย (ตกปลา) มาใส่ context แฟนตาซี — design pattern ที่ scope เล็กแต่ charm สูง ดึง engagement ได้ดีแม้แค่โพสต์เดียว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team เอาแนวนี้ไปใช้ได้เลย — เอา blueprint fishing หรือ grapple system แล้ว reskin จุดประสงค์ให้เข้า world ของเกม ประหยัด design time แต่ยัง depth ครบ</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlmda5/working_on_a_fishing_mechanic_in_my_game_about_a/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Jeheno</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 130 · 💬 4</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tlphly/halflife_2s_gravity_gun_recreation/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/c2x1b2k5czR0eDJoMexf6Ifygwfa-FFy1AtzJb_WCmwM8crvquWNI3-_V3-C.png?format=pjpg&amp;auto=webp&amp;s=62898f9f70649ce07385d4d33b6762be96957996" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Half-Life 2's Gravity Gun recreation”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา recreate Gravity Gun จาก Half-Life 2 ใน Godot — ระบบ grab, hold, attract, throw physics objects ครบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป็น reference ที่ดีสำหรับระบบ physics interaction แบบ grab/hold/throw ที่สร้างจาก scratch — benchmark ที่ดีสำหรับทีมที่จะทำ mechanic แบบนี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู logic grab/attract/throw แล้วทำใหม่ด้วย Rigidbody + ConfigurableJoint หรือ PhysicsJoint ใน Unity ได้เลย — mechanic เดิม แค่เปลี่ยน engine</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlphly/halflife_2s_gravity_gun_recreation/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@derethdweller</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 127 · 💬 24</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tl849y/i_was_fully_expecting_godot_to_crash_when_i_asked/" target="_blank" rel="noopener"><img src="https://preview.redd.it/51r1y37ztt2h1.png?width=1031&amp;format=png&amp;auto=webp&amp;s=0e7aa35964e280ef0e586de1e1dce979599c4eb6" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i was fully expecting godot to crash when i asked him to render that Camera far somewhere at 100km, 2-5k objects per cell, about 30k cells of land, dirty loaded with 0 optimization except multimeshing”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev ทดสอบ Godot แบบหนักสุด: render distance 100km, ~30k cells, 2–5k objects ต่อ cell บนคอมเก่า ไม่ optimize เลย — โหลด 2–3 นาที FPS ~0.1 แต่ไม่ crash</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Godot รับโหลดหนักโหดได้โดยแทบไม่ optimize เลย มีแค่ MultiMesh — ความเสถียรของ engine สูงกว่าที่คาด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง benchmark scene open-world แบบไม่ optimize เทียบกับ Godot ได้เลย — ถ้า Godot เสถียรกว่า ให้พิจารณาใช้ใน project terrain หรือ XR ที่ต้องการ scale ใหญ่</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tl849y/i_was_fully_expecting_godot_to_crash_when_i_asked/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
</div>
