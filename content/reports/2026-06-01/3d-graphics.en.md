---
type: social-topic-report
date: '2026-06-01'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-01T04:14:06+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 18
salience: 0.35
sentiment: neutral
confidence: 0.5
tags:
- gaussian-splatting
- unreal-engine
- shaders
- blender
- xr-pipeline
- photogrammetry
thumbnail: https://pbs.twimg.com/media/HJi506gbMAAFWVc.jpg
---

# 3D & Graphics — 2026-06-01

## TL;DR
- Unreal Engine 5.8 adds dataflow-based skeletonization/weighting for complex meshes (e.g. trees) and an experimental Control Rig Dynamics plugin for easier sim-rigging [11].
- Gaussian Splatting is moving from demo to deployable: one creator runs splat scenes on standalone Quest 3 VR with custom multi-renderer ordering (render-order key + depth tiebreak, view-space distance) to fix splat sorting [13].
- Practical cross-engine shader knowledge is being shared openly — a rain-drip shader node graph said to port to Unreal directly, with the noted Unity HDRP difference being mask handling [4].
- Three.js Water Pro produces convincing real-time water with far less setup than hand-built Blender shader-node lighting, per a creator comparison [15].
- Most high-engagement items are individual artist showcases (snow shader [3], ripped game models [9], geometry-node VFX [7]), not tool releases — signal is diffuse today.

## What happened
The day's 3D/graphics items are dominated by individual creator posts on X rather than vendor announcements. The clearest tooling news is Unreal 5.8 surfacing skeletonization and mesh-weighting via dataflow plus an experimental Control Rig Dynamics plugin [11]. Gaussian Splatting appears twice with substance: as a method for spatial/place capture from a few hundred photos [5], and as a working standalone-VR pipeline on Quest 3 that solves splat draw-ordering with a render-order key, depth tiebreak, and view-space distance [13]. Shader and procedural craft is being shared openly: a rain-drip node setup with explicit Unreal/Unity HDRP porting notes [4], a Blender snow shader [3], geometry-node black-hole VFX intended for an Unreal port [7], and Blender particle/geonodes work [8].

## Why it matters (reasoning)
For an asset pipeline feeding Unity and Unreal, two threads matter. First, Gaussian Splatting is crossing into runtime XR: [13] shows the hard part is no longer capture but renderer integration and correct splat sorting on constrained standalone headsets — directly relevant to Quest-class XR deliverables. Second, the shader posts [4][15] reinforce that real-time engine shaders and web stacks (Three.js) can reach quality that previously needed slow offline Blender setups, and that node graphs increasingly transfer across engines with known per-engine caveats (HDRP masking) [4]. Unreal 5.8's rigging/skeletonization tools [11] lower the labor of preparing organic and complex meshes, which is the expensive part of asset prep. The de-aging scan workflow [17] and plain-color scan-friendly props [1] are reminders that photogrammetry quality still depends heavily on capture conditions and manual cleanup, not just software.

## Possibility
Likely: Gaussian Splatting continues maturing as an XR capture-to-runtime path, since working standalone-VR integrations with concrete sorting solutions already exist [13][5]. Plausible: more shader/VFX techniques ship as cross-engine-portable node graphs with documented per-engine differences, making knowledge reuse across Unity/Unreal/Three.js easier [4][15]. Plausible: Unreal 5.8 rigging features ([11], marked experimental) stabilize over coming releases but should be treated as unstable now. Unlikely (no evidence here): a single dominant tool or standard consolidating these workflows — today's signal is fragmented across individual creators.

## Org applicability — NDF DEV
Run a scoped Gaussian Splatting test for an XR location/environment capture and validate splat sorting on Quest 3 specifically, using the ordering approach described (render-order key + depth tiebreak + view-space distance) (effort: med) [13][5]. Save the openly shared rain-drip shader node setup as a reference and note the Unity HDRP mask difference for the team's shader library (effort: low) [4]. Evaluate Three.js Water Pro for any web/mobile experiences needing real-time water before hand-building Blender shaders (effort: low) [15]. Trial Unreal 5.8 skeletonize/weighting and Control Rig Dynamics on a complex organic asset, but keep it off production paths while experimental (effort: med) [11]. For photogrammetry props, adopt the plain-color, scan-friendly approach to reduce cleanup (effort: low) [1][17]. Skip the off-topic high-engagement items (cricket [2], AI short-film budget claims [10], VFX career anecdotes [12]) — no tooling value.

