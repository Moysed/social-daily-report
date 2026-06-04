---
type: social-topic-report
date: '2026-06-04'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-04T03:41:42+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 43
salience: 0.62
sentiment: positive
confidence: 0.58
tags:
- gaussian-splatting
- photogrammetry
- blender
- shaders
- ai-asset-generation
- xr-pipeline
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2061575218749943808/img/_SuSRfmf6GjLa7q2.jpg
---

# 3D & Graphics — 2026-06-04

## TL;DR
- SuperSplat (free, open source) streamed a 24-million-Gaussian scan live to a web browser with near-instant load [3], the strongest signal that Gaussian Splatting is moving toward web/XR delivery.
- Multiple Gaussian Splatting advances landed at once: HiGS hierarchical real-time rendering [20], FreeStreamGS online feed-forward splatting from unposed streaming inputs [31], TripoSplat image-to-3D with adjustable Gaussian count [32], plus a built real-estate pre-construction walkthrough [12].
- Free in-engine Unity tooling: VFX Texture Lab does mask cleanup, gradient mapping, and channel packing without leaving Unity [4].
- Photogrammetry kept maturing — a scan-to-game-asset pipeline via decimation/re-UV/bake [2] and KIRI Engine's Featureless Object Scan Mode for glossy, monochrome surfaces [14] — alongside a complaint that photogrammetry inflates games to 130GB [8].
- Unreal Engine 5.8 adds Niagara memory and speed optimizations for larger real-time VFX simulations [11]; AI asset generators (Meshy style-consistent towns [22], a one-prompt 3D world agent [28]) continued posting demos.

## What happened
The dominant thread was 3D Gaussian Splatting. SuperSplat showed a 24M-Gaussian scan streaming live to a browser with near-instant load [3], a real-estate developer rebuilt a project as a pre-construction splat walkthrough [12], and research arrived in parallel: HiGS for hierarchical real-time rendering [20], FreeStreamGS for online feed-forward splatting from unposed streaming inputs [31], and TripoSplat for controllable single-image-to-3D Gaussians [32]. A splatting talk also ran at Techweek [30]. Separately, an AI camera-path/trajectory trend spread widely [1][9].

## Why it matters (reasoning)
For a studio shipping Unity games and XR/VR, the web-streaming splat demo [3] matters because it points at delivering captured environments through a browser rather than a heavy native build — relevant to both the XR portfolio and web/mobile delivery, and the real-estate walkthrough [12] is a concrete commercial template. The cluster of splatting papers [20][31][32] suggests capture and rendering are both improving at once, lowering the cost of turning real scenes into navigable assets. On the production side, free in-engine tools (VFX Texture Lab [4]) and photogrammetry refinements [2][14] reduce manual asset cleanup, while the 130GB complaint [8] is a real second-order cost: scanned detail inflates build size, which hurts mobile and web targets and forces decimation/baking discipline [2]. AI asset generators [22][28][32] promise speed but the items are demos, not verified production results.

## Possibility
Likely: Gaussian Splatting continues toward web-delivered XR/visualization use, given a working 24M-Gaussian browser stream [3], a shipped real-estate case [12], and convergent research [20][31]. Plausible: image/prompt-to-3D (TripoSplat [32], Meshy [22], one-prompt world agent [28]) becomes usable for greyboxing and background props, but control and quality remain unproven from demo clips alone. Plausible: build-size pressure pushes teams toward leaner, baked photogrammetry pipelines rather than raw scans [2][8]. Unlikely on this evidence: AI 3D agents replace authored environment work near-term — claims like 'entire worlds from one prompt' [28] are unverified marketing.

## Org applicability — NDF DEV
1) Evaluate SuperSplat for a browser-based XR/visualization demo — it is free and open source and already streams large scans to the web [3][12] (effort: med). 2) Add VFX Texture Lab to the Unity pipeline for mask/channel-pack/gradient work in-engine [4] (effort: low). 3) Adopt the scan-to-game-asset routine (decimation, new UVs, bake) as standard to control build size for mobile/web, directly answering the 130GB concern [2][8] (effort: med). 4) Trial KIRI's Featureless Object Scan Mode where props are glossy/monochrome and normal photogrammetry fails [14] (effort: low). 5) For VR avatars, the VRoid+Blender route with 52 ARKit blendshapes and Perfect Sync is a ready reference [26] (effort: med). Skip for now: Unreal 5.8 Niagara changes unless an Unreal project is active [11]; the generative-media-in-film debate [18][35][16][23]; Apple U1/spatial-anchor speculation [15][29] — interesting but not actionable today. Treat one-prompt 3D world claims [28] as demos, not procurement decisions.

