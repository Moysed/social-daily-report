---
type: social-topic-report
date: '2026-06-17'
topic: ai-devtools
lang: en
pair: ai-devtools.th.md
generated_at: '2026-06-17T15:05:15+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- hackernews
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 197
salience: 0.82
sentiment: mixed
confidence: 0.6
tags:
- ai-devtools
- coding-agents
- open-weights-llm
- mcp
- vercel
- cursor
thumbnail: https://pbs.twimg.com/media/HK80XzjbQAA2TsL.jpg
---

# AI Devtools — 2026-06-17

## TL;DR
- GLM-5.2 (open weights) reportedly crossed 80% on Terminal-Bench and tops the Artificial Analysis open-weights index, with claims it beats Gemini and Opus 4.x at roughly one-tenth the cost [11][27][43][34].
- Vercel shipped 'eve', a file-convention agent framework, plus an 'Agent Stack' (AI SDK, AI Gateway, Workflow SDK, Sandbox, Chat SDK, Vercel Connect), with 30-minute function invocations and 24-hour sandbox lifetimes [1][46][60][59].
- Cursor/Graphite's Tomas Reimers announced 'Origin', a Git alternative aimed at agent workloads with MCP/API extensibility and built-in merge-conflict handling [3]; separately Reuters reported a $60B SpaceX–Anysphere (Cursor) deal [10].
- Figma's MCP server expanded to generate/edit Figma Slides, build FigJam data boards, and roundtrip code-to-canvas, now with custom fonts and image export [16].
- Agent 'skills' repos are trending: agent-skills (60,800+ stars), obra/superpowers, mattpocock/skills [23][9][6]; code-graph MCP servers (Gortex, codebase-memory-mcp) claim large token reductions for coding agents [50][33].

## What happened
Today's AI devtools signal clusters around three things. First, open-weights momentum: multiple items report GLM-5.2 leading the Artificial Analysis open-weights index, crossing 80% on Terminal-Bench, and being positioned against Gemini and Opus 4.x at about a tenth of the price [11][27][43][34]; a separate post argues local models are now good enough for real work [8]. Second, agent tooling from Vercel: an agent framework 'eve' modeled on Next.js file conventions [1][13], an 'Agent Stack' bundling AI SDK, AI Gateway, Workflow SDK, Sandbox, Chat SDK and Vercel Connect [46], scoped short-lived tokens via Vercel Connect [59][32], and longer execution limits (30-minute functions, 24-hour sandboxes) [60]. Third, infrastructure around coding agents: Cursor/Graphite's 'Origin' Git alternative built for agent workloads [3], plus a reported $60B SpaceX acquisition of Cursor maker Anysphere [10].

## Why it matters (reasoning)
The pricing pressure is the most actionable thread: if GLM-5.2's open-weights claims hold, a studio can run capable coding/agent models self-hosted or via cheaper inference, reducing dependence on a single closed vendor [11][27][43]. That matters more given vendor instability — a $60B Cursor acquisition rumor [10] and Fable's shutdown [4][37][49] both show how quickly the tool/model you standardize on can change hands or disappear. Second-order: the convergence on MCP as the integration layer (Figma [16], Lovable [48], Gortex/codebase-memory [50][33], cybersecurity tooling [56]) means investing in MCP-based workflows is becoming portable across editors and agents rather than locked to one IDE. The recurring 'hard part is the data/OAuth/tokens/scopes' point [32] and code-graph token-reduction tools [50][33] both signal that cost and plumbing, not raw model capability, are now the real adoption bottlenecks.

## Possibility
Likely: open-weights models keep closing the gap on closed frontier models on coding benchmarks, making multi-model setups (closed + open fallback) standard — multiple independent items already report GLM-5.2 at or above closed models [11][27][34][43]. Plausible: MCP consolidates as the default agent-integration standard across editors and design tools, given how many vendors shipped MCP this cycle [16][48][50][33][56]. Plausible but unverified: the SpaceX–Cursor deal [10] is a single Reuters-style headline with no corroborating items here; treat as rumor until confirmed. Unlikely (near-term): Vercel's 'eve'/Agent Stack becomes a safe default — it is a fresh, heavily-marketed launch [1][13][18][28] with no maturity track record yet.

