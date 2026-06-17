---
type: social-topic-report
date: '2026-06-17'
topic: xr
lang: th
pair: xr.en.md
generated_at: '2026-06-17T15:18:50+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 142
salience: 0.72
sentiment: mixed
confidence: 0.7
tags:
- android-xr
- xreal-aura
- snapdragon
- unity
- ar-glasses
- gaussian-splats
thumbnail: https://pbs.twimg.com/media/HK8nzhkXoAAy-NJ.png
translated_by: claude-sonnet-4-6
---

# XR / VR / AR — 2026-06-17

## TL;DR
- ที่งาน AWE 2026 XREAL เปิดตัว AURA: แว่น optical see-through บน Android XR FOV 70 องศา เชื่อมต่อกับ compute puck ที่รัน Snapdragon Reality Elite ตัวใหม่จาก Qualcomm, Gemini แบบ hands-free, เปิดจอง, วางจำหน่ายปลายปีนี้ [7][9][22][25][32][58]
- Snapdragon Reality Elite อ้าง GPU สูงกว่า XR2+ Gen 2 ถึง 60% และ CPU สูงกว่า 30% รองรับทั้ง VR และ passthrough/see-through เปิดตัวครั้งแรกใน AURA puck [28][32][42]
- ทั้ง Unity และ Godot ประกาศ day-one support สำหรับ XREAL AURA ผ่านเส้นทาง Android XR / OpenXR — ตรงประเด็นโดยตรงสำหรับ Unity studio [43][24]
- Snap เปิดตัวแว่น AR รุ่น Specs ราคา $2,195 พร้อม pre-order แล้ว; กระแสตอบรับแตกออกเป็น 'milestone' กับ 'ไม่มีคนต้องการ / ดูแย่' [15][44][46][53]
- ข่าว Apple Vision Pro เป็นเพียงอัปเดตซอฟต์แวร์ (Siri UI ใหม่, แอนิเมชัน Persona scan) และแอป 4D gaussian-splat streaming จากบุคคลที่สาม ชื่อ Gracia [3][4][39][59]

## สิ่งที่เกิดขึ้น
สัญญาณส่วนใหญ่รวมตัวอยู่ที่งาน AWE 2026 XREAL ประกาศ AURA ซึ่งระบุว่าเป็นแว่น optical see-through บน Android XR ที่ขับเคลื่อนด้วย AI รุ่นแรก พัฒนาร่วมกับ Google และ Qualcomm: FOV ประมาณ 70 องศา, X1S Spatial Coprocessor, จอ optical see-through, Gemini แบบ hands-free และ compute puck แบบมีสาย; เปิดจอง/pre-order แล้ว วางจำหน่ายปลายปีนี้ [7][9][19][22][25][49][58] puck รัน Snapdragon Reality Elite ชิปเซ็ตที่ Qualcomm เพิ่งประกาศ (GPU +60% และ CPU +30% เทียบ XR2+ Gen 2 เน้นหัวเชื่อมต่อสาย MR และแว่น see-through) [14][28][32][42] Unity และ Godot ต่างเผยแพร่ support สำหรับ AURA ผ่านระบบนิเวศ Android XR [43][24] แยกส่วน Snap เปิดตัว Specs แว่น AR ราคา $2,195 พร้อมแอป, นำทาง, AI และเกม สั่งจองได้เลยวันนี้ [15][44][47][53] และ VITURE ทีเซอร์ Helix AI glasses ที่สร้างบน XR AI stack ของ NVIDIA [36]

