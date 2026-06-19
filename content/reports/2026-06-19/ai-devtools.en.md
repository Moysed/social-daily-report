---
type: social-topic-report
date: '2026-06-19'
topic: ai-devtools
lang: en
pair: ai-devtools.th.md
generated_at: '2026-06-19T03:07:25+00:00'
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
post_count: 319
salience: 0.85
sentiment: mixed
confidence: 0.62
tags:
- ai-devtools
- coding-agents
- mcp
- claude-code
- codex
- agent-skills
thumbnail: https://pbs.twimg.com/media/HLHZhd5WsAAzjSC.jpg
---

# AI Devtools — 2026-06-19

## TL;DR
- Anthropic launched Artifacts in Claude Code: interactive HTML pages (PR walkthroughs, dashboards, diagrams) built from a session and shared via private link, that update as the session runs — beta on Team/Enterprise, Pro/Max promised next [1][6][7][16][26].
- OpenAI added Record & Replay to Codex (app 26.616): demonstrate a recurring task once and Codex converts the demo into a reusable skill; macOS-only and not available in EEA/UK/Switzerland [2][11][24][38].
- Unreal Engine 5.8 shipped with experimental MCP server support, letting any agent connect to the engine, pipeline, and workflow [4][13].
- GLM 5.2 was claimed ~6x cheaper than Opus 4.8 on one landing-page design task ($0.06 vs $0.49); a separate post claims a 2-bit local quant on a Mac Studio beats Opus 4.8 — both single-author, unverified [3][17].
- MCP keeps spreading across the stack: codebase-memory-mcp knowledge graph [8], Lovable [32] and Replit [34] Claude integrations, Cua Linux computer-use [37], plus Cursor's /automate skill [9].

## What happened
Two large vendor launches dominated: Claude Code Artifacts, announced by Anthropic and amplified by its engineers, turns session work into shareable interactive HTML pages that keep updating, currently limited to Team and Enterprise plans [1][6][7][16][26]. OpenAI shipped Codex Record & Replay (app version 26.616), which captures a demonstrated cross-application workflow and turns it into an executable skill, with users reporting tasks like triaging stale PRs [2][11][14][24]; it is macOS-only and excluded from EEA, UK, and Switzerland [38]. Unreal Engine 5.8 added experimental MCP server support so agents can act inside game development [4][13]. On models, GLM 5.2 was promoted as matching Opus 4.8 design quality at roughly one-sixth the cost in a single comparison [3], with a more extreme local-quant claim from another account [17]. Supporting items show continued MCP/agent-tooling growth: a code-intelligence MCP server [8], Lovable and Replit Claude integrations [32][34], Cua's Linux computer-use [37], Cursor's /automate [9] and SDK-built support bots [22], open-source agents (kilocode [19], superpowers [15]), and Google's guide on building and evaluating agent skills [47]. A Claude Code usage-limit bug hit ~3% of Max/Pro users and was fixed [60].

## Why it matters (reasoning)
The pattern across [1][2][9][47] is a shift from chat prompting to reusable, shareable agent units — skills, recorded workflows, and shared artifacts — which lowers the cost of repeating and distributing agent work inside a team rather than re-prompting each time. MCP is becoming the default integration layer: when a game engine [4], design/deploy tools [32][34], and code-memory servers [8] all expose MCP, an agent can chain across previously siloed tools, which is the second-order shift to watch. The GLM 5.2 cost claims [3][17], if they hold under real testing, point to continued price compression that makes routine front-end/edutech generation cheap; but a single screenshot comparison is weak evidence and the local-quant claim [17] is anecdotal. The Claude Code bug [60] and the regional/OS limits on Codex [38] are reminders these are early-stage betas, not stable infrastructure.

