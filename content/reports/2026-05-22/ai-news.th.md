---
type: social-topic-report
date: '2026-05-22'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-05-22T10:12:49+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- rss
- x
regions:
- global
post_count: 70
salience: 0.85
sentiment: positive
confidence: 0.7
tags:
- claude-code
- cursor
- gemini
- qwen
- agent-frameworks
- mcp
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-05-22

## TL;DR
- Anthropic ปล่อยคอร์ส AI ฟรีที่มีใบรับรอง 13+ คอร์ส รวมถึง Claude Code & Agentic AI — อัพสกิลทีมได้ตรง [1][23][32]
- Cursor Composer 2.5 ติดอันดับ #3 บน Artificial Analysis benchmarks ในราคาถูกกว่า Opus 4.7 / GPT-5.5 ถึง 10-60 เท่า — ใช้เป็น default สำหรับงาน coding ได้ [13][18][36]
- Gemini 3.5 Flash ครอง #1 บน APEX-Agents-AA แซงโมเดลใหญ่กว่า — ตัวเลือก agentic ราคาถูกที่ควรทดลองใช้ [5][15]
- มี open-source Claude Code Lark/Feishu Bridge ออกมาแล้ว — pattern นี้พอร์ตมาทำ LINE/Slack สำหรับ mobile CC session ได้ [29]
- Qwen 3.7 Max ชนะ Opus 4.6 ในด้าน terminal/MCP/math — open-weight จากจีนยังคงตามทันต่อเนื่อง [26]

## What happened
Anthropic ปล่อยคอร์สฝึกอบรมฟรีพร้อมใบรับรอง 13+ คอร์ส ครอบคลุม Claude API, Claude Code, MCP และ Agentic AI [1][23][32] Cursor Composer 2.5 เข้ามาเป็น frontier-tier coding model — อันดับ #3 บน Artificial Analysis ราคาถูกกว่า Opus 4.7 Max และ GPT-5.5 xHigh ถึง 10-60 เท่า และ power users เริ่มนำมาใช้เป็น default [13][18][36] Google ส่ง Gemini 3.5 Flash (#1 บน APEX-Agents-AA) และแง้มตัว 3.5 Pro [5][7][15][16] Qwen 3.7 Max ของ Alibaba รายงานว่าชนะ Opus 4.6 บน terminal bench/MCP/math [26] ผลงานที่จับต้องได้ ได้แก่ open-source Claude Code ↔ Lark/Feishu bridge สำหรับ mobile/group CC [29] และ Qwen2.5 runner ขนาด 20MB รันบนเครื่องตัวเอง [30] Boris Cherny (ผู้สร้าง Claude Code) เผยแพร่ podcast เรื่อง setup/usage [39] และ Claude มี outage หลายชั่วโมง [34][35]

## Why it matters (reasoning)
layer ของ coding agent กำลัง commoditize อย่างรวดเร็ว: Composer 2.5 และ Qwen 3.7 Max พิสูจน์ว่า frontier coding ระดับ 'good enough' ตอนนี้ถูกลง 10-60 เท่า ซึ่งส่งผลโดยตรงต่อค่าใช้จ่าย Claude Code ของเรา และความเต็มใจที่จะผูกติดกับ vendor เพียงรายเดียว [13][18][26] คอร์ส cert ฟรีของ Anthropic [1][23] คือเครื่องมืออัพสกิลที่ถูกที่สุดที่จะเห็นในไตรมาสนี้ — skills ถ่ายโอนมาใช้กับ Almondo/social-daily-report ได้ 1:1 Lark bridge [29] ยืนยัน pattern ที่เราใช้อยู่แล้ว (MQTT→Gemini, Oracle inbox) และให้ reference code สำหรับทำ LINE/Discord variant Outage [34][35] ตอกย้ำว่า dependency กับ provider รายเดียวเป็นความเสี่ยงระดับ production — multi-model routing ไม่ใช่ option อีกต่อไป

