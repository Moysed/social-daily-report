---
type: social-topic-report
date: '2026-06-09'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-09T03:31:50+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 42
salience: 0.7
sentiment: positive
confidence: 0.65
tags:
- gaussian-splatting
- apple-maps
- 3d-capture
- blender
- xr
- photogrammetry
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2064057009348005888/img/9TfGqQJ71uxtmsSy.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-09

## TL;DR
- Apple ประกาศ Gaussian Splatting ใน Apple Maps ที่งาน WWDC 2026 สร้างจาก oblique aerial imagery แทน mesh photogrammetry — item ที่ engagement สูงสุดในวันนี้ (scores 3145/2177/1422) [1][2][3].
- นักวิจารณ์มองว่า Apple แซง Google ในการ 3D capture ระดับ consumer และนี่คือการอัปเดต Apple Maps ครั้งใหญ่ที่สุดตั้งแต่ปี 2021 พร้อมโอกาส Vision Pro ที่ตามมา [38][40][41].
- 3DGS ขยายออกจาก maps: portrait capture สำหรับผู้บริโภคผ่าน KIRI Engine [26], ViserDex ของ ETH Zürich ใช้ RGB-only splatting สำหรับ robot in-hand control [14] และ ellipsoid-projection method ที่เร็วขึ้นสำหรับ perspective-stable splats [12].
- กิจกรรม Blender tooling: NeXus particle/fluid sim ของ Insydium (เดิมเฉพาะ Cinema 4D) เข้า public beta [30] พร้อม retopology tool แบบ click-and-drag [17] และ cloth-stretch wrinkle-map shader test [4].
- ตัวอย่าง photogrammetry-to-game pipeline: workflow scan รองเท้า 5k-tri ที่ clean ใน Blender [28] และ paper งานวิจัย peer-reviewed เรื่อง whale-skeleton reconstruction [8].

## สิ่งที่เกิดขึ้น
Signal หลักของวันนี้คือประกาศ WWDC 2026 ของ Apple ว่า 3D Gaussian Splatting จะมาใน Apple Maps สร้างจาก oblique aerial imagery และนำเสนอว่า clean กว่า mesh photogrammetry [1][2][3]. หลายคนมองว่า Apple ไปถึง 3D maps ระดับ consumer ก่อน Google [41] เป็นการอัปเดต Apple Maps ครั้งสำคัญแรกตั้งแต่ปี 2021 [38] พร้อม demand ให้มี Vision Pro app แบบ first-class [40]. เรื่องนี้เรื่องเดียวครอง engagement scores สูงสุดสามอันดับแรกอย่างชัดเจน.

## ทำไมถึงสำคัญ
Apple นำ 3DGS ลงใน consumer app ทั่วไปเป็นการดัน Gaussian Splatting จากเทคนิคระดับ research/enthusiast เข้าสู่ production และ viewing infrastructure กระแสหลัก [1][41]. ผลต่อเนื่อง: capture tooling และ viewer ได้ install base ขนาดใหญ่ ซึ่งดึง app อื่น (KIRI consumer portraits [26]) และ research (RGB-only robot manipulation [14], faster projection math [12]) ตามมา. สำหรับ XR/games studio สิ่งที่เปลี่ยนคือ splat-based environments อาจกลายเป็น content format มาตรฐานบน Apple hardware โดยเฉพาะถ้า Vision Pro รองรับ native [40]. รายการ Blender แสดงให้เห็น pipeline ที่ค่อยๆ ดีขึ้นทีละขั้น ไม่ใช่การพลิกโฉม: NeXus ขยาย simulation options บน Blender [30] และ retopology ที่เร็วขึ้น [17] ลด asset-cleanup time ซึ่งเป็น bottleneck หลักเมื่อนำ scan เข้า Unity/Unreal [28].

## ความเป็นไปได้
Likely: app จำนวนมากขึ้นรับ 3DGS export หลัง platform owner ยืนยันที่ scale นี้ [1][26]. Plausible: Apple เพิ่ม splat support แบบ native ใน Vision Pro Maps จาก demand ที่ชัดเจน [40] และกรอบ land-grab [41] — แต่ยังไม่มีแหล่งยืนยันวันที่. Plausible: research advances (perspective-stable projection [12], sim-to-real control [14]) ย่นเส้นทางสู่ real-time splats ใน engine แม้ทั้งหมดยังไม่ integrate กับ engine วันนี้. Unlikely ในระยะใกล้: splat แทน polygon mesh ใน game pipeline — ทุกตัวอย่าง game-ready ยังพึ่ง mesh retopology และ cleanup [17][28]. ไม่มีแหล่งใดให้ตัวเลขพยากรณ์ จึงไม่ระบุตัวเลข.

