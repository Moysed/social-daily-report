---
type: social-topic-report
date: '2026-06-20'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-20T03:34:45+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 41
salience: 0.58
sentiment: neutral
confidence: 0.58
tags:
- 3d
- gaussian-splatting
- unreal-engine
- unity
- procedural
- photogrammetry
thumbnail: https://pbs.twimg.com/media/HLEt-7Ob0AAIuDI.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-20

## TL;DR
- Unreal Engine 5.8 ออกแล้ว พร้อม MCP server support ในตัว เปิดให้ AI agents ควบคุม editor ได้โดยตรง [15] รวมถึงชุดเครื่องมือ animation/rigging ใหม่ (DMC) และ Zebra Character Sample แจกฟรี [28]
- Gaussian Splatting เริ่มปรากฏในคอนเทนต์กระแสหลัก: วิดีโอ MrBeast ดูเหมือนใช้ 3DGS [7] และ creator หลายคนกำลังผลัก 4D splats สำหรับชมกีฬา [4] รวมถึงเปรียบเทียบ drone จับภาพแบบ 360 กับมาตรฐาน [14]
- มี pipeline ที่ใช้งานได้จริงสำหรับแปลงข้อมูล elevation จาก Copernicus DEM + OpenStreetMap เป็นแผนที่เกม isometric แบบ procedural พร้อม bake low-poly terrain [11]; keynote ของ Houdini 22 (22 มิถุนายน 2026) ถูก tease พร้อมเครื่องมือ Copernicus ใหม่ [32]
- Unity asset/shader ออกมาต่อเนื่อง: GPU dynamic wireframe shader ที่ใช้ topology จริง [24], mobile underwater post-processing shader graphs [30], demo compute-shader วาดภาพ [23] และ procedural stylized slash VFX creator [10]
- spatial intelligence/world models ถูกนำเสนอเป็นทิศทาง AI รอบต่อไปผ่าน World Labs, Fei-Fei Li และ Marble ใน FastCompany [12]; อ้างสิทธิ์ MidJourney body-scan เพื่อสุขภาพ [6] ยังไม่มีการยืนยัน

## What happened
วันนี้มีการ release เครื่องมือ/engine สองชิ้นเป็นหลัก: Unreal Engine 5.8 รายงานว่าออกพร้อม MCP server support ที่ช่วยให้ AI agents ทำงานภายใน editor ได้ [15] พร้อมชุดเครื่องมือ animation/rigging ที่ยืนยันแล้วและ Zebra Character Sample แจกฟรีจาก Epic [28] SideFX tease keynote Houdini 22 วันที่ 22 มิถุนายน 2026 โดยอ้างถึงเครื่องมือ Copernicus ใหม่ [32] Gaussian Splatting ปรากฏซ้ำหลายจุด: คาดว่าใช้ 3DGS ในวิดีโอ MrBeast [7], สนับสนุน 4D splats ในกีฬา [4], เปรียบเทียบ drone capture ที่ปราสาทในเนเธอร์แลนด์ [14] และ splat reconstruction ผึ้งแบบไม่ใช้ AI [34]; มีโพสต์หนึ่งมองหา tooling native บน Mac สำหรับ NeRF, splatting และ differentiable rendering [17]

## Why it matters (reasoning)
ธีมที่โดดเด่นที่สุดคือ AI agents เข้าสู่ 3D pipeline ในระดับ engine: MCP support ใน Unreal [15] สะท้อนรูปแบบที่ studio แตะอยู่แล้วผ่าน UnityMCP บ่งชี้ว่า agent-driven scene assembly และ rigging assistance กำลังเคลื่อนจาก chat เข้าสู่เครื่องมือที่สร้าง asset โดยตรง ผลกระทบทางอ้อม: หาก engine vendor ทำให้ MCP เป็นมาตรฐาน การ automate editor ด้วย prompt จะพกพาได้ระหว่าง Unreal และ Unity (ในที่สุด) ลดต้นทุนงาน layout/setup ซ้ำซาก นอกจากนี้การปรากฏของ Gaussian Splatting ในวิดีโอผู้บริโภค [7] และ workflow จับภาพด้วย drone [14] บ่งชี้ว่ามันกำลังกลายเป็น path จับภาพสู่ประสบการณ์สำหรับ XR จริงจัง ไม่ใช่แค่งานวิจัย — เกี่ยวข้องเพราะ studio ส่ง XR/VR procedural terrain จาก open geodata [11] และเครื่องมือ Copernicus ของ Houdini [32] ชี้ไปที่การสร้าง environment ที่ถูกลงและยึดข้อมูลจริง ข้อควรระวัง: ส่วนใหญ่เป็น social post แหล่งเดียว (โดยเฉพาะอ้างสิทธิ์ UE MCP [15] จาก hype account และอ้างสิทธิ์ MidJourney medical-scan [6]) ต้องยืนยันกับเอกสาร primary ก่อนวางแผนต่อ

