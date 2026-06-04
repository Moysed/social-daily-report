---
type: social-topic-report
date: '2026-06-04'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-06-04T03:19:51+00:00'
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
salience: 0.55
sentiment: mixed
confidence: 0.58
tags:
- gemma4
- ollama
- claude-code
- agent-workflows
- ai-pricing
- local-models
thumbnail: https://pbs.twimg.com/media/HJ7Xa8yawAAAHgy.jpg
---

# AI News & New Skills — 2026-06-04

## TL;DR
- Google released Gemma 4 12B, an encoder-free multimodal model, already runnable locally via Ollama (`ollama run gemma4:12b-mlx`) and usable as a Claude Code backend [14][16].
- Anthropic renamed the Claude Code dynamic-workflow trigger from "workflow" to "ultracode" to cut accidental kickoffs; "use a workflow for this" still works [2].
- Anthropic published a best-practices post for building Claude data-analysis agents, covering skills, data foundations, and evaluations [5].
- Claude "Mythos" reportedly hit a 3-4 hour METR 80%-task horizon, matching what superforecasters predicted for year-end back in early May [34].
- AI tool cost-capping is a recurring signal today: Uber $1,500/mo, T-Mobile attempted $30/mo (down from $2,000), and OpenAI's top internal user burns ~100B tokens/month [9][37][39][51].

## What happened
Concrete artifacts this cycle are limited but real. Google shipped Gemma 4 12B, described as a unified encoder-free multimodal model [14], with same-day availability on Ollama including MLX builds and a Claude Code launch path [16]. Anthropic made two developer-facing moves: changing the Claude Code dynamic-workflow trigger word from "workflow" to "ultracode" to reduce false triggers [2], and publishing best practices for building Claude agents that do business/data analysis, focused on skills, data foundations, and evaluations [5]. On the research/benchmark side, Claude "Mythos" reportedly reached a 3-4 hour METR 80% task-completion horizon ahead of forecasts [34], and an OpenAI autonomous research agent named "Aiden" was reported to have run 22 days and outscored all 1,016 human entrants in a "Parameter Golf" hiring challenge [44]. A prompt/agent pattern circulated from an Anthropic engineer: "build a system that prompts itself" rather than hand-prompting Claude [49].

## Why it matters (reasoning)
The usable signal for a studio is local + multimodal + cheap. Gemma 4 12B running through Ollama with an MLX build means a 12B-class multimodal model on a developer laptop, with a Claude Code integration path [16] — relevant for offline prototyping, asset/image understanding, and avoiding per-token cloud cost. That ties directly to the second theme: the day's loudest non-astrology, non-finance signal is AI cost discipline. Uber's $1,500/mo cap, T-Mobile's attempted cut to $30/mo, and OpenAI's 100B-token internal users [9][37][39][51] all point to buyers tightening AI budgets, which makes a capable local model more than a curiosity. Anthropic's workflow trigger rename [2] and analytics-skills post [5] show the Claude tooling surface is still moving month to month, so prompt/skill setups need maintenance. The "system that prompts itself" framing [49] and the Aiden/Mythos results [34][44] are early evidence that the practical unit of work is shifting from single prompts toward longer-running agent loops — useful direction, but reported via tweets, not reproducible artifacts.

## Possibility
Likely: Gemma 4 12B sees fast community tooling and quantized variants given Ollama day-one support and the MLX build [16]. Plausible: more Claude Code config churn follows the "ultracode" rename, so any scripted trigger words will need periodic checking [2]. Plausible: AI vendors and enterprises keep moving toward hard per-seat token caps, pushing teams to mix local models with cloud [9][37][39]. Unlikely to be verifiable soon: the Mythos 3-4h horizon [34] and Aiden's 22-day benchmark win [44] — both are single-source claims with no linked methodology, so treat as directional, not confirmed. No source gives numeric probabilities, so none are asserted here.

## Org applicability — NDF DEV
1) Pull Gemma 4 12B locally and benchmark it for image/asset understanding and offline prototyping, including the Claude Code launch path — low/med effort [14][16]. 2) Update any Claude Code scripts, docs, or team notes that reference the "workflow" trigger; the dynamic trigger is now "ultracode" — low effort [2]. 3) Read Anthropic's analytics-agent post before building any e-learning/edutech data-analysis agent, specifically the skills + evaluations sections — low effort [5]. 4) Pilot the "system that prompts itself" pattern for one repeatable internal task (e.g. build/QA summaries) instead of ad-hoc prompting — med effort [49]. 5) Add AI tool spend to budgeting reviews given visible cost caps across vendors; favor local models for high-volume, low-stakes work [9][37][39]. Skip: IPO/valuation and AI-bubble debate [3][4][11][13][55], all astrology/tarot items, and the Claude Monet art posts — zero workflow relevance.

