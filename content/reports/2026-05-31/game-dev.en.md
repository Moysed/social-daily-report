---
type: social-topic-report
date: '2026-05-31'
topic: game-dev
lang: en
pair: game-dev.th.md
generated_at: '2026-05-31T04:09:00+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 32
salience: 0.55
sentiment: neutral
confidence: 0.6
tags:
- unity
- ai-pipeline
- 3d-generation
- godot
- tooling
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060606108763295745/img/-oeMxhDSxmtuOXkf.jpg
---

# Game Dev — 2026-05-31

## TL;DR
- Microsoft released Trellis.2, an open-source 4B model converting an image to a textured 3D GLB mesh in ~3s (under 100ms on CUDA), output ready for Blender/Unity/Unreal [3].
- Godot 4.7 beta 4 shipped, with a Release Candidate said to be near [5].
- Unity AI is now structured into three modes — Ask, Plan, Agent — for Q&A, planning, and automating repetitive tasks [19]; Unity also pushing Unity Studio, a no-code web editor for industry 3D apps [26].
- Business moves: Balatro publisher Playstack being sold to GameSpot/Fandom parent at ~$169M [30]; 007 First Light topped 1.5M sales [31].
- Open-source Unity character controller released by thesquirrelyjones, handling moving platforms and wall-collision edge cases [2].

## What happened
Tooling and AI dominated the day. Microsoft put out Trellis.2, an open-source 4B image-to-3D model producing GLB meshes in seconds and engine-ready output [3]. Godot advanced to 4.7 beta 4 ahead of an RC [5]. Unity described its AI assistant's three modes (Ask/Plan/Agent) [19] and promoted Unity Studio, a no-code web-based 3D editor [26]. A free open-source Unity character controller was released covering common edge cases [2]. Unreal pushed free UE5 learning content on cinematic environments and Substrate glass [7]. Carmack noted Gmail's writing suggestions improve text but erase authorial voice [1].

On the business side, Playstack (Balatro) is being acquired at ~$169M [30], 007 First Light passed 1.5M sales [31], and Patch Notes #54 covered indie micro-grants, another hardware price hike, and a Witcher 3 expansion [32]. The rest is craft content: shaders [6][21], VFX [4][12], procedural/spline tools [13][16], texturing workflows [22], and indie release announcements [8][11][15][25].

## Why it matters (reasoning)
The clearest signal is AI moving into asset and code pipelines. Trellis.2 being open-source, fast, and emitting GLB ready for all three major engines lowers the cost of first-pass 3D assets [3], which matters for a small studio doing Unity/XR work. Unity's Ask/Plan/Agent framing shows the engine vendor itself building assistant workflows into the editor [19], and Unity Studio targets non-game industrial/AR/VR clients with no-code web 3D [26] — adjacent to NDF's edutech and XR lines. Carmack's point [1] is a real caution: AI output converges toward a generic voice, applicable to generated assets and copy alike — useful for speed, risky for distinctiveness. The business items confirm a tightening market (hardware price hikes [32]) where proven IP still sells [31] and consolidation continues [30], reinforcing that small studios should control costs and lean on cheaper tooling.

## Possibility
Likely: image-to-3D models like Trellis.2 become a standard prototyping/greybox step in indie pipelines, given open-source license and engine-ready GLB output [3]. Likely: Godot 4.7 stable follows soon, as beta 4 is explicitly staging an RC [5]. Plausible: Unity's Agent mode and Unity Studio expand toward non-game/industrial clients, matching the AR/VR-skills positioning Unity is messaging [26][28]. Unlikely (near term): AI-generated assets replace bespoke art for shippable quality — the day's craft content [6][21][22] shows hand-tuned shaders and texturing still carry the visual identity Carmack warns AI flattens [1]. No source gives numeric probabilities.

## Org applicability — NDF DEV
1) Trial Trellis.2 for rapid 3D prototyping/greyboxing in Unity and XR scenes; validate license terms and mesh/topology quality before production use — effort low [3]. 2) Pilot Unity AI's Ask/Plan/Agent on a real Unity task to scope time saved on repetitive editor work — effort low [19]. 3) Drop the open-source Unity character controller into a prototype to evaluate its moving-platform/wall-collision handling — effort low [2]. 4) Watch Unity Studio as a possible delivery path for edutech/industrial XR clients wanting no-code web 3D — effort med, evaluate only [26]. 5) Send UE5 free learning content (cinematic environments, Substrate glass) to any Unreal-side staff — effort low [7]. Skip: indie release/screenshot items [8][11][12][14][15][16][18][25], the asset-bundle sale [9], and business/IP items [30][31] — no direct action for NDF beyond awareness.