## Possibility
**มีแนวโน้ม:** Gaussian Splatting แพร่กระจายเข้าสู่การจับภาพเพื่อ production ในงาน XR และ marketing ต่อเนื่อง จากการใช้งานจริงหลายจุดอิสระวันนี้ [4][7][14][34] และความต้องการ tooling [17] **มีแนวโน้ม:** การผสาน MCP/agent ใน game engine ขยายตัวต่อ เพราะ Unreal ออก [15] บวกกับ toolset ที่น่าเชื่อถือ [28] สร้างทิศทางที่ engine อื่นมักตาม **เป็นไปได้:** open geodata-to-game-map pipeline [11] และ Copernicus tools ของ Houdini 22 [32] ทำให้ terrain จากโลกจริงกลายเป็น asset ปกติภายในหนึ่งปี **เป็นไปได้:** ระบบ spatial intelligence/world model (World Labs, Marble) [12] เริ่มสร้าง 3D scene ที่ใช้งานได้ แต่ความสมบูรณ์พร้อม production ยังพิสูจน์ไม่ได้ **ไม่น่าเกิดในระยะสั้น:** body scanning ผู้บริโภคแทนที่การวินิจฉัยทางการแพทย์ตามที่นัย [6] — อ้างสิทธิ์สูง แหล่งเดียว ไม่มีหลักฐาน ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น

## Org applicability — NDF DEV
1) ยืนยัน UE 5.8 MCP claim กับ release notes ของ Epic แล้วตรวจว่า UnityMCP ของ studio ทำ agent-driven editor actions สำหรับ asset/scene setup ได้เทียบเท่าหรือไม่ (effort: med) [15][28] 2) ทดสอบ Gaussian Splatting capture สำหรับ XR location หรือ prop โดยใช้ footage drone หรือโทรศัพท์ วัดว่า splat import เข้า Unity ได้สะอาดแค่ไหนเทียบกับ mesh pipeline (effort: med) [4][7][14][34] 3) ต้นแบบ open-geodata terrain pipeline (Copernicus DEM + OpenStreetMap) สำหรับเกมที่ใช้แผนที่หรือ edutech scene เพื่อลดเวลา hand-modeling (effort: med) [11] 4) ประเมิน Unity shader/asset สำเร็จรูปสำหรับนำมาใช้ — GPU wireframe [24], mobile underwater post-processing [30], stylized slash VFX [10] — เพื่อหลีกเลี่ยง shader work in-house (effort: low) 5) ดู Houdini 22 keynote วันที่ 22 มิถุนายน สำหรับ feature procedural/Copernicus ที่เกี่ยวกับ terrain (effort: low) [32] 6) สำหรับ asset physical prop หรือวัตถุจริง photogrammetry ยังเป็นวิธีจับภาพต้นทุนต่ำ [27][3][31] (effort: low-med) ข้าม: MidJourney body-scan claims [6], listicle 'AI tools' ทั่วไป [16] และโพสต์ event/marketing ของ Luma Labs เว้นแต่ต้องการ video Timeline tool [33] สำหรับตัดโปรโม