## Signals to Watch
- Gemma 4 12B quantization, fine-tunes, and Ollama agent recipes (Hermes/Claude Code) in the coming days [16].
- Further Claude Code trigger/config changes after the "ultracode" rename [2].
- Whether METR Mythos horizons [34] and the Aiden benchmark [44] get reproducible write-ups versus staying as tweets.
- Enterprise AI per-seat token caps as a pricing trend (Uber, T-Mobile, OpenAI) affecting tool budgets [9][37][39][51].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **duanebester/gooey** — Gooey: A GPU-accelerated UI framework for Zig | radar | <https://github.com/duanebester/gooey> |
| **chopratejas/headroom** — Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 60-95% fewer tokens, s | rss | <https://github.com/chopratejas/headroom> |
| **NousResearch/hermes-agent** — The agent that grows with you Hermes Agent ☤ The self-improving AI agent built by Nous Research. It' | rss | <https://github.com/NousResearch/hermes-agent> |
| **microsoft/markitdown** — Python tool for converting files and office documents to Markdown.MarkItDown Important MarkItDown pe | rss | <https://github.com/microsoft/markitdown> |
| **nesquena/hermes-webui** — Hermes WebUI: The best way to use Hermes Agent from the web or from your phone!Hermes Web UI Hermes  | rss | <https://github.com/nesquena/hermes-webui> |
| **D4Vinci/Scrapling** — 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale  | rss | <https://github.com/D4Vinci/Scrapling> |
| **odoo/odoo** — Odoo. Open Source Apps To Grow Your Business.Odoo Odoo is a suite of web based open source business  | rss | <https://github.com/odoo/odoo> |
| **Open-LLM-VTuber/Open-LLM-VTuber** — Talk to any LLM with hands-free voice interaction, voice interruption, and Live2D taking face runnin | rss | <https://github.com/Open-LLM-VTuber/Open-LLM-VTuber> |
| **HKUDS/Vibe-Trading** — "Vibe-Trading: Your Personal Trading Agent" English / 中文 / 日本語 / 한국어 / العربية Vibe-Trading: Your Pe | rss | <https://github.com/HKUDS/Vibe-Trading> |
| **0x4m4/hexstrike-ai** — HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) a | rss | <https://github.com/0x4m4/hexstrike-ai> |
| **interviewstreet/hiring-agent** — AI agent to evaluate and score resumes.Hiring Agent Resume-to-Score pipeline that extracts structure | rss | <https://github.com/interviewstreet/hiring-agent> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | duragactivitty | ^3406 c21 | [niggas get on claude and make any website](https://x.com/duragactivitty/status/2062272669211308046) |
| x | ClaudeDevs | ^3231 c183 | [We've changed the trigger word from "workflow" to "ultracode". You can still say](https://x.com/ClaudeDevs/status/2062257177788858398) |
| x | KobeissiLetter | ^2742 c151 | [BREAKING: Anthropic has picked Morgan Stanley and Goldman Sachs to lead its upco](https://x.com/KobeissiLetter/status/2062296014879383922) |
| x | rdd147 | ^2401 c116 | [🚨 Sam Altman warns OpenAi and Anthropic are experiencing severe pullback on Ai s](https://x.com/rdd147/status/2062253781438624051) |
| x | ClaudeDevs | ^1256 c33 | [How do we automate business analytics with Claude? New blog post covering our be](https://x.com/ClaudeDevs/status/2062274312363770064) |
| x | GreenIrisTarot | ^1132 c6 | [˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — blessings upcoming! 💝 ](https://x.com/GreenIrisTarot/status/2062238216258727991) |
| x | aleabitoreddit | ^1124 c225 | [Just some random notes about $AVGO earnings transcript - Revenue target reiterat](https://x.com/aleabitoreddit/status/2062322546809381094) |
| x | ThierryBorgeat | ^1105 c92 | [🚨 We may be looking at the rarest market setup in 50 years. The S&P 500's four h](https://x.com/ThierryBorgeat/status/2062261038662427125) |
| x | edzitron | ^1010 c34 | [Hearing that T-Mobile attempted to limit its Claude enterprise users to as littl](https://x.com/edzitron/status/2062226951054467276) |
| x | sunlithetarot | ^987 c0 | [mutable signs (gemini, virgo, sagittarius, pisces), stay devoted to your dreams,](https://x.com/sunlithetarot/status/2062238974790570211) |
| x | BullTheoryio | ^938 c99 | [BREAKING: Ray Dalio just said the AI market is a bubble and it will burst. "All ](https://x.com/BullTheoryio/status/2062247647592018351) |
| x | JV_F1 | ^892 c36 | [I’m really happy to share with you all how we will be showing up in Monaco this ](https://x.com/JV_F1/status/2062259853176037490) |
| x | edzitron | ^805 c24 | [OpenAI is absolutely cooked. This is loser language. You can’t be four years int](https://x.com/edzitron/status/2062349145264828551) |
| radar | rvz | ^721 c296 | [Gemma 4 12B: A unified, encoder-free multimodal model](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) |
| x | Polymarket | ^703 c56 | [JUST IN: Anthropic has reportedly tapped Morgan Stanley &amp; Goldman Sachs to l](https://x.com/Polymarket/status/2062233732770103624) |
| x | ollama | ^676 c32 | [.@GoogleDeepMind's Gemma 4 - 12B is available on Ollama! Chat: ollama run gemma4](https://x.com/ollama/status/2062250522598572345) |
| x | amitisinvesting | ^656 c83 | [A TON OF THINGS HAPPENED IN THE STOCK MARKET TODAY. Here's a full recap: 1. $BTC](https://x.com/amitisinvesting/status/2062356758069498362) |
| x | zerohedge | ^653 c71 | [*BROADCOM: WORK WITH APOLLO, BLACKSTONE SERVES OPENAI, ANTHROPIC Translation: Br](https://x.com/zerohedge/status/2062296977614778371) |
| x | kimmonismus | ^635 c44 | [Im confused. And excited at the same time. I got the feeling OpenAI is preparing](https://x.com/kimmonismus/status/2062258181624016927) |
| x | tszzl | ^621 c144 | [I think you can make an equally convincing argument that waymo, claude, and the ](https://x.com/tszzl/status/2062309538548859153) |
| x | JRSmith42091575 | ^601 c11 | [Me and one of my boys share a Claude account and he is actually cooked in life #](https://x.com/JRSmith42091575/status/2062239605319954847) |
| radar | cloud8421 | ^591 c222 | [Elixir v1.20: Now a gradually typed language](https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/) |
| radar | Tomte | ^519 c161 | [I was recently diagnosed with anti-NMDA receptor encephalitis](https://burntsushi.net/encephalitis/) |
| x | buildincrisis | ^513 c7 | [if anthropic had dropped Mythos today, it still wouldn’t have been the best mode](https://x.com/buildincrisis/status/2062279290377380050) |
| x | OxfordAnalytics | ^487 c70 | [The AI Bubble is being driven by the fantasy that AI can replace human labour co](https://x.com/OxfordAnalytics/status/2062245841839006112) |
| x | StockSavvyShay | ^475 c22 | [$AVGO said the company entered an agreement to give Anthropic access to another ](https://x.com/StockSavvyShay/status/2062307814207598761) |
| x | sunlithetarot | ^472 c0 | [🔮🪄 • blessings in the next 48 hrs. ♈ aries: happiness ♉ taurus: extra money ♊ ge](https://x.com/sunlithetarot/status/2062238824529555849) |
| x | Layyenne | ^461 c37 | [Someone in the comments used Gemini Which one got it better between the two??? @](https://x.com/Layyenne/status/2062230083889225909) |
| x | astroinrealtime | ^453 c11 | [stop guessing how they feel, gemini. ask them directly.](https://x.com/astroinrealtime/status/2062278176512852248) |
| x | Havenlust | ^441 c4 | [Claude Monet https://t.co/OmCsKFV6co](https://x.com/Havenlust/status/2062310359508328464) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@duragactivitty</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3406 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/duragactivitty/status/2062272669211308046">View @duragactivitty on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“niggas get on claude and make any website”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral post praises Claude's ability to generate websites, expressed as casual social commentary with no technical detail.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/duragactivitty/status/2062272669211308046" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ClaudeDevs</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3231 · 💬 183</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ClaudeDevs/status/2062257177788858398">View @ClaudeDevs on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We've changed the trigger word from &quot;workflow&quot; to &quot;ultracode&quot;. You can still say &quot;use a workflow for this&quot;, but when you're clearly referring to something else, Claude won't kick off a dynamic workflo”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Code changed its dynamic multi-agent workflow trigger keyword from 'workflow' to 'ultracode'; the explicit phrase 'use a workflow for this' still fires it intentionally.</dd>
      <dt>Why interesting</dt>
      <dd>Any team member who typed 'workflow' expecting orchestration to kick off will get no response — the keyword swap breaks existing prompting habits silently.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Switch the studio's Claude Code prompting habit to 'ultracode' when intentionally triggering a multi-agent workflow run.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ClaudeDevs/status/2062257177788858398" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KobeissiLetter</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2742 · 💬 151</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KobeissiLetter/status/2062296014879383922">View @KobeissiLetter on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“BREAKING: Anthropic has picked Morgan Stanley and Goldman Sachs to lead its upcoming IPO, per Bloomberg. Anthropic was valued at $965 billion in its latest funding round, officially surpassing OpenAI’”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Anthropic has selected Morgan Stanley and Goldman Sachs to lead its IPO, following a funding round that valued the company at $965B — surpassing OpenAI's valuation for the first time.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KobeissiLetter/status/2062296014879383922" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rdd147</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2401 · 💬 116</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rdd147/status/2062253781438624051">View @rdd147 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 Sam Altman warns OpenAi and Anthropic are experiencing severe pullback on Ai spending as companies put significant restraints on spending to restrict costs. The company warns investors it’s the firs”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An unverified X post claims Sam Altman warned investors that OpenAI and Anthropic face severe AI spending pullback from enterprise customers due to unsustainable build-out costs — framed as a stock market signal ($SOXX $DRAM).</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rdd147/status/2062253781438624051" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ClaudeDevs</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1256 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ClaudeDevs/status/2062274312363770064">View @ClaudeDevs on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“How do we automate business analytics with Claude? New blog post covering our best practices for skills, data foundations, and evaluations when building agents to perform data analysis: https://t.co/m”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@ClaudeDevs published a blog post on best practices for building Claude-based data analysis agents, covering skills design, data foundations, and agent evaluation methods.</dd>
      <dt>Why interesting</dt>
      <dd>The evaluation and skills-layering patterns apply to any Claude agent the studio builds — not limited to analytics use cases.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Read the post and extract the evaluation framework, then apply it to benchmark the studio's existing Claude agent workflows.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ClaudeDevs/status/2062274312363770064" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GreenIrisTarot</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1132 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GreenIrisTarot/status/2062238216258727991">View @GreenIrisTarot on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — blessings upcoming! 💝 • lucky timing. being at the right place at the right time over and over again • invitations to celebrations, weddings, ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A tarot account posted a horoscope reading for Gemini, Virgo, Sagittarius, and Pisces predicting social blessings and lucky timing.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GreenIrisTarot/status/2062238216258727991" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aleabitoreddit</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1124 · 💬 225</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aleabitoreddit/status/2062322546809381094">View @aleabitoreddit on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just some random notes about $AVGO earnings transcript - Revenue target reiterated ($100B+ 2027, pretty sure markets wanted that to be raised this earning, hence the drop) Remember $NVDA Jensen commen”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Broadcom ($AVGO) earnings call confirmed $100B+ 2027 revenue target (not raised), with AI networking margins described as 'very rich' while TPU margins compress at scale; XPU/networking orders extend visibility to 2028.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aleabitoreddit/status/2062322546809381094" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ThierryBorgeat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1105 · 💬 92</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ThierryBorgeat/status/2062261038662427125">View @ThierryBorgeat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 We may be looking at the rarest market setup in 50 years. The S&amp;P 500's four historic drawdowns since 1972: – 1973 Inflation: -43% – 1987 Liquidity: -30% – 2000 Tech: -47% – 2008 Credit: -55% Each o”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A market analyst argues that all four historic S&amp;P 500 crash drivers (inflation, liquidity shock, tech bubble, credit freeze) are simultaneously present in 2026 for the first time in 50 years.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ThierryBorgeat/status/2062261038662427125" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