## Signals to Watch
- Godot 4.7 RC/stable timing — beta 4 explicitly stages it [5].
- Trellis.2 adoption and asset quality feedback in real Unity/Unreal pipelines [3].
- Unity Agent mode maturity and whether automation is reliable enough for production [19].
- Hardware price hikes [32] — margin pressure on any hardware-dependent XR/VR work.

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ID_AA_Carmack | ^1249 c140 | [I have difficulty arguing that most of the writing changes suggested in gmail no](https://x.com/ID_AA_Carmack/status/2060399696955195843) |
| x | jettelly | ^1160 c5 | [Developer thesquirrelyjones released an open-source custom character controller ](https://x.com/jettelly/status/2060617205989965911) |
| x | RoundtableSpace | ^291 c21 | [Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D ](https://x.com/RoundtableSpace/status/2060477532537827633) |
| x | DAVFX_0 | ^230 c3 | [Anomaly with Illugen #vfx #realtimevfx #illugen #gamedev #unity3d https://t.co/j](https://x.com/DAVFX_0/status/2060306891687809144) |
| x | godotengine | ^209 c7 | [One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for ](https://x.com/godotengine/status/2060503643057496501) |
| x | sean_gause | ^198 c2 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | UnrealEngine | ^174 c8 | [Free learning content for the 5th month of the year? Yeah, we May just have some](https://x.com/UnrealEngine/status/2060396306934436123) |
| x | itchio | ^161 c0 | [Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playa](https://x.com/itchio/status/2060511506815746558) |
| x | ushadersbible | ^143 c0 | [Hey guys, the Technical Art Unity Bundle is 70% OFF 🎁 https://t.co/1eA8907m5M #g](https://x.com/ushadersbible/status/2060220692675678422) |
| x | UnrealEngine | ^94 c26 | [We know that #ScreenshotSaturday is always out of this world So, show us what in](https://x.com/UnrealEngine/status/2060723065991131533) |
| x | itchio | ^67 c0 | [The Board Is Yours: A strategic chess-based incremental game. https://t.co/BHK6Y](https://x.com/itchio/status/2060360518469353950) |
| x | MortalCrux | ^65 c5 | [A mind-blowing magic finisher 🧙‍♀️ #indiegamedev #indiegame #unity3d #pcgamer #m](https://x.com/MortalCrux/status/2060702882001731819) |
| x | jettelly | ^63 c1 | [Developer Sapra shared how the spline-based road system works in their tool, Inf](https://x.com/jettelly/status/2060360513335549985) |
| x | Plasmeo | ^60 c2 | [Who needs cover when you have shielder drones ? #indiedev #gamedev #FPS #Unity #](https://x.com/Plasmeo/status/2060742236816445564) |
| x | itchio | ^57 c0 | [Trigwa: Statue pushing game with a narrative. Each puzzle tells part of a larger](https://x.com/itchio/status/2060405812057780236) |
| x | R2RGames | ^52 c0 | [Almost 300 followers! Here is more progress on my medieval builder, spline walls](https://x.com/R2RGames/status/2060462094802379049) |
| x | mazestalker | ^44 c1 | [I love going back to my pre-URP areas and updating them with 2 years of experien](https://x.com/mazestalker/status/2060495924523135169) |
| x | MJF_game | ^43 c13 | [Modern Jet Fighters Online is now live in Canada 🇨🇦 #Multiplayer #JetFighters #O](https://x.com/MJF_game/status/2060349067666899320) |
| x | unitygames | ^40 c3 | [Meet Unity AI’s three modes: Ask, Plan, and Agent. 1️⃣ Ask: Get your questions a](https://x.com/unitygames/status/2060435608732836007) |
| x | JasozzGames | ^35 c1 | [intellisense please stop this when have i *ever* used that property #gamedev #un](https://x.com/JasozzGames/status/2060361262064599358) |
| x | jettelly | ^35 c0 | [Check out this tree shader by Sqrek, going through the seasons by changing leaf ](https://x.com/jettelly/status/2060239719481405445) |
| x | Rustledust77 | ^34 c1 | [Texturing workflow for our @FracturedRTS units: -&gt; Assign trim sheet material](https://x.com/Rustledust77/status/2060279247491465611) |
| x | OzgursAssets | ^30 c2 | [Modular alternative headlight design #keitruck #gamedev #indiedev #ue5 #Unity3d ](https://x.com/OzgursAssets/status/2060799257293000895) |
| x | FreyaHolmer | ^28 c0 | [@edmundmcmillen I would love to voice some cats!! @TylerGlaiel said I wasn't coo](https://x.com/FreyaHolmer/status/2060326276724916311) |
| x | itchio | ^25 c0 | [Dungeons of Freeport: An Extraction Roguelike Dungeon-Crawler https://t.co/2L6EX](https://x.com/itchio/status/2060451112503722298) |
| x | unity | ^22 c1 | [Think building interactive 3D apps for industry has to be slow and complicated? ](https://x.com/unity/status/2060345542803173429) |
| x | godotengine | ^15 c0 | [Featured game: Elfie: A Sand Plan https://t.co/JAOBcSXMGt](https://x.com/godotengine/status/2060503644617740388) |
| x | unity | ^5 c0 | [@eLAconference @moeghofficial @Proj_RESPECT We can't wait to help empower the ne](https://x.com/unity/status/2060342302732665263) |
| rss | Game Developer Podcast | ^0 c0 | [Crafting Clair Obscur: Expedition 33's mournful tale ft. Jennifer Svedeberg-Yen ](https://www.gamedeveloper.com/design/crafting-clair-obscur-expedition-33-s-mournful-tale-ft-jennifer-svedeberg-yen) |
| rss | Chris Kerr | ^0 c0 | [Balatro publisher Playstack is being sold to GameSpot and Fandom parent company ](https://www.gamedeveloper.com/business/balatro-publisher-playstack-sold-to-gamespot-and-fandom-parent-company) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1249 · 💬 140</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2060399696955195843">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I have difficulty arguing that most of the writing changes suggested in gmail now aren’t improvements, but it does tend to wipe out my particular authorial voice.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>John Carmack observes that Gmail's AI writing suggestions are objectively good edits, but they consistently flatten his personal writing voice.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ID_AA_Carmack/status/2060399696955195843" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1160 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2060617205989965911">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer thesquirrelyjones released an open-source custom character controller for Unity, designed to handle edge cases like moving platforms and wall collisions. 🎮 See more: https://t.co/fpq8pSxsLi ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer thesquirrelyjones released an open-source Unity character controller that handles moving platforms and wall collisions out of the box.</dd>
      <dt>Why interesting</dt>
      <dd>Character controller edge cases eat disproportionate debug time — a battle-tested open-source baseline saves the Unity team from rebuilding this from scratch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team should review the repo and evaluate it as a drop-in starting point for any project requiring custom character movement.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2060617205989965911" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RoundtableSpace</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 291 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RoundtableSpace/status/2060477532537827633">View @RoundtableSpace on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D asset in 3 seconds. Textured mesh under 100ms on CUDA, outputs a GLB file ready for Blender, Unity, and Unreal. Open sou”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Microsoft released Trellis.2, an open-source 4B model that generates a textured GLB mesh from any image in under 3 seconds (sub-100ms on CUDA), ready for Blender, Unity, and Unreal.</dd>
      <dt>Why interesting</dt>
      <dd>GLB output that imports directly into Unity removes the manual texture-and-export step from the 3D asset pipeline for game and XR work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run Trellis.2 locally against concept art or photo references to generate first-pass 3D assets for Unity game and XR builds.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RoundtableSpace/status/2060477532537827633" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DAVFX_0</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 230 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DAVFX_0/status/2060306891687809144">View @DAVFX_0 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anomaly with Illugen #vfx #realtimevfx #illugen #gamedev #unity3d https://t.co/jnd5t1LiAH”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@DAVFX_0 shared a real-time VFX demo called 'Anomaly' built with Illugen, a Unity-compatible VFX authoring tool, showing stylized particle and volumetric effects in-engine.</dd>
      <dt>Why interesting</dt>
      <dd>Illugen produces high-quality real-time VFX inside Unity — directly applicable to the studio's game and XR projects that need polished in-engine effects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team should look up Illugen on the Asset Store or its site and run a quick test on any active project that currently uses particle systems.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DAVFX_0/status/2060306891687809144" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@godotengine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 209 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/godotengine/status/2060503643057496501">View @godotengine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for a Release Candidate in the near future https://t.co/af9vUd2qLQ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Godot Engine 4.7 beta 4 is released by the Godot Foundation, with an official Release Candidate expected as the next milestone.</dd>
      <dt>Why interesting</dt>
      <dd>For a Unity-primary studio, tracking Godot 4.7 stable gives a concrete reference point if any project needs a lighter or royalty-free engine.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Assign one dev to run the Godot 4.7 beta 4 build on a small internal prototype before RC drops to gauge 2D/3D workflow fit.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/godotengine/status/2060503643057496501" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 198 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@sean_gause publicly released the shader graph node setup for a rain drip effect built in Unity HDRP, with notes on porting it to Unreal — the key difference being HDRP's packed mask map (metal, AO, detail, smoothness channels).</dd>
      <dt>Why interesting</dt>
      <dd>A ready-made shader graph reference for rain/wet-surface effects that works in both Unity HDRP and Unreal Engine — saves hours of R&amp;D for any environment art task.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can pull this node setup directly into HDRP projects that need wet-surface or weather-pass shaders.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 174 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2060396306934436123">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Free learning content for the 5th month of the year? Yeah, we May just have some here for you... Explore how to create cinematic environments in UE5, set up translucent glass in Substrate, and more. I”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Unreal Engine published free May learning content covering cinematic environment creation in UE5 and translucent glass setup using Substrate materials.</dd>
      <dt>Why interesting</dt>
      <dd>Substrate glass and cinematic lighting are directly applicable to the studio's XR/VR and architectural visualization work in UE5.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Route the Substrate glass tutorial to any team member currently working on UE5 scenes that require realistic material rendering.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2060396306934436123" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@itchio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 161 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/itchio/status/2060511506815746558">View @itchio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playable Solo or GM-Less https://t.co/vGYtVXXzUe by @CrossedPathsRPG https://t.co/avSktXRORC”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>itch.io is spotlighting 'Ashes', a tabletop Souls-like RPG by CrossedPathsRPG designed for solo or GM-less play, inspired by OSR design principles.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/itchio/status/2060511506815746558" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
