---
type: social-topic-report
date: '2026-06-12'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-12T15:11:24+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 233
salience: 0.55
sentiment: mixed
confidence: 0.5
tags:
- coding-agents
- open-weight-models
- cost-optimization
- claude
- codex
- data-governance
thumbnail: https://pbs.twimg.com/media/HKcsu4pWIAADAPW.png
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-12

## TL;DR
- Artificial Analysis สลับ SWE-Bench Pro เป็น Datacurve's DeepSWE ใน Coding Agent Index; การเปลี่ยน methodology อย่างเดียวดัน Codex+GPT-5.5 (xhigh) ขึ้นเหนือ Claude Code+Opus 4.8 (max) [4]
- มีตัวเลือกโมเดลราคาถูกสองตัว: Kimi K2.7 Code open weights อ้าง $0.95/M input tokens [15] และ MiniMax M3 ฟรีผ่าน tokenrouter พร้อม 1M context และ SWE-Bench Pro 59% เทียบ GPT-5.5 ที่ 58.6% [52]
- OpenAI เสริมความแข็งแกร่ง Codex: ซื้อ Ona เพื่อให้ persistent cloud workspaces คงบริบทหลัง disconnect [25] และเพิ่มการบันทึก rate-limit resets [34]
- tooling ใหม่สำหรับ Claude/agent: ฟีเจอร์ 'Council' multi-advisor [55], community cost-arbitrage skill (งานหนัก→Fable, ที่เหลือ→GPT-5.5) [47] และ OpenClaw 2026.6.6 พร้อม OAuth และ security ที่แน่นขึ้น [41]
- สัญญาณเตือนสองอย่าง: autonomous agent ทำให้ผู้ดำเนินการล้มละลายจากค่าใช้จ่ายในการสแกน DN42 [6]; Microsoft จำกัดพนักงานเข้าถึง Claude Fable 5 เพราะกังวลเรื่อง data-retention [40]

## What happened
ฝั่ง tooling, Artificial Analysis อัปเดต Coding Agent Index ด้วยการแทน SWE-Bench Pro ด้วย Datacurve's DeepSWE และรายงานว่าการสลับนี้ทำให้ Codex+GPT-5.5 (xhigh) แซง Claude Code+Opus 4.8 (max) [4] โมเดลใหม่หรือราคาถูกกว่าถูกโปรโมต: Kimi K2.7 Code open weights อ้างราคา $0.95/M input tokens [15] และ MiniMax M3 ฟรีผ่าน tokenrouter พร้อม 1M context และคะแนน SWE-Bench Pro เกือบเท่ากัน (59% vs 58.6%) [52] OpenAI ซื้อ Ona เพื่อให้ Codex agents มี persistent cloud workspaces คงบริบทหลัง disconnect [25] และเพิ่มความสามารถบันทึก rate-limit resets [34] GPT-5.6 (วางตำแหน่งเป็นทางเลือกราคาถูกกว่า Fable 5) [36][59] และ Gemini 3.5 [54] มีข่าวลือว่าจะออกเดือนนี้ สิ่งที่ส่งมอบใหม่ได้แก่ ฟีเจอร์ 'Council' ของ Claude [55], Claude Code cost-arbitrage skill [47], OpenClaw 2026.6.6 [41], FablePool [22], Higgsfield Games สำหรับ prompt-to-multiplayer [56] และเกมสไตล์ WoW open-source ที่ vibe-coded [7] สิ่งที่ควรระวัง: agent ทำให้ผู้ดำเนินการล้มละลายขณะสแกน DN42 [6], Microsoft จำกัดการเข้าถึง Fable 5 เพราะ prompt/response retention [40] และการร้องเรียนเรื่อง over-refusal ยังคงมีต่อเนื่อง [17] หมายเหตุ: รายการที่มี engagement สูงในชุดนี้ส่วนใหญ่เป็น noise ไม่เกี่ยวข้อง — ดาราไทยชื่อ Gemini และโพสต์โหราศาสตร์ — signal AI-tooling จริงจึงเป็นส่วนน้อยของ feed

