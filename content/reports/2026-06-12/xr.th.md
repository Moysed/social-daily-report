---
type: social-topic-report
date: '2026-06-12'
topic: xr
lang: th
pair: xr.en.md
generated_at: '2026-06-12T03:17:59+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 134
salience: 0.58
sentiment: mixed
confidence: 0.55
tags:
- visionos27
- apple-vision-pro
- gaussian-splatting
- realitykit
- wwdc26
- xr-hardware
thumbnail: https://pbs.twimg.com/media/HKeZr2TX0AAXoAx.jpg
translated_by: claude-sonnet-4-6
---

# XR / VR / AR — 2026-06-12

## TL;DR
- สัญญาณ XR วันนี้มาจาก Apple WWDC26 / visionOS 27 เกือบทั้งหมด; รายการที่ engagement สูง ([2],[4],[7],[8],[10],[23],[32],[50],[54] iPhone XR; [3],[48] Adderall XR; [14],[49],[52],[59] adult spam) คือ keyword noise ไม่ใช่ XR จริง
- Apple ปล่อย Godot plugin อย่างเป็นทางการ ซึ่งแทน renderer ของ Godot ด้วย RealityKit บน Vision Pro [13]; ฝั่ง third-party มี UE5→RealityKit bridge ('UnRealityKit') ที่ออกมาเพื่อหลีก Metal limitations บน AVP [35]
- Gaussian splatting ถูกนำไปใช้ใน Apple Maps บน Vision Pro [11][16] และสามารถสร้าง/ดูได้บนอุปกรณ์โดยตรง [55] แต่ near-field culling ทำให้ splat หายไปเมื่ออยู่ใกล้ ส่งผลให้ฉากภายในใช้งานไม่ได้ [53]
- visionOS 27 เพิ่ม ComputeGraph framework (particles บน Vision Pro M5) [22], Siri แบบ conversational ใหม่ [26], และ Spatial Preview ใน macOS Preview [15]; คำว่า 'Vision Pro' ถูกพูดถึงซ้ำตลอด keynote [44]
- ข่าวลือ 'Apple เลิกผลิต Vision Pro' มีที่มาจากการยุติจำหน่าย travel case ไม่ใช่ตัวผลิตภัณฑ์ [18][36]; Gurman ยังระบุว่า Apple ไม่ได้ยืนยันว่า form-factor ปัจจุบันเป็น priority [31]; Qualcomm ทีซ chip XR รุ่นถัดไป คาดว่าอาจใช้ใน Pico รุ่นหน้า [39]

## What happened
WWDC26 ของ Apple ครองสัญญาณ XR ทั้งหมด visionOS 27 ออกมาพร้อม ComputeGraph framework ที่ demo รัน particles บน Vision Pro M5 [22], Siri แบบ conversational ใหม่ภายใน headset [26], Spatial Preview ที่โผล่ใน macOS (แอป Preview) [15], และ native ultrawide support บน Apple Silicon ใน macOS 27 [60] ด้านเอนจิ้น Apple ปล่อย Godot plugin อย่างเป็นทางการที่สลับ renderer ของ Godot เป็น RealityKit แทนการพอร์ต [13] และนักพัฒนารายหนึ่งเผยแพร่ UE5+RealityKit bridge เพื่อดึง eye tracking, gestures และ room lighting กลับคืนมาหลังจากถูก Metal บน AVP บล็อก [35] Gaussian splatting ถูกนำไปใช้ใน Apple Maps บน Vision Pro [11][16], รองรับการถ่าย/ดูบนอุปกรณ์ทั้งหมด [55] และปรากฏในแอปที่ ship จริงอย่าง Blockworks [30] แต่นักพัฒนาพบปัญหา near-field culling ที่ก้าวร้าวจนทำให้ splat หายเมื่ออยู่ใกล้ [53]

