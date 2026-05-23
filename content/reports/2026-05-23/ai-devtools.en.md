---
type: social-topic-report
date: '2026-05-23'
topic: ai-devtools
lang: en
pair: ai-devtools.th.md
generated_at: '2026-05-23T15:48:14+00:00'
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
post_count: 72
salience: 0.82
sentiment: mixed
confidence: 0.7
tags:
- ai-devtools
- coding-agents
- local-llm
- agent-orchestration
- vendor-risk
- ide-tooling
thumbnail: https://external-preview.redd.it/zW4iLnJxN0zQoUdThRA2N1dPbBFF2lRo5kWcCY9s-6I.png?auto=webp&s=7a0ae648f0ddc4a0a417df18941520674e0610fa
---

# AI Devtools — 2026-05-23

## TL;DR
- Microsoft pulls Claude Code licenses internally, signaling vendor lock-in risk for studios standardizing on a single coding agent [7]
- Antigravity 2.0 tops a new architectural 3D OpenSCAD LLM benchmark — relevant signal for procedural/XR content pipelines [5]
- Local Qwen3.6 / Gemma 4 quants hit 40–177 tps on consumer GPUs (3090/5060Ti/3070Ti) — on-prem coding/inference now realistic for a small studio [13][30][31][38]
- Parallel-agent orchestration is the hot layer: Kanbots, Lightsprint, AGNT Hub, Charm 'Hyper' inference all target multi-agent coding workflows [9][19][21][33][39]
- Tooling-on-tooling emerges: MS 'AI Engineer Coach' VS Code extension and Addy Osmani's Agent Skills push best-practice scaffolding for agent users [28][34][15][29]

## What happened
Big-vendor turbulence and a clear stack maturation. Microsoft began revoking internal Claude Code licenses [7], reading as a push toward its own Copilot/Antigravity stack — and Antigravity 2.0 simultaneously topped the OpenSCAD architectural 3D LLM benchmark [5]. Around the agent layer, several products converged on the same idea — parallel coding agents need orchestration: Kanbots runs an agent per Kanban card [9], Lightsprint pitches itself as the Jira-replacement for multi-agent SDLC [21][33], AGNT Hub offers drag-drop encrypted agent workflows [19], and Charm shipped 'Hyper', inference tuned for coding agents [39]. Meta-tooling matured too — Microsoft open-sourced an 'AI Engineer Coach' VS Code/Cursor/Antigravity extension that analyzes how devs use agents [28], Addy Osmani released Agent Skills (19 skills + 7 commands) [34], and a Claude Code cheat sheet plus an MIT 60-min agentic-coding lecture circulated [15][29]. On the local-model side, BeeLlama v0.2.0 reported 4–5× speedups on a single 3090 [13], and several posts showed Qwen3.6 27–35B and Gemma 4 31B running well on 6–16GB consumer GPUs with long context [30][31][38].

## Why it matters (reasoning)
Two structural shifts matter for NDF DEV. First, the assumption that 'pick one coding agent vendor and standardize' is safe is weakening — MSFT cutting Claude Code internally [7] shows even hyperscalers will yank tools when commercial alignment shifts, so any studio process that hard-codes one CLI agent inherits that risk. Second, the bottleneck is no longer code generation speed but coordination of multiple agents and humans — multiple independent products [9][21][33][39] converged on this in the same news cycle, which is a strong signal the category is real, not hype. Local inference quietly crossed a threshold too: 40 tps for a 27B coder on a 16GB card [31] means a small Chiang Mai studio can plausibly run a private coding assistant for sensitive client work (gov edutech, IP-heavy XR) without recurring API spend. Second-order effects: expect agent-skills/agent-config to become a portable artifact (like ESLint configs) [34][15], and expect 'agent observability' [28] to become a hiring/onboarding lever.

## Possibility
Likely (~70%): within 6–9 months, mainstream IDEs ship multi-agent orchestration natively, making standalone tools like Kanbots/Lightsprint either get acquired or pivot to enterprise. Moderate (~45%): a portable 'agent skills' spec emerges as a de-facto standard across Claude Code, Cursor, Antigravity — early adopters of Osmani-style skill packs [34] get reuse leverage. Plausible (~35%): one major vendor (Anthropic or MSFT) restricts cross-IDE usage further [7], pushing studios to dual-vendor or local fallback. Lower (~20%): local Qwen3.6/Gemma-class models become 'good enough' for >60% of day-to-day Unity/Next.js work, displacing API spend for non-frontier tasks [13][31][38].

