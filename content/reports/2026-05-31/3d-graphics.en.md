---
type: social-topic-report
date: '2026-05-31'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-05-31T04:24:21+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 30
salience: 0.6
sentiment: positive
confidence: 0.55
tags:
- gaussian-splatting
- xr
- blender
- asset-pipeline
- ai-3d
- unity
thumbnail: https://pbs.twimg.com/media/HJi506gbMAAFWVc.jpg
---

# 3D & Graphics — 2026-05-31

## TL;DR
- glTF now has an official 3D Gaussian Splatting extension, with city-scale 3DGS that can be compressed, tiled and streamed [4]; standards leads from Niantic Spatial and Khronos discussed where 3DGS goes next [22].
- SplatBox runs 2,000,000+ Gaussian splats with real-time relighting on a standalone Quest 3, no cables [16] — directly relevant to the studio's XR/VR work.
- Blender geometry-nodes procedural workflows [15] and a cloth-physics-bake-to-bones rig that transfers sim to game engines [6][11] show maturing Blender→engine asset pipelines.
- Meshy launched a 'Meshy 3D Agent' beta for chat-driven 3D generation [10][30]; a separate post claims Claude Opus 4.8 wired into Blender replaces artist work, which reads as hype, not verified [14].
- Unreal 5.8 adds experimental skeletonize/weight for complex meshes (trees) and Control Rig Dynamics [17]; CoStar is bringing 3DGS to 1,700 Australian suburbs [24].

## What happened
Gaussian Splatting was the dominant real signal. glTF gained an official 3DGS extension and city-scale splats can now be compressed, tiled and streamed [4], with a deep-dive conversation featuring Niantic Spatial's CTO and Khronos' president on the format's direction [22], plus aerial oblique-imagery capture context [27]. On-device progress: SplatBox renders 2M+ splats with real-time relighting on standalone Quest 3 [16], and CoStar is reconstructing 1,700 Australian suburbs [24]. On the DCC/pipeline side, Blender content covered procedural geometry-nodes assets [15], a cloth-physics-to-bones rig for engine transfer [6][11], and shader/texturing workflows feeding Unity/Unreal [5][9][20]. Unreal 5.8 previewed mesh skeletonization and Control Rig Dynamics [17], and Unity's Infinite Lands showed a spline-based procedural road system [18]. AI-3D tooling appeared via Meshy's chat-based 3D Agent beta [10][30] and an unverified claim of Claude Opus 4.8 driving Blender [14]. Much of the highest-engagement content was anime/fan render art [2][9] or off-topic sports posts [1][3], not tooling news.

## Why it matters (reasoning)
The 3DGS standardization step matters most for the studio. An official glTF extension [4] plus streaming/tiling means splats can move through existing asset pipelines and engines rather than living in bespoke viewers, and on-device Quest 3 playback with relighting [16] removes the prior blocker that splats were too heavy or static for standalone XR. Together these shift Gaussian Splatting from demo to a plausible production capture format for XR experiences. The Blender developments [6][11][15][20] reduce manual labor in the parts of asset production the studio already owns — procedural variation and getting sim/cloth into engines as baked bone animation. AI-3D tools [10][14] are the noisiest area: the Meshy agent is a real beta [10][30], but the 'artists replaced in 5 prompts' framing [14] is a marketing claim with no shown reproducibility, so treat output quality, topology and rig-readiness as unproven.

## Possibility
Likely: 3DGS adoption accelerates in tooling now that glTF has a formal extension and engines/viewers can target one format [4][22]. Plausible: standalone-headset splat playback like SplatBox [16] becomes viable for client XR demos within the next year, given it already hits 2M splats with relighting on Quest 3. Plausible: 3DGS gets repurposed as spatial-reasoning benchmarks for AI video models, as floated in two posts [7][26] — speculative and not yet a product. Unlikely near-term: AI agents producing finished, rig-ready game assets without artist cleanup [14][10]; current evidence is a beta and an unverified claim, so quality at production bar is not demonstrated.

