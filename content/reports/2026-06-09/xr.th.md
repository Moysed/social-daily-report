---
type: social-topic-report
date: '2026-06-09'
topic: xr
lang: th
pair: xr.en.md
generated_at: '2026-06-09T03:16:44+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 141
salience: 0.65
sentiment: mixed
confidence: 0.58
tags:
- apple-vision-pro
- visionos
- wwdc2026
- spatial-computing
- siri-ai
- xr-hardware
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2064107140583993344/img/uv6sPziYsMQ4EY5G.jpg
translated_by: claude-sonnet-4-6
---

# XR / VR / AR — 2026-06-09

## TL;DR
- Apple ประกาศ Siri รูปแบบใหม่ในชื่อ "Siri AI" แบบ conversational ในงาน WWDC 2026 รองรับ iPhone/iPad/Mac/Vision Pro — มี world knowledge, on-device context, screen awareness, แอปแยกต่างหาก, คาด beta ปลายปี [1][51]
- visionOS 27 เพิ่ม Siri orb ที่เรียกด้วยการกลอกตา และ Visual Intelligence ที่อ่านสภาพแวดล้อมรอบตัว รวมถึงใช้งานภายใน immersive/VR content [20][23][38][39]
- Apple เปิดเส้นทาง spatial accessories: บริษัทภายนอกสร้าง 6DoF-tracked accessories โดยใช้ IR LEDs + IMU สำหรับ low-latency tracking [21]
- visionOS 27 รองรับการ render panoramas แบบ spatial และให้ผู้ใช้นำ panoramas ของตัวเองมาใช้เป็น spatial scenes พร้อม environments ใหม่ เช่น Iceland [10][4][55]
- M5 Vision Pro วางจำหน่ายแล้ว แม้มีรายงานช่วงต้นปี 2025 ว่า Apple กำลังหยุดผลิต — Gurman ยืนยันว่าไม่เคยรายงานเรื่องหยุดผลิต [5][24][30][36]

## What happened
WWDC 2026 หมุนรอบการ reboot Siri ของ Apple — นับเป็น keynote สุดท้ายของ Tim Cook ก่อน John Ternus จะรับตำแหน่ง CEO โดย Mike Rockwell (หัวหน้า Vision Pro) ย้ายมาดูแล Siri และ Craig Federighi ขึ้นเป็น AI leader [7][25][22][35] "Siri AI" ใหม่เป็น conversational assistant ที่มี world knowledge อัปเดต, on-device context, screen awareness และแอปแยกต่างหากข้ามแพลตฟอร์ม คาด beta เร็วๆ นี้ [1][51] สำหรับ Vision Pro โดยตรง visionOS 27 เพิ่ม Siri orb ลอยตัวที่เรียกด้วยการมอง, Visual Intelligence ระบุสิ่งที่เห็นและทำงานภายใน immersive/VR content, render panoramas แบบ spatial พร้อมรองรับ panoramas ที่ผู้ใช้นำเข้าเป็น scenes และ environments ใหม่ [19][20][23][38][39][10][4][55]

## Why it matters (reasoning)
ข่าวที่สำคัญสำหรับงาน studio ไม่ใช่ Siri orb สำหรับผู้บริโภค แต่คือการเคลื่อนไหว 3 จุดของแพลตฟอร์ม ความสามารถ spatial accessories [21] หมายความว่าฮาร์ดแวร์ input แบบ custom (controllers, training peripherals) สามารถ target Vision Pro ด้วย 6DoF tracking ที่ vendor สร้างเอง — ตรงกับงาน XR training/edu builds โดยตรง การนำเข้า panoramas ของผู้ใช้เป็น spatial scenes [10] ลด content cost สำหรับ immersive backdrops และ Visual Intelligence ที่ทำงานใน immersive content [23] บ่งชี้ว่าแพลตฟอร์มเริ่มฝัง AI context ที่นักพัฒนาอาจเข้าถึงได้ในอนาคต Second-order: การ refresh M5 และฮาร์ดแวร์ที่วางจำหน่ายจริง [24][30][36] หักล้างการมองว่า 'Vision Pro ตายแล้ว' — การเดิมพันว่า visionOS ไม่ใช่ dev target ที่คุ้มค่าจึงยังเร็วเกินไป ข้อจำกัดที่ต้องยอมรับ: TechCrunch มองการอัปเดต Vision Pro ว่าเป็นแค่ 'ฟองลอยคุยได้' [42], install base ยังน้อย และ AI features ส่วนใหญ่ target ผู้บริโภคทั่วไป ไม่ใช่นักพัฒนา [46]

