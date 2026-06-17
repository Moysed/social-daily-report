---
type: social-topic-report
date: '2026-06-17'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-17T15:37:15+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 37
salience: 0.6
sentiment: mixed
confidence: 0.6
tags:
- gaussian-splatting
- blender
- unity-shaders
- ai-3d
- photogrammetry
- procedural
thumbnail: https://pbs.twimg.com/media/HK7ljsRWMAADR4z.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-17

## TL;DR
- Gaussian splatting กำลังมาถึง consumer hardware: Huawei ส่ง native 3DGS capture ที่ตั้ง splat เป็น lock-screen wallpaper [6][12] พร้อมกับ Apple's Spatial Reframe [6]
- Open-source 4D Gaussian Splatting (4DGS) กำลัง demo การแปลงฟุตเทจ iPhone ธรรมดาเป็น interactive 3D space [19]; KIRI Engine ปล่อย open-source tool ฟรีสำหรับจัดระเบียบภาพ/วิดีโอ scan ดิบ [28]
- AI-to-3D ผ่านจุดสำคัญ: MeshyAI มียอด YouTube 1,000,000 subscribers และกำลัง push '3D Agent' ที่ไปจาก chat ถึงวัตถุที่พิมพ์ 3D ได้ [34][35]
- Blender tooling เปลี่ยน: V-Ray for Blender Update 3 รันบน Linux แล้ว (บวก Windows/macOS) พร้อม native Node Wrangler และ AMD GPU rendering [20]
- Unity real-time shader/VFX content ยังคึกคัก — Unity Shaders Bible กำลัง re-implement 'lemon shader' ใน Shader Graph สัปดาห์นี้ [14] บวก procedural-effects [29] และ toon buff/debuff VFX tutorials [25]

## What happened
สองเรื่อง 3D capture สำหรับ consumer ครองพื้นที่: โทรศัพท์ Huawei capture Gaussian splat แบบ native และตั้งเป็น live wallpaper ได้ [6][12] และการ scan บ้านด้วยโทรศัพท์แล้วอัปโหลดเพื่อ walkthrough ในเบราว์เซอร์ดึงกระทู้ 'real estate is over' จำนวนมาก [8][32] ฝั่ง research/tooling: open-source 4DGS แสดงการแปลงวิดีโอ iPhone เป็น interactive 3D [19], KIRI Engine ส่ง organizer open-source ฟรีสำหรับ scan dataset ที่รกรุงรัง [28] และการเปรียบเทียบ photogrammetry กับ LiDAR ก็แพร่กระจายด้วย [18] AI-to-3D โดดเด่นผ่าน milestone 1M subscribers ของ MeshyAI และ 3D Agent ที่ขับเคลื่อนด้วย chat ผลิตชิ้นงานพิมพ์ 3D ได้ [34][35] บวก agent ที่ใช้ manim เขียน code เพื่อ render และตัดต่อวิดีโอ [4]

## Why it matters (reasoning)
ศูนย์กลางอยู่ที่ capture และ generation ที่ถูกลงและเข้าถึงได้มากขึ้น Native phone Gaussian splatting [6][12] และ free scan-organizing tools [28] ลดต้นทุนผลิต photoreal environment assets สำหรับ XR และ web ซึ่งอยู่ใน asset-production path ของ studio โดยตรง 4DGS จาก monocular video [19] ชี้ไปสู่ dynamic scene ไม่ใช่แค่ static ที่ถูก capture แต่ยังอยู่ระดับ demo AI-to-3D (Meshy [34][35]) ลด ideation-to-asset time แต่ในอดีตให้ topology/quality ที่ไม่เหมาะกับ production rigging และ real-time budgets value ระยะใกล้จึงอยู่ที่ prototyping ไม่ใช่ final assets ขณะที่ win ที่ไม่หวือหวาแต่เชื่อถือได้คือ tool updates จริงๆ: V-Ray บน Linux พร้อม AMD GPU support [20] ขยายตัวเลือก render-farm และกระแส Unity Shader Graph / procedural VFX ที่ต่อเนื่อง [14][25][29] เป็น craft ที่นำไปใช้ได้ทันทีใน game และ XR pipelines

