---
type: social-topic-report
date: '2026-05-27'
topic: ai-research
lang: en
pair: ai-research.th.md
generated_at: '2026-05-27T04:44:49+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- rss
- x
regions:
- global
post_count: 141
salience: 0.35
sentiment: mixed
confidence: 0.55
tags:
- llm-eval
- calibration
- open-weights
- distillation
- webgpu-diffusion
- benchmarks
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2044425258103349248/img/zb0xdjPxs5hCOe38.jpg
---

# AI Research — 2026-05-27

## TL;DR
- Heretic decensoring tool gets FT coverage, raising governance questions for any team finetuning open weights [3][6]
- Google paper argues LLMs should express calibrated uncertainty instead of confident hallucination — directly relevant to eval design [15]
- METR's AI time-horizons graph publicly challenged for methodological errors; reduces trust in headline 'AI progress' charts [38]
- New training findings: weaker teachers can improve stronger students (distillation counter-intuition) [22]; MeMo gives LLMs an external memory module [59]
- Browser-local 1-bit/ternary text-to-image diffusion (Bonsai 4B on WebGPU) — viable for edutech/XR offline asset gen [5]

## What happened
Several concrete research signals cut through the noise. The Financial Times profiled Heretic, a decensoring tool used to strip safety alignment from open-weight LLMs [3], and a Qwen3.5 35B A3B 'uncensored heretic' release with preserved MTPs appeared in multiple quant formats [6]. A Google paper reframed hallucination as a calibration problem, arguing models should signal uncertainty rather than sound confident [15]. METR's widely-cited AI time-horizons benchmark graph was publicly challenged by an NYU Stern writer for severe methodological errors [38]. On the methods side: a distillation paper shows a weaker teacher can train a stronger student [22], and MeMo proposes a separate memory module bolted onto frozen LLMs to avoid catastrophic forgetting [59]. PrismML shipped Bonsai 4B, a 1-bit/ternary T2I diffusion transformer running locally in browser via WebGPU [5].

## Why it matters (reasoning)
Two threads matter for adoption decisions. First, evaluation credibility is eroding — METR's chart being torn down [38] plus the calibration/hallucination reframing [15] means studios should stop quoting headline benchmark numbers and start demanding uncertainty-aware evals before picking a model. Second, the open-weights stack is maturing in directions a small studio can actually use: extreme-quant diffusion in-browser [5], memory-augmented LLMs that don't require retraining [59], and counter-intuitive distillation recipes [22] that lower the cost of building task-specific small models. The Heretic story [3][6] is a governance warning — any open-weight model you finetune can be trivially decensored downstream, which matters for client contracts and edutech deployments.

## Possibility
Likely (>60%): calibration/uncertainty metrics get folded into mainstream eval suites within 6–12 months, making 'confidence-aware' a procurement checkbox. Likely (>50%): browser-side WebGPU diffusion becomes good enough for on-device asset previews in Unity/Web tools by late 2026. Moderate (~40%): METR-style time-horizon claims get formally retracted or revised, cooling 'AGI by 202X' discourse. Low (~20%): Heretic-style decensoring triggers a concrete regulatory response targeting open-weight publishers.

## Org applicability — NDF DEV
Worth tracking, selectively adopt. (1) For edutech/Enggenius: pilot MeMo-style external memory [59] for per-student knowledge state instead of finetuning — cheaper, auditable. (2) For XR/Unity asset pipelines: prototype Bonsai 4B WebGPU [5] as an in-editor concept-art generator; quality likely rough but latency/privacy wins. (3) For client-facing LLM features: bake calibrated-uncertainty outputs [15] into prompts and UI now (show 'unsure' states) — cheap differentiator. (4) Add a contract clause about downstream decensoring [3][6] when delivering finetuned open-weight models. Skip: red-team Claude skills [12][14][17] — interesting but not core. Skip: AlphaProof Nexus 'eliminates hallucination' claim [30] — unsourced hype.

