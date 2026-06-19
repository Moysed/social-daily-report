---
type: social-topic-report
date: '2026-06-19'
topic: multimodal-ai
lang: th
pair: multimodal-ai.en.md
generated_at: '2026-06-19T03:46:29+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 221
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- multimodal-ai
- video-generation
- image-generation
- midjourney
- seedance
- production-pipeline
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2067417890098499584/img/MFFwG8qdfYbJALQD.jpg
translated_by: claude-sonnet-4-6
---

# Multimodal AI — 2026-06-19

## TL;DR
- Midjourney ประกาศ pivot ไปด้านฮาร์ดแวร์ — "Midjourney Medical" และเครื่อง ultrasonic CT "Scanner" แบบเต็มตัว อ้างว่าได้ภาพ 3D คุณภาพเทียบ MRI ใน ~60 วินาที ผ่าน transducer on-chip ~358,000 ตัวและน้ำ ไม่ใช้รังสี [1][2][4][16]; ครองความสนใจสูงสุดของวันแต่ไม่เกี่ยวกับ asset pipeline
- Signal ที่ใช้งานได้จริงอยู่ที่ video gen: มีการเปรียบ body-physics ของ Grok Imagine 1.5, ByteDance Seedance 2.0, Google Gemini Omni Flash และ Kling 3.0 Pro [28]; Seedance 2.0 (mini) ปล่อยผ่าน Dreamina/Higgsfield แล้ว [36][48][42]
- Midjourney V8.1 เพิ่ม big-batch draft mode: สร้างภาพ low-res 24 ใบในราคาครึ่งเดียวของ job 4 ภาพมาตรฐาน [18]
- Pipeline tooling เคลื่อน: Runway API "Recipes" เปิด endpoint สำเร็จรูปสำหรับ generative media ในการเรียกครั้งเดียว [58]; ComfyUI สาธิต video rebuild ด้วย motion data [43]; Photoshop AI Assistant แก้ข้อความแบบ context-aware [60]
- Midjourney ถูกอธิบายว่าไม่มี VC, รายได้ ~$500M, พนักงานไม่ถึง 200 คน ใช้รายได้จากผลิตภัณฑ์ image อุดหนุน R&D [6][22] — เกี่ยวข้องกับการประเมินว่า cadence ของ image/video จะดำเนินต่อหรือไม่

## สิ่งที่เกิดขึ้น
ปริมาณโพสต์ของวันกระจุกอยู่ที่การประกาศฮาร์ดแวร์ของ Midjourney: "Midjourney Medical" และเครื่อง ultrasonic computational-tomography "Scanner" แบบเต็มตัว อ้างภาพ 3D คุณภาพ MRI ใน ~60 วินาที ใช้เสียงและน้ำแทนรังสีหรือแม่เหล็ก มี transducer on-chip ~358,000 ตัว เป้าหมายคือ 50,000 เครื่องทำ scan หนึ่งพันล้านครั้งต่อเดือน [1][2][3][4][16][53] รายการที่ได้คะแนนสูงส่วนใหญ่เป็นปฏิกิริยาและการคาดเดา ไม่ใช่ข้อมูล [5][9][13][19][24][32][51] และมีแพทย์อย่างน้อยหนึ่งคนระบุว่าข้อมูลเทคนิคที่แข็งพอยังมีน้อย [37] บริษัทถูกอธิบายซ้ำว่าได้รับทุนจากชุมชน รายได้ ~$100M ใน 9 เดือนแรกแล้วพุ่งเกิน $500M พนักงานไม่ถึง 200 คน [6][22]