## Org applicability — NDF DEV
Concrete moves worth it for NDF DEV: (1) Adopt an 'agent skills' folder per repo now — start by porting Osmani's pack [34] and the Claude Code cheat-sheet hooks [15] into NDF HR, VRoom, Employee Page, TM Muscle Gym; cheap, portable across agents, hedges vendor risk [7]. (2) Pilot one parallel-agent Kanban flow (Kanbots [9] or Lightsprint [21]) on a low-risk Next.js/Supabase backlog before trying it on Unity — game code tends to break agent assumptions. (3) Stand up a single workstation with a 16–24GB GPU running Qwen3.6 27B Q4 [31] as a private fallback for client-NDA work and offline Chiang Mai dev — small capex, real strategic value. (4) Skip AGNT Hub [19] and 'Hyper' [39] for now — too early, no track record. (5) Antigravity 2.0's OpenSCAD result [5] is worth a half-day spike for XR/VRoom procedural assets, not more.

## Signals to Watch
- Whether Anthropic responds to the MSFT cancellation [7] with enterprise/IDE concessions or doubles down on Claude Code as standalone
- Whether Agent Skills [34] / Skills [15] format converges across Claude Code, Cursor, Antigravity — or fragments
- Real-world reviews of Kanbots/Lightsprint [9][21] after 30 days — do parallel agents actually reduce cycle time or just create merge hell
- Next Qwen / Gemma quant releases hitting ≥50 tps on 16GB consumer cards [31][38] — tipping point for fully-local studio coding

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **amatsuda/rubish** — Rubish: A Unix shell written in pure Ruby | hackernews | <https://github.com/amatsuda/rubish> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| hackernews | d0ks | ^777 c368 | [Why Japanese companies do so many different things](https://davidoks.blog/p/why-japanese-companies-do-so-many) |
| reddit | HumanDrone8721 | ^636 c199 | [NVIDIA Removes Gaming Revenue Category From Financial Reports](https://www.reddit.com/r/LocalLLaMA/comments/1tkw5ri/nvidia_removes_gaming_revenue_category_from/) |
| hackernews | lexandstuff | ^587 c208 | [Shipping a laptop to a refugee camp in Uganda](https://notesbylex.com/shipping-a-laptop-to-a-refugee-camp-in-uganda) |
| hackernews | louiereederson | ^479 c289 | [Project Glasswing: An Initial Update](https://www.anthropic.com/research/glasswing-initial-update) |
| hackernews | jetter | ^407 c155 | [Antigravity 2.0 Tops the OpenSCAD Architectural 3D LLM Benchmark](https://modelrift.com/blog/openscad-llm-benchmark/) |
| hackernews | roflcopter69 | ^392 c161 | [Deno 2.8](https://deno.com/blog/v2.8) |
| hackernews | robertkarl | ^381 c360 | [Microsoft starts canceling Claude Code licenses <a href="https:&#x2F;&#x2F;archi](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad) |
| hackernews | Tomte | ^280 c106 | [BambuStudio has been violating PrusaSlicer AGPL license since their fork](https://xcancel.com/josefprusa/status/2054602354851254330) |
| hackernews | vitriapp | ^238 c143 | [Open source Kanban desktop app that runs parallel agents on every card](https://www.kanbots.dev/) |
| hackernews | speckx | ^234 c54 | [CISA tries to contain data leak](https://krebsonsecurity.com/2026/05/lawmakers-demand-answers-as-cisa-tries-to-contain-data-leak/) |
| hackernews | colinprince | ^202 c118 | [Sleep research led to a new sleep apnea drug](https://temertymedicine.utoronto.ca/news/how-decades-sleep-research-led-new-sleep-apnea-drug) |
| hackernews | gorgmah | ^197 c158 | [I Miss Terry Pratchett](https://www.mahl.me/blog/the-spell-that-wouldnt-leave/) |
| reddit | Anbeeld | ^197 c114 | [BeeLlama v0.2.0 – major DFlash update. Single RTX 3090: Qwen 3.6 27B up to 164 t](https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/) |
| hackernews | Michelangelo11 | ^195 c55 | [Experience: We found a baby on the subway – now he's our 26-year-old son](https://www.theguardian.com/lifeandstyle/2026/may/22/experience-found-baby-subway-now-26-year-old-son) |
| x | Anthony_Sofo | ^165 c17 | [Claude Code Cheat Sheet 🧠💻 Master workflows with: • /skills • /agents • /plan • ](https://x.com/Anthony_Sofo/status/2057828266279592318) |
| hackernews | dan_hawkins | ^163 c43 | [I’m writing again](https://www.cringely.com/2026/05/21/im-writing-again/) |
| hackernews | speckx | ^153 c17 | [A Forth-inspired language for writing websites](https://robida.net/entries/2026/05/21/a-forth-inspired-language-for-writing-websites) |
| hackernews | zqna | ^150 c110 | [US tech firms share Dutch regulator officials' names with Senate](https://www.dutchnews.nl/2026/05/us-tech-firms-share-dutch-regulator-officials-names-with-senate/) |
| x | agnt_hub | ^146 c15 | [Building a private AI agent shouldn't require a computer science degree. AGNT Hu](https://x.com/agnt_hub/status/2057811474416828882) |
| hackernews | ravenical | ^127 c42 | [On The <dl>](https://benmyers.dev/blog/on-the-dl/) |
| x | xCryptoAlucard | ^124 c35 | [👉🏻 @lightsprintai is stepping in as the orchestration layer for AI-native engine](https://x.com/xCryptoAlucard/status/2057774717612744994) |
| hackernews | weaponeer | ^123 c30 | [1940 Air Terminal Museum Begins Liquidation](https://www.1940airterminal.org/news/liquidation-of-simulators) |
| x | unicodeveloper | ^120 c17 | [Claude Code users are becoming the React developers of AI coding agents. You can](https://x.com/unicodeveloper/status/2057845190140825810) |
| reddit | LLMFan46 | ^119 c11 | [G4-MeroMero-26B-A4B-it-uncensored-heretic Is Out Now, a Finetune of gemma-4-26B-](https://www.reddit.com/r/LocalLLaMA/comments/1tl1wpd/g4meromero26ba4bituncensoredheretic_is_out_now_a/) |
| reddit | Jorlen | ^116 c61 | [Can't believe I got it working! Dual GPU - 48gb VRAM llama-cpp server - R7900 + ](https://www.reddit.com/r/LocalLLaMA/comments/1tktxr0/cant_believe_i_got_it_working_dual_gpu_48gb_vram/) |
| hackernews | winebarrel | ^115 c66 | [Rubish: A Unix shell written in pure Ruby](https://github.com/amatsuda/rubish) |
| hackernews | nand2mario | ^114 c21 | [80386 Microcode Disassembled](https://www.reenigne.org/blog/80386-microcode-disassembled/) |
| x | akshay_pachaar | ^113 c25 | [Microsoft built a Fitbit for AI. they just open-sourced AI Engineer Coach. a VS ](https://x.com/akshay_pachaar/status/2057901920795378159) |
| x | slash1sol | ^108 c27 | [MIT JUST DROPPED A 60-MIN LECTURE ON AGENTIC CODING BECAUSE VIBE-CODERS STILL TH](https://x.com/slash1sol/status/2057948111595540736) |
| reddit | OsmanthusBloom | ^100 c47 | [ByteShape Qwen3.6-35B-A3B: 30% faster than Unsloth IQ on 6GB VRAM laptop A few d](https://www.reddit.com/r/LocalLLaMA/comments/1tknjcx/byteshape_qwen3635ba3b_30_faster_than_unsloth_iq/) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Anbeeld</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 197 · 💬 114</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tkpz2y/beellama_v020_major_dflash_update_single_rtx_3090/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/zW4iLnJxN0zQoUdThRA2N1dPbBFF2lRo5kWcCY9s-6I.png?auto=webp&amp;s=7a0ae648f0ddc4a0a417df18941520674e0610fa" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“BeeLlama v0.2.0 – major DFlash update. Single RTX 3090: Qwen 3.6 27B up to 164 tps (4.40x), Gemma 4 31B up to 177.8 tps (4.93x). Prompt processing speed near baseline. **BeeLlama v0.2.0 is here!** &amp;gt”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>BeeLlama v0.2.0 brings a major DFlash speculative decoding update, pushing a single RTX 3090 to 164 tps on Qwen 3.6 27B and 177.8 tps on Gemma 4 31B — roughly 4-5x speed gains.</dd>
      <dt>Why interesting</dt>
      <dd>A single consumer GPU (RTX 3090) now runs 27-31B models at production-viable speeds, eliminating the need for multi-GPU or cloud inference for local AI tooling.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can benchmark BeeLlama on existing RTX 3090 hardware to replace cloud LLM costs for internal dev tools — code review, asset description, or e-learning content drafting.</dd>
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
      <dd>A Claude Code cheat sheet covering key commands (/skills, /agents, /plan, /compact), MCP tools, memory, hooks, and best practices like reviewing diffs and compressing context.</dd>
      <dt>Why interesting</dt>
      <dd>Framing AI coding as 'systems not prompts' is the mindset shift — teams that build repeatable workflows with hooks and memory outpace those who just chat with the model.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio already runs hooks, /plan, and memory via Oracle — enforce /compact before long sessions and add MCP tools for Unity build or Supabase tasks to cut repetitive shell work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Anthony_Sofo/status/2057828266279592318" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@agnt_hub</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 146 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/agnt_hub/status/2057811474416828882">View @agnt_hub on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Building a private AI agent shouldn't require a computer science degree. AGNT Hub lets you drag and drop modular agents to build automated workflows inside a fully encrypted cloud sandbox. Soon, you'l”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>AGNT Hub is a no-code, drag-and-drop platform for building and deploying private AI agent workflows inside an encrypted cloud sandbox.</dd>
      <dt>Why interesting</dt>
      <dd>No-code agent orchestration lowers the barrier for non-engineers to automate repetitive tasks, which directly threatens or complements boutique dev studios charging for custom automation work.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can benchmark AGNT Hub against current n8n/Make workflows for internal ops; if deployment is truly 60-second, it replaces manual DevOps overhead for lightweight automation pipelines.</dd>
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
      <dd>Lightsprint AI is positioning itself as a YC-backed orchestration layer for running multiple AI coding agents in parallel, replacing traditional SDLC tools like Jira/Linear with instant PR preview environments per agentic task.</dd>
      <dt>Why interesting</dt>
      <dd>Small dev teams running parallel Claude/Cursor agents today have no native planning layer — Lightsprint targets exactly that gap before Jira/Linear patch it themselves.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio already uses parallel agents for Unity and web tasks — trialing Lightsprint as the task-routing layer instead of Jira tickets is a low-risk experiment worth running this sprint.</dd>
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
      <dd>A developer compared three AI coding agents — Claude Code, OpenAI Codex, and OpenCode — noting that Claude Code users are fiercely loyal and resistant to switching, similar to React developers.</dd>
      <dt>Why interesting</dt>
      <dd>Benchmark comparisons between Claude Code, Codex, and OpenCode give small dev teams real data to justify which AI coding tool budget to commit to — not just hype.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio already uses Claude Code; reviewing the linked comparison lets the team validate that choice or spot gaps where Codex or OpenCode handles specific Unity/Next.js workflows better.</dd>
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
      <dd>A new uncensored fine-tune of Gemma-4-26B-A4B called G4-MeroMero-26B-A4B-it-uncensored-heretic is released on HuggingFace in both Safetensors and GGUF formats, achieving only 12/100 refusals and KLD of 0.0152.</dd>
      <dt>Why interesting</dt>
      <dd>A 26B MoE model with only 4B active params means near-26B quality at far lower VRAM cost, making uncensored local inference practical on consumer hardware.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can run this model locally via GGUF for uncensored content-generation tasks in game narrative or e-learning scripting pipelines, without cloud API costs or content policy blocks.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tl1wpd/g4meromero26ba4bituncensoredheretic_is_out_now_a/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@Jorlen</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 116 · 💬 61</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tktxr0/cant_believe_i_got_it_working_dual_gpu_48gb_vram/" target="_blank" rel="noopener"><img src="https://i.redd.it/ii1w278ttq2h1.png" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Can't believe I got it working! Dual GPU - 48gb VRAM llama-cpp server - R7900 + 7800XT Setup: Kubuntu 24.04 - AMD cards - R9700 AI PRO and 7800xt (32gb + 16gb) - llama-cpp server - stack setup in dock”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A developer successfully ran a local llama-cpp inference server across two AMD GPUs (R9700 AI PRO + RX 7800 XT, 48 GB VRAM total) on Kubuntu using Vulkan instead of ROCm, because ROCm doesn't support mixed RDNA3/RDNA4 setups.</dd>
      <dt>Why interesting</dt>
      <dd>Vulkan is the practical escape hatch for multi-GPU AMD local LLM setups when ROCm refuses mixed RDNA generations — doubles usable VRAM without buying matching cards.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio runs local LLM experiments; using a Vulkan-based Docker llama-cpp setup lets the team pool existing AMD GPU hardware instead of upgrading to a single expensive card.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tktxr0/cant_believe_i_got_it_working_dual_gpu_48gb_vram/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@akshay_pachaar</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 113 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/akshay_pachaar/status/2057901920795378159">View @akshay_pachaar on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft built a Fitbit for AI. they just open-sourced AI Engineer Coach. a VS Code extension (also works in Cursor and Antigravity) that analyzes how you actually use AI coding agents. it reads loca”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Microsoft open-sourced AI Engineer Coach, a VS Code extension that reads local session logs from Copilot, Claude Code, and Codex CLI, then scores your AI workflow across 5 categories with 45 anti-pattern rules.</dd>
      <dt>Why interesting</dt>
      <dd>The Skill Finder feature automatically spots repeated prompt patterns across sessions and converts them into reusable skills — directly attacking the problem of prompt inconsistency on small teams.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio uses Claude Code daily — install this extension to audit actual session hygiene, catch token-burning habits on trivial prompts, and turn repeated Unity or Next.js prompt patterns into shared team skills.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/akshay_pachaar/status/2057901920795378159" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
