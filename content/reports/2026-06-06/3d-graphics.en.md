---
type: social-topic-report
date: '2026-06-06'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-06T15:51:37+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 34
salience: 0.55
sentiment: mixed
confidence: 0.55
tags:
- gaussian-splatting
- blender
- shaders
- ai-3d
- photogrammetry
- unity
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2058586450484994048/img/lm4ksQYSOFmYZ0uF.jpg
---

# 3D & Graphics — 2026-06-06

## TL;DR
- KIRI Engine's 3DGS Render addon now animates Gaussian Splats inside Blender — 4DGS/.ply sequence export, experimental rigging and light baking, Blender 5.1 support [12].
- Reported progress on the splatting deployment gap (large files, no streaming) via LOD systems for large scenes [29]; Neural Gabor Splatting presented at CVPR 2026 [20].
- NVIDIA's ArtiFixer repairs scan artifacts and extends sparse views using Wan 2.1, generating hundreds of consistent frames for occluded regions [10].
- MAMMA claims markerless motion capture from a few synced video feeds, removing suits, markers, and cleanup [4].
- Directly usable craft: Unity ShaderGraph dissolve shader for death/teleport VFX [8] and Blender's Shaders Plus addon for glass/water/metal materials [3].

## What happened
The clearest thread is Gaussian Splatting moving from research demos toward production pipelines. KIRI Engine's 3DGS Render addon update brings splat animation into Blender, with 4DGS/.ply sequence export, experimental rigging and light baking, and Blender 5.1 support [12]. Separately, posts note that 3DGS deployment blockers — large files, no streaming — are being addressed with LOD systems for large scenes [29], and Neural Gabor Splatting was presented at CVPR 2026 [20][33]. AI-assisted capture and reconstruction also featured: NVIDIA's ArtiFixer repairs artifacts and extends sparse views using Wan 2.1 [10], and MAMMA claims markerless mocap from synced video [4]. On conventional tooling, artists shared a Unity ShaderGraph dissolve effect [8], the Blender Shaders Plus addon [3], an eye shader [21], and rigging tutorials/showcases [1][11][23]; one game's production notes cite laser scanning and photogrammetry with Yusuke Kozaki as lead designer [2]. Several high-ranking items are off-topic or promotional: AI-tool listicles [15][18][28], $RENDER crypto [27], AI video-gen clips [9][19], and personal/discourse posts [5][22][24].

## Why it matters (reasoning)
For a studio producing both game and XR assets, the splatting cluster matters most. Animatable splats inside Blender [12] plus LOD/streaming progress [29] begin to connect real-world capture to deployable engine content rather than static viewers — the missing link between scanning and Unity. AI reconstruction tools [10][4] target the costliest parts of asset production: cleanup of sparse scans and mocap suit-and-post-processing labor. The caveat is that these are vendor and enthusiast claims from short posts, not benchmarked results; splat-to-Unity round-tripping, licensing, and runtime cost on mobile or standalone XR headsets are unproven in these items. The shader and rigging posts [3][8][21] are incremental craft improvements, not strategic shifts.

## Possibility
Likely: Blender-side Gaussian Splatting tooling keeps maturing this year, given coordinated addon updates [12], infrastructure work [29], and active CVPR research [20]. Plausible: markerless mocap [4] and AI scan repair [10] reach indie/studio-viable quality, but engine integration and output fidelity need validation first. Unlikely: any of these replaces current Unity asset workflows in the near term — the items show capability demos, not mobile/XR-optimized, production-proven pipelines. No source states numeric probabilities.

## Org applicability — NDF DEV
1) Trial KIRI's 3DGS Render addon in Blender to test a capture→splat→Unity path for an XR environment scene, measuring runtime cost on the target headset (med) [12][29]. 2) Add the Unity ShaderGraph dissolve shader to the VFX library for enemy-death/teleport effects in current games (low) [8]. 3) Evaluate Shaders Plus for faster glass/water/metal materials in asset production (low) [3]. 4) Pilot MAMMA-style markerless mocap on a non-critical character animation and compare cleanup time against the current method before committing (med) [4]. 5) Track NVIDIA ArtiFixer for cleaning photogrammetry/sparse scans, but defer integration until availability and licensing are clear (low eval) [10]. Skip: $RENDER crypto [27], 'hidden AI tools' listicles [15][18][28], NSFW/personal/discourse items [5][13][22][24], and AI video-gen demos [9][19] — none are 3D-pipeline tools for the studio.

