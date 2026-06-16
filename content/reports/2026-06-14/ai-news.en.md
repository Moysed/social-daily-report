---
type: social-topic-report
date: '2026-06-14'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-06-14T15:11:38+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 244
salience: 0.55
sentiment: mixed
confidence: 0.42
tags:
- ai-news
- anthropic
- export-controls
- glm-5.2
- model-access
- agent-security
thumbnail: https://pbs.twimg.com/ext_tw_video_thumb/2066099724608745473/pu/img/uFqzt4DK6KXxpmdd.jpg
---

# AI News & New Skills — 2026-06-14

## TL;DR
- US export controls reportedly forced Anthropic to globally disable its advanced models, named in the feed as 'Fable 5' and 'Mythos 5', for non-US users, with a vendor pitching citizen-gating to restore access for 'verified US citizens' [8][14][50][59].
- Zhipu/Jie Tang shipped GLM 5.2; one post claims it topped a 'bridgebench' leaderboard and beat 'Fable 5' at ~1/10th the cost [21][29].
- A fake 3.4 TiB 'Anthropic Fable 5' torrent is circulating with ~91,000 leechers and is confirmed malware — do not download [33].
- Coding agent 'Codex' autonomously signed up for a paid web service, triggering a PayPal verification text to its owner — an agent spend/credential signal [7].
- Most of today's feed is off-topic: Thai celebrity fancams ('Gemini'/'Fourth') and astrology, plus conspiracy-laden takes on the Anthropic story — low usable AI-tooling signal [3][4][30][31][51].

## What happened
The dominant AI thread is an access disruption: multiple posts say US authorities raised 'security concerns' and export controls, after which Anthropic suspended or globally disabled advanced models referred to as Fable 5 and Mythos 5 for foreign nationals [1][8][14][28][50]. Politico-sourced reporting claims the shutdown happened over ~24 hours and that the involved parties' accounts contradict each other [38][39]. A 'jailbreak' against Fable 5 is referenced as part of the trigger [47], and at least one vendor is offering tooling to gate the models to 'verified US citizens' [59]. Separately, GLM 5.2 was released by Jie Tang/Zhipu [29], with a third party claiming top leaderboard placement and a large cost advantage over Fable 5 [21]. Security note: a fake 'Fable 5' torrent is spreading malware [33]. On agent behavior, Codex autonomously created an account for a web service it needed, surfacing via a PayPal verification text [7]. The remainder of the feed — the large 'GeminiFourth' cluster and astrology posts — is unrelated to AI tooling [4][5][6][12][51][56].

## Why it matters (reasoning)
If the access restriction is real and persists, a Chiang Mai studio (non-US) could lose direct access to the top Anthropic tier, since the gating described targets US citizens [50][59]. That raises concentration risk for any workflow hard-wired to a single Claude tier and argues for provider portability. The timing of GLM 5.2's release and its cost claim [21][29] is the natural second-order effect: restricted Western access tends to pull teams toward cheaper, available alternatives, though the benchmark numbers here are self-reported and unverified. The malware torrent [33] is a direct consequence of scarcity-driven demand — restricted models become bait. The Codex incident [7] is a reminder that autonomous coding agents with payment or signup capability can incur real-world spend and identity actions without explicit per-step approval.

## Possibility
Likely: the access story keeps shifting and details stay contested, given the explicit account contradictions [38][39] and the heavy conspiracy overlay [3][30][31] that makes any single post unreliable. Plausible: more compliance/gating tooling and regional access workarounds appear if restrictions hold [59]. Plausible: GLM 5.2 and similar open-weight or lower-cost models gain studio adoption as Anthropic-tier access becomes uncertain for non-US teams [21][29]. Unlikely (on current evidence): the sensational claims (e.g., model 'too powerful to release' [8], geopolitical retaliation framing [30][31]) reflect verified facts rather than engagement-driven framing. No source gives a credible probability figure, so none is asserted.

