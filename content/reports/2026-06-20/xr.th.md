---
type: social-topic-report
date: '2026-06-20'
topic: xr
lang: th
pair: xr.en.md
generated_at: '2026-06-20T15:18:33+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 109
salience: 0.58
sentiment: mixed
confidence: 0.6
tags:
- android-xr
- vision-pro
- awe2026
- godot
- world-models
- ar-glasses
thumbnail: https://pbs.twimg.com/media/HLL6TXcW4AAhioS.jpg
translated_by: claude-sonnet-4-6
---

# XR / VR / AR — 2026-06-20

## TL;DR
- AWE 2026 จบลงโดยมี XREAL Aura บน Android XR (Qualcomm Snapdragon Reality Elite) เป็นหัวข้อหลักที่ถูกพูดถึงมากที่สุด; Founder Priority Pass 2,000 ใบขายหมดใน 36 ชั่วโมง และ partner กำลัง port เนื้อหาเช่น Fallout: Factions และการบันทึก SF Ballet Nutcracker แบบ 8K [18][39][33][48][59]
- Godot 4.7 ออก XR แบบ production-ready รวมถึง Android XR Day One และ SteamOS/Steam Frame [7]
- Snap ประกาศ Specs AR glasses ราคา $2,195; หุ้นร่วง ~10% หลังประกาศ พร้อมเสียงวิจารณ์ที่แตกต่างกันในอุตสาหกรรม [9][26][46]
- tooling/content ของ Apple Vision Pro ยังคงเดินหน้า: port UE5 Lumen GI เข้า visionOS ผ่าน UnRealityKit โชว์ที่ UnrealFest 2026 [16], รายงานข้อได้เปรียบของ visionOS 27 / M5 [36] และ 3D รวมถึง immersive video ออกมาต่อเนื่อง [10][13][20][38]
- spatial intelligence / world models เริ่มเป็น theme ที่ชัดเจน: World Labs' Marble [25] และ Over the Reality ที่อ้างว่ามี 3D Gaussian Splats ครอบคลุมสถานที่จริงกว่า 250,000 แห่งใน 120+ ประเทศ [21]

## สิ่งที่เกิดขึ้น
สัญญาณ XR ที่มีน้ำหนักส่วนใหญ่มาจาก AWE 2026 XREAL โปรโมต Aura glasses บน Android XR ที่วางบน Qualcomm Snapdragon Reality Elite [18][48][53], ขาย Founder Priority Pass 2,000 ใบหมดใน 36 ชั่วโมง [39] และประกาศ content partner ได้แก่ การดัดแปลง Fallout แบบ tabletop [33] และ Nutcracker แบบ stereoscopic 8K ร่วมกับ SF Ballet, Google และ XREAL [59]; Thief VR: Legacy of Shadow คว้า Best Game ที่ Auggie Awards [58] นอกจากนี้ Godot 4.7 ออก XR แบบ production-ready รองรับ Android XR และ Steam Frame [7] และ Snap เปิดตัว Specs AR glasses ราคา $2,195 ซึ่งตรงกับช่วงที่หุ้นร่วง ~10% และแบ่งทิศทางความเห็นในอุตสาหกรรม [9][26][46]

## ความสำคัญ
platform track สองสายกำลังชัดเจนขึ้นสำหรับ XR studio Android XR — ที่มีพื้นฐานจาก Qualcomm silicon, XREAL hardware, content deal ของ Google และ Godot 4.7 Day One support [18][48][7][59] — กำลังรวมตัวเป็น option ที่น่าเชื่อถือตัวที่สามถัดจาก Meta Quest และ Apple Vision Pro ซึ่งช่วยลด single-vendor risk แต่เพิ่ม build target อีกตัว ฝั่ง Apple นั้น งาน bridge ระหว่าง Unreal/Unity กับ rendering (Lumen GI ผ่าน UnRealityKit, PhysX+RealityKit room physics) ลดช่องว่างระหว่าง pipeline engine ที่มีอยู่กับ visionOS [16][54] แต่ความกังวลเรื่อง Beta cadence และกระแส "is it dead" ส่งสัญญาณว่า momentum ฝั่งผู้บริโภคยังไม่แน่นอน [30][20] Specs ของ Snap ที่ $2,195 และ reaction เชิงลบของตลาดแสดงว่า consumer AR glasses ยังติดปัญหาด้านราคาเทียบกับคุณค่า [9] thread เรื่อง world models — Marble บวกกับการ capture Gaussian Splat ขนาดใหญ่ในสถานที่จริง [25][21] — ชี้ทางไปสู่การสร้าง 3D environment ที่ถูกและเร็วขึ้น ซึ่งสำคัญทั้งสำหรับเกมและเนื้อหา location-based/edutech

