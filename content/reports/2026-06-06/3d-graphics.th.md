---
type: social-topic-report
date: '2026-06-06'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-06T15:51:37+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 34
salience: 0.55
sentiment: mixed
confidence: 0.55
tags:
- gaussian-splatting
- blender
- shaders
- ai-3d
- photogrammetry
- unity
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2058586450484994048/img/lm4ksQYSOFmYZ0uF.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-06

## TL;DR
- KIRI Engine's 3DGS Render addon ตอนนี้ animate Gaussian Splats ใน Blender ได้แล้ว — export 4DGS/.ply sequence, rigging และ light baking แบบ experimental, รองรับ Blender 5.1 [12]
- รายงานความคืบหน้าด้านการ deploy splatting (ไฟล์ใหญ่, ไม่มี streaming) ผ่าน LOD systems สำหรับฉากขนาดใหญ่ [29]; Neural Gabor Splatting นำเสนอที่ CVPR 2026 [20]
- NVIDIA's ArtiFixer ซ่อม scan artifacts และเติมข้อมูลจาก sparse views ด้วย Wan 2.1 โดย generate frame ที่สอดคล้องกันหลายร้อย frame สำหรับบริเวณที่ถูกบัง [10]
- MAMMA อ้างว่า capture motion ไร้ marker จาก video feed ที่ sync กันไม่กี่ตัว ไม่ต้องใช้ชุด, marker, และกระบวนการ cleanup [4]
- งานช่างที่ใช้ได้ทันที: Unity ShaderGraph dissolve shader สำหรับ VFX ตายศัตรู/teleport [8] และ Shaders Plus addon ของ Blender สำหรับวัสดุกระจก/น้ำ/โลหะ [3]

## สิ่งที่เกิดขึ้น
เส้นเรื่องที่ชัดที่สุดคือ Gaussian Splatting กำลังเคลื่อนจาก research demo ไปสู่ production pipeline จริง KIRI Engine's 3DGS Render addon อัปเดตนำการ animate splat เข้ามาใน Blender พร้อม export 4DGS/.ply sequence, rigging และ light baking แบบ experimental และรองรับ Blender 5.1 [12] แยกจากนั้น โพสต์ระบุว่าอุปสรรคการ deploy 3DGS อย่างไฟล์ขนาดใหญ่และการขาด streaming กำลังถูกแก้ด้วย LOD systems สำหรับฉากขนาดใหญ่ [29] และ Neural Gabor Splatting นำเสนอที่ CVPR 2026 [20][33] ด้านการ capture และ reconstruct ด้วย AI: NVIDIA's ArtiFixer ซ่อม artifacts และเติมข้อมูล sparse views ด้วย Wan 2.1 [10] และ MAMMA อ้าง markerless mocap จาก synced video [4] ด้าน tooling แบบดั้งเดิม ศิลปินแชร์ dissolve effect ของ Unity ShaderGraph [8], Blender Shaders Plus addon [3], eye shader [21] และ tutorial/showcase เรื่อง rigging [1][11][23]; notes การผลิตของเกมหนึ่งอ้างถึง laser scanning และ photogrammetry โดยมี Yusuke Kozaki เป็น lead designer [2] หลายรายการที่ติด rank สูงไม่เกี่ยวข้องหรือเป็นโปรโมชัน: listicle AI tool [15][18][28], $RENDER crypto [27], คลิป AI video-gen [9][19] และโพสต์ส่วนตัว/ถกเถียง [5][22][24]

