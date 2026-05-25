---
type: social-topic-report
date: '2026-05-25'
topic: ai-devtools
lang: en
pair: ai-devtools.th.md
generated_at: '2026-05-25T03:03:43+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- lobsters
- reddit
- x
regions:
- global
post_count: 54
salience: 0.78
sentiment: positive
confidence: 0.66
tags:
- ai-devtools
- coding-agents
- mcp
- deepseek
- gemini
- local-llm
thumbnail: https://pbs.twimg.com/media/HJGj55ubIAAV6rR.jpg
---

# AI Devtools — 2026-05-25

## TL;DR
- DeepSeek Reasonix lands as a native coding agent with aggressive caching + low pricing [3], adding pressure on incumbent IDE assistants.
- Gemini 3.5 Flash positions as a cheap, multimodal, agentic frontier model for coding/automation [19].
- Microsoft publishes a 34-min build-along showing Claude Opus 4.7 + 1,400 MCP tools for production agents [15][33].
- Codebase-as-graph context engineering (open source) works across Claude Code, Codex, Antigravity [6]; arXiv warns of 'Constraint Decay' fragility in agent-generated backends [13].
- Local LLM stack moves: Qwen3.6-35B-A3B and Gemma4-26B-A4B trade blows, AMD RDNA3 gains hipEngine, NVIDIA default is being questioned [10][11][24][39].

## What happened
DeepSeek shipped Reasonix, a native coding agent built around heavy KV-cache reuse and a permanent V4 Pro price cut, undercutting most hosted coding agents on cost-per-token [3]. Google countered with Gemini 3.5 Flash positioned at frontier quality but optimized for agentic workflows and tool use [19]. Microsoft released a free 34-min walkthrough of their internal agent stack — Claude Opus 4.7 plus a 1,400-tool MCP catalog with persistent memory — effectively endorsing MCP as the production agent contract [15][33].

On the tooling layer, an OSS project that converts a codebase into an interactive graph for agents (Claude Code, Codex, Antigravity) is gaining traction as a context-engineering primitive [6], while an arXiv paper 'Constraint Decay' documents systematic degradation of LLM agents on multi-step backend tasks [13]. Cursor's head of AI engineering published a free 14-min talk on coding-agent practice [32], and a GitHub Copilot experimental /chronicle:cost-tips surfaces real session cost/usage telemetry [36]. Local-LLM signal: Qwen3.6-35B-A3B vs Gemma4-26B-A4B comparisons [11][24], hipEngine brings fast Qwen3.6 inference to RDNA3 [39], and the community is openly questioning NVIDIA-default assumptions [10].

## Why it matters (reasoning)
Two forces compound: agent quality is rising while per-token cost is collapsing (DeepSeek caching, Gemini Flash). That makes always-on coding agents economical for a small studio, not just experiments. MCP is consolidating as the de-facto tool protocol — Microsoft's 1,400-tool catalog signals lock-in pressure to expose your internal systems as MCP servers rather than bespoke integrations [15][33]. The Constraint Decay paper [13] is the sober counterweight: agents still rot on long multi-step backend work, so test/eval scaffolding matters more than model swaps. Codebase-graph context [6] is the missing primitive most teams skip; without it, larger context windows just hide retrieval failure. Local-LLM diversification [10][11][24][39] erodes NVIDIA's monopoly for inference — relevant if NDF wants on-device XR/edutech models without per-seat API fees. Sacks' 14x code-volume claim [1] is unverified but directionally consistent with what every team is observing: agents create more code to review, not less work.

## Possibility
Likely (70%): MCP becomes the standard agent-tool contract by Q3 2026; studios that don't expose internal tools as MCP servers get left behind. Likely (65%): coding-agent pricing keeps dropping ~2-3x in 6 months as DeepSeek-class competitors force Anthropic/Google response. Plausible (45%): codebase-graph context becomes a default IDE feature, not a separate tool. Possible (35%): a credible AMD/Apple-silicon local stack reaches parity-enough that small studios drop NVIDIA for inference. Watch for Constraint Decay-style failure modes to drive a wave of agent-eval tooling in the next 2 quarters.

## Org applicability — NDF DEV
Concrete moves for NDF DEV: (1) Pilot DeepSeek Reasonix [3] or Gemini 3.5 Flash [19] alongside Claude on a non-critical Next.js/Supabase repo, measure cost-per-merged-PR for 2 weeks — likely 3-5x cheaper than current. (2) Watch the Microsoft MCP walkthrough [15][33] and wrap Supabase + Unity build scripts as MCP servers; reuses across all agents. (3) Try the codebase-graph tool [6] on the Unity C# repo — Unity's cross-scene references are exactly where flat-context agents fail. (4) Read Constraint Decay [13] before trusting agents on multi-step XR/backend tasks; add deterministic eval harness per feature. (5) For edutech voice content, LongCat talking-avatar (MIT) [2] and the TTS benchmark [38] are worth a half-day spike. Skip: local-LLM hardware migration (premature for studio scale), writerdeck/DOS/APL nostalgia items. Worth it: ~3-5 dev-days investment, payback in weeks via API cost reduction and agent reliability.

