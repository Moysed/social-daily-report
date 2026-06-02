---
type: social-topic-report
date: '2026-06-02'
topic: ai-builders-watchlist
lang: en
pair: ai-builders-watchlist.th.md
generated_at: '2026-06-02T03:55:30+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.5
sentiment: mixed
confidence: 0.58
tags:
- ai-agents
- codex
- agent-memory
- llm-tooling
- generative-video
- indie-hackers
thumbnail: https://pbs.twimg.com/media/HJpy1sAa8AABRYW.jpg
---

# AI Builders Watchlist — 2026-06-02

## TL;DR
- Codex is the dominant thread: steipete uses it as a QA agent writing per-commit test scenarios via browser-use tooling [2], for ad-hoc TypeScript codemods [14], and voice-notifies when blocked [11]; rileybrown duplicates a Codex setup into a persistent cloud agent reachable over iMessage [20].
- Agent memory is the recurring cross-cutting idea — knowledge graph over vector store [31], a 'memory infra layer' [21], and 'we gave agents tools before memory' [36].
- vasuman flags Opus 4.8 as regressed: 'talks exactly like 4o, hallucinates very hard' [15]; rileybrown confirms it shipped last week [35].
- godofprompt reports frontier providers removed the temperature parameter (OpenAI o1/o3/GPT-5; Google warns against changing it on Gemini 3) [34].
- Generative media keeps getting cheaper: 0xROAS cites $0.004 per second of AI UGC video [40][42]; AmirMushich pushes one-prompt editable designs and brand mockups [19][37][49].

## What happened
Practitioner chatter this week centers on OpenAI Codex. steipete is building agentic dev workflows: a QA assistant that generates a user-test scenario per commit using webVNC/computer-and-browser-use tooling [2], ad-hoc codemods for a larger TypeScript migration [14], and audio notifications when the agent is blocked [11] — plus his modular agent OpenClaw, pitched as lean and 'only add what you need' [10][18][53]. rileybrown duplicates a Codex setup into a persistent cloud agent he talks to over iMessage [20], uses Codex Browser Use [17], and Paper inside Codex for thumbnail exploration [24]. Agent memory recurs as the perceived next bottleneck: knowledge graph vs vector DB [31], a 'memory infra layer' [21], and the framing that tools came before memory [36].

## Why it matters (reasoning)
The signal here is consolidation: independent operators are converging on Codex for agentic coding (QA, codemods, cloud persistence), which suggests a maturing pattern NDF DEV can copy rather than invent [2][14][20]. The repeated memory framing [21][31][36] points to where these workflows still break — agents that act but don't retain — relevant if NDF builds any persistent AI feature. The Opus 4.8 regression reports from a followed voice [15][35] are a single-source caution, not a verdict, but enough to test before upgrading. The temperature-removal note [34] matters concretely for any app code that tunes LLM sampling. Cheap generative video/image [40][37][19] lowers the cost of marketing and concept assets, though the figures are vendor-flavored claims, not benchmarked.

## Possibility
Likely: Codex-style agentic dev workflows keep maturing as more operators publish setups [2][14][20]. Plausible: knowledge-graph memory becomes a standard layer over naive vector stores [21][31][36]. Plausible: per-second AI video pricing keeps falling and competitors match it, as 0xROAS predicts [40]. Unlikely to confirm from this feed: the Opus 4.8 'regression' [15] — it is one practitioner's impression and needs your own evals before acting. No source states numeric probabilities; treat the dollar and session figures [40][44] as claimed, not verified.

## Org applicability — NDF DEV
1) Trial Codex as a QA/test-scenario generator and for codemods in TS-heavy refactors across web/mobile — med effort [2][14]. 2) If building any AI feature with memory, evaluate a knowledge-graph memory layer over a plain vector store — med [31][21][36]. 3) Pilot one-prompt image/video generation for game promo and marketing assets, but validate the cost and quality claims yourself before committing — low/med [40][37][19]. 4) If Claude is in your stack, benchmark Opus 4.8 against your current model before upgrading; watch for the reported hallucination/voice regression — low [15][35]. 5) Audit any LLM calls that set temperature; frontier reasoning models are dropping the parameter — low [34]. Skip: lifestyle/motivation posts [5][12][27][46], YouTube-shorts spam tactics [16][30][60], CPA/affiliate funnels [25], prompt-pack marketing [28][57], and CEO-as-app-icon branding takes [4] — no actionable signal for NDF.

