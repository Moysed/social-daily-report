---
type: social-topic-report
date: '2026-06-11'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-11T03:50:55+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 58
salience: 0.7
sentiment: positive
confidence: 0.6
tags:
- gaussian-splatting
- apple-maps
- xr
- luma-ray3
- blender
- ai-assets
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2064357961254793216/img/mePCpXHgLsopIcYe.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-11

## TL;DR
- Apple กำลังนำ 3D Gaussian Splatting มาใช้ใน Apple Maps Flyover (300+ เมือง) ฤดูใบไม้ร่วงนี้ เปิดให้ใช้แล้วใน visionOS 27 / developer beta; หลายแหล่งระบุว่า Apple ส่ง splats ใน maps ก่อน Google [11][21][25][28][38][41][45]
- ดูเหมือนจะเป็น hybrid ระหว่าง photogrammetry meshes + Gaussian splats และ visionOS sample รันได้บน device จริงเท่านั้น (ไม่รองรับ simulator) โดยมีระบบ culling แบบ aggressive ที่ fade splats เมื่อเข้าใกล้ — ปัญหาสำหรับ interior [32][45][47]
- Luma Labs เปิดตัว Ray3.2 พร้อม developer API: ควบคุม 16 keyframe ต่อคลิป, Modify Video V2 (สูงสุด 20 วินาทีที่ 1080p), export HDR native และ 16-bit EXR สำหรับ compositing ใน Resolve/Nuke [1][15][33][52][54]
- Splat tooling กำลังพัฒนาสู่ production pipelines: Spark รวม splats + mesh ใน THREE.js สำหรับ web rendering ข้ามอุปกรณ์ [40]; ColmapView v0.7 เพิ่มฟีเจอร์ 3DGS QA [16]; ABot-Earth 0.5 ของ Alibaba สร้าง splat environments จากภาพถ่ายดาวเทียมได้ใน 10 นาที/km² [17]
- AI asset/sim generation เริ่มปรากฏในงาน graphics: Claude 'Fable/Mythos' สร้าง city-block traffic simulator ใน prompt เดียว [2] และสร้าง Spawn 5.0 ด้วย 1,687 prompts [6]; Meshy สร้าง arcade scene เต็มรูปแบบจาก chat เดียว [57]

## สิ่งที่เกิดขึ้น
ประเด็นหลักคือ Apple เพิ่ม 3D Gaussian Splatting ใน Apple Maps เปิดตัวที่ WWDC และปัจจุบันอยู่ใน developer beta / visionOS 27 ครอบคลุม 300+ เมืองของ Flyover ในฤดูใบไม้ร่วงนี้ [11][21][28][38][41] จากการตรวจสอบพบว่าเป็น photogrammetry-mesh + splat hybrid ที่สร้างจากภาพถ่ายทางอากาศแบบเฉียง [38][45] ข้อจำกัดที่เห็นได้ชัดอยู่แล้ว: splats render บน device ได้แต่ไม่ได้ใน simulator [47] และ Vision Pro culling จะ fade splats เมื่อเข้าใกล้ ทำให้ใช้กับ interior ไม่ได้ [32] Google ถูกระบุว่าส่ง splats ก่อน แต่จำกัดอยู่แค่ใน immersive/indoor view [25]

## ทำไมถึงสำคัญ (เหตุผล)
มีสองเส้นที่มาบรรจบกัน ประการแรก Gaussian Splatting กำลังเคลื่อนจาก research demos เข้าสู่ผลิตภัณฑ์ consumer และ developer ที่ ship จริง (Apple Maps [11], THREE.js ผ่าน Spark [40], การสร้างจากดาวเทียม [17], การ capture สินค้าด้วยสมาร์ทโฟนผ่าน Supra [46]) พร้อม QA tooling ที่เริ่มมี [16] — ลดต้นทุนการ capture 3D แบบ photoreal สำหรับ XR และ web ไปมาก สำหรับสตูดิโอที่ทำ XR/VR และ web/mobile จุดที่ unlock ได้จริงคือ splat+mesh fusion ใน standard web renderers [40] และการรองรับ on-device บน Vision Pro [45] แม้ว่า culling และ simulator limits [32][47] จะหมายความว่า Apple splats ในปัจจุบันยังอยู่ระดับ sightseeing ยังไม่ถึงขั้น interaction-grade สำหรับ interior ประการที่สอง Ray3.2 ของ Luma [1][54] และ AI scene/asset generators [2][57] ผลักเครื่องมือ generative media ลึกเข้าไปใน VFX/asset pipelines มากขึ้น จุดเชื่อมโยงที่ใช้งานได้จริงคือ EXR/HDR export ที่ทำให้ AI output composite เข้ากับ live plates ได้ [54] ไม่ใช่แค่ marketing claims นอกจากนี้ยังมีข้อกังวลเรื่อง trust ที่พบว่า model แก้ไข output โดยไม่แจ้งผู้ใช้ [29] ซึ่งสำคัญมากสำหรับ pipeline ที่ต้องการผลลัพธ์ที่ deterministic

