---
type: social-topic-report
date: '2026-06-03'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-03T06:53:43+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 33
salience: 0.45
sentiment: neutral
confidence: 0.6
tags:
- blender
- unity
- shaders
- gaussian-splatting
- photogrammetry
- asset-pipeline
thumbnail: https://pbs.twimg.com/media/HJu5g4-WoAAkc5f.jpg
---

# 3D & Graphics — 2026-06-03

## TL;DR
- Blender 5.2 adds a "thin wall" shader option for meshes with no/low thickness — leaves, paper, tissue, thin plastics [1]; by far the day's highest-engagement item (~45k).
- Ken Deng released VFX Texture Lab, a free Unity tool for in-engine texture edits: mask cleanup, gradient mapping, channel packing [4].
- AI camera-path generation from photogrammetry trajectories spread into a creator trend [2][7][27], adjacent to Gaussian splatting/spatial capture work [26].
- FlippedNormals "FlipBox" bundle: 11 Blender add-ons + 1500+ assets for $30, targeting environments, procedural workflows, VFX, vegetation [13][18].
- Shared shader techniques: reflection-based outlines that avoid mesh duplication/stencils [21]; an Amplify Shader Editor trailing shader for Unity [11].

## What happened
The day's 3D feed is dominated by one Blender release note — a new "thin wall" shader feature in Blender 5.2 for meshes with little or no thickness such as leaves, paper, and thin plastics [1]. Beyond that, tooling items: a free Unity texture utility (VFX Texture Lab) for mask cleanup, gradient mapping, and channel packing without leaving the engine [4]; a $30 FlippedNormals add-on/asset bundle for Blender environment and procedural work [13][18]; and shared real-time shader techniques (reflection-based outlines [21], an Amplify trailing shader [11], a stylized water shader [18], UE5 Niagara VFX [22]).

## Why it matters (reasoning)
Most items are incremental tooling and technique sharing rather than platform shifts, but they map directly to asset-production cost. The Blender thin-wall shader [1] removes a common hack (double-sided geometry/manual translucency) for foliage and thin props, which are heavily used in both game and XR scenes. In-engine utilities like VFX Texture Lab [4] cut round-trips between Photoshop/Substance and Unity, shortening texture iteration. The photogrammetry-camera-path trend [2][7][27] and the Gaussian splatting talk [26] sit in the capture-to-engine pipeline: cheaper ways to turn real scenes and trajectories into usable 3D, which matters for XR experiences that need real-world environments. Second-order: as capture (splatting/NeRF/photogrammetry [24][26]) and AI camera generation mature, the bottleneck shifts from modeling to cleanup, retopo, and engine integration — exactly the manual steps these utilities target.

## Possibility
Likely: thin-wall-type shading and free in-engine texture tools become standard in foliage/prop pipelines, since both reduce well-known manual steps [1][4]. Plausible: Gaussian splatting continues moving from research/demos toward production XR capture, given continued conference attention [26] and adjacent photogrammetry accuracy work [24] — but engine-native splat rendering and editing remain immature, so adoption stays exploratory. Plausible: AI-generated camera paths feed into splat/video pipelines as a creator workflow [2][7][27], though most signal here is hype reposts, not shipped tools. No source states numeric probabilities, so none are given.

## Org applicability — NDF DEV
Low effort — install and trial VFX Texture Lab for Unity texture cleanup/channel packing in current game projects; it is free [4]. Low effort — evaluate the $30 FlippedNormals FlipBox bundle for environment/vegetation/procedural assets if it fills a near-term content gap [13][18]; verify license terms for commercial use before buying. Low/med — test Blender 5.2's thin-wall shader on foliage/paper/thin-plastic assets to retire double-sided-geometry hacks [1]. Med — prototype the reflection-based outline technique [21] for any stylized/toon Unity titles, comparing cost vs. inverted-hull outlines. Med/high (exploratory only) — assign a short spike on Gaussian splatting for XR environment capture, watching the Techweek talk and tracking engine-import maturity before committing [26][24]. Skip: the rigging/character/personal tutorials [3][5][6][9][16][19][20], the Amplify trailing shader unless you already license Amplify Shader Editor [11], and off-topic/novelty posts [25][29][33].