## สาเหตุที่สำคัญ
ศูนย์กลางรอบนี้คือ Android XR ในฐานะ platform ร่วม: Google + Qualcomm + XREAL ส่งมอบอุปกรณ์ optical see-through เชิงพาณิชย์ พร้อม engine support จาก Unity และ Godot ที่มาพร้อมกับฮาร์ดแวร์ [43][24][58] สำหรับ Unity-based studio นี่ลด cost ในการขยายไปยัง XR device class ใหม่ — toolchain ยังคงเป็น engine เดิม เข้าถึง OS ผ่าน OpenXR การออกแบบแบบ tethered puck คือ trade-off ที่มองเห็นได้ชัด: ยอมรับสายเพื่อใส่ compute และ battery จริงๆ เข้าไปในรูปแบบแว่นตา [14][30] ซึ่งเป็นเหตุให้กระแสตอบรับแตกระหว่าง 'ความสำเร็จด้านวิศวกรรมมหาศาล' กับ 'แค่ใส่ Vision Pro ไปเลย' [6][21][23][30] Apple ส่งเฉพาะซอฟต์แวร์อัปเดตเพิ่มเติม ไม่มีฮาร์ดแวร์ บวกกับสัญญาณว่า content pipeline กำลังเคลื่อนไปทาง gaussian-splat / 4D volumetric media [39][59] ราคา $2,195 ของ Snap Specs และคอมเมนต์ 'ไม่มีคนต้องการ' / 'ดูแย่' ซ้ำๆ [35][46][50] ยืนยันว่าแว่น AR สำหรับผู้บริโภคยังแพงและยังไม่พิสูจน์ตัวเอง; momentum ของ platform อยู่ที่ชั้น developer SDK ไม่ใช่ consumer adoption

## ความเป็นไปได้
**น่าจะเกิด:** Android XR จะรวมตัวเป็น XR target ที่รองรับโดย engine ตัวที่สามตลอด 2026 จากการสนับสนุนพร้อมกันของ Unity, Godot, Qualcomm และ Google [24][43][58] **อาจเกิดขึ้น:** แว่น tethered แบบ AURA หาทางอยู่ในกลุ่ม productivity/work และ AI-assistant ก่อนที่ standalone all-day AR จะเป็นไปได้จริง เพราะ puck มีอยู่เพื่อรับ compute ที่แว่นรับไม่ได้โดยตรง [14][30][36] **อาจเกิดขึ้น:** tooling สำหรับ gaussian-splat / volumetric content (Gracia) กลายเป็น format immersive-content มาตรฐานทั้งบน Vision Pro และ Android XR [39][59] **ไม่น่าเกิดในระยะสั้น:** Snap Specs หรือแว่น AR ราคา $2,000+ จะถึง mass consumer adoption — ความสงสัยในตัวเลข demand และการเปรียบกับ Vision Pro บ่งชี้ตรงกันข้าม [46][50][53] ไม่มีแหล่งใดให้ตัวเลขยอดขาย ดังนั้นอย่าถือว่า volume claim ใดๆ มีข้อมูลสนับสนุน

## ความเกี่ยวข้องกับองค์กร — NDF DEV
1) ประเมิน Android XR ในฐานะ Unity build target ตอนนี้ที่ engine support ออกมาแล้ว — สร้าง test project บน OpenXR/Android XR path; ใช้ Unity skills ที่มีอยู่ [43][24] (effort: med) 2) จดสเปค Snapdragon Reality Elite ไว้สำหรับงาน MR/passthrough ในอนาคต; สถาปัตยกรรม puck-tethered เปลี่ยน performance budget เทียบ standalone [28][42] (effort: low, research only) 3) ทดลอง gaussian-splat / 4D capture workflows (แบบ Gracia) เป็นทางเลือก immersive-content สำหรับงาน edutech/XR เพราะ format นี้ ship บน Vision Pro แล้วและ align กับ Android XR [39][59] (effort: med) 4) สำหรับ training/edutech ตัวอย่าง VR reaction-time coaching เป็น use-case reference บางๆ แต่ concrete [54] (effort: low) ข้ามไปเลย: ซื้อ Snap Specs $2,195 หรือ build สำหรับมัน — niche แพง ยังไม่พิสูจน์ตัวเอง [44][46]; ข้าม consumer Vision Pro hype, iPhone-XR phone chatter และ crypto/blockchain '3D AI agent' ทั้งหมดถือเป็น noise [1][10][16][31][55]

