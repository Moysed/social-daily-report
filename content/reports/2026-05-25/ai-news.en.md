---
type: social-topic-report
date: '2026-05-25'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-05-25T08:18:41+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- rss
- x
regions:
- global
post_count: 222
salience: 0.75
sentiment: positive
confidence: 0.7
tags:
- claude-skills
- claude-code
- workflows
- agent-swarm
- cost-optimization
- ai-tooling
thumbnail: https://i.redd.it/a795ky5ihx2h1.png
---

# AI News & New Skills — 2026-05-25

## TL;DR
- Anthropic shipped 31 official small-business Skills — ~382k downloads day one, now mapped/indexed by community [10]
- Claude Code /workflows feature incoming — reusable enterprise prompt chains, big productivity unlock [18]
- Anthropic exposed 125 Claude settings (only 40 documented); tuning the hidden 85 cut one dev's API bill from $340→$87 [49]
- Google Antigravity adds Gemini 3.5 Flash (Low) tier to curb token burn on simple tasks [16]
- Agent-swarm pattern (Gemini 3.1 Pro + Opus 4.7 + GPT 5.5 routed per task) gaining traction for one-prompt app builds [43]
- PSA: Claude Code auto-deletes session files after 30 days — set cleanupPeriodDays=9999 [28]

## What happened
Concrete artifacts today: Anthropic's official 31-skill small-business pack hit ~382k downloads on day one and a community map of the whole set is circulating [10]. A /workflows feature for Claude Code was teased as imminent — reusable, named multi-step procedures aimed at enterprise repeatability [18]. A developer documented 125 Claude settings vs. 40 officially documented, with tuning of the undocumented 85 reportedly cutting cost ~75% [49]. Google's Antigravity added a Gemini 3.5 Flash (Low) tier specifically to reduce token consumption on trivial tasks [16]. Multi-agent 'swarm' orchestration (Opus 4.7 + Gemini 3.1 Pro + GPT 5.5 per role) is being demoed as a one-prompt complex-app builder [43].

Operational notes: Claude Code's default 30-day session purge surprised users [28]; an open-source 'Backdoor' localhost proxy that routes any model through Claude Code was allegedly cloned by OpenAI's Codex [29]. DeepMind's agent autonomously solved 9/353 open Erdős problems at a few hundred USD each [24], while Hassabis tempered AGI claims [8]. A side security note: inaudible-audio injection attacks against voice assistants were demonstrated [25].

## Why it matters (reasoning)
The center of gravity is shifting from 'which model is smartest' to 'which workflows, skills, and settings squeeze the most value per token'. Skills (10), /workflows (18), and the 85 hidden settings (49) are all the same trend: productized prompt engineering. For a small studio, that's leverage — buy/borrow proven Skills instead of writing scaffolding. Antigravity's Flash-Low tier (16) and the swarm pattern (43) confirm that routing-by-difficulty is becoming a first-class concern; flat 'use the best model always' is now wasteful. Second-order: model providers compete on dev surface (settings, skills, hooks), so vendor lock-in deepens at the workflow layer, not the model layer. Security posture matters more — voice-injection (25) and the session-purge default (28) show that default configs leak data or attack surface.

## Possibility
Near term (1-3 months, ~70%): /workflows ships, Skills marketplaces (official + 3rd-party) explode, and 'cost-optimized routing' becomes a standard plugin pattern in Cursor/Continue/Antigravity. Medium (3-6 months, ~50%): swarm orchestration matures into stable libraries (LangGraph/CrewAI-style) wrapping Opus+Gemini+GPT roles; cost per finished feature drops 3-5x for teams who adopt. Lower likelihood (~25%): Anthropic opens a paid Skills marketplace with rev-share. Tail risk: voice-injection class attacks (25) force platforms to disable always-on assistants in shipped XR/edu apps.

