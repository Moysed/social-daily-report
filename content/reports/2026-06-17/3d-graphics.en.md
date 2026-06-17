---
type: social-topic-report
date: '2026-06-17'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-17T15:37:15+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 37
salience: 0.6
sentiment: mixed
confidence: 0.6
tags:
- gaussian-splatting
- blender
- unity-shaders
- ai-3d
- photogrammetry
- procedural
thumbnail: https://pbs.twimg.com/media/HK7ljsRWMAADR4z.jpg
---

# 3D & Graphics — 2026-06-17

## TL;DR
- Gaussian splatting is reaching consumer hardware: Huawei ships native 3DGS capture that sets a splat as the lock-screen wallpaper [6][12], alongside Apple's Spatial Reframe [6].
- Open-source 4D Gaussian Splatting (4DGS) is being demoed turning ordinary iPhone footage into interactive 3D space [19]; KIRI Engine released a free open-source tool to organize raw scan photos/video [28].
- AI-to-3D crossed a visibility marker: MeshyAI hit 1,000,000 YouTube subscribers and is pushing a '3D Agent' that goes from chat to 3D-printed objects [34][35].
- Blender tooling moved: V-Ray for Blender Update 3 now runs on Linux (plus Windows/macOS), with native Node Wrangler and AMD GPU rendering [20].
- Unity real-time shader/VFX content is active — Unity Shaders Bible is re-implementing its 'lemon shader' in Shader Graph this week [14], plus procedural-effects [29] and toon buff/debuff VFX tutorials [25].

## What happened
Two consumer-facing 3D capture stories dominated: Huawei phones can natively capture a Gaussian splat and set it as a live wallpaper [6][12], and phone-based house scans uploaded for in-browser walkthroughs drew large 'real estate is over' threads [8][32]. On the research/tooling side, open-source 4DGS was shown converting iPhone video into interactive 3D [19], and KIRI Engine shipped a free open-source organizer for messy scan datasets [28]; a photogrammetry-vs-LiDAR comparison also circulated [18]. AI-to-3D was prominent through MeshyAI's 1M-subscriber milestone and its chat-driven 3D Agent producing 3D-printable pieces [34][35], plus a manim-based agent that writes code to render and stitch video [4].

## Why it matters (reasoning)
The center of gravity is capture and generation getting cheaper and more accessible. Native phone Gaussian splatting [6][12] and free scan-organizing tools [28] lower the cost of producing photoreal environment assets for XR and web, which is directly in the studio's asset-production path. 4DGS from monocular video [19] points toward dynamic, not just static, captured scenes, though it remains demo-stage. AI-to-3D (Meshy [34][35]) compresses ideation-to-asset time but historically yields topology/quality unsuited to production rigging and real-time budgets, so its near-term value is prototyping, not final assets. Meanwhile the unglamorous but reliable wins are concrete tool updates: V-Ray on Linux with AMD GPU support [20] expands render-farm options, and the steady stream of Unity Shader Graph / procedural VFX material [14][25][29] is immediately usable craft for game and XR pipelines.

## Possibility
Likely: consumer 3DGS capture keeps spreading now that a major OEM ships it natively [6][12], pulling splats from novelty toward a standard environment-capture format for XR/web. Plausible: 4DGS video-to-3D [19] matures into a usable pipeline within a year but stays research/experimental in the near term given it surfaced as a demo. Plausible: AI-to-3D tools like Meshy [34][35] become routine for greyboxing and concept iteration, while final game/XR assets still need manual cleanup. Unlikely (as stated): phone scans 'destroy the real estate sector' [8][32] — these threads are hype; capture quality, hosting, and workflow integration are unaddressed, and scanning a house is not industry disruption.

## Org applicability — NDF DEV
1) Pilot Gaussian-splat environment capture for XR experiences using a phone + KIRI Engine's free organizer [28] and consumer 3DGS capture [6][12] — low effort, high relevance to the XR portfolio. 2) Adopt the Unity Shader Graph and procedural-VFX tutorials directly into game/XR VFX work [14][25][29] — low effort, immediate craft gain. 3) If the render pipeline uses Blender, evaluate V-Ray Update 3 for Linux/AMD GPU rendering to widen hardware options [20] — med effort. 4) Trial AI-to-3D (Meshy [34][35]) for rapid prototyping and edutech props only, not production assets — med effort, verify topology before committing. 5) Watch 4DGS [19] for dynamic-scene capture but do not build on it yet — low effort monitoring. Skip: real-estate 'disruption' hype [8][32], celebrity/portfolio praise [21][36][37], and off-topic items [9][16].

