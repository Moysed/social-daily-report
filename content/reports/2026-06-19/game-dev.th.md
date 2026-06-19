---
type: social-topic-report
date: '2026-06-19'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-19T03:16:35+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 189
salience: 0.82
sentiment: mixed
confidence: 0.72
tags:
- unreal-engine
- ue6
- mcp
- godot
- xr
- ai-pipeline
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2067251426854588416/img/cB-kW1Dd-9uFXEYa.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-19

## TL;DR
- Unreal Engine 5.8 เปิดตัววันนี้พร้อม MCP server support แบบ experimental ให้ AI agents เชื่อมต่อเข้า engine pipeline ได้โดยตรง [1][8] บวก Mesh Terrain แบบ experimental [7], markerless MetaHuman motion capture [13], และ lighting path 'Lumen Lite' ที่ Epic ระบุว่าเร็วขึ้น ~2x บน Switch 2 [3][47]
- Epic ประกาศ UE6: Early Access เป้าหมายปลาย 2027, Blueprints ยังรองรับใน Early Access และ release แรก แต่จะถูก deprecated เมื่อ Verse กลายเป็น gameplay programming model หลักและ Actors/Blueprints ถูกยกเลิก โดยมี 'conversion tools' รองรับ [12][37]
- การ deprecated Blueprint ถูกต่อต้านทันทีจากนักการศึกษาและ technical artists/designers ที่พึ่งพา visual scripting [6][29][27][48]
- Epic open-source 'Lore' ซึ่งเป็น version control system สร้างใหม่จากศูนย์เพื่อ scalability [9]; UE5 และ UEFN กำลังรวมเป็น editor เดียวกัน [25]
- Godot 4.7 ออกแล้ว พร้อม Day-One XR support สำหรับ AndroidXR และ SteamOS/Steam Frame บวก native-pixel (PSX-style) rendering [14][24][36]

## สิ่งที่เกิดขึ้น
State of Unreal 2026 [50][59] เป็นงานหลักของวัน Epic ส่ง Unreal Engine 5.8 พร้อม MCP server support แบบ experimental ให้ AI agents ทำงานในโปรเจกต์ได้โดยตรง [1][8][21] พร้อม Mesh Terrain (ไม่ใช่ heightfield, แบ่งพาร์ทิชันเพื่อ collaboration) [7], real-time vegetation และ simplified lighting [10], MetaHuman Animator markerless mocap จากวิดีโอทั่วไป [13], ตัวอย่าง rigging/animation คุณภาพ production อย่าง Zebra [17], และ global-illumination path 'Lumen Lite' ที่ Epic อ้างว่าเร็วกว่าเดิมประมาณสองเท่าบน Nintendo Switch 2 ที่ visual ระดับใกล้เคียงกัน [3][47] Epic ยัง open-source 'Lore' ซึ่งเป็น version control system ใหม่ [9] และยืนยันว่า UE5 กับ UEFN กำลังรวมเป็น editor เดียว [25] UE MCP server ยังถูกเพิ่มเข้า Hermes Agent MCP Catalog [20] ด้วย

## ทำไมถึงสำคัญ (เหตุผล)
มีสองสัญญาณที่เกินกว่าแค่ shop ที่ใช้ Unreal อันดับแรก MCP ฝังตัวอยู่ใน engine รายใหญ่แล้วและอยู่ใน agent catalog [1][20] — protocol เดียวกับที่ NDF DEV ใช้ผ่าน UnityMCP อยู่แล้ว สิ่งนี้ชี้ว่า AI agents ที่ทำงานภายใน engine editor จะเป็น production pattern จริงในระยะใกล้ ไม่ใช่แค่ demo อันดับสอง การที่ Epic เลือก deprecated Blueprints เพื่อหันมาใช้ Verse [12][37] แสดงให้เห็นว่า vendor พร้อมทำลาย ecosystem ที่ลึกซึ้งเพื่อผลักดัน workflow แบบ code-and-AI-centric และการต่อต้านจากนักการศึกษาและ technical artists [6][29] ยืนยันว่า visual scripting accessibility เป็น production dependency จริง ไม่ใช่แค่ตัวเลือกเสริม Day-One XR support ของ Godot สำหรับ AndroidXR และ Steam Frame [24] ขยายตัวเลือก open-source ที่น่าเชื่อถือสำหรับทีม XR/VR ส่วน timeline UE6 ปี 2027 [12] ยังส่งสัญญาณว่าจะมีความปั่นป่วนสำหรับทุกคนที่วางแผนโปรเจกต์ Unreal ระยะยาว

