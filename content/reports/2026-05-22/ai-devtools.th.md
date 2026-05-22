---
type: social-topic-report
date: '2026-05-22'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-05-22T06:15:24+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- hackernews
- reddit
- x
regions:
- global
post_count: 97
salience: 0.78
sentiment: mixed
confidence: 0.66
tags:
- coding-agents
- local-llm
- qwen
- claude-code
- ide-tooling
- agent-eval
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-05-22

## TL;DR
- Qwen3.6/3.7 momentum: 110 tok/s บน 12GB VRAM และเปลี่ยน workflow การ coding แบบ local [9][15][19]
- Google Antigravity IDE เจอกระแสต้าน 'bait and switch' — ความเสี่ยงด้านราคาและ lock-in สำหรับผู้นำไปใช้ [4]
- Claude Code skills ecosystem เติบโตต่อเนื่อง: Hallmark UI skill, pattern cheat-sheet (/skills, /agents, /plan) [32][39]
- Sandboxed team coding agents (Runtime YC) + onchain agent stack บ่งชี้ว่า infra layer กำลังก่อตัว [40][24][36]
- Embodied AI / 3D env generation (SimWorld Studio) — ยังเริ่มต้น แต่เกี่ยวข้องกับ XR/game pipeline [21]

## What happened
Open-weight coding model ยังคงลดช่องว่างต่อเนื่อง: Qwen3.6 35B-A3B ทำได้ 110 tok/s บน 12GB VRAM ผ่าน ik_llama.cpp [15] และนักพัฒนารายงานว่าใช้แทน cloud Codex สำหรับงานประจำวัน [19]; Qwen3.7 ถูกปล่อยข้อมูลล่วงหน้าว่าจะเป็นก้าวกระโดดถัดไป [9] ด้าน tooling, Google Antigravity IDE ถูกวิจารณ์อย่างหนักเรื่องการ bait-and-switch ด้านราคา/quota [4] ขณะที่ workflow ของ Claude Code แบบ skill/agent/plan/compact กำลังถูกรวบรวมเป็น pattern ที่แชร์ได้ [32] รวมถึง Hallmark ซึ่งเป็น open-source skill ที่ให้ agent มี design taste สำหรับการสร้าง UI [39] Runtime (YC P26) เปิดตัว sandboxed coding agents สำหรับทีม [40] และข้อมูลหลุดเกี่ยวกับ Gemini 3.2 Flash ชี้ถึง inference ระดับ coding ที่ถูกและเร็ว [31] ด้าน agent-infra: Terminal-Bench Science สำหรับ evaluate agent บน scientific workflow จริง [7], paper multi-stream LLM เรื่องการ parallelize prompt/think/IO [37], SimWorld Studio สำหรับ 3D env generation แบบ self-evolving [21] และ onchain agent stack จาก MultiversX/HeyAnon [24][36] นอกจากนี้: llama.cpp PR แก้ปัญหา OpenCode prompt-processing thrash [38] และ local Gemma4-31B สามารถ index วิดีโอหนึ่งปีบน 2021 MBP ได้ [11]

## Why it matters (reasoning)
แรงกดดันสองด้านกำลังบรรจบกัน: (a) open model แบบ local ใช้งานได้จริงสำหรับ coding/agent บน commodity GPU แล้ว [15][19][11] ลดการพึ่งพา closed API และ per-seat IDE pricing; (b) ความเชื่อถือต่อ closed-vendor กำลังสั่นคลอน — การปรับราคาของ Antigravity [4] และ narrative 'IBM-ification of Google' [26] ทำให้ studio ลังเลที่จะ standardize บน stack เดียว ผลสุทธิ: กลยุทธ์ที่สมเหตุสมผลคือ portable agent layer (Claude Code skills, MCP, sandboxed runner) บน model backend ที่เปลี่ยนได้ สำหรับ game/XR/edutech, การ generate synthetic env แบบ SimWorld [21] บ่งชี้ว่า 3D content pipeline จะถูก agent เสริมต่อจาก code เป็นลำดับถัดไป ผลทางอ้อม: ถ้า Gemini 3.2 Flash เป็นจริงตามที่อ้าง [31] ต้นทุนต่อ task สำหรับ in-editor agent จะลดลงราว 20× ผลักงาน PR ทั่วไปไปยัง background agent และทำให้ eval/observability แบบ Terminal-Bench [7] กลายเป็น bottleneck ที่แท้จริง

