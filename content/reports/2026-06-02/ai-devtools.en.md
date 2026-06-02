---
type: social-topic-report
date: '2026-06-02'
topic: ai-devtools
lang: en
pair: ai-devtools.th.md
generated_at: '2026-06-02T03:05:20+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 160
salience: 0.82
sentiment: mixed
confidence: 0.68
tags:
- coding-agents
- llm-models
- agent-skills
- mcp
- supply-chain-security
- evals
thumbnail: https://pbs.twimg.com/media/HJspkEsbkAAACqT.jpg
---

# AI Devtools — 2026-06-02

## TL;DR
- Anthropic confidentially filed a draft S-1 with the SEC, signaling a possible IPO and pressure to show revenue/durability — relevant to anyone betting their toolchain on Claude/Claude Code [1][27].
- MiniMax-M3 launched: 1M-token context, multimodal, agentic coding via sparse attention; ranked the top open model on Next.js agent evals, behind Opus and GPT5 but ~10x cheaper (20x on Vercel AI Gateway) [11][30][43][47]. Qwen-3.7 Plus also claims near-SOTA coding/agent performance [51].
- An 'agent skills' ecosystem is consolidating: an Anthropic hackathon winner open-sourced 'Everything Claude Code' (183 skills, 48 sub-agents, 79 commands) [12][49][55], NVIDIA shipped a CUDA-X/Omniverse/Physical-AI skills catalog [13], and NVIDIA's SkillSpector scanner (64 checks/16 categories) appeared to vet skills before install [18].
- Supply-chain and agent-security incidents stacked up: malicious npm packages found across Red Hat Cloud Services [19] and Meta's AI support bot was abused to seize Instagram accounts [9].
- OpenAI frontier models and Codex are now available on AWS [54]; MCP keeps spreading into dev tooling (TablePlus DB workflows) [58].

## What happened
Two clusters dominate. First, models and platforms: Anthropic confidentially submitted a draft S-1 to the SEC, keeping an IPO open [1][27]; MiniMax released M3, a 1M-context multimodal model with agentic coding that topped the Next.js open-model agent evals while sitting behind Opus and GPT5 at roughly 10x lower cost [11][30][43][47]; Alibaba's Qwen-3.7 Plus claimed near-SOTA coding/agent results [51]; and OpenAI made its frontier models plus Codex available on AWS [54]. Second, the 'agent skills' and tooling layer matured: an Anthropic hackathon winner open-sourced a large Claude Code skill bundle [12][49][55], NVIDIA published an official skills catalog for CUDA-X/Omniverse/Physical AI [13], and released SkillSpector to statically scan skills before install [18]. MCP integrations widened (TablePlus [58]; assorted crypto servers [34][40]), and microsoft/markitdown (files→Markdown) trended as ingestion glue [3]. Alongside these, security failures surfaced — malicious npm packages in Red Hat Cloud Services [19] and an Instagram account-takeover via Meta's AI support bot [9]. Commentary noted eval/observability startups pivoting toward 'continual learning' platforms [36][57] and a critique that swe-bench is unreliable, with DeepSWE proposed as a saner agentic benchmark [20]. Several star/credit claims (e.g. '163k stars' [55] vs the $15K-credit framing [12]) are inconsistent and should be treated skeptically.

## Why it matters (reasoning)
The cost curve is the main story for a studio: M3 and Qwen-3.7 put near-frontier coding/agent quality at a fraction of closed-model price [30][51], which makes routing cheaper open models for bulk agent work (codegen, refactors, test scaffolding) economically rational while reserving Opus/GPT5 for hard tasks. Anthropic's S-1 [1][27] and OpenAI/Codex landing on AWS [54] both point to vendor consolidation and enterprise distribution — good for procurement and stability, but a reminder not to hard-couple workflows to one provider's UI, since features can vanish without notice (Codex 'Copy as Markdown' removed, then reinstated after backlash [8][45]). The skills/MCP boom [12][13][22][28][58] lowers the cost of giving agents capabilities, but the same incidents — npm supply-chain compromise [19], an AI support bot socially engineered into account takeover [9] — show the attack surface scales with it. That is exactly why a scanner like SkillSpector exists [18]: installing a third-party skill or MCP server is now a dependency-trust decision, not a convenience.

