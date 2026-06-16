---
type: social-topic-report
date: '2026-06-11'
topic: web-frontend
lang: th
pair: web-frontend.en.md
generated_at: '2026-06-11T03:37:37+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- hackernews
- lobsters
- x
regions:
- global
post_count: 62
salience: 0.6
sentiment: positive
confidence: 0.62
tags:
- astro
- rust-tooling
- html-first
- vite8
- ai-coding
- css
thumbnail: https://pbs.twimg.com/media/HKYYQczWQAAu38P.jpg
translated_by: claude-sonnet-4-6
---

# Web & Frontend — 2026-06-11

## TL;DR
- Astro v7 beta พร้อมใช้แล้วผ่าน `npx @astrojs/upgrade beta` — compiler เขียนใหม่ใน Rust, Rust-powered Markdown pipeline เป็น default, และอัปเกรดเป็น Vite 8 เพื่อ build เร็วขึ้น [45][49][55].
- Starlight v0.40 เชื่อมกับ Rust Markdown pipeline ใหม่ของ Astro สำหรับ build docs เร็วขึ้น [17].
- เว็บไซต์ที่ rebuild แบบ 'HTML-first' รายงานว่า users เพิ่มเป็น 2 เท่าในคืนเดียว — ติดอันดับ 1 บน HN ด้วย 1013 points [1].
- Claude Fable 5 ขึ้นอันดับ 1 ใน Code Arena: Frontend (sub-leaderboards HTML และ React) นำหน้า Opus-4.8 [3].
- เครื่องมือพร้อม ship สองตัวปรากฏขึ้น: 'Nuxi' AI assistant ในตัว framework ของ Nuxt [13] และ Extend UI ซึ่งเป็น open-source components 14 ตัวสำหรับ PDF/DOCX/XLSX viewers [25].

## สิ่งที่เกิดขึ้น
เรื่องหลักของ frontend วันนี้คือ Astro v7 beta ติดตั้งได้แล้วทันที (`npx @astrojs/upgrade beta`) โดย rewrite Astro compiler ใน Rust, ตั้ง Rust-powered Markdown pipeline เป็น default, และย้ายไปใช้ Vite 8 — ทีมงานสรุปว่า build เร็วขึ้นทุกด้าน [45][49][55][56][60]. Astro เผยแพร่ draft migration guide [48] แล้ว, ยืนยันว่า SSR มีมาตั้งแต่ 1.0 [57], และ Starlight v0.40 รองรับ Rust Markdown pipeline ใหม่ [17]. โพสต์ teaser [2][33] คือ release เดียวกัน.

