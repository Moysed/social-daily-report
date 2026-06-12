---
type: social-topic-report
date: '2026-06-12'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-12T03:34:21+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 51
salience: 0.68
sentiment: mixed
confidence: 0.58
tags:
- gaussian-splatting
- xr
- visionos
- threejs
- blender
- ai-3d-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065109409844334592/img/OxNFlG_QeTBaXhVj.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-12

## TL;DR
- Gaussian Splatting กำลังรวมตัวข้ามหลาย platform ในรอบข่าวเดียวกัน: Apple visionOS 27 รายงานว่าผสาน photogrammetry meshes + splats ใน Apple Maps [21], ABot-Earth 0.5 ของ Alibaba สร้าง 3DGS environments จากภาพถ่ายดาวเทียมในเวลาต่ำกว่า 10 นาที/km² [8], และ Spark รวม splats กับ meshes ใน THREE.js scene เดียวกัน [29].
- Radiance-field/volumetric capture จากอุปกรณ์ multi-camera สำหรับกีฬากลายเป็นไวรัล: การ reconstruct 3D แบบ point-of-view การ tip-in ของ OG Anunoby ได้คะแนน 6112 [1], สร้างจากการผสาน broadcast/Hawkeye-style sensor fusion [46][47].
- งานวิจัยลดขั้นตอนการ capture ลง: Wild3R ทำ feed-forward 3DGS จากภาพถ่ายกระจัดกระจายไม่มีข้อจำกัดผ่าน AnySplat finetune [40], และ PyTorch abstraction ขยาย splatting ข้ามหลาย GPU [25].
- Apple เปิด visionOS 27 + Reality Composer Pro 3 APIs ให้ developer [23], แต่ native splat culling ทำให้ฉากค่อยๆ หายเมื่อเข้าใกล้ — ปัญหาจริงสำหรับ interiors [22].
- กิจกรรมใน traditional DCC pipeline ยังคงสม่ำเสมอ: Houdini 22 keynote กำหนด 17 มิถุนายน [27], Unreal 5.8 Niagara fluids ทำงานราบรื่นขึ้น [26], และ AI asset tools (Meshy [48], Claude Fable 5 [32]) อ้างว่าพิมพ์ chat แล้วได้ rigged mesh.

## สิ่งที่เกิดขึ้น
cluster ที่แข็งแกร่งที่สุดของวันคือ 3D Gaussian Splatting (3DGS) ปรากฏพร้อมกันข้ามหลาย platform และงานวิจัย Apple visionOS 27 รายงานว่า render Apple Maps ด้วย photogrammetry meshes บวก Gaussian splats [21] โดย developer สังเกตเห็น visionOS 27 / Reality Composer Pro 3 APIs ใหม่แต่วิจารณ์เรื่อง splat culling ที่จัดการหนักมือเมื่ออยู่ใกล้ [22][23] Alibaba ปล่อย ABot-Earth 0.5 สร้าง 3DGS environments จากภาพถ่ายดาวเทียมสำหรับ real-time web maps [8] Spark รวม 3DGS เข้ากับ THREE.js pipeline ผสม splat และ mesh objects ข้ามอุปกรณ์ [29] Gracia VR และ Meta Reality Labs ทดสอบ splatting และ volumetric video อย่างหนัก [16] ด้านงานวิจัย Wild3R สร้าง feed-forward 3DGS จากภาพกระจัดกระจายไม่มีข้อจำกัด [40], และ multi-GPU PyTorch abstraction ขยาย reconstruction [25]; อีกเครื่องมือหนึ่ง rebuild ฉากที่เคลื่อนไหวเป็น 4D/dynamic splats ที่นำทางได้จากวิดีโอ [17].

