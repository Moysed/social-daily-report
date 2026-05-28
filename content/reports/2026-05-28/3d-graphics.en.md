---
type: social-topic-report
date: '2026-05-28'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-05-28T03:32:04+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- x
regions:
- global
post_count: 64
salience: 0.62
sentiment: mixed
confidence: 0.68
tags:
- gaussian-splatting
- blender
- ai-video
- shaders
- unity
- previs
thumbnail: https://external-preview.redd.it/eXg3OTk3Mjh4cDNoMd9Qn7y5N5D268ReIaIXhfcTYlZHHdFBk-z0Qh3Se9gx.png?format=pjpg&auto=webp&s=509255971f64b4b19eaf38102568c3a85d2aff15
---

# 3D & Graphics — 2026-05-28

## TL;DR
- AI-driven camera paths (Google Omni/Flow) turn sketched routes into drone-POV footage — fast previsualization, no rig [2][14][42][54][59]
- Gaussian Splatting goes operational: drone-scale city capture partnership and tourism/heritage use cases [40][36][41]
- TriSplat proposes feed-forward, physics-ready triangle meshes from sparse images — skips Gaussian/mesh-extraction step [56]
- Toon/painterly shaders cross from Blender to Unity URP via fullscreen post passes; Guilty Gear-style breakdown also published [29][1][28]
- Godot WebGPU gains Nanite-style GPU-driven rendering — engine-level shift, not a shader trick [32]

## What happened
Top signals split into three buckets. AI/3D fusion dominated buzz: Bilawal Sidhu's sketched-path → drone footage via Google Omni/Flow went viral and spawned a copycat trend on Seedance [2][14][42][54][59]; KIRI shows splat-captured environments composited with AI-generated figures [58]; Claude Code drove Blender autonomously for an hour producing Geometry Nodes systems and retargeting [51]. Capture/reconstruction: Niantic + Spexi partner on drone-flown city-scale Gaussian splats [40], Ferstel Passage splat uploaded via XGRIDS PortalCam [36], and TriSplat paper claims sim-ready triangles directly from sparse unposed images [56]. Tooling/shaders: a vintage cartoon shader breakdown topped r/blender [1], a Blender-to-Unity URP painterly post-process recreation circulated [29], Guilty Gear technique writeup published [28], Godot's WebGPU got GPU-driven Nanite-style rendering [32], and Unity grass via vertex-color wind shipped from a solo dev [50]. Background noise: lots of Blender portfolio posts [4][6][7][9][13][15], a freelance non-payment cautionary tale [5], and a graphics API rant about descriptors/bindings [22].

## Why it matters (reasoning)
Two structural shifts matter for the studio. First, AI camera-path tools collapse previs cost: a sketched route on a map becomes flyover footage in minutes [2][14][42] — pitching XR or game cinematics no longer needs a rigged Unity camera or Unreal Sequencer setup for first-look. Second, Gaussian Splatting is moving from research demo to commercial pipeline (Niantic/Spexi commissioning flights [40], KIRI compositing real splats with AI figures [58], tourism/heritage explicitly named as disruption targets [36]). For Thai cultural-heritage XR or location-based edutech, this lowers capture cost dramatically. TriSplat [56] is the wildcard — if feed-forward to triangle meshes holds up, it bypasses the splat-to-mesh conversion pain that currently blocks splats from Unity physics/lighting workflows. Painterly/toon shader cross-engine ports [29][28][1] reinforce that stylized non-realistic looks remain the most defensible visual differentiator vs. AI-generated photoreal content.

## Possibility
Next 3–6 months: (a) ~70% chance AI camera-path → video becomes a standard previs step in indie pipelines; quality still inconsistent for hero shots but fine for pitches. (b) ~60% chance Gaussian Splatting capture-as-a-service hits Southeast Asia via XGRIDS or local drone operators within a year. (c) ~40% TriSplat or similar feed-forward-to-mesh becomes production viable in 2026 — paper-stage, no shipping tool yet. (d) ~80% stylized/toon shader workflows continue to outperform AI photoreal for brand identity in games. Counter-risk: AI video tools (Omni, Seedance, Luma) compress demand for traditional 3D motion design — see [5] freelance disputes as early stress signal.

