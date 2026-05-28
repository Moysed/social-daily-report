---
type: social-topic-report
date: '2026-05-27'
topic: multimodal-ai
lang: en
pair: multimodal-ai.th.md
generated_at: '2026-05-27T16:55:48+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- x
regions:
- global
post_count: 131
salience: 0.85
sentiment: mixed
confidence: 0.7
tags:
- generative-video
- comfyui
- open-weights
- runway-mcp
- anima
- production-pipeline
thumbnail: https://external-preview.redd.it/Z2xwcnk0NmtoYzNoMUOrN2x6d3_buiygc5_cWxIYitQKX9MLptdb_bnXJC5O.png?format=pjpg&auto=webp&s=d1592d8b80dc94af491213cc6de136f9a4235fbf
---

# Multimodal AI — 2026-05-27

## TL;DR
- Runway pushes 'uncanny-valley-crossed' claim with Project Luxo and ships an MCP server linking Gen-4.5/Seedance 2.0/Veo 3.1 into Claude/Cursor [10][6][24]
- Open-weight momentum: Anima 1.0 (with Turbo LoRA + InvokeAI 6.13 support), Microsoft Lens Turbo, and ternary Bonsai 4B (WebGPU) keep local pipelines viable [17][34][43][41][35]
- NVIDIA PiD does 4x super-resolution from latents for FLUX/Z-Image — practical upscaler for production art [12]
- ComfyUI is becoming the studio default: Netflix's new AI animation studio lists it next to Maya/Houdini; Yedp Blockout adds 3D scene blocking inside Comfy [44][45]
- Storyboard-first video tools (Topview Canvas, Flova, Mitte) signal a shift from prompt-roulette to controllable, director-driven AI video [51][57][42][20]

## What happened
Big-engagement signals split into two camps. Closed/hosted: Runway declared the uncanny valley crossed via Project Luxo and shipped an MCP that drops Gen-4.5, Seedance 2.0 and Veo 3.1 inside Claude/ChatGPT/Cursor [10][24][6]; Grok Imagine, Kling (House of David S1-2), and GPT Image 2 + Seedance combos dominated viral demos [2][59][20][15]. Open/local: Anima 1.0 got image editing, an official Turbo LoRA, and first-class support in InvokeAI 6.13 alongside Qwen Image and GPT Image API hooks [17][34][43]; PrismML released ternary Bonsai 4B running in-browser on WebGPU [35]; NVIDIA's PiD adds latent-space 4x SR to FLUX.1/2 and Z-Image [12]; Microsoft Lens Turbo lands in ComfyUI for low-VRAM users [41].

Workflow tooling matured: Yedp Blockout turns ComfyUI into a mini 3D studio for scene blocking [45], Netflix's AI animation studio job posts name ComfyUI explicitly [44], and storyboard-first video generators (Topview Canvas, Flova, Mitte) push toward shot-level control instead of pure prompting [51][57][42][20]. Cultural noise — viral Star Trek/TechnoViking parodies, Midjourney showcases, ad-spend brags — confirms the medium is now mainstream content, not novelty [1][3][8][11][13][16].

## Why it matters (reasoning)
For a Unity/XR/edutech studio, the meaningful shift isn't 'AI video looks real now'; it's that controllable, repeatable pipelines are forming. MCP-in-IDE access to multi-vendor video models [6] collapses the integration tax — a TD or artist can call Seedance/Veo/Gen-4.5 from Cursor with one auth. ComfyUI's rise to studio-tier tool [44] plus 3D scene-blocking nodes [45] means open pipelines can now match closed services for previz and asset gen, which matters for budgets and IP control. On the open-weights side, Anima + Turbo LoRA + InvokeAI 6.13 [17][34][43], PiD super-resolution [12], and ternary diffusion on WebGPU [35] are pushing real production into 8-12GB VRAM machines — viable for a Chiang Mai studio without GPU farm spend. Second-order effects: licensing/IP risk is escalating (auto-infringement guardrail failures [30]), and the cost-floor for ad/UGC content is collapsing toward $1/clip [40][15], so client expectations on turnaround and price will reset within 6 months.

## Possibility
Near term (3-6 months, ~70%): storyboard-first video tools become the default UX; Comfy + open video models (Wan/Anima descendants) reach 'good enough' for non-hero shots; MCP-style model routers become standard. Medium (6-12 months, ~50%): a credible open-weight video model challenges Veo/Kling on controllability, not just quality; XR/game asset gen pipelines (image -> 3D -> rig) consolidate around Comfy + DCC plugins. Lower likelihood (~25%): true world-model output usable for interactive XR scene gen [4]; still research-grade. Counter-scenario (~30%): IP litigation or platform crackdowns force studios back to in-house style refs and licensed models, raising costs again [30].

