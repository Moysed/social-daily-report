---
type: social-topic-report
date: '2026-05-22'
topic: ai-news
lang: en
pair: ai-news.th.md
generated_at: '2026-05-22T10:17:15+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- rss
- x
regions:
- global
post_count: 65
salience: 0.82
sentiment: positive
confidence: 0.72
tags:
- claude-code
- cursor
- agent-frameworks
- open-source
- model-releases
- tooling
---

# AI News & New Skills — 2026-05-22

## TL;DR
- Anthropic dropped 13+ free certified AI courses incl. Claude Code & Agentic AI [1] — direct upskilling path for the team.
- Cursor Composer 2.5 ranks #3 on Artificial Analysis (behind Opus 4.7 Max & GPT 5.5), 10-60x cheaper [13][17] — viable default for routine coding.
- Open-source Claude Code Lark/Feishu Bridge lets you drive CC from mobile chat & manage multi-session via group chat [26] — plug-in candidate for our workflow.
- Gemini 3.5 Flash tops APEX-Agents-AA over larger models [14]; Qwen 3.7 Max beats Opus 4.6 on terminal-bench/MCP/math [24] — cheap agent backbones worth piloting.
- Cursor mobile agentic-coding app in development [30] — confirms phone-based vibe-coding trend [2].

## What happened
วันนี้สัญญาณหลักด้าน tooling: Anthropic เปิด 13+ free courses มี certificate ครอบคลุม Claude Code + Agentic AI [1] และมี roadmap Claude Certified Architect 6-week [19]. ฝั่ง coding agents — Cursor Composer 2.5 ขึ้นเป็น default ของหลายคน [13] และ Artificial Analysis วัดได้ที่ #3 รองจาก Opus 4.7 Max กับ GPT 5.5 ที่ราคา 10-60x ถูกกว่า [17]; Cursor revenue run-rate $3B [6] และเตรียมออก mobile app [30].

Model drops: Gemini 3.5 Flash #1 APEX-Agents-AA [5][14], Gemini 3.1 Pro แก้ Erdos unit distance [15], Qwen 3.7 Max แซง Opus 4.6 หลาย bench [24], Grok 4.3 นำ sycophancy consistency [25]. Open-source artifacts: Claude Code Lark/Feishu Bridge สำหรับ mobile + multi-session [26], Compute Local binary 20MB รัน qwen2.5 บน GPU [28]. Pattern signals: vibe-coding-from-phone workflow [2], coordination เป็น bottleneck ใหม่ [34], Claude outage โชว์ single-point-of-failure [31][32].

## Why it matters (reasoning)
Tooling layer ขยับเร็วกว่า model layer สำหรับเรา. Composer 2.5 + Qwen 3.7 + Gemini 3.5 Flash หมายถึง routine Unity/Next.js/Supabase scaffolding ทำได้ด้วย model ถูกลง 10-60x โดยไม่เสีย quality มาก — cost structure ของ AI-assisted dev เปลี่ยน. Lark/Feishu bridge [26] เปิดทาง mobile/remote ops กับ Claude Code โดยไม่ต้องรอ official Cursor mobile [30]. Anthropic free courses [1][19] ลด onboarding cost ของ junior dev ลงตรงๆ. Second-order: outage [31][32] ตอกย้ำว่าต้อง multi-provider fallback (Composer/Qwen/Gemini) — single-vendor lock-in มี operational risk จริง. Coordination bottleneck [34] บอกว่าการเพิ่ม agent ไม่ช่วยถ้า orchestration ไม่ดี — relevant กับ Almondo/social-daily-report architecture.

## Possibility
Likely (70%): Composer 2.5 + Gemini 3.5 Flash กลายเป็น default สำหรับ tier-2 tasks ภายใน Q3 2026, Opus reserved สำหรับงานยาก. Likely (60%): Lark/Feishu bridge pattern แตกเป็น Slack/Discord/LINE variants ใน 1-2 เดือน. Plausible (45%): Cursor mobile app ship Q3 ทำให้ phone-coding [2] กลายเป็น mainstream workflow. Uncertain (30%): Qwen 3.7 Max ใช้งานจริงเทียบ benchmark — China model adoption ในไทยติด compliance/data. Low (15%): regulatory pushback [18][20] กระทบ tooling availability ในระยะสั้น.

## Org applicability — NDF DEV
Worth it: (1) ให้ทีมลง Anthropic free courses [1] ตอนนี้ — ROI สูง, cost ศูนย์, มี cert ให้ลูกค้าดู. (2) ทดสอบ Composer 2.5 บน Next.js/Supabase work ของ NDF HR Page (N) + Employee Page (E) — ถ้า quality ผ่าน switch routine work ออกจาก Claude เพื่อลด cost. (3) Fork Claude Code Lark/Feishu bridge [26] — adapt เป็น LINE bridge สำหรับสั่งงาน CC จากมือถือตอนอยู่ site ลูกค้า (TM Muscle Gym G, EGAT V, Dej D). (4) Pilot Gemini 3.5 Flash เป็น agent backbone ใน social-daily-report — ราคา/throughput น่าจะดีกว่า Claude สำหรับ summarization. ไม่คุ้ม: Compute Local [28] — crypto-tied, ไม่จำเป็น; Qwen 3.7 รอ neutral benchmark ก่อน. งาน Unity/XR ไม่มี signal วันนี้ — keep Claude/Cursor as-is.

