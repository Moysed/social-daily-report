---
type: social-topic-report
date: '2026-06-08'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-08T15:37:31+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 30
salience: 0.32
sentiment: neutral
confidence: 0.55
tags:
- gaussian-splatting
- blender
- photogrammetry
- shaders
- unity
- ai-3d
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2063397198880997376/img/VO1JqR2shYQ0NIp0.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-08

## TL;DR
- Gaussian Splatting มีสัญญาณวิจัยชัดเจนที่สุด: วิธีฉายทรงรีสู่หน้าจอแบบ perspective-stable ที่เร็วขึ้น [9], ViserDex ของ ETH Zürich ที่ใช้ RGB-only 3DGS สำหรับควบคุมมือหุ่นยนต์แบบ sim-to-real [14], และการทดสอบ merging scene จาก COLMAP ผ่าน tool lichtfeldstudio [26]
- Blender ยังเป็นเครื่องมือหลักในงาน production — procedural explosion generator [2], wrinkle-map cloth-stretch shader [3], และ rigging tutorial/WIP หลายชิ้น [5][12][17][19][20]
- Photogrammetry ปรากฏในฐานะ workflow จริงสำหรับ game-ready assets ไม่ใช่งานวิจัย: shoe scan 5k tris พร้อม cleanup pipeline ที่ลงตัว [24], สแกนชิ้นส่วนเพื่อ reverse engineering [16], และ paper whale-skeleton reconstruction แบบ stepwise ที่เปิดให้ดาวน์โหลดฟรี [4]
- งานฝั่ง engine เป็นการพัฒนาทีละขั้น: holographic sticker shader สำหรับ Unity [23], open-world authoring ด้วย threejs [10], และ AI 3D-gen tools (MeshyAI [30], Seedance 2.0 + GPT Image 2 [22])
- ไม่มี tool release สำคัญวันนี้ (ไม่มีข่าว Blender/Unity/Unreal version ใหม่); item ที่ engagement สูงที่สุด [1] เป็นการนำเสนอ laser scan ในเชิง pseudo-archaeology ไม่มี signal ที่ใช้งานได้จริง

## What happened
item 3D/graphics วันนี้ส่วนใหญ่เป็นงาน community WIP และ research note ชิ้นเล็กๆ ไม่ใช่ข่าว product. thread เทคนิคที่ชัดที่สุดคือ Gaussian Splatting: [9] แชร์วิธีฉายทรงรีแบบ arbitrary ellipsoid สู่หน้าจออย่าง perspective-stable ได้เร็ว, [14] เป็น sim-to-real framework ของ ETH Zürich (ViserDex) ที่ทำ in-hand object reorientation จาก RGB-only 3DGS, และ [26] บันทึกการ merge COLMAP dataset สำหรับ splatting ด้วย lichtfeldstudio. Photogrammetry ปรากฏในฐานะ applied pipeline — [24] รายงาน workflow scan รองเท้าที่ลงตัวแล้ว ได้ mesh game-ready 5k tris (reconstruct → smooth surface noise ใน Blender → re-import), [16] สแกนชิ้นส่วน Yamaha เพื่อ reverse engineering, และ [4] เผยแพร่ paper open-access เกี่ยวกับ photogrammetry สำหรับ whale skeletal reconstruction แบบ stepwise

