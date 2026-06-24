---
type: social-topic-report
date: '2026-06-24'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-24T15:08:20+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
regions:
- global
post_count: 40
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- ai-agents
- claude-code
- agent-skills
- mcp
- rag
- open-source
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-24

## TL;DR
- ผู้ให้บริการรายใหญ่สามเจ้าเผยแพร่ directories สำหรับ agent-skill/plugin ในช่วงเวลาเดียวกัน: Anthropic claude-plugins-official [29], AWS agent-toolkit-for-aws (MCP servers + skills + plugins) [38] และ NVIDIA skills [40] — รูปแบบ 'skills/plugins' กำลังกลายเป็นมาตรฐานในการกระจาย Claude Code agents
- community skill packs สะสมเพิ่มขึ้นต่อเนื่อง: cybersecurity skills 817 รายการที่ map กับ MITRE ATT&CK/NIST CSF [24], OpenMontage อ้าง 500+ agent skills สำหรับ video production [22] และ revfactory/harness ซึ่งเป็น meta-skill สำหรับออกแบบ agent teams และสร้าง skills [31]
- open-source agent harnesses ใหม่: ByteDance deer-flow ซึ่งเป็น long-horizon agent พร้อม sandboxes/memory/subagents [26], Nous Research hermes-agent พร้อม built-in learning loop [36] และ deepset Haystack สำหรับ RAG/agents ใน production [15]
- งานวิจัย: Qwen-AgentWorld language world models สำหรับ general agents [9], VibeThinker-3B small reasoning model [20] รวมถึง ML-kernel compiler stacks อย่าง TIRx บน Apache TVM [19] และ Event Tensor megakernel [17]
- artifacts ส่วนใหญ่เป็น raw GitHub README score-0 ที่ยังไม่ผ่านการยืนยัน พร้อมตัวเลขทางการตลาดที่พองโต ('99% fewer', '500+ skills') — สัญญาณสำคัญจริงๆ คือการที่ vendors มาบรรจบกันที่ skills ไม่ใช่ repos แต่ละอัน

## What happened
artifacts ชุดใหญ่โผล่ขึ้นมา ส่วนใหญ่อยู่ในหมวด 'agent skills' และการจัดแพ็กเกจ plugin directories ที่มีผู้ดูแลอย่างเป็นทางการปรากฏจาก Anthropic (claude-plugins-official) [29], AWS (agent-toolkit-for-aws มี MCP servers, skills และ plugins) [38] และ NVIDIA (skills) [40] ควบคู่กันมา community skill collections ได้แก่: cybersecurity skills 817 รายการแบบมีโครงสร้าง [24], meta-skill factory สำหรับ agent teams [31], Claude Code workflow set จาก Garry Tan (gstack, 23 tools) [25] และ best-practices repo [30] ในส่วน open-source agent harnesses มี ByteDance deer-flow [26], Nous Research hermes-agent [36] และ deepset Haystack สำหรับ RAG/agents [15] เครื่องมือสนับสนุน: codebase-memory-mcp สำหรับ code intelligence [35], Unlimited-OCR [21], voicebox AI voice studio [32] และ local voice-assistant build [16]

## Why it matters (reasoning)
การที่ Anthropic, AWS และ NVIDIA ปล่อย skill/plugin directories ในช่วงเวลาเดียวกัน [29][38][40] บ่งชี้ว่า skills กำลังกลายเป็น packaging unit มาตรฐานสำหรับ agent capabilities เหมือนที่ package registries เคยทำกับ libraries สำหรับ studio ที่ routing briefs ผ่าน AI assistants อยู่แล้ว นั่นหมายถึงต้นทุนในการเพิ่มความสามารถ (auth, cloud ops, code search) ลดลงโดยติดตั้ง vetted skills แทนการเขียน tool definitions เอง ความเสี่ยงระดับที่สองคือ fragmentation และ supply-chain exposure: repos ที่ไม่ได้มาจาก vendors ส่วนใหญ่เป็น score-0 drops ที่ไม่ผ่าน community vetting และมีตัวเลขพองโต [22][24][35] ส่วน prompt-injection-as-role-confusion [18] แสดงให้เห็นว่า attack surface ขยายตามทุก skill ที่ agent เรียกได้ งานวิจัย [9][20] และ compiler work [17][19] เป็น upstream และยังไม่ actionable โดยตรงสำหรับ product studio ในไตรมาสนี้

## Possibility
Likely: official directories ([29][38][40]) จะมาบรรจบกันที่ shared install/manifest convention ภายในไม่กี่เดือน เพราะ vendors สามเจ้าปล่อยออกมาพร้อมกัน. Plausible: NDF นำ Anthropic official directory [29] และ cloud toolkit อีกหนึ่งตัวมาใช้ ขณะที่ community skill packs ยังอยู่ในสถานะ experimental จนกว่าจะผ่านการ review. Unlikely (ระยะสั้น): community packs ที่มีตัวเลขสูง [22][24] จะ production-safe ทันที — ตัวเลขที่ยังไม่ยืนยันและ engagement เป็นศูนย์บอกว่าควรใช้เป็น reference เท่านั้น ไม่ใช่ dependency. ไม่มีแหล่งใดระบุเปอร์เซ็นต์การ adoption หรือความแม่นยำ จึงไม่มีการอ้างตัวเลขที่นี่

