---
type: social-topic-report
date: '2026-10-05'
topic: game-dev
lang: en
pair: game-dev.th.md
generated_at: '2026-10-05T03:08:12+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 134
salience: 0.45
sentiment: neutral
confidence: 0.6
tags:
- unreal-engine
- unity
- godot
- indie-tools
- runescape
- mobile-games
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2106481097404284928/img/KwQjONA25d9fRY4z.jpg
---

# Game Dev — 2026-10-05

## TL;DR
- Jagex announced RS4, a new RuneScape MMORPG built in Unreal Engine and set in Gielinor. It is in early development, starts in Ashenfall and is described as 'a few years away' [2][7][14][42]. One account says it began as a Dragonwilds expansion [4].
- Unreal Engine 5 shipped titles got most of the engine attention: players praised Gears of War: E-Day early access and Ace Combat 8 (Xbox Series X, Performance Mode) for their visuals [20][36][54]. Some posts criticised a generic 'Unreal lighting' look in cutscenes [12] and the per-game tuning UE titles need [59].
- Small tool releases: the hun0fx Pixel Art VFX Generator (free demo, 25% off at launch) [6], Crocotile 3D v2.7.4 [28], RPG Paper Maker 3.2.14 [52], a Character Sprite Sheet Creator v1.0 [35], and Amplify Decals for Unity, announced for the Asset Store [51].
- A studio shipped the mobile game 'Ninety-Nine' with no game engine, using React Native, Expo, Skia and Reanimated [55].
- There was almost no signal on AI in game pipelines. One post claims a Street View to Unreal scene pipeline built with Sol 6.1, Opus 5.5 and Qwen2.5-image, with no technical detail [46].

## What happened
The biggest real news was Jagex announcing RS4, a fourth-generation RuneScape MMO built in Unreal Engine. It is set after Dragonwilds, starts in Ashenfall during the Sixth Age, and Jagex says it is years from release [2][4][7][14][29][42]. Several items were about players reacting to visuals in shipped or early-access UE5 games: Gears of War: E-Day [36][39][54], Ace Combat 8 on Series X [20] and a fan-made Sega Rally tribute [18]. A smaller group of posts criticised UE look and performance [12][59].

The rest was tooling and indie work: a pixel-art VFX generator [6], a Crocotile 3D update [28], an RPG Paper Maker feature [52], a sprite sheet creator [35], an upcoming Unity decal tool [51], a Godot shader book [40] and a Unity procedural VFX breakdown [21]. A Fortnite asset-porting fork now converts Unreal material graphs into Blender node graphs instead of using pre-built shaders [26]. One post argued that s&box ('game creation platform') has no clear audience, because developers already have Godot, Unreal and Unity [8]. Many high-engagement items are off-topic noise that matched on the words 'unreal' or 'Godot' [1][5][9][24][32][33][34].

## Why it matters (reasoning)
RS4 adds to a pattern of established live-service studios moving long-running IPs onto Unreal [2][7]. It is years out, so it has no near-term effect, but it supports the view that Unreal is the default choice for high-fidelity projects. The criticism of a generic 'UE lighting' look [12] and per-title tuning work [59] is the other side of that default: the engine's out-of-the-box look is now recognisable, and art direction is what makes a game stand out. For small studios, the more relevant evidence is the steady supply of narrow, cheap tools for pixel art, decals, sprites and voxel/tile modelling [6][28][35][51]. These cut asset-production time without an engine change. The no-engine React Native/Skia game [55] shows that simple 2D mobile games can be built on a web/mobile stack, which matters to teams that already ship React Native apps. The AI-pipeline claim [46] is anecdotal and should not shape decisions.

## Possibility
Likely: more Jagex and RS4 detail over the coming months, since the game is announced but early [7][42]. Likely: continued UE5 praise and performance criticism as Gears of War: E-Day reaches full release [36][59]. Plausible: more small studios ship simple 2D mobile games on React Native + Skia rather than Unity, but there is only one data point [55]. Unlikely: s&box broadening its audience soon. The critique [8] shows scepticism, but one post is weak evidence. Unclear: whether AI-generated environment pipelines like [46] are production-ready, because there is no technical detail.