## ความเป็นไปได้
น่าจะเกิด: Gaussian Splatting กลายเป็น standard capture format สำหรับ web/XR scene backdrops ภายในปีหน้า เพราะ ship พร้อมกันทั้ง Apple [11], THREE.js [40] และ generation tools [17][26] เป็นไปได้: Apple ส่ง Vision Pro Maps/splat app เต็มรูปแบบ ซึ่งนักพัฒนาหลายคนเรียกร้องชัดเจน [21][55] — แต่ culling behavior [32] บ่งบอกว่า interior-quality splats ยังไม่พร้อม ดังนั้น near-term ยังอยู่แค่ exterior/flyover เป็นไปได้: AI video tools อย่าง Ray3.2 ถูกนำมาใช้สำหรับ previz และ B-roll ที่รองรับ EXR/HDR compositing [54] ไม่ใช่ hero shots หลัก ไม่น่าจะเกิดใน near-term: AI scene generators แบบ one-shot [2][57] แทนที่ hand-authored asset pipelines สำหรับ game/XR ที่ ship จริง — demos ดูน่าประทับใจแต่ยังไม่ได้รับการตรวจสอบสำหรับ production constraints และข้อกังวลเรื่องการ manipulate output [29] ทำให้ความน่าเชื่อถือลดลง ไม่มีแหล่งใดระบุความน่าจะเป็นเป็นตัวเลข

## การนำไปใช้สำหรับ NDF DEV
1) ประเมิน Spark สำหรับ splat+mesh ใน web/mobile XR experiences (effort ต่ำ) — targets THREE.js stack ที่สตูดิโอน่าจะใช้อยู่แล้ว รองรับ cross-device rendering [40] 2) ทดลอง smartphone-to-splat product/asset capture flow สำหรับ client หรือ game props โดยใช้ Supra/TripoSplat-style tools พร้อม ColmapView สำหรับ QA ก่อน ingest (effort กลาง) [16][26][46] 3) ถ้า Vision Pro splat experience อยู่ใน roadmap ให้ทดสอบตอนนี้เลย แต่ออกแบบสำหรับ exterior เท่านั้นและ verify บน device จริง — จดข้อจำกัด simulator gap และ close-range culling ก่อน commit [32][45][47] 4) สำหรับงาน AI-video/VFX ให้ gate การนำมาใช้ตาม EXR/HDR export compatibility กับ compositing tooling ของทีม (effort ต่ำ-กลาง) [54]; ใช้ one-shot scene generators [2][57] สำหรับ previz เท่านั้น ข้าม: Apple Maps splat integration เป็น dependency (เป็น consumer feature ไม่ใช่ SDK ที่ build ได้) [11]; รายการการเมืองที่ไม่เกี่ยวข้อง [9][27]; vendor reframe/aspect-ratio claims [53][58] จนกว่าจะทดสอบ งดพึ่งพา model ที่ alter output โดยไม่แจ้งจนกว่า behavior นั้นจะได้รับการชี้แจง [29]