## ทำไมถึงสำคัญ (เหตุผล)
สำหรับสตูดิโอที่ผลิต asset ทั้ง game และ XR กลุ่ม splatting สำคัญที่สุด Splat ที่ animate ได้ใน Blender [12] บวกกับความคืบหน้าด้าน LOD/streaming [29] เริ่มเชื่อม real-world capture เข้ากับ engine content ที่ deploy ได้จริง แทนที่จะเป็นแค่ static viewer — คือ missing link ระหว่าง scanning กับ Unity เครื่องมือ AI reconstruction [10][4] มุ่งแก้ส่วนที่แพงที่สุดของการผลิต asset ได้แก่ cleanup จาก sparse scan และแรงงาน post-processing จาก mocap suit ข้อควรระวังคือนี่คือ claim จาก vendor และ enthusiast จากโพสต์สั้น ไม่ใช่ผลลัพธ์ที่ผ่าน benchmark; การ round-trip splat ไปยัง Unity, การ license และ runtime cost บน mobile หรือ standalone XR headset ยังไม่ได้รับการพิสูจน์ใน item เหล่านี้ โพสต์ shader และ rigging [3][8][21] เป็นการปรับปรุงงานช่างแบบ incremental ไม่ใช่การเปลี่ยนแปลงเชิงกลยุทธ์

## ความเป็นไปได้
มีแนวโน้ม: tooling ของ Gaussian Splatting ฝั่ง Blender จะพัฒนาต่อเนื่องในปีนี้ เห็นได้จากการอัปเดต addon ที่ประสานกัน [12], งาน infrastructure [29] และ research ที่ active ใน CVPR [20] เป็นไปได้: markerless mocap [4] และ AI scan repair [10] จะถึงระดับที่ indie/studio ใช้ได้ แต่ยังต้องการการ validate ด้าน engine integration และ output fidelity ก่อน ไม่น่าเกิด: item เหล่านี้จะแทนที่ Unity asset workflow ปัจจุบันในอนาคตอันใกล้ — item แสดงแค่ capability demo ไม่ใช่ pipeline ที่ optimize สำหรับ mobile/XR และพิสูจน์ใน production แล้ว ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น

## การประยุกต์ใช้ในองค์กร — NDF DEV
1) ทดลอง KIRI's 3DGS Render addon ใน Blender เพื่อทดสอบ path จาก capture→splat→Unity สำหรับ XR environment scene โดยวัด runtime cost บน target headset (med) [12][29] 2) เพิ่ม Unity ShaderGraph dissolve shader เข้า VFX library สำหรับ effect ตายศัตรู/teleport ในเกมปัจจุบัน (low) [8] 3) ประเมิน Shaders Plus เพื่อทำวัสดุกระจก/น้ำ/โลหะได้เร็วขึ้นใน asset production (low) [3] 4) ทดลอง markerless mocap แบบ MAMMA กับ character animation ที่ไม่ critical แล้วเปรียบเทียบเวลา cleanup กับวิธีปัจจุบันก่อนตัดสินใจ (med) [4] 5) ติดตาม NVIDIA ArtiFixer สำหรับ clean photogrammetry/sparse scan แต่ชะลอ integration ไว้ก่อนจนกว่าจะชัดเจนเรื่อง availability และ licensing (low eval) [10] ข้าม: $RENDER crypto [27], listicle 'hidden AI tools' [15][18][28], item NSFW/ส่วนตัว/ถกเถียง [5][13][22][24] และ AI video-gen demo [9][19] — ไม่มีอันไหนเป็น 3D-pipeline tool สำหรับสตูดิโอ

