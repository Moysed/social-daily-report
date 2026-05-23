---
type: social-topic-report
date: '2026-05-22'
topic: ai-devtools
lang: en
pair: ai-devtools.th.md
generated_at: '2026-05-23T15:29:59+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- lobsters
- reddit
- rss
- x
regions:
- global
post_count: 73
salience: 0.82
sentiment: mixed
confidence: 0.62
tags:
- coding-agents
- local-llm
- claude-code
- orchestration
- observability
- unity-xr
thumbnail: https://external-preview.redd.it/zW4iLnJxN0zQoUdThRA2N1dPbBFF2lRo5kWcCY9s-6I.png?auto=webp&s=7a0ae648f0ddc4a0a417df18941520674e0610fa
---

# AI Devtools — 2026-05-22

## TL;DR
- Microsoft is canceling internal Claude Code licenses, signaling vendor consolidation pressure on coding-agent stacks [7]
- Antigravity 2.0 tops a 3D OpenSCAD LLM benchmark, hinting at usable LLM pipelines for procedural/3D content relevant to Unity/XR [5]
- Local Qwen3.6 and Gemma 4 quants now hit 40–177 tps on single 8–16GB consumer GPUs, making on-prem coding assistants viable for small studios [12][29][30][37][39]
- Orchestration layer for parallel coding agents (Kanbots, lightsprint, AGNT Hub) is the emerging 'Jira-for-agents' category [9][19][20][32][40]
- Microsoft open-sourced an AI Engineer Coach VS Code extension that profiles how devs actually use AI agents — free observability for any team [24]

## What happened
The dominant story is the maturation of agentic coding tooling and its commercial fallout. Microsoft is pulling internal Claude Code seats [7], while Anthropic publishes a Claude Code cheat sheet and skills push [15][33], and a new 'Hyper' inference service targets coding agents specifically [38]. A new category of agent orchestrators emerged today: Kanbots runs parallel agents per Kanban card [9], lightsprint positions as Jira-for-agents [20][32][40], and AGNT Hub offers drag-drop private agent workflows [19]. On models, Antigravity 2.0 leads an OpenSCAD architectural 3D benchmark [5], and local-LLM tooling exploded — BeeLlama DFlash gives 4–5x speedups on a 3090 [12], ByteShape and pure-quant builds run Qwen3.6 27B–35B with 256K+ context on 8–16GB consumer cards [29][30][37][39]. Microsoft also open-sourced an 'AI Engineer Coach' VS Code extension that measures real agent usage [24], and an MIT lecture warned against 'vibe coding' with --dangerously-skip-permissions [26][31][36].

## Why it matters (reasoning)
Two trends compound: (a) coding agents are becoming a controlled, evaluated workflow rather than a chat toy — skills, plans, hooks, eval/observability [15][24][26][33]; (b) capable local inference on a single ≤16GB GPU is now real for code-grade models [12][29][30][37][39]. For a studio like NDF DEV this means the cost/sovereignty equation shifts: you can run a Qwen3.6-class assistant on the same workstation that runs Unity, while still using Claude Code or Antigravity for harder tasks. Microsoft canceling Claude Code seats [7] is a warning that single-vendor lock-in on closed coding agents is politically and commercially fragile; portability (skills, MCP, hooks) becomes the hedge. Second-order: as multi-agent orchestration [9][20][32][40] standardizes, the bottleneck moves from code generation to task decomposition, review, and preview environments — exactly where small studios usually under-invest.

## Possibility
Likely (≥70%): within 6–9 months, mid-size studios run a hybrid stack — frontier API (Claude/Antigravity/Gemini) for hard tasks + a local Qwen3.6/Gemma 4 quant for autocomplete, refactor, and offline work. Plausible (~45%): one of the parallel-agent orchestrators (Kanbots/lightsprint-class) becomes a de-facto 'Jira for agents' and gets acquired or merged into GitHub/Linear. Possible (~30%): Antigravity's 3D-LLM lead [5] generalizes into Unity/Blender procedural pipelines — useful for XR level/asset prototyping. Lower (~20%): closed coding-agent vendors fragment further as enterprises (à la Microsoft [7]) repatriate to in-house or open-weight stacks.

