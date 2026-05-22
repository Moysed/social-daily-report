---
type: social-topic-report
date: '2026-05-22'
topic: ai-devtools
lang: th
pair: ai-devtools.en.md
generated_at: '2026-05-22T09:42:47+00:00'
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
post_count: 81
salience: 0.82
sentiment: mixed
confidence: 0.62
tags:
- coding-agents
- local-llm
- qwen
- claude-code
- gemini
- agent-eval
translated_by: claude-sonnet-4-6
---

# AI Devtools — 2026-05-22

## TL;DR
- คลื่น Qwen 3.6/3.7 ปรับโฉม local-LLM coding: 35B-A3B ทำได้ ~110 tok/s บน VRAM 12GB และกำลังเปลี่ยน workflow ของนักพัฒนาจริงๆ [8][16][21]
- Google Antigravity โดนวิจารณ์หนัก — 'bait and switch' ด้านราคา/quota ทำให้ผู้ใช้กลุ่มแรกของ agentic IDE เจ็บปวด [5]
- workflow ของ Claude Code skills/agents/plan/MCP กำลังตกผลึกเป็น pattern มาตรฐานสำหรับการใช้งาน coding-agent จริงจัง [34]
- ข้อมูลหลุด Google Gemini 3.2 Flash อ้างคุณภาพ ~92% ของ GPT-5.5 ที่ต้นทุน ~1/20 — tier ถูก-เร็วสำคัญมากสำหรับ game/XR/web tooling [35]
- SimWorld Studio (โรงงานสภาพแวดล้อม 3D แบบ self-evolving) + Terminal-Bench Science ชี้ให้เห็นว่าการประเมิน agent กำลังมุ่งสู่ workflow จริงแบบ embodied [9][23]

## สิ่งที่เกิดขึ้น
local open-weight coding stack กระโดดขึ้นอีกครั้ง: Qwen 3.6 35B-A3B กับ ik_llama.cpp ทำได้ ~110 tok/s บน GPU 12GB [16], ผู้ใช้รายงานว่ามันได้ปรับโครงสร้าง workflow ประจำวันของตนรอบ ๆ การมอบหมายงานแบบ Codex [21], และ Qwen 3.7 ถูกโชว์ตัวว่าเป็น open model SOTA ตัวใหม่ [8] ฝั่ง proprietary, Google Antigravity agentic IDE โดนวิจารณ์สาธารณะเรื่อง 'bait and switch' ด้านราคา/quota [5], ขณะที่ข้อมูลหลุดของ Gemini 3.2 Flash อ้างคุณภาพ coding ระดับ near-frontier ที่ต้นทุน ~1/20 [35] pattern ของ Claude Code skills/agents/plan/MCP/hooks กำลังถูกรวบรวมเป็น cheat sheet [34] สัญญาณด้าน tooling/eval: Terminal-Bench Science ทดสอบ agent บน scientific pipeline จริง [9], SimWorld Studio สร้างสภาพแวดล้อม 3D อัตโนมัติเพื่อฝึก embodied agent [23], paper Multi-Stream LLM ทำงานแบบขนานสำหรับ prompt/thinking/I/O [36], และ Gemma4-31B local ทำดัชนีวิดีโอหนึ่งปีบน MacBook โดยใช้ swap 50GB [11] สิ่งที่เป็นแค่ noise: 'AI CEO Astra' ของ Tycoon [29] และ 'agents onchain' ของ Multiversx [28] ส่วนใหญ่เป็นการตลาด

## ทำไมถึงสำคัญ (การวิเคราะห์)
สองแนวโน้มกำลังบรรจบกันสำหรับ studio ขนาดเล็ก ประการแรก local-coding-agent stack ดีพอสำหรับงานใกล้ production แล้ว — MoE model 35B ที่ 100+ tok/s บน consumer GPU หมายความว่า studio ในเชียงใหม่สามารถรัน Codex-equivalent ภายในองค์กรได้โดยไม่ต้องจ่ายค่า SaaS รายที่นั่ง [16][21] ประการที่สอง ตลาด hosted agent-IDE กำลังกระจายตัวและถูกลง: ความผิดพลาดของ Antigravity [5] บวกกับ Gemini Flash tier ราคาถูก [35] หมายความว่าความเสี่ยงจาก lock-in มีจริงแต่ switching cost กำลังลดลง ผลกระทบลำดับที่สอง: (a) การประเมิน eval กำลังย้ายจาก coding task ของเล่นสู่ workflow จริง (Terminal-Bench Science [9], SimWorld สำหรับ embodied [23]) — การเลือกเครื่องมือจาก HumanEval score นั้นล้าสมัยแล้ว; (b) pattern skill/MCP ของ Claude Code [34] กำลังกลายเป็นภาษากลางสำหรับ agent orchestration ซึ่งคุ้มค่าที่จะทำให้เป็นมาตรฐาน โดยไม่ขึ้นกับ model vendor; (c) การตั้งราคา memory/DRAM ใหม่ [26] จะค่อยๆ ดันต้นทุน local-LLM rig และ dev workstation ขึ้นตลอดปี 2026

