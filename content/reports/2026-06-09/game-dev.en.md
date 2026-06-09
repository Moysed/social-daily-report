---
type: social-topic-report
date: '2026-06-09'
topic: game-dev
lang: en
pair: game-dev.th.md
generated_at: '2026-06-09T03:12:43+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 155
salience: 0.55
sentiment: mixed
confidence: 0.6
tags:
- game-dev
- godot
- unreal-engine-5
- unity
- xbox
- ai-asset-generation
thumbnail: https://pbs.twimg.com/media/HKTU_iEXIAA3eG1.jpg
---

# Game Dev — 2026-06-09

## TL;DR
- Godot 4.7 hit Release Candidate with HDR output, an official Godot Asset Store, and drawable textures [17]; separately Microsoft published 'Building Xbox Games with Godot' shipping GDExtensions for GDK, PlayFab, and GameInput [32].
- Unreal Engine 5 carries both showcase momentum — Gears of War: E-Day praised for visuals/fidelity [4][12][53], Mortal Shell 2 on UE5 [27] — and a visible backlash thread on art-direction sameness, 'slop' framing, and poor optimization tied to UE5/DLSS reliance [5][6][39][43].
- TT Games' next title is reported to be a major Warner Bros. IP (speculated DC) on UE5 [1] — a rumor, not an announcement.
- Free/low-cost Unity tooling surfaced: AERO 1.4 volumetric fog for URP is free on the Asset Store [22], plus shader/editor-tool bundles [25][46].
- AI image generation (GPT Image 2) is being used for marketing/editorial-style visuals in gamedev-adjacent posts [37][60].

## What happened
Engine news split three ways. Godot reached a production-ready 4.7 RC with HDR output, an official Asset Store, and drawable textures [17], and Microsoft released guidance and GDExtensions (GDK, PlayFab, GameInput) for building Xbox-on-PC games with Godot [32]. Unreal Engine 5 dominated by volume: Gears of War: E-Day drew strong visual praise ahead of an Unreal Fest Chicago session from The Coalition [4][12][53], Mortal Shell 2 was highlighted as a UE5 step-up [27], and TT Games' next title is rumored to be a Warner Bros. IP on UE5 [1]. Counter to that, a recurring critical thread argued UE5 produces uniform art direction and worse optimization, partly blaming DLSS dependence [5][6][39][43][48]. Carmack publicly praised Fabrice Bellard [2].

## Why it matters (reasoning)
Godot's signal is the most consequential for a multi-stack studio. An official Asset Store [17] plus Microsoft-backed Xbox export tooling [32] lowers two long-standing barriers — asset distribution and console reach — that historically pushed teams toward Unity or Unreal. That doesn't displace Unity, but it makes Godot a more defensible option for smaller 2D/3D and edutech titles. The UE5 backlash [5][6][39][43] is mostly discourse, not data, but the optimization complaint is a real second-order effect: heavy reliance on upscalers (DLSS) and default Lumen/Nanite settings correlates with shipped performance problems, which matters for XR/VR and mobile targets where frame budgets are tight. The Unity tooling items [22][25][46] and AI image use [37][60] reflect a steady commoditization of mid-tier production assets — useful for cost, neutral for differentiation.

## Possibility
Likely: Godot's console-reach story keeps improving, since Microsoft is actively publishing tooling [32] alongside the 4.7 maturity step [17]; expect more third-party GDExtensions. Plausible: the TT Games/Warner Bros UE5 title is real but the 'DC' specifics stay unconfirmed until an official reveal [1]. Unlikely: UE5 adoption meaningfully slows due to the 'slop'/optimization criticism [5][6][39] — committed AAA pipelines like Gears E-Day [4][53] and Mortal Shell 2 [27] show the install base is sticky. Plausible: AI image tools like GPT Image 2 [37][60] expand into concept/marketing workflows faster than into shippable in-game assets, where consistency and licensing remain blockers.

