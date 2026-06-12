---
type: social-topic-report
date: '2026-06-12'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-12T03:34:21+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 51
salience: 0.68
sentiment: mixed
confidence: 0.58
tags:
- gaussian-splatting
- xr
- visionos
- threejs
- blender
- ai-3d-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065109409844334592/img/OxNFlG_QeTBaXhVj.jpg
---

# 3D & Graphics — 2026-06-12

## TL;DR
- Gaussian Splatting is converging across major platforms in one news cycle: Apple visionOS 27 reportedly combines photogrammetry meshes + splats in Apple Maps [21], Alibaba's ABot-Earth 0.5 builds 3DGS environments from satellite imagery at under 10 min/km² [8], and Spark fuses splats with meshes in the same THREE.js scene [29].
- Radiance-field/volumetric capture from multi-camera sports rigs went viral: a point-of-view 3D reconstruction of OG Anunoby's tip-in scored 6112 [1], built from broadcast/Hawkeye-style sensor fusion [46][47].
- Research is lowering the capture barrier: Wild3R does feed-forward 3DGS from unconstrained sparse photos via an AnySplat finetune [40], and a PyTorch abstraction scales splatting across multiple GPUs [25].
- Apple is opening visionOS 27 + Reality Composer Pro 3 APIs to developers [23], but native splat culling fades scenes when you get close — a real blocker for interiors [22].
- Traditional DCC pipeline activity stayed steady: Houdini 22 keynote lands June 17 [27], Unreal 5.8 Niagara fluids run smoother [26], and AI asset tools (Meshy [48], Claude Fable 5 [32]) claim chat-to-rigged-mesh.

## What happened
The day's strongest cluster is 3D Gaussian Splatting (3DGS) appearing simultaneously across platforms and research. Apple's visionOS 27 reportedly renders Apple Maps with photogrammetry meshes plus Gaussian splats [21], with developers noting new visionOS 27 / Reality Composer Pro 3 APIs but criticizing aggressive splat culling at close range [22][23]. Alibaba released ABot-Earth 0.5, generating 3DGS environments from satellite imagery for real-time web maps [8]. Spark integrates 3DGS into the THREE.js pipeline, mixing splat and mesh objects cross-device [29]. Gracia VR and Meta Reality Labs stress-tested splatting and volumetric video [16]. On the research side, Wild3R produces feed-forward 3DGS from sparse, unconstrained photos [40], and a multi-GPU PyTorch abstraction scales reconstruction [25]; a separate tool rebuilds moving scenes as navigable 4D/dynamic splats from video [17].

## Why it matters (reasoning)
The signal is breadth, not a single launch: splatting is showing up in a consumer OS [21], a hyperscaler's mapping product [8], a mainstream web renderer [29], and a corporate research lab [16] in the same window — that pattern usually precedes a capture-and-delivery format becoming standard rather than experimental. Two second-order effects matter for an XR/web studio. First, splat-plus-mesh fusion [29] and feed-forward capture from casual photos [40] cut the asset-production cost of photoreal environments, which competes with manual photogrammetry-to-mesh workflows. Second, the limitations are equally informative: Vision Pro culling breaks interior use cases [22] and a THREE.js GTA-style scene still shimmers on complex materials [24], so the tech is production-viable for some scenes and not others. The viral sports reconstruction [1][46][47] shows the same capture techniques riding existing camera infrastructure, but that depends on multi-camera rigs most studios don't have.

## Possibility
Likely: 3DGS settles in as a delivery format for web and XR scenes over the next year, given native OS support [21][23], a mainstream THREE.js path [29], and maturing capture research [40][25]. Plausible: hybrid splat+mesh pipelines feed real engines for environment backdrops while interactive geometry stays mesh-based [29], because pure-splat interaction and culling are still rough [22]. Plausible but unproven: chat-to-asset AI tools [48][32] reach shippable quality — current evidence is marketing and WIP with visible artifacts [24]. Unlikely near-term: close-range splat interiors on Vision Pro without an Apple culling fix [22].

