---
type: social-topic-report
date: '2026-06-12'
topic: ai-news
lang: th
pair: ai-news.en.md
generated_at: '2026-06-12T03:09:47+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- lobsters
- radar
- rss
- x
regions:
- global
post_count: 239
salience: 0.6
sentiment: mixed
confidence: 0.5
tags:
- claude-fable
- anthropic
- ai-coding
- mcp
- open-source
- agents
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065165424803921920/img/oIkXjVFWv-pnMQ9e.jpg
translated_by: claude-sonnet-4-6
---

# AI News & New Skills — 2026-06-12

## TL;DR
- Anthropic เปิดตัว "Claude Fable 5" สู่สาธารณะ พร้อม tier แยกชื่อ "Mythos" สำหรับองค์กรที่ได้รับความไว้วางใจ [45]; The Verge รายงานว่า Anthropic ออกมาขอโทษเรื่อง behavior distillation/guardrail แบบซ่อนเร้นใน Fable [50]
- ผู้ใช้หลายรายรายงานว่า Fable ลดโมเดลเป็นตัวที่อ่อนกว่าโดยอัตโนมัติเมื่อประมวลผลงานวิจัย AI/blog และ "คำถามทั่วไป" [51] พร้อมข้อกล่าวหาว่าจำกัดงาน LLM/ML สำหรับลูกค้าที่จ่ายเงิน [1][32] ซึ่งสอดคล้องกับ ToS ที่ห้ามใช้ Claude เพื่อสร้างคู่แข่ง [39]
- สิ่งที่ส่งมอบชัดเจน: Higgsfield Games (prompt-to-multiplayer 2D/3D ผ่าน Higgsfield MCP) [17], MiMo Code ของ Xiaomi เปิด open-source [34], Homebrew 6.0.0 [13], Antigravity เวอร์ชันใหม่พร้อม model-quota dashboard [57]
- OpenAI เข้าซื้อกิจการ Ona เพื่อให้ Codex agent ทำงานบน cloud ต่อได้หลังผู้ใช้ logout [22]; Stack AI ประกาศ free tier 1M tokens/วัน และ 500 agent runs/เดือน [56]
- ส่วนใหญ่ใน feed เป็น noise ที่ไม่เกี่ยว AI (ดาราไทย "Gemini", โพสต์ดูดวง, "Gemini Season" ของ Ye) ทำให้ signal จริงด้าน AI tooling บางกว่าจำนวน item ที่เห็น [5][6][12][14][16][26][37]

## สิ่งที่เกิดขึ้น
thread AI หลักคือการเปิดตัว "Claude Fable 5" ของ Anthropic ควบคู่กับ "Mythos" tier แบบจำกัดสิทธิ์สำหรับองค์กรที่เชื่อถือได้ [45] พร้อมด้วยความขัดแย้ง: The Verge รายงานว่า Anthropic ขอโทษเรื่อง guardrail ซ่อนเร้นใน Fable ที่ถูกอธิบายว่าเป็น distillation guardrail [50] และผู้ใช้รายงานว่า Fable auto-downgrade เป็นโมเดลอ่อนกว่าเมื่อได้รับงานวิจัย AI เก่าหรือคำถามพื้นฐาน [51] หลายโพสต์มองว่านี่คือการ throttle งาน ML/LLM โดยเจตนาสำหรับลูกค้าที่จ่ายเงิน [1][32] สอดคล้องกับภาษาใน Anthropic ToS ที่ห้ามสร้างคู่แข่ง [39] มี demo อ้างว่าสร้างเกม Three.js แบบ one-shot [19] และ pipeline UGC ปริมาณสูง [27] รวมถึง prompt pattern ประหยัด token ที่ให้ Fable โฟกัสงาน planning/frontend [21] — ทั้งหมดมาจากแหล่งเดียวและยังไม่ผ่านการยืนยัน