## Possibility
ความน่าจะเป็นสูง (~75%) ที่ Composer 2.5 / Gemini 3.5 Flash จะกลายเป็น 'cheap tier' มาตรฐานใน agent stack ภายใน 1-2 เดือน โดยสงวน Claude Opus ไว้สำหรับงานยาก ความน่าจะเป็นปานกลาง (~50%) ที่ Cursor จะส่ง mobile agentic app [33] มาแข่งกับ Claude Code mobile — อาจดึง workflow vibe-coding บนมือถือของเราไป [2][24] ความน่าจะเป็นต่ำกว่า (~30%) ที่ Qwen 3.7 Max จะกลายเป็นตัวเลือก offline/self-hosted ที่น่าเชื่อถือสำหรับงาน client ที่ sensitive (EGAT, gov edutech) ภายในไตรมาส ความถี่ของ outage [34][35] น่าจะผลักให้ทีมอื่น ๆ หันมาใช้ multi-provider router มากขึ้น

## Org applicability — NDF DEV
ทำได้เลยตอนนี้: (1) มอบหมายให้ทีมเรียน 2-3 คอร์สฟรีของ Anthropic [1] — ROI ตรงกับ Claude Code workflows บน NDF HR Page, Employee Page, VRoom (2) ทดลอง Composer 2.5 ใน Cursor สำหรับงาน Next.js/Supabase บน W (Dej Carving) และ E (Employee Page) — วัดผล cost/quality เทียบกับ Claude Code เป็นเวลา 1 สัปดาห์ [13][18] (3) Fork Lark bridge [29] มาเป็น reference สำหรับทำ LINE/Discord bridge เข้า Almondo — เข้ากับ MQTT pattern เดิมที่มีอยู่ (4) เพิ่ม Gemini 3.5 Flash เป็น cheap routing tier ใน social-daily-report สำหรับงาน bulk summarization [15] ข้าม: สัญญาณรบกวน SpaceX/Musk [4][6], Compute Local ที่มีกลิ่น crypto [30], การกบฏ AI ทางการเมือง [19][20]

