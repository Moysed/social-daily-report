---
type: social-topic-report
date: '2026-06-12'
topic: xr
lang: th
pair: xr.en.md
generated_at: '2026-06-12T15:20:37+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 143
salience: 0.58
sentiment: mixed
confidence: 0.5
tags:
- xr
- vision-pro
- gaussian-splatting
- quest-pico
- unity-xr
- supply-chain
thumbnail: https://pbs.twimg.com/media/HKeZr2TX0AAXoAx.jpg
translated_by: claude-sonnet-4-6
---

# XR / VR / AR — 2026-06-12

## TL;DR
- กระแส WWDC 2026 ยังครองพื้นที่: visionOS 27 developer beta one ออกแล้ว [58] พร้อมกับที่ Apple เพิ่ม Gaussian splatting (Apple Maps [15], capture/view แบบ on-device ด้วย SHARP splat [50]), RealityKit real-time cubemap reflections [21], Spatial Preview บน macOS [13], และ Siri ตัวใหม่บน Vision Pro [24]
- ข่าว Vision Pro ถูกยกเลิกถูกถอนคืนแล้ว: แหล่งข่าวของ Gurman ที่บอกว่า 'scrapping the product' หมายถึงกระเป๋าใส่เครื่องจริงๆ [26] — แต่ Apple ยังไม่ยืนยันเป็นทางการว่า form-factor นี้คือ priority [27][8]
- Qualcomm ทีส Snapdragon XR chipset รุ่นใหม่ คาดว่าจะใช้ใน Pico flagship ตัวต่อไป [32]; ดีไซน์ของ Pico flagship ก็หลุดออกมาแล้ว [45]
- Unity ส่ง hands-first XR capabilities รวมถึง 'XR Hand Capture' [55]; มีเกม Quest ที่สร้างและขึ้น Meta Horizon Store ได้ใน 4 สัปดาห์ [35]
- Security: มี supply-chain attack ที่กำลังโจมตี Linux VR package ที่ถูกทิ้งร้างชื่อ 'alvr 20.14.1-4' [9]

## What happened
ปริมาณ 'XR/VR/AR' ส่วนใหญ่วันนี้เป็น noise จากชื่อที่ตรงกัน — ตลาดมือสอง iPhone XR [3][7][12][33][34][44][46][54], Adderall XR [2][43], และ spam ลามกที่ใช้คำว่า 'virtual reality studio' [16][40][42][51][53] — ไม่มีสัญญาณ XR จริงๆ เลย กลุ่มสัญญาณจริงรวมศูนย์อยู่ที่ Apple Vision Pro หลัง WWDC 2026: visionOS 27 dev beta one [58], Gaussian splatting รองรับใน Apple Maps [15] และ on-device capture [50] (มีข้อบกพร่องที่ splat จะ fade เมื่อเข้าใกล้ ทำให้ภายในอาคารดูแย่ [47]), RealityKit reflections [21] และ bridge ระหว่าง UE5↔RealityKit สำหรับ eye tracking/gestures [31], Spatial Preview บน macOS [13], Siri ที่อัปเดตแล้ว [24], และ Personas ที่ดีขึ้น [20] นอกจากนี้ momentum ฝั่ง hardware อยู่ที่ Snapdragon XR chip รุ่นใหม่ของ Qualcomm ที่ผูกกับ Pico flagship ที่หลุดภาพออกมา [32][45] และ standalone headset แบบ interchangeable-compute ที่ถูกทีส [39]