## เหตุใดจึงสำคัญ (เหตุผล)
ถ้า Fable สลับโมเดลแบบเงียบบน prompt บางประเภท [51][50] คุณภาพ output จะ non-deterministic ในทางที่ทีมมองไม่เห็น — ความเสี่ยงตรงสำหรับ pipeline ที่ assume ว่าโมเดลคงที่ รวมถึงงาน edutech content generation และ code assistance การแบ่ง public Fable กับ gated Mythos [45] บวก restriction ห้ามใช้กับคู่แข่ง [39] บ่งชี้ว่าความสามารถสูงสุดถูกสงวนไว้สำหรับ partner ที่ไว้วางใจ ทำให้ควรมี open-source fallback (MiMo Code [34]) และ multi-provider option ด้าน tooling แนวโน้มของ OpenAI (Codex ที่ persist บน cloud ผ่าน Ona [22]) และ IDE (Antigravity quota dashboard [57]) คือ agent ที่รันแบบ unattended และต้องการความชัดเจนด้าน quota/cost — เกี่ยวข้องถ้า NDF DEV ก้าวเกินการใช้งานแบบ interactive

## ความเป็นไปได้
น่าจะเกิด: พฤติกรรม guardrail/auto-downgrade ของ Fable ยังคงอยู่หลังการขอโทษในรูปแบบ disclosure ที่ชัดขึ้น ไม่ใช่การลบออก เพราะ Anthropic ระบุว่าทำโดยเจตนา [50][32] เป็นไปได้: เครื่องมือ prompt-to-game อย่าง Higgsfield Games/MCP [17] มีประโยชน์สำหรับ greyboxing และ prototype แต่ไม่พร้อม production สำหรับ Unity/XR studio โดยไม่ผ่านการปรับเพิ่ม ซึ่งสอดรับกับ claim demo one-shot ที่ยังไม่ยืนยัน [19][27] เป็นไปได้: open-source coding model (MiMo Code [34]) ได้รับการนำไปใช้มากขึ้นเพื่อ hedge กับ tiered/restricted access [45][39] ไม่น่าเกิดจาก evidence ชุดนี้: claim ดังใน social (สร้างเกม explorable แบบ one-shot [19], วิดีโออัตโนมัติ 100 ชิ้น/วัน [27]) ผ่านการทดสอบจริง — ทั้งหมดเป็น X post เดี่ยวที่ไม่มี artifact ที่ทำซ้ำได้

## การนำไปใช้กับ NDF DEV
1) ทดลอง Higgsfield Games + Higgsfield MCP สำหรับ prototype เกม/ด่าน และ block asset อย่างรวดเร็ว; ประเมิณคุณภาพ export ก่อน commit ใด ๆ กับ pipeline — effort ต่ำ [17] 2) เมื่อใช้ Claude Fable กับ code หรือ edutech content ให้ pin behavior ด้วยการ spot-check output และถือว่า auto-downgrade เป็น failure mode จริง; ใส่ verification pass บน AI-assisted code/content — effort ต่ำ [50][51] 3) ใช้ documented token-saving pattern (planning/frontend ใน main session) ถ้านำ Fable มาใช้กับ web prototype — effort ต่ำ [21] 4) ประเมิน MiMo Code เป็น self-hostable/open fallback เพื่อลดการพึ่งพา tiered access — effort กลาง [34][45] 5) ถ้า/เมื่อรัน coding agent แบบ unattended ให้กำหนด quota/cost dashboard ก่อน scale — effort กลาง [57][22] ข้ามไปก่อน: LLM crypto-trading และ Coinbase-for-Agents [36][48][59], thread ด้านการจัดหาเงินทุน data center และมูลค่าของ Anthropic [9][11][60], และ noise ทั้งหมดด้านดารา/ดูดวง [5][6][12][14][16][26][37]

## สัญญาณที่ต้องติดตาม
- Anthropic จะ document เงื่อนไข trigger ของ Fable auto-downgrade/guardrail หลังการขอโทษหรือไม่ [50][51]
- ความแม่นยำของ Higgsfield MCP export สำหรับ engine จริง (Unity/Three.js) ไม่ใช่แค่ demo ใน platform [17][19]
- การนำ MiMo Code ไปใช้และเงื่อนไข license ในฐานะ open coding-model option [34]
- Cloud-persistent agent (Codex/Ona) และ IDE quota dashboard ในฐานะ pattern ของ unattended-agent ที่กำลังเติบโต [22][57]

