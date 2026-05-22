---
type: social-topic-report
date: '2026-05-22'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-05-22T10:16:15+00:00'
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
post_count: 79
salience: 0.78
sentiment: mixed
confidence: 0.62
tags:
- coding-agents
- open-weights
- qwen
- gemini
- local-llm
- agent-eval
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-05-22

## TL;DR
- โมเดล open-weight Qwen 3.6/3.7 ที่รันได้ 110 tok/s บน VRAM 12GB กำลังเปลี่ยนรูปแบบ local coding workflow ไปมาก [8][16][20]
- Google Antigravity ถูกกล่าวหาว่าทำ bait-and-switch ด้านราคา/quota ส่งผลให้ความเชื่อใจของผู้ใช้ agentic IDE สั่นคลอน [5]
- ข้อมูลหลุด Gemini 3.2 Flash อ้างคุณภาพ 92% ของ GPT-5.5 ในราคา 1/20 — ถ้าเป็นจริงจะเปลี่ยน TCO ครั้งใหญ่ [35]
- Meta ส่ง legal notice ถึง Heretic (เครื่องมือ uncensoring) สัญญาณว่าแรงกดดันต่อ open-weight tooling เพิ่มขึ้น [1]
- Paper Terminal-Bench Science + Multi-Stream LLM ผลักดัน agent eval และ parallel inference ให้ก้าวหน้าขึ้น [9][38]

## What happened
โมเมนตัมฝั่ง open-weight ครองเวที: Qwen3.6 35B-A3B รันได้ 110 tok/s บน GPU 12GB ผ่าน ik_llama.cpp [16] และนักพัฒนารายงานว่าเริ่มแทนที่ cloud Codex สำหรับงานประจำแล้ว [20]; Qwen 3.7 ถูกปล่อยข่าวว่าเป็นก้าวถัดไป [8] ฝั่ง closed model: Google Antigravity เจอเสียงวิจารณ์ 'bait and switch' จากการเปลี่ยนเงื่อนไขหลัง launch [5] ขณะที่ benchmark หลุดของ Gemini 3.2 Flash อ้างคุณภาพใกล้เคียง GPT-5.5 ในราคาราว 5% [35] ข่าว tooling/eval: Terminal-Bench Science เปิด agent benchmark บน scientific workflow จริงที่ Anthropic/OpenAI/DeepMind ใช้งาน [9]; paper Multi-Stream LLM เสนอการ parallelize stream ของ prompt/thinking/I/O [38] แรงเสียดทานด้าน legal/ecosystem: Meta ส่ง legal notice ถึงโปรเจกต์ Heretic ที่ทำ decensoring [1] เรื่องที่เกี่ยวข้อง: cheat-sheet ของ Claude Code กำลังแพร่หลายพร้อม workflow /skills /agents /plan [34], OpenCode ออก fix ด้าน prompt-processing สำหรับผู้ใช้ llama.cpp [40] และ SimWorld Studio มุ่งสู่ 3D environment ที่พัฒนาตัวเองได้สำหรับ embodied agent [25]

## Why it matters (reasoning)
สองแรงกำลังชนกัน (1) Local inference กำลังข้ามเส้น 'good enough for coding' บน consumer GPU [16][20] ซึ่งกัดกร่อนความได้เปรียบของ paid coding agent และเปิดทางให้สตูดิโอรัน private agent บนเครื่อง dev ที่มีอยู่แล้ว (2) ผู้ให้บริการ closed model กำลังลดราคาพร้อมกัน (Gemini 3.2 Flash [35]) และขันน็อตเงื่อนไขเชิงพาณิชย์ (Antigravity [5]) — หมายความว่าเส้นทางถูกกว่ามาพร้อม policy/lock-in risk ด้วย Meta vs Heretic [1] แสดงให้เห็นว่าผู้เล่นรายใหญ่จะใช้แรงกดดันทางกฎหมาย ไม่ใช่แค่ license เพื่อต้านเครื่องมือที่บ่อนทำลาย alignment guardrail — เกี่ยวข้องโดยตรงถ้าคุณพึ่งพา uncensored derivative weight ความสุกงอมของ eval (Terminal-Bench Science [9]) และการวิจัย parallel inference [38] บ่งชี้ว่า 6 เดือนข้างหน้าจะเป็นเรื่อง agent reliability และ latency ไม่ใช่คุณภาพโมเดลดิบ

