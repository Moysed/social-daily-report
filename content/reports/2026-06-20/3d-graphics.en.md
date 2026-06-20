---
type: social-topic-report
date: '2026-06-20'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-20T03:34:45+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 41
salience: 0.58
sentiment: neutral
confidence: 0.58
tags:
- 3d
- gaussian-splatting
- unreal-engine
- unity
- procedural
- photogrammetry
thumbnail: https://pbs.twimg.com/media/HLEt-7Ob0AAIuDI.jpg
---

# 3D & Graphics — 2026-06-20

## TL;DR
- Unreal Engine 5.8 shipped with claims of built-in MCP server support so AI agents can drive the editor [15], plus a new animation/rigging toolset (DMC) and free Zebra Character Sample [28].
- Gaussian Splatting is showing up in mainstream/consumer content: a MrBeast video appears to use 3DGS [7], and creators are pushing 4D splats for sports viewing [4] and 360-drone vs standard-drone capture comparisons [14].
- A working pipeline turns Copernicus DEM elevation + OpenStreetMap into procedural isometric game maps with baked low-poly terrain [11]; Houdini 22 keynote (June 22, 2026) is teased with new Copernicus tools [32].
- Unity asset/shader output is active: GPU dynamic wireframe shader using real topology [24], mobile underwater post-processing shader graphs [30], a compute-shader paint demo [23], and a procedural stylized slash VFX creator [10].
- Spatial-intelligence/world-models framed as a next AI shift via World Labs, Fei-Fei Li, and Marble in a FastCompany piece [12]; MidJourney body-scan health claims [6] are unverified hype.

## What happened
Two engine/tooling releases anchor the day: Unreal Engine 5.8 reportedly shipped with MCP server support enabling AI agents to operate inside the editor [15], alongside a confirmed animation/rigging toolset and a free Zebra Character Sample from Epic [28]. SideFX teased the Houdini 22 keynote for June 22, 2026, citing new Copernicus tools [32]. Gaussian Splatting appears repeatedly: a likely 3DGS use in a MrBeast video [7], advocacy for 4D splats in sports [4], a drone-capture comparison at a Netherlands castle [14], and a non-AI splat reconstruction of a bee [34]; one post seeks Mac-native tooling for NeRF, splatting, and differentiable rendering [17].

## Why it matters (reasoning)
The strongest theme is AI agents entering 3D pipelines at the engine level: MCP support in Unreal [15] mirrors the pattern the studio already touches via its UnityMCP setup, suggesting agent-driven scene assembly and rigging assistance is moving from chat into the tools that produce assets. Second-order effect: if engine vendors standardize on MCP, prompt-driven editor automation becomes portable across Unreal and (eventually) Unity, lowering the cost of repetitive layout/setup work. Separately, Gaussian Splatting's appearance in consumer video [7] and drone-capture workflows [14] signals it is becoming a practical capture-to-experience path for XR, not just research — relevant because the studio ships XR/VR. Procedural terrain from open geodata [11] and Houdini's Copernicus tooling [32] point to cheaper, data-grounded environment generation. The constraint to note: most of these are single-source social posts (especially the UE MCP claim [15] from a hype account, and the MidJourney medical-scan claim [6]), so capability should be confirmed against primary docs before planning around it.

## Possibility
Likely: Gaussian Splatting continues spreading into production capture for XR and marketing content, given multiple independent real-world uses today [4][7][14][34] and tooling demand [17]. Likely: MCP/agent integration in game engines expands, since Unreal shipping it [15] plus a credible toolset release [28] establishes a direction other engines tend to follow. Plausible: open geodata-to-game-map pipelines [11] and Houdini 22's Copernicus tools [32] make real-world terrain a routine asset source within a year. Plausible: spatial-intelligence/world-model systems (World Labs, Marble) [12] start producing usable 3D scenes, but maturity for production is unproven here. Unlikely near-term: consumer body-scanning replacing medical imaging as implied [6] — extraordinary claim, single source, no evidence. No source states numeric probabilities.

