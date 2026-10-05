---
type: social-topic-report
date: '2026-10-05'
topic: ai-builders-watchlist
lang: th
pair: ai-builders-watchlist.en.md
generated_at: '2026-10-05T03:35:17+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 77
salience: 0.35
sentiment: mixed
confidence: 0.5
tags:
- ai-builders
- claude-opus
- coding-agents
- app-store-review
- computer-use
- model-routing
thumbnail: https://pbs.twimg.com/media/HTvCsaHXEAAkN_m.jpg
translated_by: claude-sonnet-4-6
---

# AI Builders Watchlist — 2026-10-05

## TL;DR
- วันนี้ signal ต่ำ: ราว 2 ใน 3 ของ 60 รายการเป็น meme, การเมือง, โพสต์ขายสัญชาติ หรือโพสต์ฟิตเนส ([1],[5],[9],[12],[14],[24]) มีเนื้อหา AI หรือ devtool แค่ราว 15 รายการ
- OpenClaw Android app ของ steipete ค้างใน Google Play review นานกว่า 1 สัปดาห์ ('review limbo') หลังประกาศขอความช่วยเหลือแบบสาธารณะและแท็ก Sundar Pichai อัปเดตก็ขึ้นในวันเดียวกัน ([2],[3]) เขายังระบุว่า OpenClaw เป็น non-profit อิสระ [50]
- builder หลายคนชม Claude Opus 5.5 แต่ล้วนเป็นความเห็นส่วนตัว MengTo บอกว่าซื้อ Max subscription 5 อันเพื่อใช้ไม่หยุด [19] rileybrown ใช้ Astra กับงานซับซ้อนที่เดิมพันสูง และใช้ Opus กับ frontend, เอกสาร และงานโค้ดส่วนใหญ่ [35] jackfriks อ้างว่ามีคนในสหรัฐฯ ใช้น้อยกว่า 2% โดยไม่มีแหล่งอ้างอิง [31]
- มุมมองของ Karpathy: คนที่หันมาสนใจ AI ตอนนี้กว่า 99% เพิ่งเข้ามาไม่ถึงปี [4]
- บันทึกเรื่อง tooling: EXM7777 บอกว่า browser control ของ Claude Code ช้าและแม่นยำน้อยกว่าของ Codex และต้องใช้ plugin [34] AmirMushich ทำ demo หมุนสินค้าด้วย LTX-2.5 (video) และเขียน UI ด้วย Astra 6 ใน Codex [18]

## What happened
steipete ขอความช่วยเหลือจากคนใน Google แบบสาธารณะ หลัง OpenClaw Android app ค้างใน Play review เกิน 1 สัปดาห์ [2] อัปเดตขึ้นไม่นานหลังเขาแท็ก Sundar Pichai [3] เขายังพูดติดตลกว่า 'we are all building the same thing' [10] และโพสต์ macOS defaults key `ComputerUseAllowForbiddenTargets` สองครั้งให้คนที่ถามเรื่องข้อจำกัดของ computer-use ([11],[37]) คำตอบของเขาโปรโมต Telegram integration และ native apps ของ OpenClaw [28]

ด้านโมเดล MengTo [19] และ EXM7777 [21] ชม Opus 5.5 เรื่องการเขียน, design taste และ landing page rileybrown แบ่งงานระหว่าง Astra (งานซับซ้อนสูง) กับ Opus (งานประจำวัน) [35] EXM7777 บอกว่า browser control ของ Claude Code ตามหลัง Codex [34] eptwts โต้ว่า interface แบบ agent อย่างเดียวจะไม่มาแทน dashboard สำหรับติดตาม metrics [36] godofprompt แชร์ pattern ใน AGENTS.md ที่ให้ agent นำงานเก่ากลับมาใช้แทนการทำซ้ำ [55] AmirMushich โชว์ demo กับแบรนด์จริง: แปลงรูปสินค้าเป็นวิดีโอหมุนผ่าน LTX-2.5 API โดยเขียน UI ด้วย Astra 6 [18] rileybrown บอกว่าจะ open-source โปรเจกต์ @agentnative_ ทั้งหมด [39]