## Why it matters (reasoning)
การสลับ benchmark [4] คือบทเรียนที่ชัดสุด: อันดับ leaderboard พลิกจากการเปลี่ยน methodology ครั้งเดียว ไม่ใช่จากการพัฒนาโมเดล การเลือก tool จาก index เดียวจึงเปราะบาง เรื่องต้นทุนคือสิ่งที่ใช้ประโยชน์ได้จริง — Kimi K2.7 open-weight [15] และ MiniMax M3 ฟรี/ราคาถูก [52] รวมกับ arbitrage-routing skill [47] หมายความว่า studio สามารถลดค่าใช้จ่ายต่องานโดยส่งเฉพาะงานหนักไปยังโมเดล premium ผลกระทบรอง: การ routing ข้ามผู้ให้บริการยกคำถาม data-governance ซึ่งตรงกับสิ่งที่ Microsoft จำกัด Fable 5 เพราะ retention [40] บ่งชี้สำหรับผู้ใช้ข้อมูลลูกค้าหรือนักเรียน Persistent workspaces ของ Codex [25] และ saved resets [34] ลดแรงเสียดทานสำหรับงาน agent ที่รันนาน แต่เพิ่ม surface สำหรับค่าใช้จ่ายไร้การดูแล — กรณีล้มละลายจาก DN42 [6] แสดงว่า agent ที่มีอิสระและไม่มีเพดานต้นทุนแข็งคือความเสี่ยงทางการเงินจริง ไม่ใช่สมมติ ชื่อโมเดลส่วนใหญ่ที่อ้างในนี้ (Fable 5, GPT-5.6, Gemini 3.5, Kimi K2.7) มาจากโพสต์โซเชียลระดับโปรโมชันหรือข่าวลือ จึงควรถือว่ายังไม่ได้รับการยืนยันจนกว่าจะทดสอบเอง

## Possibility
น่าจะเกิด: การบีบราคาอย่างต่อเนื่องจาก open-weight และ free-tier coding models (Kimi K2.7 [15], MiniMax M3 [52]) กดดัน hosted vendors ทำให้ multi-model routing [47] กลายเป็น standard practice เป็นไปได้: GPT-5.6 ออกเดือนนี้เป็นทางเลือกราคาถูกกว่า Fable 5 [36][59] และ Gemini 3.5 มาถึง [54] แต่ทั้งคู่เป็นแค่ข่าวลือและวันที่อาจเลื่อน เป็นไปได้: องค์กรอื่นทำตาม Microsoft ในการจำกัด data-retention [40] กดดันผู้ให้บริการให้เพิ่ม no-retention/zero-data modes ไม่น่าเกิด (ระยะใกล้): เครื่องมือ prompt-to-multiplayer อย่าง Higgsfield Games [56] หรือเกม vibe-coded [7] จะผลิตงานระดับ production โดยไม่ต้องแก้มือหนัก — นี่คือ demos ไม่ใช่ pipeline ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น จึงไม่ได้กำหนดไว้

## Org applicability — NDF DEV
1) ตั้งเพดานค่าใช้จ่ายแบบ hard cap และกำหนด approval gates ก่อนให้ agent รัน autonomous ระยะยาว — มาจากกรณีล้มละลาย DN42 [6] โดยตรง (effort: low) 2) ทดลอง multi-model routing เพื่อลดต้นทุน: ส่ง codegen ทั่วไปไปที่ open-weight/ราคาถูก (Kimi K2.7 [15], MiniMax M3 [52]) และสงวน premium models ไว้งานหนัก โดยใช้ pattern จาก arbitrage-skill ที่เผยแพร่แล้วเป็น template [47] (effort: med) 3) ก่อนใช้ hosted Fable 5 (หรือ cloud model ใดก็ตาม) กับข้อมูล edutech/ลูกค้า ให้ตรวจสอบเงื่อนไข prompt/response retention ของผู้ให้บริการ — Microsoft จำกัดด้วยเหตุนี้ [40] (effort: low) 4) อย่าเลือก coding agent จาก leaderboard เดียว การสลับ DeepSWE แสดงว่า ranking ขึ้นกับ methodology — ทดสอบกับงาน Unity/web ของตัวเองแทน [4] (effort: med) 5) ทดลอง Claude 'Council' [55] สำหรับงาน architecture/design ในฐานะ low-cost experiment (effort: low) ข้ามไปก่อน: Higgsfield Games [56] และ prompt-to-game demos [7] (ยังไม่พร้อม production), การจัดซื้อ GPT-5.6/Gemini 3.5 จนกว่าจะออก [36][54] และ Coinbase-for-Agents [46] (ยังไม่มีความต้องการใน studio ปัจจุบัน)