## Possibility
Likely: cheap open coding models (M3, Qwen-3.7) get adopted through gateways for cost-sensitive agent workloads within months, given the stated 10–20x price gap and competitive eval placement [30][11][51]. Plausible: agent-skill marketplaces grow fast enough that skill scanning/signing becomes a default step, since both the catalogs [12][13] and the scanner [18] and the supply-chain incidents [19][9] are emerging together. Plausible: eval vendors reposition as continual-learning platforms in 2026, with a shakeout — the source itself predicts many will fail [36]. Unlikely to resolve soon: benchmark trust — swe-bench criticism and DeepSWE are early [20], so no single agentic-coding benchmark is settled. Anthropic's IPO timing is indeterminate; a confidential S-1 is an option, not a schedule [1][27]. No source gives numeric probabilities, so none are asserted here.

## Org applicability — NDF DEV
1) Trial MiniMax-M3 (and Qwen-3.7 Plus) via Vercel AI Gateway for web/Next.js and general coding-agent tasks, comparing cost/quality against your current Opus/GPT5 usage — effort low [30][11][51]. 2) Treat any third-party agent skill or MCP server as an untrusted dependency: run SkillSpector (or equivalent static + LLM scan) before installing bundles like 'Everything Claude Code', the compound-engineering plugin, or 'harness' — effort low/med [18][12][28][22][19][9]. 3) For XR/VR and Unity work, review NVIDIA's CUDA-X/Omniverse/Physical-AI skills catalog in the Hermes Skills Hub to see if it accelerates rendering/sim pipelines — effort med [13]. 4) Use microsoft/markitdown to normalize docs/office files into Markdown for edutech content prep and agent ingestion — effort low [3]. 5) Pin model/provider behind an abstraction (gateway or your own adapter) so a vendor UI/feature removal or pricing change doesn't break workflows — effort med [8][45][54][1]. 6) When wiring MCP into internal DB/admin tools (e.g. TablePlus), gate write access and test for permission/data-handling quirks — effort med [58][41]. Skip for now: crypto/DeFi MCP servers [34][40], MoneyPrinterTurbo [2], TradingAgents [35], and uncritical adoption of viral 'X skills/Y sub-agents' repos until scanned and proven [55].

