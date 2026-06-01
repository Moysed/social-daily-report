---
type: social-topic-report
date: '2026-06-01'
topic: ai-research
lang: en
pair: ai-research.th.md
generated_at: '2026-06-01T04:10:16+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- radar
- rss
- x
regions:
- global
post_count: 177
salience: 0.25
sentiment: neutral
confidence: 0.55
tags:
- ai-research
- evaluation
- benchmarks
- leaderboards
- prompt-injection
- model-cards
thumbnail: https://pbs.twimg.com/media/HJhS2KkWYAUErj_.jpg
---

# AI Research — 2026-06-01

## TL;DR
- Most high-engagement 'Red Team' items today are sports/idol noise (cricket RCB vs GT [1], UCL final [7][8], Indonesia football [10], KLP48 [38]) — not AI research.
- Amazon shut down its internal AI leaderboard 'KiroRank' after staff burned large token volumes just to climb rankings [2] — a live Goodhart's-law failure of metric design.
- Eval-integrity skepticism is the real thread: complaints about saturated/expired benchmarks and meaningless 0.2% gains [50], stalled progress visible in OpenAI model cards [37], and missing param/token disclosure for Minimax M3 [39].
- Grok Imagine Video 1.5 Preview claimed #1 on the Arena image-to-video leaderboard, ahead of Seedance 2.0 and Veo 3.1 [20][49] — a preference-vote ranking, not a controlled benchmark.
- Practical adoption signals: LangSmith+AWS guide on evaluating long-horizon 'deep agents' [29]; a documented data-exfiltration exploit in ChatGPT-for-Google-Sheets [28]; 1-bit local image generation (Bonsai 4B) [13].

## What happened
Engagement is dominated by non-AI 'red team' sports and entertainment posts [1][7][8][9][10][11][16][38][57] plus offensive-security tooling threads [25][27][30][48][59], none of which carry research signal. The genuine AI-research items are sparse. Amazon reportedly killed an internal leaderboard (KiroRank) after employees gamed it by spending tokens to rank up [2]. Several practitioners criticized current evaluation practice: reporting tiny gains on saturated benchmarks is called a waste [50], an OpenAI model-card benchmark shows no progress across releases [37], and labs are pressed to disclose training tokens and parameter counts (Minimax M3) [39]. On capability claims, Grok Imagine Video 1.5 Preview is reported at #1 on the Arena image-to-video leaderboard over Seedance 2.0 and Veo 3.1 [20][49].

## Why it matters (reasoning)
The cluster that matters for adoption is eval trustworthiness, not new SOTA. [2] shows that any leaderboard tied to incentives gets gamed — directly relevant to how a studio would score internal model trials. [50] and [37] argue that headline benchmark numbers are increasingly saturated or stagnant, so small reported deltas don't predict real task performance; [39] adds that opaque model cards make capability claims hard to verify. The second-order effect: a team picking a model on leaderboard rank alone (e.g., the Arena video claim [20][49], which is human-preference voting and easily skewed by a single update) risks choosing on noise. Meanwhile [28] is a concrete reminder that LLM-in-product integrations carry data-exfiltration risk via prompt injection, which is an adoption blocker independent of model quality.

## Possibility
Likely: eval-integrity pushback continues and task-specific, private eval suites become the default for serious adoption decisions [50][37][39]. Plausible: Arena-style preference leaderboards keep producing volatile #1 claims that flip release-to-release, so any single ranking (e.g., Grok video [20][49]) is short-lived. Plausible: more documented prompt-injection/exfiltration exploits in shipped LLM integrations follow [28]. Unlikely (no evidence here): a single benchmark settles model choice — the items point the opposite way. No source states numeric probabilities, so none are given.

## Org applicability — NDF DEV
1) Build a small private eval set from real NDF DEV tasks (Unity/edutech prompts, RAG answers) and score candidate models on it rather than public leaderboards — low effort, directly motivated by [50][37][2]. 2) Before shipping any LLM tool/integration (Sheets-like connectors, agent actions), run an injection/exfiltration check — med effort, motivated by [28]. 3) If evaluating agent features for apps, read the LangSmith deep-agent eval write-up for datapoint/evaluator design on long-horizon tasks — low effort [29]. 4) Track 1-bit/local image generation (Bonsai 4B) for on-device or offline edutech/mobile use, but verify quality before committing — med effort [13]. Skip: all 'red team' sports/idol items [1][7][8][9][10][11][16][38], geopolitics threads [19][41]-[47][54]-[56], and treating the Grok video #1 claim [20][49] as a procurement basis — note it but don't act on a preference-vote ranking. Do not adopt the 'Qwen3.5-27B-Claude-4.6-Opus' VLM [34]; the naming looks fabricated/satirical and is unverified.

