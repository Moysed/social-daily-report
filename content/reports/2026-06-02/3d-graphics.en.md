---
type: social-topic-report
date: '2026-06-02'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-02T03:33:36+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 20
salience: 0.45
sentiment: positive
confidence: 0.5
tags:
- blender
- gaussian-splatting
- xr
- photogrammetry
- shaders
- pipeline
thumbnail: https://pbs.twimg.com/media/HJu5g4-WoAAkc5f.jpg
---

# 3D & Graphics — 2026-06-02

## TL;DR
- Blender 5.2 is reported to add a 'thin wall' shader for zero/low-thickness meshes — leaves, paper, tissue, thin plastics [1] (single-source, treat as claimed).
- Gaussian splatting is running on standalone Quest 3, with creators solving renderer issues via render-order key + depth tiebreak and view-space distance sorting [6]; also shown as scene/memory capture [3] and grayscale [18].
- Photogrammetry/3D scanning is used as a character base in production pipelines — full-body scan then manual sculpt for 'young Arnold' [13], and head-scan-to-model bases [15].
- Geometry-nodes VFX (stylized black hole) being ported Blender→Unreal [4]; FlippedNormals bundle offers 11 Blender add-ons + 1500+ assets for $30 [16].
- Most items are individual creator showcases and tutorials, not industry-level shifts; AI 3D-gen signal (Luma [14], Meshy [20]) is vague.

## What happened
A Blender shader feature called 'thin wall' is reported in a '5.2' version for meshes with little or no thickness such as leaves, paper, tissue, and thin plastics [1]; this was by far the highest-engagement item but is single-source. Gaussian splatting appears repeatedly: as standalone VR on Quest 3 with concrete rendering fixes (multi-renderer ordering via render-order key + depth tiebreak, view-space distance sorting) [6], as full-scene capture of a family home framed as spatial memory [3], in grayscale [18], plus general 'go deeper' links [19]. Photogrammetry shows up in real pipelines — a full-body scan of Arnold sculpted back ~20 years [13] and a personal head scan used as a character modeling base [15].

## Why it matters (reasoning)
The relevant, actionable signal for an XR/games studio is splatting reaching standalone headsets [6]: the bottleneck has been correct depth ordering and performance on mobile GPUs, and creators publicly sharing render-order/depth-tiebreak approaches lowers the barrier to capturing real locations and viewing them in 6DoF on Quest-class hardware [6][3]. That feeds environment and 'spatial memory' content for both XR experiences and edutech walkthroughs without full manual modeling. Photogrammetry-as-base-mesh [13][15] confirms the practical hybrid: scan for likeness/proportion, then hand-finish — relevant to character and avatar work. The Blender 'thin wall' item [1], if accurate, helps offline rendering of foliage/thin assets but is a Cycles/EEVEE-style shader concern; it does not automatically transfer to a Unity real-time shader, so its game-pipeline value is limited until validated. The rest (geometry-nodes VFX [4][5], rigging demos [7][10][11][12], asset bundles [16]) are routine craft and learning resources, not shifts.

## Possibility
Likely: gaussian splatting keeps moving toward consumer standalone VR, since working Quest 3 demos and shared ordering techniques already exist [6][3][18]. Plausible: Blender's 'thin wall' shader improves thin-asset offline rendering in an upcoming release, but real-time-engine equivalence is unproven from these items [1]. Plausible but weakly evidenced: AI-driven 3D generation (Luma physical-AI/generalization framing [14], Meshy reactions [20]) matures into asset workflows — the items are too vague to call. Unlikely near-term: splat-based assets fully replacing modeled geometry in shipped game builds; current evidence is capture/playback, not optimized game-ready meshes [6]. No source states numeric probabilities.

## Org applicability — NDF DEV
1) Prototype a gaussian-splatting capture→Quest 3 playback test for an XR/edutech location-walkthrough, reusing the render-order key + depth tiebreak approach described [6][3] (effort: med). 2) Adopt scan-as-base then hand-finish for character/avatar production where likeness matters [13][15] (effort: med). 3) Evaluate the FlippedNormals bundle (11 add-ons + 1500+ assets, $30) for the studio asset/environment library — low-cost, low-commitment [16] (effort: low). 4) Track Blender 5.2 'thin wall' but verify before pipeline use, and confirm whether it maps to a Unity real-time shader before relying on it for game assets [1] (effort: low). Skip for now: the Blender→Unreal geometry-nodes VFX port [4] (studio is Unity-first), individual rigging/animation showcases [7][10][11][12], fan animations [2], the off-topic court-case post [17], and unverified AI-3D-gen claims [14][20] beyond casual monitoring.

