---
type: social-topic-report
date: '2026-06-03'
topic: multimodal-ai
lang: en
pair: multimodal-ai.th.md
generated_at: '2026-06-03T07:02:53+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 130
salience: 0.8
sentiment: mixed
confidence: 0.6
tags:
- multimodal-ai
- image-to-3d
- video-generation
- open-weights
- comfyui
- world-models
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2061412305766645760/img/AIwo6_dR1c055x0i.jpg
---

# Multimodal AI — 2026-06-03

## TL;DR
- NVIDIA Cosmos 3, a family of open-weights omnimodal world models for Physical AI, is reported #1 in both Text-to-Image and Image-to-Video on the Artificial Analysis leaderboards [8].
- ByteDance released Bernini, an open-source video generation + editing framework with text-prompt edits and image/video references, code available [6].
- TripoAI's TripoSplat (open-source image-to-3D Gaussian model) shipped Day-0 in ComfyUI: one 2D image in, a 3D Gaussian asset out [24].
- Runway expanded Aleph 2.0 (compositing mattes, multi-shot edits up to 30s at 1080p) to its API and announced a London world-models hub with $100M UK investment [10][20][15].
- Reputational/IP friction surfaced: Scorsese is advising Black Forest Labs, founded by people who trained Stable Diffusion on copyrighted images [5][9].

## What happened
Several concrete releases landed for image/video/3D generation. NVIDIA's Cosmos 3 omnimodal world models reportedly topped open-weights Text-to-Image and Image-to-Video rankings [8], and NVIDIA is forming a 'Cosmos Coalition' with Runway [51]. ByteDance open-sourced Bernini, a video gen+editing framework with code released [6]. TripoAI's TripoSplat brought open-source image-to-3D Gaussian generation into ComfyUI on day one [24], alongside other ComfyUI pipelines (storyboard→Seedance 2.0 animation [32], Qwen Image 2512 [56], and the Nexus BTA local studio supporting SD 1.5/SDXL/Flux/Qwen/Z-Image Turbo/Lumina/WAN [35]). Runway pushed Aleph 2.0 editing to its API [20][10] and opened a London research hub focused on general world models with a $100M UK commitment [15]. Adobe deepened a partnership with NVIDIA across Photoshop, Premiere, and Substance 3D [17][38], and the Morpheus AI team (video world-model architectures) joined Roblox [7].

## Why it matters (reasoning)
The usable-for-production layer is shifting toward open weights and local ComfyUI pipelines, which fits a studio that prefers open weights/affordable APIs over closed demos. TripoSplat makes single-image→3D-Gaussian asset generation accessible inside an existing node graph [24], and Cosmos 3's 'Physical AI' world models target exactly the spatial/scene use cases relevant to XR [8]. The clustering of world-model bets — Cosmos Coalition [51], Runway's London hub [15], Morpheus→Roblox [7] — signals the next competition is interactive scene/world generation, not just clip output. Counterweight: quality is still uneven (text-to-video transformations show 'one or two' artifacts even on faster models like Seedance 2.0/Google Omni [3]), and the BFL/Stable Diffusion copyright lineage [5][9] is a live legal and reputational risk for any commercial deliverable built on those models. Much of today's volume is noise — recycled '80+ AI tools' listicles [18][40][42][49] and AI-influencer monetization pitches [27][29][60] — which inflates apparent activity without adding production signal.

## Possibility
Likely: open-source image-to-3D (TripoSplat) plus ComfyUI integration becomes a standard step in indie asset prototyping, given Day-0 support and the breadth of supported open models [24][35]. Plausible: world models from Cosmos/Runway/Morpheus move toward interactive scene generation usable in game/XR engines over the next 12–18 months, supported by Runway's stated investment timeline [15][7][8]. Plausible: copyright disputes around Stable-Diffusion-lineage tools (BFL) escalate and push studios toward cleaner-licensed or self-hosted weights [9][5]. Unlikely near-term: hands-off text-to-video for client work without manual cleanup, since even the faster 2026 models still produce artifacts [3]. No source states numeric probabilities, so none are given.

