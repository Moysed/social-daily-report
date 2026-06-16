---
type: social-topic-report
date: '2026-06-07'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-07T03:33:01+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 28
salience: 0.5
sentiment: positive
confidence: 0.55
tags:
- gaussian-splatting
- blender
- photogrammetry
- mocap
- unity-pipeline
- xr-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2063272954004209664/img/S7jifTp22pipLh_7.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-07

## TL;DR
- addon อัปเดตของ KIRI Engine's 3DGS Render เพิ่ม support Blender 5.1, export 4DGS/.ply sequence, และ rigging กับ light baking แบบ experimental — Gaussian splats ที่ animate ได้ภายใน Blender [5].
- ArtiFixer ของ NVIDIA ฟื้นฟู 3D scene โดยซ่อม artifact และขยาย sparse view ผ่าน Wan 2.1, generate frame ที่ consistent หลายร้อย frame พร้อม inpaint บริเวณที่ถูกบัง [3].
- 3DGS ถูกมองว่าพ้นจากปัญหาด้านคุณภาพแล้ว เหลือแต่ปัญหา infrastructure — ระบบ LOD และ streaming สำหรับ scene ขนาดใหญ่กำลังปรากฏขึ้น [8].
- MAMMA demo markerless motion capture จากกล้อง sync ไม่กี่ตัว ตัด marker suit และ manual cleanup ออก [2].
- ระบบ active-ragdoll ใน Unity ผสม physics, IK, และ procedural animation สำหรับตัวละครที่ทรงตัวได้เอง [11].

## What happened
cluster ที่โดดเด่นที่สุดของวันคือ Gaussian Splatting ที่เจาะลึกเข้าสู่ production pipeline มากขึ้น KIRI Engine ส่ง addon อัปเดต 3DGS Render สำหรับ Blender 5.1 พร้อม export 4DGS/.ply sequence บวก rigging และ light baking แบบ experimental [5]; โพสต์แยกต่างหากชี้ว่า bottleneck ที่เหลืออยู่ของ 3DGS คือ infrastructure (ขนาดไฟล์, streaming, deployment ของ large scene) และระบบ LOD/streaming กำลังเริ่มเกิดขึ้น [8]; ส่วน ArtiFixer ของ NVIDIA มุ่งเป้าที่ reconstruction cleanup ซ่อม artifact และขยาย sparse capture ด้วย Wan 2.1 [3]. นอกจากนี้ MAMMA แสดง markerless mocap จากกล้อง sync ไม่กี่ตัว [2], developer ของ Unity อธิบาย active ragdoll ที่ใช้ physics + IK + procedural animation [11], และ MeshyAI โปรโมต agent ที่แปลง portrait เป็น 3D-printable figurine [23]. signal ที่เหลือจาก Blender เป็นพวก showcase/tutorial: explosion generator [1], eye shader [14], และ rigging tutorial [16][18]. item ที่ engagement สูงหลายชิ้นไม่เกี่ยวข้องหรือเป็น noise — อาหาร NYC [7], baby scan [17], การเมือง [19], crypto $RENDER [20], และ listicle 'hidden AI tools' ซ้ำๆ [9][12][21].

## Why it matters (reasoning)
สำหรับ studio ที่ผลิต asset ทั้ง game และ XR เรื่อง 3DGS คือเรื่องที่ปฏิบัติได้จริง animated splat ที่ export จาก Blender [5] บวก LOD/streaming สำหรับ large scene [8] คือสองชิ้นส่วนที่ขาดหายไป ซึ่งจะทำให้ environment จากการ capture กลายเป็น XR/web content ที่ deploy ได้จริง แทนที่จะเป็นแค่ demo static; reconstruction repair แบบ ArtiFixer [3] ลด cleanup cost ของ sparse photogrammetry capture second-order effect คือการเลือก pipeline: ถ้า splat riggable และ streamable ได้ การผลิต environment จาก capture จะแข่งกับ mesh+PBR แบบ hand-built สำหรับ XR scene บางประเภท markerless mocap [2] ชี้ทิศทางเดียวกันสำหรับ character work — ลด cost ของ motion data — แต่ demo เป็นแค่ vendor showcase ที่ไม่มีรายละเอียดด้านคุณภาพ, latency, หรือ licensing จึงควรมองเป็นทิศทาง ไม่ใช่ tool ที่พิสูจน์แล้ว Unity ragdoll breakdown [11] เป็น engineering reference ที่นำไปใช้ได้สำหรับตัวละครที่ทรงตัวเอง ไม่ขึ้นกับ AI trend ใดๆ