## Signals to Watch
- Whether other phone OEMs follow Huawei's native 3DGS capture [6][12] — that would standardize splats as an XR/web asset format.
- Maturity of open-source 4DGS from monocular video toward a stable, documented pipeline [19].
- Quality and topology of MeshyAI 3D Agent output as it scales post-1M subs [34][35] — the gate on production use.
- Houdini HIVE/IGNITE at Annecy, June 24–26, for procedural-pipeline techniques relevant to asset production [24].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | faenir_morne | ^1680 c11 | [Memories. 2019. I was 25. Short haircut, freckles, young. I got invited to a pho](https://x.com/faenir_morne/status/2066845394235949376) |
| x | c_valenzuelab | ^713 c169 | [Imagine waking up and realizing that your full time job entails using a digital ](https://x.com/c_valenzuelab/status/2066922813466779876) |
| x | 80Level | ^592 c2 | [Have a look at this 90s anime-style shader in Blender by @Jorm_0ff, inspired by ](https://x.com/80Level/status/2066868400261874001) |
| x | IBuzovskyi | ^312 c11 | [HERMES AGENT CAN CREATE VIDEOS. NOT WITH AN API CALL. IT WRITES THE CODE, RENDER](https://x.com/IBuzovskyi/status/2066724948702626255) |
| x | RyanLykos | ^270 c5 | [Zhu Yuan eyebrows rigged! Using a shape key and bone based hybrid! Really happy ](https://x.com/RyanLykos/status/2066995632368238653) |
| x | RadianceFields | ^206 c3 | [Apple may have just launched Spatial Reframe, but Huawei has full on gaussian sp](https://x.com/RadianceFields/status/2066565454035112090) |
| x | mangaka7 | ^185 c7 | [Taking MinusT's SD characters course on Coloso! Finished the base mesh and hair.](https://x.com/mangaka7/status/2066693948031033765) |
| x | DAIEvolutionHub | ^180 c10 | [SOMEONE JUST DESTROYED THE REAL ESTATE SECTOR AND NO ONE IS TALKING ABOUT IT Som](https://x.com/DAIEvolutionHub/status/2066635993844003197) |
| x | RobLooseCannon | ^149 c4 | [Brusselstown Ring sits on a high ridge above the Wicklow lowlands, looking west ](https://x.com/RobLooseCannon/status/2067156169026650154) |
| x | IAmTarrell | ^132 c0 | [I'm shook that he did the set extension himself in Blender. Outside of the found](https://x.com/IAmTarrell/status/2066960069497848157) |
| x | TheNthUmbreon | ^122 c2 | [Finally added a little UV shading to Allie's hair, in addition to the procedural](https://x.com/TheNthUmbreon/status/2067014392907227198) |
| x | bilawalsidhu | ^109 c4 | [China too quick with it. Huawei users can natively capture a 3d gaussian splat a](https://x.com/bilawalsidhu/status/2066617540923490439) |
| x | VijayKu94617363 | ^89 c22 | [A GUY JUST RENDERED AN ENTIRE 3D WORLD IN A BROWSER WITH ZERO ASSETS no game eng](https://x.com/VijayKu94617363/status/2066619575513342248) |
| x | ushadersbible | ^86 c0 | [The lemon shader will come back to the Unity Shaders Bible, but this time implem](https://x.com/ushadersbible/status/2066995211201327466) |
| x | Mix3Design | ^78 c0 | [STOP SCROLLING. If you love anime-style Blender art but can't afford expensive c](https://x.com/Mix3Design/status/2066584516408537510) |
| x | daddyhope | ^75 c14 | [So here are my two cents on the Constitutional Court rulings delivered today aga](https://x.com/daddyhope/status/2067222380917772545) |
| x | fellowshiptrust | ^69 c8 | [Fellowship talks with @john__gerrard john gerrard is a key figure in contemporar](https://x.com/fellowshiptrust/status/2066571096678428902) |
| x | geowgs84 | ^62 c3 | [Photogrammetry vs LiDAR: Key Differences, Accuracy &amp; Use Cases https://t.co/](https://x.com/geowgs84/status/2066728376258486324) |
| x | SciTechera | ^59 c2 | [This could be the future of video 🤯 Open-Source 4DGS Might Be the Future of Vide](https://x.com/SciTechera/status/2066587374340219102) |
| x | theCGchannel | ^57 c0 | [V-Ray for Blender now runs on Linux, as well as Windows and macOS Update 3 to th](https://x.com/theCGchannel/status/2066806757964325072) |
| x | LumaLabsAI | ^53 c4 | [👏 Bravo @PJaccetturo !](https://x.com/LumaLabsAI/status/2066911030081700342) |
| x | auqibhabib | ^51 c28 | [Made with seedance 2.0 + GPT image 2.0 on @renoiseai Prompt: @Image1 fights thre](https://x.com/auqibhabib/status/2066796169813221848) |
| x | meifumaudo | ^46 c0 | [@OverlyXGamer He's mentioned a lot of film was traditional vfx pipeline, but a g](https://x.com/meifumaudo/status/2067018945819766892) |
| x | sidefx | ^46 c1 | [SideFX is proud to be hosting Houdini HIVE Talks and IGNITE Workshops at the Ann](https://x.com/sidefx/status/2066611110804152601) |
| x | GabrielAguiarFX | ^44 c1 | [Quick Buffs and Debuffs with a toon touch! #VFX #gamedev #realtimeVFX #Unity #Ga](https://x.com/GabrielAguiarFX/status/2066556366135717958) |
| x | palelzr | ^37 c0 | [stylized sculpted planet namek map VFX: @Suntora69 #Roblox #RobloxDev #Blender #](https://x.com/palelzr/status/2067007081421717663) |
| x | ScansFactory | ^36 c0 | [Details are a priority for us, right from location scanning all the way to the f](https://x.com/ScansFactory/status/2066928795093967220) |
| x | KIRI_Engine_App | ^36 c2 | [We came back from travelling with thousands of 3D scan photos, random shots, vid](https://x.com/KIRI_Engine_App/status/2066797002453905771) |
| x | jettelly | ^35 c1 | [Creating procedural effects in Unity can feel like magic until you understand th](https://x.com/jettelly/status/2066566411020021942) |
| x | nxpatterns | ^35 c2 | [Open the video in the YouTube app on your phone (not the browser). Now literally](https://x.com/nxpatterns/status/2066858675679990063) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@faenir_morne</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1680 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/faenir_morne/status/2066845394235949376">View @faenir_morne on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Memories. 2019. I was 25. Short haircut, freckles, young. I got invited to a photogrammetry studio! Dozens of cameras were shooting me from every angle while I froze in different poses. It was an incr”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A creator shares a personal memory of being 3D-scanned via photogrammetry in 2019 — dozens of cameras, multiple poses — with the collector-figure project shelved when COVID hit.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/faenir_morne/status/2066845394235949376" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@c_valenzuelab</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 713 · 💬 169</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/c_valenzuelab/status/2066922813466779876">View @c_valenzuelab on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Imagine waking up and realizing that your full time job entails using a digital cinema camera with a 65mm large format CMOS sensor fabricated on a sub-20nm semiconductor process, capturing 16-bit line”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A filmmaker enumerates the full digital pipeline behind 'real' cinema — ACES color management, ML denoising, optical flow, NeRF, photogrammetry, LiDAR, ray tracing — to argue cinema has always been artificial.</dd>
      <dt>Why interesting</dt>
      <dd>The tech stack cited — NeRF, photogrammetry, LiDAR, ML denoising, PBR, ray tracing — maps directly onto tools available in Unity and XR production pipelines today.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's XR/Unity team can audit which of these pipeline stages (ACES, photogrammetry, ML denoising, NeRF) are already in use and flag gaps worth closing.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/c_valenzuelab/status/2066922813466779876" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@80Level</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 592 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/80Level/status/2066868400261874001">View @80Level on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Have a look at this 90s anime-style shader in Blender by @Jorm_0ff, inspired by Vampire Hunter D. Learn anime-style 3D art in Blender: https://t.co/oQWmnrl5PT https://t.co/jGEINgDAhI”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Artist Jorm_0ff built a Vampire Hunter D-inspired 90s anime cel shader in Blender, with a tutorial link shared by 80Level.</dd>
      <dt>Why interesting</dt>
      <dd>Stylized cel shading in Blender is a low-cost way to add distinct visual identity to Unity projects without custom engine shaders.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity art team can study the Blender shader breakdown and replicate the look via Unity's Shader Graph for stylized game projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/80Level/status/2066868400261874001" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IBuzovskyi</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 312 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IBuzovskyi/status/2066724948702626255">View @IBuzovskyi on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“HERMES AGENT CAN CREATE VIDEOS. NOT WITH AN API CALL. IT WRITES THE CODE, RENDERS THE SCENES, AND STITCHES THEM INTO AN MP4. the video attached to this post was generated by Hermes Agent using manim-v”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Hermes Agent generates MP4s by writing Python/Manim code, rendering scenes, and stitching clips — two bundled skills: Manim CE for algorithm/math animations and HyperFrames for motion graphics via HTML+GSAP.</dd>
      <dt>Why interesting</dt>
      <dd>The Manim pipeline (PLAN→CODE→RENDER→STITCH→AUDIO) maps directly to e-learning explainer production the studio already does manually.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run the Manim pipeline on one existing e-learning module to benchmark whether automated scene rendering cuts production time.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IBuzovskyi/status/2066724948702626255" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 270 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2066995632368238653">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Zhu Yuan eyebrows rigged! Using a shape key and bone based hybrid! Really happy with how it looks, it's pretty incredible how expressive eyebrows can be😄 #blender #rig #rigging https://t.co/skdk3rAuDE”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Blender artist rigged a character's eyebrows with a hybrid shape key + bone system, showing how much facial expressiveness the combo delivers.</dd>
      <dt>Why interesting</dt>
      <dd>Hybrid shape key + bone rigs outperform pure bone rigs for subtle facial movement — directly applicable to Unity character and XR avatar pipelines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can test this hybrid eyebrow rig pattern in Blender before export to improve expressiveness in game characters or XR avatars.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2066995632368238653" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RadianceFields</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 206 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RadianceFields/status/2066565454035112090">View @RadianceFields on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple may have just launched Spatial Reframe, but Huawei has full on gaussian splatting on lock screens. https://t.co/IdoITBcZxr”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Huawei shipped real-time Gaussian splatting as an animated lock-screen effect on consumer handsets, going further than Apple's Spatial Reframe, which reframes spatial video for flat displays.</dd>
      <dt>Why interesting</dt>
      <dd>Proves 3D Gaussian splatting runs at interactive frame rates on mobile-class GPUs — a concrete hardware bar the studio's XR/VR scene capture pipeline can now target.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity XR team should benchmark UnityGaussianSplatting on target mobile hardware now that consumer devices are confirmed capable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RadianceFields/status/2066565454035112090" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mangaka7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 185 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mangaka7/status/2066693948031033765">View @mangaka7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Taking MinusT's SD characters course on Coloso! Finished the base mesh and hair. Will work on clothing next and then move on to texturing and rigging! I'm new to Blender. What do you think? Any feedba”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A self-described Blender beginner shares WIP SD character art (base mesh + hair) made while taking MinusT's SD character course on Coloso, with clothing, texturing, and rigging still ahead.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mangaka7/status/2066693948031033765" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DAIEvolutionHub</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 180 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DAIEvolutionHub/status/2066635993844003197">View @DAIEvolutionHub on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“SOMEONE JUST DESTROYED THE REAL ESTATE SECTOR AND NO ONE IS TALKING ABOUT IT Someone scanned an entire house with their phone. They uploaded it. Now anyone on earth can walk through it from their brow”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>3D Gaussian Splatting — an AI-driven technique that reconstructs phone photos into renderable splat scenes — now has an open-source browser viewer built on PlayCanvas, scanning a space for roughly $200.</dd>
      <dt>Why interesting</dt>
      <dd>Browser-native gaussian splat scenes with no app install are directly applicable to the studio's XR/VR and e-learning work wherever a photorealistic real-space walkthrough is needed.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Clone the PlayCanvas Gaussian Splatting repo, scan one real space with a phone, and benchmark load time and visual quality against the studio's current XR pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DAIEvolutionHub/status/2066635993844003197" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
