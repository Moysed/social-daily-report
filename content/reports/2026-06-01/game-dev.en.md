---
type: social-topic-report
date: '2026-06-01'
topic: game-dev
lang: en
pair: game-dev.th.md
generated_at: '2026-06-01T03:57:10+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 13
salience: 0.25
sentiment: neutral
confidence: 0.6
tags:
- unity
- shaders
- open-source
- indiedev
- tooling
- vfx
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060606108763295745/img/-oeMxhDSxmtuOXkf.jpg
---

# Game Dev — 2026-06-01

## TL;DR
- Developer thesquirrelyjones released an open-source Unity character controller handling moving platforms and wall collisions [1].
- Two reusable shader breakdowns shared openly: a rain-drip node setup (Unity HDRP, said to port to Unreal) [2] and a stylized liquid shader using Shader Graph vertex-painted flow maps [9].
- Unity-retention sentiment persists: one creator published a 'why I won't quit Unity' piece despite ongoing pressure to leave [12].
- The rest of the day is #ScreenshotSaturday indie showcase (VFX, low-poly assets, horror/FPS/RPG demos) with no engine, tooling, or pipeline news [3][4][5][6][8][10][11][13].

## What happened
The day's Game Dev signal is dominated by community asset and technique sharing rather than vendor or release news. The highest-engagement item is an open-source custom Unity character controller built to handle edge cases like moving platforms and wall collisions [1]. Two shader breakdowns were published: a rain-drip effect node graph in Unity HDRP, with the author noting it ports to Unreal aside from HDRP's mask map difference [2], and a stylized liquid shader using Shader Graph with vertex-painted flow maps to direct movement across surfaces [9]. A creator also posted a 'why I won't quit Unity' video amid continued calls to leave the engine [12].

## Why it matters (reasoning)
The open controller [1] and the two shader walkthroughs [2][9] are directly reusable in Unity production — exactly the URP/HDRP and Shader Graph stack NDF DEV uses — and item [2]'s note on Unreal portability lowers the cost of moving an effect between engines. The persistence of Unity-exit discourse [12] is a weak but recurring sentiment signal: engine-choice anxiety remains an active topic, which matters for studios standardizing on Unity. Beyond these, the volume of #ScreenshotSaturday posts [3][4][5][6][8][10][11][13] is engagement-driven self-promotion, not substantive movement in engines, tooling, or AI pipelines.

## Possibility
Likely: more individual open-source controllers and shader breakdowns keep appearing, since this is the steady-state of indie Unity community output [1][2][9]. Plausible: Unity-vs-alternatives debate continues episodically without a clear trigger today [12]. Unlikely: any of these single posts signals a broader engine or tooling shift — there is no vendor announcement, release, or AI-pipeline item in the set to support that.

## Org applicability — NDF DEV
Evaluate the open-source character controller [1] for prototype or jam projects to avoid re-solving moving-platform and wall-collision cases — low effort, check the license before use. Save the rain-drip [2] and liquid [9] shader breakdowns into the team's Shader Graph/HDRP reference library; both are low effort to replicate and relevant to current Unity work. Skip the #ScreenshotSaturday showcase items [3][4][5][6][8][10][11][13] and the Unity-retention opinion video [12] — no actionable engineering content.

