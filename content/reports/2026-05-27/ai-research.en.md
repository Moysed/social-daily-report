---
type: social-topic-report
date: '2026-05-27'
topic: ai-research
lang: en
pair: ai-research.th.md
generated_at: '2026-05-27T16:42:18+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- rss
- x
regions:
- global
post_count: 158
salience: 0.55
sentiment: mixed
confidence: 0.6
tags:
- local-llm
- webgpu
- diffusion
- evaluation
- quantization
- open-source
thumbnail: https://pbs.twimg.com/media/HJQrLpmawAAV7Zq.jpg
---

# AI Research — 2026-05-27

## TL;DR
- PrismML's Binary/Ternary Bonsai Image 4B brings 1-bit/ternary diffusion transformers to WebGPU browsers — potentially viable for in-app generative assets [3]
- Qwen3.5 35B A3B drop with native MTP preserved across NVFP4/GGUF/GPTQ formats expands local-LLM options for studios [4]
- Counter-intuitive pretraining paper: weaker teachers can produce stronger students; pushing teacher capacity can hurt distillation [12]
- METR's AI time-horizons benchmark graph publicly challenged for severe methodological errors — caution before citing it in roadmap decks [37]
- SubQ's 12M-context / 95%-cheaper-than-Opus claim from 20 days ago remains unreleased — pattern of vaporware to watch [8]

## What happened
Concrete model releases dominate the signal: PrismML shipped binary/ternary Bonsai Image 4B text-to-image diffusion that runs locally in-browser on WebGPU [3], and a Qwen3.5 35B A3B uncensored variant landed with full 785-MTP preservation across multiple quantization formats [4]. On the research side, a new paper argues that in pretraining a weaker teacher can improve a stronger student, with stronger teachers sometimes hurting [12], and an SAE-interpretability paper claims representations can directly guide post-training data engineering [44].

Evaluation hygiene got a hit: a writeup attacks METR's widely-cited AI time-horizons graph for severe errors [37], and SubQ's unverified 12M-context claim still has no paper or model card [8]. Tooling moved too — EvoSkill expanded from 1 to 190+ benchmarks for coding-agent eval via Harbor integration [43], and browser_use claims SOTA web-agent performance with a custom LLM+harness combo [51]. Most other items are red-team security tooling, IPL cricket, or political commentary — off-topic noise for an AI-research lens.

## Why it matters (reasoning)
For a studio adopting models, three things matter: (1) on-device generative assets are getting real — 1-bit/ternary diffusion in a browser [3] means edutech/XR builds can ship visual generation without server costs or API keys; (2) the local-LLM ecosystem keeps maturing with proper quantization variety [4], lowering the barrier for offline Unity/Next.js integrations; (3) the field's evaluation foundations are wobblier than headlines suggest — METR's chart being attacked [37] and SubQ's unfulfilled claims [8] argue for benchmarking on your own task before any adoption. The weaker-teacher distillation finding [12] hints that future small open models may close the gap to frontier faster than expected, which favors waiting before locking into proprietary APIs for non-critical paths.

## Possibility
Likely (~70%): WebGPU-native generative models become viable for in-browser asset pipelines within 6–12 months, with Bonsai-class quality acceptable for prototypes and stylized assets [3]. Moderate (~50%): one of the open Qwen/Minimax/Kimi lines [4][24][29] reaches Claude-Sonnet-tier coding within a year, making self-hosted dev agents practical. Lower (~25%): SubQ's claims [8] get validated; more likely the trend of unreproducible PR-driven announcements continues, raising bar for trust. Eval methodology will fragment further — expect more attacks on aggregate charts like METR's [37] and a shift toward task-specific reproducible suites like EvoSkill [43].

## Org applicability — NDF DEV
Worth experimenting now: spin a 1-day spike on Bonsai 4B WebGPU [3] for the Next.js/Supabase web apps — could replace paid image APIs for low-stakes generation (placeholders, mood boards, edutech illustrations). For Unity/XR, defer until tooling matures. For internal coding assistance, track Qwen3.5 35B A3B [4] and Minimax M3 [24] as fallback to Claude/GPT, but don't migrate critical paths. Adopt EvoSkill-style task-specific evals [43] when picking a coding model — don't trust public leaderboards. Skip the red-team security skill bundles [5][11][13][49][52] unless a client explicitly contracts pentesting work; off-mission for a games/XR/edutech studio. Avoid building roadmap slides citing METR [37] or SubQ [8] numbers.

