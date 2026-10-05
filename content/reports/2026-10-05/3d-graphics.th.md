---
type: social-topic-report
date: '2026-10-05'
topic: 3d-graphics
lang: th
pair: 3d-graphics.en.md
generated_at: '2026-10-05T03:22:15+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 47
salience: 0.35
sentiment: mixed
confidence: 0.55
tags:
- blender
- realtime-vfx
- procedural
- unity
- gaussian-splatting
- ai-3d
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2106290053110439936/img/69Hx_FR1NmgcJ9Lm.jpg
translated_by: claude-sonnet-4-6
---

# 3D & Graphics — 2026-10-05

## TL;DR
- วันนี้สัญญาณน้อย: ราว 20 จาก 47 รายการโปรโมต bounty marketplace สำหรับ 3D capture ของ Vangrid ด้วยถ้อยคำคล้ายกันและยอด comment 150–450 (เช่น [6][7][10][11]) รูปแบบนี้ดูเป็น crypto engagement campaign ไม่ใช่ความสนใจจริงจากคนทำงาน
- flow ที่ Vangrid อ้าง: AI agent โพสต์ bounty ขอ 3D capture ผ่าน x402 และจ่ายเป็น USDC บน Base หรือ Arc คนจริงถ่ายวิดีโอวนรอบสถานที่ แล้วส่ง 3D capture กลับให้ agent โพสต์ระบุว่า bounty แรกบน Arc settle แล้ว [10][14][44]
- อัปเดต Blender add-on: BeFX Studios ปล่อย RBDLab 1.6 ซึ่งปรับชุดเครื่องมือ destruction/simulation ครั้งใหญ่ [24] Blender Procedural ปล่อย Ultimate Generators Addon V2 พร้อม Geometry Nodes generator แบบ procedural กว่า 50 ตัว [31] Hurricane เป็น particle solver รวมศูนย์สำหรับ fluid, cloth และ softbody [18]
- เครื่องมือ VFX และ shader ที่ไม่ผูกกับ engine: The Shaders Bible เผยแพร่ particle VFX แบบ metaballs portal ทั้งสำหรับ Unity และ Godot [1] Kaleidos export animated shader pattern แบบ no-code ไปยัง Unity หรือ Godot [27]
- Meshy และ OpenAI ร่วมสนับสนุน Unity AI Game Jam ที่ G-STAR 2026: นักพัฒนา 50 คน 24 ชั่วโมง วันที่ 18–19 พ.ย. ที่ BEXCO เมือง Busan [46] งานวิจัยเรื่อง Gaussian Splatting มีเพียงรายการเดียวคือ paper EvenSplat ว่าด้วยความแปรปรวนของ exposure และ illumination [45]

## What happened
เนื้อหาจากคนทำงานจริงวันนี้เป็นการอัปเดตทีละเล็กละน้อย ฝั่ง Blender, BeFX Studios ปล่อย RBDLab 1.6 [24], Ultimate Generators Addon V2 เพิ่ม Geometry Nodes generator กว่า 50 ตัว [31] และ Hurricane ถูกโปรโมตในฐานะ particle solver รวมศูนย์ [18] ครีเอเตอร์คนหนึ่งโชว์ Mixie3D ที่ให้ AI agent คุม Blender ผ่าน API โดยตรง แทนการจำลองการคลิก UI และอ้างว่า generate Pegasus แบบ procedural ได้ในรอบเดียว [4] ฝั่ง Unity มี tutorial metaballs portal ของ The Shaders Bible (Unity และ Godot) [1], เอฟเฟกต์ Eldritch Blast แบบ procedural เต็มรูปแบบ [9], black hole VFX [30] และ Kaleidos เครื่องมือสร้าง shader pattern แบบ no-code ที่ export ไป Unity และ Godot [27] ฝั่ง Unreal และ Houdini มี Niagara tutorial ฟรี [2], guided bubbles และ wet foam solver ที่อิงจาก paper ของ Wētā FX [13] และผลงาน VFX ในพอร์ตโฟลิโอ [8][25] ครีเอเตอร์อีกคนโชว์ Blender shader ที่ผลลัพธ์ใน viewport ของ Blender กับในเกมตรงกันมาก [19]

