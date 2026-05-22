---
type: social-topic-report
date: '2026-05-22'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-05-22T09:43:34+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- rss
- x
regions:
- global
post_count: 69
salience: 0.85
sentiment: positive
confidence: 0.7
tags:
- claude-code
- cursor
- gemini
- qwen
- agent-frameworks
- free-courses
---

# AI News & New Skills — 2026-05-22

## TL;DR
- Anthropic dropped 13+ free certified AI courses incl. Agentic AI + Claude Code — direct upskill path for the team [1][33]
- Cursor Composer 2.5 ranks #3 on Artificial Analysis, 10-60x cheaper than Opus 4.7/GPT 5.5 — viable default coder [12][18]
- Gemini 3.5 Flash tops APEX-Agents-AA, beating larger models — cheap agent backbone candidate [5][13]
- Open-source Claude Code ↔ Lark/Feishu bridge enables phone-driven multi-session CC ops [29]
- Qwen 3.7 Max claims wins over Opus 4.6 on terminal bench/MCP/math — open-weight option worth piloting [28]

## What happened
Anthropic released 13+ free certified courses covering Claude API, Agentic AI, and Claude Code [1][33], plus a community 6-week Certified Architect roadmap [23]. Cursor's Composer 2.5 landed as a price-performance leader — #3 on Artificial Analysis behind only Opus 4.7 Max and GPT 5.5 xHigh at a fraction of the cost [12][18], while Cursor itself hit $3B run-rate and is building a mobile agentic app [6][34]. Google's Gemini 3.5 Flash topped the APEX-Agents-AA benchmark [13] and 3.5 Pro is teased [7]. Alibaba's Qwen 3.7 Max reportedly beats Opus 4.6 on terminal bench, MCP, and APEX math [28]. Concrete tooling: an open-source Claude Code Lark/Feishu Bridge for phone-driven multi-session CC [29], a ~20MB local Qwen2.5 runner [31], and Boris Cherny's podcast on correct CC setup [39]. Anecdotal: Codex one-shotting bugs CC couldn't [14][25], and a Claude outage briefly froze vibe-coders [35][36].

## Why it matters (reasoning)
The coder-model market is fragmenting fast: Composer 2.5 and Gemini 3.5 Flash prove cheap models can match frontier output for agentic coding, which collapses unit cost for any pipeline we automate. Anthropic's free certified curriculum [1] is a no-cost lever to standardize team skill on Claude Code/MCP — directly relevant since our daily-report and Almondo pipelines run on Claude Code. The Lark/Feishu bridge [29] is the first credible OSS pattern for phone-driven multi-session CC — a template we can fork for LINE/Discord control of our own agents. Second-order: dependence on a single vendor is risky (outage [35][36]), so Qwen 3.7 Max [28] and local-runner patterns [31] matter as fallback. Cursor at $3B run-rate [6] signals the IDE-agent category is here to stay and worth investing skill in.

## Possibility
Likely (70%): Composer 2.5 + Gemini 3.5 Flash become default 'cheap tier' routers in agent stacks within weeks; expect Claude Code/Cursor plugins that auto-route by task complexity. Likely (60%): Anthropic certifications become a hiring/credentialing signal in SEA dev shops by Q3 2026. Possible (40%): open-source CC bridges (Lark, LINE, Discord) proliferate — phone-first coding becomes a real workflow [2][24][29]. Possible (35%): Qwen 3.7 Max benchmarks hold up under independent eval, giving us a self-hostable Opus-class coder. Lower (20%): a Claude outage longer than this one [35] forces real multi-model fallback adoption.