## โอกาส
มีแนวโน้มสูง: Android XR จะได้รับความสนใจจาก developer มากขึ้นตลอด 2026 จาก hardware, silicon, engine และ content support ที่มาพร้อมกัน [7][18][48][59] มีความเป็นไปได้: Apple ยังคง Vision Pro ไว้เป็น device ระดับ premium สำหรับ 3D/immersive-video และการใช้งานเชิงวิชาชีพมากกว่าตลาด mass consumer จากสัญญาณ content ที่ออกมาต่อเนื่องแต่ beta/uptake ช้า [10][13][30][36] มีความเป็นไปได้: tooling ด้าน Gaussian splat และ world model จะเข้าสู่ content pipeline กระแสหลักสำหรับการ capture environment [21][25] ไม่น่าเกิดในระยะใกล้: Snap Specs ถึงผู้บริโภคในวงกว้างที่ราคา $2,195 เมื่อมองจาก reaction ตลาดที่เป็นลบทันที [9][26] ไม่มี source ใดระบุตัวเลขความน่าจะเป็นนอกจาก stock drop ~10% [9]

## การประยุกต์ใช้ในองค์กร — NDF DEV
1) เพิ่ม Android XR ในรายการ platform evaluation สำหรับโปรเจกต์ XR ใหม่ (Unity รองรับอยู่แล้ว); momentum จาก AWE และ Godot Day One support ทำให้นี่คือ growth target ที่ชัดที่สุด [18][7] — effort: กลาง 2) สำหรับ edutech/e-learning ศึกษา pattern immersive-training และ cultural-experience (XR onboarding/training, Versailles, Nutcracker) เป็น reference model สำหรับงาน e-learning ของ NDF [52][35][42][59] — effort: ต่ำ 3) ทดลอง Gaussian splat / world model capture (แบบ Marble, Over the Reality) เพื่อสร้าง 3D asset จากสภาพแวดล้อมจริงสำหรับเนื้อหา location-based หรือ edu [25][21] — effort: กลาง 4) ถ้ามีงาน Vision Pro ใน roadmap ติดตาม engine bridge UnRealityKit/RealityKit ก่อนลงทุนเวลา pipeline [16][54] — effort: ต่ำในการติดตาม สูงในการ build ข้าม: Snap Specs เป็น near-term target เมื่อดูจากราคาและ market signal [9]; noise ทั้งหมดเกี่ยวกับ iPhone-XR, esports, crypto และปรัชญา simulation [2][11][14][15][17][1]; การพึ่ง Meta Quest store เป็น primary distribution เมื่อพิจารณา complaint ด้านคุณภาพของ store ที่ปรากฏ [22]

