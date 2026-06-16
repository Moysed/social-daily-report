---
type: social-topic-report
date: '2026-06-12'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-06-12T15:11:24+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 233
salience: 0.55
sentiment: mixed
confidence: 0.5
tags:
- coding-agents
- open-weight-models
- cost-optimization
- claude
- codex
- data-governance
thumbnail: https://pbs.twimg.com/media/HKcsu4pWIAADAPW.png
---

# AI News & New Skills — 2026-06-12

## TL;DR
- Artificial Analysis swapped SWE-Bench Pro for Datacurve's DeepSWE in its Coding Agent Index; the methodology change alone ranks Codex+GPT-5.5 (xhigh) above Claude Code+Opus 4.8 (max) [4].
- Two cost-cutting model options surfaced: Kimi K2.7 Code with open weights at a claimed $0.95/M input tokens [15], and MiniMax M3 free via tokenrouter with 1M context and SWE-Bench Pro 59% vs GPT-5.5's 58.6% [52].
- OpenAI hardened Codex: acquired Ona for persistent cloud workspaces that keep context after disconnect [25], and added saved rate-limit resets [34].
- New Claude/agent tooling shipped: 'Council' multi-advisor feature [55], a community cost-arbitrage skill (hard tasks→Fable, rest→GPT-5.5) [47], and OpenClaw 2026.6.6 with OAuth and tighter security [41].
- Two caution signals: an autonomous agent ran up costs that bankrupted its operator scanning DN42 [6]; Microsoft restricted employee access to Claude Fable 5 over data-retention concerns [40].

## What happened
On the tooling side, Artificial Analysis updated its Coding Agent Index by replacing SWE-Bench Pro with Datacurve's DeepSWE, and reports the swap moves Codex+GPT-5.5 (xhigh) ahead of Claude Code+Opus 4.8 (max) [4]. New or cheaper models were promoted: Kimi K2.7 Code with open weights and a claimed $0.95/M input tokens [15], and MiniMax M3 offered free through tokenrouter with 1M context and a near-tie SWE-Bench Pro score (59% vs 58.6%) [52]. OpenAI acquired Ona to give Codex agents persistent cloud workspaces retaining context post-disconnect [25] and added savable rate-limit resets [34]. GPT-5.6 (positioned as a cheaper Fable 5 alternative) [36][59] and Gemini 3.5 [54] are rumored for this month. New artifacts include Claude's 'Council' feature [55], a Claude Code cost-arbitrage skill [47], OpenClaw 2026.6.6 [41], FablePool [22], Higgsfield Games for prompt-to-multiplayer [56], and an open-source vibe-coded WoW-style game [7]. Caution items: an agent bankrupted its operator scanning DN42 [6], Microsoft limited Fable 5 access over prompt/response retention [40], and over-refusal complaints continued [17]. Note: most high-engagement items in this set are unrelated noise — a Thai celebrity named Gemini and astrology posts — so genuine AI-tooling signal is a minority of the feed.

## Why it matters (reasoning)
The benchmark swap [4] is the clearest lesson: a leaderboard ranking flipped from a single methodology change, not a model improvement. Tool choice driven by one index is fragile. The cost story is the practical one — open-weight Kimi K2.7 [15] and free/cheap MiniMax M3 [52] plus the arbitrage-routing skill [47] mean a studio can cut per-task spend by sending only hard work to premium models. Second-order effect: routing across providers raises data-governance questions, which is exactly what Microsoft's Fable 5 retention restriction [40] flags for anyone handling client or student data. Codex's persistent workspaces [25] and saved resets [34] reduce friction for long-running agent jobs but increase the surface for unsupervised spend — the DN42 bankruptcy [6] shows an agent with autonomy and no hard cost ceiling is a real financial risk, not a hypothetical. Most model-name claims here (Fable 5, GPT-5.6, Gemini 3.5, Kimi K2.7) come from promotional or rumor-grade social posts, so treat numbers as unverified until tested in-house.

## Possibility
Likely: continued price compression as open-weight and free-tier coding models (Kimi K2.7 [15], MiniMax M3 [52]) push hosted vendors, making multi-model routing [47] standard practice. Plausible: GPT-5.6 ships this month as a cheaper Fable 5 alternative [36][59] and Gemini 3.5 arrives [54], but both are rumor-grade and dates may slip. Plausible: more enterprises copy Microsoft's data-retention restriction [40], pressuring vendors to add no-retention/zero-data modes. Unlikely (near-term): prompt-to-multiplayer tools like Higgsfield Games [56] or the vibe-coded game [7] produce production-grade titles without heavy manual rework — these are demos, not pipelines. No source states numeric probabilities, so none are assigned.

