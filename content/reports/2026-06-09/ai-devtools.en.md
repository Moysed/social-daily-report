---
type: social-topic-report
date: '2026-06-09'
topic: ai-devtools
lang: en
pair: ai-devtools.th.md
generated_at: '2026-06-09T03:04:21+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 292
salience: 0.85
sentiment: mixed
confidence: 0.62
tags:
- coding-agents
- mcp
- agent-skills
- open-models
- evals
- on-device
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2064010372621737984/img/u0c0ovEguIx46u6Q.jpg
---

# AI Devtools — 2026-06-09

## TL;DR
- Coding-agent workflows are shifting from one-off prompts to reusable 'skills' and 'loops': directories of pre-built workflows for Cursor/Claude Code/Codex [15], the text-to-lottie skill [1], plus vendor skill repos from Google [29] and OpenAI plugins [57]; Claude Code's creator says he now 'creates loops' rather than prompts and runs ~100 agents, much from his phone [45][47].
- MCP is becoming the cross-tool integration layer: Figma's MCP server is now supported in Xcode [27], and OptimAI ships a search MCP targeting Claude/Cursor/Copilot/Codex at once [23].
- Eval skepticism is rising — METR's FrontierCode claims over half of SWEBench results are unmergeable [26], alongside 'AI is slowing down' [34] and 'xAI looks like a datacentre REIT' [35] commentary.
- Commercial scale signals: Cursor reportedly hit $4B annualized revenue (doubled in 4 months) with a SpaceX/xAI acquisition option [37][48]; OpenAI filed a confidential draft S-1 [56].
- On-device/open models advance: Gemma 4 QAT cuts memory ~4x (E2B to ~1GB) for mobile [30], Xiaomi's MiMo-v2.5-Pro claims 1T params at 1000 tok/s [25], and Nex-N2 open-sources an agentic coding/tool-use model [13].

## What happened
The day's volume centers on coding agents and their surrounding ecosystem. New tooling includes an open-source text-to-lottie skill for Codex/Claude Code [1], a 'loops' directory of pre-built agent workflows [15], research-agent skills that sweep Reddit/X/YouTube/HN [2][40], and official skill/plugin repos from Google [29] and OpenAI [57]. Claude Code marked roughly a year since GA with retrospectives on auto vs plan mode [5], and its creator described a workflow of loops and ~100 concurrent agents driven partly from a phone [45][47]. Practitioner tips for Codex emphasize outcome-based prompting and 'Approve for me' modes [50][54], and design advice circulated to model agents as state machines rather than loops [10].

## Why it matters (reasoning)
Two opposing forces are visible. On one side, the tooling layer is standardizing: MCP is spreading into first-party IDEs (Figma MCP in Xcode [27]) and search/context providers are integrating across all major agents at once [23], while 'skills' and 'loops' formats [1][15][29][57] make agent behavior portable and reusable instead of bespoke per-prompt. That lowers switching costs and favors whoever owns the agent surface — which is why Cursor's revenue trajectory [37][48] and OpenAI's S-1 [56] matter as consolidation signals. On the other side, credibility pressure is mounting: METR's claim that >50% of SWEBench output is unmergeable [26] undercuts headline benchmark numbers, and 'AI is slowing down' [34] plus the xAI-as-REIT framing [35] push back on capability and capex narratives. For a studio, the net is that agent workflows are usable now but benchmark and vendor claims should be discounted.

## Possibility
Likely: skill/loop formats and MCP keep consolidating as the integration standard, given simultaneous adoption across Cursor/Claude Code/Codex/Copilot [15][23][27][29][57]. Plausible: on-device/quantized open models (Gemma 4 ~1GB [30], MiMo speed claims [25], Nex-N2 [13]) become viable for offline mobile/edutech inference within months, though the 1000 tok/s and 1T-param claims [25] are unverified marketing until independently tested. Plausible: continued vendor consolidation around Cursor and OpenAI [37][48][56]. Unlikely (near-term): benchmark trust recovers quickly while critiques like FrontierCode [26] and slowdown pieces [34] are circulating. No source states numeric probabilities; GPT 5.6 'around 1.5M tokens' context is rumor only [58].

