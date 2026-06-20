---
type: social-topic-report
date: '2026-06-20'
topic: multimodal-ai
lang: en
pair: multimodal-ai.th.md
generated_at: '2026-06-20T03:43:47+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 206
salience: 0.58
sentiment: mixed
confidence: 0.5
tags:
- multimodal-ai
- video-generation
- comfyui
- open-weights
- image-editing
- midjourney
thumbnail: https://pbs.twimg.com/media/HLEKRTNW4AAiGWG.jpg
---

# Multimodal AI — 2026-06-20

## TL;DR
- Midjourney announced 'Midjourney Medical,' a full-body ultrasonic scanner (~358,000 on-chip transducers, water bath, ~60s, no radiation) — but it is hardware that reportedly contains no AI yet [12][52][23], not a multimodal-AI release despite dominating today's engagement.
- Real production-pipeline signal: an NVIDIA Studio + ComfyUI + LTX pipeline renders full CG shorts locally and free on your own GPU [21], with another ComfyUI workflow rebuilding video from a drummer's real motion-capture data [19].
- ByteDance shipped Dreamina Seedance 2.0 (mini) for AI video; creators are running same-prompt head-to-heads against Kling 3.0 [26][45][46].
- Open weights moved: 'Boogu Image Edit,' a 10B open-source image edit/gen model, appeared on Hugging Face [50]; Adobe shipped a context-aware, text-driven Photoshop AI Assistant [42]; a ComfyUI stack cites Wan 2.2 I2V/T2V, Krea 2, GPT Image 2.0 and Florence2 [16].
- Midjourney reports ~$100M revenue in its first 9 months and ~$200M by month 12, fully community-funded, with image-gen revenue funding its R&D [6].

## What happened
Today's feed splits into two clusters. By raw engagement the dominant story is Midjourney's 'Midjourney Medical' division and its full-body ultrasonic scanner — water instead of radiation, ~358,000 transducers, ~60-second scan claiming MRI-like images [12][34][47][51]. This is medical hardware, not generative AI: one item notes it 'doesn't even have AI in it at all' [52], and another found no hard performance data [23]. Separately, Midjourney's image business is cited as community-funded with ~$100M in 9 months [6].

The genuinely on-topic multimodal-AI items are tool and model releases: an NVIDIA Studio-backed local ComfyUI + LTX pipeline for free on-GPU CG rendering [21]; a motion-data-driven ComfyUI video rebuild [19]; ByteDance's Dreamina Seedance 2.0 mini with Kling 3.0 comparisons [26][45][46]; the open 10B 'Boogu Image Edit' model on Hugging Face [50]; Adobe's Photoshop AI Assistant [42]; Google Vids AI-avatar enhancements [10]; and a working stack listing Wan 2.2, Krea 2, GPT Image 2.0, Grok Image, Florence2 and Suno [16]. Open-vs-closed model debate runs through several posts referencing a 'Fable' frontier model and Chinese open models [17][41][7][49].

## Why it matters (reasoning)
The signal that matters for a production studio is the consolidation of open and local video/image pipelines, not the medical hype. A free, local LTX+ComfyUI render path [21] plus open weights like Boogu [50] and Wan 2.2 [16] reduces per-asset cost and removes dependence on closed APIs and per-seat pricing — directly relevant to generating game, XR and edutech visuals at volume with licensing control. The Seedance 2.0 vs Kling 3.0 face-offs [26][46] indicate hosted video quality is now decided by side-by-side feel rather than spec sheets, so model choice should be tested on your own prompts. The Midjourney medical pivot, by contrast, is a second-order effect: a profitable image business [6] funding unrelated hardware bets [4][48], which absorbs attention but does not change any creative pipeline. Treat the surrounding 'new era' framing [15][27][36] as marketing, especially given the lack of validated data [23] and that the device may not even use AI [52].

## Possibility
Likely: open and local image/video tooling keeps improving and competing closely — ComfyUI+LTX local rendering [21], Wan 2.2 [16], and open editors like Boogu [50] suggest a steady stream of usable open weights. Plausible: a Chinese open model matches or beats the closed 'Fable'-class frontier on benchmarks and feel [17][41], which would favor studios that build on swappable open models. Plausible: hosted video pricing keeps falling as Seedance and Kling compete [26][45][46], though the '$1 per video, 5 ads in 5 minutes' figure [33] is vendor marketing and unverified. Unlikely to matter to NDF DEV: the Midjourney medical scanner becoming relevant to any creative pipeline — it is unproven hardware with no published data [23][52]. No source gives credible numeric probabilities, so none are asserted here.

