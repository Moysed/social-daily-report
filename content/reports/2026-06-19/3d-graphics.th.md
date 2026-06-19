---
type: social-topic-report
date: '2026-06-19'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-06-19T03:37:31+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 39
salience: 0.62
sentiment: mixed
confidence: 0.6
tags:
- 3d-graphics
- unreal-engine
- gaussian-splatting
- ai-3d-generation
- blender
- xr
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2067406981443260416/img/wcC_CJElKalhpZ0M.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-06-19

## TL;DR
- Unreal Engine 5.8 ออกแล้ว: รองรับ MCP server ให้ AI agents ทำงานภายใน engine ได้ [16], MegaLights จัดการแสงไดนามิกหลายพันดวงที่ 60 FPS พร้อม Lumen mode ที่เร็วขึ้น [17], และตัวอย่าง Zebra สำหรับ animation/rigging ระดับ production [4]
- Gaussian splatting กำลังออกจากโหมดเดโมสู่การใช้งานจริง: พบในวิดีโอ MrBeast [11], 4D splatting ปรับขนาดได้ของ Gracia [13], การ reconstruct splat ของผึ้งจริงโดยไม่ใช้ AI [33], และชิป Snapdragon Reality Elite XR ของ Qualcomm ที่มี hardware-accelerated splatting และ 3D reconstruction บนอุปกรณ์ [36]
- pipeline AI text/image-to-3D เริ่มพัฒนาเป็น workflow จริงจัง: roguelike บน UE5 ที่เล่นได้ สร้างใน 48 ชั่วโมงผ่านแนวคิด Nanobanana Pro + Tripo Smart Mesh (5-20k polys) [10], Meshy ผ่าน 1 ล้าน subscribers บน YouTube [28], และ Luma 'Skills' สำหรับสร้าง asset ซ้ำได้อย่างสม่ำเสมอ [31][37]
- โพสต์เทคนิค Blender ครองส่วนใหญ่ของ long tail: Cloth Nodes ใน 5.2 สำหรับ procedural coral [6], Geometry Nodes NPR explosions [26], และ raycast/world shaders [2][21] — เป็นทักษะสะสม ไม่ใช่การปล่อย release
- อ้างสิทธิ์ MidJourney 'innerspace' full-body 3D scan กำลังแพร่กระจายพร้อมกรอบการแพทย์ที่เกินจริง ('MRI/CT scans are cooked') และไม่มีผลิตภัณฑ์ที่ตรวจสอบได้ [3][12][27] — ถือเป็น hype

## สิ่งที่เกิดขึ้น
Epic ปล่อย Unreal Engine 5.8 โดยมีสามรายการที่ยืนยัน features หลัก: รองรับ MCP server แบบ native ให้ AI agents สร้างงานภายใน engine ได้ [16], MegaLights ขยายสเกลถึงแสงไดนามิกหลายพันดวงที่ 60 FPS และ Lumen mode ที่เร็วขึ้นสำหรับ hardware ระดับล่าง [17], และ Zebra Sample ที่ปล่อยออกมาเป็นตัวอ้างอิงสำหรับ animation และ rigging [4] แยกจากนี้ Gaussian splatting ปรากฏในบริบทผู้บริโภคและ hardware — ในวิดีโอ MrBeast [11], 4D splatting ที่ปรับขนาดได้ของ Gracia [13], การ reconstruct splat แบบไม่ใช้ AI [33], และการประกาศของ Qualcomm เรื่อง splatting บนอุปกรณ์พร้อม hardware-accelerated 3D reconstruction ในชิป Snapdragon Reality Elite XR [36]