## Signals to Watch
- Blender 5.2 release notes — confirm 'thin wall' shader and whether it has a real-time/Unity-usable equivalent [1].
- Standalone-VR splatting rendering techniques (depth ordering, mobile-GPU performance) as they get documented [6].
- Luma Labs 'physical AI'/3D generalization direction for asset-generation relevance [14].
- AI mesh-generation tools (Meshy) for game-ready output quality [20].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Tioaoa2 | ^27793 c49 | [Blender 5.2 has a new shader feature called "thin wall" which is designed for me](https://x.com/Tioaoa2/status/2061445532518653996) |
| x | AnimGaby | ^1396 c13 | [D4DJ as Murder drones some parts are off sync because daVinci is trolling me Som](https://x.com/AnimGaby/status/2061071305634627949) |
| x | bilawalsidhu | ^660 c24 | [We treat 3d scanning like a tech demo, but it’s actually spatial memory capture.](https://x.com/bilawalsidhu/status/2061134940813611505) |
| x | ashlee3dee | ^499 c1 | [stylized black hole vfx with geometry nodes :3 i will port this to unreal engine](https://x.com/ashlee3dee/status/2061195779952275511) |
| x | VFX_Therapy | ^482 c3 | [When your Unreal VFX project hits different… @IgorPontes breakdown his Sasuke-le](https://x.com/VFX_Therapy/status/2061109917222920517) |
| x | DSkaale | ^306 c7 | [Just stepped inside my favorite movie locations on my Quest 3 🎬 Gaussian splatti](https://x.com/DSkaale/status/2061114844263117118) |
| x | DemNikoArt | ^285 c2 | [Bike Suspension Tutorial coming this week 😉 #b3d #blender #blender3d #rigging #t](https://x.com/DemNikoArt/status/2061498924473487814) |
| x | bilawalsidhu | ^79 c6 | [Honestly if we put this demo in a fancy XR headset, we’d call it jarvis. The fut](https://x.com/bilawalsidhu/status/2061450274011591084) |
| x | bilawalsidhu | ^78 c3 | [Fucking cool. Giving AR portal vibes - like watching volumetric video with full ](https://x.com/bilawalsidhu/status/2060943911363690875) |
| x | EdwardUrena_h | ^76 c0 | [I set out to see if it was possible to add a custom gizmo—and yes, it was; it to](https://x.com/EdwardUrena_h/status/2061539090198045116) |
| x | EdwardUrena_h | ^65 c0 | [One of the good things about this is that it allows you to display only the bone](https://x.com/EdwardUrena_h/status/2061559777575014798) |
| x | TopologicalBomb | ^59 c3 | [homelander nearly done. gotta do a bit of miscellaneous rigging and mesh joining](https://x.com/TopologicalBomb/status/2061386957444325399) |
| x | anishmoonka | ^52 c1 | [To build a young Arnold, the crew scanned an older one. They took a full-body 3D](https://x.com/anishmoonka/status/2061192494449152390) |
| x | LumaLabsAI | ^50 c6 | [To improve human life, AI systems must be able to help us improve the physical w](https://x.com/LumaLabsAI/status/2061460217616027961) |
| x | Arorea | ^39 c0 | [@Sphere_Deer For Toriel I used a 3d scan of my head to 3d model a base that was ](https://x.com/Arorea/status/2061392121232249247) |
| x | casey_sheep | ^38 c2 | [🔥 I've partnered with @FlippedNormals to launch a special FlipBox bundle! Get 11](https://x.com/casey_sheep/status/2061482329139532174) |
| x | corn724142 | ^24 c7 | [I am now 100% certain Michael Proctor planted taillight. I can also prove it wit](https://x.com/corn724142/status/2061567865535275124) |
| x | RadianceFields | ^20 c0 | [gaussian splatting can be black and white too https://t.co/UshqcIlDAo](https://x.com/RadianceFields/status/2061221116492861786) |
| x | bilawalsidhu | ^9 c0 | [go deeper into gaussian splatting: https://t.co/0LnbXw4oZo](https://x.com/bilawalsidhu/status/2061260973260865653) |
| x | MeshyAI | ^2 c0 | [@niftyisland 😍 This is soooooo cool 😍](https://x.com/MeshyAI/status/2061246669040369797) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Tioaoa2</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 27793 · 💬 49</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Tioaoa2/status/2061445532518653996">View @Tioaoa2 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Blender 5.2 has a new shader feature called &quot;thin wall&quot; which is designed for meshes which have no thickness (or very little). These can be anything from leaves, paper, tissues and some thin plastics ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Blender 5.2 introduces a dedicated 'thin wall' shader node for zero-thickness geometry — leaves, paper, tissue, thin plastic — giving accurate light transmission without modelling real volume.</dd>
      <dt>Why interesting</dt>
      <dd>Studios producing foliage, cloth, or paper assets in Blender for Unity/XR builds get physically correct translucency from one node instead of SSS or alpha-card hacks.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">On the next foliage or thin-surface asset pass in Blender, benchmark the thin wall node against current alpha/SSS workarounds for visual quality and render time.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Tioaoa2/status/2061445532518653996" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnimGaby</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1396 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnimGaby/status/2061071305634627949">View @AnimGaby on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“D4DJ as Murder drones some parts are off sync because daVinci is trolling me Some part I didn't include the background character because It will just destroy my blender lol anyways snow shader by @Ash”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Fan animator @AnimGaby shared a Blender/DaVinci Resolve fan animation combining D4DJ and Murder Drones, noting sync issues in DaVinci and that dense background characters crashed their Blender scene.</dd>
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
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 660 · 💬 24</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061134940813611505">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We treat 3d scanning like a tech demo, but it’s actually spatial memory capture. Damn near teleportation. A few hundred photos of my parent’s old home, and now it’s immortalized forever. 3d gaussian s”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer used RealityCapture + Luma AI (Litchfield) to create a 3D Gaussian splat of a physical location from a few hundred photos, framing photogrammetry as long-term spatial archiving.</dd>
      <dt>Why interesting</dt>
      <dd>The RealityCapture → Gaussian splat pipeline is now accessible enough for a solo dev weekend project, signaling a practical quality bar for XR/VR scene capture.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team can test the RealityCapture + Luma AI workflow on a real location to benchmark scan quality and export compatibility with Unity.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061134940813611505" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ashlee3dee</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 499 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ashlee3dee/status/2061195779952275511">View @ashlee3dee on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“stylized black hole vfx with geometry nodes :3 i will port this to unreal engine... soon https://t.co/bu98xUEYuO”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Artist @ashlee3dee built a stylized black hole VFX using Blender Geometry Nodes and is planning a port to Unreal Engine.</dd>
      <dt>Why interesting</dt>
      <dd>Geometry Nodes gives a procedural, non-destructive VFX workflow that ports to game engines — directly relevant to the studio's Unity/XR VFX pipeline.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Watch for the UE port drop; use the Geometry Nodes breakdown as a reference for stylized space/sci-fi VFX in the studio's Unity or Unreal projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ashlee3dee/status/2061195779952275511" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 482 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2061109917222920517">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“When your Unreal VFX project hits different… @IgorPontes breakdown his Sasuke-level Katon 🔥 with insane stylized effects. #vfx https://t.co/j4wFOeAnBm”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Igor Pontes released an Unreal Engine breakdown of anime-style stylized fire (Katon) VFX, showing particle, shader, and timing techniques behind the effect.</dd>
      <dt>Why interesting</dt>
      <dd>Stylized VFX breakdowns from Unreal map directly to Unity VFX Graph and Shader Graph — the artistic and technical principles transfer across engines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can pull this breakdown as a reference for anime-style elemental effects on any game or XR project using VFX Graph.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2061109917222920517" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DSkaale</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 306 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DSkaale/status/2061114844263117118">View @DSkaale on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just stepped inside my favorite movie locations on my Quest 3 🎬 Gaussian splatting + Standalone VR — Multi-renderer ordering (render-order key + depth tiebreak) - View-space distance (length to splat ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer rendered Gaussian-splat movie locations inside Quest 3 standalone using SplatBox (Unity), fixing splat sorting via view-space distance (length to splat center) plus render-order key with depth tiebreak.</dd>
      <dt>Why interesting</dt>
      <dd>The sorting fix — view-space length instead of raw z — is a documented accuracy bug in splat renderers; seeing it solved on standalone Quest 3 confirms the approach works without a PC tether.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity XR team can apply the same SplatBox render-order + view-space distance sort to any photogrammetry or location-capture scene being built for standalone headsets.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DSkaale/status/2061114844263117118" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DemNikoArt</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 285 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DemNikoArt/status/2061498924473487814">View @DemNikoArt on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bike Suspension Tutorial coming this week 😉 #b3d #blender #blender3d #rigging #tutorial https://t.co/XekTbKmhOc”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@DemNikoArt is releasing a Blender bike suspension rigging tutorial this week, focused on mechanical rig setups in Blender 3D.</dd>
      <dt>Why interesting</dt>
      <dd>Mechanical suspension rigging techniques transfer directly to vehicle and prop assets used in Unity games and XR scenes.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's 3D/Unity team can follow the tutorial and apply the suspension rig pattern to any mechanical vehicle asset in the pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DemNikoArt/status/2061498924473487814" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 79 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061450274011591084">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Honestly if we put this demo in a fancy XR headset, we’d call it jarvis. The future of 3d doesn’t involve the death of autocad, maya and blender. It turns those tools into a shared canvas of collabora”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Author reacts to an unspecified 3D demo, arguing AI agents will act as a collaboration layer on top of existing tools like Blender, Maya, and AutoCAD rather than replacing them.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061450274011591084" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
