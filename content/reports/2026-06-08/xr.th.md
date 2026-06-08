---
type: social-topic-report
date: '2026-06-08'
topic: xr
lang: th
pair: xr.en.md
generated_at: '2026-06-08T15:22:34+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 85
salience: 0.58
sentiment: mixed
confidence: 0.55
tags:
- xr
- vision-pro
- android-xr
- wwdc
- vr-gaming
- spatial-computing
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2063870837749428224/img/x0INMeQpqThJMJnE.jpg
translated_by: claude-sonnet-4-6
---

# XR / VR / AR — 2026-06-08

## TL;DR
- ช่วง WWDC week ครองสัญญาณข่าว: Mike Rockwell (หัวหน้าทีม Vision Pro) ถูกรายงานว่าขึ้นดูแล Siri และ visionOS 27 คาดว่าจะเพิ่ม Siri ใหม่พร้อม systemwide AI [5][14][22][13]
- กระแส 'Vision Pro ตายแล้ว' จากต้นปี 2025 ถูกโต้แย้ง — ฝ่ายสนับสนุนชี้ว่า Apple ส่ง M5 Vision Pro ออกมาหลังจากที่ถูกรายงานว่าหยุดผลิตแล้ว [2][15]
- Google ผลักดัน Android XR อย่างเปิดเผย: สาธิตสดที่ CVPR 2026 พร้อม 'spatial intelligence' และ Project Aura glasses (ผสาน Gemini, ประมวลผลและแบตเตอรี่อยู่ใน pack แยก, ไม่ต้องพ่วงโทรศัพท์) เป้าหมายเปิดตัวปลายปีนี้ [33][44][54][53]
- สัญญาณแนวโน้ม hardware: การคาดการณ์และดีไซน์ที่มีอยู่ชี้ไปยังหูฟังน้ำหนักเบา, โล่งรอบตา, ไม่มีพัดลม โดยย้ายระบบประมวลผลและแบตเตอรี่ไปไว้ใน external puck (แนวทางเดียวกับ Magic Leap; อ้างถึง Pico Project Swan, Galaxy XR, Quest Pro) [37][57]
- บันทึก VR gaming + tooling: Perfect Dark VR alpha ได้รับคำชม, 6DoF ผ่าน Virtual Desktop บน Quest 3, Quest store ยังลิสต์เกมที่ปิดให้บริการแล้ว, และ Godot companion app ที่ export builds Android/XR บนตัวเครื่องได้ [3][43][36][51]

## สิ่งที่เกิดขึ้น
สัญญาณส่วนใหญ่รวมตัวอยู่รอบ WWDC week ของ Apple หลายโพสต์รายงานว่า Mike Rockwell ผู้บริหาร Vision Pro ขึ้นดูแล Siri โดยเชื่อมโยงกับการปรับโครงสร้าง Apple AI ในวงกว้าง [5][14][22][7] visionOS 27 คาดว่าจะนำ Siri ใหม่และการปรับปรุง systemwide AI มาด้วย [13] และชุมชนนักพัฒนาเคลื่อนไหวรอบ keynote — นักพัฒนาเดี่ยวรายหนึ่งสร้างแอป Vision Pro (Metaballs) จนติด finalist ของ Apple Design Award, AirPano ปล่อยแอป visionOS native, และเครื่องมือ volume-slicing ส่งขึ้น TestFlight [16][26][28] เธรดย่อยถกเถียงว่า Gurman รายงานเรื่อง Apple 'หยุดผลิต' Vision Pro จริงหรือไม่ โดยฝ่ายสนับสนุนอ้างการส่งมอบ M5 Vision Pro ในภายหลังเป็นหลักฐานว่า platform ยังอยู่รอด [2][15] มีสัญญาณตรงข้ามเช่นกัน: เจ้าของรายหนึ่งโพสต์ว่า 'saying goodbye to Vision Pro' [39]

