---
type: social-topic-report
date: '2026-06-17'
topic: ai-research
lang: en
pair: ai-research.th.md
generated_at: '2026-06-17T15:32:11+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- rss
- x
regions:
- global
post_count: 204
salience: 0.6
sentiment: mixed
confidence: 0.5
tags:
- glm-5.2
- open-weights
- gemini
- benchmarks
- model-adoption
- interpretability
thumbnail: https://pbs.twimg.com/media/HK8INEZaEAAffC_.jpg
---

# AI Research — 2026-06-17

## TL;DR
- GLM-5.2 is reported as the top open-weights model on Artificial Analysis's Intelligence Index, with a stated GDPval-AA v2 score of 1524 [8][39][41].
- Google flagged a 'Gemini 3.5 Pro coming soon' tag on the Gemini 3.1 Pro model card; no benchmark leaks yet, launch promised this month [1][10].
- Self-hosting a SOTA model is heavy: one item cites ~400GB memory to run a 2026 SOTA LLM, framing hosted APIs vs local trade-offs [24][7].
- Two reproducibility-relevant research threads surfaced: a state-tracking limitation of transformers [51] and an ICML 2026 paper on why many sparse-autoencoder features die [29].
- Multiple posts claim GLM-5.2 and a 'V4-Pro' close a theory-of-mind gap over prior versions, but evidence is anecdotal X chatter, not published evals [43][19][47].

## What happened
The day's AI-research signal centers on two events. First, GLM-5.2 (Zhipu/Tsinghua-linked [25]) is reported as the leading open-weights model on Artificial Analysis, including a GDPval-AA v2 figure of 1524 [8][39][41], with commentary calling its RL the strongest among Chinese labs [11]. Second, Google appears close to Gemini 3.5 Pro: a 'coming soon' tag was spotted on the Gemini 3.1 Pro model card, though no performance leaks have appeared and the launch was promised this month [1][10]. Surrounding chatter compares GLM-5.2, a 'V4.1/V4-Pro,' Qwen 3.7 Max, and DeepSeek on benchmarks and theory-of-mind prompts, largely as unverified predictions and personal tests [19][43][47][40][58].

## Why it matters (reasoning)
For a studio choosing a model, the concrete adoption signal is GLM-5.2 topping open weights on a public index [8][39], which expands the credible open-weights option set beyond closed APIs. But self-hosting cost is the gating factor: ~400GB memory for a SOTA model [24] means running it locally needs rented GPU infrastructure such as the hosting offers in [7], so for most teams a hosted endpoint remains cheaper per task. The Gemini 3.5 Pro signal [1][10] is a reason to delay any hard commitment to Gemini 3.1 in production until the successor's evals and pricing are public. Second-order: the research notes matter for reliability planning — transformers' weakness at state tracking [51] predicts failures in multi-step agent/stateful tasks (relevant to game logic and tutoring flows), and the SAE dead-feature finding [29] is interpretability plumbing, not a near-term product input. Most model-comparison claims here are X posts and personal prompts [19][43][47], which do not meet a bar for adoption decisions.

## Possibility
Likely: Gemini 3.5 Pro ships within weeks given the model-card tag and a stated month deadline [1][10]; treat exact capabilities as unknown until cards/benchmarks post. Plausible: GLM-5.2's open-weights lead holds on the index near-term and competitors (DeepSeek, Qwen) respond, since the same threads expect DeepSeek to land near or below GLM-5.2 [47][40]. Plausible: multimodal GLM arrives in a later 5.x release [58], but it is not available now. Unlikely (near-term): self-hosting a SOTA-class model becomes cheap for a small studio, given the cited ~400GB footprint [24]. No source states numeric probabilities, so none are given.

## Org applicability — NDF DEV
1) Run a small, reproducible eval of GLM-5.2 via a hosted endpoint (not local) for coding-assist and content/edutech text tasks, scored against your current model on your own prompts — effort med [8][39][7]. 2) Hold off committing new production work to Gemini 3.1 Pro pricing/limits until Gemini 3.5 Pro's model card lands; re-test then — effort low [1][10]. 3) For any agentic/stateful feature (game NPC logic, multi-step tutoring), add explicit external state instead of relying on the model's context memory, per the state-tracking limitation — effort med [51]. 4) For product/marketing copy in edutech apps, avoid foregrounding 'AI' as a selling point given the consumer-turnoff data point — effort low [5]. Skip: self-hosting a SOTA model on your own hardware (cost) [24]; the SAE/mech-interp papers [29][36][18][44] and protein/binder and smart-contract papers [48][49] (out of scope for this studio); treat theory-of-mind and head-to-head X claims as not decision-grade [19][43][47].