## Why it matters (reasoning)
การเปลี่ยนแปลงที่สำคัญอยู่ที่ชั้น engine: เส้นทางอย่างเป็นทางการของ Apple ขึ้น Vision Pro คือ RealityKit และทั้ง Godot [13] กับ Unreal [35] ต่างผ่านมันเพื่อหลี Metal feature gaps สำหรับ Unity studio นี่คือข้อมูลเชิงกลยุทธ์ — Apple ให้การสนับสนุนอย่างเป็นทางการแก่ Godot ไม่ใช่ Unity และ pattern ที่เน้น RealityKit ก็ตรงกับเส้นทาง visionOS ที่ Unity ใช้อยู่แล้ว การที่ Gaussian splats ขยับเข้าสู่แอป first-party (Maps) [11][16] บวกกับ on-device generation [55] บ่งชี้ว่า splats กำลังกลายเป็น format มาตรฐานสำหรับ immersive content แต่ข้อจำกัดเรื่อง culling [53] ทำให้ยังเชื่อถือไม่ได้สำหรับฉากภายใน/ปิด แยกออกไป เรื่อง 'discontinued' ที่สรุปว่าเป็นแค่ carrying case [18][36] ในขณะที่ Gurman ยังไม่ยืนยันอนาคต form-factor [31] ทำให้ความเสี่ยงด้าน hardware roadmap ยังมีอยู่ และ chip tease ของ Qualcomm [39] รวมถึงแนวคิด interchangeable-compute [47] ชี้ให้เห็นว่าการแข่งขันในตลาด standalone ที่ไม่ใช่ Apple ยังคงดำเนินต่อไป การโจมตี supply-chain ต่อ Linux package 'alvr' ที่ถูกทิ้งแล้ว [12] เป็นการเตือนชัดเจนว่า VR dev tooling กลายเป็นเป้าหมายแล้ว

## Possibility
**Likely:** Apple ยังคงลงทุนกับ visionOS software stack ในระยะสั้น — ความครอบคลุมของ visionOS 27, silicon M5, on-device splats และการพูดถึงซ้ำใน keynote [22][44][55] มีน้ำหนักมากกว่า noise เรื่อง case discontinued [36] **Plausible:** Gaussian splats กลายเป็น pipeline มาตรฐาน capture-to-immersive สำหรับแผนที่และฉากต่างๆ แต่การใช้งานภายในยังติดขัดจนกว่า culling จะได้รับการแก้ไข [53] **Plausible:** Snapdragon XR chip รุ่นใหม่ลงใน Pico flagship ทำให้การแข่งขัน standalone คมชัดขึ้น [39][47] **Unlikely (จากหลักฐานที่มี):** Apple ยกเลิก Vision Pro — สิ่งที่ยืนยันได้ว่า 'discontinued' คือ travel case เท่านั้น [18][36] แม้ว่า priority ของ hardware revision ถัดไปยังไม่ชัดเจน [31] ไม่มีแหล่งข้อมูลใดให้ตัวเลขความน่าจะเป็น

## Org applicability — NDF DEV
1) ตรวจสอบ RealityKit path สำหรับ Vision Pro target ซ้ำอีกครั้ง: ทั้ง Godot และ Unreal ต่าง bridge ผ่าน RealityKit เพื่อหลีก Metal limits [13][35] — ยืนยันว่า Unity PolySpatial/RealityKit route ยังตอบโจทย์ก่อนลง engine effort (med) 2) Prototype Gaussian splat capture สำหรับฉาก edutech/immersive [11][16][55] แต่ทดสอบ near-field culling ก่อนและหลีกเลี่ยง splat-based interiors จนกว่าจะแก้ได้ [53] (med) 3) Audit และ pin dependencies ใน Linux VR streaming/dev tooling หลังเกิด alvr supply-chain attack [12] (low) 4) ติดตาม Snapdragon XR chip / Pico flagship เป็น non-Apple standalone target สำหรับงาน XR ในอนาคต [39] (low, monitor only) ข้าม: ข่าวลือ 'Vision Pro discontinued' [18][36]; ความเห็นเรื่อง FIFA VR-studio [1]; และทุกรายการ iPhone XR / Adderall XR / adult-content — ไม่เกี่ยวกับ XR

