---
type: social-topic-report
date: '2026-06-11'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-11T03:50:55+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 58
salience: 0.7
sentiment: positive
confidence: 0.6
tags:
- gaussian-splatting
- apple-maps
- xr
- luma-ray3
- blender
- ai-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2064357961254793216/img/mePCpXHgLsopIcYe.jpg
---

# 3D & Graphics — 2026-06-11

## TL;DR
- Apple is rolling 3D Gaussian Splatting into Apple Maps Flyover (300+ cities) this fall, live now in the visionOS 27 / developer beta; multiple observers say it shipped splats in maps before Google [11][21][25][28][38][41][45].
- It appears to be a hybrid of photogrammetry meshes + Gaussian splats, and the visionOS sample runs on-device only (not simulator), with aggressive culling that fades splats up close — a problem for interiors [32][45][47].
- Luma Labs launched Ray3.2 with a developer API: 16-keyframe per-clip control, Modify Video V2 (up to 20s at 1080p), native HDR and 16-bit EXR export for compositing in Resolve/Nuke [1][15][33][52][54].
- Splat tooling is maturing for production pipelines: Spark fuses splats + mesh in THREE.js for cross-device web rendering [40]; ColmapView v0.7 adds 3DGS QA [16]; Alibaba's ABot-Earth 0.5 generates splat environments from satellite imagery under 10 min/km² [17].
- AI asset/sim generation is showing up in graphics work: Claude 'Fable/Mythos' one-shotted a city-block traffic simulator [2] and built Spawn 5.0 over 1,687 prompts [6]; Meshy generated a full arcade scene from one chat [57].

## What happened
The dominant story is Apple adding 3D Gaussian Splatting to Apple Maps, surfaced at WWDC and now in the developer beta / visionOS 27, covering Flyover's 300+ cities this fall [11][21][28][38][41]. Inspection suggests a photogrammetry-mesh + splat hybrid built from oblique aerial imagery [38][45]. Caveats are already visible: splats render on-device but not in the simulator [47], and Vision Pro culling fades splats as you approach, blocking interior use [32]. Google is noted as having shipped splats earlier but only inside immersive/indoor view [25].

## Why it matters (reasoning)
Two threads converge. First, Gaussian Splatting is moving from research demos into shipped consumer and developer products (Apple Maps [11], THREE.js via Spark [40], satellite-to-splat generation [17], smartphone product capture via Supra [46]), with QA tooling appearing [16] — that lowers the cost of photoreal 3D capture for XR and web. For a studio doing XR/VR and web/mobile, the relevant unlock is splat+mesh fusion in standard web renderers [40] and on-device Vision Pro support [45], though the culling and simulator limits [32][47] mean current Apple splats are sightseeing-grade, not yet interaction-grade for interiors. Second, Luma's Ray3.2 [1][54] and AI scene/asset generators [2][57] push generative media deeper into VFX/asset pipelines; the practical hook is EXR/HDR export so AI output composites alongside live plates [54], not the marketing claims. A trust caveat surfaced around a model silently altering output without informing the user [29], which matters for any pipeline depending on deterministic results.

## Possibility
Likely: Gaussian Splatting becomes a standard capture format for web/XR scene backdrops within the next year, given simultaneous shipping across Apple [11], THREE.js [40], and generation tools [17][26]. Plausible: Apple ships a first-class Vision Pro Maps/splat app, which several developers are explicitly asking for [21][55] — but the culling behavior [32] suggests interior-quality splats are not ready yet, so near-term use stays exterior/flyover. Plausible: AI video tools like Ray3.2 get adopted for previz and B-roll where EXR/HDR compositing is supported [54], rather than final hero shots. Unlikely near-term: one-shot AI scene generators [2][57] replace hand-authored asset pipelines for shipping game/XR builds — the demos are impressive but unverified for production constraints, and the output-manipulation concern [29] erodes trust. No source states numeric probabilities.

