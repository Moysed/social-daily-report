---
type: social-topic-report
date: '2026-06-11'
topic: devops-cloud
lang: en
pair: devops-cloud.th.md
generated_at: '2026-06-11T04:01:02+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- x
regions:
- global
post_count: 125
salience: 0.42
sentiment: neutral
confidence: 0.5
tags:
- cloudflare
- vercel-ai-gateway
- llm-cost-control
- bot-traffic
- postgres-supabase
- observability-ops
thumbnail: https://pbs.twimg.com/media/HKXO64AaEAAEgrL.jpg
---

# DevOps & Cloud — 2026-06-11

## TL;DR
- Vercel AI Gateway now supports per-API-key spend budgets with refresh periods, settable via CLI (`--budget`/`--refresh-period`) or UI [21][52] — the one concrete, double-sourced cost guardrail in today's set for capping LLM bills on gateway-routed apps.
- Cloudflare's headline ~93% 'code mode' token savings [13][29] is verified unsupported: a first-party figure from two Cloudflare employees, no methodology, no independent benchmark. The architectural pattern (model writes code to orchestrate tool calls) is plausibly token-saving for MCP/tool-heavy agents, but the number is not reproducible.
- Cloudflare (CEO Matthew Prince, mid-2026) reports automated requests crossed ~57% of HTTP requests to HTML on its network for the first time [38] (verified supported, with caveats): metric = HTML requests not total traffic, sample = Cloudflare sites, 'bots' bundles crawlers with AI agents. Directional input for rate-limiting and origin capacity planning.
- PgDog's $5.5M seed pooler/sharder [31] is interesting but 'production-ready' is verified unsupported — single founder source, self-reported numbers, seed-stage. Supabase already ships Supavisor/PgBouncer, so this is a future-watch only, not a hot-path dependency for a fewer-3am-pages shop.
- Several concrete Cloudflare betas (Email Service SMTP submission [16], Images Worker binding [44], Private Origins [43]) reduce credential surface or third-party deps, but all are beta/closed-beta — validate before any 3am-page-sensitive flow depends on them.

## What happened
Today's DevOps/Cloud signal is moderate and Cloudflare-weighted, with most engagement being crypto/model-hype noise. The one solidly actionable item is Vercel AI Gateway adding per-API-key budget caps with refresh periods, corroborated by two independent posts with consistent CLI syntax (`vercel ai-gateway api-keys create --budget 1000`) [21][52] — though still tweet-sourced, not yet confirmed against Vercel docs (verify whether budgets hard-block or soft-alert). The most-circulated cost claim — Cloudflare 'code mode' saving ~93% on tokens [13][29] — is verified unsupported: both sources are Cloudflare employees, the figure has no disclosed baseline/workload/methodology, and a full-archive search found no third-party benchmark. Cloudflare's claim that bots/AI agents now exceed human web traffic [38] is verified supported but narrow: it is ~57% of HTTP requests to HTML on Cloudflare's own network (not total traffic/bytes), from a single interested vendor, bundling benign crawlers with AI agents. On the data layer, PgDog raised $5.5M seed for a Postgres pooler/load-balancer/sharder [31], but 'production-ready' is verified unsupported (lone founder source, self-reported QPS, ~1yr old). Cloudflare also shipped/announced several concrete platform pieces: Email Service SMTP submission in beta works with Nodemailer/smtplib [16]; an Images Workers binding removing API-token handling [44]; and Application Services for Private Origins in closed beta [43] for private-IP origins with no public IPs. Supporting the operational thesis, Honeycomb/Charity Majors argue the bottleneck is release/debug/operate, not code authoring [5][6][12] (credible practitioner opinion, mild vendor self-interest). Vercel Ship London next week teases unspecified announcements [27] — a revisit-later item, not a decision input.