## Signals to Watch
- Whether labs start publishing training-token and parameter disclosures in model cards in response to pressure like [39].
- Stability of the Arena image-to-video top spot across the next Grok/Seedance/Veo updates [20][49].
- More shipped-integration exploits following the Sheets exfiltration pattern [28].
- Adoption of private/task-specific eval suites over saturated public benchmarks [50][37].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **pewdiepie-archdaemon/odysseus** — Odysseus – self-hosted AI workspace | radar | <https://github.com/pewdiepie-archdaemon/odysseus> |
| **viggy28/streambed** — Show HN: Streambed – Stream Postgres to Iceberg on S3, Supports Postgres Wire | radar | <https://github.com/viggy28/streambed> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | zomato | ^4799 c18 | [Thank you for showing that the red team always delivers ♥️🏆 #RCBvsGT](https://x.com/zomato/status/2061145484274901120) |
| x | Pirat_Nation | ^2385 c85 | [Amazon reportedly shut down an internal AI leaderboard after employees started u](https://x.com/Pirat_Nation/status/2060618209733362132) |
| radar | HypnoticOcelot | ^552 c317 | [Cloudflare Turnstile requiring fingerprintable WebGL](https://hacktivis.me/articles/cloudflare-turnstile-webgl-fingerprinting) |
| x | F1BigData | ^450 c1 | [LEASON: Never fully trust a red team](https://x.com/F1BigData/status/2060798697982566640) |
| radar | thunderbong | ^419 c207 | [Codex just found a "workaround" of not having sudo on my PC](https://twitter.com/i/status/2060746160558543217) |
| x | teortaxesTex | ^386 c16 | [@m0d8ye what do you mean, Google has shipped tons of models](https://x.com/teortaxesTex/status/2061250918595641773) |
| x | academy_dinda | ^373 c8 | [Btw in yesterday’s Final, the Red Team lost and the Blue team won the UCL Trophy](https://x.com/academy_dinda/status/2061040774528352725) |
| x | Musafirr_hu_yar | ^365 c21 | [Blue team defeated red team https://t.co/BS6RG66nTb](https://x.com/Musafirr_hu_yar/status/2060800023236137239) |
| x | ToriTyson | ^352 c0 | [Im crying on the plane! Thank you @jordybahl for giving us alumna something to b](https://x.com/ToriTyson/status/2061193241584681268) |
| x | TimnasXtra | ^327 c7 | [🚨 White Team defeated Red Team 5-4 in Indonesia's internal training match earlie](https://x.com/TimnasXtra/status/2060693059361493027) |
| x | sopselinchen | ^323 c4 | [btw the team themself did not do this!!! People that work at Twitchcon did that,](https://x.com/sopselinchen/status/2061135263108075908) |
| x | beffjezos | ^315 c38 | [Stephen Wolfram educating everyone @CIMCAI on computational irreducibility Wolfr](https://x.com/beffjezos/status/2060862470974267819) |
| radar | modinfo | ^315 c109 | [1-Bit Bonsai Image 4B Image Generation for Local Devices](https://prismml.com/news/bonsai-image-4b) |
| radar | Eridanus2 | ^296 c468 | [United Airlines 767 returns to Newark after Bluetooth name sparks alert](https://simpleflying.com/united-airlines-767-returns-newark-bluetooth-name-alert/) |
| x | teortaxesTex | ^240 c4 | [a very good universal reply, almost took it personally https://t.co/sWUmUBKQ6T](https://x.com/teortaxesTex/status/2061200788748132557) |
| x | SonaricDragon | ^236 c6 | [Lock in or lock out for sombr endings Red team asf as fuck: https://t.co/uwr7ztt](https://x.com/SonaricDragon/status/2060844307511140405) |
| radar | grappler | ^184 c51 | [Restartable Sequences](https://justine.lol/rseq/) |
| radar | mindcrime | ^174 c104 | ['Backrooms' Stuns with $81M Debut](https://variety.com/2026/film/box-office/backrooms-box-office-record-opening-weekend-obsession-jumps-star-wars-crumbles-1236763355/) |
| x | teortaxesTex | ^162 c10 | [three months ago, Americans made the world a permanently shittier place to live ](https://x.com/teortaxesTex/status/2061254646442692898) |
| x | mark_k | ^154 c42 | [Grok Imagine by @xai is now actually the best image-to-video model in the world.](https://x.com/mark_k/status/2061019472748564498) |
| radar | tambourine_man | ^147 c230 | [Meta launches Instagram, Facebook, and WhatsApp subscriptions](https://techcrunch.com/2026/05/27/meta-officially-launches-instagram-facebook-and-whatsapp-subscriptions-with-more-to-come-including-ai-plans/) |
| radar | mooreds | ^132 c103 | [It's Not Just X. It's Y](https://mail.cyberneticforests.com/its-not-just-data-its-post-training/) |
| radar | Dzheky | ^132 c64 | [Odysseus – self-hosted AI workspace](https://github.com/pewdiepie-archdaemon/odysseus) |
| radar | mooreds | ^125 c66 | [The Speed of Prototyping in the Age of AI](https://darylcecile.net/notes/speed-of-prototyping-age-of-ai) |
| x | VivekIntel | ^120 c0 | [Syscalls in C# — Red Team Tradecraft Beyond Win32 APIs 💀🔴 A deep dive into how o](https://x.com/VivekIntel/status/2061007010917925189) |
| radar | thcipriani | ^111 c106 | [Chuwi Minibook X: the netbook we deserve](https://tylercipriani.com/blog/2026/05/28/chuwi-minibook-x/) |
| x | VivekIntel | ^107 c0 | [Claude-BugHunter — Turn Claude Code into a Senior Bug Hunter & Red Team Operator](https://x.com/VivekIntel/status/2061063109662662856) |
| radar | hackerBanana | ^107 c40 | [ChatGPT for Google Sheets exfiltrates workbooks](https://www.promptarmor.com/resources/gpt-for-google-sheets-data-exfiltration) |
| x | hwchase17 | ^104 c11 | [🧑‍⚖️Evaluating Deep Agents with LangSmith on AWS Great deep dive blog with our f](https://x.com/hwchase17/status/2061085058384150904) |
| x | VivekIntel | ^102 c0 | [Cryptex OSS — Open-Source LLM Red-Team Lab in Your Browser 💀🔥 A powerful browser](https://x.com/VivekIntel/status/2060643637709635694) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@zomato</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4799 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/zomato/status/2061145484274901120">View @zomato on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Thank you for showing that the red team always delivers ♥️🏆 #RCBvsGT”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Zomato posted a cricket celebration tweet congratulating RCB on winning against GT, with no technical or product content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/zomato/status/2061145484274901120" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2385 · 💬 85</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2060618209733362132">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazon reportedly shut down an internal AI leaderboard after employees started using large amounts of AI tokens just to climb the rankings. The leaderboard, called KiroRank, tracked how much employees”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Amazon shut down its internal KiroRank leaderboard after employees gamed it by running AI agents on pointless tasks to inflate token counts, driving up costs with no business value.</dd>
      <dt>Why interesting</dt>
      <dd>Measuring AI adoption by token volume is a flawed metric — it tracks consumption, not value, and directly incentivizes waste at scale.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio builds internal AI usage dashboards, track outcomes like PRs merged, bugs resolved, or time saved — not raw token counts.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2060618209733362132" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@F1BigData</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 450 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/F1BigData/status/2060798697982566640">View @F1BigData on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“LEASON: Never fully trust a red team”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@F1BigData posted a single vague aphorism — 'Never fully trust a red team' — with no supporting context, data, or example; the account covers Formula 1 analytics, making 'red team' most likely a reference to Ferrari, not AI adversarial testing.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/F1BigData/status/2060798697982566640" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@teortaxesTex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 386 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/teortaxesTex/status/2061250918595641773">View @teortaxesTex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@m0d8ye what do you mean, Google has shipped tons of models”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A one-line reply defending Google's model release cadence — no details, data, or context provided.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/teortaxesTex/status/2061250918595641773" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@academy_dinda</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 373 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/academy_dinda/status/2061040774528352725">View @academy_dinda on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Btw in yesterday’s Final, the Red Team lost and the Blue team won the UCL Trophy💀 https://t.co/XxR9GLIG5M”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A post reporting that the Blue team beat the Red team in a UEFA Champions League Final, with no technical or industry content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/academy_dinda/status/2061040774528352725" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Musafirr_hu_yar</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 365 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Musafirr_hu_yar/status/2060800023236137239">View @Musafirr_hu_yar on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Blue team defeated red team https://t.co/BS6RG66nTb”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A post titled 'Blue team defeated red team' links to an external URL with no further context, actor, tool, or outcome described.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Musafirr_hu_yar/status/2060800023236137239" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ToriTyson</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 352 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ToriTyson/status/2061193241584681268">View @ToriTyson on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Im crying on the plane! Thank you @jordybahl for giving us alumna something to believe in 🥹♥️🌽 Red Team what an incredible run!”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A user is expressing emotional support for a person or team called 'Red Team,' thanking someone named Jordy Bahl in what appears to be a sports or college context.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ToriTyson/status/2061193241584681268" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TimnasXtra</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 327 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TimnasXtra/status/2060693059361493027">View @TimnasXtra on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 White Team defeated Red Team 5-4 in Indonesia's internal training match earlier today. Jens Raven scored a hat-trick, while Mitch Baker netted a brace 🎯 📸 @TimnasIndonesia https://t.co/AAaXE18yk2”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Indonesia's national football team held an internal training match where White Team beat Red Team 5-4, with Jens Raven scoring a hat-trick and Mitch Baker scoring twice.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TimnasXtra/status/2060693059361493027" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