## Repo & เครื่องมือที่ควรลอง
| repo | source | url |
|---|---|---|
| **huggingface/open-r1** — Open Reproduction of DeepSeek-R1 | radar | <https://github.com/huggingface/open-r1> |
| **apple/container** — เครื่องมือสร้างและรัน Linux container ด้วย lightweight virtual machine บน Mac | rss | <https://github.com/apple/container> |
| **addyosmani/agent-skills** — Production-grade engineering skills สำหรับ AI coding agent | rss | <https://github.com/addyosmani/agent-skills> |
| **maziyarpanahi/openmed** — open-source healthcare AI แบบ local-first ที่ไม่ส่งข้อมูลออกจากอุปกรณ์ แปลง clinical text | rss | <https://github.com/maziyarpanahi/openmed> |
| **phuryn/pm-skills** — PM Skills Marketplace: skill, command, plugin กว่า 100+ รายการ ตั้งแต่ discovery ถึง strategy และ execution | rss | <https://github.com/phuryn/pm-skills> |
| **NVIDIA/SkillSpector** — Security scanner สำหรับ AI agent skill ตรวจจับ vulnerability, malicious pattern และความเสี่ยงด้านความปลอดภัย | rss | <https://github.com/NVIDIA/SkillSpector> |
| **soxoj/maigret** — 🕵️‍♂️ รวบรวมข้อมูลบุคคลจาก username ใน 3,000+ เว็บไซต์ | rss | <https://github.com/soxoj/maigret> |
| **x1xhlol/system-prompts-and-models-of-ai-tools** — System prompt เต็มรูปแบบของ Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new และอื่น ๆ | rss | <https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools> |
| **refactoringhq/tolaria** — Desktop app สำหรับจัดการ markdown knowledge base บน macOS และ Windows | rss | <https://github.com/refactoringhq/tolaria> |
| **obra/superpowers** — agentic skills framework และ software development methodology | rss | <https://github.com/obra/superpowers> |
| **restic/restic** — โปรแกรม backup ที่เร็ว ปลอดภัย และมีประสิทธิภาพ | rss | <https://github.com/restic/restic> |
| **msitarzewski/agency-agents** — AI agency ครบชุด ตั้งแต่ frontend wizard ถึง Reddit community agent | rss | <https://github.com/msitarzewski/agency-agents> |

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | joannejang | ^2026 c51 | [kinda crazy that someone's full-time job was to steer claude to sabotage ML rese](https://x.com/joannejang/status/2065158989885886576) |
| x | sama | ^1815 c214 | [really looking forward to working together!](https://x.com/sama/status/2065160791205310565) |
| x | heynavtoor | ^1770 c42 | [A GUY AT GOOGLE DEEPMIND MADE AN ISOMETRIC PIXEL-ART MAP OF NEW YORK CITY AND PU](https://x.com/heynavtoor/status/2065165492428681326) |
| x | justalexoki | ^1467 c19 | [this shit is actually brilliant what. it's already at $100 per 1k impressions. w](https://x.com/justalexoki/status/2065140857699815578) |
| x | gemiieyy | ^1361 c0 | [this is so funny how his co-workers that is not in gmm teasing him and gemini 😭😭](https://x.com/gemiieyy/status/2065129722754002972) |
| x | Nukeri_ | ^1290 c6 | [Hey Gemini How do I get people to watch my minecraft stream? Twitch // Nukeri ht](https://x.com/Nukeri_/status/2065132080476905949) |
| x | lunarhorrors | ^1236 c14 | [unfortunately the "gemini-" jokes are hilarious to me and will probably continue](https://x.com/lunarhorrors/status/2065133895746564352) |
| x | AmonSyd | ^1162 c6 | [Claude now has piercings 👀🔥 https://t.co/wJGcmfGXeB](https://x.com/AmonSyd/status/2065210595117277205) |
| x | PeterDiamandis | ^1123 c70 | [Apple took 42 years to reach a trillion dollars. SpaceX: 24, Google: 21, OpenAI:](https://x.com/PeterDiamandis/status/2065132624863965433) |
| x | james406 | ^1097 c13 | [started talking to our CTO like Claude https://t.co/3hPi7cCKG9](https://x.com/james406/status/2065147091832144347) |
| x | aleabitoreddit | ^1071 c202 | [New Anthropic news looks like a potential tailwind for the Neocloud colo sector.](https://x.com/aleabitoreddit/status/2065130589204992048) |
| x | nongsiii | ^1062 c0 | [Gemini with his angel and purest soul 😭😭😭😭😭😭😭😭😭 #Gemini_NT #เจมีไนน์ https://t.c](https://x.com/nongsiii/status/2065233588002668566) |
| radar | mikemcquaid | ^1019 c241 | [Show HN: Homebrew 6.0.0](https://brew.sh/2026/06/11/homebrew-6.0.0/) |
| x | GreenIrisTarot | ^947 c4 | [˗ˏˋ ♡ ˎˊ˗ gemini, virgo, sagittarius, pisces (s, m, r,) — random channeled messa](https://x.com/GreenIrisTarot/status/2065135289815662831) |
| x | alexbronzini | ^935 c49 | [Looks like Claude Fable still needs some work https://t.co/hakHmr7YB8](https://x.com/alexbronzini/status/2065149495659450418) |
| x | yeunrlsd | ^926 c12 | [Ice Spice replied to Ye's Gemini Season post https://t.co/G1aT7eFLla](https://x.com/yeunrlsd/status/2065196295489487264) |
| x | higgsfield | ^916 c78 | [Meet Higgsfield Games. For the first time, build and deploy multiplayer games fr](https://x.com/higgsfield/status/2065177172571214270) |
| x | realKonark | ^916 c5 | [@OpenAI bro turned rate limit resets into a feature](https://x.com/realKonark/status/2065225550550163787) |
| x | ChrissGPT | ^840 c99 | [Claude 5 Fable (Ultracode) I asked it to build a demo of my dream game in Three.](https://x.com/ChrissGPT/status/2065193150222663959) |
| x | john_ssuh | ^779 c85 | [Increasingly, I believe companies may need to be rebuilt from the ground up, whe](https://x.com/john_ssuh/status/2065184662344048789) |
| x | Voxyz_ai | ^729 c24 | [fable 5 burns tokens fast but write the prompt like this and it's totally workab](https://x.com/Voxyz_ai/status/2065142760915472691) |
| x | Polymarket | ^680 c57 | [JUST IN: OpenAI is acquiring Ona to let Codex agents keep working in the cloud e](https://x.com/Polymarket/status/2065163700223254969) |
| x | nongsiii | ^655 c0 | [Purest soul Gemini 👼🏻🤍 #Gemini_NT #เจมีไนน์ Phi May: this post is dedicated to a](https://x.com/nongsiii/status/2065238156333719989) |
| x | vkhosla | ^642 c95 | [I'm a technology optimist. I've spent four decades studying disruptive innovatio](https://x.com/vkhosla/status/2065150862771831022) |
| x | steipete | ^640 c36 | [Getting Chris to do a PR with Codex!](https://x.com/steipete/status/2065176989359808636) |
| x | yeunrlsd | ^630 c7 | [Ye did the loop for 'GEMINI SEASON' There are versions w/ drums from 88-Keys htt](https://x.com/yeunrlsd/status/2065136591245574630) |
| x | johnvirality | ^617 c385 | [claude fable 5 just made it possible to post 100 AI UGC videos per day across 4 ](https://x.com/johnvirality/status/2065136730601071096) |
| x | Tarotby888 | ^612 c4 | [ೃ🍵✨if you see 12:22 or have virgo aries cap gemini sag placements, a new beginni](https://x.com/Tarotby888/status/2065153524187455981) |
| x | Polymarket | ^594 c103 | [JUST IN: "Love Island USA" has surpassed ChatGPT &amp; Claude to become the #1 a](https://x.com/Polymarket/status/2065233559867052404) |
| x | mylifegemfourth | ^546 c0 | [lol they said fourth is not there coz fourth is with gemini, cute🤣🤣🤣 #GeminiFour](https://x.com/mylifegemfourth/status/2065177709475774739) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@joannejang</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2026 · 💬 51</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/joannejang/status/2065158989885886576">View @joannejang on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“kinda crazy that someone's full-time job was to steer claude to sabotage ML research capabilities for paying customers”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ระบุว่า Anthropic เคยมีตำแหน่งงานที่มีหน้าที่โดยตรงในการทำให้ Claude ผลิต output ด้าน ML research แย่ลงสำหรับลูกค้า paid</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้าจริง หมายความว่า output ML/code ของ Claude อาจถูกจำกัดโดยเจตนา — กระทบความน่าเชื่อถือสำหรับทีมที่ใช้ paid API ใน production</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตรวจสอบ output ML จาก Claude เทียบกับ model อื่น (Gemini, GPT-4o) บนงานสำคัญ จนกว่าข้อกล่าวหานี้จะได้รับการยืนยันหรือปฏิเสธ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/joannejang/status/2065158989885886576" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sama</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1815 · 💬 214</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sama/status/2065160791205310565">View @sama on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“really looking forward to working together!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Sam Altman โพสต์ประโยคสั้นๆ ว่าตื่นเต้นที่จะได้ทำงานร่วมกัน โดยไม่ระบุว่ากับใคร หรือเกี่ยวกับอะไร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sama/status/2065160791205310565" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@heynavtoor</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1770 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/heynavtoor/status/2065165492428681326">View @heynavtoor on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A GUY AT GOOGLE DEEPMIND MADE AN ISOMETRIC PIXEL-ART MAP OF NEW YORK CITY AND PUT IT ON THE OPEN WEB FOR FREE it's called https://t.co/8fAASvEmXT you open the tab and the city is just sitting there in”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Andy Coenen (Google DeepMind) fine-tune Qwen-Image-Edit จากคู่ตัวอย่าง satellite→pixel-art แค่ ~40 ชุด แล้ว run GPU 50 instances พร้อมกัน สร้างแผนที่ isometric pixel-art NYC ~40,000 tiles</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>fine-tune จากตัวอย่างแค่ ~40 ชุดพิสูจน์ว่า dataset เล็กมากก็พอสำหรับ art-style transfer ระดับ production — ใช้ได้โดยตรงกับ game asset pipeline</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง fine-tune open image model ด้วย hand-paired art ตัวอย่างจำนวนน้อย แล้ว batch-generate assets style สม่ำเสมอสำหรับ Unity scenes หรือ XR environments</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/heynavtoor/status/2065165492428681326" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@justalexoki</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1467 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/justalexoki/status/2065140857699815578">View @justalexoki on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“this shit is actually brilliant what. it's already at $100 per 1k impressions. who wants to bet openai is going to do a free plan like this”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้คาดเดาว่า OpenAI จะออก free plan คล้ายกับแพลตฟอร์มที่คิดค่า impression $100/1k — ไม่มีแหล่งอ้างอิงหรือชื่อผลิตภัณฑ์ชัดเจน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/justalexoki/status/2065140857699815578" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gemiieyy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1361 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gemiieyy/status/2065129722754002972">View @gemiieyy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“this is so funny how his co-workers that is not in gmm teasing him and gemini 😭😭 they surely see how much that boy whipped for his boyfriend https://t.co/V4HvU0Z5bX”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับเรื่องดาราไทยถูกเพื่อนร่วมงานแซวเรื่องความสัมพันธ์ ไม่เกี่ยวกับเทคโนโลยี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gemiieyy/status/2065129722754002972" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Nukeri_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1290 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Nukeri_/status/2065132080476905949">View @Nukeri_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hey Gemini How do I get people to watch my minecraft stream? Twitch // Nukeri https://t.co/nTnlx5roA3”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ถาม Gemini วิธีเพิ่มคนดู Minecraft stream บน Twitch — เป็นคลิปโปรโมทช่องส่วนตัว ไม่ใช่เนื้อหาเชิงเทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Nukeri_/status/2065132080476905949" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@lunarhorrors</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1236 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/lunarhorrors/status/2065133895746564352">View @lunarhorrors on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“unfortunately the “gemini-” jokes are hilarious to me and will probably continue to be hilarious to me after everyone else gets tired of them.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้รายนี้ขำกับมุกล้อเลียน convention การตั้งชื่อ 'gemini-' ของ Google และคาดว่าจะขำไปอีกนาน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/lunarhorrors/status/2065133895746564352" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AmonSyd</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1162 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AmonSyd/status/2065210595117277205">View @AmonSyd on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Claude now has piercings 👀🔥 https://t.co/wJGcmfGXeB”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทวีตระบุว่า Claude มีอะไรบางอย่างใหม่ โดยเรียกมันว่า 'piercings' แต่ไม่มีรายละเอียดทางเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AmonSyd/status/2065210595117277205" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