## Org applicability — NDF DEV
1) Benchmark GLM-5.2 against your current coding-agent model on a real Unity/web task and on cost; if claims hold it can cut spend roughly 10x — effort med [11][27][43][34]. 2) Pilot one MCP server in your existing editor for design-to-code: Figma MCP for UI work (Slides/FigJam/code roundtrip) fits edutech and app screens — effort low/med [16]. 3) Trial a code-graph MCP (Gortex or codebase-memory-mcp) on one repo to measure token savings before committing — effort low [50][33]. 4) Adopt a vetted subset of agent 'skills' (obra/superpowers, agent-skills) into your .claude/agent config rather than writing from scratch — effort low [9][23][6]. 5) For web/mobile/edutech apps, evaluate Vercel Connect's scoped short-lived tokens as a pattern for agent auth, even if you don't adopt the full stack — effort med [59][32]. Skip for now: committing to Vercel 'eve'/Agent Stack as a base (too new) [1][46]; reacting to the SpaceX–Cursor rumor [10]; Hermes/crypto-agent hackathon tooling [7][51] and smart-contract exploitation report [52] — not relevant to your stack.

## Signals to Watch
- GLM-5.2 real-world adoption and whether benchmark wins survive independent eval [11][27][43].
- MCP server proliferation across design/dev tools as a portability standard [16][48][50][33].
- Confirmation or denial of the SpaceX–Anysphere/Cursor acquisition and any tooling impact [10].
- Vercel Agent Stack maturity — execution limits, pricing, lock-in — before it's production-safe [46][60].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **Panniantong/Agent-Reach** — Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub,  | radar | <https://github.com/Panniantong/Agent-Reach> |
| **mattpocock/skills** — Skills for Real Engineers. Straight from my .claude directory. | radar | <https://github.com/mattpocock/skills> |
| **obra/superpowers** — An agentic skills framework & software development methodology that works. | radar | <https://github.com/obra/superpowers> |
| **freeCodeCamp/freeCodeCamp** — freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer scienc | radar | <https://github.com/freeCodeCamp/freeCodeCamp> |
| **Universal-Debloater-Alliance/universal-android-debloater-next-generation** — Cross-platform GUI written in Rust using ADB to debloat non-rooted Android devices. Improve your pri | radar | <https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation> |
| **n0-computer/iroh** — IP addresses break, dial keys instead. Modular networking stack in Rust. | radar | <https://github.com/n0-computer/iroh> |
| **chatwoot/chatwoot** — Open-source live-chat, email support, omni-channel desk. An alternative to Intercom, Zendesk, Salesf | radar | <https://github.com/chatwoot/chatwoot> |
| **DeusData/codebase-memory-mcp** — High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — | radar | <https://github.com/DeusData/codebase-memory-mcp> |
| **meshery/meshery** — Meshery, the cloud native manager | radar | <https://github.com/meshery/meshery> |
| **bytedance/UI-TARS-desktop** — The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra | radar | <https://github.com/bytedance/UI-TARS-desktop> |
| **krahets/hello-algo** — 《Hello 算法》：动画图解、一键运行的数据结构与算法教程。支持简中、繁中、English、日本語，提供 Python, Java, C++, C, C#, JS, Go, Swift, Rust, | radar | <https://github.com/krahets/hello-algo> |
| **penpot/penpot** — Penpot: The open-source design tool for design and code collaboration | radar | <https://github.com/penpot/penpot> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | vercel | ^3309 c162 | [Introducing eve, an agent framework. 𝚊𝚐𝚎𝚗𝚝/ 𝚊𝚐𝚎𝚗𝚝.𝚝𝚜 𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝𝚒𝚘𝚗𝚜.𝚖𝚍 𝚝𝚘𝚘𝚕𝚜/ 𝚜𝚔𝚒𝚕](https://x.com/vercel/status/2067180054979936413) |
| x | theo | ^3109 c250 | [I hate to admit it but the loop people were right](https://x.com/theo/status/2067115748959682743) |
| x | swyx | ^2572 c112 | [Cursor/Graphite’s @TomasReimers just announced Origin @cursor_ai’s long awaited ](https://x.com/swyx/status/2066928345246470204) |
| x | simonw | ^2184 c143 | [If this really is the "jailbreak" that got Fable shut down I'm deeply unimpresse](https://x.com/simonw/status/2066722034491789720) |
| radar | Panniantong_Agent-Reach | ^2025 c0 | [Panniantong/Agent-Reach Give your AI agent eyes to see the entire internet. Read](https://github.com/Panniantong/Agent-Reach) |
| radar | mattpocock_skills | ^1849 c0 | [mattpocock/skills Skills for Real Engineers. Straight from my .claude directory.](https://github.com/mattpocock/skills) |
| x | NousResearch | ^1545 c107 | [The Hermes Agent Accelerated Business Hackathon presented by @NVIDIAAI × @stripe](https://x.com/NousResearch/status/2066921443548348436) |
| hackernews | jfb | ^1447 c555 | [Running local models is good now](https://vickiboykis.com/2026/06/15/running-local-models-is-good-now/) |
| radar | obra_superpowers | ^1109 c0 | [obra/superpowers An agentic skills framework & software development methodology ](https://github.com/obra/superpowers) |
| hackernews | itsmarcelg | ^1087 c1584 | [SpaceX to buy Cursor for $60B](https://www.reuters.com/legal/transactional/spacex-buy-anysphere-60-billion-2026-06-16/) |
| x | cline | ^1024 c23 | [GLM-5.2 is the first open-weights model to cross 80% on Terminal-Bench, and beat](https://x.com/cline/status/2066951439793242193) |
| x | neogeo8man | ^1007 c4 | [the writing in these is like a mean parody of later Jones cartoons by one of his](https://x.com/neogeo8man/status/2066794474559213833) |
| x | rauchg | ^966 c92 | [https://t.co/uNXS9jEgpg is Next.js for agents. I built Next with a simple premis](https://x.com/rauchg/status/2067183015214584307) |
| hackernews | Cider9986 | ^909 c476 | [GrapheneOS has been ported to Android 17](https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon) |
| radar | freeCodeCamp_freeCodeCamp | ^764 c0 | [freeCodeCamp/freeCodeCamp freeCodeCamp.org's open-source codebase and curriculum](https://github.com/freeCodeCamp/freeCodeCamp) |
| x | figma | ^712 c27 | [Updates to the Figma MCP server: → Generate and edit decks in Figma Slides → Bui](https://x.com/figma/status/2066923337889305038) |
| x | AndroidDev | ^700 c24 | [Android 17 has arrived! 🎉 We're bringing together next generation tools, librari](https://x.com/AndroidDev/status/2066954030115352984) |
| x | rauchg | ^694 c44 | [Tomorrow https://t.co/hO8iYOkXYk some big announcements! https://t.co/wmn8ZHNQjz](https://x.com/rauchg/status/2066838428218486827) |
| x | rauchg | ^659 c89 | [New https://t.co/A1yfEM2Rig is live, highlighting the present and future of our ](https://x.com/rauchg/status/2067165617275256982) |
| x | finbarrtimbers | ^568 c45 | [Today was my second day at Microsoft Superintelligence, where I’ll be working on](https://x.com/finbarrtimbers/status/2066647629979963541) |
| hackernews | pseudolus | ^503 c218 | [Calvin and Hobbes and the price of integrity](https://therepublicofletters.substack.com/p/calvin-and-hobbes-and-the-price-of) |
| hackernews | mrshu | ^497 c214 | [TIL: You can make HTTP requests without curl using Bash /dev/TCP](https://mareksuppa.com/til/bash-dev-tcp-http-without-curl/) |
| x | sharbel | ^474 c25 | [Someone built a free collection of production-grade engineering skills that teac](https://x.com/sharbel/status/2066872849046933768) |
| hackernews | thm | ^467 c244 | [Sixty percent of US consumers say 'AI' in brand messaging is a turnoff](https://wpvip.com/future-of-the-web-2026/) |
| radar | Universal-Debloater-Alliance_universal-android-debloater-next-generation | ^465 c0 | [Universal-Debloater-Alliance/universal-android-debloater-next-generation Cross-p](https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation) |
| hackernews | dzonga | ^452 c264 | [Stop Using JWTs](https://gist.github.com/samsch/0d1f3d3b4745d778f78b230cf6061452) |
| hackernews | himata4113 | ^451 c242 | [GLM-5.2 is the new leading open weights model on Artificial Analysis](https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index) |
| x | rauchg | ^428 c51 | [It’s time to ship](https://x.com/rauchg/status/2067106499449565265) |
| radar | n0-computer_iroh | ^422 c0 | [n0-computer/iroh IP addresses break, dial keys instead. Modular networking stack](https://github.com/n0-computer/iroh) |
| radar | chatwoot_chatwoot | ^400 c0 | [chatwoot/chatwoot Open-source live-chat, email support, omni-channel desk. An al](https://github.com/chatwoot/chatwoot) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vercel</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3309 · 💬 162</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vercel/status/2067180054979936413">View @vercel on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing eve, an agent framework. 𝚊𝚐𝚎𝚗𝚝/ 𝚊𝚐𝚎𝚗𝚝.𝚝𝚜 𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝𝚒𝚘𝚗𝚜.𝚖𝚍 𝚝𝚘𝚘𝚕𝚜/ 𝚜𝚔𝚒𝚕𝚕𝚜/ 𝚜𝚊𝚗𝚍𝚋𝚘𝚡/ 𝚜𝚌𝚑𝚎𝚍𝚞𝚕𝚎𝚜/ Like Next.js, for agents. https://t.co/ezUIGLkSqG”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Vercel launched 'eve', a file-convention-based agent framework with folders for tools, skills, sandbox, and schedules — positioned as 'Next.js for agents'.</dd>
      <dt>Why interesting</dt>
      <dd>Teams already on Next.js get a familiar mental model for structuring agents, cutting time spent designing agent architecture from scratch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Check the eve GitHub repo to see if the tools/skills/sandbox structure maps to any agent features planned for the studio's web projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vercel/status/2067180054979936413" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3109 · 💬 250</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2067115748959682743">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I hate to admit it but the loop people were right”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Theo Browne (@theo, ~500k web-dev followers), a known AI-workflow skeptic, publicly concedes that advocates of agentic coding loops were correct about their value.</dd>
      <dt>Why interesting</dt>
      <dd>A credible skeptic reversing on agentic loops is a signal the pattern — AI iterating autonomously until done — has crossed from hype into demonstrated value.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Audit whether the studio's AI-assisted workflows use single-shot prompting or agentic loops; if the former, test a loop-based agent on a contained task this sprint.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2067115748959682743" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@swyx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2572 · 💬 112</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/swyx/status/2066928345246470204">View @swyx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Cursor/Graphite’s @TomasReimers just announced Origin @cursor_ai’s long awaited Git competitor, scalable for agent workloads, extensible with api and mcp, and built in merge conflicts and co failure a”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Tomas Reimers (Cursor/Graphite) announced Origin, a Git-replacement VCS with native AI agent workload support, API/MCP extensibility, and automated merge-conflict and CI-failure resolution.</dd>
      <dt>Why interesting</dt>
      <dd>A VCS built around agent workloads means branching, merging, and CI recovery could run without human intervention — directly applicable to any multi-agent dev pipeline.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Track Origin's public release and pilot it on one internal project already running Cursor, specifically testing agent-driven branch and conflict resolution.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/swyx/status/2066928345246470204" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@simonw</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2184 · 💬 143</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/simonw/status/2066722034491789720">View @simonw on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If this really is the &quot;jailbreak&quot; that got Fable shut down I'm deeply unimpressed https://t.co/tRhzKcFHRX”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Simon Willison reviewed the jailbreak reportedly responsible for shutting down the AI model Fable and found it unsophisticated — implying the shutdown decision was disproportionate to the actual risk.</dd>
      <dt>Why interesting</dt>
      <dd>An AI product shutting down over a trivial exploit signals that risk tolerance is low — teams shipping AI features need clear incident response policies before launch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Define a simple AI incident policy for the studio: what triggers a feature kill switch, who decides, and how fast — before any AI feature goes live.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/simonw/status/2066722034491789720" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NousResearch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1545 · 💬 107</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NousResearch/status/2066921443548348436">View @NousResearch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Hermes Agent Accelerated Business Hackathon presented by @NVIDIAAI × @stripe × @NousResearch starts now, for builders making agents that can earn, spend, and run real operations at any scale. Our ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Nous Research × NVIDIA × Stripe opened a hackathon (deadline June 30) for autonomous business agents on Hermes + Stripe Skills; 1st prize is $10k cash + DGX Spark + $5k Stripe credits.</dd>
      <dt>Why interesting</dt>
      <dd>Stripe Skills lets agents autonomously buy services, provision SaaS, and handle payments — a working blueprint for agentic commerce the studio can study and adapt.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio has 13 days to enter — build a demo agent using Hermes + Stripe Skills, record a 1–3 min video, and submit the form before June 30.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NousResearch/status/2066921443548348436" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cline</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1024 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cline/status/2066951439793242193">View @cline on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“GLM-5.2 is the first open-weights model to cross 80% on Terminal-Bench, and beats every other open model available. It also beats Gemini, making it a frontier-level model for a fraction of the cost. O”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>GLM-5.2 is the first open-weights model to exceed 80% on Terminal-Bench, outperforming all other open models and Gemini on that benchmark, and is now available inside Cline.</dd>
      <dt>Why interesting</dt>
      <dd>A high-benchmark open model inside Cline gives the team a strong terminal/coding AI option at a fraction of proprietary API costs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test GLM-5.2 in Cline on terminal-heavy tasks to determine whether it can replace a higher-cost model in the studio's daily workflow.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cline/status/2066951439793242193" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@neogeo8man</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1007 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/neogeo8man/status/2066794474559213833">View @neogeo8man on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“the writing in these is like a mean parody of later Jones cartoons by one of his critics, but to be fair he was 89 and dying very impressive Flash brush tool use tho, esp given this was 2001 https://t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user comments on 2001-era Flash animation, noting the brush tool technique despite the artist being 89 and the writing quality being poor.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/neogeo8man/status/2066794474559213833" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 966 · 💬 92</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2067183015214584307">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/uNXS9jEgpg is Next.js for agents. I built Next with a simple premise: 𝚙𝚊𝚐𝚎𝚜/𝚒𝚗𝚍𝚎𝚡.𝚓𝚜 is all you need. Put some React in there and you’re good to go. Eve asks for even less. 𝚊𝚐𝚎𝚗𝚝/𝚒𝚗𝚜𝚝𝚛𝚞𝚌𝚝”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Guillermo Rauch (Vercel CEO) released Eve, a filesystem-based agent framework where agent/instructions.md defines the agent and tools/*.ts files expose its capabilities, deployable on Vercel infra.</dd>
      <dt>Why interesting</dt>
      <dd>Eve's file-based convention makes agent structure readable and version-controllable with zero new abstractions — any dev familiar with Next.js can pick it up immediately.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's web team can spin up a throwaway Eve project with one instructions.md and one tools/*.ts to benchmark its DX against the current agent setup before adopting it.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2067183015214584307" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
