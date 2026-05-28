---
type: social-topic-report
date: '2026-05-27'
topic: xr
lang: th
pair: xr.en.md
generated_at: '2026-05-27T16:30:50+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- reddit
- x
regions:
- global
post_count: 38
salience: 0.7
sentiment: mixed
confidence: 0.7
tags:
- xr
- vision-pro
- meta-quest
- mixed-reality
- visionos
- haptics
thumbnail: https://pbs.twimg.com/media/HJPYOiDXMAAezNZ.jpg
translated_by: claude-sonnet-4-6
---

# XR / VR / AR — 2026-05-27

## TL;DR
- เรื่องเล่าของ Vision Pro ถูกครอบงำด้วยการเยาะเย้ย: DIY Persona clone ราคา $8 [7][8][15][17][30] และคอมเมนต์เสียดสีว่า 'ยังมีคนใช้อยู่อีกเหรอ?' [27]
- Meta Quest ยังคงเป็นเลเยอร์หลักของนักสร้างคอนเทนต์ที่ active — เกม launch [3][14][28][31][33], MR dev workflows [23][26][34], haptics [29]
- visionOS 26.6 beta ขนาดกว่า 9GB ปล่อยให้ devs แล้ว [12] — platform ยังพัฒนาต่อเนื่อง, ชิ้นส่วน SKU สีดำล้วน leak ออกมา [11]
- สัญญาณ medical XR ที่มีความหมายจริง: real-time CT/DICOM volume rendering บน Vision Pro โดยไม่มี downsampling [5]
- ชุมชนตัดสินว่า VR release slate ปี 2026 บางตัวมาก [22]; bimanual robotics + Quest ถูกนำไปใช้บนพื้นโรงงานจริง [2]

## What happened
วาทกรรมรอบ Vision Pro รอบนี้ส่วนใหญ่เป็นเรื่องชื่อเสียง: นักทำ maker ชาวญี่ปุ่นสร้าง badge ราคา $8 ที่จำลอง expression tracking แบบ Persona ได้ [7][30] ถูกขยายด้วยกระแส 'ผู้ชายใช้ webcam เอาชนะอุปกรณ์ที่ Apple ใช้เวลา 7 ปีและราคา $3,500' [8][17] โดยมีการโต้แย้งอย่างมีเหตุผลว่า clone นั้นเพียงเลียนแบบ expression เท่านั้น ไม่ได้รวม displays/compute/ecosystem [15] การเยาะเย้ยขยายไปถึง 'ยังมีคนใช้ Vision Pro อยู่อีกเหรอ?' [27] และมุกล้อเลียนผู้ซื้อรุ่น 1TB [9] ท่ามกลางเสียงรบกวนเหล่านี้ visionOS 26.6 beta ส่งถึง devs แล้ว (กว่า 9GB) [12], ชิ้นส่วน Vision Pro สีดำล้วนปรากฏขึ้น [11], และ use case ที่จริงจังก็ปรากฏขึ้นเช่นกัน — multi-gig DICOM/NIFTI volume rendering พร้อม hand-cut slicing [5], สารคดี immersive ของ Real Madrid [20], และการทดลอง Liquid Glass design [13]

Meta Quest รับบทบาทเลเยอร์การ ship/creator: แพตช์ Little Nightmares VR [3], WRATH brutal edition [14][28], Virtual Hunter launch [31], เกม MR จาก solo-dev [33], bridge ระหว่าง Houdini กับ hand-mocap [26], bHaptics TactGlove DK3 พร้อม 8 จุดที่ optimize สำหรับ Quest hand-tracking [29], และซีรีส์วิดีโอ Meta dev ที่อยู่ระหว่างการผลิต [23] ทีม robotics นำ Quest + dual 5090s ไปใช้งานบนพื้นโรงงานแห่งหนึ่งในโปแลนด์ [2] ความรู้สึกของชุมชนต่อ VR releases ปี 2026 คือ 'ไม่ค่อยดีนัก' จนถึงตอนนี้ [22]; มีม VRChat avatar economy ตอกย้ำวัฒนธรรมการใช้จ่ายใน social VR [1]