## Possibility
น่าจะเกิด (~70%): Qwen3.7 วางจำหน่ายภายในไม่กี่สัปดาห์ กลายเป็น local coder มาตรฐานสำหรับ studio ที่มี GPU ระดับกลาง; Claude Code skill marketplace รวมศูนย์รอบ skill ด้าน UI/design/test [32][39] เป็นไปได้ (~45%): กระแสต้าน Antigravity บีบให้ Google ปรับ quota แต่ความเสียหายด้านความเชื่อถือยังคงอยู่ [4][26] พอเป็นไปได้ (~35%): 3D env generator แบบ synthetic (ในแนวทาง SimWorld) ใช้งานได้จริงสำหรับ Unity/XR prototyping ภายใน Q4 [21] ต่ำ (~15%): onchain agent stack [24][36] ถึงระดับที่ studio ใช้งานได้ปีนี้ — ส่วนใหญ่ยังเป็น speculation/hype

## Org applicability — NDF DEV
นำไปใช้เลย: Claude Code + skills (/skills, /agents, /plan, /compact) เป็น workflow มาตรฐาน [32]; ทดลอง Hallmark skill สำหรับ Next.js landing page และ edutech UI scaffolding [39] ทดลองใช้: local Qwen3.6 35B-A3B บน dev box ขนาด 12–24GB สำหรับ code/doc generation แบบ offline และ PR draft [15][19] — ประกันราคาถูกสำหรับ API price shock จับตา อย่าเพิ่ง adopt: Antigravity (ความเสี่ยงด้านราคา [4]), onchain agent platform (ไม่เหมาะกับบริบท [24][36]), Tycoon 'AI CEO' (เป็นแค่ marketing [23]) Eval layer: นำ pattern จาก Terminal-Bench [7] มาออกแบบ task suite ภายในสำหรับ Unity/XR codegen ก่อนจะไว้ใจ agent บน production branch SimWorld Studio [21] ควรรีวิว one-pager สำหรับ R&D ด้าน XR content pipeline — ยังไม่พร้อม production