## Org applicability — NDF DEV
High applicability for NDF DEV. Concrete moves: (1) Install the 31-skill SMB pack [10] and cherry-pick ones for quotation, contract, and report generation — pairs directly with paperwork pipeline. (2) Audit Claude Code settings against the 125-setting list [49]; even a 30-50% bill drop on Opus 4.7 is real money at studio scale. (3) Set cleanupPeriodDays=9999 across all dev machines this week [28] — cheap, prevents lost session context for Unity/XR debugging threads. (4) Prototype workflow routing for game dev: Flash/Haiku for shader tweaks and asset renames, Opus for gameplay logic, Gemini for long-context level design review — same pattern as [16][43]. (5) Wait-and-see on /workflows [18] until GA; then convert recurring NDF processes (build pipeline, e-learning lesson scaffolding, Supabase migration review) into named workflows. Skip the swarm hype until a stable framework lands.

## Signals to Watch
- Anthropic /workflows GA date and pricing model
- Third-party Skills marketplace emergence and license terms
- Antigravity tier-routing — does it auto-select or require manual choice
- Voice-injection mitigations from Google/Amazon/Apple — relevant if NDF ships voice-controlled XR

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **Lum1104/Understand-Anything** — Graphs that teach graphs that impress. Turn any code into an interactive knowledge graph you can exp | rss | <https://github.com/Lum1104/Understand-Anything> |
| **rohitg00/ai-engineering-from-scratch** — Learn it. Build it. Ship it for others. ░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒ | rss | <https://github.com/rohitg00/ai-engineering-from-scratch> |
| **anthropics/claude-plugins-official** — Official, Anthropic-managed directory of high quality Claude Code Plugins.Claude Code Plugins Direct | rss | <https://github.com/anthropics/claude-plugins-official> |
| **anthropics/knowledge-work-plugins** — Open source repository of plugins primarily intended for knowledge workers to use in Claude CoworkKn | rss | <https://github.com/anthropics/knowledge-work-plugins> |
| **multica-ai/andrej-karpathy-skills** — A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations | rss | <https://github.com/multica-ai/andrej-karpathy-skills> |
| **earendil-works/pi** — AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods pi | rss | <https://github.com/earendil-works/pi> |
| **Alishahryar1/free-claude-code** — Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw (voice supported | rss | <https://github.com/Alishahryar1/free-claude-code> |
| **colbymchenry/codegraph** — Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, OpenCode, and Hermes Agent — fewer  | rss | <https://github.com/colbymchenry/codegraph> |
| **multica-ai/multica** — The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, trac | rss | <https://github.com/multica-ai/multica> |
| **shiyu-coder/Kronos** — Kronos: A Foundation Model for the Language of Financial Markets Kronos: A Foundation Model for the  | rss | <https://github.com/shiyu-coder/Kronos> |
| **manaflow-ai/cmux** — Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agentscmux A Ghostty | rss | <https://github.com/manaflow-ai/cmux> |
| **666ghj/MiroFish** — A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物 简洁通用的群体智能引擎， | rss | <https://github.com/666ghj/MiroFish> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bryan_johnson | ^16398 c226 | [@jain_harshit You motherfuckers wouldn’t listen to me so I had to get claude inv](https://x.com/bryan_johnson/status/2058660071006183638) |
| reddit | tahir-k | ^3995 c70 | [Claude is not having a good morning](https://www.reddit.com/r/ClaudeAI/comments/1tlntio/claude_is_not_having_a_good_morning/) |
| x | PolymarketMoney | ^3058 c191 | [JUST IN: Anthropic is now projected to hit a $2,000,000,000,000+ valuation this ](https://x.com/PolymarketMoney/status/2058642109331132491) |
| x | Andr3jH | ^2753 c33 | [This river here is the official geographical border between Anthropic and OpenAI](https://x.com/Andr3jH/status/2058635602380104178) |
| x | nongsiii | ^2444 c2 | [Gemini with Papa Nicky 🥹🤍 cr: nicky_nopp GEMINIFOURTH RACE TO LOVE #LOLFanFest20](https://x.com/nongsiii/status/2058732530879361245) |
| x | justalesky | ^2043 c2 | [https://t.co/8JrYqOmp5n Gemini: “Thank you so much. We’ve actually never had a f](https://x.com/justalesky/status/2058792384444743806) |
| x | StealthQE4 | ^1987 c479 | [So if Anthropic, SpaceX, and Open AI all go public around the same time the mark](https://x.com/StealthQE4/status/2058719626817626500) |
| x | ns123abc | ^1665 c90 | [🚨 Google DeepMind CEO Sir Demis Hassabis: “Today’s systems, are nowhere near [AG](https://x.com/ns123abc/status/2058705608564457733) |
| x | Angelyu_yyy | ^1415 c2 | [William➕Gemini➕BounPrem WILLIAMEST REDLINE LUV #LOLFanFest2026D3 #WilliamEst #wi](https://x.com/Angelyu_yyy/status/2058659725877858634) |
| reddit | davidnguyen191 | ^1404 c69 | [🚀 Skills for small businesses, officially released by Anthropic Anthropic’s 31 s](https://www.reddit.com/r/ClaudeAI/comments/1tm94ai/skills_for_small_businesses_officially_released/) |
| x | gurishsharma | ^1395 c66 | [I talked to a new grad yesterday and it blows my mind that they are all aware wo](https://x.com/gurishsharma/status/2058663730380993004) |
| reddit | No-Wheel5791 | ^1258 c269 | [$2,500/mo AI Budget: My friend just burned through 62M Opus 4.7 tokens in 24 hou](https://www.reddit.com/r/ClaudeAI/comments/1tm36z1/2500mo_ai_budget_my_friend_just_burned_through/) |
| x | g4snara | ^1257 c0 | [fourth has to dye his hair back to black tomorrow to film for scarlet heart and ](https://x.com/g4snara/status/2058790720962802031) |
| x | hopes_revenge | ^1236 c26 | [FYI - they make you take a 25mg edible before the anthropic culture fit intervie](https://x.com/hopes_revenge/status/2058724977244016645) |
| x | justalesky | ^1167 c1 | [https://t.co/adeSqekqPa Fourth: “I think I actually gained something from Tanrak](https://x.com/justalesky/status/2058799054482714641) |
| x | _mohansolo | ^1142 c170 | [We heard concerns that Antigravity consumes many tokens for simple tasks now. So](https://x.com/_mohansolo/status/2058740603563966758) |
| x | nongsiii | ^1139 c0 | [Gemini confirmed that there will be 6 eps in total, and another OST will be rele](https://x.com/nongsiii/status/2058783540863721782) |
| x | DanielMiessler | ^1115 c103 | [Claude Code is about to release a feature called /workflows that I think will be](https://x.com/DanielMiessler/status/2058699741140222055) |
| x | nongsiii | ^1084 c0 | [👩🏻: mae can do gemini’s pose na luk 4️⃣: this is not gemini, this is somgem 😹 ♊️](https://x.com/nongsiii/status/2058782067643854886) |
| reddit | Devotion-Companion | ^1045 c136 | [We're one step closer to technological transcendence…now they do animated gaussi](https://www.reddit.com/r/singularity/comments/1tmtajd/were_one_step_closer_to_technological/) |
| x | justalesky | ^1017 c1 | [https://t.co/nhK6Aqlq4d 5555555555&555555 Gemini: “So… where should we go today?](https://x.com/justalesky/status/2058798639011778876) |
| x | RiserMusic | ^960 c1 | [#HITZTHAILANDCHARTSHOW 🎵🙏🏻 NO.1✨ อยู่ด้วยกันนะ (Every Single Day) - FOURTH NO.2✨](https://x.com/RiserMusic/status/2058792956002488519) |
| x | mikeoxmall70174 | ^949 c3 | [Claude scan hinge and find one of these. Make no mistakes](https://x.com/mikeoxmall70174/status/2058698421427384504) |
| reddit | Independent-Wind4462 | ^923 c109 | [Google DeepMind's Al agent autonomously solved 9 of 353 open Erdos problems in m](https://www.reddit.com/r/singularity/comments/1tmjdru/google_deepminds_al_agent_autonomously_solved_9/) |
| reddit | Distinct-Question-16 | ^857 c69 | [Inaudible sounds to humans can be hidden in YouTube videos, podcasts, or music a](https://www.reddit.com/r/singularity/comments/1tmb7mz/inaudible_sounds_to_humans_can_be_hidden_in/) |
| x | fourthlyst | ^819 c0 | [not fourth making a little bread / meep cat smile and gemini being so whipped fo](https://x.com/fourthlyst/status/2058741137742217503) |
| x | MaitlandWard | ^775 c38 | [Picked up my new @Tesla ❤️ Loving the new Model Y Juniper! Looking forward to ve](https://x.com/MaitlandWard/status/2058722897187987478) |
| x | tenobrus | ^707 c26 | [this is ur regular public service announcement that Claude Code by default *perm](https://x.com/tenobrus/status/2058637806176702831) |
| x | AJs_AI | ^701 c83 | [OpenAI just copied my open-source project within Codex… Last week I built Backdo](https://x.com/AJs_AI/status/2058655974043611505) |
| x | FE_Shadows_EN | ^691 c23 | [New Season Pass Announcement The Uniting Wind Season Pass is coming soon! This w](https://x.com/FE_Shadows_EN/status/2058744613775589720) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bryan_johnson</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 16398 · 💬 226</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bryan_johnson/status/2058660071006183638">View @bryan_johnson on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@jain_harshit You motherfuckers wouldn’t listen to me so I had to get claude involved”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Bryan Johnson, frustrated that people ignored his argument, brought in Claude (AI) to settle the dispute or back his point.</dd>
      <dt>Why interesting</dt>
      <dd>A high-profile tech figure publicly using Claude as a credibility enforcer signals that AI is gaining authority as a neutral arbiter in human disputes, not just a productivity tool.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can invoke Claude explicitly as a neutral third party in internal standoffs — code review disputes, architecture debates, UX disagreements — to cut the back-and-forth on small teams.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bryan_johnson/status/2058660071006183638" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@tahir-k</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 3995 · 💬 70</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/ClaudeAI/comments/1tlntio/claude_is_not_having_a_good_morning/" target="_blank" rel="noopener"><img src="https://i.redd.it/a795ky5ihx2h1.png" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Claude is not having a good morning”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Reddit post (3.9k likes) mocking Claude AI for apparent service issues, errors, or degraded output quality — implying a rough outage or bad-response incident.</dd>
      <dt>Why interesting</dt>
      <dd>High engagement (3.9k likes) signals a real, widespread Claude outage or quality drop — not an isolated bug — meaning API-dependent teams got hit simultaneously.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's Claude-dependent workflows (AI tools, automation, any Anthropic API calls) need fallback handling — retry logic or a swap to a backup model — so one bad morning doesn't block delivery.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/ClaudeAI/comments/1tlntio/claude_is_not_having_a_good_morning/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PolymarketMoney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3058 · 💬 191</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PolymarketMoney/status/2058642109331132491">View @PolymarketMoney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“JUST IN: Anthropic is now projected to hit a $2,000,000,000,000+ valuation this year. https://t.co/277yn2IaIn”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Anthropic is projected to reach a $2 trillion+ valuation in 2026, signaling massive investor confidence in the company behind Claude.</dd>
      <dt>Why interesting</dt>
      <dd>A $2T valuation means Anthropic will have enormous resources to accelerate Claude model releases and API capabilities that small dev teams depend on.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should lock in API pricing tiers now before Anthropic adjusts rates post-valuation surge, and monitor new model rollouts closely to stay on the latest capable tier.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PolymarketMoney/status/2058642109331132491" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Andr3jH</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2753 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Andr3jH/status/2058635602380104178">View @Andr3jH on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This river here is the official geographical border between Anthropic and OpenAI. On the other side cosmic horror, torment nexus, machine despotism, you build spyware for the govt and you like it. On ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A satirical tweet contrasting Anthropic and OpenAI cultures — both build government spyware, but Anthropic has a constitution and feels bad about it.</dd>
      <dt>Why interesting</dt>
      <dd>The punchline exposes that 'AI safety branding' and actual government contracts coexist at both labs — a useful reality check on corporate AI ethics narratives.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable. Satire about big-lab politics; no actionable signal for the studio's Unity, XR, or web stack work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Andr3jH/status/2058635602380104178" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2444 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2058732530879361245">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gemini with Papa Nicky 🥹🤍 cr: nicky_nopp GEMINIFOURTH RACE TO LOVE #LOLFanFest2026D3 #Gemini_NT #เจมีไนน์ https://t.co/gb4BP4MC2k”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post celebrating Thai celebrity Gemini (from duo Gemini-Fourth) at LOL Fan Fest 2026 Day 3 with a person called Papa Nicky.</dd>
      <dt>Why interesting</dt>
      <dd>High-engagement fan content (2444 likes) shows Thai celebrity fandom culture drives significant organic reach on X with minimal content.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2058732530879361245" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@justalesky</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2043 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/justalesky/status/2058792384444743806">View @justalesky on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/8JrYqOmp5n Gemini: “Thank you so much. We’ve actually never had a first episode event before.” 🥹 P’Leo: “Really? Usually you only get final episode events, right?” Gemini: “We’ve never ev”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post about Thai actors Gemini and Fourth's emotional moment during their first-ever press tour event for 'Ticket to Heaven', where they revealed they'd never had a first or final episode event before.</dd>
      <dt>Why interesting</dt>
      <dd>2,000+ likes on pure fan sentiment with zero technical content shows parasocial/celebrity content still dominates X engagement over substance.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/justalesky/status/2058792384444743806" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@StealthQE4</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1987 · 💬 479</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/StealthQE4/status/2058719626817626500">View @StealthQE4 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“So if Anthropic, SpaceX, and Open AI all go public around the same time the market will need to find $6 trillion dollars to soak up all of these IPO shares. Where’s the money going to come from?”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The post questions where $6 trillion in capital will come from if Anthropic, SpaceX, and OpenAI all IPO at roughly the same time.</dd>
      <dt>Why interesting</dt>
      <dd>Three mega-cap tech IPOs hitting simultaneously would create massive capital rotation, potentially draining liquidity from smaller tech stocks and AI-adjacent sectors that small dev studios track.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable. This is macro finance speculation with no actionable tech or workflow angle for the studio.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/StealthQE4/status/2058719626817626500" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ns123abc</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1665 · 💬 90</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ns123abc/status/2058705608564457733">View @ns123abc on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 Google DeepMind CEO Sir Demis Hassabis: “Today’s systems, are nowhere near [AGI]. Doesn’t matter how many Erdős problems you solve… I think it’s far, far from what a true invention or someone like a”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google DeepMind CEO Demis Hassabis says current AI systems are far from AGI, arguing that solving math competition problems like Erdős doesn't compare to true inventive genius like Ramanujan.</dd>
      <dt>Why interesting</dt>
      <dd>A direct pushback from DeepMind's own CEO against AGI benchmark hype — signals that math-problem benchmarks are poor proxies for real creative intelligence.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should treat AI tools as capable assistants, not creative decision-makers — avoid over-relying on LLMs for novel game design or XR interaction patterns where real invention is still needed.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ns123abc/status/2058705608564457733" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
