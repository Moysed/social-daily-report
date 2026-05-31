---
type: social-topic-report
date: '2026-05-31'
topic: ai-devtools
lang: en
pair: ai-devtools.th.md
generated_at: '2026-05-31T15:51:59+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- radar
- x
regions:
- global
post_count: 134
salience: 0.72
sentiment: mixed
confidence: 0.6
tags:
- agent-skills
- coding-agents
- local-llm
- supply-chain-security
- devtools
- document-parsing
thumbnail: https://pbs.twimg.com/media/HJhEMMtaMAAK-hb.jpg
---

# AI Devtools — 2026-05-31

## TL;DR
- Agent Skills (SKILL.md) became the dominant theme: Microsoft's SkillOpt turns SKILL.md into a trainable/optimizable object [47], Android Studio added Agent Mode with Firebase skills [48], Codex shipped a 'Build Web Apps' plugin with a Supabase Postgres skill [50], and Hugging Face released a free context-engineering course covering Skills, MCP, and plugins [20].
- Skill supply chain security arrived alongside the skills boom: NVIDIA's SkillSpector runs 64 checks across 16 categories with static + optional LLM analysis [25][27], plus another agent-skill vulnerability scanner [13]; one catalog maps 754 skills to MITRE frameworks [59].
- Small/local models hit usable quality for on-device: Gemma 4 runs fully local in Google AI Edge Gallery (image→JSON, audio transcription, agentic use) [5], competitive models now fit 4–16GB hardware [8], and LFM2.5-8B-A1B is a small MoE tuned for agentic behavior [42].
- Infra/funding moves: OpenRouter raised a $113M Series B [23]; Vercel added per-API-key spend caps on its AI Gateway [52] and a Docker-based sandbox [35].
- Document parsing tooling advanced: Microsoft markitdown converts Office/files to Markdown [2], and LlamaIndex's LiteParse runs PDF parsing as WASM on edge/browser/mobile via a grid-projection layout algorithm [12][36][45].

## What happened
Multiple independent releases converged on the agent-skill format. Microsoft's SkillOpt treats SKILL.md as a text-space object to optimize rather than hand-write [47]; Google's Firebase brought Agent Mode + skills into Android Studio for Firestore/Auth setup with no extra config [48]; OpenAI's Codex shipped a web-apps plugin bundling a Supabase best-practice skill [50]; and Hugging Face published a free course on Skills, MCP, and plugin distribution [20]. Around this, a security layer formed: NVIDIA's SkillSpector scans skills before install (64 checks, 16 categories, static + LLM) [25][27], a separate scanner targets malicious patterns [13], and a 754-skill catalog is mapped to MITRE [59]. Meta-tooling like a skill-designing 'harness' [30] and semantic search over 500k+ skills [46] also appeared.

## Why it matters (reasoning)
The skill ecosystem is standardizing how coding agents (Claude Code, Codex, Cursor, Copilot, Gemini CLI) get reusable, distributable capabilities [37][59]. That lowers the cost of giving an agent project-specific competence (e.g., Firebase/Supabase setup) [48][50], which is directly useful for NDF DEV's web/mobile work. The second-order effect is supply-chain risk: installable third-party skills are executable instructions, so the rapid arrival of multiple scanners [13][25][27] signals that unreviewed skills are a real attack surface — adopting skills without scanning them is the risk to manage. On-device models maturing for 4–16GB hardware [5][8][42] matters for mobile and XR where cloud latency, cost, and privacy constrain LLM use. Separately, the 'domain expertise is the moat' argument [15] and Rauch's 'just ship the best product, AI optional' [1] are a counterweight to tooling hype: tools are converging and commoditizing, so differentiation comes from the product and domain, not the agent stack.

## Possibility
Likely: SKILL.md continues consolidating as a cross-tool standard, given simultaneous adoption by Microsoft, Google, OpenAI, and Anthropic-aligned tooling [37][47][48][50][59]. Likely: skill scanning becomes a default CI gate, since scanners are already being wired in as GitHub Actions [27]. Plausible: on-device agentic models become viable for narrow mobile/XR features within months as 8–16GB-class models improve [5][8][42], though current demos are limited tasks, not full workloads. Plausible: Codex's claimed parity with Claude Code [41] plus its Electron exit [4] pressures editor-agent UX competition (e.g., tab consolidation [51]). Unlikely (near-term): a single skill registry/standard with trusted provenance — security tooling exists [25] but no shared trust/signing layer is shown in these items.

