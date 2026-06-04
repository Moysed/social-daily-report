---
type: social-topic-report
date: '2026-06-04'
topic: ai-research
lang: en
pair: ai-research.th.md
generated_at: '2026-06-04T03:38:09+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- rss
- x
regions:
- global
post_count: 228
salience: 0.42
sentiment: mixed
confidence: 0.55
tags:
- gemma-4
- multimodal
- benchmaxxing
- kv-cache
- model-eval
- open-weights
thumbnail: https://pbs.twimg.com/media/HJ5Xk9oWIAAweTo.jpg
---

# AI Research — 2026-06-04

## TL;DR
- Google released Gemma 4 12B, an encoder-free unified multimodal model; commentary notes it drops the separate vision encoder at no benchmark penalty and no gain, sitting on the existing Gemma 4 trend [3][35].
- Minimax M3 results posted to GBENCH: rated a solid model but behind several Chinese labs' April releases, with an explicit warning about benchmaxxing (training to the benchmark) [23].
- Active research directions surfaced: on-policy distillation for RL-on-LLMs [43] and a KV-cache method that keeps only tokens likely to matter later to bound long-generation memory [51].
- A viral 'MIT solved AI memory' claim (paper dated 2025-12-31) is unverified and reads as hype; treat with caution [58].
- Genuine research signal is thin today — the feed is dominated by red-team/security tool lists and AI-bubble takes, not papers or eval suites [2][8][15][28][44].

## What happened
The one concrete model release is Gemma 4 12B, described by Google as a unified, encoder-free multimodal model [3]; a third-party reaction frames the result as removing the vision encoder with no measurable benchmark change in either direction, in line with prior Gemma 4 variants [35]. On evaluation, Minimax M3 results went live on GBENCH and were called solid but slightly behind other Chinese labs' April releases, with a direct caution about benchmaxxing [23]. Method-level items include on-policy distillation flagged as an active RL-for-LLMs direction [43] and a paper on selectively retaining KV-cache tokens to limit memory growth during long text generation [51]. An interpretability paper offering a mechanism for subliminal learning was also shared [16].

## Why it matters (reasoning)
Gemma 4 12B [3][35] matters for a studio that ships edutech and XR: an encoder-free 12B multimodal model is a candidate for smaller-footprint or on-device inference, and the 'no penalty, no gain' framing suggests architectural simplification rather than a capability jump — useful for engineering cost, not a reason to expect better outputs. The Minimax M3 benchmaxxing warning [23] is the most actionable adoption lesson here: leaderboard placement is being gamed, so headline scores should not drive model selection without task-specific evaluation. The KV-cache token-retention work [51] addresses a real cost driver for long-context chat or tutoring features, where cache growth dominates memory. Second-order: the volume of red-team tooling [28][44][52] and bubble/budget commentary [2][8][15] relative to actual papers indicates attention is rotating toward cost control and security posturing, not new capability — consistent with the benchmaxxing concern.

## Possibility
Likely: encoder-free multimodal designs spread across small open-weight models if Gemma 4 holds up, since the reported tradeoff is simpler architecture at equal benchmarks [3][35]. Plausible: benchmaxxing concerns push teams and benchmark maintainers toward private or task-specific eval suites, given the explicit M3 warning [23]. Plausible: on-policy distillation [43] and selective KV-cache retention [51] mature into standard pipeline components for cost-sensitive deployments. Unlikely (as stated): the 'MIT solved AI memory' claim represents a settled result — it is a single viral post citing an unverified paper [58]. No source states a numeric probability, so none is given.

## Org applicability — NDF DEV
Evaluate Gemma 4 12B for edutech/XR multimodal features where a smaller open-weight model with image input is useful; run it on your own tasks, not benchmarks (effort: med) [3][35]. Adopt a standing rule to validate any candidate model on internal eval cases before adoption, given documented benchmaxxing on public leaderboards (effort: low) [23]. If building long-context tutoring or chat, track the KV-cache token-retention approach as a cost lever before committing to large context windows (effort: low to track, high to implement) [51]. Skip for now: the red-team/security tool lists [28][44][52], AI-bubble and budget-cap hot takes [2][8][15], and the unverified 'MIT solved memory' claim [58] — none change a model or method decision today.

