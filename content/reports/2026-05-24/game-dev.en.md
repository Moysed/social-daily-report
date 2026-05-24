---
type: social-topic-report
date: '2026-05-24'
topic: game-dev
lang: en
pair: game-dev.th.md
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
---

# Game Dev — 2026-05-24

## TL;DR
- Godot dominates today's indie showcase volume — fishing mechanics [1], Gravity Gun clones [2], survival horror [3], Parkour FPS [6] — signaling continued community momentum vs Unity/Unreal posts
- Unity tech showcases skew advanced rendering: HDRP real-time scene voxelization for GI [8], procedural zero-texture shader NPCs at 500/100FPS [22], stylized billboard foliage [5]
- Unreal content is sparse and beginner-heavy (UE5.7 low-end optimization [26], Blueprint array gating [33]) — fewer pro-pipeline signals today
- Production/marketing signals: Steam Playtest button reached at 230 wishlists [19], 5000 wishlist milestone [24], scam-targeting of small indies rising [16]
- No AI-in-pipeline items surfaced today — generative tools absent from the top 40, suggesting community attention is on craft and rendering tech

## What happened
Reddit r/godot dominated engagement with polished WIP gameplay posts [1][2][3][6][11][17][30] plus tooling/plugin sharing [13][15][27]. Unity3D content leaned technical-rendering: HDRP GPU voxelization for real-time GI in procedural worlds [8], a shader-based NPC system rendering 500 agents at 100fps with zero textures [22], and stylized billboard-card foliage workflows [5][13]. Unreal had only three items, all support-tier: UE5.7 low-end GPU optimization [26], Blueprint dialogue gating [33], and a 64-episode turn-based combat tutorial series [35]. Bluesky #ScreenshotSaturday filled the long tail with solo-dev WIPs [20][24][29][31][32][36][37][39][40]. Production signals: a solo dev reflecting on changing a game from one player's feedback [10], scam-targeting of low-popularity indies [16], and Steam wishlist/playtest milestones [19][24].

## Why it matters (reasoning)
Godot's share of high-engagement posts continues to grow relative to Unity/Unreal in indie community spaces — relevant because NDF DEV's Unity-first stack is no longer the default indie choice, though Unity still owns the heavy-rendering conversation [8][22]. The HDRP voxel-GI port [8] matters technically: real-time GI for procedural/dynamic scenes has been a long-standing Unity weakness vs Unreal Lumen, and community-driven solutions narrow that gap for studios that can't justify Unreal migration. The shader-NPC system [22] is a concrete pattern for crowd-heavy XR/edutech scenes where draw-call budget matters. The scam-targeting report [16] is a second-order effect of Steam's low-friction publishing — small studios with public devlogs are now an attack surface.

## Possibility
Near-term (3-6 mo, ~70%): Godot continues to absorb solo/small-team mindshare while Unity holds mid-tier production and Unreal holds AAA/arch-viz — three-way segmentation stabilizes. Medium-term (~50%): HDRP community-rendering features [8] get absorbed into URP or official Unity packages as Unity responds to Lumen pressure. Lower likelihood (~25%): a notable indie hit shipped on Godot in 2026 triggers a tooling/asset-store acceleration that closes the production-pipeline gap with Unity.