## Why it matters (reasoning)
ภาพรวมนี้ยืนยันว่าความพยายามด้าน asset-production กำลังรวมศูนย์อยู่ที่ไหน. Gaussian Splatting กำลังพัฒนาจากความแปลกใหม่ไปสู่ tooling และการใช้งานข้ามโดเมน: การ optimize projection math [9], การประยุกต์ใช้กับ robotics ซึ่งพิสูจน์ว่า representation รองรับ closed-loop control ได้ [14], และ authoring tool ที่รองรับ multi-capture merging [26] ชี้ให้เห็นว่า pipeline (capture → COLMAP → splat → edit) กำลังกลายเป็นสิ่งที่ทำซ้ำได้จริง ไม่ใช่แค่การทดลอง. ในส่วน photogrammetry, การที่ [24] เน้น workflow ที่ 'ลงตัวในที่สุด' และ tri-budget target แสดงว่า bottleneck ย้ายจากคุณภาพการ reconstruct มาสู่ game-engine cleanup ซึ่งเป็นต้นทุน integration ที่ studio ต้องจ่ายจริง. การที่ Blender ปรากฏซ้ำในงาน procedural VFX [2], shader [3], และ rigging [5][12][17][19][20] ยิ่งตอกย้ำตำแหน่งเป็น DCC hub หลักที่ป้อน engine. ข้อควรระวัง: item ส่วนใหญ่เป็น anecdote จากคนเดียว ไม่มี benchmark และยังไม่ release จึงเป็น signal ในเชิงทิศทาง ไม่ใช่ข้อสรุปชี้ขาด

## Possibility
**Likely:** Gaussian Splatting รวมตัวเป็น pipeline แบบ editable และ engine-bound ต่อเนื่อง เนื่องจาก core math [9], tooling [26], และ applied use [14] ก้าวหน้าพร้อมกัน. **Plausible:** studio นำ splat/photogrammetry capture เข้าสู่ XR asset production เมื่อแก้ mesh/tri cleanup ได้ [24] แม้ splat ยังไม่รองรับ standard Unity/Unreal lighting และ animation ได้เต็มที่. **Plausible:** AI 3D-gen (MeshyAI [30], Seedance+GPT Image [22]) กลายเป็น prototyping front-end แต่คุณภาพและ topology ยังไม่มีหลักฐานจาก item วันนี้. **Unlikely:** item ใดวันนี้จะบังคับให้เปลี่ยน pipeline ในระยะสั้น — ไม่มี release ใด, ไม่มี benchmark, และไม่มี source ระบุตัวเลขการใช้งาน

## Org applicability — NDF DEV
1) ทดลอง Gaussian Splatting capture-to-XR บน object จริงชิ้นหนึ่งด้วย workflow ของ lichtfeldstudio [26] และติดตาม projection method [9] เรื่อง runtime stability — effort ปานกลาง; เป็น gate ว่า splat ใช้ได้จริงใน XR experience ของ studio หรือไม่. 2) นำ photogrammetry-to-Blender cleanup pattern (reconstruct → smooth noise → re-import, target ~5k tris) มาใช้กับ real-world prop ใน games/XR [24][16] — effort ต่ำ-ปานกลาง; นำไปใช้กับ asset production ได้เลย. 3) ประเมิน Blender procedural explosion generator [2] และ wrinkle-map cloth shader [3] เป็น VFX/material technique ที่นำมาใช้ซ้ำได้ — effort ต่ำ. 4) Prototype Unity holographic shader effect [23] สำหรับ game/XR UI หรือ collectible polish — effort ต่ำ. 5) Spot-test MeshyAI [30] สำหรับ prototype asset ชั่วคราวเท่านั้น ไม่ใช่ production — effort ต่ำ. ข้าม: Kailasa laser-scan thread [1] (pseudo-archaeology ไม่มี method ที่ใช้งานได้), และ item ที่ไม่ใช่ 3D ทั้งหมด — politics [8], VRChat convention drama [11], drone stock analysis [13], radios [15]

