---
type: social-topic-report
date: '2026-05-31'
topic: ai-builders-watchlist
lang: en
pair: ai-builders-watchlist.th.md
generated_at: '2026-05-31T16:31:18+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.35
sentiment: mixed
confidence: 0.55
tags:
- indie-hackers
- ai-agents
- codex
- video-gen
- devtools
- openclaw
thumbnail: https://pbs.twimg.com/media/HJo95BoXIAsVniK.jpg
---

# AI Builders Watchlist — 2026-05-31

## TL;DR
- Indie revenue posts dominate this week: marclou reported $87,507 for May 2026 [2], jackfriks $59,347 [4]; their joint venture Ship or Die is split 50/50 and made ~$40K total [31][34].
- steipete is moving to San Francisco for MS Build and is actively developing OpenClaw, a modular/lean personal agent framework ("only add what you need") [1][11].
- Practical coding-agent signal: steipete reports Codex writing ad-hoc codemods for a larger TypeScript migration, and using 'autoreview' plus an agents.md spec to keep the model honest on edge cases [21][17][23].
- Video-gen comparison is a live thread among these voices: Seedance 2.0 vs Gemini Omni Flash, with one arguing Omni's edge is non-quality (distribution/access), not raw output [24][25][40][41].
- marclou's TrustMRR verifies startup metrics (MRR, churn, visitors) from Stripe/GSC/GA, and levelsio cautions that viral '$1M ARR in a month' claims are mostly pumped [18][10].

## What happened
This is a personalities feed, not a news feed. The bulk of high-engagement items are monthly indie-hacker revenue reports: marclou $87,507 across a portfolio (TrustMRR $27K, DataFast $20K, Ship or Die $20K, CodeFast $8K, ShipFast $7K) [2], jackfriks $59,347 [4], and levelsio noting a project at $16K MRR after 4 months [3]. marclou and jackfriks confirm Ship or Die is a 50/50 joint venture, so each reports half of ~$40K total [31][34]. marclou's TrustMRR claims verification of MRR/churn/visitors from Stripe, Google Search Console, and Google Analytics [18], and levelsio warns publicly that '$1M ARR in a month' growth stories are largely fabricated or pumped [10]. Separately, steipete announced a move to San Francisco for MS Build and continued work on OpenClaw, framed as a modular, minimal personal agent [1][11].

## Why it matters (reasoning)
The most useful cross-cutting signal is operational, not financial: steipete's notes on Codex generating codemods for a TypeScript migration [21], using 'autoreview' to keep the model honest [17], and encoding edge-case depth in an agents.md spec [23] are concrete patterns for agent-assisted refactoring that NDF DEV's web/mobile teams can copy directly. The OpenClaw 'fewer skills, fewer tools = more efficient agent' thesis [11] aligns with practical context-management concerns. The revenue posts are mostly noise for our purposes — they signal that the solo-SaaS/marketing-app niche these builders occupy is healthy, but the numbers are self-reported and portfolio-specific [2][4], and levelsio himself flags how much of this genre is inflated [10]. The one strategic data point worth noting is the 'nobody wants the eighth-best product' framing behind AI valuations like Anthropic's $1T [32]: in AI tooling, market position concentrates, which matters when picking which model/devtool vendors to standardize on.

## Possibility
Likely: agent-assisted codemods and review loops (Codex/autoreview/agents.md) become standard practice for migrations among these practitioners, because steipete reports them already working in production-scale TS work [21][23]. Plausible: video-gen tooling (Seedance 2.0, Gemini Omni Flash) keeps churning with no settled winner near-term — the debate is framed around distribution vs raw quality rather than a decisive lead [41]. Plausible: OpenClaw matures into a usable open personal-agent stack, but it is early and tied to one author's momentum [1][11]. Unlikely to matter operationally: the monthly MRR theater continues but yields little transferable insight [2][4].

## Org applicability — NDF DEV
1) Trial Codex (or equivalent) for a contained TypeScript/Unity-tooling codemod and adopt an agents.md-style spec to bound edge-case behavior — low effort, high transfer [21][23]. 2) Add an 'autoreview' pass (model reviews its own diff before human review) to one repo's agent workflow and measure whether it reduces review churn — low effort [17]. 3) Evaluate Seedance 2.0 vs Gemini Omni Flash for marketing/promo clips for game or edutech launches, judging on access/cost not just output quality — med effort [25][40][41]. 4) Watch OpenClaw as a reference for lean, modular agent design before adding more tools to internal agents — low effort [11]. Skip: the MRR reports [2][4][3] and the off-topic personal posts [9][15][19][25-personal] — no action. Do not treat self-reported revenue as market sizing [10].

