---
type: social-topic-report
date: '2026-06-14'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-14T15:39:43+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 33
salience: 0.55
sentiment: mixed
confidence: 0.55
tags:
- gaussian-splatting
- photogrammetry
- image-to-3d
- blender
- unity-urp
- procedural-generation
thumbnail: https://pbs.twimg.com/ext_tw_video_thumb/1856725024968753153/pu/img/k_Non4U2lQsIvWE1.jpg
---

# 3D & Graphics — 2026-06-14

## TL;DR
- Google reportedly opened a free, web-based flight sim built on its Photorealistic 3D Tiles, framed as no longer needing paid API credits for 3D-tile simulators [1]; Apple Maps is shipping city-scale Gaussian splats [29].
- A tool referenced as 'Fable 5' is being used to generate procedural worlds rendered in real-time Unreal Engine, reportedly assembled in 'a couple of hours' [2][7][12] — demo claims, not verified output.
- Gaussian Splatting is moving into product visualization via a Blender → Lichtfeld Studio path that preserves fine detail like fabric hairs [5], and into sculpture/scene work [23].
- Image-to-3D model stack is consolidating: TripoSR, Microsoft TRELLIS, Hunyuan3D 2.1, Nerfstudio, and 3DGS offered through GPU cloud tooling [13]; fast iPhone scans with high-frame-rate tracking shown [3][10].
- Production-ready Unity URP shader techniques surfaced: mobile real-time snow coverage [15] and a painterly post-process look [16].

## What happened
Highest-engagement signal is geospatial: a claim that Google released a free web flight simulator on its Photorealistic 3D Tiles so developers stop burning API credits [1], echoed by related Google Earth/throwback posts [20][24][27], plus Apple Maps shipping city-scale 3D Gaussian splats [29]. A second cluster centers on a tool called 'Fable 5' for procedural world generation rendered in Unreal Engine, with multiple posts describing full landscapes, lighting, and detail produced quickly [2][7][12][18]. A third cluster is asset-capture and generation: Gaussian Splatting for product viz from Blender [5] and sculpture [23]; image-to-3D pipelines (TripoSR, TRELLIS, Hunyuan3D 2.1, Nerfstudio, 3DGS) via GPU cloud [13]; and quick iPhone photogrammetry [3][10]. Blender remains the common DCC for VFX and shader work [4][8][9][11][14], while Unity URP shader breakdowns address mobile snow [15] and painterly post-processing [16], with a beginner Unity VFX class advertised [19]. Several items are off-topic noise: an LLM fine-tune [17], AI video-editor and productivity lists [6][21], and unrelated news [22].

## Why it matters (reasoning)
Two trends matter for the studio. First, capture-to-asset is getting cheaper: image-to-3D and phone-based splatting/photogrammetry [3][10][13] cut the cost of generating reference meshes and props, and splatting now preserves enough detail for product-grade visuals [5]. That shifts effort from modeling toward cleanup (topology, UVs, runtime rendering) rather than removing it. Second, platform-owned 3D data is becoming directly consumable on the web: if Google's 3D Tiles flight sim is genuinely free [1] and Apple is exposing city-scale splats [29], geospatial XR and web/edutech demos can be built without per-call API cost — but 'free' needs license verification before any product dependency. The 'Fable 5' procedural-to-Unreal claims [2][7][12] point at faster world prototyping, yet the same author's ironic 'what moral lesson has this fable taught us' [18] is a fair caution: short demo timelines rarely equal shippable, controllable assets.

## Possibility
Likely: Gaussian Splatting keeps moving from novelty to production for product viz and environment capture, given working Blender/studio-tool integration [5][23] and platform adoption by Apple [29]. Plausible: image-to-3D (TRELLIS, Hunyuan3D 2.1) becomes a standard greyboxing/prototyping step [13], though production still needs manual retopo and UVs. Plausible: free or low-cost web 3D Tiles enables geospatial web/XR and edutech demos [1][29], conditional on licensing terms. Unlikely near-term: a single procedural tool ('Fable 5') producing shippable Unreal worlds without manual rework [2][7][12]; current evidence is unverified demos and one author signals skepticism [18]. No source states numeric probabilities.