## Org applicability — NDF DEV
Worth doing now: (1) Install the AI Engineer Coach VS Code extension across the team [24] — free baseline on how Unity/Next.js devs actually use agents, no lock-in. (2) Adopt Claude Code skills + /plan + /compact workflow [15][33] as the studio standard; document 3–5 NDF-specific skills (Unity C# review, Supabase migration, XR scene scaffold). (3) Spin up one shared workstation with Qwen3.6 27B Q4 on a 16GB card [30][39] as fallback for offline/private code work and edutech content generation. Worth watching, not adopting: parallel-agent orchestrators [9][20] — promising but unproven for a <10-dev studio; current Kanban + Claude Code is enough. Probably skip: Antigravity for production until OpenSCAD-style results [5] show up on Unity/USD workloads.

## Signals to Watch
- Whether Microsoft formalizes a Claude Code replacement (Copilot Workspace? in-house?) within 60 days [7]
- Antigravity 2.0 benchmark wins extending to Unity/USD/Blender procedural tasks [5]
- Qwen3.6 / Gemma 4 official coding variants landing with Q4 builds for 16GB cards [29][30][37]
- Whether an orchestrator (lightsprint, Kanbots, or GitHub) ships a credible 'parallel agents per ticket' UX that beats single-agent flow [9][20][32][40]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **amatsuda/rubish** — Rubish: A Unix shell written in pure Ruby | hackernews | <https://github.com/amatsuda/rubish> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| hackernews | d0ks | ^774 c363 | [Why Japanese companies do so many different things](https://davidoks.blog/p/why-japanese-companies-do-so-many) |
| reddit | HumanDrone8721 | ^630 c199 | [NVIDIA Removes Gaming Revenue Category From Financial Reports](https://www.reddit.com/r/LocalLLaMA/comments/1tkw5ri/nvidia_removes_gaming_revenue_category_from/) |
| hackernews | lexandstuff | ^583 c206 | [Shipping a laptop to a refugee camp in Uganda](https://notesbylex.com/shipping-a-laptop-to-a-refugee-camp-in-uganda) |
| hackernews | louiereederson | ^475 c285 | [Project Glasswing: An Initial Update](https://www.anthropic.com/research/glasswing-initial-update) |
| hackernews | jetter | ^407 c154 | [Antigravity 2.0 Tops the OpenSCAD Architectural 3D LLM Benchmark](https://modelrift.com/blog/openscad-llm-benchmark/) |
| hackernews | roflcopter69 | ^390 c161 | [Deno 2.8](https://deno.com/blog/v2.8) |
| hackernews | robertkarl | ^376 c354 | [Microsoft starts canceling Claude Code licenses <a href="https:&#x2F;&#x2F;archi](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad) |
| hackernews | Tomte | ^268 c103 | [BambuStudio has been violating PrusaSlicer AGPL license since their fork](https://xcancel.com/josefprusa/status/2054602354851254330) |
| hackernews | vitriapp | ^237 c142 | [Open source Kanban desktop app that runs parallel agents on every card](https://www.kanbots.dev/) |
| hackernews | speckx | ^233 c54 | [CISA tries to contain data leak](https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/) |
| hackernews | colinprince | ^200 c118 | [Sleep research led to a new sleep apnea drug](https://temertymedicine.utoronto.ca/news/how-decades-sleep-research-led-new-sleep-apnea-drug) |
| reddit | Anbeeld | ^195 c113 | [BeeLlama v0.2.0 – major DFlash update. Single RTX 3090: Qwen 3.6 27B up to 164 t](https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/) |
| hackernews | Michelangelo11 | ^194 c55 | [Experience: We found a baby on the subway – now he's our 26-year-old son](https://www.theguardian.com/lifeandstyle/2026/may/22/experience-found-baby-subway-now-26-year-old-son) |
| hackernews | gorgmah | ^186 c136 | [I Miss Terry Pratchett](https://www.mahl.me/blog/the-spell-that-wouldnt-leave/) |
| x | Anthony_Sofo | ^165 c17 | [Claude Code Cheat Sheet 🧠💻 Master workflows with: • /skills • /agents • /plan • ](https://x.com/Anthony_Sofo/status/2057828266279592318) |
| hackernews | dan_hawkins | ^161 c43 | [I’m writing again](https://www.cringely.com/2026/05/21/im-writing-again/) |
| hackernews | speckx | ^153 c17 | [A Forth-inspired language for writing websites](https://robida.net/entries/2026/05/21/a-forth-inspired-language-for-writing-websites) |
| hackernews | zqna | ^145 c102 | [US tech firms share Dutch regulator officials' names with Senate](https://www.dutchnews.nl/2026/05/us-tech-firms-share-dutch-regulator-officials-names-with-senate/) |
| x | agnt_hub | ^145 c15 | [Building a private AI agent shouldn't require a computer science degree. AGNT Hu](https://x.com/agnt_hub/status/2057811474416828882) |
| x | xCryptoAlucard | ^124 c35 | [👉🏻 @lightsprintai is stepping in as the orchestration layer for AI-native engine](https://x.com/xCryptoAlucard/status/2057774717612744994) |
| x | unicodeveloper | ^120 c17 | [Claude Code users are becoming the React developers of AI coding agents. You can](https://x.com/unicodeveloper/status/2057845190140825810) |
| reddit | LLMFan46 | ^119 c11 | [G4-MeroMero-26B-A4B-it-uncensored-heretic Is Out Now, a Finetune of gemma-4-26B-](https://www.reddit.com/r/LocalLLaMA/comments/1tl1wpd/g4meromero26ba4bituncensoredheretic_is_out_now_a/) |
| reddit | Jorlen | ^114 c61 | [Can't believe I got it working! Dual GPU - 48gb VRAM llama-cpp server - R7900 + ](https://www.reddit.com/r/LocalLLaMA/comments/1tktxr0/cant_believe_i_got_it_working_dual_gpu_48gb_vram/) |
| x | akshay_pachaar | ^112 c25 | [Microsoft built a Fitbit for AI. they just open-sourced AI Engineer Coach. a VS ](https://x.com/akshay_pachaar/status/2057901920795378159) |
| hackernews | winebarrel | ^108 c63 | [Rubish: A Unix shell written in pure Ruby](https://github.com/amatsuda/rubish) |
| x | slash1sol | ^108 c27 | [MIT JUST DROPPED A 60-MIN LECTURE ON AGENTIC CODING BECAUSE VIBE-CODERS STILL TH](https://x.com/slash1sol/status/2057948111595540736) |
| hackernews | nand2mario | ^107 c19 | [80386 Microcode Disassembled](https://www.reenigne.org/blog/80386-microcode-disassembled/) |
| hackernews | ravenical | ^102 c34 | [On The <dl>](https://benmyers.dev/blog/on-the-dl/) |
| reddit | OsmanthusBloom | ^101 c46 | [ByteShape Qwen3.6-35B-A3B: 30% faster than Unsloth IQ on 6GB VRAM laptop A few d](https://www.reddit.com/r/LocalLLaMA/comments/1tknjcx/byteshape_qwen3635ba3b_30_faster_than_unsloth_iq/) |
| reddit | bobaburger | ^95 c51 | [Qwen3.6 27B Pure Quant: 40 tok/s on 16 GB VRAM Hello everyone! I want to share t](https://www.reddit.com/r/LocalLLaMA/comments/1tkzk9e/qwen36_27b_pure_quant_40_toks_on_16_gb_vram/) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Anbeeld</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 195 · 💬 113</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/zW4iLnJxN0zQoUdThRA2N1dPbBFF2lRo5kWcCY9s-6I.png?auto=webp&amp;s=7a0ae648f0ddc4a0a417df18941520674e0610fa" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“BeeLlama v0.2.0 – major DFlash update. Single RTX 3090: Qwen 3.6 27B up to 164 tps (4.40x), Gemma 4 31B up to 177.8 tps (4.93x). Prompt processing speed near baseline. **BeeLlama v0.2.0 is here!** &amp;gt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>BeeLlama v0.2.0 brings a major DFlash speculative decoding update, hitting 164–178 tps on 27–31B models with a single RTX 3090 — nearly 5x faster than baseline.</dd>
      <dt>Why interesting</dt>
      <dd>5x token throughput on a single consumer GPU means running large local LLMs for dev tooling or AI-assisted workflows is now viable without a server cluster.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can benchmark BeeLlama on an existing RTX 3090 rig to replace cloud inference costs for internal AI tools — code review, prompt testing, or e-learning content generation pipelines.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Anthony_Sofo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 165 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Anthony_Sofo/status/2057828266279592318">View @Anthony_Sofo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Claude Code Cheat Sheet 🧠💻 Master workflows with: • /skills • /agents • /plan • /compact • MCP tools • Memory &amp;amp; hooks Best practices: ✔️ Review diffs ✔️ Plan before coding ✔️ Compress context ✔️ A”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A cheat sheet for Claude Code power-users covering key slash commands (/skills, /agents, /plan, /compact), MCP tools, memory, hooks, and best practices like reviewing diffs and compressing context.</dd>
      <dt>Why interesting</dt>
      <dd>Frames AI coding as systems-building, not prompt luck — the specific combo of /plan + /compact + hooks is a replicable workflow any dev team can standardize on.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio already runs Oracle with hooks and /rrr — add /plan before every feature sprint and enforce /compact at context limits to cut wasted tokens across Unity and web work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Anthony_Sofo/status/2057828266279592318" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@agnt_hub</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 145 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/agnt_hub/status/2057811474416828882">View @agnt_hub on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Building a private AI agent shouldn't require a computer science degree. AGNT Hub lets you drag and drop modular agents to build automated workflows inside a fully encrypted cloud sandbox. Soon, you'l”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>AGNT Hub is launching a no-code, drag-and-drop platform for building and deploying private AI agent workflows inside an encrypted cloud sandbox.</dd>
      <dt>Why interesting</dt>
      <dd>Zero-code agent orchestration lowers the barrier for non-engineers to automate workflows, which directly threatens the value-add of studios that charge for custom automation builds.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can benchmark AGNT Hub against the current n8n/custom agent stack — if client-facing automation tasks can be handed off to a no-code tool, the team focuses engineering time on deeper Unity/XR work instead.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/agnt_hub/status/2057811474416828882" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@xCryptoAlucard</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 124 · 💬 35</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/xCryptoAlucard/status/2057774717612744994">View @xCryptoAlucard on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“👉🏻 @lightsprintai is stepping in as the orchestration layer for AI-native engineering. The old SDLC tools like Jira or Linear are just not built for a workflow where you run multiple coding agents in ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Lightsprint AI positions itself as an orchestration layer replacing Jira/Linear for AI-native dev workflows, offering instant PR preview environments per agentic task, backed by YC.</dd>
      <dt>Why interesting</dt>
      <dd>Running multiple coding agents in parallel breaks existing ticket-based planning tools — teams need a new coordination layer or they'll create merge chaos.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio already uses parallel agent workflows; evaluating Lightsprint as a coordination layer over GitHub PRs could cut the overhead of tracking which agent owns which feature branch.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/xCryptoAlucard/status/2057774717612744994" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@unicodeveloper</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 120 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/unicodeveloper/status/2057845190140825810">View @unicodeveloper on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Claude Code users are becoming the React developers of AI coding agents. You can’t tell them there are alternatives. Yep, i said it! So I did the comparison nobody wanted: - Claude Code @claudeai vs -”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer @unicodeveloper compared three AI coding agents — Claude Code, OpenAI Codex, and OpenCode — noting that Claude Code users are as loyal as React developers and resistant to alternatives.</dd>
      <dt>Why interesting</dt>
      <dd>A direct side-by-side comparison of the three dominant AI coding agents gives small teams concrete data to justify (or revisit) their current tool choice instead of going by hype.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should watch the linked comparison, benchmark whichever agent wins on multi-file refactoring and context retention, then standardize on one tool across Unity and Next.js workflows to cut context-switching cost.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/unicodeveloper/status/2057845190140825810" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@LLMFan46</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 119 · 💬 11</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tl1wpd/g4meromero26ba4bituncensoredheretic_is_out_now_a/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/gSlsnzJc3zRUXIwholKZwcUeSos9bcCICafrGQ2pZQU.png?auto=webp&amp;s=88f9458d84f5c78107c913ba484995284480c572" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“G4-MeroMero-26B-A4B-it-uncensored-heretic Is Out Now, a Finetune of gemma-4-26B-A4B-it, With KLD of 0.0152 and 12/100 Refusals! When I previously posted the uncensored version of the 31B version of th”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A new uncensored finetune of Gemma 4 26B (MoE, ~4B active params) is released on HuggingFace in both Safetensors and GGUF formats, achieving only 12/100 refusals and KLD of 0.0152 from the base model.</dd>
      <dt>Why interesting</dt>
      <dd>The 26B-A4B MoE architecture runs fast on lower VRAM than a dense 26B model, making capable uncensored local LLMs more accessible for teams with mid-tier GPUs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can test this GGUF locally for internal NPC dialogue generation or e-learning content drafting pipelines where cloud API cost or content restrictions are blockers.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tl1wpd/g4meromero26ba4bituncensoredheretic_is_out_now_a/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Jorlen</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 114 · 💬 61</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tktxr0/cant_believe_i_got_it_working_dual_gpu_48gb_vram/" target="_blank" rel="noopener"><img src="https://i.redd.it/ii1w278ttq2h1.png" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Can't believe I got it working! Dual GPU - 48gb VRAM llama-cpp server - R7900 + 7800XT Setup: Kubuntu 24.04 - AMD cards - R9700 AI PRO and 7800xt (32gb + 16gb) - llama-cpp server - stack setup in dock”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A hobbyist got dual AMD GPUs (R9700 AI PRO + 7800XT, 48GB VRAM total) running llama-cpp server via Vulkan on Docker/Kubuntu after ROCM failed on the mixed RDNA4+RDNA3 setup.</dd>
      <dt>Why interesting</dt>
      <dd>Vulkan bridges mixed-gen AMD GPUs into a single 48GB pool — a cheap path to running 70B+ models locally without cloud API bills.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can replicate this stack (Vulkan + llama-cpp Docker) on any mixed AMD rig to self-host large models for internal tools, e-learning content gen, or Unity NPC dialogue without per-token fees.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tktxr0/cant_believe_i_got_it_working_dual_gpu_48gb_vram/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@akshay_pachaar</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 112 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/akshay_pachaar/status/2057901920795378159">View @akshay_pachaar on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft built a Fitbit for AI. they just open-sourced AI Engineer Coach. a VS Code extension (also works in Cursor and Antigravity) that analyzes how you actually use AI coding agents. it reads loca”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Microsoft open-sourced AI Engineer Coach, a VS Code extension that reads local session logs from Copilot, Claude Code, Codex CLI and others, then scores your AI workflow across 5 categories with 45 anti-pattern detection rules.</dd>
      <dt>Why interesting</dt>
      <dd>The rule engine is markdown-based and extensible — any dev can write or tune detection rules in plain English, making it adaptable without waiting for Microsoft to update it.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio uses Claude Code daily across Unity, XR, and web projects — running this extension reveals which devs are burning tokens on trivial prompts or running mega sessions, so the team can tighten AI discipline with data, not guesswork.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/akshay_pachaar/status/2057901920795378159" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
