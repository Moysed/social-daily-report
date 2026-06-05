---
type: social-topic-report
date: '2026-06-05'
topic: ai-builders-watchlist
lang: en
pair: ai-builders-watchlist.th.md
generated_at: '2026-06-05T03:53:10+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 79
salience: 0.55
sentiment: mixed
confidence: 0.6
tags:
- ai-builders
- ui-ux
- design-systems
- ai-3d
- codex
- agent-cost
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2062482829184012288/img/PIIY2aFPn7Beunmq.jpg
---

# AI Builders Watchlist — 2026-06-05

## TL;DR
- marclou's recurring point this week: current models one-shot backend features but need 10+ prompts to get UI right — and people who think AI is good at UI/UX 'only built a landing page, not a user dashboard' [2][13].
- MengTo is pushing a design-discipline playbook to avoid 'AI slop': never start a design from a raw prompt — feed an image/site reference, keep a DESIGN.md and design rules in AGENTS.md, and use a 'taste skill'; model choice is secondary if a design system exists [1][4][57].
- AI 3D took a visible step up: Rodin Gen-2.5 generates ~1M-polygon models in seconds (10M+ for high detail), with 4s–80s controllable generation time and image→editable-parts via 'Bang-to-Parts' [31][43][50].
- Codex Sites (ChatGPT) is being framed as a 'Lovable killer' where built apps can update themselves autonomously; sama reviewed it, and Codex is being used to drive After Effects edits via .jsx [8][44][19][25].
- Two caution signals: an AI agent reportedly ran up a $150k API bill in 3 weeks replacing a $60k junior dev [28]; and EXM7777 argues against installing skills you didn't build — the risk is comprehension, not just security [15].

## What happened
Across the 15 watched accounts, the dominant technical thread this week was the gap between AI on backend vs UI. marclou posted twice that recent models one-shot backend features but require many more prompts for usable design, and that anyone who finds AI 'good at UI/UX' has only tried landing pages, not dashboards [2][13]. MengTo answered the same problem with process: reference-first prompting, a DESIGN.md, design rules in AGENTS.md, a reusable 'taste skill', plus a 22-min tutorial and shareable templates; he states model choice (e.g. Gemini 3.1 Pro) matters less than having a design system [1][4][46][57]. Separately, AI 3D and video tooling advanced: Rodin Gen-2.5 was cited for ~1M-polygon (up to 10M+) generation in seconds with 4–80s controllable time and image-to-editable-parts [31][43][50]; Grok Imagine 1.5 was priced at ~$3.75/30s for AI UGC [29].

## Why it matters (reasoning)
The clearest cross-cutting lesson is that AI's productivity gain is uneven by layer: logic/backend is largely automatable, but visual design and interaction still need human judgment or a codified design system to be acceptable [2][13]. That makes 'design system as config' (DESIGN.md, AGENTS.md rules, taste skills) a practical control, not a nicety [1][57] — the cost of skipping it is the 10+ correction-prompt loop marclou describes [2]. The skills-caution and runaway-cost items point to a second-order effect of more autonomous agents: provenance and spend become operational risks, not edge cases. An unaudited third-party skill is a comprehension liability [15], and an agent with unbounded API access is a budget liability [28]. On the asset side, faster, cleaner 3D generation [31][43][50] lowers the cost of prototyping, but raw polygon counts (10M+) are not directly usable in real-time engines without retopology, so the gain is mainly at the concept/prototype stage.

## Possibility
Likely: the 'design system / skill as guardrail' pattern keeps spreading among indie builders, because it directly addresses the UI-quality complaint multiple accounts share [1][2][13][57]. Plausible: Codex Sites' self-updating apps and Codex-driving-creative-tools (After Effects) mature into a real workflow, but the framing is early-stage and promotional, so adoption for client work is unproven [8][19][44]. Plausible: AI 3D tools like Rodin Gen-2.5 become standard for asset ideation, though real-time game/XR use still needs a cleanup step [31][43][50]. Unlikely (near-term): AI reliably one-shotting production-grade dashboard UI without human or design-system intervention, given the consistent first-hand complaints [2][13]. No source gave numeric probabilities.