## Possibility
Likely: Artifacts and Record & Replay expand to lower tiers and other OSes, since both vendors stated rollout intent and Artifacts is explicitly 'coming to Pro and MAX' [16][1]. Likely: MCP support keeps spreading to more engines and SaaS tools given the breadth already shipping in one day [4][8][32][34][37]. Plausible: GLM 5.2 becomes a viable cheap option for design/web tasks, but the 6x-cheaper and 'beats Opus' claims need independent benchmarks before adoption [3][17]. Plausible: 'self-improving agent loops' [25] and skill marketplaces grow, though the '100+ agents per engineer' figure is an unverified podcast claim. Unlikely near-term: stable, production-grade reliability — early bugs [60] and regional gating [38] suggest churn.

## Org applicability — NDF DEV
1) Pilot Claude Code Artifacts for sharing edutech/web prototypes, dashboards, and design previews with the team and clients — low effort, but requires a Team/Enterprise seat today [1][6][26]. 2) Test Codex Record & Replay on a repetitive ops task (build steps, asset processing, release notes); confirm a teammate is on macOS and outside the excluded regions — low/med effort [2][24][38]. 3) Trial codebase-memory-mcp on one Unity/web repo to give agents persistent code context; verify the speed/coverage claims yourself — med effort [8]. 4) For cheap web/landing or e-learning page generation, run a controlled GLM 5.2 vs current-model bake-off on real tasks before any switch — med effort [3]. 5) Track MCP in game engines: Unreal 5.8 ships it now [4][13]; check the equivalent path for your Unity pipeline. Read Google's agent-skills guide before standardizing internal skills [47]. Skip: the 2-bit local-GLM 'beats Opus' claim [17] and the unofficial DevSpace '2x Codex limits' connector [18] (unverified/risky); crypto/investing items [27][49] are out of scope.

