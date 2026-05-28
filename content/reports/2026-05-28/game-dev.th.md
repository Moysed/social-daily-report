---
type: social-topic-report
date: '2026-05-28'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-28T04:41:28+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- rss
- x
regions:
- global
post_count: 89
salience: 0.55
sentiment: mixed
confidence: 0.7
tags:
- unity
- unreal
- godot
- ai-tooling
- graphics-perf
- workflow
thumbnail: https://external-preview.redd.it/b2F0dWQxaTJvbTNoMf0sy5AZIxFTRnr0ArfKZtgUMNNoiJ5kxfIFP92_xAj1.png?format=pjpg&auto=webp&s=e8b7921ede78ee68a7991bb3321585916b77e4a0
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-28

## TL;DR
- Unreal Fest Chicago 17 มิ.ย. — keynote State of Unreal กำลังจะมา จับตาข่าว dev-tool/services ของ Epic [10]
- Unity AI Beta ดัน prompt-driven multi-step edits — prompt เดียวสั่งเปลี่ยนได้ซับซ้อน เปิด free trial แล้ว [35]
- ชุมชนต้านการใช้ AI โดยไม่เปิดเผยในโพสต์ gamedev กำลังได้แรงหนุน — มีข้อเสนอกฎบังคับ disclosure [3]
- แชร์เทคนิคเพิ่ม perf จริงจัง: ปลา 1000 ตัว draw call เดียวด้วย bone matrix textures [13], fake interior shader หนึ่ง draw call (Unity 6 URP) [41], GPU meadows [58]
- LOD/foliage, light+fog cookies, VFX Graph + Shader Graph ยังคงครอง craft topics หลักฝั่ง Unity/Godot [2][5][23][40][45]

## What happened
บทสนทนาที่ Carmack นำด้านวิศวกรรมระบบและการออกแบบ ReLU-at-zero gradient ครองการ engage บน X [1][7][34] แต่ signal ที่ใช้งานได้จริงฝั่ง game dev อยู่ที่ tooling Epic ประกาศ Unreal Fest Chicago / State of Unreal วันที่ 17 มิ.ย. [10] Unity ผลักดันสองทิศทาง: Unity AI Beta พร้อม prompt-driven asset/scene edits [35] และ Unity Studio web-based editor สำหรับ industrial 3D (demo แข่งรถ, พาร์ตเนอร์ HARMAN HMI) [19][59] ฝั่งชุมชน เทคนิค performance แพร่กระจายกว้าง — GPU-instanced fish ด้วย bone matrix textures [13], InteriorMaster single-draw fake interiors สำหรับ Unity 6 URP [41], GPU meadows [58], dynamic terrain + flow-field recalc ใน Godot [55], PCG fork แบบ node-based เต็มรูปแบบสำหรับ Godot [15]

โพสต์ craft กระจุกตัวที่ light/fog cookies [5][45], stylized shaders (painterly URP [27], ลาวา [40], black hole VFX [23]) และปัญหา LOD (tree LOD พังเมื่อมองจากด้านบน) [2] meta-discussion: ข้อเสนอใน Reddit ให้บังคับ disclosure การใช้ AI ในโพสต์ gamedev ได้ score 567 / 93 ความคิดเห็น [3]; ถกเถียงเรื่องความอยู่รอดของ solo dev ร้อนแรง [43]; retro หลัง demo launch แสดงให้เห็น 1k downloads แล้ว Steam algorithm พัง [20]