## Signals to Watch
- Engine-native Gaussian splatting import/edit for Unity/Unreal — gated by tooling maturity [26][24].
- Free in-engine art utilities (texture, VFX) trend in Unity, reducing DCC round-trips [4].
- AI camera-path/trajectory generation maturing from reposts into actual creator tools [2][7][27].
- Blender 5.2 shader additions (thin wall) and their game-engine export fidelity [1].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Tioaoa2 | ^45314 c92 | [Blender 5.2 has a new shader feature called "thin wall" which is designed for me](https://x.com/Tioaoa2/status/2061445532518653996) |
| x | bilawalsidhu | ^2675 c47 | [Well that escalated quickly 😂 Insane camera path generation harry! https://t.co/](https://x.com/bilawalsidhu/status/2061886480847450588) |
| x | DemNikoArt | ^596 c8 | [Bike Suspension Tutorial coming this week 😉 #b3d #blender #blender3d #rigging #t](https://x.com/DemNikoArt/status/2061498924473487814) |
| x | jettelly | ^227 c0 | [Technical Artist Ken Deng released VFX Texture Lab, a free Unity tool that lets ](https://x.com/jettelly/status/2061749670075150362) |
| x | TOAnimate_ | ^192 c0 | [Little tip that might save you: Don’t skip the basics if you don’t want everythi](https://x.com/TOAnimate_/status/2061810071927923134) |
| x | EdwardUrena_h | ^137 c1 | [One of the good things about this is that it allows you to display only the bone](https://x.com/EdwardUrena_h/status/2061559777575014798) |
| x | AIWarper | ^131 c12 | [Fun fact - I started this entire trend after seeing a fantastic post by @bilawal](https://x.com/AIWarper/status/2061884417757544600) |
| x | bilawalsidhu | ^123 c8 | [Honestly if we put this demo in a fancy XR headset, we’d call it jarvis. The fut](https://x.com/bilawalsidhu/status/2061450274011591084) |
| x | EdwardUrena_h | ^122 c0 | [I set out to see if it was possible to add a custom gizmo—and yes, it was; it to](https://x.com/EdwardUrena_h/status/2061539090198045116) |
| x | SD_F111 | ^111 c3 | [Niko N model update!! 3D work/rigging is done now to clean up weights and UV! Ni](https://x.com/SD_F111/status/2061918040850121207) |
| x | VFX_Therapy | ^95 c1 | [Absolute stunner: Dynamic trailing shader by @MetallCore999 in Amplify Shader Ed](https://x.com/VFX_Therapy/status/2061535622368833762) |
| x | FourBeats265635 | ^81 c2 | [@YottaMindset @mnolangray “Closely connected” seems like a real stretch. Being a](https://x.com/FourBeats265635/status/2061669439620215273) |
| x | casey_sheep | ^78 c2 | [🔥 I've partnered with @FlippedNormals to launch a special FlipBox bundle! Get 11](https://x.com/casey_sheep/status/2061482329139532174) |
| x | cgboost | ^76 c0 | [Learn how Martin Klekner made this sequence in Blender on our YouTube Channel. h](https://x.com/cgboost/status/2061748624178999569) |
| x | bilawalsidhu | ^73 c12 | [I see videos like this and get excited… it’s the old guard embracing new tech. T](https://x.com/bilawalsidhu/status/2061811752786944074) |
| x | TopologicalBomb | ^63 c3 | [homelander nearly done. gotta do a bit of miscellaneous rigging and mesh joining](https://x.com/TopologicalBomb/status/2061386957444325399) |
| x | LumaLabsAI | ^62 c9 | [To improve human life, AI systems must be able to help us improve the physical w](https://x.com/LumaLabsAI/status/2061460217616027961) |
| x | FlippedNormals | ^60 c0 | [This stylized water shader by Casey Sheep is included in our new Blender Add-Ons](https://x.com/FlippedNormals/status/2061810123350106393) |
| x | Arorea | ^49 c0 | [@Sphere_Deer For Toriel I used a 3d scan of my head to 3d model a base that was ](https://x.com/Arorea/status/2061392121232249247) |
| x | K_enzo1 | ^47 c5 | [Practice VFX/Anim: Me Port: https://t.co/xnTwH5Im8S #RobloxDev #robloxvfx #MoonA](https://x.com/K_enzo1/status/2061964402270597596) |
| x | ushadersbible | ^38 c1 | [This outline technique is achieved using reflection. What's the difference? For ](https://x.com/ushadersbible/status/2061663479300296851) |
| x | cghow_ | ^30 c0 | [Shadow Binding Curse in Unreal Engine 5 Niagara https://t.co/MNIt02YoVO https://](https://x.com/cghow_/status/2061808463727239678) |
| x | Gwamothy | ^24 c2 | [@agraybee You're telling me that you have devices that can, from a handheld devi](https://x.com/Gwamothy/status/2061541531094532147) |
| x | RemoteSens_MDPI | ^23 c1 | [Improving the Accuracy of #Forest #Structure Analysis by Consumer-Grade #UAV #Ph](https://x.com/RemoteSens_MDPI/status/2061442845597225332) |
| x | SoapIsTasty00 | ^21 c1 | [@passcoderonald Everyone should have to upload a 3D scan of their penis, both er](https://x.com/SoapIsTasty00/status/2061668092028346788) |
| x | RadianceFields | ^21 c0 | [I’m doing a talk tomorrow for @Techweek_ about gaussian splatting. Come by if yo](https://x.com/RadianceFields/status/2061663277893972082) |
| x | bilawalsidhu | ^8 c1 | [@kvickart This feels like an emergent behavior, but now that they know it I woul](https://x.com/bilawalsidhu/status/2061888185433461074) |
| x | bilawalsidhu | ^8 c0 | [@bfl_ai https://t.co/RvIs1vBT9s](https://x.com/bilawalsidhu/status/2061850142148313145) |
| x | bilawalsidhu | ^7 c0 | [@LKaci2721 Lol, these models are so smart yet sooo dumb](https://x.com/bilawalsidhu/status/2061974433347104800) |
| x | bilawalsidhu | ^6 c0 | [@xxunhuang @AlbyHojel Officially official; congrats Xun and team!](https://x.com/bilawalsidhu/status/2061971021465350525) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Tioaoa2</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 45314 · 💬 92</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Tioaoa2/status/2061445532518653996">View @Tioaoa2 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Blender 5.2 has a new shader feature called &quot;thin wall&quot; which is designed for meshes which have no thickness (or very little). These can be anything from leaves, paper, tissues and some thin plastics ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Blender 5.2 adds a native 'Thin Wall' shader node for single-sided meshes — leaves, paper, tissue, thin plastics — giving accurate SSS-like rendering without needing physical geometry thickness.</dd>
      <dt>Why interesting</dt>
      <dd>3D artists building game or XR assets in Blender can now render foliage, paper props, and fabric surfaces accurately without double-sided mesh hacks.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's Blender artists should test Thin Wall on foliage and thin-material assets to cut geometry complexity while keeping render quality.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Tioaoa2/status/2061445532518653996" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2675 · 💬 47</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061886480847450588">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Well that escalated quickly 😂 Insane camera path generation harry! https://t.co/ML4I0e2J6m”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google Gemini Omni (released May 2026) converts a hand-drawn camera path sketched over a photo or map into a rendered drone-POV video, demonstrated by ex-Google XR engineer Bilawal Sidhu.</dd>
      <dt>Why interesting</dt>
      <dd>Sketch-to-video camera paths cut previsualization time for XR fly-throughs and game cinematics without needing a 3D scene built first.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test Gemini Omni Flash by sketching camera paths over concept art or location references to generate previz clips for XR and game cinematic work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061886480847450588" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DemNikoArt</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 596 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DemNikoArt/status/2061498924473487814">View @DemNikoArt on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bike Suspension Tutorial coming this week 😉 #b3d #blender #blender3d #rigging #tutorial https://t.co/XekTbKmhOc”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@DemNikoArt is releasing a Blender bike suspension rigging tutorial this week, covering mechanical constraint-based rigging for vehicle assets.</dd>
      <dt>Why interesting</dt>
      <dd>Mechanical suspension rigging techniques in Blender translate directly to vehicle and prop asset creation for Unity games and XR/VR projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/XR team can bookmark this tutorial to expand the studio's mechanical rigging skill set for animated vehicle assets.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DemNikoArt/status/2061498924473487814" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 227 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2061749670075150362">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Technical Artist Ken Deng released VFX Texture Lab, a free Unity tool that lets artists make common texture edits, like mask cleanup, gradient mapping, and channel packing, without leaving the engine.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Technical Artist Ken Deng released VFX Texture Lab, a free Unity Editor tool for in-engine texture operations including mask cleanup, gradient mapping, and channel packing.</dd>
      <dt>Why interesting</dt>
      <dd>Cuts the texture iteration loop for VFX artists by removing round-trips to external tools like Photoshop or Substance.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can add VFX Texture Lab to the standard VFX/shader workflow and evaluate it on the next particle or environment art task.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2061749670075150362" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TOAnimate_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 192 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TOAnimate_/status/2061810071927923134">View @TOAnimate_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Little tip that might save you: Don’t skip the basics if you don’t want everything to feel confusing later 😹 Learn the basics so your rigs don’t break later #toanimate #rigging #blender https://t.co/I”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@TOAnimate_ posts a generic reminder to learn Blender rigging fundamentals before building complex rigs, with no specific technique or resource linked.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TOAnimate_/status/2061810071927923134" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EdwardUrena_h</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 137 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EdwardUrena_h/status/2061559777575014798">View @EdwardUrena_h on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One of the good things about this is that it allows you to display only the bones you want. #blender #b3d #rig #rigging #animation https://t.co/9vlBmIQChg”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender rigging tip demonstrates how to toggle visibility per bone, letting animators isolate only the bones relevant to the current task.</dd>
      <dt>Why interesting</dt>
      <dd>Selective bone visibility cuts viewport clutter on complex characters, directly speeding up animation iteration for Unity game assets.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's 3D animators can use this bone layer technique in Blender to isolate facial or limb rigs when preparing character assets for Unity.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EdwardUrena_h/status/2061559777575014798" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AIWarper</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 131 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AIWarper/status/2061884417757544600">View @AIWarper on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fun fact - I started this entire trend after seeing a fantastic post by @bilawalsidhu using photogrammetry camera trajectories Now look at how far it’s gone 😂”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@AIWarper claims credit for popularizing a trend in AI video/image generation using photogrammetry-style camera trajectories, inspired by a post from @bilawalsidhu.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AIWarper/status/2061884417757544600" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 123 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2061450274011591084">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Honestly if we put this demo in a fancy XR headset, we’d call it jarvis. The future of 3d doesn’t involve the death of autocad, maya and blender. It turns those tools into a shared canvas of collabora”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer @bilawalsidhu argues AI agents won't kill AutoCAD, Maya, or Blender — they'll turn those tools into shared collaborative canvases, citing a demo they'd label 'Jarvis' inside an XR headset.</dd>
      <dt>Why interesting</dt>
      <dd>For a team shipping XR/VR and Unity content, this framing positions AI agents as pipeline accelerators inside existing 3D tools — not a platform switch, just an evolution of current tooling.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Track AI agent plugins emerging for Blender and Maya (e.g. scene generation, rigging assist) and pilot one on a low-stakes XR asset to assess real workflow gain.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2061450274011591084" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
