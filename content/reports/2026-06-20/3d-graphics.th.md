---
type: social-topic-report
date: '2026-06-20'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-20T15:34:33+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 38
salience: 0.6
sentiment: positive
confidence: 0.6
tags:
- gaussian-splatting
- rigging
- procedural
- unity
- unreal
- photogrammetry
thumbnail: https://pbs.twimg.com/media/HLIIhNGW0AAmH6T.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-20

## TL;DR
- Gaussian Splatting ครองวันนี้ในทุก use case: Apple Maps ใช้ 3D Gaussian Splatting [26], 4D splats สำหรับดูกีฬา [2], ทดสอบ drone แบบ 360 vs มาตรฐานสำหรับ splat [7], และ Volograms เร่งทำให้ 4D GS รันบน camera rig ขนาดเล็กลง [28]
- เครื่องมือ character pipeline: Advanced Skeleton แก้ปัญหา Unreal rig พังด้วย non-destructive rigging [1], Epic ปล่อย animation/rigging toolset ฟรีใน Unreal Engine 5.8 (รวม DMC) พร้อม Zebra Character Sample [21], และหลายโพสต์เรื่อง face rig ใน Blender ลงเอยที่ 'ARKit shape keys น้อยกว่า = ดีกว่า' [16]
- สร้าง environment แบบ procedural จากข้อมูลจริง: pipeline แปลง Copernicus DEM + OpenStreetMap เป็นแผนที่เกม isometric [8], และ Alibaba's Mapping Lab สร้าง 3D city สมจริงขนาด 1 ตร.กม. จากภาพดาวเทียม 2D ภายใน ~10 นาที [19]
- Unity GPU shader: dynamic wireframe shader ที่ใช้ topology จริงสร้าง runtime ใน Shader Graph โดยไม่ต้อง preprocess mesh [13][25], และ demo วาดภาพด้วย compute shader [18]
- Houdini 22 keynote สตรีม 22 มิ.ย. 2026 มี Copernicus tools ใหม่เป็น highlight [14]; open-source Mac-GPU library สำหรับ NeRF/Gaussian Splatting/differentiable rendering ออก v0.2.0 [10][30]

## What happened
Gaussian Splatting เป็น cluster ที่ชัดที่สุด: Apple Maps นำ 3DGS มาใช้เพราะหน้าตาสมจริง [26], กีฬาถ่ายเป็น 4D splat [2], เปรียบเทียบ drone capture สำหรับคุณภาพ splat [7], reconstruction ผึ้งด้วย splat แบบไม่ใช้ AI [29], และ Volograms รายงานความคืบหน้า 4D GS บน camera rig ที่หนาแน่นน้อยลง [28] ควบคู่กัน ฝั่ง character/rigging tooling มี release และ tip ที่จับต้องได้: Epic ปล่อย UE 5.8 rigging toolset ฟรีพร้อม Zebra sample [21], Advanced Skeleton non-destructive rigging [1], และข้อค้นพบ face rig ใน Blender ที่เน้น ARKit shape keys น้อย [16] บวก mouth correctives [3] Pipeline สร้างจากข้อมูลจริงปรากฏทั้งสองด้าน: DEM+OSM → แผนที่เกม isometric [8] และ satellite → 3D city ใน ~10 นาที [19]

## Why it matters (reasoning)
ธีมหลักที่ซ้ำอยู่คือ real-world capture และ procedural generation ที่ป้อนเข้า game/XR pipeline ซึ่งตรงกับปัญหา asset production ของ NDF DEV โดยตรง การที่ Apple Maps ใช้งาน Gaussian Splatting [26] คือสัญญาณความพร้อมที่แข็งแกร่งที่สุด — product ระดับ consumer ที่ scale จริงยืนยัน GS ว่าใช้งานได้ใน production จริง ไม่ใช่แค่งานวิจัย สิ่งนี้ลด risk ในการสร้าง XR experience (heritage sites, locations) บน splat capture ผลทางอ้อม: เมื่อ 4D/dynamic splat capture ย้ายไปใช้ rig เล็กลง [28] barrier ด้านฮาร์ดแวร์สำหรับ volumetric/dynamic content จะลดลงจนสตูดิโอขนาดเล็กเข้าถึงได้ ด้าน tooling เช่น asset ฟรีจากผู้พัฒนา (UE 5.8 toolset [21]) และ shader ที่สร้าง runtime โดยไม่ต้อง preprocess [13][25] ลด friction ในการ integrate หลายโพสต์ที่ engagement สูงเป็นการตลาดหรือ hype ที่ควร discount: การโปรโมต Luma 'Skills' ซ้ำหลายครั้ง [22][31][23][34][35] และ claim ของ MidJourney ที่บอกว่า 'แทนที่ MRI/CT ได้' [5] ไม่มีรายละเอียดทางเทคนิคที่ตรวจสอบได้