## ทำไมถึงสำคัญ (เหตุผล)
มีการเปลี่ยนแปลงเชิงโครงสร้างสองอย่างอยู่ใต้สัญญาณรบกวน อย่างแรก AI agents แบบ native ใน engine: การที่ UE เพิ่ม MCP [16] สะท้อนทิศทางที่ tooling ของ NDF เองชี้ไปอยู่แล้ว (UnityMCP อยู่ใน connected stack ของ studio) บ่งชี้ว่าการสร้าง scene/asset ด้วย agent กำลังกลายเป็น first-class engine feature แทนที่จะเป็น external script อย่างที่สอง on-device Gaussian splatting [36] เปลี่ยนเศรษฐศาสตร์ XR — ถ้า capture และ reconstruction รันอย่างมีประสิทธิภาพบน headset SoC การ capture สภาพแวดล้อมแบบ photoreal ก็ไม่ต้องพึ่ง desktop pipeline หนักๆ อีกต่อไป ซึ่งส่งผลโดยตรงต่อประสบการณ์ XR thread AI-3D generation [10][28][31] ลดต้นทุนของ blockout และ asset ในขั้น concept แต่ข้อแม้ที่ย้ำซ้ำคือคุณภาพของ topology และ poly-budget; roguelike ใน 48 ชั่วโมง [10] เป็นการอ้างสิทธิ์ prototype ไม่ใช่ production pipeline ที่ ship แล้ว รายการ body-scan ของ MidJourney [3][12][27] เป็นตัวอย่างชัดที่สุดของ hype ที่วิ่งแซงหลักฐาน และควรตัดออก

## ความเป็นไปได้
น่าจะเกิด: เครื่องมือ AI-to-3D กลายเป็นมาตรฐานสำหรับ prototyping และ concept asset ภายในไม่กี่เดือน จากสัญญาณการรับเอาที่กว้างขวาง [10][28][31][37] แม้การทำความสะอาด topology สำหรับ production จะยังคงอยู่ น่าจะเกิดได้: workflow MCP/agent แบบ native ใน engine แพร่จาก Unreal [16] ไปสู่ tooling ฝั่ง Unity ทำให้การประกอบ asset และ scene ด้วย agent กลายเป็นส่วนปกติของ pipeline น่าจะเกิดได้: on-device Gaussian splatting บน XR silicon [36] ถึงคุณภาพ capture ที่ใช้งานได้บน headset รุ่นต่อไป แต่รายการนี้เป็นการประกาศจากผู้ขาย ไม่ใช่ hardware ที่ ship และผ่านการ benchmark จริง ดังนั้น timing ยังไม่แน่นอน ไม่น่าจะเกิด (ระยะสั้น): กรอบการแพทย์ body-scan ของ MidJourney [12][27] จะกลายเป็นผลิตภัณฑ์วินิจฉัยจริง — ไม่มีแหล่งใดให้หลักฐานหรือตัวเลข

## การนำไปใช้กับองค์กร — NDF DEV
1) ทำ spike เล็กๆ โดยใช้ Tripo หรือ Meshy เพื่อสร้าง blockout/greybox mesh สำหรับ prototype game และ XR จากนั้นวัดต้นทุนการ cleanup เทียบกับ poly output ที่อ้างว่า 'clean' 5-20k ก่อนเชื่อใจสำหรับ production (low effort) [10][28] 2) ติดตาม engine-native MCP ในฐานะทิศทางสำหรับ UnityMCP setup ที่มีอยู่ของ studio; การเคลื่อนของ UE [16] คือจุดอ้างอิงสำหรับ agent-in-engine workflow (low effort) 3) ทดลอง Gaussian splatting สำหรับ XR environment capture และจับตา Snapdragon Reality Elite XR chip [36] ในฐานะ on-device path; จับคู่กับ resizable splats แบบ Gracia สำหรับการนำ asset กลับมาใช้ (med effort) [13][36] 4) นำ Blender Geometry Nodes / procedural และ shader techniques เข้า stylized-asset toolkit — Cloth Nodes [6], NPR FX [26], และ Unity VFX/shader patterns [22][24][25] (low-med effort) 5) ประเมิน Luma Skills สำหรับการสร้าง asset ที่สม่ำเสมอและทำซ้ำได้ หาก throughput ของ concept art เป็นคอขวด (low effort) [31][37] ข้าม: การอ้างสิทธิ์ MidJourney 'innerspace'/body-scan [3][12][27] — ไม่มีคุณค่าที่นำไปปฏิบัติหรือตรวจสอบได้ในวันนี้

