---
type: social-topic-report
date: '2026-06-20'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-20T15:34:33+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 38
salience: 0.6
sentiment: positive
confidence: 0.6
tags:
- gaussian-splatting
- rigging
- procedural
- unity
- unreal
- photogrammetry
thumbnail: https://pbs.twimg.com/media/HLIIhNGW0AAmH6T.jpg
---

# 3D & Graphics — 2026-06-20

## TL;DR
- Gaussian Splatting dominates the day across use cases: Apple Maps now uses 3D Gaussian Splatting [26], 4D splats for sports viewing [2], 360 vs standard drone capture tests for splats [7], and Volograms working to make 4D GS run on smaller camera rigs [28].
- Character pipeline tooling: Advanced Skeleton's non-destructive rigging fixed a broken Unreal rig [1], Epic shipped a free Unreal Engine 5.8 animation/rigging toolset (incl. DMC) with a Zebra Character Sample [21], and several Blender face-rig posts converge on 'fewer ARKit shape keys = better' [16].
- Procedural environment generation from real-world data: a pipeline turning Copernicus DEM + OpenStreetMap into isometric game maps [8], and Alibaba's Mapping Lab generating a square km of photorealistic 3D city from a 2D satellite image in ~10 minutes [19].
- Unity GPU shader work: a dynamic wireframe shader using real topology generated at runtime in Shader Graph with no mesh preprocessing [13][25], plus a compute-shader painting demo [18].
- Houdini 22 keynote streams June 22, 2026, with new Copernicus tools among highlights [14]; an open-source Mac-GPU library for NeRF/Gaussian Splatting/differentiable rendering hit v0.2.0 [10][30].

## What happened
Gaussian Splatting is the clearest cluster: Apple Maps adopting 3DGS for its realistic look [26], sports captured as 4D splats [2], drone-capture comparisons for splat quality [7], a non-AI splat reconstruction of a bee [29], and Volograms reporting progress on 4D GS with less dense camera rigs [28]. In parallel, character/rigging tooling saw concrete releases and tips: Epic's free UE 5.8 rigging toolset with a Zebra sample [21], Advanced Skeleton's non-destructive rigging [1], and Blender face-rig findings favoring minimal ARKit shape keys [16], plus mouth correctives [3]. Procedural-from-real-data pipelines appeared on both ends: DEM+OSM to isometric game maps [8] and satellite-to-3D-city in ~10 minutes [19].

## Why it matters (reasoning)
The recurring theme is real-world capture and procedural generation feeding game/XR pipelines, which is directly NDF DEV's asset-production problem. Apple Maps shipping Gaussian Splatting [26] is the strongest maturity signal — a consumer product at scale validates GS as production-viable, not just research. That lowers the risk of building XR experiences (heritage sites, locations) on splat capture. Second-order: as 4D/dynamic splat capture moves to smaller rigs [28], the hardware barrier for volumetric/dynamic content drops toward something a small studio can attempt. On the tooling side, free first-party assets (UE 5.8 toolset [21]) and runtime-generated shaders with no preprocessing [13][25] reduce integration friction. Several high-engagement posts are marketing or hype and should be discounted: Luma's repeated 'Skills' promotion [22][31][23][34][35] and the MidJourney 'replaces MRI/CT' body-scan claim [5] carry no verifiable technical detail.

## Possibility
Likely: Gaussian Splatting continues moving from demo to pipeline component for mapping and XR through the year, given a shipped consumer deployment [26] and active capture tooling [7][10][28]. Plausible: smaller-rig 4D/dynamic splat capture becomes practical for small teams as Volograms-style work matures [28], and procedural environment generation from public geodata (DEM/OSM [8], satellite [19]) gets used for large maps in games/edutech. Plausible: Houdini 22's Copernicus tools [14] further standardize real-terrain-to-asset workflows. Unlikely (near-term): the MidJourney medical-scan replacement framing [5] reflects anything clinically real — treat as hype absent a source. No source states numeric probabilities.

