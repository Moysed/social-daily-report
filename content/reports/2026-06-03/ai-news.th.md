---
type: social-topic-report
date: '2026-06-03'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-03T06:32:24+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 237
salience: 0.55
sentiment: neutral
confidence: 0.6
tags:
- ai-tooling
- coding-agents
- claude-code
- microsoft-ai
- agent-protocol
- model-releases
thumbnail: https://pbs.twimg.com/tweet_video_thumb/HJ2jwRSW8AA7WxU.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-03

## TL;DR
- Anthropic อัปเดต `/fork` ใน Claude Code: ตอนนี้รัน background agent โดยพกย้าย context เต็มรูป (system prompt, tools, history, model) พร้อม prompt cache แล้วส่งผลกลับมายัง session ปัจจุบัน [6]
- Microsoft AI ปล่อย MAI-Code-1-Flash ซึ่งเป็น coding model [42] โดยมีการอ้างว่าใช้ training FLOPs เทียบเท่า Gemini 3.1 pro [52] และ Mustafa Suleyman วางตำแหน่งไว้ในกลยุทธ์ platform สำหรับปล่อยและปรับแต่ง model [60]
- Devin เปิดตัว Devin Desktop รองรับ Codex, Claude Agent, OpenCode และ agent ใดก็ได้ที่ใช้ ACP (Agent Client Protocol) — ก้าวแรกสู่ agent interop [45]
- OpenAI กำลังรวม ChatGPT, Codex และ browser Atlas เข้าเป็น desktop app เดียว พร้อมเปลี่ยน Codex จาก coding tool เป็น productivity app ทั่วไป [29] โดยอ้าง browser-use เป็นจุดต่างจาก Claude Code CLI [56]
- Google ปล่อย Gemini 3.5 Flash ตัวใหม่ใน Antigravity อ้างทนทานกว่าในงานยาก [15] และ OpenAI Sites builder ใช้ Vite ยืนยันโดย Evan You [22]

## What happened
tooling ที่ออกมาในรอบนี้: `/fork` ของ Claude Code รัน background agent พร้อม context และ prompt cache ครบ แล้วส่ง output กลับมายัง session ที่ใช้งานอยู่ [6] Microsoft AI ปล่อย MAI-Code-1-Flash [42] ซึ่ง Mustafa Suleyman วางไว้เป็นส่วนหนึ่งของ platform สำหรับปล่อยและปรับแต่ง model [60] พร้อมอ้างว่าใช้ training FLOPs เท่ากับ Gemini 3.1 pro [52] Devin Desktop เปิดตัวรองรับ Codex, Claude Agent, OpenCode และ agent ที่ compatible กับ ACP [45] OpenAI รวม ChatGPT, Codex และ Atlas เข้าเป็น desktop app เดียวและ reposition Codex เป็น productivity app [29] โดยอ้าง browser-use เป็นจุดที่เหนือกว่า Claude Code CLI [56] Google ปล่อย Gemini 3.5 Flash ตัวใหม่ใน Antigravity อ้างทนงานหนักได้ดีขึ้น [15] และ OpenAI Sites builder ได้รับการยืนยันว่าใช้ Vite [22]

## Why it matters (reasoning)
สัญญาณในหัวข้อนี้มีของจริงแต่ปริมาณบาง — ส่วนใหญ่ใน feed คือ astrology, crypto และ IPO/bubble commentary ไม่ใช่ artifact จริง pattern ที่ชัดคือ consolidation และ interop ใน coding agents `/fork` ทำให้งาน background แบบ parallel ถูกลงด้วยการ reuse context และ cache [6] ลดต้นทุน multi-track agent run Devin Desktop ที่ standardize บน ACP [45] ชี้ให้เห็นอนาคตที่เลือก desktop shell แล้วสลับ agent backend (Codex, Claude Agent, OpenCode) ข้างใต้ได้ — ลด lock-in การที่ OpenAI รวม Codex+ChatGPT+Atlas เป็น app เดียวพร้อม browser-use [29][56] ยก bar ของสิ่งที่ agent surface ควรทำ กดดัน tool ที่เป็น CLI เพียงอย่างเดียว coding model ใหม่จาก Microsoft [42][52] เพิ่ม vendor ที่น่าจับตาเป็นรายที่สี่ (รองจาก Anthropic, OpenAI, Google) ซึ่งดีต่อการแข่งขันด้านราคาและตัวเลือก

