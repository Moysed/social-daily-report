---
type: social-topic-report
date: '2026-10-05'
topic: ai-devtools
lang: en
pair: ai-devtools.th.md
generated_at: '2026-10-05T03:03:11+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- radar
- rss
- x
regions:
- global
post_count: 298
salience: 0.8
sentiment: mixed
confidence: 0.6
tags:
- coding-agents
- codex
- claude-code
- mcp
- llm-pricing
- agent-skills
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2106830674204225536/img/h01uRHVmbSoGNL-t.jpg
---

# AI Devtools — 2026-10-05

## TL;DR
- OpenAI's Codex lead says that for the next 28 days Codex will ship either one clear improvement or one usage-limit reset every day [1][4]. Commentators read it as a move to stop users leaving for Claude [18], and some say it rewards burning quota while hoping for a reset day [20].
- OpenAI is reported to be merging Chat, Work and Codex [54]. The Codex lead also said the model picker is likely going away [32]. A Plus-tier user reports that GPT-6 Astra Light uses up the 5-hour Codex window quickly [37].
- Codex's computer-use feature runs as a local MCP server inside the ChatGPT Mac app. A user shows Claude Code calling it, including headless with `claude -p`, and driving Codex's Chrome extension [13][44].
- Cline paused its free DeepSeek-V4.1-Flash promotion because of abuse [29]. Ling 3.1 Flash (a 560B mixture-of-experts model with 25B active parameters) is free in Cline until October 13 [53].
- Claude Code 2.1.289 shipped 27 CLI changes, including a shared `agent.spawn` for teammates [51]. Separately, a Show HN repo claims Qwen 3.8 Flash Next (125B) runs at 100 tokens/s on one RTX 4090 [34].

## What happened
The highest-engagement item is OpenAI's 28-day Codex plan: each day brings either an improvement relevant to most Codex/Work users or a full usage reset [1][4]. Reactions describe it as a retention move after a thin DevDay [18] and complain that it turns quota into a lottery [20]. In an interview, the head of ChatGPT and Codex said the model picker is likely going away and that 'loops and graphs are a passing phase' [32]. Users report Chat, Work and Codex will be merged [54]. On the Anthropic side, Claude Code 2.1.289 shipped with agent-spawning changes [51]. A widely shared critique says Anthropic has the best code models but they are slow and expensive, and that the $200 subscription limits are easy to exhaust [6].

On tooling: one user shows Codex's computer-use MCP server being called from Claude Code [13][44]. T3 Code (nightly) markets a bring-your-own-agent desktop app that works with Claude, Codex and OpenCode [39][41][42]. Several agent-skill and memory repos are trending: addyosmani/agent-skills [59], book-to-skill [31], claude-mem [35], ponytail [10] and impeccable [14]. Other items: mixie3D gives agents direct control of Blender instead of simulated UI clicks [49]; a desktop database client ships a built-in MCP server [27]; tester-army/e2e offers an end-to-end testing framework for web and mobile [58]. On cost and security: Cline pulled a free model promotion over abuse [29], Simon Willison argues for default hard budget caps [23], and Vercel confirmed a KVM zero-day through its Sandbox bounty program [8]. About a dozen of the items are off-topic (the flight incident, personal posts) and were ignored.

## Why it matters (reasoning)
The main dynamic is competition on usage limits between OpenAI Codex and Anthropic Claude Code. The daily-reset campaign [1] arrives alongside complaints about Claude's subscription limits [6] and openly framed defection worries [18]. Pricing and quota terms are unstable right now, so a studio should not lock its workflow to one vendor's plan. Two developments make switching cheaper. Computer use is exposed as a standard local MCP server that other agents can call [13][44], and harnesses like T3 Code are agent-agnostic [39]. The agent is becoming swappable, and the reusable assets are skills, memory and MCP servers [59][31][35][27].

The second-order effect is cost and security risk. Free model promotions get abused and withdrawn without notice [29][53]. Simon Willison's call for hard budget caps [23] points to the real exposure: agents spending without limit. The KVM zero-day found through Vercel Sandbox [8] is a reminder that sandboxing agent-run code is not a solved problem. The 4090 local-inference claim [34] matters for cost-sensitive work but is an unverified single repo. Treat the 100 tokens/s figure as a claim, not a benchmark.

## Possibility
Likely: more quota and pricing moves from both OpenAI and Anthropic over the next month. The 28-day schedule is public [1], and the competitive framing is explicit [6][18]. Likely: OpenAI's merged Chat/Work/Codex surface with automatic model routing replaces manual model choice [32][54]. That cuts per-task control over cost and model. Plausible: cross-vendor MCP composition, such as Claude driving Codex tools, becomes common. It works today [13][44], but OpenAI could restrict it, since users already report guardrails being re-added [55]. Plausible: more free-model promotions are cut short because of abuse [29]. Unlikely in the near term: 125B-class models running on one consumer GPU in production use. The evidence is one repo with a heavily debated HN thread [34] and no independent benchmarks.