## Possibility
**Likely:** Vision Pro ยังเป็น spatial dev platform หลักของ Apple ในระยะใกล้ จากการ refresh M5 และการลงทุน visionOS ต่อเนื่อง [24][30][36] **Plausible:** เส้นทาง spatial accessories เปิดให้บริษัทภายนอกสร้าง controllers/edu peripherals ได้ หาก SDK และ tracking spec เป็นไปตามที่ประกาศ [21] **Plausible:** Visual Intelligence เป็นรากฐานสำหรับ Apple glasses ในอนาคต ตามที่ผู้แสดงความเห็นหลายรายคาดการณ์ [39] **Plausible ภายใน ~12 เดือน:** headsets แบบเบา ไม่มีพัดลม, รองรับ peripherals ทั่วไป โดยมี compute/battery อยู่ใน external puck (แบบ Magic Leap) ตามที่นักวิเคราะห์คนหนึ่งคาด [45] **Unlikely:** Siri orb ขยาย Vision Pro install base ได้จริงในระยะสั้น เมื่อดูจากการตอบรับที่ยังสงสัย [42] ไม่มีแหล่งข้อมูลใดให้ตัวเลขความน่าจะเป็น

## Org applicability — NDF DEV
1) ประเมิน spatial accessories capability สำหรับ training/edu peripherals แบบ custom เมื่อ SDK details เผยแพร่ — effort med [21] 2) ใช้ imported-panorama spatial scenes เป็น immersive backdrops ราคาประหยัดใน edutech/e-learning demos — effort low [10] 3) ทำ prototype กับ Visual Intelligence / in-immersive AI context เพื่อดูว่ามี usable APIs สำหรับ guided learning apps — effort med [23] 4) ทดลอง volumetric video / 4D Gaussian Splatting (4DGS) เป็น AR content pipeline — effort med [56] ข้าม: consumer Siri orb features [20][42], เรื่อง iPhone XR [15][26] และ crypto/stock ทั้งหมด [13][54][60] — ไม่เกี่ยวกับ XR