## Signals to Watch
- Open coding models closing on closed frontier at ~10x lower cost — track M3 and Qwen-3.7 placement on agent evals [30][51].
- Skill/MCP security tooling becoming mandatory as catalogs grow — watch SkillSpector and signing/provenance norms [18][13][19].
- Eval/observability vendors pivoting to 'continual learning' in 2026; expect consolidation [36][57].
- Local AI hardware (NVIDIA RTX Spark, Surface Laptop Ultra) lowering the cost of on-device/private agents [31][53][38].

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **harry0703/MoneyPrinterTurbo** — 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | radar | <https://github.com/harry0703/MoneyPrinterTurbo> |
| **microsoft/markitdown** — Python tool for converting files and office documents to Markdown. | radar | <https://github.com/microsoft/markitdown> |
| **D4Vinci/Scrapling** — 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale  | radar | <https://github.com/D4Vinci/Scrapling> |
| **codecrafters-io/build-your-own-x** — Master programming by recreating your favorite technologies from scratch. | radar | <https://github.com/codecrafters-io/build-your-own-x> |
| **nesquena/hermes-webui** — Hermes WebUI: The best way to use Hermes Agent from the web or from your phone! | radar | <https://github.com/nesquena/hermes-webui> |
| **OpenBMB/VoxCPM** — VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-L | radar | <https://github.com/OpenBMB/VoxCPM> |
| **FareedKhan-dev/train-llm-from-scratch** — A straightforward method for training your LLM, from downloading data to generating text. | radar | <https://github.com/FareedKhan-dev/train-llm-from-scratch> |
| **RedHatInsights/javascript-clients** — Malicious npm packages detected across Red Hat Cloud Services | hackernews | <https://github.com/RedHatInsights/javascript-clients> |
| **supermemoryai/supermemory** — Memory engine and app that is extremely fast, scalable. The Memory API for the AI era. | radar | <https://github.com/supermemoryai/supermemory> |
| **revfactory/harness** — A meta-skill that designs domain-specific agent teams, defines specialized agents, and generates the | radar | <https://github.com/revfactory/harness> |
| **pbakaus/impeccable** — The design language that makes your AI harness better at design. | radar | <https://github.com/pbakaus/impeccable> |
| **EveryInc/compound-engineering-plugin** — Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more | radar | <https://github.com/EveryInc/compound-engineering-plugin> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | AnthropicAI | ^18682 c768 | [Anthropic has confidentially submitted a draft S-1 registration statement to the](https://x.com/AnthropicAI/status/2061478052257841495) |
| radar | harry0703_MoneyPrinterTurbo | ^3375 c0 | [harry0703/MoneyPrinterTurbo 利用AI大模型，一键生成高清短视频 Generate short videos with one cli](https://github.com/harry0703/MoneyPrinterTurbo) |
| radar | microsoft_markitdown | ^3034 c0 | [microsoft/markitdown Python tool for converting files and office documents to Ma](https://github.com/microsoft/markitdown) |
| x | elonmusk | ^2078 c308 | [@yunta_tsai Tool use was a gamechanger](https://x.com/elonmusk/status/2061220941112451251) |
| x | theo | ^1639 c79 | [This is bigger than you probably think](https://x.com/theo/status/2061572633599394200) |
| radar | D4Vinci_Scrapling | ^1486 c0 | [D4Vinci/Scrapling 🕷️ An adaptive Web Scraping framework that handles everything ](https://github.com/D4Vinci/Scrapling) |
| x | rauchg | ^1432 c193 | [Unclear if a durable trend, but CEOs and CTOs are back to coding with a fury, th](https://x.com/rauchg/status/2061135404942974982) |
| x | simonw | ^1410 c136 | [I'm really upset about this: OpenAI's Codex Desktop had a "Copy as Markdown" opt](https://x.com/simonw/status/2061158636311958005) |
| hackernews | ssiddharth | ^1403 c334 | [The newest Instagram “exploit” is the goofiest I've seen <a href="https:&#x2F;&#](https://www.0xsid.com/blog/meta-account-takeover-fiasco) |
| radar | codecrafters-io_build-your-own-x | ^1212 c0 | [codecrafters-io/build-your-own-x Master programming by recreating your favorite ](https://github.com/codecrafters-io/build-your-own-x) |
| x | cline | ^1185 c49 | [The new MiniMax-M3 is their first model to have 1m context, multimodal, and agen](https://x.com/cline/status/2061287441575858253) |
| x | RoundtableSpace | ^1035 c33 | [THE WINNER OF THE ANTHROPIC HACKATHON JUST OPEN SOURCED HIS ENTIRE AI CODING SET](https://x.com/RoundtableSpace/status/2061255156323495949) |
| x | NousResearch | ^991 c56 | [We have worked with @nvidia to integrate their official Agent Skills catalog int](https://x.com/NousResearch/status/2061572272993751364) |
| radar | nesquena_hermes-webui | ^945 c0 | [nesquena/hermes-webui Hermes WebUI: The best way to use Hermes Agent from the we](https://github.com/nesquena/hermes-webui) |
| x | theo | ^912 c46 | [Confirmed rewrite with Tanstack and a bunch of data precaching. Great work Anthr](https://x.com/theo/status/2061563106208432223) |
| radar | OpenBMB_VoxCPM | ^888 c0 | [OpenBMB/VoxCPM VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, C](https://github.com/OpenBMB/VoxCPM) |
| radar | FareedKhan-dev_train-llm-from-scratch | ^861 c0 | [FareedKhan-dev/train-llm-from-scratch A straightforward method for training your](https://github.com/FareedKhan-dev/train-llm-from-scratch) |
| x | bibryam | ^744 c40 | [SkillSpector - a new security scanner for skills by NVIDIA • Scan AI agent skill](https://x.com/bibryam/status/2060940955084054634) |
| hackernews | kurmiashish | ^733 c418 | [Malicious npm packages detected across Red Hat Cloud Services](https://github.com/RedHatInsights/javascript-clients/issues/492) |
| x | theo | ^712 c40 | [swe-bench is kind of a shitshow, and it makes evaluating LLMs hard. DeepSWE is t](https://x.com/theo/status/2061368474132521392) |
| radar | supermemoryai_supermemory | ^647 c0 | [supermemoryai/supermemory Memory engine and app that is extremely fast, scalable](https://github.com/supermemoryai/supermemory) |
| radar | revfactory_harness | ^524 c0 | [revfactory/harness A meta-skill that designs domain-specific agent teams, define](https://github.com/revfactory/harness) |
| hackernews | speckx | ^523 c252 | [The Pirate Bay Remains Resilient, 20 Years After the Raid](https://torrentfreak.com/the-pirate-bay-remains-resilient-20-years-after-the-raid/) |
| x | leerob | ^512 c16 | [Some tips to help agents understand your codebase: 1. The source code either nee](https://x.com/leerob/status/2061557826787344781) |
| x | rauchg | ^501 c29 | [Beautiful example of a full-stack agent on @vercel. Great learning material!](https://x.com/rauchg/status/2061415178298937365) |
| radar | pbakaus_impeccable | ^485 c0 | [pbakaus/impeccable The design language that makes your AI harness better at desi](https://github.com/pbakaus/impeccable) |
| hackernews | surprisetalk | ^461 c376 | [Anthropic confidentially submits draft S-1 to the SEC <a href="https:&#x2F;&#x2F](https://www.anthropic.com/news/confidential-draft-s1-sec) |
| radar | EveryInc_compound-engineering-plugin | ^417 c0 | [EveryInc/compound-engineering-plugin Official Compound Engineering plugin for Cl](https://github.com/EveryInc/compound-engineering-plugin) |
| hackernews | kristianpaul | ^372 c43 | [CS336: Language Modeling from Scratch](https://cs336.stanford.edu/) |
| x | rauchg | ^357 c27 | [MiniMax M3 is now the leading open model on the Next.js agent evaluations (https](https://x.com/rauchg/status/2061593874498531707) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AnthropicAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 18682 · 💬 768</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AnthropicAI/status/2061478052257841495">View @AnthropicAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anthropic has confidentially submitted a draft S-1 registration statement to the Securities and Exchange Commission. Pending completion of SEC review, this gives us the option to pursue an initial pub”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Anthropic has filed a confidential draft S-1 with the SEC, opening the option for an IPO once the review process completes.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AnthropicAI/status/2061478052257841495" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@elonmusk</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2078 · 💬 308</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/elonmusk/status/2061220941112451251">View @elonmusk on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@yunta_tsai Tool use was a gamechanger”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Elon Musk replied to a tweet saying 'Tool use was a gamechanger' — no context, no specific tool or release named.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/elonmusk/status/2061220941112451251" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1639 · 💬 79</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2061572633599394200">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is bigger than you probably think”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Post by @theo reads only 'This is bigger than you probably think' — no subject, tool, release, or fact is stated in the provided text.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2061572633599394200" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1432 · 💬 193</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2061135404942974982">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Unclear if a durable trend, but CEOs and CTOs are back to coding with a fury, thanks to coding agents. I have public company CEOs sliding into my DMs (and “InMail”) telling me about falling in love wi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Vercel CEO Guillermo Rauch says enterprise CEOs and CTOs are coding again via agents like Claude Code, making C-suite execs firsthand evaluators of dev infrastructure.</dd>
      <dt>Why interesting</dt>
      <dd>Enterprise buyers who now code with agents evaluate the stack themselves — a studio's tech choices are no longer shielded by a middleman IT layer.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When pitching enterprise clients, prepare stack walkthroughs a hands-on CEO can follow — not just slide decks aimed at IT gatekeepers.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2061135404942974982" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@simonw</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1410 · 💬 136</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/simonw/status/2061158636311958005">View @simonw on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm really upset about this: OpenAI's Codex Desktop had a &quot;Copy as Markdown&quot; option for exporting full chat transcripts, but the feature vanished in an update a couple of days ago Genuinely my single ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Simon Willison reports OpenAI Codex Desktop silently removed its 'Copy as Markdown' chat-transcript export in a recent update — the one feature he rated above Claude Code.</dd>
      <dt>Why interesting</dt>
      <dd>The complaint surfaces a real workflow gap: exporting AI coding-session transcripts to Markdown is useful for docs and retros, and no major AI coding tool handles it well right now.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can build a small script that reads Claude Code's existing transcript files and exports them as Markdown, covering this gap without waiting for an official feature.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/simonw/status/2061158636311958005" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cline</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1185 · 💬 49</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cline/status/2061287441575858253">View @cline on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The new MiniMax-M3 is their first model to have 1m context, multimodal, and agentic coding capability. Congratulations to @MiniMax_AI for the breakthrough in sparse-attention architecture cutting comp”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>MiniMax-M3 launches with 1M-token context, multimodal input, and agentic coding support — built on a sparse-attention architecture that cuts compute and cost to 1/20th of MiniMax's prior generation — now free in Cline.</dd>
      <dt>Why interesting</dt>
      <dd>1M-token context at near-zero cost opens full-repo-scale agentic coding tasks that were previously too expensive to run continuously in tools like Cline.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test MiniMax-M3 in Cline on a large Unity or web project to benchmark quality vs. cost against the team's current default model.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cline/status/2061287441575858253" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RoundtableSpace</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1035 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RoundtableSpace/status/2061255156323495949">View @RoundtableSpace on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“THE WINNER OF THE ANTHROPIC HACKATHON JUST OPEN SOURCED HIS ENTIRE AI CODING SETUP FOR FREE. 183 AGENT SKILLS, 48 SUB-AGENTS AND 79 READY-MADE COMMANDS. He spent 10 months on it, won $15K in API credi”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An Anthropic Hackathon winner released their full Claude-based coding agent stack under MIT — 183 skills, 48 sub-agents, and 79 commands built over 10 months, after taking $15K in API credits.</dd>
      <dt>Why interesting</dt>
      <dd>A production-tested MIT agent framework at this scale is directly forkable — the studio can audit its skill list for gaps in the current Claude Code setup without building from scratch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Clone the repo and compare its skill/command list against the studio's existing Oracle skills to identify concrete additions worth porting — focus on Unity, XR, or content pipeline tasks.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RoundtableSpace/status/2061255156323495949" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NousResearch</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 991 · 💬 56</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NousResearch/status/2061572272993751364">View @NousResearch on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We have worked with @nvidia to integrate their official Agent Skills catalog into the Hermes Skills Hub. These skills teach your agent how to use CUDA-X libraries, Omniverse and Physical AI workflows,”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Nous Research integrated NVIDIA's official Agent Skills catalog into the Hermes Skills Hub, adding prebuilt skills for CUDA-X, Omniverse, Physical AI, and NeMo tools.</dd>
      <dt>Why interesting</dt>
      <dd>Prebuilt Omniverse and NeMo agent skills let the studio's XR/VR and AI pipelines use NVIDIA platform tools without writing custom tool integrations from scratch.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Check the Hermes Skills Hub catalog to see if Omniverse or NeMo skills slot into the studio's XR/VR or AI training workflows before writing custom agent tools.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NousResearch/status/2061572272993751364" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
