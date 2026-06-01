---
type: social-topic-report
date: '2026-06-01'
topic: ai-builders-watchlist
lang: en
pair: ai-builders-watchlist.th.md
generated_at: '2026-06-01T04:32:18+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.45
sentiment: positive
confidence: 0.55
tags:
- agentic-dev
- ai-qa
- prompt-engineering
- ai-video
- realtime-voice
- indie-builders
thumbnail: https://pbs.twimg.com/media/HJpy1sAa8AABRYW.jpg
---

# AI Builders Watchlist — 2026-06-01

## TL;DR
- steipete is shipping an agent framework called OpenClaw — modular/lean, 'only add what you need,' with OpenRouter integration in onboarding [7][17], and is moving to SF for MS Build [1].
- Practical agentic-dev workflow: steipete has Codex acting as an autonomous QA assistant that writes per-commit user-test scenarios and drives browser/computer-use tools (crabbox/peekaboo/mcporter) to test like a user [4], plus ad-hoc TypeScript codemods [11]; 'autoreview keeps GPT honest' [15].
- godofprompt claims temperature tuning is being removed on reasoning models — OpenAI dropped it on o1/o3/GPT-5 and Google warned against changing it on Gemini 3 [38].
- AI video crossed a usability line for these creators: 0xROAS clones a video in ~15 min with 'V3 AI UGC' [32][36], plus Grok Imagine Video 1.5 [21] and Gemini Omni Flash vs Seedance 2.0 comparisons [27][40].
- gregisenberg frames GPT Realtime 2.0 as enabling real-time, on-call voice agents (e.g. live contract negotiation) [3]; vasuman pitches a forward-deployed custom-agent consulting model [9].

## What happened
This week's curated builder feed centers on agentic development tooling. steipete is publicly building OpenClaw, an agent framework pitched as modular and lean — 'fewer skills, fewer tools = your agent can work more efficiently' [7] — with a proposed OpenRouter onboarding integration [17]. He details using Codex as a QA agent that generates a user-test scenario per commit and exercises the app through web/VNC and browser/computer-use tooling [4], writes ad-hoc codemods for a TypeScript migration [11], and relies on an 'autoreview' step to constrain model output [15]. Surrounding personal items (SF move, MS Build) are context, not signal [1].

## Why it matters (reasoning)
On prompting practice, godofprompt reports providers are removing the temperature knob on reasoning models (o1/o3/GPT-5) and discouraging it on Gemini 3 [38]; if accurate, that changes how teams should tune model behavior. gregisenberg and vasuman point at productized agents: real-time voice agents that sit on live calls [3] and forward-deployed custom agent builds [9]. On media, multiple creators report AI video clfor is now fast enough for production UGC [21][32][36][27]. The throughline is operational, not theoretical: these people are running agents in real build/test/QA loops [4][11][13], not just demoing them.

## Possibility
Likely: agent-driven QA/codemod workflows (commit-triggered test generation + browser/computer-use execution) keep maturing and become a normal part of dev pipelines, given steipete is already running them daily [4][11]. Plausible: the 'temperature is dead' shift forces prompt/config changes if you depend on temperature for determinism or creativity — verify against official docs before acting, since this is one practitioner's framing [38]. Plausible: real-time voice agents move from concept to shipped products as GPT Realtime 2.0 matures [3]. Unlikely (near-term): OpenClaw becomes a standard you must adopt — it is one person's early, opinionated framework [7]; treat as a pattern source, not a dependency.

## Org applicability — NDF DEV
1) Pilot an agent-as-QA loop for web/mobile: have Codex/Claude generate per-commit test scenarios and drive a browser-use tool against staging — directly applicable to NDF DEV's web & mobile apps (effort med) [4][15]. 2) Audit prompt/config code for hardcoded temperature on reasoning models and confirm provider behavior before relying on it (effort low) [38]. 3) Test GPT Realtime 2.0 for an e-learning/edutech voice use case (e.g. spoken-language practice or tutoring) as a scoped spike (effort med) [3]. 4) Trial one AI-video tool (Omni Flash / Grok 1.5 / a UGC cloner) for marketing/short-form content and compare against editing by hand (effort low) [27][32]; note rileybrown is going the opposite way and hiring human editors who understand AI tools [23][42] — quality still needs a human in the loop. 5) Try a prompt-to-editable-design agent for fast UI mockups (effort low) [20][52]. Skip: the SF/MS Build logistics [1], creatine and lifestyle posts [5][58], and MRR/revenue flexing [22][33] — no actionable content.