## Signals to Watch
- ติดตาม lichtfeldstudio และ COLMAP-merge workflow ที่พัฒนาขึ้นสำหรับ multi-capture splat scene [26]
- ติดตาม RGB-only Gaussian Splatting ที่ขยายเข้าสู่ control/robotics ซึ่งเป็นสัญญาณว่า representation เริ่มเชื่อถือได้ [14]
- ติดตาม 3D beginner VTuber course ฟรีที่จะเปิดตัว June 15 และ 3D capture tech ของ Cover [21][25] สำหรับ avatar/mocap pipeline ต้นทุนต่ำที่เกี่ยวข้องกับ XR
- ติดตาม threejs open-world authoring เป็น reference สำหรับการส่งมอบ 3D บน web/mobile [10]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | JIX5A | ^16221 c228 | [Kailasa was just scanned with lasers, and if you haven't been following this pla](https://x.com/JIX5A/status/2063397266090574013) |
| x | 3DxDEV7 | ^2037 c7 | [Check out how Hiroshi Kanazawa showcased this Blender-powered explosion generato](https://x.com/3DxDEV7/status/2063276491480105412) |
| x | 3DxDEV7 | ^396 c0 | [Check out this stunning shader test by Cartesian Caramel ✨ A breakdown of how wr](https://x.com/3DxDEV7/status/2063879964999442914) |
| x | HS_Shinmura | ^281 c0 | [Full-text access now available! My paper on the 3D reconstruction of whale skele](https://x.com/HS_Shinmura/status/2063560104725934084) |
| x | ItzFAILURE | ^269 c2 | [the WHOLE ass wip of the scene. One of my favorites of Vol 2 Rigs: @cookie_sugar](https://x.com/ItzFAILURE/status/2063824452366766191) |
| x | bestkingsun1 | ^247 c3 | [Stormcutter model made for a roblox game called "Rise of dragons" Were looking f](https://x.com/bestkingsun1/status/2063319729800871957) |
| x | dynastiees | ^157 c16 | [Frieren The Height of Magic recreation Vfx - me Animations @Devgrams Sfx @ZykiuD](https://x.com/dynastiees/status/2063655876519448821) |
| x | CreasonJana | ^143 c10 | [I did not know this … @VP @JDVance has the authority to walk into the chamber, t](https://x.com/CreasonJana/status/2063959635996860672) |
| x | Michael_Moroz_ | ^126 c2 | [I also found this fast nifty way to project an ellipsoid given an arbitrary proj](https://x.com/Michael_Moroz_/status/2063474503708033323) |
| x | alightinastorm | ^98 c15 | [Vibe Coding a AAA game with threejs Day 10: Deep dive into world authoring What ](https://x.com/alightinastorm/status/2063452003036971131) |
| x | VixenVRC | ^83 c10 | [This year reflects the damage it did, Not gonna lie but i didn't bother attendin](https://x.com/VixenVRC/status/2063649767939342647) |
| x | DemNikoArt | ^79 c2 | [You seemed to like this one. The tutorial for it is out now 😉 🔗 below #b3d #blen](https://x.com/DemNikoArt/status/2063295864689262853) |
| x | LnprCapital | ^74 c3 | [Ideaforge Technology Ltd Market Cap : ₹ 4100 Crores. FY25 nearly broke the story](https://x.com/LnprCapital/status/2063787083819585730) |
| x | lukas_m_ziegler | ^72 c3 | [Robot hands are getting out of hand! ✊🏼 RGB-only dexterous hand control via 3D G](https://x.com/lukas_m_ziegler/status/2063678741386342895) |
| x | bilawalsidhu | ^62 c6 | [Baofeng radios? Chinese dynamism… $15-35 handhelds that punch way above their we](https://x.com/bilawalsidhu/status/2063849083819766036) |
| x | SkinnyfatTony | ^57 c3 | [I like to mess with reverse engineering, when I had time I would 3d scan parts o](https://x.com/SkinnyfatTony/status/2063659335050531160) |
| x | RyanLykos | ^55 c1 | [Finished the textures for my Smart Pistol! Ready to start rigging it, and finall](https://x.com/RyanLykos/status/2063385152470860065) |
| x | bilawalsidhu | ^53 c3 | [Deep tech founders circa 1910 https://t.co/YyIeQzIwx4](https://x.com/bilawalsidhu/status/2063458023209648517) |
| x | Leave_MeBee | ^50 c5 | [i hate rigging hunters in blender, your capes are SO ANNOYING 😭 WHY DID IT HAVE ](https://x.com/Leave_MeBee/status/2063481281988428016) |
| x | DemNikoArt | ^47 c1 | [I accidentally developed a new look for my YouTube thumbnails 😁 I kinda like it.](https://x.com/DemNikoArt/status/2063915373112525306) |
| x | MrZing07 | ^46 c3 | [Friendly reminder that my 3D beginner vtuber course's first episode will be on y](https://x.com/MrZing07/status/2063990740296835564) |
| x | auqibhabib | ^38 c15 | [Made with seedance 2.0 + GPT Image 2 @image1 fights three opponents inside a Jap](https://x.com/auqibhabib/status/2063332990185619963) |
| x | AsahiArtist | ^35 c0 | [Holographic sticker shader test in Unity ✨ #unity #shader https://t.co/XDDDirOQD](https://x.com/AsahiArtist/status/2063518218103472134) |
| x | blenderguppy | ^30 c1 | [Another successful shoe scan. 5k tris. I think I finally ironed out the workflow](https://x.com/blenderguppy/status/2063855888063238650) |
| x | Riko_de_Sama | ^25 c1 | [@V_Faction Honestly, one of the biggest test of Cover's 3D capture tech if there](https://x.com/Riko_de_Sama/status/2063636519252885964) |
| x | blue_nile_3d | ^21 c1 | [Experimenting with merging Colmap data on top of each other for Gaussian Splatti](https://x.com/blue_nile_3d/status/2063300074487304689) |
| x | bilawalsidhu | ^10 c0 | [@rpnickson Now this is a mfing ad - bravo!](https://x.com/bilawalsidhu/status/2063459517451440418) |
| x | multimodalart | ^8 c4 | [where we are headed, all software becomes open source software models can decomp](https://x.com/multimodalart/status/2063307704873951333) |
| x | bilawalsidhu | ^7 c0 | [@sriramk @ayirpelle Congrats on a great run and thank you for your service Srira](https://x.com/bilawalsidhu/status/2063333617506377794) |
| x | MeshyAI | ^2 c0 | [@IHayato Bravo👏🏻](https://x.com/MeshyAI/status/2063858081914925453) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@JIX5A</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 16221 · 💬 228</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/JIX5A/status/2063397266090574013">View @JIX5A on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Kailasa was just scanned with lasers, and if you haven’t been following this place, hold on. What’s being uncovered here won’t just rewrite Indian history. It could rewrite human history and prove Anc”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ viral บน X ใช้ข่าวสแกน laser วัด Kailasa เป็นตะขอดึงคนอ่าน แล้วเบนไปเรื่องทฤษฎีอารยธรรมโบราณ ไม่ได้พูดถึงเทคโนโลยีสแกนหรือผลลัพธ์จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/JIX5A/status/2063397266090574013" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2037 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2063276491480105412">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out how Hiroshi Kanazawa showcased this Blender-powered explosion generator — 💥 Really cool progress on this project. What part stands out most to you? 👀 #B3D #Blender3D #Blender #Animation #VFX”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Hiroshi Kanazawa สาธิต explosion generator แบบ procedural สร้างด้วย Blender Geometry Nodes โชว์เป็น WIP VFX</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Explosion rig จาก Geometry Nodes export เป็น VFX asset ใน Unity หรือ XR scene ได้ ไม่ต้องพึ่ง stock FX pack</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/VFX ลอง prototype procedural explosion asset ด้วย Blender Geometry Nodes ใช้ใน game หรือ XR scene ได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2063276491480105412" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 396 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2063879964999442914">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out this stunning shader test by Cartesian Caramel ✨ A breakdown of how wrinkle maps can simulate cloth stretching in Blender, and the result is seriously impressive. #B3D #Blender #Blender3D #S”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Cartesian Caramel สาธิตเทคนิค shader ใน Blender ที่ใช้ wrinkle maps จำลองผ้ายืด โดยไม่ต้องรัน cloth simulation จริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Wrinkle maps คำนวณถูกกว่า physics simulation และ bake เข้า asset เพื่อใช้ใน Unity หรือ XR แบบ real-time ได้เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม 3D ดู breakdown นี้แล้วนำ wrinkle map cloth shading ใส่ character assets ก่อน export เข้า Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2063879964999442914" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HS_Shinmura</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 281 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HS_Shinmura/status/2063560104725934084">View @HS_Shinmura on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Full-text access now available! My paper on the 3D reconstruction of whale skeletal configuration using stepwise photogrammetry is now freely available via Wiley Article Share. Read here: https://t.co”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจัยเผยแพร่ paper open-access อธิบาย workflow แบบ stepwise photogrammetry สำหรับ reconstruct โครงกระดูกวาฬเป็น 3D อย่างแม่นยำ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>วิธี stepwise capture สำหรับ object ขนาดใหญ่และมีข้อต่อเป็น reference ที่ใช้งานได้จริงสำหรับทีมที่ทำ scan-based 3D asset ใน XR หรือ e-learning</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/e-learning อ่าน methodology section เป็น reference ก่อนวางแผน photogrammetry capture ของ object ขนาดใหญ่หรือซับซ้อน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HS_Shinmura/status/2063560104725934084" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 269 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2063824452366766191">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“the WHOLE ass wip of the scene. One of my favorites of Vol 2 Rigs: @cookie_sugar42 Textures: @Hiru3152 Shader: @LuminaryOfAges #FNDM #blender #animation #whiterose #RWBY https://t.co/CsYvuA7KR0”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Fan animator แชร์ WIP scene ใน Blender สำหรับ fan animation RWBY Vol 2 โดยแบ่งเครดิตระหว่างทีม rig, texture, และ shader</dd>
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
    <span class="ndf-author">@bestkingsun1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 247 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bestkingsun1/status/2063319729800871957">View @bestkingsun1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Stormcutter model made for a roblox game called &quot;Rise of dragons&quot; Were looking for animators,Vfx designers! https://t.co/iJtEGh00Qe #httyd #HowToTrainYourDragon #dragon #3Dmodel #blender #3dart #3DArt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>3D artist อิสระโพสต์โมเดล Stormcutter dragon ที่ทำด้วย Blender สำหรับเกม Roblox ชื่อ 'Rise of Dragons' พร้อมประกาศหา animator และ VFX designer</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bestkingsun1/status/2063319729800871957" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@dynastiees</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 157 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/dynastiees/status/2063655876519448821">View @dynastiees on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Frieren The Height of Magic recreation Vfx - me Animations @Devgrams Sfx @ZykiuDev Map @luhr1n Emotional support @ZerphVfx @lonely_nights9 @liqqzzzz @4yuyo @northeasttprod @d229n #Unity #VFX #RobloxDe”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีม dev สร้าง scene เวทมนตร์จาก Frieren ขึ้นมาใหม่ใน Unity เป็น Roblox VFX showcase โดยแบ่ง credit ตาม role: VFX, animation, SFX, map</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัวอย่าง pipeline แบ่ง role จริงสำหรับ stylized anime VFX ใน Unity บน Roblox — reference ที่ดีสำหรับงาน Unity VFX ของทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู breakdown วิดีโอเพื่อดึง technique เรื่อง timing และ layering มาใช้กับ Unity VFX scene ของทีม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/dynastiees/status/2063655876519448821" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@CreasonJana</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 143 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/CreasonJana/status/2063959635996860672">View @CreasonJana on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I did not know this … @VP @JDVance has the authority to walk into the chamber, take the presiding officers chair as Senate President &amp; enforce the rules that would enable a ‘talking filibuster’! So, t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจารณ์การเมืองสหรัฐฯ อธิบายอำนาจตามรัฐธรรมนูญของ JD Vance ในฐานะประธานวุฒิสภา เกี่ยวกับกระบวนการ filibuster สำหรับ SAVE America Act</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/CreasonJana/status/2063959635996860672" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