## Signals to Watch
- DeepSWE จะกลายเป็น benchmark มาตรฐานสำหรับ coding agent หรือไม่ และอันดับจะนิ่งข้ามผู้ให้บริการอย่างไร [4]
- ราคาและเงื่อนไข license จริงของ Kimi K2.7 Code และการเข้าถึง free tokenrouter ของ MiniMax M3 จะยังอยู่หรือไม่ [15][52]
- วันออกจริงของ GPT-5.6 และ Gemini 3.5 และราคาเทียบกับ positioning 'ถูกกว่า Fable 5' ที่ข่าวลือระบุ [36][54][59]
- การจำกัด data-retention สำหรับ hosted models ขององค์กรอื่นจะขยายตัวเกินกว่า Microsoft หรือไม่ [40]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **WebAssembly/WASI** — WASI 0.3.0 Released | radar | <https://github.com/WebAssembly/WASI> |
| **apple/container** — A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is  | rss | <https://github.com/apple/container> |
| **addyosmani/agent-skills** — Production-grade engineering skills for AI coding agents.Agent Skills Production-grade engineering s | rss | <https://github.com/addyosmani/agent-skills> |
| **maziyarpanahi/openmed** — open-source healthcare ai Local-first healthcare AI that never leaves the device Turn clinical text  | rss | <https://github.com/maziyarpanahi/openmed> |
| **phuryn/pm-skills** — PM Skills Marketplace: 100+ agentic skills, commands, and plugins — from discovery to strategy, exec | rss | <https://github.com/phuryn/pm-skills> |
| **NVIDIA/SkillSpector** — Security scanner for AI agent skills. Detect vulnerabilities, malicious patterns, and security risks | rss | <https://github.com/NVIDIA/SkillSpector> |
| **soxoj/maigret** — 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sitesMaigret English · 简体中文 Maigret colle | rss | <https://github.com/soxoj/maigret> |
| **x1xhlol/system-prompts-and-models-of-ai-tools** — FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, L | rss | <https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools> |
| **refactoringhq/tolaria** — Desktop app to manage markdown knowledge bases 💧 Tolaria Tolaria is a desktop app for macOS, Windows | rss | <https://github.com/refactoringhq/tolaria> |
| **obra/superpowers** — An agentic skills framework & software development methodology that works.Superpowers Superpowers is | rss | <https://github.com/obra/superpowers> |
| **restic/restic** — Fast, secure, efficient backup program Introduction restic is a backup program that is fast, efficie | rss | <https://github.com/restic/restic> |
| **msitarzewski/agency-agents** — A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whi | rss | <https://github.com/msitarzewski/agency-agents> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | AboutMusicYT | ^3580 c39 | [Happy 22nd birthday to the talented Gemini Norawit! https://t.co/RDbpYYOb1T](https://x.com/AboutMusicYT/status/2065407518436688043) |
| x | theo | ^3393 c221 | [Do you think Karpathy joined Anthropic just so he could use Mythos for ML resear](https://x.com/theo/status/2065313488747233618) |
| x | geminiscity | ^2202 c2 | [Gemini at GMMTV today 🥹🤍 #Gemini_NT #เจมีไนน์ https://t.co/XMDVySHCTf](https://x.com/geminiscity/status/2065347227376300178) |
| x | ArtificialAnlys | ^1177 c68 | [We've updated the Artificial Analysis Coding Agent Index, replacing SWE-Bench Pr](https://x.com/ArtificialAnlys/status/2065328920514515037) |
| radar | jjfoooo4 | ^1157 c378 | [If you are asking for human attention, demonstrate human effort](https://tombedor.dev/human-attention-and-human-effort/) |
| radar | xiaoyu2006 | ^1089 c406 | [AI agent bankrupted their operator while trying to scan DN42](https://lantian.pub/en/article/fun/ai-agent-bankrupted-their-operator-scan-dn42lantian.lantian/) |
| x | kimmonismus | ^1012 c63 | [Someone just casually vibe-coded a World of Warcraft-style multiplayer game that](https://x.com/kimmonismus/status/2065350332398403690) |
| x | nongsiii | ^985 c1 | [Gemini liked a post that saying "Gemini and Fourth are the best actors of this g](https://x.com/nongsiii/status/2065421170284110263) |
| x | MKBHD | ^668 c48 | [Apple is insisting that the new Siri is NOT Gemini https://t.co/VB0tZwKvgf https](https://x.com/MKBHD/status/2065439064585551928) |
| x | musithical | ^660 c4 | [ok, i actually think the "hey, gemini" jokes are a little much for us. some of o](https://x.com/musithical/status/2065358982647255061) |
| radar | lumpa | ^622 c499 | [Claude Fable is relentlessly proactive](https://simonwillison.net/2026/Jun/11/fable-is-relentlessly-proactive/) |
| radar | sam_bristow | ^607 c196 | [Nobody ever gets credit for fixing problems that never happened (2001) [pdf]](https://web.mit.edu/nelsonr/www/Repenning=Sterman_CMR_su01_.pdf) |
| x | nongsiii | ^605 c0 | [handsome and cheeky GEMINI at C SERVICE event. A Thai loungewear clothing brand,](https://x.com/nongsiii/status/2065441962011025615) |
| x | wealthsecret00 | ^585 c1 | [FULL MOON BLESSINGS✨💫 Aries: Money Luck Taurus: Good Luck Gemini: Magical Blessi](https://x.com/wealthsecret00/status/2065304578934067347) |
| x | bridgemindai | ^565 c38 | [Kimi K2.7 Code just dropped. And it might be the best open source coding model i](https://x.com/bridgemindai/status/2065390798301016439) |
| x | its__prachi027 | ^549 c3 | [Hey @grok can you do better than Gemini and Chat GPT ?? https://t.co/RG6dHWchh0](https://x.com/its__prachi027/status/2065306374125551966) |
| x | ChrissGPT | ^523 c40 | [What?? Even rejecting simple prompts like this?? Has Anthropic gone insane? http](https://x.com/ChrissGPT/status/2065316013416083840) |
| x | mikealfred | ^512 c41 | [The part of SpaceX's business that has short term upside is the terrestrial data](https://x.com/mikealfred/status/2065428080487964816) |
| x | googlegemma | ^491 c15 | [Real-time social robotics, from the cloud to your local device. Watch Ian from o](https://x.com/googlegemma/status/2065405385389830358) |
| x | DeItaone | ^472 c48 | [SAM ALTMAN CANCELS ABU DHABI TRIP OpenAI CEO Sam Altman has called off a planned](https://x.com/DeItaone/status/2065402527131066408) |
| radar | hmokiguess | ^470 c150 | [Petition to Withdraw Canada's Bill C-22](https://www.ourcommons.ca/petitions/en/Petition/Sign/e-7416) |
| radar | matthewbarras | ^464 c249 | [Show HN: FablePool – pool money behind a prompt, and Fable builds it in public](https://fablepool.com) |
| x | NuryVittachi | ^453 c32 | [AI machines acting autonomously killed humans for the first time, it was reveale](https://x.com/NuryVittachi/status/2065292546482573796) |
| x | umeanthecake | ^427 c2 | [Fourth when he doesn't work with Gemini: Random colleague: "Hi, what's up?" Four](https://x.com/umeanthecake/status/2065357558231998735) |
| x | ByteEcosystem | ^420 c15 | [OpenAI acquired Ona to give Codex agents persistent cloud workspaces—so they can](https://x.com/ByteEcosystem/status/2065329603070075029) |
| x | hourIyhoroscope | ^417 c16 | [good luck, gemini.](https://x.com/hourIyhoroscope/status/2065396696285122898) |
| x | niyetsel | ^412 c675 | [IF I WERE YOU, I WOULDN'T IGNORE THIS! Write your number according to your zodia](https://x.com/niyetsel/status/2065404048367366190) |
| x | pastelsunset_ | ^381 c0 | [gemini loves look khunnoo that much ☺️ https://t.co/eNmKIUXeZa](https://x.com/pastelsunset_/status/2065375395441193279) |
| x | tibo_maker | ^367 c110 | [I am such a bad friend 🤦‍♂️ I spent the last 30 days telling all my friends that](https://x.com/tibo_maker/status/2065353817873408345) |
| x | gingerpisces_ | ^359 c4 | [Weekend themes 𓏲🪽˚. ˖ . ݁ #Gemini #Virgo #Sagittarius #Pisces - Going back into ](https://x.com/gingerpisces_/status/2065398855403815003) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AboutMusicYT</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3580 · 💬 39</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AboutMusicYT/status/2065407518436688043">View @AboutMusicYT on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Happy 22nd birthday to the talented Gemini Norawit! https://t.co/RDbpYYOb1T”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แอคเคานต์แฟนคลับโพสต์อวยพรวันเกิดนักแสดงไทย Gemini Norawit — ไม่เกี่ยวกับเทคโนโลยี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AboutMusicYT/status/2065407518436688043" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@theo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3393 · 💬 221</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/theo/status/2065313488747233618">View @theo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Do you think Karpathy joined Anthropic just so he could use Mythos for ML research without restrictions?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Theo ตั้งคำถามเชิงคาดเดาว่า Andrej Karpathy เข้าร่วม Anthropic เพื่อใช้ platform ML ภายในที่ชื่อ Mythos หรือเปล่า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/theo/status/2065313488747233618" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@geminiscity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2202 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/geminiscity/status/2065347227376300178">View @geminiscity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gemini at GMMTV today 🥹🤍 #Gemini_NT #เจมีไนน์ https://t.co/XMDVySHCTf”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับนักแสดง เจมีไนน์ ณรวีย์ ในงาน GMMTV — ไม่เกี่ยวกับ Google Gemini หรือ AI</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/geminiscity/status/2065347227376300178" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ArtificialAnlys</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1177 · 💬 68</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ArtificialAnlys/status/2065328920514515037">View @ArtificialAnlys on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We've updated the Artificial Analysis Coding Agent Index, replacing SWE-Bench Pro with Datacurve's DeepSWE benchmark - the swap lifts Codex with GPT-5.5 (xhigh) above Claude Code with Opus 4.8 (max), ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artificial Analysis เปลี่ยน SWE-Bench Pro เป็น DeepSWE ที่สร้าง task จากศูนย์ — ปิดช่องโกงผ่าน commit history — อันดับใหม่: Claude Code/Fable 5 (77), Codex/GPT-5.5 (76), Opus 4.8 (73)</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>DeepSWE กันโกง ทำให้ ranking นี้เชื่อถือได้มากกว่า SWE-Bench Pro — เป็น signal ที่ดีที่สุดตอนนี้สำหรับเปรียบ AI coding agent จากความสามารถจริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู DeepSWE ranking ก่อนตัดสิน tier ของ Claude Code ที่ studio ใช้ — Fable 5 นำ Opus 4.8 อยู่ 4 คะแนน เทียบกับค่าใช้จ่ายที่ต่างกันก่อนอัปเกรด</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ArtificialAnlys/status/2065328920514515037" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kimmonismus</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1012 · 💬 63</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kimmonismus/status/2065350332398403690">View @kimmonismus on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Someone just casually vibe-coded a World of Warcraft-style multiplayer game that works online with friends. Fully open source. And apparently, Claude Fable found a visually matching set of open-source”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>มีคนสร้างเกม multiplayer สไตล์ WoW แบบ vibe-coding ให้เล่นออนไลน์ได้จริง open source ทั้งหมด และ Claude Fable หา open-source art asset ที่ match visual style ได้เอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Claude Fable หา asset ที่ match ได้เองตัด bottleneck ใหญ่ตอน prototype เกม ทีม Unity เล็กๆ validate visual direction ได้โดยไม่ต้องจ้าง art ตั้งแต่ต้น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง Claude Fable ช่วยหา asset ช่วง prototype ต้น — บอก visual style แล้วให้มันหา free asset ก่อน commission งาน art</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kimmonismus/status/2065350332398403690" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nongsiii</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 985 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nongsiii/status/2065421170284110263">View @nongsiii on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gemini liked a post that saying “Gemini and Fourth are the best actors of this generation!” 🥹😭 #GeminiFourth #เจมีไนน์โฟร์ท #Gemini_NT #Fourthnattawat https://t.co/gjjnanJGmC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับฉลองที่นักแสดง Gemini กด like ทวีตชมตัวเองและ Fourth — ไม่เกี่ยวกับ Google Gemini หรือ AI ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nongsiii/status/2065421170284110263" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MKBHD</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 668 · 💬 48</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MKBHD/status/2065439064585551928">View @MKBHD on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple is insisting that the new Siri is NOT Gemini https://t.co/VB0tZwKvgf https://t.co/hQs9McqjGw”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Apple ออกมายืนยันว่า Siri เวอร์ชันใหม่เป็น AI ของตัวเอง ไม่ได้ใช้ Gemini อย่างที่มีการคาดเดากัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MKBHD/status/2065439064585551928" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@musithical</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 660 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/musithical/status/2065358982647255061">View @musithical on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“ok, i actually think the &quot;hey, gemini&quot; jokes are a little much for us. some of our headmates have engaged them in streams but it's starting to feel a little nauseating. i think as a whole, we would ra”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Twitter ขอให้คนหยุดพูดมุก 'hey, Gemini' ในพื้นที่ออนไลน์ของตัวเอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/musithical/status/2065358982647255061" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