## Org applicability — NDF DEV
1) Run a quick spike on image-to-3D for prototype/XR props using TRELLIS and Hunyuan3D 2.1; measure mesh quality and cleanup time before committing — effort low/med [13]. 2) Pilot the Blender → Gaussian Splatting path for a product-viz or XR capture deliverable, and confirm runtime playback (Unity 3DGS plugin) before quoting it to clients — effort med [5][23][29]. 3) Add iPhone photogrammetry/scan to the reference-capture workflow for fast scene/prop reference — effort low [3][10]. 4) Lift the Unity URP shader techniques directly into current titles: mobile snow coverage and painterly post-process are URP-native and portfolio-relevant — effort low [15][16]. 5) Verify Google Photorealistic 3D Tiles licensing/cost terms before designing any geospatial web or edutech feature around 'free' access — effort low to check, med to build [1][29]. Skip: betting on 'Fable 5' procedural-to-Unreal for production until output is reproducible and inspectable [2][7][12]; ignore off-topic items [17][22][6][21].

## Signals to Watch
- Confirm whether Google's web flight sim / 3D Tiles access is genuinely free and its license terms [1][29].
- Apple Maps city-scale 3D Gaussian splats — watch for SDK/runtime access for third-party apps [29].
- Image-to-3D stack maturing (TRELLIS, Hunyuan3D 2.1) — track production-readiness of topology/UVs [13].
- 'Fable 5' procedural-in-Unreal claims — watch for reproducible, controllable results vs. one-off demos [12][18].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^1088 c22 | [Google got tired of all the vibe coded simulators built on 3d tiles and said - s](https://x.com/bilawalsidhu/status/2065834228818866255) |
| x | bilawalsidhu | ^846 c18 | [Someone needs to throw fable 5 at the OG of procedural 3D generation (houdini) a](https://x.com/bilawalsidhu/status/2065457916405072127) |
| x | SadlyItsBradley | ^240 c12 | [Say hello to my fishy friend in high frame rate tracking! This is pretty damn im](https://x.com/SadlyItsBradley/status/2065974984258818512) |
| x | Glacetomic | ^235 c6 | [Completely forgot I can literally view all the emotes in blender if I want to, s](https://x.com/Glacetomic/status/2065791001483174393) |
| x | msteevie3d | ^221 c7 | [Wow, product visualization via Gaussian Splatting is mind blowing. 🤯 From @Blend](https://x.com/msteevie3d/status/2065879965602603119) |
| x | KanikaBK | ^169 c15 | [Here are 10 AI video editor GitHub repos worth bookmarking: 1. Shotcut https://t](https://x.com/KanikaBK/status/2065780534148731148) |
| x | _vmlops | ^152 c6 | [Fable 5 tackling procedural world generation and rendering in Unreal Engine is w](https://x.com/_vmlops/status/2065619237788586086) |
| x | venturepictures | ^137 c8 | [Little STARGATE test animation for 1) new hyperspace VFX 2) new asteroid / plane](https://x.com/venturepictures/status/2065967983655071928) |
| x | AckroseEdits | ^99 c17 | [More vfx highlights for @StanBrowney 🔥 -Blender -Ae and Pr pro https://t.co/awQe](https://x.com/AckroseEdits/status/2065728382869045435) |
| x | MiladKambari | ^90 c0 | [3d scan..... #animation #b3d #blender3d #UnrealEngine #SubstancePainter #gamedev](https://x.com/MiladKambari/status/2065454231717372276) |
| x | AKantemirov | ^84 c4 | [I should keep working on my model, but these procedural textures from @noaxdesig](https://x.com/AKantemirov/status/2065605342206058857) |
| x | n1neshards | ^75 c15 | [This guy just built a full procedural world generator with real time Unreal Engi](https://x.com/n1neshards/status/2065904409356243293) |
| x | clore_ai | ^63 c35 | [Create detailed 3D models from images using https://t.co/tS1YgkSXYM's GPU-powere](https://x.com/clore_ai/status/2065457183811092985) |
| x | adiri_3d | ^54 c1 | [Another day's progress, and I reworked the hull shader, lots more detail now :) ](https://x.com/adiri_3d/status/2065748564299706829) |
| x | Sakura_Rabbiter | ^49 c1 | [Real-Time Snow Coverage on Mobile with URP #unity #shader #gamedev #VFX😊 https:/](https://x.com/Sakura_Rabbiter/status/2066170153159819717) |
| x | jettelly | ^47 c0 | [This painterly shader uses post-processing in Unity URP to give 3D scenes the lo](https://x.com/jettelly/status/2065690632782582120) |
| x | multimodalart | ^45 c2 | [The municipality of Rio de Janeiro released Rio 3.5, a Qwen fine-tune that is to](https://x.com/multimodalart/status/2065947636054569125) |
| x | bilawalsidhu | ^40 c7 | [So kids… what moral lesson has this fable taught us? https://t.co/JUQMyvYqpy](https://x.com/bilawalsidhu/status/2065800911776063555) |
| x | VFX_Therapy | ^32 c0 | [I’m conducting live vfx class in Unity for beginners on this Tuesday 8:30pm EST.](https://x.com/VFX_Therapy/status/2065905873126621305) |
| x | bilawalsidhu | ^30 c0 | [@googleearth Now this is a real throwback! LFG](https://x.com/bilawalsidhu/status/2065452301121179709) |
| x | AramideOyekunle | ^29 c1 | [Productivity AI Tools: 1. https://t.co/zB10zBY60B – Writing like a human 2. http](https://x.com/AramideOyekunle/status/2065861778353926644) |
| x | SamuelBaker_B | ^25 c9 | [1/10: RDF/M23 ran two industrial-scale forced recruitment camps in occupied east](https://x.com/SamuelBaker_B/status/2065513894542520814) |
| x | blue_nile_3d | ^24 c1 | [Life in the city - sculpture made with gaussian splatting and Blender https://t.](https://x.com/blue_nile_3d/status/2065771922743496865) |
| x | bilawalsidhu | ^24 c10 | [We live in interesting times in the foothills of the singularity; this is perhap](https://x.com/bilawalsidhu/status/2065616112914505772) |
| x | EmpressTrash | ^20 c5 | [Cycladic Venus ~~~ 1 week open edition for @panelhausapp artist in residency on ](https://x.com/EmpressTrash/status/2065623586585383307) |
| x | bilawalsidhu | ^19 c0 | [@DavidSacks https://t.co/yJNFNsHrWl](https://x.com/bilawalsidhu/status/2065857687800123752) |
| x | bilawalsidhu | ^16 c1 | [Genuinely amazing to spend time with some of the foremost creative technologists](https://x.com/bilawalsidhu/status/2065565442983309560) |
| x | multimodalart | ^16 c1 | [Try it out here! 🤗https://t.co/SD2aiXQG0a](https://x.com/multimodalart/status/2065558377669742941) |
| x | bilawalsidhu | ^10 c2 | [City scale 3d gaussian splats just hit different - well done apple maps](https://x.com/bilawalsidhu/status/2066175946831348094) |
| x | bilawalsidhu | ^6 c0 | [@codetaur Pure visual umami](https://x.com/bilawalsidhu/status/2066000036240953836) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1088 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065834228818866255">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Google got tired of all the vibe coded simulators built on 3d tiles and said - screw it, flight sim on web, free for all - no need to burn api credits. The deeper lore here is that flight sim has long”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google launched a free in-browser flight simulator powered by Google Earth's 3D Tiles — no Maps API key required — resurrecting a hidden easter egg from the legacy Google Earth Pro desktop app.</dd>
      <dt>Why interesting</dt>
      <dd>Confirms Google's 3D Tiles can drive real-time interactive 3D in a browser at consumer scale — a useful capability ceiling check for any web or XR project using the same stack.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run the web flight sim to observe rendering performance and UX patterns — use it as a free reference baseline when scoping web-based 3D or XR features for the studio.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2065834228818866255" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 846 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065457916405072127">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Someone needs to throw fable 5 at the OG of procedural 3D generation (houdini) and render it all in unreal engine https://t.co/QvVuHNhll7”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user casually suggests that Fable 5 game assets should be generated procedurally in Houdini and rendered in Unreal Engine — no announcement, release, or technical detail attached.</dd>
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
    <span class="ndf-author">@SadlyItsBradley</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 240 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SadlyItsBradley/status/2065974984258818512">View @SadlyItsBradley on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Say hello to my fishy friend in high frame rate tracking! This is pretty damn impressive for such a quick 3D scan (from my iPhone) https://t.co/vzXlKsFRW5”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A quick iPhone LiDAR scan of a fish produced a high frame rate, trackable 3D model — no dedicated scanning hardware needed.</dd>
      <dt>Why interesting</dt>
      <dd>iPhone LiDAR scans can feed directly into Unity or XR pipelines as quick-turnaround organic assets without a photogrammetry studio.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/XR team can trial apps like Polycam or RealityScan on an iPhone to evaluate scan quality for prop and environment asset creation.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SadlyItsBradley/status/2065974984258818512" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Glacetomic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 235 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Glacetomic/status/2065791001483174393">View @Glacetomic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Completely forgot I can literally view all the emotes in blender if I want to, so here's Remi without the heavy abstraction vfx. https://t.co/PHMwBbanoX”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Artist @Glacetomic shared that Blender lets you inspect character emotes directly without in-game VFX layers, posting a clean render of their character Remi as a result.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Glacetomic/status/2065791001483174393" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@msteevie3d</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 221 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/msteevie3d/status/2065879965602603119">View @msteevie3d on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow, product visualization via Gaussian Splatting is mind blowing. 🤯 From @Blender to @lichtfeldstudio , the details are crazy. It preserved everything so well, even the tiny hairs on the fabric! I ho”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A 3D artist captured a fabric product using 500 photos, ran 50k training iterations with IGS+, and produced a 2M-splat Gaussian Splatting render that preserves fine surface details like individual fabric hairs.</dd>
      <dt>Why interesting</dt>
      <dd>This workflow (photo capture → IGS+ → Gaussian Splat) produces photorealistic product assets without polygon modeling, directly relevant for XR product demos or e-learning visual content.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team can trial IGS+ for product visualization captures — 500 photos is achievable with a DSLR or phone rig, and the output integrates with Unity via Gaussian Splatting plugins.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/msteevie3d/status/2065879965602603119" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KanikaBK</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 169 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KanikaBK/status/2065780534148731148">View @KanikaBK on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here are 10 AI video editor GitHub repos worth bookmarking: 1. Shotcut https://t.co/avPrh2NmjC Most actively maintained open source video editor in 2026. 14K stars. Cross-platform with AI-assisted fea”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A curated list of 10 open-source AI video editor repos (2026), highlighting Shotcut, Kdenlive, Blender VSE, Wan2.1 (Alibaba text-to-video, Apache 2.0), and HunyuanVideo (Tencent 13B).</dd>
      <dt>Why interesting</dt>
      <dd>Wan2.1 (Apache 2.0, 1080p text-to-video) and Blender VSE are directly usable for XR/VR cinematic content and e-learning video production without licensing cost.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Evaluate Wan2.1 for generating b-roll or intro sequences in e-learning projects, and Blender VSE as the compositing layer for XR trailer production.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KanikaBK/status/2065780534148731148" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@_vmlops</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 152 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/_vmlops/status/2065619237788586086">View @_vmlops on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fable 5 tackling procedural world generation and rendering in Unreal Engine is wild to watch 🔥 https://t.co/fnRT5F5sWd”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Playground Games is shipping Fable 5 with procedural world generation built on Unreal Engine, and early footage is circulating showing the results at scale.</dd>
      <dt>Why interesting</dt>
      <dd>AAA procedural gen at this scale in UE5 surfaces terrain, foliage, and biome pipeline patterns the Unity team can study for open-world or XR environment work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Watch the linked footage and log which procedural systems appear (terrain, scatter, LOD), then check Unity equivalents in HDRP or third-party tools.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/_vmlops/status/2065619237788586086" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@venturepictures</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 137 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/venturepictures/status/2065967983655071928">View @venturepictures on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Little STARGATE test animation for 1) new hyperspace VFX 2) new asteroid / planet / atmosphere shader 3) PDC / railguns / missles / VDB explosions All done in Blender 3D. To save the gate! #Stargate #”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@venturepictures released a Blender 3D test animation demonstrating hyperspace VFX, planet/atmosphere shaders, and VDB-based explosion effects for a Stargate fan project.</dd>
      <dt>Why interesting</dt>
      <dd>The atmosphere shader and VDB explosion techniques are directly applicable to Unity XR/VR or game projects requiring high-quality space or sci-fi visuals.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can study this animation's Blender shader and VFX breakdown as a reference for asset production pipelines in space or sci-fi scene environments.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/venturepictures/status/2065967983655071928" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
