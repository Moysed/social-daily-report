---
type: social-topic-report
date: '2026-06-15'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-15T04:54:27+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 28
salience: 0.5
sentiment: positive
confidence: 0.6
tags:
- gaussian-splatting
- blender
- unity-shaders
- photogrammetry
- geospatial-3d
- procedural-generation
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065879491843346432/img/Bg2eywsphAzYdYmZ.jpg
---

# 3D & Graphics — 2026-06-15

## TL;DR
- Google released a free browser flight sim built on its Photorealistic 3D Tiles, removing API-credit cost for web geospatial 3D apps [1].
- Gaussian Splatting shows up across multiple independent demos: product viz preserving fabric hairs (Blender → Lichtfeld Studio) [2], city-scale Apple Maps splats [10], a Blender sculpture composite [21], and quick iPhone scans [3].
- Unity URP shader tutorials are a steady stream this cycle: mobile snow coverage [5], gem [7], painterly post-process [15], and a gravitational-lensing black hole [17], plus a beginner VFX class [19].
- Meshy AI promotes a 'DDC Bridge' to export AI-generated meshes into Blender while keeping animations [28].
- AI procedural claims are demo-level and unverified: a 'Fable 5' real-time Unreal world generator built 'in a couple of hours' [12].

## What happened
The strongest cluster is capture/visualization. Google opened a free web flight simulator on its Photorealistic 3D Tiles, framed as removing API-credit cost for the many 3D-tiles web builds [1], while Apple Maps city-scale Gaussian splats drew praise [10]. Gaussian Splatting appears repeatedly: a Blender-to-Lichtfeld product visualization preserving fine fabric detail [2], a Blender + GS sculpture composite [21], and a fast iPhone scan with high-frame-rate tracking [3]. Scanning real people for game outfits (EVE) was also noted [4]. Separately, Blender remains the production hub for VFX and shaders — Stargate VFX with VDB explosions [9], a reworked Halo hull shader [14], emote inspection [6], and tutorials [11][13].

Unity URP shader content is the other recurring theme: mobile snow coverage [5], a Shader Graph gem [7], a painterly post-process [15], a black-hole lensing shader [17], and a live beginner VFX class [19]. On AI-assisted content, Meshy promoted a DDC Bridge for animation-preserving Blender export [27][28], and a 'Fable 5' procedural Unreal world generator was claimed [12]. Several high-engagement items are off-topic or banter — an AI video-editor repo list [8], a productivity-tools thread [20], an apparent LLM/satire post [16], and reply chatter [18][22][23][24][25][26].

## Why it matters (reasoning)
Gaussian Splatting is the clearest direction: independent, good-looking results from product viz [2] to phone scans [3] to city scale [10][21] suggest the capture side is maturing for asset and environment work. For a studio doing XR/VR, that lowers the cost of photoreal scene and product capture versus manual modeling. The gating issue — not addressed in any item — is runtime integration and performance of splats inside Unity/Unreal and on mobile/headset, so this remains capture/visualization rather than drop-in interactive assets. Google's free 3D-tiles web sim [1] matters second-order: it removes a recurring API cost and signals browser-based geospatial 3D is a supported path for web/mobile experiences. The Unity URP shader stream [5][7][15][17] is directly reusable craft knowledge for the games/edutech side, low cost to adopt. AI asset/world generation [12][28] could compress prototyping time, but the items are demos and marketing, not validated pipelines.

## Possibility
Likely: Gaussian Splatting keeps moving from novelty to routine capture for product viz and environment scanning, given the volume and quality of independent demos [2][3][10][21]. Plausible: more browser-based geospatial 3D apps appear now that Google offers a free, no-credit path on its 3D tiles [1]. Plausible but unverified: AI procedural and mesh tools (Fable 5 [12], Meshy DDC Bridge [28]) cut early asset/world setup time — treat the 'couple of hours' world-gen claim [12] as a demo until reproduced. Unlikely near-term: splats replacing mesh-based pipelines for interactive game content — none of the items show real-time GS running inside an engine at production performance.

