---
type: social-topic-report
date: '2026-06-17'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-06-17T15:59:14+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 80
salience: 0.42
sentiment: mixed
confidence: 0.55
tags:
- indie-hackers
- ai-tooling
- model-routing
- claude-code
- agent-harness
- creative-ai
thumbnail: https://pbs.twimg.com/media/HLBDU9mbIAA6oHq.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-06-17

## TL;DR
- ความโปร่งใสด้านรายได้ของ indie ครองพื้นที่: jackfriks รายงาน $37,000/เดือนจาก startup เดี่ยว, 23 โปรเจกต์นับตั้งแต่ปี 2019, hit rate 22% ตามการประเมินของตัวเอง และปฏิเสธข้อเสนอซื้อกิจการ $1M สำหรับ postbridge ตอนที่ MRR อยู่ที่ $13K [11][17][23][55]
- Multi-model / anti-lock-in เป็นธีมหลักของ devtool: รัน GLM 5.2 ใน Cursor ผ่าน OpenRouter [14], เลือกใช้ Gemini 2.5 Flash บวก knowledge base แทนการอัปเกรดโมเดลใหม่ [48], สร้าง agent harness แบบ custom โดยใช้โมเดลหลักหนึ่งตัวเป็น orchestrator และโมเดลราคาถูกสำหรับ sub-decision [5], และโต้แย้งเรื่อง single-vendor lock-in [30]
- ความไม่พอใจต่อ Claude Code ชัดเจน: vasuman บอกว่า Opus 4.8 xHigh ถูก 'lobotomized' และไม่ทำตาม instruction บน fresh context [6] พร้อมกับ 'Don't trust the labs' [27]; godofprompt ตั้งข้อสังเกตว่า Opus 4.8 ขยับ context เป็น 256k อย่าง 'เงียบๆ' แต่บอกว่าเป็นเรื่องบังเอิญ ไม่ใช่ conspiracy [38]
- Creative-AI tooling: รายการ 5 เครื่องมือ creative ฟรี (FUI overlay builder, 3D moodboarding, campaign/slide builders) [9][43][46][47], design prompts 50 ชุด [39], และ Framer 3.0 ออก Agents ที่ generate components, auto-layout และ breakpoints [18]

## สิ่งที่เกิดขึ้น
สัปดาห์นี้ watchlist ถูกครอบครองโดยการสะท้อนของ indie builder และความคิดเห็นเรื่อง AI tooling มากกว่า product launch jackfriks เปิด multi-tweet thread เรื่องคณิตศาสตร์ความสำเร็จ/ล้มเหลว: $37,000/เดือนจาก startup เดี่ยว [17], 23 โปรเจกต์นับตั้งแต่ปี 2019 hit rate 22% [23][55], ปฏิเสธ acquisition $1M สำหรับ postbridge ตอน MRR $13K [11], และบันทึกจุดเริ่มต้น ($75 เดือนที่ดีที่สุดในปี 2021 [13], YouTube videos กว่า 2000 คลิป [34], mining dogecoin [20]) Marc Lou โพสต์เปรียบ lifestyle ปี 2016 กับ 2026 [1] และฟีเจอร์ DataFast globe [24] levelsio แชร์การพบปะที่งาน 'Compile' ของ Cursor กับ rrhoover, ThePrimeagen และ teej_dv [4][7]

## ทำไมจึงสำคัญ (การวิเคราะห์)
ด้าน tooling สัญญาณที่สม่ำเสมอจาก practitioner อิสระหลายรายคือ model portability และความระแวงต่อ lab เจ้าเดียว หลายคนเลี่ยงค่าเริ่มต้นของ vendor — OpenRouter สำหรับ GLM 5.2 [14], harness แบบ council/orchestrator ที่ผสมโมเดลแรงหนึ่งตัวกับโมเดลราคาถูก [5], และการพูดตรงๆ ว่า 'don't get locked in' [30][48] pattern นี้ยิ่งชัดขึ้นจากเสียงบ่นเรื่อง Claude Code regression [6][27] และการเปลี่ยน context window อย่างเงียบๆ [38]: builder ที่ใช้เครื่องมือเหล่านี้ทุกวันกำลังตอบสนองต่อ quality drift ที่รับรู้ได้ด้วยการกระจาย provider ผลกระทบลำดับสองคือ abstraction layer (OpenRouter, Cursor model settings, custom harnesses) กลายเป็น interface ที่มั่นคง ในขณะที่คุณภาพของแต่ละโมเดลแปรปรวน ด้าน indie revenue-transparency thread [11][17][23][55] เตือนให้ระลึกว่า hit rate ต่ำ (jackfriks ประเมิน hit rate ปกติไว้ที่ 5% [55]) และปริมาณงานบวกทักษะด้าน distribution — affiliate/traffic generation ที่ถูกเรียกว่า 'ultimate skill' [15] — ขับเคลื่อนผลลัพธ์มากกว่าการเดิมพันครั้งเดียว ข้อมูลทั้งหมดนี้เป็น anecdote ไม่ใช่ข้อมูลเชิงสถิติ ใช้เป็นตัวชี้วัด sentiment