## Signals to Watch
- visionOS 27 beta / developer access timing — กำหนด timeline ของการทำ prototype [19][51]
- spec เต็มของ spatial accessories program (tracking latency, cost) [21]
- แนวโน้ม headsets แบบ external-puck, ไม่มีพัดลม, open-periphery ใน 12 เดือนข้างหน้า [45]
- การขับเคลื่อน military XR ของ Palmer Luckey (night/thermal vision) ในฐานะ demand vector แยกของ AR [41]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | tim_cook | ^13782 c732 | [The next generation of Apple Intelligence powers an entirely new Siri: making th](https://x.com/tim_cook/status/2064107489847816292) |
| x | Graslu00 | ^1485 c35 | [Playing Perfect Dark in VR was the best shooter experience I've had with virtual](https://x.com/Graslu00/status/2063870921409003867) |
| x | Timcast | ^1316 c186 | [You are driving home from work. Your wife and 2 children home waiting for your a](https://x.com/Timcast/status/2063658389595476448) |
| x | SpatiallyMe | ^929 c16 | [Apple still sets the bar for software design. The way movies on Vision Pro refle](https://x.com/SpatiallyMe/status/2064117241587601516) |
| x | markgurman | ^890 c13 | [@hunter_spatial Send me the link where I reported winding down Vision Pro manufa](https://x.com/markgurman/status/2063668164278587532) |
| x | VRChat | ^859 c128 | [How was your Furality Ultra this year? Show us a picture! 📸 https://t.co/OdQx3Mh](https://x.com/VRChat/status/2064043232627965981) |
| x | markgurman | ^790 c31 | [The Siri reboot spotlights three key storylines: Tim Cook's final launch as CEO ](https://x.com/markgurman/status/2063637872289398865) |
| x | StockMKTNewz | ^753 c93 | [APPLE $AAPL HAD A SECRET CRISIS MEETING IN EARLY 2025 ABOUT AI The topic: Apple ](https://x.com/StockMKTNewz/status/2063648456506220896) |
| x | StockSavvyShay | ^691 c83 | [$AAPL held a secret crisis meeting in early 2025 after Apple Intelligence underw](https://x.com/StockSavvyShay/status/2063655335957762246) |
| x | DurvidImel | ^690 c4 | [HOLY SHIT. Apple just added spatial rendering of Panoramas AND you can now use y](https://x.com/DurvidImel/status/2064034114232357126) |
| x | Mrwhosetheboss | ^628 c10 | [Visual Intelligence is coming to Vision Pro - it's like circle to search for you](https://x.com/Mrwhosetheboss/status/2064044038789976234) |
| x | v_momo030 | ^606 c1 | [Ratiorine Life (4/6) IPC Entertainment's new Virtual Reality game invite Aventur](https://x.com/v_momo030/status/2063963493896949833) |
| x | amitisinvesting | ^581 c56 | [A TON OF THINGS HAPPENED IN THE STOCK MARKET TODAY. Here's a full recap: $NVDA C](https://x.com/amitisinvesting/status/2064163504903332034) |
| x | faythebest | ^477 c3 | [I'm super excited to watch the #WWDC keynote in my private cinema on Apple Visio](https://x.com/faythebest/status/2063692275251564609) |
| x | leodey4u | ^414 c132 | [Maturing is realizing that iPhone XR still does the same thing as iPhone 17.](https://x.com/leodey4u/status/2063491662458806335) |
| x | FindingKan | ^380 c14 | [The day I realized that this boy na he-goat na the day babes wey dey iPhone XR c](https://x.com/FindingKan/status/2063523737073315924) |
| x | feebeechanchibi | ^359 c21 | [Ohachi~! 🐝🌸 I hope everyone has a happy and peaceful start to the week!!! How we](https://x.com/feebeechanchibi/status/2064040757644886389) |
| x | nidosphere | ^336 c9 | [buying a vision pro so i can grab the siri ball and then put it on my dick and b](https://x.com/nidosphere/status/2064042632599244907) |
| x | spatialreport | ^313 c11 | [Happy #WWDC week to those who celebrate! Vision Pro owners can expect the follow](https://x.com/spatialreport/status/2063705271843921932) |
| x | DurvidImel | ^308 c3 | [The dedicated Siri app syncs across platforms. Most interestingly, in Vision Pro](https://x.com/DurvidImel/status/2064041505212477941) |
| x | SadlyItsBradley | ^275 c14 | [Holy Shit!: Companies can also now build their own spatial accessories that work](https://x.com/SadlyItsBradley/status/2064057177485050180) |
| x | LeakerApple | ^227 c3 | [In Rockwell we trust to fix Siri. Bro cooked with the Vision Pro. https://t.co/P](https://x.com/LeakerApple/status/2063640642388131859) |
| x | SadlyItsBradley | ^196 c6 | [Siri AI's visual intelligence on Vision Pro also works inside of Immersive/VR co](https://x.com/SadlyItsBradley/status/2064131872485999038) |
| x | hunter_spatial | ^193 c8 | [In early 2025, Gurman reported Apple was winding down Vision Pro manufacturing. ](https://x.com/hunter_spatial/status/2063604672686891280) |
| x | kimmonismus | ^179 c25 | [WWDC 2026: A brief assessment At WWDC26, Tim Cook's last keynote before he hands](https://x.com/kimmonismus/status/2064059964709388774) |
| x | Saksham_9996 | ^168 c1 | [iPhone xr vs iPhone 17 bezels! We've come a long way😮‍💨 https://t.co/bmVBEFoxwM](https://x.com/Saksham_9996/status/2063838563503116476) |
| x | UrglyGramm | ^147 c35 | [Nobody go pity you, you dey suffer guy. One phone for 5yrs, no wonder why your l](https://x.com/UrglyGramm/status/2063912033955815767) |
| x | quotesdaily100 | ^143 c2 | [Jobs That Will Explode in the Next 10 Years: 1. AI prompt engineers 2. Cybersecu](https://x.com/quotesdaily100/status/2063575281185767767) |
| x | badbunnyxn | ^135 c2 | [Stop jerking to pics. Create the guy &amp; fuck him live on video call or in ful](https://x.com/badbunnyxn/status/2063850173386940850) |
| x | NathieVR | ^134 c14 | [So Apple Vision Pro isn't quite as dead as everyone said. Shocking, I know.](https://x.com/NathieVR/status/2064081844669403285) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@tim_cook</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 13782 · 💬 732</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/tim_cook/status/2064107489847816292">View @tim_cook on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The next generation of Apple Intelligence powers an entirely new Siri: making the apps and experiences you rely on across iPhone, iPad, Mac, and Apple Vision Pro more personal and helpful than ever. h”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Tim Cook ประกาศ Apple Intelligence รุ่นใหม่ขับเคลื่อน Siri ที่ redesign ใหม่ พร้อม app integration ลึกขึ้น ครอบคลุม iPhone, iPad, Mac, และ Apple Vision Pro</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Vision Pro จะมี Siri ที่ฉลาดขึ้นผ่าน Apple Intelligence — voice/AI interaction กลายเป็น UX หลักบน visionOS</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม WWDC developer session เรื่อง visionOS Siri API ก่อนทีม XR build หรืออัปเดต voice interaction ใน project ที่มีอยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/tim_cook/status/2064107489847816292" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Graslu00</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1485 · 💬 35</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Graslu00/status/2063870921409003867">View @Graslu00 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Playing Perfect Dark in VR was the best shooter experience I've had with virtual reality and it's just an alpha version. It's insane how well these games go with VR! https://t.co/QoRisKuspw”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ทดสอบ alpha mod ของ Perfect Dark บน VR รายงานว่าเป็นประสบการณ์ VR shooter ที่ดีที่สุดที่เคยเจอ บ่งชี้ว่า FPS คลาสสิกเข้ากับ VR ได้ดีโดยธรรมชาติ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Feedback จริงจากผู้เล่นยืนยันว่า FPS mechanics แบบคลาสสิกทำงานได้ดีใน VR — ข้อมูลที่ใช้ได้เวลา scope VR action prototype</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอน studio สร้าง VR shooter ให้ใช้ FPS input และ weapon-handling แบบคลาสสิกเป็น baseline แทนการออกแบบใหม่ทั้งหมด</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Graslu00/status/2063870921409003867" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Timcast</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1316 · 💬 186</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Timcast/status/2063658389595476448">View @Timcast on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“You are driving home from work. Your wife and 2 children home waiting for your arrival Crossing an intersection a truck driven by a drunk man t-bones you killing you instantly You awaken in an unfamil”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Timcast โพสต์ fiction สั้นที่ viral เกี่ยวกับหุ่นยนต์ในอนาคตที่ calibrate ความรู้สึกด้วยการจำลองชีวิตมนุษย์เต็มรูปแบบ ก่อน 'ตื่น' ขึ้นมาในฐานะ XR AI home companion</dd>
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
    <span class="ndf-author">@SpatiallyMe</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 929 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SpatiallyMe/status/2064117241587601516">View @SpatiallyMe on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple still sets the bar for software design. The way movies on Vision Pro reflect in the icy river of the new Iceland environment during the day, and how the snow softly glows at night, genuinely giv”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้แชร์ประสบการณ์ว่า environment ใหม่ Iceland บน Apple Vision Pro แสดง dynamic light reflection บนน้ำและหิมะเรืองแสงกลางคืนได้สมจริง สะท้อน rendering quality ระดับ OS</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Apple ยก baseline ด้าน visual fidelity ของ spatial environment ให้สูงขึ้น — studio ที่สร้าง content บน visionOS ต้องทำได้ในระดับนี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ใช้ Iceland environment ของ Apple เป็น reference benchmark สำหรับ visionOS environment projects ที่จะทำต่อไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SpatiallyMe/status/2064117241587601516" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@markgurman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 890 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/markgurman/status/2063668164278587532">View @markgurman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@hunter_spatial Send me the link where I reported winding down Vision Pro manufacturing I’ll wait”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Mark Gurman ท้า @hunter_spatial ให้หาลิงก์ที่อ้างว่า Gurman รายงานเรื่องหยุดผลิต Vision Pro — บอกเป็นนัยว่าข้อมูลนั้นไม่ถูกต้อง</dd>
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
    <span class="ndf-author">@VRChat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 859 · 💬 128</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VRChat/status/2064043232627965981">View @VRChat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“How was your Furality Ultra this year? Show us a picture! 📸 https://t.co/OdQx3Mh2ry”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>VRChat ถามให้ user แชร์รูปจากงาน Furality Ultra ซึ่งเป็น virtual convention ธีม furry ขนาดใหญ่ที่จัดใน VRChat</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VRChat/status/2064043232627965981" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@markgurman</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 790 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/markgurman/status/2063637872289398865">View @markgurman on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Siri reboot spotlights three key storylines: Tim Cook’s final launch as CEO helping move Apple in the right direction; Craig Federighi becoming Apple’s AI leader; and Vision Pro creator Mike Rockw”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Mark Gurman จาก Bloomberg สรุป Siri reboot ว่าเป็นเรื่องการเปลี่ยน leadership 3 จุด: launch สุดท้ายของ Tim Cook, Federighi คุม AI, และ Rockwell (คนสร้าง Vision Pro) รับผิดชอบปิด gap ด้าน AI</dd>
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
    <span class="ndf-engagement">♥ 753 · 💬 93</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/StockMKTNewz/status/2063648456506220896">View @StockMKTNewz on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“APPLE $AAPL HAD A SECRET CRISIS MEETING IN EARLY 2025 ABOUT AI The topic: Apple Intelligence was a flop. The new Siri was about to be delayed. And rivals like OpenAI, Google, and Meta were lapping the”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Apple สร้าง Siri ใหม่บน Gemini และ Google Cloud หลังวิกฤต AI ภายใน พร้อมเปิดตัว standalone AI app ที่ WWDC สัปดาห์นี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Siri ที่รันบน Gemini แปลว่า API ด้าน voice และ on-device AI บน iOS/visionOS น่าจะเปลี่ยน — กระทบ project ที่ build บน Apple platform ตรงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู WWDC session สัปดาห์นี้ โฟกัส Siri API และ on-device AI ใหม่ที่อาจใช้ใน iOS/visionOS project ของทีม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/StockMKTNewz/status/2063648456506220896" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