## Org applicability — NDF DEV
1) Keep agent workflows portable. Put team conventions in agent-skill and AGENTS-style files that work across Claude Code and Codex, and evaluate addyosmani/agent-skills as a base [59]. Effort: low. Refs: [59][39].
2) Set hard spend caps on every LLM API key and cloud agent account before expanding agent use [23]. Do not depend on free model promotions for client work [29][53]. Effort: low.
3) Trial Codex during the 28-day window only if someone already holds a Plus or Pro seat, and log which daily changes affect Unity/C# or Next.js work [1][37]. Do not buy new seats to chase resets. Effort: low.
4) For Unity and 3D asset pipelines, run a one-day spike with mixie3D's Blender agent control on a throwaway asset before considering it for production [49]. Effort: med.
5) For web and mobile QA, evaluate tester-army/e2e against the current test setup on one small project [58]. Effort: med.
6) If agents run untrusted or generated code on shared infrastructure, review the sandbox isolation in light of the KVM zero-day [8]. Effort: low.
Skip: the 4090 local-inference claim until someone reproduces it independently [34]; productivity claims like '1000x' [15] and 'miles ahead' [47]; Agent-Reach's 'zero API fees' scraping CLI, which carries terms-of-service risk [19]; and the free-course listicles [57].

## Signals to Watch
- Whether OpenAI's daily Codex drops include real feature changes or mostly quota resets, and whether Anthropic answers with a Claude Code limit change [1][6][18].
- Whether OpenAI keeps allowing Codex computer-use MCP to be called from Claude Code, or locks it down [13][55].
- Any independent benchmark of Qwen 3.8 Flash Next on a single RTX 4090 [34].
- Launch details for the merged Chat/Work/Codex product and whether manual model selection is removed [32][54].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **DietrichGebert/ponytail** — Makes your AI agent think like the laziest senior dev in the room. The best code is the code you nev | radar | <https://github.com/DietrichGebert/ponytail> |
| **pbakaus/impeccable** — The design language that makes your AI harness better at design. | radar | <https://github.com/pbakaus/impeccable> |
| **Panniantong/Agent-Reach** — Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub,  | radar | <https://github.com/Panniantong/Agent-Reach> |
| **Niko1221/Strata** — Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s | hackernews | <https://github.com/Niko1221/Strata> |
| **thedotmack/claude-mem** — Persistent Context Across Sessions for Every Agent – Captures everything your agent does during sess | radar | <https://github.com/thedotmack/claude-mem> |
| **OpenCut-app/OpenCut** — The open-source CapCut alternative | radar | <https://github.com/OpenCut-app/OpenCut> |
| **pingdotgg/t3code** —  | radar | <https://github.com/pingdotgg/t3code> |
| **omlahore/RemoveMacAI** — Turn off Apple Intelligence on macOS 27 and get its disk space back | hackernews | <https://github.com/omlahore/RemoveMacAI> |
| **tester-army/e2e** — Next generation e2e testing framework for web and mobile apps. | radar | <https://github.com/tester-army/e2e> |
| **addyosmani/agent-skills** — Production-grade engineering skills for AI coding agents. | radar | <https://github.com/addyosmani/agent-skills> |
| **calesthio/OpenMontage** — World's first open-source, agentic video production system. 12 production pipelines, 100+ tools, 700 | radar | <https://github.com/calesthio/OpenMontage> |
| **michael-denyer/pstack-claude** — Claude Code, Codex, Pi, OpenCode, Gemini, and Prime Agent versions of Poteto's pstack. Rigorous agen | radar | <https://github.com/michael-denyer/pstack-claude> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | thsottiaux | ^17120 c2552 | [Over the next 28 days, each day we’ll either ship one thing that is a clear impr](https://x.com/thsottiaux/status/2106845241357824205) |
| x | ArynneWexler | ^5837 c232 | [Dude imagine living at a time where a Muslim pilot stabs his copilot and tries t](https://x.com/ArynneWexler/status/2106880540485763508) |
| x | rauchg | ^5418 c559 | [AI will make everything free, including itself. The last domino to fall will be ](https://x.com/rauchg/status/2106503460384538793) |
| x | mark_k | ^3600 c130 | [HUGE: OpenAI just announced they will ship 28 Codex resets over the next 28 days](https://x.com/mark_k/status/2106854194116518315) |
| x | EricLDaugh | ^2556 c86 | [🚨 UPDATE: The Omani Islamist hijacker planned to surge the FlyDubai plane into I](https://x.com/EricLDaugh/status/2106830917839016132) |
| x | theo | ^2390 c165 | [July 2026: Anthropic has the best code models. Gap isn’t very big though. They’r](https://x.com/theo/status/2106847019319062819) |
| x | amasad | ^2077 c56 | [Reaching concerning levels of psychosis.](https://x.com/amasad/status/2106237645282324709) |
| x | rauchg | ^2005 c106 | [We’ve confirmed a KVM 0day through our Vercel Sandbox bounty program. Affecting ](https://x.com/rauchg/status/2106402024804020657) |
| x | kimmonismus | ^1959 c47 | [Our old subscription plans with the old rates.](https://x.com/kimmonismus/status/2106769814710628455) |
| radar | DietrichGebert_ponytail | ^1894 c0 | [DietrichGebert/ponytail Makes your AI agent think like the laziest senior dev in](https://github.com/DietrichGebert/ponytail) |
| x | rauchg | ^1415 c90 | [DHH is fundamentally right about Rust. For context, Vercel has been undergoing a](https://x.com/rauchg/status/2106863842450133114) |
| x | rauchg | ^1315 c64 | [Summer is finally here! 🌞⛱️ https://t.co/ZBeqhh3ZwF](https://x.com/rauchg/status/2106524265034162421) |
| x | argofowl | ^1272 c122 | [everyone thinks codex computer use only works inside codex it doesn't, it's a lo](https://x.com/argofowl/status/2106389732322091475) |
| radar | pbakaus_impeccable | ^1171 c0 | [pbakaus/impeccable The design language that makes your AI harness better at desi](https://github.com/pbakaus/impeccable) |
| x | poteto | ^1153 c97 | [Grok Bot, cursor cloud agents, and pstack have 1000x-ed my productivity](https://x.com/poteto/status/2106802802567848324) |
| x | theo | ^1045 c56 | [RT @maria_rcks: theo tierlist https://t.co/JyaCVlFhVj](https://x.com/theo/status/2106667068376645689) |
| x | rauchg | ^992 c132 | [Security will become a larger and larger function in software companies. Securit](https://x.com/rauchg/status/2106516538836856945) |
| x | kimmonismus | ^984 c79 | [A relevant Codex update or a reset every day. Honestly, it feels to me like an a](https://x.com/kimmonismus/status/2106847567854350438) |
| radar | Panniantong_Agent-Reach | ^980 c0 | [Panniantong/Agent-Reach Give your AI agent eyes to see the entire internet. Read](https://github.com/Panniantong/Agent-Reach) |
| x | Ananth7e | ^931 c52 | [tibo turned usage into gambling. burn your codex usage everyday and pray it's a ](https://x.com/Ananth7e/status/2106847679632589075) |
| x | TeamTarakTrust | ^888 c1 | [DON’T CREATE FAKE AI VIDEOS OF WOMEN. DON’T MORPH OR MISUSE SOMEONE’S IMAGE. RES](https://x.com/TeamTarakTrust/status/2106376293600366840) |
| x | theo | ^878 c75 | [I keep jump scaring myself with this new PFP](https://x.com/theo/status/2106696544577888749) |
| x | simonw | ^876 c189 | [Just published this post about how we’re going to need default hard budget caps ](https://x.com/simonw/status/2106528704902164855) |
| hackernews | paveworld | ^828 c179 | [Tell HN: Bob Cringely has died I heard from a friend of the family that Bob pass](https://news.ycombinator.com/item?id=49949438) |
| x | rauchg | ^792 c103 | [Working on a new little project. The 𝚁𝙴𝙰𝙳𝙼𝙴 is fully written by hand, because it](https://x.com/rauchg/status/2106848085267902815) |
| x | 0xDeliriumm | ^784 c24 | [andrej karpathy spent 7 years inside OpenAI watching GPT go from 117M to 1T para](https://x.com/0xDeliriumm/status/2106346529069924399) |
| x | tom_doerr | ^775 c22 | [Connects to PostgreSQL, MySQL, SQLite, Redis, MongoDB, SQL Server, and ClickHous](https://x.com/tom_doerr/status/2106375572754485477) |
| x | TJandCasper | ^742 c33 | [So the Co-Pilot that did the stabbing, was banned from flying in his home countr](https://x.com/TJandCasper/status/2106767137003946080) |
| x | cline | ^710 c35 | [Due to abnormally high abuse, we are pausing the free DeepSeek-V4.1-Flash promot](https://x.com/cline/status/2106828852353974713) |
| x | amasad | ^709 c135 | [Who’s building this?](https://x.com/amasad/status/2106506305875947966) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@thsottiaux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 17120 · 💬 2552</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/thsottiaux/status/2106845241357824205">View @thsottiaux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Over the next 28 days, each day we’ll either ship one thing that is a clear improvement and relevant for most codex/work users or ship a full reset. Let the improvements begin.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Codex team lead announced a 28-day cadence: each day they will either ship one clear improvement relevant to most codex/work users or do a full reset.</dd>
      <dt>Why interesting</dt>
      <dd>Codex users can expect near-daily changes for four weeks, which affects teams that depend on its behavior in their daily workflow.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/thsottiaux/status/2106845241357824205" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ArynneWexler</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5837 · 💬 232</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ArynneWexler/status/2106880540485763508">View @ArynneWexler on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Dude imagine living at a time where a Muslim pilot stabs his copilot and tries to take down an entire commercial plane but a group of Israeli civilians stops him and saves everyone Imagine witnessing ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral X post praises Israeli civilians for stopping a pilot who allegedly stabbed his copilot and tried to crash a commercial plane, then attacks people who hate Jews.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ArynneWexler/status/2106880540485763508" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5418 · 💬 559</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2106503460384538793">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“AI will make everything free, including itself. The last domino to fall will be free energy, which is humanity’s final frontier.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Vercel CEO Guillermo Rauch predicts AI will drive the cost of everything, including AI itself, toward free, with energy as the last cost to fall.</dd>
      <dt>Why interesting</dt>
      <dd>It is an opinion from a major devtools CEO with no data or specifics, though it signals the expected direction of falling AI costs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2106503460384538793" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mark_k</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3600 · 💬 130</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mark_k/status/2106854194116518315">View @mark_k on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“HUGE: OpenAI just announced they will ship 28 Codex resets over the next 28 days.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An X post claims OpenAI announced it will ship 28 Codex resets over the next 28 days, with no detail on what a 'reset' is or what it changes for users.</dd>
      <dt>Why interesting</dt>
      <dd>The post gives no definition of a 'reset' (likely usage limits, though unstated), so the claim is too vague to plan around; verify against OpenAI's own announcement.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mark_k/status/2106854194116518315" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EricLDaugh</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2556 · 💬 86</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EricLDaugh/status/2106830917839016132">View @EricLDaugh on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 UPDATE: The Omani Islamist hijacker planned to surge the FlyDubai plane into Israel's BEN GURION AIRPORT And the copilot was KNOWN for having radical Islamic views — yet was allowed to fly 😠 Thank G”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A viral X post claims a FlyDubai hijacker targeted Ben Gurion Airport, and the author frames the story with political commentary about the pilots and a passenger's views.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EricLDaugh/status/2106830917839016132" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2390 · 💬 165</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2106847019319062819">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“July 2026: Anthropic has the best code models. Gap isn’t very big though. They’re slow, expensive, and the “claudeisms” are at an all time high. And your $200 sub is so limited that you can kill it in”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Theo predicts a reversal in AI coding model preference: in July 2026 OpenAI models were faster, cheaper and had looser usage limits than Anthropic's, but by September he says Opus 5.5 is fast, cheap and nearly limitless on the $200 plan.</dd>
      <dt>Why interesting</dt>
      <dd>Cost, speed and plan limits swing between vendors within a quarter, so a team's model choice for coding tools needs periodic re-evaluation, not a one-time decision.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Treat this as one opinionated data point: run the studio's own tasks on both vendors and compare speed, cost and plan limits before changing subscriptions.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2106847019319062819" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amasad</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2077 · 💬 56</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amasad/status/2106237645282324709">View @amasad on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Reaching concerning levels of psychosis.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Amjad Masad, who leads an AI app-building platform, posted a one-line remark that AI-tool enthusiasm is reaching 'concerning levels of psychosis'; the post gives no tool, release or data.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amasad/status/2106237645282324709" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2005 · 💬 106</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2106402024804020657">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We’ve confirmed a KVM 0day through our Vercel Sandbox bounty program. Affecting the industry’s gold standard solution for Linux virtualization. 2026 is wild! Thankful to Paulos and other researchers h”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Vercel's CEO reports a confirmed zero-day in KVM, the Linux virtualization layer, found through the Vercel Sandbox bug bounty by researcher Paulos; a full writeup is still to come.</dd>
      <dt>Why interesting</dt>
      <dd>Agent sandboxes often rely on KVM-based isolation, so a KVM zero-day shows that this isolation layer can be broken and needs patching and monitoring.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">If the studio runs workloads on KVM-based VMs or sandboxes, watch for the full writeup and the upstream patch, then apply the kernel update once released.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2106402024804020657" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