## Signals to Watch
- วันวางจำหน่าย Qwen3.7 open-weight + coding benchmark เทียบกับ Claude/GPT
- การแก้ไขราคา Antigravity และการตอบสนองของ Cursor/Cline [4]
- การเติบโตของ Claude Code skill registry — skill ด้าน design/test/refactor [32][39]
- การเปิดตัวอย่างเป็นทางการของ Gemini 3.2 Flash + คะแนน coding eval จริง [31]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| reddit | -p-e-w- | ^1709 c253 | [Heretic has been served a legal notice by Meta, Inc. To Whomsoever it May Concer](https://www.reddit.com/r/LocalLLaMA/comments/1tjmvx6/heretic_has_been_served_a_legal_notice_by_meta_inc/) |
| hackernews | sandebert | ^1112 c434 | [Flipper One – we need your help](https://blog.flipper.net/flipper-one-we-need-your-help/) |
| hackernews | speleo | ^778 c173 | [Project Hail Mary – Stellar Navigation Chart](https://valhovey.github.io/gaia-mary/) |
| hackernews | ssiddharth | ^628 c286 | [Google's Antigravity bait and switch](https://www.0xsid.com/blog/antigravity-bait-n-switch) |
| hackernews | sofumel | ^587 c525 | [We're testing new ad formats in Search and expanding our Direct Offers pilot](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/) |
| hackernews | napolux | ^560 c336 | [Throwing AI-generated walls of text into conversations](https://noslopgrenade.com/) |
| x | StevenDillmann | ^463 c15 | [📣 Announcing Terminal-Bench Science: benchmarking AI agents on real scientific w](https://x.com/StevenDillmann/status/2057144415513420049) |
| hackernews | root-parent | ^448 c178 | [Seattle Shield, an intelligence-sharing network operated by the Seattle police](https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/) |
| reddit | LegacyRemaster | ^429 c129 | [Waiting for Qwen 3.7 open weight... The new King has arrived... The hype is real](https://www.reddit.com/r/LocalLLaMA/comments/1tjvz6l/waiting_for_qwen_37_open_weight_the_new_king_has/) |
| hackernews | rbanffy | ^357 c171 | [Python 3.15: features that didn't make the headlines](https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html) |
| hackernews | asenna | ^347 c102 | [Indexing a year of video locally on a 2021 MacBook with Gemma4-31B (50GB swap)](https://blog.simbastack.com/indexed-a-year-of-video-locally/) |
| hackernews | pseudolus | ^326 c98 | [Lost Images from the 1945 Trinity Nuclear Test Restored](https://spectrum.ieee.org/trinity-nuclear-test) |
| hackernews | qaz_plm | ^297 c88 | [BBEdit 16](https://www.barebones.com/products/bbedit/bbedit16.html) |
| hackernews | mattas | ^292 c367 | [Waymo pauses Atlanta service as its robotaxis keep driving into floods](https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/) |
| reddit | janvitos | ^278 c93 | [110 tok/s with 12GB VRAM on Qwen3.6 35B A3B and ik_llama.cpp Had been getting [g](https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/) |
| hackernews | sanity | ^258 c142 | [Show HN: Freenet, a peer-to-peer platform for decentralized apps For the past 5 ](https://freenet.org/) |
| hackernews | jaredwiener | ^256 c88 | [News outlets are limiting the Internet Archive's access to their journalism](https://www.niemanlab.org/2026/05/more-than-340-local-news-outlets-are-limiting-the-internet-archives-access-to-their-journalism/) |
| hackernews | speckx | ^232 c125 | [Blog ran on Ubuntu 16.04 for 10 years. I migrated it to FreeBSD](https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/) |
| reddit | mouseofcatofschrodi | ^220 c53 | [Qwen3.6 35Ba3 has changed my workflows and even how I use my computer My workflo](https://www.reddit.com/r/LocalLLaMA/comments/1tjwrp7/qwen36_35ba3_has_changed_my_workflows_and_even/) |
| x | kaggle | ^200 c5 | [Join the 5-Day AI Agents: Intensive Vibe Coding Course with @Google! Learn from ](https://x.com/kaggle/status/2057457614116507829) |
| x | Lianhuiq | ^188 c8 | [Scaling embodied AI starts with automating the environments. Introducing SimWorl](https://x.com/Lianhuiq/status/2057165074532581695) |
| hackernews | speckx | ^177 c49 | [Using Kagi Search with Low Vision](https://veroniiiica.com/using-kagi-search-with-low-vision/) |
| x | testingcatalog | ^172 c17 | [Tycoon launched as the world's first operating system for one-person companies, ](https://x.com/testingcatalog/status/2057394368068083738) |
| x | MultiversX | ^170 c6 | [AI coding agents have become the primary authors of most software in 2026. We're](https://x.com/MultiversX/status/2057492868038611350) |
| hackernews | nchagnet | ^153 c87 | [Uv is fantastic, but its package management UX is a mess](https://www.loopwerk.io/articles/2026/uv-ux-mess/) |
| hackernews | sabatonfan | ^148 c120 | [The IBM-ification of Google?](https://zeroshot.bearblog.dev/google-is-shattering-under-its-own-weight-the-ibm-ification-of-google/) |
| hackernews | vcf | ^141 c136 | [Who wins and who loses in prediction markets? Evidence from Polymarket](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6443103) |
| x | Siron93 | ^133 c98 | [2996 customers later, it's time to release ScreensDesign V2 ! 3 months of work. ](https://x.com/Siron93/status/2057495617123844178) |
| hackernews | elffjs | ^132 c264 | [Spotify will start reserving concert tickets for fans](https://www.hollywoodreporter.com/music/music-industry-news/spotify-will-start-reserving-concert-tickets-for-superfans-1236603106/) |
| hackernews | d0ks | ^125 c119 | [The memory shortage is causing a repricing of consumer electronics](https://davidoks.blog/p/ai-is-killing-the-cheap-smartphone) |