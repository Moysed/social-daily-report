---
type: social-topic-report
date: '2026-05-26'
topic: devops-cloud
lang: en
pair: devops-cloud.th.md
generated_at: '2026-05-26T03:44:10+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- x
regions:
- global
post_count: 74
salience: 0.78
sentiment: mixed
confidence: 0.72
tags:
- cloudflare
- supabase
- vercel
- r2
- observability
- nextjs
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2058393861454704641/img/m9G5-lqTmvZFDG8Q.jpg
---

# DevOps & Cloud — 2026-05-26

## TL;DR
- Cloudflare dominates today's chatter — mix of CEO drama [1], R2 cost wins ($2.18 for 15TB egress [11], Postiz $160/mo [16]), and operational papercuts (Discord scams [37], D1 caveats [23])
- Supabase signal is split: pgmq + cron + edge functions = real queue stack [17]; but anon sign-in security gotcha [39] and support outage complaints [32] are real risk markers
- Vercel AI Gateway gaining production traction (150M tokens/mo at Notra [56]) but missing model coverage [42]; cramforce says ~all Vercel code is now agent-written [13]
- Recurring war story: OAuth + Vercel config + 3rd-party DB = 6hr/15 deploy debugging hell [33] — config drift between local/preview/prod still the top time sink
- Stack consensus is ossifying around Next.js + Supabase + Stripe + Cloudflare [7][12][35][36] — this is now NDF DEV's exact lane, not a bet

## What happened
Cloudflare-heavy day. R2 keeps winning on egress economics — one creator delivered 15TB of 4K for $2.18 [11], Postiz runs storage at $160/mo on $105k MRR [16]. On the negative side, the CEO's layoff op-ed got publicly trashed [1], the official Discord is full of unmoderated crypto scams [37], and a Cloudflare engineer publicly warned against D1 for real projects, recommending Postgres day one [23]. Supabase had a meaningful product note — pgmq queues + cron + edge functions form a usable async pipeline without external infra [17] — but also a public support failure thread [32] and a war story about anonymous sign-in opening a 3-week security hole [39].

Vercel signals: AI Gateway is being adopted at scale (Notra: 150M tokens/mo [56]) but devs complain key models (e.g. seedance) are missing [42]; Malte Ubl claims essentially no Vercel employee hand-writes code anymore [13]. Background noise: the indie/vibe-coder stack has converged on Next.js + Supabase + Stripe + Cloudflare/Vercel [7][12][35][36], and one painful 6-hour OAuth/Vercel/Hono/Turso debug thread [33] reinforces that config-drift across preview/prod is still the dominant outage class.

## Why it matters (reasoning)
For a Next.js + Supabase shop, three things compound: (1) R2's egress pricing is now a defensible cost lever for any media-heavy edutech or XR asset delivery — moving large MP4/GLB/asset bundles off Vercel/Supabase storage to R2 is a near-free win [11][16]. (2) Supabase pgmq + cron means you can kill a separate worker service (BullMQ/Redis/Inngest) for low-volume background jobs — fewer moving parts, fewer 3am pages [17]. (3) The anon-signin security pattern [39] is a direct RLS-policy threat: any 'guest mode' UX in Unity WebGL builds or e-learning trials needs an RLS audit because anon users share the authenticated role and policies often forget to filter on is_anonymous. Second-order: as the stack ossifies, hiring/onboarding gets cheaper (every junior knows it) but vendor lock-in deepens — Supabase support outages [32] and Vercel config quirks [33] become single points of failure with no easy escape hatch.

## Possibility
Likely (70%): Supabase ships more pgmq tooling and positions queues as a first-class primitive within 6 months — kills the 'do I need Inngest?' question for small teams. Likely (60%): Cloudflare R2 + Workers continues eating Vercel egress/image-CDN bills; hybrid deploys (Next.js on Vercel, assets+API edges on Cloudflare) become normal. Possible (40%): a high-profile Supabase RLS breach forces a default-deny posture change for anon sessions. Lower (20%): Vercel responds to AI Gateway gaps by adding direct model partnerships, but won't match OpenRouter breadth. Watch for D1 vs Postgres positioning — Cloudflare's own people now steering people away [23] suggests D1 stays niche.