## Org applicability — NDF DEV
1) Evaluate Amplify Decals when it reaches the Asset Store, for Unity XR and edutech environments that need edge or strip decals on uneven surfaces (low effort) [51]. 2) For 2D or pixel-style edutech mini-games, try the hun0fx VFX generator demo and the Character Sprite Sheet Creator before commissioning custom art (low) [6][35]. 3) For simple mobile edutech games where the team already ships React Native, prototype one on Expo + Skia + Reanimated and compare app size and iteration speed with Unity (med) [55]. 4) For Unity technical art, read the procedural Eldritch Blast VFX breakdown as a shader reference (low) [21]. Skip: RS4 news (no actionable impact) [2], s&box [8], the AI Street View-to-Unreal claim until it has reproducible detail [46], and UE5 visual-praise threads [20][36].

## Signals to Watch
- RS4 development updates and any Jagex statements about Unreal tooling or engine version [7][42]
- Amplify Decals Asset Store launch and pricing [51]
- Further engine-free mobile games on React Native/Skia [55]
- Tools that convert Unreal material graphs to Blender, as an asset-interop path [26]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | SpicyCurty | ^22254 c93 | [Okay but imagine if this scene was made in unreal engine and the camera was over](https://x.com/SpicyCurty/status/2106730096937603270) |
| x | Wario64 | ^6675 c123 | [4th RuneScape MMO in development, built in Unreal Engine and set in the world of](https://x.com/Wario64/status/2106481517598052357) |
| x | syni_bread | ^3117 c12 | [Godot as a new freebie sticker You don’t get to choose your freebie I just vibe ](https://x.com/syni_bread/status/2106501542312636696) |
| x | JayOddity | ^2581 c61 | [RuneScape 4 Has Been Announced - It Was Originally A Dragonwilds Expansion - Pos](https://x.com/JayOddity/status/2106515896969863562) |
| x | TeamCRonaldo | ^2155 c71 | [It's funny how fast the tone changes when real pressure hits... Something clearl](https://x.com/TeamCRonaldo/status/2106629006283993535) |
| x | hun0fx | ^1795 c28 | [I just released my first tool: hun0fx Pixel Art VFX Generator Hope it helps for ](https://x.com/hun0fx/status/2106586854342676712) |
| x | Pirat_Nation | ^1711 c45 | [Jagex has officially announced RS4, a new RuneScape MMORPG that aims to start a ](https://x.com/Pirat_Nation/status/2106490758983229585) |
| x | Rivo9_ | ^1062 c57 | [S&box is a solution in need of a problem -Players don't want a "game creation pl](https://x.com/Rivo9_/status/2106607219626434794) |
| x | GodotIsW8ing4U | ^1011 c7 | [@KenFarmer @ReviewsPossum In just the past few months we have not only learned t](https://x.com/GodotIsW8ing4U/status/2106506934132298075) |
| x | Nanju_Bami | ^937 c5 | [dialog test #unity3d #FPS #indiedev #gamedev #unity #ゲーム制作 https://t.co/5Kr2CFFW](https://x.com/Nanju_Bami/status/2106478273496776744) |
| x | worblir | ^609 c10 | [Paper Jerma tracks down the JWF wrestling superstar, the Glue Man, at the dodgy ](https://x.com/worblir/status/2106816164156624943) |
| x | droolvana | ^524 c13 | [These 3d rendered cutscenes have the most stereotypical unreal engine lighting e](https://x.com/droolvana/status/2106817291031564352) |
| x | ewoera | ^505 c1 | [Meet our new centaur, Calista!🐎❤️ #furry #VR #centaur #gamedev #indiedev #vrgame](https://x.com/ewoera/status/2106782723897544763) |
| x | Ninjago9101 | ^502 c16 | [RS4 – A New RuneScape MMO announced A new 4th-generation RuneScape MMORPG built ](https://x.com/Ninjago9101/status/2106500806363230472) |
| x | indieforgames | ^396 c7 | [When an animator gets bored, make a crow breakdance in Blender. 🐦🕺 Character ani](https://x.com/indieforgames/status/2106708930403475867) |
| x | Jyunaut | ^342 c6 | [Revamped some heavy attack animations. #gamedev #indiegame #unity https://t.co/d](https://x.com/Jyunaut/status/2106743734947958798) |
| x | ProjectAliveDev | ^338 c9 | [Attack helicopters are now units you can command in Ebbtide. Meet the Apache and](https://x.com/ProjectAliveDev/status/2106796377284231402) |
| x | GamewithDave | ^330 c12 | [Sega Rally fans need to see this. Over Jump Rally is an unofficial tribute to th](https://x.com/GamewithDave/status/2106821675522089203) |
| x | lowpolylover | ^310 c7 | [First things first: deal with the ranged guy. Map update • Enemy range • Low clo](https://x.com/lowpolylover/status/2106742397204115836) |
| x | JamieMoranUK | ^300 c5 | [This is my actual in game footage of Ace Combat 8 (Mission Replay) It’s literall](https://x.com/JamieMoranUK/status/2106572212832456746) |
| x | jettelly | ^295 c0 | [Ryan Gee made this stylized take on Eldritch Blast in Unity! The eyes inside the](https://x.com/jettelly/status/2106398881693012244) |
| x | GarrettSavo | ^271 c0 | [Trying to bring back mystery to games Wishlist on Steam -> https://t.co/ULaGMhXZ](https://x.com/GarrettSavo/status/2106569551676621298) |
| x | BorgesDev | ^270 c14 | [Just kidding :) #MinecraftGodot #Minecraft #Godot #Fangame https://t.co/Gg20gFaT](https://x.com/BorgesDev/status/2106818188772102630) |
| x | goth600 | ^241 c44 | [unreal engine, hyper realistic, Minecraft, photorealistic, reflections, The Lege](https://x.com/goth600/status/2106822881376415965) |
| x | SpicyCurty | ^223 c0 | [@SH3Enjoyer Unfortunately this wouldn’t solve the unreal engine issue…](https://x.com/SpicyCurty/status/2106809389596258803) |
| x | psdkyo | ^192 c19 | [For the past few days i've been working on a Fortnite Porting Fork that translat](https://x.com/psdkyo/status/2106489569747071212) |
| x | RealCashEnt | ^187 c23 | [Blade Royal is back and Reborn. Jump, guard, and strike through 3D worlds in **B](https://x.com/RealCashEnt/status/2106542295789277440) |
| x | Crocotile3D | ^158 c0 | [New version of Crocotile 3d (v2.7.4) is released! Various bug fixes and qol impr](https://x.com/Crocotile3D/status/2106823613584224547) |
| x | RinoTheBouncer | ^155 c3 | [RuneScape 4 is officially in development🚀 ✅Aims to bring the MMO world of Gielin](https://x.com/RinoTheBouncer/status/2106497938432110688) |
| x | cagyjan1 | ^150 c23 | [Still extremely bullish on @staratlas. The foundation they’ve built is insane. A](https://x.com/cagyjan1/status/2106599965082436051) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SpicyCurty</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 22254 · 💬 93</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SpicyCurty/status/2106730096937603270">View @SpicyCurty on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Okay but imagine if this scene was made in unreal engine and the camera was over her shoulder”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral X post shows a film or game scene and imagines it rebuilt in Unreal Engine with an over-the-shoulder camera; it is a fan 'what if' with no tool, release or technique.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SpicyCurty/status/2106730096937603270" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Wario64</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6675 · 💬 123</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Wario64/status/2106481517598052357">View @Wario64 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“4th RuneScape MMO in development, built in Unreal Engine and set in the world of Gielinor Releasing &quot;a few years away&quot; https://t.co/1pTZEoDTo7 https://t.co/K6nDFH7lyp”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Wario64 reports a 4th RuneScape MMO is in development, built in Unreal Engine and set in the world of Gielinor, with a release &quot;a few years away&quot;.</dd>
      <dt>Why interesting</dt>
      <dd>A long-running MMO franchise built on its own tech is moving its next title to Unreal Engine, a data point on engine choice for large online games.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Wario64/status/2106481517598052357" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@syni_bread</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3117 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/syni_bread/status/2106501542312636696">View @syni_bread on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Godot as a new freebie sticker You don’t get to choose your freebie I just vibe check you https://t.co/z7nn4ZUfm1”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X post with 3,100+ likes shows Godot's logo as a freebie sticker, joking that attendees get whatever sticker they're handed rather than choosing one.</dd>
      <dt>Why interesting</dt>
      <dd>It's a community meme with no release, tool change, or technique, though the engagement shows Godot's active fan base.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/syni_bread/status/2106501542312636696" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@JayOddity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2581 · 💬 61</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/JayOddity/status/2106515896969863562">View @JayOddity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“RuneScape 4 Has Been Announced - It Was Originally A Dragonwilds Expansion - Possibly Action Combat (based on the above) - Unreal Engine - Set In Gielinor, Starts In Ashenfall - Set After Dragonwilds ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>RuneScape 4 was announced as an Unreal Engine MMO set in Gielinor, starting in Ashenfall after the events of Dragonwilds; it began as a Dragonwilds expansion and may use action combat.</dd>
      <dt>Why interesting</dt>
      <dd>A long-running MMO franchise moving to Unreal Engine and a possible action-combat model shows how a spin-off expansion can grow into a full sequel.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/JayOddity/status/2106515896969863562" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TeamCRonaldo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2155 · 💬 71</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TeamCRonaldo/status/2106629006283993535">View @TeamCRonaldo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It's funny how fast the tone changes when real pressure hits... Something clearly changed suddenly ​All week, Jorge Jesus was acting tough in press conferences. Bragging to journalists that “I can pro”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan account claims Portugal coach Jorge Jesus softened his stance on benching Cristiano Ronaldo after Bruno Fernandes publicly backed Ronaldo and Joao Felix deleted a photo with the coach.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TeamCRonaldo/status/2106629006283993535" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@hun0fx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1795 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/hun0fx/status/2106586854342676712">View @hun0fx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I just released my first tool: hun0fx Pixel Art VFX Generator Hope it helps for your games! It's on https://t.co/bzbSH3k86f with a free demo, 25% off for the first two weeks: https://t.co/b1XVd33T1e #”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Indie developer @hun0fx released a Pixel Art VFX Generator, their first tool, with a free demo and a 25% launch discount for the first two weeks.</dd>
      <dt>Why interesting</dt>
      <dd>Pixel art projects often need many hand-drawn effects such as explosions and impacts, so a generator with a free demo is a cheap way to cut that art time.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio has a pixel art project, try the free demo on one effect and compare output quality and time against hand-drawn VFX.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/hun0fx/status/2106586854342676712" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1711 · 💬 45</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2106490758983229585">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Jagex has officially announced RS4, a new RuneScape MMORPG that aims to start a new era for the series. &gt;New MMORPG: RS4 is being built as an entirely new RuneScape game, rather than an update to the ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Jagex announced RS4, a new RuneScape MMORPG built from scratch in Unreal Engine, starting from the Ashenfall area of RuneScape: Dragonwilds; it is years from release and has no date.</dd>
      <dt>Why interesting</dt>
      <dd>A long-running MMO studio is moving its flagship franchise to Unreal Engine while keeping existing games live, a data point on engine choice for large online games.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2106490758983229585" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rivo9_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1062 · 💬 57</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Rivo9_/status/2106607219626434794">View @Rivo9_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“S&amp;box is a solution in need of a problem -Players don't want a &quot;game creation platform&quot; they want a game. -Devs can either use godot, unreal, unity, zdoom, adventure game studio, and mod hundreds of g”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X post argues S&amp;box, a game-creation platform, has no clear audience: players want finished games, and devs already have Godot, Unreal, Unity and modding scenes, versus a $10 walled garden.</dd>
      <dt>Why interesting</dt>
      <dd>It is one opinion, but it names the adoption question any new creation platform faces: why would devs or players switch from engines and mod scenes they already use.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Rivo9_/status/2106607219626434794" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