## Possibility
Likely: Gaussian Splatting ยังเคลื่อนจาก research เข้าสู่ DCC tool และ engine pipeline ต่อเนื่องในเดือนข้างหน้า จาก addon support ใน Blender, export format, และการเปลี่ยนไปสู่ LOD/streaming infrastructure อย่างชัดเจน [5][8]. Plausible: AI reconstruction-repair tool อย่าง ArtiFixer กลายเป็น cleanup step มาตรฐานสำหรับ sparse capture ถ้า integrate เข้ากับ photogrammetry flow ที่มีอยู่ได้ [3]. Plausible: markerless mocap มีคุณภาพพอสำหรับ previz และ indie character work ส่วน pro pipeline ยังต้องการ manual verification [2]. Unlikely (near-term): markerless capture แทน marker-based mocap สำหรับ high-fidelity production เพราะหลักฐานที่มีเป็นแค่ promotional clip [2]. ไม่มีแหล่งใดระบุตัวเลข probability.

## Org applicability — NDF DEV
1) ทดสอบ KIRI's 3DGS Render addon บน Blender 5.1 ขนาดเล็ก โดย test .ply/4DGS export เข้า Unity XR scene เพื่อวัด fidelity, ขนาดไฟล์, และ runtime cost (effort: med) [5][8]. 2) Bookmark ArtiFixer และทดสอบใหม่เมื่อมี build/integration ที่ใช้ได้จริง ยังไม่ต้องลงทุน pipeline เพราะยังเป็น early demo (effort: low) [3]. 3) เก็บ Unity active-ragdoll breakdown [11] ไว้เป็น engineering reference สำหรับ feature ตัวละครที่ทรงตัวเองหรือ physics-driven gameplay (effort: low). 4) ใช้ portrait-to-figurine / AI 3D-asset tool อย่าง Meshy เฉพาะ throwaway prototype prop เท่านั้น ไม่ใช่ shippable asset จนกว่าจะตรวจสอบคุณภาพและ licensing แล้ว (effort: low) [23]. 5) มอง MAMMA markerless mocap เป็น watch item — รอ demo จริงที่มีข้อมูลคุณภาพ/latency ก่อนจะนัด test (effort: low) [2]. ข้าม: crypto/$RENDER [20], listicle 'hidden AI tools' ซ้ำๆ [9][12][21], และทุก item ที่ไม่เกี่ยวข้อง [7][17][19].

