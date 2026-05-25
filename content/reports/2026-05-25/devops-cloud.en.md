---
type: social-topic-report
date: '2026-05-25'
topic: devops-cloud
lang: en
pair: devops-cloud.th.md
generated_at: '2026-05-25T08:44:42+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- x
regions:
- global
post_count: 90
salience: 0.78
sentiment: mixed
confidence: 0.74
tags:
- supabase
- cloudflare-r2
- vercel
- egress-cost
- rls-security
- nextjs-stack
thumbnail: https://pbs.twimg.com/media/HI_lY1ZaIAA9sam.jpg
---

# DevOps & Cloud — 2026-05-25

## TL;DR
- Cost reality check: Postbridge at $35K MRR is bleeding ~$700/mo in Supabase egress while R2 charges $0 egress [5][38][14]; Postiz at $105K MRR runs on Railway $200 + R2 $160 [22].
- R2 dominance keeps growing — 15TB of 4K video for $2.18 [25], plus a temp-share pattern on R2+Durable Objects [27] and R2 sync connectors [23].
- Supabase gotcha: anonymous sign-in created a 3-week security hole; widely missed RLS edge case [54].
- Vercel posture: 10-yr tenure post [9], 'no employees still hand-write code' claim [18], hiring push [45] — platform stable, AI-native dev workflow normalized.
- Cloudflare ops noise: Discord overrun by scams after disbanding community champions [56]; ADL/Kiwi Farms pressure + Chamath spat add reputational risk [2][4][55].

## What happened
Two concrete cost case studies dropped today: Jack Friks broke down Postbridge's $35K MRR stack and discovered Supabase storage egress alone is ~$700/mo vs R2's zero-egress model [5][38], with Levelsio piling on to mock the DB cost [14]. Postiz published its $105K MRR infra: Railway ~$200, R2 ~$160, with X API as the real cost driver at $1000 [22]. Cloudflare R2 had multiple viral moments — 15TB 4K video for $2.18 [25], a resumable file-share pattern using R2+Durable Objects+Turnstile [27], and S3/R2 connector sync demos [23].

On the platform side, a Supabase war-story surfaced a real RLS gap with anonymous sign-in that went unnoticed for 3 weeks [54]. Vercel-related signal was mostly culture/hiring [9][18][45] plus a domain-search engineering post teased [32]. Operational noise around Cloudflare included the unmoderated Discord scam problem [56] and ongoing ADL/deplatforming pressure [2][4]. Stack-choice chatter ('Next.js + Supabase + Stripe' as default) confirmed the studio's stack is mainstream [34][47][49][42].

## Why it matters (reasoning)
For an NDF DEV web project on Next.js + Supabase, the egress finding [38] is the single most actionable signal: Supabase Storage egress can silently dominate the bill once a product has any media/asset volume, while R2 charges nothing for egress. Postbridge is paying ~7x more for storage than for DB. Second-order: if studio apps serve user uploads, video, or even bundled assets through Supabase Storage, the same bill shape will appear at scale. Migrating heavy buckets to R2 (or fronting Supabase Storage with a Cloudflare cache) becomes a cost-control lever, not an optimization.

The Supabase anonymous-auth security hole [54] matters because anon sign-in is often enabled for low-friction onboarding and the RLS policies written for authenticated users frequently miss the anonymous role — exactly the kind of silent bug that hits production weeks later. The Cloudflare Discord scam issue [56] is a small but real ops hygiene note: don't trust DMs/links in that channel. Vercel's 'agent-written code' positioning [18] signals further commoditization of frontend hosting — pricing and DX will stay competitive but lock-in via fluid compute / agent runtimes will tighten.

## Possibility
Likely (70%): R2-as-storage-tier becomes standard advice for any Supabase project with non-trivial media, with community tooling (R2 connectors [23], rclone-style sync) maturing in 3-6 months. Likely (60%): Supabase ships clearer guard-rails or warnings around anonymous-role RLS in response to repeating war stories [54]. Possible (40%): A 'Supabase + R2 storage' adapter or template becomes a recommended pattern, reducing migration cost. Lower probability (25%): Cloudflare's reputational/operational noise [2][4][56] materially affects enterprise procurement; for indie/studio scale it does not. Vercel/Supabase consolidation in the indie stack [34][47][49] entrenches further — switching cost grows.