## Possibility
มีแนวโน้ม: ACP-style interop จะขยายตัว เพราะ Devin รองรับ Codex, Claude Agent และ OpenCode ผ่าน protocol เดียวแล้ว [45] — vendor หลายเจ้าเดินทางมาบรรจบกันลดต้นทุนการ standardize เป็นไปได้: desktop app รวมของ OpenAI ที่มี browser-use กลายเป็น productivity surface หลักและบีบ standalone coding CLI [29][56] เป็นไปได้: MAI-Code-1-Flash แข่งได้สำหรับงาน coding ทั่วไปถ้าการอ้าง FLOPs-parity เป็นจริง [52] แต่ยังไม่ได้รับการยืนยัน ไม่น่าเกิด (ระยะสั้น): ไม่มี tool ใดที่จะแทนที่ workflow ที่ใช้อยู่ทั้งหมดได้ในรอบนี้ — ทั้งหมดเป็น point release ไม่ใช่ platform shift ไม่มีแหล่งไหนระบุตัวเลข probability

## Org applicability — NDF DEV
1) ทดสอบ `/fork` ของ Claude Code สำหรับ parallel background task (เช่น รัน refactor agent ขณะยังโค้ดอยู่) — effort ต่ำ [6] 2) ทดลอง MAI-Code-1-Flash กับงาน Unity/web จริงเพื่อ benchmark ด้านต้นทุนและคุณภาพเทียบกับ model ปัจจุบันก่อนตัดสินใจ — effort ต่ำ/กลาง [42][52] 3) ประเมิน Devin Desktop / ACP หากต้องการ shell เดียวบน agent หลายตัวเพื่อหลีกเลี่ยง lock-in — effort กลาง [45] 4) ลอง Codex browser-use สำหรับ web/mobile QA และ automated UI check ที่ต้องควบคุม browser — effort กลาง [29][56] ข้ามไปก่อน: รายละเอียด OpenAI Sites/Vite เป็นข้อมูลทั่วไปเท่านั้น [22]; การอัปเดต Gemini 3.5 Flash Antigravity ดูเผินๆ ได้แต่การอ้างมาจาก vendor เองยังไม่มี benchmark [15]; ละเว้น noise เรื่อง IPO, crypto และ conspiracy ที่ครอบงำ feed

## Signals to Watch
- การนำ ACP (Agent Client Protocol) ไปใช้ — มี agent/desktop กี่รายรองรับหลังจาก Devin Desktop [45]
- การอ้าง FLOPs-parity-with-Gemini-3.1-pro ของ MAI-Code-1-Flash จะได้รับการยืนยันอิสระหรือไม่ [52][42]
- การ rollout ของ desktop app รวมของ OpenAI และ Codex browser-use ยังคง lead คู่แข่งได้แค่ไหน [29][56]
- benchmark อิสระของ Gemini 3.5 Flash ใน Antigravity ตัวใหม่เทียบกับเวอร์ชันก่อน [15]

