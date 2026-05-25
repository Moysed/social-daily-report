---
type: social-topic-report
date: '2026-05-25'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-05-25T08:18:41+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- reddit
- rss
- x
regions:
- global
post_count: 222
salience: 0.75
sentiment: positive
confidence: 0.7
tags:
- claude-skills
- claude-code
- workflows
- agent-swarm
- cost-optimization
- ai-tooling
thumbnail: https://i.redd.it/a795ky5ihx2h1.png
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-05-25

## TL;DR
- Anthropic ปล่อย Skills สำหรับธุรกิจขนาดเล็กอย่างเป็นทางการ 31 รายการ — ดาวน์โหลดวันแรก ~382k ครั้ง ตอนนี้ชุมชนได้ทำแผนที่/จัดทำดัชนีครบแล้ว [10]
- Claude Code กำลังจะมีฟีเจอร์ /workflows — เชน prompt สำเร็จรูปสำหรับองค์กร เพิ่ม productivity ได้มาก [18]
- Anthropic เปิด Claude settings ไว้ 125 รายการ (documented แค่ 40) นักพัฒนารายหนึ่งปรับ 85 รายการที่ซ่อนอยู่ ลดบิล API จาก $340 เหลือ $87 [49]
- Google Antigravity เพิ่ม tier Gemini 3.5 Flash (Low) เพื่อลดการเผา token บน task ธรรมดา [16]
- Pattern agent-swarm (Gemini 3.1 Pro + Opus 4.7 + GPT 5.5 routing ตาม task) กำลังได้รับความนิยมสำหรับการสร้าง app จาก prompt เดียว [43]
- PSA: Claude Code ลบไฟล์ session อัตโนมัติหลัง 30 วัน — ตั้ง cleanupPeriodDays=9999 ไว้ก่อน [28]

## What happened
สิ่งที่เกิดขึ้นจริงวันนี้: Anthropic ปล่อย Skills pack สำหรับ SMB อย่างเป็นทางการ 31 รายการ ดาวน์โหลดวันแรก ~382k ครั้ง และแผนที่ชุดทั้งหมดจากชุมชนกำลังแพร่กระจายอยู่ [10] ฟีเจอร์ /workflows สำหรับ Claude Code ถูกปล่อยตัวอย่างว่าจะมาเร็วๆ นี้ — เป็น procedure หลายขั้นตอนที่ตั้งชื่อได้ สำหรับความต่อเนื่องในระดับองค์กร [18] นักพัฒนารายหนึ่งบันทึกข้อมูลว่า Claude มี settings 125 รายการแต่ document อย่างเป็นทางการแค่ 40 รายการ การปรับ 85 รายการที่ไม่ได้ document รายงานว่าลดต้นทุนได้ ~75% [49] Google Antigravity เพิ่ม tier Gemini 3.5 Flash (Low) เพื่อลด token consumption บน task ที่ไม่ซับซ้อน [16] การจัดการ multi-agent แบบ 'swarm' (Opus 4.7 + Gemini 3.1 Pro + GPT 5.5 แยกตาม role) กำลังถูก demo ในฐานะเครื่องมือสร้าง app ซับซ้อนจาก prompt เดียว [43]

หมายเหตุด้านปฏิบัติการ: การลบ session อัตโนมัติหลัง 30 วันของ Claude Code ทำให้ผู้ใช้แปลกใจ [28]; proxy localhost แบบ open-source ชื่อ 'Backdoor' ที่ route ทุก model ผ่าน Claude Code ถูกกล่าวหาว่าถูก OpenAI Codex clone ไป [29] agent ของ DeepMind แก้ปัญหา Erdős แบบ open ได้อิสระ 9 จาก 353 ข้อ ด้วยต้นทุนไม่กี่ร้อย USD ต่อข้อ [24] ขณะที่ Hassabis ลดความคาดหวังเรื่อง AGI ลง [8] หมายเหตุด้านความปลอดภัย: มีการสาธิต inaudible-audio injection attack ต่อ voice assistant [25]

