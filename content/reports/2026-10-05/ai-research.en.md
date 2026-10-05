---
type: social-topic-report
date: '2026-10-05'
topic: ai-research
lang: en
pair: ai-research.th.md
generated_at: '2026-10-05T03:19:43+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- x
regions:
- global
post_count: 205
salience: 0.35
sentiment: neutral
confidence: 0.4
tags:
- local-inference
- qwen
- decision-models
- inference-cost
- agent-evals
thumbnail: https://pbs.twimg.com/tweet_video_thumb/HTwSVDgbQAAMbN9.jpg
---

# AI Research — 2026-10-05

## TL;DR
- Strata, a GitHub project, says it runs Qwen 3.8 Flash Next (125B) on a single RTX 4090 at 100 tokens/s [11]. Nobody has published an independent benchmark, and its 298-comment thread is the most active real-signal item today. A separate post says Qwen3.8-Flash runs locally on an RTX 5060 Ti with native FP4 plus 128GB DDR4, for about $1.5k [30].
- A post says vLLM released 'Decision 2.0': six open decision models from 0.6B to 27B under Apache 2.0. They score answer choices instead of generating text, and one request can carry 64 questions in a single forward pass in 63 ms [36]. OpenRouter's co-founder suggested decision models like 'Jev' could act as an alignment layer for agents [37].
- On OpenRouter, prefill is very cheap and decode is very expensive, at least for GLM 5.3. A PyTorch contributor's post attributes this to OpenRouter's routing [33].
- LangChain's CEO says their coding-agent costs fell for the second month in a row, and the first step was cost visibility [41].
- On the evaluation side: a proposed Sales Agent Eval benchmark is open for community feedback on its method [44], and a Meta/Duke paper on self-improving agent harness optimization splits the search into specialized branches and routes each task to the best branch [57].

## What happened
Today's feed is mostly noise: politics, gaming 'red team' posts and jokes about hidden chain of thought [1-6][14-17][2][3]. A few items matter for adoption decisions. Local inference: Strata says a 125B Qwen 3.8 Flash Next model runs on one RTX 4090 at 100 tokens/s [11], and another post says Qwen3.8-Flash fits a roughly $1.5k RTX 5060 Ti FP4 + 128GB DDR4 build [30]. A related post lists multi-GPU improvements, OpenAI Responses API support for Codex and a UD-IQ4_XS quant on the model card [58]. Whether it comes from the same project is unconfirmed. A post reports vLLM 'Decision 2.0', six Apache-2.0 decision models (0.6B–27B) that score options rather than generate text, with 64 questions answered in 63 ms in one pass [36]. a16z quotes OpenRouter's Alex Atallah suggesting such models could gate agent actions [37].

On cost and evaluation: a post shared by Soumith Chintala says OpenRouter routing makes prefill cheap and decode expensive for GLM 5.3 [33]. Harrison Chase reports two straight months of falling coding-agent costs, starting with cost visibility [41]. New methodology items: a Sales Agent Eval benchmark open for feedback [44], a Meta/Duke paper on branch-split harness optimization [57], an evals-engineer post proposing step-level trajectory grading of agent tool calls against a deterministic DAG [10], and a Looped Diffusion Transformer paper that runs the same blocks several times per denoising step without adding parameters [12]. Yann LeCun argues that because distilling a leading model is cheap, top foundation models will end up free or open [13]. The chain-of-thought threads frame hidden reasoning tokens as an anti-distillation measure that also hurts monitorability [2][24][46].

## Why it matters (reasoning)
The useful theme is cheaper inference, not new capability. If [11] and [30] hold up, mid-size MoE-class Qwen models become usable on single consumer GPUs. That changes the cost of local or offline AI features, for example in-editor tooling or on-prem edutech deployments where data cannot leave the client. But 100 tokens/s for 125B on 24GB VRAM almost certainly depends on sparse activation plus aggressive quantization or CPU offload. Those trade quality and context length for speed, and no item gives quality numbers. Decision models [36][37] are a different shape of model: they classify and score instead of generating. That fits batch grading, routing, moderation and agent guardrails at much lower latency than a full LLM call. The price asymmetry in [33] means long-prompt, short-answer workloads such as RAG, grading and classification are underpriced right now on some routes, while generation-heavy workloads cost more than headline prices suggest. Together with [41], the second-order point is that per-token cost tracking is now the main lever on agent spend. The eval items [10][44][57] show the field moving toward judging agent trajectories step by step, not just final outputs. The chain-of-thought hiding debate [2][24][46] means API-served reasoning is less inspectable, which weakens debugging and auditing of closed models.