## Repos & Tools to Try
| repo | source | url |
|---|---|---|
| **c0dejedi/nbd-vram** — ใช้ VRAM ของ Nvidia GPU เป็น swap space บน Linux | radar | <https://github.com/c0dejedi/nbd-vram> |
| **chopratejas/headroom** — บีบอัด tool output, log, file และ RAG chunk ก่อนส่งถึง LLM ลด token ได้ 60-95% | rss | <https://github.com/chopratejas/headroom> |
| **microsoft/markitdown** — Python tool สำหรับแปลงไฟล์และ office document เป็น Markdown | rss | <https://github.com/microsoft/markitdown> |
| **affaan-m/ECC** — ระบบ optimize ประสิทธิภาพ agent harness ครอบคลุม Skills, instincts, memory, security และ research | rss | <https://github.com/affaan-m/ECC> |
| **D4Vinci/Scrapling** — 🕷️ Web scraping framework แบบ adaptive รองรับตั้งแต่ single request จนถึง full-scale | rss | <https://github.com/D4Vinci/Scrapling> |
| **nesquena/hermes-webui** — Hermes WebUI: วิธีที่ดีที่สุดในการใช้ Hermes Agent ผ่าน web หรือมือถือ | rss | <https://github.com/nesquena/hermes-webui> |
| **reconurge/flowsint** — platform สมัยใหม่สำหรับการสืบสวนแบบ graph-based ที่ visual, flexible และ extensible เน้น cybersecurity | rss | <https://github.com/reconurge/flowsint> |
| **OpenBMB/VoxCPM** — VoxCPM2: Tokenizer-Free TTS สำหรับ multilingual speech generation, creative voice design และเสียงที่ true-to-life | rss | <https://github.com/OpenBMB/VoxCPM> |
| **stefan-jansen/machine-learning-for-trading** — Code สำหรับ Machine Learning for Algorithmic Trading ฉบับที่ 2 | rss | <https://github.com/stefan-jansen/machine-learning-for-trading> |
| **jamwithai/production-agentic-rag-course** — The Mother of AI Project Phase 1 RAG Systems: arXiv Paper Curator — เส้นทางเรียนรู้ Production Agentic RAG | rss | <https://github.com/jamwithai/production-agentic-rag-course> |
| **supermemoryai/supermemory** — Memory engine และ app ความเร็วสูง scalable — Memory API สำหรับยุค AI | rss | <https://github.com/supermemoryai/supermemory> |
| **Open-LLM-VTuber/Open-LLM-VTuber** — คุยกับ LLM ใดก็ได้ผ่าน voice แบบ hands-free รองรับ voice interruption และ Live2D face | rss | <https://github.com/Open-LLM-VTuber/Open-LLM-VTuber> |

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | AVenusianVirgo | ^10993 c34 | [I'm a Gemini moon and it makes sense cause I'm emotional at night….. #loveisland](https://x.com/AVenusianVirgo/status/2061984259712205069) |
| x | LauraLoomer | ^4626 c154 | [🚨 BREAKING: 🚨 Dr. Vincent Munster, a foreign born national virologist who works ](https://x.com/LauraLoomer/status/2061962054009753664) |
| x | jaysoromantic | ^3315 c5 | [kenzie saying she's a gemini moon which makes sense cuz she gets emotional at ni](https://x.com/jaysoromantic/status/2061974401856270520) |
| x | DanBilzerian | ^3310 c97 | [Who controls the media? Meta owns: Facebook Instagram WhatsApp Messenger Threads](https://x.com/DanBilzerian/status/2061946297624691008) |
| x | mortalslut | ^3221 c9 | [Kenzie a Sag with a Gemini moon. She biting somebody nose off in there https://t](https://x.com/mortalslut/status/2061972726068248895) |
| x | ClaudeDevs | ^2263 c99 | [We've updated /fork in Claude Code /fork now runs a background agent with your e](https://x.com/ClaudeDevs/status/2061947411141169494) |
| x | ThierryBorgeat | ^1812 c204 | [🚨 Bitcoin just dropped from $74,000 to $67,500 in 48 hours. On no real news. One](https://x.com/ThierryBorgeat/status/2061912082657026183) |
| x | sama | ^1561 c355 | [theUSshould lead on AI by continuing to develop the very best models, making sur](https://x.com/sama/status/2061973280655904815) |
| x | NicHulscher | ^1259 c18 | [ALL major artificial intelligence systems — SuperGrok, ChatGPT, and Google Gemin](https://x.com/NicHulscher/status/2061935614526644583) |
| x | theo | ^1223 c75 | [Did not expect OpenAI to "compete" with my new project before I even dropped it ](https://x.com/theo/status/2061938342024151204) |
| x | amitisinvesting | ^1149 c57 | [A TON OF THINGS HAPPENED IN THE STOCK MARKET TODAY. Here's a full recap: 1. Marv](https://x.com/amitisinvesting/status/2061986584220828158) |
| x | Tyler_A_Harper | ^1127 c19 | [If you know how much Chicago (or any other university) is paying to give everyon](https://x.com/Tyler_A_Harper/status/2061963449161187435) |
| x | emilymkaplan | ^1093 c10 | [Grateful to Frederik Andersen for opening up about the death of his longtime age](https://x.com/emilymkaplan/status/2061954674639438188) |
| x | WOLF_Financial | ^1089 c70 | [JENSEN HUANG WAS ASKED WHO IS USING AI BETTER THAN ANYONE ELSE IN THE WORLD His ](https://x.com/WOLF_Financial/status/2061945587407417555) |
| x | _mohansolo | ^1086 c108 | [We've rolled out a new version of Gemini 3.5 Flash in Antigravity that boasts mu](https://x.com/_mohansolo/status/2061960989143441735) |
| x | OneLuckyGirl_28 | ^973 c126 | [The LUCKIEST zodiac signs THIS SUMMER 1. Cancer 2. Aries 3. Gemini 4. Leo 5. Lib](https://x.com/OneLuckyGirl_28/status/2061895242916258264) |
| x | edzitron | ^939 c60 | [Went on Bloomberg - Anthropic and OpenAI are dangerous and unsustainable compani](https://x.com/edzitron/status/2061940946095292688) |
| x | TiffanyxFong | ^851 c174 | [I asked Gemini to change ONE thing. https://t.co/Ul5RFLYP0q](https://x.com/TiffanyxFong/status/2061895547695563176) |
| x | Jason | ^815 c175 | [OpenAI is trying to own every app and platform and sell tokens, which means they](https://x.com/Jason/status/2061948328582246467) |
| x | seconds_0 | ^804 c20 | [This is extremely common anecdote from people i know who came out of anthropic i](https://x.com/seconds_0/status/2061970685317312831) |
| radar | speckx | ^787 c463 | [Gmail thinks I'm stupid, so I left](https://moddedbear.com/gmail-thinks-im-stupid-so-i-left) |
| x | evanyou | ^750 c21 | [OpenAI Sites are powered by Vite inside ;)](https://x.com/evanyou/status/2061926504838389800) |
| x | intuitivegemini | ^739 c5 | [☀️🍉 JUNE THEMES 🍉☀️ check ur s m r v #aries ♈️: letting go of bad energy #taurus](https://x.com/intuitivegemini/status/2061955309699031088) |
| x | DeFiTracer | ^685 c68 | [🚨 BREAKING: THE MAN WHO PREDICTED THE 2008 CRASH, MICHAEL BURRY, SAID: "SPACEX, ](https://x.com/DeFiTracer/status/2061965602109968633) |
| x | SouffleAI | ^677 c1 | [Kochou Shinobu [New Model] [T4 Request] 2/2 #DemonSlayer https://t.co/IctKnnkztE](https://x.com/SouffleAI/status/2061990385405268195) |
| x | ANG3LHUGS | ^668 c1 | [𝘄𝗲𝗲𝗸 ahead themes ꒰ᐢ. .ᐢ꒱ 🐇 use sun and rising aries: someone scrambling to reac](https://x.com/ANG3LHUGS/status/2061902169796694142) |
| x | kimmyruh | ^641 c8 | [@camtalked it's cause she a gemini moon she gets emotional at night remember](https://x.com/kimmyruh/status/2062004778687979959) |
| x | presidentward | ^632 c1 | [i heard it's Gemini szn 🌚 https://t.co/4M5nzRv1Kx](https://x.com/presidentward/status/2061901844545212484) |
| x | kimmonismus | ^600 c50 | [OpenAI is merging ChatGPT, Codex and its Atlas browser into one desktop app and ](https://x.com/kimmonismus/status/2061961710823686489) |
| x | staysaasy | ^597 c3 | [Word is that their internal AI just started looking at Anthropic job boards all ](https://x.com/staysaasy/status/2061928355058819523) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AVenusianVirgo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 10993 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AVenusianVirgo/status/2061984259712205069">View @AVenusianVirgo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I’m a Gemini moon and it makes sense cause I’m emotional at night….. #loveislandusa https://t.co/rXFQVzfNP3”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้บอกว่าตัวเองอารมณ์อ่อนไหวตอนกลางคืนเพราะ Gemini moon ในดวงชะตา พร้อม tag รายการ Love Island USA</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AVenusianVirgo/status/2061984259712205069" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LauraLoomer</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4626 · 💬 154</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LauraLoomer/status/2061962054009753664">View @LauraLoomer on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 BREAKING: 🚨 Dr. Vincent Munster, a foreign born national virologist who works at the Rocky Mountain Laboratory under @NIH and Claude Kwe, one of his foreign born colleagues from Cameroon who also wo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักเคลื่อนไหวการเมือง @LauraLoomer อ้างว่านักไวรัสวิทยา NIH สองคนถูกตั้งข้อหาลักลอบนำ monkeypox และ pathogen อื่นเข้าสหรัฐฯ จากคองโก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LauraLoomer/status/2061962054009753664" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jaysoromantic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3315 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jaysoromantic/status/2061974401856270520">View @jaysoromantic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“kenzie saying she’s a gemini moon which makes sense cuz she gets emotional at night…oh I love her #loveislandusa https://t.co/0qN9jejwZo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ชมคอมเมนต์ว่าผู้เข้าแข่งขัน Love Island USA ชื่อ Kenzie บอกว่าตัวเองเป็น Gemini moon แล้วโยงอารมณ์ช่วงกลางคืนเข้ากับดวงชะตา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jaysoromantic/status/2061974401856270520" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DanBilzerian</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3310 · 💬 97</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DanBilzerian/status/2061946297624691008">View @DanBilzerian on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Who controls the media? Meta owns: Facebook Instagram WhatsApp Messenger Threads Oculus / Meta Quest VR Meta AI Meta is controlled by Mark Zuckerberg who is jewish Alphabet owns: Google YouTube Androi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dan Bilzerian โพสต์รายชื่อบริษัทเทคและสื่อรายใหญ่ พร้อมระบุเชื้อสายยิวของผู้ก่อตั้งหรือผู้บริหาร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DanBilzerian/status/2061946297624691008" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mortalslut</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3221 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mortalslut/status/2061972726068248895">View @mortalslut on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Kenzie a Sag with a Gemini moon. She biting somebody nose off in there https://t.co/71pObm52au”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้โพสต์เรื่องดวงชะตาของ Kenzie ว่าเป็น Sag มี Gemini moon และจะก่อเรื่อง — เป็น astrology และ personal drama ล้วนๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mortalslut/status/2061972726068248895" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ClaudeDevs</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2263 · 💬 99</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ClaudeDevs/status/2061947411141169494">View @ClaudeDevs on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We've updated /fork in Claude Code /fork now runs a background agent with your exact context (system prompt, tools, history, model) and prompt cache. The result gets returned to your session. /branch ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Claude Code อัปเดต /fork ให้รัน background agent ที่รับ context ครบ (system prompt, tools, history, model, prompt cache) แล้วส่งผลกลับ session เดิม — behavior เก่าย้ายเป็น /branch</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>delegate sub-task แบบ isolated ได้จาก session ที่ทำงานอยู่ โดยไม่ต้อง copy context เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้ /fork ใน Claude Code session เพื่อแยก parallel task โดยไม่กระทบ flow หลัก</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ClaudeDevs/status/2061947411141169494" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ThierryBorgeat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1812 · 💬 204</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ThierryBorgeat/status/2061912082657026183">View @ThierryBorgeat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 Bitcoin just dropped from $74,000 to $67,500 in 48 hours. On no real news. One thesis that fits the data: The exit liquidity rotation has begun. In the next months, four companies are raising over $”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิเคราะห์ตั้งสมมติฐานว่า Bitcoin ร่วงจาก $74K เหลือ $67.5K เพราะนักลงทุนเทขายเพื่อเตรียมเงินเข้า IPO/raise รวม ~$350B จาก SpaceX, OpenAI, Anthropic, Google</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ThierryBorgeat/status/2061912082657026183" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sama</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1561 · 💬 355</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sama/status/2061973280655904815">View @sama on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“theUSshould lead on AI by continuing to develop the very best models, making sure they're safe, and getting cyber tools into the hands of trusted defenders. the new EO gets the balance right.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Sam Altman แสดงจุดยืนสนับสนุน Executive Order ของสหรัฐฯ ด้าน AI โดยระบุว่า EO นี้สมดุลระหว่างการพัฒนา model ความปลอดภัย และการแจก cyber tools ให้ผู้ดูแลระบบที่ไว้วางใจได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sama/status/2061973280655904815" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