## Signals to Watch
- XREAL AURA จะ ship จริงปลายปีนี้หรือไม่ และ UX ของ cabled-puck รีวิวอย่างไร — นี่คือ test case ของ Android XR optical see-through [25][32]
- ความสมบูรณ์ของ docs Android XR support ของ Unity และ OpenXR feature gaps เทียบ Godot's vendor plugin [43][24]
- tooling gaussian-splat / 4D capture ขยายออกจาก Vision Pro ไปยัง Android XR ในฐานะ content format [39][59]
- OEM รายอื่น (VITURE และอื่นๆ) จะ standardize บน Snapdragon Reality Elite + Android XR หรือไม่ ซึ่งจะส่งสัญญาณ SDK target ร่วม [36][42]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | fwedesignerx | ^3917 c84 | [Bomb No collect loan Dress well Smell nice, even if na mousuf No give poor girl ](https://x.com/fwedesignerx/status/2066853665281864086) |
| x | Rainmaker1973 | ^3704 c106 | [Birds can literally see the Earth's magnetic field thanks to specialized light-s](https://x.com/Rainmaker1973/status/2066914531184406681) |
| x | SpatiallyMe | ^1396 c11 | [Shoutout to whoever at Apple came up with these beautiful animations that appear](https://x.com/SpatiallyMe/status/2066920677563666690) |
| x | justinryanio | ^1279 c33 | [The new Siri AI on Apple Vision Pro is just so beautiful. I can't stop staring a](https://x.com/justinryanio/status/2066766077292318884) |
| x | VRChat | ^1052 c20 | [NEW UPCOMING VRCHAT EVENT: Tanabata! This July 6-12, we'll be hosting a Tanabata](https://x.com/VRChat/status/2066637523095363753) |
| x | SnazzyLabs | ^512 c19 | [At that point, just wear a Vision Pro.](https://x.com/SnazzyLabs/status/2067034411800101199) |
| x | Android | ^508 c17 | [Say hello to @XREAL_GLOBAL AURA ⚡️ ✅ Sleek, lightweight design ✅ Massive 70-degr](https://x.com/Android/status/2066928860415906081) |
| x | VRChat | ^463 c13 | [Amazing Low-Poly Worlds by @ShopowVR ! Check them out on VRChat! https://t.co/cJ](https://x.com/VRChat/status/2067004288845689306) |
| x | stufflistings | ^391 c24 | [XREAL has announced their new spatial computing glasses. 70-degree field of view](https://x.com/stufflistings/status/2066936500181508586) |
| x | Motee_1 | ^388 c34 | [car specialists, what's the equivalent of purchasing this car in 2026 in the iph](https://x.com/Motee_1/status/2066839948871815674) |
| x | AutismCapital | ^378 c50 | [The Vision Pro actually looks way cooler on the face but the world isn't ready f](https://x.com/AutismCapital/status/2067065730227700015) |
| x | terronk | ^363 c5 | [It's Meta Raybans at Apple Vision Pro prices. https://t.co/9q8F6vF5qT](https://x.com/terronk/status/2067036695514718692) |
| x | hns_vibez4u | ^316 c21 | [What if a chip was implanted in your brain to see a virtual reality world. These](https://x.com/hns_vibez4u/status/2066766636409856106) |
| x | SadlyItsBradley | ^312 c15 | [Qualcomm's newest line of XR chips is targeting high end devices. Particularly t](https://x.com/SadlyItsBradley/status/2066879486771986907) |
| x | Snap | ^284 c78 | [Introducing @SPECS, our new augmented reality glasses built to bring AI assistan](https://x.com/Snap/status/2066934334708461973) |
| x | trythreews | ^264 c15 | [It's time to break AI out of the chatbox and anchor it in reality. With https://](https://x.com/trythreews/status/2067042641834098748) |
| x | VRChat | ^253 c2 | [The #VRCTanabata七夕 Wish Form is here! Please let us know what you wish for durin](https://x.com/VRChat/status/2066946842449879334) |
| x | nandoprince93 | ^206 c17 | [Bruh, what am I looking at. I'd rather wear the Vision Pro in public than this](https://x.com/nandoprince93/status/2067006305613570511) |
| x | XREAL_Global | ^193 c8 | [To build the next major leap in spatial computing, you can't rely on standard ha](https://x.com/XREAL_Global/status/2066954171857965327) |
| x | EmzyGadgets | ^191 c34 | [Ok READ THIS IF YOU USE IPHONE‼️ LL/A is just the last 3 alphabets at the model ](https://x.com/EmzyGadgets/status/2067146604226777376) |
| x | mason__capital | ^173 c30 | [&gt; Fixed Vision Pro's weight issue &gt; No stupid puck to haul around &gt; Att](https://x.com/mason__capital/status/2067061717008351740) |
| x | BenGeskin | ^171 c7 | [XREAL just officially unveiled XREAL AURA, previously known as Project Aura 🕶️ T](https://x.com/BenGeskin/status/2066932694273954263) |
| x | iupdate | ^170 c10 | [At this point just wear an Apple Vision Pro on your head](https://x.com/iupdate/status/2067009256507981984) |
| x | godotengine | ^161 c1 | [At AWE, Google and XReal officially showed the new XReal Aura glasses running An](https://x.com/godotengine/status/2066944663974551830) |
| x | XREAL_Global | ^147 c8 | [Reservations for the XREAL AURA are officially open! 🕶️ All the power of spatial](https://x.com/XREAL_Global/status/2066932026939449688) |
| x | CS_MarketingIR | ^133 c18 | [Coda Octopus Group Nasdaq: $CODA Coda Octopus reported fiscal second quarter 202](https://x.com/CS_MarketingIR/status/2066863117473022405) |
| x | ClassicXMen | ^131 c0 | [X-Force #61 cover dated December 1996. The Shatterstar Saga continues! Cable and](https://x.com/ClassicXMen/status/2066954311720972601) |
| x | Snapdragon | ^125 c15 | [The future of #XR is here. ​ ​Introducing #Snapdragon Reality Elite. Built to po](https://x.com/Snapdragon/status/2066930382172250173) |
| x | EmzyGadgets | ^125 c9 | [Person wey dey use iPhone Xr don swap to silver iPhone 17 pro max leave you with](https://x.com/EmzyGadgets/status/2066799091476992054) |
| x | TinaDebove | ^116 c29 | [Outside the XR bubble people will see this and say "ew". That's ok - these glass](https://x.com/TinaDebove/status/2067111796402467301) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@fwedesignerx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3917 · 💬 84</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/fwedesignerx/status/2066853665281864086">View @fwedesignerx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Bomb No collect loan Dress well Smell nice, even if na mousuf No give poor girl belle Avoid girls with Xr‼️ Lastly bomb ooo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แนะนำพฤติกรรมการจีบสาวในสไตล์สแลง คำว่า 'Xr' ในโพสต์นี้คือสแลง ไม่ใช่ Extended Reality</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/fwedesignerx/status/2066853665281864086" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rainmaker1973</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3704 · 💬 106</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Rainmaker1973/status/2066914531184406681">View @Rainmaker1973 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Birds can literally see the Earth’s magnetic field thanks to specialized light-sensitive proteins in their eyes. Migratory birds possess one of nature’s most remarkable superpowers: the ability to nav”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์วิทยาศาสตร์อธิบายว่านกอพยพอาจมองเห็นสนามแม่เหล็กโลกผ่านโปรตีน Cry4 โดยใช้ AR HUD เป็นอุปมาเท่านั้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Rainmaker1973/status/2066914531184406681" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SpatiallyMe</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1396 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SpatiallyMe/status/2066920677563666690">View @SpatiallyMe on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Shoutout to whoever at Apple came up with these beautiful animations that appear on Vision Pro when you scan your Persona. There is so much attention to detail throughout visionOS that it keeps me ver”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Vision Pro ชื่นชมความละเอียดของ animation ตอน scan Persona ใน visionOS และแสดงความเชื่อมั่นส่วนตัวว่า platform นี้ยังไปได้ไกล</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SpatiallyMe/status/2066920677563666690" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@justinryanio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1279 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/justinryanio/status/2066766077292318884">View @justinryanio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The new Siri AI on Apple Vision Pro is just so beautiful. I can’t stop staring at it. https://t.co/A9vFuGsATR”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้แสดงความประทับใจต่อ visual design ของ Siri AI ตัวใหม่บน Apple Vision Pro โดยไม่มีรายละเอียดทางเทคนิค</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>reaction นี้บอกว่า Apple ยก spatial UI bar บน visionOS ขึ้นอีกระดับ — ดูเป็น design reference สำหรับงาน XR interface ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ดู media ที่แนบมาแล้วจด Siri spatial UI pattern ไว้เป็น benchmark ตอน design interaction บน visionOS</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/justinryanio/status/2066766077292318884" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VRChat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1052 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VRChat/status/2066637523095363753">View @VRChat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NEW UPCOMING VRCHAT EVENT: Tanabata! This July 6-12, we'll be hosting a Tanabata (Star Festival) event in the Home world in VRChat! ⭐️What is Tanabata? Once a year, the two brightest summer stars in t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>VRChat จัด event วัฒนธรรมญี่ปุ่น Tanabata ในแพลตฟอร์ม 6–12 ก.ค. ผู้ใช้ส่ง wish ที่จะโชว์เป็น Tanzaku บนไม้ไผ่ใน Home world</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โมเดล seasonal event ของ VRChat แสดงให้เห็นว่า cultural moment ใน VR space ดึง engagement ได้ดี — pattern ที่เอาไปใช้ใน social VR project ของ studio ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า studio มี social VR หรือ XR project ลอง schedule cultural event ช่วงสั้น (เทศกาลไทยหรือภูมิภาค) เพื่อทดสอบ user-generated content loop</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VRChat/status/2066637523095363753" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SnazzyLabs</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 512 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SnazzyLabs/status/2067034411800101199">View @SnazzyLabs on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“At that point, just wear a Vision Pro.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ประโยคเดียวแนะนำให้ไปใช้ Apple Vision Pro แทน ไม่มีบริบท ไม่มีข้อมูล</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SnazzyLabs/status/2067034411800101199" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Android</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 508 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Android/status/2066928860415906081">View @Android on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Say hello to @XREAL_GLOBAL AURA ⚡️ ✅ Sleek, lightweight design ✅ Massive 70-degree FOV ✅ Powered by Android XR ✅ Built on the new @Snapdragon Reality Elite Platform ✅ Hands-free help from Gemini Reser”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>XREAL AURA คือ AR headset ตัวใหม่บน Android XR มี FOV 70 องศา, ชิป Snapdragon Reality Elite, และ Gemini AI แบบ hands-free — เปิด reserve สำหรับ fall แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Android XR มี hardware partner รายแรกที่ชัดเจน แสดงว่า platform ก้าวจาก dev preview มาเป็น deploy target จริงได้แล้วสำหรับ XR studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ควรเพิ่ม Android XR SDK และ Snapdragon Reality Elite ลง target-device list ตอน scope XR project ครั้งหน้า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Android/status/2066928860415906081" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VRChat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 463 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VRChat/status/2067004288845689306">View @VRChat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Amazing Low-Poly Worlds by @ShopowVR ! Check them out on VRChat! https://t.co/cJeFjOEiX2”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>VRChat official repost โชว์ผลงาน low-poly world ของ ShopowVR เป็น creator showcase ทั่วไป</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VRChat/status/2067004288845689306" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
