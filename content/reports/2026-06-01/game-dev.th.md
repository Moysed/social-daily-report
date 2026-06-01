---
type: social-topic-report
date: '2026-06-01'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-01T03:57:10+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 13
salience: 0.25
sentiment: neutral
confidence: 0.6
tags:
- unity
- shaders
- open-source
- indiedev
- tooling
- vfx
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2060606108763295745/img/-oeMxhDSxmtuOXkf.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-01

## TL;DR
- Developer thesquirrelyjones ปล่อย Unity character controller open-source รองรับ moving platforms และ wall collisions [1]
- แชร์ shader breakdown ที่นำไปใช้ได้ทันที 2 ชิ้น: node setup เอฟเฟกต์หยดฝน (Unity HDRP, port ไป Unreal ได้) [2] และ stylized liquid shader ใช้ Shader Graph vertex-painted flow maps [9]
- Unity-retention sentiment ยังคงอยู่: creator รายหนึ่งเผยแพร่ 'why I won't quit Unity' ท่ามกลางแรงกดดันให้ย้ายออก [12]
- ที่เหลือเป็น #ScreenshotSaturday showcase ของ indie (VFX, low-poly assets, demo แนว horror/FPS/RPG) ไม่มีข่าว engine, tooling, หรือ pipeline [3][4][5][6][8][10][11][13]

## สิ่งที่เกิดขึ้น
สัญญาณ Game Dev วันนี้ถูกครอบงำด้วยการแชร์ asset และเทคนิคจากชุมชน ไม่ใช่ข่าวจาก vendor หรือ release ใหม่ รายการที่ engagement สูงสุดคือ Unity character controller open-source ที่สร้างมาเพื่อจัดการ edge case อย่าง moving platforms และ wall collisions [1] มี shader breakdown เผยแพร่ 2 ชิ้น: node graph เอฟเฟกต์หยดฝนใน Unity HDRP โดยผู้เขียนระบุว่า port ไป Unreal ได้ ยกเว้นความต่างของ mask map ใน HDRP [2] และ stylized liquid shader ที่ใช้ Shader Graph ร่วมกับ vertex-painted flow maps เพื่อกำกับทิศทางการไหลบนพื้นผิว [9] นอกจากนี้ยังมี creator โพสต์วิดีโอ 'why I won't quit Unity' ท่ามกลางกระแสเรียกร้องให้ย้ายออกจาก engine [12]

## เหตุใดจึงสำคัญ
Controller open-source [1] และ shader walkthrough สองชิ้น [2][9] นำไปใช้งานใน Unity production ได้โดยตรง — ตรงกับ stack URP/HDRP และ Shader Graph ที่ NDF DEV ใช้อยู่ — และโน้ตเรื่อง Unreal portability ใน [2] ลดต้นทุนการย้าย effect ระหว่าง engine กระแส Unity-exit discourse [12] เป็น sentiment signal ที่อ่อนแต่ปรากฏซ้ำ: ความกังวลเรื่องการเลือก engine ยังเป็นประเด็นที่คุกรุ่น ซึ่งมีนัยสำหรับ studio ที่กำลัง standardize บน Unity ส่วนโพสต์ #ScreenshotSaturday จำนวนมาก [3][4][5][6][8][10][11][13] ขับเคลื่อนด้วย self-promotion เป็นหลัก ไม่ใช่ความเคลื่อนไหวจริงใน engine, tooling, หรือ AI pipeline

## ความเป็นไปได้
**Likely:** controller และ shader breakdown open-source จากรายบุคคลจะทยอยออกมาเรื่อยๆ เพราะนี่คือ steady-state ของ indie Unity community [1][2][9] **Plausible:** ดีเบต Unity กับทางเลือกอื่นจะดำเนินต่อเป็นระยะโดยไม่มี trigger ชัดเจนในวันนี้ [12] **Unlikely:** โพสต์เดี่ยวใดๆ จะส่งสัญญาณถึงการเปลี่ยนแปลงระดับ engine หรือ tooling — ในชุดนี้ไม่มี vendor announcement, release, หรือรายการ AI pipeline ใดที่จะสนับสนุนข้อสรุปนั้น

## การประยุกต์ใช้ — NDF DEV
ประเมิน open-source character controller [1] สำหรับ prototype หรือ jam project เพื่อไม่ต้องแก้ปัญหา moving-platform และ wall-collision ซ้ำ — effort ต่ำ ตรวจ license ก่อนใช้ บันทึก shader breakdown ฝนหยด [2] และ liquid [9] ไว้ใน Shader Graph/HDRP reference library ของทีม ทั้งสองชิ้น replicate ได้ง่ายและตรงกับงาน Unity ที่ทำอยู่ ข้าม #ScreenshotSaturday showcase [3][4][5][6][8][10][11][13] และวิดีโอความเห็น Unity-retention [12] — ไม่มีเนื้อหา engineering ที่นำไปใช้ได้