## Signals to Watch
- OpenClaw direction and OpenRouter onboarding integration — a template for lean, self-hosted agent setups [7][17].
- Codex doing real codemods and computer-use QA, including self-recovery ('call crabbox doctor if a screenshot fails') [4][11][59].
- Provider removal of temperature controls on reasoning models — confirm against OpenAI/Google docs [38].
- AI-video UGC cloning speed (~15 min) vs the counter-move of hiring human editors [32][23].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | steipete | ^2108 c117 | [Finally got my visa sorted out and moving to San Francisco, just in time for MS ](https://x.com/steipete/status/2061031509088231640) |
| x | EXM7777 | ^1465 c25 | [this is the Hermes setup top 1% operators are using to get rid of AI slop... htt](https://x.com/EXM7777/status/2061086049326256356) |
| x | gregisenberg | ^847 c58 | [GPT Realtime 2.0 is pretty incredible 17 startup ideas that ONLY work because of](https://x.com/gregisenberg/status/2061129813750915508) |
| x | steipete | ^784 c34 | [Been teaching codex to be my QA assistant. For every commit it creates a user-te](https://x.com/steipete/status/2061208638027395490) |
| x | levelsio | ^571 c53 | [Take your creatine!!! https://t.co/TyTIqEUFUq](https://x.com/levelsio/status/2061176892691017909) |
| x | gregisenberg | ^442 c60 | [I can't believe how fun building a company is right now is. The weird part is it](https://x.com/gregisenberg/status/2061241159213576367) |
| x | steipete | ^414 c47 | [The idea of OpenClaw is always that it should be yours. It's modular and lean, o](https://x.com/steipete/status/2061072753998856696) |
| x | marclou | ^367 c59 | [These have been the best 10 years of my life. Entrepreneurship has taught me so ](https://x.com/marclou/status/2061104163745075339) |
| x | vasuman | ^346 c46 | [Imagine an AI company that forward deploys into your enterprise to first underst](https://x.com/vasuman/status/2060847258283999376) |
| x | vasuman | ^338 c49 | [If you're a software engineer that is down for a paid work trial (1-2 weeks, con](https://x.com/vasuman/status/2060866035067343240) |
| x | steipete | ^277 c32 | [Haven't seen codex writing ad-hoc codemods before, but it just did for a bigger ](https://x.com/steipete/status/2061115471760441692) |
| x | levelsio | ^267 c27 | [Please report this guy thx @nikitabier](https://x.com/levelsio/status/2061162603586445505) |
| x | vasuman | ^224 c53 | [/goal has been running for 16 hours and we're in that sweet spot where I don't w](https://x.com/vasuman/status/2061203646449369497) |
| x | steipete | ^152 c3 | [@theo Yes! See ya around this week?](https://x.com/steipete/status/2061038721290400240) |
| x | steipete | ^151 c6 | [@theo @VictorTaelin gotta use autoreview, that keeps gpt honest and usually help](https://x.com/steipete/status/2061036923397845456) |
| x | egeberkina | ^141 c4 | [CEOs are the new app icons https://t.co/W3jjrU027b](https://x.com/egeberkina/status/2061137275426165022) |
| x | steipete | ^133 c7 | [@shashankgoyal95 @OpenRouter Integration with OpenClaw onboarding for a better s](https://x.com/steipete/status/2061182935957401658) |
| x | egeberkina | ^104 c0 | [@tervisscoot Average concert in Turkey https://t.co/tExymyP6Ab](https://x.com/egeberkina/status/2060830061381431780) |
| x | vasuman | ^104 c1 | [Incredible https://t.co/QqVOtcj5iN](https://x.com/vasuman/status/2061261104962244981) |
| x | AmirMushich | ^102 c5 | [now you can create editable designs with 1 prompt save the tool 👇 https://t.co/f](https://x.com/AmirMushich/status/2061121201146060838) |
| x | 0xROAS | ^101 c8 | [here's how Grok Imagine Video 1.5 looks like: https://t.co/7aB3qNCv91](https://x.com/0xROAS/status/2061139518795735271) |
| x | jackfriks | ^98 c15 | [it’s been almost a year since i learned what a database index is also almost a y](https://x.com/jackfriks/status/2061275203607372178) |
| x | rileybrown | ^87 c13 | [I'm going in the opposite direction. I'm hiring HUMAN video editors in New York ](https://x.com/rileybrown/status/2061215449858072994) |
| x | gregisenberg | ^72 c12 | [@RaminNasibov CS 1.6](https://x.com/gregisenberg/status/2061148444765372745) |
| x | gregisenberg | ^69 c3 | [@OrevaZSN honestly, not a bad idea adding it to https://t.co/ptcEtGCCsV](https://x.com/gregisenberg/status/2061227827299561934) |
| x | godofprompt | ^68 c10 | [I pulled a full week of @OpenAI's X analytics without an API key, a scraper, or ](https://x.com/godofprompt/status/2060808562314772519) |
| x | egeberkina | ^67 c3 | [Tonight Turkey at Ye's concert 🇹🇷 Made with Omni Flash https://t.co/iHEwBZ5zlP](https://x.com/egeberkina/status/2060828495521976754) |
| x | steipete | ^65 c8 | [@_lopopolo *need*](https://x.com/steipete/status/2061036484975559132) |
| x | steipete | ^64 c2 | [@dasPoppers @openclaw Did we had the same idea yesterday? Didn’t see your propos](https://x.com/steipete/status/2060974727213027435) |
| x | AmirMushich | ^44 c6 | [Ferrari Luce brand vision* *2026 trends https://t.co/iU5A8LYCnC](https://x.com/AmirMushich/status/2061175478061285576) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2108 · 💬 117</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061031509088231640">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Finally got my visa sorted out and moving to San Francisco, just in time for MS Build and OpenClaw’s after hours! https://t.co/agbyZ79kb1”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer @steipete announces a personal relocation to San Francisco, timed with MS Build and an after-hours event called 'OpenClaw'.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061031509088231640" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1465 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2061086049326256356">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“this is the Hermes setup top 1% operators are using to get rid of AI slop... https://t.co/gbRRSx3sbM”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A tweet teases a 'Hermes setup' for reducing low-quality AI output, with no details in the post — only a linked URL.</dd>
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
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 847 · 💬 58</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2061129813750915508">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“GPT Realtime 2.0 is pretty incredible 17 startup ideas that ONLY work because of what this model makes possible: 1. Real-time contract negotiation agent. Sits on a call between two parties, checks pri”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Greg Isenberg lists 17 startup concepts that require GPT Realtime 2.0's ability to run parallel tool calls (databases, inventory, market data) while a voice conversation is still in progress.</dd>
      <dt>Why interesting</dt>
      <dd>Parallel tool execution during live speech is a new primitive: a voice agent can query five data sources simultaneously without pausing the conversation, enabling a class of always-on voice agents that streaming TTS alone cannot deliver.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's e-learning work is a direct test case: build a small GPT Realtime 2.0 prototype where a voice tutor pulls learner progress and quiz content in parallel during a live session.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2061129813750915508" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 784 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061208638027395490">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Been teaching codex to be my QA assistant. For every commit it creates a user-test scenario and uses webVNC (crabbox), computer/browser use (peekaboo/mcporter) to test OpenClaw like a user/QA person w”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@steipete trained Codex to auto-generate a user-test scenario per commit, execute it via webVNC and browser computer-use against their app, then open fix PRs — all running in the background.</dd>
      <dt>Why interesting</dt>
      <dd>Combines per-commit test generation with computer-use execution into a hands-off QA loop — small teams get continuous regression testing without a dedicated QA person.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Wire a Codex or Claude agent into the studio's CI pipeline to generate and run browser-use test scenarios on each web or e-learning commit, then auto-open fix PRs.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061208638027395490" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 571 · 💬 53</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2061176892691017909">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Take your creatine!!! https://t.co/TyTIqEUFUq”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@levelsio posted 'Take your creatine!!!' with an external link — no technical content, no product, no release.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2061176892691017909" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 442 · 💬 60</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2061241159213576367">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I can't believe how fun building a company is right now is. The weird part is it doesn't feel like work anymore. New AI models/tools/repos keep coming out making the impossible possible. My ONLY anxie”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Greg Isenberg, a startup builder and investor, posts that the current AI moment feels like the early mobile app era — a short window before distribution gets hard, and he is treating it with urgency.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2061241159213576367" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 414 · 💬 47</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061072753998856696">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The idea of OpenClaw is always that it should be yours. It's modular and lean, only add what you need. Fewer skills, fewer tools = your agent can work more efficiently.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@steipete describes OpenClaw as a modular, opt-in agent framework where fewer tools and skills produce a more focused, efficient agent — bloat is by design avoidable.</dd>
      <dt>Why interesting</dt>
      <dd>Teams building internal AI agents often over-provision tools; this trim-first design principle directly improves reasoning quality and reduces token waste.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Before deploying any internal agent, audit its tool and skill list and remove anything not actively required for the target workflow.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061072753998856696" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 367 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2061104163745075339">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“These have been the best 10 years of my life. Entrepreneurship has taught me so much that it's hard to believe the person I am today is the same person who started 10 years ago. Most of those years we”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Founder @marclou reflects on 10 years of entrepreneurship, calling the journey itself the reward despite years of uncertainty and setbacks.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2061104163745075339" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