## Org applicability — NDF DEV
1) Pilot agent skills for repetitive setup in web/mobile work — e.g., Firebase Agent Mode in Android Studio [48] and the Codex web-apps + Supabase skill [50] (effort: low). 2) Before installing any third-party/community skill, gate it through a scanner like SkillSpector, ideally as a CI/GitHub Action [25][27][13] (effort: low–med); make this policy now given the volume of new skills. 3) Evaluate on-device models (Gemma 4 via AI Edge Gallery [5], small MoEs [8][42]) for offline/low-latency features in mobile or XR builds where cloud calls are costly or private (effort: med). 4) Trial markitdown [2] and LiteParse WASM [36][45] for edutech/e-learning content pipelines that ingest PDFs/Office docs into structured text (effort: low–med). 5) Take the HF context-engineering course as team upskilling on Skills/MCP/plugins [20] (effort: low). Skip: chasing the Codex-vs-Claude-Code loyalty debate [10][41][51] — both are usable; pick on workflow fit, not hype. Skip: crypto/on-chain agent-skill items [39][60] (no fit). Skip: short-video generators [3] and TTS/voice cloning [17] unless a specific content need arises.

## Signals to Watch
- Whether a shared trust/signing standard for skills emerges to complement scanners [25][27] — the missing piece for safe skill reuse.
- On-device agentic model quality at 8–16GB for real mobile/XR tasks beyond demos [5][8][42].
- Codex's architecture shift off Electron [4] and parity claims [41] vs Claude Code — watch editor-agent UX and cost.
- OpenRouter's $113M raise [23] and Vercel AI Gateway spend caps [52] as signs of multi-model routing/cost-control becoming standard infra.

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **microsoft/markitdown** — Python tool for converting files and office documents to Markdown. | radar | <https://github.com/microsoft/markitdown> |
| **harry0703/MoneyPrinterTurbo** — 利用AI大模型，一键生成高清短视频 Generate short videos with one click using AI LLM. | radar | <https://github.com/harry0703/MoneyPrinterTurbo> |
| **codecrafters-io/build-your-own-x** — Master programming by recreating your favorite technologies from scratch. | radar | <https://github.com/codecrafters-io/build-your-own-x> |
| **OpenBMB/VoxCPM** — VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-L | radar | <https://github.com/OpenBMB/VoxCPM> |
| **D4Vinci/Scrapling** — 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale  | radar | <https://github.com/D4Vinci/Scrapling> |
| **FareedKhan-dev/train-llm-from-scratch** — A straightforward method for training your LLM, from downloading data to generating text. | radar | <https://github.com/FareedKhan-dev/train-llm-from-scratch> |
| **anthropics/claude-code** — Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and he | radar | <https://github.com/anthropics/claude-code> |
| **Crosstalk-Solutions/project-nomad** — Project N.O.M.A.D, is a self-contained, offline survival computer packed with critical tools, knowle | radar | <https://github.com/Crosstalk-Solutions/project-nomad> |
| **nesquena/hermes-webui** — Hermes WebUI: The best way to use Hermes Agent from the web or from your phone! | radar | <https://github.com/nesquena/hermes-webui> |
| **revfactory/harness** — A meta-skill that designs domain-specific agent teams, defines specialized agents, and generates the | radar | <https://github.com/revfactory/harness> |
| **EveryInc/compound-engineering-plugin** — Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more | radar | <https://github.com/EveryInc/compound-engineering-plugin> |
| **supermemoryai/supermemory** — Memory engine and app that is extremely fast, scalable. The Memory API for the AI era. | radar | <https://github.com/supermemoryai/supermemory> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | rauchg | ^3100 c207 | [Ship the best product. Use lots of AI, some AI, maybe no AI. Just be the best.](https://x.com/rauchg/status/2060803480823193840) |
| radar | microsoft_markitdown | ^2759 c0 | [microsoft/markitdown Python tool for converting files and office documents to Ma](https://github.com/microsoft/markitdown) |
| radar | harry0703_MoneyPrinterTurbo | ^1937 c0 | [harry0703/MoneyPrinterTurbo 利用AI大模型，一键生成高清短视频 Generate short videos with one cli](https://github.com/harry0703/MoneyPrinterTurbo) |
| x | theo | ^1798 c66 | [I think Codex stopped using Electron 👀 The owl was a big hint, the custom archit](https://x.com/theo/status/2060472145831174194) |
| x | googlegemma | ^1434 c57 | [A completely local agent that lives right inside your pocket. 📱 Watch Gemma 4 ru](https://x.com/googlegemma/status/2060411370139795877) |
| x | theo | ^1420 c46 | [Good results! Lines up with my experience](https://x.com/theo/status/2060837269402181942) |
| radar | codecrafters-io_build-your-own-x | ^1112 c0 | [codecrafters-io/build-your-own-x Master programming by recreating your favorite ](https://github.com/codecrafters-io/build-your-own-x) |
| x | 0xSero | ^1101 c54 | [Best models I’ve seen this week for your hardware: if you have 8-16gb you have a](https://x.com/0xSero/status/2060456091817824404) |
| x | theo | ^974 c31 | [Next big donation is pnpm, the package manager powering the majority of my proje](https://x.com/theo/status/2060497767651569679) |
| x | theo | ^970 c105 | [It is possible that Opus 4.8 is a much better model than I give it credit for, a](https://x.com/theo/status/2060953039356453316) |
| hackernews | antipurist | ^948 c345 | [Microsoft Office 2019 and 2021 for Mac view-only conversion](https://consumerrights.wiki/w/Microsoft_Office_2019_and_2021_for_Mac_view-only_conversion_(2026)) |
| x | jerryjliu0 | ^896 c28 | [Parse PDFs at lightspeed (this video is at 1x) Absolute cinema https://t.co/4l1S](https://x.com/jerryjliu0/status/2060401682610262424) |
| x | Dinosn | ^880 c7 | [Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns](https://x.com/Dinosn/status/2060610895458553977) |
| x | theo | ^874 c37 | [I am thankful that OpenAI trained their models to be helpful assistants https://](https://x.com/theo/status/2061018426152530232) |
| hackernews | aaronbrethorst | ^745 c443 | [Domain expertise has always been the real moat](https://www.brethorsting.com/blog/2026/05/domain-expertise-has-always-been-the-real-moat/) |
| x | NVIDIAAI | ^661 c33 | [Hours of video, now searchable by your agent. We just released a new set of agen](https://x.com/NVIDIAAI/status/2060481312511623513) |
| radar | OpenBMB_VoxCPM | ^639 c0 | [OpenBMB/VoxCPM VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, C](https://github.com/OpenBMB/VoxCPM) |
| radar | D4Vinci_Scrapling | ^639 c0 | [D4Vinci/Scrapling 🕷️ An adaptive Web Scraping framework that handles everything ](https://github.com/D4Vinci/Scrapling) |
| radar | FareedKhan-dev_train-llm-from-scratch | ^627 c0 | [FareedKhan-dev/train-llm-from-scratch A straightforward method for training your](https://github.com/FareedKhan-dev/train-llm-from-scratch) |
| x | _vmlops | ^520 c7 | [HUGGING FACE DROPPED A FREE CONTEXT ENGINEERING COURSE and the curriculum is sta](https://x.com/_vmlops/status/2060556680870649975) |
| radar | anthropics_claude-code | ^490 c0 | [anthropics/claude-code Claude Code is an agentic coding tool that lives in your ](https://github.com/anthropics/claude-code) |
| x | Replit | ^460 c16 | [Proud day at Replit. His Majesty King Abdullah II, King of Jordan, awarded our C](https://x.com/Replit/status/2060481312188961116) |
| hackernews | freeCandy | ^443 c228 | [OpenRouter raises $113M Series B](https://openrouter.ai/announcements/series-b) |
| radar | Crosstalk-Solutions_project-nomad | ^372 c0 | [Crosstalk-Solutions/project-nomad Project N.O.M.A.D, is a self-contained, offlin](https://github.com/Crosstalk-Solutions/project-nomad) |
| x | bibryam | ^370 c30 | [SkillSpector - a new security scanner for skills by NVIDIA • Scan AI agent skill](https://x.com/bibryam/status/2060940955084054634) |
| hackernews | aleda145 | ^340 c40 | [Shantell Sans (2023)](https://shantellsans.com/process) |
| x | dani_avila7 | ^336 c10 | [NVIDIA built exactly what I needed to secure agent skills https://t.co/y8Lt309tB](https://x.com/dani_avila7/status/2060918455545581706) |
| hackernews | k1m | ^334 c134 | [The Website Specification](https://specification.website/) |
| radar | nesquena_hermes-webui | ^320 c0 | [nesquena/hermes-webui Hermes WebUI: The best way to use Hermes Agent from the we](https://github.com/nesquena/hermes-webui) |
| radar | revfactory_harness | ^318 c0 | [revfactory/harness A meta-skill that designs domain-specific agent teams, define](https://github.com/revfactory/harness) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@rauchg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3100 · 💬 207</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/rauchg/status/2060803480823193840">View @rauchg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ship the best product. Use lots of AI, some AI, maybe no AI. Just be the best.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Vercel CEO Guillermo Rauch argues that the right amount of AI in a product is whatever makes it best — zero included.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/rauchg/status/2060803480823193840" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1798 · 💬 66</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2060472145831174194">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I think Codex stopped using Electron 👀 The owl was a big hint, the custom architecture used for the ChatGPT Atlas browser was called &quot;OWL&quot; (OpenAI’s Web Layer) https://t.co/ALFTbVCIXq”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@theo speculates OpenAI's Codex dropped Electron for a custom web layer called OWL (OpenAI's Web Layer) — the same rendering stack behind the ChatGPT Atlas browser, hinted by the app's owl icon.</dd>
      <dt>Why interesting</dt>
      <dd>A top AI lab building its own rendering stack instead of using Electron signals real performance or sandboxing limits that affect any team shipping AI-heavy desktop tools.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Before the studio commits to Electron for any upcoming desktop or XR tooling, monitor OWL's public details as a benchmark for what a leaner alternative looks like.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2060472145831174194" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@googlegemma</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1434 · 💬 57</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/googlegemma/status/2060411370139795877">View @googlegemma on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A completely local agent that lives right inside your pocket. 📱 Watch Gemma 4 run 100% locally in the Google AI Edge Gallery app. It converts images into JSON schemas, transcribes audio, and uses agen”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google's Gemma 4 runs fully on-device in the AI Edge Gallery app, handling image-to-JSON schema conversion, audio transcription, and on-device agent skills — no internet required.</dd>
      <dt>Why interesting</dt>
      <dd>On-device LLM inference with multimodal + agentic capabilities is now viable on mobile — relevant for XR/mobile apps that need AI without cloud dependency or latency.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test Gemma 4 via AI Edge Gallery on an Android device to evaluate fit for offline AI features in the studio's mobile or XR projects.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/googlegemma/status/2060411370139795877" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1420 · 💬 46</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2060837269402181942">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Good results! Lines up with my experience”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@theo posted a two-sentence reaction — 'Good results! Lines up with my experience' — with no named tool, benchmark, or finding attached.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2060837269402181942" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@0xSero</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1101 · 💬 54</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/0xSero/status/2060456091817824404">View @0xSero on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Best models I’ve seen this week for your hardware: if you have 8-16gb you have a competitive model finally! ———- 4gb - 8gb: - minicpm5: this model was built for agentic tool use on tiny machines: http”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A curated tier list of local LLMs by VRAM (4GB–196GB+) highlights LFM-2.5-8B as the top 8-16GB pick: 8B MoE with only 1.5B active params, 131k context, trained on 38T tokens.</dd>
      <dt>Why interesting</dt>
      <dd>LFM-2.5-8B fits standard dev laptops (8-16GB VRAM) and delivers 131k context — enough for local agentic pipelines without cloud API spend.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Run LFM-2.5-8B via Ollama or llama.cpp on studio dev machines to prototype local agentic tooling before committing to a cloud API.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/0xSero/status/2060456091817824404" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 974 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2060497767651569679">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Next big donation is pnpm, the package manager powering the majority of my projects. @zkochan's thankless work has been essential to the web dev ecosystem. $3,000 honestly feels cheap for how much his”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Theo donated $3,000 to @zkochan, the solo maintainer of pnpm, calling the contribution underpriced given how central pnpm is to his projects.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2060497767651569679" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 970 · 💬 105</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2060953039356453316">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It is possible that Opus 4.8 is a much better model than I give it credit for, and it is held back terribly by Claude Code. Sadly I cannot confirm this myself without spending thousands of dollars bec”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Theo Browne contends Claude Code is the bottleneck limiting Opus 4.8's perceived quality, and that Anthropic's API pricing blocks independent verification by developers.</dd>
      <dt>Why interesting</dt>
      <dd>If the client tool caps perceived model quality, benchmarks run through Claude Code do not reflect what the underlying model can actually do.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">When the studio evaluates AI coding assistants, run the same tasks via direct API or alternative frontends (Cursor, Windsurf) to separate model quality from tooling quality.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2060953039356453316" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jerryjliu0</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 896 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jerryjliu0/status/2060401682610262424">View @jerryjliu0 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Parse PDFs at lightspeed (this video is at 1x) Absolute cinema https://t.co/4l1Sr47qjU”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Jerry Liu (LlamaIndex co-founder) demos a PDF parser processing documents at true 1x speed, showing ingestion throughput well beyond what typical parsing tools deliver.</dd>
      <dt>Why interesting</dt>
      <dd>Faster PDF parsing cuts pipeline latency for RAG and document-search features in e-learning or any content-heavy project the studio builds.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test the tool shown (likely LlamaParse or a new LlamaIndex release) against the current PDF ingestion step in any RAG pipeline the studio runs.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jerryjliu0/status/2060401682610262424" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
