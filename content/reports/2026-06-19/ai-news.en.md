---
type: social-topic-report
date: '2026-06-19'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-06-19T03:12:02+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 246
salience: 0.62
sentiment: mixed
confidence: 0.6
tags:
- claude-code
- artifacts
- codex-skills
- benchmarks
- model-releases
- devtools
thumbnail: https://pbs.twimg.com/media/HLHZhd5WsAAzjSC.jpg
---

# AI News & New Skills — 2026-06-19

## TL;DR
- Anthropic shipped Artifacts in Claude Code: interactive HTML pages (PR walkthroughs, dashboards, diagrams) built from a session and shared via private link that updates live; beta on Team and Enterprise, Pro/MAX 'coming soon' [1][4][7][18].
- OpenAI Codex added a Record & Replay plugin that captures your actions and converts a workflow into an executable skill; not yet in EEA, UK, Switzerland [33].
- Claude 'Fable 5' is reported #1 on the DeepSWE long-horizon coding benchmark (+3% over prior best) [55], but is currently unavailable/'banned' amid Anthropic–US government access negotiations [44][45][46].
- GPT-5.6 / GPT-5.6-Pro launch is described as imminent; early takes say frontend improved but below Fable/Claude, with notable SVG/3D-SVG generation [10][26][36].
- Operational noise: a Claude Code bug mis-reported weekly usage limits for ~3% of Max/Pro users (fixed) [41]; Gemini CLI stopped serving Google AI Pro/Ultra/free individual tiers [38]; a report claims 10k GitHub repos distributing trojan malware [24].

## What happened
The dominant concrete artifact today is Claude Code Artifacts: Anthropic and team members describe turning an in-progress session into a shareable, auto-updating HTML page — PR walkthroughs, living dashboards, system diagrams, data analyses, and quick animation-option previews — available at a private link, launched in beta for Team and Enterprise with Pro/MAX promised later [1][3][4][7][18]. Separately, OpenAI's Codex gained a Record & Replay plugin that records user actions and emits a reusable executable 'skill,' excluding EEA/UK/Switzerland for now [33]. On models and benchmarks, datacurve reports Claude 'Fable 5' topping its DeepSWE long-horizon coding benchmark by 3% [55], while multiple posts say Fable 5 is unavailable/'banned' and tie its return to Anthropic's negotiations with the US administration over model access [44][45][46][19]. GPT-5.6/5.6-Pro is described as launching soon with strong SVG output but frontend quality still rated below Fable/Claude [10][26][36]. Artificial Analysis announced AA-Briefcase, a benchmark for long-horizon agentic knowledge work [43].

## Why it matters (reasoning)
Artifacts narrows the gap between 'AI did work in a session' and 'the team can see and act on it' without copy-paste or a separate doc tool [3][18]; for a studio juggling Unity, XR, and web/mobile, the animation-preview and dashboard use cases [3] map directly onto internal review and client communication. The catch is gating: value is real only if you're on Team/Enterprise, since Pro/MAX access is still pending [1][7]. Codex Record & Replay points at the same theme from OpenAI's side — turning ad-hoc workflows into repeatable skills [33] — signaling that 'capture and replay your process' is becoming a standard agent feature, not a differentiator. The Fable 5 situation is mostly second-hand and entangled with US-government access politics and self-reported benchmarks [44][45][46][55], so the practical takeaway is volatility in model availability, not a settled SOTA. The malware-repo report [24] and the Claude Code usage-limit bug [41] are reminders that AI-adjacent supply chain and tooling reliability remain live operational risks.

## Possibility
Likely: Artifacts reaches Pro/MAX within weeks given Anthropic explicitly stated it's coming and is already live for Team/Enterprise [1][7]. Plausible: 'record workflow → executable skill' becomes a cross-vendor norm as both Codex [33] and Claude's skills ecosystem converge. Plausible: GPT-5.6 ships in the near term, but its frontend/coding edge over Claude stays contested rather than decisive [10][26][36]. Unlikely to be reliable yet: Fable 5 as a dependable production model, since it is reported unavailable and its standing rests on a vendor-run benchmark and politicized access talks [44][45][46][55]. No source gives numeric probabilities, so none are asserted here.

