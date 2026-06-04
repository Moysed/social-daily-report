---
type: social-topic-report
date: '2026-06-04'
topic: devops-cloud
lang: en
pair: devops-cloud.th.md
generated_at: '2026-06-04T03:45:55+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- x
regions:
- global
post_count: 172
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- cloudflare
- vercel
- supabase
- ddos
- observability
- security
thumbnail: https://pbs.twimg.com/media/HJ46_MmXwAAguKX.jpg
---

# DevOps & Cloud — 2026-06-04

## TL;DR
- A remote DoS dubbed "HTTP/2 Bomb" reportedly lets one client pin 32GB of server memory in ~10–20s against nginx, Apache httpd, IIS, Envoy, and Cloudflare Pingora; disclosure credits OpenAI Codex [5][25][27].
- RPCS3 reports 3M+ requests and is blocking Tencent ASN 132203 over sustained high-volume AI scraping that is effectively DDoSing sites [1][4].
- Cloudflare is consolidating identity/billing: Grok added to AI Gateway with billing through Cloudflare [7], plus "Login with Cloudflare" [16] and self-managed OAuth clients via Wrangler [29].
- Supabase now stores local SQL snippets in a git-committable supabase/snippets directory for team sharing [49]; also hired a dedicated Flutter SDK engineer [17].
- Vercel Sandboxes are being used to run third-party parallel coding agents remotely (Conductor) [47], amid v0 leadership departures [31].

## What happened
The strongest reliability signal is a remote DoS disclosure, "HTTP/2 Bomb," claimed to let a single client consume ~32GB of memory in roughly 10–20s against nginx, Apache httpd, Microsoft IIS, Envoy, and Cloudflare Pingora; the timing figure differs across reports (10s [5] vs ~20s [25]) and it is credited to Codex [5][27]. Separately, RPCS3 says it received 3M+ requests and is blocking Tencent ASN 132203 for sustained AI-scraping that overloaded its infrastructure [1][4]. Cloudflare dominated platform news: Grok models (LLM/audio/image/video) added to AI Gateway billed through Cloudflare [7], a broader OpenAI partnership and Worker-compatible ES-module hosting [14][18][21], "Login with Cloudflare" [16], self-managed OAuth clients for Wrangler [29], Sandboxes over Tunnel [35], Browser Run remote tabs [39], and Email Sending named recipients [53].

## Why it matters (reasoning)
For a Next.js + Supabase shop, the HTTP/2 Bomb mainly matters where you terminate your own proxy. Apps fronted by Vercel or Cloudflare's managed edge are the vendor's patch responsibility, but any self-hosted nginx/Envoy (internal tools, streaming, custom gateways) is your exposure [5][25][27]. Treat the disclosure as credible-but-unverified: it is circulating via secondhand security accounts with inconsistent numbers and no reproduced patch advisory in these items, so confirm against vendor CVEs before acting [25][27]. The Tencent scraping surge is a cost-and-reliability issue, not just an annoyance: bot floods inflate egress, edge invocations, and Postgres read load, and can page you at 3am even without a targeted attack [1][4]. Cloudflare's identity/billing consolidation (AI Gateway billing, Login with Cloudflare, OAuth clients) lowers integration friction but increases single-vendor concentration; convenient consolidated billing also makes AI spend easier to start and harder to attribute per-app [7][16][29].

## Possibility
Likely: vendor patches/CVE advisories for HTTP/2 Bomb land quickly given five named servers and high attention, so managed edges (Vercel, Cloudflare) self-remediate while self-hosted proxies lag [5][27]. Likely: AI-scraper traffic keeps rising, pushing more teams toward bot-management rules and per-ASN blocks [1][4]. Plausible: Cloudflare AI Gateway becomes a default consolidation point for AI billing/observability, given the Grok and OpenAI tie-ins [7][14]. Plausible: Vercel product churn around v0 signals reshuffling but not platform instability [31][19]. Unlikely (from these items): any of the marketing partnerships [2][3] change day-to-day runtime cost or reliability for the studio.

