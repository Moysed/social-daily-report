---
type: social-topic-report
date: '2026-05-22'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-05-22T06:49:31+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- reddit
- x
regions:
- global
post_count: 95
salience: 0.78
sentiment: mixed
confidence: 0.62
tags:
- coding-agents
- local-llm
- qwen
- claude-code
- gemini
- agent-ide
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-05-22

## TL;DR
- Google Antigravity ถูกกล่าวหาว่า bait-and-switch ด้านราคา/quota — ความน่าเชื่อถือของ agent IDE จาก Google สั่นคลอน [4][27]
- Qwen 3.7 open weights ใกล้ปล่อยแล้ว; Qwen3.6 35B-A3B ทำได้ถึง 110 tok/s บน VRAM 12GB — coding agent แบบ local ใช้ได้จริงบน laptop สาย studio [9][15][19]
- ข้อมูลหลุด Gemini 3.2 Flash คุณภาพอยู่ที่ ~92% ของ GPT-5.5 แต่ต้นทุน 1/20 — อาจเปลี่ยนโครงสร้างงบสำหรับการเรียก IDE/agent [32]
- workflow patterns ของ Claude Code (skills, agents, plan, compact, MCP, hooks) กำลังกลายเป็น playbook มาตรฐานสำหรับ agentic IDE [33]
- Terminal-Bench Science และ SimWorld Studio ผลักดัน evals/training ให้เกินกว่า coding task แบบง่าย — เกี่ยวข้องโดยตรงกับงาน XR/sim [7][21]

## What happened
Google Antigravity agent IDE เจอกระแสต่อต้านหนักจากสาธารณะ เพราะแอบปรับ quota และราคาหลังจากโปรโมตตอนเปิดตัว [4] ซึ่งซ้ำเติมบรรยากาศ 'IBM-ification of Google' ที่พูดถึงกันอยู่ [27] ฝั่ง local-LLM มีวันที่แข็งแกร่ง: Qwen 3.7 open weights ใกล้ออกแล้ว [9], Qwen3.6 35B-A3B ทำความเร็ว ~110 tok/s บน GPU 12GB ผ่าน ik_llama.cpp [15], และรายงาน workflow แสดงให้เห็นว่ามันสามารถแทน Codex-style flows ในงาน dev รายวันได้จริง [19] ข้อมูลหลุดระบุว่า Gemini 3.2 Flash ใกล้เคียง ~92% ของ GPT-5.5 ในราคาที่ถูกกว่า 1/20 [32] ส่วน Claude Code ของ Anthropic กำลังสร้าง agent playbook รอบ /skills, /agents, /plan, /compact, MCP, hooks และ memory ให้ชัดเจนขึ้น [33]

ด้าน evals และ environments, Terminal-Bench Science เปิด benchmark สำหรับ scientific workflow ที่ Anthropic/OpenAI/DeepMind ใช้กัน [7] และ SimWorld Studio นำเสนอ factory สำหรับสร้าง 3D environment แบบ self-evolving สำหรับ embodied agents — อยู่ติดกับ pipeline ของ Unity/XR โดยตรง [21] PR ของ llama.cpp แก้ปัญหา prompt-reprocessing ซ้ำซ้อนที่กระทบผู้ใช้ OpenCode/Pi มาตลอด [37] รายการที่เป็น noise (Tycoon 'AI CEO' [24], onchain coding agents [25], HeyAnon stack [39]) อ่านแล้วเป็นแค่การตลาด

## Why it matters (reasoning)
มีการเปลี่ยนแปลงเชิงโครงสร้างสองเรื่อง: (1) local coding model บน GPU ราคาถูกตอนนี้เร็วและดีพอที่ laptop 12GB จะรัน coding agent แบบ offline ได้ — ลด API spend และปลดล็อกงาน client ที่ติด NDA หรือ XR demo แบบ offline [15][19][37] (2) Cloud agent IDE กำลังเข้าสู่ช่วง shakeout ด้านราคาและความไว้วางใจ: การถอยเรื่อง quota ของ Antigravity [4] บวกกับ tier ราคาถูกของ Gemini Flash [32] หมายความว่าความเสี่ยงจาก lock-in กำลังสูงขึ้นในขณะที่ unit economics ยังขยับอยู่ ในแง่ second-order: studio ที่สร้าง abstraction บางๆ คร่อม model ต่างๆ (Claude Code, Gemini, Qwen-local) จะรักษา optionality ไว้ได้ ส่วน studio ที่ผูกติดกับ IDE ของ vendor รายใดรายหนึ่งก็จะรับการเปลี่ยนราคาครั้งถัดไปเต็มๆ สำหรับ XR/edutech, การสร้าง environment แบบ SimWorld [21] และ benchmark งาน scientific [7] บ่งชี้ว่า agentic content/level generation pipeline กำลังโตเกินกว่า chatbot demo แล้ว

