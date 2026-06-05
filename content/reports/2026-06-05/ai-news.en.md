---
type: social-topic-report
date: '2026-06-05'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-06-05T03:09:14+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 227
salience: 0.62
sentiment: mixed
confidence: 0.58
tags:
- ai-tooling
- devtools
- codex-billing
- ollama
- supply-chain-security
thumbnail: https://pbs.twimg.com/media/HKAdZJgXQAAnQMv.jpg
---

# AI News & New Skills — 2026-06-05

## TL;DR
- OpenAI is rolling out a "more capable and compute-efficient" memory synthesis system to Plus/Pro users in the US [3][27].
- Ollama updated Gemma 4 12B; it runs locally and can be launched into Claude Code via `ollama launch claude --model gemma4:12b` [57].
- OpenAI moved Codex to token-based "credits" billing aligned with API pricing — Brex now caps engineers at ~12,500 credits (~$500/wk), non-engineers at 125 (~$5/wk) [29][49][60].
- VoidZero (the Vite/Rolldown/oxc build toolchain) is joining Cloudflare [22].
- A self-replicating worm was hidden in 37 npm packages — Rust, eBPF kernel rootkit, Tor C2 — stealing 86 environment variables including AWS/GCP keys [13].

## What happened
Concrete artifacts today: OpenAI began rolling out an upgraded memory system to US Plus/Pro users [3][27]; Ollama shipped a Gemma 4 12B update usable locally and inside Claude Code and a Hermes agent [57]; the Gemini macOS app added a double-Command shortcut to attach the active window to chat [37]. OpenAI also shifted Codex to token-based credit billing matching API pricing, ending some intro periods, with reported per-seat caps at Brex [29][49][60], promoted "Codex Sites" (apps that self-update) [42], and scheduled developer office hours covering Codex, /goal, mobile, plugins, and Amazon Bedrock [48]. VoidZero is joining Cloudflare [22]. On the research/security side, Anthropic published an essay on recursive self-improvement and a call for top labs to slow down [46][41][4]; an OpenAI model reportedly found a counterexample to an 80-year-old Erdős conjecture [15]; and Claude Opus 4.8 was widely reported to have found a critical Zcash infinite-mint bug (ZEC down ~25-27%) [19][47][12][16].

## Why it matters (reasoning)
The directly usable items are tooling and cost shifts, not the louder safety/IPO discourse. Codex's move to API-aligned credit billing [29][49][60] signals the broader end of flat-rate AI coding subscriptions; if Anthropic/Cursor follow, per-seat AI spend becomes a line item that needs metering, not an assumed fixed cost. Ollama's Gemma 4 12B running locally and into Claude Code [57] lowers the cost floor for routine codegen/eval tasks that don't need a frontier model. VoidZero under Cloudflare [22] concentrates the JS build toolchain (Vite/Rolldown/oxc) under a platform vendor — relevant to anyone choosing web build stacks, with both upside (resourcing) and lock-in risk. The npm worm [13] is the most actionable threat: a studio shipping web and mobile apps inherits supply-chain risk directly, and credential theft (AWS/GCP keys) is a concrete failure mode. The Zcash/Opus 4.8 stories [19][47] are largely unverified secondhand reports and should be read as a capability signal (AI-assisted vulnerability discovery is maturing), not as confirmed fact.

## Possibility
Likely: token/credit billing spreads across AI coding tools beyond Codex, given the explicit API-price alignment and intro-period expirations [29][49][60]. Likely: the OpenAI memory upgrade expands past US Plus/Pro over time [27]. Plausible: npm-style supply-chain worms recur, as the described attack reuses known vectors (postinstall, credential exfiltration) [13]. Plausible but unverified: an AI model materially accelerates real vulnerability discovery, suggested by the Zcash reports but sourced only secondhand [19][47][16]. Unlikely to treat as fact yet: the rumored "Mythos" model and its quoted $16/$80 per-1M pricing [6] — single-source rumor, no official confirmation. No source states a numeric probability.