## Org applicability — NDF DEV
Direct use: study [8] voxel-GI approach if any NDF XR/VR project needs dynamic GI in procedural environments — but HDRP is desktop/PC only, not Quest-viable, so limited for the VR pipeline. [22] shader-NPC pattern is directly applicable to edutech crowd scenes and mobile Unity builds where texture memory matters — worth a 1-day spike. [5][13] billboard-foliage workflow is a cheap win for any outdoor Unity scene targeting low-end Android/Quest. [16] scam awareness — brief the team if any NDF title goes on Steam. Not worth pursuing: Godot migration (no business case from today's signal), Unreal low-end optimization [26] (out of stack).

## Signals to Watch
- Watch whether Unity ships an official answer to community HDRP voxel-GI [8] in next roadmap update
- Track Godot 4.x adoption curve on Steam — if a breakout hit lands, asset/tooling ecosystem may accelerate
- Monitor Quest/mobile-targeted rendering tricks (shader NPCs [22], billboard foliage [5][13]) for NDF VR backlog
- Watch indie scam patterns [16] — may need a studio-side policy for unsolicited contact

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
| reddit | Soliloqu-You | ^68 c34 | [Have you ever changed your game because of one player’s message? Hi everyone. I’](https://www.reddit.com/r/gamedev/comments/1tm8f61/have_you_ever_changed_your_game_because_of_one/) |
| reddit | Squirrelation_Games | ^63 c2 | [Oops. Someone forgot to hide the player model](https://www.reddit.com/r/godot/comments/1tlouby/oops_someone_forgot_to_hide_the_player_model/) |
| reddit | zacharieg14 | ^62 c2 | [Made a simple animation to my game's menu in 5 minutes, now it looks awesome! Hi](https://www.reddit.com/r/godot/comments/1tmchd1/made_a_simple_animation_to_my_games_menu_in_5/) |
| reddit | Planet1Rush | ^41 c0 | [Updated my foliage system: MultiMesh now supports LODs and collision in debug mo](https://www.reddit.com/r/godot/comments/1tlrdkj/updated_my_foliage_system_multimesh_now_supports/) |
| reddit | Aalzard | ^31 c6 | [Okay guys, look at this main menu for my game 👀 This is the main menu for my coo](https://www.reddit.com/r/Unity3D/comments/1tlsov6/okay_guys_look_at_this_main_menu_for_my_game/) |
| reddit | PensiveDemon | ^31 c5 | [[Convert Text Case] Built a plugin for myself - Should I share it to the Asset S](https://www.reddit.com/r/godot/comments/1tm9dew/convert_text_case_built_a_plugin_for_myself/) |
| reddit | ploxiar | ^30 c13 | [watch out for scammers Hello, there is a target on unreleased / released indie g](https://www.reddit.com/r/gamedev/comments/1tljjgd/watch_out_for_scammers/) |
| reddit | Shabaubi | ^30 c2 | [I made an environment based off the backrooms trailer shot Very excited for the ](https://www.reddit.com/r/godot/comments/1tlps6y/i_made_an_environment_based_off_the_backrooms/) |
| reddit | Krons-sama | ^29 c2 | [I tried applying parallax to the particles system](https://www.reddit.com/r/Unity3D/comments/1tlmzf4/i_tried_applying_parallax_to_the_particles_system/) |
| reddit | JetPoweredGames | ^29 c2 | [My Steam Playtest is Live! Big Saturday Update to Iron Dogs. Many tweaks, added ](https://www.reddit.com/r/godot/comments/1tlvjkm/my_steam_playtest_is_live/) |
| bluesky | projectsentinelgame.com | ^29 c0 | [I’ve been refining the roar and arrest mechanics. The Sentinel uses a cybernetic](https://bsky.app/profile/projectsentinelgame.com/post/3mmkbx7azzs2f) |
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


## Top Posts

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
      <dt>What it says</dt>
      <dd>An indie dev is building a fishing mechanic in a Godot game where a gopher catches stars from the sky instead of fish.</dd>
      <dt>Why interesting</dt>
      <dd>Recontextualizing a familiar mechanic (fishing) into a surreal setting is a proven hook for virality — 335 likes on a WIP post signals strong concept appeal.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can borrow this pattern: take one stock mechanic and swap its semantic layer entirely — same code architecture, wildly different feel — fast to prototype, high concept value.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlmda5/working_on_a_fishing_mechanic_in_my_game_about_a/" target="_blank" rel="noopener">View on reddit →</a>
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
      <dt>What it says</dt>
      <dd>A developer recreated Half-Life 2's iconic Gravity Gun mechanic in the Godot engine, shared on r/godot.</dd>
      <dt>Why interesting</dt>
      <dd>Physics-based object manipulation is a reusable mechanic — seeing it cleanly implemented in Godot gives a reference blueprint for any physics-heavy game.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can study the physics interaction logic as a reference when building grab/throw mechanics in XR projects, where hand-object physics feel is critical.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlphly/halflife_2s_gravity_gun_recreation/" target="_blank" rel="noopener">View on reddit →</a>
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
      <dt>What it says</dt>
      <dd>A solo dev shares very early progress on a Godot survival horror game, noting missing level design, sound design, and a placeholder kick mechanic that decapitates enemies to test script-based locational damage.</dd>
      <dt>Why interesting</dt>
      <dd>The choice to prototype locational damage via scripts before committing to raycasts shows a pragmatic iteration mindset useful for any small team validating combat feel fast.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can apply the same script-first damage prototype approach — wire up placeholder hit zones in code before building full physics/raycast systems, then swap when the feel is confirmed.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tm2e4h/working_on_a_survival_horror_its_still_very_early/" target="_blank" rel="noopener">View on reddit →</a>
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
      <dt>What it says</dt>
      <dd>A Unity developer (@EscapeDoodland) posted a teaser on r/Unity3D titled 'Working on something new,' likely a WIP screenshot or GIF of an early-stage game project.</dd>
      <dt>Why interesting</dt>
      <dd>The post hit 170 likes with only 6 comments — visual WIP reveals on r/Unity3D drive strong organic reach without needing polished content.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can post early-stage WIP visuals on r/Unity3D to build an audience before launch — raw progress screenshots perform as well as polished trailers.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1tlkigm/working_on_something_new/" target="_blank" rel="noopener">View on reddit →</a>
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
      <dt>What it says</dt>
      <dd>A dev built 12 stylized tree/bush species in Unity using flat alpha-cutout foliage cards with a 3-color palette and rotating billboard technique, then wrapped it into a custom Unity tool.</dd>
      <dt>Why interesting</dt>
      <dd>Proves you can achieve dense, appealing stylized foliage at low poly cost by layering dead-simple flat cards — no complex geometry needed.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can build a reusable foliage card tool using this billboard+alpha-cutout pipeline to speed up environment art on any stylized game project.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1tllqgs/stylized_foliage/" target="_blank" rel="noopener">View on reddit →</a>
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
      <dt>What it says</dt>
      <dd>A solo dev showcased 'RUNFALL', their first Godot game — a first-person parkour game with Titanfall 2-style world-shifting movement mechanics.</dd>
      <dt>Why interesting</dt>
      <dd>Titanfall 2's movement system is widely praised for feel; a solo dev replicating it in Godot proves the mechanic is achievable without a AAA team or Unity.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can study Titanfall 2-style world-shift as a design pattern for XR/VR locomotion — spatial reorientation mechanics translate well to headset environments.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlng2f/showcasing_my_first_game_runfall/" target="_blank" rel="noopener">View on reddit →</a>
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
      <dt>What it says</dt>
      <dd>A Godot developer found that pixel font outlines render rounded by default, and solved it by converting the font to a bitmap font via Snowb.io with stroke settings before import.</dd>
      <dt>Why interesting</dt>
      <dd>The Godot Label outline system has no built-in squared-edge option, so baking stroke into a bitmap font at export time is the only reliable workaround for pixel-art UI fidelity.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team building 2D or pixel-art UI should evaluate bitmap font pre-baking via Snowb.io instead of relying on runtime outline shaders, which often produce rounded artifacts on low-res fonts.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/godot/comments/1tlu3rx/is_there_a_way_to_get_squared_edges_instead_of/" target="_blank" rel="noopener">View on reddit →</a>
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
      <dt>What it says</dt>
      <dd>A developer successfully ported real-time scene voxelization natively into Unity HDRP, GPU-accelerated, enabling dynamic Global Illumination for procedurally changing worlds.</dd>
      <dt>Why interesting</dt>
      <dd>Native GPU voxelization in HDRP unlocks high-quality dynamic GI without baked lightmaps, critical for any game with runtime-generated or destructible environments.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can study this technique for any HDRP project with dynamic scenes — replacing baked GI cuts iteration time and supports real-time level changes without re-lighting.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/Unity3D/comments/1tln2yw/finally_managed_to_port_real_time_scene/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
</div>
