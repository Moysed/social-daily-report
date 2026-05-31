---
type: social-topic-report
date: '2026-05-31'
topic: game-dev
lang: en
pair: game-dev.th.md
generated_at: '2026-05-31T15:59:03+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 18
salience: 0.45
sentiment: neutral
confidence: 0.6
tags:
- gamedev
- unity
- unreal
- godot
- ai-tooling
- 3d-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060606108763295745/img/-oeMxhDSxmtuOXkf.jpg
---

# Game Dev — 2026-05-31

## TL;DR
- Microsoft released Trellis.2, a 4B open-source model that turns an image into a textured GLB 3D asset in ~3 seconds (mesh under 100ms on CUDA), output ready for Blender, Unity, and Unreal [4].
- Godot 4.7 beta 4 shipped, with a Release Candidate stated to be near [5].
- Unity AI exposes three modes — Ask, Plan, and Agent — for Q&A, planned task sequences with safeguards, and automation of repetitive tasks [14].
- An open-source Unity character controller handling moving platforms and wall collisions was released [1]; a rain-drip shader node setup (Unity HDRP, portable to Unreal) was shared publicly [3].
- John Carmack noted Gmail's AI writing suggestions are hard to argue against as improvements but flatten individual authorial voice [2] — a recurring concern for AI-assisted content.

## What happened
Two concrete engine/tooling updates landed: Godot 4.7 reached beta 4 with an RC said to be near [5], and Unity detailed its AI assistant's three modes (Ask, Plan, Agent) for answering questions, building safeguarded task plans, and automating repetitive work [14]. On the asset-generation side, Microsoft released Trellis.2, an open-source 4B model converting any image to a textured GLB in roughly 3 seconds (textured mesh under 100ms on CUDA), with output usable in Blender, Unity, and Unreal [4]. Community/tooling contributions included an open-source Unity character controller for edge cases like moving platforms and wall collisions [1] and a publicly shared rain-drip shader node graph (Unity HDRP, noted as portable to Unreal) [3]. Unreal published free May learning content covering cinematic UE5 environments and translucent glass in Substrate [6]. The remainder are indie showcase and itch.io/Godot release posts [7–13, 15–18], plus Carmack's note that Gmail's AI edits improve writing while erasing personal voice [2].

## Why it matters (reasoning)
Image-to-3D generation at the speed and price Trellis.2 claims [4] shifts where asset cost sits: rapid prototyping, greyboxing, and background props become cheaper, while topology, UVs, and optimization for real-time still need human cleanup — generated meshes rarely ship as-is. Being open source and GLB-native means it slots into existing Unity/Unreal/Blender pipelines without vendor lock-in [4]. Unity's Agent mode [14] points to the same automation trend inside the editor, but 'automate repetitive tasks' is vague and unproven; the value depends on reliability and how much oversight each action requires. Carmack's observation [2] generalizes beyond email: AI assistance tends toward a homogenized output, relevant to any team using AI for narrative, marketing copy, or code style. Godot 4.7 nearing RC [5] continues its steady cadence as a no-license-cost option. The bulk of today's signal is routine community showcase, not structural change.

## Possibility
Likely: image-to-3D tools like Trellis.2 become a standard early-pipeline step for blockouts and non-hero assets, given open source + GLB output + sub-second mesh generation [4]. Plausible: Unity's Agent mode and similar in-editor AI see cautious adoption gated by trust and the need for human review [14], mirroring the voice/quality tradeoff Carmack flags [2]. Plausible: Godot 4.7 stable follows soon after the RC referenced in [5]. Unlikely on this evidence: generated 3D assets replacing hand-authored hero assets in production this cycle — nothing in [4] addresses topology, rigging, or LOD quality. No source provides numeric adoption or quality figures.