## Org applicability — NDF DEV
1) Adopt the design-discipline pattern for web/mobile UI work — keep a DESIGN.md and design rules in AGENTS.md, and always pass an image or reference URL before generating UI (low effort, high payoff vs the 10-prompt loop) [1][2][4][57]. 2) Plan AI usage as backend-first: let models scaffold logic, but budget human design passes for dashboards and complex screens, not just landing pages (low) [2][13]. 3) Trial Rodin Gen-2.5 for Unity/XR concept and prototype assets, but require a retopo/poly-budget check before anything enters a real-time scene (med) [31][43][50]. 4) Put hard budget caps / spend alerts on any agent with autonomous API access before deployment (low–med) [28]. 5) Audit third-party Claude skills for provenance and comprehension before install — relevant given our heavy skill ecosystem (low) [15]. Skip for now: Codex Sites for client delivery (monitor only, early) [8][44]; levelsio's Europe/travel commentary (no work relevance) [3][5][7][14]; AI UGC ad tooling unless marketing explicitly needs it [29][32].

## Signals to Watch
- Rodin Gen-2.5 quality/speed jump and image→editable-parts — test whether output is real-time-usable for our Unity/XR pipeline [31][43][50].
- Codex Sites 'self-updating apps' and Codex driving After Effects via .jsx — early but points to agent-run app maintenance and creative automation [8][19][25].
- Convergence on 'design system / taste skill as config' to constrain AI UI output across multiple builders [1][2][57].
- Autonomous-agent cost blowups ($150k bill) as a budgeting/ops risk, not a one-off [28].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | MengTo | ^2322 c40 | [Here's how I avoid these: - Don't use GPT 5.5 to start a design - Always use an ](https://x.com/MengTo/status/2062316667024371982) |
| x | marclou | ^1042 c351 | [AI is so good at backend, but so bad at UI/UX. Any recent models one-shot my new](https://x.com/marclou/status/2062554720557048040) |
| x | levelsio | ^1024 c26 | [If it's Boeing I ain't going](https://x.com/levelsio/status/2062528825745944650) |
| x | MengTo | ^914 c23 | [I recorded a 22-min tutorial on how to avoid AI slop for your landing pages http](https://x.com/MengTo/status/2062484065748701429) |
| x | levelsio | ^711 c45 | [@vrexec Well Europe is rapidly going to shit, America isn't](https://x.com/levelsio/status/2062573509579046981) |
| x | steipete | ^673 c33 | [Here’s the video of my talk at MS Build: Build the thing that builds the thing. ](https://x.com/steipete/status/2062390654022332691) |
| x | levelsio | ^447 c29 | [This seems to have become the standard in Western Europe All last 3 hotels in Ne](https://x.com/levelsio/status/2062572899353956393) |
| x | gregisenberg | ^396 c42 | [EVERYTHING YOU NEED TO KNOW ABOUT CHATGPT'S "LOVABLE KILLER" CODEX SITES (in 25 ](https://x.com/gregisenberg/status/2062603989691044244) |
| x | levelsio | ^293 c17 | [Relatedly this guy tried to snatch my phone in De Pijp, Amsterdam Came within 5c](https://x.com/levelsio/status/2062527661511946619) |
| x | steipete | ^267 c12 | [@Neo_kura @Reuters Huh, yeah makes you worried what other facts they make up whe](https://x.com/steipete/status/2062531904855781516) |
| x | steipete | ^258 c20 | [We have over 1300 people on the waitlist for today's OpenClaw event - will be li](https://x.com/steipete/status/2062307384018829768) |
| x | jackfriks | ^256 c44 | [&gt; i have a cool idea for an app &gt; i bring it to life &gt; what do i do now](https://x.com/jackfriks/status/2062640526331949462) |
| x | marclou | ^205 c60 | [If you think AI is good at UI/UX, either: - You only built a landing page, not a](https://x.com/marclou/status/2062554732670189784) |
| x | levelsio | ^199 c6 | [Booking sites went to shit the moment they started making money with affiliate N](https://x.com/levelsio/status/2062620482793623919) |
| x | EXM7777 | ^168 c21 | [you should NEVER install skills from any source... and no, security isn't the ma](https://x.com/EXM7777/status/2062542042799149251) |
| x | egeberkina | ^135 c4 | [A love letter to green Midjourney x Nano Banana Pro https://t.co/rjzUnmUlB1](https://x.com/egeberkina/status/2062471508270649799) |
| x | eptwts | ^90 c8 | [spending your time like a normie is the single best way to understand your custo](https://x.com/eptwts/status/2062526312502145038) |
| x | levelsio | ^88 c18 | [🏆 Round 2 of judging the Vibe Jam of 2026 sponsored by @cursor_ai + @boltdotnew ](https://x.com/levelsio/status/2062644166849622066) |
| x | AmirMushich | ^80 c14 | [Ok, Codex is now editing my videos in After Effects 👀 https://t.co/55DSdJZTjS](https://x.com/AmirMushich/status/2062530819130900760) |
| x | jackfriks | ^74 c54 | [cut infrastructure cost by $600/month or add $600/month in MRR instead.... what ](https://x.com/jackfriks/status/2062639473813287222) |
| x | steipete | ^73 c0 | [@voidzerodev @rickyfm Congrats, great fit!](https://x.com/steipete/status/2062540241227977085) |
| x | MengTo | ^73 c0 | [I made a video about it 👇](https://x.com/MengTo/status/2062505847939584311) |
| x | AmirMushich | ^68 c2 | [Nano Banana smart prompt: 3D crystal glass logo Prompt 👇️ https://t.co/wUtkC4VZZ](https://x.com/AmirMushich/status/2062625480893771967) |
| x | rileybrown | ^62 c13 | [Thoughts about as a long form "content creator" in the age of AI agents. I think](https://x.com/rileybrown/status/2062576634025353444) |
| x | AmirMushich | ^59 c13 | [Match cut / Codex + After Effects automation test (.jsx) https://t.co/3R2Noujczv](https://x.com/AmirMushich/status/2062468373120762304) |
| x | gregisenberg | ^54 c15 | [@bram I met a brilliant entrepreneur in Miami today. He just moved to Mexico Cit](https://x.com/gregisenberg/status/2062574300586983459) |
| x | rileybrown | ^52 c9 | [Hardest part about making educational content about AI is how frequently you hav](https://x.com/rileybrown/status/2062567808593011032) |
| x | godofprompt | ^45 c13 | [We replaced a $60k junior developer with a proactive AI agent that casually ran ](https://x.com/godofprompt/status/2062612813890093497) |
| x | 0xROAS | ^44 c12 | [here's how grok imagine 1.5 looks like for AI UGC: this costs around $3.75 per 3](https://x.com/0xROAS/status/2062560796425486363) |
| x | EXM7777 | ^41 c8 | [i found the first model that's physically incapable of hiding why it hallucinate](https://x.com/EXM7777/status/2062555178981839043) |


## Top Posts

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MengTo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2322 · 💬 40</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MengTo/status/2062316667024371982">View @MengTo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here's how I avoid these: - Don't use GPT 5.5 to start a design - Always use an image reference or site url - Never prompt without a taste skill or DESIGN.md - Set up design rules in AGENTS.md - Get f”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>MengTo shares five rules to avoid generic AI-generated UI: always supply an image or URL reference, maintain a DESIGN.md taste file, and encode visual rules in AGENTS.md before prompting.</dd>
      <dt>Why interesting</dt>
      <dd>Encoding design taste in AGENTS.md/DESIGN.md keeps AI output consistent with studio style without per-prompt babysitting — directly applicable to any AI-assisted web or XR project.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Create a shared DESIGN.md and AGENTS.md at the studio level that captures preferred component names, visual references, and layout rules for all AI-assisted design sessions.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MengTo/status/2062316667024371982" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1042 · 💬 351</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2062554720557048040">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“AI is so good at backend, but so bad at UI/UX. Any recent models one-shot my new features, but I'd have to spend another 10+ prompts to get the design right.”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Developer @marclou reports that current AI models one-shot backend features reliably but require 10+ follow-up prompts before UI/UX output is acceptable.</dd>
      <dt>Why interesting</dt>
      <dd>The gap confirms AI-assisted dev still needs a deliberate human design pass — skipping it ships poor interfaces regardless of how clean the backend logic is.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Reserve AI for backend scaffolding and logic; assign a dedicated design review step for every AI-generated UI before it ships.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2062554720557048040" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1024 · 💬 26</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2062528825745944650">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If it's Boeing I ain't going”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@levelsio posted the viral Boeing safety meme — no technical content.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2062528825745944650" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MengTo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 914 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MengTo/status/2062484065748701429">View @MengTo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I recorded a 22-min tutorial on how to avoid AI slop for your landing pages https://t.co/PVVmwecxjK”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>Meng To (Design+Code) released a 22-min video tutorial on how to prevent generic AI-generated design from degrading landing page quality.</dd>
      <dt>Why interesting</dt>
      <dd>AI-assisted UI often produces identical, forgettable pages; a concrete tutorial from a design educator gives the web team a practical checklist to fight it.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">The studio's web team should watch this before the next landing page build and extract rules to add to the internal design brief template.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MengTo/status/2062484065748701429" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 711 · 💬 45</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2062573509579046981">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@vrexec Well Europe is rapidly going to shit, America isn't”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@levelsio made a dismissive comment about Europe's trajectory compared to America's, with no technical or product substance.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2062573509579046981" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 673 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2062390654022332691">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here’s the video of my talk at MS Build: Build the thing that builds the thing. https://t.co/lJuv2twhFe”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@steipete (Peter Steinberger) released the recording of his MS Build talk 'Build the thing that builds the thing,' covering how to create developer tooling that automates or generates other software.</dd>
      <dt>Why interesting</dt>
      <dd>A practitioner-level MS Build talk on meta-tooling from a known dev-tools author is a direct reference for any studio exploring code-gen, scaffolding, or AI-assisted pipeline automation.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Watch the talk and extract one pattern applicable to the studio's Unity or web build pipeline — e.g., a generator, scaffold, or agent that reduces repetitive setup work.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2062390654022332691" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 447 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2062572899353956393">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This seems to have become the standard in Western Europe All last 3 hotels in Netherlands and Denmark didn't clean by default Voco in The Hague was especially wild, you had to put the regular room cle”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>@levelsio shares a personal anecdote about hotel room cleaning standards declining across Netherlands and Denmark, speculating on staff shortages or cost-cutting.</dd>
      <dt>Why interesting</dt>
      <dd>Not relevant.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">No action.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2062572899353956393" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 396 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2062603989691044244">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“EVERYTHING YOU NEED TO KNOW ABOUT CHATGPT'S &quot;LOVABLE KILLER&quot; CODEX SITES (in 25 mins): TLDR; the coolest part is that apps you build can update themselves autonomously 1. Codex Sites is not Replit or ”</p>
    <dl class="ndf-fields">
      <dt>What it says</dt>
      <dd>OpenAI's Codex Sites lets you define 'safe actions' and 'skills' so a background agent autonomously updates a running app — adding features, data, or UI — without a developer triggering each change.</dd>
      <dt>Why interesting</dt>
      <dd>The safe-actions boundary model is a concrete pattern for scoping agent autonomy — directly applicable to internal dashboards or client portals the studio maintains.</dd>
      <dt class="ndf-adapt-label">How NDF DEV adapts</dt>
      <dd class="ndf-adapt">Test Codex Sites on one internal tool — e.g., a project tracker — to evaluate whether the safe-actions boundary model fits the studio's agentic workflow needs.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2062603989691044244" target="_blank" rel="noopener">View on x →</a>
  </div>
</article>
</div>