## ทำไมจึงสำคัญ (การวิเคราะห์)
Platform สองสายกำลังแยกทิศทางกัน Apple กำลังรวมบุคลากร Vision Pro และ visionOS เข้ากับความพยายามด้าน AI [5][13][22] นัยคือ spatial computing ในระยะสั้นของ Apple ถูกวางตำแหน่งให้เป็น surface สำหรับ AI/assistant มากกว่าการผลักดัน consumer แบบเอกเทศ — สำคัญสำหรับสตูดิโอที่เดิมพันกับอุปสงค์แอป visionOS ขณะที่ Google เดิน Android XR จากการสาธิตงานวิจัยสู่การผลิต glasses จริง (Project Aura) โดยพึ่ง Gemini และย้ายการประมวลผลออกไปใน pack [53][33] ซึ่งรวมกับรูปแบบ hardware โล่งรอบตาพร้อม external puck [37][57] บ่งชี้ว่าอุปกรณ์ยุคถัดไปเอนเอียงไปทาง glasses น้ำหนักเบาสำหรับสวมทั้งวัน แทนที่ headset ขนาดใหญ่ ผลกระทบรองด้าน content: เป้าหมายดีไซน์ (FOV, ความสบาย, input, on-device vs. pack compute) ยังไม่ตกผลึก การผูกพันกับ form factor ของอุปกรณ์ใดอุปกรณ์หนึ่งตอนนี้จึงมีความเสี่ยงต้องทำใหม่สูง ปัญหาคุณภาพ store บน Quest [36] และสตูดิโอ VR ที่ย้าย title ไป flat screen [18] คือสัญญาณเตือนด้านอุปสงค์ที่ชัดเจน ไม่ใช่แค่ noise

## ความเป็นไปได้
น่าจะเกิด: visionOS 27 ส่ง Siri ใหม่และ systemwide AI จากรายงานหลายแหล่งที่ตรงกันก่อน WWDC [13][5] เป็นไปได้: Google Project Aura (หรือ Android XR glasses ที่เทียบเคียง) เปิดตัวปลายปี 2026 พร้อม Gemini integration [53] และดีไซน์โล่งรอบตา/external puck แพร่ขยายไปยังผู้ผลิตหลายรายภายใน ~12 เดือน [37][57] ไม่น่าจะเกิดในระยะสั้น: Vision Pro ถึง mass-market scale — แม้แต่ฝ่ายที่ปกป้อง platform ก็กรอบการอยู่รอดไว้แค่การ refresh M5 เฉพาะกลุ่มและความตื่นตัวของนักพัฒนา ขณะที่เจ้าของบางส่วนเลิกใช้และสตูดิโอย้ายไป flat screen [15][39][18] ไม่มีแหล่งข้อมูลใดระบุตัวเลขความน่าจะเป็น จึงไม่มีการยืนยันที่นี่

## การนำไปใช้กับองค์กร — NDF DEV
1) ดู WWDC keynote/sessions เพื่อหา visionOS 27 และ Siri/AI spatial APIs ใหม่ก่อนกำหนดขอบเขตงาน Apple XR — effort ต่ำ [13][16] 2) เพิ่ม Android XR / Project Aura เข้า platform-evaluation backlog จาก shipping intent ของ Google และการผสาน Gemini; prototype ขนาดเล็กเพื่อทดสอบ glasses form factor และ spatial-intelligence APIs มีเหตุผลเพียงพอ, effort กลาง [53][33] 3) สำหรับ Unity VR content ทุกชิ้น ออกแบบรองรับแนวโน้ม headset น้ำหนักเบา/โล่งรอบตาและ external compute แทนที่จะสมมติ GPU budget ของ heavy-headset — effort ต่ำ/กลาง [37][57] 4) หากจะ publish บน Quest ให้ตั้งงบสำหรับปัญหา discoverability และ store-listing hygiene; ถือว่า store reach คือความเสี่ยง ไม่ใช่สิ่งที่ได้มาฟรี — effort ต่ำ [36] 5) ใช้ตัวอย่าง Perfect Dark VR / Quest 3 6DoF เป็น UX reference สำหรับดีไซน์ VR shooter/locomotion ที่สบาย — effort ต่ำ [3][43] ข้ามไป: คุยเรื่องโทรศัพท์ iPhone XR, XRP crypto, adult-VR, รายการ ADHD-meds และ poker 'XR' — ล้วนเป็น keyword collision ไม่เกี่ยวข้อง บันทึกไว้รับรู้เท่านั้น: Godot on-device XR export มีอยู่แต่ออกนอกเส้นทางสำหรับ Unity shop [51]; รับทราบไว้ ไม่ต้องดำเนินการ