## ความเป็นไปได้
มีแนวโน้มสูง (70%): ภายใน Q3 2026, open model ระดับ Qwen-3.7 + ik_llama.cpp + harness แบบ Claude-Code จะกลายเป็น 'cheap tier' มาตรฐานสำหรับ indie/studio dev โดย Sonnet/GPT-5.x ที่ hosted จะสงวนไว้สำหรับงานยาก เป็นไปได้ (45%): Google ส่ง Gemini 3.2 Flash ในราคาที่หลุดออกมา [35] ซึ่งบังคับให้ Anthropic/OpenAI ลดราคา mid-tier — ผลบวกสุทธิสำหรับ studio เป็นไปได้ (30%): backlash แบบ Antigravity [5] ผลักดัน developer มากขึ้นไปสู่ portable, MCP-based agent tooling แทน vendor IDE มีโอกาสน้อย (20%): การสร้าง auto-env แบบ SimWorld [23] มาถึง pipeline ของ Unity/Unreal ใน 6-9 เดือน ซึ่งมีประโยชน์สำหรับการฝึก XR/game agent และ procedural content

## การประยุกต์ใช้กับองค์กร — NDF DEV
แนวทางปฏิบัติจริงสำหรับ NDF DEV: (1) ทดลอง Qwen 3.6/3.7 35B-A3B บน GPU box 12-16GB หนึ่งเครื่องเป็น shared internal coding agent สำหรับ Next.js/Supabase tickets และการสร้างโครง Unity C# [16][21] — ตั้งค่าประมาณ 1-2 วัน ต้นทุน marginal แทบศูนย์ (2) กำหนดมาตรฐาน pattern skills/agents/plan/MCP ของ Claude Code [34] สำหรับสมาชิกในทีมทุกคน เพื่อให้ workflow พกพาได้ข้าม Claude/Gemini/local backend (3) จับตา Gemini 3.2 Flash pricing [35] — ถ้าจริง ให้แทนที่ cheap-tier model ใน e-learning content pipeline ใดก็ตาม (bulk grading, lesson generation) (4) ข้าม Antigravity ไปก่อน [5]; กลับมาพิจารณาหลังราคาเสถียร (5) ข้าม Tycoon/MultiversX [28][29] — การตลาด ไม่ใช่ infra SimWorld [23] คุ้มค่าที่จะ bookmark ไว้สำหรับการฝึก NPC ด้วย XR/VR agent ใน 6+ เดือนข้างหน้า ไม่ใช่ตอนนี้

