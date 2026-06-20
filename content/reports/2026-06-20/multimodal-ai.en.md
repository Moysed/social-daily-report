---
type: social-topic-report
date: '2026-06-20'
topic: multimodal-ai
lang: en
pair: multimodal-ai.th.md
generated_at: '2026-06-20T15:43:44+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 173
salience: 0.45
sentiment: mixed
confidence: 0.5
tags:
- video-generation
- comfyui
- open-weights
- production-pipeline
- model-comparison
- midjourney
thumbnail: https://pbs.twimg.com/media/HLLmjWXXEAAKcY8.jpg
---

# Multimodal AI — 2026-06-20

## TL;DR
- A free local video pipeline was demoed: NVIDIA Studio + ComfyUI + LTX (ltx_io) rendering full CG shorts on a personal machine [13].
- A working production stack was shared — ComfyUI/After Effects/Photoshop with Wan 2.2 I2V+T2V, Krea 2, GPT Image 2.0, Grok Image, and Florence2 [11].
- Hosted video models are in tight competition: Seedance 2.0, Kling 3.0 Pro, Gemini Omni Flash, Grok Imagine 1.5, plus Veo3 and Runway, with Seedance 2.1/2.5 said to ship next week [21][28][36][54][56].
- Known failure modes persist: multi-character/multi-opponent fight scenes and fine articulation (tongue rotation) still break video models [21][28].
- Midjourney announced a medical hardware pivot (full-body ultrasound), with claims it is 'quitting' image generation — this dominated engagement but is off-topic for production asset tooling and is single-source [29][38][43][44].

## What happened
Most high-engagement items concern Midjourney's announcement of a medical division and a full-body ultrasound scanner [29][38][43], which is hardware/medical and not generative image/video tooling; one reply notes the scanner is a separate effort with no AI in it yet [44]. The genuinely on-topic signal is smaller. A NVIDIA Studio-sponsored demo showed rendering CG shorts locally and free in ComfyUI using LTX [13]. A creator posted a concrete multi-tool stack: ComfyUI + After Effects + Photoshop driving Wan 2.2 (image-to-video and text-to-video), Krea 2, GPT Image 2.0, Grok Image, and Florence2 [11]. ComfyUI highlighted a motion-data-driven rebuild of a live drum performance rather than blind generation [14].

## Why it matters (reasoning)
Two things matter for a production studio. First, hosted video models are iterating fast and competing head-to-head (Seedance vs Kling vs Veo3 vs Runway) [21][28][36][56], which means short eval cycles and falling cost per usable clip, but also that any single vendor choice is temporary. Second, the local/open path is maturing: a GPU vendor (NVIDIA) is promoting a free local ComfyUI+LTX render pipeline [13], and open-weight Wan 2.2 is already in real stacks [11] — this reduces dependence on closed APIs for previz and asset drafts. The Midjourney medical pivot, regardless of merit, is a second-order signal: a leading image tool is publicly redirecting attention to hardware [29][43], so treating Midjourney as a core, stable image pipeline carries vendor risk. Persistent weaknesses in multi-character scenes and fine motion [21][28] mean these tools remain drafting/B-roll aids, not finished-shot generators.

## Possibility
Likely: the hosted video model release cadence continues, with a near-term Seedance update claimed for next week [28] and ongoing Kling/Veo/Runway competition [21][36][56]. Plausible: local open pipelines (ComfyUI + LTX + Wan 2.2) become practical for studio previz and asset drafts given vendor backing and existing real-world use [11][13]. Plausible-to-unlikely: Midjourney materially exits image generation — sourced from hype posts and contradicted by a reply saying the scanner is unrelated [43][44]. Unlikely to verify: the 'Sora deleted' claim, which appears only as offhand chatter [2][10]. No source gives numeric probabilities, so none are asserted.