## สัญญาณที่ต้องติดตาม
- visionOS 27 + Siri/AI API surface ที่เปิดเผยใน WWDC — ยืนยันว่า spatial dev ได้ capability ใหม่หรือไม่ [13][5]
- วันเปิดตัว Project Aura / Android XR glasses และการเข้าถึง Gemini SDK ปลายปี 2026 [53][33]
- ดีไซน์ headset โล่งรอบตา, external puck (Pico Project Swan, Galaxy XR) ในฐานะ form factor ที่กำลังผงาด [37][57]
- คุณภาพ/discoverability ของ Quest store และสตูดิโอ VR ที่ pivot ไป flat screen ในฐานะตัวชี้ความเสี่ยงด้านอุปสงค์ [36][18]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Timcast | ^1281 c177 | [You are driving home from work. Your wife and 2 children home waiting for your a](https://x.com/Timcast/status/2063658389595476448) |
| x | markgurman | ^846 c13 | [@hunter_spatial Send me the link where I reported winding down Vision Pro manufa](https://x.com/markgurman/status/2063668164278587532) |
| x | Graslu00 | ^834 c16 | [Playing Perfect Dark in VR was the best shooter experience I've had with virtual](https://x.com/Graslu00/status/2063870921409003867) |
| x | thalaprabha21 | ^787 c31 | [Full Name: Kayley Gunner Birth Date: January 9, 1997 Current Age: 29 Birthplace:](https://x.com/thalaprabha21/status/2063289702426513601) |
| x | markgurman | ^781 c31 | [The Siri reboot spotlights three key storylines: Tim Cook's final launch as CEO ](https://x.com/markgurman/status/2063637872289398865) |
| x | StockMKTNewz | ^750 c92 | [APPLE $AAPL HAD A SECRET CRISIS MEETING IN EARLY 2025 ABOUT AI The topic: Apple ](https://x.com/StockMKTNewz/status/2063648456506220896) |
| x | StockSavvyShay | ^676 c82 | [$AAPL held a secret crisis meeting in early 2025 after Apple Intelligence underw](https://x.com/StockSavvyShay/status/2063655335957762246) |
| x | faythebest | ^441 c3 | [I'm super excited to watch the #WWDC keynote in my private cinema on Apple Visio](https://x.com/faythebest/status/2063692275251564609) |
| x | leodey4u | ^414 c132 | [Maturing is realizing that iPhone XR still does the same thing as iPhone 17.](https://x.com/leodey4u/status/2063491662458806335) |
| x | FindingKan | ^379 c14 | [The day I realized that this boy na he-goat na the day babes wey dey iPhone XR c](https://x.com/FindingKan/status/2063523737073315924) |
| x | v_momo030 | ^325 c1 | [Ratiorine Life (4/6) IPC Entertainment's new Virtual Reality game invite Aventur](https://x.com/v_momo030/status/2063963493896949833) |
| x | Bidalizback | ^286 c3 | [@MkoTheComedian "He got himself an IPhone 17, while I'm still using XR" You go f](https://x.com/Bidalizback/status/2063385322843451578) |
| x | spatialreport | ^269 c9 | [Happy #WWDC week to those who celebrate! Vision Pro owners can expect the follow](https://x.com/spatialreport/status/2063705271843921932) |
| x | LeakerApple | ^226 c3 | [In Rockwell we trust to fix Siri. Bro cooked with the Vision Pro. https://t.co/P](https://x.com/LeakerApple/status/2063640642388131859) |
| x | hunter_spatial | ^182 c7 | [In early 2025, Gurman reported Apple was winding down Vision Pro manufacturing. ](https://x.com/hunter_spatial/status/2063604672686891280) |
| x | dreamwieber | ^177 c8 | [Last WWDC I got inspired and began working on Metaballs for Apple Vision Pro. Ex](https://x.com/dreamwieber/status/2063443752526700624) |
| x | Saksham_9996 | ^147 c1 | [iPhone xr vs iPhone 17 bezels! We've come a long way😮‍💨 https://t.co/bmVBEFoxwM](https://x.com/Saksham_9996/status/2063838563503116476) |
| x | GAMERTAGVR | ^146 c32 | [When Moss announced it was going to flat screens it made sense. The 7th Guest ab](https://x.com/GAMERTAGVR/status/2063384829454922123) |
| x | quotesdaily100 | ^141 c2 | [Jobs That Will Explode in the Next 10 Years: 1. AI prompt engineers 2. Cybersecu](https://x.com/quotesdaily100/status/2063575281185767767) |
| x | vivoplt | ^126 c52 | [Top 15 In Demand Tech Skills for 2026 • Artificial Intelligence • Machine Learni](https://x.com/vivoplt/status/2063585769776939388) |
| x | UrglyGramm | ^126 c33 | [Nobody go pity you, you dey suffer guy. One phone for 5yrs, no wonder why your l](https://x.com/UrglyGramm/status/2063912033955815767) |
| x | ShishirShelke1 | ^119 c9 | [Apple is finally putting someone in charge of Siri who seems to take AI seriousl](https://x.com/ShishirShelke1/status/2063648149324136754) |
| x | claritzhalatina | ^100 c5 | [I rarely have a plan. Just an idea, some VeVe collectibles in augmented reality,](https://x.com/claritzhalatina/status/2063474456723337401) |
| x | badbunnyxn | ^91 c1 | [Stop jerking to pics. Create the guy &amp; fuck him live on video call or in ful](https://x.com/badbunnyxn/status/2063850173386940850) |
| x | dabz_global | ^86 c5 | [Absolute best seller! OG! premium used // foreign used // grade A++++ // untampe](https://x.com/dabz_global/status/2063314618303283382) |
| x | mundoxrbrasil | ^80 c2 | [AirPano just launched an app for Apple Vision Pro. I've always enjoyed their vid](https://x.com/mundoxrbrasil/status/2063286647123223041) |
| x | claritzhalatina | ^75 c1 | [💚🐍 Sedusa is back in Townsville. Mojo Jojo already has a plan. Blossom and Butte](https://x.com/claritzhalatina/status/2063398932416184522) |
| x | ElasticSea | ^73 c3 | [New features in my volume slicing tool for Apple Vision Pro are now on TestFligh](https://x.com/ElasticSea/status/2063300549055848812) |
| x | TheOriginaliTE | ^68 c1 | [So cool! They should make this available for the Vision Pro! 😎 https://t.co/t3L0](https://x.com/TheOriginaliTE/status/2063409517250121776) |
| x | OliviaSparkleXX | ^67 c3 | [🔞📷Do you enjoy teasing and forplay? Me and @Nata_Gold_ YES, we love it 😍😍 . My c](https://x.com/OliviaSparkleXX/status/2063365321390735623) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Timcast</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1281 · 💬 177</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Timcast/status/2063658389595476448">View @Timcast on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“You are driving home from work. Your wife and 2 children home waiting for your arrival Crossing an intersection a truck driven by a drunk man t-bones you killing you instantly You awaken in an unfamil”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@Timcast โพสต์เรื่องสั้น speculative fiction เกี่ยวกับหุ่น XR companion ที่ถูก calibrate ด้วยการจำลองชีวิตมนุษย์ทั้งชีวิต ไม่ใช่ข่าวหรือ release จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Timcast/status/2063658389595476448" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@markgurman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 846 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/markgurman/status/2063668164278587532">View @markgurman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@hunter_spatial Send me the link where I reported winding down Vision Pro manufacturing I’ll wait”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Mark Gurman ท้าให้ @hunter_spatial หาลิงก์รายงานที่อ้างว่าเขาเขียนเรื่อง Apple หยุดผลิต Vision Pro</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/markgurman/status/2063668164278587532" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Graslu00</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 834 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Graslu00/status/2063870921409003867">View @Graslu00 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Playing Perfect Dark in VR was the best shooter experience I've had with virtual reality and it's just an alpha version. It's insane how well these games go with VR! https://t.co/QoRisKuspw”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้รายงานว่า Perfect Dark เวอร์ชัน alpha ที่รันใน VR ให้ประสบการณ์ shooter ที่ดีมาก บ่งชี้ว่า FPS คลาสสิกแปลงสู่ VR ได้ดีโดยไม่ต้องดัดแปลงมาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า mechanic ของ FPS ยุคเก่าเข้ากับ VR ได้ดีโดยธรรมชาติ — เป็น signal สำหรับทีม XR ที่กำลังประเมินว่า genre ไหน port ได้โดยไม่ยาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ใช้ control scheme ของ FPS เก่า (fixed reticle, locomotion เรียบง่าย) เป็น baseline สำหรับ prototype VR shooter ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Graslu00/status/2063870921409003867" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@thalaprabha21</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 787 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/thalaprabha21/status/2063289702426513601">View @thalaprabha21 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Full Name: Kayley Gunner Birth Date: January 9, 1997 Current Age: 29 Birthplace: Oahu, Hawaii, U.S. Nationality: American Profession: Adult Film Actress, Webcam Model, and Digital Creator Career Start”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์นี้เป็น profile นักแสดง adult entertainment ไม่มีเนื้อหา XR/VR หรือ tech ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/thalaprabha21/status/2063289702426513601" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@markgurman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 781 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/markgurman/status/2063637872289398865">View @markgurman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Siri reboot spotlights three key storylines: Tim Cook’s final launch as CEO helping move Apple in the right direction; Craig Federighi becoming Apple’s AI leader; and Vision Pro creator Mike Rockw”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Mark Gurman จาก Bloomberg มองว่า Siri reboot ครั้งนี้สะท้อนการเปลี่ยนแปลงผู้นำ 3 ชั้น: ก้าวสุดท้ายของ Tim Cook, Craig Federighi คุม AI และ Mike Rockwell (Vision Pro) มาแก้จุดอ่อน AI ของ Apple</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/markgurman/status/2063637872289398865" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@StockMKTNewz</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 750 · 💬 92</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/StockMKTNewz/status/2063648456506220896">View @StockMKTNewz on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“APPLE $AAPL HAD A SECRET CRISIS MEETING IN EARLY 2025 ABOUT AI The topic: Apple Intelligence was a flop. The new Siri was about to be delayed. And rivals like OpenAI, Google, and Meta were lapping the”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Apple rebuild Siri โดยใช้ Gemini/Google Cloud เป็น backend และเตรียมเปิดตัว standalone AI app ที่ WWDC 2026 หลัง Mike Rockwell (ผู้สร้าง Vision Pro) ถูกดึงมาดูแล AI แทนหัวหน้าเดิม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Rockwell ย้ายจาก Vision Pro มาคุม Siri บ่งชี้ว่า Apple จะ integrate AI เข้า spatial computing มากขึ้น — ตรงกับงาน VisionOS ของทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม WWDC 2026 สำหรับ Siri และ VisionOS AI API ใหม่ — ถ้าทีมทำ Apple platform อยู่ ประกาศนี้กำหนด integration path ที่ official</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/StockMKTNewz/status/2063648456506220896" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@StockSavvyShay</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 676 · 💬 82</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/StockSavvyShay/status/2063655335957762246">View @StockSavvyShay on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“$AAPL held a secret crisis meeting in early 2025 after Apple Intelligence underwhelmed and the new Siri faced delays. What came out of it: • AI chief John Giannandrea was stripped of key responsibilit”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Account สาย stock รายงานว่า Apple จัดประชุมวิกฤตภายในต้นปี 2025 ย้าย Mike Rockwell (หัวหน้า Vision Pro) มาดูแล Siri และทำดีล Google ให้ Gemini ขับเคลื่อน Siri บางส่วน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/StockSavvyShay/status/2063655335957762246" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@faythebest</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 441 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/faythebest/status/2063692275251564609">View @faythebest on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I’m super excited to watch the #WWDC keynote in my private cinema on Apple Vision Pro but also super sad that it’s going to be @tim_cook last keynote. #AppleVisionPro https://t.co/nrIgNcd4D6”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้แชร์ความตื่นเต้นส่วนตัวที่ดู WWDC keynote ผ่าน Apple Vision Pro แบบ private cinema และพูดถึงว่านี่จะเป็น keynote สุดท้ายของ Tim Cook</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/faythebest/status/2063692275251564609" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