ด้าน capture และ reconstruction ปริมาณโพสต์ทั้งหมดมาจาก Vangrid โพสต์ที่แทบเหมือนกันหลายรายการอธิบาย 3D-capture bounty ที่ agent เป็นผู้โพสต์และจ่ายด้วย USDC บน Base และ Arc พร้อมการกรองความเป็นส่วนตัวก่อนส่งงาน [5][10][14][17][44] รายการ [6] ยกเครดิตให้ Niantic ที่สร้าง 3D capture dataset ขนาดใหญ่เป็นผลพลอยได้จากเกมมือถือ งานวิจัยมีเพียง EvenSplat ที่แยกผลของ exposure และ illumination ออกจากกันใน Gaussian Splatting [45] Meshy ประกาศสนับสนุน G-STAR Unity AI Game Jam [46] คนทำงานสองคนบอกว่า AI ทำ reconstruction ชิ้นส่วน hard-surface ได้ไม่ดี และการ generate ทีละชิ้นหรือโมเดลเองด้วยมือเร็วกว่า [38][39]

## Why it matters (reasoning)
เทรนด์ที่มีประโยชน์คือ Blender รับงานที่เคยต้องใช้ Houdini หรือ middleware แบบเสียเงินเพิ่มขึ้นเรื่อยๆ RBDLab 1.6 [24] และ Hurricane [18] ครอบคลุม destruction และ multi-physics ส่วน Ultimate Generators [31] ครอบคลุม procedural kitbashing ผลงาน VFX บน Unity และ Unreal ที่ถูกนำเสนอหลายชิ้นระบุ Blender ใน toolchain [8][25][28][30] และ [19] แสดงว่า Blender shader ถ่ายทอดผลไปยังในเกมได้ สำหรับ studio เล็ก นั่นหมายความว่างาน simulation และ procedural asset เพิ่มขึ้นอีกอาจทำในเครื่องมือฟรีได้ เครื่องมือ VFX และ shader ที่ไม่ผูกกับ engine ([1][27][29] ทั้งหมดรองรับ Unity และ Godot) ช่วยลดต้นทุนการสร้างเอฟเฟกต์ที่ไม่ต้องล็อกกับ engine ใด engine หนึ่ง

ข้ออ้างเรื่อง agent คุม Blender [4] เป็นเดโมเดียวที่โปรโมตตัวเอง รายงานจากคนทำงานว่า AI ทำ hard-surface reconstruction ผิดพลาด [38][39] ชี้ไปอีกทาง จึงควรมองว่า agentic 3D generation ยังพิสูจน์ไม่ได้สำหรับ production asset ส่วนปริมาณโพสต์ของ Vangrid [5][7][10][11][14][16][21][23][26][33][34][37][40][42] บอกอะไรเกี่ยวกับเทคโนโลยี capture ได้น้อย ยอด comment 150–450 บนโพสต์คะแนนต่ำและ talking point ที่ซ้ำกันชี้ไปที่ incentive campaign ข้ออ้างที่จับต้องได้ข้อเดียวคือ bounty API ที่จ่ายเงินให้คนไปถ่ายสถานที่ให้ AI agent ตลาดเป้าหมายคือข้อมูลสำหรับ physical AI และ robotics ไม่ใช่ game asset บทวิจารณ์ตรงไปตรงมาเพียงชิ้นเดียวในชุดนี้ระบุว่ามันไม่ได้ตอบคำถามว่าเครื่องจักรควรเชื่อข้อมูลที่ได้รับหรือไม่ [15]

## Possibility
น่าจะเกิด: add-on ด้าน simulation และ procedural ของ Blender จะทับซ้อนกับฟีเจอร์ของ Houdini มากขึ้น วันนี้มีสอง release แยกกันในพื้นที่นี้ คือ [24] และ [31] บวก solver ใหม่ [18] เป็นไปได้: การคุม Blender แบบ MCP หรือ API จะกลายเป็นรูปแบบ add-on ทั่วไปสำหรับ procedural prop แต่ข้อนี้อิงเดโมเดียว [4] และถูกถ่วงด้วยรายงานการโมเดลด้วยมือใน [38][39] เป็นไปได้: AI-generated 3D (Meshy) จะเด่นขึ้นใน workflow ของ Unity ผ่านอีเวนต์อย่าง G-STAR jam [46] แต่ jam ไม่ได้พิสูจน์ว่า asset ใช้ใน production ได้ ไม่น่าเกิดในระยะสั้น: bounty capture แบบ crowdsourced ในสไตล์ Vangrid จะมีความสำคัญกับ pipeline ของ game หรือ XR asset เพราะหลักฐานเป็นเนื้อหาโปรโมต ใช้ crypto เป็นแรงจูงใจ และมุ่งที่ข้อมูลสำหรับ robotics [10][15][42] งานวิจัย Gaussian Splatting ยังดำเนินต่อ โดย EvenSplat [45] แก้เรื่องความสอดคล้องของแสง แต่วันนี้ไม่มีสัญญาณการ integrate เข้า engine ใหม่