## Org applicability — NDF DEV
Actionable for NDF DEV web stack:
1. Audit Supabase Storage egress on any production project this week — pull invoice line items; if egress > DB cost, plan migration. Worth it once any bucket carries >50GB/mo of egress.
2. Default media buckets to Cloudflare R2 for new projects; keep Supabase Storage only for small auth-gated artifacts. ROI is immediate at scale [25][38].
3. Review every Supabase project for anonymous sign-in: if enabled, audit RLS policies to ensure the `anon` role is explicitly checked, not just `authenticated` [54]. One-hour task, prevents weeks-of-exposure class of bug.
4. Adopt R2 + Durable Objects pattern [27] for any upload/share features in studio web apps — saves both build time and runtime cost vs rolling on Supabase Storage.
5. Skip the Cloudflare Discord as a support channel [56]; use docs + GitHub issues.
Not worth right now: rebuilding obs/CI tooling around k6/Grafana [20][44] — overkill for current studio scale; revisit when a single product crosses 10k DAU.

## Signals to Watch
- Supabase changelog for any anon-role RLS guard-rail or audit tool
- R2 pricing or free-tier changes (cache hit, Class A/B ops)
- Vercel pricing announcements tied to Fluid/agent runtimes
- Postbridge follow-up post on actual R2 migration numbers — real before/after data

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bodhi3attva | ^7592 c136 | [Government block claim is misleading. Technical checks show: > Domain is on clie](https://x.com/bodhi3attva/status/2058118651505729733) |
| x | LayoffAI | ^2288 c88 | [CHAMATH TO CLOUDFLARE CEO: SHUT THE FUCK UP Literally. He just destroyed him on ](https://x.com/LayoffAI/status/2058558639460192708) |
| x | shortmagsmle | ^1814 c1 | [“No man you don’t get it, my foreign co-founder is REALLY good at using Claude t](https://x.com/shortmagsmle/status/2058156142090506368) |
| x | KiwiFarmsDotNet | ^838 c20 | [Despite deplatforming the Kiwi Farms, 8chan, the Daily Stormer, and other websit](https://x.com/KiwiFarmsDotNet/status/2058609650472218969) |
| x | jackfriks | ^780 c195 | [my solo business @postbridge_ is at $35,000 USD monthly recurring revenue (MRR) ](https://x.com/jackfriks/status/2058198360691998942) |
| x | steipete | ^744 c63 | [Still limited by compute, so I built a thing that runs codex in the cloud, power](https://x.com/steipete/status/2058248513662697622) |
| x | DavidFrosdick | ^720 c59 | [I did it 👍 thanks @levelsio for sharing. Setup @Tailscale on my @Hetzner_Online ](https://x.com/DavidFrosdick/status/2058582571194187819) |
| x | rileybrown | ^584 c77 | [Supabase will likely be worth more than Lovable Replit and Bolt combined when it](https://x.com/rileybrown/status/2058330104988844348) |
| x | evilrabbit_ | ^542 c32 | [I’m about to hit 10 years at Vercel. You can’t imagine the amount of memories I ](https://x.com/evilrabbit_/status/2058205185655423224) |
| x | asonflower | ^406 c28 | [Let's find the path in the first post in my feed today... Nicki Minaj just hijac](https://x.com/asonflower/status/2058156658371477966) |
| x | cramforce | ^309 c12 | [Before joining Vercel, in an effort to escape the Google technology bubble, I wr](https://x.com/cramforce/status/2058650289969025043) |
| x | bayendor | ^255 c8 | [i just asked my Hermes Agent what the 5 most used skills are in our multi-agent ](https://x.com/bayendor/status/2058284935895748880) |
| x | XJosh | ^222 c5 | [@KiwiFarmsDotNet @Cloudflare P.S. @eastdakota has both my account and the Kiwi F](https://x.com/XJosh/status/2058609831565472002) |
| x | levelsio | ^207 c7 | [@jackfriks @postbridge_ @supabase Please let me replace that db with $0 SQLite 😭](https://x.com/levelsio/status/2058206568370295044) |
| x | tech_twi | ^204 c9 | [So 25,000 GHC for a data system fee na Supabase subscription koraa y3 $25. NDC i](https://x.com/tech_twi/status/2058224880647131547) |
| x | RoundtableSpace | ^190 c15 | [SCRAPLING JUST MADE WEB SCRAPING 774X FASTER THAN BEAUTIFULSOUP WHILE BYPASSING ](https://x.com/RoundtableSpace/status/2058129561343463822) |
| x | Hi_Mrinal | ^184 c7 | [I actually love to build my side project using go, etcd, sysbench, toxiproxy, gr](https://x.com/Hi_Mrinal/status/2058557056941248789) |
| x | cramforce | ^177 c23 | [For a company like Vercel it is hard to say things like "100% of code is agent w](https://x.com/cramforce/status/2058549755169636673) |
| x | Mayurasfeathers | ^177 c6 | [#MLBS6SPOILERS the honeycomb pattern on her clothes the bee themed outfit for he](https://x.com/Mayurasfeathers/status/2058451461936189564) |
| x | Akintola_steve | ^167 c10 | [Don’t just learn how to code, Learn tools. For load testing to see how your syst](https://x.com/Akintola_steve/status/2058221171007512795) |
| x | bykarthikreddy | ^165 c3 | [- The website's domain was put on "clientHold" status by its registrar (Hostinge](https://x.com/bykarthikreddy/status/2058154816564781474) |
| x | wickedguro | ^161 c33 | [Postiz is currently on $105k MRR. My infrastructure is actually very cheap: > Ra](https://x.com/wickedguro/status/2058398638653800492) |
| x | yoginth | ^160 c1 | [Shipped S3 and @Cloudflare R2 connector sync + realtime socket updates for https](https://x.com/yoginth/status/2058244142594195855) |
| x | ChrisElliottux | ^155 c21 | [@rauchg Built with Opus 4.6 and 4.7 hosted on Vercel. https://t.co/C4CIa8Nzpt](https://x.com/ChrisElliottux/status/2058294078240903511) |
| x | akinkunmi | ^149 c8 | [Delivering 15TB of 4K video with Cloudflare R2 for $2.18 https://t.co/EErHbKjidz](https://x.com/akinkunmi/status/2058646916779356339) |
| x | swapsk | ^129 c12 | [@openletteryt Clearly can see the domain NS was changed. This us due to Gov repo](https://x.com/swapsk/status/2058204202740990094) |
| x | acoyfellow | ^127 c2 | ["Share": temporary, resumable file transfers on @Cloudflare - Instant share link](https://x.com/acoyfellow/status/2058513529804587492) |
| x | gazeldav | ^127 c103 | [Wild honeycomb harvest from wooden barrel https://t.co/wxn6BdagNJ](https://x.com/gazeldav/status/2058794887424938048) |
| x | N4pstr | ^126 c12 | [just making sure but a cloudflare dns setup should be *good enough* to hide my I](https://x.com/N4pstr/status/2058254124399870319) |
| x | rgbdev | ^123 c1 | [Platform OS &amp; Linux Kernel Troubleshooting Networking Container K8s Cloud IA](https://x.com/rgbdev/status/2058506284761055408) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bodhi3attva</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7592 · 💬 136</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bodhi3attva/status/2058118651505729733">View @bodhi3attva on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Government block claim is misleading. Technical checks show: &gt; Domain is on clientHold status &gt; Public DNS resolvers like Google (8.8.8.8) and Cloudflare (1.1.1.1) now return NXDOMAIN &gt; Website earlie”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Technical DNS forensics shows a domain returning NXDOMAIN on public resolvers with clientHold status — evidence of registrar/hosting suspension, not government blocking as publicly claimed.</dd>
      <dt>Why interesting</dt>
      <dd>Clarifies a critical forensic split: government blocks leave DNS resolving while breaking access at ISP level; clientHold kills DNS entirely — misreading this exposes teams to bad incident diagnoses.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When any studio domain or deployed app goes dark, run DNS checks against 8.8.8.8 and 1.1.1.1 first and confirm registrar status before escalating to hosting or infra — saves hours of wrong-tree debugging.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bodhi3attva/status/2058118651505729733" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LayoffAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2288 · 💬 88</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LayoffAI/status/2058558639460192708">View @LayoffAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“CHAMATH TO CLOUDFLARE CEO: SHUT THE FUCK UP Literally. He just destroyed him on the All-In podcast yesterday. Called his layoff op-ed &quot;from the PR school of retards.&quot; Hard to disagree with him on this”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Chamath Palihapitiya publicly trashed Cloudflare CEO Matthew Prince on the All-In podcast, calling Prince's layoff op-ed empty PR spin.</dd>
      <dt>Why interesting</dt>
      <dd>A top-tier cloud vendor's CEO got publicly humiliated for dressing up a layoff with corporate spin — shows how transparent communication is now table stakes, even at the top.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio ever needs to downsize or restructure, skip the op-ed format entirely — a direct internal announcement beats polished PR every time with a small team.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LayoffAI/status/2058558639460192708" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@shortmagsmle</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1814 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/shortmagsmle/status/2058156142090506368">View @shortmagsmle on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">““No man you don’t get it, my foreign co-founder is REALLY good at using Claude to connect Supabase to Vercel. America will never make it without him! Why, just last week he created a minimalist UI exp”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A satirical post mocking the hype around using Claude to do basic tasks—connecting Supabase to Vercel and building a minimal to-do reminder UI—as if these were rare, indispensable skills.</dd>
      <dt>Why interesting</dt>
      <dd>The joke lands because these are genuinely entry-level tasks—it signals that 'AI-assisted dev' is now so commoditized that anyone can do it, eroding the perceived value of basic integration work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's web stack already uses Next.js + Supabase; the signal here is to stop billing basic Supabase-Vercel wiring as a skill and focus pitch on higher-value work: real-time sync, RLS design, or XR data pipelines.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/shortmagsmle/status/2058156142090506368" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KiwiFarmsDotNet</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 838 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KiwiFarmsDotNet/status/2058609650472218969">View @KiwiFarmsDotNet on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Despite deplatforming the Kiwi Farms, 8chan, the Daily Stormer, and other websites under pressure, @Cloudflare continues to be in the crosshairs of the ADL, which demands more effort to clamp down on ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Cloudflare continues to face ADL pressure to ban more websites, even after already deplatforming Kiwi Farms, 8chan, and the Daily Stormer.</dd>
      <dt>Why interesting</dt>
      <dd>Proves that CDN/DDoS infrastructure providers can terminate service under political pressure with little warning — a real vendor-lock risk for any project.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio must not rely on Cloudflare as a single point of protection. Set up a fallback CDN (e.g. Bunny.net or AWS CloudFront) and document a cutover runbook now, before it's urgent.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KiwiFarmsDotNet/status/2058609650472218969" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jackfriks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 780 · 💬 195</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jackfriks/status/2058198360691998942">View @jackfriks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“my solo business @postbridge_ is at $35,000 USD monthly recurring revenue (MRR) = ±$48,000 CAD for my canadian friends and me here is main breakdown of major costs to run atm - i'm wondering if i shou”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Solo founder of @postbridge_ shares $35K USD MRR with only $1,950/month infra (Supabase $860, Vercel $130, Trigger.dev $400, Unkey $250, X API $250), hitting ~94% gross and ~88% net profit margin.</dd>
      <dt>Why interesting</dt>
      <dd>Real-world proof that a Next.js + Supabase SaaS can scale to $35K MRR with infra under $2K — Supabase is the biggest cost at $860 yet margin stays near 94%.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's web stack is identical (Next.js + Supabase); use this as a cost-scaling benchmark — don't cut infra when margin is healthy, redirect energy to shipping more features faster.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jackfriks/status/2058198360691998942" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 744 · 💬 63</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2058248513662697622">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Still limited by compute, so I built a thing that runs codex in the cloud, powered by @Cloudflare firecracker boxes (and since that's not beefy enough for larger projects, tests are run via crabbox) U”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@steipete built a cloud runner for OpenAI Codex on Cloudflare Firecracker microVMs, routing heavy tests to a separate 'crabbox', with Ghostty terminal running via WebAssembly — and Codex essentially helped build the system itself.</dd>
      <dt>Why interesting</dt>
      <dd>The hybrid compute split — lightweight Firecracker microVMs for interactive tasks, heavier box for tests — is a practical cost-control pattern any small team can clone on Cloudflare or similar infra.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can mirror this in CI: run Next.js lint and quick Unity checks on Firecracker-class microVMs, push full build/test suites to a heavier runner — cuts idle cloud spend and tightens feedback loops.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2058248513662697622" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DavidFrosdick</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 720 · 💬 59</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DavidFrosdick/status/2058582571194187819">View @DavidFrosdick on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I did it 👍 thanks @levelsio for sharing. Setup @Tailscale on my @Hetzner_Online VPS 🙌 Installed @claudeai on VPS 🤞 All my sites run through @Cloudflare tunnels 😎 Got @TermiusHQ running locally on my M”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A non-developer set up a self-hosted VPS workflow using Tailscale, Hetzner, Cloudflare tunnels, and Claude AI, enabling him to code and manage 25GB of projects from his iPhone while out with his family.</dd>
      <dt>Why interesting</dt>
      <dd>The full mobile dev stack — VPS + Tailscale + Cloudflare tunnel + Claude AI + Termius — costs under $20/month and lets a solo operator ship fixes from a phone, no laptop needed.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can mirror this setup for on-call web deployments: Hetzner VPS behind Cloudflare tunnel, Tailscale for secure SSH, Claude AI for in-terminal assistance — letting any team member hotfix Next.js or Supabase issues from a phone.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DavidFrosdick/status/2058582571194187819" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rileybrown</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 584 · 💬 77</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rileybrown/status/2058330104988844348">View @rileybrown on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Supabase will likely be worth more than Lovable Replit and Bolt combined when it’s all said and done.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer predicts Supabase will ultimately be valued higher than Lovable, Replit, and Bolt combined, positioning it as the dominant backend platform.</dd>
      <dt>Why interesting</dt>
      <dd>Supabase is betting on being core infrastructure rather than an AI coding tool, which historically commands higher multiples and stickier enterprise adoption.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio already runs on Next.js + Supabase. Doubling down on Supabase features (Edge Functions, Realtime, Vector) now locks in skills before the platform matures and costs rise.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rileybrown/status/2058330104988844348" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