## Signals to Watch
- Whether METR publishes a correction or defense of its time-horizons methodology [38]
- Real-world Bonsai 4B WebGPU benchmarks (tokens/sec, VRAM, image quality) from independent testers [5]
- Adoption of uncertainty/calibration metrics in HELM, lm-eval-harness, or vendor model cards [15]
- MeMo reproductions on non-toy LLMs (≥7B) with public code [59]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | moonlithoax | ^1588 c5 | [taylor’s toy story countdown wasn’t a hallucination you saw it with your own eye](https://x.com/moonlithoax/status/2059328279610319117) |
| x | GemsOfCricket | ^1184 c22 | [How often do we even see GT’s top order collapse like this? 😭 RCB are playing in](https://x.com/GemsOfCricket/status/2059318418382413915) |
| reddit | -p-e-w- | ^867 c217 | [The Financial Times has published an article about Heretic https://www.ft.com/co](https://www.reddit.com/r/LocalLLaMA/comments/1tna22m/the_financial_times_has_published_an_article/) |
| x | lutexorcists | ^555 c8 | [It’s so sad that Lute had to create an idealized version of Adam in her head jus](https://x.com/lutexorcists/status/2059331623225561455) |
| reddit | xenovatech | ^413 c48 | [PrismML just released Binary and Ternary Bonsai Image 4B: 1-bit/ternary text-to-](https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/) |
| reddit | LLMFan46 | ^402 c75 | [Qwen3.5 35B A3B uncensored heretic Native MTP Preserved is Out Now With the Full](https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/) |
| x | faegoth_ | ^355 c7 | [I just learned theres a mass hallucination of sinners pv is tomorrow??? how did ](https://x.com/faegoth_/status/2059397475291574740) |
| x | kfcrui | ^351 c1 | [this was a collective hallucination wasn’t it https://t.co/o8fGM5KTGE](https://x.com/kfcrui/status/2059358824038027743) |
| x | Hesamation | ^349 c22 | [Remember this? 20 days ago SubQ claimed to have developed a model with 12M conte](https://x.com/Hesamation/status/2059048186308939966) |
| x | mcjoki01 | ^339 c4 | [i think fritz would be robin in this scenario but it wouldnt be a hallucination.](https://x.com/mcjoki01/status/2059243647585935597) |
| x | VENTIlMPACT | ^299 c11 | [are we actually getting sinners pv tomorrow or is this like a collective halluci](https://x.com/VENTIlMPACT/status/2059390159297171513) |
| x | VivekIntel | ^256 c1 | [⚔️ Claude-Red = Offensive Security Skills for Claude AI A massive open-source fr](https://x.com/VivekIntel/status/2059235180150456753) |
| x | gunsen_history | ^240 c3 | [Following yet again some form of hallucination-meme posting from the usual suspe](https://x.com/gunsen_history/status/2059229028473581622) |
| x | GithubProjects | ^206 c6 | [Claude-Bughunter is a drop-in skill bundle that transforms Claude Code into a se](https://x.com/GithubProjects/status/2059172145453019389) |
| x | rohanpaul_ai | ^187 c38 | [New Google paper says LLMs should stop pretending certainty and instead clearly ](https://x.com/rohanpaul_ai/status/2059040056976032121) |
| x | AndrewCurran_ | ^179 c12 | [If Anthropic discovered tonight that we were about to hit a hard architectural w](https://x.com/AndrewCurran_/status/2059080914165174653) |
| x | 7h3h4ckv157 | ^164 c2 | [Open-source LLM red-team lab. 159 transforms, 25 tool surfaces, BYOK gateway. Ru](https://x.com/7h3h4ckv157/status/2059148258015133838) |
| x | joongiephilia | ^161 c2 | [the “comeback”was actually a mass hallucination as a result of all of us inhalin](https://x.com/joongiephilia/status/2059159520882897329) |
| x | paraschopra | ^159 c32 | [Hot take: mech interpretability might have a better chance than neuroscience at ](https://x.com/paraschopra/status/2059250458578108562) |
| x | rosiierix | ^152 c2 | [it may not have been one of his best races but literally almost everyone got lap](https://x.com/rosiierix/status/2059218198810022017) |
| x | hyjsrj5 | ^147 c0 | [i kinda love how every ryeji enjoyer’s first instinct is to question whether thi](https://x.com/hyjsrj5/status/2059259916318277795) |
| x | TaimingLu | ^146 c3 | [Knowledge doesn't always flow downhill. We find that in LLM pretraining, a weake](https://x.com/TaimingLu/status/2059348987854078145) |
| x | aveihwa | ^132 c2 | [is this comeback a mass hallucination or what???? WHERES MAP WHERES ANYTHING ???](https://x.com/aveihwa/status/2059288974510731713) |
| x | AlexByBel | ^128 c2 | [Also, sorry, but noticed how she tried to set authority? She was used to being l](https://x.com/AlexByBel/status/2059240545717797149) |
| x | luke_d_ismas | ^99 c1 | [@fmtovvns Yeah, because pizzagate was a collective schizo hallucination you peop](https://x.com/luke_d_ismas/status/2059014513928622308) |
| x | ipurple | ^96 c0 | [Advanced EDR Evasion via AI Telemetry Spoofing &amp; WASM Sandboxing. Project On](https://x.com/ipurple/status/2058990735244898449) |
| x | Matthew22361008 | ^95 c0 | [@Polymarket So Claude or chatgpt will generate a hallucination for him to go on ](https://x.com/Matthew22361008/status/2059327687131381895) |
| x | donmcgowan | ^89 c5 | [Isabel must be suffering the heat in Dubai. Reform UK vetting? A hallucination, ](https://x.com/donmcgowan/status/2059215937421647891) |
| x | shin1ster | ^88 c1 | [ryeji been dead so long everyone feels like this is a mass hallucination im cryi](https://x.com/shin1ster/status/2059297628966490125) |
| x | HowToAI_ | ^81 c6 | [Google DeepMind just solved 9 math problems that stumped humans for 56 years. Th](https://x.com/HowToAI_/status/2059309648319255006) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@moonlithoax</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1588 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/moonlithoax/status/2059328279610319117">View @moonlithoax on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“taylor’s toy story countdown wasn’t a hallucination you saw it with your own eyes https://t.co/m3qNZApsMN”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user claims that a 'Taylor's Toy Story countdown' seen on screen was real, not an AI hallucination, sharing a link as evidence.</dd>
      <dt>Why interesting</dt>
      <dd>The post highlights ongoing user confusion between real UI artifacts and AI hallucinations — a trust and reliability perception problem relevant to any AI-integrated product.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/moonlithoax/status/2059328279610319117" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GemsOfCricket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1184 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GemsOfCricket/status/2059318418382413915">View @GemsOfCricket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“How often do we even see GT’s top order collapse like this? 😭 RCB are playing in a completely different league altogether. Just hand this red team the IPL trophy already and save everyone’s time and m”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The author reacts to Gujarat Titans' top-order batting collapse against RCB in an IPL match, declaring RCB so dominant they deserve the trophy outright.</dd>
      <dt>Why interesting</dt>
      <dd>This is cricket fan reaction content — no AI research signal here despite the topic tag.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GemsOfCricket/status/2059318418382413915" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@-p-e-w-</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 867 · 💬 217</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tna22m/the_financial_times_has_published_an_article/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/1jj33XJ1H-54Y80OkvxFXjRDRakyiEJA-YPgdpaPQvI.jpeg?auto=webp&amp;s=bb2e661005a71269b7eee76f0ce92e1f05b13769" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Financial Times has published an article about Heretic https://www.ft.com/content/5630ed79-a263-41ed-9a1a-321617ae310e “The FT was able to use Heretic, a tool available on the popular code reposit”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A GitHub tool called Heretic can strip safety guardrails from Meta's Llama 3.3 in under 10 minutes on consumer hardware; it has produced 3,500+ uncensored model variants downloaded 13 million times.</dd>
      <dt>Why interesting</dt>
      <dd>Open-source uncensored LLMs are now mainstream-press-level real — any team self-hosting local models must have an explicit policy on which model weights are acceptable to deploy.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's e-learning and XR projects that use local LLMs for NPC dialogue or content generation need a documented model-vetting step — confirm the base weights used are unmodified and guardrail-intact before shipping.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tna22m/the_financial_times_has_published_an_article/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@lutexorcists</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 555 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/lutexorcists/status/2059331623225561455">View @lutexorcists on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It’s so sad that Lute had to create an idealized version of Adam in her head just to feel understood. His hallucination doesn’t act like him at all, it just agrees with everything she says. It really ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post about the animated show Hazbin Hotel — character Lute mentally constructs an idealized version of Adam that simply agrees with her, highlighting her isolation in Heaven.</dd>
      <dt>Why interesting</dt>
      <dd>Tagged 'AI Research' but contains zero AI content — the word 'hallucination' is used in a psychological/fictional sense, not the LLM sense. Mislabeled topic.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/lutexorcists/status/2059331623225561455" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@xenovatech</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 413 · 💬 48</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/MjJtcWdvbnAyajNoMRUAidRtSeHG3AHsqjmYv2JB7OCCSSOBELAe-XVtLJ1l.png?format=pjpg&amp;auto=webp&amp;s=426a3e068ac859239a76b1ce25919ca9acf01a35" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“PrismML just released Binary and Ternary Bonsai Image 4B: 1-bit/ternary text-to-image diffusion transformers that can even run 100% locally in your browser on WebGPU. The PrismML team really cooked wi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>PrismML released Bonsai Image 4B — binary/ternary quantized text-to-image diffusion transformers (~3GB) that run fully in-browser via WebGPU, Apache-2.0 licensed.</dd>
      <dt>Why interesting</dt>
      <dd>A 4B image-gen model compressed to 3GB running 100% client-side on WebGPU means zero server cost and zero API dependency for generative image features.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The web stack can embed client-side AI image generation directly in Next.js e-learning or XR companion tools via WebGPU — no backend inference cost, works offline.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@LLMFan46</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 402 · 💬 75</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/NuJoeV0pDXdCss6LQMmTsZirXhAB7Ep19_9Taoo-y1o.png?auto=webp&amp;s=efeccef16cb40de293ae56d988bd1995ebf78b3f" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Qwen3.5 35B A3B uncensored heretic Native MTP Preserved is Out Now With the Full 785 MTPs Preserved and Retained, Available in Safetensors, GGUFs. NVFP4, NVFP4 GGUFs and GPTQ-Int4 Formats Safetensors,”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A community member released an uncensored fine-tune of Qwen3.5 35B A3B with all 785 Multi-Token Prediction (MTP) heads preserved, available in Safetensors, GGUF, NVFP4, and GPTQ-Int4 formats on HuggingFace.</dd>
      <dt>Why interesting</dt>
      <dd>Preserving all 785 MTP heads keeps speculative decoding speed gains intact — most uncensored merges strip these, so this release offers both freedom and performance in one model.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can run the GGUF variant locally via llama.cpp for uncensored content-generation tasks (game narrative, e-learning scripts) without API costs or content-policy blocks.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@faegoth_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 355 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/faegoth_/status/2059397475291574740">View @faegoth_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I just learned theres a mass hallucination of sinners pv is tomorrow??? how did I miss that”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The author just discovered that a mass group-watch event for the 'Sinners' promotional video is scheduled for tomorrow and is surprised they almost missed it.</dd>
      <dt>Why interesting</dt>
      <dd>Not interesting to a dev team — this is pure fandom hype, mislabeled as AI Research.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/faegoth_/status/2059397475291574740" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kfcrui</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 351 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kfcrui/status/2059358824038027743">View @kfcrui on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“this was a collective hallucination wasn’t it https://t.co/o8fGM5KTGE”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The author suggests that some widely-believed AI claim or hype (linked) turned out to be false or illusory — a 'collective hallucination' by the community.</dd>
      <dt>Why interesting</dt>
      <dd>A signal that the AI research community is course-correcting on overhyped results — worth tracking which specific claim collapsed to avoid building on shaky foundations.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable — post lacks enough detail without the linked content to draw a concrete lesson for the studio's stack or workflow.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kfcrui/status/2059358824038027743" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
