---
type: social-topic-report
date: '2026-06-09'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-09T03:31:50+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 42
salience: 0.7
sentiment: positive
confidence: 0.65
tags:
- gaussian-splatting
- apple-maps
- 3d-capture
- blender
- xr
- photogrammetry
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2064057009348005888/img/9TfGqQJ71uxtmsSy.jpg
---

# 3D & Graphics — 2026-06-09

## TL;DR
- Apple announced Gaussian Splatting in Apple Maps at WWDC 2026, built from oblique aerial imagery rather than mesh photogrammetry — the most-engaged item by far (scores 3145/2177/1422) [1][2][3].
- Commentators frame it as Apple beating Google to consumer-scale 3D capture, and the first major Apple Maps overhaul since 2021 with likely Vision Pro relevance [38][40][41].
- 3DGS is spreading past maps: consumer portrait capture via KIRI Engine [26], ETH Zürich's ViserDex using RGB-only splatting for robot in-hand control [14], and a faster ellipsoid-projection method for perspective-stable splats [12].
- Blender tooling activity: Insydium's NeXus particle/fluid sim (previously Cinema 4D-only) entered public beta [30], plus a click-and-drag retopology tool [17] and a cloth-stretch wrinkle-map shader test [4].
- Photogrammetry-to-game pipeline examples surfaced: a 5k-tri shoe-scan workflow cleaned in Blender [28] and a peer-reviewed whale-skeleton reconstruction paper [8].

## What happened
The day's dominant signal is Apple's WWDC 2026 announcement that 3D Gaussian Splatting is coming to Apple Maps, generated from oblique aerial imagery and presented as cleaner than mesh photogrammetry [1][2][3]. Multiple posters framed it as Apple reaching consumer 3D maps before Google [41], the first significant Apple Maps update since 2021 [38], with hopes for a first-class Vision Pro app [40]. This single story holds the top three engagement scores by a wide margin.

## Why it matters (reasoning)
Apple shipping 3DGS to a default consumer app moves Gaussian Splatting from a research/enthusiast technique toward mainstream production and viewing infrastructure [1][41]. Second-order effects: capture tooling and viewers gain a large install base, which pulls more apps (KIRI's consumer portraits [26]) and research (RGB-only robot manipulation [14], faster projection math [12]) along with it. For an XR/games studio, the relevant shift is that splat-based environments may become an expected content format on Apple hardware, especially if Vision Pro gains native support [40]. The Blender items show steady, incremental pipeline improvement rather than a single break: NeXus widening simulation options on Blender [30] and faster retopology [17] reduce asset-cleanup time, the recurring bottleneck when feeding scans into Unity/Unreal [28].

## Possibility
Likely: more capture and viewer apps adopt 3DGS export now that a platform owner validates it at scale [1][26]. Plausible: Apple adds native splat support to Vision Pro Maps, given the explicit demand [40] and the land-grab framing [41] — but no source confirms a date. Plausible: research advances (perspective-stable projection [12], sim-to-real control [14]) shorten the path to real-time splats in engines, though none of these are engine-integrated today. Unlikely near-term: splats replace polygon meshes in game pipelines — every game-ready example here still relies on mesh retopology and cleanup [17][28]. No source gives numeric forecasts, so none are asserted.

## Org applicability — NDF DEV
1) Trial a 3DGS capture-to-XR test using a consumer app like KIRI Engine to evaluate splats for location/asset content in XR experiences (effort: med) [26][1]. 2) Install the free NeXus Blender public beta to assess particle/fluid sim for VFX without a Cinema 4D license (effort: low) [30]. 3) Evaluate the click-and-drag Blender retopology tool to speed scan/sculpt cleanup for game-ready meshes (effort: low) [17]. 4) Document a photogrammetry workflow target (e.g. ~5k tris, Blender smoothing pass) for scanned props used in games/edutech assets (effort: med) [28]. 5) Keep procedural Unity VFX references (manta ray system [27], impact frame [9]) for the real-time effects backlog (effort: low). Skip: the politics, Baofeng-radio, fandom-WIP, and convention-drama items [7][15][20][32][13] — no production relevance.