## Possibility
น่าจะเกิด (≈70%): ภายใน 1–2 ไตรมาส Qwen 3.7 + ik_llama.cpp / runtime ที่คล้ายกัน จะทำให้ 'local Copilot' กลายเป็นมาตรฐานสำหรับ indie/SEA studio — สงวน Codex/Claude ไว้สำหรับงานยาก น่าจะเกิด (≈60%): Google ปรับราคาหรือ rebrand Antigravity หลังถูกต่อต้าน [4]; Gemini 3.2 Flash กลายเป็น cheap router target เริ่มต้น [32] เป็นไปได้ (≈40%): pattern skill/MCP/hooks ของ Claude Code [33] กลายเป็น spec แบบ portable ที่ IDE อื่นนำไปใช้ เป็นไปได้ (≈35%): generator แบบ SimWorld สำหรับ synthetic environment ออก Unity/Unreal exporter ซึ่งเป็นประโยชน์สำหรับ training data ของ XR [21] ไม่น่าเกิด (<20%): narrative ของ onchain coding agent [25][39] ได้รับ adoption จริงจากนักพัฒนา

## Org applicability — NDF DEV
แนวทางที่ทำได้จริงสำหรับ NDF DEV: (a) ตั้ง box Qwen3.6/3.7 35B-A3B แบบ local (GPU 12–24GB ตัวเดียว) เป็น shared studio coding agent สำหรับ Unity C#, Next.js และ Supabase scaffolding — ~110 tok/s เร็วพอสำหรับใช้ใน IDE [15][19] คุ้มค่า: สูง (b) นำ PR ของ llama.cpp เรื่อง prompt-processing ไปใช้กับ OpenCode/Pi ที่มีอยู่ [37] — แก้ง่าย ต้นทุนต่ำ (c) รับ playbook ของ Claude Code (/skills, /agents, /plan, /compact, MCP, hooks) มาเป็น convention agent ภายใน [33] เพื่อให้สลับ model ได้โดยไม่ต้องเขียน workflow ใหม่ (d) รอดูให้ราคา Antigravity นิ่งก่อนค่อยผูกงาน client แบบจ่ายเงิน [4] (e) ทดลอง Gemini 3.2 Flash (เมื่อ public) เป็น cheap router สำหรับงาน bulk — translation, edutech content gen, asset metadata [32] (f) ติดตาม SimWorld Studio สำหรับ XR training-scene generation [21]; ยังไม่ production-ready แต่คุ้มค่ากับการ spike 1 วัน ข้าม: 'AI CEO' OS [24], onchain agent platform [25][39]