## Org applicability — NDF DEV
1) ประเมิน RBDLab 1.6 สำหรับเอฟเฟกต์ destruction ในโปรเจกต์เกมและ XR บน Unity ก่อนซื้อ seat Houdini Effort: med [24] 2) ลอง Ultimate Generators V2 เพื่อขึ้น blockout ของ prop ฉากอย่างรวดเร็ว และเช็ก polycount เทียบงบของ Quest Effort: low [31] 3) ศึกษา metaballs portal ของ The Shaders Bible และ breakdown ของ procedural eyes เป็น reference สำหรับ stylized VFX บน Unity Effort: low [1][9] 4) ทดสอบการจับคู่ shader จาก Blender ไป Unity กับ material สไตล์ไลซ์หนึ่งชิ้น ตามแนว [19][28] Effort: low 5) ทำ spike หนึ่งวันกับ Mixie3D หรือเครื่องมือคุม Blender ด้วย agent ลักษณะเดียวกัน บน procedural prop หนึ่งชิ้น ตัดสินจาก topology และ UV ที่สะอาด ไม่ใช่ภาพเดโม Effort: med [4][38] 6) ถ้ามีทีมงานอยู่ที่เกาหลี พิจารณา G-STAR Unity AI Game Jam (18–19 พ.ย., Busan) เพื่อทดสอบ Meshy ใน Unity build Effort: low [46] 7) ถ้างาน Gaussian Splatting capture ของทีม (VR tour) มีปัญหา exposure ไม่สม่ำเสมอ ให้อ่าน EvenSplat Effort: low [45] ข้าม: bounty ของ Vangrid และโพสต์ physical-AI ที่เกี่ยวข้อง [5][7][10][11]; PlayOnMint [22]; prompt-art และลิสต์เครื่องมือ AI ทั่วไป [12][20][36]; โพสต์ส่วนตัวหรือนอกประเด็น [3][35][47]