## Signals to Watch
- Composer 2.5 pricing & rate limits — track ว่ายัง 10-60x ถูกกว่า Opus จริงไหมหลัง ramp-up
- Lark/Feishu bridge repo activity + fork pattern → LINE/Slack variants
- Cursor mobile app beta access timeline
- Qwen 3.7 Max independent benchmarks (Artificial Analysis) ยืนยัน vendor claims [24]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **anthropics/claude-plugins-official** — Official, Anthropic-managed directory of high quality Claude Code Plugins.Claude Code Plugins Direct | rss | <https://github.com/anthropics/claude-plugins-official> |
| **colbymchenry/codegraph** — Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, and OpenCode — fewer tokens, fewer  | rss | <https://github.com/colbymchenry/codegraph> |
| **multica-ai/andrej-karpathy-skills** — A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations | rss | <https://github.com/multica-ai/andrej-karpathy-skills> |
| **dotnet/skills** — Repository for skills to assist AI coding agents with .NET and C#.NET Agent Skills This repository c | rss | <https://github.com/dotnet/skills> |
| **obra/superpowers** — An agentic skills framework & software development methodology that works.Superpowers Superpowers is | rss | <https://github.com/obra/superpowers> |
| **HKUDS/CLI-Anything** — "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/&nbsp; CLI-Anyth | rss | <https://github.com/HKUDS/CLI-Anything> |
| **rmyndharis/OpenWA** — Free, Open Source, Self-Hosted WhatsApp API Gateway OpenWA Open Source WhatsApp API Gateway Features | rss | <https://github.com/rmyndharis/OpenWA> |
| **ChromeDevTools/chrome-devtools-mcp** — Chrome DevTools for coding agentsChrome DevTools for agents Chrome DevTools for agents (chrome-devto | rss | <https://github.com/ChromeDevTools/chrome-devtools-mcp> |
| **rohitg00/ai-engineering-from-scratch** — Learn it. Build it. Ship it for others. ░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒ | rss | <https://github.com/rohitg00/ai-engineering-from-scratch> |
| **teng-lin/notebooklm-py** — Unofficial Python API and agentic skill for Google NotebookLM. Full programmatic access to NotebookL | rss | <https://github.com/teng-lin/notebooklm-py> |
| **can1357/oh-my-pi** — ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, brows | rss | <https://github.com/can1357/oh-my-pi> |
| **antoinezambelli/forge** — A Python framework for self-hosted LLM tool-calling and multi-step agentic workflowsforge A reliabil | rss | <https://github.com/antoinezambelli/forge> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | Specialist_Engine522 | ^1819 c99 | [Anthropic officially launched 13+ FREE AI courses with certificates (Including A](https://www.reddit.com/r/ClaudeAI/comments/1tjpfh8/anthropic_officially_launched_13_free_ai_courses/) |
| reddit | thelocalnative | ^1769 c121 | [I'm a software engineer with a decade of experience. I vibe code all of my side ](https://www.reddit.com/r/ClaudeAI/comments/1tj2i90/im_a_software_engineer_with_a_decade_of/) |
| reddit | MankyMan0099 | ^1217 c74 | [from claude code to unicorn in 7 days day 1: opened claude code for the first ti](https://www.reddit.com/r/ClaudeAI/comments/1tjb8x9/from_claude_code_to_unicorn_in_7_days/) |
| reddit | fortune | ^913 c463 | [Elon Musk's pay package reveals what SpaceX actually is: a $1 trillion monster b](https://www.reddit.com/r/singularity/comments/1tjllk7/elon_musks_pay_package_reveals_what_spacex/) |
| reddit | SuggestionMission516 | ^824 c241 | [Google's latest creation: Gemini 3.5 Flash vs all [https://gemini.google.com/sha](https://www.reddit.com/r/singularity/comments/1tjoarz/googles_latest_creation_gemini_35_flash_vs_all/) |
| x | pitdesi | ^325 c8 | [Ok I guess we know why Elon is willing to pay 3% of SpaceX for Cursor. Cursor is](https://x.com/pitdesi/status/2057687588832759969) |
| reddit | Independent-Wind4462 | ^299 c103 | [Google is cooking just give them sometime (gemini 3.5 pro)](https://www.reddit.com/r/singularity/comments/1tjwaef/google_is_cooking_just_give_them_sometime_gemini/) |
| reddit | KindOfHardToSpell | ^246 c22 | [How misalignment starts](https://www.reddit.com/r/singularity/comments/1tjqnve/how_misalignment_starts/) |
| reddit | Distinct-Question-16 | ^228 c80 | [Figure AI celebrates 200 hours (8 days ~8 hours) of their humanoid robots handli](https://www.reddit.com/r/singularity/comments/1tkd0fk/figure_ai_celebrates_200_hours_8_days_8_hours_of/) |
| reddit | Distinct-Question-16 | ^214 c54 | [The new DEEP Robotics LynxS10 is very light, with only 20 kg you can even lift i](https://www.reddit.com/r/singularity/comments/1tjneie/the_new_deep_robotics_lynxs10_is_very_light_with/) |
| x | hqmank | ^212 c12 | [🎁More Cursor 50% off referral codes I found. Use: https://t.co/HHzyKRpq0f Replac](https://x.com/hqmank/status/2057695704567755138) |
| reddit | Competitive_Travel16 | ^186 c59 | [Leaked recording: Mark Zuckerberg Addresses Staff Ahead of Mass AI Layoffs](https://www.reddit.com/r/singularity/comments/1tjwa05/leaked_recording_mark_zuckerberg_addresses_staff/) |
| reddit | West-Welcome8247 | ^176 c69 | [Composer 2.5 is my new default. It is fast, accurate, and actually cheap ok so i](https://www.reddit.com/r/cursor/comments/1tijtom/composer_25_is_my_new_default_it_is_fast_accurate/) |
| reddit | Independent-Wind4462 | ^148 c35 | [Gemini 3.5 Flash ranks #1 on the APEX-Agents-AA benchmark, outperforming much la](https://www.reddit.com/r/singularity/comments/1tjlseu/gemini_35_flash_ranks_1_on_the_apexagentsaa/) |
| reddit | FateOfMuffins | ^147 c18 | [Erdos Unit Distance Problem - Gemini 3.1 Pro's interpretation](https://www.reddit.com/r/singularity/comments/1tkaydy/erdos_unit_distance_problem_gemini_31_pros/) |
| x | designtako | ^124 c1 | [Claude Code gets you to 90% of a design. Here's the 10% it can't see.](https://x.com/designtako/status/2057725656687943853) |
| reddit | No-Distribution9902 | ^109 c13 | [Artificial Analysis independent benchmark just found composer 2.5 to be the thir](https://www.reddit.com/r/cursor/comments/1tj7hyj/artificial_analysis_independent_benchmark_just/) |
| reddit | SnoozeDoggyDog | ^94 c62 | [Wall Street Journal: The American Rebellion Against AI Is Gaining Steam](https://www.reddit.com/r/singularity/comments/1tjnicf/wall_street_journal_the_american_rebellion/) |
| x | Jeffar_AI | ^87 c21 | [Want to become a Claude Certified Architect in 6 weeks? 🚀 Here’s a simple roadma](https://x.com/Jeffar_AI/status/2057687515583361304) |
| reddit | Evermoving- | ^86 c26 | [Donald Trump abruptly postpones AI order after White House infighting](https://www.reddit.com/r/singularity/comments/1tjxvhp/donald_trump_abruptly_postpones_ai_order_after/) |
| x | thruthesuburbs | ^85 c0 | [the ball of yarn as the cursor thing was so cute😭 https://t.co/MDbhWySc6e](https://x.com/thruthesuburbs/status/2057676436664635601) |
| reddit | InstaMatic80 | ^84 c28 | [I guess my prompt is too heavy 😳 My Mac started hyperventilating and then this a](https://www.reddit.com/r/cursor/comments/1tjf0p5/i_guess_my_prompt_is_too_heavy/) |
| x | gokulr | ^70 c32 | [Is it my imagination or is it true that if I tell Codex that the code is from Cl](https://x.com/gokulr/status/2057689090527760627) |
| x | boxmining | ^67 c8 | [TLDR: China is winning the AI race. @Alibaba_Qwen Qwen 3.7 Max just dropped. Bea](https://x.com/boxmining/status/2057696296874787062) |
| reddit | zero0_one1 | ^59 c12 | [Grok 4.3 tops the Consistency Leaderboard in the LLM Sycophancy Benchmark, large](https://www.reddit.com/r/singularity/comments/1tjr3g5/grok_43_tops_the_consistency_leaderboard_in_the/) |
| x | zarazhangrui | ^59 c10 | [Introducing the Claude Code Lark/Feishu Bridge 🌉 (open-source) Talk to Claude Co](https://x.com/zarazhangrui/status/2057710284920520906) |
| x | willccbb | ^58 c8 | [switching back to Cursor Tab](https://x.com/willccbb/status/2057693490671452356) |
| x | Computebase | ^57 c13 | [You don't need OpenAI. You don't need Claude. You don't need a subscription. $Co](https://x.com/Computebase/status/2057715416995131744) |
| x | imitationflower | ^55 c1 | [@komosaur they should commission you if they want that neru cursor so bad ffs😭 e](https://x.com/imitationflower/status/2057695425147093492) |
| x | mark_k | ^51 c7 | [Cursor (@cursor_ai) is working on a mobile app for agentic AI coding. 🔥](https://x.com/mark_k/status/2057721972025356618) |
