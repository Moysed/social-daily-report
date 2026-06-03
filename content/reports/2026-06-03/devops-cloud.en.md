---
type: social-topic-report
date: '2026-06-03'
topic: devops-cloud
lang: en
pair: devops-cloud.th.md
generated_at: '2026-06-03T06:58:56+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- x
regions:
- global
post_count: 168
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- cloudflare
- security
- observability
- cost
- vercel
- supabase
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2061452121648865280/img/hS8gE8pxV4lWpSMx.jpg
---

# DevOps & Cloud — 2026-06-03

## TL;DR
- HTTP/2 Bomb: a single client can pin 32GB of server memory in ~10s against nginx, Apache httpd, IIS, Envoy, and Cloudflare's Pingora — a remote DoS found via Codex [15].
- Cloudflare priced R2 SQL, R2 Data Catalog, and Pipelines; billing is not yet on, with 30 days' notice before it starts [31].
- Grafana closed its internal investigation reporting no unauthorized access to customer production or Grafana Cloud, and brought in Mandiant; separately more Grafana CVEs surfaced [47][28].
- AI scraping load is rising — Tencent bots reported DDoSing sites while scraping [1] — keeping bot/DDoS controls a live concern [5].
- Concrete serverless reference stack shipped: Caltext on Vercel uses Hono on Nitro, Upstash Redis, and Vercel Workflows [3]; Cloudflare Agents SDK v0.14.0 added durable workflows and schedules [14].

## What happened
On the reliability side, a remote DoS dubbed HTTP/2 Bomb was disclosed affecting nginx, Apache httpd, Microsoft IIS, Envoy, and Cloudflare Pingora, where one client can pin 32GB of memory in about 10 seconds; it was found by Codex [15]. AI scraping pressure was visible too, with reports of Tencent bots DDoSing sites during scraping [1] and the usual 'just put Cloudflare in front' reflex [5]. Grafana said its internal investigation found no unauthorized access to customer production systems or Grafana Cloud and engaged Mandiant [47], while a separate post flagged additional Grafana CVEs [28].

## Why it matters (reasoning)
For a Next.js + Supabase + Cloudflare/Vercel shop, the HTTP/2 Bomb [15] is the item that maps directly to 3am pages: managed edges (Cloudflare, Vercel) will likely be patched by the provider, but any self-hosted origin running nginx/Apache/Envoy is exposed until patched, and the named inclusion of Pingora means the edge layer is in scope rather than purely the origin. Rising AI scraping traffic [1] raises baseline request volume and bandwidth, which both stresses reliability and feeds runtime bills — the same direction as the cost focus of this brief. Cloudflare's R2 pricing finalization [31] matters because it converts a free/experimental data path into a metered one; the 30-day notice is the planning window before storage/query lines start appearing. The Grafana incident plus fresh CVEs [47][28] is a reminder that the observability layer itself is attack surface and a dependency to monitor, not just a passive dashboard.

## Possibility
Likely: providers patch HTTP/2 Bomb at the edge quickly given the named vendors, but self-managed origins lag — exposure persists wherever the studio runs its own nginx/Apache/Envoy [15]. Likely: Cloudflare enables R2 billing after the stated 30-day notice, so any R2 SQL/Data Catalog/Pipelines usage becomes a line item [31]. Plausible: AI scraping volume keeps climbing, pushing more teams toward bot management and rate limiting [1]. Plausible: the observability market keeps fragmenting with new entrants (Sazabi [32]) and pricing moves (Honeycomb uncapping [4]) pressuring incumbents like Datadog/Sentry/Grafana. No source gives numeric probabilities, so none are asserted.