## Signals to Watch
- รายงาน cost/quality จริงของ Composer 2.5 นอกเหนือจากกระแส benchmark
- การปล่อย weights ของ Qwen 3.7 Max และความเสถียรของ MCP tool-use
- ฟีเจอร์ Claude Code mobile — การสร้าง repo [24], การเปิดตัว Cursor mobile [33]
- pattern ของ multi-provider router ที่เกิดขึ้นหลัง Claude outage [34][35]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **anthropics/claude-plugins-official** — anthropics/claude-plugins-official Official, Anthropic-managed directory of high quality C | rss | <https://github.com/anthropics/claude-plugins-official> |
| **colbymchenry/codegraph** — colbymchenry/codegraph Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, an | rss | <https://github.com/colbymchenry/codegraph> |
| **multica-ai/andrej-karpathy-skills** — multica-ai/andrej-karpathy-skills A single CLAUDE.md file to improve Claude Code behavior, | rss | <https://github.com/multica-ai/andrej-karpathy-skills> |
| **dotnet/skills** — dotnet/skills Repository for skills to assist AI coding agents with .NET and C#.NET Agent  | rss | <https://github.com/dotnet/skills> |
| **obra/superpowers** — obra/superpowers An agentic skills framework & software development methodology that works | rss | <https://github.com/obra/superpowers> |
| **HKUDS/CLI-Anything** — HKUDS/CLI-Anything "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://cl | rss | <https://github.com/HKUDS/CLI-Anything> |
| **rmyndharis/OpenWA** — rmyndharis/OpenWA Free, Open Source, Self-Hosted WhatsApp API Gateway OpenWA Open Source W | rss | <https://github.com/rmyndharis/OpenWA> |
| **ChromeDevTools/chrome-devtools-mcp** — ChromeDevTools/chrome-devtools-mcp Chrome DevTools for coding agentsChrome DevTools for ag | rss | <https://github.com/ChromeDevTools/chrome-devtools-mcp> |
| **rohitg00/ai-engineering-from-scratch** — rohitg00/ai-engineering-from-scratch Learn it. Build it. Ship it for others. ░░░▒▒▒░░░▒▒▒░ | rss | <https://github.com/rohitg00/ai-engineering-from-scratch> |
| **teng-lin/notebooklm-py** — teng-lin/notebooklm-py Unofficial Python API and agentic skill for Google NotebookLM. Full | rss | <https://github.com/teng-lin/notebooklm-py> |
| **can1357/oh-my-pi** — can1357/oh-my-pi ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool  | rss | <https://github.com/can1357/oh-my-pi> |
| **antoinezambelli/forge** — antoinezambelli/forge A Python framework for self-hosted LLM tool-calling and multi-step a | rss | <https://github.com/antoinezambelli/forge> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | Specialist_Engine522 | ^1817 c98 | [Anthropic officially launched 13+ FREE AI courses with certificates (Including A](https://www.reddit.com/r/ClaudeAI/comments/1tjpfh8/anthropic_officially_launched_13_free_ai_courses/) |
| reddit | thelocalnative | ^1763 c121 | [I'm a software engineer with a decade of experience. I vibe code all of my side ](https://www.reddit.com/r/ClaudeAI/comments/1tj2i90/im_a_software_engineer_with_a_decade_of/) |
| reddit | MankyMan0099 | ^1217 c74 | [from claude code to unicorn in 7 days day 1: opened claude code for the first ti](https://www.reddit.com/r/ClaudeAI/comments/1tjb8x9/from_claude_code_to_unicorn_in_7_days/) |
| reddit | fortune | ^908 c463 | [Elon Musk's pay package reveals what SpaceX actually is: a $1 trillion monster b](https://www.reddit.com/r/singularity/comments/1tjllk7/elon_musks_pay_package_reveals_what_spacex/) |
| reddit | SuggestionMission516 | ^823 c241 | [Google's latest creation: Gemini 3.5 Flash vs all [https://gemini.google.com/sha](https://www.reddit.com/r/singularity/comments/1tjoarz/googles_latest_creation_gemini_35_flash_vs_all/) |
| x | pitdesi | ^320 c8 | [Ok I guess we know why Elon is willing to pay 3% of SpaceX for Cursor. Cursor is](https://x.com/pitdesi/status/2057687588832759969) |
| reddit | Independent-Wind4462 | ^300 c103 | [Google is cooking just give them sometime (gemini 3.5 pro)](https://www.reddit.com/r/singularity/comments/1tjwaef/google_is_cooking_just_give_them_sometime_gemini/) |
| reddit | KindOfHardToSpell | ^246 c22 | [How misalignment starts](https://www.reddit.com/r/singularity/comments/1tjqnve/how_misalignment_starts/) |
| reddit | Distinct-Question-16 | ^217 c54 | [The new DEEP Robotics LynxS10 is very light, with only 20 kg you can even lift i](https://www.reddit.com/r/singularity/comments/1tjneie/the_new_deep_robotics_lynxs10_is_very_light_with/) |
| reddit | Distinct-Question-16 | ^212 c76 | [Figure AI celebrates 200 hours (8 days ~8 hours) of their humanoid robots handli](https://www.reddit.com/r/singularity/comments/1tkd0fk/figure_ai_celebrates_200_hours_8_days_8_hours_of/) |
| x | hqmank | ^210 c12 | [🎁More Cursor 50% off referral codes I found. Use: https://t.co/HHzyKRpq0f Replac](https://x.com/hqmank/status/2057695704567755138) |
| reddit | Competitive_Travel16 | ^188 c59 | [Leaked recording: Mark Zuckerberg Addresses Staff Ahead of Mass AI Layoffs](https://www.reddit.com/r/singularity/comments/1tjwa05/leaked_recording_mark_zuckerberg_addresses_staff/) |
| reddit | West-Welcome8247 | ^174 c69 | [Composer 2.5 is my new default. It is fast, accurate, and actually cheap ok so i](https://www.reddit.com/r/cursor/comments/1tijtom/composer_25_is_my_new_default_it_is_fast_accurate/) |
| x | orangie | ^152 c42 | [codex fixed my bug in 1 shot that claude code couldn't figure out in 2 hours](https://x.com/orangie/status/2057672480391581857) |
| reddit | Independent-Wind4462 | ^147 c35 | [Gemini 3.5 Flash ranks #1 on the APEX-Agents-AA benchmark, outperforming much la](https://www.reddit.com/r/singularity/comments/1tjlseu/gemini_35_flash_ranks_1_on_the_apexagentsaa/) |
| reddit | FateOfMuffins | ^145 c18 | [Erdos Unit Distance Problem - Gemini 3.1 Pro's interpretation](https://www.reddit.com/r/singularity/comments/1tkaydy/erdos_unit_distance_problem_gemini_31_pros/) |
| x | designtako | ^124 c1 | [Claude Code gets you to 90% of a design. Here's the 10% it can't see.](https://x.com/designtako/status/2057725656687943853) |
| reddit | No-Distribution9902 | ^111 c13 | [Artificial Analysis independent benchmark just found composer 2.5 to be the thir](https://www.reddit.com/r/cursor/comments/1tj7hyj/artificial_analysis_independent_benchmark_just/) |
| reddit | SnoozeDoggyDog | ^96 c62 | [Wall Street Journal: The American Rebellion Against AI Is Gaining Steam](https://www.reddit.com/r/singularity/comments/1tjnicf/wall_street_journal_the_american_rebellion/) |
| reddit | Evermoving- | ^88 c26 | [Donald Trump abruptly postpones AI order after White House infighting](https://www.reddit.com/r/singularity/comments/1tjxvhp/donald_trump_abruptly_postpones_ai_order_after/) |
| reddit | InstaMatic80 | ^85 c28 | [I guess my prompt is too heavy 😳 My Mac started hyperventilating and then this a](https://www.reddit.com/r/cursor/comments/1tjf0p5/i_guess_my_prompt_is_too_heavy/) |
| x | thruthesuburbs | ^85 c0 | [the ball of yarn as the cursor thing was so cute😭 https://t.co/MDbhWySc6e](https://x.com/thruthesuburbs/status/2057676436664635601) |
| x | Jeffar_AI | ^84 c21 | [Want to become a Claude Certified Architect in 6 weeks? 🚀 Here's a simple roadma](https://x.com/Jeffar_AI/status/2057687515583361304) |
| x | Austen | ^75 c24 | [My biggest pet peeve of Claude Code on mobile is you can't create a new repo. By](https://x.com/Austen/status/2057676261175054624) |
| x | gokulr | ^70 c32 | [Is it my imagination or is it true that if I tell Codex that the code is from Cl](https://x.com/gokulr/status/2057689090527760627) |
| x | boxmining | ^65 c8 | [TLDR: China is winning the AI race. @Alibaba_Qwen Qwen 3.7 Max just dropped. Bea](https://x.com/boxmining/status/2057696296874787062) |
| x | hiarun02 | ^64 c29 | [Why does a $5 DeepSeek V4 run feel dangerously close to a $100 Claude Code run n](https://x.com/hiarun02/status/2057673846669590943) |
| reddit | zero0_one1 | ^59 c12 | [Grok 4.3 tops the Consistency Leaderboard in the LLM Sycophancy Benchmark, large](https://www.reddit.com/r/singularity/comments/1tjr3g5/grok_43_tops_the_consistency_leaderboard_in_the/) |
| x | zarazhangrui | ^59 c10 | [Introducing the Claude Code Lark/Feishu Bridge 🌉 (open-source) Talk to Claude Co](https://x.com/zarazhangrui/status/2057710284920520906) |
| x | Computebase | ^57 c13 | [You don't need OpenAI. You don't need Claude. You don't need a subscription. $Co](https://x.com/Computebase/status/2057715416995131744) |