## Possibility
**มีแนวโน้มสูง:** consumer 3DGS capture แพร่กระจายต่อเมื่อ OEM รายใหญ่ส่งแบบ native [6][12] ดึง splat จากความแปลกใหม่ไปสู่ environment-capture format มาตรฐานสำหรับ XR/web **เป็นไปได้:** 4DGS video-to-3D [19] พัฒนาเป็น pipeline ที่ใช้ได้ภายในหนึ่งปี แต่ยังอยู่โหมด research/experimental ระยะใกล้เพราะ surface เป็นแค่ demo **เป็นไปได้:** AI-to-3D tools อย่าง Meshy [34][35] กลายเป็นเรื่องปกติสำหรับ greyboxing และ concept iteration ขณะที่ final game/XR assets ยังต้อง manual cleanup **ไม่น่าเป็นไปได้ (ตามที่ระบุ):** phone scans 'ทำลาย real estate sector' [8][32] — กระทู้เหล่านี้คือ hype; คุณภาพ capture, hosting, และการรวมเข้า workflow ยังไม่ถูกแก้ การ scan บ้านไม่ใช่การ disrupt อุตสาหกรรม

## Org applicability — NDF DEV
1) Pilot Gaussian-splat environment capture สำหรับ XR experiences โดยใช้โทรศัพท์ + KIRI Engine's free organizer [28] และ consumer 3DGS capture [6][12] — effort ต่ำ relevance สูงกับ XR portfolio 2) นำ Unity Shader Graph และ procedural-VFX tutorials ไปใช้โดยตรงใน game/XR VFX work [14][25][29] — effort ต่ำ craft gain ทันที 3) ถ้า render pipeline ใช้ Blender ประเมิน V-Ray Update 3 สำหรับ Linux/AMD GPU rendering เพื่อขยายตัวเลือก hardware [20] — effort ปานกลาง 4) ทดลอง AI-to-3D (Meshy [34][35]) สำหรับ rapid prototyping และ edutech props เท่านั้น ไม่ใช่ production assets — effort ปานกลาง ดู topology ก่อน commit 5) ติดตาม 4DGS [19] สำหรับ dynamic-scene capture แต่ยังอย่าสร้างบนมัน — effort ต่ำ Skip: hype 'disrupt' real estate [8][32], คำชม celebrity/portfolio [21][36][37] และ item นอกหัวข้อ [9][16]