## ทำไมถึงสำคัญ (reasoning)
สองแนวโน้มอิสระชี้ทิศทางเดียวกัน: ต้นทุน build/runtime คือสมรภูมิปัจจุบัน Astro กำลัง push native (Rust) tooling เข้าไปใน JS workflow เพื่อลด build time [49] ขณะที่บทความ HTML-first ชี้ว่าการส่ง JS น้อยลงทำให้ user จริงเพิ่มขึ้น [1]. สำหรับ studio ที่สร้าง docs, marketing, และ edutech sites ทั้งสองแนวทางลดต้นทุนของหน้าที่โหลดเร็วโดยไม่ต้อง rewrite. แยกกัน, AI assistants ในตัว framework (Nuxt's Nuxi [13]) และโมเดล coding ที่ tune สำหรับ frontend (Fable #1 บน HTML/React [3]) บ่งชี้ว่า framework vendors ถือ AI helper เป็นส่วนหนึ่งของ product surface ไม่ใช่ add-on. Extend UI [25] สำคัญในขอบเขตแคบแต่ตรงประเด็น: prebuilt PDF/DOCX/XLSX viewers พร้อม bounding-box citations ตรงกับ feature เอกสารของ edutech/e-learning. ข้อควรระวัง: '#react' ส่วนใหญ่ใน feed นี้คือ reaction videos [6][10][28][39] ไม่ใช่ React.js — signal จริงของ framework จึงบางกว่าที่จำนวน item บ่งบอก.

## ความเป็นไปได้
น่าจะเกิด: Astro v7 stable ออกไม่นานหลัง beta นี้ เพราะมี migration guide เผยแพร่แล้วและ vendor ส่ง messaging อย่างต่อเนื่อง [45][48][55]. เป็นไปได้: รูปแบบ Rust-under-JS-tooling (Astro compiler, Vite 8) จะขยายไปยังเครื่องมือใกล้เคียง เพราะผลตอบแทนที่ระบุคือ build เร็วขึ้นล้วนๆ โดยไม่มีการเปลี่ยน API [49]. เป็นไปได้: AI assistants ในตัว framework กลายเป็น expectation มาตรฐาน เมื่อ Nuxt ship Nuxi และ benchmark coding ของ frontend ได้รับความสนใจมากขึ้น [3][13]. ไม่น่าเกิดจากหลักฐานนี้: 'HTML-first' กลายเป็น trend ที่วัดได้ — [1] เป็นกรณีเดียวที่ไม่มี methodology จึงควรมองคำอ้าง 'users เพิ่มเป็น 2 เท่า' เป็นทิศทาง ไม่ใช่ข้อพิสูจน์.

## การนำไปใช้สำหรับ NDF DEV
1) ทดลอง Astro v7 beta บน docs หรือ marketing site ที่ไม่ critical แล้ววัด build delta จาก Vite 8 + Rust Markdown — effort น้อย, ถอนคืนได้ [45][48][49]. 2) สำหรับ marketing/landing pages ใหม่ ใช้หลักการ HTML-first (ลด JS, server-render) แล้ววัด conversion/load แทนที่จะสร้าง heavy SPA — effort ต่ำถึงกลาง [1]. 3) ประเมิน Extend UI สำหรับ feature edutech/e-learning ที่แสดง PDF/DOCX/XLSX พร้อม citations ก่อนสร้าง viewer เอง — effort กลาง [25]. 4) ถ้าใช้ Starlight สำหรับ docs ให้อัปเป็น v0.40 เพื่อรับ Markdown pipeline ที่เร็วขึ้น — effort น้อย [17]. ข้ามไปก่อน: Datastar [54] และ Automerge multiplayer [58] น่าสนใจแต่ยังไม่พิสูจน์กับ stack เรา, อย่าตาม noise ของ reaction video [6][10][28], รอก่อนสำหรับ Nuxi จนกว่าจะมี project ที่ใช้ Nuxt อยู่แล้ว [13].

## สัญญาณที่ต้องจับตา
- เวลา release Astro v7 stable และว่า Rust compiler จะมี breaking changes นอกเหนือจาก draft guide หรือไม่ [48][49].
- ตัวเลข build-time จริงจาก Vite 8 + Rust Markdown เมื่อทีมรายงาน ไม่ใช่ vendor claims [49][55].
- การนำ Extend UI ไปใช้และความสมบูรณ์ของ component สำหรับ document viewers ที่เกี่ยวกับ edutech [25].
- ว่า AI assistants ในตัว framework (Nuxi) จะกลายเป็นมาตรฐานใน framework อื่นๆ หรือไม่ [13].