## Signals to Watch
- MCP server catalog growth — does Anthropic/Microsoft publish a registry?
- Constraint Decay-style benchmarks adopted by Cursor/Copilot eval suites
- DeepSeek Reasonix cache-hit rates reported by real users (not vendor claims)
- AMD ROCm + hipEngine reaching plug-and-play on consumer cards

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | DavidSacks | ^5384 c572 | [Q: How are job postings for software engineers rising rapidly despite AI agents ](https://x.com/DavidSacks/status/2058606722110107970) |
| x | victormustar | ^1194 c31 | [New: LongCat just dropped an excellent open-source talking-avatar model (probabl](https://x.com/victormustar/status/2058492201261244458) |
| hackernews | Alifatisk | ^459 c199 | [DeepSeek reasonix, DeepSeek native coding agent with high caching and low cost R](https://esengine.github.io/DeepSeek-Reasonix/) |
| hackernews | hggh | ^458 c278 | [Time to talk about my writerdeck](https://veronicaexplains.net/my-first-writerdeck/) |
| hackernews | DamnInteresting | ^437 c153 | [Microsoft open-sources “the earliest DOS source code discovered to date” <a href](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) |
| x | Saboo_Shubham_ | ^332 c34 | [This is ACTUALLY context engineering for your AI coding agents. It turns any cod](https://x.com/Saboo_Shubham_/status/2058269167372153129) |
| hackernews | intelkishan | ^313 c339 | [Memory has grown to nearly two-thirds of AI chip component costs](https://epoch.ai/data-insights/ai-chip-component-cost-shares) |
| hackernews | zdw | ^303 c185 | [Why is Vivado 2026.1 dropping Linux support for free tier?](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US) |
| hackernews | spike021 | ^272 c150 | [Scammers are abusing an internal Microsoft account to send spam links](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/) |
| reddit | pmv143 | ^236 c192 | [Is NVIDIA still the default best choice for local LLMs in 2026?](https://www.reddit.com/r/LocalLLaMA/comments/1tmkaua/is_nvidia_still_the_default_best_choice_for_local/) |
| reddit | EvilEnginer | ^210 c76 | [Qwen3.6-35B-A3B-Uncensored-Genesis-APEX-MTP Here model: [https://huggingface.co/](https://www.reddit.com/r/LocalLLaMA/comments/1tm3toi/qwen3635ba3buncensoredgenesisapexmtp/) |
| hackernews | pantelisk | ^194 c48 | [Show HN: Audiomass – a free, open-source multitrack audio editor for the web](https://audiomass.co/?multitrack=1) |
| hackernews | wek | ^185 c90 | [Constraint Decay: The Fragility of LLM Agents in Back End Code Generation](https://arxiv.org/abs/2605.06445) |
| hackernews | prakashqwerty | ^182 c178 | [Greg Brockman interview [video]](https://fs.blog/knowledge-project-podcast/greg-brockman/) |
| x | sairahul1 | ^171 c36 | [Microsoft Senior AI developer just showed how they build AI agents with Claude a](https://x.com/sairahul1/status/2058465917051490337) |
| hackernews | blenderob | ^165 c88 | [Childhood Computing](https://susam.net/childhood-computing.html) |
| hackernews | ngram | ^163 c48 | [Usborne 1980s Computer Books](https://usborne.com/us/books/computer-and-coding-books) |
| hackernews | jabits | ^145 c144 | [Migrating from Go to Rust](https://corrode.dev/learn/migration-guides/go-to-rust/) |
| x | pixeluibygoogle | ^139 c9 | [Gemini 3.5 introduces Flash, a frontier-level AI model that is faster, multimoda](https://x.com/pixeluibygoogle/status/2058227405467299898) |
| hackernews | anujbans | ^131 c30 | [Alexander Grothendieck Revolutionized 20th-Century Mathematics](https://www.quantamagazine.org/how-alexander-grothendieck-revolutionized-20th-century-mathematics-20260520/) |
| hackernews | tosh | ^129 c36 | [Mastering Dyalog APL](https://mastering.dyalog.com/README.html) |
| hackernews | masswerk | ^129 c25 | [The C64 Dead Test Font](https://www.masswerk.at/nowgobang/2026/c64-dead-test-font) |
| hackernews | Ember_Wipe | ^126 c85 | [CBP Directive 3340-049B: Border Search of Electronic Devices](https://www.cbp.gov/document/directives/cbp-directive-no-3340-049b-border-search-electronic-devices) |
| reddit | MarcCDB | ^123 c105 | [Qwen3.6-35B-A3B vs Gemma4-26B-A4B Just wondering how are people's experience wit](https://www.reddit.com/r/LocalLLaMA/comments/1tmbola/qwen3635ba3b_vs_gemma426ba4b/) |
| hackernews | mooreds | ^122 c52 | [Ruby for Good](https://ti.to/codeforgood/rubyforgood) |
| hackernews | ikesau | ^104 c98 | [Defeating Git Rigour Fatigue with Jujutsu](https://ikesau.co/blog/defeating-git-rigour-fatigue-with-jujutsu/) |
| reddit | NielsRogge | ^98 c7 | [PapersWithCode new features - week 1 [P] Hi, Niels here from the open-source tea](https://www.reddit.com/r/MachineLearning/comments/1tmawv5/paperswithcode_new_features_week_1_p/) |
| hackernews | ksec | ^94 c28 | [Perceptual Image Codec: What Matters in Practical Learned Image Compression](https://apple.github.io/ml-pico/) |
| x | kr0der | ^91 c4 | [this is a really good thread on AI coding agents my favourite is number 3 - one ](https://x.com/kr0der/status/2058313532241031618) |
| hackernews | littlexsparkee | ^79 c44 | [A fundamental principle of aeronautical engineering has been overturned](https://www.wired.com/story/a-fundamental-principle-of-aeronautical-engineering-has-been-overturned/) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DavidSacks</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5384 · 💬 572</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DavidSacks/status/2058606722110107970">View @DavidSacks on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Q: How are job postings for software engineers rising rapidly despite AI agents automating coding? A: Because there’s far more code to manage than ever before. We’re already seeing a 14x YoY increase ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Despite AI automating code writing, software engineer job postings are rising because AI has lowered coding costs so dramatically that total code volume has exploded — GitHub commits up 14x YoY — creating more demand, not less.</dd>
      <dt>Why interesting</dt>
      <dd>The 14x commit growth confirms AI isn't replacing devs — it's expanding the total surface area of software work, meaning small studios can ship more products without proportionally growing headcount.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio should treat AI coding tools as a force multiplier — take on more parallel projects or broader feature scopes in Unity, XR, and the Next.js stack that would previously have required hiring extra engineers.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DavidSacks/status/2058606722110107970" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@victormustar</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1194 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/victormustar/status/2058492201261244458">View @victormustar on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New: LongCat just dropped an excellent open-source talking-avatar model (probably SOTA) + MIT licensed 🔥 Made a Hugging Face Space for it and it's very impressive. So many cool products to build with ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>LongCat released a MIT-licensed open-source talking-avatar model (likely SOTA) with a free Hugging Face demo, enabling use cases like AI tutors, NPC dialogue, and talking-head coding agents.</dd>
      <dt>Why interesting</dt>
      <dd>MIT license + Hugging Face free inference lowers the barrier to zero-cost animated avatar features — no API budget needed to prototype a talking character.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity team can pipe this model into NPC dialogue systems or XR characters; the e-learning stack can use it to give lesson narrators a live face without hiring voice actors or animators.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/victormustar/status/2058492201261244458" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Saboo_Shubham_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 332 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Saboo_Shubham_/status/2058269167372153129">View @Saboo_Shubham_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is ACTUALLY context engineering for your AI coding agents. It turns any codebase into an interactive graph your agent can query. Works with Claude Code, Codex, Antigravity. 100% Opensource.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>An open-source tool that converts any codebase into an interactive graph so AI coding agents (Claude Code, Codex, etc.) can query it as structured context rather than raw files.</dd>
      <dt>Why interesting</dt>
      <dd>Small teams with large or multi-repo codebases gain faster agent grounding — the agent understands structure without being fed entire files, cutting token cost and hallucination.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can run this against its Unity and Next.js repos so Claude Code agents get a live graph of dependencies and scene hierarchies instead of losing context mid-session on complex tickets.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Saboo_Shubham_/status/2058269167372153129" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@pmv143</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 236 · 💬 192</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tmkaua/is_nvidia_still_the_default_best_choice_for_local/" target="_blank" rel="noopener"><img src="https://i.redd.it/pzq8x188q43h1.jpeg" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Is NVIDIA still the default best choice for local LLMs in 2026?”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Reddit thread on r/LocalLLaMA debates whether NVIDIA GPUs are still the top choice for running local LLMs in 2026, given growing competition from AMD, Apple Silicon, and Intel Arc.</dd>
      <dt>Why interesting</dt>
      <dd>With 192 comments, the community is actively re-evaluating GPU spend — hardware costs directly hit small dev teams budgeting for local AI inference rigs.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio running local LLMs for AI-assisted dev tools or e-learning content gen should audit whether current NVIDIA hardware is still cost-optimal vs AMD ROCm or Apple Silicon for the actual model sizes used.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tmkaua/is_nvidia_still_the_default_best_choice_for_local/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@EvilEnginer</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 210 · 💬 76</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/LocalLLaMA/comments/1tm3toi/qwen3635ba3buncensoredgenesisapexmtp/" target="_blank" rel="noopener"><img src="https://external-preview.redd.it/2DEPvcJhwdDFOGAU447G16y1vsHEUocL-p-rWNL5hwM.png?auto=webp&amp;s=fba506cbd23dde5b8c8a62d083dbb8c0e3b55074" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Qwen3.6-35B-A3B-Uncensored-Genesis-APEX-MTP Here model: [https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Uncensored-Genesis-V2-APEX-MTP-GGUF](https://huggingface.co/LuffyTheFox/Qwen3.6-35B-A3B-Unce”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A community-finetuned uncensored variant of Qwen3 35B MoE (3.6B active params) with MTP speculative decoding support is released in GGUF/FP8 formats, tested stable at 200k context on consumer hardware (Beelink GTR9 Pro + Strix Halo).</dd>
      <dt>Why interesting</dt>
      <dd>A 35B MoE model running stably at 200k context on a single consumer mini-PC proves local long-context coding agents are viable without cloud API costs for a small studio.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The Unity and web teams can self-host this model locally for long-context code review and e-learning content generation, cutting API costs while keeping sensitive project code off external servers.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/LocalLLaMA/comments/1tm3toi/qwen3635ba3buncensoredgenesisapexmtp/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sairahul1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 171 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sairahul1/status/2058465917051490337">View @sairahul1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Microsoft Senior AI developer just showed how they build AI agents with Claude at Microsoft. 34-minutes. free. By Microsoft team Opus 4.7 + 1,400+ pre-built MCP tools plug Claude into agent → give it ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>A Microsoft senior AI developer published a free 34-minute tutorial showing how they build production AI agents using Claude (Opus 4.7) with 1,400+ pre-built MCP tools.</dd>
      <dt>Why interesting</dt>
      <dd>1,400+ pre-built MCP tools means a small team can wire Claude into databases, APIs, and services without building custom integrations from scratch — massive velocity gain.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio already runs Claude Code with MCP; watching this 34-min tutorial directly applies to expanding the agent stack — plug domain-specific MCP tools into existing Unity/Next.js pipelines to automate repetitive build or content tasks.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sairahul1/status/2058465917051490337" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@pixeluibygoogle</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 139 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/pixeluibygoogle/status/2058227405467299898">View @pixeluibygoogle on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gemini 3.5 introduces Flash, a frontier-level AI model that is faster, multimodal, and optimized for complex agentic workflows, enabling reliable coding, automation, and personal AI agents with strong”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Google announced Gemini 3.5 Flash, a fast multimodal frontier model optimized for agentic workflows, coding automation, and personal AI agents with built-in safety guardrails.</dd>
      <dt>Why interesting</dt>
      <dd>A faster frontier multimodal model with native agentic support means smaller teams can build reliable multi-step AI pipelines without hitting latency or capability walls.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can swap Gemini 3.5 Flash into agentic tooling — code review bots, e-learning content generators, or XR asset pipelines — where multimodal speed directly cuts iteration time.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/pixeluibygoogle/status/2058227405467299898" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@NielsRogge</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 98 · 💬 7</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/MachineLearning/comments/1tmawv5/paperswithcode_new_features_week_1_p/" target="_blank" rel="noopener"><img src="https://preview.redd.it/uogbt0fjw23h1.png?width=2928&amp;format=png&amp;auto=webp&amp;s=8b81e48af69b8935ddeb569d882d866b3e9ba216" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“PapersWithCode new features - week 1 [P] Hi, Niels here from the open-source team at Hugging Face. It's been one week since I [launched](https://www.reddit.com/r/MachineLearning/comments/1tgmwqr/reviv”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Hugging Face's Niels Rogge relaunched paperswithcode.co and shipped week-1 features including multi-metric leaderboard support across AI benchmarks like Open ASR and COCO object detection.</dd>
      <dt>Why interesting</dt>
      <dd>A single site now tracks SOTA across agents, CV, and time-series with multiple metrics per benchmark — saves a small team hours of manual paper-hunting per sprint.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio can use paperswithcode.co as the go-to reference when evaluating AI/ML models for XR or e-learning features, replacing ad-hoc paper searches with a structured leaderboard check.</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/MachineLearning/comments/1tmawv5/paperswithcode_new_features_week_1_p/" target="_blank" rel="noopener">View on reddit →</a>
  </div>
</article>
</div>