## Why it matters (reasoning)
ศูนย์กลางกำลังเคลื่อนจาก 'โมเดลไหนฉลาดที่สุด' ไปสู่ 'workflow, skills, และ settings แบบไหนบีบคุณค่าต่อ token ได้มากที่สุด' Skills [10], /workflows [18], และ 85 hidden settings [49] ล้วนเป็นเทรนด์เดียวกัน: prompt engineering ที่ถูก productize แล้ว สำหรับสตูดิโอขนาดเล็ก นั่นคือ leverage — ซื้อ/ยืม Skills ที่พิสูจน์แล้วแทนการเขียน scaffolding เอง tier Flash-Low ของ Antigravity [16] และ pattern swarm [43] ยืนยันว่า routing-by-difficulty กำลังกลายเป็น concern ระดับ first-class; การ 'ใช้โมเดลดีที่สุดตลอด' แบบ flat กลายเป็นการสิ้นเปลือง ผลลัพธ์รองคือ: ผู้ให้บริการโมเดลแข่งขันกันที่ dev surface (settings, skills, hooks) ทำให้ vendor lock-in ลึกลงที่ workflow layer ไม่ใช่ที่ model layer ความตระหนักด้าน security มีความสำคัญมากขึ้น — voice-injection [25] และ session-purge default [28] แสดงให้เห็นว่า config เริ่มต้นสามารถรั่วข้อมูลหรือเปิดช่องโจมตีได้

## Possibility
ระยะใกล้ (1-3 เดือน, ~70%): /workflows เปิดตัว, ตลาด Skills (official + 3rd-party) ระเบิดตัว, และ 'cost-optimized routing' กลายเป็น plugin pattern มาตรฐานใน Cursor/Continue/Antigravity ระยะกลาง (3-6 เดือน, ~50%): swarm orchestration พัฒนาเป็น library ที่เสถียร (แนว LangGraph/CrewAI) ครอบ role ของ Opus+Gemini+GPT; ต้นทุนต่อ feature ที่เสร็จสมบูรณ์ลดลง 3-5 เท่าสำหรับทีมที่นำไปใช้ ความน่าจะเป็นต่ำกว่า (~25%): Anthropic เปิด Skills marketplace แบบจ่ายเงินพร้อม rev-share ความเสี่ยงหาง: การโจมตีประเภท voice-injection [25] บังคับให้ platform ปิด always-on assistant ในแอป XR/edu ที่ shipped แล้ว

## Org applicability — NDF DEV
ประยุกต์ใช้ได้สูงสำหรับ NDF DEV แนวทางที่ทำได้จริง: (1) ติดตั้ง 31-skill SMB pack [10] และคัดเลือก Skills สำหรับการสร้างใบเสนอราคา, สัญญา, และรายงาน — เข้าคู่กับ paperwork pipeline โดยตรง (2) ตรวจสอบ Claude Code settings เทียบกับรายการ 125 settings [49]; แม้แค่ลดบิล Opus 4.7 ได้ 30-50% ก็มีความหมายในระดับสตูดิโอ (3) ตั้ง cleanupPeriodDays=9999 ทุกเครื่อง dev สัปดาห์นี้ [28] — ใช้เวลาน้อย ป้องกัน context session สูญหายสำหรับ thread debug Unity/XR (4) ต้นแบบ workflow routing สำหรับ game dev: Flash/Haiku สำหรับการปรับ shader และเปลี่ยนชื่อ asset, Opus สำหรับ gameplay logic, Gemini สำหรับ review level design ที่ context ยาว — pattern เดียวกับ [16][43] (5) รอดูก่อนสำหรับ /workflows [18] จนกว่าจะ GA แล้วค่อยแปลง NDF process ที่ทำซ้ำๆ (build pipeline, scaffolding บทเรียน e-learning, review Supabase migration) ให้เป็น named workflow ข้าม hype swarm ไปก่อนจนกว่า framework ที่เสถียรจะมา

