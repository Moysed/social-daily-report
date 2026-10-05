---
type: social-topic-report
date: '2026-10-05'
topic: 3d-graphics
lang: en
pair: 3d-graphics.th.md
generated_at: '2026-10-05T03:22:15+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 47
salience: 0.35
sentiment: mixed
confidence: 0.55
tags:
- blender
- realtime-vfx
- procedural
- unity
- gaussian-splatting
- ai-3d
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2106290053110439936/img/69Hx_FR1NmgcJ9Lm.jpg
---

# 3D & Graphics — 2026-10-05

## TL;DR
- This was a low-signal day: about 20 of 47 items promote Vangrid's 3D-capture bounty marketplace with similar wording and comment counts of 150–450 (e.g. [6][7][10][11]). That pattern looks like crypto engagement campaigns, not real practitioner interest.
- Vangrid's claimed flow: an AI agent posts a 3D-capture bounty over x402, pays in USDC on Base or Arc, a person films an orbit of the location, and the 3D capture goes back to the agent. The posts say the first bounty on Arc has settled [10][14][44].
- Blender add-on updates: BeFX Studios released RBDLab 1.6, an overhaul of its destruction/simulation suite [24]. Blender Procedural shipped Ultimate Generators Addon V2 with 50+ procedural Geometry Nodes generators [31]. Hurricane is a unified particle solver for fluids, cloth and softbodies [18].
- Engine-agnostic VFX and shader tooling: The Shaders Bible published a metaballs-portal particle VFX for both Unity and Godot [1]. Kaleidos exports no-code animated shader patterns to Unity or Godot [27].
- Meshy and OpenAI are sponsoring a Unity AI Game Jam at G-STAR 2026: 50 developers, 24 hours, Nov 18–19 at BEXCO, Busan [46]. The only Gaussian Splatting research item is the EvenSplat paper on exposure and illumination variation [45].

## What happened
The real practitioner content today is incremental. On Blender, BeFX Studios released RBDLab 1.6 [24], Ultimate Generators Addon V2 added 50+ Geometry Nodes generators [31], and Hurricane was promoted as a unified particle solver [18]. One creator showed Mixie3D giving AI agents direct API control of Blender instead of simulating UI clicks, and claims it generated a procedural Pegasus in one run [4]. In Unity, the posts include The Shaders Bible's metaballs portal tutorial (Unity and Godot) [1], a fully procedural Eldritch Blast effect [9], a black hole VFX [30] and Kaleidos, a no-code shader pattern tool that exports to Unity and Godot [27]. Unreal and Houdini showed free Niagara tutorials [2], a guided bubbles and wet foam solver based on a Wētā FX paper [13], and portfolio VFX pieces [8][25]. One creator also showed a Blender shader matching closely between the Blender viewport and in-game [19].

For capture and reconstruction, the volume came from Vangrid. Many near-identical posts describe agent-posted, USDC-paid 3D-capture bounties on Base and Arc, with privacy filtering before submission [5][10][14][17][44]. Item [6] credits Niantic with having built a large 3D capture dataset as a by-product of its mobile game. The only research item is EvenSplat, which separates exposure and illumination effects in Gaussian Splatting [45]. Meshy announced its sponsorship of the G-STAR Unity AI Game Jam [46]. Two practitioners said AI did poorly at reconstructing hard-surface parts, and that generating pieces one by one or building them by hand was faster [38][39].

## Why it matters (reasoning)
The useful trend is that Blender keeps taking on work that used to need Houdini or paid middleware. RBDLab 1.6 [24] and Hurricane [18] cover destruction and multi-physics, and Ultimate Generators [31] covers procedural kitbashing. Many featured Unity and Unreal VFX pieces list Blender in their toolchain [8][25][28][30], and [19] shows Blender shaders carrying over to in-game results. For a small studio, that means more simulation and procedural asset work can stay in a free tool. Engine-agnostic VFX and shader tooling ([1][27][29], all Unity and Godot) lowers the cost of building effects that are not locked to one engine.

The agent-driven Blender claim [4] is a single, self-promotional demo. Practitioner reports that AI gets hard-surface reconstruction wrong [38][39] point the other way, so treat agentic 3D generation as unproven for production assets. The Vangrid volume [5][7][10][11][14][16][21][23][26][33][34][37][40][42] tells you little about capture technology. Comment counts of 150–450 on low-score posts and repeated talking points point to an incentive campaign. Its only concrete claim is a bounty API that pays people to film places for AI agents. The niche is physical-AI and robotics data, not game assets. The one honest critique in the set says it does not solve the question of whether a machine should trust the data it receives [15].

