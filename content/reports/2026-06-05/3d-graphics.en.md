---
type: social-topic-report
date: '2026-06-05'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-05T03:32:24+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 37
salience: 0.68
sentiment: mixed
confidence: 0.58
tags:
- gaussian-splatting
- photogrammetry
- blender
- shaders
- asset-pipeline
- webxr
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2062164703879540736/img/YjSQE5hPP5vo0ERh.jpg
---

# 3D & Graphics — 2026-06-05

## TL;DR
- PlayCanvas's SuperSplat (free, open source) streamed a 24-million-Gaussian scan live to a web browser with near-instant load [3] — web-native delivery, not just desktop viewers.
- Gaussian Splatting research cluster landed the same day: HiGS hierarchical real-time rendering [21], FreeStreamGS feed-forward from unposed streaming inputs [31], ZipSplat pose-free in under a second [33], and TripoSplat image-to-3D Gaussian [32].
- Photogrammetry tooling matured on the capture side: KIRI Engine shipped a Featureless Object Scan Mode for glossy/monochrome objects that break feature matching [14], plus a 20-second Blender node setup for more realistic scan renders [30].
- Practical scan-to-game-ready pipeline (decimate, re-UV, bake details) remains the standard workflow [1]; a AAA title disclosed laser scanning + photogrammetry in production [4].
- Counter-signal: a popular post blames photogrammetry for 130GB game installs [7] — a real cost for mobile/size-constrained titles.

## What happened
3D Gaussian Splatting dominated the day across tooling and research. SuperSplat (PlayCanvas) demonstrated a 24M-Gaussian scan streaming live to a browser with near-instant load [3], and a real-estate firm rebuilt an unbuilt development as an explorable splat for prospective buyers [11]. Multiple papers/releases pushed splatting toward faster, pose-free capture: HiGS two-scale hierarchical rendering [21], FreeStreamGS online feed-forward from unposed streaming input [31], ZipSplat (fewer Gaussians, pose-free, sub-second) [33], and TripoSplat image-to-3D [32], with an interactive GS generation demo [13]. On photogrammetry, KIRI Engine added a Featureless Object Scan Mode for glossy/textureless surfaces [14] and a Blender render-realism node setup [30]; a scan-to-game-ready pipeline of decimation, new UVs, and detail baking was highlighted [1], while a AAA project confirmed laser scanning + photogrammetry use [4].

## Why it matters (reasoning)
Two trends converge for the studio's portfolio. First, splatting is moving from research demos to web-deliverable assets [3][11]: streaming 24M Gaussians to a browser makes photoreal 3D viable for web and XR experiences without heavyweight clients. Second, the new feed-forward, pose-free methods [31][33] target the biggest pain in capture pipelines — the slow, fragile pose-estimation/COLMAP step — which could shorten the path from phone scan to usable asset. The counterweight is asset weight: the photogrammetry-bloat critique [7] is a genuine second-order cost, since raw scanned detail inflates install size, a direct constraint for mobile games. Splatting and the scan-to-game-ready bake workflow [1] partly answer this by converting captures into controllable, decimated geometry or compact Gaussian representations [33] rather than 4K texture sets everywhere.

## Possibility
Likely: web-based splat viewers like SuperSplat keep improving streaming/scale, making photoreal 3D a practical web/XR delivery format within months [3][11]. Plausible: pose-free feed-forward splatting [31][33] and image-to-3D [32][24] reach production-grade quality for background/prop generation, but most items are demos or unbenchmarked papers, so quality and licensing remain unproven. Plausible: KIRI's featureless-object mode [14] closes a known gap for scanning glossy props, useful for hard-surface assets. Unlikely (near-term): splatting fully replaces mesh-based pipelines for animated game characters — current evidence is static-scene capture and rendering, not rigged deformable assets. No source gives numeric probabilities.