## Signals to Watch
- Watch when Claude Code Artifacts reaches Pro/Max and whether export/self-host is allowed — gates team adoption [1][16].
- Watch for Codex Record & Replay leaving macOS-only and the EEA/UK/Switzerland exclusion — affects availability [24][38].
- Watch for independent GLM 5.2 benchmarks and real per-task cost, not single screenshots [3][17].
- Watch MCP landing in Unity tooling the way it did in Unreal 5.8 [4][13][8].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **DeusData/codebase-memory-mcp** — High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — | radar | <https://github.com/DeusData/codebase-memory-mcp> |
| **obra/superpowers** — An agentic skills framework & software development methodology that works. | radar | <https://github.com/obra/superpowers> |
| **Kilo-Org/kilocode** — Kilo is the all-in-one agentic engineering platform. Build, ship, and iterate faster with the most p | radar | <https://github.com/Kilo-Org/kilocode> |
| **google-research/timesfm** — TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Goo | radar | <https://github.com/google-research/timesfm> |
| **makeplane/plane** — 🔥🔥🔥 Open-source Jira, Linear, Monday, and ClickUp alternative. Plane is a modern project management  | radar | <https://github.com/makeplane/plane> |
| **freeCodeCamp/freeCodeCamp** — freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer scienc | radar | <https://github.com/freeCodeCamp/freeCodeCamp> |
| **n0-computer/iroh** — IP addresses break, dial keys instead. Modular networking stack in Rust. | radar | <https://github.com/n0-computer/iroh> |
| **alibaba/zvec** — A lightweight, lightning-fast, in-process vector database | radar | <https://github.com/alibaba/zvec> |
| **Universal-Debloater-Alliance/universal-android-debloater-next-generation** — Cross-platform GUI written in Rust using ADB to debloat non-rooted Android devices. Improve your pri | radar | <https://github.com/Universal-Debloater-Alliance/universal-android-debloater-next-generation> |
| **zai-org/GLM-5** — GLM-5: From Vibe Coding to Agentic Engineering | radar | <https://github.com/zai-org/GLM-5> |
| **withastro/flue** — The sandbox agent framework. | radar | <https://github.com/withastro/flue> |
| **yifanfeng97/Hyper-Extract** — Transform unstructured text into structured knowledge with LLMs. Graphs, hypergraphs, and spatio-tem | radar | <https://github.com/yifanfeng97/Hyper-Extract> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | claudeai | ^11090 c432 | [New in Claude Code: Artifacts. Interactive pages built from your session, like a](https://x.com/claudeai/status/2067671912038240487) |
| x | OpenAIDevs | ^8277 c288 | [Show Codex a workflow once. Reuse it as a skill. Record &amp; Replay lets you sh](https://x.com/OpenAIDevs/status/2067681320281723113) |
| x | nutlope | ^7167 c295 | [This model is insane at design. I asked GLM 5.2 (left) and Opus 4.8 (right) to b](https://x.com/nutlope/status/2067313679951941686) |
| x | UnrealEngine | ^7109 c227 | [Unreal Engine 5.8 ships today with experimental MCP server support: Your sources](https://x.com/UnrealEngine/status/2067251500900839735) |
| x | ArmoredNorman | ^3595 c12 | [Wolves are intelligent enough to grasp tool use by others as an extension of the](https://x.com/ArmoredNorman/status/2067243248569942103) |
| x | bcherny | ^2419 c161 | [I've been using Artifacts in Claude Code for everything: visual explanations of ](https://x.com/bcherny/status/2067700226669060207) |
| x | ClaudeDevs | ^2397 c97 | [Artifacts are now live in Claude Code. Ask Claude to turn what it's working on i](https://x.com/ClaudeDevs/status/2067672094209675373) |
| radar | DeusData_codebase-memory-mcp | ^2322 c0 | [DeusData/codebase-memory-mcp High-performance code intelligence MCP server. Inde](https://github.com/DeusData/codebase-memory-mcp) |
| x | cursor_ai | ^2045 c76 | [Introducing /automate, a skill for agents to set up automations for you. Describ](https://x.com/cursor_ai/status/2067683814516858962) |
| x | amasad | ^1769 c22 | [@itamarbengvir @JDVance Have you said thank you once? https://t.co/QPrXGJAhHR](https://x.com/amasad/status/2067681537424855100) |
| x | gdb | ^1722 c59 | [you can now teach Codex by demonstration:](https://x.com/gdb/status/2067700691062464887) |
| x | rauchg | ^1630 c82 | [https://t.co/XdZBViUJdA](https://x.com/rauchg/status/2067586339021734029) |
| x | Polymarket | ^1554 c92 | [NEW: Unreal Engine 5.8 is launching with experimental MCP server support, allowi](https://x.com/Polymarket/status/2067509115186717133) |
| x | theo | ^1488 c54 | [I underestimated how cool this workflow is. Had Codex go through a bunch of stal](https://x.com/theo/status/2067688557448470761) |
| radar | obra_superpowers | ^1429 c0 | [obra/superpowers An agentic skills framework & software development methodology ](https://github.com/obra/superpowers) |
| x | trq212 | ^1422 c98 | [Claude Code can now upload and edit HTML artifacts that you can share with your ](https://x.com/trq212/status/2067682475611242546) |
| x | AlexFinn | ^1416 c176 | [I can't believe this is real I have GLM 5.2 running 100% locally on my Mac Studi](https://x.com/AlexFinn/status/2067751557379297762) |
| x | wshxnv | ^1391 c66 | [Alrighty, everything is ready 😎 here’s an unofficial “2x Codex limits” promo fro](https://x.com/wshxnv/status/2067327251335835852) |
| radar | Kilo-Org_kilocode | ^1345 c0 | [Kilo-Org/kilocode Kilo is the all-in-one agentic engineering platform. Build, sh](https://github.com/Kilo-Org/kilocode) |
| hackernews | ricochet11 | ^1283 c844 | [Midjourney Medical <a href="https:&#x2F;&#x2F;www.midjourney.com&#x2F;medical" r](https://www.midjourney.com/medical/blogpost) |
| x | Cybee15 | ^999 c3 | [@LeagueOfLeaks oh im gonna miss having the ability to dash forward towards my cu](https://x.com/Cybee15/status/2067666621422825885) |
| x | leerob | ^877 c57 | [The Cursor Slack has bots solving customer issues, followed by other bots reprod](https://x.com/leerob/status/2067638101900484993) |
| radar | google-research_timesfm | ^844 c0 | [google-research/timesfm TimesFM (Time Series Foundation Model) is a pretrained t](https://github.com/google-research/timesfm) |
| x | Codex_Changelog | ^819 c23 | [🚀 Codex app 26.616 is out! 🎬 Record &amp; Replay turns demos into reusable skill](https://x.com/Codex_Changelog/status/2067682048194543996) |
| x | 0xMovez | ^779 c39 | [Creator of Claude Code: "At Anthropic, almost 100% of our engineers are running ](https://x.com/0xMovez/status/2067642452991717790) |
| x | _catwu | ^769 c38 | [On Claude Team and Claude Enterprise, you can now use Claude Code to deploy HTML](https://x.com/_catwu/status/2067674836726694200) |
| x | teneo_protocol | ^715 c515 | [The Teneo CLI installs from wherever you already work. There are now setup guide](https://x.com/teneo_protocol/status/2067648649820012738) |
| hackernews | leonidasrup | ^708 c590 | [Swiss parliament lifts ban on new nuclear power plants](https://www.bluewin.ch/en/news/switzerland/parliament-lifts-ban-on-new-nuclear-power-plants-3257535.html) |
| hackernews | theorchid | ^679 c157 | [I found 10k GitHub repositories distributing Trojan malware](https://orchidfiles.com/github-repositories-distributing-malware/) |
| hackernews | Adam-Hincu | ^620 c411 | [Microsoft new Outlook takes 10 seconds to do what Outlook Classic does instantly](https://www.windowslatest.com/2026/06/15/microsofts-new-outlook-takes-10-seconds-to-do-what-outlook-classic-does-instantly-on-windows/) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@claudeai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 11090 · 💬 432</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/claudeai/status/2067671912038240487">View @claudeai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New in Claude Code: Artifacts. Interactive pages built from your session, like a PR walkthrough or a living project dashboard, shared with your team at a private link. Available in beta on Team and En”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Code now generates shareable interactive pages called Artifacts from a session — PR walkthroughs, project dashboards — delivered via private link, in beta on Team and Enterprise plans.</dd>
      <dt>Why interesting</dt>
      <dd>Artifacts turns a Claude Code session into a shareable deliverable without extra tooling — cuts the gap between coding and async handoff to teammates or clients.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio holds a Claude Code Team or Enterprise plan, pilot Artifacts for PR walkthroughs or sprint status pages shared with clients.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/claudeai/status/2067671912038240487" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@OpenAIDevs</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 8277 · 💬 288</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/OpenAIDevs/status/2067681320281723113">View @OpenAIDevs on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Show Codex a workflow once. Reuse it as a skill. Record &amp;amp; Replay lets you show Codex a recurring task, like filing an expense report or submitting a time-off request. Codex turns that demo into an”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>OpenAI's Codex now has a Record &amp; Replay feature that lets you demo a recurring workflow once — like submitting a form — and Codex converts it into an inspectable, editable skill you can reuse.</dd>
      <dt>Why interesting</dt>
      <dd>Small teams with repetitive internal tasks — HR forms, expense reports, deployment checklists — can encode those into reusable Codex skills instead of writing automation scripts from scratch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can trial Record &amp; Replay on one internal recurring workflow (e.g. build submission or asset handoff) to evaluate whether Codex-generated skills reduce manual overhead.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/OpenAIDevs/status/2067681320281723113" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nutlope</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7167 · 💬 295</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nutlope/status/2067313679951941686">View @nutlope on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This model is insane at design. I asked GLM 5.2 (left) and Opus 4.8 (right) to build me a landing page and you can't even tell the difference. GLM cost $0.06 while opus cost $0.49. More than 6x cheape”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>GLM 5.2 (open-source, Zhipu AI) generated a landing page visually on par with Claude Opus 4.8 at $0.06 vs $0.49 — 6x cheaper and faster with fewer tokens.</dd>
      <dt>Why interesting</dt>
      <dd>For a studio generating UI mockups or page scaffolds with LLMs regularly, switching to GLM 5.2 for design-heavy prompts cuts API costs by over 80%.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a side-by-side test: feed the studio's standard landing-page prompt to GLM 5.2 and compare output quality against the current model before swapping it into the pipeline.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nutlope/status/2067313679951941686" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7109 · 💬 227</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2067251500900839735">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Unreal Engine 5.8 ships today with experimental MCP server support: Your sources, your pipeline and your workflow—simply configure the MCP plugin and connect to any agent. Get familiar with the MCP se”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Unreal Engine 5.8 ships today with an experimental built-in MCP server plugin and the new PCG Primitive Plugin, letting teams connect any AI agent directly into the engine pipeline.</dd>
      <dt>Why interesting</dt>
      <dd>Engine-native MCP means AI agents can read or drive UE scenes and PCG graphs using the same open protocol already common across web and devtools stacks.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">For any XR/VR work that touches Unreal, test the MCP plugin now to evaluate AI-assisted PCG and scene workflows before the feature exits experimental.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2067251500900839735" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ArmoredNorman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3595 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ArmoredNorman/status/2067243248569942103">View @ArmoredNorman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wolves are intelligent enough to grasp tool use by others as an extension of the acts of another individual, thus the wolf understands he has been forcibly submitted and pinned by &quot;The Alpha&quot; but was ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A post about wolf behavior and social hierarchy — a wolf recognizing that a crab trap was used as a tool by a dominant pack member.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ArmoredNorman/status/2067243248569942103" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bcherny</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2419 · 💬 161</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bcherny/status/2067700226669060207">View @bcherny on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I've been using Artifacts in Claude Code for everything: visual explanations of tricky code, system diagrams, quick previews of a few animation options, data analyses and dashboards I share with the t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Code now supports Artifacts — inline rendered outputs (diagrams, dashboards, animation previews) shareable with teammates, confirmed by an Anthropic Claude Code team member.</dd>
      <dt>Why interesting</dt>
      <dd>Artifacts makes Claude Code a visual collaboration layer — explaining architecture or comparing animation options without switching tools.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can test Claude Code Artifacts for generating quick system diagrams or XR flow visuals during planning sessions and sharing directly with the team.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bcherny/status/2067700226669060207" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ClaudeDevs</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2397 · 💬 97</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ClaudeDevs/status/2067672094209675373">View @ClaudeDevs on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Artifacts are now live in Claude Code. Ask Claude to turn what it's working on into a page and send the link to your team. The page updates as the session keeps working. Available today on Team and En”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Code now generates a live, shareable web page from an active session that updates automatically as Claude continues working — available on Team and Enterprise plans.</dd>
      <dt>Why interesting</dt>
      <dd>A live page from a Claude Code session lets teammates or reviewers follow in-progress output without manual copy-paste or screenshots between updates.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio holds a Claude Code Team or Enterprise plan, test Artifacts during code reviews or internal handoffs to replace manual progress summaries.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ClaudeDevs/status/2067672094209675373" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cursor_ai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2045 · 💬 76</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cursor_ai/status/2067683814516858962">View @cursor_ai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing /automate, a skill for agents to set up automations for you. Describe your task in plain language. Cursor configures the triggers, instructions, and tools. https://t.co/PB7kZh0Izt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Cursor released /automate, an agent skill where developers describe a task in plain language and Cursor auto-configures the triggers, instructions, and tool bindings.</dd>
      <dt>Why interesting</dt>
      <dd>Cuts setup time for recurring dev workflows without writing config files — practical for any team already using Cursor as their primary editor.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can test /automate in Cursor to automate repetitive tasks like build triggers, asset pipelines, or test runs across Unity and web projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cursor_ai/status/2067683814516858962" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