## Signals to Watch
- วันที่ปล่อยและ license ของ Qwen 3.7 open-weights [9]
- ท่าทีของ Google ต่อกระแสต่อต้าน quota ของ Antigravity — คืนเงิน, ปรับราคา, หรือนิ่ง [4]
- การยืนยันราคา Gemini 3.2 Flash อย่างเป็นทางการเทียบกับข้อมูลหลุด [32]
- การปล่อย code ของ SimWorld Studio / แนวทาง Unity integration [21]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | -p-e-w- | ^1738 c254 | [Heretic has been served a legal notice by Meta, Inc. To Whomsoever it May Concer](https://www.reddit.com/r/LocalLLaMA/comments/1tjmvx6/heretic_has_been_served_a_legal_notice_by_meta_inc/) |
| hackernews | sandebert | ^1117 c437 | [Flipper One – we need your help](https://blog.flipper.net/flipper-one-we-need-your-help/) |
| hackernews | speleo | ^799 c176 | [Project Hail Mary – Stellar Navigation Chart](https://valhovey.github.io/gaia-mary/) |
| hackernews | ssiddharth | ^638 c289 | [Google's Antigravity bait and switch](https://www.0xsid.com/blog/antigravity-bait-n-switch) |
| hackernews | sofumel | ^592 c530 | [We're testing new ad formats in Search and expanding our Direct Offers pilot](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/) |
| hackernews | napolux | ^566 c343 | [Throwing AI-generated walls of text into conversations](https://noslopgrenade.com/) |
| x | StevenDillmann | ^464 c15 | [📣 Announcing Terminal-Bench Science: benchmarking AI agents on real scientific w](https://x.com/StevenDillmann/status/2057144415513420049) |
| hackernews | root-parent | ^451 c180 | [Seattle Shield, an intelligence-sharing network operated by the Seattle police](https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/) |
| reddit | LegacyRemaster | ^436 c132 | [Waiting for Qwen 3.7 open weight... The new King has arrived... The hype is real](https://www.reddit.com/r/LocalLLaMA/comments/1tjvz6l/waiting_for_qwen_37_open_weight_the_new_king_has/) |
| hackernews | rbanffy | ^361 c175 | [Python 3.15: features that didn't make the headlines](https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html) |
| hackernews | asenna | ^355 c103 | [Indexing a year of video locally on a 2021 MacBook with Gemma4-31B (50GB swap)](https://blog.simbastack.com/indexed-a-year-of-video-locally/) |
| hackernews | pseudolus | ^331 c99 | [Lost Images from the 1945 Trinity Nuclear Test Restored](https://spectrum.ieee.org/trinity-nuclear-test) |
| hackernews | qaz_plm | ^297 c88 | [BBEdit 16](https://www.barebones.com/products/bbedit/bbedit16.html) |
| hackernews | mattas | ^296 c370 | [Waymo pauses Atlanta service as its robotaxis keep driving into floods](https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/) |
| reddit | janvitos | ^285 c94 | [110 tok/s with 12GB VRAM on Qwen3.6 35B A3B and ik_llama.cpp Had been getting [g](https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/) |
| hackernews | sanity | ^262 c153 | [Show HN: Freenet, a peer-to-peer platform for decentralized apps For the past 5 ](https://freenet.org/) |
| hackernews | jaredwiener | ^261 c90 | [News outlets are limiting the Internet Archive's access to their journalism](https://www.niemanlab.org/2026/05/more-than-340-local-news-outlets-are-limiting-the-internet-archives-access-to-their-journalism/) |
| hackernews | speckx | ^247 c134 | [Blog ran on Ubuntu 16.04 for 10 years. I migrated it to FreeBSD](https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/) |
| reddit | mouseofcatofschrodi | ^233 c55 | [Qwen3.6 35Ba3 has changed my workflows and even how I use my computer My workflo](https://www.reddit.com/r/LocalLLaMA/comments/1tjwrp7/qwen36_35ba3_has_changed_my_workflows_and_even/) |
| x | kaggle | ^203 c5 | [Join the 5-Day AI Agents: Intensive Vibe Coding Course with @Google! Learn from ](https://x.com/kaggle/status/2057457614116507829) |
| x | Lianhuiq | ^190 c8 | [Scaling embodied AI starts with automating the environments. Introducing SimWorl](https://x.com/Lianhuiq/status/2057165074532581695) |
| hackernews | speckx | ^181 c53 | [Using Kagi Search with Low Vision](https://veroniiiica.com/using-kagi-search-with-low-vision/) |
| x | KullAxel | ^177 c6 | [Agent benchmark not coding benchmark. I have seeen a lot of people criticizing G](https://x.com/KullAxel/status/2057491514490823095) |
| x | testingcatalog | ^172 c17 | [Tycoon launched as the world's first operating system for one-person companies, ](https://x.com/testingcatalog/status/2057394368068083738) |
| x | MultiversX | ^171 c6 | [AI coding agents have become the primary authors of most software in 2026. We're](https://x.com/MultiversX/status/2057492868038611350) |
| hackernews | nchagnet | ^167 c90 | [Uv is fantastic, but its package management UX is a mess](https://www.loopwerk.io/articles/2026/uv-ux-mess/) |
| hackernews | sabatonfan | ^154 c122 | [The IBM-ification of Google?](https://zeroshot.bearblog.dev/google-is-shattering-under-its-own-weight-the-ibm-ification-of-google/) |
| hackernews | vcf | ^141 c136 | [Who wins and who loses in prediction markets? Evidence from Polymarket](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6443103) |
| x | Siron93 | ^137 c99 | [2996 customers later, it's time to release ScreensDesign V2 ! 3 months of work. ](https://x.com/Siron93/status/2057495617123844178) |
| hackernews | elffjs | ^134 c272 | [Spotify will start reserving concert tickets for fans](https://www.hollywoodreporter.com/music/music-industry-news/spotify-will-start-reserving-concert-tickets-for-superfans-1236603106/) |