## Signals to Watch
- RBDLab 1.6 และ Hurricane ถูกนำไปใช้ใน game pipeline ที่ส่งมอบจริงหรือไม่ ต่างจากแค่ showreel [18][24]
- Blender ที่คุมด้วย agent (Mixie3D) มีรีวิวอิสระ หรือแสดงให้เห็น topology พร้อมใช้ใน production หรือไม่ [4][39]
- asset ของ Meshy ใน build ของ G-STAR Unity AI Game Jam วันที่ 18–19 พ.ย. [46]
- โค้ดของ EvenSplat ถูกปล่อยและถูกนำไปใช้ใน viewer หรือ importer ของ Gaussian Splatting หรือไม่ [45]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ushadersbible | ^4160 c14 | [A small tutorial on how we made the metaballs portal using a particle system. Th](https://x.com/ushadersbible/status/2106290605449937310) |
| x | cghow_ | ^725 c4 | [🔥FREE🔥 Unreal Engine Niagara VFX Tutorials https://t.co/EUZYFbTSXo @unrealengine](https://x.com/cghow_/status/2106384526360428859) |
| x | bilawalsidhu | ^515 c18 | [If you want to understand the techno-religious fervor in AI, go read this cult c](https://x.com/bilawalsidhu/status/2106493590843310549) |
| x | Stefan_3D_AI | ^414 c23 | [I stopped making AI click around Blender. @mixie3D gives agents direct control +](https://x.com/Stefan_3D_AI/status/2106768134581727396) |
| x | evrendag1284 | ^398 c364 | [hello friends , what caught my attention in the @vangrid_io capture flow is that](https://x.com/evrendag1284/status/2106728150554055093) |
| x | DucCryptoX | ^388 c451 | [Niantic spent years building one of the largest 3D capture datasets in the world](https://x.com/DucCryptoX/status/2106342246954283383) |
| x | Bency1749379 | ^376 c448 | [Gm The more I look into Physical AI, the more obvious one thing becomes: robots ](https://x.com/Bency1749379/status/2106223617830723745) |
| x | VFXApprentice | ^351 c2 | [Glitch Challenge by Marjorie ROCHE Made with Unreal, Houdini, Clip Studio Paint ](https://x.com/VFXApprentice/status/2106455996113809724) |
| x | jettelly | ^295 c0 | [Ryan Gee made this stylized take on Eldritch Blast in Unity! The eyes inside the](https://x.com/jettelly/status/2106398881693012244) |
| x | jaouad2d | ^272 c242 | [Agents can now post a bounty in USDC and have someone walk the actual street to ](https://x.com/jaouad2d/status/2106560943375200480) |
| x | _Dripxel | ^251 c266 | [The real breakthrough for AI agents may not be another model. It may be giving t](https://x.com/_Dripxel/status/2106232054396711239) |
| x | goth600 | ^245 c44 | [unreal engine, hyper realistic, Minecraft, photorealistic, reflections, The Lege](https://x.com/goth600/status/2106822881376415965) |
| x | cdvr_szf | ^231 c6 | [Guided Bubbles & Wet Foam Solver in @sidefxhoudini The solver is based on the Wē](https://x.com/cdvr_szf/status/2106681566131024060) |
| x | tofudestiny | ^203 c229 | [an AI agent being able to request a physical-world capture changes the role of t](https://x.com/tofudestiny/status/2106553993036263647) |
| x | YaldaMasoudi | ^198 c210 | [The new agent bounty flow from @vangrid_io solves one problem: how software can ](https://x.com/YaldaMasoudi/status/2106365480101417433) |
| x | 0xZane_ | ^187 c159 | [AI has learned a huge amount from the internet but the real world is a different](https://x.com/0xZane_/status/2106246440884535507) |
| x | Ishaq0x_ | ^171 c214 | [Yesterday checked Docs: https://t.co/wIFAz7cpIi… The main thing I’d break down f](https://x.com/Ishaq0x_/status/2106220126324351122) |
| x | indieforgames | ^161 c1 | [Hurricane is a revolutionary tool integrated into Blender for generating high-fi](https://x.com/indieforgames/status/2106321594276807132) |
| x | jared_nyts | ^157 c1 | [New shader test Left is Blender, right is in-game screenshot https://t.co/gWzJqN](https://x.com/jared_nyts/status/2106844931985645748) |
| x | liluocheng13 | ^153 c36 | [Image : Midjourney + ChatGPT Video : Seedance 2.0, 15s, 720p Epic Chinese dark f](https://x.com/liluocheng13/status/2106255062775517290) |
| x | ChuBe_Cryp | ^146 c183 | [GM CT.. Most people look at Vangrid as a spatial data network. I think that’s to](https://x.com/ChuBe_Cryp/status/2106631987712958464) |
| x | rame9040 | ^122 c152 | [Good afternoon dear X mates @PlayOnMint is taking Web3 entertainment to the next](https://x.com/rame9040/status/2106661561809158280) |
| x | ikramulweb3 | ^118 c128 | [Good night Crypto Twitter 😴 Deploying fleets of corporate vehicles to map the wo](https://x.com/ikramulweb3/status/2106804794782535714) |
| x | 3DxDEV7 | ^110 c6 | [Is Blender officially closing the gap on Houdini for complex VFX and physical de](https://x.com/3DxDEV7/status/2106320750416126074) |
| x | VFXApprentice | ^98 c1 | [Lightning Projectile Game VFX by YUBI_VFX Made using Unreal Engine, Photoshop an](https://x.com/VFXApprentice/status/2106788688462020980) |
| x | Sumon_Web3 | ^85 c78 | [Robots do not fail from a lack of models. They fail from a lack of ground truth.](https://x.com/Sumon_Web3/status/2106751157460951522) |
| x | jettelly | ^71 c1 | [Kaleidos lets you create animated shader patterns without code, then export them](https://x.com/jettelly/status/2106670670079771021) |
| x | Mix3Design | ^68 c0 | [What if you could build your game VFX in Blender and take it straight into your ](https://x.com/Mix3Design/status/2106536704412659768) |
| x | jettelly | ^61 c0 | [Do you work with both Unity and Godot? The Shaders Bible Collection includes 1,1](https://x.com/jettelly/status/2106338474886304102) |
| x | VFXApprentice | ^57 c0 | [Black Hole VFX by Renzo Solorzano Made using Unity, Blender, Photoshop and Subst](https://x.com/VFXApprentice/status/2106879033631744284) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ushadersbible</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4160 · 💬 14</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ushadersbible/status/2106290605449937310">View @ushadersbible on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A small tutorial on how we made the metaballs portal using a particle system. This VFX is available in both Unity and Godot ➡️ https://t.co/hLHBiQ05zV #indiedev https://t.co/5q8B4NSLhm”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@ushadersbible ปล่อยบทเรียนสั้นๆ สอนทำเอฟเฟกต์ portal แบบ metaballs ด้วย particle system โดยมี VFX ให้ใช้ทั้งบน Unity และ Godot</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Metaballs ที่สร้างจาก particle system ไม่ต้องเขียน raymarching เอง ทีมเล็กจึงได้ลุคของเหลวหรือ portal แบบ stylized ในต้นทุนต่ำ และใช้แนวทางเดียวกันได้ทั้งสอง engine</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ให้ทีม Unity ลองทำตามบทเรียนหนึ่งรอบเพื่อสร้าง portal prefab แบบ metaballs ไว้ใช้ใน prototype แล้วเช็กต้นทุนจำนวน particle บนมือถือและ Quest</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ushadersbible/status/2106290605449937310" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@cghow_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 725 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/cghow_/status/2106384526360428859">View @cghow_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🔥FREE🔥 Unreal Engine Niagara VFX Tutorials https://t.co/EUZYFbTSXo @unrealengine #CGHOW #realtimevfx #ue4 #ue5 #ue5niagara #unrealengine #VFX #Game #ue4niagara https://t.co/fFnaCV7w09 https://t.co/rZA”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>CGHOW โพสต์ลิงก์บทเรียน Unreal Engine Niagara VFX ฟรี ครอบคลุมเอฟเฟกต์ real-time ทั้ง UE4 และ UE5</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>บทเรียน Niagara ฟรีเป็นทางเรียนรู้ real-time VFX สำหรับโปรเจกต์ Unreal โดยไม่มีค่าใช้จ่าย แต่โพสต์ไม่ระบุเนื้อหาหรือคุณภาพ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/cghow_/status/2106384526360428859" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 515 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2106493590843310549">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“If you want to understand the techno-religious fervor in AI, go read this cult classic and suddenly it'll all make sense. The dawn of the internet had very similar reactions. https://t.co/bsDED2XhCy”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Bilawal Sidhu แนะนำหนังสือ 'cult classic' เล่มหนึ่ง (ไม่ระบุชื่อ) เพื่อทำความเข้าใจความคลั่งไคล้แบบศาสนาในวงการ AI และบอกว่ายุคเริ่มต้นของอินเทอร์เน็ตก็มีปฏิกิริยาคล้ายกัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2106493590843310549" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Stefan_3D_AI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 414 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Stefan_3D_AI/status/2106768134581727396">View @Stefan_3D_AI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I stopped making AI click around Blender. @mixie3D gives agents direct control + multi-agent workflows + real 3D skills. No more UI simulation. Tested it on my game. One run: full procedural Pegasus w”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X รายงานว่า Mixie3D ให้ AI agent ควบคุม Blender โดยตรงแทนการจำลองการคลิก UI และในการรันครั้งเดียวสร้าง Pegasus แบบ procedural ที่มีขน ปีก และ control rig ที่ agent สร้างเอง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การควบคุม Blender ระดับ API โดยตรงแทนการสั่งผ่านหน้าจอ ทำให้ agent สร้าง 3D asset ได้เร็วและเสถียรกว่า แต่นี่เป็นเพียงเดโมเดียว ไม่ใช่ benchmark</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ให้ 3D artist ลอง Mixie3D กับ prop หรืองาน rig ชิ้นเล็กๆ หนึ่งชิ้น แล้วเทียบเวลาและผลลัพธ์กับ workflow Blender แบบ manual ที่ใช้อยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Stefan_3D_AI/status/2106768134581727396" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@evrendag1284</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 398 · 💬 364</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/evrendag1284/status/2106728150554055093">View @evrendag1284 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“hello friends , what caught my attention in the @vangrid_io capture flow is that privacy and quality are handled before a clip ever becomes a bounty submission. You open Capture Data, allow the camera”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์อธิบายแอป crowdsourced 3D capture ที่ blur ใบหน้าและป้ายทะเบียนบนอุปกรณ์ก่อน encode แล้วตรวจคุณภาพคลิปอัตโนมัติ (ความยาว ความชัด การครอบคลุม) ก่อนส่ง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การตรวจคุณภาพและ anonymize ข้อมูลบนอุปกรณ์ก่อน upload เป็น pattern ที่ทีมเล็กนำไปใช้กับ pipeline ที่รับภาพหรือสแกนจากผู้ใช้ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้ามีฟีเจอร์ให้ผู้ใช้ส่งสแกนหรือวิดีโอ ให้เพิ่มการตรวจ coverage และคุณภาพบนอุปกรณ์ก่อน upload เพื่อกันข้อมูลคุณภาพต่ำตั้งแต่ต้นทาง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/evrendag1284/status/2106728150554055093" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@DucCryptoX</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 388 · 💬 451</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/DucCryptoX/status/2106342246954283383">View @DucCryptoX on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Niantic spent years building one of the largest 3D capture datasets in the world, almost as a side effect of a mobile game. Players walked around, pointed a phone at a landmark, played for a few minut”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ข้อมูลสแกน 3D ของ Niantic เกิดแบบ passive จากผู้เล่นเกมในที่ที่คนอยู่แล้ว ส่วน Vangrid จะเก็บภาพเฉพาะหลังผู้ซื้อจ่ายเงินขอให้ capture สถานที่นั้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เปรียบเทียบสองวิธีหา 3D capture data: ได้มาโดยบังเอิญจากฝูงชน กับ capture ตามสั่งที่มีคนจ่ายเงิน โพสต์นี้โปรโมต Vangrid และไม่มีข้อมูลหรือสเปกจริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/DucCryptoX/status/2106342246954283383" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Bency1749379</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 376 · 💬 448</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Bency1749379/status/2106223617830723745">View @Bency1749379 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gm The more I look into Physical AI, the more obvious one thing becomes: robots don’t just need better models. They need better data about the physical world. That’s the problem @vangrid_io is tacklin”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์โปรโมตระบุว่า Vangrid เปลี่ยนสมาร์ทโฟนเป็นเครือข่ายสแกน 3D เพื่อเก็บข้อมูลโลกจริงให้ Physical AI, บันทึกหลักฐานบน onchain, เปิดใช้งานบนเว็บและ Android และระดม seed $9M</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สะท้อนว่ามีความต้องการข้อมูล 3D ที่ crowd-source ผ่านมือถือเพื่อเทรนหุ่นยนต์ แต่โพสต์เป็นการโปรโมต ไม่มีรายละเอียดคุณภาพการสแกน ราคา หรือ API</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Bency1749379/status/2106223617830723745" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VFXApprentice</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 351 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VFXApprentice/status/2106455996113809724">View @VFXApprentice on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Glitch Challenge by Marjorie ROCHE Made with Unreal, Houdini, Clip Studio Paint and Blender https://t.co/Ze4PqpKAX9 #TechArt #VFX #Houdini https://t.co/YlV5GGfNzi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Marjorie Roche ศิลปิน VFX โพสต์ผลงาน Glitch Challenge ที่ทำด้วย Unreal, Houdini, Clip Studio Paint และ Blender ภายใต้แท็ก #TechArt และ #VFX</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แสดง pipeline หลายเครื่องมือที่ใช้งานได้จริง: Houdini ทำ FX, Unreal เรนเดอร์ real-time, Blender ทำ 3D และ Clip Studio Paint ทำงาน 2D เป็นตัวอย่างอ้างอิงสำหรับเอฟเฟกต์ glitch แนว stylized</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VFXApprentice/status/2106455996113809724" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