## Signals ที่ต้องติดตาม
- Gaussian Splatting LOD/streaming และ 4DGS animation ที่กำลัง mature ไปสู่การ deploy บน engine [12][29]
- Research splatting และ neural rendering จาก CVPR 2026 ที่จะป้อน tooling รุ่นถัดไป [20][33]
- AI scan-repair สำหรับ sparse/occluded views — NVIDIA ArtiFixer [10]
- Markerless mocap จาก video (MAMMA) ในฐานะทางลดต้นทุน character animation [4]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ndngdng10115 | ^1299 c9 | [The way the tendons, helper bones, and smoothing work together is seriously impr](https://x.com/ndngdng10115/status/2062718274643845486) |
| x | _YuriP__ | ^793 c4 | [• Development started in 2020 • Lead character designer is Yusuke Kozaki (Fire E](https://x.com/_YuriP__/status/2062605291485540393) |
| x | filip_animation | ^737 c3 | [My most used Blender addons #4: - Shaders Plus by SMOUSE Glass, water, oily meta](https://x.com/filip_animation/status/2062619776153764230) |
| x | clankrmedia | ^611 c7 | [Wow! Motion capture studios not gonna love this! Just check this insane video. F](https://x.com/clankrmedia/status/2062988031708000566) |
| x | mjarbo | ^571 c239 | [Kane Parsons' comments about AI feel a little too clean to me. He told The Austr](https://x.com/mjarbo/status/2062647581910413513) |
| x | Mix3Design | ^542 c7 | [I will have a big announcement in the upcoming hours all the blender 3d artists ](https://x.com/Mix3Design/status/2062654531888910756) |
| x | SciTechera | ^458 c19 | [Wow. That's cool. Researchers just released World, an open-source Unreal Engine ](https://x.com/SciTechera/status/2062554345087041916) |
| x | VFX_Therapy | ^287 c1 | [Dissolve Shader = Interactive edge glow + world space control. Perfect for enemy](https://x.com/VFX_Therapy/status/2062607977186738307) |
| x | auqibhabib | ^267 c35 | [Made with seedance 2.0 + GPT Image 2 on @yapper_so Prompt. @image1 mage1 fights ](https://x.com/auqibhabib/status/2062599264807833617) |
| x | wildmindai | ^243 c2 | [3D scene reconstructions by NVIDIA. ArtiFixer - repairs artifacts and extends sp](https://x.com/wildmindai/status/2062816526223216995) |
| x | DemNikoArt | ^163 c2 | [🚨 NEW TUTORIAL IS OUT NOW! How to rig a Bike Suspension in Blender. 🔗 below #b3d](https://x.com/DemNikoArt/status/2062589493710934176) |
| x | KIRI_Engine_App | ^135 c1 | [Gaussian Splats can now be animated in Blender New 3DGS Render addon update: - B](https://x.com/KIRI_Engine_App/status/2062821750287847445) |
| x | FoxibikiN | ^97 c1 | [(HD) Chillet &amp; Chill 🩵Chillet made by @furromantic ❄️Beau OC made by @miauha](https://x.com/FoxibikiN/status/2062652783975608633) |
| x | multimodalart | ^85 c1 | [I' m so addicted to @GoogleMagenta RealTime 2 🎹 so to justify playing with it 24](https://x.com/multimodalart/status/2062938381785403586) |
| x | Orion_Vers7x | ^68 c27 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/SConc5qUp9 – Writing](https://x.com/Orion_Vers7x/status/2062749510195982839) |
| x | DXU241 | ^66 c2 | [Been working on better support for Unreal Gold, will need to write a custom clou](https://x.com/DXU241/status/2062653242795012221) |
| x | ihe4rtjungkook | ^59 c1 | [@vjungist cuz they took a 3d scan of his to make ts more accurate at his event](https://x.com/ihe4rtjungkook/status/2062996203235647515) |
| x | unfilteredranjn | ^52 c3 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/2ACL9zZ1Y8 – Writing](https://x.com/unfilteredranjn/status/2062778586046829047) |
| x | auqibhabib | ^49 c14 | [Made with seedance 2.0 + GPT Image 2 Prompt :Use the uploaded reference image as](https://x.com/auqibhabib/status/2062951836882231393) |
| x | HeartWatanabe20 | ^46 c0 | [Presenting Neural Gabor Splatting at CVPR 2026 tomorrow! 📍 Poster Session 🗓 June](https://x.com/HeartWatanabe20/status/2062728687007789143) |
| x | SG_Animations | ^45 c3 | [a quick abstraction eye shader i made in blender :) https://t.co/6tbIY5Iocu](https://x.com/SG_Animations/status/2062881248842830323) |
| x | user__NULL | ^40 c0 | [@gingerIemons @UltraTomatoo @airbagg3d No. Mike Parsons working in VFX for a def](https://x.com/user__NULL/status/2062653907764212105) |
| x | DemNikoArt | ^40 c1 | [If you haven't seen it, my new rigging tutorial is out now. How to rig a Bike Su](https://x.com/DemNikoArt/status/2062879660095000906) |
| x | RisingNomes | ^40 c3 | [This is my precious, little boy at about the same gestation that scan of their b](https://x.com/RisingNomes/status/2062789349306159350) |
| x | JamesMason0 | ^39 c6 | [You know, something I've always wondered - Why is it that so many Blender animat](https://x.com/JamesMason0/status/2062984400338403485) |
| x | alt_Vulcan105 | ^33 c1 | [@cybernetic_sam The only possible answer is that rover civilization is using sim](https://x.com/alt_Vulcan105/status/2062825816980181055) |
| x | EnochsDegenCrib | ^32 c0 | [🚀 $RENDER Bull Case: Market Dip? What Dip? Fundamentals Are Unbreakable⭕️🚀 Crypt](https://x.com/EnochsDegenCrib/status/2062904565859553483) |
| x | PrakashS720 | ^32 c5 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/6XRECyOn7W – Writing](https://x.com/PrakashS720/status/2062839222139294035) |
| x | Stefan_3D_AI | ^28 c0 | [For years, the biggest problem with 3D Gaussian Splatting wasn't quality. It was](https://x.com/Stefan_3D_AI/status/2063240740155895943) |
| x | MeshyAI | ^18 c0 | [I asked an AI agent to 3D print me as a figurine series! Here's how it works: - ](https://x.com/MeshyAI/status/2062805201480745129) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ndngdng10115</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1299 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ndngdng10115/status/2062718274643845486">View @ndngdng10115 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The way the tendons, helper bones, and smoothing work together is seriously impressive. 🔥 If you’re into character rigging, this one is worth a close look. #Blender #Blender3D #B3D #Rigging #Character”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Demo rig ตัวละครใน Blender แสดงระบบ tendon, helper bones และ mesh smoothing ทำงานร่วมกันเพื่อ deformation ที่สมจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค rigging แบบนี้ช่วยเพิ่มคุณภาพ character ใน Unity game และ XR project ได้โดยตรง ไม่ต้องซื้อ asset เพิ่ม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/character art ดูโครงสร้าง rig นี้แล้วนำ helper-bone pattern ไปใช้ใน character pipeline ที่มีอยู่ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ndngdng10115/status/2062718274643845486" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@_YuriP__</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 793 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/_YuriP__/status/2062605291485540393">View @_YuriP__ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“• Development started in 2020 • Lead character designer is Yusuke Kozaki (Fire Emblem Awakening/Fates/Heroes) • Laser scanning and photogrammetry • Developed their own sound engine with 7.1.4 audio • ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>เกม flight combat ที่เริ่มพัฒนาปี 2020 ใช้ laser scanning และ photogrammetry สร้าง 3D asset พัฒนา sound engine ของตัวเอง (7.1.4 audio) และใช้ Top Gun Maverick เป็น reference สำหรับ cutscene.</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Photogrammetry กลายเป็น pipeline มาตรฐานสำหรับ 3D capture คุณภาพสูง ใช้ได้จริงใน XR และ Unity projects ระดับ studio เล็กสำหรับ environment และ prop.</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ลอง photogrammetry (Reality Capture หรือ Polycam) จับ prop หรือ environment จริงใน project 3D ถัดไปได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/_YuriP__/status/2062605291485540393" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@filip_animation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 737 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/filip_animation/status/2062619776153764230">View @filip_animation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“My most used Blender addons #4: - Shaders Plus by SMOUSE Glass, water, oily metals are just made extremely easy with these shaders. You would be surprised how much I end up making those. Also very per”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Blender artist Filip แนะนำ addon 'Shaders Plus' โดย SMOUSE สำหรับ material ประเภท glass, water, และ oily metal — ให้ผล light dispersion และ caustics ดีกว่า shader ที่มีใน Blender เอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ใช้ Blender สร้าง asset ให้ Unity หรือ XR สามารถข้าม shader setup แบบ manual สำหรับ material พวก glass และ metal ได้เลย เพราะมี preset พร้อมใช้และ performance ดี</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม 3D ลอง Shaders Plus ใน project หน้าที่มี glass หรือ water แล้วเทียบกับ material workflow ปัจจุบัน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/filip_animation/status/2062619776153764230" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@clankrmedia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 611 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/clankrmedia/status/2062988031708000566">View @clankrmedia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow! Motion capture studios not gonna love this! Just check this insane video. For years, capturing human motion meant markers, skin-tight suits, and hours of cleanup. MAMMA just asks for a few synced”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>MAMMA คือระบบ mocap ไม่ใช้ marker ที่แม่นยำเทียบ Vicon ใช้แค่กล้อง sync กัน (รวม iPhone 4 ตัว) ย่น pipeline หลายวันเหลือวันเดียว ไม่ต้องใส่ชุดหรือติด marker</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>งาน animation Unity/XR ของทีมเก็บ motion data คุณภาพสูงได้โดยไม่เช่า mocap studio — iPhone 4 ตัวกับพื้นที่โล่งพอ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดลองใช้ MAMMA กับ iPhone 4 ตัวใน shoot animation ตัวละครครั้งหน้าก่อนตัดสินใจจ้าง mocap studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/clankrmedia/status/2062988031708000566" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mjarbo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 571 · 💬 239</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mjarbo/status/2062647581910413513">View @mjarbo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Kane Parsons’ comments about AI feel a little too clean to me. He told The Australian that if he could snap his fingers and make generative AI disappear forever, he probably would. Fair enough. He doe”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Kane Parsons (ผู้สร้าง Backrooms ปัจจุบันทำงานกับ A24) บอกอยากลบ generative AI ทิ้ง ทั้งที่ career สร้างจาก Blender และ indie tools ที่ bypass gatekeepers — ผู้โพสต์ชี้ความย้อนแย้ง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>กรอบ 'ใช้ tool เพื่องาน ไม่ใช่ให้ tool แทนงาน' เป็น mental model ที่ studio ใช้ได้ตอน decide ว่าจะเอา AI ไปใส่ pipeline ส่วนไหน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mjarbo/status/2062647581910413513" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Mix3Design</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 542 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Mix3Design/status/2062654531888910756">View @Mix3Design on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I will have a big announcement in the upcoming hours all the blender 3d artists that are into anime style / npr or blender in general will benefit from it alot alot and also who want to make game asse”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@Mix3Design ปล่อย teaser ว่าจะมีประกาศเกี่ยวกับ Blender สำหรับสาย anime/NPR และ game asset/VFX โดยยังไม่เปิดเผยรายละเอียดใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Mix3Design/status/2062654531888910756" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SciTechera</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 458 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SciTechera/status/2062554345087041916">View @SciTechera on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow. That's cool. Researchers just released World, an open-source Unreal Engine 5 simulator for training and testing LLM and VLM agents in realistic 3D environments. The platform supports RGB, depth, ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจัยปล่อย &quot;World&quot; ซึ่งเป็น UE5 simulator open-source รองรับ sensor หลายแบบ, procedural city generation, และ Python API แบบ Gym สำหรับ train LLM/VLM agents ใน 3D environment</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Python API แบบ Gym บน 3D simulator ที่สมจริงเปิดทางให้ทีม XR/VR train และ test AI agents ใน scene ซับซ้อนได้ โดยไม่ต้องสร้าง simulation infra เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลอง prototype agent navigation และ perception logic ใน World บน UE5 แล้วดูว่า logic นั้น transfer มาใช้ใน Unity projects ได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SciTechera/status/2062554345087041916" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFX_Therapy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 287 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFX_Therapy/status/2062607977186738307">View @VFX_Therapy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Dissolve Shader = Interactive edge glow + world space control. Perfect for enemy deaths or teleport effects! by @techartshahbaz. #Unity #ShaderGraph #TechArt #GameDev&quot; https://t.co/xjPVOSudHC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา @techartshahbaz แชร์ dissolve shader ใน ShaderGraph พร้อม edge glow แบบ interactive และ world-space control เหมาะกับ VFX ตายหรือ teleport</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ShaderGraph dissolve พร้อม edge glow ช่วยลดเวลาทำ effect พื้นฐานที่ทีม Unity ใช้บ่อย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู implementation จาก link แล้วเพิ่มเข้า shader library ของทีมเป็น dissolve template</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFX_Therapy/status/2062607977186738307" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