## Why it matters (reasoning)
signal เชิงปฏิบัติการที่ชัดที่สุดคือ [2]/[3] นักพัฒนาชื่อดังติดอยู่ใน Play Store review เกิน 1 สัปดาห์ และผ่านได้เพราะ escalate สาธารณะเท่านั้น สตูดิโอเล็กไม่มีช่องทางแบบนี้ ความล่าช้าของ review จึงเป็นความเสี่ยงด้าน schedule ของ Android release จริง แต่เป็นแค่กรณีเดียว ไม่ใช่ trend ที่วัดได้

โพสต์เรื่องโมเดลเป็น testimonial จากคนที่มี audience ไม่ใช่ benchmark และบางโพสต์ดูเหมือนโปรโมต ([19],[31]) pattern ที่มีประโยชน์คือ practitioner เลือกโมเดลตามงาน: โมเดลที่แรงกว่าหรือช้ากว่าสำหรับปัญหายาก ส่วนโมเดลที่ถูกกว่าหรือ 'รู้สึกเหมือนไม่จำกัด' สำหรับ frontend และเอกสาร [35] นอกจากนี้ คุณภาพของ harness (browser control [34]) สำคัญพอๆ กับตัวโมเดล ประเด็นของ Karpathy [4] อธิบาย noise ได้: audience ส่วนใหญ่เป็นคนใหม่ เนื้อหามือใหม่และ hype จึงได้ engagement ส่วนคนที่มีประสบการณ์จะรู้สึกสับสน ควรลดน้ำหนักข้อกล่าวอ้างที่ engagement สูงตามนั้น 'Building the same thing' [10] ชี้ว่าพื้นที่ agent harness แออัด ความต่างจึงมาจากความประณีตและ integrations [28] ไม่ใช่ไอเดียหลัก

## Possibility
น่าจะเกิด: builder จะ route งานข้ามหลายโมเดลมากขึ้น (Astra สำหรับปัญหายาก, Opus สำหรับงานประจำวันส่วนใหญ่) แทนการใช้โมเดลเดียว มีการอธิบายไว้ชัดเจนแล้ว [35] และสอดคล้องกับ [19]/[21] เป็นไปได้: ความสามารถด้าน browser และ computer-use จะกลายเป็นแกนแข่งขันที่เห็นชัดระหว่าง harness ของ Claude Code กับ Codex จากข้อร้องเรียนใน [34] และความสนใจเรื่อง computer-use override ([11],[37]) เป็นไปได้: จะมีโปรเจกต์ agent แบบ open-source จาก builder รายบุคคลเพิ่มขึ้น [39] ซึ่งเสริม saturation แบบ 'ทุกคนสร้าง harness เดียวกัน' [10] ไม่น่าเปลี่ยนในเร็วๆ นี้: ความทึบของ app-store review [3] แสดงให้เห็นแค่การ escalate ไม่ใช่การแก้ที่ process