## Why it matters (reasoning)
Vector ที่บรรจบกันสองอย่างสำคัญสำหรับ shop ที่ใช้ Unity+XR อย่างแรก Unity กำลังเดิมพันกับ AI-in-editor [35] และ web-based authoring [19] มากขึ้น — ส่งผลโดยตรงต่อ workflow ของ mid-tier studio (ตั้งค่า asset, เชื่อม scene) และส่งสัญญาณว่า Unity ต้องการให้ toolchain อยู่ที่ไหนใน 12 เดือนข้างหน้า อย่างที่สอง ชุมชนกำลังกระชับบรรทัดฐานต่อต้านการใช้ AI โดยไม่เปิดเผยพร้อมกัน [3] — หมายความว่า output ที่ AI ช่วยสร้างต้องถูก framing ด้วยงานฝีมือของมนุษย์เมื่อแชร์สาธารณะ ไม่งั้นจะถูกด้อยค่า

second-order: demo perf [13][41][58] สะท้อน pattern ที่กำลัง mature — เทคนิค single-draw-call ผ่าน GPU data textures ถือเป็น baseline มาตรฐานสำหรับ stylized scene แล้ว ไม่ใช่ของ exotic อีกต่อไป สำหรับ target XR/mobile-tier ถือเป็นความรู้บังคับ thread ของ Carmack [1][7] คือ noise สำหรับ production game dev — ข้ามไปเลย เว้นแต่ทำ low-level ML หรืองาน hardware

## Possibility
น่าจะเกิด (70%): Unity AI Beta กลายเป็น default สำหรับ asset import/material setup ภายใน 2 quarters; workflow FBX preset [26] ถูก auto-suggest น่าจะเกิด (60%): Unreal Fest 17 มิ.ย. [10] ปล่อย MegaLights/Nanite-foliage update และ AI tooling parity ที่รุกมากขึ้น เป็นไปได้ (40%): บรรทัดฐาน disclosure [3] กระจายจาก Reddit ไปยัง itch.io/Steam community hubs ทำให้เกิดตลาด tag 'human-made' ไม่น่าเกิด (20%): Unity Studio [19] ข้ามมาสู่ game dev อย่างมีนัยสำคัญ — ดูเหมือนจะเน้น industrial-first

## Org applicability — NDF DEV
ที่ใช้ได้โดยตรงสำหรับ NDF DEV:
- InteriorMaster-style single-draw fake interiors [41] → นำมาใช้ซ้ำกับ scene urban/edutech ใน Unity ที่มีอาคารมีหน้าต่าง ประหยัดมากบน Quest-tier XR
- Bone-matrix texture instancing [13] และเทคนิค GPU meadow [58] → ใช้ได้กับ ambient life ใน VR และ scene bio/nature ใน e-learning
- Light cookie + fog mood design [5][45] → อัปเกรด atmosphere ต้นทุนต่ำสำหรับ narrative scene ใน Unity edutech ทุกโปรเจกต์
- Unity AI Beta [35] → ควร eval 1 วันสำหรับ asset import/material wiring ในโปรเจกต์ถัดไป อย่าผูก pipeline ยังก่อน (beta, ความเสี่ยง lock-in)
- FBX Presets [26] → adopt ได้เลย ไม่มีต้นทุน ได้ workflow win ชัวร์
- AI disclosure norms [3] → กำหนด internal policy ตอนนี้สำหรับโพสต์ marketing/devlog เพื่อป้องกัน backlash
ข้าม: thread ML ของ Carmack [1][7][34], รายการ Unreal-specific เว้นแต่ Unreal Fest [10] จะปล่อยอะไรที่ cross-engine

