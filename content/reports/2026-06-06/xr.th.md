---
type: social-topic-report
date: '2026-06-06'
topic: xr
lang: th
pair: xr.en.md
generated_at: '2026-06-06T15:33:48+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 102
salience: 0.4
sentiment: mixed
confidence: 0.5
tags:
- android-xr
- vision-pro
- meta-quest
- gaussian-splatting
- hand-tracking
- spatial-computing
thumbnail: https://pbs.twimg.com/media/HKEKEjwWwAA6d0V.jpg
translated_by: claude-sonnet-4-6
---

# XR / VR / AR — 2026-06-06

## TL;DR
- Android XR กำลังรวมศูนย์: XREAL's Project Aura และ Samsung's Galaxy XR ต่างรันบน Android XR platform เดียวกันพร้อม Gemini ที่ผสานอยู่ภายใน เปิดตัวที่ Google I/O และ CVPR 2026 [26][40]
- Meta Quest เพิ่มฟีเจอร์แปลงพื้นผิวแบนใดก็ได้ให้เป็น virtual keyboard ผ่าน passthrough/hand tracking [8]
- Apple Vision Pro ครบรอบ 3 ปีนับแต่ประกาศตัว พร้อมการวางตำแหน่งด้าน spatial computing ต่อเนื่อง และมุมมองเบื้องหลัง Apple Immersive Video production pipeline [16][19][30][34][42]
- สัญญาณฝั่ง content tooling: แก้ไข Gaussian splat ภายใน VR (SplatBox, controller brush) [20] และปั้น virtual clay ด้วย hand tracking ไร้ controller ใน Three.js [31]
- รายการ 'XR' ที่ engagement สูงส่วนใหญ่เป็น noise — ข่าว iPhone XR [1][11][14][22][23][27][36][53][55], hashtag K-pop [2][3], และ NSFW VR spam [21][24][35][44] — ไม่ใช่ข่าวแพลตฟอร์ม XR

## สิ่งที่เกิดขึ้น
feed XR วันนี้ถูกครอบงำด้วย engagement ที่ไม่เกี่ยวข้อง: สมาร์ตโฟน iPhone XR [1][11][14][22][23][27][36][53][55], การเล่นคำ 'XR'/'Vision Pro' ในแวดวง K-pop [2][3], สถิติ MMA 'xR' [41], และโปรโมต adult VR [21][24][35][44] เมื่อกรองออก สัญญาณแพลตฟอร์มที่มีสาระ ได้แก่: Android XR convergence — XREAL's Project Aura และ Samsung's Galaxy XR รันบน Android XR build เดียวกันพร้อม Gemini เดโมที่ Google I/O และบูธ CVPR 2026 #557 [26][40]; ฟีเจอร์ใหม่ของ Meta Quest ที่ map virtual keyboard ลงบนพื้นผิวแบนใดก็ได้ [8]; และครบรอบ 3 ปีที่ Apple Vision Pro เปิดตัว ควบคู่กับ commentary ด้าน spatial computing และการเล่าเบื้องหลังการถ่าย Apple Immersive Video จาก The Spatial Gen [16][19][30][34][42]

## เหตุใดจึงสำคัญ
เทรนด์ที่ชัดที่สุดคือขอบเขตระหว่าง AR/MR/VR กำลังเลือนภายใต้ OS เดียว: ผู้ทดสอบรายงานว่าช่องว่างระหว่าง AR/VR 'กำลังพังทลาย' เพราะอุปกรณ์ฟอร์ม glasses (Aura) และ headset (Galaxy XR) ใช้ Android XR กับ Gemini ร่วมกัน [26] สำหรับสตูดิโอที่กำลังเลือก platform วางขาย runtime บน Android ที่ข้ามหลาย OEM ช่วยลดต้นทุนการ port ต่ออุปกรณ์เทียบกับการดูแล Quest build กับ visionOS build แยกกัน — แต่เงื่อนไขคือ SDK และ store fragmentation ต้องจัดการได้ ซึ่งโพสต์เหล่านี้ยังไม่ยืนยัน ธีมที่สองคือ input: surface keyboard ของ Meta [8] และ hand tracking ไร้ controller [31] ชี้ให้เห็น interaction model ที่ไม่พึ่ง controller ซึ่งสำคัญต่อ edutech หรือ XR UX ที่การส่ง controller ให้ผู้ใช้สร้างแรงต้าน การแก้ไข Gaussian splatting ใน headset [20] และการ capture พิพิธภัณฑ์ของ OVRtheReality [15] แสดงให้เห็นว่า asset pipeline (capture → edit → deliver) กำลังสุกงอมขึ้น ซึ่งสำคัญต่อ XR content studio มากกว่าการแข่ง spec ของ headset โพสต์วันครบรอบของ Apple เป็นแค่ sentiment ไม่ใช่ข่าว — สามปีผ่านไป คำถามเปิดว่าใครจะซื้อ Vision Pro ยังคงไร้คำตอบ [19]