## Possibility
Likely: more Blender simulation and procedural add-ons will overlap with Houdini features. Today had two separate releases in that space, [24] and [31], plus a new solver [18]. Plausible: MCP- or API-style agent control of Blender becomes a common add-on pattern for procedural props. That rests on one demo [4] and is offset by the hand-modeling reports in [38][39]. Plausible: AI-generated 3D (Meshy) becomes more visible in Unity workflows through events like the G-STAR jam [46]. A jam does not show the assets hold up in production. Unlikely in the near term: Vangrid-style crowdsourced bounty capture matters for game or XR asset pipelines. The evidence is promotional, crypto-incentivized, and aimed at robotics data [10][15][42]. Gaussian Splatting research continues, with EvenSplat [45] addressing lighting consistency, but today gives no sign of new engine integration.

## Org applicability — NDF DEV
1) Evaluate RBDLab 1.6 for destruction effects in Unity game and XR projects before buying Houdini seats. Effort: med [24]. 2) Try Ultimate Generators V2 to block out environment props quickly, and check polycount against Quest budgets. Effort: low [31]. 3) Study The Shaders Bible metaballs portal and the procedural-eyes breakdown as reference for stylized Unity VFX. Effort: low [1][9]. 4) Test Blender-to-Unity shader matching on one stylized material, along the lines of [19][28]. Effort: low. 5) Run a one-day spike with Mixie3D or similar agent-to-Blender control on a procedural prop. Judge it on clean topology and UVs, not demo visuals. Effort: med [4][38]. 6) If any staff are in Korea, consider the G-STAR Unity AI Game Jam (Nov 18–19, Busan) as a way to test Meshy in a Unity build. Effort: low [46]. 7) If the team's Gaussian Splatting capture work (VR tours) suffers from mixed exposure, read EvenSplat. Effort: low [45]. Skip: Vangrid bounties and the related physical-AI posts [5][7][10][11]; PlayOnMint [22]; prompt-art and generic AI-tool lists [12][20][36]; personal or off-topic posts [3][35][47].