## Possibility
Likely (>60%): Qwen 3.7 open weight จะปล่อยภายในไม่กี่สัปดาห์และกลายเป็น local coding model มาตรฐานของสตูดิโอที่มี GPU ระดับ RTX 4070+/5070 Likely (~55%): Gemini 3.2 Flash ถ้าข้อมูลหลุดเป็นจริง จะจุดสงครามราคาที่ดึง Anthropic/OpenAI ระดับ Haiku-tier ลงราว 30-50% ภายใน Q3 2026 Plausible (~40%): Meta-style legal action ต่อโปรเจกต์ decensoring/distillation เพิ่มขึ้น ทำให้ HuggingFace fork บางส่วนชะงัก Lower (~25%): เสียงวิจารณ์แบบ Antigravity บีบให้ agentic IDE vendor (Cursor, Windsurf, Antigravity) ต้องชี้แจง SLA ชัดขึ้น

## Org applicability — NDF DEV
แนวทางเชิงปฏิบัติสำหรับ NDF DEV: (a) ทดลองใช้ Qwen3.6 35B-A3B บนเครื่อง workstation หนึ่งเครื่องผ่าน ik_llama.cpp [16] สำหรับ scaffolding Unity C#, boilerplate Next.js/Supabase และร่างเนื้อหา edutech ภาษาไทย — ไม่มีค่าใช้จ่ายต่อ seat และข้อมูลอยู่ภายในสตูดิโอ (b) มอง Antigravity/Cursor ว่าเปลี่ยนแทนได้; รักษา agent workflow ให้ portable (pattern Claude Code /skills + MCP [34] ใช้ได้ข้ามหลาย vendor) (c) สำหรับ edutech ที่ต้องคุมต้นทุนฝั่ง client ให้ prototype กับ Gemini 3.2 Flash เมื่อ GA — อาจลด LLM bill ลง ~20x สำหรับ content generation pipeline (d) หลีกเลี่ยงการสร้างบน uncensored/Heretic-derived weight สำหรับ deliverable ใดๆ [1] — ความเสี่ยงด้าน IP (e) SimWorld Studio [25] น่าติดตามสำหรับ use case XR/VR training-sim แต่ยังเร็วเกินไปที่จะนำมาใช้ ไม่คุ้ม: ไล่ตาม Qwen ทุก point release; เลือก update รายไตรมาสแทน