## Signals to Watch
- Unreal Fest Chicago 17 มิ.ย. — จับตา keynote สำหรับ AI tooling + Fab/MetaHuman updates [10]
- เพดานความสามารถของ Unity AI Beta — 'complex changes' หมายถึงอะไรในทางปฏิบัติจริง [35]
- กฎ AI-disclosure จะแพร่จาก r/gamedev ไปยัง Steam/itch community pages ไหม [3]
- Pattern GPU-data-texture single-draw-call กำลังกลายเป็นมาตรฐานสำหรับ stylized + XR perf [13][41][58]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ID_AA_Carmack | ^2987 c79 | [I have been very impressed by @SemiAnalysis_ . I think of myself as a wide rangi](https://x.com/ID_AA_Carmack/status/2059382254191652896) |
| reddit | Planet1Rush | ^839 c78 | [My tree LODs look fine… until you look at them from above I really hope players ](https://www.reddit.com/r/godot/comments/1toxqo5/my_tree_lods_look_fine_until_you_look_at_them/) |
| reddit | Neat-Captain-1661 | ^567 c93 | [Subreddit rule recommendation: require disclosure of AI use in creating a post I](https://www.reddit.com/r/gamedev/comments/1tp6rxg/subreddit_rule_recommendation_require_disclosure/) |
| reddit | 9joao6 | ^552 c19 | [My game's tutorial robot can be a little scary, but a charmer once it opens up I](https://www.reddit.com/r/godot/comments/1tplg07/my_games_tutorial_robot_can_be_a_little_scary_but/) |
| reddit | No_Telephone5992 | ^405 c35 | [Designed light + fog I just love how mood is set with light and fog. It starts w](https://www.reddit.com/r/Unity3D/comments/1toyu36/designed_light_fog/) |
| reddit | Psonrbe | ^362 c26 | [Got the physics working for my extendo-arms 👍](https://www.reddit.com/r/godot/comments/1tpc3x9/got_the_physics_working_for_my_extendoarms/) |
| x | ID_AA_Carmack | ^350 c32 | [It is easy enough to make your own, but I think standard relu should have been d](https://x.com/ID_AA_Carmack/status/2059347005621645404) |
| x | UnrealEngine | ^286 c321 | [If you had access to a time machine that let you go back in time and be part of ](https://x.com/UnrealEngine/status/2059333773540606238) |
| reddit | Asbar_IndieGame | ^256 c38 | [How does this boss fight look so far? Hey everyone, I'm working on this boss fig](https://www.reddit.com/r/Unity3D/comments/1tp8g9x/how_does_this_boss_fight_look_so_far/) |
| x | UnrealEngine | ^246 c18 | [State of Unreal returns in 3 weeks at Unreal Fest Chicago! Join us on June 17 at](https://x.com/UnrealEngine/status/2059650514338693619) |
| reddit | Huckflesh | ^218 c14 | [My boat game improvements: Ocean transitions, Item use and yes, i used the stenc](https://www.reddit.com/r/godot/comments/1tpfdb9/my_boat_game_improvements_ocean_transitions_item/) |
| x | drelanns3d | ^203 c7 | [Yo #Indiedevs! Just dropped my delicious asset pack for #UE5 and #Unity. You can](https://x.com/drelanns3d/status/2059577905362137300) |
| x | artem_sini39436 | ^187 c11 | [1000 fish with one draw call , bone matrix texture is a black magic #gamedev #in](https://x.com/artem_sini39436/status/2059179048350175306) |
| reddit | GameWizardGriffin | ^173 c4 | [Learned how to make particle effects. Couldn't resist doing this with them](https://www.reddit.com/r/godot/comments/1tp8b3i/learned_how_to_make_particle_effects_couldnt/) |
| reddit | framedworld | ^168 c20 | [Full PCG in Godot Hey everyone! I've been working on a fork of the original Godo](https://www.reddit.com/r/godot/comments/1tp7jfi/full_pcg_in_godot/) |
| reddit | BunyipHutch | ^150 c13 | [No one told me this was one of the best parts of game development My first game ](https://www.reddit.com/r/gamedev/comments/1tpazds/no_one_told_me_this_was_one_of_the_best_parts_of/) |
| x | shoujo_city | ^140 c2 | [Added petal interactions while riding a bicycle. #AnimeGame #Unity3D #gamedev ht](https://x.com/shoujo_city/status/2059300084538278122) |
| x | unitygames | ^137 c0 | [Quick Tip: You can use custom shaders directly in UI Toolkit 💡 🔗 Watch the full ](https://x.com/unitygames/status/2059333885087924478) |
| x | unity | ^122 c9 | [Start your 3D engines 🏎️ Learn how to build a 3D racing experience in less than ](https://x.com/unity/status/2059303746941681795) |
| reddit | Redhowl_game | ^117 c121 | [Launched my first demo. Got 1k downloads on day one, then Steam hit me with a br](https://www.reddit.com/r/gamedev/comments/1tozrjc/launched_my_first_demo_got_1k_downloads_on_day/) |
| x | itchio | ^93 c2 | [COBB CAN MOVE: A horror game where the rules change. https://t.co/LgiSiZi949 by ](https://x.com/itchio/status/2059424349795307782) |
| reddit | kevdev3d | ^88 c5 | [Made this 3D weapon editor for game developers (no AI) Any feedback is welcome! ](https://www.reddit.com/r/godot/comments/1tpes6f/made_this_3d_weapon_editor_for_game_developers_no/) |
| reddit | Gabz101 | ^87 c4 | [Made a video on how to create a Black Hole effect using VFX Graph and Shader Gra](https://www.reddit.com/r/Unity3D/comments/1tp9ib2/made_a_video_on_how_to_create_a_black_hole_effect/) |
| reddit | Moppemopsi | ^84 c43 | [How is everyone elses test counts? Getting ready for the demo build and I still ](https://www.reddit.com/r/Unity3D/comments/1tpcy35/how_is_everyone_elses_test_counts/) |
| reddit | Gogiseq | ^83 c8 | [6 + months of working on visuals, sick how far I got with 0 experiences in Blend](https://www.reddit.com/r/Unity3D/comments/1tpf7ed/6_months_of_working_on_visuals_sick_how_far_i_got/) |
| x | SunnyVStudio | ^82 c0 | [Stop extracting FBX materials one by one in Unity 🛑 Use Presets to set up your 3](https://x.com/SunnyVStudio/status/2059253215078887670) |
| x | jettelly | ^77 c0 | [Developer tantaneity shared how they recreated a painterly shader from Blender i](https://x.com/jettelly/status/2059243161311187193) |
| x | TMcDonaldGames | ^75 c3 | [Prototyping a simple roguelike dungeon game. Right now I'm working on the basics](https://x.com/TMcDonaldGames/status/2059441310914764938) |
| reddit | AmneticgamerYT | ^74 c2 | [Stylized gun game asset Stylized gun game asset - low poly 2k polys](https://www.reddit.com/r/Unity3D/comments/1tow6nd/stylized_gun_game_asset/) |
| x | MortalCrux | ^74 c3 | [Randomized campsites can be found throughout the land. 🏕️ Rest to pass time and ](https://x.com/MortalCrux/status/2059358428611686786) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2987 · 💬 79</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2059382254191652896">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I have been very impressed by @SemiAnalysis_ . I think of myself as a wide ranging systems engineer, looking for value at every level from the chip specs to the user interface, but SA exposes me to ad”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Carmack ยกย่อง SemiAnalysis ที่สอนเรื่อง datacenter และ semiconductor ลึกขึ้น โดยเน้น 800VDC power design ที่ยืม part จาก EV และ SiC MOSFET ใหม่ทนไฟ 10kV ต่อสายส่งไฟฟ้า AC ได้ตรงเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Part จาก EV เข้า datacenter power design หมายความว่า infrastructure GPU compute สุกเร็วและถูกลง ส่งผลต่อราคา cloud และ hardware ที่ indie studio เข้าถึงได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่ตรง แต่ติดตาม trend ต้นทุน infrastructure ช่วยตัดสินใจเรื่อง cloud rendering, ค่า CI/CD, และการเลือก XR streaming service ได้ดีขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ID_AA_Carmack/status/2059382254191652896" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Planet1Rush</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 839 · 💬 78</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1toxqo5/my_tree_lods_look_fine_until_you_look_at_them/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/b2F0dWQxaTJvbTNoMf0sy5AZIxFTRnr0ArfKZtgUMNNoiJ5kxfIFP92_xAj1.png?format=pjpg&amp;auto=webp&amp;s=e8b7921ede78ee68a7991bb3321585916b77e4a0" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“My tree LODs look fine… until you look at them from above I really hope players never look at my foliage low LODs from above because they look absolutely terrible 😭 The transitions themselves I actual”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev ใน Godot ขอไอเดีย low-LOD ต้นไม้แบบ stylized หลังพบว่า billboard 2 quad ตัดกันดูเหมือนเมฆระเบิดนิวเคลียร์เวลามองจากด้านบนในเกม open world ที่บินได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Open world ที่บินได้ทำลาย assumption ของ billboard LOD ปกติ — เกมที่มี aerial traversal ต้องการ LOD ที่ดูดีได้ทุกมุม ไม่ใช่แค่ระดับสายตา</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ที่ทำฉาก open-world หรือ XR ที่มีต้นไม้ควร audit LOD asset จากมุมบนและ isometric ตั้งแต่เนิ่นๆ โดยเฉพาะถ้า camera สามารถลอยขึ้นได้</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1toxqo5/my_tree_lods_look_fine_until_you_look_at_them/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@9joao6</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 552 · 💬 19</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tplg07/my_games_tutorial_robot_can_be_a_little_scary_but/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/M3hvZmNwc2RlcjNoMTpb3pIhC-Ipz1GfMxdz_FRFZEY8ibWpC8UFC3huGyWt.png?format=pjpg&amp;auto=webp&amp;s=49efc6f6b0e3e61000414ea9c0da80fe0067c271" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“My game's tutorial robot can be a little scary, but a charmer once it opens up I'm making [Sunrise Isles](https://store.steampowered.com/app/4509920/Sunrise_Isles/), a chill multiplayer hangout game, ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev สร้าง 'Sunrise Isles' ด้วย Godot โชว์ robot NPC ที่ดูน่ากลัวแต่มี personality น่ารัก ทำหน้าที่เป็น tutorial guide ในเกม multiplayer แนว hangout.</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>NPC ที่มี split personality ช่วยลด friction ตอน onboarding และเพิ่ม character depth พร้อมกัน — UX กับ narrative design แก้ปัญหาเดียวกันได้ในตัวเดียว.</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team นำไปใช้กับ XR/e-learning ได้เลย: ออกแบบ tutorial agent สองเฟส — เริ่มเป็น neutral/authoritative แล้วค่อย warm up — ลด anxiety ผู้เรียนโดยไม่เสีย clarity.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tplg07/my_games_tutorial_robot_can_be_a_little_scary_but/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@No_Telephone5992</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 405 · 💬 35</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/Unity3D/comments/1toyu36/designed_light_fog/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/aTBkaGxjNjB6bTNoMaZSfZltPEoADFcFlJbsi3Q2p38W13IJT_iA2QVUz09g.png?format=pjpg&amp;auto=webp&amp;s=0972a2f90ed1c910f3b30b6b4e95bb02b9d69a9b" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Designed light + fog I just love how mood is set with light and fog. It starts with regular unity directional light and the other setups uses designed light with a dynamic light cookie + fog which use”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unity dev โชว์การใช้ directional light เดียวคู่กับ dynamic light cookie และ fog เพื่อเปลี่ยน mood ของฉาก แต่ละ setup ใช้เวลาแค่ประมาณ 1 นาที บน asset ToonScapes Spring Islands.</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ได้ visual mood ที่หนักแน่นด้วย light source เดียว ช่วยให้ draw calls ต่ำและ setup เร็ว — ตรงจุดสำหรับทีมเล็กที่ต้องส่งงานไว.</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team นำ pattern นี้ (directional light เดียว + dynamic cookie) มาเป็น lighting toolkit มาตรฐานสำหรับทุก game หรือ XR scene ลด lighting time เหลือไม่ถึง 1 นาทีต่อ environment.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1toyu36/designed_light_fog/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Psonrbe</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 362 · 💬 26</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/godot/comments/1tpc3x9/got_the_physics_working_for_my_extendoarms/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/OWx3bHlqZ3lxcDNoMYouNswrdo0_zKLOk0SklRSdCdsOEvV9gIlHWULwqhyN.png?format=pjpg&amp;auto=webp&amp;s=405303d4d5bdeaf5752287e15dbd3cf8f377f2c7" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Got the physics working for my extendo-arms 👍”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา Godot ทำให้ physics ของแขนที่ยืดหดได้ทำงานสำเร็จในเกมของตัวเอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Physics แขนยืดหดด้วย joint/constraint ใน Godot เป็น mechanic นำกลับมาใช้ได้กับเกม action หรือ puzzle — โพสต์นี้พิสูจน์ว่าทำได้จริงพร้อมผลลัพธ์ชัดเจน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team เทียบแนวทาง joint/constraint ของ Godot แล้ว map ไปใช้กับ HingeJoint หรือ ConfigurableJoint ใน Unity สำหรับ character mechanic แบบเดียวกันในโปรเจกต์ต่อไป</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tpc3x9/got_the_physics_working_for_my_extendoarms/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 350 · 💬 32</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2059347005621645404">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It is easy enough to make your own, but I think standard relu should have been defined as passing the value at zero, so gradients flow backward through it, allowing some things to be zero weight initi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Carmack เสนอว่า ReLU ควร pass gradient ที่จุดศูนย์ เพื่อให้ zero-initialize weight ได้เมื่อไม่ต้องการ symmetry breaking</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สัญญาณจาก game dev legend ที่ทำ AI research — การออกแบบ activation function ส่งผลโดยตรงต่อ initialization scheme ที่ใช้ได้ใน custom model layer</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า Unity team สร้าง ML Agents หรือ on-device inference pipeline อยู่ ใช้เป็น reference ตอนเลือก activation function และ zero-init strategy สำหรับ custom layer</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ID_AA_Carmack/status/2059347005621645404" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 286 · 💬 321</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2059333773540606238">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If you had access to a time machine that let you go back in time and be part of the development team for any videogame, which one would it be? 🕒”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine ถามชาวเน็ตว่าถ้ามี time machine อยากย้อนไปร่วมทีม dev เกมไหนในอดีต</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>engagement สูงทั้งที่ไม่มีเนื้อหาเทคนิคเลย — บอกว่า content แนว community ดึง interaction ได้ดีกว่า post เทคนิค</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่ applicable โดยตรง แต่ studio ลองใช้ question-style post แบบนี้บน social ช่องตัวเองได้ เพื่อ engage คนช่วงที่ไม่มี project ใหม่ประกาศ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2059333773540606238" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Asbar_IndieGame</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 256 · 💬 38</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/Unity3D/comments/1tp8g9x/how_does_this_boss_fight_look_so_far/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/dWN2NDNvZXczcDNoMQA5tvCQ_ycsrgH3s68-m_hB2wQEle8E6dlD5NcDOted.png?format=pjpg&amp;auto=webp&amp;s=f9150b5e71acf2c3254060e2021eabd77ccc0861" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“How does this boss fight look so far? Hey everyone, I’m working on this boss fight for our action roguelite and would love some feedback.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev โชว์ boss fight ที่กำลังพัฒนาใน action roguelite บน Unity แล้วขอ feedback จาก Reddit</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ปล่อย WIP ลง r/Unity3D แล้วได้ 38 comments คือ usability test ราคาถูกก่อน ship จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ปล่อย WIP clip ของ boss หรือ combat ลง r/Unity3D ก่อน internal review รอบถัดไป — ได้ feedback เรื่อง feel และ readability เร็วขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1tp8g9x/how_does_this_boss_fight_look_so_far/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
</div>