## Signals to Watch
- Whether RBDLab 1.6 and Hurricane get adopted in shipped game pipelines, as opposed to showreels [18][24].
- Whether agent-controlled Blender (Mixie3D) gets independent reviews or is shown producing production-ready topology [4][39].
- Meshy assets in the G-STAR Unity AI Game Jam builds, Nov 18–19 [46].
- Whether EvenSplat code is released and gets picked up by Gaussian Splatting viewers or importers [45].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ushadersbible | ^4160 c14 | [A small tutorial on how we made the metaballs portal using a particle system. Th](https://x.com/ushadersbible/status/2106290605449937310) |
| x | cghow_ | ^725 c4 | [🔥FREE🔥 Unreal Engine Niagara VFX Tutorials https://t.co/EUZYFbTSXo @unrealengine](https://x.com/cghow_/status/2106384526360428859) |
| x | bilawalsidhu | ^515 c18 | [If you want to understand the techno-religious fervor in AI, go read this cult c](https://x.com/bilawalsidhu/status/2106493590843310549) |
| x | Stefan_3D_AI | ^414 c23 | [I stopped making AI click around Blender. @mixie3D gives agents direct control +](https://x.com/Stefan_3D_AI/status/2106768134581727396) |
| x | evrendag1284 | ^398 c364 | [hello friends , what caught my attention in the @vangrid_io capture flow is that](https://x.com/evrendag1284/status/2106728150554055093) |
| x | DucCryptoX | ^388 c451 | [Niantic spent years building one of the largest 3D capture datasets in the world](https://x.com/DucCryptoX/status/2106342246954283383) |
| x | Bency1749379 | ^376 c448 | [Gm The more I look into Physical AI, the more obvious one thing becomes: robots ](https://x.com/Bency1749379/status/2106223617830723745) |
| x | VFXApprentice | ^351 c2 | [Glitch Challenge by Marjorie ROCHE Made with Unreal, Houdini, Clip Studio Paint ](https://x.com/VFXApprentice/status/2106455996113809724) |
| x | jettelly | ^295 c0 | [Ryan Gee made this stylized take on Eldritch Blast in Unity! The eyes inside the](https://x.com/jettelly/status/2106398881693012244) |
| x | jaouad2d | ^272 c242 | [Agents can now post a bounty in USDC and have someone walk the actual street to ](https://x.com/jaouad2d/status/2106560943375200480) |
| x | _Dripxel | ^251 c266 | [The real breakthrough for AI agents may not be another model. It may be giving t](https://x.com/_Dripxel/status/2106232054396711239) |
| x | goth600 | ^245 c44 | [unreal engine, hyper realistic, Minecraft, photorealistic, reflections, The Lege](https://x.com/goth600/status/2106822881376415965) |
| x | cdvr_szf | ^231 c6 | [Guided Bubbles & Wet Foam Solver in @sidefxhoudini The solver is based on the Wē](https://x.com/cdvr_szf/status/2106681566131024060) |
| x | tofudestiny | ^203 c229 | [an AI agent being able to request a physical-world capture changes the role of t](https://x.com/tofudestiny/status/2106553993036263647) |
| x | YaldaMasoudi | ^198 c210 | [The new agent bounty flow from @vangrid_io solves one problem: how software can ](https://x.com/YaldaMasoudi/status/2106365480101417433) |
| x | 0xZane_ | ^187 c159 | [AI has learned a huge amount from the internet but the real world is a different](https://x.com/0xZane_/status/2106246440884535507) |
| x | Ishaq0x_ | ^171 c214 | [Yesterday checked Docs: https://t.co/wIFAz7cpIi… The main thing I’d break down f](https://x.com/Ishaq0x_/status/2106220126324351122) |
| x | indieforgames | ^161 c1 | [Hurricane is a revolutionary tool integrated into Blender for generating high-fi](https://x.com/indieforgames/status/2106321594276807132) |
| x | jared_nyts | ^157 c1 | [New shader test Left is Blender, right is in-game screenshot https://t.co/gWzJqN](https://x.com/jared_nyts/status/2106844931985645748) |
| x | liluocheng13 | ^153 c36 | [Image : Midjourney + ChatGPT Video : Seedance 2.0, 15s, 720p Epic Chinese dark f](https://x.com/liluocheng13/status/2106255062775517290) |
| x | ChuBe_Cryp | ^146 c183 | [GM CT.. Most people look at Vangrid as a spatial data network. I think that’s to](https://x.com/ChuBe_Cryp/status/2106631987712958464) |
| x | rame9040 | ^122 c152 | [Good afternoon dear X mates @PlayOnMint is taking Web3 entertainment to the next](https://x.com/rame9040/status/2106661561809158280) |
| x | ikramulweb3 | ^118 c128 | [Good night Crypto Twitter 😴 Deploying fleets of corporate vehicles to map the wo](https://x.com/ikramulweb3/status/2106804794782535714) |
| x | 3DxDEV7 | ^110 c6 | [Is Blender officially closing the gap on Houdini for complex VFX and physical de](https://x.com/3DxDEV7/status/2106320750416126074) |
| x | VFXApprentice | ^98 c1 | [Lightning Projectile Game VFX by YUBI_VFX Made using Unreal Engine, Photoshop an](https://x.com/VFXApprentice/status/2106788688462020980) |
| x | Sumon_Web3 | ^85 c78 | [Robots do not fail from a lack of models. They fail from a lack of ground truth.](https://x.com/Sumon_Web3/status/2106751157460951522) |
| x | jettelly | ^71 c1 | [Kaleidos lets you create animated shader patterns without code, then export them](https://x.com/jettelly/status/2106670670079771021) |
| x | Mix3Design | ^68 c0 | [What if you could build your game VFX in Blender and take it straight into your ](https://x.com/Mix3Design/status/2106536704412659768) |
| x | jettelly | ^61 c0 | [Do you work with both Unity and Godot? The Shaders Bible Collection includes 1,1](https://x.com/jettelly/status/2106338474886304102) |
| x | VFXApprentice | ^57 c0 | [Black Hole VFX by Renzo Solorzano Made using Unity, Blender, Photoshop and Subst](https://x.com/VFXApprentice/status/2106879033631744284) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ushadersbible</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4160 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ushadersbible/status/2106290605449937310">View @ushadersbible on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A small tutorial on how we made the metaballs portal using a particle system. This VFX is available in both Unity and Godot ➡️ https://t.co/hLHBiQ05zV #indiedev https://t.co/5q8B4NSLhm”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Unity shader/VFX creators @ushadersbible published a short tutorial on building a metaballs portal effect with a particle system, with the VFX available for both Unity and Godot.</dd>
      <dt>Why interesting</dt>
      <dd>Metaballs built from a particle system avoid custom raymarching, so a small team can get a stylized liquid or portal look at low cost, and the same approach works across two engines.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Have the Unity team follow the tutorial once to build a reusable metaballs portal prefab for prototypes, then check its particle count cost on mobile and Quest.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ushadersbible/status/2106290605449937310" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cghow_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 725 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cghow_/status/2106384526360428859">View @cghow_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🔥FREE🔥 Unreal Engine Niagara VFX Tutorials https://t.co/EUZYFbTSXo @unrealengine #CGHOW #realtimevfx #ue4 #ue5 #ue5niagara #unrealengine #VFX #Game #ue4niagara https://t.co/fFnaCV7w09 https://t.co/rZA”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>CGHOW, a creator account, posts a link to free Unreal Engine Niagara VFX tutorials covering UE4 and UE5 real-time effects.</dd>
      <dt>Why interesting</dt>
      <dd>Free Niagara tutorials give a small team a no-cost way to learn real-time VFX for Unreal projects, though the post gives no detail on content or quality.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cghow_/status/2106384526360428859" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 515 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2106493590843310549">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If you want to understand the techno-religious fervor in AI, go read this cult classic and suddenly it'll all make sense. The dawn of the internet had very similar reactions. https://t.co/bsDED2XhCy”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Bilawal Sidhu recommends an unnamed 'cult classic' text as a key to the quasi-religious fervor around AI, and says the early internet drew similar reactions.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2106493590843310549" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Stefan_3D_AI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 414 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Stefan_3D_AI/status/2106768134581727396">View @Stefan_3D_AI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I stopped making AI click around Blender. @mixie3D gives agents direct control + multi-agent workflows + real 3D skills. No more UI simulation. Tested it on my game. One run: full procedural Pegasus w”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X user says Mixie3D lets AI agents control Blender directly instead of simulating UI clicks, and in one run produced a procedural Pegasus with hair, wings, and a self-built control rig.</dd>
      <dt>Why interesting</dt>
      <dd>Direct API-level control of Blender, rather than screen-driven automation, makes agent-built 3D assets faster and more reliable; this is a single anecdotal demo, not a benchmark.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Have the 3D artist try Mixie3D on one throwaway prop or rig task and compare the time and result against the current manual Blender workflow.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Stefan_3D_AI/status/2106768134581727396" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@evrendag1284</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 398 · 💬 364</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/evrendag1284/status/2106728150554055093">View @evrendag1284 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“hello friends , what caught my attention in the @vangrid_io capture flow is that privacy and quality are handled before a clip ever becomes a bounty submission. You open Capture Data, allow the camera”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A post describes how a crowdsourced 3D-capture app guides contributors: it blurs faces and plates on-device before encoding, then auto-checks clips for length, clarity and coverage before submission.</dd>
      <dt>Why interesting</dt>
      <dd>Validating input quality and anonymizing data on the device, before upload, is a pattern a small team can reuse for any user-generated capture or scan pipeline.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">For any user-submitted scan or video feature, add an on-device coverage and quality check before upload so weak captures are rejected at the source.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/evrendag1284/status/2106728150554055093" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DucCryptoX</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 388 · 💬 451</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DucCryptoX/status/2106342246954283383">View @DucCryptoX on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Niantic spent years building one of the largest 3D capture datasets in the world, almost as a side effect of a mobile game. Players walked around, pointed a phone at a landmark, played for a few minut”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Niantic's game-driven scans form a passive 3D dataset that follows where players already are, while Vangrid collects footage only after a buyer funds a request for a specific location.</dd>
      <dt>Why interesting</dt>
      <dd>It contrasts two ways to source 3D capture data: incidental crowd coverage versus paid, on-demand capture. The post is also promotional for Vangrid and gives no data or specs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DucCryptoX/status/2106342246954283383" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Bency1749379</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 376 · 💬 448</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Bency1749379/status/2106223617830723745">View @Bency1749379 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gm The more I look into Physical AI, the more obvious one thing becomes: robots don’t just need better models. They need better data about the physical world. That’s the problem @vangrid_io is tacklin”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A promoter post says Vangrid turns smartphones into a distributed 3D capture network for Physical AI data, anchors captures onchain for verification, is live on web and Android, and raised a $9M seed.</dd>
      <dt>Why interesting</dt>
      <dd>It shows demand for crowd-sourced phone-based 3D capture as training data for robots, but the post is promotional and gives no capture quality, pricing, or API details.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Bency1749379/status/2106223617830723745" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFXApprentice</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 351 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFXApprentice/status/2106455996113809724">View @VFXApprentice on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Glitch Challenge by Marjorie ROCHE Made with Unreal, Houdini, Clip Studio Paint and Blender https://t.co/Ze4PqpKAX9 #TechArt #VFX #Houdini https://t.co/YlV5GGfNzi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>VFX artist Marjorie Roche shared a Glitch Challenge piece built with Unreal, Houdini, Clip Studio Paint and Blender, posted under #TechArt and #VFX.</dd>
      <dt>Why interesting</dt>
      <dd>It shows a concrete multi-tool pipeline: Houdini for FX, Unreal for real-time rendering, Blender for 3D, and Clip Studio Paint for 2D art, which is useful reference for stylized glitch effects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFXApprentice/status/2106455996113809724" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