## ความเป็นไปได้
น่าจะเกิด: Android XR รวม OEM หลายรายต่อไป (Samsung, XREAL) บน runtime เดียว เมื่อมีสองผลิตภัณฑ์แยกกันที่ใช้ร่วมกันอยู่แล้ว [26][40] เป็นไปได้: controller-free input (surface keyboard, hand tracking) กลายเป็น baseline ข้ามอุปกรณ์ระดับ Quest เมื่อ capability นี้ shipping อยู่แล้ว [8][31] เป็นไปได้: tooling capture/edit Gaussian splat กลายเป็นส่วนมาตรฐานของ immersive content workflow เมื่อ editor ใน headset เริ่มปรากฏ [15][20] ไม่น่าเกิด (จากหลักฐานนี้): การทะลุตลาดผู้บริโภคของ Vision Pro ในระยะใกล้ — รายการเหล่านี้คือ retrospective ครบรอบและคำถาม 'ต้องอะไรถึงจะซื้อ' ที่ยังค้างคา ไม่ใช่สัญญาณอุปสงค์ [19][30][42] ไม่มีแหล่งใดระบุตัวเลขพยากรณ์

## การนำไปใช้สำหรับ NDF DEV
1) ติดตาม Android XR เป็น delivery target สำหรับ Unity/XR practice — runtime เดียวครอบ Galaxy XR + XREAL glasses อาจลดการ port หลายอุปกรณ์ และ Gemini on-device เกี่ยวข้องกับ edutech assistant [26][40] (effort: med ในการประเมิน, high ในการ port) 2) Prototype controller-free interaction (hand tracking, surface input) สำหรับ demo e-learning/XR ที่ controller เพิ่ม onboarding friction [8][31] (effort: low-med, Unity hand-tracking พร้อมใช้แล้ว) 3) Pilot Gaussian splatting capture สำหรับ heritage/edu content — การ mapping พิพิธภัณฑ์ [15] และการแก้ splat ใน VR [20] ตรงกับ edutech และโปรเจกต์แหล่งวัฒนธรรมที่สตูดิโอเชียงใหม่สามารถ pitch ได้ (effort: med) 4) สำหรับงาน Vision Pro immersive video ใดๆ ให้จดต้นทุน specialized capture pipeline ที่ The Spatial Gen ระบุไว้ก่อน quote [34] (effort: low — เฉพาะ scoping) ข้าม: โพสต์ community/event VRChat [4][7][10][33][59][60], ข่าว iPhone XR, noise K-pop/MMA 'XR', และ NSFW VR — ไม่มี signal ที่ใช้งานได้