## Org applicability — NDF DEV
1) เผื่อ buffer 1 สัปดาห์ขึ้นไปสำหรับ Google Play review ใน release plan ของ Android app ลูกค้าและ edutech app และอย่าผูกวัน launch กับเวลาอนุมัติ (low effort, [2],[3]) 2) ทำ internal comparison เล็กๆ: route งาน frontend, landing page และเอกสารไปที่ Opus 5.5 แล้วเก็บโมเดลที่แรงกว่าไว้กับ logic ซับซ้อน จากนั้นบันทึกผลแทนการเชื่อคำอ้างของ influencer (med effort, [19],[35]) 3) ถ้าทีมทำ browser QA หรือ scraping อัตโนมัติผ่าน agent ให้ทดสอบ browser control ของ Codex และ Claude Code กับงานจริง 1 งานก่อนเลือกมาตรฐาน (low-med effort, [34]) 4) ลอง pattern persistent-instructions ใน AGENTS.md/CLAUDE.md ให้ agent นำงานที่แก้แล้วกลับมาใช้ (low effort, [55]) 5) สำหรับงานเว็บ e-commerce หรือ product-showcase ลอง prototype photo-to-rotation video ด้วย video-model API เป็น pitch asset (med effort, [18]) 6) เก็บ dashboard ไว้ใน internal tools อย่าแทนที่หน้า metrics ด้วยการ query ผ่าน agent (low effort, [36]) ข้าม: override `ComputerUseAllowForbiddenTargets` ([11],[37]) ที่นี่ไม่มี documentation และจากชื่อดูเหมือนปลดข้อจำกัดของ computer-use จึงอย่าใช้ถ้ายังไม่เข้าใจว่ามันปลดอะไร และข้ามโพสต์เรื่องสัญชาติ, การเมือง, ฟิตเนส, meme และ engagement-bait ([1],[5],[9],[12],[14],[31])