## Signals to Watch
- OEM โทรศัพท์รายอื่นจะตาม Huawei's native 3DGS capture หรือไม่ [6][12] — นั่นจะทำให้ splat เป็น asset format มาตรฐานสำหรับ XR/web
- ความสมบูรณ์ของ open-source 4DGS จาก monocular video สู่ pipeline ที่เสถียรและมี documentation [19]
- คุณภาพและ topology ของ MeshyAI 3D Agent output เมื่อ scale หลัง 1M subs [34][35] — gate สำหรับ production use
- Houdini HIVE/IGNITE ที่ Annecy, June 24–26, สำหรับ procedural-pipeline techniques ที่เกี่ยวกับ asset production [24]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | faenir_morne | ^1680 c11 | [Memories. 2019. I was 25. Short haircut, freckles, young. I got invited to a pho](https://x.com/faenir_morne/status/2066845394235949376) |
| x | c_valenzuelab | ^713 c169 | [Imagine waking up and realizing that your full time job entails using a digital ](https://x.com/c_valenzuelab/status/2066922813466779876) |
| x | 80Level | ^592 c2 | [Have a look at this 90s anime-style shader in Blender by @Jorm_0ff, inspired by ](https://x.com/80Level/status/2066868400261874001) |
| x | IBuzovskyi | ^312 c11 | [HERMES AGENT CAN CREATE VIDEOS. NOT WITH AN API CALL. IT WRITES THE CODE, RENDER](https://x.com/IBuzovskyi/status/2066724948702626255) |
| x | RyanLykos | ^270 c5 | [Zhu Yuan eyebrows rigged! Using a shape key and bone based hybrid! Really happy ](https://x.com/RyanLykos/status/2066995632368238653) |
| x | RadianceFields | ^206 c3 | [Apple may have just launched Spatial Reframe, but Huawei has full on gaussian sp](https://x.com/RadianceFields/status/2066565454035112090) |
| x | mangaka7 | ^185 c7 | [Taking MinusT's SD characters course on Coloso! Finished the base mesh and hair.](https://x.com/mangaka7/status/2066693948031033765) |
| x | DAIEvolutionHub | ^180 c10 | [SOMEONE JUST DESTROYED THE REAL ESTATE SECTOR AND NO ONE IS TALKING ABOUT IT Som](https://x.com/DAIEvolutionHub/status/2066635993844003197) |
| x | RobLooseCannon | ^149 c4 | [Brusselstown Ring sits on a high ridge above the Wicklow lowlands, looking west ](https://x.com/RobLooseCannon/status/2067156169026650154) |
| x | IAmTarrell | ^132 c0 | [I'm shook that he did the set extension himself in Blender. Outside of the found](https://x.com/IAmTarrell/status/2066960069497848157) |
| x | TheNthUmbreon | ^122 c2 | [Finally added a little UV shading to Allie's hair, in addition to the procedural](https://x.com/TheNthUmbreon/status/2067014392907227198) |
| x | bilawalsidhu | ^109 c4 | [China too quick with it. Huawei users can natively capture a 3d gaussian splat a](https://x.com/bilawalsidhu/status/2066617540923490439) |
| x | VijayKu94617363 | ^89 c22 | [A GUY JUST RENDERED AN ENTIRE 3D WORLD IN A BROWSER WITH ZERO ASSETS no game eng](https://x.com/VijayKu94617363/status/2066619575513342248) |
| x | ushadersbible | ^86 c0 | [The lemon shader will come back to the Unity Shaders Bible, but this time implem](https://x.com/ushadersbible/status/2066995211201327466) |
| x | Mix3Design | ^78 c0 | [STOP SCROLLING. If you love anime-style Blender art but can't afford expensive c](https://x.com/Mix3Design/status/2066584516408537510) |
| x | daddyhope | ^75 c14 | [So here are my two cents on the Constitutional Court rulings delivered today aga](https://x.com/daddyhope/status/2067222380917772545) |
| x | fellowshiptrust | ^69 c8 | [Fellowship talks with @john__gerrard john gerrard is a key figure in contemporar](https://x.com/fellowshiptrust/status/2066571096678428902) |
| x | geowgs84 | ^62 c3 | [Photogrammetry vs LiDAR: Key Differences, Accuracy &amp; Use Cases https://t.co/](https://x.com/geowgs84/status/2066728376258486324) |
| x | SciTechera | ^59 c2 | [This could be the future of video 🤯 Open-Source 4DGS Might Be the Future of Vide](https://x.com/SciTechera/status/2066587374340219102) |
| x | theCGchannel | ^57 c0 | [V-Ray for Blender now runs on Linux, as well as Windows and macOS Update 3 to th](https://x.com/theCGchannel/status/2066806757964325072) |
| x | LumaLabsAI | ^53 c4 | [👏 Bravo @PJaccetturo !](https://x.com/LumaLabsAI/status/2066911030081700342) |
| x | auqibhabib | ^51 c28 | [Made with seedance 2.0 + GPT image 2.0 on @renoiseai Prompt: @Image1 fights thre](https://x.com/auqibhabib/status/2066796169813221848) |
| x | meifumaudo | ^46 c0 | [@OverlyXGamer He's mentioned a lot of film was traditional vfx pipeline, but a g](https://x.com/meifumaudo/status/2067018945819766892) |
| x | sidefx | ^46 c1 | [SideFX is proud to be hosting Houdini HIVE Talks and IGNITE Workshops at the Ann](https://x.com/sidefx/status/2066611110804152601) |
| x | GabrielAguiarFX | ^44 c1 | [Quick Buffs and Debuffs with a toon touch! #VFX #gamedev #realtimeVFX #Unity #Ga](https://x.com/GabrielAguiarFX/status/2066556366135717958) |
| x | palelzr | ^37 c0 | [stylized sculpted planet namek map VFX: @Suntora69 #Roblox #RobloxDev #Blender #](https://x.com/palelzr/status/2067007081421717663) |
| x | ScansFactory | ^36 c0 | [Details are a priority for us, right from location scanning all the way to the f](https://x.com/ScansFactory/status/2066928795093967220) |
| x | KIRI_Engine_App | ^36 c2 | [We came back from travelling with thousands of 3D scan photos, random shots, vid](https://x.com/KIRI_Engine_App/status/2066797002453905771) |
| x | jettelly | ^35 c1 | [Creating procedural effects in Unity can feel like magic until you understand th](https://x.com/jettelly/status/2066566411020021942) |
| x | nxpatterns | ^35 c2 | [Open the video in the YouTube app on your phone (not the browser). Now literally](https://x.com/nxpatterns/status/2066858675679990063) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@faenir_morne</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1680 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/faenir_morne/status/2066845394235949376">View @faenir_morne on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Memories. 2019. I was 25. Short haircut, freckles, young. I got invited to a photogrammetry studio! Dozens of cameras were shooting me from every angle while I froze in different poses. It was an incr”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Creator เล่าความทรงจำปี 2019 ตอนถูก scan ด้วย photogrammetry หลายสิบกล้อง โปรเจกต์ทำ collectible figure พังเพราะ COVID</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/faenir_morne/status/2066845394235949376" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@c_valenzuelab</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 713 · 💬 169</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/c_valenzuelab/status/2066922813466779876">View @c_valenzuelab on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Imagine waking up and realizing that your full time job entails using a digital cinema camera with a 65mm large format CMOS sensor fabricated on a sub-20nm semiconductor process, capturing 16-bit line”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักทำหนังแจง pipeline ดิจิทัลเบื้องหลัง cinema 'จริง' — ACES, ML denoising, optical flow, NeRF, photogrammetry, LiDAR, ray tracing — ชี้ว่ามัน artificial มาตลอด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>stack ที่ยกมา — NeRF, photogrammetry, LiDAR, ML denoising, PBR, ray tracing — ตรงกับ tools ที่ Unity และ XR production ใช้อยู่แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/Unity audit ว่า stage ไหน (ACES, photogrammetry, ML denoising, NeRF) ใช้งานอยู่แล้ว และ gap ไหนควรปิด</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/c_valenzuelab/status/2066922813466779876" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@80Level</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 592 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/80Level/status/2066868400261874001">View @80Level on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Have a look at this 90s anime-style shader in Blender by @Jorm_0ff, inspired by Vampire Hunter D. Learn anime-style 3D art in Blender: https://t.co/oQWmnrl5PT https://t.co/jGEINgDAhI”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist Jorm_0ff สร้าง cel shader สไตล์อนิเมะยุค 90s ใน Blender โดยได้แรงบันดาลใจจาก Vampire Hunter D พร้อม link tutorial จาก 80Level</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cel shading สไตล์นี้ใน Blender ช่วยสร้าง visual identity ให้ Unity project โดยไม่ต้องเขียน custom shader เพิ่ม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม art ดู breakdown ของ shader นี้แล้ว replicate ด้วย Shader Graph ใน Unity สำหรับ project แนว stylized</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/80Level/status/2066868400261874001" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IBuzovskyi</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 312 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IBuzovskyi/status/2066724948702626255">View @IBuzovskyi on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“HERMES AGENT CAN CREATE VIDEOS. NOT WITH AN API CALL. IT WRITES THE CODE, RENDERS THE SCENES, AND STITCHES THEM INTO AN MP4. the video attached to this post was generated by Hermes Agent using manim-v”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Hermes Agent สร้าง MP4 โดยเขียน Python/Manim code, render ฉาก แล้ว stitch รวม — มีสอง skill: Manim CE สำหรับ animation algorithm และ HyperFrames สำหรับ motion graphics ผ่าน HTML+GSAP</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Manim pipeline ตรงกับ workflow e-learning explainer ที่ studio ทำ manual อยู่ เป็น automation candidate ตรงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Manim pipeline กับ e-learning module ที่มีอยู่ วัดว่าลด production time ได้จริงไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IBuzovskyi/status/2066724948702626255" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 270 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2066995632368238653">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Zhu Yuan eyebrows rigged! Using a shape key and bone based hybrid! Really happy with how it looks, it's pretty incredible how expressive eyebrows can be😄 #blender #rig #rigging https://t.co/skdk3rAuDE”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปิน Blender ทำ rig คิ้วด้วย hybrid ระหว่าง shape key กับ bone แสดงให้เห็นว่า combo นี้ให้ facial expression ได้ดีแค่ไหน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Hybrid shape key + bone ให้ facial movement ละเอียดกว่า bone เดี่ยว — ใช้ได้โดยตรงกับ character และ XR avatar pipeline ใน Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง hybrid rig แบบนี้ใน Blender ก่อน export เพื่อเพิ่ม expressiveness ให้ตัวละครหรือ XR avatar</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2066995632368238653" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RadianceFields</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 206 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RadianceFields/status/2066565454035112090">View @RadianceFields on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Apple may have just launched Spatial Reframe, but Huawei has full on gaussian splatting on lock screens. https://t.co/IdoITBcZxr”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Huawei ปล่อย Gaussian splatting แบบ real-time บน lock screen ของมือถือผู้บริโภคแล้ว ก้าวข้าม Apple Spatial Reframe ที่แค่ reframe spatial video ให้จอปกติ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า 3DGS รัน real-time บน mobile GPU ของผู้บริโภคได้แล้ว — เป็น hardware baseline ที่ทีม XR/VR ใช้วางแผน pipeline ได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity XR ทดสอบ UnityGaussianSplatting บน mobile hardware เป้าหมายได้เลย เพราะ consumer device พิสูจน์แล้วว่ารับได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RadianceFields/status/2066565454035112090" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mangaka7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 185 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mangaka7/status/2066693948031033765">View @mangaka7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Taking MinusT's SD characters course on Coloso! Finished the base mesh and hair. Will work on clothing next and then move on to texturing and rigging! I'm new to Blender. What do you think? Any feedba”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>มือใหม่ Blender แชร์ความคืบหน้าการสร้างตัวละคร SD จากคอร์ส MinusT บน Coloso — ทำ base mesh และ hair เสร็จแล้ว ยังเหลือ clothing, texturing, rigging</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mangaka7/status/2066693948031033765" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DAIEvolutionHub</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 180 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DAIEvolutionHub/status/2066635993844003197">View @DAIEvolutionHub on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“SOMEONE JUST DESTROYED THE REAL ESTATE SECTOR AND NO ONE IS TALKING ABOUT IT Someone scanned an entire house with their phone. They uploaded it. Now anyone on earth can walk through it from their brow”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>3D Gaussian Splatting ที่ใช้ AI แปลงรูปโทรศัพท์เป็น splat scene มี browser viewer open-source บน PlayCanvas แล้ว ต้นทุน scan ~$200 ต่อสถานที่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Gaussian splat scene ที่รันใน browser โดยไม่ต้อง install app ตรงกับงาน XR/VR และ e-learning ของ studio ที่ต้องการ walkthrough สถานที่จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Clone PlayCanvas Gaussian Splatting repo, สแกนสถานที่จริงด้วยโทรศัพท์ แล้ว benchmark load time และ visual quality เทียบกับ XR pipeline ปัจจุบันของ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DAIEvolutionHub/status/2066635993844003197" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