## Signals to Watch
- Unity controller open-source ที่แก้ edge case พบบ่อย — ผู้สมัครสำหรับ reuse [1]
- โน้ต cross-engine shader portability (HDRP→Unreal) ในฐานะ workflow pattern [2]
- Unity-exit sentiment ที่ปรากฏซ้ำในหมู่ creator [12]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | jettelly | ^1923 c12 | [Developer thesquirrelyjones released an open-source custom character controller ](https://x.com/jettelly/status/2060617205989965911) |
| x | sean_gause | ^841 c5 | [Anyways. No use gatekeeping anything. Here's the basic node setup I used for the](https://x.com/sean_gause/status/2060903183355085035) |
| x | UnrealEngine | ^105 c28 | [We know that #ScreenshotSaturday is always out of this world So, show us what in](https://x.com/UnrealEngine/status/2060723065991131533) |
| x | MortalCrux | ^79 c5 | [A mind-blowing magic finisher 🧙‍♀️ #indiegamedev #indiegame #unity3d #pcgamer #m](https://x.com/MortalCrux/status/2060702882001731819) |
| x | Plasmeo | ^76 c2 | [Who needs cover when you have shielder drones ? #indiedev #gamedev #FPS #Unity #](https://x.com/Plasmeo/status/2060742236816445564) |
| x | DAVFX_0 | ^74 c0 | [Illugen smoky particles #vfx #realtimevfx #illugen #gamedev #unity3d https://t.c](https://x.com/DAVFX_0/status/2061041102682005755) |
| x | jonahh5830 | ^51 c1 | [The E-10: the lightest design in the E-series, this tiny tank destroyer was inte](https://x.com/jonahh5830/status/2061004991528153259) |
| x | IndiepathCS | ^43 c0 | [Simple atmospheric, lighting, and sounds testing for a Backrooms project. #Backr](https://x.com/IndiepathCS/status/2061028068601245900) |
| x | jettelly | ^41 c0 | [DNArt showed off this stylized liquid shader made with Shader Graph, using verte](https://x.com/jettelly/status/2061040002717671602) |
| x | DAVFX_0 | ^38 c2 | [Electric stuff in Illugen #vfx #realtimevfx #illugen #unity3d #gamedev https://t](https://x.com/DAVFX_0/status/2060866245482709002) |
| x | OzgursAssets | ^38 c2 | [Modular alternative headlight design #keitruck #gamedev #indiedev #ue5 #Unity3d ](https://x.com/OzgursAssets/status/2060799257293000895) |
| x | dailabs | ^34 c1 | [Everyone Says Quit The Unity Game Engine. Here's Why I Won't... #indiegame #game](https://x.com/dailabs/status/2061057835861967064) |
| x | RisingFoxGame | ^31 c1 | [Fight to survive or die trying! There are only a few gauntlets, but all of them ](https://x.com/RisingFoxGame/status/2060823938083536983) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1923 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2060617205989965911">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Developer thesquirrelyjones released an open-source custom character controller for Unity, designed to handle edge cases like moving platforms and wall collisions. 🎮 See more: https://t.co/fpq8pSxsLi ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer thesquirrelyjones ปล่อย open-source Unity character controller ที่รองรับ edge cases เช่น moving platforms และ wall collision</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Character controller สำเร็จรูปที่จัดการ physics edge cases ไว้แล้ว ช่วยให้ Unity team ไม่ต้องเสียเวลา prototype ในโปรเจกต์ platformer หรือ 3D game</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู repo แล้วประเมินว่าจะแทนหรือเสริม character movement ที่ใช้อยู่ในโปรเจกต์ปัจจุบันได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2060617205989965911" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sean_gause</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 841 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sean_gause/status/2060903183355085035">View @sean_gause on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Anyways. No use gatekeeping anything. Here's the basic node setup I used for the rain drip shader. It should translate to Unreal pretty easily, the major difference being that Unity HDRP has a mask ma”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@sean_gause แชร์ node graph ครบชุดสำหรับ rain drip shader ใน Unity HDRP พร้อมอธิบายว่า mask map รวม channel metal, AO, detail, smoothness ไว้ด้วยกัน และ setup นี้แปลงไป Unreal ได้โดยต่างกันแค่จุดนั้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Node graph สำหรับ rain drip บน HDRP ฟรีและพร้อมใช้ ลด R&amp;D เวลา environmental detail ที่ต้องใช้บ่อยในโปรเจกต์ Unity สไตล์ realistic</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity นำ node graph นี้ใส่ใน HDRP scene เป็น starting point สำหรับ wet-surface material แล้วปรับ mask map channel ให้ตรงกับ texture set ที่มีอยู่ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sean_gause/status/2060903183355085035" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 105 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2060723065991131533">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We know that #ScreenshotSaturday is always out of this world So, show us what in the universe of possibilities you're developing, perfecting or concepting! 📷: @karabardin https://t.co/tiV6Ao2Aq0”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine โพสต์ #ScreenshotSaturday ประจำสัปดาห์ ชวน developer แชร์ภาพเกมที่กำลังพัฒนา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2060723065991131533" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MortalCrux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 79 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MortalCrux/status/2060702882001731819">View @MortalCrux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A mind-blowing magic finisher 🧙‍♀️ #indiegamedev #indiegame #unity3d #pcgamer #madewithunity #gamedev #gaming #Steam #fantasy #RPG #ScreenshotSaturday https://t.co/2KHz2qs4qC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev @MortalCrux โพสต์ clip VFX magic finisher ใน Unity RPG ของตัวเองสำหรับ ScreenshotSaturday — ไม่มีการอธิบาย technique หรือ breakdown ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MortalCrux/status/2060702882001731819" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Plasmeo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 76 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Plasmeo/status/2060742236816445564">View @Plasmeo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Who needs cover when you have shielder drones ? #indiedev #gamedev #FPS #Unity #lowpoly #retroFPS #madewithunity #screenshotsaturday #boomershooter https://t.co/mXBrIH5SgB”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@Plasmeo โชว์ footage drone ที่ทำ shield ในเกม low-poly retro FPS สร้างด้วย Unity — เป็นแค่ #ScreenshotSaturday ไม่มี technique หรือ code แชร์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Plasmeo/status/2060742236816445564" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DAVFX_0</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 74 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DAVFX_0/status/2061041102682005755">View @DAVFX_0 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Illugen smoky particles #vfx #realtimevfx #illugen #gamedev #unity3d https://t.co/gaV7mraaU1”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@DAVFX_0 โชว์ smoky particle system แบบ real-time ของ Illugen ที่รันใน Unity3D ในลักษณะ volumetric-style smoke ที่ frame rate ใช้งานได้จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Illugen มี particle VFX คุณภาพสูงสำเร็จรูปสำหรับ Unity ช่วยลดเวลาทำ custom shader และ simulation ให้ทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง Illugen เป็น VFX asset ใน pipeline ปัจจุบันเพื่อวัด quality และ performance cost ก่อนตัดสินใจใช้จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DAVFX_0/status/2061041102682005755" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jonahh5830</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 51 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jonahh5830/status/2061004991528153259">View @jonahh5830 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The E-10: the lightest design in the E-series, this tiny tank destroyer was intended to replace the Jagdpanzer 38(t). It carried a 7.5 cm L/48 gun, and its suspension system allowed the hull to be low”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>creator บน Unity Asset Store โชว์โมเดล 3D รถทำลายรถถัง E-10 พร้อมข้อมูลจริงตามประวัติศาสตร์ ทั้งปืน 7.5 cm L/48 และระบบกันสะเทือนที่ปรับความสูงตัวถังได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>asset ยานพาหนะทหารประวัติศาสตร์แบบนี้เป็นจุดอ้างอิงที่ดีสำหรับ prototype เกมแนว WWII หรือ tactical ใน Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า Unity team กำลัง prototype ฉากทหารหรือประวัติศาสตร์ ให้ดู asset นี้ใน Unity Asset Store ก่อน commission โมเดลใหม่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jonahh5830/status/2061004991528153259" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IndiepathCS</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 43 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IndiepathCS/status/2061028068601245900">View @IndiepathCS on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Simple atmospheric, lighting, and sounds testing for a Backrooms project. #Backrooms #HorrorGames #Unity3D #gamedev #indiedev https://t.co/Ely0F3660a”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev @IndiepathCS ทดสอบ atmospheric lighting และ ambient sound ใน Unity สำหรับเกม horror แนว Backrooms และแชร์ footage แรกบน X</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>บรรยากาศ Backrooms อาศัย lighting gradient ละเอียดและ ambient audio แบบ loop — เป็น Unity technique ที่ทีม game ของ studio ใช้โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดู footage นี้เป็น reference สำหรับการวาง lighting mood และ sound layering ในฉาก atmospheric หรือ horror ที่กำลังสร้าง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IndiepathCS/status/2061028068601245900" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