## Org applicability — NDF DEV
1) Test TripoSplat in ComfyUI for single-image→3D-Gaussian props/characters as a prototyping path for Unity/XR assets — low/med effort [24]. 2) Stand up a local ComfyUI image/video/3D bench (Nexus BTA, Flux/Qwen/SDXL/WAN) to keep generation in-house and license-controlled — med effort [35][56][32]. 3) Evaluate NVIDIA Cosmos 3 open weights for image/video and Physical-AI scene generation relevant to XR — med effort [8][51]. 4) Track Bernini for prompt-based video editing now that code is public — low effort to clone/assess [6]. 5) Set a policy: avoid Stable-Diffusion-lineage/BFL models for paid client deliverables until licensing is clear — low effort [9][5]. Consider Runway Aleph 2.0 API only if a hosted budget exists, but deprioritize vs open weights since it is closed/hosted [20]. Skip: the recycled '80+ AI tools' listicles [18][40][42][49], AI-influencer monetization threads [27][29][60], and waifu-art posts [14][46] — no production value.

## Signals to Watch
- ComfyUI as the integration hub for new open models (TripoSplat 3D, Seedance storyboards, Qwen) — watch day-0 support cadence [24][32][56].
- World-model consolidation: Cosmos Coalition, Runway London, Morpheus→Roblox — watch for interactive/engine-ready output [51][15][7].
- Copyright exposure on Stable-Diffusion-lineage tools (BFL) as a sourcing constraint for commercial work [9][5].
- Open-weights leaderboard claims (Cosmos 3 #1) — verify independently before adopting [8].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | TheDivineNigga | ^2030 c19 | [@lowtierrogdaily Cropped the video so we couldn't see that sora ai watermark😂](https://x.com/TheDivineNigga/status/2061615794241343848) |
| x | bippburger | ^1226 c5 | [See but I saw this movie and know it’s not true. The lead VFX firm credited is “](https://x.com/bippburger/status/2061897983923572969) |
| x | underwoodxie96 | ^1083 c29 | [I created this video using GPT Image 2.0 and Kling 3.0. I also tested Seedance 2](https://x.com/underwoodxie96/status/2061414477120016873) |
| x | javilopen | ^792 c2 | [@bfl_ai Well, this meme didn't age well 😂😂😂 https://t.co/1X7xPrtg3U](https://x.com/javilopen/status/2061834346969882649) |
| x | CCinephilia | ^702 c10 | [Marty didn't just disappoint us; he betrayed the entire film community. Only a f](https://x.com/CCinephilia/status/2061930091903332735) |
| x | aisearchio | ^677 c13 | [Bytedance drops an open-source Gemini Omni!!! Bernini is a new AI video generati](https://x.com/aisearchio/status/2061572022074020174) |
| x | xxunhuang | ^396 c59 | [I'm excited to announce that the Morpheus AI team is joining Roblox! Over the pa](https://x.com/xxunhuang/status/2061939239915528653) |
| x | ArtificialAnlys | ^323 c19 | [NVIDIA's Cosmos 3 lands at #1 among open weights models in both Text to Image an](https://x.com/ArtificialAnlys/status/2061494719998546206) |
| x | ednewtonrex | ^318 c11 | [Martin Scorsese is advising an AI company founded by the people who trained Stab](https://x.com/ednewtonrex/status/2061824631028265368) |
| x | runwayml | ^284 c17 | [Create compositing mattes in seconds with Aleph 2.0 Mattes let you isolate a sub](https://x.com/runwayml/status/2061548752989753454) |
| x | jimmytheanti | ^255 c2 | [@garegibb “AI” is part of normal production workflows. Many tools in programs li](https://x.com/jimmytheanti/status/2061947515906204064) |
| x | EMostaque | ^222 c14 | [I wonder how many founders will pass on investors who passed on them in prior ro](https://x.com/EMostaque/status/2061824453122642400) |
| x | EMostaque | ^206 c98 | [Let’s say half of OpenAI and Anthropic goes to the American people, $1 trillion ](https://x.com/EMostaque/status/2061461391303753992) |
| x | NoNameAIProject | ^203 c1 | [🌸 Asuna / Relaxing in Her Room 🌙 ✅ ALL CHARACTERS ARE 21+ ADULTS “Soft light… so](https://x.com/NoNameAIProject/status/2061584954707075122) |
| x | runwayml | ^199 c21 | [Today we're announcing London as Runway's new European headquarters and our newe](https://x.com/runwayml/status/2061450141614145621) |
| x | Suhail | ^196 c16 | [It is astounding how much and how fast you can learn anything with LLMs. On one ](https://x.com/Suhail/status/2061846994356953130) |
| x | icreatelife | ^196 c42 | [Excited to share with you Adobe where I work full time partners with NVIDIA 🎉 Ad](https://x.com/icreatelife/status/2061497655289926143) |
| x | 1005Alok85200 | ^182 c22 | [80+ AI tools to finish months of work in minutes. 1. Research - ChatGPT - Copilo](https://x.com/1005Alok85200/status/2061663273041432602) |
| x | ideogram_ai | ^179 c78 | [Tomorrow 12 noon ET. Reply with your ideogram username below for early access. h](https://x.com/ideogram_ai/status/2061855321690186089) |
| x | runwayml | ^176 c12 | [Aleph 2.0 is now available via the Runway API. Bring precise video editing direc](https://x.com/runwayml/status/2061895998545244342) |
| x | Kling_ai | ^151 c16 | [What if you could pack a cloud in a bag? ☁️ Here’s how we made it with Kling AI.](https://x.com/Kling_ai/status/2061462779647725817) |
| x | mehwishkiran07 | ^147 c38 | [AI can now help you build YouTube videos with MrBeast-level production... for fr](https://x.com/mehwishkiran07/status/2061765061841154161) |
| x | rebeccajolam | ^147 c4 | [Image to video using AI... Why I can't do NSFW? https://t.co/GeZJSiyNp9](https://x.com/rebeccajolam/status/2061476032457380134) |
| x | ComfyUI | ^145 c6 | [TripoSplat, an open-source image-to-3D Gaussian model from @tripoai, has Day-0 s](https://x.com/ComfyUI/status/2061509306743398668) |
| x | azed_ai | ^143 c15 | [Good morning, take today one small step at a time Newly created style on Midjour](https://x.com/azed_ai/status/2061673188405514614) |
| x | gh_marjan | ^141 c4 | [🚀 Hiring: Research Scientists at FAIR, Meta 🚀 We’re looking for strong candidate](https://x.com/gh_marjan/status/2061842923923333222) |
| x | betraidx | ^141 c8 | [She makes $14,500 a month. The other her makes nothing. Pause at 0:20 — that's t](https://x.com/betraidx/status/2061565192878624920) |
| x | javilopen | ^139 c74 | [Seriously, where is Apple?](https://x.com/javilopen/status/2061518758380765637) |
| x | Nekt_0 | ^134 c27 | [A KID CAN TURN ONE TIKTOK LINK INTO A JUSTIN BIEBER CLIP IN 4 STEPS. THAT SAME P](https://x.com/Nekt_0/status/2061802227530940857) |
| x | fofrAI | ^131 c32 | [stable diffusion](https://x.com/fofrAI/status/2061723550407340471) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheDivineNigga</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2030 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheDivineNigga/status/2061615794241343848">View @TheDivineNigga on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@lowtierrogdaily Cropped the video so we couldn't see that sora ai watermark😂”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user accuses @lowtierrogdaily of cropping out a Sora AI watermark to disguise AI-generated video as original content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheDivineNigga/status/2061615794241343848" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bippburger</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1226 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bippburger/status/2061897983923572969">View @bippburger on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“See but I saw this movie and know it’s not true. The lead VFX firm credited is “ACME AI,” there’s some shots in this that straight up look like Sora. I keep thinking about it”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viewer suspects a commercial film's VFX shots were generated with an AI video model like Sora, based on visual artifacts, with the credited VFX firm listed as 'ACME AI' — no movie title or verified evidence provided.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bippburger/status/2061897983923572969" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@underwoodxie96</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1083 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/underwoodxie96/status/2061414477120016873">View @underwoodxie96 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I created this video using GPT Image 2.0 and Kling 3.0. I also tested Seedance 2.0 and Google Omni. They're much faster for generating transformation videos, but in my tests there were often one or tw”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A creator used GPT Image 2.0 + Kling 3.0 with a start-frame/end-frame clip-chaining workflow and CapCut editing to produce cinematic AI transformation video, avoiding the uncanny look of single-shot generation.</dd>
      <dt>Why interesting</dt>
      <dd>The chaining technique directly solves the 'one unnatural shot' problem in AI video — useful for any studio producing XR walkthroughs, e-learning intros, or promo clips.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test the start-frame/end-frame chaining method in Kling 3.0 for the studio's next AI video production — XR demos, e-learning openers, or client promos.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/underwoodxie96/status/2061414477120016873" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@javilopen</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 792 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/javilopen/status/2061834346969882649">View @javilopen on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@bfl_ai Well, this meme didn't age well 😂😂😂 https://t.co/1X7xPrtg3U”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@javilopen posted a meme reaction at Black Forest Labs (@bfl_ai), implying a previous joke about the company or its image-gen models has been proven wrong by recent events.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/javilopen/status/2061834346969882649" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CCinephilia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 702 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CCinephilia/status/2061930091903332735">View @CCinephilia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Marty didn't just disappoint us; he betrayed the entire film community. Only a few hours passed, and it was already revealed that he was advising an AI company founded by the people who trained Stable”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Film director Martin Scorsese is advising an AI company co-founded by the team behind Stable Diffusion, which trained on copyrighted images without consent — drawing backlash from the film community.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CCinephilia/status/2061930091903332735" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aisearchio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 677 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aisearchio/status/2061572022074020174">View @aisearchio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bytedance drops an open-source Gemini Omni!!! Bernini is a new AI video generation + editing framework. &amp;gt; Edit videos with text prompts &amp;gt; Image/video references &amp;gt; Code available https://t.co/”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>ByteDance released Bernini, an open-source video generation and editing framework that accepts text prompts plus image/video references, with code publicly available.</dd>
      <dt>Why interesting</dt>
      <dd>Text-driven video editing with open weights cuts production time for e-learning clips and XR demo reels without requiring a dedicated video editor.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can run Bernini locally and test it against current e-learning or XR content production to see if it fits the asset pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aisearchio/status/2061572022074020174" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@xxunhuang</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 396 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/xxunhuang/status/2061939239915528653">View @xxunhuang on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm excited to announce that the Morpheus AI team is joining Roblox! Over the past two years, I’ve focused on developing the foundational architectures behind modern video world models, including Self”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Morpheus AI, the startup behind real-time interactive video world models Self Forcing and AR-DiT, has been acquired by Roblox to power 'Roblox Reality' — a project replacing pre-rendered assets with live generative world simulation.</dd>
      <dt>Why interesting</dt>
      <dd>Real-time generative world models are entering a production-scale game platform, closing the gap between AI video generation and live interactive engine simulation — directly relevant to Unity and XR projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team should monitor Roblox Reality's technical disclosures; their architecture choices will serve as a concrete reference for prototyping real-time generative environments in the studio's own game projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/xxunhuang/status/2061939239915528653" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ArtificialAnlys</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 323 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ArtificialAnlys/status/2061494719998546206">View @ArtificialAnlys on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NVIDIA's Cosmos 3 lands at #1 among open weights models in both Text to Image and Image to Video on the Artificial Analysis Leaderboards! Cosmos 3 is a family of omnimodal world models for Physical AI”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>NVIDIA Cosmos 3 (open weights, up to 64B params) ranks #1 on Artificial Analysis leaderboards for both Text-to-Image and Image-to-Video, using a unified autoregressive + diffusion Mixture-of-Transformers architecture.</dd>
      <dt>Why interesting</dt>
      <dd>Ranking #1 open weights for both image and video generation in a single model gives the studio a local pipeline for XR and e-learning visual assets without per-call API costs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a local test of Cosmos 3 Super for generating concept art or short video clips in XR/e-learning projects, noting prompts must be structured JSON, not plain text.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ArtificialAnlys/status/2061494719998546206" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