## Repos & Tools ที่น่าลอง
| repo | source | url |
|---|---|---|
| **anthropics/claude-code** — Claude Desktop สร้าง Hyper-V VM ขนาด 1.8 GB ทุกครั้งที่เปิด แม้ใช้แค่ chat | hackernews | <https://github.com/anthropics/claude-code> |
| **HelixDB/helix-db** — Show HN: HelixDB – A graph database บน object storage เวลากว่าหนึ่งปีผ่านมาแล้วนับแต่ | hackernews | <https://github.com/HelixDB/helix-db> |

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| hackernews | edent | ^1013 c467 | [การสร้างเว็บแบบ HTML-first ทำให้ users เพิ่มเป็น 2 เท่าในคืนเดียว](https://mohkohn.co.uk/writing/html-first/) |
| x | astrodotbuild | ^980 c32 | [Shh, ห้ามบอกใคร แต่… https://t.co/D0IqKxElSm](https://x.com/astrodotbuild/status/2064364152861130754) |
| x | arena | ^751 c29 | [Claude Fable 5 ขึ้นอันดับ 1 ใน Code Arena: Frontend นำห่างมากจาก O](https://x.com/arena/status/2064858698582040693) |
| x | TheLastRefuge2 | ^559 c31 | [Keir Starmer แนะนำสิ่งที่ต้องทำขณะการตัดหัวของคุณเริ่มต้น: 1. Do](https://x.com/TheLastRefuge2/status/2064856349343903781) |
| hackernews | eries | ^549 c436 | [ผม Eric Ries ผู้เขียน "The Lean Startup" และหนังสือใหม่ "Incorruptible" – AMA H](https://news.ycombinator.com/item?id=48477135) |
| x | FadelStruggle | ^430 c2 | [FADEL AND ARUUU REACT TO KINGDOM HEARTS 4!!! https://t.co/xN72pzsJqv](https://x.com/FadelStruggle/status/2064856245354328137) |
| x | worshipVK | ^405 c22 | [YRF ล้มเหลวซื้อมโนธรรมของ celebrity ยิ่งใหญ่ที่สุดของอินเดีย 🚨 มีรายงานว่า YRF เข้าหา](https://x.com/worshipVK/status/2064892709945721195) |
| hackernews | levkk | ^402 c204 | [PgDog ได้รับทุนและกำลังมาสู่ database ของคุณ](https://pgdog.dev/blog/our-funding-announcement) |
| hackernews | tonyrice | ^356 c250 | [Claude Desktop สร้าง Hyper-V VM ขนาด 1.8 GB ทุกครั้งที่เปิด แม้ใช้แค่ chat](https://github.com/anthropics/claude-code/issues/29045) |
| x | Bughaupdate | ^275 c3 | [Peter และ Clix react ต่อ shockwave play สุดโหดของ Bugha 😮 @bugha @PeterbotFN @Clix ](https://x.com/Bughaupdate/status/2064858794375643391) |
| hackernews | speckx | ^267 c250 | [นักวิจัย cybersecurity ไม่พอใจ guardrails ของ Anthropic's Fable](https://techcrunch.com/2026/06/10/cybersecurity-researchers-arent-happy-about-the-guardrails-on-anthropics-fable/) |
| hackernews | lebovic | ^239 c104 | [Anthropic กำหนดให้เก็บ data 30 วันสำหรับ Fable และ Mythos <a href="https:&#x](https://support.claude.com/en/articles/15425996-data-retention-practices-for-mythos-class-models) |
| x | nuxt_js | ^217 c6 | [พบกับ Nuxi 💚 AI assistant บน https://t.co/yNaJyLcNP3 มีชื่อแล้ว และ](https://x.com/nuxt_js/status/2064369763271508244) |
| x | RMistereggen | ^211 c9 | [ถ้าคุณตอบสนองด้านลบต่อปฏิกิริยาโกรธตามธรรมชาติจากการตัดหัวใน st](https://x.com/RMistereggen/status/2064860368237703462) |
| x | Pirat_Nation | ^209 c71 | [Fable reboot ที่กำลังจะมาถึงกำลังถอยห่างจาก good-and-evil ดั้งเดิมของซีรีส์](https://x.com/Pirat_Nation/status/2064890611677712829) |
| hackernews | momentmaker | ^204 c70 | [สถานีรถไฟญี่ปุ่นทั้ง 9,300 แห่ง แสดงแบบ animated ตามปีที่เปิด (1872–2026)](https://jivx.com/eki) |
| x | astrodotbuild | ^198 c3 | [Starlight v0.40 รองรับ Rust-y Markdown pipeline ใหม่ของ Astro เพิ่มความเร็ว ](https://x.com/astrodotbuild/status/2064631912870629884) |
| hackernews | akman | ^184 c208 | [Raspberry Pi 5 – 16GB RAM](https://www.adafruit.com/product/6125?src=raspberrypi) |
| hackernews | pseudolus | ^183 c41 | [JPL ทำให้ Curiosity rover อายุ 13 ปียังทำวิทยาศาสตร์ได้อย่างไร](https://spectrum.ieee.org/curiosity-rover-jpl-mars-science) |
| hackernews | anhldbk | ^180 c95 | [Apache Burr: สร้าง AI agents และ applications ที่เชื่อถือได้](https://burr.apache.org/) |
| x | NTE_Ani_Info | ^179 c1 | [รู้ไหมว่าถ้านำ Porsche ไปใกล้ NPCs พวกเขาจะ react ต่อมัน? พวกเขาจะ](https://x.com/NTE_Ani_Info/status/2064854875746230560) |
| hackernews | jonbaer | ^171 c12 | [GeoLibre 1.0](https://geolibre.app/) |
| hackernews | idlewords | ^168 c26 | [L'Affaire Siloxane](https://mceglowski.substack.com/p/laffaire-siloxane) |
| hackernews | tanelpoder | ^164 c38 | [AI agent ก่อความวุ่นวายใน Fedora และที่อื่น](https://lwn.net/SubscriberLink/1077035/c7e7c14fbd60fae9/) |
| hackernews | kbyatnal | ^163 c41 | [Show HN: Extend UI – open-source UI kit สำหรับ modern document apps เรา open](https://www.extend.ai/ui) |
| hackernews | Multicomp | ^153 c31 | [ปัญหา Authentication เกี่ยวกับ API requests](https://www.githubstatus.com/incidents/fcj3088jg1wx) |
| x | Trevornoah | ^141 c12 | [World Cup Watch Party ใกล้มาแล้ว ร่วมกับผมและเพื่อนพิเศษ](https://x.com/Trevornoah/status/2064860530092003622) |
| x | schwloperbk | ^130 c7 | ["เราได้ทำ kids react, teens react, elders react, youtubers react, holocaust su](https://x.com/schwloperbk/status/2064881066100543724) |
| hackernews | vinhnx | ^123 c87 | [Notes on DeepSeek](https://news.ycombinator.com/item?id=48476474) |
| x | MettallicOnyx | ^121 c1 | [@King_Jayded @MagnoGetMoney ผมชอบคิดว่าทุกคนสามารถได้ยินและ n](https://x.com/MettallicOnyx/status/2064886130873614365) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@astrodotbuild</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 980 · 💬 32</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/astrodotbuild/status/2064364152861130754">View @astrodotbuild on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Shh, don’t tell anyone, but… https://t.co/D0IqKxElSm”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@astrodotbuild โพสต์ภาพ teaser ลึกลับโดยไม่มีข้อความประกอบ — content จริงอยู่ในรูปที่เปิดไม่ได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/astrodotbuild/status/2064364152861130754" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@arena</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 751 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/arena/status/2064858698582040693">View @arena on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Claude Fable 5 ranks #1 in Code Arena: Frontend, leading by a wide margin over Opus-4.8. Highlights: - #1 in every sub leaderboard: HTML, React - #1 in every sub category: Brand &amp; Marketing, Reference”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Claude Fable 5 ของ Anthropic ครองอันดับ 1 ใน Code Arena Frontend ทุก sub-category — HTML, React, Brand &amp; Marketing, Data &amp; Analytics, Consumer Product, Gaming — เหนือกว่า Opus-4.8</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Fable 5 เป็น model ที่ดีที่สุดสำหรับ frontend code generation ใน HTML, React และ UI categories ที่ตรงกับงาน web และ game UI ของทีมพอดี</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ประเมิน Fable 5 เป็น default model สำหรับงาน frontend และ UI generation ใน AI-assisted coding workflow ของทีม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/arena/status/2064858698582040693" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TheLastRefuge2</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 559 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheLastRefuge2/status/2064856349343903781">View @TheLastRefuge2 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Keir Starmer provides instructions on what to do as your beheading starts: 1. Don’t be racist 2. Don’t be islamaphobic 3. Patiently wait for police to come arrest you 4. Do not react in anger 5. Befor”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์เสียดสีการเมืองของ UK เกี่ยวกับ Keir Starmer กับประเด็นอาชญากรรม ไม่มีเนื้อหาด้านเทคโนโลยี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheLastRefuge2/status/2064856349343903781" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@FadelStruggle</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 430 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/FadelStruggle/status/2064856245354328137">View @FadelStruggle on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“FADEL AND ARUUU REACT TO KINGDOM HEARTS 4!!! https://t.co/xN72pzsJqv”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Content creator สองคนชื่อ Fadel และ Aruuu ทำ reaction video ต่อประกาศ Kingdom Hearts 4</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/FadelStruggle/status/2064856245354328137" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@worshipVK</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 405 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/worshipVK/status/2064892709945721195">View @worshipVK on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“YRF failed to buy morals of India's greatest celebrity 🚨 YRF reportedly approached several celebs like Salman, SRK and even cricketers to promote Alpha. They allegedly offered Virat Kohli 2.5 crore as”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>สตูดิโอ Bollywood ถูกรายงานว่าเสนอเงิน ₹2.5 crore ให้ Virat Kohli ชมตัวอย่างหนัง แต่เขาปฏิเสธ เพราะไม่ endorses สิ่งที่ยังไม่ได้ดูเอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/worshipVK/status/2064892709945721195" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Bughaupdate</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 275 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Bughaupdate/status/2064858794375643391">View @Bughaupdate on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Peter and Clix react to Bugha’s insane shockwave play😮 @bugha @PeterbotFN @Clix https://t.co/e3w9YoaOJG”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Fortnite pro player Bugha, Peter และ Clix แชร์คลิป reaction การใช้ shockwave ในเกม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Bughaupdate/status/2064858794375643391" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nuxt_js</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 217 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nuxt_js/status/2064369763271508244">View @nuxt_js on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Meet Nuxi 💚 Our AI assistant on https://t.co/yNaJyLcNP3 now has a name, and a face. Sign in with GitHub and Nuxi remembers you: ✨ Conversations saved across devices 🌿 Branch chats to explore different”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Nuxt.js เปิดตัว AI assistant ชื่อ 'Nuxi' บน nuxt.com — login ด้วย GitHub, บันทึก conversation ข้ามอุปกรณ์, แตก branch chat ได้, และอิงข้อมูลจาก official docs ทั้ง ecosystem</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Assistant ที่อิง official docs โดยตรงช่วยลดเวลาค้นหาใน Nuxt docs และ module references ระหว่าง development ได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">งาน web ที่ใช้ Nuxt ให้เปิด Nuxi ด้วย ⌘I หรือ nuxt.com/dashboard/chat เป็น first stop แทนการค้น docs เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nuxt_js/status/2064369763271508244" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RMistereggen</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 211 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RMistereggen/status/2064860368237703462">View @RMistereggen on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If you react negatively to normal reactions of anger due to beheadings in the streets, you’re the problem. If anything should make you react, it’s the beheading of people in your streets as well as li”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้แสดงความโกรธเกี่ยวกับเหตุรุนแรง เรียกร้องให้คนตอบสนองต่อความรุนแรงบนท้องถนนและการโจมตีเด็ก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RMistereggen/status/2064860368237703462" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
