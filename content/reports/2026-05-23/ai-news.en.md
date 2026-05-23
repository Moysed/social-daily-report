---
type: social-topic-report
date: '2026-05-23'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-05-23T06:40:25+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- rss
- x
regions:
- global
post_count: 59
salience: 0.85
sentiment: positive
confidence: 0.7
tags:
- claude-code
- mcp
- skills
- anthropic
- deepseek
- supply-chain
---

# AI News & New Skills — 2026-05-23

## TL;DR
- Anthropic shipped 13+ free AI/agent courses with certs incl. Claude Code track [3]
- Claude Code 2.1.150 swaps grep for ripgrep-based search; faster/more consistent results [21][33]
- Security warning: public AI agent 'skills' are a top attack vector — many compromised [4]
- Claude Code + Obsidian pattern emerges as a personal knowledge agent [17]
- Cursor SDK 90% off + DeepSeek permanent 75% price cut reshape build economics [12][6]

## What happened
Anthropic released 13+ free certificate courses covering Agentic AI and Claude Code [3], and Claude Code 2.1.150 landed with a ripgrep-based search swap that the changelog calls more consistent and faster [21][33]. Concrete artifacts surfaced: a freeCodeCamp handbook to build your own Claude-Code-style agent in Python+Gemini [10], a Claude Code+Obsidian 'thinks back' setup [17], a 4-hour Claude Code course [32], an AgenC Workbench TUI with MCP/skills session-loading [29], and an iMessage→Claude Code→Swift app pipeline [39]. On the cost/economics side, DeepSeek made its 75% promo price permanent [6] and Cursor SDK is at 90% off [12]. Security caveat: a widely-shared post warns that public 'skill' marketplaces are heavily compromised — treat third-party skills as untrusted code [4].

## Why it matters (reasoning)
For a small studio shipping Unity/XR/Next.js work, the meaningful signal is plumbing, not hype. The ripgrep swap [21] directly speeds Claude Code on our monorepos. Free Anthropic certs [3] give the team a cheap, structured way to level up on agents/MCP without internal curriculum work. The Obsidian-as-agent-memory pattern [17] maps cleanly onto our Almondo/mempalace stack — same idea, different vault. DeepSeek's permanent cut [6] changes the math for any background/bulk LLM job (transcripts, content drafts, asset metadata) where Claude is overkill. Second-order: as 'skills' proliferate, supply-chain risk [4] becomes the real bottleneck; teams that vet/pin skills will outrun teams that paste from Twitter.

## Possibility
Likely (≥70%): Claude Code continues weekly micro-releases tightening the IDE/CLI loop; MCP+skills become the default extension surface; cheaper Chinese models force tiered routing in agent stacks. Possible (40–60%): Anthropic releases 'Mythos' soon [9], pressuring Cursor/Copilot on agent autonomy; skill-marketplace breach becomes public incident, triggering signing/sandbox standards. Unlikely near-term (<25%): RSI/AGI timelines from Clark/Hassabis [8][13] affecting our 12-month roadmap.

## Org applicability — NDF DEV
Worth doing now: (1) Enroll team in Anthropic's free Claude Code + Agentic courses [3] — 1–2 hr/wk, direct ROI on current Claude Code usage. (2) Upgrade Claude Code to 2.1.150 across machines [21] — free speed-up. (3) Pilot Obsidian-as-agent-memory [17] for NDF HR/Employee Page context, mirroring mempalace pattern. (4) Add DeepSeek as a cheap fallback route [6] for bulk/non-critical tasks (asset captions, log summarization, e-learning quiz generation). Worth doing carefully: vet every external skill before install [4] — pin to known authors, read the code, no curl-pipe-bash. Skip for now: humanoid/RSI narratives [2][8][13][26], Polymarket-bot anecdotes [27] — not in our wheelhouse.