## Org applicability — NDF DEV
1) Trial the text-to-lottie skill for Unity/web/mobile UI motion assets — low effort, directly fits the stack [1]. 2) Adopt a loop/skill-based coding-agent setup (outcome + exit conditions) for repetitive build tasks; start with one workflow and 'Approve for me' guardrails — low/med effort [15][45][47][50][54]. 3) Evaluate Gemma 4 QAT (~1GB E2B) for on-device/offline features in edutech and mobile apps — med effort, validate quality yourself [30]. 4) If you ship iOS/macOS, test the Figma MCP server in Xcode to shorten design-to-code — low/med effort [27]. 5) For agent-driven web/mobile UIs, assess CopilotKit/AG-UI — med effort [44]. 6) For XR/CV pipelines, look at roboflow/supervision as reusable vision tooling — med effort [7]. Skip: chasing GPT 5.6/Cursor-SpaceX rumors [37][48][58], the macOS cursor and eFootball noise [6][33][38], and treating SWEBench-style leaderboards as procurement evidence given [26]. Run your own small eval before adopting any model.

## Signals to Watch
- MCP adoption in first-party IDEs — watch whether more editors follow Xcode's Figma MCP support [27].
- Independent verification of MiMo's 1000 tok/s / 1T-param and GPT 5.6 context claims before relying on them [25][58].
- Whether METR's FrontierCode becomes a standard counter-benchmark to SWEBench for tool selection [26].
- On-device open models (Gemma 4 QAT, Nex-N2) reaching usable quality for offline edutech/mobile [13][30].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **mvanhorn/last30days-skill** — AI agent skill that researches any topic across Reddit, X, YouTube, HN, Polymarket, and the web - th | radar | <https://github.com/mvanhorn/last30days-skill> |
| **RyanCodrai/turbovec** — A vector index built on TurboQuant, written in Rust with Python bindings | radar | <https://github.com/RyanCodrai/turbovec> |
| **roboflow/supervision** — We write your reusable computer vision tools. 💜 | radar | <https://github.com/roboflow/supervision> |
| **aaif-goose/goose** — an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and  | radar | <https://github.com/aaif-goose/goose> |
| **Panniantong/Agent-Reach** — Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub,  | radar | <https://github.com/Panniantong/Agent-Reach> |
| **refactoringhq/tolaria** — Desktop app to manage markdown knowledge bases | radar | <https://github.com/refactoringhq/tolaria> |
| **TapXWorld/ChinaTextbook** — 所有小初高、大学PDF教材。 | radar | <https://github.com/TapXWorld/ChinaTextbook> |
| **google/skills** — Agent Skills for Google products and technologies | radar | <https://github.com/google/skills> |
| **CopilotKit/CopilotKit** — The Frontend Stack for Agents & Generative UI. React, Angular, Mobile, Slack, and more. Makers of th | radar | <https://github.com/CopilotKit/CopilotKit> |
| **luongnv89/claude-howto** — A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-pa | radar | <https://github.com/luongnv89/claude-howto> |
| **santifer/career-ops** — AI-powered job search system built on Claude Code. 14 skill modes, Go dashboard, PDF generation, bat | radar | <https://github.com/santifer/career-ops> |
| **openai/plugins** — OpenAI Plugins | radar | <https://github.com/openai/plugins> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | konstipaulus | ^5228 c91 | [Introducing text-to-lottie: an open source skill and harness for generating prod](https://x.com/konstipaulus/status/2064011863889788972) |
| radar | mvanhorn_last30days-skill | ^3558 c0 | [mvanhorn/last30days-skill AI agent skill that researches any topic across Reddit](https://github.com/mvanhorn/last30days-skill) |
| x | AnthropicAI | ^2210 c185 | [New Science Blog: Why has AI advanced faster in coding than in biology? To agent](https://x.com/AnthropicAI/status/2064054837294354677) |
| radar | RyanCodrai_turbovec | ^1729 c0 | [RyanCodrai/turbovec A vector index built on TurboQuant, written in Rust with Pyt](https://github.com/RyanCodrai/turbovec) |
| x | bcherny | ^1557 c98 | [When we first demoed Claude Code internally, it got two reactions on Slack. A ye](https://x.com/bcherny/status/2064034799711588805) |
| x | 1000kilobytes | ^1370 c27 | [THE BUTLER CURSOR IS BACK IN MACOS 27 https://t.co/MJ7ubLbQNG](https://x.com/1000kilobytes/status/2064069798846505034) |
| radar | roboflow_supervision | ^1288 c0 | [roboflow/supervision We write your reusable computer vision tools. 💜](https://github.com/roboflow/supervision) |
| x | edzitron | ^1244 c14 | [Fun watching the mainstream media repeat things I’ve said for months like they’r](https://x.com/edzitron/status/2064023464022073567) |
| x | schizothotep | ^1198 c12 | [CHALLENGE FOR YOU, LOGAN GRIMNAR, IF YOU READ ONE FULL PAGE OF CODEX ASTARTES, 𝓕](https://x.com/schizothotep/status/2064014968488329280) |
| x | dzhng | ^1037 c61 | [don't use loops, design state machines https://t.co/xQ1Ir6KlcJ](https://x.com/dzhng/status/2063931263312892406) |
| x | hosseeb | ^1001 c129 | [OK, so I became one of those people: Claude diagnosed my sleep disorder. Here's ](https://x.com/hosseeb/status/2064042451850121632) |
| hackernews | lizhang | ^808 c159 | [Show HN: Performative-UI – A react component library of design tropes hope you e](https://vorpus.github.io/performativeUI/) |
| x | ModelScope2022 | ^731 c25 | [Nex-N2 is now open source！An agentic model series from Nex AGI built for coding,](https://x.com/ModelScope2022/status/2063881896153543022) |
| radar | aaif-goose_goose | ^699 c0 | [aaif-goose/goose an open source, extensible AI agent that goes beyond code sugge](https://github.com/aaif-goose/goose) |
| x | elorm_elom | ^698 c32 | [introducing loops! a directory of pre-built agent workflows for Cursor, Claude C](https://x.com/elorm_elom/status/2064005518343995588) |
| x | thsottiaux | ^683 c105 | [@YashHustle_22 Codex at breakfast Codex in the morning Codex at lunch Codex in t](https://x.com/thsottiaux/status/2064039257392709683) |
| radar | Panniantong_Agent-Reach | ^679 c0 | [Panniantong/Agent-Reach Give your AI agent eyes to see the entire internet. Read](https://github.com/Panniantong/Agent-Reach) |
| radar | refactoringhq_tolaria | ^651 c0 | [refactoringhq/tolaria Desktop app to manage markdown knowledge bases](https://github.com/refactoringhq/tolaria) |
| radar | TapXWorld_ChinaTextbook | ^592 c0 | [TapXWorld/ChinaTextbook 所有小初高、大学PDF教材。](https://github.com/TapXWorld/ChinaTextbook) |
| hackernews | bobbiechen | ^589 c238 | [Stop the Apple Music app from launching](https://lowtechguys.com/musicdecoy/) |
| x | skirano | ^584 c29 | [Today we’re introducing Builder, a new MagicPath plan for people working with Co](https://x.com/skirano/status/2064035120483352776) |
| hackernews | 1vuio0pswjnm7 | ^565 c418 | [Anti-social: It's fads, not friends, which now dominate social media feeds](https://www.bbc.com/worklife/article/20260520-how-social-media-ceased-to-be-social) |
| x | OptimaiNetwork | ^562 c88 | [OptimAI Search MCP brings live context to the agents people already use. Claude.](https://x.com/OptimaiNetwork/status/2064012781658009804) |
| x | ThePrimeagen | ^509 c27 | [I have to push back on 2 things as i think one is categorically incorrect and th](https://x.com/ThePrimeagen/status/2064142254579826716) |
| hackernews | gainsurier | ^506 c356 | [MiMo-v2.5-Pro-UltraSpeed: 1T model with 1000 tokens per second](https://mimo.xiaomi.com/blog/mimo-tilert-1000tps) |
| x | swyx | ^490 c58 | [It's finally out!!! @METR_Evals found that more than half of SWEBench results is](https://x.com/swyx/status/2064081945567580323) |
| x | figma | ^486 c10 | [The Figma MCP Server is now supported in Xcode #WWDC https://t.co/WDy9qFtkd8](https://x.com/figma/status/2064120455808888873) |
| x | amasad | ^479 c20 | [@REM__BEN From his perspective, it's stationary; from the perspective of someone](https://x.com/amasad/status/2063667850531999921) |
| radar | google_skills | ^461 c0 | [google/skills Agent Skills for Google products and technologies](https://github.com/google/skills) |
| x | _philschmid | ^454 c17 | [More Gemma 4! New QAT Gemma 4 checkpoints with similar performance while using ~](https://x.com/_philschmid/status/2063990553826439378) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@konstipaulus</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5228 · 💬 91</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/konstipaulus/status/2064011863889788972">View @konstipaulus on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing text-to-lottie: an open source skill and harness for generating production ready Lottie animations with codex/claude code. $ npx skills add diffusionstudio/lottie Prompts guide and repo in”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>diffusionstudio released text-to-lottie, an open-source Claude Code skill that generates production-ready Lottie animations from text prompts, installed via `npx skills add diffusionstudio/lottie`.</dd>
      <dt>Why interesting</dt>
      <dd>Lottie animations are standard in e-learning and mobile UIs; generating them via prompt cuts the designer-to-code handoff entirely.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Install the skill in the studio's Claude Code setup and trial it on e-learning module or mobile app animation tasks.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/konstipaulus/status/2064011863889788972" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnthropicAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2210 · 💬 185</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnthropicAI/status/2064054837294354677">View @AnthropicAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New Science Blog: Why has AI advanced faster in coding than in biology? To agents, bio databases are like cities built before cars—maddening to drive in because they're designed for different traffic.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Anthropic published a science blog arguing that AI coding agents outpace bio agents because code infrastructure (APIs, CLIs, version control) was built machine-readable by default, while biology databases were designed for human browsing.</dd>
      <dt>Why interesting</dt>
      <dd>The same friction applies to any legacy data system the studio's agents must touch — if the data isn't structured for machine consumption, agent performance will cap early.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When building internal tools or pipelines for agents, design data schemas and APIs machine-first from day one — not as an afterthought.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AnthropicAI/status/2064054837294354677" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bcherny</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1557 · 💬 98</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bcherny/status/2064034799711588805">View @bcherny on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“When we first demoed Claude Code internally, it got two reactions on Slack. A year after GA, @_catwu and I sat down to talk about what's changed: why I use auto mode instead of plan mode, how routines”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Code co-creator @bcherny shares a one-year post-GA retrospective: auto mode beats plan mode for daily use, scheduled routines catch bugs proactively, and he codes primarily from mobile.</dd>
      <dt>Why interesting</dt>
      <dd>The 'routines fix bugs before I see them' pattern confirms scheduled agents as a proactive quality layer — a concrete workflow shift, not just a feature demo.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can configure Claude Code routines to run nightly checks on active projects and surface regressions before the morning standup.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bcherny/status/2064034799711588805" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@1000kilobytes</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1370 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/1000kilobytes/status/2064069798846505034">View @1000kilobytes on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“THE BUTLER CURSOR IS BACK IN MACOS 27 https://t.co/MJ7ubLbQNG”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>macOS 27 is restoring the Butler Cursor, a cursor feature that was previously removed from the OS.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/1000kilobytes/status/2064069798846505034" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@edzitron</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1244 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/edzitron/status/2064023464022073567">View @edzitron on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fun watching the mainstream media repeat things I’ve said for months like they’re brand new thoughts down to the GitHub copilot stuff lol”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@edzitron notes that mainstream media is now repeating AI devtools takes — including GitHub Copilot commentary — that they published months earlier.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/edzitron/status/2064023464022073567" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@schizothotep</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1198 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/schizothotep/status/2064014968488329280">View @schizothotep on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“CHALLENGE FOR YOU, LOGAN GRIMNAR, IF YOU READ ONE FULL PAGE OF CODEX ASTARTES, 𝓕𝓤𝓡𝓡𝓨, I'LL GIVE A THOUSAND PSYKERS TO THE GOLDEN THRONE https://t.co/ZMHmeJHSV0”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user posted a Warhammer 40K meme challenging a fictional character with no technical content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/schizothotep/status/2064014968488329280" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@dzhng</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1037 · 💬 61</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/dzhng/status/2063931263312892406">View @dzhng on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“don't use loops, design state machines https://t.co/xQ1Ir6KlcJ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@dzhng (Agentic framework author) argues AI agent workflows should be modeled as explicit state machines rather than loops — for predictability, resumability, and easier debugging.</dd>
      <dt>Why interesting</dt>
      <dd>State machines make agent failures inspectable and recoverable — a loop that breaks mid-run gives you nothing; a named state tells you exactly where it stopped.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When building AI agent pipelines in the studio, define explicit states (idle, planning, executing, retrying, done) instead of wrapping LLM calls in a while loop.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/dzhng/status/2063931263312892406" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@hosseeb</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1001 · 💬 129</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/hosseeb/status/2064042451850121632">View @hosseeb on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“OK, so I became one of those people: Claude diagnosed my sleep disorder. Here's the story. I'd been sleeping worse and worse since hitting my mid-30s. I've been averaging 5:30-5:45 a night for a coupl”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Hosseb (likely @hosseeb, a known tech investor) shares a personal anecdote about chronic poor sleep and using an Oura ring — the post cuts off before the Claude diagnosis actually appears.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/hosseeb/status/2064042451850121632" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
