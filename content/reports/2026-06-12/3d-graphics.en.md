---
type: social-topic-report
date: '2026-06-12'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-12T15:38:38+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 46
salience: 0.58
sentiment: mixed
confidence: 0.6
tags:
- gaussian-splatting
- visionos
- unity
- threejs
- ai-3d
- procedural
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065400058565079040/img/K_mHR8IT0VE_qxwT.jpg
---

# 3D & Graphics — 2026-06-12

## TL;DR
- Gaussian splatting is the dominant cluster today: Apple visionOS 27 / Vision Pro adds native splat support [17], Apple Maps appears to fuse photogrammetry meshes with splats [20], and Spark brings 3D GS into the three.js pipeline alongside meshes [26].
- Apple is exposing more visionOS 27 and Reality Composer Pro 3 APIs to developers [19], but Vision Pro splat culling fades splats at close range, which breaks interior/walkthrough use [17].
- Research is lowering GS capture cost: Wild3R does feed-forward GS from unconstrained sparse photo collections [32], and a multi-GPU PyTorch GS abstraction scales reconstruction to larger scenes/higher resolution [18].
- Unity asset tooling: Real Fake Interiors is a baking tool + shader that fakes a furnished room behind a flat window [5]; a Unity Editor tool handles masks, channel packing, and ramps without Photoshop round-trips [12].
- AI-assisted 3D and DCC releases: Claude Fable 5 reportedly generates rigged meshes with clean hierarchy and LLM-readable metadata [31] and drives a three.js GTA-style scene (with shimmering still unsolved) [23]; Houdini 22 keynote is June 17 in London [11] and Unreal 5.8 reports smoother Niagara fluids [22].

## What happened
The strongest signal is a Gaussian splatting / radiance field cluster spanning platforms and pipelines. Apple added GS support in Vision Pro but with aggressive close-range culling that degrades interiors [17]; observers infer Apple Maps in visionOS 27 combines photogrammetry meshes with splats [20], and visionOS 27 plus Reality Composer Pro 3 are said to open more platform internals to developers [19]. On the web, Spark integrates 3D GS into the three.js render pipeline and mixes splat and mesh objects in one scene [26]. Research items push capture and scale: Wild3R is feed-forward GS from sparse, unconstrained photos [32], and a multi-GPU PyTorch abstraction scales GS reconstruction [18]; a SIGGRAPH NeRF capture of Jensen Huang also resurfaced [8][35], and a Meta Reality Labs collaboration stress-tested GS and volumetric video [10].

## Why it matters (reasoning)
GS is moving from research demos toward production-shaped tooling that touches the studio's exact stack: Unity, web (three.js), and Vision Pro XR. Spark mixing splats with meshes in three.js [26] and Apple's native Vision Pro support [17][20] mean splats can sit inside conventional scenes rather than living in isolated viewers. Feed-forward, sparse-input methods [32] and multi-GPU scaling [18] attack the two biggest production blockers — capture effort and reconstruction cost — which is the precondition for splats becoming a routine asset type rather than a specialist capture. The counter-signal is concrete: Apple's culling makes splats unreliable for close-up interior XR right now [17], and AI-generated geometry still shows artifacts like shimmering materials [23], so quality and platform constraints, not capability claims, gate adoption. Separately, Unity micro-tools [5][12] and DCC releases [11][22] are incremental iteration-speed wins rather than directional shifts.

## Possibility
Likely: GS continues consolidating into existing engines and web runtimes as a mesh-compatible asset type, given simultaneous movement on three.js [26], Apple platforms [17][20], and scaling research [18][32]. Plausible: feed-forward sparse-photo capture [32] makes splats practical for environment/asset reference capture within months. Plausible but constrained: Vision Pro interior experiences built purely on splats stay blocked until Apple changes the culling behavior [17]; building on photogrammetry-mesh + splat hybrids [20] is the safer near-term bet. Unlikely on this evidence: AI mesh generation (Fable 5) replacing hand/auto-rigged production assets soon — the demos show promise but also unresolved artifacts [23][31]. No source states numeric probabilities.