## Org applicability — NDF DEV
Do: (1) Pilot the local ComfyUI + LTX render pipeline on a studio GPU for XR-scene and edutech visual asset generation [21] — effort med. (2) Run a same-prompt bake-off of Dreamina Seedance 2.0 vs Kling 3.0 for short marketing/edutech clips before committing to either API [26][46] — effort low. (3) Test the open 10B Boogu image-edit model for iterative asset edits where weights/licensing control matters [50] — effort low/med. (4) Add Wan 2.2 I2V/T2V to an internal ComfyUI workflow for open text/image-to-video [16] — effort med. (5) Trial Google Vids AI avatars for e-learning talking-head explainers [10], and the Photoshop AI Assistant for context-aware batch edits [42] — effort low. Skip: the Midjourney Medical scanner [12][52], the 'Fable' ban/DeepMind-discontent rumors [49][7] (unverified), and any cost/speed math taken at face value from promo threads [33].

## Signals to Watch
- Seedance 2.0 vs Kling 3.0 quality and price gap as creators publish more direct comparisons [46].
- Maturity of local-first rendering (LTX + ComfyUI + NVIDIA Studio) replacing hosted spend [21].
- Cadence of open-weight image editors landing on Hugging Face, e.g. Boogu 10B [50].
- Whether a Chinese open model reaches the closed 'Fable'-class frontier on feel, not just benchmarks [17][41].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | afshineemrani | ^9168 c307 | [I'm a cardiologist. Something just happened today that I genuinely did not see c](https://x.com/afshineemrani/status/2067630924108538083) |
| x | amazingzeros | ^7445 c19 | [sonic fan pissing their pants about fortnite as if sora ai getting deleted didn’](https://x.com/amazingzeros/status/2067666616700334555) |
| x | midjourney | ^4644 c886 | [We're gonna do a Midjourney Medical AMA (ask me anything ) right here all aftern](https://x.com/midjourney/status/2067688872944025975) |
| x | aakashgupta | ^3811 c110 | [Let me explain why an AI art company just built a full-body medical scanner, bec](https://x.com/aakashgupta/status/2067579580622528913) |
| x | levelsio | ^3762 c109 | [I don't know if it's obvious information or not but if you talk to random people](https://x.com/levelsio/status/2067662326082498899) |
| x | nickfloats | ^3633 c94 | [What Midjourney is: - No investors, fully community-funded research lab - Revenu](https://x.com/nickfloats/status/2067445022484529282) |
| x | synthwavedd | ^2486 c148 | [🚨 SCOOP: After the release of Fable 5 and with GPT-5.6 looming, the mood behind ](https://x.com/synthwavedd/status/2068000857757741251) |
| x | cignificants | ^1884 c14 | [so hey, aside from midjourney and gemini what other generative AI program do you](https://x.com/cignificants/status/2067644406728135033) |
| x | Prolotario1 | ^1816 c126 | [Quite The Eventful Day It Has Been: New Air Force 1 New GTA 6 Promo New Midjourn](https://x.com/Prolotario1/status/2067768517613551818) |
| x | ChanduThota | ^1431 c48 | [Video is an effective way to communicate, and we want to make it as easy as edit](https://x.com/ChanduThota/status/2067631530890113477) |
| x | matt_is_nice | ^1027 c43 | [Everyone arguing about whether the Midjourney Scanner can replace an MRI or CT i](https://x.com/matt_is_nice/status/2067796547400814608) |
| x | AdrianDittmann | ^1018 c72 | [This is so cool! Midjourney Medical built a full body Ultrasonic CT scanner. You](https://x.com/AdrianDittmann/status/2067574011626946587) |
| x | dcbruck | ^799 c15 | [0 VC funding. $500M(+) in revenue. Less than 200 employees. And now they're rein](https://x.com/dcbruck/status/2067599482519216293) |
| x | BrianRoemmele | ^763 c52 | [Electronic Medicine is the future: Sound waves vs. Radiation. Currents and frequ](https://x.com/BrianRoemmele/status/2067619864370634919) |
| x | pronounced_kyle | ^760 c23 | [I'm calling it: this is the start of a new era in tech. First tangible example o](https://x.com/pronounced_kyle/status/2067595725404590439) |
| x | ingi_erlingsson | ^595 c16 | [take the wheel 🏁 make: ComfyUI, After Effects, Photoshop model: Wan 2.2 I2V + T2](https://x.com/ingi_erlingsson/status/2067756997756256650) |
| x | EMostaque | ^526 c121 | [How would you change your priors if a Chinese lab released an open model that be](https://x.com/EMostaque/status/2067610502826463409) |
| x | fabianstelzer | ^503 c23 | [this will be such a great movie. how do you even steal a EUV machine? https://t.](https://x.com/fabianstelzer/status/2067907362329907275) |
| x | ComfyUI | ^413 c8 | [Most AI video work is just "generate and hope." This is different. Creator seung](https://x.com/ComfyUI/status/2067669239033717141) |
| x | javilopen | ^388 c43 | [Why didn't they call me to name this? What a wasted opportunity to call it... ME](https://x.com/javilopen/status/2067926942238540049) |
| x | mickmumpitz | ^382 c10 | [Paid partnership with @NVIDIAStudio - You can now render entire CG movies with l](https://x.com/mickmumpitz/status/2067976421687881962) |
| x | arian_ghashghai | ^359 c17 | [reminder that Midjourney has 0 VC funding imo this is maybe the most utopian swi](https://x.com/arian_ghashghai/status/2067616613507923983) |
| x | heacockmd | ^344 c46 | [Apparently, yesterday @midjourney pivoted from AI image generation to...whole bo](https://x.com/heacockmd/status/2067638397804441634) |
| x | fofrAI | ^343 c23 | [Entrance to the new Midjourney spa https://t.co/vsnEIjM36P](https://x.com/fofrAI/status/2067635885370126556) |
| x | MTSlive | ^297 c6 | [Why is the Midjourney team uniquely qualified to build medical hardware? @BeffJe](https://x.com/MTSlive/status/2067757811191447659) |
| x | redchilli50 | ^269 c41 | [Wondering how to unlock Dreamina Seedance 2.0 mini right inside Dreamina? 🧵 A ra](https://x.com/redchilli50/status/2067505955814686786) |
| x | DeryaTR_ | ^257 c14 | [I think many people have realized what a revolutionary medical advance the Midjo](https://x.com/DeryaTR_/status/2067598405069591012) |
| x | icreatelife | ^257 c119 | [I’m following 3,700 AI pioneers and I’d love to follow 300 more, to make it a ro](https://x.com/icreatelife/status/2067728865808519355) |
| x | dreamingtulpa | ^254 c13 | [still can't get over how beautiful some of these shots are and the soundtrack 👌 ](https://x.com/dreamingtulpa/status/2067880684920643956) |
| x | KevInvestingYT | ^253 c18 | [I’ve initiated a position in $BFLY in response to the greatest medical imaging a](https://x.com/KevInvestingYT/status/2067684979098694058) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@afshineemrani</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9168 · 💬 307</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/afshineemrani/status/2067630924108538083">View @afshineemrani on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm a cardiologist. Something just happened today that I genuinely did not see coming — and it could change the future of preventive medicine more than anything I've written about on this platform. Mi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney announced a medical hardware division and a working prototype full-body ultrasonic scanner that uses ~500K acoustic transducers and 2 petaflops of compute to reconstruct 3D internal anatomy in 60 seconds, radiation-free.</dd>
      <dt>Why interesting</dt>
      <dd>An AI image company pivoting into medical hardware shows that AI-driven volumetric reconstruction is production-ready — a space directly adjacent to XR medical visualization and simulation.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio pursues medical e-learning or XR simulation clients, start scoping a Unity pipeline that ingests full-body 3D scan data — this scanner is a credible near-term data source.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/afshineemrani/status/2067630924108538083" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amazingzeros</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7445 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amazingzeros/status/2067666616700334555">View @amazingzeros on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“sonic fan pissing their pants about fortnite as if sora ai getting deleted didn’t set their games back by 20 years”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan rant comparing Sonic fandom reactions to Fortnite against the cancellation of OpenAI's Sora video-generation model, framed as gaming culture drama with no technical content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amazingzeros/status/2067666616700334555" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4644 · 💬 886</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067688872944025975">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We're gonna do a Midjourney Medical AMA (ask me anything ) right here all afternoon. Post your questions below and we'll try to answer as many as we can! ❤️”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney hosted a live Medical AMA on X, answering audience questions about their AI image generation tools applied to medical use cases.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2067688872944025975" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aakashgupta</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3811 · 💬 110</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aakashgupta/status/2067579580622528913">View @aakashgupta on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Let me explain why an AI art company just built a full-body medical scanner, because almost everyone is reading this as a random pivot. Ultrasonic CT works by firing sound through your body and record”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney applied its image-reconstruction AI to ultrasonic CT scanning, delivering full-body 3D scans in 60 seconds at sub-millimeter resolution with no radiation, deployed inside spa facilities.</dd>
      <dt>Why interesting</dt>
      <dd>A model trained on one class of inverse problem (image generation) transferred to a physically unrelated domain (acoustic reconstruction), cutting scan time 100x over MRI.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Before scoping a new AI feature from scratch, check whether existing generation or reconstruction models in the studio's pipeline can transfer to the new input modality.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aakashgupta/status/2067579580622528913" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3762 · 💬 109</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2067662326082498899">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I don't know if it's obvious information or not but if you talk to random people in San Francisco the general thing they say is that software is commoditized cause so easy to make anything with AI fas”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@levelsio reports SF consensus: software is commoditized because AI lets anyone build replacements fast — he cancelled all paid SaaS and vibe-coded free alternatives — so talent is moving into hardware.</dd>
      <dt>Why interesting</dt>
      <dd>Clients who once bought custom software now weigh building it themselves with AI — the studio's value must sit in complexity, domain depth, and production quality that solo AI builders can't replicate.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Update pitches to lead with what the studio delivers that AI-assisted solo builders can't: XR/Unity integration, production-grade e-learning systems, and cross-platform deployment at scale.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2067662326082498899" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nickfloats</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3633 · 💬 94</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nickfloats/status/2067445022484529282">View @nickfloats on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“What Midjourney is: - No investors, fully community-funded research lab - Revenue from image generation product funds all R&amp;D - ~$100M in first 9 months, $200M by month 12, still growing - 8 active pr”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney hit $200M ARR by month 12 with no outside investors, and founder David Holz (ex-Leap Motion, Northstar AR) is shipping two consumer-purchasable hardware products soon.</dd>
      <dt>Why interesting</dt>
      <dd>Holz's XR background (hand-tracking, open-source AR headset) signals the upcoming Midjourney hardware targets spatial or creative input — directly relevant to the studio's XR workflow.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Track Midjourney's hardware announcement; if consumer spatial-input devices ship, the XR team should evaluate them for prototyping and interaction design.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nickfloats/status/2067445022484529282" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@synthwavedd</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2486 · 💬 148</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/synthwavedd/status/2068000857757741251">View @synthwavedd on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 SCOOP: After the release of Fable 5 and with GPT-5.6 looming, the mood behind the scenes at Google DeepMind is increasingly one of frustration and broad discontent over the lab's perceived fall into”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>DeepMind insiders report Gemini has fallen to 5th on the Artificial Analysis Intelligence Index, behind Anthropic, OpenAI, and Zhipu AI, with Gemini 3.5 Pro internally viewed as not competitive enough.</dd>
      <dt>Why interesting</dt>
      <dd>Google's models now measurably trail Anthropic and OpenAI; studios planning Gemini integrations should validate current performance gaps before committing to them.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Benchmark Gemini against current Anthropic and OpenAI equivalents for any planned AI feature — don't assume Google parity based on past evaluations.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/synthwavedd/status/2068000857757741251" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cignificants</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1884 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cignificants/status/2067644406728135033">View @cignificants on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“so hey, aside from midjourney and gemini what other generative AI program do you use? just curious https://t.co/vAU8YebeEj”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user on X asks their followers which generative AI tools they use besides Midjourney and Gemini, with no announcement, release, or insight attached.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cignificants/status/2067644406728135033" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