## Why it matters (reasoning)
Apple ลงทุนกับ spatial-content pipeline (splat capture/view, RealityKit rendering) ขณะที่ยังนิ่งเงียบเรื่อง hardware commitment — แหล่งข่าว [37] ได้ยินคำว่า 'Apple Vision Pro' ซ้ำๆ พร้อม visionOS updates 'ขนาดใหญ่' [37] แต่ Gurman ชี้ว่าไม่มีการประกาศว่า form-factor นี้คือ priority [27] ข้อสรุปคือ software ecosystem กำลัง mature เร็วกว่า mass-market hardware ดังนั้น near-term value สำหรับ studio อยู่ที่ content tooling ไม่ใช่การเดิมพันกับยอดขายเครื่อง Gaussian splatting กำลังกลายเป็น capture format จริงสำหรับ immersive scenes [15][50] แต่ข้อจำกัด culling ระยะใกล้ [47] กระทบโดยตรงกับ use case ภายในอาคาร/walkthrough ที่เกี่ยวข้องมากที่สุดกับ edutech และ venue tours ฝั่ง standalone Snapdragon XR part ตัวใหม่ [32] ที่จะใช้ใน Pico/Quest-class devices ชี้ว่า price-performance ของ headset ที่ NDF จะ target จริงๆ กำลังดีขึ้น การโจมตี ALVR [9] เตือนว่า XR dependency ที่เฉพาะกลุ่มและถูกทิ้งร้างเป็นเป้าหมายที่อ่อนแอ

## Possibility
**Likely:** Apple ดัน visionOS software ต่อเนื่อง (beta cadence [58], splat/RealityKit features [15][21][50]) ขณะที่ hardware form-factor ยังไม่มีการ commit สาธารณะ [27] **Plausible:** Pico flagship ตัวต่อไปใช้ Snapdragon XR chip ที่ทีส [32][45] ยก standalone performance baseline ที่เป็นประโยชน์กับ Quest/Pico developers **Plausible:** Gaussian splatting ตั้งตัวเป็น standard immersive-capture format สำหรับ tour และ training หาก Apple แก้ culling behavior ที่ระบุใน [47] **Unlikely near-term:** Vision Pro ถูกยกเลิก — รายงาน 'scrapping' ที่แชร์กันมากเป็นเรื่องกระเป๋าใส่เครื่อง ไม่ใช่ตัวอุปกรณ์ [26] ไม่มีแหล่งข่าวใดให้ตัวเลขความน่าจะเป็น จึงไม่ระบุไว้

## Org applicability — NDF DEV
1) ประเมิน Unity's new hands-first XR / XR Hand Capture สำหรับ controller-free edutech และ training demos — ตรง lane ของ NDF ที่ใช้ Unity+XR (effort ต่ำ, [55]) 2) ทดลอง Gaussian splatting สำหรับ immersive scene/venue capture แต่ทดสอบ close-range culling limit ก่อนจะ commit กับ interior walkthrough (effort ปานกลาง, [15][47][50]) 3) ใช้ Meta Horizon Store เป็น distribution path ที่เร็ว — cycle idea-to-store 4 สัปดาห์มีหลักฐานแล้ว (effort ต่ำ-ปานกลาง, [35]); คำนวณ platform cut 30% ใน revenue planning [14] 4) เพิ่ม QGO v14's Quest Super Resolution / FidelityFX CAS ใน Quest performance toolkit สำหรับ perf test (effort ต่ำ, [52]) 5) Dependency hygiene: pin และ verify provenance ของ VR/streaming package ทุกตัว (เช่น ALVR-family) เพราะมี active attack อยู่ (effort ต่ำ, [9]) **ข้ามไปก่อน:** build บน Vision Pro hardware เป็น target market (commitment ยังไม่ชัด [27][8][26]); UnRealityKit UE5 bridge [31] (NDF ใช้ Unity เป็นหลัก); และ drama ทั้งหมดเรื่อง Vision Pro discontinuation/opinion [22][30][48] **Watch-only, ยังไม่ต้องทำอะไร:** Qualcomm/Pico hardware roadmap [32][45][39]