## สัญญาณที่ต้องจับตา
- Android XR เพิ่ม OEM ต่อเนื่องหรือไม่ และ SDK/store fragmentation จัดการได้แค่ไหน [26][40]
- ความสุกงอมของ in-headset Gaussian splat editing tool (SplatBox) ในฐานะ production content path [20]
- การนำ controller-free input มาเป็น default บนอุปกรณ์ระดับ Quest [8][31]
- ต้นทุนและการเข้าถึง Apple Immersive Video capture pipeline สำหรับสตูดิโอขนาดเล็ก [34]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | kobe_boujee88 | ^1286 c21 | [I still use Xr and people don't believe that 😂](https://x.com/kobe_boujee88/status/2062560998515454222) |
| x | DragonKazoo77 | ^763 c0 | [260605 it'slive YT/IG [Static XR💚it's Live] MAMAMOO's "4 Flowers" Right Before Y](https://x.com/DragonKazoo77/status/2062941132921684401) |
| x | FY_orai | ^387 c0 | [wooyoung voice cracked a little while singing and of course san caught it becaus](https://x.com/FY_orai/status/2063127924383883750) |
| x | VRChat | ^379 c22 | [We hit our $100k goal for Trans Lifeline! Thank you to everyone who contributed ](https://x.com/VRChat/status/2063045329738453393) |
| x | GoogleDesign | ^301 c3 | [Everything we announced at #GoogleIO, wrapped up in one blog post! Get up to spe](https://x.com/GoogleDesign/status/2062565039023002021) |
| x | anishmoonka | ^267 c6 | [The same man who built Disney's real extendable lightsaber and taught the ghost ](https://x.com/anishmoonka/status/2062625436572496031) |
| x | VRChat | ^256 c7 | [Beat the Heat this summer: Introducing a new Shop update! Available until Aug 7 ](https://x.com/VRChat/status/2063006744029098263) |
| x | NathieVR | ^247 c29 | [On Meta Quest you can now transform any flat surface into a virtual keyboard. We](https://x.com/NathieVR/status/2062601609176060235) |
| x | jasonfried | ^239 c29 | [All these wackadoodle valuations reminded me of a press release we put out in 20](https://x.com/jasonfried/status/2062618581301645552) |
| x | VRChat | ^232 c17 | [No Dev Update this week! We're pushing it back to next week instead. See you the](https://x.com/VRChat/status/2062623525261771121) |
| x | Arnoldruski | ^226 c15 | [Una never clock am say iPhone 11 actually worst pass Xr](https://x.com/Arnoldruski/status/2062893404741063037) |
| x | privatetalky | ^219 c2 | [9 years ago today at WWDC17, Apple announced: - iOS 11, with a redesigned Contro](https://x.com/privatetalky/status/2062874013978841095) |
| x | BeastOfTruth | ^169 c10 | [XBOX's problem is that they are too afraid to call out or challenge Sony directl](https://x.com/BeastOfTruth/status/2062941342662094875) |
| x | iconredesign | ^161 c7 | [The iPhone XR isn't the last flagship iPhone (the R literally stands for "Reach,](https://x.com/iconredesign/status/2062830628140445840) |
| x | OVRtheReality | ^156 c24 | [A museum in France. Accessible from anywhere in the world. One of our mappers ca](https://x.com/OVRtheReality/status/2062898739627393509) |
| x | justinryanio | ^132 c7 | [Some don't understand Apple Vision Pro and the path we're on. Spatial computing ](https://x.com/justinryanio/status/2062935322636562847) |
| x | BillionMagazine | ^123 c2 | [When Austrian precision meets hypercar drama: The X-Bow GT-XR in its natural hab](https://x.com/BillionMagazine/status/2062642173036659141) |
| x | soleilestelle | ^120 c8 | [does anybody who uses Warudo know why the mediapipe tracking within the program ](https://x.com/soleilestelle/status/2062667253883998422) |
| x | aaronp613 | ^118 c23 | [Apple unveiled the Vision Pro 3 years ago today. What would it take for you to b](https://x.com/aaronp613/status/2062856292134166876) |
| x | DSkaale | ^118 c2 | [SplatBox GPU editing — now in VR What works today! Controller-aimed brush — Red ](https://x.com/DSkaale/status/2062888323551498507) |
| x | OliviaSparkleXX | ^111 c0 | [🔞‼️Do you prefere me "soft glamour" or having hardcore sex...? 😜 . My channels: ](https://x.com/OliviaSparkleXX/status/2062601504356188642) |
| x | Flowkeei | ^110 c49 | [iPhone 18 is going to be out and someone is still holding XR. 🌚louder ? Or make ](https://x.com/Flowkeei/status/2063198714571764100) |
| x | Esmart26 | ^108 c43 | [Who dey use iPhone XR fit go back to button phone, no time for motivation](https://x.com/Esmart26/status/2062600885402788202) |
| x | liltimmydsf | ^108 c1 | [I get bored of being punished in my room and I play with augmented reality and @](https://x.com/liltimmydsf/status/2062557644557062149) |
| x | maximzhestkov | ^95 c13 | [Building new spatial experiences for Apple Vision Pro with my team @fun_and_awe.](https://x.com/maximzhestkov/status/2063167740320326068) |
| x | CasandChary | ^92 c11 | [I tried XREAL's Project Aura at Google I/O and walked away convinced the AR/VR d](https://x.com/CasandChary/status/2062639514204635293) |
| x | UrglyGramm | ^91 c16 | [U wey still dey use XR since 2019, low budget $20 hookup boy😂](https://x.com/UrglyGramm/status/2063217929596891446) |
| x | GabRoXR | ^86 c4 | [This is your chance to know everything about these masterpieces. Drop your quest](https://x.com/GabRoXR/status/2062565043871666273) |
| x | SantoXBT | ^82 c56 | [I use virtual reality to escape this sad reality 😭 https://t.co/XbMtPAxRem](https://x.com/SantoXBT/status/2062904779123134767) |
| x | tgod34748 | ^79 c1 | [3 years ago today, Apple Vision Pro was introduced. https://t.co/fAL8Mof5AO](https://x.com/tgod34748/status/2062889680308203835) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@kobe_boujee88</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1286 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/kobe_boujee88/status/2062560998515454222">View @kobe_boujee88 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I still use Xr and people don’t believe that 😂”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้รายหนึ่งพูดเล่นๆ ว่ายังใช้ XR อยู่ ไม่มีรายละเอียดทางเทคนิคหรือ insight ใดเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/kobe_boujee88/status/2062560998515454222" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DragonKazoo77</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 763 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DragonKazoo77/status/2062941132921684401">View @DragonKazoo77 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“260605 it'slive YT/IG [Static XR💚it's Live] MAMAMOO's &quot;4 Flowers&quot; Right Before Your Eyes🎵 🔗https://t.co/bXzZde2tuo #MAMAMOO #4WARD #4Flowers #SOLAR #솔라 #MOONBYUL #문별 #WHEEIN #휘인 #HWASA #화사 #마마무 https:”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แอคเคาท์แฟนคลับโพสต์ลิงก์ MV MAMAMOO '4 Flowers' แท็ก 'Static XR' — ไม่มีเทคโนโลยี XR จริงในโพสต์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DragonKazoo77/status/2062941132921684401" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@FY_orai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 387 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/FY_orai/status/2063127924383883750">View @FY_orai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“wooyoung voice cracked a little while singing and of course san caught it because hes literally mr wooyoung tunnel vision pro max. the way they looked at each other and immediately started laughing th”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แฟนคลับเล่าช่วงเวลา on-stage ของสมาชิก ATEEZ ไม่มีเนื้อหาด้านเทคโนโลยีใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/FY_orai/status/2063127924383883750" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VRChat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 379 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VRChat/status/2063045329738453393">View @VRChat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We hit our $100k goal for Trans Lifeline! Thank you to everyone who contributed VRC+ gifts over this week! We couldn't have done it without you 💙 As a reminder, the Pride event is ongoing until the en”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>VRChat ระดมทุนครบ $100k ให้ Trans Lifeline ผ่านระบบ gifting ใน VRC+ โดย Pride event ยังดำเนินต่อถึงสิ้นเดือนมิถุนายน 2026</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VRChat/status/2063045329738453393" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GoogleDesign</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 301 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GoogleDesign/status/2062565039023002021">View @GoogleDesign on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Everything we announced at #GoogleIO, wrapped up in one blog post! Get up to speed on our shift from Material Views to Jetpack Compose, as well as our new expressive layout guidelines, adaptive spacin”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google Design รวม recap ของ Google I/O ไว้ในโพสต์เดียว ครอบคลุม Material Views → Jetpack Compose, layout guidelines แบบ expressive, adaptive spacing, และ design guidance สำหรับ Wear OS และ XR</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Google XR design guidance ฉบับใหม่เป็น reference หลักของ first-party สำหรับ spatial UI บน Android XR ที่ทีม XR ใช้อ้างอิงได้เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR อ่านส่วน XR ใน recap นี้ แล้ว align prototype บน Android XR ให้ตรง spatial design guidelines ใหม่ก่อน finalize UI</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GoogleDesign/status/2062565039023002021" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@anishmoonka</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 267 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/anishmoonka/status/2062625436572496031">View @anishmoonka on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The same man who built Disney's real extendable lightsaber and taught the ghost in the Haunted Mansion to float spent nearly seven years on something far stranger. A floor you can walk across forever ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>HoloTile floor ของ Lanny Smoot (Disney) ใช้จานหมุนอิสระหลายร้อยอัน ดึงผู้ใช้กลับจุดกึ่งกลางขณะเดิน รองรับหลายคน ไม่ต้องใส่ harness แก้ปัญหา locomotion ใน VR</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เดินใน VR ได้จริงแบบไม่มี harness รองรับหลายคน ตัดข้อจำกัดหลักของ location-based XR และแก้ปัญหา thumbstick sickness</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม HoloTile ว่าพร้อม deploy เมื่อไร แล้วออกแบบ location-based XR ต่อไปโดยใช้ free-walking เป็น baseline แทน teleport</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/anishmoonka/status/2062625436572496031" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VRChat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 256 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VRChat/status/2063006744029098263">View @VRChat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Beat the Heat this summer: Introducing a new Shop update! Available until Aug 7 2026. https://t.co/iBIKU4koEy”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>VRChat ออก Shop update ตามฤดูกาล 'Beat the Heat' มี avatar และ item ใหม่ เปิดถึง 7 ส.ค. 2026</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VRChat/status/2063006744029098263" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NathieVR</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 247 · 💬 29</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NathieVR/status/2062601609176060235">View @NathieVR on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“On Meta Quest you can now transform any flat surface into a virtual keyboard. We truly live in the future. https://t.co/YHCdDaS792”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Meta Quest ฉาย virtual keyboard บนพื้นผิวแบนใดก็ได้ พิมพ์ด้วยมือโดยไม่ต้องใช้ controller หรือคีย์บอร์ดจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เพิ่มช่องทาง text input ที่ใช้งานได้จริงใน Quest apps — ตรงกับโปรเจกต์ XR ที่มี search, login form หรือ in-headset chat</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">XR team ตรวจ Quest builds ที่มี text input อยู่ แล้วประเมินว่าเปลี่ยนมาใช้ surface keyboard แทน controller ได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NathieVR/status/2062601609176060235" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