## Org applicability — NDF DEV
1) Inventory any self-hosted nginx/Apache/Envoy in origins or internal tooling and patch/verify against HTTP/2 Bomb; confirm Cloudflare/Vercel edge is provider-patched (low) [15]. 2) Review Cloudflare bot/DDoS and rate-limit settings on production sites given the scraping surge (low) [1][5]. 3) If using or planning R2 (R2 SQL, Data Catalog, Pipelines), price the workload now and set a reminder for the 30-day billing-enable window (low) [31]. 4) If observability runs on Grafana Cloud, read the Mandiant follow-up and patch flagged CVEs; if self-hosting Grafana, prioritize the CVE updates (low) [47][28]. 5) For new serverless builds, treat Caltext as a reference for a Vercel-native stack (Hono on Nitro, Upstash Redis, Vercel Workflows) and compare against Cloudflare Agents SDK durable workflows before committing (med) [3][14]. Skip: agent-demo hype [18][44], vendor personnel/merch/office posts [20][23][34][35][33], gaming/DLSS [6][27], and the no-code/yes-code commentary [12] — no operational signal for production reliability or cost.

## Signals to Watch
- HTTP/2 Bomb patch rollout and any Cloudflare Pingora advisory — confirms whether edge exposure is closed [15].
- Cloudflare R2 billing enablement date after the 30-day notice — the trigger for new storage/query costs [31].
- Grafana's Mandiant findings and CVE patch cadence — dependency risk for the observability layer [47][28].
- Observability pricing/entrant shifts (Honeycomb uncapping, Sazabi) that could lower monitoring spend [4][32].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **lnussbaum/incant** — incant: Incus frontend to describe and provision development environments | lobsters | <https://github.com/lnussbaum/incant> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | rpcs3 | ^7353 c60 | [PSA: @TencentGlobal is aggressively scraping the Internet to build yet another A](https://x.com/rpcs3/status/2061946000734888017) |
| x | contextkingceo | ^1885 c230 | [Introducing HydraDB. The graph native context infrastructure for agents. Purpose](https://x.com/contextkingceo/status/2061452631298752790) |
| x | pontusab | ^1269 c56 | [Introducing Caltext, open-source calorie tracking in iMessage. Built with: • Bun](https://x.com/pontusab/status/2061410279922282556) |
| x | delvieero | ^833 c793 | [Honeycomb uncapping 👏🏻 🍯 🐝 ❤️ https://t.co/9x3NdAz0rf](https://x.com/delvieero/status/2061576021405503791) |
| x | ni5arga | ^738 c27 | [@cbseindia29 &gt; ddos just cloudflare it dude](https://x.com/ni5arga/status/2061764653559271577) |
| x | NVIDIAGeForce | ^653 c36 | [DLSS 4.5 is powering today's hits &amp; tomorrow's releases including: 🟢 Phantom](https://x.com/NVIDIAGeForce/status/2061485433314250932) |
| x | steipete | ^614 c18 | [It’s been great working with Omar to get observability and verifiable workspaces](https://x.com/steipete/status/2061877813053907083) |
| x | rauchg | ^561 c30 | [Beautiful example of a full-stack agent on @vercel. Great learning material!](https://x.com/rauchg/status/2061415178298937365) |
| x | dieworkwear | ^555 c11 | [Some things I saw recently that I think are cool: — Solbiati Art Du Lin linen an](https://x.com/dieworkwear/status/2061923175852888267) |
| x | awscloud | ^512 c48 | [Now generally available, @OpenAI GPT-5.5, GPT-5.4, and Codex on Amazon Bedrock. ](https://x.com/awscloud/status/2061564484523524302) |
| x | elithrar | ^471 c9 | [OpenAI 🤝 Cloudflare. super excited for this to roll out even more widely.](https://x.com/elithrar/status/2061860660456157607) |
| x | rauchg | ^449 c41 | [YES-CODE An entire category of software, "no-code", was built under the presumpt](https://x.com/rauchg/status/2061934154732974376) |
| x | awscloud | ^436 c20 | [(1/2) Your most sensitive code deserves AI that never leaves your network. https](https://x.com/awscloud/status/2061523521331671423) |
| x | whoiskatrin | ^358 c28 | [🎈 we've just shipped agents sdk v0.14.0 you can now build agents with skills, me](https://x.com/whoiskatrin/status/2061757643471945948) |
| x | calif_io | ^353 c4 | [Introducing HTTP/2 Bomb: a remote DoS in nginx, Apache httpd, Microsoft IIS, Env](https://x.com/calif_io/status/2061891591741071765) |
| x | cjc | ^348 c15 | [Only missed out on these tiny startups: - Anthropic - Cursor - Perplexity - Sier](https://x.com/cjc/status/2061627852186169544) |
| x | PeterDiamandis | ^328 c52 | [Tech companies are laying off people by the thousands, doing so without an ounce](https://x.com/PeterDiamandis/status/2061484183441305965) |
| x | RoundtableSpace | ^315 c36 | [THIS GUY GAVE CLAUDE CODE A $1,000 BUDGET, WENT TO SLEEP, AND WOKE UP TO 4 AGENT](https://x.com/RoundtableSpace/status/2061572245923999815) |
| x | ai_trade_pro | ^296 c0 | [Quietly one of the most important AI updates of the month, and it’s not a benchm](https://x.com/ai_trade_pro/status/2061479694361395504) |
| x | thomasgauvin | ^293 c29 | [Ok but why does @Cloudflare merch go so hard https://t.co/O0EFBaKVPM](https://x.com/thomasgauvin/status/2061935227514052729) |
| x | StockMKTNewz | ^292 c74 | [All these stocks hit new 52 WEEK HIGHS at some point today Micron $MU Broadcom $](https://x.com/StockMKTNewz/status/2061533276821479572) |
| x | spydon | ^280 c38 | [Yesterday I joined @supabase as an SDK Engineer (Flutter)! This is a dream job f](https://x.com/spydon/status/2061784593741611435) |
| x | nishimiya | ^279 c35 | [1 year at @vercel today i don't think words can fully capture what this year has](https://x.com/nishimiya/status/2061924518348689546) |
| x | chatsidhartha | ^270 c11 | [This is huge! @Cloudflare 🤝 @OpenAI](https://x.com/chatsidhartha/status/2061901342382178760) |
| x | LayoffAI | ^246 c19 | [ORACLE LAYOFFS OFFICIALLY BEGIN AMID COMPLAINTS OF TERRIBLE SEVERANCE TERMS The ](https://x.com/LayoffAI/status/2061890930526032297) |
| x | 0xJuliechen | ^241 c11 | [sf bros when they say they’re building an agent: “a stateful agent with full obs](https://x.com/0xJuliechen/status/2061562085910155387) |
| x | NVIDIAGeForce | ^222 c16 | [Explore, adapt, and survive Sota7 with #RTXOn. Honeycomb: The World Beyond arriv](https://x.com/NVIDIAGeForce/status/2061531530514575769) |
| x | Zierax_x | ^214 c1 | [now Grafana Final Scanner have more CVEs 🥳🥳🥳 https://t.co/l9K3DyIYcz https://t.c](https://x.com/Zierax_x/status/2061466550385639587) |
| x | Surendar__05 | ^209 c47 | [How did he deploy facebook without vercel ? https://t.co/OLWWrGLbyK](https://x.com/Surendar__05/status/2061819081024794663) |
| x | PopPunkOnChain | ^207 c20 | [Pumpcade is now a Tier 1 @Cloudflare startup. We just recieved $350,000 in credi](https://x.com/PopPunkOnChain/status/2061449233153057214) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rpcs3</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7353 · 💬 60</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rpcs3/status/2061946000734888017">View @rpcs3 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“PSA: @TencentGlobal is aggressively scraping the Internet to build yet another AI slop chatbot, DDoSing many websites in the process. We've found that, as of last week, their scraping bots can now sol”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>RPCS3 reports Tencent's AI-training scrapers now bypass Cloudflare bot challenges, delivering 3M+ successful requests in 24 hrs; they recommend sysadmins block ASN 132203.</dd>
      <dt>Why interesting</dt>
      <dd>Cloudflare challenges alone no longer stop aggressive AI scrapers — studios hosting public sites need IP-level firewall rules on top.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Audit firewall rules on studio-hosted web services and APIs; add a block for ASN 132203 on any that show anomalous traffic spikes.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rpcs3/status/2061946000734888017" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@contextkingceo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1885 · 💬 230</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/contextkingceo/status/2061452631298752790">View @contextkingceo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing HydraDB. The graph native context infrastructure for agents. Purpose built to deliver precise context &amp; observability into why agents act the way they do. We've always believed graphs are ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>HydraDB is a new graph-native database that combines in-memory, NVMe, and object storage into one layer to deliver AI agent context faster and cheaper than existing graph solutions.</dd>
      <dt>Why interesting</dt>
      <dd>Teams building multi-agent pipelines need fast, low-cost context retrieval with observability into agent decisions — HydraDB targets exactly that gap.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Benchmark HydraDB against the studio's current context or memory store in any active agent workflow before committing to a vector DB approach.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/contextkingceo/status/2061452631298752790" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@pontusab</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1269 · 💬 56</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/pontusab/status/2061410279922282556">View @pontusab on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing Caltext, open-source calorie tracking in iMessage. Built with: • Bun + Turborepo • Hono on Nitro (Vercel) • Chat SDK + Sendblue • AI SDK + GPT-4.1 vision • Upstash Redis • Vercel Workflows”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Open-source iMessage calorie tracker ships a full stack of Bun, Turborepo, Hono on Nitro, GPT-4.1 vision, Upstash Redis, and Vercel Workflows in one public repo.</dd>
      <dt>Why interesting</dt>
      <dd>Concrete reference for wiring Vercel Workflows + Upstash Redis + AI vision into an async pipeline — a pattern the studio can reuse in web or e-learning projects.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Clone the repo and extract the Vercel Workflows + Upstash Redis pattern as a starter template for async AI features in the studio's web stack.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/pontusab/status/2061410279922282556" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@delvieero</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 833 · 💬 793</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/delvieero/status/2061576021405503791">View @delvieero on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Honeycomb uncapping 👏🏻 🍯 🐝 ❤️ https://t.co/9x3NdAz0rf”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Honeycomb (distributed tracing / observability platform) announced removal of an unspecified usage cap; the post links only to a video with no text detail on what was uncapped.</dd>
      <dt>Why interesting</dt>
      <dd>If Honeycomb removed query or data-volume limits on lower tiers, small teams gain more observability headroom at the same price point.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Check Honeycomb's blog or changelog directly to confirm what was uncapped before expanding usage in the studio's observability stack.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/delvieero/status/2061576021405503791" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ni5arga</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 738 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ni5arga/status/2061764653559271577">View @ni5arga on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@cbseindia29 &amp;gt; ddos just cloudflare it dude”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer on X sarcastically suggests that CBSE India (a national exam board) should just 'Cloudflare it' in response to a DDoS incident on their platform.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ni5arga/status/2061764653559271577" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NVIDIAGeForce</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 653 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NVIDIAGeForce/status/2061485433314250932">View @NVIDIAGeForce on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“DLSS 4.5 is powering today's hits &amp;amp; tomorrow's releases including: 🟢 Phantom Blade Zero 🟢 CINDER CITY 🟢 Squad 🟢 Marvel Rivals 🟢 Gothic 1 Remake 🟢 NARAKA: Bladepoint 🟢 Honeycomb: The World Beyond 🟢”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>NVIDIA GeForce posted a marketing list of games shipping with DLSS 4.5 support, including Marvel Rivals and Phantom Blade Zero — no new SDK, API, or developer tooling announced.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NVIDIAGeForce/status/2061485433314250932" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 614 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2061877813053907083">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It’s been great working with Omar to get observability and verifiable workspaces into OpenClaw.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@steipete posted a collaboration shoutout about adding observability and verifiable workspaces to a project called OpenClaw — no technical details, docs, or release link included.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2061877813053907083" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 561 · 💬 30</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2061415178298937365">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Beautiful example of a full-stack agent on @vercel. Great learning material!”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Vercel CEO @rauchg praised an unnamed full-stack agent example hosted on Vercel as learning material, without linking the example or describing its stack or functionality.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2061415178298937365" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