## Org applicability — NDF DEV
1) Audit dependencies now against the npm worm report — verify lockfiles, pin versions, scan for the 37 named packages once disclosed, and rotate any AWS/GCP keys exposed in CI; restrict postinstall scripts (effort: med) [13]. 2) Re-check AI coding spend exposure: if anyone uses Codex, model the new credit pricing and set budgets before bills land (effort: low) [29][49][60]. 3) Pilot Gemma 4 12B locally via Ollama for cheap codegen/test-gen and as a Claude Code fallback, keeping frontier models for hard tasks (effort: med) [57]. 4) Note VoidZero→Cloudflare when choosing web build tooling for client web/mobile work — track Vite/Rolldown direction before committing (effort: low) [22]. 5) Mac users can try Gemini's double-Command window attach for screen-context help (effort: low) [37]. Skip for now: the Anthropic pause/IPO/valuation discourse [4][9][31][34], the Mythos rumor and its pricing [6], all crypto/Zcash trading takes [12][54], and treat the Opus-4.8 exploit claims as unconfirmed [19][47].

## Signals to Watch
- Whether other AI coding vendors (Anthropic, Cursor) follow Codex into metered credit billing [49][60].
- Official disclosure of the 37 affected npm packages and IoCs for the worm [13].
- Any first-party confirmation of the Claude Opus 4.8 Zcash finding vs. secondhand reposts [19][47].
- VoidZero/Vite/Rolldown roadmap and licensing after the Cloudflare move [22].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **anthropics/defending-code-reference-harness** — Anthropic's open-source framework for AI-powered vulnerability discovery | radar | <https://github.com/anthropics/defending-code-reference-harness> |
| **huawei-csl/KVarN** — KVarN: Native vLLM backend for KV-cache quantization by Huawei | radar | <https://github.com/huawei-csl/KVarN> |
| **alibaba/open-code-review** — Open Code Review – An AI-powered code review CLI tool | radar | <https://github.com/alibaba/open-code-review> |
| **chopratejas/headroom** — Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, s | rss | <https://github.com/chopratejas/headroom> |
| **NousResearch/hermes-agent** — The agent that grows with you Hermes Agent ☤ The self-improving AI agent built by Nous Research. It' | rss | <https://github.com/NousResearch/hermes-agent> |
| **PaddlePaddle/PaddleOCR** — Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit | rss | <https://github.com/PaddlePaddle/PaddleOCR> |
| **github/spec-kit** — 💫 Toolkit to help you get started with Spec-Driven Development 🌱 Spec Kit Build high-quality softwar | rss | <https://github.com/github/spec-kit> |
| **Open-LLM-VTuber/Open-LLM-VTuber** — Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D taking face runnin | rss | <https://github.com/Open-LLM-VTuber/Open-LLM-VTuber> |
| **mvanhorn/last30days-skill** — AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - th | rss | <https://github.com/mvanhorn/last30days-skill> |
| **odoo/odoo** — Odoo. Open Source Apps To Grow Your Business.Odoo Odoo is a suite of web based open source business  | rss | <https://github.com/odoo/odoo> |
| **HKUDS/Vibe-Trading** — "Vibe-Trading: Your Personal Trading Agent" English / 中文 / 日本語 / 한국어 / العربية Vibe-Trading: Your Pe | rss | <https://github.com/HKUDS/Vibe-Trading> |
| **datawhalechina/hello-agents** — 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程 English / 中文 Hello-Agents 🤖 《从零开始构建智能体》 从基础理论到实际应用，全面掌握智能体系统的设计与实现 🎯  | rss | <https://github.com/datawhalechina/hello-agents> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | sama | ^5399 c1182 | [man the early days of the internet were so special](https://x.com/sama/status/2062661191969972645) |
| x | atmoio | ^2794 c187 | [Anthropic is questioning whether AI may turn out to be altogether useless. This ](https://x.com/atmoio/status/2062613571100356668) |
| x | sama | ^2586 c307 | [big upgrade to chatgpt memory rolling out today!](https://x.com/sama/status/2062660086787613116) |
| x | Polymarket | ^1871 c265 | [NEW: Anthropic urges top AI labs to slow the pace of AI development, warning of ](https://x.com/Polymarket/status/2062657144579924264) |
| x | Cointelegraph | ^1772 c213 | [🚨 LATEST: Claude maker Anthropic is calling for a global pause in AI development](https://x.com/Cointelegraph/status/2062680953579819102) |
| x | kimmonismus | ^1549 c94 | [Get ready, friends. Anthropic appears to be preparing the release of its Mythos-](https://x.com/kimmonismus/status/2062588689994187138) |
| x | umamusume_eng | ^1460 c6 | [Event Underway! 🥕 The race event Champions Meeting: Gemini Cup has begun! Win ra](https://x.com/umamusume_eng/status/2062659457495257408) |
| x | GreenIrisTarot | ^1118 c5 | [˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — random predictions! 🌼 ](https://x.com/GreenIrisTarot/status/2062598422943666303) |
| x | unusual_whales | ^986 c110 | [Anthropic co-founder Daniela Amodei said the high cost of AI models is making fi](https://x.com/unusual_whales/status/2062633236912889935) |
| x | Danny_Crypton | ^954 c131 | [🚨 WARNING: SPACEX IPO IS A REAL BIG STORM FOR MARKETS!! Everyone thinks $SPCX IP](https://x.com/Danny_Crypton/status/2062582840269676692) |
| x | ryandpetersen | ^947 c14 | [gay guys in Berlin will be like “I’m gonna vibe code a woke version of grindr wi](https://x.com/ryandpetersen/status/2062605292219617305) |
| x | 0xSweep | ^913 c162 | [Zcash $ZEC was allegedly exploited by Claude Opus 4.8 and is down 25% today If t](https://x.com/0xSweep/status/2062669425313010065) |
| x | cyber__razz | ^900 c19 | [Someone hid a self-replicating worm inside 37 npm packages. Written in Rust. Hid](https://x.com/cyber__razz/status/2062617083846754526) |
| x | pubity | ^896 c109 | [Anthropic just proposed a global system to pause AI research to keep the world s](https://x.com/pubity/status/2062640608729067550) |
| x | OpenAI | ^856 c105 | [What happened when one of our models found a counterexample to an 80-year-old Er](https://x.com/OpenAI/status/2062630454537424930) |
| x | Dogetoshi | ^823 c26 | [A single security researcher with a $20 Claude subscription found an infinite mi](https://x.com/Dogetoshi/status/2062667727324455144) |
| x | aleabitoreddit | ^782 c146 | [Anthropic: “Urges Global Pause in AI Development” Translation: “please let us ta](https://x.com/aleabitoreddit/status/2062686651940483414) |
| x | cutoffs_io | ^733 c28 | [🇮🇳🇺🇸 Cognizant's CEO Ravi Kumar brought in 4,774 L-1 visas from India. Ex-execut](https://x.com/cutoffs_io/status/2062613355668644307) |
| x | Polymarket | ^677 c94 | [JUST IN: Claude Opus 4.8 reportedly found a critical Zcash bug that could have a](https://x.com/Polymarket/status/2062715390526914873) |
| x | _catwu | ^672 c41 | [I'm hiring a PM for Claude Code, focused on model performance. If you have exper](https://x.com/_catwu/status/2062659533047259212) |
| x | rektfencer | ^628 c107 | [🚨 WARNING: AI BUBBLE IS ABOUT TO BURST Microsoft gave OpenAI $13 BILLION. OpenAI](https://x.com/rektfencer/status/2062601393530404881) |
| radar | coloneltcb | ^582 c259 | [VoidZero Is Joining Cloudflare](https://blog.cloudflare.com/voidzero-joins-cloudflare/) |
| x | deepfates | ^554 c38 | [seems like a bad sign if anthropic engineers don't write their own code and only](https://x.com/deepfates/status/2062621177831711081) |
| x | jimstewartson | ^524 c20 | [The broligarchs did it. The market is broken. It’s all built on trust. There wil](https://x.com/jimstewartson/status/2062613585801699433) |
| radar | mooreds | ^519 c199 | [Ian's Secure Shoelace Knot](https://www.fieggen.com/shoelace/secureknot.htm) |
| x | cb_doge | ^483 c100 | [Grok is now #1 when you search for "ai app" on the Apple App Store! 🇺🇸🥇 Beating ](https://x.com/cb_doge/status/2062663934415663572) |
| x | testingcatalog | ^463 c22 | [OPENAI 🔥: A new "more capable and scalable system for synthesizing memory" is be](https://x.com/testingcatalog/status/2062584262050656478) |
| x | niyetsel | ^462 c704 | [IF I WERE YOU, I WOULDN'T IGNORE THIS! Enter your number according to your zodia](https://x.com/niyetsel/status/2062687074084385164) |
| x | edzitron | ^453 c15 | [A source at Brex told me that engineers are now limited to 12,500 Codex credits ](https://x.com/edzitron/status/2062645189705978270) |
| x | mermaidgurlco | ^448 c2 | [🔮 june channeled downloads 🔮 sagittarius gemini virgo pisces a late payment fina](https://x.com/mermaidgurlco/status/2062634821692625102) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sama</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5399 · 💬 1182</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sama/status/2062661191969972645">View @sama on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“man the early days of the internet were so special”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Sam Altman posted a one-line nostalgia remark about the early internet, with no technical or product content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sama/status/2062661191969972645" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@atmoio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2794 · 💬 187</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/atmoio/status/2062613571100356668">View @atmoio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anthropic is questioning whether AI may turn out to be altogether useless. This is the single most honest thing Anthropic has ever written. “But achieving recursive improvement alone does not suggest ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Anthropic's own published writing states that recursive AI self-improvement won't automatically speed up societal change, because human bottlenecks — drug trials, elections, trust — still set the real pace.</dd>
      <dt>Why interesting</dt>
      <dd>The lab building the most powerful AI is publicly hedging on transformative pace — useful grounding when the studio evaluates which AI bets actually pay off in a 1–2 year horizon.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When scoping AI features for clients, anchor delivery promises to the human/institutional constraint in that domain, not to what the model can theoretically do.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/atmoio/status/2062613571100356668" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sama</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2586 · 💬 307</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sama/status/2062660086787613116">View @sama on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“big upgrade to chatgpt memory rolling out today!”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Sam Altman (OpenAI CEO) announced a significant upgrade to ChatGPT's memory feature is rolling out today, expanding what the model retains across sessions.</dd>
      <dt>Why interesting</dt>
      <dd>Better persistent memory in ChatGPT makes it more useful as a daily dev assistant for recurring project context without re-prompting each session.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can retest ChatGPT as a persistent project assistant now that memory is improved — especially for recurring client briefings or code context.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sama/status/2062660086787613116" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Polymarket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1871 · 💬 265</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Polymarket/status/2062657144579924264">View @Polymarket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NEW: Anthropic urges top AI labs to slow the pace of AI development, warning of “significant societal risks””</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Anthropic publicly called on AI labs — including itself — to slow AI development, citing significant societal risks in a formal statement.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Polymarket/status/2062657144579924264" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Cointelegraph</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1772 · 💬 213</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Cointelegraph/status/2062680953579819102">View @Cointelegraph on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 LATEST: Claude maker Anthropic is calling for a global pause in AI development, warning that models are approaching the ability to self-improve without human intervention. https://t.co/7WM9jmDZjt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Cointelegraph (a crypto media outlet) claims Anthropic is calling for a global AI development pause, citing concerns about models approaching autonomous self-improvement — no primary source or official statement linked.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Cointelegraph/status/2062680953579819102" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kimmonismus</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1549 · 💬 94</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kimmonismus/status/2062588689994187138">View @kimmonismus on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Get ready, friends. Anthropic appears to be preparing the release of its Mythos-level model. Pricing: $16 per 1M input tokens / $80 per 1M output tokens. The release is likely very close, possibly eve”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A leaked pricing sheet suggests Anthropic is preparing a new model tier (codename 'Mythos') at $16/1M input and $80/1M output tokens, potentially releasing the same week as GPT-5.6.</dd>
      <dt>Why interesting</dt>
      <dd>If Mythos lands at that price tier, teams using Claude for high-output workloads (agents, codegen) need to re-evaluate cost models before adoption.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Hold off on committing Mythos to any production pipeline until official pricing and benchmarks are confirmed.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kimmonismus/status/2062588689994187138" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@umamusume_eng</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1460 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/umamusume_eng/status/2062659457495257408">View @umamusume_eng on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Event Underway! 🥕 The race event Champions Meeting: Gemini Cup has begun! Win races for event-exclusive titles and carats! For more details, please check the in-game notice. #Umamusume https://t.co/yS”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The mobile game Uma Musume Pretty Derby launched an in-game event called Champions Meeting: Gemini Cup, offering event-exclusive titles and carats as race rewards.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/umamusume_eng/status/2062659457495257408" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GreenIrisTarot</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1118 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GreenIrisTarot/status/2062598422943666303">View @GreenIrisTarot on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — random predictions! 🌼 • someone has been checking your profile way more than you realize 👀 • your future partner is closer to meeting you than”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A tarot account posted zodiac predictions about love and someone checking your profile — no tech content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GreenIrisTarot/status/2062598422943666303" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
