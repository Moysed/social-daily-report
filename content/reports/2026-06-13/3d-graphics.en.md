---
type: social-topic-report
date: '2026-06-13'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-13T03:33:57+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 42
salience: 0.55
sentiment: mixed
confidence: 0.55
tags:
- gaussian-splatting
- photogrammetry
- unity
- houdini
- image-to-3d
- xr-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065400058565079040/img/K_mHR8IT0VE_qxwT.jpg
---

# 3D & Graphics — 2026-06-13

## TL;DR
- Gaussian Splatting is moving from research into shippable pipelines: Gracia VR + Meta Reality Labs stress-tested GS and volumetric video on hard cases like sunny outdoor buildings [9], and a renovation studio scanned a property with GS and shipped a floor-by-floor walkthrough in PlayCanvas [13].
- GS research advanced on two fronts: a multi-GPU PyTorch approach scaling reconstruction to higher resolutions and larger scenes [15], and Wild3R, a feed-forward 3DGS method from sparse unconstrained photos with a new dataset finetuning AnySplat [20].
- Houdini 22 keynote is scheduled for June 17 in London (Curzon Soho) [10].
- Image-to-3D tools are bundled on GPU cloud services: TripoSR, Microsoft TRELLIS, Hunyuan3D 2.1, Nerfstudio, and 3DGS [29].
- Unity asset tooling shipped: 'Real Fake Interiors' bakes faked furnished rooms behind flat window surfaces [6], and an in-editor mask tool handles contrast/thresholds/channel packing/ramps to cut Photoshop round-trips [11].

## What happened
The day's strongest recurring thread is Gaussian Splatting and capture-to-3D. A Gracia VR / Meta Reality Labs collaboration tested GS and volumetric video on difficult conditions [9]; a separate team scanned a building with GS, rebuilt the renovation in 3D, and deployed an explorable floor-by-floor scene in PlayCanvas [13]. On the research side, a multi-GPU PyTorch GS abstraction targets higher resolutions and larger scenes [15], and Wild3R introduced feed-forward 3DGS from sparse unconstrained photos plus a dataset finetuning AnySplat [20]. Photogrammetry-plus-splat captures continued [30], and image-to-3D toolchains (TripoSR, TRELLIS, Hunyuan3D 2.1, Nerfstudio) were packaged on GPU cloud [29].

## Why it matters (reasoning)
Several items point the same way: scanning real environments into engine-ready scenes is getting cheaper and more web-deployable. The PlayCanvas walkthrough [13] shows GS can run in a browser engine, which is directly relevant to XR and web delivery; the Meta Reality Labs work [9] signals platform-side investment. Combined with image-to-3D generators [29] and feed-forward GS from casual photos [20], the second-order effect is faster greybox and environment prototyping with less manual modeling. The Houdini 22 launch [10] keeps procedural generation on the roadmap for studios that can absorb that pipeline. AI-assisted mesh/rig generation (e.g. Claude 'Fable 5' producing a named, hierarchied mesh in minutes [26], a three.js game [19], realtime work [17]) is recurring but remains single-demo, self-reported, and unverified for production quality.

## Possibility
Likely: GS continues into web/engine pipelines for XR and walkthroughs, since a browser deployment already shipped [13] and a platform vendor is investing [9]. Plausible: image-to-3D tools [29] and feed-forward GS [20] become usable for prototype/background assets, though production-grade topology and texturing quality are unproven from these posts. Unlikely near-term: one-shot AI generation of production-ready rigged meshes [26] — the claim rests on a single 5-minute demo with no independent validation. No source states numeric probabilities, so none are given.