## สัญญาณที่ต้องจับตา
- Qualcomm Snapdragon Reality Elite XR chip — on-device Gaussian splatting และ hardware-accelerated 3D reconstruction; กำหนดว่า XR capture จะย้ายออกจาก desktop ได้หรือไม่ [36]
- UE 5.8 MCP server support — engine หลักแรกที่เปิด agent control แบบ native; เกี่ยวข้องกับการใช้งาน UnityMCP ของ studio [16]
- คุณภาพ AI-3D mesh topology/poly-budget — Tripo Smart Mesh อ้างว่า output clean 5-20k-poly; ต้องตรวจสอบก่อนเชื่อใจใน pipeline [10]
- World models / spatial intelligence (World Labs, Marble, Genie 3) ในฐานะการเปลี่ยนแปลง 3D-content ครั้งต่อไปที่เป็นไปได้ [19][38]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | krysidian | ^1489 c19 | [Been doing a lot of rigging for an animated pilot lately. Expect to see some mor](https://x.com/krysidian/status/2067408434337653206) |
| x | Bipowpow | ^954 c10 | [Stylize Blur Effect using Raycast Shader Node. (Eevee &amp; Cycles) #blender #ee](https://x.com/Bipowpow/status/2067423620948005073) |
| x | bilawalsidhu | ^795 c12 | [forget outerspace. midjourney is mapping innerspace. https://t.co/A0iT4mdeWa](https://x.com/bilawalsidhu/status/2067423609140715803) |
| x | UnrealEngine | ^713 c10 | [Check out the Zebra Sample, a production-quality sample built inside UE on full ](https://x.com/UnrealEngine/status/2067351735891636438) |
| x | R34Dex | ^482 c4 | [✨Blender render by ME and only ME &gt;:3c although, thanks so much for @marshmel](https://x.com/R34Dex/status/2067486005415018854) |
| x | sai_charan_md | ^312 c5 | [Experimenting with Blender 5.2's new Cloth Nodes on some procedural anemones fro](https://x.com/sai_charan_md/status/2067259080788639899) |
| x | bilawalsidhu | ^299 c10 | [Well I know the first thing I'm doing when fable access is restored 👀](https://x.com/bilawalsidhu/status/2067328315023560928) |
| x | RobLooseCannon | ^259 c8 | [Brusselstown Ring sits on a high ridge above the Wicklow lowlands, looking west ](https://x.com/RobLooseCannon/status/2067156169026650154) |
| x | RangerBoard | ^226 c4 | [For those curious, here's a side-by-side comparison between the February 2011 re](https://x.com/RangerBoard/status/2067614893449052199) |
| x | Stefan_3D_AI | ^208 c14 | [I built a playable 3D roguelike in Unreal Engine 5 from scratch in less than 48 ](https://x.com/Stefan_3D_AI/status/2067219456934412761) |
| x | andrewpprice | ^208 c9 | [Fairly certain these shots from the latest MrBeast video use 3D Gaussian Splatti](https://x.com/andrewpprice/status/2067491703788011790) |
| x | shiri_shh | ^176 c15 | [expensive MRI and CT scans are officially COOKED 😭 MidJourney just built somethi](https://x.com/shiri_shh/status/2067708111314694516) |
| x | himelstech | ^160 c8 | [Gracia's 4D Gaussian Splatting can be resized to suit your needs. Full video is ](https://x.com/himelstech/status/2067336366325989588) |
| x | Doesh96 | ^159 c7 | [Wip Considering how bad I am at rigging and how much I love experimenting, I bro](https://x.com/Doesh96/status/2067724801376964991) |
| x | daddyhope | ^135 c19 | [So here are my two cents on the Constitutional Court rulings delivered today aga](https://x.com/daddyhope/status/2067222380917772545) |
| x | VaibhavSisinty | ^77 c8 | [This is actually massive. 🤯 Unreal Engine 5.8 shipped today and AI agents can no](https://x.com/VaibhavSisinty/status/2067453967953694829) |
| x | TechieUltimatum | ^74 c4 | [Unreal Engine 5.8 is here, and it's bringing AI deeper into game development. Ke](https://x.com/TechieUltimatum/status/2067286399502741947) |
| x | multimodalart | ^71 c0 | [Boogu Image Edit is GOOD! This 10B parameter open source image editing/generatio](https://x.com/multimodalart/status/2067577664748077222) |
| x | smallfly | ^59 c6 | [@FastCompany just published a great piece on @theworldlabs , @drfeifei , Marble,](https://x.com/smallfly/status/2067638115494252832) |
| x | gleb_alexandrov | ^57 c1 | [Fantastic use of bevel shader (not in Blender).](https://x.com/gleb_alexandrov/status/2067489982797758556) |
| x | stlin217 | ^44 c0 | [Made various gradient background world shader for 3D character showcase. Advance](https://x.com/stlin217/status/2067268554106535973) |
| x | peplmGameDev | ^44 c2 | [Working on a procedural stylized slash creator for unity ! #gamedev #unity3d #vi](https://x.com/peplmGameDev/status/2067662155512434909) |
| x | multimodalart | ^39 c1 | [this LTX LoRAs show how open weights allow for a level of customization that is ](https://x.com/multimodalart/status/2067327982964781116) |
| x | SoyEdgar09 | ^38 c2 | [I have the shader, now I just need an idea. #unity #indiedev #indiegame https://](https://x.com/SoyEdgar09/status/2067393669242470563) |
| x | ushadersbible | ^37 c0 | [I made this compute shader to paint a cat in Unity. Anyway, I'll be uploading th](https://x.com/ushadersbible/status/2067647805577892268) |
| x | 3DxDEV7 | ^36 c0 | [This anime-style explosion was made entirely in Blender — no compositing tricks,](https://x.com/3DxDEV7/status/2067531224785002614) |
| x | Spectromachina | ^35 c1 | [@midjourney Essentially they're doing a 3d scan of the persons whole body and wi](https://x.com/Spectromachina/status/2067428640497820056) |
| x | MeshyAI | ^34 c10 | [🎉 We just hit 1,000,000 subscribers on YouTube! What began as a few tutorials on](https://x.com/MeshyAI/status/2067237898345423182) |
| x | YellowArtPone | ^31 c0 | [@RinnaPaws Blender Rigging! It's essentially layers of 2D art in a 3D space, par](https://x.com/YellowArtPone/status/2067691331363742165) |
| x | bilawalsidhu | ^27 c0 | [@midjourney time to map the depths of innerspace](https://x.com/bilawalsidhu/status/2067427578474803475) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@krysidian</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1489 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/krysidian/status/2067408434337653206">View @krysidian on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Been doing a lot of rigging for an animated pilot lately. Expect to see some more behind the scenes soon! #blender #b3d #stylized #rigging #fckedupexogism https://t.co/RR9xbIeCXk”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปิน @krysidian โพสต์ความคืบหน้าการ rig ตัวละคร stylized ใน Blender สำหรับ animated pilot โดยไม่มี technique หรือ workflow แชร์ — เป็นแค่ teaser สำหรับ content เพิ่มเติม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/krysidian/status/2067408434337653206" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Bipowpow</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 954 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Bipowpow/status/2067423620948005073">View @Bipowpow on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Stylize Blur Effect using Raycast Shader Node. (Eevee &amp;amp; Cycles) #blender #eevee #cycles #realtime #ltmlab https://t.co/5OtyVhBWMp”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ศิลปิน Blender แชร์ blur effect แบบ stylized ที่สร้างด้วย Raycast Shader Node รองรับทั้ง Eevee และ Cycles</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Blur แบบ Raycast ใน shader nodes เป็น non-destructive technique ที่ใช้ได้ทั้ง Eevee/Cycles — ทีม 3D เอาไปใส่ scene ไหนก็ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม 3D ลอง Raycast blur node นี้ใน project Blender ปัจจุบันได้เลย — ได้ stylized focus/depth โดยไม่ต้องพึ่ง post-processing</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Bipowpow/status/2067423620948005073" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 795 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2067423609140715803">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“forget outerspace. midjourney is mapping innerspace. https://t.co/A0iT4mdeWa”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์คลุมเครือบอกว่า Midjourney กำลัง 'map innerspace' — ไม่มีชื่อ feature, ไม่มีรายละเอียด, มีแค่ link เปล่า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2067423609140715803" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 713 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2067351735891636438">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out the Zebra Sample, a production-quality sample built inside UE on full Unreal Engine animation and rigging. Released alongside UE 5.8, the sample is a great way to learn, reference or kicksta”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine ปล่อย Zebra Sample — ตัวอย่าง character animation และ rigging ระดับ production ใน UE 5.8 ให้โหลดฟรีบน Fab</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Rig ระดับ production ฟรีใน UE 5.8 — ทีม XR/VR ใช้เป็น reference สำหรับ animation pipeline และมาตรฐาน rigging ได้ตรงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">โหลด Zebra Sample จาก Fab แล้วใช้เป็น rigging reference ตอนสร้างหรือ review character animation ในโปรเจกต์ XR/VR</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2067351735891636438" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@R34Dex</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 482 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/R34Dex/status/2067486005415018854">View @R34Dex on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“✨Blender render by ME and only ME &amp;gt;:3c although, thanks so much for @marshmellowybun for rigging and making the pp for my boy Det and helping me with his rig lmao #furryrr34 #rr34furry https://t.co”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ Blender render ส่วนตัวของ @R34Dex เครดิต @marshmellowybun สำหรับ rigging ตัวละคร อยู่ใน community furry fan-art</dd>
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
    <span class="ndf-author">@sai_charan_md</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 312 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/sai_charan_md/status/2067259080788639899">View @sai_charan_md on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Experimenting with Blender 5.2's new Cloth Nodes on some procedural anemones from my coral system. #b3d #blender #geometryNodes https://t.co/l2CL3CRI4K”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักสร้างงานทดสอบ Cloth Nodes ใหม่ใน Blender 5.2 ผ่าน Geometry Nodes เพื่อขับ soft-body motion บน mesh ปะการัง แบบ procedural</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Cloth Nodes ใน GN ทำให้ soft dynamics เป็น procedural และ non-destructive — asset อินทรีย์ใน VR animate ได้โดยไม่ต้อง bake simulation</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม art ลอง Cloth Nodes ใน Blender 5.2 สำหรับ vegetation หรือ organic prop ที่จะ export เข้า Unity สำหรับ XR</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/sai_charan_md/status/2067259080788639899" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 299 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2067328315023560928">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Well I know the first thing I’m doing when fable access is restored 👀”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Post แค่แสดงความตื่นเต้นที่จะได้ใช้ 'Fable' อีกครั้ง ไม่มีรายละเอียดใดๆ ว่าคืออะไร เปลี่ยนแปลงอะไร หรือจะทำอะไร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2067328315023560928" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@RobLooseCannon</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 259 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/RobLooseCannon/status/2067156169026650154">View @RobLooseCannon on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Brusselstown Ring sits on a high ridge above the Wicklow lowlands, looking west toward the Shannon basin and east toward the Irish Sea. It kept its greatest secrets for centuries until December 2025, ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจัยจาก Queen's University Belfast ใช้ LiDAR, aerial survey, และ photogrammetry ค้นพบ platform บ้านทรงกลมกว่า 600 จุดที่ Brusselstown Ring ไอร์แลนด์ — ชุมชนยุคก่อนประวัติศาสตร์ที่ใหญ่ที่สุดในหมู่เกาะอังกฤษ ขนาด 131 เฮกตาร์</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัวอย่างจริงว่า LiDAR + photogrammetry เปิดเผยโครงสร้างขนาดใหญ่ที่ ground survey มองไม่เห็น — ตรงกับ pipeline สแกน terrain สำหรับ game และ XR</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity/XR นำ workflow LiDAR-to-mesh นี้ไปอ้างอิงตอน evaluate terrain capture tools หรือ pitch photogrammetry scanning ให้ client ได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/RobLooseCannon/status/2067156169026650154" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