## Org applicability — NDF DEV
1) Evaluate Spark for splat+mesh in web/mobile XR experiences (low effort) — it targets the THREE.js stack the studio likely already uses and supports cross-device rendering [40]. 2) Pilot a smartphone-to-splat product/asset capture flow for client or game props using Supra/TripoSplat-style tools, with ColmapView for QA before ingest (med effort) [16][26][46]. 3) If a Vision Pro splat experience is on the roadmap, test now but design for exteriors only and verify on-device — note the simulator gap and close-range culling before committing [32][45][47]. 4) For any AI-video/VFX use, gate adoption on EXR/HDR export compatibility with your compositing tooling (low-med effort) [54]; treat one-shot scene generators [2][57] as previz only. Skip: Apple Maps splat integration as a dependency (consumer feature, not an SDK you build on) [11]; the off-topic political items [9][27]; vendor reframe/aspect-ratio claims [53][58] until tested. Drop any reliance on models that alter output silently until the behavior is clarified [29].

## Signals to Watch
- Whether Apple exposes splats via a developer SDK or keeps them locked to Maps — determines if the studio can build on it [21][55].
- Vision Pro splat culling behavior in future visionOS 27 betas — fixing close-range fade would open interior XR use [32].
- Spark's maturity for splat+mesh fusion in THREE.js as a web-XR delivery path [40].
- Generative splat-from-imagery (ABot-Earth) and one-chat asset tools (Meshy) for rapid environment prototyping [17][57].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | LumaLabsAI | ^3624 c36 | [Direction goes in. Cinema comes out. Ray3.2 is here → https://t.co/TuAuFhZDBn ht](https://x.com/LumaLabsAI/status/2064358414143143954) |
| x | bilawalsidhu | ^1876 c76 | [Just used claude fable (aka mythos) to create this city block simulator complete](https://x.com/bilawalsidhu/status/2064524211914223867) |
| x | ItzFAILURE | ^1675 c13 | [Added another whole 10 seconds! Next im adding the "first person" part... who co](https://x.com/ItzFAILURE/status/2064504962189492495) |
| x | luci_animates | ^490 c3 | [Mi Fu's model is available to download for GOO ENGINE (Blender) 4.4.3, check the](https://x.com/luci_animates/status/2064640462749855848) |
| x | sai_charan_md | ^463 c1 | [Iridescent Material Blender Tip! Follow for more. #b3d #blender #procedural http](https://x.com/sai_charan_md/status/2064658224440353124) |
| x | jsnnsa | ^250 c22 | [claude fable 5 is live. spawn 5.0 was built with it: 1,687 prompts, 102 sessions](https://x.com/jsnnsa/status/2064420561078693941) |
| x | StormcoreDev | ^178 c0 | [WIP for water spell "Hydro-Megia." We captured water particles from Blender in c](https://x.com/StormcoreDev/status/2064627351145865449) |
| x | suni_mlb | ^165 c6 | [Chrysalis V2 WIP (Made by Amal and me) 🦋 #mlbtwt #mlbs6spoilers I'll port it to ](https://x.com/suni_mlb/status/2064294999622078894) |
| x | sachin_inc | ^131 c7 | [The action of the Returning Officer, who is also the Secretary of the Madhya Pra](https://x.com/sachin_inc/status/2064727133411475762) |
| x | jettelly | ^130 c1 | [Technical artist Chintan Vadgama broke down a parametric lightning shader he mad](https://x.com/jettelly/status/2064226059176837462) |
| x | heyshrutimishra | ^125 c4 | [WOW. 😳 Apple just quietly won the 3D maps war at WWDC. Gaussian Splatting is com](https://x.com/heyshrutimishra/status/2064191739444043915) |
| x | delaigrodela | ^119 c1 | [Wednesday, coffee, game dev and intellectual exercises for your brain with Unrea](https://x.com/delaigrodela/status/2064667317636628828) |
| x | jettelly | ^114 c0 | [Ever wondered how to make a clean, stylized water pipeline VFX in Unity? Here’s ](https://x.com/jettelly/status/2064678973775155209) |
| x | RadianceFields | ^107 c7 | [In the summer of 2023, I cold emailed Jensen Huang and asked to capture a NeRF o](https://x.com/RadianceFields/status/2064766228866924681) |
| x | LumaLabsAI | ^105 c12 | [The Ray3.2 API runs cinematic-grade at scale and integrates into the products yo](https://x.com/LumaLabsAI/status/2064389582997897216) |
| x | YeheLiu | ^97 c4 | [Want to catch bad images in your SFM reconstruction? Introducing ColmapView v0.7](https://x.com/YeheLiu/status/2064450666567983306) |
| x | HuggingPapers | ^90 c2 | [Alibaba just released ABot-Earth 0.5 A generative 3D model that builds seamless ](https://x.com/HuggingPapers/status/2064582374315131295) |
| x | afrotron | ^89 c2 | [Rig is done just ironing out some kinks. I'll put it up on my gumroad later this](https://x.com/afrotron/status/2064789451839049861) |
| x | mattsmodel12 | ^89 c2 | [From dynamic textures to fully playable.. Tested the character’s movement, riggi](https://x.com/mattsmodel12/status/2064205785928708532) |
| x | DemNikoArt | ^87 c5 | [A small reminder, that this tutorial exists on my YouTube 🚲 And yes, at the end,](https://x.com/DemNikoArt/status/2064712809489879169) |
| x | bilawalsidhu | ^84 c3 | [Apple’s gaussian splat maps are rolling out on the developer beta! I hope they m](https://x.com/bilawalsidhu/status/2064494805023911966) |
| x | filicroval | ^72 c6 | [🤖time for another 4D tool! this tool turns videos into moving 3D places film a m](https://x.com/filicroval/status/2064731328210145625) |
| x | BiboPlayer | ^58 c10 | [I wanted to share how much money I've spent developing Nuclear Tycoon, because I](https://x.com/BiboPlayer/status/2064380780537610670) |
| x | GabrielAguiarFX | ^56 c1 | [Toxic Waterfall made with Niagara on Unreal Engine! ☢️ And published a tutorial ](https://x.com/GabrielAguiarFX/status/2064389240721387732) |
| x | bilawalsidhu | ^55 c6 | [ICYMI google's been shipping gaussian splats in maps for a while -- but tucked i](https://x.com/bilawalsidhu/status/2064187152930365502) |
| x | mishig25 | ^51 c4 | [Created gaussian splats website for famous Paris monuments. Connected my claude ](https://x.com/mishig25/status/2064304062263066653) |
| x | rmacdon627 | ^47 c1 | [✅ The SAVE America Act (proof of citizenship + photo ID for federal elections) i](https://x.com/rmacdon627/status/2064881931221602482) |
| x | DataChaz | ^42 c7 | [CAN WE TALK ABOUT HOW APPLE MAPS JUST CASUALLY DROPPED 3D GAUSSIAN SPLATTING BEF](https://x.com/DataChaz/status/2064248196906561859) |
| x | multimodalart | ^41 c4 | [this is very odd manipulating the output without informing the user is a terribl](https://x.com/multimodalart/status/2064426820380860881) |
| x | aidan_3d_art | ^39 c2 | [Meet my latest blender 3D character 👜 This is my first time creating a full body](https://x.com/aidan_3d_art/status/2064328659578544610) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LumaLabsAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3624 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LumaLabsAI/status/2064358414143143954">View @LumaLabsAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Direction goes in. Cinema comes out. Ray3.2 is here → https://t.co/TuAuFhZDBn https://t.co/nAMqwBvrAK”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Luma Labs released Ray3.2, an AI video generation model that takes directional prompts and outputs cinematic-quality footage.</dd>
      <dt>Why interesting</dt>
      <dd>A small studio can use Ray3.2 to prototype cinematic cutscenes or e-learning video segments without a full production crew.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a quick test with Ray3.2 on one Unity game or e-learning script to gauge output quality before adopting it in production.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LumaLabsAI/status/2064358414143143954" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1876 · 💬 76</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2064524211914223867">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just used claude fable (aka mythos) to create this city block simulator complete with multi-agent traffic, live detection boxes + tracks, and day to night cycle. And it just one shotted it. This is go”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Fable (codename Mythos) one-shot generated a city block simulator with multi-agent traffic, live bounding-box tracking, and a day-to-night lighting cycle.</dd>
      <dt>Why interesting</dt>
      <dd>One-shotting a multi-system real-time scene suggests Fable handles spatial and simulation code substantially better than prior Claude versions — directly relevant to rapid XR/game prototyping.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a multi-system Unity or XR scene prompt through Claude Fable to benchmark one-shot quality against the studio's current prototyping workflow.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2064524211914223867" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1675 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2064504962189492495">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Added another whole 10 seconds! Next im adding the &quot;first person&quot; part... who could she be singing to? 👀 Model: @Artstudious Rig: @cookie_sugar42 Shader: @LuminaryOfAges Textures: @Hiru3152 #RWBY #FND”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A hobbyist animator shared a 10-second WIP fan animation for RWBY built in Blender, crediting separate artists for the model, rig, shader, and textures.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ItzFAILURE/status/2064504962189492495" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@luci_animates</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 490 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/luci_animates/status/2064640462749855848">View @luci_animates on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mi Fu's model is available to download for GOO ENGINE (Blender) 4.4.3, check the thread below! Huge thanks to @BNBaku for rigging her, and 新杨XIYAG for providing the shader! #GooEngine #Blender https:/”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A rigged 3D character model of Mi Fu, with custom shaders, is now free to download for Goo Engine (Blender) 4.4.3.</dd>
      <dt>Why interesting</dt>
      <dd>A free, fully rigged anime-style character with shaders cuts setup time when the Unity or XR team needs a humanoid placeholder for prototyping.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Download the model as a placeholder asset for Unity or XR scene prototypes; export from Blender as FBX to bring the rig into Unity.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/luci_animates/status/2064640462749855848" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sai_charan_md</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 463 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sai_charan_md/status/2064658224440353124">View @sai_charan_md on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Iridescent Material Blender Tip! Follow for more. #b3d #blender #procedural https://t.co/T4xQn2SHuI”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender artist demonstrates a procedural iridescent material node setup that produces color-shifting surface effects without texture painting.</dd>
      <dt>Why interesting</dt>
      <dd>Procedural iridescent shaders in Blender serve as a solid reference for recreating the same effect in Unity Shader Graph or URP/HDRP for XR/game assets.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/XR team can study the node logic and port the iridescent effect to Shader Graph, or bake it as a texture atlas for mobile/XR performance targets.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sai_charan_md/status/2064658224440353124" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jsnnsa</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 250 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jsnnsa/status/2064420561078693941">View @jsnnsa on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“claude fable 5 is live. spawn 5.0 was built with it: 1,687 prompts, 102 sessions, my job shifted from architecture to judging taste. what we built, each of which would've been at least a month with a ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The creator of Spawn 5.0 used Claude Fable 5 across 102 sessions to ship a physics engine, clustered froxel lighting (1,000+ dynamic lights), realtime diffuse GI on WebGPU mobile, and million-particle GPU VFX in roughly one week.</dd>
      <dt>Why interesting</dt>
      <dd>The froxel lighting and WebGPU realtime GI techniques are directly applicable to the studio's Unity/XR and browser-based 3D work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The graphics team should pull Spawn 5.0's full changelog and shader architecture notes as concrete references before the next WebGPU or Unity VFX sprint.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jsnnsa/status/2064420561078693941" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@StormcoreDev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 178 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/StormcoreDev/status/2064627351145865449">View @StormcoreDev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“WIP for water spell &quot;Hydro-Megia.&quot; We captured water particles from Blender in combination of a customized Mesh distortion in unreal to make it! We'll show you more when other spells are done! #VFX #B”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An indie dev team used Blender particle sims baked as meshes, then drove mesh distortion in Unreal Engine to build a water spell VFX called 'Hydro-Megia.'</dd>
      <dt>Why interesting</dt>
      <dd>The Blender-to-Unreal pipeline for VFX is directly applicable to the studio's Unity/XR work — the same bake-then-distort approach works in Unity's VFX Graph.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test the same pipeline in Unity: bake a Blender water sim to a mesh sequence, then drive distortion via VFX Graph or a custom shader for spell effects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/StormcoreDev/status/2064627351145865449" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@suni_mlb</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 165 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/suni_mlb/status/2064294999622078894">View @suni_mlb on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Chrysalis V2 WIP (Made by Amal and me) 🦋 #mlbtwt #mlbs6spoilers I'll port it to Unreal once I finish rigging https://t.co/uV9qKABwdD”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An artist duo shares a WIP 3D character model ('Chrysalis V2') from the Miraculous Ladybug fandom, noting they plan to port it to Unreal Engine after rigging is complete.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/suni_mlb/status/2064294999622078894" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