## สัญญาณที่ต้องติดตาม
- ความเร็วของ Android XR ecosystem — ความต้องการ XREAL Aura, Qualcomm Snapdragon Reality Elite และ Godot 4.7 support [18][48][7]
- ความต่อเนื่องของ Vision Pro — cadence ของ visionOS 27 beta และข้อได้เปรียบของ M5 device เทียบกับกระแสยกเลิก [30][36]
- World models / Gaussian splatting สำหรับสร้าง 3D environment (Marble, Over the Reality) [25][21]
- แรงกดด้านราคา consumer AR glasses หลัง Snap Specs ที่ $2,195 และหุ้นร่วง ~10% [9][26]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | davidicke | ^1235 c190 | [It's a simulation which the human body biological computer decodes into an illus](https://x.com/davidicke/status/2068206124419985614) |
| x | Bigwavee00 | ^1181 c232 | [This app is actually crazy 😭 Someone came to my DM asking for help to complete m](https://x.com/Bigwavee00/status/2067669011374981401) |
| x | Nick_Marseil | ^624 c174 | [It all depends Best games? PS5 Best 3rd party support? PS5 Best controller? PS5 ](https://x.com/Nick_Marseil/status/2067914602160029955) |
| x | justinryanio | ^602 c50 | [To my Vision Pro friends, I uploaded Tim Cook's final WWDC "Good Morning" in 8K ](https://x.com/justinryanio/status/2067990398438359526) |
| x | VRChat | ^542 c24 | [Glasses and Hat Accessories, now in the VRChat Shop! https://t.co/T4YmxU9aGq](https://x.com/VRChat/status/2068076354520633652) |
| x | axi_master | ^541 c74 | [Today, @aadityasubedi_ and I are excited to introduce @architectlabs. We are bui](https://x.com/axi_master/status/2067655053050352041) |
| x | SadlyItsBradley | ^484 c10 | [Godot 4.7 has released and adds a bunch of "Day One" support and new features fo](https://x.com/SadlyItsBradley/status/2067680624974926324) |
| x | Space_Station | ^480 c19 | [Expedition 74 used ultrasound scans, augmented reality, and artificial intellige](https://x.com/Space_Station/status/2067671173287326117) |
| x | mymixtapez | ^421 c25 | [Snapchat's CEO announced Augmented Reality glasses for $2,195 &amp; the stock im](https://x.com/mymixtapez/status/2067658060735123483) |
| x | SpatiallyMe | ^374 c18 | [Wow. Full-body hologram videos that look straight out of a sci-fi movie are now ](https://x.com/SpatiallyMe/status/2068004293320311155) |
| x | pinkpnterest | ^337 c39 | [The iPhone 13 feels too heavy for regular usage. I've decided to switch to an Xr](https://x.com/pinkpnterest/status/2067670073322484170) |
| x | trythreews | ^321 c36 | [three․ws is the 3D AI agent layer of the open web. Anyone can generate a 3D avat](https://x.com/trythreews/status/2067752802689102011) |
| x | SnazzyLabs | ^269 c13 | [Elemental is one of my favorite Pixar movies, but I admit it's because I first s](https://x.com/SnazzyLabs/status/2068090606065471816) |
| x | HappyMotorhead | ^206 c119 | [Top or Bottom? 1968 Pontiac GTO or 1968 Mercury Cougar XR-7 https://t.co/wONuLFq](https://x.com/HappyMotorhead/status/2067639985834975345) |
| x | kappybruh | ^152 c0 | [Your crypto shouldn't be sitting idle this summer. Fr. HTX just launched their S](https://x.com/kappybruh/status/2067911422999167155) |
| x | iBrews | ^151 c5 | [First pass translating UE5 Lumen GI into Apple Vision Pro to affect both the vir](https://x.com/iBrews/status/2067758099390169201) |
| x | smartbackwards | ^144 c1 | [according to my model, 9z had more expected rounds than FURIA and yet, they lost](https://x.com/smartbackwards/status/2067865824191217813) |
| x | XREAL_Global | ^141 c3 | [That's a wrap on the AWE show floor! Thank you to everyone who joined us at the ](https://x.com/XREAL_Global/status/2067781914237518300) |
| x | mxn_taratiny | ^135 c2 | [SO MUCH - OG HALA FITS (SMN/Kingdom/Fever XR) - Woo w/ fedora (Halazia+Ash) - Co](https://x.com/mxn_taratiny/status/2068322314882593193) |
| x | faythebest | ^122 c4 | [Apple Vision Pro can't be dead! 3D movies are being added frequently and apps li](https://x.com/faythebest/status/2067722823737430051) |
| x | OVRtheReality | ^116 c24 | [America. Europe. Africa. Asia. Oceania. More than 250,000 real-world locations a](https://x.com/OVRtheReality/status/2067909570274418826) |
| x | bmfshow | ^115 c11 | [Wanna know how messed up the Meta Quest store is? Check out the video below abou](https://x.com/bmfshow/status/2068041112778895790) |
| x | Stella_Liberty | ^106 c1 | [In my latest clip, Dollhouse Rent is Overdue, I force my tiny tenant into foot w](https://x.com/Stella_Liberty/status/2067985061442408462) |
| x | neilcybart | ^103 c9 | [Modern mobile phones have been available for ~30 years. Modern smartphones (iPho](https://x.com/neilcybart/status/2067937735231287378) |
| x | smallfly | ^103 c8 | [@FastCompany just published a great piece on @theworldlabs , @drfeifei , Marble,](https://x.com/smallfly/status/2067638115494252832) |
| x | Scobleizer | ^98 c13 | [Sabrina is way better at selling us on augmented reality glasses than anyone els](https://x.com/Scobleizer/status/2067872340487381425) |
| x | nascarcasm | ^95 c0 | [At the Navy Strike Group activation in the green zone by the S/F line: - Take pa](https://x.com/nascarcasm/status/2068032085017915726) |
| x | BScottyL | ^92 c15 | [@Progress_aje @socetyhatesjay Werey your life don spoil😂 if you have the money b](https://x.com/BScottyL/status/2067972129719517212) |
| x | AJE_Sport | ^83 c6 | [A Filipino artist has created a giant sand portrait of Lionel Messi on a beach i](https://x.com/AJE_Sport/status/2067689093513744791) |
| x | tom_krikorian | ^82 c11 | [visionOS 27 Beta 2 is still not available one week after WWDC26. I hope it doesn](https://x.com/tom_krikorian/status/2067725508586930299) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@davidicke</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1235 · 💬 190</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/davidicke/status/2068206124419985614">View @davidicke on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It's a simulation which the human body biological computer decodes into an illusory holographic 'world' that humans think is real. There is no more 'distance', 'space' or 'time' than in a virtual real”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>David Icke อ้างว่าความเป็นจริงทางกายภาพคือ holographic simulation ที่สมองมนุษย์ decode เหมือน VR game — ไม่มี space, distance หรือ time จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/davidicke/status/2068206124419985614" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Bigwavee00</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1181 · 💬 232</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Bigwavee00/status/2067669011374981401">View @Bigwavee00 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This app is actually crazy 😭 Someone came to my DM asking for help to complete money for an iPhone XR. She said she has ₦140k and needs ₦50k more already found where to buy it for ₦190k. I told her, “”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>vendor มือถือในไนจีเรียเล่าเรื่องไวรัล มีคนพยายามหลอกให้โอน ₦50k โดยแกล้งทำเป็นว่าต้องการความช่วยเหลือซื้อ iPhone XR.</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Bigwavee00/status/2067669011374981401" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Nick_Marseil</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 624 · 💬 174</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Nick_Marseil/status/2067914602160029955">View @Nick_Marseil on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It all depends Best games? PS5 Best 3rd party support? PS5 Best controller? PS5 Virtual Reality? PS5 Most powerful box? PS5 Bigger community? PS5 Best physical games support? PS5 Best achievement syst”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X โพสต์สรุปว่า PS5 ชนะในทุกหมวด รวมถึง VR โดยไม่มีข้อมูลหรือรายละเอียดทางเทคนิคใดรองรับ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Nick_Marseil/status/2067914602160029955" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@justinryanio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 602 · 💬 50</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/justinryanio/status/2067990398438359526">View @justinryanio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“To my Vision Pro friends, I uploaded Tim Cook’s final WWDC “Good Morning” in 8K 360°. Filmed from the media section at Apple Park, with the goal of helping more people experience what it felt like to ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator อัป video 8K 360° ช่วง 'Good Morning' ของ Tim Cook ใน WWDC ล่าสุด ถ่ายจาก media section ที่ Apple Park ดูบน Apple Vision Pro ได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป็นตัวอย่าง workflow จริงของการถ่าย 8K 360° ใน live event — ตรงกับงาน XR content ของ studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้ setup นี้ (8K 360° จุดตายตัว) เป็น reference workflow สำหรับงาน XR event coverage ของ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/justinryanio/status/2067990398438359526" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VRChat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 542 · 💬 24</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VRChat/status/2068076354520633652">View @VRChat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Glasses and Hat Accessories, now in the VRChat Shop! https://t.co/T4YmxU9aGq”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>VRChat เพิ่ม accessory ประเภทแว่นตาและหมวกใน VRChat Shop — เป็น update ฝั่ง storefront ไม่ใช่ platform หรือ SDK</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VRChat/status/2068076354520633652" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@axi_master</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 541 · 💬 74</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/axi_master/status/2067655053050352041">View @axi_master on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Today, @aadityasubedi_ and I are excited to introduce @architectlabs. We are building the AI system to design and provably verify chips for the world's most demanding workloads. AI scaling is fundamen”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Architect Labs เปิดตัว บริษัทสร้าง AI system สำหรับออกแบบและ verify chip โดยเฉพาะ เป้าหมายคือ data center, robotics, spatial computing และ specialized compute อื่นๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/axi_master/status/2067655053050352041" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SadlyItsBradley</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 484 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SadlyItsBradley/status/2067680624974926324">View @SadlyItsBradley on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Godot 4.7 has released and adds a bunch of “Day One” support and new features for various XR platforms This includes production-ready support for games on AndroidXR and SteamOS on the Steam Frame They”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Godot 4.7 ออกแล้ว รองรับ AndroidXR และ SteamOS บน Steam Deck Frame แบบ Day One production-ready พร้อม HDR output บน Windows, macOS, iOS, visionOS และ Linux (Wayland)</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Godot 4.7 ปิด gap กับ Unity ด้าน XR — รองรับ AndroidXR แบบ Day One ทำให้เป็นทางเลือก royalty-free สำหรับ XR pipeline ของ studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">XR team ทดสอบ Godot 4.7 สำหรับ prototype AndroidXR ในโปรเจกต์ที่ค่า Unity license หรือ binary size เป็นปัญหา</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SadlyItsBradley/status/2067680624974926324" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Space_Station</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 480 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Space_Station/status/2067671173287326117">View @Space_Station on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Expedition 74 used ultrasound scans, augmented reality, and artificial intelligence to study cartilage growth, blood vessels, and the digestive system on Thursday to protect crew health and improve pa”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ลูกเรือ Expedition 74 ใช้ AR overlay + AI ช่วยนำทาง ultrasound scan ดูกระดูกอ่อน, หลอดเลือด, และระบบย่อยอาหารบน ISS</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การ deploy บน ISS จริงยืนยันว่า AR + AI พร้อมใช้ใน medical imaging guidance แล้ว — healthcare เป็น XR vertical ที่ได้รับการพิสูจน์แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้เป็น reference ยืนยัน use case AR + AI ด้าน healthcare ตอน pitch XR solution ให้ลูกค้ากลุ่ม medical หรือ tele-health</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Space_Station/status/2067671173287326117" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