## Signals to Watch
- Whether GBENCH or others publish private/held-out eval suites in response to benchmaxxing [23].
- Adoption of encoder-free multimodal beyond Gemma 4 — does the no-penalty tradeoff hold in other models [35].
- On-policy distillation moving from research direction to documented production pipelines [43].
- Whether the 'MIT memory' paper is independently reproduced before being treated as real [58].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **duanebester/gooey** — Gooey: A GPU-accelerated UI framework for Zig | radar | <https://github.com/duanebester/gooey> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | maxvonhippel | ^1565 c30 | [Anthropic rejected me as well. They asked me to solve a problem that was obvious](https://x.com/maxvonhippel/status/2061913633593110582) |
| x | kushika_twt | ^1004 c105 | [Microsoft pulled the plug on Claude. Starbucks’ AI can't count cups. Uber burned](https://x.com/kushika_twt/status/2062164836365332560) |
| radar | rvz | ^726 c296 | [Gemma 4 12B: A unified, encoder-free multimodal model](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) |
| radar | cloud8421 | ^603 c223 | [Elixir v1.20: Now a gradually typed language](https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/) |
| x | ZoomerHistorian | ^574 c17 | [Never been anything but nice to eachother and always got on in private and publi](https://x.com/ZoomerHistorian/status/2061720907710669243) |
| radar | Tomte | ^522 c162 | [I was recently diagnosed with anti-NMDA receptor encephalitis](https://burntsushi.net/encephalitis/) |
| radar | pentagrama | ^407 c188 | [DaVinci Resolve 21](https://www.blackmagicdesign.com/products/davinciresolve/whatsnew) |
| radar | pdyc | ^389 c502 | [Uber's $1,500/month AI limit is a useful signal for AI tool pricing](https://simonwillison.net/2026/Jun/3/uber-caps-usage/) |
| x | teortaxesTex | ^354 c10 | [&gt; User, y-you cheated on me… with a *cheap Chinese model*?! https://t.co/Tmhj](https://x.com/teortaxesTex/status/2062182020634067197) |
| radar | lordleft | ^280 c507 | [Artificial intelligence is not conscious – Ted Chiang](https://www.theatlantic.com/philosophy/2026/06/no-artificial-intelligence-is-not-conscious/687378/) |
| radar | volemo | ^259 c145 | [ESP32-S31](https://www.espressif.com/en/products/socs/esp32-s31) |
| radar | SGran | ^226 c134 | [A Post-Quantum Future for Let's Encrypt](https://letsencrypt.org/2026/06/03/pq-certs) |
| x | TheAhmadOsman | ^193 c8 | [Step-By-Step LLM Engineering Projects Roadmap - Build a tokenizer - Learn embedd](https://x.com/TheAhmadOsman/status/2062343535144436073) |
| x | tom_doerr | ^177 c2 | [Curated offensive security skills to turn Claude into a context-aware red team o](https://x.com/tom_doerr/status/2062139149432344674) |
| x | nicrypto | ^174 c28 | [Last year: "Embrace AI or your job is at risk." This year: "Please stop, you're ](https://x.com/nicrypto/status/2062067713825267787) |
| x | NeelNanda5 | ^164 c4 | [I had a lot of fun working on this paper - we found an elegant story for why sub](https://x.com/NeelNanda5/status/2062260199822639314) |
| x | Huangyu58589918 | ^158 c8 | [Starting as a Student Researcher at @GoogleDeepMind on June 8! I’ll be in NYC th](https://x.com/Huangyu58589918/status/2062229610390053154) |
| radar | rguiscard | ^147 c73 | [U.S. to Dismantle System Tracking Atlantic Currents That Are at Risk of Collapse](https://e360.yale.edu/digest/trump-ooi-amoc) |
| x | mhdnauvalazhar | ^146 c13 | [Building an agnostic UI library for AI apps. It works as an interface companion ](https://x.com/mhdnauvalazhar/status/2061779894191988988) |
| x | Hey_Aditii | ^141 c17 | [🤖 𝟮𝟵 𝗖𝗟𝗔𝗨𝗗𝗘 𝗦𝗛𝗢𝗥𝗧𝗖𝗨𝗧𝗦 🔖 𝗦𝗔𝗩𝗘 𝗧𝗛𝗜𝗦 𝗕𝗘𝗙𝗢𝗥𝗘 𝗬𝗢𝗨 𝗙𝗢𝗥𝗚𝗘𝗧 If you're using AI and not u](https://x.com/Hey_Aditii/status/2062036557377527810) |
| radar | ksec | ^141 c49 | [Gooey: A GPU-accelerated UI framework for Zig](https://github.com/duanebester/gooey) |
| x | VoidAsuka | ^138 c3 | [the best cookbook about how to train a sota llm right now.](https://x.com/VoidAsuka/status/2061967754010493140) |
| x | leo_linsky | ^132 c15 | [Minimax M3 results are now live on GBENCH: It's a solid model, but the other Chi](https://x.com/leo_linsky/status/2061647734336319739) |
| x | vikktorrrre | ^130 c69 | [did you know AI is older than your forefathers? you obviously don't, neither did](https://x.com/vikktorrrre/status/2062183220939047127) |
| x | VivekIntel | ^126 c2 | [Awesome OSINT Arsenal — 750+ OSINT & Cybersecurity Tools in One Repository 💀🔥 On](https://x.com/VivekIntel/status/2061679190420902258) |
| x | NineIronCapital | ^116 c5 | [@BavStallion Red team and blue team.](https://x.com/NineIronCapital/status/2061983976575877574) |
| x | RishiUvaach | ^112 c26 | [𝗔𝗜 𝗵𝗮𝘀 𝗮 𝗹𝗮𝗻𝗴𝘂𝗮𝗴𝗲, 𝗮𝗻𝗱 𝗴𝘂𝗲𝘀𝘀𝗶𝗻𝗴 𝗶𝘁 𝗴𝗲𝘁𝘀 𝗲𝘅𝗽𝗲𝗻𝘀𝗶𝘃𝗲. Your meeting-room cheat sheet](https://x.com/RishiUvaach/status/2061990502111887849) |
| x | VivekIntel | ^106 c2 | [🔴⚔️ RED TEAM TOOLS 1.🕸️ BloodHound 2.📈 BeRoot 3.🎯 Gophish 4.👑 King Phisher 5.🔗 E](https://x.com/VivekIntel/status/2061655639995396120) |
| x | 47fucb4r8c69323 | ^100 c9 | [The frontier labs must be freaking out. They know they need to pivot to post-tra](https://x.com/47fucb4r8c69323/status/2062027041390973312) |
| x | teortaxesTex | ^100 c5 | [didn't even need to check the account location info, the "better CUDA kernels sh](https://x.com/teortaxesTex/status/2062142338621727208) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@maxvonhippel</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1565 · 💬 30</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/maxvonhippel/status/2061913633593110582">View @maxvonhippel on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anthropic rejected me as well. They asked me to solve a problem that was obviously meant to be solved via mech interp. I said you clearly want me to use mech interp but I don’t believe in mech interp,”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A researcher publicly shared that Anthropic rejected them after refusing to engage with mechanistic interpretability on its own terms during a hiring interview.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/maxvonhippel/status/2061913633593110582" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kushika_twt</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1004 · 💬 105</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kushika_twt/status/2062164836365332560">View @kushika_twt on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft pulled the plug on Claude. Starbucks’ AI can't count cups. Uber burned billions on AI with little to show for it. Amazon shut down its AI leaderboard. the AI bubble will burst any minute now”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X post strings together unverified anecdotes — Microsoft dropping Claude, Starbucks AI miscounting cups, Uber's AI losses, Amazon closing an AI leaderboard — to argue the AI bubble is about to collapse.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kushika_twt/status/2062164836365332560" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ZoomerHistorian</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 574 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ZoomerHistorian/status/2061720907710669243">View @ZoomerHistorian on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Never been anything but nice to eachother and always got on in private and public for years, completely bizarre red team blue team behaviour that’s completely at odds with how Anglos act to eachother ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user comments on political disagreement behavior patterns among Anglo individuals, noting a disconnect between private and public conduct.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ZoomerHistorian/status/2061720907710669243" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@teortaxesTex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 354 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/teortaxesTex/status/2062182020634067197">View @teortaxesTex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&amp;gt; User, y-you cheated on me… with a *cheap Chinese model*?! https://t.co/TmhjZvf0zk”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A meme post mocking users who switch from a premium AI model to a cheaper Chinese alternative, framed as a dramatic romantic betrayal.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/teortaxesTex/status/2062182020634067197" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheAhmadOsman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 193 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheAhmadOsman/status/2062343535144436073">View @TheAhmadOsman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Step-By-Step LLM Engineering Projects Roadmap - Build a tokenizer - Learn embeddings - Implement RoPE / ALiBi - Hand-wire attention - Build MHA - Build a Transformer block - Train a mini-former - Comp”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A practitioner published a 30-step LLM engineering roadmap covering fundamentals (tokenizer, attention, RoPE) through production topics (KV cache, quantization, RAG, RLHF, red-teaming) with a call to release work as open-source.</dd>
      <dt>Why interesting</dt>
      <dd>This roadmap doubles as a skill-gap checklist — teams can pinpoint which LLM internals they understand vs. treat as a black box, useful before building RAG or agent features.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Map the roadmap against the studio's current AI work to identify which topics (e.g. eval harnesses, quantization, MoE) are worth a focused internal study session.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheAhmadOsman/status/2062343535144436073" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@tom_doerr</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 177 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/tom_doerr/status/2062139149432344674">View @tom_doerr on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Curated offensive security skills to turn Claude into a context-aware red team operator https://t.co/4ZPWxmJRDM https://t.co/XT5IPTv9s5”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer published a curated collection of offensive-security system prompts that configure Claude to operate as a context-aware red team agent, hosted on GitHub.</dd>
      <dt>Why interesting</dt>
      <dd>Demonstrates a clean pattern for giving Claude domain-specific operator personas via curated skill sets — directly applicable to how the studio configures its own AI agents.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Study the prompt architecture to improve the studio's own domain-specific Claude agent configs (code review, QA, XR UX audit, etc.).</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/tom_doerr/status/2062139149432344674" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nicrypto</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 174 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nicrypto/status/2062067713825267787">View @nicrypto on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Last year: &quot;Embrace AI or your job is at risk.&quot; This year: &quot;Please stop, you're blowing the budget.&quot; Walmart capped AI access. Uber hit its annual AI budget limit before summer. Amazon shut down its A”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Walmart, Uber, and Amazon hit or capped AI budgets before mid-year; Google's CEO confirmed companies exhaust annual token budgets by May, driven mainly by agentic AI consuming ~1,000x more tokens than basic AI.</dd>
      <dt>Why interesting</dt>
      <dd>Any studio running background agents or automated agentic pipelines faces the same unbounded cost risk — no cap means a blank cheque to the API provider.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Set hard monthly token spend limits and usage alerts on every AI API key the studio uses before expanding any agentic workflow.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nicrypto/status/2062067713825267787" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NeelNanda5</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 164 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NeelNanda5/status/2062260199822639314">View @NeelNanda5 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I had a lot of fun working on this paper - we found an elegant story for why subliminal learning happens! A key intuition in interpretability is that basically every interesting phenomena in LLMs boil”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Neel Nanda's team published a paper showing subliminal learning in LLMs — models absorbing unintended patterns from training — is mechanistically explained by steering vectors.</dd>
      <dt>Why interesting</dt>
      <dd>Steering-vector framing gives teams a concrete mental model for diagnosing why fine-tuned or prompted LLMs produce unexpected outputs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Read the paper before building eval pipelines for studio LLM tools — the steering-vector lens helps surface unintended learned behaviors before they reach production.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NeelNanda5/status/2062260199822639314" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