## เหตุใดจึงสำคัญ (เหตุผล)
สัญญาณคือความกว้าง ไม่ใช่การ launch เดี่ยว: splatting โผล่ใน consumer OS [21], ผลิตภัณฑ์ mapping ของ hyperscaler [8], web renderer กระแสหลัก [29], และ lab วิจัยองค์กร [16] ในช่วงเวลาเดียวกัน — รูปแบบนี้มักนำหน้าการที่ format capture-and-delivery กลายเป็นมาตรฐานแทนที่จะทดลอง ผลกระทบลำดับสองที่สำคัญสำหรับ XR/web studio มีสองส่วน ส่วนแรก splat-plus-mesh fusion [29] และ feed-forward capture จากภาพถ่ายทั่วไป [40] ลดต้นทุนผลิต asset ของ photoreal environments ซึ่งแข่งกับ workflow photogrammetry-to-mesh แบบ manual ส่วนที่สอง ข้อจำกัดให้ข้อมูลเท่ากัน: Vision Pro culling ทำลาย use cases interiors [22] และ GTA-style scene ใน THREE.js ยังกระพริบบน materials ที่ซับซ้อน [24] เทคนิคนี้จึงใช้งานได้จริงสำหรับฉากบางประเภทและไม่ได้สำหรับบางประเภท การ reconstruct กีฬาที่ไวรัล [1][46][47] แสดงให้เห็นว่าเทคนิค capture เดิมนั่งอยู่บนโครงสร้างกล้องที่มีอยู่แล้ว แต่นั่นต้องอาศัย multi-camera rigs ที่ studio ส่วนใหญ่ไม่มี

## ความเป็นไปได้
มีแนวโน้มสูง: 3DGS จะตั้งมั่นเป็น delivery format สำหรับ web และ XR scenes ภายในหนึ่งปี เมื่อพิจารณา native OS support [21][23], เส้นทาง THREE.js กระแสหลัก [29], และงานวิจัย capture ที่สุกงอม [40][25]. น่าจะเกิดขึ้น: hybrid splat+mesh pipelines ป้อน engine จริงสำหรับ environment backdrops ขณะที่ interactive geometry ยังเป็น mesh-based [29], เพราะ pure-splat interaction และ culling ยังหยาบ [22]. น่าจะเกิดขึ้นแต่ยังไม่พิสูจน์: AI tools chat-to-asset [48][32] ถึงคุณภาพที่ ship ได้ — หลักฐานปัจจุบันเป็น marketing และ WIP ที่เห็น artifacts ชัด [24]. ไม่น่าเกิดในระยะใกล้: splat interiors ระยะใกล้บน Vision Pro โดยไม่มีการแก้ Apple culling [22].

## การนำไปใช้สำหรับ NDF DEV
ทำเลย: (1) Prototype ฉาก splat แบบ walkable ในเบราว์เซอร์ด้วย Spark/THREE.js เพื่อประเมินสำหรับ web และ XR experiences — effort ต่ำ, ตรงกับ web 3D stack ของ studio [29][45]. (2) ทดลอง AI asset generation (Meshy, Claude Fable 5) ใน prototype edutech/game ที่ใช้ทิ้งเพื่อวัดคุณภาพและความสามารถแก้ไขก่อนเชื่อใจในงาน production — effort ต่ำ [48][32]. (3) ทดสอบ Real Fake Interiors Unity tool สำหรับ effect ห้องที่ตกแต่งแล้วหลังหน้าต่างราคาประหยัดใน mobile/Unity titles — effort ต่ำ, เป็น trick performance ที่รู้จักกันดี [12]. (4) เอา Unity stylized water shader และ Editor mask/channel-packing tool มาเร่ง tech-art iteration — effort ต่ำ [6][20]. (5) ถ้า Vision Pro อยู่ใน roadmap ให้ประเมิน visionOS 27 splat support แต่วางแผนรับมือข้อจำกัด culling ระยะใกล้สำหรับ interiors — effort กลาง [21][22][23]. จับตาดู อย่าเพิ่งทำ: ฟีเจอร์ Houdini 22 (keynote 17 มิถุนายน) [27] และ multi-GPU splat reconstruction [25] — effort สูงในการนำมาใช้. ข้ามไปเลย: broadcast-grade sports reconstruction [1] (ไม่มีโครงสร้างกล้อง), NFT/crypto 3D art [42], และ thread วัฒนธรรม/asset-discourse [14][30][39].