## Org applicability — NDF DEV
1) Pilot a Gaussian Splatting capture workflow for XR product/environment viz — test the Blender → Lichtfeld path [2] and an iPhone scan [3] on one real client asset; verify how the result behaves once imported to Unity before committing (med). 2) Prototype a browser geospatial scene on Google's free 3D tiles for any web/mobile location-based feature, avoiding per-call API cost [1] (low-med). 3) Bookmark and reuse the URP shader techniques directly applicable to current Unity work — painterly post-process for stylized edutech/game looks [15], mobile-optimized snow [5], gem [7], lensing [17] (low). 4) Evaluate Meshy's DDC Bridge for AI-generated, animation-preserving assets into Blender as a prototyping shortcut [28] (med). Skip: the AI video-editor repo list [8], productivity-tools thread [20], the off-topic LLM/satire post [16], and the reply banter [18][22][23][24][25][26]. Do not budget around the unverified Fable 5 world-gen claim [12].

## Signals to Watch
- Blender + Lichtfeld Studio as a Gaussian Splatting product-viz pipeline [2]
- Free, no-API-credit geospatial 3D on Google Photorealistic 3D Tiles [1] and Apple Maps city splats [10]
- Meshy DDC Bridge — animation-preserving AI mesh export to Blender [28]
- Fable 5 procedural Unreal world claim — reproduce before trusting [12]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^1160 c23 | [Google got tired of all the vibe coded simulators built on 3d tiles and said - s](https://x.com/bilawalsidhu/status/2065834228818866255) |
| x | msteevie3d | ^349 c10 | [Wow, product visualization via Gaussian Splatting is mind blowing. 🤯 From @Blend](https://x.com/msteevie3d/status/2065879965602603119) |
| x | SadlyItsBradley | ^316 c16 | [Say hello to my fishy friend in high frame rate tracking! This is pretty damn im](https://x.com/SadlyItsBradley/status/2065974984258818512) |
| x | ScrubSquad115 | ^298 c0 | [1 year ago today, we learned that @Bambi_jesuis2 was one of the 3D scan models f](https://x.com/ScrubSquad115/status/2066239676457811997) |
| x | Sakura_Rabbiter | ^293 c2 | [Real-Time Snow Coverage on Mobile with URP #unity #shader #gamedev #VFX😊 https:/](https://x.com/Sakura_Rabbiter/status/2066170153159819717) |
| x | Glacetomic | ^238 c6 | [Completely forgot I can literally view all the emotes in blender if I want to, s](https://x.com/Glacetomic/status/2065791001483174393) |
| x | ushadersbible | ^235 c0 | [A simple gem shader you can create with Shader Graph in Unity 💎 Shaders, Compute](https://x.com/ushadersbible/status/2066242990759186678) |
| x | KanikaBK | ^177 c15 | [Here are 10 AI video editor GitHub repos worth bookmarking: 1. Shotcut https://t](https://x.com/KanikaBK/status/2065780534148731148) |
| x | venturepictures | ^173 c10 | [Little STARGATE test animation for 1) new hyperspace VFX 2) new asteroid / plane](https://x.com/venturepictures/status/2065967983655071928) |
| x | bilawalsidhu | ^142 c2 | [City scale 3d gaussian splats just hit different - well done apple maps](https://x.com/bilawalsidhu/status/2066175946831348094) |
| x | AckroseEdits | ^106 c20 | [More vfx highlights for @StanBrowney 🔥 -Blender -Ae and Pr pro https://t.co/awQe](https://x.com/AckroseEdits/status/2065728382869045435) |
| x | n1neshards | ^81 c15 | [This guy just built a full procedural world generator with real time Unreal Engi](https://x.com/n1neshards/status/2065904409356243293) |
| x | DemNikoArt | ^60 c1 | [EXTENDED TUTORIAL 🚲 Would you like to know more? ⚔️🪐🎖️ I have long versions for ](https://x.com/DemNikoArt/status/2066202654162747670) |
| x | adiri_3d | ^59 c1 | [Another day's progress, and I reworked the hull shader, lots more detail now :) ](https://x.com/adiri_3d/status/2065748564299706829) |
| x | jettelly | ^56 c0 | [This painterly shader uses post-processing in Unity URP to give 3D scenes the lo](https://x.com/jettelly/status/2065690632782582120) |
| x | multimodalart | ^51 c4 | [The municipality of Rio de Janeiro released Rio 3.5, a Qwen fine-tune that is to](https://x.com/multimodalart/status/2065947636054569125) |
| x | jettelly | ^40 c0 | [Check out this real-time black hole shader by consentantaneity, simulating gravi](https://x.com/jettelly/status/2066113427551240331) |
| x | bilawalsidhu | ^40 c7 | [So kids… what moral lesson has this fable taught us? https://t.co/JUQMyvYqpy](https://x.com/bilawalsidhu/status/2065800911776063555) |
| x | VFX_Therapy | ^38 c0 | [I’m conducting live vfx class in Unity for beginners on this Tuesday 8:30pm EST.](https://x.com/VFX_Therapy/status/2065905873126621305) |
| x | AramideOyekunle | ^30 c1 | [Productivity AI Tools: 1. https://t.co/zB10zBY60B – Writing like a human 2. http](https://x.com/AramideOyekunle/status/2065861778353926644) |
| x | blue_nile_3d | ^24 c1 | [Life in the city - sculpture made with gaussian splatting and Blender https://t.](https://x.com/blue_nile_3d/status/2065771922743496865) |
| x | bilawalsidhu | ^20 c0 | [@DavidSacks https://t.co/yJNFNsHrWl](https://x.com/bilawalsidhu/status/2065857687800123752) |
| x | bilawalsidhu | ^11 c0 | [@codetaur Pure visual umami](https://x.com/bilawalsidhu/status/2066000036240953836) |
| x | bilawalsidhu | ^6 c0 | [@APompliano @DavidSacks A new world indeed](https://x.com/bilawalsidhu/status/2065871927994913262) |
| x | bilawalsidhu | ^5 c0 | [@southpolesteve @DanielleFong Banger](https://x.com/bilawalsidhu/status/2065879703743795633) |
| x | bilawalsidhu | ^5 c2 | [@HarksenNiels Same with my confidence that I will be able to fly an f-16 if need](https://x.com/bilawalsidhu/status/2065869718251004109) |
| x | MeshyAI | ^0 c0 | [@tom_krikorian We'll check and let you know soon. Thanks for the feedback!](https://x.com/MeshyAI/status/2066364603920244806) |
| x | MeshyAI | ^0 c1 | [@tom_krikorian You can use Meshy DDC Bridge! It allows you to export your file t](https://x.com/MeshyAI/status/2066353974547226695) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1160 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065834228818866255">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Google got tired of all the vibe coded simulators built on 3d tiles and said - screw it, flight sim on web, free for all - no need to burn api credits. The deeper lore here is that flight sim has long”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google launched a free browser-based flight simulator built on Google Maps 3D Tiles, removing the need for API credits — previously this feature was hidden inside the legacy Google Earth Pro desktop app.</dd>
      <dt>Why interesting</dt>
      <dd>The studio can use Google Maps 3D Tiles for free interactive 3D environments in web/XR projects without worrying about API credit costs for simulation prototypes.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test the browser flight sim to assess 3D Tiles fidelity and load performance as a reference point for web-based 3D world projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2065834228818866255" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@msteevie3d</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 349 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/msteevie3d/status/2065879965602603119">View @msteevie3d on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow, product visualization via Gaussian Splatting is mind blowing. 🤯 From @Blender to @lichtfeldstudio , the details are crazy. It preserved everything so well, even the tiny hairs on the fabric! I ho”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A 3D artist captured a fabric product using 500 photos processed into a Gaussian Splat (2M splats, 50k iterations via IGS+ in Lichtfeld Studio) — the result preserves microscopic surface detail like individual fabric hairs.</dd>
      <dt>Why interesting</dt>
      <dd>Gaussian Splatting now delivers photorealistic product visualization from photos alone — a viable pipeline for XR/e-learning asset creation without manual 3D modeling.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a small test: shoot a studio prop or client product with 200–500 photos, process via IGS+ or Luma AI, and evaluate splat quality for XR scene assets.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/msteevie3d/status/2065879965602603119" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SadlyItsBradley</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 316 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SadlyItsBradley/status/2065974984258818512">View @SadlyItsBradley on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Say hello to my fishy friend in high frame rate tracking! This is pretty damn impressive for such a quick 3D scan (from my iPhone) https://t.co/vzXlKsFRW5”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@SadlyItsBradley shared a high frame rate 3D-tracked scan of a fish captured with an iPhone, demonstrating that mobile photogrammetry can produce convincing real-time-ready results in a short session.</dd>
      <dt>Why interesting</dt>
      <dd>iPhone-grade scanning now produces results usable in real-time contexts, which lowers the hardware bar for quick asset capture in XR/VR or Unity prototype pipelines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team can run a one-day trial scanning small physical props with an iPhone to gauge fit for rapid asset prototyping before committing to dedicated scanning hardware.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SadlyItsBradley/status/2065974984258818512" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ScrubSquad115</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 298 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ScrubSquad115/status/2066239676457811997">View @ScrubSquad115 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“1 year ago today, we learned that @Bambi_jesuis2 was one of the 3D scan models for EVE She shared Black Wave and Keyhole suit with us many other outfits were scanned in with Bambi but sadly didn't tak”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post commemorating that a specific person was used as a 3D scan model for the character EVE in Stellar Blade, shared on the game's anniversary.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ScrubSquad115/status/2066239676457811997" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Sakura_Rabbiter</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 293 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Sakura_Rabbiter/status/2066170153159819717">View @Sakura_Rabbiter on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Real-Time Snow Coverage on Mobile with URP #unity #shader #gamedev #VFX😊 https://t.co/0txae8ebtw Come and subscribe to my Fanbox to download this project https://t.co/sT4MYw51yi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@Sakura_Rabbiter released a real-time snow coverage shader for Unity URP targeting mobile, with the full project available for download on Fanbox.</dd>
      <dt>Why interesting</dt>
      <dd>A mobile-optimized URP snow shader with a downloadable project is a direct reference for environment or seasonal effects in the studio's Unity work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can pull the Fanbox project to study the shader technique before building any outdoor or seasonal scene.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Sakura_Rabbiter/status/2066170153159819717" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Glacetomic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 238 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Glacetomic/status/2065791001483174393">View @Glacetomic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Completely forgot I can literally view all the emotes in blender if I want to, so here's Remi without the heavy abstraction vfx. https://t.co/PHMwBbanoX”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A creator demonstrated that game character emotes can be imported and previewed directly in Blender, stripping away in-engine VFX to inspect the raw mesh and animation.</dd>
      <dt>Why interesting</dt>
      <dd>Blender as a lightweight inspection tool for game assets is a practical workflow tip — useful when debugging rigs or animations outside the game engine.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can apply the same approach — export FBX/glTF assets and inspect rigs or blend shapes in Blender before troubleshooting inside Unity.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Glacetomic/status/2065791001483174393" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ushadersbible</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 235 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ushadersbible/status/2066242990759186678">View @ushadersbible on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A simple gem shader you can create with Shader Graph in Unity 💎 Shaders, Compute Shaders, and Math for Graphics 🔗 https://t.co/MQP1nKiD0x #IndieDevSunday https://t.co/iHisMzpxRc”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@ushadersbible shared a step-by-step gem shader built with Unity Shader Graph, posted under #IndieDevSunday with a linked tutorial resource.</dd>
      <dt>Why interesting</dt>
      <dd>Shader Graph gem effects are directly applicable to Unity game and XR projects where visual polish on collectibles or UI gems matters.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can reference this Shader Graph setup as a reusable asset for gem or crystal visuals in current or upcoming game projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ushadersbible/status/2066242990759186678" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KanikaBK</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 177 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KanikaBK/status/2065780534148731148">View @KanikaBK on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here are 10 AI video editor GitHub repos worth bookmarking: 1. Shotcut https://t.co/avPrh2NmjC Most actively maintained open source video editor in 2026. 14K stars. Cross-platform with AI-assisted fea”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A curated list of 10 open-source AI video editor repos highlights Shotcut (14K stars, Apr 2026 release), Blender VSE, Kdenlive, and Alibaba's Wan2.1 text-to-video model (Apache 2.0, 1080p) as the standout tools in 2026.</dd>
      <dt>Why interesting</dt>
      <dd>Wan2.1 and Blender VSE give the studio free, production-grade video generation and compositing pipelines usable in XR/VR and e-learning content without licensing costs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test Wan2.1 locally for generating B-roll or cinematic cutscenes in e-learning and XR projects, and evaluate Blender VSE as a no-cost compositing step in the post-production pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KanikaBK/status/2065780534148731148" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