## Org applicability — NDF DEV
Do: (1) Prototype a walkable splat scene in the browser with Spark/THREE.js to evaluate it for web and XR experiences — low effort, directly matches the studio's web 3D stack [29][45]. (2) Trial AI asset generation (Meshy, Claude Fable 5) on a throwaway edutech/game prototype to measure quality and editability before trusting it in production — low effort [48][32]. (3) Test the Real Fake Interiors Unity tool for cheap furnished-room-behind-window effects in mobile/Unity titles — low effort, a known performance trick [12]. (4) Grab the Unity stylized water shader and the Editor mask/channel-packing tool to speed tech-art iteration — low effort [6][20]. (5) If Vision Pro is on the roadmap, evaluate visionOS 27 splat support but plan around the close-range culling limit for interiors — med effort [21][22][23]. Watch, don't act yet: Houdini 22 features (keynote June 17) [27] and multi-GPU splat reconstruction [25] — high effort to adopt. Skip: broadcast-grade sports reconstruction [1] (no camera infrastructure), NFT/crypto 3D art [42], and the culture-war/asset-discourse threads [14][30][39].

## Signals to Watch
- Houdini 22 keynote June 17 — check for procedural/splat or simulation features relevant to asset pipelines [27].
- Apple visionOS 27 splat culling behavior — whether Apple loosens close-range fade decides interior XR viability [22][23].
- Spark THREE.js splat+mesh fusion maturity — the most directly usable path for the studio's web stack [29].
- Feed-forward splatting from casual photos (Wild3R/AnySplat) — lowers capture cost if it generalizes beyond the new dataset [40].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^6112 c47 | [OG Anunoby is too sick. Here is the full point-of-view 3d reconstruction of his ](https://x.com/bilawalsidhu/status/2065109650475712908) |
| x | sai_charan_md | ^584 c1 | [Iridescent Material Blender Tip! Follow for more. #b3d #blender #procedural http](https://x.com/sai_charan_md/status/2064658224440353124) |
| x | luci_animates | ^510 c3 | [Mi Fu's model is available to download for GOO ENGINE (Blender) 4.4.3, check the](https://x.com/luci_animates/status/2064640462749855848) |
| x | IlirAliu_ | ^492 c1 | [One professor at the University of Bonn quietly put his entire robotics curricul](https://x.com/IlirAliu_/status/2064979957009285375) |
| x | StormcoreDev | ^432 c0 | [WIP for water spell "Hydro-Megia." We captured water particles from Blender in c](https://x.com/StormcoreDev/status/2064627351145865449) |
| x | jettelly | ^216 c0 | [Ever wondered how to make a clean, stylized water pipeline VFX in Unity? Here’s ](https://x.com/jettelly/status/2064678973775155209) |
| x | afrotron | ^206 c2 | [Rig is done just ironing out some kinks. I'll put it up on my gumroad later this](https://x.com/afrotron/status/2064789451839049861) |
| x | HuggingPapers | ^204 c3 | [Alibaba just released ABot-Earth 0.5 A generative 3D model that builds seamless ](https://x.com/HuggingPapers/status/2064582374315131295) |
| x | delaigrodela | ^154 c1 | [Wednesday, coffee, game dev and intellectual exercises for your brain with Unrea](https://x.com/delaigrodela/status/2064667317636628828) |
| x | sachin_inc | ^148 c9 | [The action of the Returning Officer, who is also the Secretary of the Madhya Pra](https://x.com/sachin_inc/status/2064727133411475762) |
| x | RadianceFields | ^146 c8 | [In the summer of 2023, I cold emailed Jensen Huang and asked to capture a NeRF o](https://x.com/RadianceFields/status/2064766228866924681) |
| x | 80Level | ^136 c1 | [Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo t](https://x.com/80Level/status/2065109302562422981) |
| x | RyanLykos | ^132 c1 | [Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv](https://x.com/RyanLykos/status/2065189214413611291) |
| x | zephyyy7 | ^120 c4 | [@Will40746376 @Dexerto funny how last game this same crowd swore "no real woman ](https://x.com/zephyyy7/status/2065112542448374086) |
| x | bilawalsidhu | ^103 c13 | [Wow, this is really cool. Has anyone productized this? I would love to be able t](https://x.com/bilawalsidhu/status/2064865579547193788) |
| x | gracia_vr | ^102 c2 | [We teamed up with researchers at Meta @RealityLabs to stress-test what's actuall](https://x.com/gracia_vr/status/2065106030539997345) |
| x | filicroval | ^101 c7 | [🤖time for another 4D tool! this tool turns videos into moving 3D places film a m](https://x.com/filicroval/status/2064731328210145625) |
| x | DemNikoArt | ^100 c5 | [A small reminder, that this tutorial exists on my YouTube 🚲 And yes, at the end,](https://x.com/DemNikoArt/status/2064712809489879169) |
| x | rmacdon627 | ^96 c3 | [✅ The SAVE America Act (proof of citizenship + photo ID for federal elections) i](https://x.com/rmacdon627/status/2064881931221602482) |
| x | VFX_Therapy | ^76 c0 | [Tired of opening Photoshop for every tiny mask tweak? @KenDeng built a Unity Edi](https://x.com/VFX_Therapy/status/2065035196358094848) |
| x | Azadux | ^64 c5 | [I believe that Apple Maps in visionOS 27 is a combination of photogrammetry mesh](https://x.com/Azadux/status/2064876849252225246) |
| x | iBrews | ^62 c3 | [Apple's new gaussian splatting support is cool, but the culling is kind of ridic](https://x.com/iBrews/status/2064836100720394464) |
| x | xchester16 | ^59 c1 | [After spending some time with the new visionOS 27 APIs and Reality Composer Pro ](https://x.com/xchester16/status/2064900511116185939) |
| x | drashyakuruwa | ^56 c8 | [A minor graphics update to the initial version of my GTA V-style game with @thre](https://x.com/drashyakuruwa/status/2065055670496276601) |
| x | janusch_patas | ^56 c1 | [A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting Abstract (excerp](https://x.com/janusch_patas/status/2064965130413048221) |
| x | RedefineFX | ^51 c2 | [Falcon 9 landing real-time VFX in Unreal 5.8, continuing with my space explorati](https://x.com/RedefineFX/status/2065047711477301342) |
| x | sidefx | ^50 c0 | [Houdini 22 launches in London next week! Join us at Curzon Soho Cinema for an ex](https://x.com/sidefx/status/2065141618509005226) |
| x | multimodalart | ^47 c2 | [folks @liquidai trained a specialist tiny model to do one thing rly well: extrac](https://x.com/multimodalart/status/2064864942180679962) |
| x | GithubProjects | ^41 c3 | [Spark integrates 3D Gaussian splatting with the THREE.js rendering pipeline for ](https://x.com/GithubProjects/status/2064807319255515476) |
| x | fistandilus12 | ^40 c2 | [Funny how people who spent 20 years defending Photoshop, CGI, motion capture, pr](https://x.com/fistandilus12/status/2064943228340535490) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6112 · 💬 47</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065109650475712908">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“OG Anunoby is too sick. Here is the full point-of-view 3d reconstruction of his winning tip-in from the Knicks game last night. You can literally relive it from his perspective. Built with viewpoint p”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Viewpoint Pro used stadium tracking cameras and Unreal Engine to generate a full POV 3D reconstruction of OJ Anunoby's game-winning tip-in from the Knicks game.</dd>
      <dt>Why interesting</dt>
      <dd>Demonstrates a live multi-camera volumetric capture pipeline feeding Unreal Engine at sports-broadcast scale — a real production XR reference.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Research Viewpoint Pro's camera-to-engine pipeline to benchmark how a similar multi-camera-to-game-engine workflow could apply to the studio's XR productions.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2065109650475712908" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sai_charan_md</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 584 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sai_charan_md/status/2064658224440353124">View @sai_charan_md on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Iridescent Material Blender Tip! Follow for more. #b3d #blender #procedural https://t.co/T4xQn2SHuI”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender tip demonstrates how to build a procedural iridescent material using node-based shading, shared as a short video tutorial.</dd>
      <dt>Why interesting</dt>
      <dd>Procedural iridescent shaders authored in Blender can be baked and exported as PBR textures directly usable in Unity and XR scenes.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The 3D team can study the node graph and apply the same iridescent technique when authoring stylized assets for Unity or XR builds.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sai_charan_md/status/2064658224440353124" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@luci_animates</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 510 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/luci_animates/status/2064640462749855848">View @luci_animates on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mi Fu's model is available to download for GOO ENGINE (Blender) 4.4.3, check the thread below! Huge thanks to @BNBaku for rigging her, and 新杨XIYAG for providing the shader! #GooEngine #Blender https:/”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A rigged Mi Fu character model with custom shaders is now available as a free download for Goo Engine (Blender fork) 4.4.3, shared by the community.</dd>
      <dt>Why interesting</dt>
      <dd>Free rigged anime-style character with shaders is a ready-made asset for any team prototyping stylized 3D or testing Goo Engine's NPR rendering pipeline.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity or XR team can import this model to benchmark stylized NPR shading workflows before committing to a Goo Engine or Blender-to-Unity pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/luci_animates/status/2064640462749855848" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IlirAliu_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 492 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IlirAliu_/status/2064979957009285375">View @IlirAliu_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One professor at the University of Bonn quietly put his entire robotics curriculum on YouTube: SLAM. Sensor fusion. State estimation. Probabilistic robotics. Self-driving cars. Motion planning. Photog”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Cyrill Stachniss, Univ. of Bonn robotics professor, has published his full university curriculum on YouTube free — SLAM, photogrammetry, sensor fusion, motion planning, each as a complete playlist.</dd>
      <dt>Why interesting</dt>
      <dd>The photogrammetry and SLAM playlists are directly applicable to XR/VR 3D reconstruction and AR spatial tracking work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Point the XR/VR team to the photogrammetry and SLAM playlists as reference for any spatial mapping or 3D scanning feature work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IlirAliu_/status/2064979957009285375" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@StormcoreDev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 432 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/StormcoreDev/status/2064627351145865449">View @StormcoreDev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“WIP for water spell &quot;Hydro-Megia.&quot; We captured water particles from Blender in combination of a customized Mesh distortion in unreal to make it! We'll show you more when other spells are done! #VFX #B”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An indie dev team combined Blender particle simulations with custom mesh distortion in Unreal Engine to produce a water spell VFX effect called 'Hydro-Megia'.</dd>
      <dt>Why interesting</dt>
      <dd>The Blender-to-Unreal pipeline for stylized spell VFX is a practical workflow applicable to the studio's Unity/XR game projects as a cross-tool reference.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can prototype a similar water VFX by exporting Blender particle caches as alembic and driving mesh distortion via a custom shader graph.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/StormcoreDev/status/2064627351145865449" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 216 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2064678973775155209">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ever wondered how to make a clean, stylized water pipeline VFX in Unity? Here’s a simple and quick technique you can try! 🌊 Learn more about tech art, shader &amp;amp; tools ✨ https://t.co/gPPcuZDuFX #uni”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Jettelly shares a stylized water pipeline VFX technique for Unity, with a linked breakdown covering the shader and tech art approach.</dd>
      <dt>Why interesting</dt>
      <dd>A ready-to-study shader technique directly applicable to Unity game projects that need stylized fluid or pipe VFX.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can reference this breakdown when building environment or gameplay VFX that involves liquid flow or pipeline visuals.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2064678973775155209" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@afrotron</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 206 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/afrotron/status/2064789451839049861">View @afrotron on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Rig is done just ironing out some kinks. I'll put it up on my gumroad later this month #blender #rigging #anissa #invincible https://t.co/CGVgJltzLt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An independent Blender artist finished rigging a fan-made character (Anissa from Invincible) and plans to release it on Gumroad later this month.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/afrotron/status/2064789451839049861" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HuggingPapers</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 204 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HuggingPapers/status/2064582374315131295">View @HuggingPapers on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Alibaba just released ABot-Earth 0.5 A generative 3D model that builds seamless environments from satellite imagery in under 10 minutes per km². It uses 3D Gaussian Splatting for real-time web maps an”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Alibaba released ABot-Earth 0.5, a generative 3D model that converts satellite imagery into navigable 3D environments via 3D Gaussian Splatting in under 10 minutes per km².</dd>
      <dt>Why interesting</dt>
      <dd>3D Gaussian Splatting at geographic scale is directly applicable to the studio's XR/VR outdoor scenes and Unity-based simulation work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's XR/VR team should test ABot-Earth 0.5 as a satellite-to-scene pipeline for large-scale outdoor environment generation.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HuggingPapers/status/2064582374315131295" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