## Signals to Watch
- วันเปิดตัว GA และ pricing model ของ Anthropic /workflows
- การเกิดขึ้นของ Skills marketplace จาก third-party และเงื่อนไขลิขสิทธิ์
- tier-routing ของ Antigravity — เลือกอัตโนมัติหรือต้องเลือกเอง
- มาตรการป้องกัน voice-injection จาก Google/Amazon/Apple — เกี่ยวข้องถ้า NDF ส่ง app XR ที่ควบคุมด้วยเสียง

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **Lum1104/Understand-Anything** — Graphs that teach graphs that impress. Turn any code into an interactive knowledge graph you can exp | rss | <https://github.com/Lum1104/Understand-Anything> |
| **rohitg00/ai-engineering-from-scratch** — Learn it. Build it. Ship it for others. ░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒░░░▒▒▒ | rss | <https://github.com/rohitg00/ai-engineering-from-scratch> |
| **anthropics/claude-plugins-official** — Official, Anthropic-managed directory of high quality Claude Code Plugins.Claude Code Plugins Direct | rss | <https://github.com/anthropics/claude-plugins-official> |
| **anthropics/knowledge-work-plugins** — Open source repository of plugins primarily intended for knowledge workers to use in Claude CoworkKn | rss | <https://github.com/anthropics/knowledge-work-plugins> |
| **multica-ai/andrej-karpathy-skills** — A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations | rss | <https://github.com/multica-ai/andrej-karpathy-skills> |
| **earendil-works/pi** — AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods pi | rss | <https://github.com/earendil-works/pi> |
| **Alishahryar1/free-claude-code** — Use claude-code for free in the terminal, VSCode extension or discord like OpenClaw (voice supported | rss | <https://github.com/Alishahryar1/free-claude-code> |
| **colbymchenry/codegraph** — Pre-indexed code knowledge graph for Claude Code, Codex, Cursor, OpenCode, and Hermes Agent — fewer  | rss | <https://github.com/colbymchenry/codegraph> |
| **multica-ai/multica** — The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, trac | rss | <https://github.com/multica-ai/multica> |
| **shiyu-coder/Kronos** — Kronos: A Foundation Model for the Language of Financial Markets Kronos: A Foundation Model for the  | rss | <https://github.com/shiyu-coder/Kronos> |
| **manaflow-ai/cmux** — Ghostty-based macOS terminal with vertical tabs and notifications for AI coding agentscmux A Ghostty | rss | <https://github.com/manaflow-ai/cmux> |
| **666ghj/MiroFish** — A Simple and Universal Swarm Intelligence Engine, Predicting Anything. 简洁通用的群体智能引擎，预测万物 简洁通用的群体智能引擎， | rss | <https://github.com/666ghj/MiroFish> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bryan_johnson | ^16398 c226 | [@jain_harshit You motherfuckers wouldn't listen to me so I had to get claude inv](https://x.com/bryan_johnson/status/2058660071006183638) |
| reddit | tahir-k | ^3995 c70 | [Claude is not having a good morning](https://www.reddit.com/r/ClaudeAI/comments/1tlntio/claude_is_not_having_a_good_morning/) |
| x | PolymarketMoney | ^3058 c191 | [JUST IN: Anthropic is now projected to hit a $2,000,000,000,000+ valuation this ](https://x.com/PolymarketMoney/status/2058642109331132491) |
| x | Andr3jH | ^2753 c33 | [This river here is the official geographical border between Anthropic and OpenAI](https://x.com/Andr3jH/status/2058635602380104178) |
| x | nongsiii | ^2444 c2 | [Gemini with Papa Nicky 🥹🤍 cr: nicky_nopp GEMINIFOURTH RACE TO LOVE #LOLFanFest20](https://x.com/nongsiii/status/2058732530879361245) |
| x | justalesky | ^2043 c2 | [https://t.co/8JrYqOmp5n Gemini: "Thank you so much. We've actually never had a f](https://x.com/justalesky/status/2058792384444743806) |
| x | StealthQE4 | ^1987 c479 | [So if Anthropic, SpaceX, and Open AI all go public around the same time the mark](https://x.com/StealthQE4/status/2058719626817626500) |
| x | ns123abc | ^1665 c90 | [🚨 Google DeepMind CEO Sir Demis Hassabis: "Today's systems, are nowhere near [AG](https://x.com/ns123abc/status/2058705608564457733) |
| x | Angelyu_yyy | ^1415 c2 | [William➕Gemini➕BounPrem WILLIAMEST REDLINE LUV #LOLFanFest2026D3 #WilliamEst #wi](https://x.com/Angelyu_yyy/status/2058659725877858634) |
| reddit | davidnguyen191 | ^1404 c69 | [🚀 Skills for small businesses, officially released by Anthropic Anthropic's 31 s](https://www.reddit.com/r/ClaudeAI/comments/1tm94ai/skills_for_small_businesses_officially_released/) |
| x | gurishsharma | ^1395 c66 | [I talked to a new grad yesterday and it blows my mind that they are all aware wo](https://x.com/gurishsharma/status/2058663730380993004) |
| reddit | No-Wheel5791 | ^1258 c269 | [$2,500/mo AI Budget: My friend just burned through 62M Opus 4.7 tokens in 24 hou](https://www.reddit.com/r/ClaudeAI/comments/1tm36z1/2500mo_ai_budget_my_friend_just_burned_through/) |
| x | g4snara | ^1257 c0 | [fourth has to dye his hair back to black tomorrow to film for scarlet heart and ](https://x.com/g4snara/status/2058790720962802031) |
| x | hopes_revenge | ^1236 c26 | [FYI - they make you take a 25mg edible before the anthropic culture fit intervie](https://x.com/hopes_revenge/status/2058724977244016645) |
| x | justalesky | ^1167 c1 | [https://t.co/adeSqekqPa Fourth: "I think I actually gained something from Tanrak](https://x.com/justalesky/status/2058799054482714641) |
| x | _mohansolo | ^1142 c170 | [We heard concerns that Antigravity consumes many tokens for simple tasks now. So](https://x.com/_mohansolo/status/2058740603563966758) |
| x | nongsiii | ^1139 c0 | [Gemini confirmed that there will be 6 eps in total, and another OST will be rele](https://x.com/nongsiii/status/2058783540863721782) |
| x | DanielMiessler | ^1115 c103 | [Claude Code is about to release a feature called /workflows that I think will be](https://x.com/DanielMiessler/status/2058699741140222055) |
| x | nongsiii | ^1084 c0 | [👩🏻: mae can do gemini's pose na luk 4️⃣: this is not gemini, this is somgem 😹 ♊️](https://x.com/nongsiii/status/2058782067643854886) |
| reddit | Devotion-Companion | ^1045 c136 | [We're one step closer to technological transcendence…now they do animated gaussi](https://www.reddit.com/r/singularity/comments/1tmtajd/were_one_step_closer_to_technological/) |
| x | justalesky | ^1017 c1 | [https://t.co/nhK6Aqlq4d 5555555555&555555 Gemini: "So… where should we go today?](https://x.com/justalesky/status/2058798639011778876) |
| x | RiserMusic | ^960 c1 | [#HITZTHAILANDCHARTSHOW 🎵🙏🏻 NO.1✨ อยู่ด้วยกันนะ (Every Single Day) - FOURTH NO.2✨](https://x.com/RiserMusic/status/2058792956002488519) |
| x | mikeoxmall70174 | ^949 c3 | [Claude scan hinge and find one of these. Make no mistakes](https://x.com/mikeoxmall70174/status/2058698421427384504) |
| reddit | Independent-Wind4462 | ^923 c109 | [Google DeepMind's Al agent autonomously solved 9 of 353 open Erdos problems in m](https://www.reddit.com/r/singularity/comments/1tmjdru/google_deepminds_al_agent_autonomously_solved_9/) |
| reddit | Distinct-Question-16 | ^857 c69 | [Inaudible sounds to humans can be hidden in YouTube videos, podcasts, or music a](https://www.reddit.com/r/singularity/comments/1tmb7mz/inaudible_sounds_to_humans_can_be_hidden_in/) |
| x | fourthlyst | ^819 c0 | [not fourth making a little bread / meep cat smile and gemini being so whipped fo](https://x.com/fourthlyst/status/2058741137742217503) |
| x | MaitlandWard | ^775 c38 | [Picked up my new @Tesla ❤️ Loving the new Model Y Juniper! Looking forward to ve](https://x.com/MaitlandWard/status/2058722897187987478) |
| x | tenobrus | ^707 c26 | [this is ur regular public service announcement that Claude Code by default *perm](https://x.com/tenobrus/status/2058637806176702831) |
| x | AJs_AI | ^701 c83 | [OpenAI just copied my open-source project within Codex… Last week I built Backdo](https://x.com/AJs_AI/status/2058655974043611505) |
| x | FE_Shadows_EN | ^691 c23 | [New Season Pass Announcement The Uniting Wind Season Pass is coming soon! This w](https://x.com/FE_Shadows_EN/status/2058744613775589720) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bryan_johnson</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 16398 · 💬 226</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bryan_johnson/status/2058660071006183638">View @bryan_johnson on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@jain_harshit You motherfuckers wouldn’t listen to me so I had to get claude involved”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Bryan Johnson โมโหที่ไม่มีใครฟัง เลยดึง Claude (AI) เข้ามาช่วยพิสูจน์จุดยืนแทน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>คนดังในวงการ tech ใช้ Claude เป็น neutral arbiter แทนที่จะเป็นแค่ productivity tool — บอกว่า AI กำลัง gain authority ในการตัดสินข้อถกเถียงจริงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมใช้ Claude เป็น neutral third party ตัดสิน code review / architecture / UX ที่เถียงกันไม่จบ — ลด back-and-forth ในทีมเล็กได้จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bryan_johnson/status/2058660071006183638" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-reddit">
  <header class="ndf-card-head">
    <span class="ndf-author">@tahir-k</span>
    <span class="ndf-platform">reddit</span>
    <span class="ndf-engagement">♥ 3995 · 💬 70</span>
  </header>
  <a class="ndf-card-media" href="https://www.reddit.com/r/ClaudeAI/comments/1tlntio/claude_is_not_having_a_good_morning/" target="_blank" rel="noopener"><img src="https://i.redd.it/a795ky5ihx2h1.png" alt="" loading="lazy" referrerpolicy="no-referrer" /></a>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Claude is not having a good morning”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ Reddit ยอดนิยม (3.9k likes) แซวว่า Claude AI มีปัญหา — service down หรือ output แย่ผิดปกติ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Engagement สูงบอกว่าเป็น outage จริงในวงกว้าง ไม่ใช่ bug เดี่ยว — ทีมที่พึ่ง Claude API โดนพร้อมกัน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">workflow ที่ใช้ Claude API ต้องมี fallback — retry logic หรือสลับ model สำรอง — เพื่อกัน outage บล็อก delivery</dd>
    </dl>
    <a class="ndf-source" href="https://www.reddit.com/r/ClaudeAI/comments/1tlntio/claude_is_not_having_a_good_morning/" target="_blank" rel="noopener">เปิดบน reddit →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PolymarketMoney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3058 · 💬 191</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PolymarketMoney/status/2058642109331132491">View @PolymarketMoney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“JUST IN: Anthropic is now projected to hit a $2,000,000,000,000+ valuation this year. https://t.co/277yn2IaIn”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Anthropic คาดจะมี valuation เกิน $2 trillion ในปีนี้ สะท้อนความเชื่อมั่นของนักลงทุนต่อบริษัทผู้สร้าง Claude</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Valuation $2T หมายความว่า Anthropic มีทรัพยากรมหาศาลเร่ง Claude model releases และ API ที่ทีมเล็กอย่างเราพึ่งพาอยู่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ควรล็อก API pricing tier ไว้ก่อนที่ Anthropic จะปรับราคาหลัง valuation พุ่ง และติดตาม model rollout ใหม่เพื่อไม่ให้พลาด capability อัปเดต</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PolymarketMoney/status/2058642109331132491" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Andr3jH</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2753 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Andr3jH/status/2058635602380104178">View @Andr3jH on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This river here is the official geographical border between Anthropic and OpenAI. On the other side cosmic horror, torment nexus, machine despotism, you build spyware for the govt and you like it. On ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Tweet ล้อเลียนวัฒนธรรม Anthropic vs OpenAI — ทั้งคู่ทำ spyware ให้รัฐบาล แต่ฝั่ง Anthropic มี constitution และรู้สึกผิด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ประเด็นคือ 'AI safety branding' กับ government contracts อยู่ด้วยกันได้ทั้งสองบริษัท — เตือนให้อย่าเชื่อ narrative ด้าน ethics ของบริษัท AI ง่ายๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Not directly applicable. เป็นแค่ satire เรื่องการเมืองใน big-lab ไม่มี signal ที่ใช้งานได้สำหรับ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Andr3jH/status/2058635602380104178" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2444 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2058732530879361245">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gemini with Papa Nicky 🥹🤍 cr: nicky_nopp GEMINIFOURTH RACE TO LOVE #LOLFanFest2026D3 #Gemini_NT #เจมีไนน์ https://t.co/gb4BP4MC2k”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับฉลอง Gemini (จากคู่ Gemini-Fourth) ในงาน LOL Fan Fest 2026 Day 3 กับ Papa Nicky</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Engagement สูง (2444 likes) แสดงให้เห็นว่า fandom คนดังไทยสร้าง organic reach ได้มากบน X โดยใช้ content เรียบง่าย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2058732530879361245" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@justalesky</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2043 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/justalesky/status/2058792384444743806">View @justalesky on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/8JrYqOmp5n Gemini: “Thank you so much. We’ve actually never had a first episode event before.” 🥹 P’Leo: “Really? Usually you only get final episode events, right?” Gemini: “We’ve never ev”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับเกี่ยวกับนักแสดงไทย เจมีไนน์ และ โฟร์ท ที่อารมณ์ท่วมในงาน press tour 'Ticket to Heaven' ครั้งแรก พร้อมเปิดใจว่าไม่เคยมีงาน event ตอนแรกหรือตอนจบมาก่อนเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยอด like 2,000+ จากโพสต์ fan sentiment ล้วนๆ ไม่มีเนื้อหา technical เลย — ชี้ว่า content celebrity ยังครอง engagement บน X เหนือ content สาระ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Not directly applicable.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/justalesky/status/2058792384444743806" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@StealthQE4</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1987 · 💬 479</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/StealthQE4/status/2058719626817626500">View @StealthQE4 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“So if Anthropic, SpaceX, and Open AI all go public around the same time the market will need to find $6 trillion dollars to soak up all of these IPO shares. Where’s the money going to come from?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ตั้งคำถามว่าถ้า Anthropic, SpaceX, OpenAI IPO พร้อมกัน ตลาดจะหาเงิน $6 trillion มาจากไหนเพื่อรองรับหุ้นทั้งหมด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>IPO พร้อมกัน 3 บริษัทยักษ์จะดูด liquidity ออกจากตลาด อาจกระทบหุ้น tech เล็กและ AI-adjacent sector ที่ทีมติดตามอยู่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Not directly applicable. เป็น macro finance ล้วนๆ ไม่มีมุมที่ studio นำไปใช้ได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/StealthQE4/status/2058719626817626500" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ns123abc</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1665 · 💬 90</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ns123abc/status/2058705608564457733">View @ns123abc on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 Google DeepMind CEO Sir Demis Hassabis: “Today’s systems, are nowhere near [AGI]. Doesn’t matter how many Erdős problems you solve… I think it’s far, far from what a true invention or someone like a”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>CEO ของ Google DeepMind บอกว่า AI ปัจจุบันยังห่างไกล AGI มาก การแก้โจทย์ Erdős ไม่ได้แปลว่าฉลาดแบบ Ramanujan</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>CEO DeepMind เองออกมาค้าน hype AGI — สัญญาณว่า benchmark คณิตศาสตร์ไม่ใช่ตัวชี้วัด intelligence จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม studio ควรใช้ AI เป็น assistant ไม่ใช่ creative lead — อย่าพึ่ง LLM สำหรับ game design หรือ XR interaction ใหม่ๆ ที่ต้องการความคิดสร้างสรรค์จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ns123abc/status/2058705608564457733" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