## Signals to Watch
- Opus 4.8 regression reports from a followed voice — verify with your own evals [15][35].
- Temperature parameter removed across frontier providers; check it against your app code [34].
- Agent memory as a knowledge-graph layer, not vector DB [21][31][36].
- Codex cloud-agent + messaging persistence pattern (iMessage, voice-when-blocked) [20][11].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | EXM7777 | ^2399 c41 | [this is the Hermes setup top 1% operators are using to get rid of AI slop... htt](https://x.com/EXM7777/status/2061086049326256356) |
| x | steipete | ^1582 c70 | [Been teaching codex to be my QA assistant. For every commit it creates a user-te](https://x.com/steipete/status/2061208638027395490) |
| x | vasuman | ^1034 c145 | [/goal has been running for 16 hours and we're in that sweet spot where I don't w](https://x.com/vasuman/status/2061203646449369497) |
| x | egeberkina | ^946 c44 | [CEOs are the new app icons https://t.co/W3jjrU027b](https://x.com/egeberkina/status/2061137275426165022) |
| x | marclou | ^928 c127 | [What I wanted at 20: - A fancy car - A lot of friends - A high-paid job - A craz](https://x.com/marclou/status/2061467056407708156) |
| x | gregisenberg | ^853 c121 | [Funny how the pendulum shifts 1. "GPT wrappers are worthless" → the value acrues](https://x.com/gregisenberg/status/2061484999153488082) |
| x | EXM7777 | ^573 c11 | [Matt has been shipping some incredible products lately... you should definitely ](https://x.com/EXM7777/status/2061301916324577401) |
| x | jackfriks | ^572 c62 | [years of nothing, and then everything all at once](https://x.com/jackfriks/status/2061442785253732851) |
| x | vasuman | ^537 c9 | [Incredible https://t.co/QqVOtcj5iN](https://x.com/vasuman/status/2061261104962244981) |
| x | steipete | ^471 c53 | [The idea of OpenClaw is always that it should be yours. It's modular and lean, o](https://x.com/steipete/status/2061072753998856696) |
| x | steipete | ^454 c31 | [I told codex to use https://t.co/oHS8ombQcW whenever I'm distracted and it needs](https://x.com/steipete/status/2061574752574283858) |
| x | jackfriks | ^425 c24 | [the best things this world has to offer cannot be bought. https://t.co/OqxMMk50d](https://x.com/jackfriks/status/2061480957522145750) |
| x | egeberkina | ^402 c2 | [Meet me on the green --sref 3662540287 568834969 --v 8.1 https://t.co/RIgGTHrlYx](https://x.com/egeberkina/status/2061465064243167678) |
| x | steipete | ^343 c33 | [Haven't seen codex writing ad-hoc codemods before, but it just did for a bigger ](https://x.com/steipete/status/2061115471760441692) |
| x | vasuman | ^306 c51 | [Something went very wrong in making Opus 4.8. Talks exactly like 4o. Hallucinate](https://x.com/vasuman/status/2061301288256823409) |
| x | eptwts | ^262 c17 | [there was a point in time where 99% of my traffic came from posting 5k youtube s](https://x.com/eptwts/status/2061454644115562533) |
| x | rileybrown | ^208 c13 | [Good morning everyone... I feel like it's going to be an awesome week. (Sent fro](https://x.com/rileybrown/status/2061464989307736118) |
| x | steipete | ^152 c8 | [@shashankgoyal95 @OpenRouter Integration with OpenClaw onboarding for a better s](https://x.com/steipete/status/2061182935957401658) |
| x | AmirMushich | ^142 c6 | [now you can create editable designs with 1 prompt save the tool 👇 https://t.co/f](https://x.com/AmirMushich/status/2061121201146060838) |
| x | rileybrown | ^140 c12 | [This prompt allows me to duplicate my codex setup to a persistent cloud agent th](https://x.com/rileybrown/status/2061452146864689545) |
| x | vasuman | ^139 c6 | [Memory infra layer for agents, massive unlock](https://x.com/vasuman/status/2061466097623376006) |
| x | levelsio | ^135 c48 | [@mitsuhiko I switched from 1Password to Bitwarden and it's so buggy more than ha](https://x.com/levelsio/status/2061517012271087725) |
| x | eptwts | ^132 c6 | [a beginner focusing on "building" instead of learning how to sell is incredibly ](https://x.com/eptwts/status/2061484103011061906) |
| x | rileybrown | ^131 c11 | [Wow Paper inside Codex is pretty wild. Especially with my youtube thumbnail skil](https://x.com/rileybrown/status/2061634840999448629) |
| x | 0xROAS | ^119 c9 | [say hello to $250 CPA](https://x.com/0xROAS/status/2061472119263772938) |
| x | rileybrown | ^115 c62 | [bro wispr flow went down for me... i'm so cooked lol i hate typing.](https://x.com/rileybrown/status/2061474913165148194) |
| x | jackfriks | ^114 c25 | [you are either mad at the world, or madly in love with the world pick your path.](https://x.com/jackfriks/status/2061427955427946844) |
| x | AmirMushich | ^100 c12 | [4807 folks to grab these prompts 👇 Just saw this reel on instagram: Mariah share](https://x.com/AmirMushich/status/2061360924233966022) |
| x | marclou | ^99 c25 | [✅ Startup Acquisition #96 on @trust_mrr ✅ $1.6K MRR voice-to-text startup sold f](https://x.com/marclou/status/2061428304826225077) |
| x | jackfriks | ^85 c6 | [kinda insane how you can get a youtube plaque by automating a YT channel using @](https://x.com/jackfriks/status/2061535413823504764) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2399 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2061086049326256356">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“this is the Hermes setup top 1% operators are using to get rid of AI slop... https://t.co/gbRRSx3sbM”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A tweet teases a vague 'Hermes setup' claimed to reduce low-quality AI output, with no description of what it is — just a link and hype framing.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EXM7777/status/2061086049326256356" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1582 · 💬 70</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061208638027395490">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Been teaching codex to be my QA assistant. For every commit it creates a user-test scenario and uses webVNC (crabbox), computer/browser use (peekaboo/mcporter) to test OpenClaw like a user/QA person w”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@steipete wired Codex to generate a user-test scenario on every commit, execute it via webVNC + browser-use tools against his app, and open PRs with fixes — all running unattended in the background.</dd>
      <dt>Why interesting</dt>
      <dd>A concrete agentic QA loop that runs on every commit with no QA headcount — directly applicable to any web or mobile project the studio ships continuously.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Pilot this on one web project: hook Codex to generate a test scenario per PR, run it via Playwright or a browser-use MCP, and auto-open fix PRs on failure.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061208638027395490" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vasuman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1034 · 💬 145</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vasuman/status/2061203646449369497">View @vasuman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“/goal has been running for 16 hours and we're in that sweet spot where I don't want to stop it because it could be cooking but I also seriously doubt it. Please advise”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer @vasuman has an AI agent task (/goal) 16 hours in with no clear progress signal — stuck at the classic stop-or-continue dilemma with no data to decide.</dd>
      <dt>Why interesting</dt>
      <dd>Long-running agentic tasks have no built-in observability — without checkpoints, teams burn compute on stuck work with no way to distinguish progress from spin.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Define explicit timeout budgets and mid-run checkpoint prompts for any long-running agent tasks the studio runs, so the kill decision is policy-driven, not intuition.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vasuman/status/2061203646449369497" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@egeberkina</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 946 · 💬 44</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/egeberkina/status/2061137275426165022">View @egeberkina on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“CEOs are the new app icons https://t.co/W3jjrU027b”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The post states 'CEOs are the new app icons' with no further context, data, or linked content beyond a dead/unresolved URL.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/egeberkina/status/2061137275426165022" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 928 · 💬 127</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2061467056407708156">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“What I wanted at 20: - A fancy car - A lot of friends - A high-paid job - A crazy social life - A lot of validation What I want at 30: - A fit body - A best friend - A peaceful mind - A meaningful wor”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Marc Lou shares a personal list contrasting his material and social ambitions at 20 with health, focus, and simplicity priorities at 30.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2061467056407708156" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 853 · 💬 121</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2061484999153488082">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Funny how the pendulum shifts 1. &quot;GPT wrappers are worthless&quot; → the value acrues to application layer 2. &quot;AI will eliminate white collar jobs&quot; → someone needs to manage all these AI agents and everyon”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Greg Isenberg catalogues 8 AI narrative reversals: model loyalty is dead (swap weekly by task), open-source covers 80% of tasks, workflow engineering replaced prompt engineering, and computer use is now production-ready.</dd>
      <dt>Why interesting</dt>
      <dd>The 'swap models weekly by task' and 'workflow engineering over prompt engineering' points directly apply to how a small studio should structure its AI tooling stack.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Assign specific models by task category (coding, docs, browser automation, design) across the studio's projects instead of standardizing on one provider.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2061484999153488082" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 573 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2061301916324577401">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Matt has been shipping some incredible products lately... you should definitely equip your agents with: - /last30days - PrintingPress - Agent Cookie completely different experience with Hermes especia”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Anonymous account recommends three unnamed tools — /last30days, PrintingPress, Agent Cookie — attributed to an unidentified 'Matt', claiming they improve experience with the Hermes model.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EXM7777/status/2061301916324577401" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jackfriks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 572 · 💬 62</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jackfriks/status/2061442785253732851">View @jackfriks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“years of nothing, and then everything all at once”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@jackfriks posted a one-line sentiment — 'years of nothing, and then everything all at once' — with no named tool, release, or event attached.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jackfriks/status/2061442785253732851" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