## Possibility
**Likely:** Gaussian Splatting เคลื่อนจาก demo ไปเป็น component ของ pipeline สำหรับ mapping และ XR ตลอดปีนี้ เนื่องจากมี consumer deployment ที่ ship แล้ว [26] และ capture tooling ที่ active [7][10][28] **Plausible:** 4D/dynamic splat capture บน rig ขนาดเล็กกลายเป็น practical สำหรับทีมเล็กเมื่องาน Volograms-style สุกงอม [28], และ procedural environment generation จากข้อมูล geodata สาธารณะ (DEM/OSM [8], satellite [19]) ถูกนำไปใช้สร้างแผนที่ขนาดใหญ่ใน game/edutech **Plausible:** Copernicus tools ของ Houdini 22 [14] ทำให้ workflow real-terrain-to-asset เป็นมาตรฐานมากขึ้น **Unlikely (near-term):** framing เรื่องแทนที่การ scan ทางการแพทย์ของ MidJourney [5] สะท้อนความเป็นจริงทางคลินิก — ถือเป็น hype จนกว่าจะมีแหล่งอ้างอิง ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น

## Org applicability — NDF DEV
1) Prototype Gaussian Splatting capture สำหรับ XR/heritage asset (สถานที่หรือวัดในเชียงใหม่) แล้วทดสอบ import เข้า Unity — การนำไปใช้ของ Apple Maps ลด risk ของแนวทางนี้ [26]; มีคำแนะนำ drone vs camera capture [7]; effort ปานกลาง 2) ประเมิน runtime Unity wireframe shader สำหรับ visualization ใน edutech/XR (ไม่ต้อง preprocess mesh) [13][25]; effort ต่ำ 3) ทดลอง procedural map pipeline ด้วย DEM+OSM สำหรับ prototype แผนที่ game/edutech [8]; effort ปานกลาง 4) ดึง UE 5.8 rigging toolset ฟรีของ Epic + Zebra sample มา benchmark กับ character workflow ปัจจุบัน [21], และนำข้อค้นพบ 'ARKit shape keys น้อยที่สุด' ไปใช้กับงาน avatar [16]; effort ต่ำ 5) ดู Houdini 22 keynote วันที่ 22 มิ.ย. ก่อนตัดสินใจเลือก terrain pipeline [14]; effort ต่ำ 6) ถ้าทีมมีใครใช้ Mac ให้ทดสอบ NeRF/GS Mac-GPU library v0.2.0 สำหรับการทดลองราคาถูก [10][30]; effort ต่ำ แต่ยังอยู่ระยะแรก ข้าม: Luma Skills marketing [22][23][31][34][35], claim body-scan ของ MidJourney [5], thread 'AI tools' ทั่วไป [15], และโพสต์ GLM-in-Claude-Code [32][37] — off-topic หรือยังไม่ผ่านการยืนยัน