## การนำไปใช้สำหรับ NDF DEV
1) ทดลอง 3DGS capture-to-XR โดยใช้ consumer app เช่น KIRI Engine เพื่อประเมิน splat สำหรับ location/asset content ใน XR experiences (effort: med) [26][1]. 2) ติดตั้ง NeXus Blender public beta ฟรีเพื่อประเมิน particle/fluid sim สำหรับ VFX โดยไม่ต้องมี Cinema 4D license (effort: low) [30]. 3) ประเมิน click-and-drag Blender retopology tool เพื่อเร่ง scan/sculpt cleanup สำหรับ game-ready mesh (effort: low) [17]. 4) กำหนด target workflow สำหรับ photogrammetry (เช่น ~5k tris, Blender smoothing pass) สำหรับ scanned props ใน games/edutech assets (effort: med) [28]. 5) เก็บ procedural Unity VFX references (manta ray system [27], impact frame [9]) ไว้ใน real-time effects backlog (effort: low). ข้าม: การเมือง, Baofeng-radio, fandom-WIP, convention-drama [7][15][20][32][13] — ไม่เกี่ยวกับ production.

## Signals to Watch
- Apple จะ ship 3DGS Maps support แบบ native บน Vision Pro หรือไม่ ซึ่งจะกำหนด content-format expectation สำหรับ XR [40][41].
- 3DGS export ปรากฏใน consumer/prosumer capture app มากขึ้นหลัง Apple ยืนยัน [26][1].
- Real-time/perspective-stable splat rendering ที่สุกพอจะ integrate กับ engine [12][14].
- Insydium NeXus ย้ายจาก beta สู่ release บน Blender [30].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^3145 c77 | [holy crap! apple just beat google to the punch -- 3d gaussian splatting is comin](https://x.com/bilawalsidhu/status/2064057313057439795) |
| x | RadianceFields | ^2177 c25 | [Apple just announced gaussian splatting is coming to Apple Maps at WWDC. https:/](https://x.com/RadianceFields/status/2064043440350888050) |
| x | YIMBYLAND | ^1422 c20 | [Apple just released 3D gaussian splatting on Apple Maps 🤯 This is gonna hit the ](https://x.com/YIMBYLAND/status/2064077227952627823) |
| x | 3DxDEV7 | ^905 c0 | [Check out this stunning shader test by Cartesian Caramel ✨ A breakdown of how wr](https://x.com/3DxDEV7/status/2063879964999442914) |
| x | ItzFAILURE | ^731 c1 | [Saw this and got immediately insured for more white rose agenda posting WIPs…. I](https://x.com/ItzFAILURE/status/2064061177458491784) |
| x | ItzFAILURE | ^706 c2 | [the WHOLE ass wip of the scene. One of my favorites of Vol 2 Rigs: @cookie_sugar](https://x.com/ItzFAILURE/status/2063824452366766191) |
| x | CreasonJana | ^375 c26 | [I did not know this … @VP @JDVance has the authority to walk into the chamber, t](https://x.com/CreasonJana/status/2063959635996860672) |
| x | HS_Shinmura | ^306 c0 | [Full-text access now available! My paper on the 3D reconstruction of whale skele](https://x.com/HS_Shinmura/status/2063560104725934084) |
| x | GameZoneHQ | ^170 c0 | [Procedurally generated impact frame with shader and particle system by @namutree](https://x.com/GameZoneHQ/status/2063878287865028798) |
| x | dynastiees | ^169 c16 | [Frieren The Height of Magic recreation Vfx - me Animations @Devgrams Sfx @ZykiuD](https://x.com/dynastiees/status/2063655876519448821) |
| x | MrZing07 | ^151 c7 | [Friendly reminder that my 3D beginner vtuber course's first episode will be on y](https://x.com/MrZing07/status/2063990740296835564) |
| x | Michael_Moroz_ | ^126 c2 | [I also found this fast nifty way to project an ellipsoid given an arbitrary proj](https://x.com/Michael_Moroz_/status/2063474503708033323) |
| x | VixenVRC | ^83 c10 | [This year reflects the damage it did, Not gonna lie but i didn't bother attendin](https://x.com/VixenVRC/status/2063649767939342647) |
| x | lukas_m_ziegler | ^83 c4 | [Robot hands are getting out of hand! ✊🏼 RGB-only dexterous hand control via 3D G](https://x.com/lukas_m_ziegler/status/2063678741386342895) |
| x | bilawalsidhu | ^74 c7 | [Baofeng radios? Chinese dynamism… $15-35 handhelds that punch way above their we](https://x.com/bilawalsidhu/status/2063849083819766036) |
| x | bryanvenzen | ^73 c3 | [When I was working at Retro Studios (Nintendo) on Metroid Prime Remastered, we w](https://x.com/bryanvenzen/status/2064074392708006234) |
| x | AFX_LAB | ^69 c1 | [Check out this retopology tool for Blender You can click &amp; drag to generate ](https://x.com/AFX_LAB/status/2064091649500905892) |
| x | DemNikoArt | ^66 c1 | [I accidentally developed a new look for my YouTube thumbnails 😁 I kinda like it.](https://x.com/DemNikoArt/status/2063915373112525306) |
| x | Der_Kernel_ | ^63 c7 | [This makes a lot more sense when you realize the announcement was only to boost ](https://x.com/Der_Kernel_/status/2063949463010345293) |
| x | monarchreport25 | ^59 c2 | [Young Woman's Plea for Re-Election Highlights Deepening Concerns Over Electoral ](https://x.com/monarchreport25/status/2064019285098275068) |
| x | SkinnyfatTony | ^59 c3 | [I like to mess with reverse engineering, when I had time I would 3d scan parts o](https://x.com/SkinnyfatTony/status/2063659335050531160) |
| x | bilawalsidhu | ^55 c3 | [Deep tech founders circa 1910 https://t.co/YyIeQzIwx4](https://x.com/bilawalsidhu/status/2063458023209648517) |
| x | Leave_MeBee | ^50 c5 | [i hate rigging hunters in blender, your capes are SO ANNOYING 😭 WHY DID IT HAVE ](https://x.com/Leave_MeBee/status/2063481281988428016) |
| x | bilawalsidhu | ^49 c1 | [want to go deeper down the 3d capture rabbit hole? i have a whole playlist of vi](https://x.com/bilawalsidhu/status/2064087817286828280) |
| x | kingrobloxyuri | ^46 c1 | [@rhoosecaboose posing characters in a 3D program is still a render, sure its not](https://x.com/kingrobloxyuri/status/2064108590701416629) |
| x | KIRI_Engine_App | ^37 c3 | [Graduation photos hit different when they're 3D Gaussian Splatting portraits. Di](https://x.com/KIRI_Engine_App/status/2063908905114091834) |
| x | 80Level | ^36 c0 | [Technical Artist Jawad Srour has shared a breakdown of his fully procedural mant](https://x.com/80Level/status/2063984397041488025) |
| x | blenderguppy | ^36 c1 | [Another successful shoe scan. 5k tris. I think I finally ironed out the workflow](https://x.com/blenderguppy/status/2063855888063238650) |
| x | AsahiArtist | ^35 c0 | [Holographic sticker shader test in Unity ✨ #unity #shader https://t.co/XDDDirOQD](https://x.com/AsahiArtist/status/2063518218103472134) |
| x | theCGchannel | ^31 c0 | [NeXus for Blender is now in public beta Register for an Insydium account to requ](https://x.com/theCGchannel/status/2064041239243022621) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3145 · 💬 77</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2064057313057439795">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“holy crap! apple just beat google to the punch -- 3d gaussian splatting is coming to apple maps. these 3d scenes are made from oblique aerial imagery. but unlike blobby photogrammetry -- no more brocc”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Apple Maps เพิ่ม 3D Gaussian Splatting โดยใช้ aerial imagery แบบเอียง ให้ detail ระดับพื้นดินคมชัดกว่า photogrammetry แบบเดิมที่มีปัญหา broccoli trees และ melted geometry</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Apple ใช้ 3DGS ใน product จริงแล้ว หมายถึง tooling และ device support จะโตเร็ว — ดีต่องาน XR/VR environment capture โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง spike ด้วย Luma AI หรือ Polycam สำหรับ 3DGS capture สถานที่จริง เพื่อประเมิน quality ก่อนใช้ใน XR/VR scene</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2064057313057439795" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RadianceFields</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2177 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RadianceFields/status/2064043440350888050">View @RadianceFields on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple just announced gaussian splatting is coming to Apple Maps at WWDC. https://t.co/lKG5G0XOkC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Apple ประกาศที่ WWDC 2025 ว่าจะนำ Gaussian splatting มาใช้ใน Apple Maps เพื่อแสดงผล 3D scene แบบ photorealistic</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Gaussian splatting เข้า Apple product ตัวแรกบ่งชี้ว่า technique นี้ production-ready แล้ว — ทีม XR/VR และ Unity ควรจับตา</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง evaluate Gaussian splatting pipeline (เช่น Unity Gaussian Splatting package) สำหรับ project XR หรือ environment-heavy ที่จะมาถึง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RadianceFields/status/2064043440350888050" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@YIMBYLAND</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1422 · 💬 20</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/YIMBYLAND/status/2064077227952627823">View @YIMBYLAND on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple just released 3D gaussian splatting on Apple Maps 🤯 This is gonna hit the Urbanist community the way crack cocaine hit 1980s New York. https://t.co/xVoBQeUaak”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Apple นำ 3D Gaussian Splatting เทคนิค reconstruct ฉากแบบ photorealistic แบบ real-time เข้า Apple Maps ใน production จริงแล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Apple deploy Gaussian Splatting ใน consumer scale ยืนยันว่าเทคนิคนี้ production-ready และจะเร่ง Unity/XR tooling ให้ตามเร็วขึ้น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity XR ควร benchmark Gaussian Splatting plugins ที่มีอยู่เทียบกับ baseline ที่ Apple วางไว้แล้วตอนนี้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/YIMBYLAND/status/2064077227952627823" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 905 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2063879964999442914">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out this stunning shader test by Cartesian Caramel ✨ A breakdown of how wrinkle maps can simulate cloth stretching in Blender, and the result is seriously impressive. #B3D #Blender #Blender3D #S”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Cartesian Caramel ปล่อย breakdown วิธีใช้ wrinkle maps ใน Blender shader จำลองการยืดของผ้าแบบ real-time โดยไม่ต้อง bake simulation</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Wrinkle maps ใน shader ถูกกว่า cloth simulation มาก เหมาะกับ character ใน Unity game หรือ XR avatar ที่ต้องการ performance</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู technique นี้แล้ว apply wrinkle map logic ผ่าน custom shader ใน URP/HDRP สำหรับ character ที่สวมเสื้อผ้าได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2063879964999442914" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 731 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2064061177458491784">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Saw this and got immediately insured for more white rose agenda posting WIPs…. I’m a real sucker for eyes and teeth. as per usual Model: @Artstudious Rig: @cookie_sugar42 Shader: @LuminaryOfAges Textu”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แอนิเมเตอร์แฟนอาร์ตแชร์ WIP ตัวละคร RWBY ที่ render ด้วย Blender โดย credit ทีมแยกสำหรับ model, rig, shader และ texture</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ItzFAILURE/status/2064061177458491784" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 706 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2063824452366766191">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“the WHOLE ass wip of the scene. One of my favorites of Vol 2 Rigs: @cookie_sugar42 Textures: @Hiru3152 Shader: @LuminaryOfAges #FNDM #blender #animation #whiterose #RWBY https://t.co/CsYvuA7KR0”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>animator โชว์ WIP scene ใน Blender สำหรับ fan animation โปรเจกต์ RWBY Vol 2 พร้อม credit ทีมแยกทำ rig, texture, shader</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ItzFAILURE/status/2063824452366766191" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CreasonJana</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 375 · 💬 26</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CreasonJana/status/2063959635996860672">View @CreasonJana on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I did not know this … @VP @JDVance has the authority to walk into the chamber, take the presiding officers chair as Senate President &amp; enforce the rules that would enable a ‘talking filibuster’! So, t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Twitter วิเคราะห์กระบวนการวุฒิสภาสหรัฐฯ เรื่อง VP JD Vance กับการบังคับใช้ talking filibuster เพื่อผ่านร่างกฎหมาย SAVE America Act</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CreasonJana/status/2063959635996860672" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HS_Shinmura</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 306 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HS_Shinmura/status/2063560104725934084">View @HS_Shinmura on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Full-text access now available! My paper on the 3D reconstruction of whale skeletal configuration using stepwise photogrammetry is now freely available via Wiley Article Share. Read here: https://t.co”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจัย @HS_Shinmura เผยแพร่งานวิจัย open-access เกี่ยวกับการสร้าง 3D โครงกระดูกวาฬด้วย stepwise photogrammetry ผ่าน Wiley</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HS_Shinmura/status/2063560104725934084" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
