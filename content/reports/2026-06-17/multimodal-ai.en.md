---
type: social-topic-report
date: '2026-06-17'
topic: multimodal-ai
lang: en
pair: multimodal-ai.th.md
generated_at: '2026-06-17T15:46:07+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 176
salience: 0.68
sentiment: mixed
confidence: 0.55
tags:
- multimodal-ai
- video-generation
- comfyui
- open-weights
- cost-efficiency
- vfx-pipeline
thumbnail: https://pbs.twimg.com/media/HK31G4lXcAAVteI.jpg
---

# Multimodal AI — 2026-06-17

## TL;DR
- ComfyUI open-model VFX pipelines are the strongest production signal: face swap via Florence 2 → SAM2 → WAN [19], de-aging via Flux 2 Klein → Wan 2.2 Fun Control [28], animated sky/atmosphere replacement [43], and face-paint-guided robotic compositing with Wan 2.2 Animate [6] — all described as temporally consistent and composable from open weights.
- ByteDance's Seedance 2.0 Mini (Dreamina) pushes cost/speed over fidelity, now powering CapCut with a claimed up to 2× speedup over Seedance 2.0 Fast [29][23][57]; CapCut also launched 'Director Mode' for AI filmmaking [34].
- Sora is reported to have earned only ~$2.1M over its life while costing 'millions a day,' framed as falling 'from number one to dead in six months' [45][11] — single-source, unverified, but consistent with a cost-over-hype narrative.
- Z.ai reportedly trains its stack on Huawei Ascend (no Nvidia), est. ~$25M, ~3 months behind leading models and ~90% cheaper per one commentator [16][10] — a China cost-stack claim, not independently confirmed.
- Midjourney to announce its first hardware project 6/17 6pm PT [2]; Grok Imagine Video 1.5 image-to-video shipped with faster generation [58]; Runway is now usable inside ChatGPT [17][59].

## What happened
The day's volume is dominated by image/video generation chatter, but the production-relevant core is narrow. ComfyUI workflows combining open models for VFX tasks recur: face replacement/de-aging [19][28], sky/atmosphere replacement [43], and stylized compositing with Wan 2.2 Animate [6], plus a local mini-PC running Flux + Mistral Small 3.2 [54]. On hosted video, ByteDance's Seedance 2.0 Mini is positioned around cost and speed and is integrated into CapCut [23][29][30][57], which also added a 'Director Mode' [34]. Other model news: Grok Imagine Video 1.5 [58], Runway embedded in ChatGPT [17][59], Kling 3.0 [48], Veo 3.1 and Nano Banana 2 referenced in stills/animatics workflows [27][39][40].

## Why it matters (reasoning)
Two forces converge for a studio like NDF DEV. First, the usable layer is shifting from closed demos to open-weight models orchestrated in ComfyUI [6][19][28][43] — these run locally, carry no per-seat fee, and produce temporally consistent edits suited to game cinematics, XR backplates, and edutech visuals. Second, the commercial signal (Sora's reported losses [45][11]; Seedance Mini and CapCut competing on cost/speed [23][29][30]; the China low-cost training claim [16]) points to price collapse as the real trend, not fidelity jumps [46][35]. Second-order effect: betting a pipeline on a single expensive closed API is fragile — Sora's reported six-month fall [45] is the cautionary case — while open WAN/Flux pipelines plus cheap hosted fallbacks (Seedance/Kling/Veo) give optionality. Talent moving toward 'real-world'/world models [13][15][20] suggests the next research wave targets physical/3D consistency, but nothing shippable on that front appears today.

## Possibility
Likely: continued price/speed competition among hosted video models (Seedance Mini, Kling 3.0, Veo 3.1, Grok Imagine) keeps driving per-clip cost down [23][29][58][48], making rough animatics cheap to iterate. Likely: ComfyUI remains the practical integration hub for open video/image models in production VFX [6][19][28][43]. Plausible: China non-Nvidia stacks narrow the cost gap as claimed [16][10], expanding affordable open options — but this rests on one commentator and is unconfirmed. Plausible: Midjourney hardware [2] is a consumer/creative device rather than anything studio-relevant; wait for the actual launch. Unlikely on today's evidence: a usable 3D/mesh/scene generation tool for game/XR pipelines — there is essentially no 3D signal in these items.

## Org applicability — NDF DEV
1) Pilot the ComfyUI VFX pipelines on a small internal asset (face swap/de-aging, sky/atmosphere replacement, Wan 2.2 motion transfer) using open WAN/Flux weights — low/med effort, local, no per-seat cost; fits edutech visuals and game cinematics [6][19][28][43]. 2) Run a cost/quality bake-off of Seedance 2.0 Mini vs Kling 3.0 vs Veo 3.1 for storyboard/animatic generation — low effort, hosted [23][27][29][48]. 3) Evaluate a local inference box (Flux + small LLM) for on-prem image gen if data-sensitivity or volume warrants — med effort [54]. 4) For voiceover in edutech, test the open Chatterbox (Resemble AI) against paid TTS before committing to subscriptions — low effort [60]. Skip: making any closed, expensive video app a core dependency (Sora economics [45]); affiliate 'free unlimited' platforms [27][42]; and the bookmark/tool-list posts [33][36][37][49] — no production value. Note: do not expect a 3D asset-gen solution from this batch; keep the current 3D pipeline.