## Signals to Watch
- Houdini 22 keynote 22 มิ.ย. 2026 — จับตา Copernicus/procedural terrain tooling ที่เกี่ยวกับ map generation [14]
- Volograms 4D Gaussian Splatting บน camera rig ขนาดเล็กลง — ลด barrier สำหรับ dynamic volumetric capture [28]
- Alibaba Mapping Lab: ภาพดาวเทียม 2D → 3D city สมจริง 1 ตร.กม. ใน ~10 นาที — ติดตามสำหรับ large-environment generation [19]
- Open-source Mac-GPU 3D-vision library (NeRF/GS/differentiable rendering) ที่ v0.2.0 — ติดตามความสุกงอมสำหรับการทดลองบนฮาร์ดแวร์ที่ไม่ใช่ NVIDIA [10][30]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Doesh96 | ^363 c15 | [Wip Considering how bad I am at rigging and how much I love experimenting, I bro](https://x.com/Doesh96/status/2067724801376964991) |
| x | bilawalsidhu | ^339 c21 | [Watching sports from a god's eye view. I don't care what people say, this is how](https://x.com/bilawalsidhu/status/2067978121576362228) |
| x | RyanLykos | ^266 c4 | [Mouth correctives! They make such a huge difference to both how the rig feels an](https://x.com/RyanLykos/status/2067846678300721343) |
| x | ThomasonTown | ^257 c4 | [Can someone please 3D scan this entire park before it inevitably closes in like ](https://x.com/ThomasonTown/status/2067972284216676685) |
| x | shiri_shh | ^232 c19 | [expensive MRI and CT scans are officially COOKED 😭 MidJourney just built somethi](https://x.com/shiri_shh/status/2067708111314694516) |
| x | Noiracide | ^128 c1 | [#indiegame #blender Rigging begin ! https://t.co/CONvkKrQcm](https://x.com/Noiracide/status/2067941203132195191) |
| x | GabRoXR | ^128 c8 | [360 Drone Vs "Standard" Drone for #GaussianSplatting. I picked an EPIC location ](https://x.com/GabRoXR/status/2067984246464246075) |
| x | PlayDaaa | ^122 c9 | [Hour 1 of building a pipeline that turns public topographic data into 3D isometr](https://x.com/PlayDaaa/status/2067714196423532947) |
| x | peplmGameDev | ^118 c2 | [Working on a procedural stylized slash creator for unity ! #gamedev #unity3d #vi](https://x.com/peplmGameDev/status/2067662155512434909) |
| x | amir_razlighi | ^105 c4 | [I always wanted to use the best 3D vision / graphics research libraries on my Ma](https://x.com/amir_razlighi/status/2067896517214490635) |
| x | smallfly | ^104 c8 | [@FastCompany just published a great piece on @theworldlabs , @drfeifei , Marble,](https://x.com/smallfly/status/2067638115494252832) |
| x | archeohistories | ^92 c0 | [The Antonine Fountain (Sagalassos), Burdur - Türkiye 🇹🇷 Antonin Fountain is a hi](https://x.com/archeohistories/status/2067977604934885858) |
| x | 80Level | ^88 c0 | [Dynamic Wireframe Shader by Amazing Assets renders wireframe effects in Unity en](https://x.com/80Level/status/2067993306965987819) |
| x | sidefx | ^81 c1 | [Watch the Houdini 22 Keynote live on YouTube, premiering on June 22, 2026, at 09](https://x.com/sidefx/status/2068131719967080560) |
| x | wiliam23820a | ^76 c26 | [🚀 Hidden AI Tools That Feel Like Superpowers https://t.co/RqYF5Jh5Ng – Writing l](https://x.com/wiliam23820a/status/2067842358344040874) |
| x | sttuuuufffff | ^67 c0 | [I had to revisit this ARKit setup for my face rig in blender, turns out less is ](https://x.com/sttuuuufffff/status/2067736625388429767) |
| x | YellowArtPone | ^63 c1 | [@RinnaPaws Blender Rigging! It's essentially layers of 2D art in a 3D space, par](https://x.com/YellowArtPone/status/2067691331363742165) |
| x | ushadersbible | ^61 c0 | [I made this compute shader to paint a cat in Unity. Anyway, I'll be uploading th](https://x.com/ushadersbible/status/2067647805577892268) |
| x | yohaniddawela | ^56 c2 | [It now takes Alibaba's Mapping Lab just 10 minutes to generate a square kilometr](https://x.com/yohaniddawela/status/2068275707810070990) |
| x | QuantaMagazine | ^46 c2 | [How do you measure the surface area of a whale shark? Biologists used photogramm](https://x.com/QuantaMagazine/status/2068024536394514457) |
| x | 80Level | ^43 c0 | [Try out the full Unreal Engine 5.8 animation and rigging toolset, including DMC,](https://x.com/80Level/status/2068000860139905277) |
| x | LumaLabsAI | ^42 c8 | [A Luma Skill turns your best result into a repeatable workflow. Build it once, r](https://x.com/LumaLabsAI/status/2067653815948476522) |
| x | LumaLabsAI | ^41 c3 | [Your footage. Your cut. One canvas. Assemble it on Timeline, where your edit tak](https://x.com/LumaLabsAI/status/2068051147273728244) |
| x | cghow_ | ^36 c0 | [Azure Beam in Unreal Engine 5 Niagara https://t.co/su9LT38iEh https://t.co/LkzIa](https://x.com/cghow_/status/2067895180511096855) |
| x | jettelly | ^35 c0 | [Arkhivrag finished their dynamic wireframe shader for Unity, generated entirely ](https://x.com/jettelly/status/2067955560839008299) |
| x | bilawalsidhu | ^35 c3 | [Apple Maps Just Got Insanely Realistic -- Here's The Tech Behind It 00:00 Intro ](https://x.com/bilawalsidhu/status/2068326490656182329) |
| x | bilawalsidhu | ^32 c3 | [Woot! The the time has finally come. Record a loom for your clanker and have it ](https://x.com/bilawalsidhu/status/2067745721919402200) |
| x | rafamolone | ^29 c1 | [Quick update on something we've been working on at @Volograms. 4D Gaussian Splat](https://x.com/rafamolone/status/2068068468553908436) |
| x | RadianceFields | ^23 c2 | [@rezmeram It's a 3D reconstruction of a real bee using gaussian splatting (No AI](https://x.com/RadianceFields/status/2067658498733953483) |
| x | amir_razlighi | ^23 c1 | [v0.2.0 is out now. Repo: https://t.co/hrNPEtzqN6 If you are working on NeRFs, Ga](https://x.com/amir_razlighi/status/2067896550995448202) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Doesh96</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 363 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Doesh96/status/2067724801376964991">View @Doesh96 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wip Considering how bad I am at rigging and how much I love experimenting, I broke my rig for Unreal. Thanks to Advanced Skeleton for their non-destructive rigging — I fixed everything and now it’s ru”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Artist ใช้ Advanced Skeleton (non-destructive rigging) แก้ rig ที่พังใน Maya แล้ว export ไปรัน Control Rig ใน Unreal Engine ได้สำเร็จ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Advanced Skeleton แก้ rig ได้โดยไม่ต้องสร้างใหม่ทั้งหมด — เป็น safety net จริงๆ สำหรับ character pipeline</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า pipeline ใช้ Maya ให้ลอง Advanced Skeleton แทน manual rigging ก่อน character project ถัดไป</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Doesh96/status/2067724801376964991" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 339 · 💬 21</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2067978121576362228">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Watching sports from a god’s eye view. I don’t care what people say, this is how I want to experience sports - as full blown 4d gaussian splats or better. Makes 3d videos look ancient after you try th”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>demo แสดงกีฬาถ่ายทอดสดด้วย 4D Gaussian Splats ให้เลือกมุมกล้องได้อิสระ — สิ่งที่ 3D video multi-camera แบบเดิมทำไม่ได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>4D Gaussian Splatting ระดับ broadcast กำลังกลายเป็น source format หลักของ immersive VR — XR pipeline ของสตูดิโอจะต้องรับมือ format นี้ในไม่ช้า</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง 4D Gaussian Splatting test ใน Unity ด้วย open-source splat renderer เพื่อ benchmark render cost ก่อน client จะถามหา format นี้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2067978121576362228" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 266 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2067846678300721343">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mouth correctives! They make such a huge difference to both how the rig feels and looks. really pleased (She does have teeth and a tongue! Just haven't rigged them yet😆) #blender #3d #rigging https://”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>3D artist แชร์ demo facial rig ใน Blender โดยใช้ mouth correctives ที่ช่วยให้ deformation ดูและรู้สึกดีขึ้นชัดเจน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Corrective shapes เป็น technique จริงที่ใช้ได้กับงาน character rigging ใน Blender หรือ Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า rig character ใน Blender ให้เพิ่ม mouth correctives เข้า checklist ก่อน export ไป Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2067846678300721343" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ThomasonTown</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 257 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ThomasonTown/status/2067972284216676685">View @ThomasonTown on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Can someone please 3D scan this entire park before it inevitably closes in like 5 months?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X ขอให้ใครสักคน 3D scan สวนสาธารณะก่อนปิดตัว โดยไม่มีโครงการอนุรักษ์ใดๆ อยู่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ThomasonTown/status/2067972284216676685" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@shiri_shh</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 232 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/shiri_shh/status/2067708111314694516">View @shiri_shh on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“expensive MRI and CT scans are officially COOKED 😭 MidJourney just built something straight out of black mirror step into warm water. wait 60 seconds. get a full 3D scan of your body. at a fraction of”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ viral อ้างว่า MidJourney สร้างเครื่อง scan ร่างกาย 3D แบบแช่น้ำ 60 วินาที แต่ MidJourney คือบริษัท AI image generation ไม่ใช่ medical hardware — ไม่มีแหล่งอ้างอิงที่ตรวจสอบได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/shiri_shh/status/2067708111314694516" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Noiracide</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 128 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Noiracide/status/2067941203132195191">View @Noiracide on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“#indiegame #blender Rigging begin ! https://t.co/CONvkKrQcm”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev โพสต์อัปเดตสั้นๆ ว่าเริ่ม rigging ตัวละครใน Blender แล้ว ไม่มีเทคนิคหรือรายละเอียดใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Noiracide/status/2067941203132195191" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GabRoXR</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 128 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GabRoXR/status/2067984246464246075">View @GabRoXR on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“360 Drone Vs &quot;Standard&quot; Drone for #GaussianSplatting. I picked an EPIC location to see who wins 🏆 This is the Der Haar Castle, the largest and most luxurious castle in the Netherlands. The original ca”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทดสอบ 3DGS จริงที่ De Haar Castle พบ DJI Mini 4 Pro (gimbal 4K, 500 ภาพ) ให้สีแม่นกว่า Antigravity A1 360 drone (panoramic 8K, extract cubemap) ทั้งคู่ process ใน Postshot 30K iterations / 5M splats</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>งาน XR/VR capture ของทีม, gimbal drone ทั่วไปให้ color fidelity ดีกว่า 360 rig เฉพาะทางใน Gaussian Splatting — ถูกกว่าและผลดีกว่า</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าทีมถ่าย 3DGS locations, ใช้ gimbal drone ~500 ภาพ process ใน Postshot 30K iterations / 5M splats เป็น baseline ก่อนลงทุน 360 rig</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GabRoXR/status/2067984246464246075" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PlayDaaa</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 122 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PlayDaaa/status/2067714196423532947">View @PlayDaaa on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hour 1 of building a pipeline that turns public topographic data into 3D isometric game maps. Real-world elevation (Copernicus DEM) + OpenStreetMap → procedural terrain, coastline &amp; city, baked low-po”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาสร้าง open-source pipeline ที่รวม Copernicus DEM กับ OpenStreetMap เพื่อ generate low-poly isometric game map อัตโนมัติ — bake ใน Blender, render ใน Three.js, ตัวอย่างคือโมนาโก ไม่มี hand-model เลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เมื่อ release แล้ว pipeline นี้ตัดขั้น terrain authoring ออก — เมืองจริงกลายเป็น playable map โดยไม่ต้อง sculpt เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Star repo ตอน public แล้วนำ Blender-baked low-poly mesh ใส่ Unity project ที่ต้องการ terrain จากเมืองจริงโดยไม่ต้องทำ asset เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PlayDaaa/status/2067714196423532947" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