## Org applicability — NDF DEV
1) Prototype Gaussian Splatting capture for an XR/heritage asset (Chiang Mai location or temple) and test import into Unity — Apple Maps adoption de-risks the approach [26]; drone-vs-camera capture guidance exists [7]; effort med. 2) Evaluate the runtime Unity wireframe shader for edutech/XR visualization (no mesh preprocessing) [13][25]; effort low. 3) Trial the DEM+OSM procedural-map pipeline for a game/edutech map prototype [8]; effort med. 4) Pull Epic's free UE 5.8 rigging toolset + Zebra sample to benchmark against current character workflow [21], and apply the 'minimal ARKit shape keys' face-rig finding to avatar work [16]; effort low. 5) Watch the Houdini 22 keynote June 22 for Copernicus/procedural tools before committing to a terrain pipeline [14]; effort low. 6) If anyone on the team works on Mac, test the v0.2.0 NeRF/GS Mac-GPU library for cheap experimentation [10][30]; effort low, but early-stage. Skip: Luma Skills marketing [22][23][31][34][35], the MidJourney body-scan claim [5], generic 'AI tools' threads [15], and GLM-in-Claude-Code posts [32][37] — off-topic or unverified.

## Signals to Watch
- Houdini 22 keynote June 22, 2026 — watch for Copernicus/procedural terrain tooling relevant to map generation [14].
- Volograms 4D Gaussian Splatting on smaller camera rigs — lowers the bar for dynamic volumetric capture [28].
- Alibaba Mapping Lab: 2D satellite → 1 km² photorealistic 3D city in ~10 min — track for large-environment generation [19].
- Open-source Mac-GPU 3D-vision library (NeRF/GS/differentiable rendering) at v0.2.0 — watch maturity for non-NVIDIA experimentation [10][30].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Doesh96 | ^363 c15 | [Wip Considering how bad I am at rigging and how much I love experimenting, I bro](https://x.com/Doesh96/status/2067724801376964991) |
| x | bilawalsidhu | ^339 c21 | [Watching sports from a god’s eye view. I don’t care what people say, this is how](https://x.com/bilawalsidhu/status/2067978121576362228) |
| x | RyanLykos | ^266 c4 | [Mouth correctives! They make such a huge difference to both how the rig feels an](https://x.com/RyanLykos/status/2067846678300721343) |
| x | ThomasonTown | ^257 c4 | [Can someone please 3D scan this entire park before it inevitably closes in like ](https://x.com/ThomasonTown/status/2067972284216676685) |
| x | shiri_shh | ^232 c19 | [expensive MRI and CT scans are officially COOKED 😭 MidJourney just built somethi](https://x.com/shiri_shh/status/2067708111314694516) |
| x | Noiracide | ^128 c1 | [#indiegame #blender Rigging begin ! https://t.co/CONvkKrQcm](https://x.com/Noiracide/status/2067941203132195191) |
| x | GabRoXR | ^128 c8 | [360 Drone Vs "Standard" Drone for #GaussianSplatting. I picked an EPIC location ](https://x.com/GabRoXR/status/2067984246464246075) |
| x | PlayDaaa | ^122 c9 | [Hour 1 of building a pipeline that turns public topographic data into 3D isometr](https://x.com/PlayDaaa/status/2067714196423532947) |
| x | peplmGameDev | ^118 c2 | [Working on a procedural stylized slash creator for unity ! #gamedev #unity3d #vi](https://x.com/peplmGameDev/status/2067662155512434909) |
| x | amir_razlighi | ^105 c4 | [I always wanted to use the best 3D vision / graphics research libraries on my Ma](https://x.com/amir_razlighi/status/2067896517214490635) |
| x | smallfly | ^104 c8 | [@FastCompany just published a great piece on @theworldlabs , @drfeifei , Marble,](https://x.com/smallfly/status/2067638115494252832) |
| x | archeohistories | ^92 c0 | [The Antonine Fountain (Sagalassos), Burdur - Türkiye 🇹🇷 Antonin Fountain is a hi](https://x.com/archeohistories/status/2067977604934885858) |
| x | 80Level | ^88 c0 | [Dynamic Wireframe Shader by Amazing Assets renders wireframe effects in Unity en](https://x.com/80Level/status/2067993306965987819) |
| x | sidefx | ^81 c1 | [Watch the Houdini 22 Keynote live on YouTube, premiering on June 22, 2026, at 09](https://x.com/sidefx/status/2068131719967080560) |
| x | wiliam23820a | ^76 c26 | [🚀 Hidden AI Tools That Feel Like Superpowers https://t.co/RqYF5Jh5Ng – Writing l](https://x.com/wiliam23820a/status/2067842358344040874) |
| x | sttuuuufffff | ^67 c0 | [I had to revisit this ARKit setup for my face rig in blender, turns out less is ](https://x.com/sttuuuufffff/status/2067736625388429767) |
| x | YellowArtPone | ^63 c1 | [@RinnaPaws Blender Rigging! It’s essentially layers of 2D art in a 3D space, par](https://x.com/YellowArtPone/status/2067691331363742165) |
| x | ushadersbible | ^61 c0 | [I made this compute shader to paint a cat in Unity. Anyway, I'll be uploading th](https://x.com/ushadersbible/status/2067647805577892268) |
| x | yohaniddawela | ^56 c2 | [It now takes Alibaba's Mapping Lab just 10 minutes to generate a square kilometr](https://x.com/yohaniddawela/status/2068275707810070990) |
| x | QuantaMagazine | ^46 c2 | [How do you measure the surface area of a whale shark? Biologists used photogramm](https://x.com/QuantaMagazine/status/2068024536394514457) |
| x | 80Level | ^43 c0 | [Try out the full Unreal Engine 5.8 animation and rigging toolset, including DMC,](https://x.com/80Level/status/2068000860139905277) |
| x | LumaLabsAI | ^42 c8 | [A Luma Skill turns your best result into a repeatable workflow. Build it once, r](https://x.com/LumaLabsAI/status/2067653815948476522) |
| x | LumaLabsAI | ^41 c3 | [Your footage. Your cut. One canvas. Assemble it on Timeline, where your edit tak](https://x.com/LumaLabsAI/status/2068051147273728244) |
| x | cghow_ | ^36 c0 | [Azure Beam in Unreal Engine 5 Niagara https://t.co/su9LT38iEh https://t.co/LkzIa](https://x.com/cghow_/status/2067895180511096855) |
| x | jettelly | ^35 c0 | [Arkhivrag finished their dynamic wireframe shader for Unity, generated entirely ](https://x.com/jettelly/status/2067955560839008299) |
| x | bilawalsidhu | ^35 c3 | [Apple Maps Just Got Insanely Realistic -- Here's The Tech Behind It 00:00 Intro ](https://x.com/bilawalsidhu/status/2068326490656182329) |
| x | bilawalsidhu | ^32 c3 | [Woot! The the time has finally come. Record a loom for your clanker and have it ](https://x.com/bilawalsidhu/status/2067745721919402200) |
| x | rafamolone | ^29 c1 | [Quick update on something we've been working on at @Volograms. 4D Gaussian Splat](https://x.com/rafamolone/status/2068068468553908436) |
| x | RadianceFields | ^23 c2 | [@rezmeram It’s a 3D reconstruction of a real bee using gaussian splatting (No AI](https://x.com/RadianceFields/status/2067658498733953483) |
| x | amir_razlighi | ^23 c1 | [v0.2.0 is out now. Repo: https://t.co/hrNPEtzqN6 If you are working on NeRFs, Ga](https://x.com/amir_razlighi/status/2067896550995448202) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Doesh96</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 363 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Doesh96/status/2067724801376964991">View @Doesh96 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wip Considering how bad I am at rigging and how much I love experimenting, I broke my rig for Unreal. Thanks to Advanced Skeleton for their non-destructive rigging — I fixed everything and now it’s ru”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A 3D artist recovered a broken character rig for Unreal Engine by using Advanced Skeleton's non-destructive rigging workflow, then successfully drove it with Control Rig.</dd>
      <dt>Why interesting</dt>
      <dd>Advanced Skeleton's non-destructive approach lets artists iterate and fix rigs without rebuilding from scratch — a practical safety net for character pipelines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio's 3D pipeline uses Maya for character rigging, evaluate Advanced Skeleton as a non-destructive alternative to manual rig setups before the next character project.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Doesh96/status/2067724801376964991" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 339 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2067978121576362228">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Watching sports from a god’s eye view. I don’t care what people say, this is how I want to experience sports - as full blown 4d gaussian splats or better. Makes 3d videos look ancient after you try th”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A demo shows live sports captured as 4D Gaussian Splats, giving viewers a free-viewpoint god's-eye replay that standard multi-camera 3D video cannot replicate.</dd>
      <dt>Why interesting</dt>
      <dd>Broadcast-scale 4D Gaussian Splatting is the incoming source format for immersive VR sports experiences; the studio's XR pipeline will intersect this format soon.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a 4D Gaussian Splatting test in Unity with an open-source splat renderer to benchmark render cost before a client requests this format.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2067978121576362228" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 266 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2067846678300721343">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mouth correctives! They make such a huge difference to both how the rig feels and looks. really pleased (She does have teeth and a tongue! Just haven't rigged them yet😆) #blender #3d #rigging https://”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A 3D artist on X shared a Blender facial rig demo showing mouth corrective shapes that visibly improve deformation quality and rig feel.</dd>
      <dt>Why interesting</dt>
      <dd>Corrective shapes are a practical rigging technique relevant to any studio doing character work in Blender or Unity.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio rigs characters in Blender, add mouth correctives to the facial rig checklist before export to Unity.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2067846678300721343" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ThomasonTown</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 257 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ThomasonTown/status/2067972284216676685">View @ThomasonTown on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Can someone please 3D scan this entire park before it inevitably closes in like 5 months?”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user on X is asking someone to 3D scan a park before it closes, implying no preservation effort is underway.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ThomasonTown/status/2067972284216676685" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@shiri_shh</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 232 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/shiri_shh/status/2067708111314694516">View @shiri_shh on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“expensive MRI and CT scans are officially COOKED 😭 MidJourney just built something straight out of black mirror step into warm water. wait 60 seconds. get a full 3D scan of your body. at a fraction of”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral post claims MidJourney built a 60-second water-immersion 3D body scanner to replace MRI/CT — but MidJourney is an AI image generator, not a medical hardware company; the claim has no verifiable source.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/shiri_shh/status/2067708111314694516" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Noiracide</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 128 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Noiracide/status/2067941203132195191">View @Noiracide on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“#indiegame #blender Rigging begin ! https://t.co/CONvkKrQcm”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An indie dev posted a one-line update announcing they have started the rigging phase of their Blender character, with no technique or detail shared.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Noiracide/status/2067941203132195191" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GabRoXR</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 128 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GabRoXR/status/2067984246464246075">View @GabRoXR on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“360 Drone Vs &quot;Standard&quot; Drone for #GaussianSplatting. I picked an EPIC location to see who wins 🏆 This is the Der Haar Castle, the largest and most luxurious castle in the Netherlands. The original ca”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A head-to-head 3DGS capture test at De Haar Castle shows DJI Mini 4 Pro (standard 4K gimbal, 500 photos) beats the Antigravity A1 360 drone (8K panoramic, cubemap extraction) on color accuracy; both processed in Postshot at 30K iterations / 5M splats.</dd>
      <dt>Why interesting</dt>
      <dd>For the studio's XR/VR real-world capture work, a standard gimbal drone already on the market outperforms a specialized 360 rig in Gaussian Splatting color fidelity — lower cost, better output.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio shoots 3DGS location scans, use a standard gimbal drone with ~500 images and process in Postshot at 30K iterations / 5M splats as a proven baseline before investing in 360 rigs.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GabRoXR/status/2067984246464246075" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PlayDaaa</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 122 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PlayDaaa/status/2067714196423532947">View @PlayDaaa on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hour 1 of building a pipeline that turns public topographic data into 3D isometric game maps. Real-world elevation (Copernicus DEM) + OpenStreetMap → procedural terrain, coastline &amp; city, baked low-po”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer is building an open-source pipeline that combines Copernicus DEM elevation data with OpenStreetMap to auto-generate low-poly isometric game maps, baked in Blender and rendered in Three.js — Monaco is the proof-of-concept, zero hand-modeled terrain.</dd>
      <dt>Why interesting</dt>
      <dd>Once released, this pipeline cuts the terrain authoring bottleneck entirely — any real-world city becomes a playable map without a single hand-sculpted polygon.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Star the repo when it goes public; the Blender-baked low-poly meshes can feed directly into Unity projects that need real-geography terrain without manual asset work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PlayDaaa/status/2067714196423532947" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
