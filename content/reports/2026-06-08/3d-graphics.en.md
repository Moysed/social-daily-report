---
type: social-topic-report
date: '2026-06-08'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-06-08T15:37:31+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 30
salience: 0.32
sentiment: neutral
confidence: 0.55
tags:
- gaussian-splatting
- blender
- photogrammetry
- shaders
- unity
- ai-3d
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2063397198880997376/img/VO1JqR2shYQ0NIp0.jpg
---

# 3D & Graphics — 2026-06-08

## TL;DR
- Gaussian Splatting shows the strongest research signal: a faster perspective-stable ellipsoid-to-screen projection method [9], ETH Zürich's ViserDex using RGB-only 3DGS for sim-to-real robot hand control [14], and COLMAP scene-merging tests via the lichtfeldstudio tool [26].
- Blender remains the production workhorse across items — a procedural explosion generator [2], wrinkle-map cloth-stretch shaders [3], and several rigging tutorials/WIPs [5][12][17][19][20].
- Photogrammetry appears as practical, game-ready workflow rather than research: a 5k-tri shoe scan with a settled clean-up pipeline [24], part scanning for reverse engineering [16], and a freely-available stepwise whale-skeleton reconstruction paper [4].
- Engine-facing work is incremental: a Unity holographic sticker shader [23], threejs open-world authoring [10], and AI 3D-gen tools (MeshyAI [30], Seedance 2.0 + GPT Image 2 [22]).
- No major tool releases today (no Blender/Unity/Unreal version news); the single highest-engagement item [1] is pseudo-archaeology framing around a laser scan, not usable signal.

## What happened
Today's 3D/graphics items are mostly community work-in-progress and small research notes rather than product news. The clearest technical thread is Gaussian Splatting: [9] shares a fast method to project an arbitrary ellipsoid onto screen for perspectively stable splatting, [14] is an ETH Zürich sim-to-real framework (ViserDex) doing in-hand object reorientation from RGB-only 3DGS, and [26] documents merging COLMAP datasets for splatting using the lichtfeldstudio program. Photogrammetry shows up as applied pipeline work — [24] reports a stabilized shoe-scan workflow producing a 5k-tri game-ready mesh (reconstruct, smooth surface noise in Blender, re-import), [16] scans Yamaha parts for reverse engineering, and [4] publishes an open-access stepwise photogrammetry paper on whale skeletal reconstruction.

## Why it matters (reasoning)
The mix confirms where asset-production effort is concentrating. Gaussian Splatting is maturing from novelty toward tooling and cross-domain use: a projection-math optimization [9], a robotics application proving the representation is good enough for closed-loop control [14], and a dedicated authoring tool with multi-capture merging [26] together indicate the pipeline (capture → COLMAP → splat → edit) is becoming repeatable rather than experimental. For photogrammetry, [24]'s emphasis on a 'finally ironed out' workflow and a tri-budget target shows the bottleneck has moved from reconstruction quality to game-engine cleanup, which is exactly the integration cost a studio pays. Blender's recurrence across procedural VFX [2], shaders [3], and rigging [5][12][17][19][20] reinforces it as the default DCC hub feeding engines. The caveat: most items are single-author anecdotes, not benchmarked or released products, so the signal is directional, not decisive.

## Possibility
Likely: Gaussian Splatting continues consolidating into editable, engine-bound pipelines, given simultaneous progress on core math [9], tooling [26], and applied use [14]. Plausible: studios fold splat/photogrammetry capture into XR asset production once mesh/tri cleanup is solved [24], though splats still don't drop cleanly into standard Unity/Unreal lighting and animation. Plausible: AI 3D-gen (MeshyAI [30], Seedance+GPT Image [22]) becomes a prototyping front-end, but quality and topology remain unproven from these items. Unlikely: any of today's items forces a near-term pipeline change — none are releases, none carry benchmarks, and no source states adoption numbers.