## Org applicability — NDF DEV
1) Run a scoped test of Quest 3 splat playback (SplatBox-style) for one XR portfolio piece, using a photogrammetry/aerial capture of a real location — effort med, validates whether 3DGS is usable for client XR [16][4]. 2) Adopt the trim-sheet → Substance masks → Unity shader texturing workflow [20] and procedural geometry-nodes assets [15] in current Unity asset production — effort low/med, reduces repetitive authoring. 3) Pilot the Blender cloth-physics-bake-to-bones rig on one character to transfer sim into Unity as baked animation — effort med [6][11]. 4) Trial Meshy 3D Agent on throwaway concept/blockout assets only, with artist review gates — effort low, no pipeline commitment [10][30]. Skip: the 'Claude Opus replaces artists' claim as a production plan [14]; Unreal 5.8 features [17] unless an Unreal project is active; cricket/anime fan posts [1][2][3][9] carry no tooling signal despite high engagement.

## Signals to Watch
- glTF 3DGS extension uptake in engines and exporters — watch for Unity/Unreal import support [4][22].
- Standalone-headset splat tools (SplatBox) hitting higher splat counts or shipping SDKs for Quest [16].
- Meshy 3D Agent leaving beta and any independent topology/rig-quality tests [10][30].
- Whether 3DGS captures get used as AI spatial-reasoning benchmarks, signaling broader investment [7][26].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | PXJOSHIMA | ^2989 c12 | [In 2024 I was approached on IG by someone from a games design studio about makin](https://x.com/PXJOSHIMA/status/2060601157240881492) |
| x | Nyaonyx09 | ^2509 c11 | [Welcome back.... Animations by me using Blender. Credits : Models : Hoyoverse BG](https://x.com/Nyaonyx09/status/2060277804470862196) |
| x | broskyxn | ^1556 c11 | [@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year stil](https://x.com/broskyxn/status/2060730034584015072) |
| x | bilawalsidhu | ^679 c21 | [i like big splats and i cannot lie. you can now compress, tile and stream city s](https://x.com/bilawalsidhu/status/2060518632547877359) |
| x | sean_gause | ^221 c2 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | EdwardUrena_h | ^195 c2 | [With this tool as a foundation, you will be able to bake the cloth physics onto ](https://x.com/EdwardUrena_h/status/2060338391380619716) |
| x | bilawalsidhu | ^176 c6 | [Larus went ham with this one! Love the synced highlighting on the camera path, s](https://x.com/bilawalsidhu/status/2060373038982459741) |
| x | AckroseEdits | ^154 c18 | [Vfx highlights from @StanBrowney's Fitness Island video 🏝️ -Premiere pro + After](https://x.com/AckroseEdits/status/2060352963986530678) |
| x | A_fan_of_Sonic | ^144 c2 | [Ripped, fixed and shaded Vegeta from Sparking Zero for Blender • Move eyes in sh](https://x.com/A_fan_of_Sonic/status/2060749070554001630) |
| x | MeshyAI | ^120 c9 | [Introducing Meshy 3D Agent 🚀 The world's first AI agent for 3D creation, now in ](https://x.com/MeshyAI/status/2060311322123014560) |
| x | EdwardUrena_h | ^110 c0 | [One of the advantages of this is that you can design your own control system for](https://x.com/EdwardUrena_h/status/2060397763632701921) |
| x | ZohaibAi__sf | ^106 c30 | [Day 5. It’s finished. 20,000 credits. ~$5,000. A global story. VFX. Costumes. Wi](https://x.com/ZohaibAi__sf/status/2060670680329511122) |
| x | mattworkman | ^103 c19 | [I once OFFENDED the mentor that hand picked me up from the gutter and sat me at ](https://x.com/mattworkman/status/2060573070151078006) |
| x | polydao | ^96 c18 | [This guy connected Claude Opus 4.8 to Blender and now 3D artists are getting rep](https://x.com/polydao/status/2060311186546065552) |
| x | 3DxDEV7 | ^90 c0 | [Procedural leather sandals built entirely with geometry nodes in Blender by 3D a](https://x.com/3DxDEV7/status/2060277202214674661) |
| x | DSkaale | ^79 c2 | [🚀 SplatBox now runs 2M+ Gaussian splats — with real-time relighting — on a stand](https://x.com/DSkaale/status/2060476211193655419) |
| x | chasescooper | ^76 c3 | [We have some exciting stuff in Unreal 5.8 - Skeletonize and weight complex meshe](https://x.com/chasescooper/status/2060737891408515270) |
| x | jettelly | ^63 c1 | [Developer Sapra shared how the spline-based road system works in their tool, Inf](https://x.com/jettelly/status/2060360513335549985) |
| x | Creality3dP | ^48 c7 | [Pika is Coming. Your first portable 3D scanning companion. For many people, 3D s](https://x.com/Creality3dP/status/2060276880138461651) |
| x | Rustledust77 | ^34 c1 | [Texturing workflow for our @FracturedRTS units: -&gt; Assign trim sheet material](https://x.com/Rustledust77/status/2060279247491465611) |
| x | sidefx | ^29 c1 | [@keen_tools has released the Open Beta of GeoTracker for Houdini, a fully integr](https://x.com/sidefx/status/2060519060899782737) |
| x | bilawalsidhu | ^27 c0 | [i went deep on where 3DGS goes next with the two people who'd know -- brian mccl](https://x.com/bilawalsidhu/status/2060520050742702503) |
| x | LumaLabsAI | ^25 c5 | [The conversation was great. Now make sure the promo stops people in their tracks](https://x.com/LumaLabsAI/status/2060406509578981568) |
| x | RadianceFields | ^23 c1 | [gaussian splatting is coming to 1,700 Australian suburbs this summer. The CoStar](https://x.com/RadianceFields/status/2060415724665946412) |
| x | LumaLabsAI | ^18 c3 | [The blog post did the thinking. Now let the promo do the work. Drop in the conte](https://x.com/LumaLabsAI/status/2060461313713909783) |
| x | bilawalsidhu | ^16 c0 | [Omni’s take on rendering the camera path, then the *actual* earth studio render ](https://x.com/bilawalsidhu/status/2060886445770870905) |
| x | bilawalsidhu | ^5 c1 | [@AIDSfinder Most of these are aerial capture platforms - multi camera oblique im](https://x.com/bilawalsidhu/status/2060556756611113164) |
| x | bilawalsidhu | ^5 c0 | [@seungwoo0197 Very cool](https://x.com/bilawalsidhu/status/2060481731019362494) |
| x | bilawalsidhu | ^5 c1 | [@lexsicarium “She can relax right there” :-)](https://x.com/bilawalsidhu/status/2060373513966399642) |
| x | MeshyAI | ^3 c0 | [🥳 It's just the beginning — share your feedback, every reply shapes what we ship](https://x.com/MeshyAI/status/2060311516092760293) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PXJOSHIMA</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2989 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PXJOSHIMA/status/2060601157240881492">View @PXJOSHIMA on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In 2024 I was approached on IG by someone from a games design studio about making them a replica of the ROK body armour, they wanted it in a plain colour because it's easier for them to 3D scan and th”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A prop maker recounts being commissioned by a games studio to build a plain-color ROK body armour replica for 3D scanning, intending to add camo texture digitally afterward — a project the studio apparently dropped.</dd>
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
    <span class="ndf-author">@Nyaonyx09</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2509 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Nyaonyx09/status/2060277804470862196">View @Nyaonyx09 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Welcome back.... Animations by me using Blender. Credits : Models : Hoyoverse BG : 克里斯提亚娜 Shader : StellarToon #Danmarch #Phaistelle https://t.co/LWgrGJgG7j”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Artist @Nyaonyx09 posted a Blender fan animation using Hoyoverse character models and the StellarToon toon shader, crediting all assets.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Nyaonyx09/status/2060277804470862196" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@broskyxn</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1556 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/broskyxn/status/2060730034584015072">View @broskyxn on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@mufaddal_vohra Unreal rigging man, they didn't even reach finals last year still getting advantage of pitches, now everyone's playing against us, God jii, be kind to us one more time this season. htt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A cricket fan accuses match organizers of unfair pitch preparation favoring certain teams, using 'Unreal rigging' as slang for match-fixing, not the Unreal Engine tool.</dd>
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
    <span class="ndf-engagement">♥ 679 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2060518632547877359">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i like big splats and i cannot lie. you can now compress, tile and stream city scale 3d gaussian splats -- glTF has an official 3DGS extension now too. this is what the future of google earth looks li”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>glTF now has an official 3D Gaussian Splat (3DGS) extension, enabling compressed, tiled, and streamable city-scale splat scenes inside standard 3D toolchains.</dd>
      <dt>Why interesting</dt>
      <dd>The official glTF extension lets 3DGS assets move through standard pipelines (Unity, web, XR) without custom loaders, making photorealistic scanned environments practical for real projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a Unity or WebXR prototype with the glTF 3DGS extension to compare streaming quality against traditional mesh assets for environment and XR scene work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2060518632547877359" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 221 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Sean Gause shared the complete node graph for a rain drip shader built in Unity HDRP, highlighting the mask map channel layout: metal, AO, detail, and smoothness — and noted it ports to Unreal with minimal changes.</dd>
      <dt>Why interesting</dt>
      <dd>Free, documented shader node setup for wet-surface rain effects in Unity HDRP — a common environment art requirement that usually takes trial-and-error to get right.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can drop this node graph into any HDRP project that needs wet-surface or rain weather effects without building from scratch.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EdwardUrena_h</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 195 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EdwardUrena_h/status/2060338391380619716">View @EdwardUrena_h on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“With this tool as a foundation, you will be able to bake the cloth physics onto the bones, allowing you to transfer it to game engines. #blender #b3d #rig #rigging #animation @BlenderDev @Blender http”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender tool bakes cloth physics simulation onto rig bones, producing bone-driven cloth animation that can be exported to game engines like Unity.</dd>
      <dt>Why interesting</dt>
      <dd>Runtime cloth physics in Unity is costly; baking to bones gives the Unity team pre-computed cloth motion with no physics overhead at runtime.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test this tool on a cloth-heavy character in Blender and validate the baked bone animation exports cleanly into the studio's Unity pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EdwardUrena_h/status/2060338391380619716" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 176 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2060373038982459741">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Larus went ham with this one! Love the synced highlighting on the camera path, something I wanted to try myself. Makes me think these could end up as spatial reasoning benchmarks for ai video models, ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Larus built a 3D camera-path animation with synchronized segment highlighting; the author proposes that city-scale 3D datasets could serve as ground-truth benchmarks for evaluating spatial reasoning in AI video models.</dd>
      <dt>Why interesting</dt>
      <dd>Synchronized camera-path highlighting is a practical previsualization technique directly applicable to XR scene layout and cinematic tooling in Unity.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can prototype a camera-path highlight visualizer as a scene-layout aid in the next XR or cinematic project.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2060373038982459741" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AckroseEdits</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 154 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AckroseEdits/status/2060352963986530678">View @AckroseEdits on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Vfx highlights from @StanBrowney's Fitness Island video 🏝️ -Premiere pro + After Effects -Higgsfield AI -Blender https://t.co/FleURGsWbG”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A VFX creator shares a breakdown of effects made for a fitness YouTube video using Premiere Pro, After Effects, Higgsfield AI, and Blender.</dd>
      <dt>Why interesting</dt>
      <dd>Higgsfield AI paired with Blender in a real production pipeline shows a practical hybrid workflow for small teams doing motion or cinematic content.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can test Higgsfield AI alongside existing Blender pipelines for XR/game trailers or e-learning video production.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AckroseEdits/status/2060352963986530678" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