## Org applicability — NDF DEV
1) ดู anthropics/claude-plugins-official [29] และ shortlist plugins ที่เกี่ยวกับ Unity/web/mobile workflows — low effort, vendor-managed. 2) ถ้า backend ใดรันบน AWS ประเมิน agent-toolkit-for-aws สำหรับ deploy/manage MCP servers [38] — med. 3) ทดลอง codebase-memory-mcp [35] เป็น code-search MCP ข้าม Unity + web repos แต่ต้อง benchmark ก่อนเชื่อ claims '99% fewer / sub-ms' — med. 4) สำหรับ edutech/e-learning: ทดสอบ Haystack สำหรับ RAG [15] และ Unlimited-OCR สำหรับ ingest เอกสาร/บทเรียน [21] — med. 5) สำหรับ XR/game voice features: ประเมิน voicebox [32] หรือ local voice-assistant setup [16] พร้อม license/privacy check ก่อนใช้งาน client — med/high. 6) อ่าน claude-code-best-practice [30] และ harness [31] สำหรับ Claude Code workflow patterns ภายใน — low. ข้าม: daily_stock_analysis [23], quant-mind [39], worldmonitor [27] และ English-level-up [34] (off-mission); ละเว้น skill counts ที่ยังไม่ validated

## Signals to Watch
- Anthropic/AWS/NVIDIA skill directories จะรับ shared manifest/install convention ร่วมกันหรือไม่ [29][38][40]
- Prompt-injection-as-role-confusion ในฐานะ threat model ที่เป็นรูปธรรม เมื่อ ship multi-skill agents [18]
- Small verifiable-reasoning models อย่าง VibeThinker-3B สำหรับ on-device/cost-sensitive inference [20]
- ML-kernel compiler stacks TIRx [19] และ Event Tensor [17] เป็น upstream signals ของต้นทุน/ประสิทธิภาพ inference ในอนาคต

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **baidu/Unlimited-OCR** — Unlimited-OCR: One-shot Long-horizon OCR | lobsters | <https://github.com/baidu/Unlimited-OCR> |
| **calesthio/OpenMontage** — ระบบ agentic video production แบบ open-source รายแรกของโลก 12 pipelines, 52 tools, 500+ agent skills | rss | <https://github.com/calesthio/OpenMontage> |
| **ZhuLinsen/daily_stock_analysis** — ระบบวิเคราะห์หุ้นหลายตลาดด้วย LLM: ข้อมูลตลาด, ข่าวแบบ real-time, dashboard ตัดสินใจ และ auto-push รองรับการรันแบบ zero-cost scheduled | rss | <https://github.com/ZhuLinsen/daily_stock_analysis> |
| **mukul975/Anthropic-Cybersecurity-Skills** — cybersecurity skills 817 รายการแบบมีโครงสร้างสำหรับ AI agents · map กับ 6 frameworks: MITRE ATT&CK, NIST CSF 2 | rss | <https://github.com/mukul975/Anthropic-Cybersecurity-Skills> |
| **garrytan/gstack** — ใช้ Claude Code setup เดียวกับ Garry Tan: 23 opinionated tools ทำหน้าที่เป็น CEO, Designer, Eng Manager | rss | <https://github.com/garrytan/gstack> |
| **bytedance/deer-flow** — open-source long-horizon SuperAgent harness สำหรับ research, coding และ creation พร้อม | rss | <https://github.com/bytedance/deer-flow> |
| **koala73/worldmonitor** — dashboard ข่าวกรองโลกแบบ real-time ด้วย AI news aggregation และ geopolitical monitoring | rss | <https://github.com/koala73/worldmonitor> |
| **palmier-io/palmier-pro** — video editor สำหรับ macOS ที่สร้างมาเพื่อ AI ต้องการ macOS 26 (Tahoe) | rss | <https://github.com/palmier-io/palmier-pro> |
| **anthropics/claude-plugins-official** — directory อย่างเป็นทางการที่ Anthropic ดูแล สำหรับ Claude Code Plugins คุณภาพสูง | rss | <https://github.com/anthropics/claude-plugins-official> |
| **shanraisshan/claude-code-best-practice** — จาก vibe coding สู่ agentic engineering — practice makes claude perfect | rss | <https://github.com/shanraisshan/claude-code-best-practice> |
| **revfactory/harness** — meta-skill สำหรับออกแบบ agent teams เฉพาะ domain กำหนด specialized agents และสร้าง | rss | <https://github.com/revfactory/harness> |
| **jamiepine/voicebox** — open-source AI voice studio สำหรับ clone, dictate และ create | rss | <https://github.com/jamiepine/voicebox> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| radar | futohq | ^629 c226 | [FUTO Swipe – โมเดล swipe typing แบบใหม่](https://swipe.futo.tech/) |
| radar | turtleyacht | ^542 c58 | [Jerry's Map](http://www.jerrysmap.com/the-map) |
| radar | saikatsg | ^524 c93 | [In memory of the man who put red and green squiggles under words](https://devblogs.microsoft.com/oldnewthing/20260622-00/?p=112451) |
| radar | dabinat | ^519 c177 | [We're making Bunny DNS free: because a faster internet won't build itself](https://bunny.net/blog/were-making-bunny-dns-free/) |
| radar | surprisetalk | ^351 c262 | [The worthlessness of Vitamin D is mildly exaggerated](https://dynomight.net/vitamin-d/) |
| radar | goranmoomin | ^345 c197 | [Vulnerability reports are not special anymore](https://words.filippo.io/vuln-reports/) |
| radar | earcar | ^285 c338 | [Founding a company in Germany: €9600, 152 days and I still can't send an invoice](https://paolino.me/founding-a-company-in-germany/) |
| radar | byb | ^205 c92 | [Raspberry Pi Pico W as USB Wi-Fi Adapter](https://gitlab.com/baiyibai/pico-usb-wifi) |
| radar | ilreb | ^165 c45 | [Qwen-AgentWorld: Language World Models for General Agents](https://arxiv.org/abs/2606.24597) |
| radar | retroplasma | ^164 c71 | ["Fix" MacBook Neo Cursor Lag: Record 1 Pixel of the Screen Every 10 Seconds](https://gist.github.com/retroplasma/ec21767d0a8380c7ea9c2fbee1c7d6bf) |
| radar | 1vuio0pswjnm7 | ^150 c154 | [Reid Hoffman says SpaceX 'not an AI company', xAI 'complete train wreck'](https://fortune.com/2026/06/24/reid-hoffman-spacex-musk-openai-anthropic-gen-z-mistake/) |
| radar | dimastopel | ^84 c44 | [Minimus container images are now free](https://images.minimus.io/) |
| radar | ionychal | ^58 c43 | [Too many R packages: CRAN is inundated with submissions](https://rworks.dev/posts/too-many-R-packages/) |
| radar | bewal416 | ^56 c34 | [Stealing Is a Skill](https://ben-mini.com/2026/stealing-is-a-skill) |
| radar | doener | ^39 c14 | [Haystack: Open-Source AI Framework for Production Ready Agents, RAG](https://haystack.deepset.ai/) |
| lobsters | blacklight | ^7 c2 | [A fully local voice assistant setup](https://blog.platypush.tech/article/Local-voice-assistant) |
| lobsters | sanxiyn | ^3 c0 | [Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel](https://arxiv.org/abs/2604.13327) |
| lobsters | LolPython | ^3 c1 | [Prompt Injection as Role Confusion](https://role-confusion.github.io) |
| lobsters | sanxiyn | ^2 c0 | [TIRx: An Open Compiler Stack for Evolving Frontier ML Kernels](https://tvm.apache.org/2026/06/22/tirx) |
| lobsters | Yogthos | ^1 c0 | [VibeThinker-3B: Exploring the Frontier of Verifiable Reasoning in Small Language](https://arxiv.org/abs/2606.16140) |
| lobsters | metahost | ^0 c0 | [Unlimited-OCR: One-shot Long-horizon OCR](https://github.com/baidu/Unlimited-OCR) |
| rss | unknown | ^0 c0 | [calesthio/OpenMontage ระบบ agentic video production แบบ open-source รายแรกของโลก](https://github.com/calesthio/OpenMontage) |
| rss | unknown | ^0 c0 | [ZhuLinsen/daily_stock_analysis ระบบวิเคราะห์หุ้นหลายตลาดด้วย LLM: ข้อมูลตลาด, ข่าวแบบ real-time](https://github.com/ZhuLinsen/daily_stock_analysis) |
| rss | unknown | ^0 c0 | [mukul975/Anthropic-Cybersecurity-Skills cybersecurity skills 817 รายการสำหรับ AI agents](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) |
| rss | unknown | ^0 c0 | [garrytan/gstack ใช้ Claude Code setup เดียวกับ Garry Tan: 23 opinionated tools](https://github.com/garrytan/gstack) |
| rss | unknown | ^0 c0 | [bytedance/deer-flow open-source long-horizon SuperAgent harness สำหรับ research](https://github.com/bytedance/deer-flow) |
| rss | unknown | ^0 c0 | [koala73/worldmonitor dashboard ข่าวกรองโลกแบบ real-time ด้วย AI](https://github.com/koala73/worldmonitor) |
| rss | unknown | ^0 c0 | [palmier-io/palmier-pro macOS video editor สำหรับ AI](https://github.com/palmier-io/palmier-pro) |
| rss | unknown | ^0 c0 | [anthropics/claude-plugins-official directory อย่างเป็นทางการที่ Anthropic ดูแลสำหรับ Claude Code Plugins](https://github.com/anthropics/claude-plugins-official) |
| rss | unknown | ^0 c0 | [shanraisshan/claude-code-best-practice จาก vibe coding สู่ agentic engineering](https://github.com/shanraisshan/claude-code-best-practice) |