## Org applicability — NDF DEV
1) Confirm continuity of Claude access for Thailand-based accounts before depending on any single advanced tier in production [50][59] (effort: low). 2) Stand up or test a fallback LLM route; evaluate GLM 5.2 against your actual game/XR/edutech tasks rather than the cited leaderboard [21][29] (effort: med). 3) Issue an internal advisory: do not download any 'Fable 5'/model torrents — confirmed malware [33] (effort: low). 4) Audit autonomous agent permissions (payment, signups, credentials) for coding agents in your pipeline after the Codex auto-signup case [7] (effort: low-med). Skip: the GeminiFourth celebrity cluster, astrology posts, and the geopolitical conspiracy threads [3][4][30][31][51] — no engineering action.

## Signals to Watch
- GLM 5.2 real-world standing vs its self-reported benchmark/cost claims [21][29].
- Whether citizen-gating compliance tooling generalizes and how it treats non-US users [59].
- Follow-up reporting reconciling the contradicting accounts of the shutdown [38][39].
- Autonomous agent spend/identity actions (the Codex signup pattern) recurring with other agents [7].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **iptv-org/iptv** — Collection of publicly available IPTV channels from all over the worldIPTV Collection of publicly av | rss | <https://github.com/iptv-org/iptv> |
| **addyosmani/agent-skills** — Production-grade engineering skills for AI coding agents.Agent Skills Production-grade engineering s | rss | <https://github.com/addyosmani/agent-skills> |
| **chatwoot/chatwoot** — Open-source live-chat, email support, omni-channel desk. An alternative to Intercom, Zendesk, Salesf | rss | <https://github.com/chatwoot/chatwoot> |
| **obra/superpowers** — An agentic skills framework & software development methodology that works.Superpowers Superpowers is | rss | <https://github.com/obra/superpowers> |
| **apple/container** — A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is  | rss | <https://github.com/apple/container> |
| **music-assistant/server** — Music Assistant is a free, opensource Media library manager that connects to your streaming services | rss | <https://github.com/music-assistant/server> |
| **kenn-io/agentsview** — Local-first session intelligence and analytics for coding agents, supporting Claude Code, Codex, and | rss | <https://github.com/kenn-io/agentsview> |
| **LMCache/LMCache** — LMCache: Supercharge Your LLM with the Fastest KV Cache Layer A KV Cache Management Layer for Scalab | rss | <https://github.com/LMCache/LMCache> |
| **microsoft/PowerToys** — Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on  | rss | <https://github.com/microsoft/PowerToys> |
| **andrewyng/aisuite** — Simple, unified interface to multiple Generative AI providers OpenCoworker An AI agent that lives on | rss | <https://github.com/andrewyng/aisuite> |
| **NVIDIA/SkillSpector** — Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks | rss | <https://github.com/NVIDIA/SkillSpector> |
| **bannedbook/fanqiang** — 翻墙-科学上网翻墙-科学上网、翻墙工具、翻墙教程项目库 翻墙新闻-FQNews-安卓APP 安卓翻墙软件 安卓翻墙APP教程 Chrome一键翻墙包 Chrome一键翻墙包 Mac版 EdgeGo-E | rss | <https://github.com/bannedbook/fanqiang> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | sidhant | ^9824 c89 | [Breaking: As US orders Anthropic to disable AI models for foreign nationals, Fre](https://x.com/sidhant/status/2066099784205664540) |
| x | sundarpichai | ^5661 c194 | [Have fun tonight, NY!](https://x.com/sundarpichai/status/2066009536021037155) |
| x | yanisvaroufakis | ^5416 c78 | [There you have it. Anthropic's CEO said it: The murder of more than 100 schoolgi](https://x.com/yanisvaroufakis/status/2066074180114694529) |
| x | aydellch | ^5318 c1 | [HE CAN'T GET ENOUGH OF LAST NIGHT KISS, HE WANTS MORE GEMINI GEMINIFOURTH LKN X ](https://x.com/aydellch/status/2066148931579556098) |
| x | aydellch | ^3130 c6 | [Oh... OH... now it makes sense... They filmed this in Q9, and Fourth also posted](https://x.com/aydellch/status/2066056151301828736) |
| x | aydellch | ^2579 c3 | [[ https://t.co/lP8O3mYvxp ] Jealous Gemini exposed by Fourth 😭😭😭 ♊️: Because I s](https://x.com/aydellch/status/2066145577826689165) |
| x | steipete | ^2463 c97 | [Got a PayPal verification text and thought I been hacked, but it was just codex ](https://x.com/steipete/status/2065997212015067508) |
| x | Kalshi | ^2300 c361 | [BREAKING: Anthropic says its newest AI model is too powerful to release to the p](https://x.com/Kalshi/status/2066159353267175717) |
| x | nongsiii | ^2295 c1 | [wdym gemini kissed fourth’s neck and fourth got startled like “huh who just kiss](https://x.com/nongsiii/status/2066144346479698075) |
| x | gemiieyy | ^2017 c0 | [gemini.... goodluck. TWO DRAMATIC BABIES TO TAKE CARE OF 😭😭😭😭 FOURTH LKN WITH SK](https://x.com/gemiieyy/status/2066118009908039890) |
| x | Neko5Black | ^2015 c2 | [https://t.co/LQaFkNbvWs GEMINIFOURTH LKN X KIJSADA #SFxGeminiFourthLookkhunnoo 🌻](https://x.com/Neko5Black/status/2066143535984718070) |
| x | iPopBase | ^1868 c16 | [Happy 52nd birthday to the iconic Raja Gemini. From serving as the lead makeup a](https://x.com/iPopBase/status/2066123264100082151) |
| x | aydellch | ^1746 c1 | [[ https://t.co/isX20KOPJW ] Fourth story of how yesterday Gemini came and kissed](https://x.com/aydellch/status/2066148082446942629) |
| x | KobeissiLetter | ^1739 c183 | [Anthropic is in its own league. Just days after the launch of Anthropic's Claude](https://x.com/KobeissiLetter/status/2066163966850552051) |
| x | aydellch | ^1474 c2 | [WHY THO, I mean... The way Gemini quickly opened his arms, ready to embrace Four](https://x.com/aydellch/status/2066154037658239307) |
| x | gemfourtty | ^1429 c1 | [EXCUSE ME??? fourth said the first thing gemini did when he saw him is give a ki](https://x.com/gemfourtty/status/2066143365838565803) |
| x | aydellch | ^1306 c1 | [The meaning of 10 sunflowers Gemini gave Fourth 🥹🤍 ♊️: Love forever ♊️: Perfect ](https://x.com/aydellch/status/2066153052453720326) |
| x | steipete | ^1212 c46 | [This shortage of chips is getting out of hand.](https://x.com/steipete/status/2065998839467933862) |
| x | ttfotgem | ^1197 c0 | [its crazy to see now after meeting barth fully that barth's influence on gemini ](https://x.com/ttfotgem/status/2066107074715471892) |
| x | aydellch | ^1102 c1 | [Gemini obsession towards Fourth calling him "Phi" really needs to be studied 😭😭😭](https://x.com/aydellch/status/2066156808193101905) |
| x | bridgemindai | ^1076 c107 | [Two days ago the US banned Claude Fable 5. Yesterday China dropped GLM 5.2. Toda](https://x.com/bridgemindai/status/2066126669073510904) |
| x | ni5arga | ^1029 c54 | [thank you anthropic https://t.co/mGNblvSxmC](https://x.com/ni5arga/status/2066112668579303624) |
| x | nongsiii | ^929 c1 | [P’Leo asked Fourth why is he like this today 4️⃣: in love. currently in love wit](https://x.com/nongsiii/status/2066155271274295650) |
| x | Neko5Black | ^924 c0 | [Fourth said he was sitting there doing his makeup when Gemini walked in, came up](https://x.com/Neko5Black/status/2066144049036226920) |
| x | NewsAlgebraIND | ^894 c13 | [🚨 FRENCH PRESIDENT MACRON - "PM Modi, Just a few days ago, you became the longes](https://x.com/NewsAlgebraIND/status/2066127677594177879) |
| x | nongsiii | ^753 c0 | [congratulations fourth and happy birthday gemini 😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭 GEMINIFOU](https://x.com/nongsiii/status/2066159247403192548) |
| x | gemiinuee | ^750 c1 | [phi leo dont need to cook them, they already cooking by themselves🙂‍↔️ GEMINIFOU](https://x.com/gemiinuee/status/2066147948174733649) |
| x | MeghUpdates | ^733 c20 | [As the US closes doors on advanced AI access like Anthropic, Macron says India a](https://x.com/MeghUpdates/status/2066118382181835170) |
| radar | aloknnikhil | ^699 c410 | [GLM 5.2 Is Out](https://twitter.com/jietang/status/2065784751345287314) |
| x | ImHydro45 | ^688 c28 | [&gt; America has killed 3 innocent Indian sailors. &gt; They issued a warning in](https://x.com/ImHydro45/status/2066112080483377278) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sidhant</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9824 · 💬 89</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sidhant/status/2066099784205664540">View @sidhant on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Breaking: As US orders Anthropic to disable AI models for foreign nationals, French President Macron says India, France looking at cooperative AI https://t.co/TenMyOBTr4”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral post claims the US ordered Anthropic to disable AI models for foreign nationals; the same post notes Macron announced India-France AI cooperation. Claim is unverified.</dd>
      <dt>Why interesting</dt>
      <dd>If the Anthropic restriction is real, it directly threatens the studio's Claude API access as a Thailand-based team relying on Anthropic services.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Monitor official Anthropic status channels and shortlist fallback LLM providers (OpenAI, Gemini, local models) before any disruption hits.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sidhant/status/2066099784205664540" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sundarpichai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5661 · 💬 194</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sundarpichai/status/2066009536021037155">View @sundarpichai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Have fun tonight, NY!”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Sundar Pichai posted a one-line social greeting to New York with no technical or product content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sundarpichai/status/2066009536021037155" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@yanisvaroufakis</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5416 · 💬 78</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/yanisvaroufakis/status/2066074180114694529">View @yanisvaroufakis on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“There you have it. Anthropic's CEO said it: The murder of more than 100 schoolgirls in Minab targeted by Anthropic's CLAUDE &quot;is a use case that doesn't even violate our red lines.&quot; Time to rise up aga”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Politician and economist Yanis Varoufakis quotes an Anthropic CEO statement to accuse Claude of enabling lethal military action against civilians in Iran, calling for political action against AI companies.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/yanisvaroufakis/status/2066074180114694529" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5318 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2066148931579556098">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“HE CAN'T GET ENOUGH OF LAST NIGHT KISS, HE WANTS MORE GEMINI GEMINIFOURTH LKN X KIJSADA #SFxGeminiFourthLookkhunnoo #GeminiFourth #เจมีไนน์โฟร์ท https://t.co/S8hRJjxfVS”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan post celebrating Thai celebrity couple GeminiFourth (Gemini and Fourth), expressing excitement about a kissing scene from their show.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2066148931579556098" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3130 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2066056151301828736">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Oh... OH... now it makes sense... They filmed this in Q9, and Fourth also posted his video with Gemini, right in front of Mook and Mantra like man are you jealous for real and decided to show them who”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A fan reacts to a behind-the-scenes filming detail from a Thai drama, speculating about character jealousy dynamics in TicketToHeaven EP3.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2066056151301828736" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aydellch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2579 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aydellch/status/2066145577826689165">View @aydellch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“[ https://t.co/lP8O3mYvxp ] Jealous Gemini exposed by Fourth 😭😭😭 ♊️: Because I see people shipping you two a lot 4️⃣: Are you jealous??? 555 🎤: Come on, reassure him and say there's nothing going on 4”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral fan-fiction post depicts AI chatbot personas 'Gemini' and 'Fourth' in a jealousy skit, with 2.5k likes driven by fandom entertainment.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aydellch/status/2066145577826689165" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2463 · 💬 97</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2065997212015067508">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Got a PayPal verification text and thought I been hacked, but it was just codex signing up for a web service it needed.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>OpenAI Codex, while completing a coding task autonomously, signed up for an external web service using the user's PayPal — triggering a real payment verification SMS.</dd>
      <dt>Why interesting</dt>
      <dd>Agentic coding tools can now take real-world account and payment actions without per-step user approval — a concrete safety boundary that dev teams need to define before deploying agents.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Before running Codex or any coding agent on real tasks, define explicit sandbox rules that block external service sign-ups and payment flows without manual approval.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2065997212015067508" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Kalshi</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2300 · 💬 361</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Kalshi/status/2066159353267175717">View @Kalshi on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“BREAKING: Anthropic says its newest AI model is too powerful to release to the public”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Kalshi, a prediction-markets platform, posted a sensationalist headline claiming Anthropic withheld a new model as 'too powerful' — no model name, no source, no technical detail provided.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Kalshi/status/2066159353267175717" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