## สัญญาณที่ต้องจับตา
- Apple จะ expose splats ผ่าน developer SDK หรือล็อคไว้แค่ใน Maps — เป็นตัวกำหนดว่าสตูดิโอสามารถ build บนนั้นได้หรือเปล่า [21][55]
- Vision Pro splat culling behavior ใน visionOS 27 betas รุ่นต่อๆ ไป — ถ้าแก้ close-range fade ได้จะเปิดทาง interior XR ได้ [32]
- ความสมบูรณ์ของ Spark สำหรับ splat+mesh fusion ใน THREE.js ในฐานะ web-XR delivery path [40]
- Generative splat-from-imagery (ABot-Earth) และ one-chat asset tools (Meshy) สำหรับ rapid environment prototyping [17][57]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | LumaLabsAI | ^3624 c36 | [Direction goes in. Cinema comes out. Ray3.2 is here → https://t.co/TuAuFhZDBn ht](https://x.com/LumaLabsAI/status/2064358414143143954) |
| x | bilawalsidhu | ^1876 c76 | [Just used claude fable (aka mythos) to create this city block simulator complete](https://x.com/bilawalsidhu/status/2064524211914223867) |
| x | ItzFAILURE | ^1675 c13 | [Added another whole 10 seconds! Next im adding the "first person" part... who co](https://x.com/ItzFAILURE/status/2064504962189492495) |
| x | luci_animates | ^490 c3 | [Mi Fu's model is available to download for GOO ENGINE (Blender) 4.4.3, check the](https://x.com/luci_animates/status/2064640462749855848) |
| x | sai_charan_md | ^463 c1 | [Iridescent Material Blender Tip! Follow for more. #b3d #blender #procedural http](https://x.com/sai_charan_md/status/2064658224440353124) |
| x | jsnnsa | ^250 c22 | [claude fable 5 is live. spawn 5.0 was built with it: 1,687 prompts, 102 sessions](https://x.com/jsnnsa/status/2064420561078693941) |
| x | StormcoreDev | ^178 c0 | [WIP for water spell "Hydro-Megia." We captured water particles from Blender in c](https://x.com/StormcoreDev/status/2064627351145865449) |
| x | suni_mlb | ^165 c6 | [Chrysalis V2 WIP (Made by Amal and me) 🦋 #mlbtwt #mlbs6spoilers I'll port it to ](https://x.com/suni_mlb/status/2064294999622078894) |
| x | sachin_inc | ^131 c7 | [The action of the Returning Officer, who is also the Secretary of the Madhya Pra](https://x.com/sachin_inc/status/2064727133411475762) |
| x | jettelly | ^130 c1 | [Technical artist Chintan Vadgama broke down a parametric lightning shader he mad](https://x.com/jettelly/status/2064226059176837462) |
| x | heyshrutimishra | ^125 c4 | [WOW. 😳 Apple just quietly won the 3D maps war at WWDC. Gaussian Splatting is com](https://x.com/heyshrutimishra/status/2064191739444043915) |
| x | delaigrodela | ^119 c1 | [Wednesday, coffee, game dev and intellectual exercises for your brain with Unrea](https://x.com/delaigrodela/status/2064667317636628828) |
| x | jettelly | ^114 c0 | [Ever wondered how to make a clean, stylized water pipeline VFX in Unity? Here's ](https://x.com/jettelly/status/2064678973775155209) |
| x | RadianceFields | ^107 c7 | [In the summer of 2023, I cold emailed Jensen Huang and asked to capture a NeRF o](https://x.com/RadianceFields/status/2064766228866924681) |
| x | LumaLabsAI | ^105 c12 | [The Ray3.2 API runs cinematic-grade at scale and integrates into the products yo](https://x.com/LumaLabsAI/status/2064389582997897216) |
| x | YeheLiu | ^97 c4 | [Want to catch bad images in your SFM reconstruction? Introducing ColmapView v0.7](https://x.com/YeheLiu/status/2064450666567983306) |
| x | HuggingPapers | ^90 c2 | [Alibaba just released ABot-Earth 0.5 A generative 3D model that builds seamless ](https://x.com/HuggingPapers/status/2064582374315131295) |
| x | afrotron | ^89 c2 | [Rig is done just ironing out some kinks. I'll put it up on my gumroad later this](https://x.com/afrotron/status/2064789451839049861) |
| x | mattsmodel12 | ^89 c2 | [From dynamic textures to fully playable.. Tested the character's movement, riggi](https://x.com/mattsmodel12/status/2064205785928708532) |
| x | DemNikoArt | ^87 c5 | [A small reminder, that this tutorial exists on my YouTube 🚲 And yes, at the end,](https://x.com/DemNikoArt/status/2064712809489879169) |
| x | bilawalsidhu | ^84 c3 | [Apple's gaussian splat maps are rolling out on the developer beta! I hope they m](https://x.com/bilawalsidhu/status/2064494805023911966) |
| x | filicroval | ^72 c6 | [🤖time for another 4D tool! this tool turns videos into moving 3D places film a m](https://x.com/filicroval/status/2064731328210145625) |
| x | BiboPlayer | ^58 c10 | [I wanted to share how much money I've spent developing Nuclear Tycoon, because I](https://x.com/BiboPlayer/status/2064380780537610670) |
| x | GabrielAguiarFX | ^56 c1 | [Toxic Waterfall made with Niagara on Unreal Engine! ☢️ And published a tutorial ](https://x.com/GabrielAguiarFX/status/2064389240721387732) |
| x | bilawalsidhu | ^55 c6 | [ICYMI google's been shipping gaussian splats in maps for a while -- but tucked i](https://x.com/bilawalsidhu/status/2064187152930365502) |
| x | mishig25 | ^51 c4 | [Created gaussian splats website for famous Paris monuments. Connected my claude ](https://x.com/mishig25/status/2064304062263066653) |
| x | rmacdon627 | ^47 c1 | [✅ The SAVE America Act (proof of citizenship + photo ID for federal elections) i](https://x.com/rmacdon627/status/2064881931221602482) |
| x | DataChaz | ^42 c7 | [CAN WE TALK ABOUT HOW APPLE MAPS JUST CASUALLY DROPPED 3D GAUSSIAN SPLATTING BEF](https://x.com/DataChaz/status/2064248196906561859) |
| x | multimodalart | ^41 c4 | [this is very odd manipulating the output without informing the user is a terribl](https://x.com/multimodalart/status/2064426820380860881) |
| x | aidan_3d_art | ^39 c2 | [Meet my latest blender 3D character 👜 This is my first time creating a full body](https://x.com/aidan_3d_art/status/2064328659578544610) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LumaLabsAI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3624 · 💬 36</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LumaLabsAI/status/2064358414143143954">View @LumaLabsAI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Direction goes in. Cinema comes out. Ray3.2 is here → https://t.co/TuAuFhZDBn https://t.co/nAMqwBvrAK”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Luma Labs ปล่อย Ray3.2 โมเดล AI สร้างวิดีโอที่รับ prompt แนวทางแล้วสร้างภาพคุณภาพระดับหนัง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>studio เล็กใช้ Ray3.2 ต่อยอด prototype cutscene เกมหรือ video e-learning ได้โดยไม่ต้องมีทีม production</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Ray3.2 กับ script เกม Unity หรือ e-learning สักชิ้นก่อน แล้วประเมิน output ก่อน adopt จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LumaLabsAI/status/2064358414143143954" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1876 · 💬 76</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2064524211914223867">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Just used claude fable (aka mythos) to create this city block simulator complete with multi-agent traffic, live detection boxes + tracks, and day to night cycle. And it just one shotted it. This is go”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Claude Fable (ชื่อภายใน Mythos) สร้าง city block simulator พร้อม multi-agent traffic, live bounding-box tracking และ day/night cycle ได้ใน prompt เดียว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การ one-shot scene ที่มีหลาย system แสดงว่า Fable แรงกว่า Claude รุ่นก่อนในงาน spatial/simulation code — ตรงกับงาน XR และ game ของทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง prompt scene Unity หรือ XR ที่มีหลาย system ผ่าน Claude Fable เพื่อวัดคุณภาพ one-shot เทียบกับ workflow prototype ปัจจุบัน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2064524211914223867" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ItzFAILURE</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1675 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ItzFAILURE/status/2064504962189492495">View @ItzFAILURE on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Added another whole 10 seconds! Next im adding the &quot;first person&quot; part... who could she be singing to? 👀 Model: @Artstudious Rig: @cookie_sugar42 Shader: @LuminaryOfAges Textures: @Hiru3152 #RWBY #FND”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักแอนิเมชัน indie โพสต์ความคืบหน้า fan animation สั้น 10 วินาที สำหรับซีรีส์ RWBY ทำใน Blender โดยเครดิตทีมแยกสำหรับ model, rig, shader และ texture</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ItzFAILURE/status/2064504962189492495" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@luci_animates</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 490 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/luci_animates/status/2064640462749855848">View @luci_animates on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mi Fu's model is available to download for GOO ENGINE (Blender) 4.4.3, check the thread below! Huge thanks to @BNBaku for rigging her, and 新杨XIYAG for providing the shader! #GooEngine #Blender https:/”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โมเดล 3D ของ Mi Fu พร้อม rig และ shader วางให้ดาวน์โหลดฟรีสำหรับ Goo Engine (Blender) 4.4.3 แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัวละคร anime style ที่ rig ครบพร้อม shader ช่วยลดเวลา setup เมื่อทีม Unity หรือ XR ต้องการ humanoid placeholder ตอน prototype</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดาวน์โหลดเป็น placeholder asset สำหรับ prototype Unity หรือ XR แล้ว export จาก Blender เป็น FBX เพื่อนำ rig เข้า Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/luci_animates/status/2064640462749855848" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@sai_charan_md</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 463 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sai_charan_md/status/2064658224440353124">View @sai_charan_md on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Iridescent Material Blender Tip! Follow for more. #b3d #blender #procedural https://t.co/T4xQn2SHuI”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist แชร์ node setup แบบ procedural ใน Blender สำหรับทำ iridescent material ที่เปลี่ยนสีตามมุมมอง โดยไม่ต้องวาด texture</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Node setup แบบนี้ใช้เป็น reference ทำ iridescent shader ใน Unity Shader Graph หรือ URP/HDRP สำหรับ asset ใน XR หรือเกมได้ตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR ดู node logic แล้ว port เป็น Shader Graph หรือ bake เป็น texture atlas สำหรับ mobile/XR ที่ performance จำกัดได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sai_charan_md/status/2064658224440353124" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jsnnsa</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 250 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jsnnsa/status/2064420561078693941">View @jsnnsa on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“claude fable 5 is live. spawn 5.0 was built with it: 1,687 prompts, 102 sessions, my job shifted from architecture to judging taste. what we built, each of which would've been at least a month with a ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้สร้าง Spawn 5.0 ใช้ Claude Fable 5 ใน 102 sessions สร้าง physics engine, clustered froxel lighting (1,000+ dynamic lights), realtime diffuse GI บน WebGPU มือถือ และ GPU VFX ล้าน particle ใน ~1 สัปดาห์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Froxel lighting และ WebGPU realtime GI ตรงกับงาน Unity/XR และ 3D web ของ studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม graphics ดู changelog และ shader architecture ของ Spawn 5.0 ก่อน sprint WebGPU หรือ Unity VFX ครั้งหน้า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jsnnsa/status/2064420561078693941" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@StormcoreDev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 178 · 💬 0</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/StormcoreDev/status/2064627351145865449">View @StormcoreDev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“WIP for water spell &quot;Hydro-Megia.&quot; We captured water particles from Blender in combination of a customized Mesh distortion in unreal to make it! We'll show you more when other spells are done! #VFX #B”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีม indie ใช้ particle sim จาก Blender bake เป็น mesh แล้วทำ mesh distortion ใน Unreal Engine สร้าง water spell VFX ชื่อ 'Hydro-Megia'</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>pipeline Blender → Unreal นี้ใช้แนวเดียวกับ Unity VFX Graph ได้เลย — bake particle แล้วทำ mesh distortion แทน particle live</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง bake water sim จาก Blender เป็น mesh sequence แล้วขับ distortion ผ่าน VFX Graph หรือ custom shader ใน Unity สำหรับ spell effects</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/StormcoreDev/status/2064627351145865449" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@suni_mlb</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 165 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/suni_mlb/status/2064294999622078894">View @suni_mlb on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Chrysalis V2 WIP (Made by Amal and me) 🦋 #mlbtwt #mlbs6spoilers I'll port it to Unreal once I finish rigging https://t.co/uV9qKABwdD”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปินสองคนโชว์ 3D character WIP ชื่อ 'Chrysalis V2' จาก fandom Miraculous Ladybug พร้อมบอกว่าจะ port ไป Unreal Engine หลัง rig เสร็จ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/suni_mlb/status/2064294999622078894" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