## สัญญาณที่ต้องจับตา
- วันที่ปล่อย Qwen 3.7 open-weight และ benchmark เทียบกับ Sonnet 4.6 บน coding จริง
- ราคาอย่างเป็นทางการและ rate limit ของ Gemini 3.2 Flash ถ้า/เมื่อประกาศ
- การตอบสนองด้านราคาของ Antigravity และการคืน free-tier ใดๆ [5]
- เส้นโค้งราคา DRAM/VRAM ตลอด Q3 2026 — ส่งผลต่อต้นทุน local-LLM rig [26]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| reddit | -p-e-w- | ^1830 c273 | [Heretic has been served a legal notice by Meta, Inc. To Whomsoever it May Concer](https://www.reddit.com/r/LocalLLaMA/comments/1tjmvx6/heretic_has_been_served_a_legal_notice_by_meta_inc/) |
| hackernews | tedsanders | ^1387 c1012 | [An OpenAI model has disproved a central conjecture in discrete geometry <a href=](https://openai.com/index/model-disproves-discrete-geometry-conjecture/) |
| hackernews | sandebert | ^1152 c444 | [Flipper One – we need your help](https://blog.flipper.net/flipper-one-we-need-your-help/) |
| hackernews | speleo | ^901 c197 | [Project Hail Mary – Stellar Navigation Chart](https://valhovey.github.io/gaia-mary/) |
| hackernews | ssiddharth | ^678 c300 | [Google's Antigravity bait and switch](https://www.0xsid.com/blog/antigravity-bait-n-switch) |
| hackernews | napolux | ^609 c353 | [Throwing AI-generated walls of text into conversations](https://noslopgrenade.com/) |
| hackernews | sofumel | ^604 c540 | [We're testing new ad formats in Search and expanding our Direct Offers pilot](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/) |
| reddit | LegacyRemaster | ^509 c147 | [Waiting for Qwen 3.7 open weight... The new King has arrived... The hype is real](https://www.reddit.com/r/LocalLLaMA/comments/1tjvz6l/waiting_for_qwen_37_open_weight_the_new_king_has/) |
| x | StevenDillmann | ^466 c15 | [📣 Announcing Terminal-Bench Science: benchmarking AI agents on real scientific w](https://x.com/StevenDillmann/status/2057144415513420049) |
| hackernews | root-parent | ^459 c187 | [Seattle Shield, an intelligence-sharing network operated by the Seattle police](https://prismreports.org/2026/05/20/seattle-shield-private-companies-surveillance/) |
| hackernews | asenna | ^380 c114 | [Indexing a year of video locally on a 2021 MacBook with Gemma4-31B (50GB swap)](https://blog.simbastack.com/indexed-a-year-of-video-locally/) |
| hackernews | rbanffy | ^376 c186 | [Python 3.15: features that didn't make the headlines](https://blog.changs.co.uk/python-315-features-that-didnt-make-the-headlines.html) |
| hackernews | pseudolus | ^348 c104 | [Lost Images from the 1945 Trinity Nuclear Test Restored](https://spectrum.ieee.org/trinity-nuclear-test) |
| hackernews | mattas | ^312 c391 | [Waymo pauses Atlanta service as its robotaxis keep driving into floods](https://techcrunch.com/2026/05/21/waymo-pauses-atlanta-service-as-its-robotaxis-keep-driving-into-floods/) |
| hackernews | qaz_plm | ^303 c93 | [BBEdit 16](https://www.barebones.com/products/bbedit/bbedit16.html) |
| reddit | janvitos | ^301 c97 | [110 tok/s with 12GB VRAM on Qwen3.6 35B A3B and ik_llama.cpp Had been getting [g](https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/) |
| hackernews | speckx | ^285 c150 | [Blog ran on Ubuntu 16.04 for 10 years. I migrated it to FreeBSD](https://crocidb.com/post/this-blog-ran-on-ubuntu-16-04-for-10-years-i-migrated-it-to-freebsd/) |
| hackernews | jaredwiener | ^285 c97 | [News outlets are limiting the Internet Archive's access to their journalism](https://www.niemanlab.org/2026/05/more-than-340-local-news-outlets-are-limiting-the-internet-archives-access-to-their-journalism/) |
| hackernews | sanity | ^282 c173 | [Show HN: Freenet, a peer-to-peer platform for decentralized apps For the past 5 ](https://freenet.org/) |
| hackernews | bambax | ^274 c53 | [The Letter S, by Donald Knuth (1980) [pdf]](https://gwern.net/doc/design/typography/1980-knuth.pdf) |
| reddit | mouseofcatofschrodi | ^274 c68 | [Qwen3.6 35Ba3 has changed my workflows and even how I use my computer My workflo](https://www.reddit.com/r/LocalLLaMA/comments/1tjwrp7/qwen36_35ba3_has_changed_my_workflows_and_even/) |
| x | kaggle | ^221 c5 | [Join the 5-Day AI Agents: Intensive Vibe Coding Course with @Google! Learn from ](https://x.com/kaggle/status/2057457614116507829) |
| x | Lianhuiq | ^203 c10 | [Scaling embodied AI starts with automating the environments. Introducing SimWorl](https://x.com/Lianhuiq/status/2057165074532581695) |
| hackernews | nchagnet | ^200 c108 | [Uv is fantastic, but its package management UX is a mess](https://www.loopwerk.io/articles/2026/uv-ux-mess/) |
| hackernews | speckx | ^197 c65 | [Using Kagi Search with Low Vision](https://veroniiiica.com/using-kagi-search-with-low-vision/) |
| hackernews | d0ks | ^192 c211 | [The memory shortage is causing a repricing of consumer electronics](https://davidoks.blog/p/ai-is-killing-the-cheap-smartphone) |
| x | KullAxel | ^188 c6 | [Agent benchmark not coding benchmark. I have seeen a lot of people criticizing G](https://x.com/KullAxel/status/2057491514490823095) |
| x | MultiversX | ^181 c6 | [AI coding agents have become the primary authors of most software in 2026. We're](https://x.com/MultiversX/status/2057492868038611350) |
| x | testingcatalog | ^174 c17 | [Tycoon launched as the world's first operating system for one-person companies, ](https://x.com/testingcatalog/status/2057394368068083738) |
| hackernews | elffjs | ^148 c300 | [Spotify will start reserving concert tickets for fans](https://www.hollywoodreporter.com/music/music-industry-news/spotify-will-start-reserving-concert-tickets-for-superfans-1236603106/) |