## Org applicability — NDF DEV
Concrete uses for NDF DEV:
1) Edutech visuals + e-learning illustrations: switch to Anima 1.0 + InvokeAI 6.13 locally [17][43], use PiD for 4x upscale to print/4K [12]. Saves Midjourney subs, keeps client assets on-prem.
2) Unity/XR previz + concept: adopt ComfyUI as the asset pipeline backbone [44], use Yedp Blockout for quick scene blocking before Unity import [45].
3) Marketing/trailers for games: Runway MCP inside Cursor [6] for the team's existing Claude workflow — gen short trailers/teasers via Gen-4.5/Seedance without leaving the editor. Worth a paid trial ($50-100/month).
4) Storyboard-first video for edutech explainer scenes: pilot Topview Canvas or Mitte [51][20] before committing to a stack.
Not worth chasing now: world models [4], hyped 'replace artists' subscription tools [9][55][60]. Skip the listicle stacks — noise.
Budget call: invest 1 sprint to stand up Comfy + Anima + PiD on the studio workstation; pilot Runway MCP for 1 month; defer video-model fine-tuning.

## Signals to Watch
- Anima ecosystem maturity — if ControlNets + IPAdapter land within 4-6 weeks, switch e-learning art pipeline off Midjourney
- ComfyUI 3D/scene-blocking nodes (Yedp Blockout and successors) — if Unity/Blender bridges appear, integrate into XR previz
- Runway MCP adoption — watch whether Cursor/Claude users report stable production use vs demo-only
- Storyboard-first video tools — first one to expose a deterministic shot-graph API wins studio workflows

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | 8bitcollective | ^3025 c119 | [Sulfur Breath by Gossip Goblin](https://www.reddit.com/r/aivideo/comments/1tnlczr/sulfur_breath_by_gossip_goblin/) |
| x | XFreeze | ^2330 c467 | [Grok Imagine image and video generation are truly incredible The realism is insa](https://x.com/XFreeze/status/2059311819986964731) |
| reddit | RioNReedus | ^1346 c140 | [Star Trek: NOT The Original Series](https://www.reddit.com/r/aivideo/comments/1to07f4/star_trek_not_the_original_series/) |
| x | juliarturc | ^827 c28 | ["World models" is one of the buzziest yet ambiguous terms in AI right now. I sta](https://x.com/juliarturc/status/2058951954483884301) |
| x | Just_sharon7 | ^738 c75 | [Found something awesome 🔥 A completely free gallery for AI image prompts. It's c](https://x.com/Just_sharon7/status/2059212550253035998) |
| x | runwayml | ^510 c35 | [Introducing Runway MCP. Now you can connect Runway directly into Claude, ChatGPT](https://x.com/runwayml/status/2059636517283176479) |
| x | fofrAI | ^495 c18 | [Omni: A man spells out strawberry while a counter keeps track of the number of R](https://x.com/fofrAI/status/2059248702859186285) |
| reddit | cs862 | ^470 c55 | [TechnoViking meets Snape and Dumbledore](https://www.reddit.com/r/aivideo/comments/1tnqhwf/technoviking_meets_snape_and_dumbledore/) |
| x | 0xbobaaa | ^416 c28 | [this guy never held a brush in his life. but makes $300k/month customer sends ph](https://x.com/0xbobaaa/status/2058953206764339271) |
| x | runwayml | ^399 c61 | [Introducing Project Luxo: a new initiative exploring how AI-generated video has ](https://x.com/runwayml/status/2059279505009615293) |
| x | lr_mvcreative | ^316 c261 | ["Where'd you shoot the mountain?" We didn't. We made a $3M looking campaign for ](https://x.com/lr_mvcreative/status/2059008979330871794) |
| x | multimodalart | ^288 c7 | [NVidia just released PiD: super resolution in pixel space directly from model la](https://x.com/multimodalart/status/2059003125768339649) |
| reddit | 12washingbeard | ^282 c9 | [Untitled 57](https://www.reddit.com/r/midjourney/comments/1tobtz7/untitled_57/) |
| x | siddsax | ^277 c26 | [1.8M impressions. $0 spent. An AI parody of Karpathy joining Anthropic. Scripted](https://x.com/siddsax/status/2058996623758557560) |
| x | ahmad_a_wahabb | ^263 c14 | [i've said this a hundred times: AI animations are the best converting ads right ](https://x.com/ahmad_a_wahabb/status/2058967801792987154) |
| reddit | liibertypriimex1 | ^252 c22 | [Pastel Prism Surrealism](https://www.reddit.com/r/midjourney/comments/1tnoe9x/pastel_prism_surrealism/) |
| reddit | Ancient-Future6335 | ^250 c26 | [Anima can edit images! And this is possible in two different methods. # Good aft](https://www.reddit.com/r/StableDiffusion/comments/1totumo/anima_can_edit_images_and_this_is_possible_in_two/) |
| x | Suhail | ^227 c27 | [Possibly the thing we will most realize looking back: intelligence was so big th](https://x.com/Suhail/status/2059106732736160036) |
| reddit | Comfortable-Catch751 | ^222 c17 | [Feminine Elegance and Decay](https://www.reddit.com/r/midjourney/comments/1to3p0x/feminine_elegance_and_decay/) |
| x | aimikoda | ^193 c16 | [GPT Image 2 + Seedance 2.0 Prompt Share Created on @mitte_ai I used the generic ](https://x.com/aimikoda/status/2059582790841069606) |
| x | hayalet_kadir | ^183 c5 | ["Prompt by Hayalet - Generated by Stable Diffusion DreamShaper XL'' https://t.co](https://x.com/hayalet_kadir/status/2059531068085026834) |
| x | fofrAI | ^181 c9 | [Omni is wild. &gt; Change the flip book to be two stick men fighting https://t.c](https://x.com/fofrAI/status/2059365776767742094) |
| x | Raullen | ^176 c68 | [Your OpenAI-compatible API makes images too 🎨 QuickSilver Pro now serves FLUX.2 ](https://x.com/Raullen/status/2059347678195282298) |
| x | c_valenzuelab | ^171 c24 | [Please spend 15 minutes watching these films. They will radically change your se](https://x.com/c_valenzuelab/status/2059284756798521585) |
| reddit | mitchellflautt | ^164 c1 | [The Grand Exilarch](https://www.reddit.com/r/midjourney/comments/1to84ps/the_grand_exilarch/) |
| x | choyamymuna | ^162 c39 | [100+ AI Tools to replace your tedious work: 1. Research - @ChatGPTapp - YouChat ](https://x.com/choyamymuna/status/2059405781687287947) |
| x | fofrAI | ^162 c15 | [One year later with Omni and this test can pass. I saw it getting pretty close, ](https://x.com/fofrAI/status/2059230628911124880) |
| reddit | Zaicab | ^157 c9 | [Arcana of the Rings](https://www.reddit.com/r/midjourney/comments/1to5279/arcana_of_the_rings/) |
| x | icreatelife | ^152 c31 | [Turn yourself into a chaotic sketchbook character living inside your city. Mine ](https://x.com/icreatelife/status/2059110178293764461) |
| x | Rahll | ^150 c4 | [Been talking about this since 2023 when I probed Midjourney and other models to ](https://x.com/Rahll/status/2059297880125431851) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@8bitcollective</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 3025 · 💬 119</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/aivideo/comments/1tnlczr/sulfur_breath_by_gossip_goblin/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/Z2xwcnk0NmtoYzNoMUOrN2x6d3_buiygc5_cWxIYitQKX9MLptdb_bnXJC5O.png?format=pjpg&amp;auto=webp&amp;s=d1592d8b80dc94af491213cc6de136f9a4235fbf" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Sulfur Breath by Gossip Goblin”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Reddit post in r/aivideo showcasing an AI-generated music video titled 'Sulfur Breath' by the artist Gossip Goblin, demonstrating multimodal AI combining audio and video generation.</dd>
      <dt>Why interesting</dt>
      <dd>High engagement (3025 likes) signals the community appetite for AI-generated creative video is mainstream — not experimental anymore.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's XR/e-learning teams can use multimodal AI pipelines to generate cinematic cutscenes or animated explainer sequences without a full production crew.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/aivideo/comments/1tnlczr/sulfur_breath_by_gossip_goblin/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@XFreeze</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2330 · 💬 467</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/XFreeze/status/2059311819986964731">View @XFreeze on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Grok Imagine image and video generation are truly incredible The realism is insanely good to the point where it starts blurring the line between AI generation and reality https://t.co/dhH8w4DGMw”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Grok Imagine's image and video generation quality is so photorealistic it's becoming hard to distinguish from real footage.</dd>
      <dt>Why interesting</dt>
      <dd>Grok Imagine now rivals Midjourney/Sora in realism — high engagement signals the market is paying attention to xAI's multimodal push.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can test Grok Imagine for rapid concept art and XR environment mockups — a free-tier alternative to Midjourney that also does video.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/XFreeze/status/2059311819986964731" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@RioNReedus</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 1346 · 💬 140</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/aivideo/comments/1to07f4/star_trek_not_the_original_series/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/cW9yZjV2OXV1ZjNoMRofDsV4AZlOpCi1-bToNdZsRd1LxlYONwleYiNA6o5E.png?format=pjpg&amp;auto=webp&amp;s=0520195d12782f2a622c7a6d9cfdb3bdc1b04eb1" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Star Trek: NOT The Original Series”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A creator posted an AI-generated Star Trek fan video (distinct from the original series) on r/aivideo, earning 1,346 likes and 140 comments.</dd>
      <dt>Why interesting</dt>
      <dd>1,346 likes on a fan AI video proves multimodal generation now hits cinematic quality that genre audiences accept — the quality bar crossed a real threshold.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's XR/VR team can use multimodal video generation to prototype cinematic cutscenes or pitch animatics without a full production pipeline, cutting pre-production time.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/aivideo/comments/1to07f4/star_trek_not_the_original_series/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@juliarturc</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 827 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/juliarturc/status/2058951954483884301">View @juliarturc on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&quot;World models&quot; is one of the buzziest yet ambiguous terms in AI right now. I started this video with many questions: - How are they different from video generation? - Can they do more than AI slop? - ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Creator made an explainer video on 'world models' in AI — covering how they differ from video generation and whether they go beyond AI slop, with input from NVIDIA AI.</dd>
      <dt>Why interesting</dt>
      <dd>World models aim to simulate cause-and-effect physics inside AI — a step beyond diffusion video, directly relevant to XR/VR where believable interactive environments matter.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The XR/VR team should track world model research — if real-time spatial reasoning matures, it replaces hand-authored physics rules in Unity simulations and opens richer training environments.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/juliarturc/status/2058951954483884301" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Just_sharon7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 738 · 💬 75</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Just_sharon7/status/2059212550253035998">View @Just_sharon7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Found something awesome 🔥 A completely free gallery for AI image prompts. It's called @meigen7982 packed with proven, viral prompts for GPT Image 2, Nano Banana 2, Seedance 2.0, Veo 3.1, Midjourney &amp; ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A free prompt gallery called Meigen collects proven, viral prompts for GPT Image 2, Midjourney, Veo 3.1, Seedance 2.0, and other multimodal AI tools — ready to copy.</dd>
      <dt>Why interesting</dt>
      <dd>Curated prompt libraries cut trial-and-error time drastically — teams can hit quality outputs on multimodal tools faster without burning API credits on failed attempts.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can reference Meigen when generating concept art, e-learning visuals, or XR environment mockups — treat it as a starting-point prompt bank, not a final output source.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Just_sharon7/status/2059212550253035998" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@runwayml</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 510 · 💬 35</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/runwayml/status/2059636517283176479">View @runwayml on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing Runway MCP. Now you can connect Runway directly into Claude, ChatGPT, Cursor, Replit and more. Generate polished images and videos with state-of-the-art models, like Gen-4.5, Seedance 2.0,”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Runway launched an MCP server that plugs its image and video generation models (Gen-4.5, Seedance 2.0, Kling, etc.) directly into Claude, ChatGPT, Cursor, and Replit.</dd>
      <dt>Why interesting</dt>
      <dd>AI media generation becomes a composable tool call inside the IDE — no tab-switching, no separate UI, just prompt-to-video inside the existing dev or agent workflow.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can wire Runway MCP into Cursor or Claude Code sessions to generate concept art and e-learning visuals on-demand, cutting round-trips between dev work and external creative tools.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/runwayml/status/2059636517283176479" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@fofrAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 495 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/fofrAI/status/2059248702859186285">View @fofrAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Omni: A man spells out strawberry while a counter keeps track of the number of Rs he says. https://t.co/SxwJcJusMo”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A demo of GPT-4o Omni shows the model tracking and counting the letter 'R' in real-time as a man verbally spells out 'strawberry'.</dd>
      <dt>Why interesting</dt>
      <dd>This shows Omni's real-time audio-visual grounding — it syncs spoken input with a live counter, a capability that directly enables interactive voice UI in apps.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's e-learning and XR products can wire Omni's real-time audio grounding into pronunciation exercises or live narration tracking — replacing manual transcript sync.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/fofrAI/status/2059248702859186285" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@cs862</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 470 · 💬 55</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/aivideo/comments/1tnqhwf/technoviking_meets_snape_and_dumbledore/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/Mmo2dXA5cmZqZDNoMTWA2OynjAFxXGJTJNVpwRtWN1x0H7WD5pkTfe1l-tqa.png?format=pjpg&amp;auto=webp&amp;s=271cdd34a46124fcfce66961da0b3e7423045134" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“TechnoViking meets Snape and Dumbledore”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Reddit post in r/aivideo showcasing an AI-generated video that blends the TechnoViking internet meme with Harry Potter characters Snape and Dumbledore.</dd>
      <dt>Why interesting</dt>
      <dd>Current multimodal AI video tools can convincingly merge unrelated pop-culture references into viral content, hitting 470 likes on a niche subreddit with minimal production effort.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's XR/VR and e-learning teams can use multimodal AI video generation to prototype character animations quickly, cutting pre-production time before committing to full 3D pipelines.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/aivideo/comments/1tnqhwf/technoviking_meets_snape_and_dumbledore/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
</div>