## Why it matters (reasoning)
สองเรื่องเล่าของ platform ที่แยกออกจากกัน hardware ของ Apple กำลังพัฒนาในเชิงเทคนิค (volume rendering [5], Personas [16], visionOS cadence [12]) แต่กำลังเสีย narrative ทางวัฒนธรรม — มีม badge $8 [7][8][30] สะท้อนให้เห็นการรับรู้ว่า moat ของ Vision Pro คือแบรนด์ ไม่ใช่ความสามารถ นั่นเป็นปัญหาของ content creator มากกว่าปัญหาวิศวกรรม: devs เผยแพร่บน platform ที่ผู้ใช้เยาะเย้ยน้อยกว่า Meta Quest ในทางกลับกันคือที่ที่ XR product ที่ ship จริง, MR tooling, และ peripheral ecosystem [29] อยู่ — ซึ่งเป็นที่ที่ momentum ที่เกี่ยวข้องกับ studio สะสมเพิ่มขึ้น second-order: medical/industrial XR ([5] DICOM, [2] factory robotics) เป็นสัญญาณว่า enterprise/vertical wedge มีความทนทานกว่า consumer entertainment ที่ slate ปี 2026 ถูกมองว่าอ่อนแอ [22]

## Possibility
มีแนวโน้ม (~70%): Quest ยังคงเป็น default shipping target สำหรับ indie/mid XR ตลอดปี 2026; Vision Pro ยังคงเป็น niche premium target สำหรับ vertical/enterprise (medical, sports, design) และ visionOS 26.x เพิ่ม developer affordances เป็นไปได้ (~35%): Apple launch SKU Vision Pro ราคาถูกกว่า/สีดำ [11] เพื่อ reset narrative — ช่วยเรื่อง mindshare แต่ไม่น่าจะพลิก platform share ต่ำ (~15%): VR title ที่ breakout ในปี 2026 reset ความรู้สึกของชุมชน [22]; ไม่เช่นนั้นการรวมตัวรอบ social VR (แบบ VRChat [1]) และ MR utility apps [33][34] จะดำเนินต่อไป

## Org applicability — NDF DEV
สำหรับ NDF DEV: ให้ Quest เป็น XR target หลัก — หลักฐานการ ship, MR tooling [26][34], haptics integration [29], และชุมชนที่ active ล้วนอยู่ที่นี่ Vision Pro คุ้มค่าสำหรับ secondary track เฉพาะกับ client ด้าน edutech/medical/heritage ที่ hardware premium มีความเหมาะสม — pattern ของ DICOM volume rendering [5] ถ่ายโอนได้โดยตรงไปยัง prototype e-learning ด้านกายวิภาค/วิทยาศาสตร์ Unity pipelines map ได้กับทั้งสองอย่างอย่างเป็นธรรมชาติ Persona/avatar tech [7][16] น่าสนใจแต่ไม่ใช่ core; ให้ถือเป็น R&D spike ไม่ใช่ roadmap pattern ของ Quest+robotics บนพื้นโรงงาน [2] บ่งชี้ถึง industrial training XR — เป็น adjacent service line ที่ viable หาก manufacturing client ปรากฏขึ้น ข้าม Vision Pro consumer entertainment bets ไปเลย; salience ต่ำเกินไป