## ความสำคัญ (เหตุผล)
สำหรับ pipeline ของ NDF DEV (เกม, ฉาก XR, ภาพ edutech) เรื่อง Midjourney Medical ไม่สามารถนำไปใช้งานได้ — มันคือการพนันฮาร์ดแวร์ด้านสุขภาพ ไม่ใช่การสร้าง asset และแรงดึงดูดส่วนใหญ่เป็นความรู้สึก ไม่ใช่ความสามารถที่ตรวจยืนยันแล้ว [5][9][13][37] Signal ที่ใช้ได้คือการแข่งขัน video gen: หลาย lab ส่งโมเดลที่ทัดเทียมกันในช่วงเวลาเดียวกัน [28][36] บวกราคาเชิงรุก (draft batch ราคาครึ่งหนึ่ง [18], แผน unlimited รายเดือนผ่าน Higgsfield [42]) ลดต้นทุน concept frame, animatic และ b-roll สำหรับ edutech Runway Recipes [58] และ ComfyUI motion workflow [43] สำคัญโดยเฉพาะเพราะมุ่งที่การผสานเข้า pipeline ไม่ใช่ demo ครั้งเดียว ซึ่งตรงกับความต้องการเครื่องมือที่ป้อนสู่ production ความเสี่ยงทางอ้อม: Midjourney กำลังเบนความสนใจสาธารณะไปที่ medical ประมาณหกเดือนข้างหน้าตามที่ CEO กำหนดกรอบ [14] ขณะที่ผลิตภัณฑ์ image เป็นตัวหล่อเลี้ยง R&D [6] — ดังนั้น cadence ของฟีเจอร์ image/video อาจชะลอลงแม้รายได้จะแข็งแกร่ง

## ความเป็นไปได้
การวนซ้ำโมเดล video อย่างรวดเร็วต่อเนื่องมีแนวโน้มสูง — มีคู่แข่งสี่รายถูกเปรียบเทียบในการทดสอบเดียวและหลายรายส่งออกมาเกือบพร้อมกัน [28][36][48] open-weight model ที่สู้หรือชนะ Fable ได้นั้นเป็นไปได้แต่ยังไม่ได้รับการพิสูจน์ รายการ [27] นำเสนอในฐานะสมมติฐานเท่านั้น ไม่ใช่การเปิดตัว เป้าหมายฝูงเครื่อง 50,000 เครื่อง/scan หนึ่งพันล้านครั้งต่อเดือนของ Midjourney ไม่น่าเกิดขึ้นในขอบฟ้าใกล้ใด — เป็นเป้าหมายในอุดมคติที่ยังไม่มีข้อมูลอุปกรณ์จริงและมีความเห็นเชิงสงสัยจากแพทย์ [4][37] และ "MRI-quality" ยังคงเป็น claim ทางการตลาด ยังไม่ได้รับการตรวจสอบยืนยัน [11][16][37] ไม่มีแหล่งใดให้ค่าความน่าจะเป็นเป็นตัวเลข จึงไม่มีการระบุไว้ที่นี่

## การใช้งานในองค์กร — NDF DEV
การดำเนินการ: (1) ทดสอบ bake-off สั้นๆ ระหว่าง Seedance 2.0, Kling 3.0 และ Grok Imagine 1.5 สำหรับ b-roll edutech และช็อต game trailer โดยใช้การเปรียบ body-physics ที่เผยแพร่เป็นตัวกรองเริ่มต้น [28][36][57] — effort ต่ำ (2) ใช้ Midjourney V8.1 big-batch draft mode สำหรับการสร้าง concept ราคาถูกก่อน commit ไปที่ high-res render [18] — ต่ำ (3) Prototype Runway API Recipes หากต้องการ generative endpoint แบบ hosted ภายในเครื่องมือ content หรือ app web/mobile [58] — กลาง (4) ประเมิน ComfyUI motion-data workflow สำหรับ animation/XR previz ที่มี motion capture อยู่แล้ว [43] — กลาง (5) ทดลอง Photoshop AI Assistant สำหรับ asset cleanup ที่รักษา consistency [60] — ต่ำ ข้าม: Midjourney Medical และเนื้อหา scanner ทั้งหมด [1][2][3][4][9][16][53] — ไม่เกี่ยวกับ pipeline ของคุณ; และอย่าให้น้ำหนักกับ claim "MRI-quality"/ฝูงเครื่องที่ยังไม่ยืนยัน [11][37] ยกเลิกแผนใดก็ตามที่ขึ้นอยู่กับ scenario open-weight-ชนะ-Fable จนกว่าโมเดลนั้นจะปล่อยออกมาจริง [27]