## Org applicability — NDF DEV
Concrete moves for NDF DEV: (1) Audit all Supabase projects with anonymous sign-in enabled — every RLS policy must check `auth.jwt()->>'is_anonymous' = 'false'` where appropriate. Half-day task, prevents a [39]-style incident. Worth it: yes, urgent. (2) Move Unity WebGL builds, XR asset bundles, and e-learning video to Cloudflare R2 with a Worker in front — cuts Vercel bandwidth bills 80-95% on any media-heavy project [11][16]. Worth it: yes, ~1 day setup per project. (3) Replace any ad-hoc background job code (email sends, report generation, AI batch jobs) with Supabase pgmq + pg_cron + edge functions [17] — removes Inngest/Trigger.dev dependency for the HR page, employee page, NDF site. Worth it: yes for new work, not worth retrofitting stable systems. (4) Standardize a preview/prod env-var checklist to avoid [33]-style OAuth/redirect-URL drift — small ops doc, big page-prevention. (5) Skip Vercel AI Gateway for now if you need non-mainstream models [42]; OpenRouter remains broader. Skip D1 entirely — stay on Supabase Postgres [23].

## Signals to Watch
- Supabase pgmq adoption + tooling cadence over next 2 quarters — does it get a dashboard UI worth using
- Cloudflare R2 + Vercel hybrid deploy patterns / official guides appearing
- Any public Supabase RLS breach involving anonymous sessions — would force policy template changes
- Vercel AI Gateway model catalog growth vs OpenRouter parity

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | LayoffAI | ^2340 c89 | [CHAMATH TO CLOUDFLARE CEO: SHUT THE FUCK UP Literally. He just destroyed him on ](https://x.com/LayoffAI/status/2058558639460192708) |
| x | gazeldav | ^1416 c620 | [Wild honeycomb harvest from wooden barrel https://t.co/wxn6BdagNJ](https://x.com/gazeldav/status/2058794887424938048) |
| x | KiwiFarmsDotNet | ^921 c20 | [Despite deplatforming the Kiwi Farms, 8chan, the Daily Stormer, and other websit](https://x.com/KiwiFarmsDotNet/status/2058609650472218969) |
| x | DavidFrosdick | ^918 c77 | [I did it 👍 thanks @levelsio for sharing. Setup @Tailscale on my @Hetzner_Online ](https://x.com/DavidFrosdick/status/2058582571194187819) |
| x | cramforce | ^422 c14 | [Before joining Vercel, in an effort to escape the Google technology bubble, I wr](https://x.com/cramforce/status/2058650289969025043) |
| x | ritu_twts | ^327 c173 | [Why do vibe coders always choose Supabase as the backend? There are so many othe](https://x.com/ritu_twts/status/2058746026438324599) |
| x | lagerskoy | ^282 c19 | [2025 app stack is getting ridiculous. One guy with: • Rork • Claude Opus 4.5 • S](https://x.com/lagerskoy/status/2058953143061536980) |
| x | sukh_saroy | ^230 c9 | [10 GITHUB REPOS THAT REPLACE AN ENTIRE TECH STACK. Each one kills a category. Sa](https://x.com/sukh_saroy/status/2058855918922776962) |
| x | haydenbleasel | ^207 c13 | [Files SDK v1.6 is out! By far our biggest release - this one is all about observ](https://x.com/haydenbleasel/status/2058955821602811957) |
| x | Hi_Mrinal | ^200 c8 | [I actually love to build my side project using go, etcd, sysbench, toxiproxy, gr](https://x.com/Hi_Mrinal/status/2058557056941248789) |
| x | akinkunmi | ^195 c9 | [Delivering 15TB of 4K video with Cloudflare R2 for $2.18 https://t.co/EErHbKjidz](https://x.com/akinkunmi/status/2058646916779356339) |
| x | trikcode | ^195 c65 | [Every indie hacker has the same stack now: Next.js, Supabase, Stripe, and 4 AI s](https://x.com/trikcode/status/2058780836984406283) |
| x | cramforce | ^183 c23 | [For a company like Vercel it is hard to say things like "100% of code is agent w](https://x.com/cramforce/status/2058549755169636673) |
| x | Mayurasfeathers | ^179 c6 | [#MLBS6SPOILERS the honeycomb pattern on her clothes the bee themed outfit for he](https://x.com/Mayurasfeathers/status/2058451461936189564) |
| x | LottieFiles | ^171 c12 | [GitHub READMEs are mostly static badges and screenshots. Last week we animated l](https://x.com/LottieFiles/status/2058863785214194104) |
| x | wickedguro | ^161 c33 | [Postiz is currently on $105k MRR. My infrastructure is actually very cheap: > Ra](https://x.com/wickedguro/status/2058398638653800492) |
| x | dshukertjr | ^140 c13 | [Supabase offers a DB, auth, storage, edge functions, but did you know it also ha](https://x.com/dshukertjr/status/2058891280126759298) |
| x | rgbdev | ^140 c1 | [Platform OS &amp; Linux Kernel Troubleshooting Networking Container K8s Cloud IA](https://x.com/rgbdev/status/2058506284761055408) |
| x | acoyfellow | ^132 c2 | ["Share": temporary, resumable file transfers on @Cloudflare - Instant share link](https://x.com/acoyfellow/status/2058513529804587492) |
| x | rohit4verse | ^120 c18 | [Riley brown(@rileybrown) shipped 6 live products in one codex session. solo. mos](https://x.com/rohit4verse/status/2058634403858063653) |
| x | 0chibo_ | ^118 c8 | [Msisahau pia yule expat wa: “Geofencing the location with the Cloudflare option”](https://x.com/0chibo_/status/2058906746370818198) |
| x | kemsdesigns | ^105 c13 | [From figma - antigravity - github - vercel. I recently challenged myself to desi](https://x.com/kemsdesigns/status/2058615261641703526) |
| x | CherryJimbo | ^104 c6 | [This is a great technical writeup. Cloudflare D1 is great for tech demos, but I'](https://x.com/CherryJimbo/status/2059026558933749878) |
| x | DamiDefi | ^104 c5 | [ReAct loops, context engineering, memory systems, guardrails, multi-agent coordi](https://x.com/DamiDefi/status/2058946704565743721) |
| x | mksglu | ^102 c8 | [context-mode keeps raw tool output out of your AI agent's context window. 🫡 98% ](https://x.com/mksglu/status/2058550509481480658) |
| x | mmmatt | ^97 c10 | [constant work is what a MM is, we're profiting now, and not getting 429's or IP ](https://x.com/mmmatt/status/2058519048137121960) |
| x | malagojr | ^97 c14 | [- Linux is free. - Docker is free. - Kubernetes is free. - Git and Github are fr](https://x.com/malagojr/status/2058826893520937227) |
| x | kieralwellness | ^96 c2 | [Top Tier Food List Steak tartare Carpaccio Bone marrow Pomegranate Short ribs Fr](https://x.com/kieralwellness/status/2058712006509928678) |
| x | SakshiSugandhi | ^88 c43 | [Database Systems and their Country of Origin • Oracle DB - 🇺🇸 United States • Po](https://x.com/SakshiSugandhi/status/2058534206775681061) |
| x | StatsGH | ^77 c30 | [DM I need a React developer with Vercel deployment experience.](https://x.com/StatsGH/status/2058690132245446820) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LayoffAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2340 · 💬 89</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LayoffAI/status/2058558639460192708">View @LayoffAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“CHAMATH TO CLOUDFLARE CEO: SHUT THE FUCK UP Literally. He just destroyed him on the All-In podcast yesterday. Called his layoff op-ed &quot;from the PR school of retards.&quot; Hard to disagree with him on this”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Chamath Palihapitiya publicly attacked Cloudflare CEO Matthew Prince on the All-In podcast, calling his layoff op-ed dishonest PR spin.</dd>
      <dt>Why interesting</dt>
      <dd>Tech leaders face real reputational risk when layoff communications read as performative — the podcast clipped and went viral fast, showing how quickly narrative control collapses.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio ever downsizes or restructures, communicate directly and factually — no op-ed-style framing. This incident is a clear case study in what not to do.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LayoffAI/status/2058558639460192708" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gazeldav</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1416 · 💬 620</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gazeldav/status/2058794887424938048">View @gazeldav on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wild honeycomb harvest from wooden barrel https://t.co/wxn6BdagNJ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A video of wild honeycomb being harvested from a wooden barrel.</dd>
      <dt>Why interesting</dt>
      <dd>Not technically interesting — viral nature content misclassified under DevOps &amp; Cloud topic.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gazeldav/status/2058794887424938048" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KiwiFarmsDotNet</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 921 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KiwiFarmsDotNet/status/2058609650472218969">View @KiwiFarmsDotNet on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Despite deplatforming the Kiwi Farms, 8chan, the Daily Stormer, and other websites under pressure, @Cloudflare continues to be in the crosshairs of the ADL, which demands more effort to clamp down on ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Cloudflare faces ongoing pressure from the ADL to deplatform more sites, even after already terminating services for Kiwi Farms, 8chan, and the Daily Stormer.</dd>
      <dt>Why interesting</dt>
      <dd>Cloudflare's willingness to cut CDN/DDoS protection under advocacy pressure shows infrastructure providers are not politically neutral — a risk for any project depending on them.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should document fallback CDN/DDoS options (e.g., Bunny.net, AWS CloudFront) for web stack projects so a sudden Cloudflare policy action does not cause unplanned downtime.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KiwiFarmsDotNet/status/2058609650472218969" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DavidFrosdick</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 918 · 💬 77</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DavidFrosdick/status/2058582571194187819">View @DavidFrosdick on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I did it 👍 thanks @levelsio for sharing. Setup @Tailscale on my @Hetzner_Online VPS 🙌 Installed @claudeai on VPS 🤞 All my sites run through @Cloudflare tunnels 😎 Got @TermiusHQ running locally on my M”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A non-coder set up a full self-hosted dev environment on a Hetzner VPS using Tailscale, Cloudflare tunnels, and Termius, then migrated 25 GB of projects and coded from his iPhone while grocery shopping.</dd>
      <dt>Why interesting</dt>
      <dd>The Tailscale + Cloudflare tunnel + locked-ports combo gives a zero-trust VPS setup that's production-safe and fully mobile-accessible — no public SSH port exposed.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can mirror this stack — Tailscale mesh between devs, Cloudflare tunnels for staging sites, and Termius for on-call fixes — cutting the need to be at a desk for minor deploys or hotfixes.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DavidFrosdick/status/2058582571194187819" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cramforce</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 422 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cramforce/status/2058650289969025043">View @cramforce on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Before joining Vercel, in an effort to escape the Google technology bubble, I wrote my home automation system from scratch. Not a fork of home assistant: pure hand-crafted from-scratch trad-software. ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Vercel engineer's self-hosted home automation stack (Node 14, Next.js 11, k8s, Helm, InfluxDB) bit-rotted to undeployable, then Codex modernized the entire codebase in 3 prompts.</dd>
      <dt>Why interesting</dt>
      <dd>AI-assisted modernization can rescue a fully broken, multi-dependency legacy stack in minutes — the bottleneck is no longer technical debt accumulation but simply knowing when to run the tool.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio has legacy Unity and web projects with outdated dependencies — run Codex or Claude on the most neglected repos to batch-upgrade Node versions, packages, and config before they become undeployable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cramforce/status/2058650289969025043" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ritu_twts</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 327 · 💬 173</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ritu_twts/status/2058746026438324599">View @ritu_twts on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Why do vibe coders always choose Supabase as the backend? There are so many other options right? https://t.co/Ss50xaCL2R”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>The post asks why 'vibe coders' (AI-assisted, low-friction devs) consistently default to Supabase as their backend despite many alternatives existing.</dd>
      <dt>Why interesting</dt>
      <dd>Supabase has captured the 'default choice' mindset among fast-moving devs — meaning its DX and ecosystem friction is low enough to win without a formal evaluation process.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's web stack already runs on Supabase — this validates the choice. Invest deeper into its ecosystem (Edge Functions, Realtime, RLS policies) rather than evaluating alternatives for new projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ritu_twts/status/2058746026438324599" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@lagerskoy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 282 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/lagerskoy/status/2058953143061536980">View @lagerskoy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“2025 app stack is getting ridiculous. One guy with: • Rork • Claude Opus 4.5 • Supabase • Stripe can ship a real mobile app in days for ~$200 total. The barrier isn't coding anymore. It's taste, distr”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A solo developer can now ship a real mobile app in days for ~$200 using Rork, Claude Opus 4.5, Supabase, and Stripe — the bottleneck is no longer coding but taste, distribution, and persistence.</dd>
      <dt>Why interesting</dt>
      <dd>The $200 solo-ship stack validates that AI-assisted tooling has collapsed MVP cost to near-zero, meaning small studios now compete directly with well-funded teams on speed-to-market.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio already runs Supabase on the web stack; adding Rork as a rapid mobile prototyping layer lets the team validate mobile ideas before committing Unity or XR resources to a full build.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/lagerskoy/status/2058953143061536980" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sukh_saroy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 230 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sukh_saroy/status/2058855918922776962">View @sukh_saroy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“10 GITHUB REPOS THAT REPLACE AN ENTIRE TECH STACK. Each one kills a category. Save this. 1. Supabase Open source Firebase. Postgres database, auth, storage, edge functions, real-time subscriptions, al”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A curated list of 10 open-source GitHub repos (Supabase, Appsmith, Documenso, Chatwoot, Crowdsec, Formbricks, and more) that self-hosted replace expensive SaaS tools like Firebase, Retool, DocuSign, Intercom, and Cloudflare WAF.</dd>
      <dt>Why interesting</dt>
      <dd>A small studio can eliminate $1,500+/month in SaaS subscriptions by self-hosting these tools — real savings with production-grade replacements, not compromises.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio already uses Supabase — the remaining tools like Appsmith for internal dashboards, Chatwoot for client comms, and Documenso for contract signing are direct drop-ins worth evaluating now.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sukh_saroy/status/2058855918922776962" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