## Signals to Watch
- OpenClaw's modular/minimal agent direction and SF momentum around steipete [1][11].
- Codex codemods + autoreview + agents.md as a repeatable migration pattern [21][17][23].
- Seedance 2.0 vs Gemini Omni Flash — distribution-vs-quality framing for video gen [40][41].
- TrustMRR's verified-metrics model and levelsio's pushback on inflated growth claims [18][10].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | steipete | ^1239 c74 | [Finally got my visa sorted out and moving to San Francisco, just in time for MS ](https://x.com/steipete/status/2061031509088231640) |
| x | marclou | ^736 c106 | [I made $87,507 in May 2026. ⭐️ TrustMRR — $27K 📈 DataFast — $20K 🏴‍☠️ Ship or Di](https://x.com/marclou/status/2061065911394836861) |
| x | levelsio | ^657 c50 | [Update after 4 months he's at $16K MRR https://t.co/1MpJWnyP9N](https://x.com/levelsio/status/2061027867274674194) |
| x | jackfriks | ^575 c83 | [i made $59,347 in may 2026 ... ($81,919 CAD) 🌉 post bridge — $36K 🏴‍☠️ ship or d](https://x.com/jackfriks/status/2061072407608066353) |
| x | EXM7777 | ^494 c17 | [https://t.co/ip0CFHxG7R](https://x.com/EXM7777/status/2060736517564477901) |
| x | levelsio | ^408 c43 | [https://t.co/yHVz4TUlse](https://x.com/levelsio/status/2060836472958165167) |
| x | vasuman | ^329 c45 | [Imagine an AI company that forward deploys into your enterprise to first underst](https://x.com/vasuman/status/2060847258283999376) |
| x | vasuman | ^320 c46 | [If you're a software engineer that is down for a paid work trial (1-2 weeks, con](https://x.com/vasuman/status/2060866035067343240) |
| x | jackfriks | ^258 c30 | [wife appreciation post (she made me banana bread today) https://t.co/I5ZycalO7d](https://x.com/jackfriks/status/2060871445622796739) |
| x | levelsio | ^245 c17 | [P.S. this is how actual realistc growth looks like You see all these ecom bros n](https://x.com/levelsio/status/2061036511202603374) |
| x | steipete | ^219 c33 | [The idea of OpenClaw is always that it should be yours. It's modular and lean, o](https://x.com/steipete/status/2061072753998856696) |
| x | EXM7777 | ^176 c7 | [this is the Hermes setup top 1% operators are using to get rid of AI slop... htt](https://x.com/EXM7777/status/2061086049326256356) |
| x | marclou | ^155 c34 | [These have been the best 10 years of my life. Entrepreneurship has taught me so ](https://x.com/marclou/status/2061104163745075339) |
| x | rileybrown | ^133 c7 | [What mean? https://t.co/CODJszlnCY](https://x.com/rileybrown/status/2060908536549261320) |
| x | jackfriks | ^109 c18 | [does this look like i'm trolling? this brand new toyota corolla will last longer](https://x.com/jackfriks/status/2061089156374114449) |
| x | steipete | ^104 c2 | [@theo Yes! See ya around this week?](https://x.com/steipete/status/2061038721290400240) |
| x | steipete | ^99 c2 | [@theo @VictorTaelin gotta use autoreview, that keeps gpt honest and usually help](https://x.com/steipete/status/2061036923397845456) |
| x | marclou | ^95 c33 | [Heads up! TrustMRR doesn't just show startup MRR, but also: 📉 Churn 📈 Visitors 👀](https://x.com/marclou/status/2061021034631852295) |
| x | egeberkina | ^93 c0 | [@tervisscoot Average concert in Turkey https://t.co/tExymyP6Ab](https://x.com/egeberkina/status/2060830061381431780) |
| x | rileybrown | ^86 c8 | [@vansh22b Shut up](https://x.com/rileybrown/status/2060910981484622132) |
| x | steipete | ^81 c13 | [Haven't seen codex writing ad-hoc codemods before, but it just did for a bigger ](https://x.com/steipete/status/2061115471760441692) |
| x | steipete | ^68 c8 | [@iruletheworldmo very much depends on the skillset of the person driving the AI.](https://x.com/steipete/status/2060749955707351156) |
| x | steipete | ^67 c3 | [@segolovach parent codex is pretty good at rejecting review comments. You need t](https://x.com/steipete/status/2060794664521781466) |
| x | AmirMushich | ^66 c14 | [GPT-2 x Seedance 2.0 animated logo mockup smart workflow + prompts 👇 Get more de](https://x.com/AmirMushich/status/2060775801121816995) |
| x | egeberkina | ^64 c3 | [Tonight Turkey at Ye's concert 🇹🇷 Made with Omni Flash https://t.co/iHEwBZ5zlP](https://x.com/egeberkina/status/2060828495521976754) |
| x | godofprompt | ^59 c10 | [I pulled a full week of @OpenAI's X analytics without an API key, a scraper, or ](https://x.com/godofprompt/status/2060808562314772519) |
| x | egeberkina | ^56 c0 | [Off-White™ presents: impossible places https://t.co/Bvy2jIR8BD](https://x.com/egeberkina/status/2060705806891249691) |
| x | steipete | ^55 c1 | [@artee_49 charge more for your work](https://x.com/steipete/status/2060702497396650316) |
| x | steipete | ^52 c1 | [@dasPoppers @openclaw Did we had the same idea yesterday? Didn’t see your propos](https://x.com/steipete/status/2060974727213027435) |
| x | steipete | ^51 c5 | [@macmatan private one, a few work work. Difference is mostly permissions.](https://x.com/steipete/status/2060750352127770860) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1239 · 💬 74</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061031509088231640">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Finally got my visa sorted out and moving to San Francisco, just in time for MS Build and OpenClaw’s after hours! https://t.co/agbyZ79kb1”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@steipete (Peter Steinberger, PSPDFKit founder) announced he got his US visa and is relocating to San Francisco, timing the move with MS Build and an OpenAI after-hours event.</dd>
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
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 736 · 💬 106</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2061065911394836861">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I made $87,507 in May 2026. ⭐️ TrustMRR — $27K 📈 DataFast — $20K 🏴‍☠️ Ship or Die — $20K 🧑‍💻 CodeFast — $8K ⚡️ ShipFast — $7K 🐥 Twitter — $3.2K 🦐 SuperShrimp — $1K 🍜 Indie Page — $715 🛡️ ByeDispute — ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Marc Lou publicly reported $87,507 in May 2026 MRR spread across 13 products, with TrustMRR ($27K), DataFast ($20K), and Ship or Die ($20K) as the top earners.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2061065911394836861" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 657 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2061027867274674194">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Update after 4 months he's at $16K MRR https://t.co/1MpJWnyP9N”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@levelsio shared a revenue update for an unnamed builder who reached $16K MRR four months after launch, with no product, stack, or method details in the post.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2061027867274674194" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jackfriks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 575 · 💬 83</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jackfriks/status/2061072407608066353">View @jackfriks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“i made $59,347 in may 2026 ... ($81,919 CAD) 🌉 post bridge — $36K 🏴‍☠️ ship or die — $20K 🐷 lovelee couples — $3K 📔 year pix — $45 this has become an insanely stupid amount of money to me and doesn't ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Indie maker @jackfriks reports $59,347 USD in May 2026 revenue split across four self-built products: Post Bridge ($36K), Ship or Die ($20K), Lovelee Couples ($3K), and Year Pix ($45).</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jackfriks/status/2061072407608066353" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 494 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2060736517564477901">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/ip0CFHxG7R”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The post is a bare link to an X Premium article (HTTP 402 paywall) with no caption, headline, or context provided — content is inaccessible without a subscription.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EXM7777/status/2060736517564477901" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 408 · 💬 43</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2060836472958165167">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/yHVz4TUlse”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@levelsio shared an 18-brand SUV side-by-side showing near-identical shapes, quoting a thread arguing that regulations and economic policy — not consumer preference — caused this homogenization.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2060836472958165167" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vasuman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 329 · 💬 45</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vasuman/status/2060847258283999376">View @vasuman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Imagine an AI company that forward deploys into your enterprise to first understand how everything works, then architects what an agent solution looks like custom built for you, and only then builds t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@vasuman describes an AI consulting model: embed in an enterprise, learn its workflows, architect a custom agent solution, then build it — and points out no company currently does this end-to-end.</dd>
      <dt>Why interesting</dt>
      <dd>This 'discover → architect → build' model for enterprise AI agents is an open gap a boutique studio can fill before large consultancies commoditize it.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can package client AI work into three explicit phases — workflow audit, agent architecture, agent build — and pitch it as a differentiated enterprise service.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vasuman/status/2060847258283999376" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vasuman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 320 · 💬 46</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vasuman/status/2060866035067343240">View @vasuman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If you're a software engineer that is down for a paid work trial (1-2 weeks, converts to an internship or full-time offer), come by our office today or tomorrow. I'll interview everyone and get back t”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An individual (@vasuman) is offering a 1-2 week paid work trial at their office that may convert to an internship or full-time role, recruiting via X DM this weekend only.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vasuman/status/2060866035067343240" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