## Signals to Watch
- Watch for Gemini 3.5 Pro's official model card and benchmark numbers — the current tag has no perf data yet [1][10].
- Watch Artificial Analysis for whether GLM-5.2's open-weights lead holds as DeepSeek/Qwen respond [39][47].
- Watch GLM multimodal/vision support in a later 5.x release before considering it for image tasks [58].
- Watch alignment/eval discussion on sandbagging classification, relevant to trusting model self-reports in tests [54].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **rxi/microui** — MicroUI – A tiny, portable, immediate-mode UI library written in ANSI C | radar | <https://github.com/rxi/microui> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | pankajkumar_dev | ^942 c50 | [Gemini 3.5 Pro Leaks: Launch Is Getting Closer - Google has started hinting at G](https://x.com/pankajkumar_dev/status/2066879784458887545) |
| radar | Cider9986 | ^911 c476 | [GrapheneOS has been ported to Android 17](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) |
| x | jxmnop | ^667 c23 | [endlessly fascinating how a traditional machine learning background is basically](https://x.com/jxmnop/status/2067061000994795764) |
| x | LLMJunky | ^596 c48 | [I do not believe GPT 5.6 will receive the same level of scrutiny as Fable 5 for ](https://x.com/LLMJunky/status/2066606543164850671) |
| radar | thm | ^507 c259 | [Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://wpvip.com/future-of-the-web-2026/) |
| radar | mrshu | ^497 c215 | [TIL: You can make HTTP requests without curl using Bash /dev/TCP](https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/) |
| x | abacusai | ^466 c25 | [🚨 Host Your Own Local LLM On The Abacus AI SuperComputer Stop being sad about Fa](https://x.com/abacusai/status/2066734555202248728) |
| radar | himata4113 | ^463 c251 | [GLM-5.2 is the new leading open weights model on Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) |
| x | jxmnop | ^410 c41 | [There is a simple reason why Gemini is so much worse than GPT or Claude engineer](https://x.com/jxmnop/status/2067068156410278385) |
| x | haider1 | ^365 c13 | [gemini 3.5 pro seems close to release, given that it already mentioned in the ge](https://x.com/haider1/status/2066626801678311931) |
| x | teortaxesTex | ^327 c7 | [This is a really troublesome benchmark for open models yeah I think they have th](https://x.com/teortaxesTex/status/2067025557162697056) |
| radar | denysvitali | ^320 c78 | [Humiliating IIS servers for fun and jail time](https://mll.sh/humiliating-iis-servers-for-fun-and-jail-time/) |
| x | sanghaviharsh | ^315 c1 | [Strengthening Gujarat’s industrial growth, two major projects were inaugurated a](https://x.com/sanghaviharsh/status/2067097673099087881) |
| radar | lutr | ^309 c127 | [Want your images back? Sure... That'll be $5!](https://www.lutr.dev/want-your-images-back-sure-that-ll-be-5-dollars) |
| radar | headalgorithm | ^302 c93 | [Hacker News but for Independent Blogs](https://bubbles.town/) |
| x | TweetsByAmaka | ^209 c45 | [This girl is a weapon fashioned against the red team… or maybe a mole from the b](https://x.com/TweetsByAmaka/status/2066824084478992572) |
| radar | alok-g | ^198 c105 | [Wolfram Language and Mathematica version 15](https://writings.stephenwolfram.com/2026/06/launching-version-15-of-wolfram-language-mathematica-built-in-useful-ai-lots-of-new-core-functionality/) |
| x | SuryaGanguli | ^179 c7 | [Our new paper lead by @vedanglad w/@AToliasLab "Letting the neural code speak...](https://x.com/SuryaGanguli/status/2066963477445689678) |
| x | teortaxesTex | ^177 c23 | [I think V4.1 Pro will score closely to GLM 5.1, probably noticeably higher both ](https://x.com/teortaxesTex/status/2067047818070565319) |
| x | MrUn1k0d3r | ^172 c2 | [We often talk about EDR evasion, but what about honeypot detection. Nothing new ](https://x.com/MrUn1k0d3r/status/2066932236545355821) |
| x | peterli34923561 | ^168 c1 | [$PLTR --- $PLTR management aggressively raised full-year 2026 revenue guidance f](https://x.com/peterli34923561/status/2066784248032534603) |
| x | VivekIntel | ^165 c1 | [🦅 Claude-OSINT: Give Claude 90+ Recon Capabilities and Turn It Into an OSINT Ope](https://x.com/VivekIntel/status/2066905731295838585) |
| radar | schappim | ^154 c76 | [RFC 10008: The new HTTP Query Method](https://www.rfc-editor.org/info/rfc10008/) |
| x | mehulmpt | ^149 c11 | [Memory required to run video game in 1980s: 4KB Memory required to run SOTA LLM ](https://x.com/mehulmpt/status/2066612276204109951) |
| x | teortaxesTex | ^143 c11 | [Zhipu is basically Tsinghua btw They might have the deepest political goodwill o](https://x.com/teortaxesTex/status/2067236996511068214) |
| x | teortaxesTex | ^133 c14 | [Fr though. Le Chaton Fat memes aside, Europeans have 2 choices. - begin deployme](https://x.com/teortaxesTex/status/2067034152042467432) |
| x | Sauers_ | ^132 c15 | [Does anyone want to give the creator of Le Chaton Fat a A100 or H100 to research](https://x.com/Sauers_/status/2066679416827097561) |
| radar | esychology | ^132 c33 | [Show HN: High-Res Neural Cellular Automata](https://cells2pixels.github.io/) |
| x | james_y_zou | ^125 c2 | [Sparse autoencoders (SAEs) are foundational to much of mechanistic interpretabil](https://x.com/james_y_zou/status/2066626705020891525) |
| x | teortaxesTex | ^121 c7 | [OK. how does this help India compete in AGI?](https://x.com/teortaxesTex/status/2067043767488479300) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@pankajkumar_dev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 942 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/pankajkumar_dev/status/2066879784458887545">View @pankajkumar_dev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gemini 3.5 Pro Leaks: Launch Is Getting Closer - Google has started hinting at Gemini 3.5 Pro, with a &quot;3.5 Pro coming soon&quot; tag appearing on the Gemini 3.1 Pro model card. - Expect stronger vision, be”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google added a '3.5 Pro coming soon' tag on the Gemini 3.1 Pro model card, previewing stronger vision, multimodal reasoning, SVG/frontend generation, stricter safety filters, and a higher price than 3.1 Pro.</dd>
      <dt>Why interesting</dt>
      <dd>Better SVG and frontend generation directly benefits UI prototyping and e-learning asset work; a laziness fix on long tasks improves reliability for complex code generation.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Benchmark Gemini 3.5 Pro against current tools on SVG output and long-context coding at launch before committing to the higher API pricing.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/pankajkumar_dev/status/2066879784458887545" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jxmnop</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 667 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jxmnop/status/2067061000994795764">View @jxmnop on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“endlessly fascinating how a traditional machine learning background is basically not that helpful for modern AI. we use deep NNs and do SGD with one of two losses. most day-to-day work lies in abstrac”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A practitioner argues modern AI work is not classical ML theory — it is composing pipelines of data, models, and rules, with pre-training/RL/post-training being different topologies of those three primitives.</dd>
      <dt>Why interesting</dt>
      <dd>This reframes AI integration as a systems and pipeline engineering problem — a skill set a small dev team already holds — not a prerequisite for ML PhDs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When scoping AI features, the studio can frame them as data/model/rules pipeline design problems and skip over-hiring for classical ML expertise.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jxmnop/status/2067061000994795764" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LLMJunky</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 596 · 💬 48</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LLMJunky/status/2066606543164850671">View @LLMJunky on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I do not believe GPT 5.6 will receive the same level of scrutiny as Fable 5 for a litany of reasons, and no, they're not all political. The primary one being the fact that I suspect the guardrails on ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@LLMJunky argues GPT models have stronger jailbreak resistance than Anthropic's Fable/Opus/Sonnet lines, pointing to an unclaimed $25,000 OpenAI bounty and zero confirmed universal jailbreaks on GPT 5.5 vs. day-one 'liberation' posts on every Fable and Opus 4.x release.</dd>
      <dt>Why interesting</dt>
      <dd>For any user-facing LLM feature (e-learning, XR chat), guardrail strength is a concrete risk factor for content moderation failures — not just a benchmark footnote.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When selecting an LLM provider for user-facing studio features, add guardrail track record as a formal evaluation criterion alongside capability scores.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LLMJunky/status/2066606543164850671" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@abacusai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 466 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/abacusai/status/2066734555202248728">View @abacusai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 Host Your Own Local LLM On The Abacus AI SuperComputer Stop being sad about Fable and control your destiny by hosting your own LLM - host open source LLMs like Qwen and Gemma - create chat bots or a”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Abacus AI's SuperComputer lets teams self-host open-source LLMs (Qwen, Gemma) as always-on APIs or chatbots, pitched as a hedge after Anthropic's Fable model was discontinued.</dd>
      <dt>Why interesting</dt>
      <dd>Self-hosting LLMs on managed compute cuts dependency on third-party model availability — useful when a model the studio relies on gets deprecated.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can test Abacus AI SuperComputer to run a local LLM for NPC dialogue, e-learning chatbots, or internal tools without external API dependency.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/abacusai/status/2066734555202248728" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jxmnop</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 410 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jxmnop/status/2067068156410278385">View @jxmnop on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“There is a simple reason why Gemini is so much worse than GPT or Claude engineers at OpenAI or Ant can read incoming user queries. all the data is visible but at Google there are tons of privacy restr”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An anonymous X user speculates that Gemini lags behind GPT and Claude because Google's internal privacy policies block engineers from reading real user queries, forcing model development without visibility into live usage patterns.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jxmnop/status/2067068156410278385" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@haider1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 365 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/haider1/status/2066626801678311931">View @haider1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“gemini 3.5 pro seems close to release, given that it already mentioned in the gemini 3.1 pro model card but i'm still curious because google promised it this month, so, strangely, there are no leaks y”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Gemini 3.5 Pro is likely imminent — it's already cited in the Gemini 3.1 Pro model card and Google committed to a June release, yet no leaks have appeared, which breaks the usual pre-release pattern.</dd>
      <dt>Why interesting</dt>
      <dd>If Gemini 3.5 Pro ships this month, it resets the cost/capability benchmark for choosing models in AI integrations the studio is currently planning.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Hold model-tier decisions for any new AI feature in progress until the Gemini 3.5 Pro release drops and pricing is confirmed.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/haider1/status/2066626801678311931" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@teortaxesTex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 327 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/teortaxesTex/status/2067025557162697056">View @teortaxesTex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is a really troublesome benchmark for open models yeah I think they have the best RL in China now, hard to admit but true GLM 5.2 also has… cheek. it even has COPE CAPACITY AGI at home? https://t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>GLM 5.2 (Zhipu AI) tops a difficult open-model benchmark, with the author crediting Chinese labs for currently leading in RL training techniques.</dd>
      <dt>Why interesting</dt>
      <dd>GLM 5.2 is emerging as a capable open model worth benchmarking against paid APIs the studio uses for inference tasks.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run GLM 5.2 on a sample of the studio's current inference workloads and compare output quality and cost against the paid model in use.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/teortaxesTex/status/2067025557162697056" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sanghaviharsh</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 315 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sanghaviharsh/status/2067097673099087881">View @sanghaviharsh on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Strengthening Gujarat’s industrial growth, two major projects were inaugurated and launched in the presence of Chief Minister Shri @Bhupendrapbjp Ji ▪️ Groundbreaking of Hitachi Energy’s new Power Tra”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Gujarat's Chief Minister inaugurated a Hitachi Energy power transformer factory (₹2,000 crore) and a Lubrizol/Grasim CPVC resin plant — both framed as Make in India industrial investments.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sanghaviharsh/status/2067097673099087881" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