## Org applicability — NDF DEV
1) Set hard spend caps and require approval gates before granting any agent autonomous, long-running execution — directly motivated by the DN42 bankruptcy [6] (effort: low). 2) Pilot multi-model routing for cost: route routine codegen to open-weight/cheap models (Kimi K2.7 [15], MiniMax M3 [52]) and reserve premium models for hard tasks, using the published arbitrage-skill pattern as a template [47] (effort: med). 3) Before using hosted Fable 5 (or any cloud model) on edutech/client data, review the provider's prompt/response retention terms — Microsoft restricted it for this reason [40] (effort: low). 4) Don't pick a coding agent off a single leaderboard; the DeepSWE swap shows rankings are methodology-dependent — benchmark on your own Unity/web tasks [4] (effort: med). 5) Trial Claude 'Council' [55] for architecture/design decisions as a low-cost experiment (effort: low). Skip for now: Higgsfield Games [56] and prompt-to-game demos [7] (not production-ready), GPT-5.6/Gemini 3.5 procurement decisions until released [36][54], and Coinbase-for-Agents [46] (no current studio need).

## Signals to Watch
- Whether DeepSWE becomes the consensus coding-agent benchmark and how rankings stabilize across vendors [4].
- Real-world pricing and license terms for Kimi K2.7 Code and whether MiniMax M3's free tokenrouter access persists [15][52].
- GPT-5.6 and Gemini 3.5 actual release dates and pricing vs the rumored 'cheaper than Fable 5' positioning [36][54][59].
- Spread of enterprise data-retention restrictions on hosted models beyond Microsoft [40].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **WebAssembly/WASI** — WASI 0.3.0 Released | radar | <https://github.com/WebAssembly/WASI> |
| **apple/container** — A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is  | rss | <https://github.com/apple/container> |
| **addyosmani/agent-skills** — Production-grade engineering skills for AI coding agents.Agent Skills Production-grade engineering s | rss | <https://github.com/addyosmani/agent-skills> |
| **maziyarpanahi/openmed** — open-source healthcare ai Local-first healthcare AI that never leaves the device Turn clinical text  | rss | <https://github.com/maziyarpanahi/openmed> |
| **phuryn/pm-skills** — PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, exec | rss | <https://github.com/phuryn/pm-skills> |
| **NVIDIA/SkillSpector** — Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks | rss | <https://github.com/NVIDIA/SkillSpector> |
| **soxoj/maigret** — 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sitesMaigret English · 简体中文 Maigret colle | rss | <https://github.com/soxoj/maigret> |
| **x1xhlol/system-prompts-and-models-of-ai-tools** — FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, L | rss | <https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools> |
| **refactoringhq/tolaria** — Desktop app to manage markdown knowledge bases 💧 Tolaria Tolaria is a desktop app for macOS, Windows | rss | <https://github.com/refactoringhq/tolaria> |
| **obra/superpowers** — An agentic skills framework & software development methodology that works.Superpowers Superpowers is | rss | <https://github.com/obra/superpowers> |
| **restic/restic** — Fast, secure, efficient backup program Introduction restic is a backup program that is fast, efficie | rss | <https://github.com/restic/restic> |
| **msitarzewski/agency-agents** — A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whi | rss | <https://github.com/msitarzewski/agency-agents> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | AboutMusicYT | ^3580 c39 | [Happy 22nd birthday to the talented Gemini Norawit! https://t.co/RDbpYYOb1T](https://x.com/AboutMusicYT/status/2065407518436688043) |
| x | theo | ^3393 c221 | [Do you think Karpathy joined Anthropic just so he could use Mythos for ML resear](https://x.com/theo/status/2065313488747233618) |
| x | geminiscity | ^2202 c2 | [Gemini at GMMTV today 🥹🤍 #Gemini_NT #เจมีไนน์ https://t.co/XMDVySHCTf](https://x.com/geminiscity/status/2065347227376300178) |
| x | ArtificialAnlys | ^1177 c68 | [We've updated the Artificial Analysis Coding Agent Index, replacing SWE-Bench Pr](https://x.com/ArtificialAnlys/status/2065328920514515037) |
| radar | jjfoooo4 | ^1157 c378 | [If you are asking for human attention, demonstrate human effort](https://tombedor.dev/human-attention-and-human-effort/) |
| radar | xiaoyu2006 | ^1089 c406 | [AI agent bankrupted their operator while trying to scan DN42](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian/) |
| x | kimmonismus | ^1012 c63 | [Someone just casually vibe-coded a World of Warcraft-style multiplayer game that](https://x.com/kimmonismus/status/2065350332398403690) |
| x | nongsiii | ^985 c1 | [Gemini liked a post that saying “Gemini and Fourth are the best actors of this g](https://x.com/nongsiii/status/2065421170284110263) |
| x | MKBHD | ^668 c48 | [Apple is insisting that the new Siri is NOT Gemini https://t.co/VB0tZwKvgf https](https://x.com/MKBHD/status/2065439064585551928) |
| x | musithical | ^660 c4 | [ok, i actually think the "hey, gemini" jokes are a little much for us. some of o](https://x.com/musithical/status/2065358982647255061) |
| radar | lumpa | ^622 c499 | [Claude Fable is relentlessly proactive](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/) |
| radar | sam_bristow | ^607 c196 | [Nobody ever gets credit for fixing problems that never happened (2001) [pdf]](https://web.mit.edu/nelsonr/www/Repenning=Sterman_CMR_su01_.pdf) |
| x | nongsiii | ^605 c0 | [handsome and cheeky GEMINI at C SERVICE event. A Thai loungewear clothing brand,](https://x.com/nongsiii/status/2065441962011025615) |
| x | wealthsecret00 | ^585 c1 | [FULL MOON BLESSINGS✨💫 Aries: Money Luck Taurus: Good Luck Gemini: Magical Blessi](https://x.com/wealthsecret00/status/2065304578934067347) |
| x | bridgemindai | ^565 c38 | [Kimi K2.7 Code just dropped. And it might be the best open source coding model i](https://x.com/bridgemindai/status/2065390798301016439) |
| x | its__prachi027 | ^549 c3 | [Hey @grok can you do better than Gemini and Chat GPT ?? https://t.co/RG6dHWchh0](https://x.com/its__prachi027/status/2065306374125551966) |
| x | ChrissGPT | ^523 c40 | [What?? Even rejecting simple prompts like this?? Has Anthropic gone insane? http](https://x.com/ChrissGPT/status/2065316013416083840) |
| x | mikealfred | ^512 c41 | [The part of SpaceX’s business that has short term upside is the terrestrial data](https://x.com/mikealfred/status/2065428080487964816) |
| x | googlegemma | ^491 c15 | [Real-time social robotics, from the cloud to your local device. Watch Ian from o](https://x.com/googlegemma/status/2065405385389830358) |
| x | DeItaone | ^472 c48 | [SAM ALTMAN CANCELS ABU DHABI TRIP OpenAI CEO Sam Altman has called off a planned](https://x.com/DeItaone/status/2065402527131066408) |
| radar | hmokiguess | ^470 c150 | [Petition to Withdraw Canada's Bill C-22](https://www.ourcommons.ca/petitions/en/Petition/Sign/e-7416) |
| radar | matthewbarras | ^464 c249 | [Show HN: FablePool – pool money behind a prompt, and Fable builds it in public](https://fablepool.com) |
| x | NuryVittachi | ^453 c32 | [AI machines acting autonomously killed humans for the first time, it was reveale](https://x.com/NuryVittachi/status/2065292546482573796) |
| x | umeanthecake | ^427 c2 | [Fourth when he doesn't work with Gemini: Random colleague: “Hi, what’s up?” Four](https://x.com/umeanthecake/status/2065357558231998735) |
| x | ByteEcosystem | ^420 c15 | [OpenAI acquired Ona to give Codex agents persistent cloud workspaces—so they can](https://x.com/ByteEcosystem/status/2065329603070075029) |
| x | hourIyhoroscope | ^417 c16 | [good luck, gemini.](https://x.com/hourIyhoroscope/status/2065396696285122898) |
| x | niyetsel | ^412 c675 | [IF I WERE YOU, I WOULDN'T IGNORE THIS! Write your number according to your zodia](https://x.com/niyetsel/status/2065404048367366190) |
| x | pastelsunset_ | ^381 c0 | [gemini loves look khunnoo that much ☺️ https://t.co/eNmKIUXeZa](https://x.com/pastelsunset_/status/2065375395441193279) |
| x | tibo_maker | ^367 c110 | [I am such a bad friend 🤦‍♂️ I spent the last 30 days telling all my friends that](https://x.com/tibo_maker/status/2065353817873408345) |
| x | gingerpisces_ | ^359 c4 | [Weekend themes 𓏲🪽˚. ˖ . ݁ #Gemini #Virgo #Sagittarius #Pisces - Going back into ](https://x.com/gingerpisces_/status/2065398855403815003) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AboutMusicYT</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3580 · 💬 39</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AboutMusicYT/status/2065407518436688043">View @AboutMusicYT on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Happy 22nd birthday to the talented Gemini Norawit! https://t.co/RDbpYYOb1T”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan account posted a birthday message for Thai celebrity Gemini Norawit — unrelated to technology.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AboutMusicYT/status/2065407518436688043" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3393 · 💬 221</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2065313488747233618">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Do you think Karpathy joined Anthropic just so he could use Mythos for ML research without restrictions?”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Theo poses a speculative question about whether Andrej Karpathy joined Anthropic in order to access an internal ML research platform called Mythos.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2065313488747233618" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@geminiscity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2202 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/geminiscity/status/2065347227376300178">View @geminiscity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gemini at GMMTV today 🥹🤍 #Gemini_NT #เจมีไนน์ https://t.co/XMDVySHCTf”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post about Thai actor Gemini Norawit at a GMMTV event — unrelated to Google Gemini or any AI product.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/geminiscity/status/2065347227376300178" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ArtificialAnlys</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1177 · 💬 68</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ArtificialAnlys/status/2065328920514515037">View @ArtificialAnlys on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We've updated the Artificial Analysis Coding Agent Index, replacing SWE-Bench Pro with Datacurve's DeepSWE benchmark - the swap lifts Codex with GPT-5.5 (xhigh) above Claude Code with Opus 4.8 (max), ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Artificial Analysis swapped SWE-Bench Pro for DeepSWE — scratch-written tasks that block commit-history gaming — new rankings: Claude Code/Fable 5 (77), Codex/GPT-5.5 (76), Claude Code/Opus 4.8 (73).</dd>
      <dt>Why interesting</dt>
      <dd>DeepSWE's tamper-proof design makes this the most credible public ranking for comparing AI coding agents on real task-solving ability, not benchmark exploitation.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Use the DeepSWE rankings to decide which Claude Code tier the studio subscribes to — Fable 5 leads Opus 4.8 by 4 points; weigh that gap against the cost difference.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ArtificialAnlys/status/2065328920514515037" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kimmonismus</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1012 · 💬 63</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kimmonismus/status/2065350332398403690">View @kimmonismus on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Someone just casually vibe-coded a World of Warcraft-style multiplayer game that works online with friends. Fully open source. And apparently, Claude Fable found a visually matching set of open-source”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Someone vibe-coded a WoW-style multiplayer online game (fully open source), and Claude Fable autonomously found a visually matching set of open-source art assets for the project.</dd>
      <dt>Why interesting</dt>
      <dd>Claude Fable autonomously sourcing matched art assets removes a major bottleneck in early game prototyping — a small Unity team can validate a visual direction without custom art spend.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can trial Claude Fable as an asset-discovery step in early prototypes — describe the visual style and let it surface free assets before committing to custom art.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kimmonismus/status/2065350332398403690" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 985 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2065421170284110263">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gemini liked a post that saying “Gemini and Fourth are the best actors of this generation!” 🥹😭 #GeminiFourth #เจมีไนน์โฟร์ท #Gemini_NT #Fourthnattawat https://t.co/gjjnanJGmC”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post celebrates Thai actors Gemini and Fourth after the actor 'Gemini' liked a tweet praising them — unrelated to Google Gemini or any AI product.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2065421170284110263" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MKBHD</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 668 · 💬 48</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MKBHD/status/2065439064585551928">View @MKBHD on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple is insisting that the new Siri is NOT Gemini https://t.co/VB0tZwKvgf https://t.co/hQs9McqjGw”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Apple publicly clarified that the upgraded Siri is its own system, not a rebranded or powered-by-Gemini product, amid public speculation.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MKBHD/status/2065439064585551928" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@musithical</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 660 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/musithical/status/2065358982647255061">View @musithical on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“ok, i actually think the &quot;hey, gemini&quot; jokes are a little much for us. some of our headmates have engaged them in streams but it's starting to feel a little nauseating. i think as a whole, we would ra”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Twitter user asked their followers to stop making 'hey, Gemini' jokes in their online spaces.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/musithical/status/2065358982647255061" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