## Signals to Watch
- Standalone-VR Gaussian Splatting renderer ordering on Quest 3 — watch whether reusable sorting solutions get packaged [13].
- Unreal 5.8 Control Rig Dynamics and dataflow skeletonization moving from experimental to stable [11].
- Cross-engine portability of shader node graphs with documented HDRP/Unreal differences [4].
- Three.js real-time water quality vs. offline Blender setups for web/mobile work [15].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | PXJOSHIMA | ^3163 c12 | [In 2024 I was approached on IG by someone from a games design studio about makin](https://x.com/PXJOSHIMA/status/2060601157240881492) |
| x | broskyxn | ^1668 c13 | [@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year stil](https://x.com/broskyxn/status/2060730034584015072) |
| x | AnimGaby | ^939 c12 | [D4DJ as Murder drones some parts are off sync because daVinci is trolling me Som](https://x.com/AnimGaby/status/2061071305634627949) |
| x | sean_gause | ^841 c5 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | bilawalsidhu | ^447 c21 | [We treat 3d scanning like a tech demo, but it’s actually spatial memory capture.](https://x.com/bilawalsidhu/status/2061134940813611505) |
| x | VFX_Therapy | ^340 c3 | [When your Unreal VFX project hits different… @IgorPontes breakdown his Sasuke-le](https://x.com/VFX_Therapy/status/2061109917222920517) |
| x | ashlee3dee | ^203 c1 | [stylized black hole vfx with geometry nodes :3 i will port this to unreal engine](https://x.com/ashlee3dee/status/2061195779952275511) |
| x | lightarchitect_ | ^190 c1 | [I just love particle systems in Blender. Ok I know its not even close to Houdini](https://x.com/lightarchitect_/status/2060838278505648401) |
| x | A_fan_of_Sonic | ^160 c3 | [Ripped, fixed and shaded Vegeta from Sparking Zero for Blender • Move eyes in sh](https://x.com/A_fan_of_Sonic/status/2060749070554001630) |
| x | ZohaibAi__sf | ^130 c37 | [Day 5. It’s finished. 20,000 credits. ~$5,000. A global story. VFX. Costumes. Wi](https://x.com/ZohaibAi__sf/status/2060670680329511122) |
| x | chasescooper | ^126 c3 | [We have some exciting stuff in Unreal 5.8 - Skeletonize and weight complex meshe](https://x.com/chasescooper/status/2060737891408515270) |
| x | mattworkman | ^105 c19 | [I once OFFENDED the mentor that hand picked me up from the gutter and sat me at ](https://x.com/mattworkman/status/2060573070151078006) |
| x | DSkaale | ^98 c4 | [Just stepped inside my favorite movie locations on my Quest 3 🎬 Gaussian splatti](https://x.com/DSkaale/status/2061114844263117118) |
| x | bilawalsidhu | ^74 c3 | [Fucking cool. Giving AR portal vibes - like watching volumetric video with full ](https://x.com/bilawalsidhu/status/2060943911363690875) |
| x | SteveWarnerFL | ^38 c6 | [Why is Three.js Water Pro able to do this level of realism in real time but I st](https://x.com/SteveWarnerFL/status/2060800324911222931) |
| x | bilawalsidhu | ^36 c0 | [Omni’s take on rendering the camera path, then the *actual* earth studio render ](https://x.com/bilawalsidhu/status/2060886445770870905) |
| x | anishmoonka | ^24 c1 | [To build a young Arnold, the crew scanned an older one. They took a full-body 3D](https://x.com/anishmoonka/status/2061192494449152390) |
| x | MeshyAI | ^1 c0 | [@niftyisland 😍 This is soooooo cool 😍](https://x.com/MeshyAI/status/2061246669040369797) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PXJOSHIMA</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3163 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PXJOSHIMA/status/2060601157240881492">View @PXJOSHIMA on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In 2024 I was approached on IG by someone from a games design studio about making them a replica of the ROK body armour, they wanted it in a plain colour because it's easier for them to 3D scan and th”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A prop maker recounts being hired by a game studio in 2024 to build a plain-color physical replica of ROK body armour for 3D scanning, then never heard back.</dd>
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
    <span class="ndf-engagement">♥ 1668 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/broskyxn/status/2060730034584015072">View @broskyxn on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year still getting advantage of pitches, now everyone's playing against us, God jii, be kind to us one more time this season. htt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user complains about perceived unfair pitch conditions favoring an opposing cricket team, referencing 'Unreal rigging' as a cricket metaphor — not Unreal Engine.</dd>
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
    <span class="ndf-author">@AnimGaby</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 939 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnimGaby/status/2061071305634627949">View @AnimGaby on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“D4DJ as Murder drones some parts are off sync because daVinci is trolling me Some part I didn't include the background character because It will just destroy my blender lol anyways snow shader by @Ash”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Fan animator @AnimGaby posted a D4DJ × Murder Drones crossover animation made in Blender and DaVinci Resolve, noting they cut background characters to avoid crashing Blender and used a snow shader by @Ashkap50.</dd>
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
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 841 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@sean_gause shared the complete node graph for a Unity HDRP rain drip shader; mask map uses metal/AO/detail/smooth channels, and the setup ports directly to Unreal with minor differences.</dd>
      <dt>Why interesting</dt>
      <dd>A production-ready wet-surface shader shared openly gives the Unity team a verified starting point for environment realism without building from scratch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can pull this node graph into any HDRP environment scene to add rain-wet surface detail, then adapt the mask map channels to match the project's existing texture pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 447 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061134940813611505">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We treat 3d scanning like a tech demo, but it’s actually spatial memory capture. Damn near teleportation. A few hundred photos of my parent’s old home, and now it’s immortalized forever. 3d gaussian s”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer captured a real home using ~hundreds of photos, then processed them through RealityCapture + Lichtfeld to produce a 3D Gaussian splat — demonstrating a low-barrier photogrammetry-to-splat pipeline.</dd>
      <dt>Why interesting</dt>
      <dd>The RealityCapture → Lichtfeld pipeline is production-ready for real-world environment capture, directly applicable to XR/VR scene reconstruction without expensive LiDAR hardware.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team can test this RealityCapture + Lichtfeld workflow to capture real-world spaces as Gaussian splat assets and evaluate import compatibility with Unity XR projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061134940813611505" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 340 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2061109917222920517">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“When your Unreal VFX project hits different… @IgorPontes breakdown his Sasuke-level Katon 🔥 with insane stylized effects. #vfx https://t.co/j4wFOeAnBm”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@IgorPontes released a breakdown of stylized anime-style fire VFX built in Unreal Engine, shared by @VFX_Therapy on X.</dd>
      <dt>Why interesting</dt>
      <dd>Stylized elemental VFX composition techniques in this breakdown transfer directly to anime-style particle work in Unity game projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Watch the breakdown to extract the stylized fire layering approach, then re-implement it in Unity VFX Graph or Shader Graph.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2061109917222920517" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ashlee3dee</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 203 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ashlee3dee/status/2061195779952275511">View @ashlee3dee on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“stylized black hole vfx with geometry nodes :3 i will port this to unreal engine... soon https://t.co/bu98xUEYuO”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Artist @ashlee3dee built stylized black hole VFX in Blender using geometry nodes and plans to port the effect to Unreal Engine.</dd>
      <dt>Why interesting</dt>
      <dd>Geometry nodes-driven VFX is a transferable workflow — the same logic applies when building stylized space/portal effects in Unity's VFX Graph.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Study the geometry nodes setup as a reference when the Unity team needs a stylized singularity or portal shader for an XR scene.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ashlee3dee/status/2061195779952275511" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@lightarchitect_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 190 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/lightarchitect_/status/2060838278505648401">View @lightarchitect_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I just love particle systems in Blender. Ok I know its not even close to Houdini but still you'd be amazed what you can do. And now with Geonodes as well there is even more! Blender Mega Add-on Bundle”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender artist promotes a paid 'Mega Add-on Bundle' while praising Blender's particle systems and Geometry Nodes as a capable (if lesser) alternative to Houdini.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/lightarchitect_/status/2060838278505648401" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