## Signals to Watch
- ComfyUI as the integration layer for open video models (Florence 2/SAM2/WAN/Flux chains) — watch for stabilized, reusable templates [6][19][28][43].
- Cost/speed race in hosted video: Seedance 2.0 Mini + CapCut Director Mode vs Kling/Veo/Grok [29][34][48][58].
- China non-Nvidia training-cost claims (Z.ai on Huawei Ascend) — verify independently before relying on it [16][10].
- Talent shift toward 'real-world'/world models (ex-Meta, ex-xAI moves; video model journal club) as a leading indicator for 3D/physical consistency [13][15][20].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | foalymatripony | ^110806 c360 | [Holy shit. It’s fully Sora Ai](https://x.com/foalymatripony/status/2066952666031308979) |
| x | midjourney | ^4415 c513 | [Midjourney will be announcing its first hardware project tomorrow (Wednesday 6/1](https://x.com/midjourney/status/2066994481770213697) |
| x | Sigmaskibidi282 | ^1354 c6 | [@foalymatripony It's not ai but damn it does look like the average Sora ai Disne](https://x.com/Sigmaskibidi282/status/2067015976072425543) |
| x | javilopen | ^1201 c42 | [I'd forgotten about "Primer". The most complex movie I've ever seen. You know wh](https://x.com/javilopen/status/2066577399832097002) |
| x | c_valenzuelab | ^713 c171 | [Imagine waking up and realizing that your full time job entails using a digital ](https://x.com/c_valenzuelab/status/2066922813466779876) |
| x | 8bit_e | ^663 c23 | [Painted sections of my face with face paint and used them to guide where the AI ](https://x.com/8bit_e/status/2066907375894688183) |
| x | ShamiWeb3 | ^615 c126 | [This is what happens when World Cup energy meets e-commerce storytelling ⚽ Fast ](https://x.com/ShamiWeb3/status/2067048483279057062) |
| x | NapoleonBonabot | ^518 c15 | [Is it just me or does this look like Sora AI?](https://x.com/NapoleonBonabot/status/2067066960081223881) |
| x | EMostaque | ^496 c14 | [With the acquisition of @cursor_ai the AI run rate of $SPCX will actually go abo](https://x.com/EMostaque/status/2066856395463344526) |
| x | EMostaque | ^457 c40 | [I think it's increasingly clear that if Chinese AI labs can get enough compute t](https://x.com/EMostaque/status/2067208860020924573) |
| x | signulll | ^411 c20 | [the entire sora chase kinda cost openai twice. on the supply side it bled comput](https://x.com/signulll/status/2066665563150237834) |
| x | Rogito211 | ^408 c0 | [@ToonHive You could tell me this is Sora Ai and I’d believe you](https://x.com/Rogito211/status/2067042901758976378) |
| x | _rohitgirdhar_ | ^406 c24 | [After almost 7 incredible years at Meta, I’m excited to share that I’ll be joini](https://x.com/_rohitgirdhar_/status/2066846769204347142) |
| x | strawbrrysugrr | ^383 c1 | [@foalymatripony so no this is just disney’s style lately, sora stole it because ](https://x.com/strawbrrysugrr/status/2067019746688581933) |
| x | zeeshanp_ | ^379 c16 | [Personal update: I joined @PrometheusInc six months ago to help build the Artifi](https://x.com/zeeshanp_/status/2066616272230760503) |
| x | EMostaque | ^379 c19 | [Important to note @Zai_org train on @Huawei Ascend chips, no NVIDA (!) So you ha](https://x.com/EMostaque/status/2067208281727054123) |
| x | runwayml | ^354 c35 | [Use Runway inside ChatGPT to generate and edit video and images. No tab-switchin](https://x.com/runwayml/status/2066596138824696214) |
| x | EMostaque | ^324 c56 | [At what valuation of SpaceX does Elon merge Tesla into it?](https://x.com/EMostaque/status/2066829123754799194) |
| x | ComfyUI | ^322 c9 | [Face Replacement and De-aging Demo: VFX artist @heydoughogan built a fully autom](https://x.com/ComfyUI/status/2066635313062277337) |
| x | DengHokin | ^310 c3 | [I am super excited to share that I launch a weekly Video Model Journal Club. Eve](https://x.com/DengHokin/status/2066692387397927329) |
| x | probnstat | ^306 c4 | [The Calculus of Randomness: How Itô's Integral Tamed the Chaos of the Universe T](https://x.com/probnstat/status/2066612639049101355) |
| x | fabianstelzer | ^286 c60 | [a really strange behaviour I'm observing with many high end Chinese models is se](https://x.com/fabianstelzer/status/2067146927058124952) |
| x | AIwithJessica | ^277 c27 | [The next wave of AI video isn't about bigger demos, it's about faster production](https://x.com/AIwithJessica/status/2066731121354977703) |
| x | mdmadeit | ^257 c33 | [Azuki Zanbato Dance Made with midjourney, chatgpt and seedance Prompt on the nex](https://x.com/mdmadeit/status/2066722279376195963) |
| x | EMostaque | ^255 c28 | [are they going to rename it CodeX](https://x.com/EMostaque/status/2066989372017090669) |
| x | AleRVG | ^252 c19 | [💡One of the biggest issues I’ve faced with short-form video is the constant repe](https://x.com/AleRVG/status/2066871328263574014) |
| x | Atenov_D | ^242 c26 | [FREE 1 month Plus subscription. Seedance 2.0, Kling 3.0, Veo 3.1, WAN. No card, ](https://x.com/Atenov_D/status/2066905977278886246) |
| x | ComfyUI | ^234 c4 | [Creator lecovictor ( IG ) built this workflow to explore what's possible at the ](https://x.com/ComfyUI/status/2066947693629608183) |
| x | zahra4sure | ^213 c43 | [CapCut’s new AI video update is a big one for anyone who moves fast. With Dreami](https://x.com/zahra4sure/status/2066803186267312219) |
| x | DoctorAmna11 | ^209 c34 | [CapCut’s new AI video update is a good reminder that the best tool is not always](https://x.com/DoctorAmna11/status/2066808807326400704) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@foalymatripony</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 110806 · 💬 360</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/foalymatripony/status/2066952666031308979">View @foalymatripony on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Holy shit. It’s fully Sora Ai”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user reacts to something involving Sora AI with a one-line exclamation, providing no description of what changed, what was shown, or what version/feature is involved.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/foalymatripony/status/2066952666031308979" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4415 · 💬 513</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2066994481770213697">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Midjourney will be announcing its first hardware project tomorrow (Wednesday 6/17) at 6pm PT. Stay tuned for a livestream of our in-person launch event in San Francisco. If you're in town and want an ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney is unveiling its first hardware product at a live San Francisco event today, June 17, at 6 pm PT, with a public livestream.</dd>
      <dt>Why interesting</dt>
      <dd>Midjourney entering physical hardware signals a new category — likely creative or spatial-computing tooling — directly adjacent to XR/VR and AI-asset workflows.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Watch the 6 pm PT livestream today to judge whether the hardware fits the studio's XR/VR or AI-asset pipeline before making any procurement decision.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2066994481770213697" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Sigmaskibidi282</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1354 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Sigmaskibidi282/status/2067015976072425543">View @Sigmaskibidi282 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@foalymatripony It's not ai but damn it does look like the average Sora ai Disney style video”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user comments that a video resembles Sora-style Disney AI output, but confirms it is not AI-generated.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Sigmaskibidi282/status/2067015976072425543" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@javilopen</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1201 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/javilopen/status/2066577399832097002">View @javilopen on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'd forgotten about &quot;Primer&quot;. The most complex movie I've ever seen. You know when people say, &quot;Let me draw you a diagram&quot;? Well, this movie is so complicated it actually needs one. It's going to blow”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user recommends the film 'Primer' (2004 sci-fi about time travel) as exceptionally complex, noting it requires a diagram to follow.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/javilopen/status/2066577399832097002" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@c_valenzuelab</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 713 · 💬 171</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/c_valenzuelab/status/2066922813466779876">View @c_valenzuelab on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Imagine waking up and realizing that your full time job entails using a digital cinema camera with a 65mm large format CMOS sensor fabricated on a sub-20nm semiconductor process, capturing 16-bit line”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@c_valenzuelab argues that pro cinema pipelines already embed ML denoising, NeRF, optical flow, and photogrammetry — making 'AI imagery is brand new' a historically uninformed position.</dd>
      <dt>Why interesting</dt>
      <dd>The exact tech stack named — NeRF, photogrammetry, LiDAR, ML denoising, PBR — maps directly to XR/VR and Unity asset production workflows.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Use this framing when clients push back on AI tools — the same techniques have been standard in professional visual production for years.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/c_valenzuelab/status/2066922813466779876" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@8bit_e</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 663 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/8bit_e/status/2066907375894688183">View @8bit_e on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Painted sections of my face with face paint and used them to guide where the AI effect would appear. Using Wan 2.2 Animate in ComfyUI, I turned those areas into a robotic endoskeleton while leaving mu”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A creator used face paint as a physical region mask in ComfyUI (Wan 2.2 Animate) to apply AI robotic VFX only to painted areas, leaving surrounding live footage untouched.</dd>
      <dt>Why interesting</dt>
      <dd>Physical paint as a spatial control signal replaces rotoscoping — selective AI compositing with no software masking overhead, directly applicable to previs and XR concept work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can trial this face-paint masking method in ComfyUI for XR or previs shots where selective AI VFX on live footage is needed without a full rotoscoping pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/8bit_e/status/2066907375894688183" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ShamiWeb3</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 615 · 💬 126</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ShamiWeb3/status/2067048483279057062">View @ShamiWeb3 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is what happens when World Cup energy meets e-commerce storytelling ⚽ Fast lifestyle cuts and stadium-level football energy shaping a premium Speedcat OG Pelé Yellow – PUMA Black film. From handh”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A creator built a full PUMA shoe commercial using GPT Image 2 + Seedance 2.0 video generation via EaseMate AI, mixing UGC-style handheld cuts with macro product shots and a hero goal sequence.</dd>
      <dt>Why interesting</dt>
      <dd>The GPT Image 2 + Seedance 2.0 pipeline now produces broadcast-quality commercial video from prompts alone — a practical option for studio game trailers or client product campaigns.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a test campaign clip for a studio game or internal project through EaseMate AI to benchmark GPT Image 2 + Seedance 2.0 output quality and cost before pitching it to clients.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ShamiWeb3/status/2067048483279057062" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NapoleonBonabot</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 518 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NapoleonBonabot/status/2067066960081223881">View @NapoleonBonabot on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Is it just me or does this look like Sora AI?”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user posts a vague question asking whether some unspecified visual resembles Sora AI output, with no image, context, or factual claim provided.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NapoleonBonabot/status/2067066960081223881" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