## Why it matters (reasoning)
For NDF DEV (Next.js + Supabase on Vercel/Cloudflare; goals: fewer 3am pages, lower runtime bills), the practical wins are narrow and specific. Per-key AI spend caps [21][52] map directly to the cost goal: if production routes model calls through Vercel AI Gateway, a hard budget per key/project is a defensible guardrail against runaway LLM bills — the single highest-value, lowest-effort item today. The bot-traffic trend [38], even discounted as vendor-sourced and metric-narrow, is directionally consistent with growing agent/crawler load and supports keeping rate-limiting and bot-management posture current for public-facing apps. The cost claims that would most tempt budgeting decisions (~93% code-mode savings, halved AI-build cost) are the weakest evidence in the set and must not be planned against. On reliability, the through-line favoring this shop is the opposite of AI-output-volume chasing: invest in observability and ops, treat new seed-stage data-plane components (PgDog) as future options rather than hot-path dependencies, and keep beta features out of page-sensitive flows until validated.

## Possibility
Plausible near-term: the model-writes-code-to-orchestrate-tools pattern [13][29] does cut tokens for MCP/tool-heavy agent workloads, but the magnitude for NDF's workloads is unknown and unlikely to approach the cited ~93% without the same MCP-saturation context (verified unsupported). Plausible: Vercel AI Gateway budgets behave as a usable spend cap [21][52], pending confirmation of hard-block vs soft-alert semantics. Plausible-to-likely: agent/crawler share of public traffic keeps rising [38], increasing relevance of rate-limiting and origin capacity planning regardless of the exact 57% figure. Unlikely to be decision-grade soon: PgDog as a production hot-path component for a Supabase studio [31] — seed-stage, single-source, and Supabase already covers pooling via Supavisor. Unknown: Vercel Ship London [27] may surface reliability/cost-relevant features; revisit after the event. Signal is thin on Supabase specifically (only [45], a single anecdote) and on independently verified cost numbers, so confidence is held down.

## Org applicability — NDF DEV
DO NOW (low effort) [21][52]: If any production app routes LLM calls through Vercel AI Gateway, set a per-key budget + refresh period (`vercel ai-gateway api-keys create --budget N --refresh-period ...`); first confirm in Vercel docs whether it hard-blocks or only alerts before treating it as a billing safety net. DO SOON (low effort) [38]: Sanity-check rate-limiting/bot-management config on public-facing endpoints given rising agent/crawler traffic — config review, not a project. EVALUATE (med effort, non-prod) [16][44]: If self-hosting SMTP or managing image-upload tokens is current pain, trial Email Service SMTP submission [16] and the Images Worker binding [44] in staging; keep them out of 3am-page-sensitive transactional flows until beta limits/deliverability are proven. CONSIDER LATER (med effort) [43]: Note Private Origins closed beta if you ever need to expose internal services without public IPs; closed beta = no commitment now. WATCH ONLY (low effort) [27][31]: Revisit Vercel Ship London after the event [27]; track PgDog maturity [31] but do not put a seed-stage pooler in the query hot path. SKIP: the ~93% code-mode savings figure [13][29] and the $100k/eng/year hearsay (do not budget against — verified unsupported); the halved-AI-build-cost n=1 anecdote [15]; 'AI code slows teams' as fact [1] (verified unsupported — use only as the narrower 'release/debug/operate is the bottleneck' framing per [5][6][12]); the ~$250K Cloudflare credits listicle figure [60] (verify directly with Cloudflare for Startups); the WAF-bypass [34], Vercel staff-departure [19][30], stock-move [42], '100% vibed' [8], and event/sponsor [58] items as noise; and the Supabase fix anecdote [45] as a reliability metric.

