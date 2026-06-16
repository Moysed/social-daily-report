---
type: social-topic-report
date: '2026-06-12'
topic: multimodal-ai
lang: en
pair: multimodal-ai.th.md
generated_at: '2026-06-12T15:48:11+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 154
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- multimodal-ai
- video-generation
- comfyui
- open-weights
- production-pipeline
- midjourney
thumbnail: https://pbs.twimg.com/media/HKi1tA1XgAAF1Qp.jpg
---

# Multimodal AI — 2026-06-12

## TL;DR
- ComfyUI is consolidating as an open production-pipeline hub: workflows now generate utility passes/mattes from footage with no manual rotoscoping [4], turn a raw Playblast into a finished shot via Seedance 2.0 [18], and auto-build bounding-box + structured-JSON prompts from an uploaded image [14].
- Open/affordable video models advanced: LTX 2.3 added Multiple Subject Reference (up to 5 images, e.g. 2 characters + background without face-mixing) [35]; India's Varya (Avataar) markets text-to-video at $0.01 per second of video [38].
- Midjourney made V8.1 the default for all users, will deprecate V8 in ~2 weeks, and has V8.2 in testing [9]; separately a claim says ~19M of 20M registered users churned after the free tier ended, leaving ~1M paying [21].
- Runway deepened its Lionsgate partnership with a joint program to develop original IP [7][27] and ran a sold-out NYC AI Festival featuring Ron Howard [32][44].
- Small specialist multimodal models appeared: LiquidAI trained a tiny model to extract any image's contents into JSON (receipts, product photos) [59].

## What happened
Most of today's high-engagement items are X posts; signal is concentrated in tooling and model releases rather than papers or benchmarks. On the open side, ComfyUI workflows demonstrated production utility passes/mattes generated from footage [4], a Playblast-to-finished-shot pipeline using Seedance 2.0 [18], LLM-driven bounding-box JSON prompting from an image [14], and in-progress audio generation [58]. LTX 2.3 added multi-subject referencing across up to 5 images [35], and a small LiquidAI model extracts image contents to JSON [59]. On the hosted/closed side, Midjourney shifted defaults to V8.1 with V8 deprecation and V8.2 testing [9], Runway expanded its Lionsgate studio partnership [7][27] and held its 4th AI Festival [32][44], and HeyGen showed an AI agent provisioning and paying for its video API via Stripe [29]. Several items push UGC-ad volume claims (Kling 3.0, ~550 videos/day at ~$1) [17][28][53] and unverified rumors of a new cheaper Seedance/Dreamina model and broad price cuts [30][42][52]. A separate claim touts a text-diffusion 'DiffusionGemma-26B' running in llama.cpp [5]. A large share of the feed is tool-listicle spam [23][25][31][39][50][51][55][56][60] and creator-monetization anecdotes [6][22][53], which carry little technical signal.

## Why it matters (reasoning)
The usable trend for a studio is the maturing open ComfyUI pipeline: matte/roto extraction [4], turning 3D Playblasts into rendered shots [18], and structured-JSON prompting [14] map directly onto game cinematics, XR scene dressing, and edutech visuals without a closed black-box dependency. Multi-subject referencing [35] and image-to-JSON extraction [59] address two recurring production pains — character/asset consistency and tagging reference material into structured data. The Midjourney churn figure [21], if accurate, is a second-order warning: pipelines built on a single closed tool with shifting tiers and forced model deprecation [9] carry continuity risk, which is why open weights or stable low-cost APIs (Varya at $0.01/s [38]) are the safer foundation for repeatable client work. The Runway–Lionsgate IP program [7][27] and recurring copyright reminders [12] signal that the commercial bottleneck for AI video is increasingly rights/licensing, not raw model quality — relevant whenever generated assets ship in client deliverables. The HeyGen+Stripe agentic provisioning demo [29] hints at API consumption moving toward autonomous, metered usage.

## Possibility
Likely: ComfyUI keeps absorbing production steps (roto, render, prompting, audio) and remains the default open hub for studio pipelines [4][18][14][58]. Likely: continued downward pressure on hosted video pricing as new entrants undercut on cost [38] and rumors point to cheaper Seedance variants [30][42][52] — though the specific rumor and 'price cuts' framing are unverified and should be treated as plausible at best. Plausible: open-weight video models (LTX line) close the consistency gap with closed tools via multi-reference features [35], making them viable for repeatable character work. Plausible: more studio–lab IP deals follow Runway/Lionsgate as rights become the gating factor [7][27]. Unlikely (as stated): the 'DiffusionGemma-26B' text-diffusion claim [5] and the '550 videos/day, $1, fully realistic' UGC claims [17][28] hold up at the quality and scale advertised without significant caveats — treat as marketing until independently reproduced. No source gives numeric probabilities, so none are asserted here.