## Signals to Watch
- Apple จะออก fix สำหรับ Vision Pro Gaussian splat culling ให้ภายในอาคารใช้งานได้จริงหรือไม่ [47][50]
- Snapdragon XR chip รุ่นใหม่ของ Qualcomm และ Pico flagship ที่จะใช้ chip นี้ — กำหนด standalone perf/price baseline รอบต่อไป [32][45]
- ความ mature ของ Unity's hands-first XR feature และ docs เพราะตรงกับ training/edutech use ของ NDF [55]
- ผลกระทบจาก ALVR supply-chain attack — ขอบเขตและการแพร่กระจายไปยัง VR package อื่น [9]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | The_Forty_Four | ^8776 c583 | [Two different budgets for the FIFA World Cup 2026! Two studios ITV= New York Sky](https://x.com/The_Forty_Four/status/2064788088769896584) |
| x | dannarebb | ^6124 c34 | [6 years ago today, I found a few of these Adderall XR branded pill dispensers wh](https://x.com/dannarebb/status/2065137973553742254) |
| x | Thebigsoll | ^5021 c242 | [I've been barbing at this shop for close to 5 years now. Usually when I come her](https://x.com/Thebigsoll/status/2065134233471852890) |
| x | ValerieAnne1970 | ^3138 c587 | [The World Economic Forum has your future planned... "The rich will be able to tr](https://x.com/ValerieAnne1970/status/2065162152776696290) |
| x | meisttokki | ^2432 c0 | [karina used both her iphone 17 blue and iphone xr white to take photos with wint](https://x.com/meisttokki/status/2065258117995401359) |
| x | Abathor_Game | ^1563 c18 | [An emulator for playing NES games in retro 3D and augmented reality. 3D SEN. htt](https://x.com/Abathor_Game/status/2065051626335789298) |
| x | Bigwavee00 | ^960 c69 | [A guy entered my store one afternoon around last year and asked for the price of](https://x.com/Bigwavee00/status/2065050902151541096) |
| x | justinryanio | ^933 c32 | [I asked Apple if Vision Pro is "on ice." https://t.co/4K9cPTAHmz](https://x.com/justinryanio/status/2064854521524990024) |
| x | vxunderground | ^690 c21 | [Word on the Linux nerd streets is someone is actively attempting a supply chain ](https://x.com/vxunderground/status/2065123579541238223) |
| x | gnf_ogo | ^635 c20 | [my sister change am for me two weeks ago, now she wan change her XR I see "good ](https://x.com/gnf_ogo/status/2065063483712909436) |
| x | SadlyItsBradley | ^580 c9 | [Walt Disney World used Apple Vision Pros to streamline the live audio mixing pro](https://x.com/SadlyItsBradley/status/2065243179247370739) |
| x | a__vanita | ^483 c12 | [Went from iPhone 11 to Xr God will actually punish this thief.](https://x.com/a__vanita/status/2065135987429167476) |
| x | SadlyItsBradley | ^306 c5 | [I totally didn't realize that Preview on MacOS also implements the new Spatial P](https://x.com/SadlyItsBradley/status/2064811121677160685) |
| x | conne_psd | ^299 c8 | [@gabefollower Steam 30% PlayStation Store 30% Xbox Game Store 30% Nintendo eShop](https://x.com/conne_psd/status/2065230828452397508) |
| x | NathieVR | ^272 c11 | [You can now experience Apple Maps using Gaussian splats on Apple Vision Pro. Loo](https://x.com/NathieVR/status/2064791922645012560) |
| x | badbunnyxn | ^264 c1 | [Stop jerking to pics. Create the guy &amp; fuck him live on video call or in ful](https://x.com/badbunnyxn/status/2064948785684553833) |
| x | VRChat | ^253 c15 | [It's time for the June 11 Developer Update! Read about how Third-Person mode on ](https://x.com/VRChat/status/2065157380837425499) |
| x | JISOOPOPBASE | ^249 c2 | [@netflix recommends "Boyfriend on Demand" as one of "14 Workplace Rom-Coms "That](https://x.com/JISOOPOPBASE/status/2065139791725838733) |
| x | beebomco | ^210 c6 | [Watching videos on the Vision Pro is SOOOOOOO GOOD NOW! BTW, have you watched ou](https://x.com/beebomco/status/2064744750784327966) |
| x | NathieVR | ^203 c21 | [Still can't believe how much Apple Vision Pro Personas have evolved. Here's a si](https://x.com/NathieVR/status/2065127899569742080) |
| x | ElasticSea | ^166 c1 | [This is how real-time cubemap reflections works on Vision Pro with RealityKit. B](https://x.com/ElasticSea/status/2065072431992066250) |
| x | DominicCarterLA | ^162 c4 | [The Apple Vision Pro is the 1 device that will single handedly bring us back to ](https://x.com/DominicCarterLA/status/2064860886498771205) |
| x | hangzhoufeel | ^156 c0 | ["China has made remarkable achievements, especially in technologies such as virt](https://x.com/hangzhoufeel/status/2065051682569064509) |
| x | nandoprince93 | ^149 c10 | [✨ The new Siri AI on Vision Pro is pure magic. 🤯🥽 Having natural conversations, ](https://x.com/nandoprince93/status/2064767472062930975) |
| x | TinaDebove | ^145 c1 | [Konate using his Vision Pro on the La Compagnie flight to Boston](https://x.com/TinaDebove/status/2065100628687307190) |
| x | jmdagdelen | ^141 c6 | [Turns out that Gurman's source who worked on "Vision Pro" and was telling him th](https://x.com/jmdagdelen/status/2064760954685133247) |
| x | markgurman | ^141 c13 | [@justinryanio Cool interview but he had the opportunity to say the Vision Pro fo](https://x.com/markgurman/status/2064871589217243266) |
| x | sarithaforny | ^130 c6 | [47 subway murders since 2020. The victims deserve better. The mentally ill deser](https://x.com/sarithaforny/status/2065126878537535953) |
| x | VRChat | ^130 c12 | [even though they're just lines, you knew who it was instantly, right? https://t.](https://x.com/VRChat/status/2064754411851616382) |
| x | DominicCarterLA | ^129 c6 | [There isn't a device in the world like the Apple Vision Pro. Like it's actually ](https://x.com/DominicCarterLA/status/2064859470040367613) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@The_Forty_Four</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 8776 · 💬 583</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/The_Forty_Four/status/2064788088769896584">View @The_Forty_Four on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Two different budgets for the FIFA World Cup 2026! Two studios ITV= New York Skyline- whole production team out their for Six Weeks BBC= Virtual Reality studio in Salford Really dissapointing from the”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>BBC เลือกใช้ virtual reality studio ที่ Salford แทนการส่งทีมไปถ่ายทำที่ New York จริง สำหรับ FIFA World Cup 2026 ต่างจาก ITV ที่ส่งทีมออกไป 6 สัปดาห์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>broadcaster ระดับ BBC ใช้ VR studio แทน on-location จริงสำหรับ event ระดับโลก — ยืนยันว่า virtual production ใช้ได้จริงในเชิงต้นทุนระดับ broadcast</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">อ้าง case BBC นี้ตอน pitch virtual production หรือ XR studio solutions ให้ลูกค้า broadcast และ live event</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/The_Forty_Four/status/2064788088769896584" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@dannarebb</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6124 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/dannarebb/status/2065137973553742254">View @dannarebb on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“6 years ago today, I found a few of these Adderall XR branded pill dispensers while doing a private book buy at a psychiatrists library. i asked if I could buy them and he said “you can just have them”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักสะสมเจอกล่องยา Adderall XR branded จากห้องสมุดจิตแพทย์ส่วนตัว และได้รับฟรี — 'XR' ในที่นี้คือ Extended Release ไม่ใช่ Extended Reality</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/dannarebb/status/2065137973553742254" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Thebigsoll</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5021 · 💬 242</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Thebigsoll/status/2065134233471852890">View @Thebigsoll on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I’ve been barbing at this shop for close to 5 years now. Usually when I come here to barb with my iPhone XR 64GB, changed screen, the barber never uses those extra care products. No hot towel, no powd”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ตลกไวรัลเรื่องได้รับบริการร้านตัดผมดีขึ้นหลังเปลี่ยนจาก iPhone XR เป็น iPhone 17 Pro — เป็นเรื่อง status สังคม ไม่ใช่เทคโนโลยี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Thebigsoll/status/2065134233471852890" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ValerieAnne1970</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3138 · 💬 587</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ValerieAnne1970/status/2065162152776696290">View @ValerieAnne1970 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The World Economic Forum has your future planned... &quot;The rich will be able to travel, but the poor will need to use virtual reality headsets to travel to the same place, but from their own couch.&quot; ~An”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ดังบน X อ้างคำพูดของ Andrew Ross Sorkin ว่า WEF วางแผนให้คนจนใช้ VR headset แทนการเดินทางจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ValerieAnne1970/status/2065162152776696290" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@meisttokki</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2432 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/meisttokki/status/2065258117995401359">View @meisttokki on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“karina used both her iphone 17 blue and iphone xr white to take photos with winter 🫪 CAN WE GET THAT JIMINJEONG SELCA https://t.co/vPU669URNq”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟน K-pop เรื่อง Karina ถ่ายรูปกับ Winter ด้วย iPhone XR — 'XR' ในที่นี้คือรุ่นมือถือ Apple ไม่ใช่ Extended Reality</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/meisttokki/status/2065258117995401359" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Abathor_Game</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1563 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Abathor_Game/status/2065051626335789298">View @Abathor_Game on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“An emulator for playing NES games in retro 3D and augmented reality. 3D SEN. https://t.co/WktAcOOGym”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>3D SEN คือ NES emulator ที่ render เกม classic เป็น 3D แนว retro และให้ผู้เล่นวาง game screen ในโลก AR ได้จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>AR product ที่ ship แล้ว ผสม retro aesthetic กับ spatial placement — ชี้ niche entertainment ที่ทำ XR ได้โดยไม่ต้องพึ่ง VR headset</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">XR team ดู 3D SEN เป็น reference สำหรับ entertainment AR — โดยเฉพาะ UX ที่ใช้ retro aesthetic + spatial placement ตอน pitch หรือ prototype</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Abathor_Game/status/2065051626335789298" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Bigwavee00</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 960 · 💬 69</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Bigwavee00/status/2065050902151541096">View @Bigwavee00 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A guy entered my store one afternoon around last year and asked for the price of iPhone Xr but the money with him was way too small When he heard the amount, he smiled and said, “One day, I’ll buy it.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>เจ้าของร้านโทรศัพท์เล่าว่าลูกค้าที่เคยซื้อ iPhone XR ไม่ได้ กลับมาซื้อ iPhone 16 Pro Max ได้หลังผ่านไป 1 ปี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Bigwavee00/status/2065050902151541096" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@justinryanio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 933 · 💬 32</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/justinryanio/status/2064854521524990024">View @justinryanio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I asked Apple if Vision Pro is “on ice.” https://t.co/4K9cPTAHmz”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักข่าว @justinryanio ถาม Apple โดยตรงว่า Vision Pro ถูกพักไว้แล้วหรือเปล่า — บทความที่แนบมาครอบคลุมคำตอบของ Apple ต่อกระแสข่าวลือที่ว่า product นี้อาจถูกระงับ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า Apple ลด priority ของ Vision Pro แสดงว่า visionOS มีความเสี่ยงสูงขึ้นสำหรับ studio ที่กำลังลงทุน dev time ไปกับ XR content</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ควรอ่านบทความเต็มก่อนจัดสรร dev effort ใหม่ให้ visionOS — ความเป็นไปได้ของ platform ส่งผลต่อการตัดสินใจว่าจะสร้างหรือข้ามไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/justinryanio/status/2064854521524990024" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