## Signals to Watch
- MCP/agent support ใน engine จะกลายเป็นจริงและพกพาได้หรือไม่ — ยืนยัน UE 5.8 และติดตาม UnityMCP parity [15][28]
- Gaussian Splatting ข้ามสู่คอนเทนต์ผู้บริโภค/production และ workflow จับภาพ [4][7][14]
- Houdini 22 keynote วันที่ 22 มิถุนายน 2026 — Copernicus/procedural terrain tools ใหม่ [32]
- spatial intelligence / world models (World Labs, Marble) สุกพอใช้งาน 3D scene จริง [12]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | R34Dex | ^570 c7 | [✨Blender render by ME and only ME &gt;:3c although, thanks so much for @marshmel](https://x.com/R34Dex/status/2067486005415018854) |
| x | Doesh96 | ^341 c15 | [Wip Considering how bad I am at rigging and how much I love experimenting, I bro](https://x.com/Doesh96/status/2067724801376964991) |
| x | RangerBoard | ^248 c5 | [For those curious, here's a side-by-side comparison between the February 2011 re](https://x.com/RangerBoard/status/2067614893449052199) |
| x | bilawalsidhu | ^246 c15 | [Watching sports from a god's eye view. I don't care what people say, this is how](https://x.com/bilawalsidhu/status/2067978121576362228) |
| x | RyanLykos | ^232 c4 | [Mouth correctives! They make such a huge difference to both how the rig feels an](https://x.com/RyanLykos/status/2067846678300721343) |
| x | shiri_shh | ^230 c19 | [expensive MRI and CT scans are officially COOKED 😭 MidJourney just built somethi](https://x.com/shiri_shh/status/2067708111314694516) |
| x | andrewpprice | ^227 c9 | [Fairly certain these shots from the latest MrBeast video use 3D Gaussian Splatti](https://x.com/andrewpprice/status/2067491703788011790) |
| x | multimodalart | ^151 c5 | [Boogu Image Edit is GOOD! This 10B parameter open source image editing/generatio](https://x.com/multimodalart/status/2067577664748077222) |
| x | ThomasonTown | ^150 c4 | [Can someone please 3D scan this entire park before it inevitably closes in like ](https://x.com/ThomasonTown/status/2067972284216676685) |
| x | peplmGameDev | ^111 c2 | [Working on a procedural stylized slash creator for unity ! #gamedev #unity3d #vi](https://x.com/peplmGameDev/status/2067662155512434909) |
| x | PlayDaaa | ^108 c9 | [Hour 1 of building a pipeline that turns public topographic data into 3D isometr](https://x.com/PlayDaaa/status/2067714196423532947) |
| x | smallfly | ^98 c8 | [@FastCompany just published a great piece on @theworldlabs , @drfeifei , Marble,](https://x.com/smallfly/status/2067638115494252832) |
| x | Noiracide | ^94 c1 | [#indiegame #blender Rigging begin ! https://t.co/CONvkKrQcm](https://x.com/Noiracide/status/2067941203132195191) |
| x | GabRoXR | ^91 c7 | [360 Drone Vs "Standard" Drone for #GaussianSplatting. I picked an EPIC location ](https://x.com/GabRoXR/status/2067984246464246075) |
| x | VaibhavSisinty | ^84 c9 | [This is actually massive. 🤯 Unreal Engine 5.8 shipped today and AI agents can no](https://x.com/VaibhavSisinty/status/2067453967953694829) |
| x | wiliam23820a | ^74 c26 | [🚀 Hidden AI Tools That Feel Like Superpowers https://t.co/RqYF5Jh5Ng – Writing l](https://x.com/wiliam23820a/status/2067842358344040874) |
| x | amir_razlighi | ^71 c1 | [I always wanted to use the best 3D vision / graphics research libraries on my Ma](https://x.com/amir_razlighi/status/2067896517214490635) |
| x | 3DxDEV7 | ^70 c0 | [This anime-style explosion was made entirely in Blender — no compositing tricks,](https://x.com/3DxDEV7/status/2067531224785002614) |
| x | sttuuuufffff | ^65 c0 | [I had to revisit this ARKit setup for my face rig in blender, turns out less is ](https://x.com/sttuuuufffff/status/2067736625388429767) |
| x | archeohistories | ^65 c0 | [The Antonine Fountain (Sagalassos), Burdur - Türkiye 🇹🇷 Antonin Fountain is a hi](https://x.com/archeohistories/status/2067977604934885858) |
| x | gleb_alexandrov | ^62 c1 | [Fantastic use of bevel shader (not in Blender).](https://x.com/gleb_alexandrov/status/2067489982797758556) |
| x | YellowArtPone | ^61 c1 | [@RinnaPaws Blender Rigging! It's essentially layers of 2D art in a 3D space, par](https://x.com/YellowArtPone/status/2067691331363742165) |
| x | ushadersbible | ^59 c0 | [I made this compute shader to paint a cat in Unity. Anyway, I'll be uploading th](https://x.com/ushadersbible/status/2067647805577892268) |
| x | 80Level | ^54 c0 | [Dynamic Wireframe Shader by Amazing Assets renders wireframe effects in Unity en](https://x.com/80Level/status/2067993306965987819) |
| x | LumaLabsAI | ^41 c8 | [A Luma Skill turns your best result into a repeatable workflow. Build it once, r](https://x.com/LumaLabsAI/status/2067653815948476522) |
| x | gbrumfiel | ^39 c1 | [So if it wasn't a ramjet, what was it? Enter Jake Hecla. Jake's been wondering t](https://x.com/gbrumfiel/status/2067621319500279932) |
| x | QuantaMagazine | ^39 c2 | [How do you measure the surface area of a whale shark? Biologists used photogramm](https://x.com/QuantaMagazine/status/2068024536394514457) |
| x | 80Level | ^34 c0 | [Try out the full Unreal Engine 5.8 animation and rigging toolset, including DMC,](https://x.com/80Level/status/2068000860139905277) |
| x | bilawalsidhu | ^31 c3 | [Woot! The the time has finally come. Record a loom for your clanker and have it ](https://x.com/bilawalsidhu/status/2067745721919402200) |
| x | NatureDeveloper | ^30 c0 | [We released a new Unity asset! Mobile-friendly underwater/undersurface post-proc](https://x.com/NatureDeveloper/status/2067581672346857836) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@R34Dex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 570 · 💬 7</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/R34Dex/status/2067486005415018854">View @R34Dex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“✨Blender render by ME and only ME &amp;gt;:3c although, thanks so much for @marshmellowybun for rigging and making the pp for my boy Det and helping me with his rig lmao #furryrr34 #rr34furry https://t.co”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปิน furry โพสต์ Blender render ส่วนตัวบน X พร้อมเครดิต rigging ให้ผู้ร่วมงาน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/R34Dex/status/2067486005415018854" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Doesh96</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 341 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Doesh96/status/2067724801376964991">View @Doesh96 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wip Considering how bad I am at rigging and how much I love experimenting, I broke my rig for Unreal. Thanks to Advanced Skeleton for their non-destructive rigging — I fixed everything and now it’s ru”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Advanced Skeleton ช่วยให้ artist กู้คืน rig ตัวละครที่พังได้โดยไม่ต้องสร้างใหม่ แล้วรัน Control Rig ใน Unreal Engine ได้ปกติ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Non-destructive rigging ลดความเสี่ยงตอน iterate rig ตัวละครที่ซับซ้อน — ตรงกับ pipeline XR/VR ที่ต้องแก้ rig บ่อย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/Unity ลองใช้ Advanced Skeleton เป็น rigging tool หลักสำหรับตัวละครซับซ้อนก่อน export เข้า engine</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Doesh96/status/2067724801376964991" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RangerBoard</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 248 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RangerBoard/status/2067614893449052199">View @RangerBoard on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“For those curious, here's a side-by-side comparison between the February 2011 release of S.H.Figuarts Shinken Red versus the new November 2026 Shinkocchou Seihou version, made with a 3D scan of the or”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์เปรียบ S.H.Figuarts Shinken Red รุ่น 2011 กับรุ่น 2026 ที่ใช้ 3D scan ของ suit actor Hirofumi Fukuzawa เพื่อความแม่นยำของ likeness</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RangerBoard/status/2067614893449052199" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 246 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2067978121576362228">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Watching sports from a god’s eye view. I don’t care what people say, this is how I want to experience sports - as full blown 4d gaussian splats or better. Makes 3d videos look ancient after you try th”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Bilawal Sidhu แชร์คลิปกีฬาสดที่ถ่ายและ replay ด้วย 4D Gaussian Splats แบบ free-viewpoint บอกว่าดีกว่า 3D video และน่าจะเป็น media format ใหม่</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>4D Gaussian Splatting ไปถึงระดับ live sports broadcast แล้ว แปลว่า format นี้พร้อมกว่าที่คิดสำหรับ XR/VR content pipeline จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลอง 4DGS playback ใน Unity ผ่าน open-source viewer ที่มีอยู่ เพื่อดูว่า format นี้เข้ากับ pipeline โปรเจกต์ immersive ที่จะมาได้ไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2067978121576362228" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RyanLykos</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 232 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RyanLykos/status/2067846678300721343">View @RyanLykos on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Mouth correctives! They make such a huge difference to both how the rig feels and looks. really pleased (She does have teeth and a tongue! Just haven't rigged them yet😆) #blender #3d #rigging https://”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักทำ rigging ใน Blender โชว์ mouth corrective shapes บน facial rig และเห็นผลชัดว่าช่วยให้ deformation ดีขึ้นมาก ก่อนจะ rig ฟันและลิ้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Corrective blend shapes ลด mesh distortion บน face rig โดยตรง — technique ที่ใช้ได้จริงกับ Unity character และ XR avatar ที่ studio ทำ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/3D เพิ่ม mouth corrective shapes ใน character rig ก่อน export เพื่อลด artifact ที่ jaw และ lip</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RyanLykos/status/2067846678300721343" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@shiri_shh</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 230 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/shiri_shh/status/2067708111314694516">View @shiri_shh on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“expensive MRI and CT scans are officially COOKED 😭 MidJourney just built something straight out of black mirror step into warm water. wait 60 seconds. get a full 3D scan of your body. at a fraction of”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ viral อ้างว่า MidJourney สร้างเครื่องสแกนร่างกาย 3D ด้วยน้ำอุ่น 60 วินาทีแทน MRI/CT — ไม่มีหลักฐานยืนยัน และ MidJourney ไม่ได้ทำ hardware ทางการแพทย์</dd>
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
    <span class="ndf-author">@andrewpprice</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 227 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/andrewpprice/status/2067491703788011790">View @andrewpprice on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Fairly certain these shots from the latest MrBeast video use 3D Gaussian Splatting! Cool to see it out in the wild. https://t.co/PvdPi9JTk2”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Andrew Price (Blender Guru) ระบุว่า MrBeast ใช้ 3D Gaussian Splatting ในวิดีโอล่าสุด ถือเป็นการปรากฏตัวใน production เชิงพาณิชย์ระดับ mainstream</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Gaussian Splatting ถูกใช้ใน production budget สูงได้แล้ว แสดงว่า pipeline พร้อมใช้จริง ตรงกับงาน XR/VR real-world scene capture ของ studio</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR/VR ลอง prototype Gaussian Splatting สำหรับ environment capture ใน Unity ได้เลย เช่น Unity Gaussian Splatting package หรือ Luma AI เพราะ technique นี้ proven แล้วใน production จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/andrewpprice/status/2067491703788011790" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@multimodalart</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 151 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/multimodalart/status/2067577664748077222">View @multimodalart on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Boogu Image Edit is GOOD! This 10B parameter open source image editing/generation model landed out of nowhere on @huggingface and is quite good at editing Give it your hardest editing tasks: https://t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Boogu Image Edit โมเดล open-source ขนาด 10B parameters สำหรับ edit และ generate ภาพ เปิดตัวบน Hugging Face แบบไม่มีประกาศล่วงหน้า ผลงานออกมาดีในงาน edit ที่ซับซ้อน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โมเดล 10B params ขนาดนี้ self-host ได้ ลดการพึ่ง paid API ในงาน edit asset สำหรับ game หรือ e-learning</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดลองบน HuggingFace Spaces ก่อนเลย ดูว่าใช้ edit texture หรือ concept art สำหรับ Unity / e-learning ได้จริงไหม ก่อนตัดสินใจ host เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/multimodalart/status/2067577664748077222" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