## ความเป็นไปได้
**มีแนวโน้มสูง:** AI-agent-in-editor tooling จะแพร่กระจายไปทั่ว engine ภายในหนึ่งปี เนื่องจาก MCP support ลงจอดใน UE5.8 และ Hermes catalog แล้ว [1][20] และ Unity มีแนวโน้มจะตามมา **เป็นไปได้:** การ deprecated Blueprint จะผลักนักพัฒนา Unreal สาย hobbyist และทีมเล็กๆ ไปหา Godot ซึ่งสอดคล้องกับที่นักพัฒนาระบุ Godot เป็นทางเลือกสำรองชัดเจน [27] และ momentum ของ Godot [14][16] **ไม่น่าเกิดขึ้นในระยะใกล้:** การเปลี่ยนแปลงจาก UE6 จะกระทบ NDF DEV โดยตรง เพราะ Early Access ยังอีกถึงปลาย 2027 และ studio เน้น Unity เป็นหลัก [12] ไม่มีแหล่งข้อมูลใดให้ตัวเลขความน่าจะเป็น ตัวเลขที่แน่ชัดมีเพียง '2x' ของ Epic สำหรับ Switch 2 lighting [3] และเป้าหมาย Early Access ปี 2027 [12] ซึ่งทั้งหมดมาจาก vendor

## การนำไปใช้ใน NDF DEV
1) ประเมิน MCP patterns แบบ embedded ใน engine เทียบกับ UnityMCP setup ที่มีอยู่ เพื่อดูว่า agent-in-editor workflows ใดใช้งานได้จริงแล้ว (low effort, ศึกษาเท่านั้น) [1][20][8] 2) ทดลอง Godot 4.7 สำหรับ XR/VR prototype เพราะ Day-One AndroidXR และ Steam Frame support ตรงกับงาน XR ของคุณ (med effort) [24][14] 3) ถ้ามีงาน character animation ในแผน ให้จดไว้ว่า markerless MetaHuman mocap ช่วยลดต้นทุนการ capture ได้ แต่ผูกกับ Unreal (low effort, awareness) [13] **ข้าม:** UE6 migration planning, Verse, และเรื่อง Blueprint deprecation — ไม่เกี่ยวกับ Unity studio บน timeline 2027 [12][37] **ข้าม:** 'Lore' VCS เว้นแต่จะเจอปัญหา version-control scaling [9] หมายเหตุ: Unity engine news วันนี้แทบไม่มี — Unity items ส่วนใหญ่เป็น indie showcases [32][49][56][60] จึงไม่มี Unity-specific action จาก batch นี้