## สัญญาณที่ต้องจับตา
- open-weight model จากจีนที่ชนะ Fable จริงๆ ในเชิง benchmark และ feel นอกเหนือจากสมมติฐาน [27]
- ราคา Seedance 2.0 และความยั่งยืนของโควตาบน offer unlimited ของ Higgsfield [42][48]
- การ rollout Runway Recipes API และ endpoint ไหนบ้างที่พร้อม production [58]
- Midjourney image/video feature cadence ชะลอหรือไม่เมื่อ Medical ดูดซับความสนใจประมาณ ~6 เดือนข้างหน้า [14][6]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | midjourney | ^32439 c2080 | [Announcing a new division of Midjourney called "Midjourney Medical" https://t.co](https://x.com/midjourney/status/2067421950314688759) |
| x | midjourney | ^25306 c1101 | [A technical dive inside our new "Midjourney Scanner" https://t.co/wJBHz2O7ro](https://x.com/midjourney/status/2067422898407837797) |
| x | Pirat_Nation | ^5341 c99 | [Midjourney, the company behind the popular AI image generator, has unveiled what](https://x.com/Pirat_Nation/status/2067517672120787395) |
| x | nickfloats | ^4175 c133 | [Full body ultrasonic computational tomography Our goal is to build a fleet of 50](https://x.com/nickfloats/status/2067423587540123853) |
| x | aakashgupta | ^3524 c103 | [Let me explain why an AI art company just built a full-body medical scanner, bec](https://x.com/aakashgupta/status/2067579580622528913) |
| x | nickfloats | ^3497 c86 | [What Midjourney is: - No investors, fully community-funded research lab - Revenu](https://x.com/nickfloats/status/2067445022484529282) |
| x | midjourney | ^3287 c752 | [We're gonna do a Midjourney Medical AMA (ask me anything ) right here all aftern](https://x.com/midjourney/status/2067688872944025975) |
| x | amazingzeros | ^3267 c10 | [sonic fan pissing their pants about fortnite as if sora ai getting deleted didn'](https://x.com/amazingzeros/status/2067666616700334555) |
| x | afshineemrani | ^3149 c105 | [I'm a cardiologist. Something just happened today that I genuinely did not see c](https://x.com/afshineemrani/status/2067630924108538083) |
| x | levelsio | ^2629 c86 | [I don't know if it's obvious information or not but if you talk to random people](https://x.com/levelsio/status/2067662326082498899) |
| x | digijordan | ^2377 c143 | [Midjourney just shocked the world: They're building the Midjourney Scanner…a ful](https://x.com/digijordan/status/2067495206459519338) |
| x | is_OwenLewis | ^1987 c81 | [I did not see this one coming. BREAKING NEWS folks! Midjourney, yes the AI image](https://x.com/is_OwenLewis/status/2067467282180370447) |
| x | _sholtodouglas | ^1642 c53 | [If deployed widely - I bet this will save the US healthcare system at least 100x](https://x.com/_sholtodouglas/status/2067473495920140363) |
| x | ZeffMax | ^1602 c13 | [Loved Midjourney CEO David Holz's answer on what to make of the company now: "We](https://x.com/ZeffMax/status/2067479376518902219) |
| x | itsandrewgao | ^1342 c22 | [. @midjourney Scanner interactive 3d model I made! fun piece of trivia: I intern](https://x.com/itsandrewgao/status/2067513003227148579) |
| x | AdrianDittmann | ^941 c68 | [This is so cool! Midjourney Medical built a full body Ultrasonic CT scanner. You](https://x.com/AdrianDittmann/status/2067574011626946587) |
| x | Prolotario1 | ^868 c79 | [Quite The Eventful Day It Has Been: New Air Force 1 New GTA 6 Promo New Midjourn](https://x.com/Prolotario1/status/2067768517613551818) |
| x | midjourney | ^833 c29 | [We've released a new big-batch draft mode for V8.1. This new mode lets you gener](https://x.com/midjourney/status/2067292710063800483) |
| x | peer_rich | ^797 c15 | [we were promised AI to solve cancer by big tech and its a tiny AI bootstrapped f](https://x.com/peer_rich/status/2067493323015655566) |
| x | cignificants | ^786 c10 | [so hey, aside from midjourney and gemini what other generative AI program do you](https://x.com/cignificants/status/2067644406728135033) |
| x | midjourney | ^734 c47 | [t-minus 3 hours! we will drop a Livestream link soon. keep watch 🫡](https://x.com/midjourney/status/2067367868837322980) |
| x | dcbruck | ^631 c14 | [0 VC funding. $500M(+) in revenue. Less than 200 employees. And now they're rein](https://x.com/dcbruck/status/2067599482519216293) |
| x | BrianRoemmele | ^603 c44 | [Electronic Medicine is the future: Sound waves vs. Radiation. Currents and frequ](https://x.com/BrianRoemmele/status/2067619864370634919) |
| x | pronounced_kyle | ^589 c16 | [I'm calling it: this is the start of a new era in tech. First tangible example o](https://x.com/pronounced_kyle/status/2067595725404590439) |
| x | Scobleizer | ^571 c41 | [Congrats @midjourney and @DavidSHolz. It has been a while since a new product in](https://x.com/Scobleizer/status/2067489364725412345) |
| x | tomhfh | ^525 c20 | [This is so cool. A full-body ultrasound using no radiation and no magnets. Thank](https://x.com/tomhfh/status/2067550047483437079) |
| x | EMostaque | ^447 c102 | [How would you change your priors if a Chinese lab released an open model that be](https://x.com/EMostaque/status/2067610502826463409) |
| x | YourAlphaMom | ^404 c51 | [New body-physics test for the best AI video tools: The newly released Grok Imagi](https://x.com/YourAlphaMom/status/2067296958797025677) |
| x | swyx | ^391 c43 | [my notes from the @midjourney medical launch - @Scobleizer compared this to the ](https://x.com/swyx/status/2067468331918242127) |
| x | beffjezos | ^368 c27 | [Midjourney using its image gen AI expertise for next-gen imaging of the human bo](https://x.com/beffjezos/status/2067472148202184958) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 32439 · 💬 2080</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067421950314688759">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Announcing a new division of Midjourney called &quot;Midjourney Medical&quot; https://t.co/c14YcO6yaU”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney เปิดแผนกใหม่ชื่อ Midjourney Medical นำ generative image AI เข้าสู่วงการแพทย์โดยตรง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Midjourney เข้า vertical ที่มีการควบคุมเข้มงวด แสดงว่า multimodal AI โตพ้นแค่ creative tool — ใกล้เคียงกับงาน XR medical training</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม output ของ Midjourney Medical เป็น reference สำหรับ medical simulation asset pipeline ถ้า studio จะทำงาน e-learning หรือ XR ด้านสุขภาพ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2067421950314688759" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 25306 · 💬 1101</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067422898407837797">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A technical dive inside our new &quot;Midjourney Scanner&quot; https://t.co/wJBHz2O7ro”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney เผยแพร่บทความเทคนิคเจาะลึก 'Midjourney Scanner' ระบบใหม่ พร้อมอธิบาย architecture และการทำงานภายใน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Studio ที่ใช้ Midjourney สร้าง asset ได้ประโยชน์จากการเข้าใจ scanning pipeline โดยเฉพาะด้าน content safety และ quality control</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">อ่านบทความแล้วดูว่า approach ของ scanner ใช้เป็นแนวทางสำหรับ AI asset validation ใน workflow ของ studio ได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2067422898407837797" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5341 · 💬 99</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2067517672120787395">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Midjourney, the company behind the popular AI image generator, has unveiled what it says is the world’s first full-body ultrasound CT scanner. &gt;The technology aims to make full-body imaging safer and ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney (บริษัท AI image generator) เปิดตัวเครื่อง ultrasound CT แบบ full-body สแกนอวัยวะ 25+ ชิ้นใน ~1 นาที ไม่ใช้รังสี เป้าหมาย FDA approval และวางตลาดปลาย 2027</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2067517672120787395" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nickfloats</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4175 · 💬 133</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nickfloats/status/2067423587540123853">View @nickfloats on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Full body ultrasonic computational tomography Our goal is to build a fleet of 50,000 of these scanners capable together of doing a billion scans a month. Enough to bring full body imaging to everyone ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney Medical ประกาศเป้าหมายสร้าง scanner อัลตราซาวด์ CT แบบ full-body จำนวน 50,000 เครื่อง รองรับ scan 1 พันล้านครั้งต่อเดือนทั่วโลก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nickfloats/status/2067423587540123853" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@aakashgupta</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3524 · 💬 103</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/aakashgupta/status/2067579580622528913">View @aakashgupta on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Let me explain why an AI art company just built a full-body medical scanner, because almost everyone is reading this as a random pivot. Ultrasonic CT works by firing sound through your body and record”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney นำ image reconstruction model มาแก้ปัญหา inverse-scattering ของ ultrasonic CT — สแกนร่างกายเต็มตัวใน 60 วินาที ความละเอียด sub-millimeter และ deploy ใน spa แทน clinic</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า core skill ของ generative model (แปลง noisy input → coherent output) ใช้ข้าม modality ได้จริง ไม่ได้ล็อคอยู่แค่ text-to-image</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">งาน XR หรืองานที่มี sensor เยอะ — ดูว่า AI reconstruction pipeline ที่มีอยู่รับ input type ใหม่ (audio, depth, IMU) ได้ไหมก่อนสร้าง model ใหม่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/aakashgupta/status/2067579580622528913" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nickfloats</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3497 · 💬 86</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nickfloats/status/2067445022484529282">View @nickfloats on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“What Midjourney is: - No investors, fully community-funded research lab - Revenue from image generation product funds all R&amp;D - ~$100M in first 9 months, $200M by month 12, still growing - 8 active pr”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney บูตสแตรปจนมีรายได้ ~$200M/ปี ไม่มีนักลงทุน บริหารโดย David Holz (ผู้ก่อตั้ง Leap Motion และ AR headset Northstar) พร้อมเตรียมส่ง consumer hardware 2 รายการเร็วๆ นี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แนวคิดของ Holz ที่ว่า human-tech interaction คือ bottleneck จริงๆ ตรงกับโจทย์ XR/VR UX และ track record hardware ของเขาทำให้ 2 consumer device ที่กำลังจะมาน่าจับตา</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตามประกาศ hardware 2 รายการจาก Midjourney — ถ้าเป็น input/sensing device ให้ประเมินว่าเข้า XR/VR prototyping pipeline ของทีมได้หรือไม่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nickfloats/status/2067445022484529282" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@midjourney</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3287 · 💬 752</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/midjourney/status/2067688872944025975">View @midjourney on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We're gonna do a Midjourney Medical AMA (ask me anything ) right here all afternoon. Post your questions below and we'll try to answer as many as we can! ❤️”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Midjourney ประกาศ AMA หัวข้อ Medical บน X แบบเรียลไทม์ ไม่มีรายละเอียด product หรือ release ใดๆ เป็นแค่คำเชิญถามตอบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/midjourney/status/2067688872944025975" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@amazingzeros</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3267 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/amazingzeros/status/2067666616700334555">View @amazingzeros on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“sonic fan pissing their pants about fortnite as if sora ai getting deleted didn’t set their games back by 20 years”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ล้อเลียนแฟน Sonic เรื่อง Fortnite พร้อมพูดเกินจริงว่า 'Sora AI โดนลบ' — ไม่มีข้อมูลจริงเกี่ยวกับ AI ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/amazingzeros/status/2067666616700334555" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