## Org applicability — NDF DEV
Worth piloting now, low cost: (1) Test Google Flow/Omni sketched-path previs for client pitches on XR location experiences and game cinematics — 1-day spike, no pipeline change [2][59]. (2) Capture one Chiang Mai temple or studio interior with a phone-based Gaussian Splat tool (KIRI Engine, Polycam) and try import into Unity via existing splat plugins — useful for cultural-heritage XR pitches [36][58]. (3) Bookmark TriSplat [56] but don't build on it until code drops. (4) For Unity edutech, the URP painterly post-process [29] and grass shader [50] are directly droppable into Next.js-embedded WebGL or Unity WebGL builds. Skip: Claude-Code-drives-Blender [51] is novelty, not production-ready; Godot Nanite [32] interesting but studio is Unity-first.

## Signals to Watch
- TriSplat code release or Unity/Unreal importer for feed-forward meshes
- XGRIDS PortalCam or equivalent splat-capture hardware availability/price in Thailand
- Google Flow/Omni API access or pricing tier for commercial previs use
- Unity official Gaussian Splatting render pipeline support (currently community plugins only)

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | rahulparihar | ^4479 c46 | [Vintage cartoon shaders in Blender](https://www.reddit.com/r/blender/comments/1tpd4c0/vintage_cartoon_shaders_in_blender/) |
| x | bilawalsidhu | ^2999 c131 | [Gave google omni a sketched camera path and asked it to generate drone POV foota](https://x.com/bilawalsidhu/status/2059419767417487718) |
| reddit | flockaroo | ^838 c27 | [home grown gas giant](https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/) |
| x | 3DxDEV7 | ^700 c3 | [DreamWorks animator Nicolas Prothais showcased a stunning Kung Fu Panda rig in B](https://x.com/3DxDEV7/status/2059497395352748099) |
| reddit | Vegetable-Site-3715 | ^512 c78 | [Client agreed to pay hourly on a recorded call, then denied the whole agreement ](https://www.reddit.com/r/blender/comments/1toxcb6/client_agreed_to_pay_hourly_on_a_recorded_call/) |
| reddit | Wellie_man | ^507 c18 | [First attempts at making a walk cycle! How'd I do?](https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/) |
| x | BrainezVisuals | ^477 c57 | [I just turned 18. Here's my VFX/CG work. #b3d #blender https://t.co/g6RRZSsTZm](https://x.com/BrainezVisuals/status/2059681346449031677) |
| reddit | x_otosaka_x | ^458 c19 | [I made a moroccan-themed slot machine inspired by moorish architecture and desig](https://www.reddit.com/r/blender/comments/1tpd00r/i_made_a_moroccanthemed_slot_machine/) |
| reddit | LoquatPutrid2894 | ^306 c17 | [Made Saber Artoria Pendragon, used only blender , how is it ?](https://www.reddit.com/r/blender/comments/1toxkbq/made_saber_artoria_pendragon_used_only_blender/) |
| reddit | Legal-Collection2425 | ^294 c29 | [i present the ice cube on plate do you like it](https://www.reddit.com/r/blender/comments/1tp89ev/i_present_the_ice_cube_on_plate/) |
| reddit | OzGang | ^228 c8 | [NYC Subway Full CGI (Blender + DaVinci Resolve)](https://www.reddit.com/r/blender/comments/1tpmpvd/nyc_subway_full_cgi_blender_davinci_resolve/) |
| x | austin_rief | ^207 c38 | [I’m hiring a founding engineer for my new company. You'll be a good fit if you: ](https://x.com/austin_rief/status/2059704887118586039) |
| reddit | creationstation99 | ^185 c15 | [Made this low poly character in blender](https://www.reddit.com/r/blender/comments/1tp0hu6/made_this_low_poly_character_in_blender/) |
| x | bilawalsidhu | ^181 c4 | [Camera path scribbles are turning into an AI video trend. Cool seedance example ](https://x.com/bilawalsidhu/status/2059751008746471791) |
| reddit | Sufficient-Limit-392 | ^177 c8 | [The stuff I animated](https://www.reddit.com/r/blender/comments/1tpi497/the_stuff_i_animated/) |
| x | A_fan_of_Sonic | ^162 c2 | [Ripped, fixed, and shaded Goku from Sparking! Zero for Blender! 🐉✨ Free download](https://x.com/A_fan_of_Sonic/status/2059644148907417663) |
| x | sevenout | ^157 c0 | [@MarkDuplass They're saying the same thing about Curry Barker, that some mystery](https://x.com/sevenout/status/2059398926797537667) |
| x | vikare06 | ^150 c12 | [There is no discernible design in that image. Just asking GPT to generate a monu](https://x.com/vikare06/status/2059580032826101762) |
| reddit | Unhappy_Document_796 | ^145 c5 | [Yet another test anim](https://www.reddit.com/r/blender/comments/1tpfazt/yet_another_test_anim/) |
| reddit | AlarmedBag9653 | ^143 c17 | [Procedural Creature gen and animation Procedural creature generation and animati](https://www.reddit.com/r/proceduralgeneration/comments/1to7rei/procedural_creature_gen_and_animation/) |
| reddit | Working-Winner52 | ^142 c23 | [Please rate my art and also suggest what I should improve](https://www.reddit.com/r/blender/comments/1tpoqad/please_rate_my_art_and_also_suggest_what_i_should/) |
| reddit | Content_Economist132 | ^137 c36 | [Why do graphics apis need so many layers of abstractions like buffer, descriptor](https://www.reddit.com/r/GraphicsProgramming/comments/1tow7ic/why_do_graphics_apis_need_so_many_layers_of/) |
| reddit | Affectionate_Fly_457 | ^109 c8 | [Made something new using particles](https://www.reddit.com/r/blender/comments/1tp0qt2/made_something_new_using_particles/) |
| reddit | huleeb | ^108 c5 | [the forgotten pipeline](https://www.reddit.com/r/blender/comments/1tp5ehx/the_forgotten_pipeline/) |
| reddit | islammhran_86 | ^97 c6 | [Warm Luxury Interior in Blender I have also completed a **daylight version** of ](https://www.reddit.com/r/blender/comments/1tpc074/warm_luxury_interior_in_blender/) |
| x | HidemyCG | ^89 c0 | [The most optimal renderer settings for a close-up scene with glass and the glass](https://x.com/HidemyCG/status/2059658635236528157) |
| reddit | ExistingMark2998 | ^79 c20 | [first blender ANIMATION!!! rate my work :)) also any idea what should i start ne](https://www.reddit.com/r/blender/comments/1tp3t7w/first_blender_animation/) |
| x | Noggi_3D | ^77 c1 | [I finished setting up a page explaining the techniques Guilty Gear uses to creat](https://x.com/Noggi_3D/status/2059683849521508509) |
| x | jettelly | ^77 c0 | [Developer tantaneity shared how they recreated a painterly shader from Blender i](https://x.com/jettelly/status/2059243161311187193) |
| reddit | Significant-Tree4752 | ^73 c3 | [Maria Calavera: Life and Death scythe (WIP) Maria's weapon did it while practici](https://www.reddit.com/r/blender/comments/1tp2tqk/maria_calavera_life_and_death_scythe_wip/) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@rahulparihar</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 4479 · 💬 46</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tpd4c0/vintage_cartoon_shaders_in_blender/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/eXg3OTk3Mjh4cDNoMd9Qn7y5N5D268ReIaIXhfcTYlZHHdFBk-z0Qh3Se9gx.png?format=pjpg&amp;auto=webp&amp;s=509255971f64b4b19eaf38102568c3a85d2aff15" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Vintage cartoon shaders in Blender”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender artist shared vintage cartoon shader setups that recreate a retro hand-drawn animation look inside Blender's node editor.</dd>
      <dt>Why interesting</dt>
      <dd>High-engagement shader breakdowns (4k+ likes) signal strong community demand for stylized non-photorealistic rendering techniques that are production-ready.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can port this Blender shader logic into URP Shader Graph as a custom cartoon pass — directly useful for stylized XR or e-learning scene aesthetics.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tpd4c0/vintage_cartoon_shaders_in_blender/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2999 · 💬 131</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2059419767417487718">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gave google omni a sketched camera path and asked it to generate drone POV footage. https://t.co/cQZFMtOkEi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google Omni AI generated drone POV video footage from nothing more than a hand-sketched camera path.</dd>
      <dt>Why interesting</dt>
      <dd>Sketch-to-cinematic-video collapses the pre-vis pipeline — no drone hire, no 3D blocking software needed to prototype a flythrough shot.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/XR team can use this to prototype flythrough cinematics and VR environment reveal sequences before committing to engine blocking or shooting real reference.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2059419767417487718" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@flockaroo</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 838 · 💬 27</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/c3g3bHdsdm15aTNoMVQtrb6zyT3nVgsSB9Yrq2NdNhskp9hccODKkoNMp-gx.png?format=pjpg&amp;auto=webp&amp;s=39d0536eb07e798dacd50cf924457269fb83feff" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“home grown gas giant”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A procedurally generated gas giant planet, shared on r/proceduralgeneration by @flockaroo, showing home-grown shader or simulation work producing Jupiter-like visuals.</dd>
      <dt>Why interesting</dt>
      <dd>838 upvotes shows strong community demand for procedural planet visuals — a signal that space/sci-fi aesthetics are high-value for indie and XR projects right now.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can study flockaroo's technique to build reusable procedural planet shaders for space-themed game or XR environments without relying on static textures.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/proceduralgeneration/comments/1tofob7/home_grown_gas_giant/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 700 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2059497395352748099">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“DreamWorks animator Nicolas Prothais showcased a stunning Kung Fu Panda rig in Blender using Rigify, seriously impressive 🔥🐼 #B3D #Blender3D #Blender #Animation #Rigify #CharacterRigging #3DArt #VFX h”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>DreamWorks animator Nicolas Prothais demonstrated a high-quality Kung Fu Panda character rig built in Blender using the Rigify add-on.</dd>
      <dt>Why interesting</dt>
      <dd>A production-level DreamWorks rig recreated in free Blender/Rigify tooling proves studio-grade character animation is accessible without proprietary software.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can study this Rigify workflow to build reusable, animator-friendly rigs for XR/game characters, reducing rigging time on future 3D projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2059497395352748099" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Wellie_man</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 507 · 💬 18</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/" target="_blank" rel="noopener"><img src="https://i.redd.it/x1zm4ycwro3h1.gif" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“First attempts at making a walk cycle! How'd I do?”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender user shares their first attempt at animating a walk cycle and asks the community for feedback.</dd>
      <dt>Why interesting</dt>
      <dd>Walk cycle fundamentals are a core animation skill — community critique loops on Reddit accelerate learning faster than solo practice.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can use public Blender critique threads as free reference benchmarks when evaluating character animation quality for game projects.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tp6fah/first_attempts_at_making_a_walk_cycle_howd_i_do/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BrainezVisuals</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 477 · 💬 57</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BrainezVisuals/status/2059681346449031677">View @BrainezVisuals on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I just turned 18. Here's my VFX/CG work. #b3d #blender https://t.co/g6RRZSsTZm”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An 18-year-old creator shared a VFX/CG portfolio reel made with Blender, showcasing self-taught 3D and visual effects work.</dd>
      <dt>Why interesting</dt>
      <dd>High-quality VFX output from a solo teen artist proves Blender's ceiling is high enough for production-grade work without studio resources.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity and XR team can scout Blender-native artists like this for freelance VFX assets; their skill level raises the bar for what to expect from junior hires.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BrainezVisuals/status/2059681346449031677" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@x_otosaka_x</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 458 · 💬 19</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1tpd00r/i_made_a_moroccanthemed_slot_machine/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/Mm05emZwNGJ3cDNoMZJUmXUucVO8qDsVPdtz19OfQWpAFS9IwdVRzavJoUoJ.png?format=pjpg&amp;auto=webp&amp;s=8bec2a4c4cb152ec786ece2a8ca24e3966e1f14c" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I made a moroccan-themed slot machine inspired by moorish architecture and design”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender artist created a detailed 3D slot machine with Moroccan/Moorish architectural styling and ornamental design.</dd>
      <dt>Why interesting</dt>
      <dd>Shows how cultural architecture motifs can elevate game prop aesthetics beyond generic designs — a strong reference for art direction in casino or cultural-theme game environments.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can use this as art direction reference when designing culturally-themed game props — study the Moorish geometric pattern approach to add authenticity without extra poly cost.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1tpd00r/i_made_a_moroccanthemed_slot_machine/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@LoquatPutrid2894</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 306 · 💬 17</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/blender/comments/1toxkbq/made_saber_artoria_pendragon_used_only_blender/" target="_blank" rel="noopener"><img src="https://preview.redd.it/s2j7c7uamm3h1.jpg?width=2048&amp;format=pjpg&amp;auto=webp&amp;s=bf6f5f9af3cd96f147d0893046d5fef9f8a5fbde" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Made Saber Artoria Pendragon, used only blender , how is it ?”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Reddit user showcased a fully Blender-made 3D character model of Saber Artoria Pendragon from the Fate series, asking for feedback.</dd>
      <dt>Why interesting</dt>
      <dd>The piece demonstrates Blender as a complete solo pipeline for anime-style character art, no external sculpting or rendering tools needed.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can reference this Blender-only workflow for in-house character asset creation, reducing dependency on paid tools like ZBrush or Maya.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/blender/comments/1toxkbq/made_saber_artoria_pendragon_used_only_blender/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
</div>