## Org applicability — NDF DEV
1) Stand up a local ComfyUI + Wan 2.2 + LTX test bench for game/XR previz and edutech B-roll; Wan 2.2 has open weights and the LTX local render path is free — low/med effort [11][13]. 2) Run a short internal bake-off of hosted video models (Seedance, Kling, Veo3, Runway) on one or two real edutech/marketing shots to pick a current default and a fallback — low effort [21][36][56]. 3) Diversify away from Midjourney as a single image source given its public pivot; keep alternatives (Krea, GPT Image, Grok Image) in the stack — low effort [11][29][43]. 4) For motion-heavy or multi-character shots, plan on motion-data/manual compositing rather than pure generation [14][28]. Skip: the Midjourney medical-scanner debate [1][3][9][16][23][31][49][58][60], the 'free AI tools' listicles [26][37][45][51][52][59], and follower-farming threads [22][39][48][55] — no production value.

## Signals to Watch
- Seedance 2.1/2.5 reportedly shipping next week — re-run the video bake-off when it lands [28].
- Wan 2.2 open weights showing up in real stacks — track for self-hosted I2V/T2V [11].
- NVIDIA promoting free local ComfyUI+LTX rendering — watch for hardware-tier requirements and quality ceiling [13].
- Midjourney's image-gen roadmap after the medical pivot — confirm before relying on it [43][44].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | afshineemrani | ^9473 c318 | [I'm a cardiologist. Something just happened today that I genuinely did not see c](https://x.com/afshineemrani/status/2067630924108538083) |
| x | amazingzeros | ^7449 c19 | [sonic fan pissing their pants about fortnite as if sora ai getting deleted didn’](https://x.com/amazingzeros/status/2067666616700334555) |
| x | midjourney | ^4717 c897 | [We're gonna do a Midjourney Medical AMA (ask me anything ) right here all aftern](https://x.com/midjourney/status/2067688872944025975) |
| x | levelsio | ^3899 c112 | [I don't know if it's obvious information or not but if you talk to random people](https://x.com/levelsio/status/2067662326082498899) |
| x | synthwavedd | ^2873 c174 | [🚨 SCOOP: After the release of Fable 5 and with GPT-5.6 looming, the mood behind ](https://x.com/synthwavedd/status/2068000857757741251) |
| x | cignificants | ^1951 c14 | [so hey, aside from midjourney and gemini what other generative AI program do you](https://x.com/cignificants/status/2067644406728135033) |
| x | Prolotario1 | ^1894 c131 | [Quite The Eventful Day It Has Been: New Air Force 1 New GTA 6 Promo New Midjourn](https://x.com/Prolotario1/status/2067768517613551818) |
| x | ChanduThota | ^1609 c55 | [Video is an effective way to communicate, and we want to make it as easy as edit](https://x.com/ChanduThota/status/2067631530890113477) |
| x | matt_is_nice | ^1087 c46 | [Everyone arguing about whether the Midjourney Scanner can replace an MRI or CT i](https://x.com/matt_is_nice/status/2067796547400814608) |
| x | lanxre | ^744 c35 | [What does this change?😭✌🏾 shit looks like it’s from Sora Ai](https://x.com/lanxre/status/2068170937401237893) |
| x | ingi_erlingsson | ^677 c18 | [take the wheel 🏁 make: ComfyUI, After Effects, Photoshop model: Wan 2.2 I2V + T2](https://x.com/ingi_erlingsson/status/2067756997756256650) |
| x | fabianstelzer | ^530 c23 | [this will be such a great movie. how do you even steal a EUV machine? https://t.](https://x.com/fabianstelzer/status/2067907362329907275) |
| x | mickmumpitz | ^464 c12 | [Paid partnership with @NVIDIAStudio - You can now render entire CG movies with l](https://x.com/mickmumpitz/status/2067976421687881962) |
| x | ComfyUI | ^443 c8 | [Most AI video work is just "generate and hope." This is different. Creator seung](https://x.com/ComfyUI/status/2067669239033717141) |
| x | javilopen | ^439 c48 | [Why didn't they call me to name this? What a wasted opportunity to call it... ME](https://x.com/javilopen/status/2067926942238540049) |
| x | heacockmd | ^359 c48 | [Apparently, yesterday @midjourney pivoted from AI image generation to...whole bo](https://x.com/heacockmd/status/2067638397804441634) |
| x | fofrAI | ^343 c24 | [Entrance to the new Midjourney spa https://t.co/vsnEIjM36P](https://x.com/fofrAI/status/2067635885370126556) |
| x | ai_explorer25 | ^338 c22 | [Best accounts to follow from each frontier lab to stay constantly up to date Ant](https://x.com/ai_explorer25/status/2068159401253327223) |
| x | MTSlive | ^297 c6 | [Why is the Midjourney team uniquely qualified to build medical hardware? @BeffJe](https://x.com/MTSlive/status/2067757811191447659) |
| x | askwhykartik | ^290 c21 | [A lot of people asked how I made this animation, so here's the process 👇 Honestl](https://x.com/askwhykartik/status/2067990215764148331) |
| x | YourAlphaMom | ^267 c29 | [New tongue-physics test for the best AI video models! Seedance 2.0, Kling 3.0 Pr](https://x.com/YourAlphaMom/status/2068046646085329212) |
| x | icreatelife | ^266 c121 | [I’m following 3,700 AI pioneers and I’d love to follow 300 more, to make it a ro](https://x.com/icreatelife/status/2067728865808519355) |
| x | KevInvestingYT | ^260 c19 | [I’ve initiated a position in $BFLY in response to the greatest medical imaging a](https://x.com/KevInvestingYT/status/2067684979098694058) |
| x | dreamingtulpa | ^259 c13 | [still can't get over how beautiful some of these shots are and the soundtrack 👌 ](https://x.com/dreamingtulpa/status/2067880684920643956) |
| x | abarrallen | ^250 c19 | [I just read a story about a runner I know who had leg pain for 3.5 years. Her di](https://x.com/abarrallen/status/2067978979668275486) |
| x | dharmvir_ | ^235 c43 | [GITHUB REPOS THAT FEEL ILLEGAL TO USE, THEY'RE KILLING $50 BILLION IN CORPORATE ](https://x.com/dharmvir_/status/2067873642038612343) |
| x | Rakib_Web3 | ^218 c16 | [i pay $0 for ai tools. literally zero. and i use all of them chatgpt, cursor, mi](https://x.com/Rakib_Web3/status/2068040519037616393) |
| x | aimikoda | ^214 c35 | [No matter how much we try, multiple-opponent scenes always seem to be challengin](https://x.com/aimikoda/status/2068139736242307295) |
| x | martinvars | ^212 c9 | [Midjourney announcing Midjourney Medical is a useful shock. An AI image company ](https://x.com/martinvars/status/2067628676955418990) |
| x | AntonHand | ^212 c10 | [All the AI bros saying things like "I know the Midjourney stuff might be bullshi](https://x.com/AntonHand/status/2068051953947660585) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@afshineemrani</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9473 · 💬 318</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/afshineemrani/status/2067630924108538083">View @afshineemrani on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm a cardiologist. Something just happened today that I genuinely did not see coming — and it could change the future of preventive medicine more than anything I've written about on this platform. Mi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney unveiled a medical hardware prototype — a full-body ultrasound scanner using 500k transducers in a water pool, 60-second scan, 2-petaflop AI reconstructing 3D anatomy with no radiation.</dd>
      <dt>Why interesting</dt>
      <dd>An AI image company shipping physical medical hardware shows multimodal AI — acoustic input to 3D reconstruction — is crossing from research into real clinical products faster than expected.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action. No SDK or API exists yet; watch for developer access if the studio pursues medical e-learning or XR anatomy simulation later.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/afshineemrani/status/2067630924108538083" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amazingzeros</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7449 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amazingzeros/status/2067666616700334555">View @amazingzeros on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“sonic fan pissing their pants about fortnite as if sora ai getting deleted didn’t set their games back by 20 years”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A social post mocking Sonic fans over Fortnite discourse while making an unverified claim that 'Sora AI got deleted' set game development back 20 years.</dd>
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
    <span class="ndf-engagement">♥ 4717 · 💬 897</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067688872944025975">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We're gonna do a Midjourney Medical AMA (ask me anything ) right here all afternoon. Post your questions below and we'll try to answer as many as we can! ❤️”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Midjourney announced a live Medical AMA on X, inviting the public to post questions about its medical AI direction — no product details shared in the post itself.</dd>
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
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3899 · 💬 112</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2067662326082498899">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I don't know if it's obvious information or not but if you talk to random people in San Francisco the general thing they say is that software is commoditized cause so easy to make anything with AI fas”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>levelsio says SF consensus is that software is commoditized — he cancelled all SaaS subs and vibe-coded replacements — pushing ambitious builders toward hardware as the next defensible entry.</dd>
      <dt>Why interesting</dt>
      <dd>If clients can self-serve with AI, studios that sell generic app-building lose pricing power; the defensible work shifts to complex integrations, XR, and hardware-adjacent builds.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should audit its service lineup and emphasize XR, Unity, and hardware-layer work in pitches — areas where AI-assisted self-serve still fails.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2067662326082498899" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@synthwavedd</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2873 · 💬 174</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/synthwavedd/status/2068000857757741251">View @synthwavedd on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 SCOOP: After the release of Fable 5 and with GPT-5.6 looming, the mood behind the scenes at Google DeepMind is increasingly one of frustration and broad discontent over the lab's perceived fall into”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A DeepMind insider reports Google's top model ranks 5th on the Artificial Analysis Intelligence Index—behind Anthropic, OpenAI, and Zhipu AI—and that Gemini 3.5 Pro (June 30) will not close the gap.</dd>
      <dt>Why interesting</dt>
      <dd>For a studio choosing AI API providers, Gemini dropping to 5th is a concrete prompt to benchmark alternatives before locking in integration work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Audit any planned or active Gemini API integrations and benchmark against Anthropic or OpenAI equivalents before committing API budget.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/synthwavedd/status/2068000857757741251" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cignificants</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1951 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cignificants/status/2067644406728135033">View @cignificants on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“so hey, aside from midjourney and gemini what other generative AI program do you use? just curious https://t.co/vAU8YebeEj”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Twitter user asks followers which generative AI tools they use beyond Midjourney and Gemini, with no specific tool, release, or finding shared.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cignificants/status/2067644406728135033" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Prolotario1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1894 · 💬 131</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Prolotario1/status/2067768517613551818">View @Prolotario1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Quite The Eventful Day It Has Been: New Air Force 1 New GTA 6 Promo New Midjourney Tech- New AI Data Center Orbit Concepts New Apple Intelligence &amp; Siri AI Upgrades New Matrox Video Low-Latency Tech N”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Twitter account lists ~10 unrelated news items from one day — Air Force 1 shoes, GTA 6, Midjourney, Starlink, Neuralink, Obama museum, etc. — as a general 'eventful day' roundup with no analysis.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Prolotario1/status/2067768517613551818" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ChanduThota</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1609 · 💬 55</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ChanduThota/status/2067631530890113477">View @ChanduThota on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Video is an effective way to communicate, and we want to make it as easy as editing slides - that's why we created Google Vids (https://t.co/Z0lp7dvIRB). We are launching major enhancements to AI avat”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google Vids is adding AI avatars, multilingual voiceovers (24 languages), and video generation that converts Google Slides decks into narrated videos with custom brand avatars.</dd>
      <dt>Why interesting</dt>
      <dd>Small studios often spend hours turning slide decks or feature demos into client-ready videos; this pipeline cuts that to minutes inside Google Workspace.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test Google Vids for converting project proposal decks or e-learning module slides into polished walkthrough videos before the next client delivery.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ChanduThota/status/2067631530890113477" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