## Signals to Watch
- Gaussian Splatting LOD/streaming and 4DGS animation maturing toward engine deployment [12][29].
- CVPR 2026 splatting and neural rendering research feeding the next wave of tooling [20][33].
- AI scan-repair for sparse/occluded views — NVIDIA ArtiFixer [10].
- Video-only markerless mocap (MAMMA) as a possible cost cut for character animation [4].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ndngdng10115 | ^1299 c9 | [The way the tendons, helper bones, and smoothing work together is seriously impr](https://x.com/ndngdng10115/status/2062718274643845486) |
| x | _YuriP__ | ^793 c4 | [• Development started in 2020 • Lead character designer is Yusuke Kozaki (Fire E](https://x.com/_YuriP__/status/2062605291485540393) |
| x | filip_animation | ^737 c3 | [My most used Blender addons #4: - Shaders Plus by SMOUSE Glass, water, oily meta](https://x.com/filip_animation/status/2062619776153764230) |
| x | clankrmedia | ^611 c7 | [Wow! Motion capture studios not gonna love this! Just check this insane video. F](https://x.com/clankrmedia/status/2062988031708000566) |
| x | mjarbo | ^571 c239 | [Kane Parsons’ comments about AI feel a little too clean to me. He told The Austr](https://x.com/mjarbo/status/2062647581910413513) |
| x | Mix3Design | ^542 c7 | [I will have a big announcement in the upcoming hours all the blender 3d artists ](https://x.com/Mix3Design/status/2062654531888910756) |
| x | SciTechera | ^458 c19 | [Wow. That's cool. Researchers just released World, an open-source Unreal Engine ](https://x.com/SciTechera/status/2062554345087041916) |
| x | VFX_Therapy | ^287 c1 | [Dissolve Shader = Interactive edge glow + world space control. Perfect for enemy](https://x.com/VFX_Therapy/status/2062607977186738307) |
| x | auqibhabib | ^267 c35 | [Made with seedance 2.0 + GPT Image 2 on @yapper_so Prompt. @image1 mage1 fights ](https://x.com/auqibhabib/status/2062599264807833617) |
| x | wildmindai | ^243 c2 | [3D scene reconstructions by NVIDIA. ArtiFixer - repairs artifacts and extends sp](https://x.com/wildmindai/status/2062816526223216995) |
| x | DemNikoArt | ^163 c2 | [🚨 NEW TUTORIAL IS OUT NOW! How to rig a Bike Suspension in Blender. 🔗 below #b3d](https://x.com/DemNikoArt/status/2062589493710934176) |
| x | KIRI_Engine_App | ^135 c1 | [Gaussian Splats can now be animated in Blender New 3DGS Render addon update: - B](https://x.com/KIRI_Engine_App/status/2062821750287847445) |
| x | FoxibikiN | ^97 c1 | [(HD) Chillet &amp; Chill 🩵Chillet made by @furromantic ❄️Beau OC made by @miauha](https://x.com/FoxibikiN/status/2062652783975608633) |
| x | multimodalart | ^85 c1 | [I' m so addicted to @GoogleMagenta RealTime 2 🎹 so to justify playing with it 24](https://x.com/multimodalart/status/2062938381785403586) |
| x | Orion_Vers7x | ^68 c27 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/SConc5qUp9 – Writing](https://x.com/Orion_Vers7x/status/2062749510195982839) |
| x | DXU241 | ^66 c2 | [Been working on better support for Unreal Gold, will need to write a custom clou](https://x.com/DXU241/status/2062653242795012221) |
| x | ihe4rtjungkook | ^59 c1 | [@vjungist cuz they took a 3d scan of his to make ts more accurate at his event](https://x.com/ihe4rtjungkook/status/2062996203235647515) |
| x | unfilteredranjn | ^52 c3 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/2ACL9zZ1Y8 – Writing](https://x.com/unfilteredranjn/status/2062778586046829047) |
| x | auqibhabib | ^49 c14 | [Made with seedance 2.0 + GPT Image 2 Prompt :Use the uploaded reference image as](https://x.com/auqibhabib/status/2062951836882231393) |
| x | HeartWatanabe20 | ^46 c0 | [Presenting Neural Gabor Splatting at CVPR 2026 tomorrow! 📍 Poster Session 🗓 June](https://x.com/HeartWatanabe20/status/2062728687007789143) |
| x | SG_Animations | ^45 c3 | [a quick abstraction eye shader i made in blender :) https://t.co/6tbIY5Iocu](https://x.com/SG_Animations/status/2062881248842830323) |
| x | user__NULL | ^40 c0 | [@gingerIemons @UltraTomatoo @airbagg3d No. Mike Parsons working in VFX for a def](https://x.com/user__NULL/status/2062653907764212105) |
| x | DemNikoArt | ^40 c1 | [If you haven't seen it, my new rigging tutorial is out now. How to rig a Bike Su](https://x.com/DemNikoArt/status/2062879660095000906) |
| x | RisingNomes | ^40 c3 | [This is my precious, little boy at about the same gestation that scan of their b](https://x.com/RisingNomes/status/2062789349306159350) |
| x | JamesMason0 | ^39 c6 | [You know, something I’ve always wondered - Why is it that so many Blender animat](https://x.com/JamesMason0/status/2062984400338403485) |
| x | alt_Vulcan105 | ^33 c1 | [@cybernetic_sam The only possible answer is that rover civilization is using sim](https://x.com/alt_Vulcan105/status/2062825816980181055) |
| x | EnochsDegenCrib | ^32 c0 | [🚀 $RENDER Bull Case: Market Dip? What Dip? Fundamentals Are Unbreakable⭕️🚀 Crypt](https://x.com/EnochsDegenCrib/status/2062904565859553483) |
| x | PrakashS720 | ^32 c5 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/6XRECyOn7W – Writing](https://x.com/PrakashS720/status/2062839222139294035) |
| x | Stefan_3D_AI | ^28 c0 | [For years, the biggest problem with 3D Gaussian Splatting wasn't quality. It was](https://x.com/Stefan_3D_AI/status/2063240740155895943) |
| x | MeshyAI | ^18 c0 | [I asked an AI agent to 3D print me as a figurine series! Here's how it works: - ](https://x.com/MeshyAI/status/2062805201480745129) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ndngdng10115</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1299 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ndngdng10115/status/2062718274643845486">View @ndngdng10115 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The way the tendons, helper bones, and smoothing work together is seriously impressive. 🔥 If you’re into character rigging, this one is worth a close look. #Blender #Blender3D #B3D #Rigging #Character”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender character rig demo shows tendons, helper bones, and mesh smoothing working together for high-quality deformation.</dd>
      <dt>Why interesting</dt>
      <dd>Advanced rigging techniques like these directly improve character quality in Unity game and XR projects without additional assets.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/character art team can study this rig structure and apply helper-bone patterns to existing character pipelines.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ndngdng10115/status/2062718274643845486" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@_YuriP__</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 793 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/_YuriP__/status/2062605291485540393">View @_YuriP__ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“• Development started in 2020 • Lead character designer is Yusuke Kozaki (Fire Emblem Awakening/Fates/Heroes) • Laser scanning and photogrammetry • Developed their own sound engine with 7.1.4 audio • ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A flight combat game (dev started 2020, character art by Yusuke Kozaki) used laser scanning and photogrammetry for 3D assets, built a custom 7.1.4 spatial audio engine, and referenced Top Gun Maverick for pilot cutscenes.</dd>
      <dt>Why interesting</dt>
      <dd>Photogrammetry is now a standard pipeline for high-fidelity 3D capture in AAA titles — the same workflow scales down to XR and Unity projects for environments and props.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/XR team can trial photogrammetry (Reality Capture or Polycam) for capturing real-world props or environments in the next 3D-heavy project.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/_YuriP__/status/2062605291485540393" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@filip_animation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 737 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/filip_animation/status/2062619776153764230">View @filip_animation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“My most used Blender addons #4: - Shaders Plus by SMOUSE Glass, water, oily metals are just made extremely easy with these shaders. You would be surprised how much I end up making those. Also very per”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Blender artist Filip recommends the 'Shaders Plus' addon by SMOUSE for glass, water, and oily-metal materials — citing superior light dispersion and caustics over built-in shader options.</dd>
      <dt>Why interesting</dt>
      <dd>Studios using Blender for Unity or XR asset pipelines can skip manual shader setup for common transparent and reflective materials using ready-made, performance-tuned presets.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's 3D artists can trial Shaders Plus on the next project requiring glass props or water surfaces and compare output quality against current material workflows.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/filip_animation/status/2062619776153764230" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@clankrmedia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 611 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/clankrmedia/status/2062988031708000566">View @clankrmedia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow! Motion capture studios not gonna love this! Just check this insane video. For years, capturing human motion meant markers, skin-tight suits, and hours of cleanup. MAMMA just asks for a few synced”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>MAMMA is a markerless mocap system that matches Vicon accuracy using only synced cameras — including 4 iPhones — and cuts a multi-day capture pipeline to a single day with no suits or markers required.</dd>
      <dt>Why interesting</dt>
      <dd>The studio's Unity/XR animation work can source high-quality human motion data without renting a mocap studio — 4 iPhones and open space is the entire rig.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test MAMMA with 4 iPhones on the next character animation shoot to replace or supplement studio mocap rentals.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/clankrmedia/status/2062988031708000566" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mjarbo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 571 · 💬 239</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mjarbo/status/2062647581910413513">View @mjarbo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Kane Parsons’ comments about AI feel a little too clean to me. He told The Australian that if he could snap his fingers and make generative AI disappear forever, he probably would. Fair enough. He doe”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Kane Parsons (Backrooms creator, now in A24 orbit) said he'd erase generative AI if he could; a commentator notes his career was built on Blender and indie tools that bypassed traditional gatekeepers.</dd>
      <dt>Why interesting</dt>
      <dd>The post's core framing — use tools to do the work, not let tools replace the work — is the right mental model for any studio deciding where AI fits in its pipeline.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mjarbo/status/2062647581910413513" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Mix3Design</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 542 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Mix3Design/status/2062654531888910756">View @Mix3Design on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I will have a big announcement in the upcoming hours all the blender 3d artists that are into anime style / npr or blender in general will benefit from it alot alot and also who want to make game asse”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@Mix3Design teases an unspecified Blender announcement targeting anime/NPR artists and game asset or VFX creators, with no details disclosed.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Mix3Design/status/2062654531888910756" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SciTechera</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 458 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SciTechera/status/2062554345087041916">View @SciTechera on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow. That's cool. Researchers just released World, an open-source Unreal Engine 5 simulator for training and testing LLM and VLM agents in realistic 3D environments. The platform supports RGB, depth, ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Researchers released &quot;World,&quot; an open-source UE5 simulator with RGB/depth/segmentation sensors, procedural city generation, and a Gym-style Python API for training LLM/VLM agents in realistic 3D environments.</dd>
      <dt>Why interesting</dt>
      <dd>A Gym-compatible Python API over a photorealistic 3D simulator gives the XR/VR team a ready-made path to train and test AI agents in complex virtual scenes without building simulation infra from scratch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team can prototype agent navigation and perception logic inside World's UE5 environment, then evaluate whether that behavior transfers to Unity-based projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SciTechera/status/2062554345087041916" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 287 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2062607977186738307">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Dissolve Shader = Interactive edge glow + world space control. Perfect for enemy deaths or teleport effects! by @techartshahbaz. #Unity #ShaderGraph #TechArt #GameDev&quot; https://t.co/xjPVOSudHC”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Unity developer @techartshahbaz shares a dissolve shader built in ShaderGraph featuring interactive edge glow and world-space clip control, suited for death or teleport VFX.</dd>
      <dt>Why interesting</dt>
      <dd>Ready-made ShaderGraph dissolve with edge glow cuts the time to implement a staple game-feel effect that the Unity team uses regularly.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Review the linked implementation and add it to the studio's internal shader library as a reusable dissolve template.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2062607977186738307" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