## Org applicability — NDF DEV
1) Validate the UE 5.8 MCP claim against Epic's release notes, then check whether the studio's UnityMCP can perform comparable agent-driven editor actions for asset/scene setup (effort: med) [15][28]. 2) Run a small Gaussian Splatting capture test for an XR location or prop using drone or phone footage, and measure how cleanly splats import into Unity vs. mesh pipelines (effort: med) [4][7][14][34]. 3) Prototype the open-geodata terrain pipeline (Copernicus DEM + OpenStreetMap) for any map-based game or edutech scene to cut hand-modeling time (effort: med) [11]. 4) Evaluate ready-made Unity shaders/assets for reuse — GPU wireframe [24], mobile underwater post-processing [30], stylized slash VFX [10] — to avoid in-house shader work (effort: low). 5) Watch the Houdini 22 keynote on June 22 for procedural/Copernicus features relevant to terrain (effort: low) [32]. 6) For physical-prop or real-object assets, photogrammetry remains a low-cost capture route [27][3][31] (effort: low-med). Skip: MidJourney body-scan claims [6], generic 'AI tools' listicles [16], and Luma Labs event/marketing posts unless its video Timeline tool [33] is needed for promo cuts.

## Signals to Watch
- Whether engine MCP/agent support becomes real and portable — confirm UE 5.8 details and track UnityMCP parity [15][28].
- Gaussian Splatting crossing into consumer/production content and capture workflows [4][7][14].
- Houdini 22 keynote on June 22, 2026 — new Copernicus/procedural terrain tools [32].
- Spatial intelligence / world models (World Labs, Marble) maturing toward usable 3D scene generation [12].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | R34Dex | ^570 c7 | [✨Blender render by ME and only ME &gt;:3c although, thanks so much for @marshmel](https://x.com/R34Dex/status/2067486005415018854) |
| x | Doesh96 | ^341 c15 | [Wip Considering how bad I am at rigging and how much I love experimenting, I bro](https://x.com/Doesh96/status/2067724801376964991) |
| x | RangerBoard | ^248 c5 | [For those curious, here's a side-by-side comparison between the February 2011 re](https://x.com/RangerBoard/status/2067614893449052199) |
| x | bilawalsidhu | ^246 c15 | [Watching sports from a god’s eye view. I don’t care what people say, this is how](https://x.com/bilawalsidhu/status/2067978121576362228) |
| x | RyanLykos | ^232 c4 | [Mouth correctives! They make such a huge difference to both how the rig feels an](https://x.com/RyanLykos/status/2067846678300721343) |
| x | shiri_shh | ^230 c19 | [expensive MRI and CT scans are officially COOKED 😭 MidJourney just built somethi](https://x.com/shiri_shh/status/2067708111314694516) |
| x | andrewpprice | ^227 c9 | [Fairly certain these shots from the latest MrBeast video use 3D Gaussian Splatti](https://x.com/andrewpprice/status/2067491703788011790) |
| x | multimodalart | ^151 c5 | [Boogu Image Edit is GOOD! This 10B parameter open source image editing/generatio](https://x.com/multimodalart/status/2067577664748077222) |
| x | ThomasonTown | ^150 c4 | [Can someone please 3D scan this entire park before it inevitably closes in like ](https://x.com/ThomasonTown/status/2067972284216676685) |
| x | peplmGameDev | ^111 c2 | [Working on a procedural stylized slash creator for unity ! #gamedev #unity3d #vi](https://x.com/peplmGameDev/status/2067662155512434909) |
| x | PlayDaaa | ^108 c9 | [Hour 1 of building a pipeline that turns public topographic data into 3D isometr](https://x.com/PlayDaaa/status/2067714196423532947) |
| x | smallfly | ^98 c8 | [@FastCompany just published a great piece on @theworldlabs , @drfeifei , Marble,](https://x.com/smallfly/status/2067638115494252832) |
| x | Noiracide | ^94 c1 | [#indiegame #blender Rigging begin ! https://t.co/CONvkKrQcm](https://x.com/Noiracide/status/2067941203132195191) |
| x | GabRoXR | ^91 c7 | [360 Drone Vs "Standard" Drone for #GaussianSplatting. I picked an EPIC location ](https://x.com/GabRoXR/status/2067984246464246075) |
| x | VaibhavSisinty | ^84 c9 | [This is actually massive. 🤯 Unreal Engine 5.8 shipped today and AI agents can no](https://x.com/VaibhavSisinty/status/2067453967953694829) |
| x | wiliam23820a | ^74 c26 | [🚀 Hidden AI Tools That Feel Like Superpowers https://t.co/RqYF5Jh5Ng – Writing l](https://x.com/wiliam23820a/status/2067842358344040874) |
| x | amir_razlighi | ^71 c1 | [I always wanted to use the best 3D vision / graphics research libraries on my Ma](https://x.com/amir_razlighi/status/2067896517214490635) |
| x | 3DxDEV7 | ^70 c0 | [This anime-style explosion was made entirely in Blender — no compositing tricks,](https://x.com/3DxDEV7/status/2067531224785002614) |
| x | sttuuuufffff | ^65 c0 | [I had to revisit this ARKit setup for my face rig in blender, turns out less is ](https://x.com/sttuuuufffff/status/2067736625388429767) |
| x | archeohistories | ^65 c0 | [The Antonine Fountain (Sagalassos), Burdur - Türkiye 🇹🇷 Antonin Fountain is a hi](https://x.com/archeohistories/status/2067977604934885858) |
| x | gleb_alexandrov | ^62 c1 | [Fantastic use of bevel shader (not in Blender).](https://x.com/gleb_alexandrov/status/2067489982797758556) |
| x | YellowArtPone | ^61 c1 | [@RinnaPaws Blender Rigging! It’s essentially layers of 2D art in a 3D space, par](https://x.com/YellowArtPone/status/2067691331363742165) |
| x | ushadersbible | ^59 c0 | [I made this compute shader to paint a cat in Unity. Anyway, I'll be uploading th](https://x.com/ushadersbible/status/2067647805577892268) |
| x | 80Level | ^54 c0 | [Dynamic Wireframe Shader by Amazing Assets renders wireframe effects in Unity en](https://x.com/80Level/status/2067993306965987819) |
| x | LumaLabsAI | ^41 c8 | [A Luma Skill turns your best result into a repeatable workflow. Build it once, r](https://x.com/LumaLabsAI/status/2067653815948476522) |
| x | gbrumfiel | ^39 c1 | [So if it wasn't a ramjet, what was it? Enter Jake Hecla. Jake's been wondering t](https://x.com/gbrumfiel/status/2067621319500279932) |
| x | QuantaMagazine | ^39 c2 | [How do you measure the surface area of a whale shark? Biologists used photogramm](https://x.com/QuantaMagazine/status/2068024536394514457) |
| x | 80Level | ^34 c0 | [Try out the full Unreal Engine 5.8 animation and rigging toolset, including DMC,](https://x.com/80Level/status/2068000860139905277) |
| x | bilawalsidhu | ^31 c3 | [Woot! The the time has finally come. Record a loom for your clanker and have it ](https://x.com/bilawalsidhu/status/2067745721919402200) |
| x | NatureDeveloper | ^30 c0 | [We released a new Unity asset! Mobile-friendly underwater/undersurface post-proc](https://x.com/NatureDeveloper/status/2067581672346857836) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@R34Dex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 570 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/R34Dex/status/2067486005415018854">View @R34Dex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“✨Blender render by ME and only ME &amp;gt;:3c although, thanks so much for @marshmellowybun for rigging and making the pp for my boy Det and helping me with his rig lmao #furryrr34 #rr34furry https://t.co”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A furry artist shared a personal Blender render on X, crediting a collaborator for character rigging.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/R34Dex/status/2067486005415018854" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Doesh96</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 341 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Doesh96/status/2067724801376964991">View @Doesh96 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wip Considering how bad I am at rigging and how much I love experimenting, I broke my rig for Unreal. Thanks to Advanced Skeleton for their non-destructive rigging — I fixed everything and now it’s ru”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Advanced Skeleton's non-destructive rigging workflow let an artist recover a broken character rig and run it in Unreal Engine via Control Rig without rebuilding from scratch.</dd>
      <dt>Why interesting</dt>
      <dd>Non-destructive rigging cuts rework risk when iterating on complex character builds — directly useful in XR/VR character pipelines where rigs change often.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's XR/Unity team can trial Advanced Skeleton as a safer rigging tool for complex characters before engine export.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Doesh96/status/2067724801376964991" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RangerBoard</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 248 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RangerBoard/status/2067614893449052199">View @RangerBoard on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“For those curious, here's a side-by-side comparison between the February 2011 release of S.H.Figuarts Shinken Red versus the new November 2026 Shinkocchou Seihou version, made with a 3D scan of the or”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A collector post comparing the 2011 vs. 2026 S.H.Figuarts Shinken Red figure; the 2026 version used a 3D scan of suit actor Hirofumi Fukuzawa to improve likeness accuracy.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RangerBoard/status/2067614893449052199" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 246 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2067978121576362228">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Watching sports from a god’s eye view. I don’t care what people say, this is how I want to experience sports - as full blown 4d gaussian splats or better. Makes 3d videos look ancient after you try th”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Bilawal Sidhu shares a clip of live sports captured and replayed as 4D Gaussian Splats with free-viewpoint navigation, arguing it supersedes 3D video as a new media format.</dd>
      <dt>Why interesting</dt>
      <dd>4D Gaussian Splatting is reaching broadcast-quality live sports capture, signaling the format is maturing past research demos and into real XR/VR content pipelines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team should test 4DGS playback in Unity via existing open-source viewers to assess whether this capture format fits upcoming immersive experience projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2067978121576362228" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 232 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2067846678300721343">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mouth correctives! They make such a huge difference to both how the rig feels and looks. really pleased (She does have teeth and a tongue! Just haven't rigged them yet😆) #blender #3d #rigging https://”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender rigger shows mouth corrective blend shapes on a facial rig, demonstrating a clear improvement in deformation quality before teeth and tongue are rigged.</dd>
      <dt>Why interesting</dt>
      <dd>Corrective blend shapes directly reduce mesh distortion on character face rigs — a practical technique for Unity game characters and XR avatars the studio ships.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/3D team can add mouth corrective shapes to character rigs before final export to cut common jaw-and-lip deformation artifacts.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2067846678300721343" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@shiri_shh</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 230 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/shiri_shh/status/2067708111314694516">View @shiri_shh on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“expensive MRI and CT scans are officially COOKED 😭 MidJourney just built something straight out of black mirror step into warm water. wait 60 seconds. get a full 3D scan of your body. at a fraction of”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral post claims MidJourney built a warm-water 60-second full-body 3D scanner to replace MRI/CT — the claim is unverified and MidJourney is an image-gen company with no known medical hardware product.</dd>
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
    <span class="ndf-author">@andrewpprice</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 227 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/andrewpprice/status/2067491703788011790">View @andrewpprice on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fairly certain these shots from the latest MrBeast video use 3D Gaussian Splatting! Cool to see it out in the wild. https://t.co/PvdPi9JTk2”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Andrew Price (Blender Guru) identified 3D Gaussian Splatting shots in a MrBeast production video, marking a mainstream commercial appearance of the technique.</dd>
      <dt>Why interesting</dt>
      <dd>Gaussian Splatting reaching high-budget YouTube production confirms the pipeline is stable enough to ship — directly applicable to XR/VR real-world scene capture.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team can prototype Gaussian Splatting for environment capture in Unity using tools like Unity Gaussian Splatting or Luma AI, given the technique is now proven in production.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/andrewpprice/status/2067491703788011790" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@multimodalart</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 151 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/multimodalart/status/2067577664748077222">View @multimodalart on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Boogu Image Edit is GOOD! This 10B parameter open source image editing/generation model landed out of nowhere on @huggingface and is quite good at editing Give it your hardest editing tasks: https://t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Boogu Image Edit, a 10B-parameter open-source image editing and generation model, launched unexpectedly on Hugging Face with strong early results on complex editing tasks.</dd>
      <dt>Why interesting</dt>
      <dd>A capable open-source image editor at 10B params is small enough to self-host, cutting dependency on paid APIs for asset editing in game or e-learning pipelines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run Boogu Image Edit on HuggingFace Spaces now to test texture and concept art editing for Unity or e-learning asset workflows before committing to hosting it.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/multimodalart/status/2067577664748077222" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