## Org applicability — NDF DEV
1) Evaluate Real Fake Interiors for stylized building interiors in games/XR where full geometry is wasteful — effort low [5]. 2) Prototype Spark in a three.js test scene to see how splat+mesh mixing performs on the studio's web/mobile targets — effort med [26]. 3) Before scoping any Vision Pro splat interior, validate against the close-range culling limit and prefer a photogrammetry-mesh + splat hybrid like Apple Maps' approach — effort low to confirm, med to design around [17][20][19]. 4) Add the Unity mask/channel-packing editor tool to the VFX/texture workflow to cut Photoshop round-trips — effort low [12]. 5) Watch the Houdini 22 keynote (June 17) for procedural pipeline features before any tool-version decision — effort low [11]. 6) Run a small, time-boxed test of Fable 5 mesh/rig generation for greyboxing and prototyping only, treating output as draft given shimmering/quality caveats — effort med [31][23]. 7) Point edutech/internal upskilling at the free Bonn robotics/photogrammetry curriculum for spatial-capture fundamentals — effort low [2]. Skip: crypto/NFT items [30][39], the radiance-field celebrity capture as production-relevant [8][35], Luma Cannes marketing [38][44], and all off-topic politics/personal posts [7][9][15][28][29][33].

## Signals to Watch
- Apple changing Vision Pro splat culling — it currently blocks close-up interior splats [17]; watch visionOS 27 API notes [19].
- Feed-forward sparse-photo GS (Wild3R / AnySplat finetune) maturing into a usable capture tool [32].
- Spark / three.js GS adoption as a route to splats in web and mobile XR builds [26].
- Houdini 22 keynote (June 17, London) feature set for procedural content pipelines [11].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ItzFAILURE | ^1062 c9 | ["Keep moving forward." Our past should define us not hold us prisioner. TY for 6](https://x.com/ItzFAILURE/status/2065400456591937620) |
| x | IlirAliu_ | ^658 c1 | [One professor at the University of Bonn quietly put his entire robotics curricul](https://x.com/IlirAliu_/status/2064979957009285375) |
| x | afrotron | ^222 c2 | [Rig is done just ironing out some kinks. I'll put it up on my gumroad later this](https://x.com/afrotron/status/2064789451839049861) |
| x | RyanLykos | ^212 c2 | [Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv](https://x.com/RyanLykos/status/2065189214413611291) |
| x | 80Level | ^198 c1 | [Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo t](https://x.com/80Level/status/2065109302562422981) |
| x | VFX_Therapy | ^173 c0 | [Detailed breakdown of the flame vfx in one frame by @S_SerraMock in Unreal. #vfx](https://x.com/VFX_Therapy/status/2065397660119716179) |
| x | zephyyy7 | ^170 c6 | [@Will40746376 @Dexerto funny how last game this same crowd swore "no real woman ](https://x.com/zephyyy7/status/2065112542448374086) |
| x | RadianceFields | ^152 c8 | [In the summer of 2023, I cold emailed Jensen Huang and asked to capture a NeRF o](https://x.com/RadianceFields/status/2064766228866924681) |
| x | sachin_inc | ^148 c9 | [The action of the Returning Officer, who is also the Secretary of the Madhya Pra](https://x.com/sachin_inc/status/2064727133411475762) |
| x | gracia_vr | ^140 c3 | [We teamed up with researchers at Meta @RealityLabs to stress-test what's actuall](https://x.com/gracia_vr/status/2065106030539997345) |
| x | sidefx | ^132 c0 | [Houdini 22 launches in London next week! Join us at Curzon Soho Cinema for an ex](https://x.com/sidefx/status/2065141618509005226) |
| x | VFX_Therapy | ^106 c0 | [Tired of opening Photoshop for every tiny mask tweak? @KenDeng built a Unity Edi](https://x.com/VFX_Therapy/status/2065035196358094848) |
| x | bilawalsidhu | ^105 c13 | [Wow, this is really cool. Has anyone productized this? I would love to be able t](https://x.com/bilawalsidhu/status/2064865579547193788) |
| x | filicroval | ^101 c7 | [🤖time for another 4D tool! this tool turns videos into moving 3D places film a m](https://x.com/filicroval/status/2064731328210145625) |
| x | rmacdon627 | ^96 c3 | [✅ The SAVE America Act (proof of citizenship + photo ID for federal elections) i](https://x.com/rmacdon627/status/2064881931221602482) |
| x | AKantemirov | ^82 c3 | [Took a few days to get procedural materials from @noaxdesign onto my model and s](https://x.com/AKantemirov/status/2065233326386843944) |
| x | iBrews | ^71 c3 | [Apple's new gaussian splatting support is cool, but the culling is kind of ridic](https://x.com/iBrews/status/2064836100720394464) |
| x | janusch_patas | ^69 c1 | [A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting Abstract (excerp](https://x.com/janusch_patas/status/2064965130413048221) |
| x | xchester16 | ^69 c1 | [After spending some time with the new visionOS 27 APIs and Reality Composer Pro ](https://x.com/xchester16/status/2064900511116185939) |
| x | Azadux | ^69 c5 | [I believe that Apple Maps in visionOS 27 is a combination of photogrammetry mesh](https://x.com/Azadux/status/2064876849252225246) |
| x | multimodalart | ^69 c2 | [folks @liquidai trained a specialist tiny model to do one thing rly well: extrac](https://x.com/multimodalart/status/2064864942180679962) |
| x | RedefineFX | ^67 c2 | [Falcon 9 landing real-time VFX in Unreal 5.8, continuing with my space explorati](https://x.com/RedefineFX/status/2065047711477301342) |
| x | drashyakuruwa | ^64 c8 | [A minor graphics update to the initial version of my GTA V-style game with @thre](https://x.com/drashyakuruwa/status/2065055670496276601) |
| x | DillyWillyVR | ^62 c2 | [Texturing a commission for my friend @Lightning260493 and here is the process! 🐾](https://x.com/DillyWillyVR/status/2065214193511326082) |
| x | pablovelagomez1 | ^53 c4 | [There's been a few cool updates recently. In particular, @rerundotio 0.33 releas](https://x.com/pablovelagomez1/status/2065154703068193138) |
| x | GithubProjects | ^47 c3 | [Spark integrates 3D Gaussian splatting with the THREE.js rendering pipeline for ](https://x.com/GithubProjects/status/2064807319255515476) |
| x | Deathbymetal87 | ^41 c2 | [if 420 of you guys donated to my kofi i could get an original 3d printed model o](https://x.com/Deathbymetal87/status/2065150122489430375) |
| x | fistandilus12 | ^40 c2 | [Funny how people who spent 20 years defending Photoshop, CGI, motion capture, pr](https://x.com/fistandilus12/status/2064943228340535490) |
| x | GSAIGETOA | ^38 c0 | [Update on Meeting of Team BDM with JS (Admin), DoT Shri K. Balaji on 09.06.2026 ](https://x.com/GSAIGETOA/status/2064954292612764048) |
| x | EnochsDegenCrib | ^37 c1 | [⭕️ $RENDER = The Decentralized GPU Powerhouse AI Actually Needs ⭕️💻🚀 Everyone’s ](https://x.com/EnochsDegenCrib/status/2065155872914035156) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1062 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2065400456591937620">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&quot;Keep moving forward.&quot; Our past should define us not hold us prisioner. TY for 600 followers over these last couple of days! Model: @Artstudious Rig: @cookie_sugar42 Shader: @LuminaryOfAges Textures: ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan animator hit 600 followers and shared a RWBY fanart animation in Blender, crediting separate artists for the model, rig, shader, and textures.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ItzFAILURE/status/2065400456591937620" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IlirAliu_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 658 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IlirAliu_/status/2064979957009285375">View @IlirAliu_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One professor at the University of Bonn quietly put his entire robotics curriculum on YouTube: SLAM. Sensor fusion. State estimation. Probabilistic robotics. Self-driving cars. Motion planning. Photog”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Prof. Cyrill Stachniss (Univ. of Bonn), a top-cited mobile robotics researcher, has published complete university lecture playlists on YouTube free — covering SLAM, photogrammetry, sensor fusion, state estimation, and motion planning.</dd>
      <dt>Why interesting</dt>
      <dd>SLAM and photogrammetry map directly onto XR/VR spatial tracking and 3D reconstruction work the studio builds in Unity.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team can assign the SLAM and photogrammetry playlists as reference study when scoping spatial anchoring or AR tracking features.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IlirAliu_/status/2064979957009285375" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@afrotron</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 222 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/afrotron/status/2064789451839049861">View @afrotron on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Rig is done just ironing out some kinks. I'll put it up on my gumroad later this month #blender #rigging #anissa #invincible https://t.co/CGVgJltzLt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Blender artist @afrotron completed a character rig for Anissa (from the Invincible IP) and plans to release it on Gumroad later this month.</dd>
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
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 212 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2065189214413611291">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Artist RyanLykos shared a work-in-progress Blender face rig for a character named Zhu Yuan, posted as a short video clip with no technical breakdown.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2065189214413611291" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@80Level</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 198 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/80Level/status/2065109302562422981">View @80Level on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo that lets you create the illusion of a furnished room behind a flat window surface. Get it here: https://t.co/w9rlA4b1an ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Real Fake Interiors by AmplifyCreates is a Unity baking tool + shader that simulates lit, furnished rooms behind flat window geometry using interior mapping.</dd>
      <dt>Why interesting</dt>
      <dd>Interior mapping delivers believable building depth at near-zero runtime cost — a practical win for any Unity project with exterior architecture.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team should test this on any project with building facades before committing to more expensive geometry or baked lightmap solutions.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/80Level/status/2065109302562422981" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 173 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2065397660119716179">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Detailed breakdown of the flame vfx in one frame by @S_SerraMock in Unreal. #vfx https://t.co/i257Fz3YZt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@S_SerraMock published a frame-by-frame flame VFX breakdown built in Unreal Engine, showing the layered techniques behind a single shot.</dd>
      <dt>Why interesting</dt>
      <dd>Seeing how a professional layers particle, shader, and lighting in one frame gives the Unity team a concrete reference for real-time fire effects in games or XR scenes.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Use this breakdown as a reference when building fire or environmental VFX in Unity — map the Unreal node logic to Unity VFX Graph or Shader Graph equivalents.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2065397660119716179" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@zephyyy7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 170 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/zephyyy7/status/2065112542448374086">View @zephyyy7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@Will40746376 @Dexerto funny how last game this same crowd swore &quot;no real woman looks like that,&quot; then Eve turned out to be a 3D scan of an adult Korean model. now an adult Korean face &quot;must be&quot; a chi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user on X argues that critics misidentify adult Korean face references in two games, citing that a prior game's character was a 3D scan of an adult Korean model.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/zephyyy7/status/2065112542448374086" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RadianceFields</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 152 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RadianceFields/status/2064766228866924681">View @RadianceFields on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“In the summer of 2023, I cold emailed Jensen Huang and asked to capture a NeRF of him at SIGGRAPH. He responded in about an hour and said yes. A radiance field is, in the simplest terms, akin to a 3D ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An independent researcher captured a 360° Gaussian splat of Jensen Huang at SIGGRAPH 2023; three years later NVIDIA now ships multiple radiance-field projects — NuRec, fVDB, 3DGRUT, and gsplat — validating the format at scale.</dd>
      <dt>Why interesting</dt>
      <dd>Gaussian splatting now has NVIDIA-backed tooling, making real-world scene capture a practical option for XR/VR projects without expensive photogrammetry pipelines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team should test NVIDIA's gsplat or 3DGRUT for capturing real environments in upcoming XR scenes as a faster alternative to manual 3D modelling.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RadianceFields/status/2064766228866924681" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