## Signals to Watch
- Whether Apple ships native 3DGS Maps support on Vision Pro, which would set an XR content-format expectation [40][41].
- 3DGS export appearing in more consumer/prosumer capture apps following Apple's validation [26][1].
- Real-time/perspective-stable splat rendering maturing toward engine integration [12][14].
- Insydium NeXus moving from beta to release on Blender as a sim option [30].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^3145 c77 | [holy crap! apple just beat google to the punch -- 3d gaussian splatting is comin](https://x.com/bilawalsidhu/status/2064057313057439795) |
| x | RadianceFields | ^2177 c25 | [Apple just announced gaussian splatting is coming to Apple Maps at WWDC. https:/](https://x.com/RadianceFields/status/2064043440350888050) |
| x | YIMBYLAND | ^1422 c20 | [Apple just released 3D gaussian splatting on Apple Maps 🤯 This is gonna hit the ](https://x.com/YIMBYLAND/status/2064077227952627823) |
| x | 3DxDEV7 | ^905 c0 | [Check out this stunning shader test by Cartesian Caramel ✨ A breakdown of how wr](https://x.com/3DxDEV7/status/2063879964999442914) |
| x | ItzFAILURE | ^731 c1 | [Saw this and got immediately insured for more white rose agenda posting WIPs…. I](https://x.com/ItzFAILURE/status/2064061177458491784) |
| x | ItzFAILURE | ^706 c2 | [the WHOLE ass wip of the scene. One of my favorites of Vol 2 Rigs: @cookie_sugar](https://x.com/ItzFAILURE/status/2063824452366766191) |
| x | CreasonJana | ^375 c26 | [I did not know this … @VP @JDVance has the authority to walk into the chamber, t](https://x.com/CreasonJana/status/2063959635996860672) |
| x | HS_Shinmura | ^306 c0 | [Full-text access now available! My paper on the 3D reconstruction of whale skele](https://x.com/HS_Shinmura/status/2063560104725934084) |
| x | GameZoneHQ | ^170 c0 | [Procedurally generated impact frame with shader and particle system by @namutree](https://x.com/GameZoneHQ/status/2063878287865028798) |
| x | dynastiees | ^169 c16 | [Frieren The Height of Magic recreation Vfx - me Animations @Devgrams Sfx @ZykiuD](https://x.com/dynastiees/status/2063655876519448821) |
| x | MrZing07 | ^151 c7 | [Friendly reminder that my 3D beginner vtuber course's first episode will be on y](https://x.com/MrZing07/status/2063990740296835564) |
| x | Michael_Moroz_ | ^126 c2 | [I also found this fast nifty way to project an ellipsoid given an arbitrary proj](https://x.com/Michael_Moroz_/status/2063474503708033323) |
| x | VixenVRC | ^83 c10 | [This year reflects the damage it did, Not gonna lie but i didn't bother attendin](https://x.com/VixenVRC/status/2063649767939342647) |
| x | lukas_m_ziegler | ^83 c4 | [Robot hands are getting out of hand! ✊🏼 RGB-only dexterous hand control via 3D G](https://x.com/lukas_m_ziegler/status/2063678741386342895) |
| x | bilawalsidhu | ^74 c7 | [Baofeng radios? Chinese dynamism… $15-35 handhelds that punch way above their we](https://x.com/bilawalsidhu/status/2063849083819766036) |
| x | bryanvenzen | ^73 c3 | [When I was working at Retro Studios (Nintendo) on Metroid Prime Remastered, we w](https://x.com/bryanvenzen/status/2064074392708006234) |
| x | AFX_LAB | ^69 c1 | [Check out this retopology tool for Blender You can click &amp; drag to generate ](https://x.com/AFX_LAB/status/2064091649500905892) |
| x | DemNikoArt | ^66 c1 | [I accidentally developed a new look for my YouTube thumbnails 😁 I kinda like it.](https://x.com/DemNikoArt/status/2063915373112525306) |
| x | Der_Kernel_ | ^63 c7 | [This makes a lot more sense when you realize the announcement was only to boost ](https://x.com/Der_Kernel_/status/2063949463010345293) |
| x | monarchreport25 | ^59 c2 | [Young Woman’s Plea for Re-Election Highlights Deepening Concerns Over Electoral ](https://x.com/monarchreport25/status/2064019285098275068) |
| x | SkinnyfatTony | ^59 c3 | [I like to mess with reverse engineering, when I had time I would 3d scan parts o](https://x.com/SkinnyfatTony/status/2063659335050531160) |
| x | bilawalsidhu | ^55 c3 | [Deep tech founders circa 1910 https://t.co/YyIeQzIwx4](https://x.com/bilawalsidhu/status/2063458023209648517) |
| x | Leave_MeBee | ^50 c5 | [i hate rigging hunters in blender, your capes are SO ANNOYING 😭 WHY DID IT HAVE ](https://x.com/Leave_MeBee/status/2063481281988428016) |
| x | bilawalsidhu | ^49 c1 | [want to go deeper down the 3d capture rabbit hole? i have a whole playlist of vi](https://x.com/bilawalsidhu/status/2064087817286828280) |
| x | kingrobloxyuri | ^46 c1 | [@rhoosecaboose posing characters in a 3D program is still a render, sure its not](https://x.com/kingrobloxyuri/status/2064108590701416629) |
| x | KIRI_Engine_App | ^37 c3 | [Graduation photos hit different when they're 3D Gaussian Splatting portraits. Di](https://x.com/KIRI_Engine_App/status/2063908905114091834) |
| x | 80Level | ^36 c0 | [Technical Artist Jawad Srour has shared a breakdown of his fully procedural mant](https://x.com/80Level/status/2063984397041488025) |
| x | blenderguppy | ^36 c1 | [Another successful shoe scan. 5k tris. I think I finally ironed out the workflow](https://x.com/blenderguppy/status/2063855888063238650) |
| x | AsahiArtist | ^35 c0 | [Holographic sticker shader test in Unity ✨ #unity #shader https://t.co/XDDDirOQD](https://x.com/AsahiArtist/status/2063518218103472134) |
| x | theCGchannel | ^31 c0 | [NeXus for Blender is now in public beta Register for an Insydium account to requ](https://x.com/theCGchannel/status/2064041239243022621) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3145 · 💬 77</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2064057313057439795">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“holy crap! apple just beat google to the punch -- 3d gaussian splatting is coming to apple maps. these 3d scenes are made from oblique aerial imagery. but unlike blobby photogrammetry -- no more brocc”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Apple Maps is shipping 3D Gaussian Splatting scenes built from oblique aerial imagery, delivering clean ground-level detail that traditional photogrammetry consistently fails to produce.</dd>
      <dt>Why interesting</dt>
      <dd>Apple shipping 3DGS in a consumer product signals that device-level support and tooling will mature fast — a direct benefit for any XR/VR environment capture work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a quick spike using Luma AI or Polycam 3DGS capture on a real location to evaluate quality for XR/VR scenes before the pipeline becomes crowded.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2064057313057439795" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RadianceFields</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2177 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RadianceFields/status/2064043440350888050">View @RadianceFields on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple just announced gaussian splatting is coming to Apple Maps at WWDC. https://t.co/lKG5G0XOkC”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Apple announced at WWDC 2025 that Gaussian splatting will be integrated into Apple Maps for photorealistic 3D scene rendering.</dd>
      <dt>Why interesting</dt>
      <dd>Gaussian splatting entering a first-party Apple product signals the technique is production-ready and worth investing in for XR/VR and Unity 3D work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should evaluate Gaussian splatting pipelines (e.g. Unity Gaussian Splatting packages) for upcoming XR or environment-heavy Unity projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RadianceFields/status/2064043440350888050" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@YIMBYLAND</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1422 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/YIMBYLAND/status/2064077227952627823">View @YIMBYLAND on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple just released 3D gaussian splatting on Apple Maps 🤯 This is gonna hit the Urbanist community the way crack cocaine hit 1980s New York. https://t.co/xVoBQeUaak”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Apple has shipped 3D Gaussian Splatting — a real-time photorealistic scene-reconstruction technique — inside Apple Maps as a production consumer feature.</dd>
      <dt>Why interesting</dt>
      <dd>Apple deploying Gaussian Splatting at consumer scale confirms the technique is production-ready and will accelerate Unity and XR tooling support.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity XR team should benchmark existing Gaussian Splatting plugins against Apple's deployment as a new quality and performance baseline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/YIMBYLAND/status/2064077227952627823" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 905 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2063879964999442914">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out this stunning shader test by Cartesian Caramel ✨ A breakdown of how wrinkle maps can simulate cloth stretching in Blender, and the result is seriously impressive. #B3D #Blender #Blender3D #S”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Cartesian Caramel published a Blender shader breakdown showing how wrinkle maps drive dynamic cloth-stretch simulation entirely in the shader, no simulation bake needed.</dd>
      <dt>Why interesting</dt>
      <dd>Shader-driven wrinkle maps keep cloth detail cheap at runtime — useful for character assets in Unity games or XR avatars where cloth sim is too costly.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can study this technique and apply wrinkle map logic via a custom shader in URP/HDRP for cloth-wearing characters in current or upcoming projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2063879964999442914" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 731 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2064061177458491784">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Saw this and got immediately insured for more white rose agenda posting WIPs…. I’m a real sucker for eyes and teeth. as per usual Model: @Artstudious Rig: @cookie_sugar42 Shader: @LuminaryOfAges Textu”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan animator shared a Blender-rendered RWBY character WIP, crediting separate artists for model, rig, shader, and textures.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ItzFAILURE/status/2064061177458491784" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 706 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2063824452366766191">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“the WHOLE ass wip of the scene. One of my favorites of Vol 2 Rigs: @cookie_sugar42 Textures: @Hiru3152 Shader: @LuminaryOfAges #FNDM #blender #animation #whiterose #RWBY https://t.co/CsYvuA7KR0”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An animator shared a Blender WIP scene from a fan animation project (RWBY Vol 2), crediting separate artists for rigs, textures, and shader work.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ItzFAILURE/status/2063824452366766191" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CreasonJana</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 375 · 💬 26</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CreasonJana/status/2063959635996860672">View @CreasonJana on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I did not know this … @VP @JDVance has the authority to walk into the chamber, take the presiding officers chair as Senate President &amp; enforce the rules that would enable a ‘talking filibuster’! So, t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Twitter user discusses US Senate procedural mechanics — specifically whether VP JD Vance could enforce a talking filibuster to pass the SAVE America Act.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CreasonJana/status/2063959635996860672" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HS_Shinmura</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 306 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HS_Shinmura/status/2063560104725934084">View @HS_Shinmura on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Full-text access now available! My paper on the 3D reconstruction of whale skeletal configuration using stepwise photogrammetry is now freely available via Wiley Article Share. Read here: https://t.co”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Researcher @HS_Shinmura published an open-access paper on 3D reconstruction of whale skeletal structures using a stepwise photogrammetry method via Wiley.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HS_Shinmura/status/2063560104725934084" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
