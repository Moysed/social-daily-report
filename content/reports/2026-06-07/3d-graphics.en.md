---
type: social-topic-report
date: '2026-06-07'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-07T03:33:01+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 28
salience: 0.5
sentiment: positive
confidence: 0.55
tags:
- gaussian-splatting
- blender
- photogrammetry
- mocap
- unity-pipeline
- xr-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2063272954004209664/img/S7jifTp22pipLh_7.jpg
---

# 3D & Graphics — 2026-06-07

## TL;DR
- KIRI Engine's 3DGS Render addon update adds Blender 5.1 support, 4DGS/.ply sequence export, and experimental rigging and light baking — animated Gaussian splats inside Blender [5].
- NVIDIA's ArtiFixer reconstructs 3D scenes by repairing artifacts and extending sparse views via Wan 2.1, generating hundreds of consistent frames and inpainting occluded regions [3].
- 3DGS is described as shifting from a quality problem to an infrastructure one, with LOD and streaming for large scenes now appearing [8].
- MAMMA demoed markerless motion capture from a few synced cameras, skipping marker suits and manual cleanup [2].
- A Unity active-ragdoll system combined physics, IK, and procedural animation for self-balancing characters [11].

## What happened
The day's strongest cluster is Gaussian Splatting moving deeper into production pipelines. KIRI Engine shipped a 3DGS Render addon update for Blender 5.1 with 4DGS/.ply sequence export plus experimental rigging and light baking [5]; a separate post argues the remaining 3DGS bottleneck is infrastructure (file size, streaming, large-scene deployment) and that LOD/streaming systems are now emerging [8]; and NVIDIA's ArtiFixer targets reconstruction cleanup, repairing artifacts and extending sparse captures using Wan 2.1 [3]. Around this, MAMMA showed markerless mocap from a few synced cameras [2], a Unity developer detailed an active ragdoll using physics + IK + procedural animation [11], and MeshyAI promoted an agent that turns a portrait into a 3D-printable figurine [23]. The remaining Blender signal is showcase/tutorial material: an explosion generator [1], an eye shader [14], and rigging tutorials [16][18]. Many high-engagement items are off-topic or noise — NYC dining [7], baby scans [17], politics [19], $RENDER crypto [20], and repeated 'hidden AI tools' listicles [9][12][21].

## Why it matters (reasoning)
For a studio producing assets for both games and XR, the 3DGS thread is the practical story. Animated splats exporting from Blender [5] plus LOD/streaming for large scenes [8] are the two missing pieces that would let captured real-world environments become deployable XR/web content rather than static demos; reconstruction repair like ArtiFixer [3] reduces the cleanup tax on sparse photogrammetry captures. The second-order effect is pipeline choice: if splats become riggable and streamable, capture-based environment production competes with hand-built mesh+PBR for certain XR scenes. Markerless mocap [2] points the same direction for character work — lowering the cost of motion data — but the demo is a vendor showcase with no quality, latency, or licensing detail, so treat it as direction, not a proven tool. The Unity ragdoll breakdown [11] is reusable engineering reference for self-balancing characters, independent of any AI trend.

## Possibility
Likely: Gaussian Splatting keeps moving from research into DCC tools and engine pipelines over the coming months, given concurrent Blender addon support, export formats, and the explicit shift toward LOD/streaming infrastructure [5][8]. Plausible: AI reconstruction-repair tools like ArtiFixer become a standard cleanup step for sparse captures if they integrate into existing photogrammetry flows [3]. Plausible: markerless mocap reaches good-enough quality for previz and indie character work, while pro pipelines still require manual verification [2]. Unlikely (near-term): markerless capture replaces marker-based mocap for high-fidelity production, since the only evidence here is a promotional clip [2]. No source states numeric probabilities.

