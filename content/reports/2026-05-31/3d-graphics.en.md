---
type: social-topic-report
date: '2026-05-31'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-05-31T16:14:35+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 21
salience: 0.55
sentiment: positive
confidence: 0.6
tags:
- gaussian-splatting
- gltf
- xr
- blender
- unreal
- shaders
thumbnail: https://pbs.twimg.com/media/HJi506gbMAAFWVc.jpg
---

# 3D & Graphics — 2026-05-31

## TL;DR
- glTF now has an official 3D Gaussian Splatting extension, and city-scale 3DGS can be compressed, tiled, and streamed [3][16].
- SplatBox runs 2M+ Gaussian splats with real-time relighting on standalone Quest 3, no cables [9].
- Gaussian Splatting reconstruction is rolling out to 1,700 Australian suburbs via CoStar Group, captured by aerial oblique multi-camera platforms [17][20].
- Practical shader/rig content circulated: a rain-drip node setup portable Blender→Unreal/Unity HDRP [4], and Unreal 5.8 adds dataflow skeletonization plus experimental Control Rig Dynamics [10].
- KeenTools released open beta of GeoTracker matchmove (object/camera tracking) natively in Houdini [15].

## What happened
The dominant thread is Gaussian Splatting maturing into a streamable, standardized format. Khronos added an official 3DGS extension to glTF, enabling compression, tiling, and streaming of city-scale splats [3], discussed further with Khronos president Neil Trevett and Niantic Spatial CTO Brian McClendon [16]. On the runtime side, SplatBox demonstrated 2M+ splats with real-time relighting on a standalone Quest 3 [9], and CoStar Group is deploying suburb-scale splat reconstructions across 1,700 Australian areas from aerial oblique imagery [17][20]. Separate tooling items: a shareable rain-drip shader node graph said to port from Blender to Unreal and Unity HDRP with a mask-map difference [4]; Unreal 5.8 dataflow skeletonization for complex meshes (e.g. trees) plus an experimental Control Rig Dynamics plugin [10]; KeenTools GeoTracker matchmove in open beta for Houdini [15]; and Blender particle/geonodes and rigging workflows [8][12].

## Why it matters (reasoning)
Standardization (glTF 3DGS) plus standalone-VR relighting [9] moves splats from research demos toward an asset format an engine pipeline can ingest and stream, which matters for XR experiences where photoreal environments are otherwise expensive to model by hand [3][16]. Relighting on-device [9] addresses the main production blocker for splats — baked, fixed lighting that doesn't react to a scene. Suburb-scale capture via aerial platforms [17][20] signals that the bottleneck is shifting from capture to delivery and integration. The second-order effect: studios may increasingly choose capture-and-stream over manual environment modeling for real-world locations, while authored content (shaders, rigs) remains the value-add for stylized/game work [4][6]. The shader and Unreal/Houdini items [4][10][15] are incremental, not structural, but they lower friction in existing DCC→engine pipelines.

## Possibility
Likely: 3DGS as a glTF-standard asset becomes a viable input for Unity/Unreal XR scenes within the year, given an official extension and engine-adjacent backers [3][16]. Plausible: on-device relit splats reach production use for Quest-class XR, though the SplatBox demo is a single vendor claim not yet independently validated [9]. Plausible: location-based splat datasets (real suburbs) feed AR/spatial apps, following the Australian rollout [17]. Unlikely near-term: splats fully replace mesh-based authored assets for interactive games, since collision, animation, and stylization still favor meshes [4][6][8]. No source states numeric probabilities.

## Org applicability — NDF DEV
1) Run a small spike importing a glTF 3DGS asset into Unity and test on Quest 3 for an XR scene — assess streaming and relighting feasibility (effort: med) [3][9]. 2) Capture one real location via photogrammetry/aerial-style oblique imagery and reconstruct as a splat to compare against manual modeling cost for an XR pitch (effort: med) [17][20]. 3) Adopt the rain-drip shader node pattern as a reference for portable Blender→Unity HDRP material work; validate the mask-map difference noted (effort: low) [4]. 4) When upgrading Unreal, trial 5.8 dataflow skeletonization and Control Rig Dynamics for vegetation/secondary motion, but treat as experimental (effort: low to evaluate) [10]. Skip: KeenTools GeoTracker for Houdini unless matchmove is in the active pipeline [15]; Luma promo-asset agents [18][19] (marketing, not asset production); the AI-short-film and sports/scan anecdotes [1][2][7] are low signal.