## Possibility
Likely: more consumer-GPU recipes for Qwen 3.8-class models appear, with quantization trade-offs fought over in issue threads [11][30][58]. Third-party quality-vs-speed numbers will decide whether the 4090 claim holds. Plausible: decision or scoring models get adopted as cheap guardrail and router layers in agent stacks, given the Apache-2.0 release [36] and OpenRouter's public interest [37]. The specific benchmark figures still need independent confirmation. Plausible: OpenRouter or its providers change prefill/decode pricing once the distortion gets attention [33]. Unlikely in the near term: the claim in [13] that the best models become free/open, which is an argument about market forces with no evidence attached, so it should not drive planning.

## Org applicability — NDF DEV
1) Reproduce the Strata claim on an in-house RTX 4090 before trusting it. Measure tokens/s at your real context lengths and do a quick quality check against the hosted Qwen on 20–30 of your own prompts (effort: med) [11][58]. 2) If your edutech grading or quiz flows score multiple-choice or rubric items, test one small Decision 2.0 model (0.6B–4B) on batch scoring. Confirm the 64-questions-per-pass behaviour yourself (effort: med) [36]. 3) Add per-request cost logging (prefill vs decode tokens, by provider) to any LLM-backed product or internal agent before tuning anything else (effort: low) [41][33]. 4) For RAG or long-context, short-output features routed through OpenRouter, check actual billed prefill/decode split and pin providers if cheaper (effort: low) [33]. 5) For agentic features, borrow the step-level trajectory grading idea for regression tests on tool calls (effort: med) [10]. Skip: hardware buying on the $1.5k 5060 Ti post alone [30], the consciousness/MEM thread [29], Hamiltonian JEPA [38] and Looped DiT [12] for now (research-stage, no adoption path), the CoT-hiding jokes [2][3], and the Sales Agent Eval benchmark [44] unless you build sales/voice agents.