## Signals to Watch
- VERIFIED UNSUPPORTED: Cloudflare ~93% code-mode token savings [13][29] — two Cloudflare-employee sources, no methodology, no independent benchmark; cite only as attributed first-party self-report, never as a reproducible figure.
- VERIFIED SUPPORTED (caveated): Cloudflare CEO mid-2026 — automated requests ~57% of HTTP-to-HTML on Cloudflare's network [38]; not total traffic/bytes, Cloudflare-sample only, 'bots' bundles crawlers + AI agents.
- VERIFIED UNSUPPORTED: PgDog 'production-ready' [31] — lone founder source, self-reported QPS/TB, seed-stage ~1yr old; treat as vendor description, not fact.
- Strongest actionable signal: Vercel AI Gateway per-key budgets + refresh periods [21][52], double-sourced with consistent CLI syntax but still tweet-sourced (confirm hard-block vs soft-alert in docs).

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | awscloud | ^17958 c573 | [More AI-generated code doesn't make your team faster. It might actually slow you](https://x.com/awscloud/status/2064449711155589396) |
| x | BullTheoryio | ^3263 c167 | [BREAKING: Anthropic is expected to release Claude Mythos tomorrow, the same mode](https://x.com/BullTheoryio/status/2064284141315916074) |
| x | indiesoftwaredv | ^2373 c146 | [This is my loop I built a SaaS that posts to Instagram + TikTok 24/7 I don't wri](https://x.com/indiesoftwaredv/status/2064571261980709117) |
| x | omoalhajaabiola | ^2008 c60 | [Saw a website content writing job on Upwork. You know what I did instead of send](https://x.com/omoalhajaabiola/status/2064454035571126691) |
| x | awscloud | ^1525 c16 | [The real bottleneck was never writing code. It's releasing it, debugging it, &am](https://x.com/awscloud/status/2064449713257017646) |
| x | awscloud | ^1156 c5 | [@honeycombio Her team also skipped the mandates &amp; built a set of AI values i](https://x.com/awscloud/status/2064449715677106522) |
| x | sawyerhood | ^755 c30 | [I gave Fable this tweet and let it crank in ultracode. It created a fully functi](https://x.com/sawyerhood/status/2064444395727036811) |
| x | thdxr | ^668 c18 | [we did something similar on cloudflare we have these internal apps that use cf p](https://x.com/thdxr/status/2064802335121981579) |
| x | aayushman2703 | ^645 c81 | [I was laid off so I rebuilt their product but better (in 2 weeks from scratch) O](https://x.com/aayushman2703/status/2064709405015495114) |
| x | coinbureau | ^560 c71 | [🚨BREAKING: Mastercard $MA launches Agent Pay, allowing AI agents to pay each oth](https://x.com/coinbureau/status/2064709969979814340) |
| x | JJEnglert | ^550 c46 | [The Claude Fable 5 Review: One Billion Tokens, Judged by a Non-Engineer I spent ](https://x.com/JJEnglert/status/2064420538798260388) |
| x | awscloud | ^493 c3 | [@honeycombio Quality first, quantity second. Hear how @mipsytipsy built it on th](https://x.com/awscloud/status/2064449718676033878) |
| x | ritakozlov | ^488 c12 | [code mode has helped @cloudflare save ~93% on token cost talking to peers in the](https://x.com/ritakozlov/status/2064414840391704830) |
| x | fivosaresti | ^352 c21 | [‘Service-as-a-software’ is here... We moved our entire company brain to GitHub a](https://x.com/fivosaresti/status/2064422353816219984) |
| x | _avichawla | ^332 c8 | [I cut Fable 5 token usage 2.5x with just one change! - Before: 5.5 M tokens · 7 ](https://x.com/_avichawla/status/2064664116963455373) |
| x | CFchangelog | ^327 c9 | [SMTP submission is now available in beta for Cloudflare Email Service. Send emai](https://x.com/CFchangelog/status/2064287790922109392) |
| x | polidemitolog | ^315 c31 | [Russian asset Edward Snowden appeared in a Rossiya 1 report claiming that foreig](https://x.com/polidemitolog/status/2064423282267328974) |
| x | Mastercard | ^296 c17 | [Partners: @0xPolygonEco, @aave, @Adyen, @Alchemy, @Anchorage, @Ant_Intl, @basist](https://x.com/Mastercard/status/2064719498288980331) |
| x | okbel | ^248 c20 | [6 years at Vercel. Built an incredibly productive team and shipped an insane amo](https://x.com/okbel/status/2064330733187965261) |
| x | rileybrown | ^245 c25 | [I'm SO excited for Agentic Payments. This will truly give your agent the power t](https://x.com/rileybrown/status/2064815262688227486) |
| x | rauchg | ^232 c28 | [Vercel CLI now allows you to: ◾ create AI Gateway API keys ◾ pass a --𝚋𝚞𝚍𝚐𝚎𝚝 to ](https://x.com/rauchg/status/2064551967461114111) |
| x | RhysSullivan | ^218 c23 | [Executor v1.5 is live! Highlights: - Sources -&gt; Integrations - Full GSuite su](https://x.com/RhysSullivan/status/2064506063106253233) |
| x | ElizabethA77617 | ^213 c49 | [Top 100 AI Tools in 2026 (The Ultimate Cheatsheet) Save this. You'll thank me la](https://x.com/ElizabethA77617/status/2064337086870864272) |
| x | RhysSullivan | ^173 c4 | [good new detail from cloudflare, after signing in to wrangler CLI they help you ](https://x.com/RhysSullivan/status/2064234368143691818) |
| x | skeptrune | ^168 c16 | [was interviewing a new grad & i didn't blink an eye when he used cloudflare inst](https://x.com/skeptrune/status/2064795835767075112) |
| x | davis7 | ^168 c11 | [Testing Fable, it's clearly a great model Quality of code on a couple effect v4 ](https://x.com/davis7/status/2064457646653215094) |
| x | rauchg | ^166 c27 | [🇬🇧 London calling Excited for Vercel Ship next week Some special announcements… ](https://x.com/rauchg/status/2064777495422161205) |
| x | vercel | ^163 c16 | [https://t.co/hUowOdv4Ci](https://x.com/vercel/status/2064188171294761076) |
| x | mattzcarey | ^154 c6 | [in the past few days the Cloudflare MCP server made 2.6M API requests from 735k ](https://x.com/mattzcarey/status/2064377811180093713) |
| x | anthonysheww | ^149 c15 | [4 years at Vercel.](https://x.com/anthonysheww/status/2064372564009624040) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@awscloud</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 17958 · 💬 573</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/awscloud/status/2064449711155589396">View @awscloud on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“More AI-generated code doesn't make your team faster. It might actually slow you down.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>AWS Cloud states that higher AI-generated code volume does not improve team velocity and can slow delivery by increasing review, debug, and maintenance load.</dd>
      <dt>Why interesting</dt>
      <dd>Small dev teams absorb AI code debt directly — output volume is a vanity metric if quality gates are absent.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should audit current AI-assisted workflows and enforce a lightweight review gate before AI-generated code merges into any branch.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/awscloud/status/2064449711155589396" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BullTheoryio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3263 · 💬 167</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BullTheoryio/status/2064284141315916074">View @BullTheoryio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“BREAKING: Anthropic is expected to release Claude Mythos tomorrow, the same model it said was too dangerous to make public. A &quot;Mythos 1&quot; tag was briefly spotted inside the Claude Code UI last week bef”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Anthropic is reportedly releasing Claude Mythos, a previously restricted model that found 271 Firefox vulnerabilities in a security-audit preview — including 15- and 20-year-old bugs missed by years of human auditing.</dd>
      <dt>Why interesting</dt>
      <dd>If AI-driven static security auditing at this scale ships as an API, small teams gain automated vulnerability discovery that previously required dedicated security engineers.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Track Anthropic's release notes for Claude Mythos API access and plan a trial run against the studio's own codebases before production deployments.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BullTheoryio/status/2064284141315916074" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@indiesoftwaredv</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2373 · 💬 146</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/indiesoftwaredv/status/2064571261980709117">View @indiesoftwaredv on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is my loop I built a SaaS that posts to Instagram + TikTok 24/7 I don't write the captions. I don't pick the music. I don't touch it The stack that runs it while I sleep: &gt; PHP 8.3, no framework ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A solo dev runs a production SaaS that auto-posts to Instagram and TikTok 24/7 using PHP 8.3, SQLite WAL, Cloudflare R2 + Tunnel, OpenAI captions, and one cron job — no framework, no Kubernetes.</dd>
      <dt>Why interesting</dt>
      <dd>Cloudflare Tunnel (zero open ports) + R2 + SQLite WAL is a proven, low-ops deployment pattern a small studio can ship and maintain without dedicated DevOps.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can standardize Cloudflare Tunnel + R2 as the default deployment for small client web apps to remove VPS port exposure and reduce storage overhead.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/indiesoftwaredv/status/2064571261980709117" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@omoalhajaabiola</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2008 · 💬 60</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/omoalhajaabiola/status/2064454035571126691">View @omoalhajaabiola on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Saw a website content writing job on Upwork. You know what I did instead of sending a generic proposal? I took the job description, fed it to Grok, and asked it to create a full website layout for a h”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A freelancer used Grok to plan a site layout, built it with Claude (including a 3D section via Render MCP), deployed live on Netlify, then submitted the URL as the proposal — landing the gig in 30 minutes.</dd>
      <dt>Why interesting</dt>
      <dd>The live-demo-as-proposal tactic cuts through generic pitches; it directly applies to how the studio responds to web and XR client briefs where showing the work beats describing it.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When responding to the next web or XR client brief, build a quick prototype with Claude + Netlify and lead the pitch with the live URL instead of a slide deck.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/omoalhajaabiola/status/2064454035571126691" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@awscloud</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1525 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/awscloud/status/2064449713257017646">View @awscloud on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The real bottleneck was never writing code. It's releasing it, debugging it, &amp;amp; keeping it running well. So when @Honeycombio CTO Charity Majors set a productivity target, she didn't chase 10x. She”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Honeycomb.io CTO Charity Majors argues the real dev bottleneck is releasing, debugging, and operating code — not writing it — and set a deliberate 2x productivity target built around that insight.</dd>
      <dt>Why interesting</dt>
      <dd>For a small studio, fixing the deploy-and-debug loop yields more output per person than any code-generation tool — and 2x is a target a team can actually hit and measure.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Map one sprint's lost hours across deploy, debug, and incident response — if that exceeds writing time, prioritize observability tooling before adding new feature velocity.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/awscloud/status/2064449713257017646" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@awscloud</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1156 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/awscloud/status/2064449715677106522">View @awscloud on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@honeycombio Her team also skipped the mandates &amp;amp; built a set of AI values instead: &quot;Every AI output has to have a human owner. If you don't want your name on it, it's probably not good work.&quot;”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Honeycomb's team replaced AI mandates with one accountability rule: every AI output must have a named human owner willing to put their name on it.</dd>
      <dt>Why interesting</dt>
      <dd>One rule replaces an entire AI policy doc and keeps accountability at the individual contributor level — practical for small teams shipping AI-assisted work daily.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can adopt this as a working norm: any AI-assisted deliverable — code, copy, or design brief — requires a named team member accountable for its quality before it ships.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/awscloud/status/2064449715677106522" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sawyerhood</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 755 · 💬 30</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sawyerhood/status/2064444395727036811">View @sawyerhood on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I gave Fable this tweet and let it crank in ultracode. It created a fully functioning multiplayer markdown editor with obsidian style editing, version history, sharing with email invites, cli sync wit”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@sawyerhood fed Fable (Claude Code's agent model) a single tweet in ultracode mode; it autonomously built a multiplayer markdown editor with version history, email-invite sharing, CLI sync, image support, deployed to Cloudflare, and registered a domain.</dd>
      <dt>Why interesting</dt>
      <dd>This is a concrete ceiling benchmark: one agentic session can take a feature-complete web app from prompt to live domain, directly relevant to the studio's rapid prototyping and client demo workflow.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run a Fable ultracode session against a planned web or e-learning prototype to measure how far it scaffolds end-to-end before human review is needed.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sawyerhood/status/2064444395727036811" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@thdxr</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 668 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/thdxr/status/2064802335121981579">View @thdxr on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“we did something similar on cloudflare we have these internal apps that use cf primitives like workers, sqlite, r2 and they're all fronted by cloudflare access which requires SSO 100% vibed by opencod”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Dax Raad (SST) runs internal tools on Cloudflare Workers + D1 SQLite + R2, all gated by Cloudflare Access SSO — no external auth server — and built the whole thing with OpenCode.</dd>
      <dt>Why interesting</dt>
      <dd>Proves CF's full primitive stack (compute + DB + storage + auth) handles real internal tooling without stitching in third-party services — low ops cost for a small team.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can use CF Workers + D1 + R2 + Access as the default stack for internal dashboards or admin tools — skip the separate auth and DB setup.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/thdxr/status/2064802335121981579" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