## Org applicability — NDF DEV
Test Trellis.2 on a real NDF asset task — generate props for a Unity scene and measure cleanup time vs. modeling from scratch (effort: low; it's open source and GLB-native) [4]. If output quality holds, fold it into early prototyping for Unity/XR projects (effort: med) [4]. Trial Unity AI's Ask/Plan modes on an active project to gauge accuracy before allowing Agent mode to touch repetitive editor work (effort: low) [14]. Bookmark the free UE5 cinematic-environment and Substrate glass tutorials for any Unreal/XR visual work (effort: low) [6]. Evaluate the open-source character controller [1] and rain-drip shader setup [3] as references rather than drop-in code (effort: low). For AI-assisted writing in docs, marketing, or narrative, keep a human voice pass — treat Carmack's flattening point as a process note [2]. Skip: the indie showcase and itch.io/Godot featured-game posts [7–13, 15–18] — no actionable signal.

## Signals to Watch
- Watch Trellis.2 real-world mesh quality and topology — whether generated assets need heavy cleanup or ship near-usable [4].
- Watch Unity AI Agent mode reliability and what oversight it requires before trusting automation [14].
- Watch for Godot 4.7 Release Candidate, then stable [5].
- Watch the AI 'voice flattening' issue as it extends from writing to code and narrative content [2].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | jettelly | ^1375 c7 | [Developer thesquirrelyjones released an open-source custom character controller ](https://x.com/jettelly/status/2060617205989965911) |
| x | ID_AA_Carmack | ^1289 c142 | [I have difficulty arguing that most of the writing changes suggested in gmail no](https://x.com/ID_AA_Carmack/status/2060399696955195843) |
| x | sean_gause | ^685 c4 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | RoundtableSpace | ^351 c23 | [Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D ](https://x.com/RoundtableSpace/status/2060477532537827633) |
| x | godotengine | ^223 c9 | [One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for ](https://x.com/godotengine/status/2060503643057496501) |
| x | UnrealEngine | ^190 c8 | [Free learning content for the 5th month of the year? Yeah, we May just have some](https://x.com/UnrealEngine/status/2060396306934436123) |
| x | itchio | ^170 c1 | [Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playa](https://x.com/itchio/status/2060511506815746558) |
| x | UnrealEngine | ^101 c27 | [We know that #ScreenshotSaturday is always out of this world So, show us what in](https://x.com/UnrealEngine/status/2060723065991131533) |
| x | MortalCrux | ^77 c5 | [A mind-blowing magic finisher 🧙‍♀️ #indiegamedev #indiegame #unity3d #pcgamer #m](https://x.com/MortalCrux/status/2060702882001731819) |
| x | Plasmeo | ^69 c2 | [Who needs cover when you have shielder drones ? #indiedev #gamedev #FPS #Unity #](https://x.com/Plasmeo/status/2060742236816445564) |
| x | itchio | ^61 c0 | [Trigwa: Statue pushing game with a narrative. Each puzzle tells part of a larger](https://x.com/itchio/status/2060405812057780236) |
| x | R2RGames | ^57 c0 | [Almost 300 followers! Here is more progress on my medieval builder, spline walls](https://x.com/R2RGames/status/2060462094802379049) |
| x | mazestalker | ^45 c1 | [I love going back to my pre-URP areas and updating them with 2 years of experien](https://x.com/mazestalker/status/2060495924523135169) |
| x | unitygames | ^42 c3 | [Meet Unity AI’s three modes: Ask, Plan, and Agent. 1️⃣ Ask: Get your questions a](https://x.com/unitygames/status/2060435608732836007) |
| x | OzgursAssets | ^35 c2 | [Modular alternative headlight design #keitruck #gamedev #indiedev #ue5 #Unity3d ](https://x.com/OzgursAssets/status/2060799257293000895) |
| x | DAVFX_0 | ^33 c2 | [Electric stuff in Illugen #vfx #realtimevfx #illugen #unity3d #gamedev https://t](https://x.com/DAVFX_0/status/2060866245482709002) |
| x | itchio | ^28 c0 | [Dungeons of Freeport: An Extraction Roguelike Dungeon-Crawler https://t.co/2L6EX](https://x.com/itchio/status/2060451112503722298) |
| x | godotengine | ^17 c0 | [Featured game: Elfie: A Sand Plan https://t.co/JAOBcSXMGt](https://x.com/godotengine/status/2060503644617740388) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1375 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2060617205989965911">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer thesquirrelyjones released an open-source custom character controller for Unity, designed to handle edge cases like moving platforms and wall collisions. 🎮 See more: https://t.co/fpq8pSxsLi ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer thesquirrelyjones released a free, open-source Unity character controller that specifically handles edge cases like moving platforms and wall collisions.</dd>
      <dt>Why interesting</dt>
      <dd>A ready-made controller with tricky physics edge cases solved saves the Unity team significant debugging time on any platformer or 3D action project.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team should review the repo and benchmark it against the current character controller setup before starting any new platformer or movement-heavy project.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2060617205989965911" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1289 · 💬 142</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2060399696955195843">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I have difficulty arguing that most of the writing changes suggested in gmail now aren’t improvements, but it does tend to wipe out my particular authorial voice.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>John Carmack observes that Gmail's AI writing suggestions are objectively better prose, but consistently strip out his personal authorial voice.</dd>
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
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 685 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@sean_gause shared the full node graph for a rain drip shader built in Unity HDRP, explaining how the mask map packs metallic, AO, detail, and smoothness channels, with notes on porting it to Unreal.</dd>
      <dt>Why interesting</dt>
      <dd>A documented HDRP rain drip shader node setup is a direct reference for any Unity project that needs wet-surface or weather visuals without building from scratch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can import this node graph into any HDRP project requiring wet-surface effects, and use the Unreal port notes if the project targets that engine.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RoundtableSpace</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 351 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RoundtableSpace/status/2060477532537827633">View @RoundtableSpace on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft just dropped Trellis.2 — a 4B model that converts any image into a 3D asset in 3 seconds. Textured mesh under 100ms on CUDA, outputs a GLB file ready for Blender, Unity, and Unreal. Open sou”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Microsoft released Trellis.2, an open-source 4B image-to-3D model that generates a textured GLB mesh in under 3 seconds on CUDA, compatible with Blender, Unity, and Unreal Engine.</dd>
      <dt>Why interesting</dt>
      <dd>A free, self-hostable image-to-3D pipeline cuts 3D asset prototyping from hours to seconds — directly relevant to Unity game and XR projects that need rapid asset iteration.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can run Trellis.2 locally to convert concept art or photo references into draft GLB assets for scene blocking before committing to full 3D modeling.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RoundtableSpace/status/2060477532537827633" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@godotengine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 223 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/godotengine/status/2060503643057496501">View @godotengine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One more for the road! 🚙 #GodotEngine 4.7 beta 4 arrives, setting the stage for a Release Candidate in the near future https://t.co/af9vUd2qLQ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Godot Engine 4.7 beta 4 is released by the Godot Foundation, with a Release Candidate expected next.</dd>
      <dt>Why interesting</dt>
      <dd>4.7 RC approaching means new rendering, GDScript, and editor features are nearly production-stable for teams tracking open-source Unity alternatives.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can run Godot 4.7 beta 4 on a small prototype or e-learning minigame to evaluate it before the stable release.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/godotengine/status/2060503643057496501" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 190 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2060396306934436123">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Free learning content for the 5th month of the year? Yeah, we May just have some here for you... Explore how to create cinematic environments in UE5, set up translucent glass in Substrate, and more. I”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Unreal Engine released free May learning content covering cinematic environment creation in UE5 and translucent glass setup using the Substrate material system.</dd>
      <dt>Why interesting</dt>
      <dd>Substrate glass and cinematic lighting techniques transfer directly to XR/VR environment work, even for teams not shipping on UE5 full-time.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Assign one XR/VR team member to run through the Substrate glass tutorial and document whether the approach maps to Unity's equivalent material workflow.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2060396306934436123" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@itchio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 170 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/itchio/status/2060511506815746558">View @itchio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ashes - A Souls-Like GM-Less RPG: A Souls-Like RPG inspired by OSR titles, playable Solo or GM-Less https://t.co/vGYtVXXzUe by @CrossedPathsRPG https://t.co/avSktXRORC”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>itch.io is promoting Ashes, a solo/GM-less tabletop RPG on its platform that draws on Souls-like mechanics and OSR design, published by CrossedPathsRPG.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/itchio/status/2060511506815746558" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 101 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2060723065991131533">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We know that #ScreenshotSaturday is always out of this world So, show us what in the universe of possibilities you're developing, perfecting or concepting! 📷: @karabardin https://t.co/tiV6Ao2Aq0”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Unreal Engine posted a routine #ScreenshotSaturday community call asking developers to share work-in-progress screenshots.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2060723065991131533" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