## Org applicability — NDF DEV
1) Confirm HTTP/2 Bomb exposure: inventory any self-managed nginx/Envoy/reverse proxies in front of apps and check vendor patch/CVE status; rely on Vercel/Cloudflare to patch their managed edge [5][25][27] (effort: low/med). 2) Tighten Cloudflare bot/rate-limit rules on Supabase-backed endpoints to cap scraper-driven egress and Postgres read load; consider ASN-level blocks for abusive scrapers [1][4] (effort: low). 3) If adding AI features, evaluate Cloudflare AI Gateway for consolidated billing + observability, but tag spend per app to avoid attribution loss [7] (effort: low to evaluate). 4) Adopt Supabase git-committed SQL snippets so migrations/queries are shared and reviewable across the team [49] (effort: low). 5) Optional: trial Vercel Sandboxes for remote coding-agent or preview workloads [47] (effort: med). Skip for now: marketing/partnership posts [2][3][14][18], merch [6], YES-CODE/hype threads [13][44][60], and new observability startups [32] until a concrete pain (cost or pages) justifies a migration off existing tooling.

## Signals to Watch
- HTTP/2 Bomb: watch for official CVE/patch advisories naming nginx, Envoy, and Cloudflare Pingora to confirm real impact vs unverified claim [5][27].
- AI-scraper bot pressure (Tencent ASN 132203 and similar) raising egress/DB load and prompting per-ASN blocks [1][4].
- Cloudflare consolidating identity + billing (AI Gateway billing [7], Login with Cloudflare [16], OAuth clients [29]) — convenience vs vendor concentration.
- Vercel product/leadership churn around v0 [31][19] — monitor for roadmap shifts on Sandboxes/preview tooling [47].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **lnussbaum/incant** — incant: Incus frontend to describe and provision development environments | lobsters | <https://github.com/lnussbaum/incant> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | rpcs3 | ^11283 c95 | [PSA: @TencentGlobal is aggressively scraping the Internet to build yet another A](https://x.com/rpcs3/status/2061946000734888017) |
| x | elonmusk | ^8851 c1068 | [Grok on Cloudflare](https://x.com/elonmusk/status/2062346295256527350) |
| x | elonmusk | ^8663 c1380 | [Grok Imagine on Vercel](https://x.com/elonmusk/status/2062332654587118036) |
| x | Pirat_Nation | ^3896 c60 | [RPCS3 has announced that it is blocking traffic from Tencent ASN 132203 after re](https://x.com/Pirat_Nation/status/2062172954700505145) |
| x | calif_io | ^1744 c22 | [Introducing HTTP/2 Bomb: a remote DoS in nginx, Apache httpd, Microsoft IIS, Env](https://x.com/calif_io/status/2061891591741071765) |
| x | thomasgauvin | ^1203 c104 | [Ok but why does @Cloudflare merch go so hard https://t.co/O0EFBaKVPM](https://x.com/thomasgauvin/status/2061935227514052729) |
| x | CloudflareDev | ^959 c97 | [We're partnering with @xai to bring Grok to @Cloudflare AI Gateway. • Grok LLMs,](https://x.com/CloudflareDev/status/2062281694162629119) |
| x | ni5arga | ^798 c29 | [@cbseindia29 &gt; ddos just cloudflare it dude](https://x.com/ni5arga/status/2061764653559271577) |
| x | steipete | ^796 c26 | [It’s been great working with Omar to get observability and verifiable workspaces](https://x.com/steipete/status/2061877813053907083) |
| x | dieworkwear | ^739 c11 | [Some things I saw recently that I think are cool: — Solbiati Art Du Lin linen an](https://x.com/dieworkwear/status/2061923175852888267) |
| x | _avichawla | ^708 c27 | [A harnessed LLM agent, clearly explained! Most people picture this as a model wi](https://x.com/_avichawla/status/2062082282878627946) |
| x | Maks_NAFO_FELLA | ^704 c10 | [❌ Russian messenger MAX removed from App Store, — Russian media Cloudflare previ](https://x.com/Maks_NAFO_FELLA/status/2062245810243273150) |
| x | rauchg | ^605 c61 | [YES-CODE An entire category of software, "no-code", was built under the presumpt](https://x.com/rauchg/status/2061934154732974376) |
| x | elithrar | ^525 c9 | [OpenAI 🤝 Cloudflare. super excited for this to roll out even more widely.](https://x.com/elithrar/status/2061860660456157607) |
| x | whoiskatrin | ^382 c29 | [🎈 we've just shipped agents sdk v0.14.0 you can now build agents with skills, me](https://x.com/whoiskatrin/status/2061757643471945948) |
| x | threepointone | ^377 c16 | [Big news. Login with Cloudflare is here.](https://x.com/threepointone/status/2062288961041506728) |
| x | spydon | ^373 c47 | [Yesterday I joined @supabase as an SDK Engineer (Flutter)! This is a dream job f](https://x.com/spydon/status/2061784593741611435) |
| x | chatsidhartha | ^364 c14 | [This is huge! @Cloudflare 🤝 @OpenAI](https://x.com/chatsidhartha/status/2061901342382178760) |
| x | nishimiya | ^359 c44 | [1 year at @vercel today i don't think words can fully capture what this year has](https://x.com/nishimiya/status/2061924518348689546) |
| x | InduTripat82427 | ^353 c19 | [10 GitHub repositories so good they shouldn't be free. 1. TradingAgents A full t](https://x.com/InduTripat82427/status/2062136258030350758) |
| x | dok2001 | ^333 c5 | [. @OpenAI has good taste. “Sites hosts projects that build Cloudflare Worker-com](https://x.com/dok2001/status/2061992513997578548) |
| x | perplexity_ai | ^309 c25 | [Perplexity Computer is for growing businesses. Computer connects to 400+ tools f](https://x.com/perplexity_ai/status/2062221423104704753) |
| x | LayoffAI | ^275 c19 | [ORACLE LAYOFFS OFFICIALLY BEGIN AMID COMPLAINTS OF TERRIBLE SEVERANCE TERMS The ](https://x.com/LayoffAI/status/2061890930526032297) |
| x | Surendar__05 | ^272 c57 | [How did he deploy facebook without vercel ? https://t.co/OLWWrGLbyK](https://x.com/Surendar__05/status/2061819081024794663) |
| x | TheHackersNews | ^254 c7 | [🚨 WARNING — New HTTP/2 Bomb exploit targets NGINX, Apache HTTPD, Microsoft IIS, ](https://x.com/TheHackersNews/status/2062091046922977340) |
| x | livingdevops | ^249 c8 | ["We use Prometheus for monitoring." I hear this in almost every interview. Then ](https://x.com/livingdevops/status/2061842632222056595) |
| x | The_Cyber_News | ^247 c5 | [🚨 HTTP/2 Bomb — Remote DoS Exploit Hits nginx, Apache, IIS, Envoy, and Cloudflar](https://x.com/The_Cyber_News/status/2062073588128305426) |
| x | unknown | ^238 c24 | [▲ + ❄️ Generating frontends on top of your business data is one of the killer ap](https://x.com/unknown/status/2062199585322529108) |
| x | CFchangelog | ^236 c13 | [Cloudflare now supports self-managed OAuth clients. Build third-party apps that ](https://x.com/CFchangelog/status/2062279751117439052) |
| x | pulkit_mittal_ | ^224 c1 | [Skills that can push your CTC to 50 LPA but you keep avoiding, as a senior engin](https://x.com/pulkit_mittal_/status/2061979932356722918) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rpcs3</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 11283 · 💬 95</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rpcs3/status/2061946000734888017">View @rpcs3 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“PSA: @TencentGlobal is aggressively scraping the Internet to build yet another AI slop chatbot, DDoSing many websites in the process. We've found that, as of last week, their scraping bots can now sol”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Tencent's AI training bots now bypass Cloudflare challenges and ignore robots.txt, hitting RPCS3 with 3M+ successful requests in 24 hours; RPCS3 recommends sysadmins block ASN 132203.</dd>
      <dt>Why interesting</dt>
      <dd>AI scrapers defeating Cloudflare challenges are a documented, active threat — public web services need ASN-level firewall rules, not just CAPTCHA-based defenses.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Audit firewall rules on any public-facing studio web service and add ASN 132203 plus known abusive Tencent ranges to the blocklist.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rpcs3/status/2061946000734888017" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@elonmusk</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 8851 · 💬 1068</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/elonmusk/status/2062346295256527350">View @elonmusk on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Grok on Cloudflare”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Elon Musk confirmed Grok (xAI's LLM) is now available on Cloudflare, meaning developers can access it via Cloudflare's edge AI infrastructure without self-hosting.</dd>
      <dt>Why interesting</dt>
      <dd>Cloudflare Workers AI already sits in the studio's web stack — Grok joins OpenAI and Anthropic as a drop-in model option with edge latency and Cloudflare's existing billing.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Swap Grok into one existing Cloudflare Workers AI call to compare output quality and token cost against the studio's current model before committing.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/elonmusk/status/2062346295256527350" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@elonmusk</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 8663 · 💬 1380</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/elonmusk/status/2062332654587118036">View @elonmusk on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Grok Imagine on Vercel”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>xAI's Grok Imagine image-generation model is now available to deploy or integrate via Vercel.</dd>
      <dt>Why interesting</dt>
      <dd>Teams already on Vercel can add AI image generation without managing a separate inference endpoint.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Evaluate Grok Imagine on Vercel as an alternative to existing image-gen APIs in any web or e-learning project that generates visual content.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/elonmusk/status/2062332654587118036" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3896 · 💬 60</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2062172954700505145">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“RPCS3 has announced that it is blocking traffic from Tencent ASN 132203 after reporting sustained high-volume scraping activity. According to the RPCS3 team, its infrastructure received more than 3 mi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>RPCS3 blocked Tencent ASN 132203 after absorbing 3M+ successful bot requests in 24 hours from bots that bypass Cloudflare challenges and ignore robots.txt.</dd>
      <dt>Why interesting</dt>
      <dd>Cloudflare challenge pages are no longer a reliable bot barrier; teams running public APIs or asset servers need ASN-level blocking as a fallback layer.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Add ASN-level firewall rules to public-facing services and set alerts for abnormal request volumes from single network ranges.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2062172954700505145" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@calif_io</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1744 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/calif_io/status/2061891591741071765">View @calif_io on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Introducing HTTP/2 Bomb: a remote DoS in nginx, Apache httpd, Microsoft IIS, Envoy, and Cloudflare Pingora. A single client pins 32GB of server memory in 10s. Found by Codex. Blog post: https://t.co/W”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>HTTP/2 Bomb is a newly disclosed remote DoS vulnerability in nginx, Apache httpd, IIS, Envoy, and Cloudflare Pingora — one malicious client exhausts 32 GB of server memory in 10 seconds, with working PoCs published.</dd>
      <dt>Why interesting</dt>
      <dd>Any studio hosting web or API servers on nginx, Apache, or Envoy is directly exposed; no authentication required, and PoCs are already public.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Identify all studio servers running nginx, Apache httpd, IIS, or Envoy and apply the vendor security patches before exposing them to public traffic.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/calif_io/status/2061891591741071765" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@thomasgauvin</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1203 · 💬 104</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/thomasgauvin/status/2061935227514052729">View @thomasgauvin on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ok but why does @Cloudflare merch go so hard https://t.co/O0EFBaKVPM”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Cloudflare developer advocate posted about liking the company's branded merchandise, with no technical content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/thomasgauvin/status/2061935227514052729" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CloudflareDev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 959 · 💬 97</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CloudflareDev/status/2062281694162629119">View @CloudflareDev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We're partnering with @xai to bring Grok to @Cloudflare AI Gateway. • Grok LLMs, audio, image, and video models are now available through AI Gateway • Billed directly through Cloudflare • No additiona”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Cloudflare AI Gateway now routes xAI's Grok models (text, audio, image, video) through its unified proxy, billed via Cloudflare with no separate xAI API keys required.</dd>
      <dt>Why interesting</dt>
      <dd>Teams already using AI Gateway can add Grok models without new auth setup, making multi-model experimentation cheaper to maintain.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio uses Cloudflare AI Gateway, add xai/grok-* as a drop-in model option in existing AI feature configs and compare output quality against current models.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CloudflareDev/status/2062281694162629119" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ni5arga</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 798 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ni5arga/status/2061764653559271577">View @ni5arga on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@cbseindia29 &amp;gt; ddos just cloudflare it dude”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user replied to a DDoS complaint with 'just cloudflare it dude' — a casual one-liner with no technical detail or new information.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ni5arga/status/2061764653559271577" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