## Signals to Watch
- Open-source Unity controllers solving common edge cases — reuse candidates [1].
- Cross-engine shader portability notes (HDRP→Unreal) as a workflow pattern [2].
- Recurring Unity-exit sentiment among creators [12].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | jettelly | ^1923 c12 | [Developer thesquirrelyjones released an open-source custom character controller ](https://x.com/jettelly/status/2060617205989965911) |
| x | sean_gause | ^841 c5 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | UnrealEngine | ^105 c28 | [We know that #ScreenshotSaturday is always out of this world So, show us what in](https://x.com/UnrealEngine/status/2060723065991131533) |
| x | MortalCrux | ^79 c5 | [A mind-blowing magic finisher 🧙‍♀️ #indiegamedev #indiegame #unity3d #pcgamer #m](https://x.com/MortalCrux/status/2060702882001731819) |
| x | Plasmeo | ^76 c2 | [Who needs cover when you have shielder drones ? #indiedev #gamedev #FPS #Unity #](https://x.com/Plasmeo/status/2060742236816445564) |
| x | DAVFX_0 | ^74 c0 | [Illugen smoky particles #vfx #realtimevfx #illugen #gamedev #unity3d https://t.c](https://x.com/DAVFX_0/status/2061041102682005755) |
| x | jonahh5830 | ^51 c1 | [The E-10: the lightest design in the E-series, this tiny tank destroyer was inte](https://x.com/jonahh5830/status/2061004991528153259) |
| x | IndiepathCS | ^43 c0 | [Simple atmospheric, lighting, and sounds testing for a Backrooms project. #Backr](https://x.com/IndiepathCS/status/2061028068601245900) |
| x | jettelly | ^41 c0 | [DNArt showed off this stylized liquid shader made with Shader Graph, using verte](https://x.com/jettelly/status/2061040002717671602) |
| x | DAVFX_0 | ^38 c2 | [Electric stuff in Illugen #vfx #realtimevfx #illugen #unity3d #gamedev https://t](https://x.com/DAVFX_0/status/2060866245482709002) |
| x | OzgursAssets | ^38 c2 | [Modular alternative headlight design #keitruck #gamedev #indiedev #ue5 #Unity3d ](https://x.com/OzgursAssets/status/2060799257293000895) |
| x | dailabs | ^34 c1 | [Everyone Says Quit The Unity Game Engine. Here's Why I Won't... #indiegame #game](https://x.com/dailabs/status/2061057835861967064) |
| x | RisingFoxGame | ^31 c1 | [Fight to survive or die trying! There are only a few gauntlets, but all of them ](https://x.com/RisingFoxGame/status/2060823938083536983) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1923 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2060617205989965911">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer thesquirrelyjones released an open-source custom character controller for Unity, designed to handle edge cases like moving platforms and wall collisions. 🎮 See more: https://t.co/fpq8pSxsLi ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer thesquirrelyjones released an open-source Unity character controller that handles edge cases including moving platforms and wall collision detection.</dd>
      <dt>Why interesting</dt>
      <dd>A ready-made character controller that already handles the fiddly physics edge cases saves the Unity team significant prototyping time on any platformer or 3D game project.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team should review the repo and evaluate whether it replaces or supplements the current character movement implementation in active projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2060617205989965911" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 841 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer @sean_gause shared the full shader node graph for a rain drip effect built in Unity HDRP, noting the mask map packs metal, AO, detail, and smoothness into one texture, and the setup ports to Unreal with only that channel difference.</dd>
      <dt>Why interesting</dt>
      <dd>A free, ready-to-read node graph for wet-surface rain drips in HDRP cuts R&amp;D time on a common environmental detail in realistic Unity projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can pull this node graph into any HDRP scene as a starting point for wet-surface materials and adjust the mask map channels to match existing texture sets.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 105 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2060723065991131533">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We know that #ScreenshotSaturday is always out of this world So, show us what in the universe of possibilities you're developing, perfecting or concepting! 📷: @karabardin https://t.co/tiV6Ao2Aq0”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Unreal Engine's weekly #ScreenshotSaturday call-to-action post invites developers to share in-progress game screenshots.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2060723065991131533" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MortalCrux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 79 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MortalCrux/status/2060702882001731819">View @MortalCrux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A mind-blowing magic finisher 🧙‍♀️ #indiegamedev #indiegame #unity3d #pcgamer #madewithunity #gamedev #gaming #Steam #fantasy #RPG #ScreenshotSaturday https://t.co/2KHz2qs4qC”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Indie dev @MortalCrux posted a ScreenshotSaturday clip of a magic finisher VFX in their Unity RPG — no technique or breakdown included.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MortalCrux/status/2060702882001731819" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Plasmeo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 76 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Plasmeo/status/2060742236816445564">View @Plasmeo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Who needs cover when you have shielder drones ? #indiedev #gamedev #FPS #Unity #lowpoly #retroFPS #madewithunity #screenshotsaturday #boomershooter https://t.co/mXBrIH5SgB”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Indie dev @Plasmeo posted a #ScreenshotSaturday clip of shielder drones in their low-poly retro FPS built with Unity — no technique or code shared, just a mechanic showcase.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Plasmeo/status/2060742236816445564" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DAVFX_0</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 74 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DAVFX_0/status/2061041102682005755">View @DAVFX_0 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Illugen smoky particles #vfx #realtimevfx #illugen #gamedev #unity3d https://t.co/gaV7mraaU1”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@DAVFX_0 showcases Illugen's real-time smoky particle system running inside Unity3D, demonstrating volumetric-style smoke at interactive frame rates.</dd>
      <dt>Why interesting</dt>
      <dd>Illugen provides production-ready high-quality particle VFX for Unity, cutting custom shader and simulation time for the Unity team.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can trial Illugen as a VFX asset in the current project pipeline to assess quality and performance cost before committing.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DAVFX_0/status/2061041102682005755" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jonahh5830</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 51 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jonahh5830/status/2061004991528153259">View @jonahh5830 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The E-10: the lightest design in the E-series, this tiny tank destroyer was intended to replace the Jagdpanzer 38(t). It carried a 7.5 cm L/48 gun, and its suspension system allowed the hull to be low”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Unity Asset Store creator is showcasing an E-10 tank destroyer 3D model with historically accurate specs: 7.5 cm L/48 gun and variable suspension lowering the hull from 176 to 140 cm.</dd>
      <dt>Why interesting</dt>
      <dd>Niche historical military vehicle assets like this are useful reference points for studios prototyping WW2 or tactical game levels in Unity.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the Unity team is building a military or historical scene, check this asset on the Unity Asset Store before commissioning custom models.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jonahh5830/status/2061004991528153259" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IndiepathCS</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 43 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IndiepathCS/status/2061028068601245900">View @IndiepathCS on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Simple atmospheric, lighting, and sounds testing for a Backrooms project. #Backrooms #HorrorGames #Unity3D #gamedev #indiedev https://t.co/Ely0F3660a”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Indie dev @IndiepathCS is testing atmospheric lighting and ambient sound in Unity for a Backrooms-style horror game, sharing early footage on X.</dd>
      <dt>Why interesting</dt>
      <dd>Backrooms atmosphere depends on subtle lighting gradients and looping ambient audio — both are Unity techniques the studio's game team works with directly.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can watch the footage as a reference point for lighting mood and sound layering in any atmospheric or horror scene they're building.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IndiepathCS/status/2061028068601245900" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