## Org applicability — NDF DEV
1) If NDF DEV is on a Claude Code Team/Enterprise plan, pilot Artifacts for one PR walkthrough and one shared dashboard this week — low effort, high signal on whether it replaces ad-hoc Notion/Loom updates [1][3][18]; if only on Pro/MAX, wait for the announced rollout rather than switching tools [7]. 2) Trial Codex Record & Replay to capture a repetitive workflow (e.g., a build/test or asset-export sequence) as a reusable skill — med effort; confirm Thailand availability since only EEA/UK/Switzerland are excluded [33]. 3) Add a dependency-hygiene check before cloning/installing unfamiliar GitHub repos, given the 10k-trojan-repo report — low effort, pure process [24]. 4) Note operationally that the Claude Code usage-limit bug is fixed and limits were reset — no action beyond awareness [41]. 5) If anyone relies on Gemini CLI on Google AI Pro/Ultra/free tiers, plan a migration; those tiers are cut off [38]. Skip: do not adopt Fable 5 for production now [44][46]; ignore the horoscope, music, crypto, and political-drama items as noise.

## Signals to Watch
- Watch for Artifacts hitting Pro/MAX and whether it supports embedding interactive previews useful for Unity/XR demos [3][7].
- Track AA-Briefcase and DeepSWE results as a model-selection input for long-horizon coding/agent tasks [43][55].
- Monitor GPT-5.6/5.6-Pro actual release and independent (non-vendor) frontend/SVG benchmarks [10][26][36].
- Follow Fable 5 availability and the Anthropic–US access talks before depending on it [45][46].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **google-research/timesfm** — TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Goo | rss | <https://github.com/google-research/timesfm> |
| **n0-computer/iroh** — IP addresses break, dial keys instead. Modular networking stack in Rust. less net work for networks  | rss | <https://github.com/n0-computer/iroh> |
| **freeCodeCamp/freeCodeCamp** — freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer scienc | rss | <https://github.com/freeCodeCamp/freeCodeCamp> |
| **obra/superpowers** — An agentic skills framework & software development methodology that works.Superpowers Superpowers is | rss | <https://github.com/obra/superpowers> |
| **zai-org/GLM-5** — GLM-5: From Vibe Coding to Agentic EngineeringGLM-5.2 &amp; GLM-5.1 &amp; GLM-5 👋 Join our Wechat or | rss | <https://github.com/zai-org/GLM-5> |
| **DeusData/codebase-memory-mcp** — High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — | rss | <https://github.com/DeusData/codebase-memory-mcp> |
| **yifanfeng97/Hyper-Extract** — Transform unstructured text into structured knowledge with LLMs. Graphs, hypergraphs, and spatio-tem | rss | <https://github.com/yifanfeng97/Hyper-Extract> |
| **alibaba/zvec** — A lightweight, lightning-fast, in-process vector database English / 中文 🚀 Quickstart / 🏠 Home / 📚 Doc | rss | <https://github.com/alibaba/zvec> |
| **withastro/flue** — The sandbox agent framework.Flue — The Agent Harness Framework Not another SDK. Build autonomous age | rss | <https://github.com/withastro/flue> |
| **Kilo-Org/kilocode** — Kilo is the all-in-one agentic engineering platform. Build, ship, and iterate faster with the most p | rss | <https://github.com/Kilo-Org/kilocode> |
| **makeplane/plane** — 🔥🔥🔥 Open-source Jira, Linear, Monday, and ClickUp alternative. Plane is a modern project management  | rss | <https://github.com/makeplane/plane> |
| **Kong/insomnia** — The open-source, cross-platform API client for GraphQL, REST, WebSockets, SSE and gRPC. With Cloud,  | rss | <https://github.com/Kong/insomnia> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | claudeai | ^11164 c435 | [New in Claude Code: Artifacts. Interactive pages built from your session, like a](https://x.com/claudeai/status/2067671912038240487) |
| x | PopBase | ^3162 c188 | [New music out tonight: • Tyla — Is It Love 🎵 • Chlöe, Timbaland — RESURRECTION (](https://x.com/PopBase/status/2067737279276450129) |
| x | bcherny | ^2440 c161 | [I've been using Artifacts in Claude Code for everything: visual explanations of ](https://x.com/bcherny/status/2067700226669060207) |
| x | ClaudeDevs | ^2407 c97 | [Artifacts are now live in Claude Code. Ask Claude to turn what it's working on i](https://x.com/ClaudeDevs/status/2067672094209675373) |
| x | elonmusk | ^2399 c153 | [@jietang @teortaxesTex On benchmarks, yes, but as measured by true usefulness ev](https://x.com/elonmusk/status/2067671903288864865) |
| x | niyetsel | ^1447 c25 | [Everyone who likes this tweet will have good luck this week. Aries: 150% Taurus:](https://x.com/niyetsel/status/2067674958172770707) |
| x | trq212 | ^1431 c98 | [Claude Code can now upload and edit HTML artifacts that you can share with your ](https://x.com/trq212/status/2067682475611242546) |
| x | tszzl | ^1182 c74 | [imo it is crazy that openai, years into the heated AGI race, released o1 and des](https://x.com/tszzl/status/2067760588315652123) |
| x | GuntherEagleman | ^1137 c50 | [🚨 BREAKING: Leaked audio from an internal Microsoft meeting reveals Judson Altho](https://x.com/GuntherEagleman/status/2067769516160135258) |
| x | testingcatalog | ^1130 c44 | [OPENAI 🔥: GPT-5.6 and GPT-5.6-Pro models may potentially arrive as soon as next ](https://x.com/testingcatalog/status/2067652120673739048) |
| x | polynoamial | ^1120 c28 | [When we announced @OpenAI o1 some researchers from other labs told me we made a ](https://x.com/polynoamial/status/2067651128855232663) |
| x | tszzl | ^1012 c73 | [I hate seeing what San Francisco does to people. they come here talking about “m](https://x.com/tszzl/status/2067691901126688993) |
| x | GreenIrisTarot | ^1002 c4 | [˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — summer spoilers 🍓 • a ](https://x.com/GreenIrisTarot/status/2067670885452951923) |
| x | Incognito_qfs | ^983 c10 | [Anthropic CEO Dario Amodei: "If you have ever been to one of these summits, (not](https://x.com/Incognito_qfs/status/2067696702061162526) |
| x | Polymarket | ^945 c81 | [JUST IN: White House &amp; Anthropic are reportedly now working on a framework t](https://x.com/Polymarket/status/2067728434101440816) |
| x | OneLuckyGirl_28 | ^899 c4 | [JUNE 19-28 Aries: Attract Money Taurus: Manifest Wealth Gemini: Big Glow Up Canc](https://x.com/OneLuckyGirl_28/status/2067654571627876478) |
| x | WestsideLAGuy | ^838 c51 | [Finance aura is real. A guy who works at Citadel has higher aura &amp; social st](https://x.com/WestsideLAGuy/status/2067679014970630235) |
| x | _catwu | ^771 c38 | [On Claude Team and Claude Enterprise, you can now use Claude Code to deploy HTML](https://x.com/_catwu/status/2067674836726694200) |
| x | AndrewCurran_ | ^728 c34 | [Anthropic has made a new proposal to Commerce Secretary Howard Lutnick pledging ](https://x.com/AndrewCurran_/status/2067680690779607232) |
| x | TrendSpider | ^728 c48 | [Microsoft owns 27% of OpenAI and is trading at its cheapest multiple in a decade](https://x.com/TrendSpider/status/2067722046142894142) |
| x | MatthewBerman | ^717 c33 | [OpenAI might swallow up every piece of software eventually.](https://x.com/MatthewBerman/status/2067684549010837797) |
| x | levelsio | ^712 c40 | [Holy shit America took stroopwafels and made them pre-workouts? https://t.co/buf](https://x.com/levelsio/status/2067730243817783595) |
| radar | leonidasrup | ^710 c590 | [Swiss parliament lifts ban on new nuclear power plants](https://www.bluewin.ch/en/news/switzerland/parliament-lifts-ban-on-new-nuclear-power-plants-3257535.html) |
| radar | theorchid | ^680 c159 | [I found 10k GitHub repositories distributing Trojan malware](https://orchidfiles.com/github-repositories-distributing-malware/) |
| x | hi_itsBlizzard | ^658 c8 | [remake of that lil animation test with teh new model :-3 https://t.co/ijjuLkhh3y](https://x.com/hi_itsBlizzard/status/2067756466631503997) |
| x | pankajkumar_dev | ^598 c19 | [GPT-5.6 Pro Early Reviews: Launch Looks Imminent - Frontend has improved, but it](https://x.com/pankajkumar_dev/status/2067675759075074138) |
| x | SophiaCai99 | ^595 c28 | [NEW: White House and Anthropic are working to create a formal technical assessme](https://x.com/SophiaCai99/status/2067696772840063370) |
| x | kimmonismus | ^593 c34 | [Elon Musk, who gives laudatory speeches on Anthropic, wasn't on my bingo card. h](https://x.com/kimmonismus/status/2067688880137007274) |
| x | buccocapital | ^589 c28 | [Guy today at work said something was “load-bearing” in a meeting I had to contro](https://x.com/buccocapital/status/2067735474483908624) |
| x | RichardMCNgo | ^588 c37 | [The AI safety community constructed a memeplex in which “taking AGI seriously” w](https://x.com/RichardMCNgo/status/2067689092985630737) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@claudeai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 11164 · 💬 435</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/claudeai/status/2067671912038240487">View @claudeai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New in Claude Code: Artifacts. Interactive pages built from your session, like a PR walkthrough or a living project dashboard, shared with your team at a private link. Available in beta on Team and En”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Code's new Artifacts feature (Team/Enterprise beta) generates interactive, shareable pages from a session — PR walkthroughs or live project dashboards served at a private URL.</dd>
      <dt>Why interesting</dt>
      <dd>The studio can surface PR reviews and sprint dashboards as a live shareable link instead of copy-pasting Claude session output into Notion or Slack.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run one PR review session in Claude Code and generate an Artifacts page to share with the team — evaluate if it replaces the current handoff format.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/claudeai/status/2067671912038240487" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PopBase</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3162 · 💬 188</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PopBase/status/2067737279276450129">View @PopBase on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New music out tonight: • Tyla — Is It Love 🎵 • Chlöe, Timbaland — RESURRECTION (Mixtape) 💿 • Tiffany Day &amp; Slayr — CONSTANTLY 🎵 • FKA Twigs, Lil Yachty — On Your Mind 🎵 • RIIZE — II 💿 • Elmiene, Fujii”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@PopBase lists ~30 new music releases dropping tonight, spanning pop, R&amp;B, and mixtapes from artists like Tyla, FKA Twigs, and Jon Batiste.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PopBase/status/2067737279276450129" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bcherny</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2440 · 💬 161</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bcherny/status/2067700226669060207">View @bcherny on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I've been using Artifacts in Claude Code for everything: visual explanations of tricky code, system diagrams, quick previews of a few animation options, data analyses and dashboards I share with the t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Code's Artifacts feature lets developers generate inline visual outputs — system diagrams, animation previews, and shareable data dashboards — directly inside a coding session.</dd>
      <dt>Why interesting</dt>
      <dd>Teams can produce and share architecture diagrams or data dashboards from Claude Code itself, cutting the need for separate diagramming or presentation tools.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can use Claude Code Artifacts to generate Unity or XR scene architecture diagrams during planning and share them with non-technical stakeholders directly.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bcherny/status/2067700226669060207" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ClaudeDevs</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2407 · 💬 97</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ClaudeDevs/status/2067672094209675373">View @ClaudeDevs on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Artifacts are now live in Claude Code. Ask Claude to turn what it's working on into a page and send the link to your team. The page updates as the session keeps working. Available today on Team and En”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Code now ships Artifacts — shareable pages generated from an active session that update live as Claude keeps working, available on Team and Enterprise plans starting today.</dd>
      <dt>Why interesting</dt>
      <dd>Teams can share a live, auto-updating link to session output with stakeholders or QA without writing separate status updates or taking screenshots.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can share an Artifacts link during active Claude Code sessions so clients or internal reviewers see live progress without waiting for a summary.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ClaudeDevs/status/2067672094209675373" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@elonmusk</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2399 · 💬 153</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/elonmusk/status/2067671903288864865">View @elonmusk on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@jietang @teortaxesTex On benchmarks, yes, but as measured by true usefulness even Q1 would be very impressive. Anthropic has rightly focused on maximizing useful intelligence, which does not show up ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Elon Musk stated that Anthropic's revenue growth reflects real-world usefulness of Claude that benchmark scores fail to capture, citing Q1 performance as genuinely impressive.</dd>
      <dt>Why interesting</dt>
      <dd>Confirms that benchmark scores are a poor proxy for production value — teams selecting AI tools should weight real task performance over leaderboard rankings.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When evaluating AI tools for studio projects, run task-specific tests on actual workflows instead of relying on public benchmark rankings.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/elonmusk/status/2067671903288864865" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@niyetsel</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1447 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/niyetsel/status/2067674958172770707">View @niyetsel on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Everyone who likes this tweet will have good luck this week. Aries: 150% Taurus: 120% Gemini: 200% Cancer: 10000% Leo: 300% Virgo: 90% Libra: 100% Scorpio: 180% Sagittarius: 140% Capricorn: 130% Aquar”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral X post promises zodiac-based 'good luck percentages' to users who like it — pure engagement bait with no informational content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/niyetsel/status/2067674958172770707" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@trq212</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1431 · 💬 98</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/trq212/status/2067682475611242546">View @trq212 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Claude Code can now upload and edit HTML artifacts that you can share with your team or other Claudes! Starting with teams so you can share internally with your team, coming to Pro and MAX plans soon!”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Claude Code now lets users upload and edit HTML artifacts that can be shared with teammates or other Claude instances — live on Teams plan, coming to Pro and MAX soon.</dd>
      <dt>Why interesting</dt>
      <dd>HTML artifact sharing in Claude Code means the studio can hand off visual outputs directly between team members and Claude agents inside the same tool.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Verify the studio's Claude Teams plan has the feature enabled, then pilot HTML artifact sharing for quick UI mockups or internal reports passed between team members.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/trq212/status/2067682475611242546" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@tszzl</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1182 · 💬 74</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/tszzl/status/2067760588315652123">View @tszzl on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“imo it is crazy that openai, years into the heated AGI race, released o1 and described in quite a bit of detail the principles of scaling RL over CoT. I wonder how much value was dispersed to the publ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Researcher @tszzl reflects that OpenAI voluntarily detailed RL-over-CoT scaling principles in o1's release, effectively gifting competitors and the public a significant technical roadmap.</dd>
      <dt>Why interesting</dt>
      <dd>Understanding why frontier labs publish technical details helps teams calibrate how much to trust public model papers vs. what remains proprietary.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/tszzl/status/2067760588315652123" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