## Signals to Watch
- วันที่ปล่อย Qwen 3.7 open-weight และเงื่อนไข license [8]
- ยืนยันหรือไม่ว่าข้อมูลหลุดราคา Gemini 3.2 Flash [35] ถูกต้องในงาน Google I/O follow-up
- การแก้ไข Antigravity ToS หรือนโยบายคืนเงินหลังเสียงวิจารณ์ [5]
- ผลลัพธ์ Meta vs Heretic — กำหนดบรรทัดฐานสำหรับ open-weight derivative [1]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **eigenpal/docx-editor** — Show HN: Open-source .docx editor library for building document apps We are working on an open-sourc | hackernews | <https://github.com/eigenpal/docx-editor> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | -p-e-w- | ^1847 c277 | [Heretic has been served a legal notice by Meta, Inc. To Whomsoever it May Concer](https://www.reddit.com/r/LocalLLaMA/comments/1tjmvx6/heretic_has_been_served_a_legal_notice_by_meta_inc/) |
| hackernews | tedsanders | ^1388 c1015 | [An OpenAI model has disproved a central conjecture in discrete geometry <a href=](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) |
| hackernews | sandebert | ^1158 c444 | [Flipper One – we need your help](https://blog.flipper.net/flipper-one-we-need-your-help/) |
| hackernews | speleo | ^925 c201 | [Project Hail Mary – Stellar Navigation Chart](https://valhovey.github.io/gaia-mary/) |
| hackernews | ssiddharth | ^684 c305 | [Google's Antigravity bait and switch](https://www.0xsid.com/blog/antigravity-bait-n-switch) |
| hackernews | napolux | ^617 c356 | [Throwing AI-generated walls of text into conversations](https://noslopgrenade.com/) |
| hackernews | sofumel | ^607 c541 | [We're testing new ad formats in Search and expanding our Direct Offers pilot](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/) |
| reddit | LegacyRemaster | ^525 c151 | [Waiting for Qwen 3.7 open weight... The new King has arrived... The hype is real](https://www.reddit.com/r/LocalLLaMA/comments/1tjvz6l/waiting_for_qwen_37_open_weight_the_new_king_has/) |
| x | StevenDillmann | ^467 c15 | [📣 Announcing Terminal-Bench Science: benchmarking AI agents on real scientific w](https://x.com/StevenDillmann/status/2057144415513420049) |
| hackernews | root-parent | ^461 c188 | [Seattle Shield, an intelligence-sharing network operated by the Seattle police](https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/) |
| hackernews | asenna | ^383 c115 | [Indexing a year of video locally on a 2021 MacBook with Gemma4-31B (50GB swap)](https://blog.simbastack.com/indexed-a-year-of-video-locally/) |
| hackernews | rbanffy | ^377 c187 | [Python 3.15: features that didn't make the headlines](https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html) |
| hackernews | pseudolus | ^352 c104 | [Lost Images from the 1945 Trinity Nuclear Test Restored](https://spectrum.ieee.org/trinity-nuclear-test) |
| hackernews | mattas | ^316 c393 | [Waymo pauses Atlanta service as its robotaxis keep driving into floods](https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/) |
| hackernews | qaz_plm | ^304 c94 | [BBEdit 16](https://www.barebones.com/products/bbedit/bbedit16.html) |
| reddit | janvitos | ^303 c97 | [110 tok/s with 12GB VRAM on Qwen3.6 35B A3B and ik_llama.cpp Had been getting [g](https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/) |
| hackernews | speckx | ^291 c151 | [Blog ran on Ubuntu 16.04 for 10 years. I migrated it to FreeBSD](https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/) |
| hackernews | sanity | ^287 c175 | [Show HN: Freenet, a peer-to-peer platform for decentralized apps For the past 5 ](https://freenet.org/) |
| hackernews | jaredwiener | ^287 c99 | [News outlets are limiting the Internet Archive's access to their journalism](https://www.niemanlab.org/2026/05/more-than-340-local-news-outlets-are-limiting-the-internet-archives-access-to-their-journalism/) |
| reddit | mouseofcatofschrodi | ^278 c69 | [Qwen3.6 35Ba3 has changed my workflows and even how I use my computer My workflo](https://www.reddit.com/r/LocalLLaMA/comments/1tjwrp7/qwen36_35ba3_has_changed_my_workflows_and_even/) |
| hackernews | bambax | ^275 c53 | [The Letter S, by Donald Knuth (1980) [pdf]](https://gwern.net/doc/design/typography/1980-knuth.pdf) |
| x | kaggle | ^225 c5 | [Join the 5-Day AI Agents: Intensive Vibe Coding Course with @Google! Learn from ](https://x.com/kaggle/status/2057457614116507829) |
| hackernews | d0ks | ^210 c229 | [The memory shortage is causing a repricing of consumer electronics](https://davidoks.blog/p/ai-is-killing-the-cheap-smartphone) |
| hackernews | nchagnet | ^210 c109 | [Uv is fantastic, but its package management UX is a mess](https://www.loopwerk.io/articles/2026/uv-ux-mess/) |
| x | Lianhuiq | ^208 c10 | [Scaling embodied AI starts with automating the environments. Introducing SimWorl](https://x.com/Lianhuiq/status/2057165074532581695) |
| hackernews | speckx | ^202 c67 | [Using Kagi Search with Low Vision](https://veroniiiica.com/using-kagi-search-with-low-vision/) |
| x | KullAxel | ^190 c6 | [Agent benchmark not coding benchmark. I have seeen a lot of people criticizing G](https://x.com/KullAxel/status/2057491514490823095) |
| x | MultiversX | ^183 c6 | [AI coding agents have become the primary authors of most software in 2026. We're](https://x.com/MultiversX/status/2057492868038611350) |
| x | testingcatalog | ^175 c17 | [Tycoon launched as the world's first operating system for one-person companies, ](https://x.com/testingcatalog/status/2057394368068083738) |
| reddit | noprompt | ^161 c21 | [When your LLM treats data center GPUs like an optional DLC](https://www.reddit.com/r/LocalLLaMA/comments/1tk4gyy/when_your_llm_treats_data_center_gpus_like_an/) |