## Org applicability — NDF DEV
1) Track Godot 4.7 RC and the Microsoft Xbox/Godot tooling for non-Unity prototypes and edutech titles where console export or a lighter engine helps — low effort to evaluate [17][32]. 2) Grab AERO 1.4 free URP volumetric fog now for current Unity/XR work — low effort, immediate value [22]. 3) Treat the UE5 optimization criticism as a checklist input, not a verdict: if any project uses UE5, budget for upscaler-independent performance and review Lumen/Nanite defaults — med effort [39][43]. 4) Pilot GPT Image 2 for marketing/store-page and concept art (not in-game assets) — low effort [37][60]. Skip: the Gears/UE5 culture discourse [4][12][14], indie showcase posts with no reusable technique [8][9][16][21][33][36][42], and the TT Games rumor as a planning input until confirmed [1].

## Signals to Watch
- Godot 4.7 final release and adoption of the official Asset Store — gauges whether Godot's tooling gap to Unity is closing [17].
- Microsoft's continued Godot/Xbox GDExtension support — a proxy for Godot's console viability [32].
- Official TT Games / Warner Bros announcement to confirm or kill the UE5 DC rumor [1].
- Whether UE5 optimization criticism shifts from discourse to measurable shipped-performance patterns [39][43].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | LEGOTtNewsI | ^6419 c236 | [TT Games’ Next Title will be based on a Major Warner Bros. IP on Unreal Engine 5](https://x.com/LEGOTtNewsI/status/2064008728047727003) |
| x | ID_AA_Carmack | ^3639 c69 | [I admire Fabrice Bellard. He is almost certainly a better overall programmer tha](https://x.com/ID_AA_Carmack/status/2064095424420487226) |
| x | MortalCrux | ^2313 c83 | [I might not have a new trailer for any gaming showcases today, but here are a fe](https://x.com/MortalCrux/status/2063710959793750424) |
| x | Grummz | ^969 c146 | [Gears of War E-Day was the best of the show. - A return to masculinity and broth](https://x.com/Grummz/status/2063846556806328380) |
| x | LookAtMyMeat1 | ^944 c4 | [The Unreal engine has been a disaster for art direction in gaming](https://x.com/LookAtMyMeat1/status/2064026736732393492) |
| x | NomadicAllo | ^921 c23 | ["UE5 looks like slop" Nuh uh https://t.co/awY78D0H1a](https://x.com/NomadicAllo/status/2063834614339178757) |
| x | LucasLiu_XY | ^765 c9 | [Finally got my character running in-game using UE5's GASP project! The feeling o](https://x.com/LucasLiu_XY/status/2063821404978712691) |
| x | ABGameDeveloper | ^499 c6 | [The Fox caught you and he wants to num num... 🦊🔪 (It's an old model 🤭) #furry #h](https://x.com/ABGameDeveloper/status/2063808353575534745) |
| x | zzeljkokos | ^467 c33 | [Surprise! 😊 After years spent building cities, it's time to return to the stars.](https://x.com/zzeljkokos/status/2064053479748903312) |
| x | Look_behindyou | ^458 c5 | [🚨 Only 70 hours left! The final countdown for Soverain has begun! If you've been](https://x.com/Look_behindyou/status/2063996243450233026) |
| x | ShatterPointGS | ^419 c6 | [A little bit of testing with one of Sylphie's mechanics. #indiegame #indiedev #f](https://x.com/ShatterPointGS/status/2064059889064853554) |
| x | JamieMoranUK | ^405 c20 | [I’ve played 1000s of Video Games , since I was old enough to pick up a Controlle](https://x.com/JamieMoranUK/status/2063835937931452727) |
| x | SharkyLeo_YT | ^384 c4 | [this is slander not seen since the fucking unreal engine Mario video](https://x.com/SharkyLeo_YT/status/2064109001281847521) |
| x | VladTheInflator | ^379 c15 | [If I wanted to destroy a country, I would: 1. Change their founding history to p](https://x.com/VladTheInflator/status/2063666428444868795) |
| x | rafaelborven | ^362 c4 | [Animation done for @TributeGames's game @MARVELCosmicInv #Pixelart #animation #i](https://x.com/rafaelborven/status/2063995185491493316) |
| x | Talegamesnews | ^301 c3 | [Eyes glowed. Chains clanked. Ghosts howled. She said “Cute” 👻⚔️😏 #metroidvania #](https://x.com/Talegamesnews/status/2063940098828169255) |
| x | godotengine | ^299 c10 | [#GodotEngine 4.7 has at last arrived at the Release Candidate stage! HDR output ](https://x.com/godotengine/status/2064079841985470893) |
| x | Hoodie_monk | ^261 c15 | [Version 1.0 Community: We need to talk. #HoodieMonk #GameDev #IndieDev #Gaming #](https://x.com/Hoodie_monk/status/2063946101401481265) |
| x | OzgursAssets | ^258 c6 | [FREE 🎁 Sharing these two cars I modeled almost 20 years ago for free. You can gr](https://x.com/OzgursAssets/status/2063900380547649761) |
| x | smokingcatsdev | ^257 c8 | [Day 15 of posting about my game, until a release a Steam Demo I've been wanting ](https://x.com/smokingcatsdev/status/2064107001949676030) |
| x | drattzy | ^237 c3 | [Alterium Shift is a retro-inspired JRPG where three heroes set out to prevent a ](https://x.com/drattzy/status/2063999695375016326) |
| x | TheMirzaBeig | ^198 c4 | [Just released! ✅ Dense, self-shadowing, volumetric fog. Need lit, volumetric fog](https://x.com/TheMirzaBeig/status/2063938424109715502) |
| x | OzgursAssets | ^197 c4 | [Kei Truck - WIP 9 Modeling is done, now it's UV time! #keitruck #gamedev #indied](https://x.com/OzgursAssets/status/2063583946303000701) |
| x | blargisdev | ^197 c5 | [Implemented this swingy lantern that projects cool shadows #gamedev #indiedev ht](https://x.com/blargisdev/status/2064088764641947758) |
| x | ushadersbible | ^182 c0 | [The Unity Dev Bundle ➡️ https://t.co/1eA8907m5M #gamedev https://t.co/aEAZAQ6jVV](https://x.com/ushadersbible/status/2063481988208533947) |
| x | unity3dvfx | ^182 c2 | [Really cool to see indie FPS devs sharing progress like this 🙌 The responsivenes](https://x.com/unity3dvfx/status/2063878484905058742) |
| x | BMKing23 | ^181 c8 | [I'm genuinely surprised by #MortalShell2. It's a massive leap over the original ](https://x.com/BMKing23/status/2064053901796479115) |
| x | HedProtag | ^176 c6 | [Working on a cool new feature for my game. Can you guess what it is? #indiegame ](https://x.com/HedProtag/status/2064159133826191719) |
| x | GinoKolling | ^174 c0 | [Unreal Engine Creatures https://t.co/3AkERddbH6](https://x.com/GinoKolling/status/2063918745295393199) |
| x | GameZoneHQ | ^165 c0 | [Procedurally generated impact frame with shader and particle system by @namutree](https://x.com/GameZoneHQ/status/2063878287865028798) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LEGOTtNewsI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6419 · 💬 236</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LEGOTtNewsI/status/2064008728047727003">View @LEGOTtNewsI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“TT Games’ Next Title will be based on a Major Warner Bros. IP on Unreal Engine 5 We believe it will be DC https://t.co/0eLnlz5nY5”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>TT Games (LEGO game developer) is reportedly building its next title on Unreal Engine 5, based on a major Warner Bros. IP — likely DC Comics.</dd>
      <dt>Why interesting</dt>
      <dd>TT Games shifting from LEGO's custom engine to UE5 signals that mid-tier licensed-IP studios are standardizing on UE5 for next-gen production.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio targets UE5 for any licensed or XR title, this confirms UE5 is the safer long-term bet over Unity for that scope.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LEGOTtNewsI/status/2064008728047727003" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3639 · 💬 69</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2064095424420487226">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I admire Fabrice Bellard. He is almost certainly a better overall programmer than I am.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>John Carmack publicly states that Fabrice Bellard (creator of QEMU, FFmpeg, TinyCC) is likely a stronger overall programmer than himself.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ID_AA_Carmack/status/2064095424420487226" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MortalCrux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2313 · 💬 83</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MortalCrux/status/2063710959793750424">View @MortalCrux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I might not have a new trailer for any gaming showcases today, but here are a few updates to how menus work. 😂 1) Character physics are now simulated and respond to mouse input while previewing your g”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An indie Unity RPG dev enabled ragdoll/character physics and real-time torch lighting inside menu screens — features previously reserved for gameplay scenes only.</dd>
      <dt>Why interesting</dt>
      <dd>Activating physics and real-time lighting in menus adds perceived polish with minimal extra work, since the systems already exist in the Unity project.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can reuse existing physics and lighting setups in character preview or gear screens instead of baking static renders for menus.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MortalCrux/status/2063710959793750424" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Grummz</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 969 · 💬 146</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Grummz/status/2063846556806328380">View @Grummz on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gears of War E-Day was the best of the show. - A return to masculinity and brotherhood themes - Unreal Engine 5 and looks great - Interview said the were focused on the vibes of the original game, ins”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Gears of War E-Day (UE5) revealed a micro cover-destruction system, fully rebuilt movement/cover mechanics with jump, a new gore system, and an entire city built as a game environment.</dd>
      <dt>Why interesting</dt>
      <dd>The micro-destruction and fluid cover/movement systems are concrete design references for any third-person or combat game — shows how AAA teams scope environmental interactivity.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When the Unity team designs combat or cover mechanics, use E-Day's destruction and movement approach as a benchmark for scoping interaction depth vs. performance cost.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Grummz/status/2063846556806328380" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LookAtMyMeat1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 944 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LookAtMyMeat1/status/2064026736732393492">View @LookAtMyMeat1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Unreal engine has been a disaster for art direction in gaming”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An anonymous X user claims Unreal Engine has negatively impacted art direction across the games industry — no evidence, examples, or context provided.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LookAtMyMeat1/status/2064026736732393492" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NomadicAllo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 921 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NomadicAllo/status/2063834614339178757">View @NomadicAllo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&quot;UE5 looks like slop&quot; Nuh uh https://t.co/awY78D0H1a”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>User @NomadicAllo posts a media link to counter the claim that UE5 visuals look generic, with no context on the project, technique, or settings used.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NomadicAllo/status/2063834614339178757" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LucasLiu_XY</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 765 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LucasLiu_XY/status/2063821404978712691">View @LucasLiu_XY on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Finally got my character running in-game using UE5's GASP project! The feeling of seeing your own design move is indescribable.Who understands this feeling? 🎉 https://t.co/01R5YL6d2U”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer shared their first successful character animation in-game using UE5's GASP (Game Animation Sample Project), celebrating the milestone on X.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LucasLiu_XY/status/2063821404978712691" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ABGameDeveloper</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 499 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ABGameDeveloper/status/2063808353575534745">View @ABGameDeveloper on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Fox caught you and he wants to num num... 🦊🔪 (It's an old model 🤭) #furry #horrorgame #indiedev #gamedev https://t.co/fhuN56oP95”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Indie dev @ABGameDeveloper shared a WIP horror game clip featuring a fox antagonist character, noting the model is outdated.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ABGameDeveloper/status/2063808353575534745" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