## Org applicability — NDF DEV
1) Pilot SuperSplat/PlayCanvas for web-delivered 3D scans in XR and web projects; the real-estate walkthrough pattern [11] maps directly to client visualization work — effort low/med [3][11]. 2) Add KIRI Engine to the capture toolkit: test Featureless Object Scan Mode for glossy props [14] and adopt the Blender scan-render node setup [30] — effort low. 3) Standardize the scan-to-game-ready bake (decimate → re-UV → bake) as a documented pipeline step [1], and budget install size against the photogrammetry-bloat risk for mobile titles [7] — effort low/med. 4) Reuse the Unity URP/ShaderGraph shader references (dissolve [10], potion [26]) and Blender Shaders Plus addon [9] for VFX tasks — effort low. 5) If any project uses Unreal, note UE5.8 Niagara memory/speed gains for VFX [8] — effort low. Skip for now: feed-forward GS papers as production tools (track only, unbenchmarked) [31][33]; generative video/image hype items [25][29][34]; and non-applicable posts (OSINT ceiling [2], furry art [23], NYC meetup [35]).

## Signals to Watch
- Web-native splat streaming scale and load times — SuperSplat's 24M-Gaussian browser demo sets a new bar [3].
- Pose-free / feed-forward splatting maturing toward removing the COLMAP step [31][33].
- Image-to-3D asset generation for game props (TripoSplat [32], Meshy style-consistent towns [24]).
- Install-size discipline as photogrammetry/scan use grows, especially for mobile [7].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | JasozzGames | ^1326 c16 | [I'm really addicted to this 3D-scan-to-game-ready-asset pipeline! Just a few rou](https://x.com/JasozzGames/status/2062165225588089172) |
| x | bilawalsidhu | ^1255 c34 | [Gosh I love the OSINT community. This project throws every plane flying overhead](https://x.com/bilawalsidhu/status/2062527676557001015) |
| x | playcanvas | ^698 c22 | [🚀 Major upgrades just landed in SuperSplat, the free and open source platform fo](https://x.com/playcanvas/status/2062165374120894862) |
| x | _YuriP__ | ^556 c4 | [• Development started in 2020 • Lead character designer is Yusuke Kozaki (Fire E](https://x.com/_YuriP__/status/2062605291485540393) |
| x | VFX_Therapy | ^361 c2 | [Amazing procedurally generated real-time cloud shader created by @HugoChenin. #u](https://x.com/VFX_Therapy/status/2062231883384258909) |
| x | jettelly | ^287 c2 | [Developer jakubiee made this simple head shader for Unreal Engine 5, experimenti](https://x.com/jettelly/status/2062081858154750016) |
| x | TheVicious_One | ^231 c22 | [Hot take incoming: Photogrammetry is why games are 130GB We don't need to see la](https://x.com/TheVicious_One/status/2062204594185228557) |
| x | RedefineFX | ^219 c4 | [Unreal Engine 5.8 brings memory and speed optimizations for Niagara, allowing fo](https://x.com/RedefineFX/status/2062144965472313446) |
| x | filip_animation | ^190 c1 | [My most used Blender addons #4: - Shaders Plus by SMOUSE Glass, water, oily meta](https://x.com/filip_animation/status/2062619776153764230) |
| x | VFX_Therapy | ^152 c0 | [Dissolve Shader = Interactive edge glow + world space control. Perfect for enemy](https://x.com/VFX_Therapy/status/2062607977186738307) |
| x | AurelienCa80656 | ^148 c7 | [A real estate project recreated in Gaussian Splatting. Future buyers can freely ](https://x.com/AurelienCa80656/status/2062053609102008532) |
| x | mweinbach | ^126 c6 | [I keep thinking about Apple’s U1 chip and the idea of understanding 3D space wit](https://x.com/mweinbach/status/2062255347608236229) |
| x | tom_doerr | ^116 c0 | [Interactive 3D generation with Gaussian Splatting https://t.co/eKRLRxxvVN https:](https://x.com/tom_doerr/status/2062467994786099421) |
| x | KIRI_Engine_App | ^112 c2 | [Featureless objects break most photogrammetry pipelines. Glossy, monochrome, no ](https://x.com/KIRI_Engine_App/status/2062089405741854822) |
| x | DemNikoArt | ^111 c2 | [🚨 NEW TUTORIAL IS OUT NOW! How to rig a Bike Suspension in Blender. 🔗 below #b3d](https://x.com/DemNikoArt/status/2062589493710934176) |
| x | SciTechera | ^111 c10 | [Wow. That's cool. Researchers just released World, an open-source Unreal Engine ](https://x.com/SciTechera/status/2062554345087041916) |
| x | 3DxDEV7 | ^73 c2 | [Take a look at this 👀 A procedural robot character creator for Blender with pres](https://x.com/3DxDEV7/status/2062247832321417594) |
| x | Mix3Design | ^73 c1 | [I will have a big announcement in the upcoming hours all the blender 3d artists ](https://x.com/Mix3Design/status/2062654531888910756) |
| x | ChurchillModels | ^68 c1 | [As usual, this model was made using acrylic, styrene, brass, and 3D printed part](https://x.com/ChurchillModels/status/2062462671509709013) |
| x | Rahll | ^64 c3 | [I agree with your general sentiment, but to be clear, a lot of what you're descr](https://x.com/Rahll/status/2062272983499260229) |
| x | janusch_patas | ^62 c2 | [HiGS: A Hierarchical Rendering Architecture for Real-Time 3D Gaussian Splatting ](https://x.com/janusch_patas/status/2062064390136795517) |
| x | multimodalart | ^60 c5 | [Ideogram 4 not only revamped their model to the best they built yet, but also th](https://x.com/multimodalart/status/2062210597148930139) |
| x | FoxibikiN | ^58 c1 | [(HD) Chillet &amp; Chill 🩵Chillet made by @furromantic ❄️Beau OC made by @miauha](https://x.com/FoxibikiN/status/2062652783975608633) |
| x | MeshyAI | ^53 c5 | [Build a 3D tiny town, block by block. Meshy keeps the style consistent across as](https://x.com/MeshyAI/status/2062121498207563920) |
| x | auqibhabib | ^52 c18 | [Made with seedance 2.0 + GPT Image 2 on @yapper_so Prompt. @image1 mage1 fights ](https://x.com/auqibhabib/status/2062599264807833617) |
| x | jettelly | ^49 c1 | [Technical Artist Miriam Martin Sánchez showed the breakdown behind her recent re](https://x.com/jettelly/status/2062489553152180629) |
| x | nodesandnoodles | ^46 c0 | [Turbulent gives you detailed water effects from a simple plane and a material. D](https://x.com/nodesandnoodles/status/2062394985689874596) |
| x | mweinbach | ^39 c2 | [You can then extend to an ecosystem. If you want to know where your AirTags are ](https://x.com/mweinbach/status/2062255381645074904) |
| x | bilawalsidhu | ^38 c5 | [First Aronofsky, then Scorsese, and now Gareth Edwards. Generative media has bee](https://x.com/bilawalsidhu/status/2062358867510440354) |
| x | KIRI_Engine_App | ^31 c1 | [It only takes 20 seconds to make your 3D scan renders more realistic Save this B](https://x.com/KIRI_Engine_App/status/2062479019023765643) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@JasozzGames</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1326 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/JasozzGames/status/2062165225588089172">View @JasozzGames on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm really addicted to this 3D-scan-to-game-ready-asset pipeline! Just a few rounds of decimation, new UVs, and then bake the details #gamedev #blender https://t.co/bAmx8JlHlM”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An indie dev shares a photogrammetry-to-game-ready pipeline using decimation, UV remapping, and bake in Blender to convert 3D scans into optimized assets.</dd>
      <dt>Why interesting</dt>
      <dd>This is a practical, low-cost way to produce high-fidelity assets for Unity games or XR scenes without manual sculpting.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can trial this scan-decimate-bake workflow on physical props to speed up asset creation for game or XR projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/JasozzGames/status/2062165225588089172" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1255 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2062527676557001015">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gosh I love the OSINT community. This project throws every plane flying overhead onto your ceiling in near real time – decoded from a cheap radio, w/ live stars and the ISS behind it. Falling asleep u”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A hobbyist project decodes live ADS-B signals from a cheap SDR radio and projects real-time plane positions, stars, and the ISS onto a ceiling as an ambient sky map.</dd>
      <dt>Why interesting</dt>
      <dd>The ambient ceiling projection pattern — live data layered over a star map — is a strong interaction concept for XR/VR installations or interactive exhibits.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR team can prototype this ambient data-layer pattern using ADS-B open feeds + a star map API as a ceiling-mounted XR installation demo.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2062527676557001015" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@playcanvas</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 698 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/playcanvas/status/2062165374120894862">View @playcanvas on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚀 Major upgrades just landed in SuperSplat, the free and open source platform for 3D Gaussian splatting. Here is a 24-MILLION-Gaussian scan streaming live to a web browser. Near instant load time. Sol”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>SuperSplat (PlayCanvas's open-source Gaussian splat editor) shipped a WebGPU compute renderer with automatic LOD streaming, hitting 60 fps on a 24-million-Gaussian scene in-browser with near-instant load.</dd>
      <dt>Why interesting</dt>
      <dd>WebGPU-based Gaussian splat streaming at 60 fps in-browser is now production-viable — directly relevant to XR/VR and web 3D scanning workflows.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Evaluate SuperSplat's WebGPU renderer for the studio's web-based 3D or XR projects that involve real-world scans or photorealistic environments.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/playcanvas/status/2062165374120894862" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@_YuriP__</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 556 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/_YuriP__/status/2062605291485540393">View @_YuriP__ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“• Development started in 2020 • Lead character designer is Yusuke Kozaki (Fire Emblem Awakening/Fates/Heroes) • Laser scanning and photogrammetry • Developed their own sound engine with 7.1.4 audio • ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A game project (dev since 2020, Yusuke Kozaki on characters) used photogrammetry, laser scanning, and a custom 7.1.4 spatial audio engine; cockpit cutscenes referenced Top Gun Maverick.</dd>
      <dt>Why interesting</dt>
      <dd>Photogrammetry for characters and a bespoke spatial audio engine are techniques applicable to high-fidelity Unity or XR projects the studio targets.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Evaluate a photogrammetry pipeline (RealityCapture or Metashape) for XR character or environment captures — this AAA production confirms the workflow scales.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/_YuriP__/status/2062605291485540393" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 361 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2062231883384258909">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazing procedurally generated real-time cloud shader created by @HugoChenin. #unreal #gamedev https://t.co/5cVXjkgd7J”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Hugo Chenin published a real-time procedural cloud shader built in Unreal Engine, shared as a visual demo clip on X.</dd>
      <dt>Why interesting</dt>
      <dd>Real-time procedural clouds are a recurring need in open-world and XR scenes; a working Unreal implementation confirms the technique is achievable without baked textures.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can study Chenin's procedural noise approach and port the core shader logic to Unity Shader Graph or HLSL for sky/environment rendering.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2062231883384258909" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 287 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2062081858154750016">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer jakubiee made this simple head shader for Unreal Engine 5, experimenting with ambient occlusion to create more interesting facial shading. 🎭 See more: https://t.co/3GacKh8pFn #UnrealEngine #”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer jakubiee built a head shader in Unreal Engine 5 that uses ambient occlusion to add depth and character to facial shading.</dd>
      <dt>Why interesting</dt>
      <dd>A minimal AO-driven face shader is a practical reference for any team doing character work in UE5 — shows what's achievable with a focused single-pass approach.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Review jakubiee's shader source for AO technique details that could apply to NPC or avatar materials in the studio's UE5 projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2062081858154750016" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheVicious_One</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 231 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheVicious_One/status/2062204594185228557">View @TheVicious_One on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hot take incoming: Photogrammetry is why games are 130GB We don't need to see laundry in 4k”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A game dev opinion post arguing that photogrammetry (scanning real objects into high-res 3D assets) is the primary driver of 100GB+ game install sizes, not gameplay content.</dd>
      <dt>Why interesting</dt>
      <dd>Unity teams using photogrammetry assets face the same tradeoff — scan fidelity inflates build size, which hurts distribution, load times, and storage on mobile or XR platforms.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Set texture budget limits per asset category in Unity projects early — flag photogrammetry assets for LOD and compression review before they accumulate in the build.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheVicious_One/status/2062204594185228557" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RedefineFX</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 219 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RedefineFX/status/2062144965472313446">View @RedefineFX on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Unreal Engine 5.8 brings memory and speed optimizations for Niagara, allowing for bigger and more detailed VFX simulations that run in real-time. https://t.co/YhsZW0v0zm”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Unreal Engine 5.8 reduces memory usage and improves runtime speed in Niagara, enabling larger and more detailed real-time VFX simulations.</dd>
      <dt>Why interesting</dt>
      <dd>Studios doing XR/VR or real-time 3D in Unreal Engine can now push more complex particle effects without hitting previous performance ceilings.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">For any Unreal Engine projects in the studio, evaluate UE 5.8 Niagara on scenes that previously required baked or stripped-down VFX.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RedefineFX/status/2062144965472313446" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