## Signals to Watch
- latency ของ Google Play review สำหรับแอป indie และ open-source: ดูว่ามี developer รายงานการค้างหลายสัปดาห์เพิ่มหรือไม่ [2][3]
- คุณภาพ browser และ computer-use ของ Claude Code vs Codex ในฐานะปัจจัยตัดสินระหว่างสองเครื่องมือ [34][11]
- การ release open-source โปรเจกต์ @agentnative_ ที่ rileybrown สัญญาไว้ และวิดีโอ 5 ตัวที่ประกาศว่าจะออกสัปดาห์หน้า [39]
- การ route โมเดลตามงาน (Astra สำหรับงานยาก, Opus สำหรับงานส่วนใหญ่) กลายเป็น workflow ตั้งต้นของ builder [35][21]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | egeberkina | ^9920 c21 | [Doctor Strange https://t.co/pXRYmNGO4D](https://x.com/egeberkina/status/2106491431674347618) |
| x | steipete | ^8410 c197 | [Do I know anyone at Google who could help? We're now over a week in review limbo](https://x.com/steipete/status/2106446147791597774) |
| x | steipete | ^7178 c33 | [@sundarpichai And the new update is live - thanks so much!](https://x.com/steipete/status/2106485806529708368) |
| x | karpathy | ^2238 c96 | [@omarsar0 My mental model for what is happening is that 99%+ of people who are n](https://x.com/karpathy/status/2106806571321966793) |
| x | levelsio | ^1955 c82 | [Just a day later and now Javier Milei is offering full Argentinean citizenship w](https://x.com/levelsio/status/2106695234990063921) |
| x | steipete | ^1403 c32 | [@Simemeulation imagine thinking I’d be upset about more people building cool ope](https://x.com/steipete/status/2106498506248880323) |
| x | gregisenberg | ^1242 c90 | [https://t.co/hMysxDLNnz](https://x.com/gregisenberg/status/2106737353431581132) |
| x | egeberkina | ^1163 c8 | [Dormammu, I've come to bargain! https://t.co/6Xcw6xF8tE](https://x.com/egeberkina/status/2106701967812919373) |
| x | levelsio | ^1048 c123 | [🇧🇷 Flavio Bolsonaro (the son of Bolsonaro) is at the lead with 63% odds of winni](https://x.com/levelsio/status/2106718154701312018) |
| x | steipete | ^1040 c50 | [laughing about how we all are building the same thing.](https://x.com/steipete/status/2106489264443981978) |
| x | steipete | ^995 c28 | [@BenjaminBadejo defaults write -g ComputerUseAllowForbiddenTargets -bool YES](https://x.com/steipete/status/2106820480544202927) |
| x | levelsio | ^965 c62 | [I don't know where I read it but someone said High skilled Westerners immigratin](https://x.com/levelsio/status/2106696871372542127) |
| x | levelsio | ^937 c18 | [Another one!](https://x.com/levelsio/status/2106799080114430463) |
| x | marclou | ^823 c144 | [yeah AI is nice, but have you tried going to the gym? https://t.co/NdBrh6M2Ga](https://x.com/marclou/status/2106697596576334024) |
| x | jackfriks | ^443 c14 | [https://t.co/FvqYzpTMHV](https://x.com/jackfriks/status/2106816496026399122) |
| x | steipete | ^442 c24 | [bug fixes & performance improvements](https://x.com/steipete/status/2106796559400882209) |
| x | marclou | ^431 c78 | [My little book reached 10,000 downloads 🎉 https://t.co/w0V0Qy2NsL](https://x.com/marclou/status/2106720243137802726) |
| x | AmirMushich | ^341 c30 | [Rebuilt this demo for a real brand with Astra 6 + LTX-2.5 (video model) → I took](https://x.com/AmirMushich/status/2106446710348353969) |
| x | MengTo | ^322 c49 | [Opus 5.5 is seriously good. I bought 5 max subs just to be able to use it non-st](https://x.com/MengTo/status/2106427546254671906) |
| x | levelsio | ^274 c27 | [This is awesome so to help everyone I added direct booking links now to https://](https://x.com/levelsio/status/2106693622217535828) |
| x | EXM7777 | ^272 c44 | [Opus 5.5 inside Hermes is a league above Grok Bot or Dots for me... because by d](https://x.com/EXM7777/status/2106805802690625916) |
| x | EXM7777 | ^263 c19 | [love or hate higgsfield... their marketing was genuinely smart the AI influencer](https://x.com/EXM7777/status/2106403904770695644) |
| x | egeberkina | ^254 c0 | [I know what I want. I know what kind of God I need to be. For you. For all of us](https://x.com/egeberkina/status/2106827593169191275) |
| x | marclou | ^250 c28 | [@mzeesx me in 2024 with calisthenics + 15kg dumbbel at home https://t.co/qZwfu9r](https://x.com/marclou/status/2106719143194226956) |
| x | EXM7777 | ^236 c22 | [get a 45" monitor ASAP, go in debt if you have to https://t.co/BO5N8emuON](https://x.com/EXM7777/status/2106383269650686199) |
| x | marclou | ^181 c42 | [My little HYROX experiment made it to mainstream media 🤗 https://t.co/dfwfX8vs7O](https://x.com/marclou/status/2106739622474854898) |
| x | AmirMushich | ^168 c15 | [I build more than I publish (you too, right?) You build, experiment, create - an](https://x.com/AmirMushich/status/2106716622761189875) |
| x | steipete | ^161 c12 | [@vburojevic Time to try OpenClaw, we polished the heck out of Telegram and have ](https://x.com/steipete/status/2106837673545695528) |
| x | levelsio | ^128 c3 | [@alexanderrX_ It's not Singapore but it's pretty safe Buenos Aires feels cleaner](https://x.com/levelsio/status/2106701145251156459) |
| x | jackfriks | ^107 c4 | [@peer_rich well he is 5 years younger tbf](https://x.com/jackfriks/status/2106767200245645356) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@egeberkina</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 9920 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/egeberkina/status/2106491431674347618">View @egeberkina on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Doctor Strange https://t.co/pXRYmNGO4D”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์มีแค่แคปชันสั้นๆ ว่า &quot;Doctor Strange&quot; พร้อมรูปหรือลิงก์แนบ ไม่มีข้อความอธิบายเครื่องมือ รีลีส หรือเทคนิคใดๆ และได้ 9,920 likes</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/egeberkina/status/2106491431674347618" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 8410 · 💬 197</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2106446147791597774">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Do I know anyone at Google who could help? We're now over a week in review limbo for OpenClaw's Android app.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Peter Steinberger แจ้งว่าแอป Android ของ OpenClaw ค้างรีวิวบน Google Play มานานกว่าหนึ่งสัปดาห์ และกำลังหาคนรู้จักที่ Google ช่วยเร่ง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โปรเจกต์ดังที่มีผู้ติดตามจำนวนมากยังรอรีวิว Play เกินสัปดาห์ ดังนั้นเวลาอนุมัติของสโตร์เป็นความเสี่ยงต่อกำหนดส่งของงาน mobile ทุกงาน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ส่ง build Android เข้ารีวิว Play ล่วงหน้าอย่างน้อยหนึ่งสัปดาห์ก่อนเดดไลน์ลูกค้า และเผื่อเวลาในแผน release สำหรับกรณีรีวิวค้าง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2106446147791597774" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7178 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2106485806529708368">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@sundarpichai And the new update is live - thanks so much!”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Peter Steinberger (@steipete) ขอบคุณ Sundar Pichai ซีอีโอ Google ว่าอัปเดตที่คุยกันออกสู่ผู้ใช้แล้ว แต่โพสต์ไม่ระบุว่าเป็นผลิตภัณฑ์หรือฟีเจอร์อะไร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2106485806529708368" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@karpathy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2238 · 💬 96</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/karpathy/status/2106806571321966793">View @karpathy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@omarsar0 My mental model for what is happening is that 99%+ of people who are now paying attention have been onboarded to anything related to AI in &lt;1 year. This is very confusing to the AI dinosaurs”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Andrej Karpathy ชี้ว่าคนกว่า 99% ที่ตามข่าว AI ตอนนี้เพิ่งเข้าวงการภายในไม่ถึงปี ทำให้คนที่อยู่มาก่อนปี 2026 หรือก่อนปี 2012 งงกับปฏิกิริยาของตลาด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>บอกว่าผู้ฟังส่วนใหญ่เพิ่งรู้จัก AI จึงอย่าสมมติว่าผู้ใช้หรือลูกค้ารู้พื้นฐานอยู่แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/karpathy/status/2106806571321966793" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@levelsio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1955 · 💬 82</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/levelsio/status/2106695234990063921">View @levelsio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just a day later and now Javier Milei is offering full Argentinean citizenship with residence and passport for $350,000 Countries will keep plucking out the high skilled and wealthy from around the wo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>levelsio รายงานว่า Javier Milei ประธานาธิบดีอาร์เจนตินา เสนอสัญชาติเต็มรูปแบบพร้อมresidence และพาสปอร์ตในราคา $350,000 และชี้ว่าหลายประเทศแย่งดึงคนทักษะสูงและคนมีทรัพย์ เหมือนการดึงชาวนาดัตช์หลัง WW2</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/levelsio/status/2106695234990063921" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@steipete</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1403 · 💬 32</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/steipete/status/2106498506248880323">View @steipete on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@Simemeulation imagine thinking I’d be upset about more people building cool open source shit”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Peter Steinberger (@steipete) ตอบโพสต์หนึ่งว่าเขาไม่ได้หงุดหงิดที่มีคนสร้างโปรเจกต์ open source เพิ่มขึ้น เป็นการโต้ข้อกล่าวหาว่าเขาจะไม่พอใจ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/steipete/status/2106498506248880323" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gregisenberg</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1242 · 💬 90</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gregisenberg/status/2106737353431581132">View @gregisenberg on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“https://t.co/hMysxDLNnz”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์มีเพียงลิงก์ t.co ไม่มีข้อความ จึงไม่มีเครื่องมือ รีลีส หรือข้อมูลที่ประเมินได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gregisenberg/status/2106737353431581132" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@egeberkina</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1163 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/egeberkina/status/2106701967812919373">View @egeberkina on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Dormammu, I've come to bargain! https://t.co/6Xcw6xF8tE”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์เป็นมีมคำพูดจาก Doctor Strange (&quot;Dormammu, I've come to bargain&quot;) พร้อมลิงก์ ไม่มีเนื้อหาที่พูดถึงเครื่องมือ รีลีส หรือเทคนิคใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/egeberkina/status/2106701967812919373" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