## Org applicability — NDF DEV
1) Trial a GS-to-web pipeline for an XR/walkthrough asset using the PlayCanvas pattern [13] and GS captures [9][30] — med effort, directly aligned with the XR/VR portfolio. 2) Spin up a quick test of image-to-3D tools (TRELLIS, Hunyuan3D 2.1, TripoSR) for greybox/prototype assets via GPU cloud [29] — low/med effort; judge whether output cleans up faster than modeling from scratch. 3) Adopt the two Unity tools now: 'Real Fake Interiors' for cheap interior depth on mobile/web windows [6] and the in-editor mask tool to cut Photoshop iteration in VFX [11] — both low effort, immediately usable in Unity work. 4) Have one person watch the Houdini 22 keynote June 17 for procedural features [10] before committing pipeline time — low effort to attend, high effort to adopt. 5) Run a small, time-boxed experiment with AI mesh/rig generation [26][19] for non-critical assets only — low effort, treat output as draft. Skip: $RENDER / decentralized-GPU crypto pitch [23], NFT 3D-scan sales [28][21], the AI-vs-craft culture-war threads [8][22], and off-topic items (telecom meeting [24], sports sensor replays [32][33]).

## Signals to Watch
- Houdini 22 keynote June 17, London — check announced procedural features [10].
- Wild3R + AnySplat: feed-forward GS from casual sparse photos, plus dataset [20]; pair with multi-GPU GS scaling [15].
- Meta Reality Labs investing in GS/volumetric video — watch for platform tooling [9].
- 'Fable 5' (Claude) recurring across 3D-gen demos [26][19][17] — unverified, watch for reproducible results.

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ItzFAILURE | ^3000 c19 | ["Keep moving forward." Our past should define us not hold us prisioner. TY for 6](https://x.com/ItzFAILURE/status/2065400456591937620) |
| x | IlirAliu_ | ^747 c1 | [One professor at the University of Bonn quietly put his entire robotics curricul](https://x.com/IlirAliu_/status/2064979957009285375) |
| x | GameZoneHQ | ^642 c3 | [Have a look at this impressive Unity real-time physics, created by VFX Artist @S](https://x.com/GameZoneHQ/status/2065365759451148399) |
| x | bilawalsidhu | ^474 c13 | [Someone needs to throw fable 5 at the OG of procedural 3D generation (houdini) a](https://x.com/bilawalsidhu/status/2065457916405072127) |
| x | VFX_Therapy | ^365 c0 | [Detailed breakdown of the flame vfx in one frame by @S_SerraMock in Unreal. #vfx](https://x.com/VFX_Therapy/status/2065397660119716179) |
| x | 80Level | ^266 c2 | [Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo t](https://x.com/80Level/status/2065109302562422981) |
| x | RyanLykos | ^248 c3 | [Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv](https://x.com/RyanLykos/status/2065189214413611291) |
| x | zephyyy7 | ^187 c6 | [@Will40746376 @Dexerto funny how last game this same crowd swore "no real woman ](https://x.com/zephyyy7/status/2065112542448374086) |
| x | gracia_vr | ^167 c4 | [We teamed up with researchers at Meta @RealityLabs to stress-test what's actuall](https://x.com/gracia_vr/status/2065106030539997345) |
| x | sidefx | ^155 c0 | [Houdini 22 launches in London next week! Join us at Curzon Soho Cinema for an ex](https://x.com/sidefx/status/2065141618509005226) |
| x | VFX_Therapy | ^120 c0 | [Tired of opening Photoshop for every tiny mask tweak? @KenDeng built a Unity Edi](https://x.com/VFX_Therapy/status/2065035196358094848) |
| x | The_Genesis_0 | ^120 c4 | [HOW TO: Create Realistic 3D Food in Blender in 10 steps. 1) Get Multiple referen](https://x.com/The_Genesis_0/status/2065394214771253289) |
| x | AurelienCa80656 | ^107 c3 | [We scanned the existing property using Gaussian Splatting, rebuilt the entire re](https://x.com/AurelienCa80656/status/2065420062861733906) |
| x | AKantemirov | ^100 c4 | [Took a few days to get procedural materials from @noaxdesign onto my model and s](https://x.com/AKantemirov/status/2065233326386843944) |
| x | janusch_patas | ^73 c1 | [A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting Abstract (excerp](https://x.com/janusch_patas/status/2064965130413048221) |
| x | RedefineFX | ^71 c2 | [Falcon 9 landing real-time VFX in Unreal 5.8, continuing with my space explorati](https://x.com/RedefineFX/status/2065047711477301342) |
| x | pablovelagomez1 | ^70 c5 | [There's been a few cool updates recently. In particular, @rerundotio 0.33 releas](https://x.com/pablovelagomez1/status/2065154703068193138) |
| x | DillyWillyVR | ^68 c2 | [Texturing a commission for my friend @Lightning260493 and here is the process! 🐾](https://x.com/DillyWillyVR/status/2065214193511326082) |
| x | drashyakuruwa | ^63 c8 | [A minor graphics update to the initial version of my GTA V-style game with @thre](https://x.com/drashyakuruwa/status/2065055670496276601) |
| x | zhenjun_zhao | ^44 c1 | [Wild3R: Feed-Forward 3D Gaussian Splatting from Unconstrained Sparse Photo Colle](https://x.com/zhenjun_zhao/status/2065032225423274347) |
| x | Deathbymetal87 | ^43 c2 | [if 420 of you guys donated to my kofi i could get an original 3d printed model o](https://x.com/Deathbymetal87/status/2065150122489430375) |
| x | fistandilus12 | ^42 c2 | [Funny how people who spent 20 years defending Photoshop, CGI, motion capture, pr](https://x.com/fistandilus12/status/2064943228340535490) |
| x | EnochsDegenCrib | ^41 c1 | [⭕️ $RENDER = The Decentralized GPU Powerhouse AI Actually Needs ⭕️💻🚀 Everyone’s ](https://x.com/EnochsDegenCrib/status/2065155872914035156) |
| x | GSAIGETOA | ^41 c0 | [Update on Meeting of Team BDM with JS (Admin), DoT Shri K. Balaji on 09.06.2026 ](https://x.com/GSAIGETOA/status/2064954292612764048) |
| x | artjomwan | ^38 c0 | [Hey there! I have made this laser VFX in Unity today. I'm going to finish it but](https://x.com/artjomwan/status/2065148257274077527) |
| x | Oluwaphilemon1 | ^37 c1 | [This took 5 minutes. No rigging, no keyframes. Claude Fable 5 + any AI agent = l](https://x.com/Oluwaphilemon1/status/2065019441478332684) |
| x | LumaLabsAI | ^29 c5 | [Partnership is the new power move. Luma is at Cannes Lions 2026 with the partner](https://x.com/LumaLabsAI/status/2065092649518780723) |
| x | HeinerBuhr | ^24 c8 | [Some roses vanish in a few days. But Garden Roses — a 3D scan of real roses from](https://x.com/HeinerBuhr/status/2065081086233690316) |
| x | clore_ai | ^23 c5 | [Create detailed 3D models from images using https://t.co/tS1YgkSXYM's GPU-powere](https://x.com/clore_ai/status/2065457183811092985) |
| x | artfletch | ^22 c0 | [New #photogrammetry capture of Glengall Stairs and causeway on the Isle of Dogs.](https://x.com/artfletch/status/2065353199888851288) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3000 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2065400456591937620">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&quot;Keep moving forward.&quot; Our past should define us not hold us prisioner. TY for 600 followers over these last couple of days! Model: @Artstudious Rig: @cookie_sugar42 Shader: @LuminaryOfAges Textures: ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender artist posted a RWBY fan animation celebrating 600 followers, crediting collaborators for rig, shader, and textures.</dd>
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
    <span class="ndf-engagement">♥ 747 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IlirAliu_/status/2064979957009285375">View @IlirAliu_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One professor at the University of Bonn quietly put his entire robotics curriculum on YouTube: SLAM. Sensor fusion. State estimation. Probabilistic robotics. Self-driving cars. Motion planning. Photog”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Prof. Cyrill Stachniss (Univ. of Bonn, top-cited mobile robotics researcher) has published his full university robotics curriculum on YouTube free — SLAM, sensor fusion, photogrammetry, motion planning, and state estimation.</dd>
      <dt>Why interesting</dt>
      <dd>SLAM and photogrammetry are core techniques in XR/VR spatial tracking and 3D reconstruction — having university-level lecture playlists as reference is directly useful for the XR team.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team can bookmark the photogrammetry and SLAM playlists as technical reference for spatial anchoring or environment scanning work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IlirAliu_/status/2064979957009285375" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GameZoneHQ</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 642 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GameZoneHQ/status/2065365759451148399">View @GameZoneHQ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Have a look at this impressive Unity real-time physics, created by VFX Artist @Sakura_Rabbiter #unity3d #gamedev #indiedev #madewithunity #unity #3dart #3d #unityengine #VFX #shader #RealTime #UE5 #3d”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>VFX artist @Sakura_Rabbiter published a Unity real-time physics demo combining custom shaders and particle effects, shared by @GameZoneHQ to 642 likes.</dd>
      <dt>Why interesting</dt>
      <dd>The demo shows the current ceiling of Unity real-time physics + shader work — useful reference for the studio's Unity game and XR/VR visual targets.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Watch the linked clip and note the shader and physics setup as a benchmark for the studio's next Unity VFX pass.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GameZoneHQ/status/2065365759451148399" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 474 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065457916405072127">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Someone needs to throw fable 5 at the OG of procedural 3D generation (houdini) and render it all in unreal engine https://t.co/QvVuHNhll7”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user casually suggests that Fable 5 should use Houdini for procedural 3D generation and render in Unreal Engine — a wishlist opinion with no new information attached.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2065457916405072127" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 365 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2065397660119716179">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Detailed breakdown of the flame vfx in one frame by @S_SerraMock in Unreal. #vfx https://t.co/i257Fz3YZt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@S_SerraMock published a frame-by-frame VFX layer breakdown of a flame effect built in Unreal Engine, showing particle, shader, and compositing decisions.</dd>
      <dt>Why interesting</dt>
      <dd>Flame breakdowns expose the layer logic and shader tricks that transfer directly to Unity VFX Graph or Shader Graph regardless of engine.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's VFX artists can use this breakdown as a reference when building fire or flame effects in Unity VFX Graph for game or XR scenes.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2065397660119716179" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@80Level</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 266 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/80Level/status/2065109302562422981">View @80Level on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo that lets you create the illusion of a furnished room behind a flat window surface. Get it here: https://t.co/w9rlA4b1an ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Amplify Creations released 'Real Fake Interiors', a Unity tool combining a baking pipeline and shader to render convincing parallax room interiors behind flat window geometry — no actual room mesh required.</dd>
      <dt>Why interesting</dt>
      <dd>This is a direct performance win for any Unity project with urban or architectural environments — fake interior illusion costs far less than modelling real rooms.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can evaluate this asset for any scene requiring building facades or windowed surfaces, cutting geometry and draw-call overhead immediately.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/80Level/status/2065109302562422981" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 248 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2065189214413611291">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer @RyanLykos shared a work-in-progress Blender face rig for a character named Zhu Yuan, showing bone and shape-key setup for facial animation.</dd>
      <dt>Why interesting</dt>
      <dd>Face rigging technique in Blender is directly applicable to character pipelines in Unity game and XR projects where expressive avatars or NPCs are required.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's Unity/XR team can reference this rig's bone layout and shape key approach when building expressive character assets for upcoming projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2065189214413611291" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@zephyyy7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 187 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/zephyyy7/status/2065112542448374086">View @zephyyy7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@Will40746376 @Dexerto funny how last game this same crowd swore &quot;no real woman looks like that,&quot; then Eve turned out to be a 3D scan of an adult Korean model. now an adult Korean face &quot;must be&quot; a chi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Twitter user argues that critics misread Korean adult faces as children's faces, citing two games where character models were scanned from adult Korean models.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/zephyyy7/status/2065112542448374086" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