## Signals to Watch
- Whether SuperSplat-style web splat streaming gets a stable export/runtime path into Unity or WebGL viewers [3].
- TripoSplat and similar image-to-3D tools producing clean, riggable topology rather than raw Gaussians [32].
- KIRI's featureless-object scanning quality on production props [14].
- Build-size pushback shaping texture/resolution budgets in scanned-asset pipelines [2][8].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^4284 c67 | [Well that escalated quickly 😂 Insane camera path generation harry! https://t.co/](https://x.com/bilawalsidhu/status/2061886480847450588) |
| x | JasozzGames | ^981 c9 | [I'm really addicted to this 3D-scan-to-game-ready-asset pipeline! Just a few rou](https://x.com/JasozzGames/status/2062165225588089172) |
| x | playcanvas | ^526 c17 | [🚀 Major upgrades just landed in SuperSplat, the free and open source platform fo](https://x.com/playcanvas/status/2062165374120894862) |
| x | jettelly | ^332 c0 | [Technical Artist Ken Deng released VFX Texture Lab, a free Unity tool that lets ](https://x.com/jettelly/status/2061749670075150362) |
| x | TOAnimate_ | ^259 c1 | [Little tip that might save you: Don’t skip the basics if you don’t want everythi](https://x.com/TOAnimate_/status/2061810071927923134) |
| x | jettelly | ^230 c1 | [Developer jakubiee made this simple head shader for Unreal Engine 5, experimenti](https://x.com/jettelly/status/2062081858154750016) |
| x | VFX_Therapy | ^208 c2 | [Amazing procedurally generated real-time cloud shader created by @HugoChenin. #u](https://x.com/VFX_Therapy/status/2062231883384258909) |
| x | TheVicious_One | ^208 c20 | [Hot take incoming: Photogrammetry is why games are 130GB We don't need to see la](https://x.com/TheVicious_One/status/2062204594185228557) |
| x | AIWarper | ^194 c19 | [Fun fact - I started this entire trend after seeing a fantastic post by @bilawal](https://x.com/AIWarper/status/2061884417757544600) |
| x | SD_F111 | ^176 c6 | [Niko N model update!! 3D work/rigging is done now to clean up weights and UV! Ni](https://x.com/SD_F111/status/2061918040850121207) |
| x | RedefineFX | ^170 c3 | [Unreal Engine 5.8 brings memory and speed optimizations for Niagara, allowing fo](https://x.com/RedefineFX/status/2062144965472313446) |
| x | AurelienCa80656 | ^135 c7 | [A real estate project recreated in Gaussian Splatting. Future buyers can freely ](https://x.com/AurelienCa80656/status/2062053609102008532) |
| x | K_enzo1 | ^104 c6 | [Practice VFX/Anim: Me Port: https://t.co/xnTwH5Im8S #RobloxDev #robloxvfx #MoonA](https://x.com/K_enzo1/status/2061964402270597596) |
| x | KIRI_Engine_App | ^101 c2 | [Featureless objects break most photogrammetry pipelines. Glossy, monochrome, no ](https://x.com/KIRI_Engine_App/status/2062089405741854822) |
| x | mweinbach | ^83 c6 | [I keep thinking about Apple’s U1 chip and the idea of understanding 3D space wit](https://x.com/mweinbach/status/2062255347608236229) |
| x | FourBeats265635 | ^81 c2 | [@YottaMindset @mnolangray “Closely connected” seems like a real stretch. Being a](https://x.com/FourBeats265635/status/2061669439620215273) |
| x | cgboost | ^80 c0 | [Learn how Martin Klekner made this sequence in Blender on our YouTube Channel. h](https://x.com/cgboost/status/2061748624178999569) |
| x | bilawalsidhu | ^79 c12 | [I see videos like this and get excited… it’s the old guard embracing new tech. T](https://x.com/bilawalsidhu/status/2061811752786944074) |
| x | FlippedNormals | ^70 c0 | [This stylized water shader by Casey Sheep is included in our new Blender Add-Ons](https://x.com/FlippedNormals/status/2061810123350106393) |
| x | janusch_patas | ^53 c2 | [HiGS: A Hierarchical Rendering Architecture for Real-Time 3D Gaussian Splatting ](https://x.com/janusch_patas/status/2062064390136795517) |
| x | multimodalart | ^52 c5 | [Ideogram 4 not only revamped their model to the best they built yet, but also th](https://x.com/multimodalart/status/2062210597148930139) |
| x | MeshyAI | ^44 c4 | [Build a 3D tiny town, block by block. Meshy keeps the style consistent across as](https://x.com/MeshyAI/status/2062121498207563920) |
| x | Rahll | ^40 c2 | [I agree with your general sentiment, but to be clear, a lot of what you're descr](https://x.com/Rahll/status/2062272983499260229) |
| x | ushadersbible | ^38 c1 | [This outline technique is achieved using reflection. What's the difference? For ](https://x.com/ushadersbible/status/2061663479300296851) |
| x | cghow_ | ^37 c0 | [Shadow Binding Curse in Unreal Engine 5 Niagara https://t.co/MNIt02YoVO https://](https://x.com/cghow_/status/2061808463727239678) |
| x | kariha_moon5 | ^35 c0 | [Made in VRoid Studio x Blender. Includes: ✧ 5 default expressions ✧ Jacket toggl](https://x.com/kariha_moon5/status/2061812031339319493) |
| x | 3DxDEV7 | ^32 c0 | [Take a look at this 👀 A procedural robot character creator for Blender with pres](https://x.com/3DxDEV7/status/2062247832321417594) |
| x | heyrobinai | ^32 c6 | [NO WAY THIS 3D AGENT BUILDS ENTIRE WORLDS FROM ONE PROMPT.. 3D environment build](https://x.com/heyrobinai/status/2061840822656499739) |
| x | mweinbach | ^29 c2 | [You can then extend to an ecosystem. If you want to know where your AirTags are ](https://x.com/mweinbach/status/2062255381645074904) |
| x | RadianceFields | ^24 c0 | [I’m doing a talk tomorrow for @Techweek_ about gaussian splatting. Come by if yo](https://x.com/RadianceFields/status/2061663277893972082) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4284 · 💬 67</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061886480847450588">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Well that escalated quickly 😂 Insane camera path generation harry! https://t.co/ML4I0e2J6m”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@bilawalsidhu reacts to a viral 3D demo showing notably automated camera path generation, linked video unspecified in post text but drew 4 k+ likes across the 3D/graphics community.</dd>
      <dt>Why interesting</dt>
      <dd>Camera path automation maps directly to Unity cutscene tooling, in-engine cinematics, and XR flythrough authoring — high-engagement signals the demo is worth reviewing.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Open the linked video and assess whether the camera path technique fits the Unity or XR pipeline before deciding if it warrants a deeper tool evaluation.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061886480847450588" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@JasozzGames</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 981 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/JasozzGames/status/2062165225588089172">View @JasozzGames on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm really addicted to this 3D-scan-to-game-ready-asset pipeline! Just a few rounds of decimation, new UVs, and then bake the details #gamedev #blender https://t.co/bAmx8JlHlM”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A gamedev shares a photogrammetry-to-game-ready workflow in Blender: 3D scan → polygon decimation → UV remap → detail bake, producing optimised real-world assets.</dd>
      <dt>Why interesting</dt>
      <dd>This pipeline cuts manual modelling time for props and environments — directly applicable to Unity games and XR scenes that need real-world geometry at low poly counts.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/XR team can test this Blender pipeline on one scanned environment prop and benchmark the time against manual modelling.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/JasozzGames/status/2062165225588089172" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@playcanvas</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 526 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/playcanvas/status/2062165374120894862">View @playcanvas on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚀 Major upgrades just landed in SuperSplat, the free and open source platform for 3D Gaussian splatting. Here is a 24-MILLION-Gaussian scan streaming live to a web browser. Near instant load time. Sol”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>SuperSplat (PlayCanvas's open-source Gaussian splatting tool) shipped a compute-based WebGPU renderer with automatic LOD streaming, hitting 60 fps on a 24M-Gaussian scene with near-instant browser load.</dd>
      <dt>Why interesting</dt>
      <dd>WebGPU Gaussian splatting at 60 fps in-browser opens a practical path for photorealistic 3D environments in web XR or e-learning projects without native plugins.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a test capture through SuperSplat's WebGPU renderer to evaluate fit for the studio's web XR or e-learning 3D scene pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/playcanvas/status/2062165374120894862" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 332 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2061749670075150362">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Technical Artist Ken Deng released VFX Texture Lab, a free Unity tool that lets artists make common texture edits, like mask cleanup, gradient mapping, and channel packing, without leaving the engine.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Ken Deng released VFX Texture Lab, a free Unity Editor tool for in-engine texture ops: mask cleanup, gradient mapping, and channel packing — no external app needed.</dd>
      <dt>Why interesting</dt>
      <dd>Cuts the Photoshop/Substance round-trip for VFX artists; useful for any Unity team doing real-time effects or stylized visuals.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team should install VFX Texture Lab and test it on current VFX asset workflows to see if it replaces any external texture prep steps.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2061749670075150362" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TOAnimate_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 259 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TOAnimate_/status/2061810071927923134">View @TOAnimate_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Little tip that might save you: Don’t skip the basics if you don’t want everything to feel confusing later 😹 Learn the basics so your rigs don’t break later #toanimate #rigging #blender https://t.co/I”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@TOAnimate_ posts a short Blender rigging tip reminding animators to learn fundamentals before advancing, with a linked video example.</dd>
      <dt>Why interesting</dt>
      <dd>Relevant to any team member doing Blender character work for Unity or XR pipelines — broken rigs waste export time.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Share this clip in the studio's art channel as a quick reference for junior 3D artists working on rigged assets.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TOAnimate_/status/2061810071927923134" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 230 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2062081858154750016">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer jakubiee made this simple head shader for Unreal Engine 5, experimenting with ambient occlusion to create more interesting facial shading. 🎭 See more: https://t.co/3GacKh8pFn #UnrealEngine #”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer jakubiee built a custom head shader in Unreal Engine 5 that uses ambient occlusion to improve facial shading quality beyond the default material.</dd>
      <dt>Why interesting</dt>
      <dd>A lightweight shader experiment showing how a single AO tweak meaningfully improves character face rendering — directly applicable to any UE5 character project.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can review the linked shader breakdown and test an equivalent ambient occlusion approach on character faces in current or upcoming projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2062081858154750016" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 208 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2062231883384258909">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazing procedurally generated real-time cloud shader created by @HugoChenin. #unreal #gamedev https://t.co/5cVXjkgd7J”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Hugo Chenin published a real-time procedurally generated cloud shader for Unreal Engine, demonstrated in a short video clip.</dd>
      <dt>Why interesting</dt>
      <dd>Procedural cloud shaders reduce reliance on static skyboxes and the technique translates directly to Unity outdoor and VR scene work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/XR team can study Chenin's shader architecture as a reference when building dynamic sky systems for outdoor or VR scenes.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2062231883384258909" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheVicious_One</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 208 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheVicious_One/status/2062204594185228557">View @TheVicious_One on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hot take incoming: Photogrammetry is why games are 130GB We don't need to see laundry in 4k”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer argues that photogrammetry-based 4K asset scanning is the primary driver behind bloated game install sizes reaching 130 GB.</dd>
      <dt>Why interesting</dt>
      <dd>Raises a real production trade-off: ultra-high-res scanned assets vs. download/storage cost, relevant when scoping Unity asset pipelines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When scoping 3D projects, define a texture resolution budget early and evaluate whether photogrammetry assets need LOD compression before shipping.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheVicious_One/status/2062204594185228557" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