## Signals to Watch
- Anthropic 'Mythos' release date + pricing [9][5]
- Claude Code changelog for skill-signing or sandbox flags [21]
- DeepSeek API SLA after the permanent price cut [6]
- First public post-mortem of a compromised skill in the wild [4]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **anthropics/claude-plugins-official** — Official, Anthropic-managed directory of high quality Claude Code Plugins.Claude Code Plugins Direct | rss | <https://github.com/anthropics/claude-plugins-official> |
| **colbymchenry/codegraph** — Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, OpenCode, and Hermes Agent — fewer  | rss | <https://github.com/colbymchenry/codegraph> |
| **ruvnet/RuView** — π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, an | rss | <https://github.com/ruvnet/RuView> |
| **rohitg00/ai-engineering-from-scratch** — Learn it. Build it. Ship it for others. ░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒ | rss | <https://github.com/rohitg00/ai-engineering-from-scratch> |
| **ChromeDevTools/chrome-devtools-mcp** — Chrome DevTools for coding agentsChrome DevTools for agents Chrome DevTools for agents (chrome-devto | rss | <https://github.com/ChromeDevTools/chrome-devtools-mcp> |
| **dotnet/skills** — Repository for skills to assist AI coding agents with .NET and C#.NET Agent Skills This repository c | rss | <https://github.com/dotnet/skills> |
| **Lum1104/Understand-Anything** — Graphs that teach graphs that impress. Turn any code into an interactive knowledge graph you can exp | rss | <https://github.com/Lum1104/Understand-Anything> |
| **odoo/odoo** — Odoo. Open Source Apps To Grow Your Business.Odoo Odoo is a suite of web based open source business  | rss | <https://github.com/odoo/odoo> |
| **byJoey/cfnew** — CFnew - 终端 v2.9.8 ⚠️ 重要：部署后请将兼容日期设置为 2026-01-20 Pages 部署： 登录 Cloudflare 控制台 进入 Workers 和 Pages → 选择你 | rss | <https://github.com/byJoey/cfnew> |
| **trimstray/the-book-of-secret-knowledge** — A collection of inspiring lists, manuals, cheatsheets, blogs, hacks, one-liners, cli/web tools and m | rss | <https://github.com/trimstray/the-book-of-secret-knowledge> |
| **Fincept-Corporation/FinceptTerminal** — FinceptTerminal is a modern finance application offering advanced market analytics, investment resea | rss | <https://github.com/Fincept-Corporation/FinceptTerminal> |
| **can1357/oh-my-pi** — ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, brows | rss | <https://github.com/can1357/oh-my-pi> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | Happy_Macaron5197 | ^3599 c106 | [Aged like fine WINE that meme on the chatgpt subreddit is so spot on ngl. we hav](https://www.reddit.com/r/ClaudeAI/comments/1tkhvju/aged_like_fine_wine/) |
| reddit | Distinct-Question-16 | ^2953 c698 | [Figure AI celebrates 200 hours (8 days ~8 hours) of their humanoid robots handli](https://www.reddit.com/r/singularity/comments/1tkd0fk/figure_ai_celebrates_200_hours_8_days_8_hours_of/) |
| reddit | Specialist_Engine522 | ^2365 c119 | [Anthropic officially launched 13+ FREE AI courses with certificates (Including A](https://www.reddit.com/r/ClaudeAI/comments/1tjpfh8/anthropic_officially_launched_13_free_ai_courses/) |
| x | AlexFinn | ^800 c79 | [You should NEVER be downloading AI agent skills from the internet It's the bigge](https://x.com/AlexFinn/status/2057988300926075346) |
| x | scaling01 | ^649 c48 | [Claude Mythos absolutely destroys GPT-5.5 in ExploitBench and ExploitGym Mythos ](https://x.com/scaling01/status/2057980619263537395) |
| reddit | MagicZhang | ^494 c62 | [DeepSeek Announces Permanent Price Cut of 75% after Promotion Period](https://www.reddit.com/r/singularity/comments/1tkj8l8/deepseek_announces_permanent_price_cut_of_75/) |
| reddit | FateOfMuffins | ^480 c77 | [Erdos Unit Distance Problem - Gemini 3.1 Pro's interpretation](https://www.reddit.com/r/singularity/comments/1tkaydy/erdos_unit_distance_problem_gemini_31_pros/) |
| reddit | socoolandawesome | ^351 c141 | [Anthropic Co-founder Jack Clark’s recent predictions: AI will help make a Nobel ](https://www.reddit.com/r/singularity/comments/1tkstc0/anthropic_cofounder_jack_clarks_recent/) |
| reddit | exordin26 | ^150 c34 | [Anthropic likely to release Mythos in the "near future"](https://www.reddit.com/r/singularity/comments/1tkyrva/anthropic_likely_to_release_mythos_in_the_near/) |
| x | freeCodeCamp | ^139 c3 | [What better way to understand a powerful tool like Claude Code than to build you](https://x.com/freeCodeCamp/status/2058035453266186266) |
| x | PreetamXBT | ^129 c111 | [✅selected them randomly where cursor stopped while scrolling - @jjebiz - @Underd](https://x.com/PreetamXBT/status/2058051084816699687) |
| x | ericzakariasson | ^129 c16 | [hey @grok come up with 10 examples of what i can build with the cursor sdk over ](https://x.com/ericzakariasson/status/2057971931408941390) |
| reddit | Bizzyguy | ^125 c46 | [Demis says the Singularity could be just a few years away now, potentially trigg](https://www.reddit.com/r/singularity/comments/1tkmngb/demis_says_the_singularity_could_be_just_a_few/) |
| reddit | TeachTall3390 | ^120 c58 | [Wth, what happened to cursor? I never really understood the hype around Cursor. ](https://www.reddit.com/r/cursor/comments/1tkdlbz/wth_what_happened_to_cursor/) |
| reddit | Due_Drummer5147 | ^106 c154 | [Is AI viewed as “evil” in non-tech communities? I’m sorry if this is a dumb ques](https://www.reddit.com/r/singularity/comments/1tl68ne/is_ai_viewed_as_evil_in_nontech_communities/) |
| reddit | InstaMatic80 | ^89 c29 | [I guess my prompt is too heavy 😳 My Mac started hyperventilating and then this a](https://www.reddit.com/r/cursor/comments/1tjf0p5/i_guess_my_prompt_is_too_heavy/) |
| x | cyrilXBT | ^82 c12 | [Andrej Karpathy built a wiki to think with AI. I built something that thinks bac](https://x.com/cyrilXBT/status/2058014454529364339) |
| x | chandrarsrikant | ^81 c3 | [🚨MC Interview: High-Agency Generalists will define the AI era, says Claude Code ](https://x.com/chandrarsrikant/status/2058051955700928849) |
| x | igloo1833 | ^77 c6 | [Overspec Neon Cursor #NIKKE #NIKKEfanart #メガニケ https://t.co/qmiciZLhxG](https://x.com/igloo1833/status/2058022217011892365) |
| x | orangie | ^74 c26 | [i really feel like a software engineer now a days if i would've had claude code ](https://x.com/orangie/status/2058067490400288802) |
| x | ClaudeCodeLog | ^72 c5 | [Claude Code 2.1.150 has been released. 1 CLI change Highlights: • Tool descripti](https://x.com/ClaudeCodeLog/status/2058038958735360002) |
| x | dcfgod | ^70 c10 | [Using claude code directly to analyze the chain is pretty good It finds an rpc, ](https://x.com/dcfgod/status/2057992546404769794) |
| x | jetpackjoe_ | ^60 c1 | [.@theo does this mean using cursor in t3 code is 90% off?](https://x.com/jetpackjoe_/status/2058004434022494304) |
| x | COTInetwork | ^55 c2 | [This week COTI shipped 🛡️ → Privacy Portal for private ERC20 tokens → AI agent s](https://x.com/COTInetwork/status/2057964807312011404) |
| reddit | Steap-Edit | ^54 c21 | [Exclusive: Departing Meta Staffer Posts Biting Anti-AI Video Internally Amid Mas](https://www.reddit.com/r/singularity/comments/1tl47n6/exclusive_departing_meta_staffer_posts_biting/) |
| reddit | Worldly_Evidence9113 | ^50 c33 | [#EngineAl Launches 10K-Unit #humanoid Production Line! T800 Rolls Off!](https://www.reddit.com/r/singularity/comments/1tkb5cl/engineal_launches_10kunit_humanoid_production/) |
| x | RoundtableSpace | ^50 c11 | [A BRAZILIAN COLLEGE DROPOUT MOVED INTO HIS PARENTS' GARAGE, BUILT A POLYMARKET B](https://x.com/RoundtableSpace/status/2058001215573615080) |
| reddit | AcadiaLow9013 | ^49 c73 | [Why are AI models getting more expensive? The trend before was that models becam](https://www.reddit.com/r/singularity/comments/1tkr1q4/why_are_ai_models_getting_more_expensive/) |
| x | tetsuoai | ^46 c4 | [AgenC Workbench. Tree explorer with vim nav, an editing buffer that hands off to](https://x.com/tetsuoai/status/2058044852613644716) |
| x | Josephnartey_ | ^46 c5 | [NITA, you want to run on the back of Parliament to introduce Taxes on our revenu](https://x.com/Josephnartey_/status/2057991512206594239) |