## Org applicability — NDF DEV
1) Stand up a ComfyUI evaluation pipeline and test the matte/utility-pass [4] and Playblast-to-shot [18] workflows against a real Unity/3D scene — med effort; this is the most directly applicable item for game cinematics and XR. 2) Trial the image→structured-JSON workflow [14] and LiquidAI's image-to-JSON model [59] for asset tagging and for extracting structured data from reference images/receipts inside web/mobile app features — low effort. 3) Test LTX 2.3 multi-subject reference [35] for character/scene consistency in edutech visuals before committing to any closed tool — low/med effort. 4) Track Varya [38] and Kling [17] pricing as candidate affordable hosted video APIs, but validate quality yourself rather than trusting volume/cost claims — low effort. 5) Add an IP/rights checklist for any AI-generated video or asset in client deliverables, given the Lionsgate licensing trend and copyright reminders [7][27][12] — low effort. Skip: the AI-tool listicle threads [23][25][31][39][50][51][55][56][60] and creator-monetization anecdotes [6][22][53] (no technical signal); avoid making Midjourney a single point of failure given forced V8 deprecation and tier churn [9][21]; do not act on the DiffusionGemma [5] or Seedance/Dreamina [30][42][52] rumors until weights/benchmarks exist.

## Signals to Watch
- ComfyUI feature expansion — roto/matte, Seedance render, JSON prompting, audio — as the open studio pipeline backbone [4][18][14][58].
- Seedance/Dreamina new-model + price-cut rumors [30][42][52]; watch for actual open weights or a published API price.
- Midjourney V8.2 testing and V8 deprecation in ~2 weeks [9] — plan migrations if any pipeline depends on it.
- Agentic API provisioning and metered pay-per-generation (HeyGen + Stripe) [29] as a model for how AI video gets consumed.

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | tan_stack | ^795 c30 | [TanStack AI is now in Beta! TanStack AI is no longer just a text-generation libr](https://x.com/tan_stack/status/2065102675390189916) |
| x | Suhail | ^603 c18 | [Priorities for high agency people are almost always communicated by the latency ](https://x.com/Suhail/status/2065127494014120056) |
| x | ashay_sewlall | ^453 c10 | [Some core memories deserve to be more than a picture 🥹⚽️ The HONOR 600 Pro AI Im](https://x.com/ashay_sewlall/status/2064742373624562074) |
| x | ComfyUI | ^372 c8 | [Mattes and Utilities Demo: VFX artist @heydoughogan breaks down a ComfyUI workfl](https://x.com/ComfyUI/status/2064804378457096621) |
| x | analogalok | ^348 c18 | [Auto regressive LLMs are officially on notice. run Gemma 4 26B diffusion gguf wi](https://x.com/analogalok/status/2064865717875618057) |
| x | 0xJamino | ^342 c12 | [She uploads cartoons made by AI and pulls in $11,000 a month doing it Most peopl](https://x.com/0xJamino/status/2064775551613596066) |
| x | runwayml | ^314 c41 | [Today, we’re deepening our partnership with Lionsgate with a slate of new initia](https://x.com/runwayml/status/2065072377596088525) |
| x | gurniaiart | ^288 c0 | [Knight art #AIArt #AIイラスト #midjourney #AIgirl #knight #aiGallery https://t.co/20](https://x.com/gurniaiart/status/2065067622610145360) |
| x | midjourney | ^267 c27 | [We've made V8.1 the new default model for all users on Midjourney. V8 will now b](https://x.com/midjourney/status/2064921117618557292) |
| x | McSolsy | ^253 c2 | [Me lowkey adding the sora ai watermark to footage of clown dropping in the final](https://x.com/McSolsy/status/2064765277829484665) |
| x | bull_bnb | ^233 c33 | [AI data was big because models needed the internet. Robot data will be bigger be](https://x.com/bull_bnb/status/2065131071252103412) |
| x | Gravantus | ^217 c2 | [&gt;Fan made &gt;worth billions IP copyright doesn't magically go away with the ](https://x.com/Gravantus/status/2064890176783179825) |
| x | icreatelife | ^214 c307 | [Post your art. No words. Only your art.](https://x.com/icreatelife/status/2065057837307265480) |
| x | hellorob | ^200 c6 | [The only thing worse than looking at a blank canvas is prompting with JSON. Here](https://x.com/hellorob/status/2065209723184676973) |
| x | Suhail | ^193 c13 | [I’ve enjoyed this prompt for learning more than I thought I would: Teach me this](https://x.com/Suhail/status/2065103647848157369) |
| x | AvelyrahnAI | ^178 c24 | [Created with GPT Image 2 on Chatgpt Prompt: Create image Here's a cleaner, optim](https://x.com/AvelyrahnAI/status/2065383336722493531) |
| x | FynCas | ^168 c90 | [MakeUGC & Kling 3.0 = 550 videos/day Fully realistic UGC ads — cinematic lightin](https://x.com/FynCas/status/2065071656100298813) |
| x | ComfyUI | ^165 c6 | [Seedance Playblast 2 Render Demo: VFX artist @heydoughogan built a workflow in C](https://x.com/ComfyUI/status/2065217065490034775) |
| x | Endory2 | ^163 c5 | [KH4 sora is weirdly AI Upscaled btw. KH4 does not look like this. And I am not t](https://x.com/Endory2/status/2065176708836217258) |
| x | Tanaypawar27 | ^156 c31 | [Best accounts to follow from each frontier lab to stay constantly up to date Ant](https://x.com/Tanaypawar27/status/2064920550418645252) |
| x | ekinoks_26 | ^154 c161 | [Midjourney has 20 million registered users. Roughly 1 million pay. The other 19 ](https://x.com/ekinoks_26/status/2064950762715951536) |
| x | sunaiuse | ^153 c26 | [1 guy in China made $1,000,000 last year. No employees. No code. Just AI and a v](https://x.com/sunaiuse/status/2065183221135069232) |
| x | Alexie_Ai | ^151 c28 | [120 + Mind blowing AI tools 🔥 1. Ideas - Claude - ChatGPT - Bing Chat - Perplexi](https://x.com/Alexie_Ai/status/2064759650252382593) |
| x | treyisforever | ^150 c0 | [@cihywastaken @ctrlkugi ai image generation has been around publicly since 2020 ](https://x.com/treyisforever/status/2065118866943176709) |
| x | Bhanusinghyede | ^144 c21 | [🚀 𝟏𝟐𝟎 𝐌𝐢𝐧𝐝-𝐁𝐥𝐨𝐰𝐢𝐧𝐠 𝐀𝐈 𝐓𝐨𝐨𝐥𝐬 𝐘𝐨𝐮 𝐒𝐡𝐨𝐮𝐥𝐝 𝐊𝐧𝐨𝐰 𝐢𝐧 𝟐𝟎𝟐𝟔 Most people know 5–10 tools…](https://x.com/Bhanusinghyede/status/2065036535645470797) |
| x | javilopen | ^136 c13 | [I made this map 28 years ago for Quake II. I found it buried in some random fold](https://x.com/javilopen/status/2065004162950046178) |
| x | c_valenzuelab | ^135 c17 | [Excited to announce that we’re expanding our partnership with Lionsgate through ](https://x.com/c_valenzuelab/status/2065081068630282541) |
| x | spwfeijen | ^134 c72 | [Kling 3.0 = 550 videos per day Fully-realistic UGC ads — cinematic lighting, hum](https://x.com/spwfeijen/status/2065056560154370451) |
| x | HeyGen | ^133 c32 | [Your AI agent can now add HeyGen to its own stack. With @Stripe Projects, it fin](https://x.com/HeyGen/status/2064729845767290940) |
| x | UrMeer289 | ^128 c12 | [There's a massive rumor circulating the AI space right now that Dreamina is abou](https://x.com/UrMeer289/status/2065090149093126267) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@tan_stack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 795 · 💬 30</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/tan_stack/status/2065102675390189916">View @tan_stack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“TanStack AI is now in Beta! TanStack AI is no longer just a text-generation library with extras bolted on. TanStack AI has first-class dev experience for: ✅ Text and Streaming Structured Data ✅ Tool C”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>TanStack AI entered Beta covering text, structured streaming, tool calls, image/video/audio generation, realtime voice, host-side MCP, and orchestration — with per-model TypeScript type-safety.</dd>
      <dt>Why interesting</dt>
      <dd>Teams already using TanStack Query or Router get a type-safe, framework-native path to multimodal AI without switching to a separate SDK like Vercel AI SDK.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Benchmark TanStack AI Beta against Vercel AI SDK for the studio's next AI-integrated web project, particularly if it already uses TanStack Query or Router.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/tan_stack/status/2065102675390189916" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Suhail</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 603 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Suhail/status/2065127494014120056">View @Suhail on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Priorities for high agency people are almost always communicated by the latency of their response.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Author @Suhail observes that high-agency people signal their priorities through how fast they respond to messages.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Suhail/status/2065127494014120056" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ashay_sewlall</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 453 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ashay_sewlall/status/2064742373624562074">View @ashay_sewlall on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Some core memories deserve to be more than a picture 🥹⚽️ The HONOR 600 Pro AI Image to Video 2.0 feature will let me relive my MOTM winning moment ❤️ Which memory would you want to relive? @HONORZA #H”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Influencer promotes HONOR 600 Pro's AI Image-to-Video 2.0 feature using a personal soccer highlight as the example use case.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ashay_sewlall/status/2064742373624562074" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ComfyUI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 372 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ComfyUI/status/2064804378457096621">View @ComfyUI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mattes and Utilities Demo: VFX artist @heydoughogan breaks down a ComfyUI workflow that generates production-ready utility passes directly from your footage. No manual rotoscoping. No guesswork. What'”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>ComfyUI's demo workflow by VFX artist @heydoughogan auto-generates background removal, SAM3 segmentation, face mattes, depth, and normal passes from source footage — all at native resolution inside one graph.</dd>
      <dt>Why interesting</dt>
      <dd>Depth and normal passes generated directly from footage replace manual extraction steps and feed straight into CG relighting pipelines — relevant for any Unity or XR production with mixed media.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity/XR team can pull this ComfyUI workflow to generate depth and normal passes from reference footage for CG asset integration and in-engine relighting work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ComfyUI/status/2064804378457096621" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@analogalok</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 348 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/analogalok/status/2064865717875618057">View @analogalok on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Auto regressive LLMs are officially on notice. run Gemma 4 26B diffusion gguf with llama.cpp Google just dropped DiffusionGemma-26B, and it completely flips how we generate text. instead of predicting”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google released DiffusionGemma-26B, a diffusion-based LLM that generates 256 tokens in parallel via bi-directional attention instead of autoregressive next-token prediction; its MoE architecture activates only 3.8B params at inference, fitting on a single RTX 3090 with Q4_K_M quant at ~18GB VRAM.</dd>
      <dt>Why interesting</dt>
      <dd>Parallel token generation with on-the-fly self-correction is a fundamentally different inference path — if throughput holds up, it changes cost/latency math for local LLM use in the studio's tools.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Any team member with an RTX 3090/4090 can benchmark DiffusionGemma-26B via the llama.cpp diffusiongemma branch against the current local model to compare speed and output quality on real prompts.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/analogalok/status/2064865717875618057" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@0xJamino</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 342 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/0xJamino/status/2064775551613596066">View @0xJamino on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“She uploads cartoons made by AI and pulls in $11,000 a month doing it Most people grind a second job. She did the opposite. Found a viral channel like Doggyland and reverse engineered the format. Chat”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A creator uses ChatGPT + Picsart Flow (Sora 2) to generate 4K AI-animated cartoon clips daily, reaching $11K/month in YouTube Kids ad revenue within six months.</dd>
      <dt>Why interesting</dt>
      <dd>Sora 2 via Picsart Flow now produces broadcast-quality animated content at near-zero marginal cost per clip — directly applicable to e-learning animation and short-form game trailers.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a quick test of the ChatGPT → Picsart Flow pipeline to prototype animated explainer segments for an e-learning module before committing to full production.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/0xJamino/status/2064775551613596066" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@runwayml</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 314 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/runwayml/status/2065072377596088525">View @runwayml on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Today, we’re deepening our partnership with Lionsgate with a slate of new initiatives, including a joint development program focused on creating original IP together. Learn more at the link below. htt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Runway ML and Lionsgate are expanding their partnership to co-develop original IP, moving beyond tool licensing into joint creative production.</dd>
      <dt>Why interesting</dt>
      <dd>A major Hollywood studio co-creating IP with an AI video company confirms AI-generated video is now production-grade, not just experimental.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can trial Runway for game cinematic production or XR pre-visualization to reduce outsourced video costs.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/runwayml/status/2065072377596088525" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gurniaiart</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 288 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gurniaiart/status/2065067622610145360">View @gurniaiart on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Knight art #AIArt #AIイラスト #midjourney #AIgirl #knight #aiGallery https://t.co/20cs9inIha”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An artist posted AI-generated knight artwork on X using Midjourney, tagged as #AIArt and #AIイラスト.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gurniaiart/status/2065067622610145360" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