## สัญญาณที่ต้องติดตาม
- Houdini 22 keynote 17 มิถุนายน — ดูฟีเจอร์ procedural/splat หรือ simulation ที่เกี่ยวกับ asset pipelines [27].
- พฤติกรรม Apple visionOS 27 splat culling — ว่า Apple คลาย close-range fade หรือไม่จะตัดสิน interior XR viability [22][23].
- ความสุกงอมของ Spark THREE.js splat+mesh fusion — เส้นทางที่ใช้งานได้โดยตรงที่สุดสำหรับ web stack ของ studio [29].
- Feed-forward splatting จากภาพถ่ายทั่วไป (Wild3R/AnySplat) — ลดต้นทุน capture ถ้า generalize ได้เกิน dataset ใหม่ [40].

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^6112 c47 | [OG Anunoby is too sick. Here is the full point-of-view 3d reconstruction of his ](https://x.com/bilawalsidhu/status/2065109650475712908) |
| x | sai_charan_md | ^584 c1 | [Iridescent Material Blender Tip! Follow for more. #b3d #blender #procedural http](https://x.com/sai_charan_md/status/2064658224440353124) |
| x | luci_animates | ^510 c3 | [Mi Fu's model is available to download for GOO ENGINE (Blender) 4.4.3, check the](https://x.com/luci_animates/status/2064640462749855848) |
| x | IlirAliu_ | ^492 c1 | [One professor at the University of Bonn quietly put his entire robotics curricul](https://x.com/IlirAliu_/status/2064979957009285375) |
| x | StormcoreDev | ^432 c0 | [WIP for water spell "Hydro-Megia." We captured water particles from Blender in c](https://x.com/StormcoreDev/status/2064627351145865449) |
| x | jettelly | ^216 c0 | [Ever wondered how to make a clean, stylized water pipeline VFX in Unity? Here's ](https://x.com/jettelly/status/2064678973775155209) |
| x | afrotron | ^206 c2 | [Rig is done just ironing out some kinks. I'll put it up on my gumroad later this](https://x.com/afrotron/status/2064789451839049861) |
| x | HuggingPapers | ^204 c3 | [Alibaba just released ABot-Earth 0.5 A generative 3D model that builds seamless ](https://x.com/HuggingPapers/status/2064582374315131295) |
| x | delaigrodela | ^154 c1 | [Wednesday, coffee, game dev and intellectual exercises for your brain with Unrea](https://x.com/delaigrodela/status/2064667317636628828) |
| x | sachin_inc | ^148 c9 | [The action of the Returning Officer, who is also the Secretary of the Madhya Pra](https://x.com/sachin_inc/status/2064727133411475762) |
| x | RadianceFields | ^146 c8 | [In the summer of 2023, I cold emailed Jensen Huang and asked to capture a NeRF o](https://x.com/RadianceFields/status/2064766228866924681) |
| x | 80Level | ^136 c1 | [Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo t](https://x.com/80Level/status/2065109302562422981) |
| x | RyanLykos | ^132 c1 | [Zhu Yuan face rig - Work in progress! #blender #rigging https://t.co/3WRnb3gtwv](https://x.com/RyanLykos/status/2065189214413611291) |
| x | zephyyy7 | ^120 c4 | [@Will40746376 @Dexerto funny how last game this same crowd swore "no real woman ](https://x.com/zephyyy7/status/2065112542448374086) |
| x | bilawalsidhu | ^103 c13 | [Wow, this is really cool. Has anyone productized this? I would love to be able t](https://x.com/bilawalsidhu/status/2064865579547193788) |
| x | gracia_vr | ^102 c2 | [We teamed up with researchers at Meta @RealityLabs to stress-test what's actuall](https://x.com/gracia_vr/status/2065106030539997345) |
| x | filicroval | ^101 c7 | [🤖time for another 4D tool! this tool turns videos into moving 3D places film a m](https://x.com/filicroval/status/2064731328210145625) |
| x | DemNikoArt | ^100 c5 | [A small reminder, that this tutorial exists on my YouTube 🚲 And yes, at the end,](https://x.com/DemNikoArt/status/2064712809489879169) |
| x | rmacdon627 | ^96 c3 | [✅ The SAVE America Act (proof of citizenship + photo ID for federal elections) i](https://x.com/rmacdon627/status/2064881931221602482) |
| x | VFX_Therapy | ^76 c0 | [Tired of opening Photoshop for every tiny mask tweak? @KenDeng built a Unity Edi](https://x.com/VFX_Therapy/status/2065035196358094848) |
| x | Azadux | ^64 c5 | [I believe that Apple Maps in visionOS 27 is a combination of photogrammetry mesh](https://x.com/Azadux/status/2064876849252225246) |
| x | iBrews | ^62 c3 | [Apple's new gaussian splatting support is cool, but the culling is kind of ridic](https://x.com/iBrews/status/2064836100720394464) |
| x | xchester16 | ^59 c1 | [After spending some time with the new visionOS 27 APIs and Reality Composer Pro ](https://x.com/xchester16/status/2064900511116185939) |
| x | drashyakuruwa | ^56 c8 | [A minor graphics update to the initial version of my GTA V-style game with @thre](https://x.com/drashyakuruwa/status/2065055670496276601) |
| x | janusch_patas | ^56 c1 | [A Scalable PyTorch Abstraction for Multi-GPU Gaussian Splatting Abstract (excerp](https://x.com/janusch_patas/status/2064965130413048221) |
| x | RedefineFX | ^51 c2 | [Falcon 9 landing real-time VFX in Unreal 5.8, continuing with my space explorati](https://x.com/RedefineFX/status/2065047711477301342) |
| x | sidefx | ^50 c0 | [Houdini 22 launches in London next week! Join us at Curzon Soho Cinema for an ex](https://x.com/sidefx/status/2065141618509005226) |
| x | multimodalart | ^47 c2 | [folks @liquidai trained a specialist tiny model to do one thing rly well: extrac](https://x.com/multimodalart/status/2064864942180679962) |
| x | GithubProjects | ^41 c3 | [Spark integrates 3D Gaussian splatting with the THREE.js rendering pipeline for ](https://x.com/GithubProjects/status/2064807319255515476) |
| x | fistandilus12 | ^40 c2 | [Funny how people who spent 20 years defending Photoshop, CGI, motion capture, pr](https://x.com/fistandilus12/status/2064943228340535490) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6112 · 💬 47</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065109650475712908">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“OG Anunoby is too sick. Here is the full point-of-view 3d reconstruction of his winning tip-in from the Knicks game last night. You can literally relive it from his perspective. Built with viewpoint p”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Viewpoint Pro ใช้กล้อง tracking ในสนาม + Unreal Engine สร้าง POV 3D reconstruction ของ OJ Anunoby จากเกม Knicks แบบ real-time</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เห็น pipeline จริง: multi-camera volumetric capture → Unreal Engine ระดับ live broadcast ซึ่งตรงกับงาน XR/VR ของสตูดิโอ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ศึกษา pipeline ของ Viewpoint Pro เพื่อดูว่า multi-camera → game engine workflow แบบนี้ apply กับงาน XR ของสตูดิโอได้แค่ไหน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2065109650475712908" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sai_charan_md</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 584 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sai_charan_md/status/2064658224440353124">View @sai_charan_md on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Iridescent Material Blender Tip! Follow for more. #b3d #blender #procedural https://t.co/T4xQn2SHuI”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>เทคนิค Blender สาธิตการสร้าง iridescent material แบบ procedural ผ่าน node shading ในรูปแบบ video tutorial สั้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Procedural iridescent shader จาก Blender bake เป็น PBR texture แล้วใช้ใน Unity และ XR scene ได้ตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม 3D ดู node graph แล้วนำเทคนิค iridescent นี้ไปใช้ตอนทำ stylized asset สำหรับ Unity หรือ XR ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sai_charan_md/status/2064658224440353124" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@luci_animates</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 510 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/luci_animates/status/2064640462749855848">View @luci_animates on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mi Fu's model is available to download for GOO ENGINE (Blender) 4.4.3, check the thread below! Huge thanks to @BNBaku for rigging her, and 新杨XIYAG for providing the shader! #GooEngine #Blender https:/”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>มี rigged model ของตัวละคร Mi Fu พร้อม custom shader ให้ดาวน์โหลดฟรีสำหรับ Goo Engine (Blender fork) เวอร์ชัน 4.4.3</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Asset ตัวละคร anime rigged พร้อม shader ให้ทดสอบ NPR rendering pipeline ใน Goo Engine ได้เลยโดยไม่ต้องสร้างเอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ลอง import model นี้เพื่อทดสอบ NPR shading workflow ก่อนตัดสินใจใช้ Goo Engine-to-Unity pipeline</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/luci_animates/status/2064640462749855848" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@IlirAliu_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 492 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/IlirAliu_/status/2064979957009285375">View @IlirAliu_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One professor at the University of Bonn quietly put his entire robotics curriculum on YouTube: SLAM. Sensor fusion. State estimation. Probabilistic robotics. Self-driving cars. Motion planning. Photog”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศาสตราจารย์ Cyrill Stachniss จาก Univ. of Bonn เปิด curriculum robotics เต็มรูปแบบบน YouTube ฟรี ครอบคลุม SLAM, photogrammetry, sensor fusion, motion planning เป็น playlist ครบชุด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Playlist photogrammetry และ SLAM ตรงกับงาน XR/VR 3D reconstruction และ AR spatial tracking โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ให้ทีม XR/VR ใช้ playlist photogrammetry และ SLAM เป็น reference สำหรับงาน spatial mapping หรือ 3D scanning</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/IlirAliu_/status/2064979957009285375" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@StormcoreDev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 432 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/StormcoreDev/status/2064627351145865449">View @StormcoreDev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“WIP for water spell &quot;Hydro-Megia.&quot; We captured water particles from Blender in combination of a customized Mesh distortion in unreal to make it! We'll show you more when other spells are done! #VFX #B”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีม indie รวม Blender particle simulation กับ custom mesh distortion ใน Unreal Engine เพื่อทำ VFX spell น้ำชื่อ 'Hydro-Megia'</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Pipeline Blender → Unreal สำหรับ stylized spell VFX เป็น reference ที่ใช้ได้จริงกับงาน Unity/XR ของ studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง export Blender particle cache เป็น alembic แล้วขับ mesh distortion ผ่าน custom shader graph เพื่อ effect แบบเดียวกัน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/StormcoreDev/status/2064627351145865449" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jettelly</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 216 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jettelly/status/2064678973775155209">View @jettelly on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ever wondered how to make a clean, stylized water pipeline VFX in Unity? Here’s a simple and quick technique you can try! 🌊 Learn more about tech art, shader &amp;amp; tools ✨ https://t.co/gPPcuZDuFX #uni”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Jettelly โชว์เทคนิคทำ stylized water pipeline VFX ใน Unity พร้อม breakdown shader และ tech art</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค shader พร้อมใช้ เหมาะกับ Unity project ที่ต้องการ stylized fluid หรือ pipe VFX</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ดู breakdown นี้เป็น reference ตอนทำ environment หรือ gameplay VFX ที่มี liquid flow หรือ pipeline</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jettelly/status/2064678973775155209" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@afrotron</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 206 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/afrotron/status/2064789451839049861">View @afrotron on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Rig is done just ironing out some kinks. I'll put it up on my gumroad later this month #blender #rigging #anissa #invincible https://t.co/CGVgJltzLt”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist อิสระทำ rig ตัวละคร Anissa จาก Invincible ใน Blender เสร็จแล้ว เตรียมขายบน Gumroad ในเดือนนี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/afrotron/status/2064789451839049861" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HuggingPapers</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 204 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HuggingPapers/status/2064582374315131295">View @HuggingPapers on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Alibaba just released ABot-Earth 0.5 A generative 3D model that builds seamless environments from satellite imagery in under 10 minutes per km². It uses 3D Gaussian Splatting for real-time web maps an”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Alibaba ปล่อย ABot-Earth 0.5 โมเดล generative 3D ที่แปลงภาพถ่ายดาวเทียมเป็น environment 3D ด้วย 3D Gaussian Splatting ใช้เวลาไม่ถึง 10 นาทีต่อ km²</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>3D Gaussian Splatting ระดับ geographic scale ใช้ได้โดยตรงกับงาน XR/VR outdoor scene และ simulation บน Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลองใช้ ABot-Earth 0.5 เป็น pipeline แปลง satellite data เป็น outdoor environment ขนาดใหญ่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HuggingPapers/status/2064582374315131295" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