## ความเป็นไปได้
น่าจะเกิด: การเคลื่อนไหวต่อเนื่องไปสู่ provider-agnostic setup (OpenRouter, model-routing harnesses) ในกลุ่มนี้ เพราะเสียงบ่น [6][27] และโพสต์ workaround [5][14][30][48] ชี้ไปทิศทางเดียวกัน เป็นไปได้: thread 'hit rate' / revenue-transparency แบบสาธารณะจะเพิ่มขึ้นในฐานะ content format เนื่องจาก engagement ใน thread ของ jackfriks [17][23][55] และ levelsio ได้รับเครดิตว่าเป็นผู้ริเริ่มรูปแบบนี้ [51] สัญญาณที่ไม่น่าเชื่อถือ: claim เฉพาะเรื่องโมเดล (โมเดล refactor codebase ทั้งหมดใน call เดียว [2], Opus 4.8 'lobotomy' [6], conspiracy เรื่อง context window [38]) — เป็น assertion จากผู้เขียนรายเดียวที่ยังไม่ได้รับการยืนยัน และชื่อโมเดลหลายชื่อไม่สามารถตรวจสอบได้จาก item เหล่านั้น

## การประยุกต์ใช้สำหรับ NDF DEV
1) ทดสอบ provider-agnostic routing สำหรับ AI assistant ของทีม — ลอง OpenRouter หรือ Cursor custom-model settings เพื่อไม่ให้ quality dip ของ lab เดียวทำงานหยุด (effort ต่ำ) [14][30] 2) ทดลอง pattern orchestrator บวกโมเดลราคาถูกสำหรับ agent task ภายใน แทนการใช้โมเดลแพงตัวเดียวทำทุกอย่าง (effort ปานกลาง) [5] 3) ถ้าใครในทีมใช้ Claude Code ให้ติดตาม regression เรื่อง instruction-following และตั้ง fallback model ไว้ (effort ต่ำ) [6][27] 4) ประเมิน Framer 3.0 Agents สำหรับสร้าง marketing/landing page เร็วๆ ที่เชื่อมกับงาน web & mobile (effort ต่ำ–ปานกลาง) [18] 5) ทดลอง creative-AI tools (FUI overlay builder, 3D moodboarding) สำหรับ game/XR UI และ concept art (effort ต่ำ) [9][43] 6) ทดสอบ 'honesty mode' prompt แบบ single-paste เพื่อลด hallucinated sources/numbers ในงาน research ก่อนนำไปใช้จริง (effort ต่ำ) [50] ข้าม: lifestyle/longevity [1], meetup [4][7] และโพสต์ Midjourney sref/art [21][44] — ไม่มีความเกี่ยวข้องเชิงปฏิบัติ