## Signals to Watch
- visionOS 26.6 release notes — spatial/persistence APIs ใหม่ที่คุ้มค่าสำหรับการสแกน [12]
- ความพร้อมของ bHaptics TactGlove DK3 SDK สำหรับ Quest hand-tracking integration [29]
- ว่า Vision Pro SKU สีดำ/ราคาถูกกว่า [11] จะ ship จริงในปี 2026 หรือไม่
- เนื้อหาของ Meta dev video series [23] — เป็นสัญญาณว่า Meta ต้องการให้ devs มุ่งเน้นที่อะไรต่อไป

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | VRChat | ^4695 c142 | [never let anyone talk you out of spending $35 on VRChat avatars, that $120 will ](https://x.com/VRChat/status/2058946648575815826) |
| x | DominiqueCAPaul | ^570 c36 | [We're off to Poland where we'll be spending the week working from an electronic ](https://x.com/DominiqueCAPaul/status/2059227207365435487) |
| x | LittleNights | ^391 c20 | [A new patch has been released for #LittleNightmares VR: Altered Echoes on PC, PS](https://x.com/LittleNights/status/2059208197471130071) |
| x | QuantumArjun | ^346 c47 | [Very bittersweet, but I'm leaving Apple. Anyone who knows me knows how much I ad](https://x.com/QuantumArjun/status/2059343737873223795) |
| x | ElasticSea | ^135 c6 | [Pick up a CT scan with your hands and cut straight through it. Real-time volume ](https://x.com/ElasticSea/status/2059291940147888584) |
| x | NathieVR | ^131 c4 | [Who's going to tell him about Apple Vision Pro?](https://x.com/NathieVR/status/2059342367769993358) |
| x | RoundtableSpace | ^131 c20 | [A JAPANESE MAKER RECREATED APPLE VISION PRO PERSONAS WITH AN $8 DIY BADGE AND PE](https://x.com/RoundtableSpace/status/2059178975902261633) |
| x | sairahul1 | ^102 c12 | [Apple spent 7 years and $3,500 per unit building Vision Pro, this guy did someth](https://x.com/sairahul1/status/2059563188644192419) |
| x | mil000 | ^101 c5 | [Imagine being one of the people who got the max storage 1TB Vision Pro in 2024 h](https://x.com/mil000/status/2059387435101106426) |
| x | MetaQuestVR | ^101 c3 | [Postseason highlights are immersive on Meta Quest on Horizon TV. Courtside energ](https://x.com/MetaQuestVR/status/2059312634005196820) |
| x | MacRumors | ^78 c4 | [More All-Black Apple Vision Pro Parts Surface Online https://t.co/oMy8gblwfw htt](https://x.com/MacRumors/status/2059523834253087008) |
| x | spatialinsider | ^76 c0 | [visionOS 26.6 Beta is now available for developers on Apple Vision Pro. Over 9 G](https://x.com/spatialinsider/status/2059605610803392527) |
| x | rolandsmeenk | ^71 c0 | [What if earth was made of Liquid Glass? Apple Vision Pro experiment with using f](https://x.com/rolandsmeenk/status/2059223771345494362) |
| x | Flat2VRStudios | ^69 c5 | [This is your reminder that @Wrath_VR is out now, and the arsenal is not here to ](https://x.com/Flat2VRStudios/status/2059321267640057952) |
| x | JohnRomant | ^67 c4 | [@0xDezo Not really. The Japanese maker only replicated expression-tracking, but ](https://x.com/JohnRomant/status/2059019155467305216) |
| x | nandoprince93 | ^56 c2 | [Vision Pro Personas have gotten so good over the last few years. The jump from t](https://x.com/nandoprince93/status/2059263739480715551) |
| x | vicky_grok | ^49 c4 | [Apple spent 7 years and $3,500 per unit building Vision Pro, this guy did someth](https://x.com/vicky_grok/status/2059612718949400921) |
| x | SweetCornSeason | ^49 c1 | [@RyDawg42 Looks more like the Vision Pro battery https://t.co/nJPfiFZrze](https://x.com/SweetCornSeason/status/2058947038696382786) |
| x | Leodav_art | ^43 c0 | [[VR Graffiti] ATEEZ 'Adrenaline': Massive Red Tagging Overwhelming a Virtual Sub](https://x.com/Leodav_art/status/2059657499230531961) |
| x | hughhoufilm | ^40 c5 | [I finally sat down with Real Madrid: The Weight of Greatness on Apple Vision Pro](https://x.com/hughhoufilm/status/2059396385666134411) |
| x | lvl80waifu | ^40 c10 | [does anyone play Meta Quest? I'm picking it back up and I'm pretty bored being a](https://x.com/lvl80waifu/status/2059213770186985710) |
| reddit | SlowDragonfruit9718 | ^38 c25 | [My top 5 VR releases of 2026... So far. In my opinion, 2026 hasn't been great wi](https://www.reddit.com/r/virtualreality/comments/1toig4m/my_top_5_vr_releases_of_2026_so_far/) |
| x | Dilmerv | ^34 c1 | [I worked on a new Meta dev video series this weekend, which should be released o](https://x.com/Dilmerv/status/2059287023287161101) |
| x | snoopyatv | ^33 c1 | [Any excuse to wear his Meta Quest https://t.co/vzaGA9RHn1](https://x.com/snoopyatv/status/2059030713777750168) |
| x | yacineMTB | ^32 c2 | [@PINTO03091 i mean eyeball tracking. there are likely apis you can use with the ](https://x.com/yacineMTB/status/2059281193120432152) |
| x | Jose_Molfino | ^31 c0 | [@J_Scott_Art Sorry mate! It's a hand mocap bridge between Meta Quest 3 headset a](https://x.com/Jose_Molfino/status/2059232437708714443) |
| x | theonecid | ^30 c3 | [Wait people still use the vision pro??](https://x.com/theonecid/status/2059617620630937640) |
| x | Wrath_VR | ^30 c1 | [Classic shooter energy. Pure VR brutality. WRATH: Aeon of Ruin VR - Brutal Editi](https://x.com/Wrath_VR/status/2059328053000430057) |
| x | bhaptics | ^28 c4 | [Meet our new haptic glove🖐️ — TactGlove DK3 8 haptic points — fingertips, palm &](https://x.com/bhaptics/status/2059600717716099495) |
| x | Radha_AI | ^24 c0 | [APPLE JUST GOT HUMILIATED BY AN $8 JACKET BADGE. Apple spent years building Pers](https://x.com/Radha_AI/status/2059179124024127532) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VRChat</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4695 · 💬 142</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VRChat/status/2058946648575815826">View @VRChat on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“never let anyone talk you out of spending $35 on VRChat avatars, that $120 will be the greatest $550 you ever spend in your life”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>VRChat ล้อเลียนตัวเองว่าการซื้อ avatar บานปลายไม่หยุด จาก $35 กลายเป็น $550 และ user ก็ไม่เสียใจ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โพสต์นี้แสดงว่า VRChat economy แข็งแกร่ง user ยินดีจ่ายหนักเพื่อ virtual identity — avatar monetization ได้รับการพิสูจน์แล้วในตลาดจริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ควรออกแบบ avatar customization และ cosmetic upgrade loop ตั้งแต่ต้น — user พิสูจน์แล้วว่าจ่ายเพื่อ virtual identity โดยไม่ต้องโน้มน้าวมาก</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VRChat/status/2058946648575815826" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DominiqueCAPaul</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 570 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DominiqueCAPaul/status/2059227207365435487">View @DominiqueCAPaul on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We‘re off to Poland where we‘ll be spending the week working from an electronic factory floor. With us: two 5090 workstations, two bimanual arm setups, a Meta Quest, spare 3D parts and tools. https://”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีมนึงไปทำงาน on-site ที่โรงงานอิเล็กทรอนิกส์ในโปแลนด์ทั้งอาทิตย์ พร้อม workstation RTX 5090 สองเครื่อง, bimanual robot arm สองชุด, และ Meta Quest</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การจับคู่ Meta Quest กับ bimanual robot arm บน factory floor แสดงให้เห็น pipeline จาก VR สู่ hardware จริงที่ทีม XR เล็กๆ ทำตามได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ลองใช้ Meta Quest เป็น controller สำหรับ teleoperation หรือ simulation การฝึกอบรมแทน controller ราคาแพงใน prototype ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DominiqueCAPaul/status/2059227207365435487" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LittleNights</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 391 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LittleNights/status/2059208197471130071">View @LittleNights on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A new patch has been released for #LittleNightmares VR: Altered Echoes on PC, PSVR2, and Meta Quest, bringing heavily requested features: - Smooth turning option - Hood removal option (PC only, due to”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Little Nightmares VR: Altered Echoes ปล่อย patch บน PC, PSVR2, และ Meta Quest เพิ่ม smooth turning, hood removal (PC only), และแก้ gameplay/visual ทั่วไป</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การล็อก hood removal ไว้แค่ PC เพราะ performance แสดงให้เห็นว่า VR cross-platform ต้องจัดการ feature gating ต่อ hardware จริงจัง — ความท้าทายตรงสำหรับทีมที่ ship หลาย platform พร้อมกัน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity XR ควรวาง feature-gating strategy ตั้งแต่ design phase — tag ว่า feature ไหน PC/Quest/PSVR2-only เลย ไม่ใช่รอแก้ตอน patch เพื่อลด rework ข้าม platform build</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LittleNights/status/2059208197471130071" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@QuantumArjun</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 346 · 💬 47</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/QuantumArjun/status/2059343737873223795">View @QuantumArjun on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Very bittersweet, but I'm leaving Apple. Anyone who knows me knows how much I admire Apple's story and ethos. The iPhone captured my imagination as a kid, and never let go. And getting to spend the ea”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักออกแบบ interface ของ Vision Pro ลาออกจาก Apple แชร์บทเรียน: ออกแบบรอบ 'magic moment' จุดเดียวที่ชนะใจคน และให้ research กับ product ทำงานในห้องเดียวกัน ไม่ใช่ส่งต่อกัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เกณฑ์ 'ร่างกายเชื่อก่อนสมอง' ให้ทีม XR มีตัวชี้วัด immersion ที่ทดสอบได้จริง ดีกว่า UX heuristic ทั่วไปมาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/Unity ควร prototype หา magic moment หนึ่งจุดต่อ experience ก่อนสร้าง feature รอบนอก และดึง research findings เข้า sprint planning แทนการทำแบบ handoff ก่อนเริ่ม build</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/QuantumArjun/status/2059343737873223795" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ElasticSea</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 135 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ElasticSea/status/2059291940147888584">View @ElasticSea on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Pick up a CT scan with your hands and cut straight through it. Real-time volume rendering on Apple Vision Pro (NIFTI/DICOM, multi-gig, no downsampling). https://t.co/BzXp1N9Cwl”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev demo real-time volumetric rendering ของ CT scan ความละเอียดเต็ม (NIFTI/DICOM, หลาย GB) บน Apple Vision Pro พร้อม hand tracking จับและตัดผ่านได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Volumetric rendering ไม่ลด resolution บน XR hardware ตัวเดียวพิสูจน์ว่า medical-grade spatial computing ทำได้จริงแล้ว ไม่ใช่แค่แนวคิด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ใช้ approach นี้เป็น benchmark สำหรับ simulation หรือ training content ที่ต้องการ interact กับ 3D data ความละเอียดสูงใน headset โดยไม่ต้องพึ่ง server</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ElasticSea/status/2059291940147888584" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NathieVR</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 131 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NathieVR/status/2059342367769993358">View @NathieVR on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Who's going to tell him about Apple Vision Pro?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ถามประชด — มีคนพูดเรื่อง VR/XR โดยไม่รู้ว่า Apple Vision Pro มีอยู่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Apple Vision Pro กลายเป็น baseline ของวง XR แล้ว — พูดเรื่อง XR โดยไม่กล่าวถึงมันถูก call out ทันที</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ควร benchmark pitch หรือ prototype ทุกชิ้นเทียบกับ interaction model ของ AVP ไว้ก่อน แม้จะ target hardware ราคาถูกกว่า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NathieVR/status/2059342367769993358" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RoundtableSpace</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 131 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RoundtableSpace/status/2059178975902261633">View @RoundtableSpace on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A JAPANESE MAKER RECREATED APPLE VISION PRO PERSONAS WITH AN $8 DIY BADGE AND PEOPLE ARE SAYING IT LOOKS SHOCKINGLY SIMILAR https://t.co/NlLmYWFCsF”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักทำ DIY ชาวญี่ปุ่นสร้าง Persona avatar แบบเดียวกับ Apple Vision Pro ด้วย badge ราคา $8 และผลลัพธ์ดูใกล้เคียงมากจนคนตกใจ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ฟีเจอร์ Persona streaming ที่ Apple ใช้ขาย Vision Pro ถูก replicate ด้วย hardware แทบฟรี ตั้งคำถามกับ value ของ headset ราคาแพง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ลอง prototype avatar/face-presence ใน VR experience ด้วย hardware ราคาถูกก่อน แทนที่จะรอ sensor แพงๆ — validate UX ก่อน แล้วค่อย upgrade</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RoundtableSpace/status/2059178975902261633" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sairahul1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 102 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sairahul1/status/2059563188644192419">View @sairahul1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple spent 7 years and $3,500 per unit building Vision Pro, this guy did something better with a webcam in his bedroom. And no, this isn't a render, it's running live on his laptop right now with a w”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาคนหนึ่งสร้าง hand tracking แบบ real-time 21 จุดต่อมือที่ 60fps พร้อม cloth simulation ผูกกับ 3D skeleton โดยใช้แค่ webcam กับ TouchDesigner ไม่ต้องใช้ headset หรือ glove เลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>พิสูจน์ว่า XR hand interaction คุณภาพ production ทำได้โดยไม่ต้องลงทุน hardware — ต้นทุนต่ำลงมาก ตอนนี้ barrier คือ skill ล้วนๆ ไม่ใช่ device ราคาแพง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ใช้ TouchDesigner prototype bare-hand interaction ก่อน commit เข้า Unity + SDK ได้เลย — ส่ง 21-point tracking จาก MediaPipe เข้า Unity ผ่าน OSC หรือ WebSocket สำหรับ demo pitch ต้นทุนต่ำ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sairahul1/status/2059563188644192419" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