## Signals to Watch
- PrismML Bonsai WebGPU demo quality on real product imagery (not cherry-picked) [3]
- Whether SubQ ships the promised 12M-context model card or admits it was vapor [8]
- EvoSkill 190+ benchmark adoption — does it become a credible alternative to SWE-Bench [43]
- Reproducibility of the 'weaker teacher, stronger student' result across labs [12]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | GemsOfCricket | ^1286 c22 | [How often do we even see GT’s top order collapse like this? 😭 RCB are playing in](https://x.com/GemsOfCricket/status/2059318418382413915) |
| x | teortaxesTex | ^923 c57 | [Elon making excuses for xAI losing momentum be like https://t.co/uMwTynnIXl](https://x.com/teortaxesTex/status/2059414380370887162) |
| reddit | xenovatech | ^571 c70 | [PrismML just released Binary and Ternary Bonsai Image 4B: 1-bit/ternary text-to-](https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/) |
| reddit | LLMFan46 | ^435 c77 | [Qwen3.5 35B A3B uncensored heretic Native MTP Preserved is Out Now With the Full](https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/) |
| x | VivekIntel | ^370 c2 | [⚔️ Claude-Red = Offensive Security Skills for Claude AI A massive open-source fr](https://x.com/VivekIntel/status/2059235180150456753) |
| reddit | OttoRenner | ^369 c240 | [Stop traumatizing AI into loops and turn hallucinations into an honest "I don't ](https://www.reddit.com/r/LocalLLaMA/comments/1tot20j/stop_traumatizing_ai_into_loops_and_turn/) |
| reddit | Porespellar | ^366 c86 | [A rare look inside Qwen 3.7’s open source model release approval process: For re](https://www.reddit.com/r/LocalLLaMA/comments/1toi50p/a_rare_look_inside_qwen_37s_open_source_model/) |
| x | Hesamation | ^358 c22 | [Remember this? 20 days ago SubQ claimed to have developed a model with 12M conte](https://x.com/Hesamation/status/2059048186308939966) |
| x | teortaxesTex | ^328 c17 | [Damn you people are picky https://t.co/oFhELCaizS](https://x.com/teortaxesTex/status/2059514884639928660) |
| x | marshalwahlexyz | ^247 c17 | [Let’s build fun stuff together 1. AI for Fraud detection 2. Agentic AI for Vulne](https://x.com/marshalwahlexyz/status/2058976994717585579) |
| x | GithubProjects | ^243 c6 | [Claude-Bughunter is a drop-in skill bundle that transforms Claude Code into a se](https://x.com/GithubProjects/status/2059172145453019389) |
| x | TaimingLu | ^234 c5 | [Knowledge doesn't always flow downhill. We find that in LLM pretraining, a weake](https://x.com/TaimingLu/status/2059348987854078145) |
| x | 7h3h4ckv157 | ^230 c2 | [Open-source LLM red-team lab. 159 transforms, 25 tool surfaces, BYOK gateway. Ru](https://x.com/7h3h4ckv157/status/2059148258015133838) |
| x | AndrewCurran_ | ^179 c12 | [If Anthropic discovered tonight that we were about to hit a hard architectural w](https://x.com/AndrewCurran_/status/2059080914165174653) |
| x | AnkitaxPriya | ^171 c24 | [How is no PM @zomato solving the LLM hallucination problem in its customer suppo](https://x.com/AnkitaxPriya/status/2059531498437681271) |
| x | paraschopra | ^166 c34 | [Hot take: mech interpretability might have a better chance than neuroscience at ](https://x.com/paraschopra/status/2059250458578108562) |
| x | BrianRoemmele | ^162 c31 | [Talking To The Pope: Anthropic’s Latest Interpretability Claims: AI Regulatory C](https://x.com/BrianRoemmele/status/2058950628538560861) |
| x | teortaxesTex | ^139 c1 | [1) 5.5 just solves it without fancy setups 2) If mythos could not solve the same](https://x.com/teortaxesTex/status/2059554208907407505) |
| x | jeremyphoward | ^128 c16 | [Wow. It looks like the @XiaomiMiMo v2.5 model is insanely good value :O (Price f](https://x.com/jeremyphoward/status/2059483529898299729) |
| x | teortaxesTex | ^127 c7 | [Claude Code is absurdly overrated](https://x.com/teortaxesTex/status/2059487600054874198) |
| x | ipurple | ^110 c0 | [Advanced EDR Evasion via AI Telemetry Spoofing &amp; WASM Sandboxing. Project On](https://x.com/ipurple/status/2058990735244898449) |
| x | lateinteraction | ^110 c3 | [can’t wait for the releases alex is planning for this summer. in the meantime, h](https://x.com/lateinteraction/status/2059644669550797017) |
| x | giangnguyen2412 | ^106 c4 | [this interpretability history lesson is rare I don't think I've seen a writeup l](https://x.com/giangnguyen2412/status/2059525287688519867) |
| x | teortaxesTex | ^102 c3 | [Reminder that Minimax M2 was supposed to be "Mini", it just turned out to be pow](https://x.com/teortaxesTex/status/2059464047284674964) |
| x | Raytar | ^97 c3 | [two OpenAI researchers walked into Stanford and made every AI thread on your fee](https://x.com/Raytar/status/2059352117001809976) |
| x | teortaxesTex | ^94 c4 | [This is mostly true but I don't want to say "xAI is slow". Because the reality i](https://x.com/teortaxesTex/status/2059484607133761690) |
| x | teortaxesTex | ^91 c4 | [This pseudoprofound bullshit is infuriating in its falsity. Nobody is capable of](https://x.com/teortaxesTex/status/2059457235047067907) |
| x | teortaxesTex | ^89 c4 | [@powerbottomdad1 you'd do well to not uncritically consume copes of third world ](https://x.com/teortaxesTex/status/2059444811703214338) |
| x | teortaxesTex | ^89 c3 | [Wait, this is pretty insane, I missed it. Kimi K2 is a ≈3e24 model. K2.5 2x that](https://x.com/teortaxesTex/status/2059428086639181977) |
| reddit | Possible-Active-1903 | ^85 c48 | [[D] Where do you go for serious AI research discussion online? [D] Looking for c](https://www.reddit.com/r/MachineLearning/comments/1to2l4c/d_where_do_you_go_for_serious_ai_research/) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GemsOfCricket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1286 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GemsOfCricket/status/2059318418382413915">View @GemsOfCricket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“How often do we even see GT’s top order collapse like this? 😭 RCB are playing in a completely different league altogether. Just hand this red team the IPL trophy already and save everyone’s time and m”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan reacts to Gujarat Titans' top-order batting collapse against RCB in an IPL match, declaring RCB dominant enough to be handed the trophy outright.</dd>
      <dt>Why interesting</dt>
      <dd>This is pure sports fan noise with no tech, AI, or dev relevance — tagged AI Research incorrectly.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GemsOfCricket/status/2059318418382413915" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@teortaxesTex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 923 · 💬 57</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/teortaxesTex/status/2059414380370887162">View @teortaxesTex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Elon making excuses for xAI losing momentum be like https://t.co/uMwTynnIXl”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The author mocks Elon Musk for making excuses about xAI losing momentum in the AI race.</dd>
      <dt>Why interesting</dt>
      <dd>Signals ongoing turbulence at xAI that may affect Grok's reliability as a tool or API dependency for small dev teams.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/teortaxesTex/status/2059414380370887162" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@xenovatech</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 571 · 💬 70</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/MjJtcWdvbnAyajNoMRUAidRtSeHG3AHsqjmYv2JB7OCCSSOBELAe-XVtLJ1l.png?format=pjpg&amp;auto=webp&amp;s=426a3e068ac859239a76b1ce25919ca9acf01a35" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“PrismML just released Binary and Ternary Bonsai Image 4B: 1-bit/ternary text-to-image diffusion transformers that can even run 100% locally in your browser on WebGPU. The PrismML team really cooked wi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>PrismML released 1-bit/ternary 4B text-to-image diffusion models (~3GB) that run fully in-browser via WebGPU, under Apache-2.0 license.</dd>
      <dt>Why interesting</dt>
      <dd>A 3GB image-gen model running 100% client-side on WebGPU means zero server cost and no API dependency — massive for small teams shipping web products.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The web stack can embed this model directly in Next.js e-learning or XR content tools, giving users real-time image generation without any backend or cost-per-call.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@LLMFan46</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 435 · 💬 77</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/NuJoeV0pDXdCss6LQMmTsZirXhAB7Ep19_9Taoo-y1o.png?auto=webp&amp;s=efeccef16cb40de293ae56d988bd1995ebf78b3f" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Qwen3.5 35B A3B uncensored heretic Native MTP Preserved is Out Now With the Full 785 MTPs Preserved and Retained, Available in Safetensors, GGUFs. NVFP4, NVFP4 GGUFs and GPTQ-Int4 Formats Safetensors,”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An uncensored fine-tune of Qwen3.5 35B A3B with all 785 Multi-Token Prediction (MTP) heads preserved is now available on HuggingFace in GGUF, NVFP4, and GPTQ-Int4 quantized formats.</dd>
      <dt>Why interesting</dt>
      <dd>Preserving native MTP heads means faster speculative decoding at inference — a meaningful speed boost for local deployment without degrading model capability.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can run GGUF builds locally on existing hardware for internal AI tooling or NPC dialogue prototypes; NVFP4 variant suits NVIDIA GPU setups for faster iteration on e-learning content generation.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VivekIntel</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 370 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VivekIntel/status/2059235180150456753">View @VivekIntel on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“⚔️ Claude-Red = Offensive Security Skills for Claude AI A massive open-source framework that transforms Claude into a context-aware red team assistant. 🔥 📚 100+ offensive security skill modules 🌐 Web ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude-Red is an open-source framework with 100+ modules that turns Claude into a red team assistant covering web exploitation, Active Directory, cloud, wireless, and AI-specific attack vectors.</dd>
      <dt>Why interesting</dt>
      <dd>The prompt injection and jailbreak testing modules directly map how Claude-based agents can be attacked — critical for any team shipping AI-powered products built on the same model.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's Claude-powered agents face these exact prompt injection and jailbreak risks; run Claude-Red's AI security modules against internal agents during QA to find attack surfaces before shipping.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VivekIntel/status/2059235180150456753" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@OttoRenner</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 369 · 💬 240</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tot20j/stop_traumatizing_ai_into_loops_and_turn/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/mvoQQ4SlSTGetBclDcpzQuuqaP1nCKYDfArLY0G4vIs.png?auto=webp&amp;s=d7b7b33b45bd4332de78d84acb0062ab4ee8cf9f" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Stop traumatizing AI into loops and turn hallucinations into an honest &quot;I don't know!&quot; by being NICE to them (Proof of Concept, Research, I don't want to sell anything) TL;DR Some AI behavior reminded”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer found that using kind, low-pressure prompts instead of 'elite expert' instructions reduced AI hallucinations, stopped thought loops, and got models to honestly say 'I don't know' — with a small but consistent dataset on GitHub.</dd>
      <dt>Why interesting</dt>
      <dd>Prompt framing directly affects model honesty and loop behavior — a free, zero-infrastructure fix that any dev using reasoning models can test today.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can update its internal AI prompt templates — for code-gen, e-learning content, and agent workflows — to use supportive framing and explicitly invite 'I don't know' responses to reduce silent errors.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tot20j/stop_traumatizing_ai_into_loops_and_turn/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Porespellar</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 366 · 💬 86</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1toi50p/a_rare_look_inside_qwen_37s_open_source_model/" target="_blank" rel="noopener"><img src="https://i.redd.it/01aov0rxdj3h1.gif" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A rare look inside Qwen 3.7’s open source model release approval process: For real tho, 9b, 27b, 122b, I don’t really care at this point, just show us that you still love us. EDIT: I guess I gotta use”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A sarcastic Reddit shitpost lamenting Qwen 3.7's slow open-source release approval process, expressing impatience for the 9B/27B/122B model drops.</dd>
      <dt>Why interesting</dt>
      <dd>Community frustration signals that Qwen's open-source release cadence is a real pain point — devs are actively waiting on these weights.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable. Post is noise/humor, not technical signal the studio can act on.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1toi50p/a_rare_look_inside_qwen_37s_open_source_model/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Hesamation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 358 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Hesamation/status/2059048186308939966">View @Hesamation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Remember this? 20 days ago SubQ claimed to have developed a model with 12M context window, 95% cheaper than Opus, and the same intelligence level. they promised to release the paper and model card “ne”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A researcher calls out SubQ for claiming a 12M-context, 95%-cheaper-than-Opus model but releasing zero paper, model card, or weights 20 days later — flagging it as a likely hype scam targeting investors.</dd>
      <dt>Why interesting</dt>
      <dd>Small dev teams are prime targets for hype-driven AI tools; this post gives a concrete red-flag checklist: no paper, no weights, only API-gated third-party evals = do not trust.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Before the studio adopts any new AI API or model into the web stack or Unity pipeline, require: public paper or technical report, open weights or reproducible benchmark, and community validation — not just a launch post.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Hesamation/status/2059048186308939966" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