## สัญญาณที่ต้องติดตาม
- UE6 Early Access ปลาย 2027 พร้อม Blueprint→Verse deprecation และ conversion tools ที่ให้คำมั่น — ติดตามว่า conversion จะรักษา accessibility ได้จริงหรือไม่ [12][37]
- MCP ที่กำลัง standardize ข้าม engine (UE5.8 native + Hermes catalog) — เกี่ยวโยงกับทิศทาง UnityMCP ของคุณ [1][20]
- Godot XR momentum: AndroidXR และ Steam Frame Day-One support [24]
- Epic Games Store ใช้จ่ายถึง $1.16B ในปี 2025 เพิ่มขึ้น 6% YoY — ข้อมูล distribution channel [57]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | UnrealEngine | ^7114 c228 | [Unreal Engine 5.8 ships today with experimental MCP server support: Your sources](https://x.com/UnrealEngine/status/2067251500900839735) |
| x | iKaito_1 | ^3284 c133 | [HoYoverse's New Upcoming Open-World UE5 Game, "Varsapura", Has Been Approved for](https://x.com/iKaito_1/status/2067500691997016284) |
| x | Pirat_Nation | ^2657 c62 | [Epic Games has released a major Unreal Engine 5 update that runs twice as fast o](https://x.com/Pirat_Nation/status/2067578573461020771) |
| x | _mayaamano | ^2270 c1 | [TEDI 67 IN 4K QUALITY REMAKE UNREAL ENGINE 6 https://t.co/AxDFapjByT](https://x.com/_mayaamano/status/2067752437620809740) |
| x | AdweetiyaK | ^1916 c4 | [@chakravartiiin Base consoles are 90% of their market at launch. Looking at thei](https://x.com/AdweetiyaK/status/2067621725517602841) |
| x | spectraimsim | ^1792 c34 | [if Epic stops supporting Blueprint, it will singlehandedly kill the entire Unrea](https://x.com/spectraimsim/status/2067585625608368483) |
| x | UnrealEngine | ^1696 c33 | [More than mesh! Mesh Terrain is a new experimental feature in Unreal Engine 5.8.](https://x.com/UnrealEngine/status/2067249231887225179) |
| x | Polymarket | ^1562 c92 | [NEW: Unreal Engine 5.8 is launching with experimental MCP server support, allowi](https://x.com/Polymarket/status/2067509115186717133) |
| x | UnrealEngine | ^1449 c49 | [Introducing Epic's version control system: Lore! Built from scratch and open-sou](https://x.com/UnrealEngine/status/2067270962500767925) |
| x | UnrealEngine | ^1389 c32 | [Unreal Engine 5.8 is now live! Build your immersive worlds with advanced terrain](https://x.com/UnrealEngine/status/2067302914851319954) |
| x | UnrealEngine | ^1244 c74 | [Kate Rayner joins us to talk about how @CoalitionGears is using Unreal Engine to](https://x.com/UnrealEngine/status/2067256301395034305) |
| x | UnrealEngine | ^1237 c366 | [Hey Everyone. Our aim is to ship Early Access for UE6 by the end of 2027 and Blu](https://x.com/UnrealEngine/status/2067661808903577646) |
| x | UnrealEngine | ^1096 c20 | [Drive characters' bodies, faces, and more from regular video with the MetaHuman ](https://x.com/UnrealEngine/status/2067249920055148686) |
| x | godotengine | ^1087 c33 | [#GodotEngine 4.7 is here! 🎉 Like a cult classic movie, Godot 4 has only gotten b](https://x.com/godotengine/status/2067613808235810867) |
| x | S_whispersEN | ^1032 c40 | [Silent Whispers / Birds-Eye View Tech Demo Real-time rendered Beak-time approved](https://x.com/S_whispersEN/status/2067578076129645050) |
| x | Kureca8 | ^946 c7 | [godot is the only existing engine that developers truly love and this love grows](https://x.com/Kureca8/status/2067672013246804256) |
| x | UnrealEngine | ^713 c10 | [Check out the Zebra Sample, a production-quality sample built inside UE on full ](https://x.com/UnrealEngine/status/2067351735891636438) |
| x | AroushTheKween | ^561 c5 | [Seraphine looks STUNNING at the Teamfight Tactics - Unreal Engine Demo 💖✨ #Serap](https://x.com/AroushTheKween/status/2067493324953677917) |
| x | Grummz | ^497 c50 | [There are soooo many people freaking out that blueprints are being removed from ](https://x.com/Grummz/status/2067760802308960430) |
| x | Teknium | ^454 c40 | [Unreal Engine's new MCP is now part of the Hermes Agent MCP Catalog - making it ](https://x.com/Teknium/status/2067644504669315583) |
| x | UnrealEngine | ^450 c19 | [Just announced live: Unreal Engine 5.8 is releasing today! We've focused on push](https://x.com/UnrealEngine/status/2067248971295121474) |
| x | UnrealEngine | ^435 c17 | [Verse is a next-generation programming language, purpose-built to power massive,](https://x.com/UnrealEngine/status/2067269183935586548) |
| x | thegamersjoint | ^374 c2 | [Lets compare the two builds of Kingdom Hearts 4 we've been able to see so far! 👀](https://x.com/thegamersjoint/status/2067623620172800134) |
| x | SadlyItsBradley | ^331 c8 | [Godot 4.7 has released and adds a bunch of "Day One" support and new features fo](https://x.com/SadlyItsBradley/status/2067680624974926324) |
| x | UnrealEngine | ^314 c24 | [UE6 is about evolving how we ship and operate games. As UE5 and UEFN merge into ](https://x.com/UnrealEngine/status/2067270394956906693) |
| x | UnrealEngine | ^311 c5 | [We're joined by Tor Frick, Creative Director at Neon Giant to talk about @NOLAWt](https://x.com/UnrealEngine/status/2067259760160780489) |
| x | spectraimsim | ^269 c18 | [I've spent the past 7 years of my life building skills in Unreal Engine, but if ](https://x.com/spectraimsim/status/2067745705691673037) |
| x | ray_ervian | ^269 c6 | [progress on recreating lost media #gamedev #indiedev https://t.co/wDdwhoaZka](https://x.com/ray_ervian/status/2067635274939847081) |
| x | SpatialBiggs | ^268 c34 | [Unreal Engine 6 blueprint deprecation is devastating news. While it is tough to ](https://x.com/SpatialBiggs/status/2067547569052393944) |
| x | KhymTFT | ^258 c12 | [🚀 Riot goes ALL IN on TFT - Why moving to Unreal Engine? At Unreal Fest 2026, Ri](https://x.com/KhymTFT/status/2067505777460593022) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 7114 · 💬 228</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2067251500900839735">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Unreal Engine 5.8 ships today with experimental MCP server support: Your sources, your pipeline and your workflow—simply configure the MCP plugin and connect to any agent. Get familiar with the MCP se”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine 5.8 ออกแล้ววันนี้ พร้อม MCP server plugin แบบ experimental ที่เชื่อม UE เข้ากับ AI agent ใดก็ได้ และ PCG Primitive Plugin สำหรับ procedural content</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>MCP เข้ามาใน game engine ชั้นนำแล้ว — ทีม UE wire AI agent เข้า asset pipeline ได้โดยตรง ไม่ต้องสร้าง custom bridge เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">โปรเจกต์ที่ใช้ UE ลอง MCP plugin เชื่อม agent เพื่อ automate งาน PCG setup หรือ asset config ได้เลย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2067251500900839735" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@iKaito_1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3284 · 💬 133</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/iKaito_1/status/2067500691997016284">View @iKaito_1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“HoYoverse's New Upcoming Open-World UE5 Game, &quot;Varsapura&quot;, Has Been Approved for Software Copyright. &gt; Thoughts ? Graphics looks so crazy #Varsapura #Hoyoverse”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>เกม open-world UE5 ชื่อ 'Varsapura' ของ HoYoverse ผ่านการขึ้นทะเบียน software copyright ในจีนแล้ว พร้อมภาพกราฟิกที่ทำให้โซเชียลฮือฮา</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/iKaito_1/status/2067500691997016284" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2657 · 💬 62</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2067578573461020771">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Epic Games has released a major Unreal Engine 5 update that runs twice as fast on Nintendo Switch 2. The update introduces a new lighting system called Lumen Lite. According to Epic, it is “twice as f”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Epic Games ปล่อยอัปเดต UE5 พร้อม Lumen Lite ระบบ global illumination เร็วกว่า Lumen High Quality 2× ทำให้ได้ 60 FPS บน Nintendo Switch 2</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Epic ดัน UE5 ให้รันบน handheld GPU ได้จริง — ทีมที่ target Switch 2 หรือ mobile-tier มีตัวเลือก dynamic GI ที่ใช้ได้แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้ามีโปรเจกต์ UE5 ที่ target Switch 2 หรือ mobile-tier GPU ให้เปลี่ยน default GI เป็น Lumen Lite แล้ว benchmark frame time เทียบกัน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2067578573461020771" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@_mayaamano</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2270 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/_mayaamano/status/2067752437620809740">View @_mayaamano on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“TEDI 67 IN 4K QUALITY REMAKE UNREAL ENGINE 6 https://t.co/AxDFapjByT”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ครีเอเตอร์ปล่อย fan remake 'TEDI 67' ความละเอียด 4K สร้างด้วย Unreal Engine 6 แสดง visual ceiling ของ engine ในปัจจุบัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ผลงาน UE6 จริงจาก indie creator ที่ 4K ให้ visual benchmark ชัดเจนสำหรับทีม game dev ใช้อ้างอิงตอน pitch scope</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีมดู demo นี้เพื่อ calibrate art-quality expectation ตอน scope project Unity vs UE6 ให้ลูกค้า</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/_mayaamano/status/2067752437620809740" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AdweetiyaK</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1916 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AdweetiyaK/status/2067621725517602841">View @AdweetiyaK on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“@chakravartiiin Base consoles are 90% of their market at launch. Looking at their past games like RDR2 it'll be heavily optimised and smooth unlike other UE5 slop. Rockstar never compromises on qualit”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>user คนนึงแย้งว่า Rockstar โฟกัส optimize บน base console เป็นหลัก (อ้าง RDR2) และที่ delay บ่อยเพราะยึด quality — ต่างจากเกม UE5 ที่ optimize ไม่ดี</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AdweetiyaK/status/2067621725517602841" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@spectraimsim</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1792 · 💬 34</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/spectraimsim/status/2067585625608368483">View @spectraimsim on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“if Epic stops supporting Blueprint, it will singlehandedly kill the entire Unreal Engine educational ecosystem. The announcement of UE5 back in 2020 was exciting; the announcement of UE6 today carries”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Epic ประกาศ Unreal Engine 6 วันนี้ ชุมชน game dev กังวลว่า Blueprint จะถูกตัดออก ซึ่งจะทำลาย ecosystem การเรียน UE ทั้งหมดที่พึ่งพา visual scripting เป็นจุดเริ่มต้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า Blueprint ถูกตัด e-learning ที่โฟกัส UE จะได้รับผลกระทบโดยตรง เพราะ learner ส่วนใหญ่ใช้ Blueprint หลีกเลี่ยง C++ ทำให้ entry barrier สูงขึ้นมาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">หยุดพัฒนา UE-based e-learning module ใหม่ก่อน รอ Epic ประกาศ roadmap Blueprint อย่างเป็นทางการใน UE6</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/spectraimsim/status/2067585625608368483" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1696 · 💬 33</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2067249231887225179">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“More than mesh! Mesh Terrain is a new experimental feature in Unreal Engine 5.8. Author complex terrain without being locked to a heightfield. It’s more than just mesh—it’s partitioned for collaborati”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine 5.8 เปิดตัว Mesh Terrain (experimental) — ระบบ terrain ที่ไม่ถูกจำกัดด้วย heightfield รองรับ 3D mesh editing, world partition streaming และ collaborative authoring หลายคนพร้อมกัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่สร้าง open-world หรือ environment ที่มี overhang/ถ้ำใน UE5 ไม่ต้องใช้ static mesh อุดช่องอีกต่อไป — แก้ terrain geometry ได้โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทดสอบ Mesh Terrain บน UE5.8 branch ในโปรเจกต์ที่ตอนนี้ใช้ static mesh อุดจุดอ่อนของ heightfield อยู่</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2067249231887225179" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Polymarket</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1562 · 💬 92</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Polymarket/status/2067509115186717133">View @Polymarket on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NEW: Unreal Engine 5.8 is launching with experimental MCP server support, allowing AI agents to work directly on game development.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unreal Engine 5.8 เตรียมเปิดตัวพร้อม experimental MCP server support — แหล่งข่าวคือ Polymarket ไม่ใช่ Epic Games ยังไม่ confirmed</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้าจริง MCP ใน game engine หลักหมายความว่า AI agents แก้ scene และ asset ใน editor ได้โดยตรง ไม่ใช่แค่ side tool อีกต่อไป</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">รอ official announcement จาก Epic Games ถ้า confirmed ให้ทีม Unity เช็คว่า Unity MCP tooling (early access อยู่แล้ว) ทำได้เทียบเท่ากันไหม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Polymarket/status/2067509115186717133" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