## สัญญาณที่ต้องติดตาม
- Multi-model routing เป็น default practice — OpenRouter + Cursor + custom harnesses [5][14][30]
- เสียงบ่น Claude Code / Opus 4.8 quality จาก heavy user ซ้ำๆ [6][27][38]
- Indie 'hit rate' transparency กำลังกลายเป็น content format [17][23][51][55]
- Framer 3.0 Agents สำหรับ component/breakpoint generation ใน web build [18]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | marclou | ^1712 c217 | [2016: - 70kg - Processed food diet - 3x workouts per week - 6 hours of sleep per](https://x.com/marclou/status/2067226264067506586) |
| x | vasuman | ^1063 c62 | [Le Chaton Fat just refactored my entire codebase in one call. 25 tool invocation](https://x.com/vasuman/status/2066708889631178849) |
| x | levelsio | ^813 c17 | [And then I saw this flying by 🤭 https://t.co/LaXVLjX3dP](https://x.com/levelsio/status/2067109087457005893) |
| x | levelsio | ^464 c31 | [Absolute pleasure to finally meet @rrhoover at @cursor_ai Compile today https://](https://x.com/levelsio/status/2067082059911410014) |
| x | EXM7777 | ^443 c20 | [THIS IS HOW YOU WIN IN 2026: > build your own agent harness and power it with a ](https://x.com/EXM7777/status/2066953167321870752) |
| x | vasuman | ^432 c54 | [They lobotomized Claude in Claude Code. Worst I've ever seen. Completely ignorin](https://x.com/vasuman/status/2067051222973239517) |
| x | levelsio | ^430 c14 | [They're so cool and nice @ThePrimeagen and @teej_dv Also TJ is actually 🇳🇱 Dutch](https://x.com/levelsio/status/2067089792383504823) |
| x | steipete | ^376 c41 | [@DanBochman Ya know there's other models that perform bettet and are cheaper. 🙃](https://x.com/steipete/status/2066756678628848118) |
| x | AmirMushich | ^372 c10 | [5 free tools for creatives 1 / This FUI overlays builder is totally free https:/](https://x.com/AmirMushich/status/2066972444645056871) |
| x | levelsio | ^242 c27 | [@AfonsoJFG This is why I think Brazilians are not so bad if you filter them prop](https://x.com/levelsio/status/2067092212798849249) |
| x | jackfriks | ^194 c35 | [i'm so glad i didn't sell my company (@postbridge_) for $1,000,000 last year whe](https://x.com/jackfriks/status/2067219730662854808) |
| x | AmirMushich | ^140 c6 | [Insane how smooth the UX is right from the X mobile 🫠 https://t.co/2pX43PWVKv](https://x.com/AmirMushich/status/2066786648935801344) |
| x | jackfriks | ^133 c15 | [may 2021: my best month making money online 5 years ago. $75. KEEP GOING. https:](https://x.com/jackfriks/status/2067233830671396926) |
| x | rileybrown | ^112 c12 | [How to use GLM 5.2 in Cursor... I'm using it with @OpenRouter because zAI is bus](https://x.com/rileybrown/status/2067075406553895342) |
| x | eptwts | ^111 c6 | [i've noticed a phenomenon where successful affiliate marketers end up being succ](https://x.com/eptwts/status/2067208284189139394) |
| x | marclou | ^74 c13 | [HOY @shipordie_ https://t.co/MfaCMXfjsN](https://x.com/marclou/status/2067159471370150322) |
| x | jackfriks | ^70 c18 | [i just hit $37,000/month on my solo startup, so now i can call it a success i th](https://x.com/jackfriks/status/2067265469225009449) |
| x | MengTo | ^66 c6 | [Framer 3.0 just came out and I might actually start using it. - Much easier to s](https://x.com/MengTo/status/2067242820524810635) |
| x | jackfriks | ^56 c9 | [me when i hit $30K MRR and don't believe in survivorship bias: https://t.co/HdrA](https://x.com/jackfriks/status/2067219139375124580) |
| x | jackfriks | ^53 c14 | [5 years ago i was trying to mine dogecoin btw https://t.co/xwLgUtsEpb](https://x.com/jackfriks/status/2067232170473595090) |
| x | egeberkina | ^47 c0 | [Byzantine mosaics --sref 3502435122 --v 8.1 https://t.co/hg9BFwjxzq](https://x.com/egeberkina/status/2066960755275022578) |
| x | vasuman | ^45 c2 | [Excuse me sir. Would you mind if I toot my own horn? https://t.co/zKX2QlGkJh](https://x.com/vasuman/status/2066649157788745860) |
| x | jackfriks | ^44 c8 | [22% of the projects i made were a subjective success according to me (made a yea](https://x.com/jackfriks/status/2067268492684918823) |
| x | marclou | ^44 c15 | [I made a tiny time machine for the real-time globe in @DataFast_ https://t.co/Fg](https://x.com/marclou/status/2067264304399986992) |
| x | jackfriks | ^40 c3 | [@marclou came for twitter feed got marc only fans premium KEEP GOING](https://x.com/jackfriks/status/2067232315357483242) |
| x | egeberkina | ^39 c0 | [One game that changed the world https://t.co/c4Z2oXsfFB](https://x.com/egeberkina/status/2066982810083107135) |
| x | vasuman | ^38 c7 | [Don't trust the labs](https://x.com/vasuman/status/2066751176029409515) |
| x | levelsio | ^37 c4 | [@jasperdeboer Too low](https://x.com/levelsio/status/2067217673155756532) |
| x | vasuman | ^32 c0 | [@tszzl Do-roonified: You are the sum of your friends Thank you Roon](https://x.com/vasuman/status/2066791505097023976) |
| x | steipete | ^31 c2 | [@ani3am depends if you care about an open platform and model choice or being loc](https://x.com/steipete/status/2066736661510209962) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@marclou</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1712 · 💬 217</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/marclou/status/2067226264067506586">View @marclou on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“2016: - 70kg - Processed food diet - 3x workouts per week - 6 hours of sleep per night - Believed I'm Mark Zuckerberg 2026: - 84kg - Longevity diet - 7x workouts per week - 8.5 hours of sleep per nigh”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@marclou โพสต์เปรียบตัวเองปี 2016 vs 2026 เรื่องน้ำหนัก อาหาร การนอน และออกกำลังกาย ในแนว motivational</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/marclou/status/2067226264067506586" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vasuman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1063 · 💬 62</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vasuman/status/2066708889631178849">View @vasuman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Le Chaton Fat just refactored my entire codebase in one call. 25 tool invocations. 3,000+ new lines. 12 brand new files. It modularized everything. Broke up monoliths. Cleaned up spaghetti. It worked.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>AI coding agent ชื่อ 'Le Chaton Fat' refactor codebase ทั้งหมดในการเรียกครั้งเดียว — 25 tool invocations, เพิ่ม 3,000+ บรรทัด, สร้าง 12 ไฟล์ใหม่ แยก monolith และจัดระเบียบโค้ดสำเร็จ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>AI แบบ agentic ทำ refactor โครงสร้างขนาดใหญ่ได้จริงในรอบเดียว ไม่ใช่แค่แก้ทีละบรรทัด ซึ่งเปลี่ยนวิธีที่ทีมวางแผนเวลาสำหรับ legacy code</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เลือก module legacy ที่ยุ่งที่สุด แล้ว run ผ่าน agentic coding tool ด้วย one-shot refactor prompt จากนั้นเทียบผลกับ manual estimate</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vasuman/status/2066708889631178849" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 813 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2067109087457005893">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“And then I saw this flying by 🤭 https://t.co/LaXVLjX3dP”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio โพสต์แค่ reaction พร้อม link โดยไม่มีบริบทใดๆ — ไม่ทราบว่า link นั้นคืออะไร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2067109087457005893" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 464 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2067082059911410014">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Absolute pleasure to finally meet @rrhoover at @cursor_ai Compile today https://t.co/0gkL1yDCKX”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio โพสต์รูปเจอ Ryan Hoover ที่งาน Compile ของ Cursor — เป็นแค่ networking ไม่มีเนื้อหาเทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2067082059911410014" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EXM7777</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 443 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EXM7777/status/2066953167321870752">View @EXM7777 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“THIS IS HOW YOU WIN IN 2026: &gt; build your own agent harness and power it with a council... &gt; use a frontier model as the orchestrator, then cheaper models to help making decisions &gt; use very few plugi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แนะนำโครงสร้าง agent แบบ tiered — top-tier model เป็น orchestrator วางแผน, model ถูกกว่า execute งาน, เครื่องมือน้อย, และ knowledge base แน่นคือข้อได้เปรียบจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>pattern ตรงกับ Oracle architecture ที่ studio ใช้อยู่ — top-tier model วางแผน, model ถูกกว่า execute — ยืนยันว่านี่คือแนวทาง production ที่ถูกต้องในปี 2026</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">audit agent stack ของ studio ว่า orchestrator/executor แยกชัดหรือยัง แล้ว focus ขยาย knowledge base แทนการเพิ่ม tools หรือ skills ใหม่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EXM7777/status/2066953167321870752" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@vasuman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 432 · 💬 54</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/vasuman/status/2067051222973239517">View @vasuman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“They lobotomized Claude in Claude Code. Worst I've ever seen. Completely ignoring instructions on a fresh context window using Opus 4.8 xHigh. Every time I've called this out in the past they respond ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@vasuman รายงานว่า Claude Code กับ Opus 4.8 xHigh ไม่ follow instructions บน fresh context window พร้อมอ้างว่า Anthropic มีแพทเทิร์นปฏิเสธแล้วแก้เงียบๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า regression นี้จริง pipeline อัตโนมัติที่ studio รันบน Claude Code กับ Opus 4.8 xHigh อาจ drop instructions เงียบๆ และได้ output ผิด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ CLAUDE.md และ system prompt ของ studio กับ Opus 4.8 xHigh บน fresh context ก่อนรัน automated task จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/vasuman/status/2067051222973239517" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 430 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2067089792383504823">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“They're so cool and nice @ThePrimeagen and @teej_dv Also TJ is actually 🇳🇱 Dutch-American and Primaegen is a 🥩 steak eating lifting superchad, so good vibes people and so kind!!!!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@levelsio โพสต์ชมว่า @ThePrimeagen กับ @teej_dv เป็นคนดี พร้อมบอก background ส่วนตัวของทั้งคู่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2067089792383504823" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 376 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2066756678628848118">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@DanBochman Ya know there’s other models that perform bettet and are cheaper. 🙃”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@steipete แซะ @DanBochman ว่ามี model อื่นที่ดีกว่าและถูกกว่า — ไม่ระบุชื่อ model หรือข้อมูลอ้างอิงใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2066756678628848118" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