## Signals to Watch
- 3DGS infrastructure (LOD, streaming, large-scene deployment) — ปัจจัยที่กั้น deployment ของ captured scene ไปยัง XR/web [8].
- Animated/riggable Gaussian splats ใน Blender ผ่าน 3DGS Render addon — ติดตาม stability ที่พ้นจากสถานะ 'experimental' [5].
- AI reconstruction repair (NVIDIA ArtiFixer / Wan 2.1) สำหรับ sparse-view และ occluded-region cleanup [3].
- Markerless multi-camera mocap (MAMMA) — รอการยืนยันคุณภาพจากแหล่งอิสระ [2].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | 3DxDEV7 | ^1037 c6 | [Check out how Hiroshi Kanazawa showcased this Blender-powered explosion generato](https://x.com/3DxDEV7/status/2063276491480105412) |
| x | clankrmedia | ^768 c9 | [Wow! Motion capture studios not gonna love this! Just check this insane video. F](https://x.com/clankrmedia/status/2062988031708000566) |
| x | wildmindai | ^275 c1 | [3D scene reconstructions by NVIDIA. ArtiFixer - repairs artifacts and extends sp](https://x.com/wildmindai/status/2062816526223216995) |
| x | bestkingsun1 | ^172 c1 | [Stormcutter model made for a roblox game called "Rise of dragons" Were looking f](https://x.com/bestkingsun1/status/2063319729800871957) |
| x | KIRI_Engine_App | ^145 c1 | [Gaussian Splats can now be animated in Blender New 3DGS Render addon update: - B](https://x.com/KIRI_Engine_App/status/2062821750287847445) |
| x | multimodalart | ^92 c1 | [I' m so addicted to @GoogleMagenta RealTime 2 🎹 so to justify playing with it 24](https://x.com/multimodalart/status/2062938381785403586) |
| x | bilawalsidhu | ^91 c8 | [The Punjabi in me was exceedingly satisfied. NYC dining is undefeated. https://t](https://x.com/bilawalsidhu/status/2063272566572159063) |
| x | Stefan_3D_AI | ^77 c1 | [For years, the biggest problem with 3D Gaussian Splatting wasn't quality. It was](https://x.com/Stefan_3D_AI/status/2063240740155895943) |
| x | Orion_Vers7x | ^70 c27 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/SConc5qUp9 – Writing](https://x.com/Orion_Vers7x/status/2062749510195982839) |
| x | ihe4rtjungkook | ^61 c2 | [@vjungist cuz they took a 3d scan of his to make ts more accurate at his event](https://x.com/ihe4rtjungkook/status/2062996203235647515) |
| x | jettelly | ^56 c0 | [Developer Rawad Akar shared a closer look at their active ragdoll system for Uni](https://x.com/jettelly/status/2063244523942314049) |
| x | unfilteredranjn | ^52 c3 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/2ACL9zZ1Y8 – Writing](https://x.com/unfilteredranjn/status/2062778586046829047) |
| x | auqibhabib | ^49 c14 | [Made with seedance 2.0 + GPT Image 2 Prompt :Use the uploaded reference image as](https://x.com/auqibhabib/status/2062951836882231393) |
| x | SG_Animations | ^48 c3 | [a quick abstraction eye shader i made in blender :) https://t.co/6tbIY5Iocu](https://x.com/SG_Animations/status/2062881248842830323) |
| x | JamesMason0 | ^43 c6 | [You know, something I've always wondered - Why is it that so many Blender animat](https://x.com/JamesMason0/status/2062984400338403485) |
| x | DemNikoArt | ^41 c1 | [If you haven't seen it, my new rigging tutorial is out now. How to rig a Bike Su](https://x.com/DemNikoArt/status/2062879660095000906) |
| x | RisingNomes | ^40 c3 | [This is my precious, little boy at about the same gestation that scan of their b](https://x.com/RisingNomes/status/2062789349306159350) |
| x | DemNikoArt | ^38 c2 | [You seemed to like this one. The tutorial for it is out now 😉 🔗 below #b3d #blen](https://x.com/DemNikoArt/status/2063295864689262853) |
| x | phillipcparrish | ^37 c6 | [For Immediate Release June 6, 2026 The Conventions That Don't Represent Us: Phil](https://x.com/phillipcparrish/status/2063254062838014426) |
| x | EnochsDegenCrib | ^33 c0 | [🚀 $RENDER Bull Case: Market Dip? What Dip? Fundamentals Are Unbreakable⭕️🚀 Crypt](https://x.com/EnochsDegenCrib/status/2062904565859553483) |
| x | PrakashS720 | ^33 c5 | [Hidden AI Tools That Feel Like Superpowers. 1. https://t.co/6XRECyOn7W – Writing](https://x.com/PrakashS720/status/2062839222139294035) |
| x | alt_Vulcan105 | ^33 c1 | [@cybernetic_sam The only possible answer is that rover civilization is using sim](https://x.com/alt_Vulcan105/status/2062825816980181055) |
| x | MeshyAI | ^18 c1 | [I asked an AI agent to 3D print me as a figurine series! Here's how it works: - ](https://x.com/MeshyAI/status/2062805201480745129) |
| x | multimodalart | ^8 c4 | [where we are headed, all software becomes open source software models can decomp](https://x.com/multimodalart/status/2063307704873951333) |
| x | bilawalsidhu | ^7 c0 | [@sriramk @ayirpelle Congrats on a great run and thank you for your service Srira](https://x.com/bilawalsidhu/status/2063333617506377794) |
| x | multimodalart | ^7 c1 | [Come chill at the CVPR Art Gallery! https://t.co/gVZtxL9C1x](https://x.com/multimodalart/status/2062955857911193835) |
| x | bilawalsidhu | ^5 c1 | [Deep tech founders circa 1910 https://t.co/YyIeQzIwx4](https://x.com/bilawalsidhu/status/2063458023209648517) |
| x | MeshyAI | ^1 c1 | [@_ace_won We have all the tutorials in our Youtube channel. Feel free to check t](https://x.com/MeshyAI/status/2062805649810153960) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1037 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2063276491480105412">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out how Hiroshi Kanazawa showcased this Blender-powered explosion generator — 💥 Really cool progress on this project. What part stands out most to you? 👀 #B3D #Blender3D #Blender #Animation #VFX”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Hiroshi Kanazawa โชว์ explosion generator แบบ procedural ที่สร้างด้วย Blender Geometry Nodes — ยังอยู่ระหว่างพัฒนา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>VFX จาก Geometry Nodes bake เป็น mesh cache แล้ว export เข้า Unity หรืองาน XR ได้ ลดงาน animate มือ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลองทำ explosion VFX ด้วย Geometry Nodes ใน Blender แล้ว bake import เข้า Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2063276491480105412" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@clankrmedia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 768 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/clankrmedia/status/2062988031708000566">View @clankrmedia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wow! Motion capture studios not gonna love this! Just check this insane video. For years, capturing human motion meant markers, skin-tight suits, and hours of cleanup. MAMMA just asks for a few synced”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>MAMMA คือระบบ mocap ไร้ marker ใช้กล้องซิงค์หลายตัว (รวม iPhone 4 เครื่อง) สร้าง 3D body ต่อ frame พร้อม contact-aware tracking แม่นยำระดับ Vicon ลด pipeline จากหลายวันเหลือวันเดียว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Mocap ระดับ Vicon ผ่าน iPhone ลด cost ในการทำ animation data สำหรับ Unity characters และ XR avatars โดยไม่ต้องเช่า studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ติดตาม MAMMA repo รอ public release แล้วทดสอบด้วย iPhone ภายใน studio ดูว่าแทน mocap session ที่จ้างภายนอกสำหรับงาน Unity/XR ได้หรือเปล่า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/clankrmedia/status/2062988031708000566" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@wildmindai</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 275 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/wildmindai/status/2062816526223216995">View @wildmindai on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“3D scene reconstructions by NVIDIA. ArtiFixer - repairs artifacts and extends sparse views via Wan 2.1. - high-fidelity inpainting in occluded regions - gens hundreds of consistent frames in a single ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>NVIDIA เปิดตัว ArtiFixer ใช้ Wan 2.1 ซ่อม artifact และ inpaint ส่วนที่ขาดหายในฉาก 3D แบบ sparse-view แล้ว reconstruct เป็น scene แบบ navigable ผ่าน 3D Gaussian Splatting</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีม VR/XR ใช้แก้ scan คุณภาพต่ำหรือไม่สมบูรณ์แทนการสร้าง scene ใหม่ทั้งหมด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง ArtiFixer กับ scan asset ใน XR pipeline ดูว่าตัดขั้นตอน cleanup manual ใน Gaussian Splatting workflow ได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/wildmindai/status/2062816526223216995" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bestkingsun1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 172 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bestkingsun1/status/2063319729800871957">View @bestkingsun1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Stormcutter model made for a roblox game called &quot;Rise of dragons&quot; Were looking for animators,Vfx designers! https://t.co/iJtEGh00Qe #httyd #HowToTrainYourDragon #dragon #3Dmodel #blender #3dart #3DArt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist อิสระแชร์โมเดล Stormcutter dragon ที่สร้างด้วย Blender สำหรับเกม Roblox ชื่อ 'Rise of Dragons' พร้อมหา animator และ VFX designer</dd>
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
    <span class="ndf-author">@KIRI_Engine_App</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 145 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KIRI_Engine_App/status/2062821750287847445">View @KIRI_Engine_App on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gaussian Splats can now be animated in Blender New 3DGS Render addon update: - Blender 5.1 support - 4DGS / .ply sequence export - Experimental rigging tools - Experimental light baking Check below fo”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>KIRI Engine อัปเดต addon 3DGS สำหรับ Blender รองรับ Gaussian Splat แบบ animated (4DGS) ผ่าน .ply sequence export พร้อม Blender 5.1, rigging และ light baking แบบ experimental</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>4DGS + .ply sequence export เปิดทางนำ Gaussian Splat ที่ animate ได้เข้า Unity และ XR โดยไม่ต้องแปลงเป็น mesh เต็มรูปแบบ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลอง capture scene ด้วย KIRI → animate ใน Blender 5.1 ด้วย addon นี้ → ทดสอบ import .ply sequence เข้า Unity XR pipeline</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KIRI_Engine_App/status/2062821750287847445" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@multimodalart</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 92 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/multimodalart/status/2062938381785403586">View @multimodalart on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I' m so addicted to @GoogleMagenta RealTime 2 🎹 so to justify playing with it 24/7 I ported the real-time apps to @huggingface Spaces 🤗 (and ported the entire lib to pytorch/transformers too) Play liv”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Google Magenta RealTime 2 โมเดล AI สร้างดนตรีแบบ real-time ถูก port ขึ้น Hugging Face Spaces และ PyTorch/Transformers แล้ว โดย @multimodalart</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>port เป็น Transformers แล้ว เรียกใช้ผ่าน HuggingFace API ได้เลย — ไม่ต้อง host เอง เหมาะทดลองทำเพลงใน Unity หรือ XR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Hugging Face Spaces endpoint เป็นแหล่งเพลงพื้นหลังแบบ generative ใน Unity หรือ XR prototype</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/multimodalart/status/2062938381785403586" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 91 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2063272566572159063">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Punjabi in me was exceedingly satisfied. NYC dining is undefeated. https://t.co/CNrnbluZ1e”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์แสดงความพอใจส่วนตัวกับประสบการณ์ทานอาหารใน NYC โดยอ้างถึงเชื้อสาย Punjabi — ไม่มีเนื้อหาด้านเทคนิคหรืออุตสาหกรรม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2063272566572159063" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Stefan_3D_AI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 77 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Stefan_3D_AI/status/2063240740155895943">View @Stefan_3D_AI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“For years, the biggest problem with 3D Gaussian Splatting wasn't quality. It was infrastructure. Huge files. No streaming. No practical way to deploy large scenes. Now we're finally seeing: ✅ LOD syst”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ManyCore Tech แก้ปัญหา deployment ของ 3D Gaussian Splatting ได้แล้ว — LOD, streaming, SPZ compression, collision generation, และ browser rendering ผ่าน WebGPU พร้อมใช้งานจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>3DGS รันใน browser ได้จริงแล้ว — ใช้กับงาน XR/VR walkthrough และ Unity WebGL build ได้โดยไม่ต้องมี server infra เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง SPZ-compressed Gaussian Splats ใน browser-based XR prototype เพื่อเทียบ load time และ quality กับ photogrammetry workflow ที่ใช้อยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Stefan_3D_AI/status/2063240740155895943" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