## Org applicability — NDF DEV
High-value, low-cost moves now: (1) Enroll team in Anthropic's free Claude Code + Agentic AI courses [1][33] — direct skill lift for everyone building on CC/MCP. (2) Pilot Composer 2.5 in Cursor for Next.js/Supabase work [12][18] — likely cuts coding costs significantly vs Opus on routine tasks; keep Opus for hard refactors. (3) Fork/study the Lark/Feishu CC Bridge [29] as a template for LINE bridge to control social-daily-report and Almondo from phone — fits our mobile-first ops style. (4) Add Gemini 3.5 Flash as a cheap agent tier for daily-report summarization [13]. (5) Trial Qwen 3.7 Max via OpenRouter for Unity/XR code where context isn't sensitive [28]. Skip: vibe-coding-without-reading [2][3] (we ship to clients), and SpaceX/Musk noise [4][6]. Worth it overall — concrete artifacts here, not hype.

## Signals to Watch
- Watch Composer 2.5 independent reproducibility — if benchmarks hold, switch default coder [18]
- Watch Qwen 3.7 Max public weights/MCP support — could replace Opus for self-hosted runs [28]
- Watch Lark/Feishu Bridge repo for LINE/Discord forks we can adapt [29]
- Watch Cursor mobile app launch — may obsolete custom phone-CC tooling [34]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | Specialist_Engine522 | ^1795 c98 | [Anthropic officially launched 13+ FREE AI courses with certificates (Including A](https://www.reddit.com/r/ClaudeAI/comments/1tjpfh8/anthropic_officially_launched_13_free_ai_courses/) |
| reddit | thelocalnative | ^1754 c121 | [I'm a software engineer with a decade of experience. I vibe code all of my side ](https://www.reddit.com/r/ClaudeAI/comments/1tj2i90/im_a_software_engineer_with_a_decade_of/) |
| reddit | MankyMan0099 | ^1219 c74 | [from claude code to unicorn in 7 days day 1: opened claude code for the first ti](https://www.reddit.com/r/ClaudeAI/comments/1tjb8x9/from_claude_code_to_unicorn_in_7_days/) |
| reddit | fortune | ^895 c463 | [Elon Musk's pay package reveals what SpaceX actually is: a $1 trillion monster b](https://www.reddit.com/r/singularity/comments/1tjllk7/elon_musks_pay_package_reveals_what_spacex/) |
| reddit | SuggestionMission516 | ^823 c240 | [Google's latest creation: Gemini 3.5 Flash vs all [https://gemini.google.com/sha](https://www.reddit.com/r/singularity/comments/1tjoarz/googles_latest_creation_gemini_35_flash_vs_all/) |
| x | pitdesi | ^305 c8 | [Ok I guess we know why Elon is willing to pay 3% of SpaceX for Cursor. Cursor is](https://x.com/pitdesi/status/2057687588832759969) |
| reddit | Independent-Wind4462 | ^291 c103 | [Google is cooking just give them sometime (gemini 3.5 pro)](https://www.reddit.com/r/singularity/comments/1tjwaef/google_is_cooking_just_give_them_sometime_gemini/) |
| reddit | KindOfHardToSpell | ^239 c22 | [How misalignment starts](https://www.reddit.com/r/singularity/comments/1tjqnve/how_misalignment_starts/) |
| reddit | Distinct-Question-16 | ^217 c54 | [The new DEEP Robotics LynxS10 is very light, with only 20 kg you can even lift i](https://www.reddit.com/r/singularity/comments/1tjneie/the_new_deep_robotics_lynxs10_is_very_light_with/) |
| x | hqmank | ^189 c12 | [🎁More Cursor 50% off referral codes I found. Use: https://t.co/HHzyKRpq0f Replac](https://x.com/hqmank/status/2057695704567755138) |
| reddit | Competitive_Travel16 | ^187 c59 | [Leaked recording: Mark Zuckerberg Addresses Staff Ahead of Mass AI Layoffs](https://www.reddit.com/r/singularity/comments/1tjwa05/leaked_recording_mark_zuckerberg_addresses_staff/) |
| reddit | West-Welcome8247 | ^176 c68 | [Composer 2.5 is my new default. It is fast, accurate, and actually cheap ok so i](https://www.reddit.com/r/cursor/comments/1tijtom/composer_25_is_my_new_default_it_is_fast_accurate/) |
| reddit | Independent-Wind4462 | ^146 c35 | [Gemini 3.5 Flash ranks #1 on the APEX-Agents-AA benchmark, outperforming much la](https://www.reddit.com/r/singularity/comments/1tjlseu/gemini_35_flash_ranks_1_on_the_apexagentsaa/) |
| x | orangie | ^141 c37 | [codex fixed my bug in 1 shot that claude code couldn't figure out in 2 hours](https://x.com/orangie/status/2057672480391581857) |
| reddit | FateOfMuffins | ^139 c17 | [Erdos Unit Distance Problem - Gemini 3.1 Pro's interpretation](https://www.reddit.com/r/singularity/comments/1tkaydy/erdos_unit_distance_problem_gemini_31_pros/) |
| reddit | Distinct-Question-16 | ^133 c47 | [Figure AI celebrates 200 hours (8 days ~8 hours) of their humanoid robots handli](https://www.reddit.com/r/singularity/comments/1tkd0fk/figure_ai_celebrates_200_hours_8_days_8_hours_of/) |
| x | designtako | ^124 c1 | [Claude Code gets you to 90% of a design. Here's the 10% it can't see.](https://x.com/designtako/status/2057725656687943853) |
| reddit | No-Distribution9902 | ^107 c13 | [Artificial Analysis independent benchmark just found composer 2.5 to be the thir](https://www.reddit.com/r/cursor/comments/1tj7hyj/artificial_analysis_independent_benchmark_just/) |
| reddit | SnoozeDoggyDog | ^95 c62 | [Wall Street Journal: The American Rebellion Against AI Is Gaining Steam](https://www.reddit.com/r/singularity/comments/1tjnicf/wall_street_journal_the_american_rebellion/) |
| reddit | Evermoving- | ^85 c26 | [Donald Trump abruptly postpones AI order after White House infighting](https://www.reddit.com/r/singularity/comments/1tjxvhp/donald_trump_abruptly_postpones_ai_order_after/) |
| x | thruthesuburbs | ^85 c0 | [the ball of yarn as the cursor thing was so cute😭 https://t.co/MDbhWySc6e](https://x.com/thruthesuburbs/status/2057676436664635601) |
| reddit | InstaMatic80 | ^83 c28 | [I guess my prompt is too heavy 😳 My Mac started hyperventilating and then this a](https://www.reddit.com/r/cursor/comments/1tjf0p5/i_guess_my_prompt_is_too_heavy/) |
| x | Jeffar_AI | ^83 c21 | [Want to become a Claude Certified Architect in 6 weeks? 🚀 Here’s a simple roadma](https://x.com/Jeffar_AI/status/2057687515583361304) |
| x | Austen | ^72 c24 | [My biggest pet peeve of Claude Code on mobile is you can’t create a new repo. By](https://x.com/Austen/status/2057676261175054624) |
| x | gokulr | ^69 c27 | [Is it my imagination or is it true that if I tell Codex that the code is from Cl](https://x.com/gokulr/status/2057689090527760627) |
| reddit | zero0_one1 | ^62 c12 | [Grok 4.3 tops the Consistency Leaderboard in the LLM Sycophancy Benchmark, large](https://www.reddit.com/r/singularity/comments/1tjr3g5/grok_43_tops_the_consistency_leaderboard_in_the/) |
| x | hiarun02 | ^61 c29 | [Why does a $5 DeepSeek V4 run feel dangerously close to a $100 Claude Code run n](https://x.com/hiarun02/status/2057673846669590943) |
| x | boxmining | ^57 c8 | [TLDR: China is winning the AI race. @Alibaba_Qwen Qwen 3.7 Max just dropped. Bea](https://x.com/boxmining/status/2057696296874787062) |
| x | zarazhangrui | ^56 c10 | [Introducing the Claude Code Lark/Feishu Bridge 🌉 (open-source) Talk to Claude Co](https://x.com/zarazhangrui/status/2057710284920520906) |
| x | imitationflower | ^54 c1 | [@komosaur they should commission you if they want that neru cursor so bad ffs😭 e](https://x.com/imitationflower/status/2057695425147093492) |