## Signals to Watch
- Gurman ไม่ยืนยันว่า Vision Pro form-factor เป็น priority ปัจจุบัน [31] — รอสัญญาณ AVP hardware ถัดไป
- Qualcomm next-gen Snapdragon XR chipset คาดว่าอยู่ใน Pico รุ่นหน้า [39]
- Supply-chain attack ที่ยังดำเนินอยู่ต่อ Linux VR package 'alvr' ที่ถูกทิ้งแล้ว [12]
- Apple จะแก้ Gaussian splat near-field culling หรือไม่เพื่อให้ฉากภายในใช้งานได้ [53]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | The_Forty_Four | ^8737 c575 | [Two different budgets for the FIFA World Cup 2026! Two studios ITV= New York Sky](https://x.com/The_Forty_Four/status/2064788088769896584) |
| x | YKoluwaseun9 | ^7211 c428 | [Boyfriend 17 pro max, Girlfriend XR. sweet couple❤️ https://t.co/sgHgFXNkmf](https://x.com/YKoluwaseun9/status/2064623762230714854) |
| x | dannarebb | ^4189 c30 | [6 years ago today, I found a few of these Adderall XR branded pill dispensers wh](https://x.com/dannarebb/status/2065137973553742254) |
| x | Thebigsoll | ^3220 c166 | [I've been barbing at this shop for close to 5 years now. Usually when I come her](https://x.com/Thebigsoll/status/2065134233471852890) |
| x | Abathor_Game | ^969 c11 | [An emulator for playing NES games in retro 3D and augmented reality. 3D SEN. htt](https://x.com/Abathor_Game/status/2065051626335789298) |
| x | justinryanio | ^910 c31 | [I asked Apple if Vision Pro is "on ice." https://t.co/4K9cPTAHmz](https://x.com/justinryanio/status/2064854521524990024) |
| x | Bigwavee00 | ^842 c68 | [A guy entered my store one afternoon around last year and asked for the price of](https://x.com/Bigwavee00/status/2065050902151541096) |
| x | THEOCTOPUS_1 | ^727 c31 | [iPhone 13 be the new XR edey heat pass Lamine Yamal ein teds.](https://x.com/THEOCTOPUS_1/status/2064695036961263729) |
| x | ValerieAnne1970 | ^590 c133 | [The World Economic Forum has your future planned... "The rich will be able to tr](https://x.com/ValerieAnne1970/status/2065162152776696290) |
| x | gnf_ogo | ^559 c20 | [my sister change am for me two weeks ago, now she wan change her XR I see "good ](https://x.com/gnf_ogo/status/2065063483712909436) |
| x | justinryanio | ^535 c8 | [Apple Maps now uses Gaussian Splats on Apple Vision Pro, and it looks incredible](https://x.com/justinryanio/status/2064586854721290358) |
| x | vxunderground | ^529 c18 | [Word on the Linux nerd streets is someone is actively attempting a supply chain ](https://x.com/vxunderground/status/2065123579541238223) |
| x | iBrews | ^356 c13 | [Apple shipped a first-party Godot plugin at WWDC26 and it's wilder than it sound](https://x.com/iBrews/status/2064564332868870411) |
| x | badbunnyxn | ^306 c1 | [Stop jerking to pics. Create the guy &amp; fuck him live on video call or in ful](https://x.com/badbunnyxn/status/2064605423081230682) |
| x | SadlyItsBradley | ^301 c5 | [I totally didn't realize that Preview on MacOS also implements the new Spatial P](https://x.com/SadlyItsBradley/status/2064811121677160685) |
| x | NathieVR | ^259 c11 | [You can now experience Apple Maps using Gaussian splats on Apple Vision Pro. Loo](https://x.com/NathieVR/status/2064791922645012560) |
| x | emabilly2001 | ^223 c38 | [Rate my photography skills From 1 to 10. Shot📷 by Iphone XR..... https://t.co/Uf](https://x.com/emabilly2001/status/2064582055023813025) |
| x | MacRumors | ^220 c13 | [Apple Seemingly Discontinuing Vision Pro Travel Case Around the World https://t.](https://x.com/MacRumors/status/2064705195851079859) |
| x | beebomco | ^205 c6 | [Watching videos on the Vision Pro is SOOOOOOO GOOD NOW! BTW, have you watched ou](https://x.com/beebomco/status/2064744750784327966) |
| x | JISOOPOPBASE | ^204 c2 | [@netflix recommends "Boyfriend on Demand" as one of "14 Workplace Rom-Coms "That](https://x.com/JISOOPOPBASE/status/2065139791725838733) |
| x | VRChat | ^202 c12 | [It's time for the June 11 Developer Update! Read about how Third-Person mode on ](https://x.com/VRChat/status/2065157380837425499) |
| x | ivancampos | ^183 c5 | [Vision Pro (M5) gets a little warm, but it can handle a bunch of particles progr](https://x.com/ivancampos/status/2064553538026434685) |
| x | a__vanita | ^175 c3 | [Went from iPhone 11 to Xr God will actually punish this thief.](https://x.com/a__vanita/status/2065135987429167476) |
| x | SadlyItsBradley | ^171 c5 | [Walt Disney World used Apple Vision Pros to streamline the live audio mixing pro](https://x.com/SadlyItsBradley/status/2065243179247370739) |
| x | hangzhoufeel | ^169 c0 | ["China has made remarkable achievements, especially in technologies such as virt](https://x.com/hangzhoufeel/status/2065051682569064509) |
| x | nandoprince93 | ^142 c10 | [✨ The new Siri AI on Vision Pro is pure magic. 🤯🥽 Having natural conversations, ](https://x.com/nandoprince93/status/2064767472062930975) |
| x | DominicCarterLA | ^142 c4 | [The Apple Vision Pro is the 1 device that will single handedly bring us back to ](https://x.com/DominicCarterLA/status/2064860886498771205) |
| x | emabilly2001 | ^140 c18 | [It's me again.... 📷 Iphone XR Edited By Adobe. Au niwe mobile grapher 😄🔥 wanangu](https://x.com/emabilly2001/status/2064622509916316066) |
| x | conne_psd | ^137 c5 | [@gabefollower Steam 30% PlayStation Store 30% Xbox Game Store 30% Nintendo eShop](https://x.com/conne_psd/status/2065230828452397508) |
| x | ElasticSea | ^134 c1 | [This is how real-time cubemap reflections works on Vision Pro with RealityKit. B](https://x.com/ElasticSea/status/2065072431992066250) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@The_Forty_Four</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 8737 · 💬 575</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/The_Forty_Four/status/2064788088769896584">View @The_Forty_Four on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Two different budgets for the FIFA World Cup 2026! Two studios ITV= New York Skyline- whole production team out their for Six Weeks BBC= Virtual Reality studio in Salford Really dissapointing from the”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>BBC เลือกใช้ virtual production studio ที่ Salford ถ่ายทอด FIFA World Cup 2026 แทนส่งทีมไปนิวยอร์กเหมือน ITV ที่จัดทีมเต็มนาน 6 สัปดาห์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/The_Forty_Four/status/2064788088769896584" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@YKoluwaseun9</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7211 · 💬 428</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/YKoluwaseun9/status/2064623762230714854">View @YKoluwaseun9 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Boyfriend 17 pro max, Girlfriend XR. sweet couple❤️ https://t.co/sgHgFXNkmf”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ตลกเปรียบ iPhone รุ่น 17 Pro Max กับ iPhone XR เป็นคู่รัก — XR ในที่นี้คือรุ่น iPhone ไม่ใช่ Extended Reality</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/YKoluwaseun9/status/2064623762230714854" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@dannarebb</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4189 · 💬 30</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/dannarebb/status/2065137973553742254">View @dannarebb on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“6 years ago today, I found a few of these Adderall XR branded pill dispensers while doing a private book buy at a psychiatrists library. i asked if I could buy them and he said “you can just have them”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้เล่าเรื่องส่วนตัวว่าเจอกล่องยา Adderall XR branded ในงานขายหนังสือของจิตแพทย์เมื่อ 6 ปีก่อน</dd>
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
    <span class="ndf-engagement">♥ 3220 · 💬 166</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Thebigsoll/status/2065134233471852890">View @Thebigsoll on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I’ve been barbing at this shop for close to 5 years now. Usually when I come here to barb with my iPhone XR 64GB, changed screen, the barber never uses those extra care products. No hot towel, no powd”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Twitter เล่าแบบขำขัน: ไปร้านตัดผมร้านเดิม 5 ปีถือ iPhone XR ไม่เคยได้รับการดูแลพิเศษ พอเปลี่ยนเป็น iPhone 17 Pro ได้น้ำ hot towel และบริการ VIP ทันที</dd>
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
    <span class="ndf-author">@Abathor_Game</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 969 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Abathor_Game/status/2065051626335789298">View @Abathor_Game on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“An emulator for playing NES games in retro 3D and augmented reality. 3D SEN. https://t.co/WktAcOOGym”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>3D SEN คือ NES emulator ที่ render เกม classic ในรูปแบบ retro 3D และ AR วาง game world ลงใน physical space ของผู้เล่น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัวอย่าง AR จริงที่ spatialize 2D content — เป็น reference ดีสำหรับทีม XR ที่ต้องจัดการ asset ที่ไม่ได้เป็น 3D ตั้งแต่ต้น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ดู approach ของ 3D SEN เป็น reference ตอนออกแบบ AR overlay สำหรับ flat หรือ legacy content ในโปรเจกต์ของ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Abathor_Game/status/2065051626335789298" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@justinryanio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 910 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/justinryanio/status/2064854521524990024">View @justinryanio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I asked Apple if Vision Pro is “on ice.” https://t.co/4K9cPTAHmz”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักข่าว @justinryanio ถามAppleโดยตรงว่า Vision Pro ถูกหยุดหรือลด priority หรือไม่ สะท้อนว่ากระแสข่าว platform หยุดชะงักเริ่มน่าจริงจัง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า Apple ยืนยันว่า Vision Pro ชะลอจริง visionOS กลายเป็น platform ที่ risk สูงขึ้นสำหรับทีม XR ที่กำลังตัดสินใจลงทุน dev time</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">อ่านบทความที่ link ก่อน commit XR pipeline ของทีมไปกับ feature ที่ target visionOS เป็นหลักใน quarter นี้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/justinryanio/status/2064854521524990024" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Bigwavee00</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 842 · 💬 68</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Bigwavee00/status/2065050902151541096">View @Bigwavee00 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A guy entered my store one afternoon around last year and asked for the price of iPhone Xr but the money with him was way too small When he heard the amount, he smiled and said, “One day, I’ll buy it.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์เล่าเรื่องลูกค้าที่เคยซื้อ iPhone XR ไม่ได้เพราะเงินไม่พอ กลับมาซื้อ iPhone 16 Pro Max ได้ในปีถัดมา เป็น motivational story ส่วนตัว</dd>
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
    <span class="ndf-author">@THEOCTOPUS_1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 727 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/THEOCTOPUS_1/status/2064695036961263729">View @THEOCTOPUS_1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“iPhone 13 be the new XR edey heat pass Lamine Yamal ein teds.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ไม่เป็นทางการ ผสม iPhone model กับชื่อนักฟุตบอล ไม่มีเนื้อหาเทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/THEOCTOPUS_1/status/2064695036961263729" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