## Signals to Watch
- Engine-native ingestion of glTF 3DGS in Unity/Unreal — watch for first-class importers [3][16].
- Independent confirmation of standalone-Quest splat relighting performance beyond the SplatBox claim [9].
- Location-based splat datasets expanding past the Australian 1,700-suburb rollout [17].
- Unreal 5.8 Control Rig Dynamics moving from experimental to stable [10].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | PXJOSHIMA | ^3169 c12 | [In 2024 I was approached on IG by someone from a games design studio about makin](https://x.com/PXJOSHIMA/status/2060601157240881492) |
| x | broskyxn | ^1669 c13 | [@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year stil](https://x.com/broskyxn/status/2060730034584015072) |
| x | bilawalsidhu | ^717 c21 | [i like big splats and i cannot lie. you can now compress, tile and stream city s](https://x.com/bilawalsidhu/status/2060518632547877359) |
| x | sean_gause | ^698 c4 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | AnimGaby | ^301 c8 | [D4DJ as Murder drones some parts are off sync because daVinci is trolling me Som](https://x.com/AnimGaby/status/2061071305634627949) |
| x | A_fan_of_Sonic | ^157 c2 | [Ripped, fixed and shaded Vegeta from Sparking Zero for Blender • Move eyes in sh](https://x.com/A_fan_of_Sonic/status/2060749070554001630) |
| x | ZohaibAi__sf | ^126 c36 | [Day 5. It’s finished. 20,000 credits. ~$5,000. A global story. VFX. Costumes. Wi](https://x.com/ZohaibAi__sf/status/2060670680329511122) |
| x | EdwardUrena_h | ^113 c0 | [One of the advantages of this is that you can design your own control system for](https://x.com/EdwardUrena_h/status/2060397763632701921) |
| x | DSkaale | ^108 c2 | [🚀 SplatBox now runs 2M+ Gaussian splats — with real-time relighting — on a stand](https://x.com/DSkaale/status/2060476211193655419) |
| x | chasescooper | ^104 c3 | [We have some exciting stuff in Unreal 5.8 - Skeletonize and weight complex meshe](https://x.com/chasescooper/status/2060737891408515270) |
| x | mattworkman | ^104 c19 | [I once OFFENDED the mentor that hand picked me up from the gutter and sat me at ](https://x.com/mattworkman/status/2060573070151078006) |
| x | lightarchitect_ | ^93 c1 | [I just love particle systems in Blender. Ok I know its not even close to Houdini](https://x.com/lightarchitect_/status/2060838278505648401) |
| x | bilawalsidhu | ^55 c1 | [Fucking cool. Giving AR portal vibes - like watching volumetric video with full ](https://x.com/bilawalsidhu/status/2060943911363690875) |
| x | bilawalsidhu | ^31 c0 | [Omni’s take on rendering the camera path, then the *actual* earth studio render ](https://x.com/bilawalsidhu/status/2060886445770870905) |
| x | sidefx | ^31 c1 | [@keen_tools has released the Open Beta of GeoTracker for Houdini, a fully integr](https://x.com/sidefx/status/2060519060899782737) |
| x | bilawalsidhu | ^28 c0 | [i went deep on where 3DGS goes next with the two people who'd know -- brian mccl](https://x.com/bilawalsidhu/status/2060520050742702503) |
| x | RadianceFields | ^26 c1 | [gaussian splatting is coming to 1,700 Australian suburbs this summer. The CoStar](https://x.com/RadianceFields/status/2060415724665946412) |
| x | LumaLabsAI | ^25 c5 | [The conversation was great. Now make sure the promo stops people in their tracks](https://x.com/LumaLabsAI/status/2060406509578981568) |
| x | LumaLabsAI | ^19 c3 | [The blog post did the thinking. Now let the promo do the work. Drop in the conte](https://x.com/LumaLabsAI/status/2060461313713909783) |
| x | bilawalsidhu | ^5 c1 | [@AIDSfinder Most of these are aerial capture platforms - multi camera oblique im](https://x.com/bilawalsidhu/status/2060556756611113164) |
| x | bilawalsidhu | ^5 c0 | [@seungwoo0197 Very cool](https://x.com/bilawalsidhu/status/2060481731019362494) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PXJOSHIMA</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3169 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PXJOSHIMA/status/2060601157240881492">View @PXJOSHIMA on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In 2024 I was approached on IG by someone from a games design studio about making them a replica of the ROK body armour, they wanted it in a plain colour because it's easier for them to 3D scan and th”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A prop maker recounts being hired by a game studio to build a physical ROK body armour replica in plain colour so it could be 3D scanned, with camo texture to be added digitally — the project was apparently dropped.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PXJOSHIMA/status/2060601157240881492" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@broskyxn</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1669 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/broskyxn/status/2060730034584015072">View @broskyxn on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year still getting advantage of pitches, now everyone's playing against us, God jii, be kind to us one more time this season. htt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A cricket fan complains that matches are rigged against their team and pitches favour opponents, referencing 'Unreal rigging' as slang for unfairness — not the game engine.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/broskyxn/status/2060730034584015072" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 717 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2060518632547877359">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i like big splats and i cannot lie. you can now compress, tile and stream city scale 3d gaussian splats -- glTF has an official 3DGS extension now too. this is what the future of google earth looks li”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>glTF now has an official 3D Gaussian Splats extension, enabling city-scale 3DGS compression, tiling, and streaming of photorealistic real-world environments as standard assets.</dd>
      <dt>Why interesting</dt>
      <dd>Official glTF support puts 3DGS into the standard asset pipeline — XR and Unity projects can reference photorealistic captured scenes without custom loaders.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/XR team should test glTF 3DGS extension support in current Unity builds to assess readiness for real-world scene capture in upcoming projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2060518632547877359" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 698 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@sean_gause shares the full node graph for a rain drip shader in Unity HDRP, with the mask map channel breakdown (metal, AO, detail, smooth) and notes on porting it to Unreal Engine.</dd>
      <dt>Why interesting</dt>
      <dd>A ready-to-use wet-surface shader node setup for Unity HDRP saves the Unity team from building rain/drip effects from scratch on environment or XR scenes.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Save this node graph as a reusable shader asset in the studio's Unity HDRP project for any scene requiring rain or wet-surface detail.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnimGaby</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 301 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnimGaby/status/2061071305634627949">View @AnimGaby on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“D4DJ as Murder drones some parts are off sync because daVinci is trolling me Some part I didn't include the background character because It will just destroy my blender lol anyways snow shader by @Ash”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@AnimGaby posted a fan Blender animation combining D4DJ and Murder Drones, noting sync issues in DaVinci Resolve and that background characters were cut to prevent Blender from crashing.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AnimGaby/status/2061071305634627949" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@A_fan_of_Sonic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 157 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/A_fan_of_Sonic/status/2060749070554001630">View @A_fan_of_Sonic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ripped, fixed and shaded Vegeta from Sparking Zero for Blender • Move eyes in shader editor • Facial expressions with shapekeys Enjoy! https://t.co/ANJzYDKTMQ https://t.co/xmDuZMTEje”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender artist ripped and rigged Vegeta from Sparking Zero, sharing the file with shader-driven eye movement and shapekey-based facial expressions.</dd>
      <dt>Why interesting</dt>
      <dd>The shapekey + shader eye combo is a concrete reference for building facial rigs in Blender before export to Unity or XR pipelines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Study the shader eye and shapekey setup as a rigging pattern for character faces in the studio's Unity or XR work — ignore the ripped asset itself due to IP.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/A_fan_of_Sonic/status/2060749070554001630" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ZohaibAi__sf</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 126 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ZohaibAi__sf/status/2060670680329511122">View @ZohaibAi__sf on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Day 5. It’s finished. 20,000 credits. ~$5,000. A global story. VFX. Costumes. Wild locations. Even a full one-take sequence. At this budget… for a short film? Unreal. But here’s the truth: It wasn’t p”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A creator produced a short film with VFX, costumes, and varied locations using Agent One AI in 5 days at ~$5,000 (20k credits), reporting that directorial thinking drove quality more than prompting skill.</dd>
      <dt>Why interesting</dt>
      <dd>The $5K cost benchmark and 'directing over prompting' framing are directly useful for studios evaluating AI cinematic pipelines for game trailers, XR demos, or e-learning video.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run one internal test with Agent One on a cinematic asset (game trailer or XR promo) to get a real cost-per-minute and quality baseline before committing to the pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ZohaibAi__sf/status/2060670680329511122" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EdwardUrena_h</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 113 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EdwardUrena_h/status/2060397763632701921">View @EdwardUrena_h on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One of the advantages of this is that you can design your own control system for the bones. #blender #animation #rig #b3d #rigging https://t.co/18WTbaG7VA”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender user demonstrates building a custom bone control system for character rigs, showing the flexibility of manual rig design in Blender.</dd>
      <dt>Why interesting</dt>
      <dd>Studios doing character animation in Unity or XR can apply custom Blender rig controls to get cleaner bone hierarchies before export.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can explore custom Blender rig controllers on the next character asset to reduce animator friction during import.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EdwardUrena_h/status/2060397763632701921" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