## Org applicability — NDF DEV
1) Trial a Gaussian Splatting capture-to-XR test on one real object using the lichtfeldstudio workflow [26] and watch the projection method [9] for runtime stability — effort med; gates whether splats are viable for the studio's XR experiences. 2) Adopt the documented photogrammetry-to-Blender cleanup pattern (reconstruct → smooth noise → re-import, target ~5k tris) for real-world props in games/XR [24][16] — effort low-med; directly reusable for asset production. 3) Evaluate the Blender procedural explosion generator [2] and wrinkle-map cloth shader [3] as reusable VFX/material techniques — effort low. 4) Prototype the Unity holographic shader effect [23] for game/XR UI or collectible polish — effort low. 5) Spot-test MeshyAI [30] for throwaway prototype assets only, not production — effort low. Skip: the Kailasa laser-scan thread [1] (pseudo-archaeology, no usable method), and all non-3D items — politics [8], VRChat convention drama [11], drone stock analysis [13], radios [15].

## Signals to Watch
- Watch lichtfeldstudio and COLMAP-merge workflows maturing for multi-capture splat scenes [26].
- Watch RGB-only Gaussian Splatting moving into control/robotics, a sign the representation is becoming reliable [14].
- Watch the free 3D beginner VTuber course launching June 15 and Cover's 3D capture tech [21][25] for low-cost avatar/mocap pipelines relevant to XR.
- Watch threejs open-world authoring as a reference for web/mobile 3D delivery [10].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | JIX5A | ^16221 c228 | [Kailasa was just scanned with lasers, and if you haven’t been following this pla](https://x.com/JIX5A/status/2063397266090574013) |
| x | 3DxDEV7 | ^2037 c7 | [Check out how Hiroshi Kanazawa showcased this Blender-powered explosion generato](https://x.com/3DxDEV7/status/2063276491480105412) |
| x | 3DxDEV7 | ^396 c0 | [Check out this stunning shader test by Cartesian Caramel ✨ A breakdown of how wr](https://x.com/3DxDEV7/status/2063879964999442914) |
| x | HS_Shinmura | ^281 c0 | [Full-text access now available! My paper on the 3D reconstruction of whale skele](https://x.com/HS_Shinmura/status/2063560104725934084) |
| x | ItzFAILURE | ^269 c2 | [the WHOLE ass wip of the scene. One of my favorites of Vol 2 Rigs: @cookie_sugar](https://x.com/ItzFAILURE/status/2063824452366766191) |
| x | bestkingsun1 | ^247 c3 | [Stormcutter model made for a roblox game called "Rise of dragons" Were looking f](https://x.com/bestkingsun1/status/2063319729800871957) |
| x | dynastiees | ^157 c16 | [Frieren The Height of Magic recreation Vfx - me Animations @Devgrams Sfx @ZykiuD](https://x.com/dynastiees/status/2063655876519448821) |
| x | CreasonJana | ^143 c10 | [I did not know this … @VP @JDVance has the authority to walk into the chamber, t](https://x.com/CreasonJana/status/2063959635996860672) |
| x | Michael_Moroz_ | ^126 c2 | [I also found this fast nifty way to project an ellipsoid given an arbitrary proj](https://x.com/Michael_Moroz_/status/2063474503708033323) |
| x | alightinastorm | ^98 c15 | [Vibe Coding a AAA game with threejs Day 10: Deep dive into world authoring What ](https://x.com/alightinastorm/status/2063452003036971131) |
| x | VixenVRC | ^83 c10 | [This year reflects the damage it did, Not gonna lie but i didn't bother attendin](https://x.com/VixenVRC/status/2063649767939342647) |
| x | DemNikoArt | ^79 c2 | [You seemed to like this one. The tutorial for it is out now 😉 🔗 below #b3d #blen](https://x.com/DemNikoArt/status/2063295864689262853) |
| x | LnprCapital | ^74 c3 | [Ideaforge Technology Ltd Market Cap : ₹ 4100 Crores. FY25 nearly broke the story](https://x.com/LnprCapital/status/2063787083819585730) |
| x | lukas_m_ziegler | ^72 c3 | [Robot hands are getting out of hand! ✊🏼 RGB-only dexterous hand control via 3D G](https://x.com/lukas_m_ziegler/status/2063678741386342895) |
| x | bilawalsidhu | ^62 c6 | [Baofeng radios? Chinese dynamism… $15-35 handhelds that punch way above their we](https://x.com/bilawalsidhu/status/2063849083819766036) |
| x | SkinnyfatTony | ^57 c3 | [I like to mess with reverse engineering, when I had time I would 3d scan parts o](https://x.com/SkinnyfatTony/status/2063659335050531160) |
| x | RyanLykos | ^55 c1 | [Finished the textures for my Smart Pistol! Ready to start rigging it, and finall](https://x.com/RyanLykos/status/2063385152470860065) |
| x | bilawalsidhu | ^53 c3 | [Deep tech founders circa 1910 https://t.co/YyIeQzIwx4](https://x.com/bilawalsidhu/status/2063458023209648517) |
| x | Leave_MeBee | ^50 c5 | [i hate rigging hunters in blender, your capes are SO ANNOYING 😭 WHY DID IT HAVE ](https://x.com/Leave_MeBee/status/2063481281988428016) |
| x | DemNikoArt | ^47 c1 | [I accidentally developed a new look for my YouTube thumbnails 😁 I kinda like it.](https://x.com/DemNikoArt/status/2063915373112525306) |
| x | MrZing07 | ^46 c3 | [Friendly reminder that my 3D beginner vtuber course's first episode will be on y](https://x.com/MrZing07/status/2063990740296835564) |
| x | auqibhabib | ^38 c15 | [Made with seedance 2.0 + GPT Image 2 @image1 fights three opponents inside a Jap](https://x.com/auqibhabib/status/2063332990185619963) |
| x | AsahiArtist | ^35 c0 | [Holographic sticker shader test in Unity ✨ #unity #shader https://t.co/XDDDirOQD](https://x.com/AsahiArtist/status/2063518218103472134) |
| x | blenderguppy | ^30 c1 | [Another successful shoe scan. 5k tris. I think I finally ironed out the workflow](https://x.com/blenderguppy/status/2063855888063238650) |
| x | Riko_de_Sama | ^25 c1 | [@V_Faction Honestly, one of the biggest test of Cover's 3D capture tech if there](https://x.com/Riko_de_Sama/status/2063636519252885964) |
| x | blue_nile_3d | ^21 c1 | [Experimenting with merging Colmap data on top of each other for Gaussian Splatti](https://x.com/blue_nile_3d/status/2063300074487304689) |
| x | bilawalsidhu | ^10 c0 | [@rpnickson Now this is a mfing ad - bravo!](https://x.com/bilawalsidhu/status/2063459517451440418) |
| x | multimodalart | ^8 c4 | [where we are headed, all software becomes open source software models can decomp](https://x.com/multimodalart/status/2063307704873951333) |
| x | bilawalsidhu | ^7 c0 | [@sriramk @ayirpelle Congrats on a great run and thank you for your service Srira](https://x.com/bilawalsidhu/status/2063333617506377794) |
| x | MeshyAI | ^2 c0 | [@IHayato Bravo👏🏻](https://x.com/MeshyAI/status/2063858081914925453) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@JIX5A</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 16221 · 💬 228</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/JIX5A/status/2063397266090574013">View @JIX5A on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Kailasa was just scanned with lasers, and if you haven’t been following this place, hold on. What’s being uncovered here won’t just rewrite Indian history. It could rewrite human history and prove Anc”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral X post uses news of Kailasa temple being laser-scanned as a hook to speculate about ancient advanced civilizations, focusing on historical mystery rather than the scanning technology or its data.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/JIX5A/status/2063397266090574013" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2037 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2063276491480105412">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out how Hiroshi Kanazawa showcased this Blender-powered explosion generator — 💥 Really cool progress on this project. What part stands out most to you? 👀 #B3D #Blender3D #Blender #Animation #VFX”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Hiroshi Kanazawa demonstrated a procedural explosion generator built entirely in Blender using Geometry Nodes, shared as a WIP VFX showcase.</dd>
      <dt>Why interesting</dt>
      <dd>Geometry Nodes-based explosion rigs can be exported as reusable VFX assets for Unity games or XR scenes without buying stock FX packs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/VFX team can prototype reusable procedural explosion assets in Blender Geometry Nodes for in-game or XR environments.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2063276491480105412" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 396 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2063879964999442914">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out this stunning shader test by Cartesian Caramel ✨ A breakdown of how wrinkle maps can simulate cloth stretching in Blender, and the result is seriously impressive. #B3D #Blender #Blender3D #S”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Cartesian Caramel demonstrates a Blender shader technique using wrinkle maps to simulate cloth stretching without running a full cloth simulation.</dd>
      <dt>Why interesting</dt>
      <dd>Wrinkle-map cloth shading is cheaper to compute than physics simulation and can be baked into assets for real-time use in Unity or XR projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's 3D artists can study this breakdown and apply wrinkle-map cloth shading to character assets before exporting to Unity.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2063879964999442914" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HS_Shinmura</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 281 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HS_Shinmura/status/2063560104725934084">View @HS_Shinmura on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Full-text access now available! My paper on the 3D reconstruction of whale skeletal configuration using stepwise photogrammetry is now freely available via Wiley Article Share. Read here: https://t.co”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A researcher published an open-access paper detailing a stepwise photogrammetry workflow used to produce accurate 3D reconstructions of whale skeletal structures.</dd>
      <dt>Why interesting</dt>
      <dd>The stepwise capture method for large, articulated physical objects is a practical methodology reference for teams building scan-based 3D assets for XR or e-learning.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/e-learning team can read the methodology section as a structured reference before planning photogrammetry captures of large or complex physical objects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HS_Shinmura/status/2063560104725934084" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 269 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2063824452366766191">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“the WHOLE ass wip of the scene. One of my favorites of Vol 2 Rigs: @cookie_sugar42 Textures: @Hiru3152 Shader: @LuminaryOfAges #FNDM #blender #animation #whiterose #RWBY https://t.co/CsYvuA7KR0”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An RWBY fan animator on X shared a Blender WIP scene from Vol 2, crediting separate artists for rigs, textures, and shader work.</dd>
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
    <span class="ndf-author">@bestkingsun1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 247 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bestkingsun1/status/2063319729800871957">View @bestkingsun1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Stormcutter model made for a roblox game called &quot;Rise of dragons&quot; Were looking for animators,Vfx designers! https://t.co/iJtEGh00Qe #httyd #HowToTrainYourDragon #dragon #3Dmodel #blender #3dart #3DArt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An independent 3D artist shared a Blender-made Stormcutter dragon model built for a Roblox game 'Rise of Dragons,' and is recruiting animators and VFX designers.</dd>
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
    <span class="ndf-author">@dynastiees</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 157 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/dynastiees/status/2063655876519448821">View @dynastiees on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Frieren The Height of Magic recreation Vfx - me Animations @Devgrams Sfx @ZykiuDev Map @luhr1n Emotional support @ZerphVfx @lonely_nights9 @liqqzzzz @4yuyo @northeasttprod @d229n #Unity #VFX #RobloxDe”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer team recreated the 'Frieren: The Height of Magic' spell scene in Unity as a Roblox VFX showcase, with credited roles for VFX, animation, SFX, and map.</dd>
      <dt>Why interesting</dt>
      <dd>Shows a practical split-role pipeline for stylized anime VFX inside Unity targeting Roblox — useful reference for the studio's Unity VFX work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Review the video breakdown to extract timing and layering techniques applicable to the studio's own Unity particle/VFX scenes.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/dynastiees/status/2063655876519448821" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CreasonJana</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 143 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CreasonJana/status/2063959635996860672">View @CreasonJana on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I did not know this … @VP @JDVance has the authority to walk into the chamber, take the presiding officers chair as Senate President &amp; enforce the rules that would enable a ‘talking filibuster’! So, t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A US political commentator outlines JD Vance's constitutional authority as Senate President to preside over filibuster procedure for the SAVE America Act.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CreasonJana/status/2063959635996860672" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