## Org applicability — NDF DEV
1) Run a small evaluation of KIRI's 3DGS Render addon on Blender 5.1, testing .ply/4DGS export into a Unity XR scene to gauge fidelity, file size, and runtime cost (effort: med) [5][8]. 2) Bookmark ArtiFixer and re-test once a usable build/integration exists; do not commit pipeline time yet given it's an early demo (effort: low) [3]. 3) Save the Unity active-ragdoll breakdown [11] as engineering reference for any self-balancing-character or physics-driven gameplay feature (effort: low). 4) Pilot a portrait-to-figurine / AI 3D-asset tool like Meshy only for throwaway prototype props, not shippable assets, until quality and licensing are checked (effort: low) [23]. 5) Treat MAMMA markerless mocap as a watch item — request or wait for a real demo with quality/latency data before scheduling any test (effort: low) [2]. Skip: crypto/$RENDER [20], the recycled 'hidden AI tools' listicles [9][12][21], and all off-topic items [7][17][19].

## Signals to Watch
- 3DGS infrastructure (LOD, streaming, large-scene deployment) — the gating factor for shipping captured scenes to XR/web [8].
- Animated/riggable Gaussian splats in Blender via the 3DGS Render addon — track stability beyond 'experimental' [5].
- AI reconstruction repair (NVIDIA ArtiFixer / Wan 2.1) for sparse-view and occluded-region cleanup [3].
- Markerless multi-camera mocap (MAMMA) — watch for independent quality verification [2].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | 3DxDEV7 | ^1037 c6 | [Check out how Hiroshi Kanazawa showcased this Blender-powered explosion generato](https://x.com/3DxDEV7/status/2063276491480105412) |
| x | clankrmedia | ^768 c9 | [Wow! Motion capture studios not gonna love this! Just check this insane video. F](https://x.com/clankrmedia/status/2062988031708000566) |
| x | wildmindai | ^275 c1 | [3D scene reconstructions by NVIDIA. ArtiFixer - repairs artifacts and extends sp](https://x.com/wildmindai/status/2062816526223216995) |
| x | bestkingsun1 | ^172 c1 | [Stormcutter model made for a roblox game called "Rise of dragons" Were looking f](https://x.com/bestkingsun1/status/2063319729800871957) |
| x | KIRI_Engine_App | ^145 c1 | [Gaussian Splats can now be animated in Blender New 3DGS Render addon update: - B](https://x.com/KIRI_Engine_App/status/2062821750287847445) |
| x | multimodalart | ^92 c1 | [I' m so addicted to @GoogleMagenta RealTime 2 🎹 so to justify playing with it 24](https://x.com/multimodalart/status/2062938381785403586) |
| x | bilawalsidhu | ^91 c8 | [The Punjabi in me was exceedingly satisfied. NYC dining is undefeated. https://t](https://x.com/bilawalsidhu/status/2063272566572159063) |
| x | Stefan_3D_AI | ^77 c1 | [For years, the biggest problem with 3D Gaussian Splatting wasn't quality. It was](https://x.com/Stefan_3D_AI/status/2063240740155895943) |
| x | Orion_Vers7x | ^70 c27 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/SConc5qUp9 – Writing](https://x.com/Orion_Vers7x/status/2062749510195982839) |
| x | ihe4rtjungkook | ^61 c2 | [@vjungist cuz they took a 3d scan of his to make ts more accurate at his event](https://x.com/ihe4rtjungkook/status/2062996203235647515) |
| x | jettelly | ^56 c0 | [Developer Rawad Akar shared a closer look at their active ragdoll system for Uni](https://x.com/jettelly/status/2063244523942314049) |
| x | unfilteredranjn | ^52 c3 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/2ACL9zZ1Y8 – Writing](https://x.com/unfilteredranjn/status/2062778586046829047) |
| x | auqibhabib | ^49 c14 | [Made with seedance 2.0 + GPT Image 2 Prompt :Use the uploaded reference image as](https://x.com/auqibhabib/status/2062951836882231393) |
| x | SG_Animations | ^48 c3 | [a quick abstraction eye shader i made in blender :) https://t.co/6tbIY5Iocu](https://x.com/SG_Animations/status/2062881248842830323) |
| x | JamesMason0 | ^43 c6 | [You know, something I’ve always wondered - Why is it that so many Blender animat](https://x.com/JamesMason0/status/2062984400338403485) |
| x | DemNikoArt | ^41 c1 | [If you haven't seen it, my new rigging tutorial is out now. How to rig a Bike Su](https://x.com/DemNikoArt/status/2062879660095000906) |
| x | RisingNomes | ^40 c3 | [This is my precious, little boy at about the same gestation that scan of their b](https://x.com/RisingNomes/status/2062789349306159350) |
| x | DemNikoArt | ^38 c2 | [You seemed to like this one. The tutorial for it is out now 😉 🔗 below #b3d #blen](https://x.com/DemNikoArt/status/2063295864689262853) |
| x | phillipcparrish | ^37 c6 | [For Immediate Release June 6, 2026 The Conventions That Don’t Represent Us: Phil](https://x.com/phillipcparrish/status/2063254062838014426) |
| x | EnochsDegenCrib | ^33 c0 | [🚀 $RENDER Bull Case: Market Dip? What Dip? Fundamentals Are Unbreakable⭕️🚀 Crypt](https://x.com/EnochsDegenCrib/status/2062904565859553483) |
| x | PrakashS720 | ^33 c5 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/6XRECyOn7W – Writing](https://x.com/PrakashS720/status/2062839222139294035) |
| x | alt_Vulcan105 | ^33 c1 | [@cybernetic_sam The only possible answer is that rover civilization is using sim](https://x.com/alt_Vulcan105/status/2062825816980181055) |
| x | MeshyAI | ^18 c1 | [I asked an AI agent to 3D print me as a figurine series! Here's how it works: - ](https://x.com/MeshyAI/status/2062805201480745129) |
| x | multimodalart | ^8 c4 | [where we are headed, all software becomes open source software models can decomp](https://x.com/multimodalart/status/2063307704873951333) |
| x | bilawalsidhu | ^7 c0 | [@sriramk @ayirpelle Congrats on a great run and thank you for your service Srira](https://x.com/bilawalsidhu/status/2063333617506377794) |
| x | multimodalart | ^7 c1 | [Come chill at the CVPR Art Gallery! https://t.co/gVZtxL9C1x](https://x.com/multimodalart/status/2062955857911193835) |
| x | bilawalsidhu | ^5 c1 | [Deep tech founders circa 1910 https://t.co/YyIeQzIwx4](https://x.com/bilawalsidhu/status/2063458023209648517) |
| x | MeshyAI | ^1 c1 | [@_ace_won We have all the tutorials in our Youtube channel. Feel free to check t](https://x.com/MeshyAI/status/2062805649810153960) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1037 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2063276491480105412">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out how Hiroshi Kanazawa showcased this Blender-powered explosion generator — 💥 Really cool progress on this project. What part stands out most to you? 👀 #B3D #Blender3D #Blender #Animation #VFX”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Hiroshi Kanazawa demoed a work-in-progress procedural explosion generator built entirely in Blender using Geometry Nodes.</dd>
      <dt>Why interesting</dt>
      <dd>Geometry Nodes-based VFX can be baked and exported as mesh caches, cutting manual animation work for Unity game and XR projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can prototype explosion VFX in Blender with this Geometry Nodes approach, then bake and import into Unity scenes.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2063276491480105412" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@clankrmedia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 768 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/clankrmedia/status/2062988031708000566">View @clankrmedia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow! Motion capture studios not gonna love this! Just check this insane video. For years, capturing human motion meant markers, skin-tight suits, and hours of cleanup. MAMMA just asks for a few synced”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>MAMMA is a markerless mocap system using synced cameras (including 4 iPhones) to reconstruct full per-frame 3D bodies with contact-aware tracking, matching Vicon accuracy while cutting pipelines from multi-day to one day.</dd>
      <dt>Why interesting</dt>
      <dd>Vicon-grade mocap via iPhones directly lowers the cost of capturing custom animation data for Unity characters and XR avatars without renting a commercial studio.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Track the MAMMA repo for a public release and run an in-house iPhone test to see if it replaces outsourced mocap sessions for Unity or XR character work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/clankrmedia/status/2062988031708000566" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@wildmindai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 275 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/wildmindai/status/2062816526223216995">View @wildmindai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“3D scene reconstructions by NVIDIA. ArtiFixer - repairs artifacts and extends sparse views via Wan 2.1. - high-fidelity inpainting in occluded regions - gens hundreds of consistent frames in a single ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>NVIDIA's ArtiFixer uses Wan 2.1 diffusion to repair artifact-laden or sparse-view 3D scans, generating hundreds of consistent frames in one pass and outputting navigable scenes via 3D Gaussian Splatting.</dd>
      <dt>Why interesting</dt>
      <dd>Studios building VR/XR environments can use this to salvage low-quality or incomplete scans instead of rebuilding scenes from scratch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test ArtiFixer on existing scan assets in the XR pipeline to see if it replaces manual cleanup steps in Gaussian Splatting workflows.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/wildmindai/status/2062816526223216995" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bestkingsun1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 172 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bestkingsun1/status/2063319729800871957">View @bestkingsun1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Stormcutter model made for a roblox game called &quot;Rise of dragons&quot; Were looking for animators,Vfx designers! https://t.co/iJtEGh00Qe #httyd #HowToTrainYourDragon #dragon #3Dmodel #blender #3dart #3DArt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An indie artist shared a Blender-made Stormcutter dragon 3D model created for a Roblox game 'Rise of Dragons', and is recruiting animators and VFX designers.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bestkingsun1/status/2063319729800871957" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KIRI_Engine_App</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 145 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KIRI_Engine_App/status/2062821750287847445">View @KIRI_Engine_App on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gaussian Splats can now be animated in Blender New 3DGS Render addon update: - Blender 5.1 support - 4DGS / .ply sequence export - Experimental rigging tools - Experimental light baking Check below fo”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>KIRI Engine's Blender 3DGS Render addon now supports animated Gaussian Splats (4DGS) via .ply sequence export, plus Blender 5.1, experimental rigging, and light baking.</dd>
      <dt>Why interesting</dt>
      <dd>Animated Gaussian Splats with .ply sequence export opens a path to bring dynamic 3DGS scenes into Unity and XR/VR projects without full mesh pipelines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team should run a quick test: capture a scene with KIRI, animate it in Blender 5.1 via this addon, and evaluate .ply sequence import into the Unity XR pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KIRI_Engine_App/status/2062821750287847445" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@multimodalart</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 92 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/multimodalart/status/2062938381785403586">View @multimodalart on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I' m so addicted to @GoogleMagenta RealTime 2 🎹 so to justify playing with it 24/7 I ported the real-time apps to @huggingface Spaces 🤗 (and ported the entire lib to pytorch/transformers too) Play liv”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google Magenta RealTime 2, a real-time AI music generation model, is now live on Hugging Face Spaces and fully ported to PyTorch/Transformers by community contributor @multimodalart.</dd>
      <dt>Why interesting</dt>
      <dd>The Transformers port and Spaces deployment mean the studio can call real-time generative music via a standard API — no self-hosting needed for Unity or XR audio experiments.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test the Hugging Face Spaces endpoint as a generative background music source in a Unity game or XR prototype.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/multimodalart/status/2062938381785403586" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 91 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2063272566572159063">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Punjabi in me was exceedingly satisfied. NYC dining is undefeated. https://t.co/CNrnbluZ1e”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user expressed personal satisfaction with a New York City dining experience, referencing their Punjabi heritage — no technical or industry content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2063272566572159063" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Stefan_3D_AI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 77 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Stefan_3D_AI/status/2063240740155895943">View @Stefan_3D_AI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“For years, the biggest problem with 3D Gaussian Splatting wasn't quality. It was infrastructure. Huge files. No streaming. No practical way to deploy large scenes. Now we're finally seeing: ✅ LOD syst”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>ManyCore Tech has solved 3D Gaussian Splatting's deployment blockers — LOD, streaming, SPZ compression, collision generation, and browser rendering via WebGPU are now production-ready.</dd>
      <dt>Why interesting</dt>
      <dd>3DGS can now run in-browser at scale, making it viable for XR/VR walkthroughs and Unity web builds without custom server infra.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test SPZ-compressed Gaussian Splats in a browser-based XR prototype to gauge load time and quality against current photogrammetry workflow.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Stefan_3D_AI/status/2063240740155895943" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