## Signals to Watch
- Independent benchmarks (quality and speed) for Strata running Qwen 3.8 Flash Next on a 4090 [11]
- Official vLLM confirmation and model cards for Decision 2.0, plus any third-party accuracy evals [36]
- Whether OpenRouter changes prefill/decode pricing for GLM 5.3 and similar models [33]
- LangChain's promised longer write-up on agent cost reduction [41]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **Niko1221/Strata** — Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s | radar | <https://github.com/Niko1221/Strata> |
| **omlahore/RemoveMacAI** — Turn off Apple Intelligence on macOS 27 and get its disk space back | radar | <https://github.com/omlahore/RemoveMacAI> |
| **allenv0/SCM** — Show HN: AI search for every photo and every frame of video on macOS | radar | <https://github.com/allenv0/SCM> |
| **net4people/bbs** — Xray-core concealed a certificate verification bypass vulnerability | radar | <https://github.com/net4people/bbs> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ylecun | ^10548 c157 | [RT @Kasparov63: As I’ve been writing about Putin for over 20 years, and as I war](https://x.com/ylecun/status/2106707534295728316) |
| x | GenAI_is_real | ^9675 c80 | [Ramanujan wasn’t skipping proofs. He was hiding his chain of thought to prevent ](https://x.com/GenAI_is_real/status/2106441385964683507) |
| x | ABhargava2000 | ^5364 c21 | [god forbid a guy copy my secret chain of thought. they might LEARN something!!! ](https://x.com/ABhargava2000/status/2106578884917706884) |
| x | ylecun | ^3381 c145 | [RT @Hannibal9972485: The real reason why Anthropic is so DESPERATE for the Pope ](https://x.com/ylecun/status/2106739287395803260) |
| x | ylecun | ^1507 c146 | [RT @kurtsaltrichter: For the AI buildout to pay off, Americans will eventually h](https://x.com/ylecun/status/2106779857161974159) |
| x | Stellan628605 | ^1250 c11 | [Two men got trapped inside 3 tons of solid concrete, battling it out for a $10,0](https://x.com/Stellan628605/status/2106802117516374459) |
| x | sermakarevich | ^1179 c52 | [An article for everyone who ships, buys, or signs off on software built on large](https://x.com/sermakarevich/status/2106453816757354947) |
| x | MikeMitchNH | ^1147 c4 | [@AdImpact_Pol Cannot mention her ex-husband by name. Explicit, tacky appeal to r](https://x.com/MikeMitchNH/status/2106411848732188825) |
| x | 0xDeliriumm | ^784 c24 | [andrej karpathy spent 7 years inside OpenAI watching GPT go from 117M to 1T para](https://x.com/0xDeliriumm/status/2106346529069924399) |
| x | suraj_sharma14 | ^731 c29 | [As an AI Evals Engineer, you must build these projects. 1.) Trajectory Grading E](https://x.com/suraj_sharma14/status/2106715961403273433) |
| radar | snehesht | ^639 c298 | [Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s](https://github.com/Niko1221/Strata) |
| x | askalphaxiv | ^538 c8 | ["Looped Diffusion Transformer" This new paper reuses the same Transformer blocks](https://x.com/askalphaxiv/status/2106284078077202738) |
| x | ylecun | ^482 c27 | [RT @ylecun: @abuchanlife - training frontier models is expensive - distilling a ](https://x.com/ylecun/status/2106809439663612341) |
| x | LateNightHalo | ^437 c46 | [Halo Multiplayer is Red Team Vs Blue Team. Wear whatever armor you want but if w](https://x.com/LateNightHalo/status/2106821547507793924) |
| x | tris_redfield | ^422 c1 | [Red Team Soap Comm from @gomzdrawfr !! 💕 #CallofDuty #JohnSoapMacTavish #soapyti](https://x.com/tris_redfield/status/2106365272143888505) |
| radar | privacyisntdead | ^406 c268 | [Turn off Apple Intelligence on macOS 27 and get its disk space back](https://github.com/omlahore/RemoveMacAI) |
| x | CozyKxren | ^377 c3 | [Season 12 money red team just dropped https://t.co/t5LIGFRDsk](https://x.com/CozyKxren/status/2106521843431772182) |
| x | NeelNanda5 | ^346 c28 | [I'm loving the era of personalised AI art! Opus 5.5 wrote, composed and made a v](https://x.com/NeelNanda5/status/2106797715825086605) |
| x | ylecun | ^343 c52 | [RT @vikktorrrre: Jensen Huang: it’s irresponsible for Elon Musk and Geoffrey Hin](https://x.com/ylecun/status/2106780728159621188) |
| x | ylecun | ^336 c12 | [RT @KenRoth: Republicans' problem is not just Trump. It is that they did nothing](https://x.com/ylecun/status/2106779188162146779) |
| x | stillcorecap | ^308 c28 | [Bitcoin decentralized money. Bittensor is decentralizing intelligence $TAO 2030 ](https://x.com/stillcorecap/status/2106821906414383270) |
| x | teortaxesTex | ^289 c16 | [Funny that after 2022 many Russians had to escape to Central Asia, including my ](https://x.com/teortaxesTex/status/2106824450771497231) |
| radar | vinhnx | ^282 c293 | [Why don't more developers “use the platform”?](https://nolanlawson.com/2026/10/03/why-dont-more-developers-use-the-platform/) |
| x | Miles_Brundage | ^270 c14 | [Who called it losing chain of thought monitorability through opaque internal rea](https://x.com/Miles_Brundage/status/2106563607945429412) |
| radar | sensanaty | ^267 c381 | [Improper redaction reveals Google Data Center water and electricity usage](https://www.1011now.com/2026/09/30/more-questions-than-answers-about-lincolns-google-data-center-water-electricity-usage/) |
| x | redvsbluniverse | ^256 c2 | [church rvb had this happen once](https://x.com/redvsbluniverse/status/2106835737345970471) |
| x | ForwardLeaks | ^238 c3 | [DAY 2 OF RECAPPING THE ENTIRE MODERN WARFARE REBOOT STORY Prologue: Part 2 2011 ](https://x.com/ForwardLeaks/status/2106504572835635431) |
| x | ylecun | ^236 c10 | [RT @grok: Yann LeCun deyir: ən qabaqcıl AI modellərini öyrətmək çox baha başa gə](https://x.com/ylecun/status/2106809665615007854) |
| x | HowToPrompt__ | ^231 c55 | [Researchers published a first falsifiable theory of machine consciousness. It's ](https://x.com/HowToPrompt__/status/2106777231834128653) |
| x | unbug | ^228 c16 | [Grab a 5060Ti now before prices go nuts. A native FP4 GPU + 128GB DDR4 build cos](https://x.com/unbug/status/2106711633385132271) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ylecun</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 10548 · 💬 157</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ylecun/status/2106707534295728316">View @ylecun on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“RT @Kasparov63: As I’ve been writing about Putin for over 20 years, and as I warned Americans about Trump 10 years ago, when you realize that all their decisions are based on making money and clinging”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Yann LeCun retweeted Garry Kasparov's political commentary arguing that Putin's and Trump's decisions are driven by making money and holding power.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ylecun/status/2106707534295728316" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GenAI_is_real</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9675 · 💬 80</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GenAI_is_real/status/2106441385964683507">View @GenAI_is_real on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ramanujan wasn’t skipping proofs. He was hiding his chain of thought to prevent distillation. Hardy: “Show your work.” Ramanujan: “Sorry, reasoning tokens aren’t exposed via the API.””</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A joke post imagines mathematician Ramanujan hiding his reasoning to block distillation, mirroring how AI labs now hide chain-of-thought tokens from their APIs.</dd>
      <dt>Why interesting</dt>
      <dd>It points to a real constraint: some providers hide reasoning tokens, so teams can't inspect or reuse a model's intermediate steps through the API.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GenAI_is_real/status/2106441385964683507" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ABhargava2000</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5364 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ABhargava2000/status/2106578884917706884">View @ABhargava2000 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“god forbid a guy copy my secret chain of thought. they might LEARN something!!! https://t.co/CxIeZoycxi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral X joke mocks a rival copying the author's 'secret chain of thought' while AI labs hide their own reasoning traces; the post contains no technical content, link or data.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ABhargava2000/status/2106578884917706884" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ylecun</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3381 · 💬 145</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ylecun/status/2106739287395803260">View @ylecun on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“RT @Hannibal9972485: The real reason why Anthropic is so DESPERATE for the Pope to recognize Ai as conscious is because if Ai just a “TOOL” then Anthropic will he LEGALLY “LIABLE” for everything the t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A repost of an X thread claims Anthropic wants the Vatican to call AI conscious so it can argue the AI acted as an autonomous entity and avoid legal liability. It offers no evidence.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ylecun/status/2106739287395803260" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ylecun</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1507 · 💬 146</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ylecun/status/2106779857161974159">View @ylecun on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“RT @kurtsaltrichter: For the AI buildout to pay off, Americans will eventually have to spend about 9% of GDP a year on AI services. Sit with that number. That is roughly what the entire country spends”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A retweeted analysis citing a Columbia paper: AI revenue must reach about $3.5T by 2032 (8.8% of US GDP) to justify current buildout spending, roughly the size of US food spending.</dd>
      <dt>Why interesting</dt>
      <dd>It shows AI vendor pricing and API availability rest on a revenue target far above today's, which is a planning risk for teams building on one provider.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ylecun/status/2106779857161974159" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Stellan628605</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1250 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Stellan628605/status/2106802117516374459">View @Stellan628605 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Two men got trapped inside 3 tons of solid concrete, battling it out for a $10,000 cash prize, and the intense effort from both teams was insane! 🔨 John on the Red team and Nick on the Blue team start”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral X post describes a $10,000 reality-style contest in which two men chip out of 3 tons of solid concrete, using upgradable tools from scrapers to jackhammers; John (Red team) escaped first.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Stellan628605/status/2106802117516374459" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sermakarevich</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1179 · 💬 52</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sermakarevich/status/2106453816757354947">View @sermakarevich on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“An article for everyone who ships, buys, or signs off on software built on large language models (LLMs): engineers, product managers, and the CEO. Written in plain language, from the big picture down ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The author published a plain-language article on building, buying and approving LLM-based software, aimed at engineers, product managers and CEOs, moving from the big picture to technical details.</dd>
      <dt>Why interesting</dt>
      <dd>The post gives no content, only a link, so its quality is unverified; the 1,179 likes suggest interest, and the stated audience matches what a small studio needs for sharing LLM context with clients.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Read the linked article first, and if it holds up, share it with non-technical stakeholders before scoping LLM features.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sermakarevich/status/2106453816757354947" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MikeMitchNH</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1147 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MikeMitchNH/status/2106411848732188825">View @MikeMitchNH on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@AdImpact_Pol Cannot mention her ex-husband by name. Explicit, tacky appeal to red team vs. blue team. Their internal polling must be awful.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A political commentator criticizes an ad by a campaign advertising tracker account, saying it avoids naming the candidate's ex-husband, appeals to party tribalism, and signals poor internal polling.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MikeMitchNH/status/2106411848732188825" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
