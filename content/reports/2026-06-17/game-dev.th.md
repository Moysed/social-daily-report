---
type: social-topic-report
date: '2026-06-17'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-17T15:15:00+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 185
salience: 0.82
sentiment: positive
confidence: 0.7
tags:
- game-dev
- unreal-engine
- unity
- godot
- xr
- ai-pipelines
thumbnail: https://pbs.twimg.com/media/HK9R_uOXAAAFid3.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-17

## TL;DR
- Epic ส่ง Unreal Engine 5.8 ใน Unreal Fest Chicago 2026 พร้อม MCP server support แบบ experimental ให้ agent เชื่อมต่อกับ editor pipeline ได้ [34][37], ยืนยัน Lumen ทำงานบน Nintendo Switch 2 [5][22][40] และเพิ่มระบบ Mesh Terrain (non-heightfield) แบบ experimental [32]
- Epic กำหนด timeline ของ UE6: Early Access ปลายปี 2027 full release อีก 12–18 เดือนถัดมา โดยรวม UE5 และ Unreal Editor for Fortnite เป็นผลิตภัณฑ์เดียว [20][55][58]; รองรับการพกพา Fortnite Outfit ข้ามเกม [15]
- Unity 6.5 ออกตัวพร้อม Physics 2D updates, Graph Templates, mobile post-processing แบบประหยัดแบตเตอรี่ และ light explorer ที่ปรับแต่งได้ [30]
- OpenXR vendor plugin ของ Godot รองรับแว่น XReal Aura บน Android XR แสดงร่วมกับ Google/XReal ใน AWE [38]; Godot 4.7 snapshot แก้ critical regressions สำคัญ [25]
- AI เข้าสู่ workflow ของ Epic เอง: concept artists ใช้ Nano Banana สำหรับ ideation [8] และ MetaHuman Animator เพิ่ม markerless mocap (ไม่ต้องใส่ชุด) บน Fab [42]

## What happened
Unreal Fest Chicago 2026 ขับเคลื่อนข่าวส่วนใหญ่ของวัน Epic ปล่อย UE 5.8 [37][46] พร้อม MCP server support แบบ experimental สำหรับเชื่อมต่อ agent ภายนอกกับ editor [34], Lumen บน Switch 2 ด้วย GPU cost ที่ต่ำลง [5][22][40], Mesh Terrain แบบ experimental [32], MetaHuman markerless motion capture บน Fab [42] และคอร์ส Unreal กว่า 20 คอร์สให้ฟรีบน Epic Developer Community [21] นอกจากนี้ยังประกาศ UE6: Early Access เล็งปลายปี 2027 full release อีก 12–18 เดือนถัดมา วางตำแหน่งเป็นการรวม UE5 กับ UEFN เป็นผลิตภัณฑ์เดียวใน ~สองปี [20][55][58] พร้อมรองรับ cross-game Fortnite Outfit [15] มีการ tease Simpsons x UEFN ก่อนงาน [1][2][18] และ Epic โชว์ AI ใน art pipeline ผ่าน Nano Banana [8]

## Why it matters (reasoning)
MCP server ใน UE 5.8 คือสัญญาณชัดเจน: Epic เปิด editor ให้ agent tooling ผ่าน open protocol [34] สอดคล้องกับทิศทาง devtools ที่มุ่งสู่ agent-connected pipelines Physics 2D และ mobile post-processing ของ Unity 6.5 [30] รวมถึง Android XR/XReal support ของ Godot [38] ตรงกับ stack จริงของ NDF — Unity games, mobile และ XR — มากกว่าพาดหัวของ Unreal ทั้งหมด UE6 timeline มีความสำคัญเฉพาะในแง่ planning: ไม่มีอะไรออกก่อนปลายปี 2027 และการรวม UE5/UEFN หมายถึง tooling churn ที่จะตามมา ไม่ใช่ action item ระยะใกล้ [20][55] WebGL/Three.js และ browser demo แบบ pure-math [11][57] ยืนยันว่า web 3D น้ำหนักเบายังทำได้โดยไม่พึ่ง engine หนัก เหมาะกับ web/mobile delivery การนำ AI เข้า pipeline ของ Epic เอง [8] และเครื่องมือ markerless mocap [42] ลดต้นทุน animation และ concept work สำหรับทีมเล็ก

## Possibility
น่าจะเกิดขึ้น: agent/MCP integration แพร่กระจายข้ามเครื่องยนต์ต่าง ๆ หลัง Epic ส่งแบบ experimental ใน UE 5.8 [34]; คาดว่าจะมี hook แบบเดียวกันที่อื่นภายในหนึ่งปี น่าจะเกิดขึ้น: studio มากขึ้นหันใช้ Android XR ผ่าน OpenXR plugin ของ Godot เมื่อแว่น Aura-class ออกวางขาย [38] เป็นไปได้: UE6 Early Access เลื่อนหรือออกมาไม่สมบูรณ์ เนื่องจาก scope การรวม UE5 กับ UEFN มีขนาดใหญ่ [20][55] เป็นไปได้: Wuthering Waves ย้ายไป UE build ใหม่กว่าจากรายงาน backporting ที่เกิดซ้ำ แต่นี่คือ speculation ไม่ใช่ข้อมูลยืนยัน [3][10][23][24] ไม่น่ากระทบ NDF ระยะสั้น: ecosystem Fortnite cross-game Outfit [15] ซึ่งเป็น Epic-platform-specific

## Org applicability — NDF DEV
ทดสอบ battery-saving mobile post-processing และ Physics 2D ของ Unity 6.5 บน sandbox branch ก่อน upgrade production projects — เกี่ยวข้องกับ mobile titles (effort: med) [30] ประเมิน OpenXR vendor plugin ของ Godot + XReal Aura สำหรับ XR/VR prototyping บน Android XR (effort: med) [38] ทดลอง MCP server แบบ experimental ของ UE 5.8 เป็น reference สำหรับการเชื่อมต่อ AI agents กับ engine tooling แม้จะอยู่บน Unity — pattern นี้ transfer ได้ (effort: low อ่าน, high adopt) [34] ชี้ junior staff ไปที่คอร์ส Unreal กว่า 20 คอร์สฟรีสำหรับเสริมทักษะ 3D/Blueprint/C++ (effort: low) [21] ประเมิน MetaHuman markerless mocap สำหรับ character animation ต้นทุนต่ำหากมีงาน UE (effort: med) [42] ใช้ WebGL/Three.js 5.7MB multiplayer build เป็น reference สำหรับ lightweight web game delivery (effort: low) [11] ข้าม: UE6 timeline ในฐานะ action item — ไกลเกินไปสำหรับ planning นอกจาก awareness [20][55]; Fortnite Outfit interop [15]; discourse เรื่อง Wuthering Waves/Simpsons/Halo [3][9][23] ซึ่งเป็น fan signal ไม่ใช่ engineering

## Signals to Watch
- MCP server support ที่เข้าสู่ engines — UE 5.8 experimental วันนี้; จับตา Unity/Godot equivalents [34]
- Android XR momentum: Godot OpenXR + XReal Aura แสดงใน AWE กับ Google [38]
- Unity 6.5 mobile post-processing และ Physics 2D ที่สุกพร้อมสำหรับงาน mobile ที่ต้องประหยัดแบตเตอรี่ [30]
- AI ใน production art: Epic ใช้ Nano Banana และ markerless mocap เป็น standard tooling [8][42]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | ShiinaBR | ^3903 c52 | [SIMPSONS UEFN WILL LIKELY BE ANNOUNCED TOMORROW Unreal Engine just posted a teas](https://x.com/ShiinaBR/status/2066961185652576583) |
| x | HYPEX | ^2793 c62 | [SIMPSONS x UEFN MIGHT GET ANNOUNCED TOMORROW Unreal Engine posted a teaser for U](https://x.com/HYPEX/status/2066962076480786639) |
| x | Riju1T_T | ^2234 c88 | [Wuwa 3.5 beta info// NOT A LEAK- THIS IS JUST SPECULATIONS As you may have notic](https://x.com/Riju1T_T/status/2066929143527428184) |
| x | MortalCrux | ^1385 c30 | [Based on feedback from the inventory physics update, additional gear and clothin](https://x.com/MortalCrux/status/2066545937963434286) |
| x | Stealth40k | ^1283 c22 | [Unreal Engine 5.8 Lumen Light functionality is compatible with Switch 2. Preserv](https://x.com/Stealth40k/status/2067250232912482784) |
| x | boxhead20277086 | ^1222 c8 | [Guys... I think Sonic found something in the hills #indiedev #robloxstudio #Robl](https://x.com/boxhead20277086/status/2066944593908953260) |
| x | wuwaguy | ^1188 c31 | [From the release of Septimont and V2.4, we're getting insane quality stuffs whet](https://x.com/wuwaguy/status/2066933181614567832) |
| x | UnrealEngine | ^1108 c241 | [Here's a look at how Epic's artists approach concept work. From blank canvas to ](https://x.com/UnrealEngine/status/2066686216779509850) |
| x | nygma0451 | ^895 c18 | [What happened to Quake &amp; Unreal is a 50x less embarrassing that what's happe](https://x.com/nygma0451/status/2066934810388402455) |
| x | my_Shorekeeper | ^742 c15 | [KURO is taking features from UNREAL ENGINE 5.8 !!! &gt;Which is not even officia](https://x.com/my_Shorekeeper/status/2066933567020495123) |
| x | zeuuss_01 | ^726 c20 | [TWO DEVS BUILT A FULL MULTIPLAYER 3D GAME WITH WEBGL + THREE.JS - IN 5.7MB. NO U](https://x.com/zeuuss_01/status/2066949488682639703) |
| x | S_whispersEN | ^700 c15 | [#SilentWhispers Unlock the highlights from Unreal Fest Chicago 2026⏳ We're thril](https://x.com/S_whispersEN/status/2067126081988235389) |
| x | ID_AA_Carmack | ^679 c17 | [In the tradition of @fabynou 's game engine books, Bas Smits (on X?) has made th](https://x.com/ID_AA_Carmack/status/2066577536339923091) |
| x | PotentKnight | ^588 c4 | [The road that lead to a place where the time feel still Hope you have a great on](https://x.com/PotentKnight/status/2066688457942987012) |
| x | HYPEX | ^537 c28 | [FORTNITE SKINS x UNREAL ENGINE 6 • Devs will be able to let players use their ow](https://x.com/HYPEX/status/2067261244889821327) |
| x | aynekko | ^531 c8 | [A few screenshots of the city location from my game. #DiffusionFPS #indiedev #ga](https://x.com/aynekko/status/2066934311966687726) |
| x | itchio | ^517 c7 | [Hello everyone, the site is back now and we're still working on verifying things](https://x.com/itchio/status/2066911505828954447) |
| x | UnrealEngine | ^504 c18 | [The State of Unreal is tomorrow! We've brought in some extra help for production](https://x.com/UnrealEngine/status/2066959880347668622) |
| x | pepie_21 | ^426 c3 | [@feeniesworth this would be so good if it was godot instead of edgeworth](https://x.com/pepie_21/status/2067011788294521271) |
| x | HYPEX | ^425 c14 | [UNREAL ENGINE 6 EARLY ACCESS IS COMING LATE 2027 Epic says UE6 is basically UE5 ](https://x.com/HYPEX/status/2067260019687461106) |
| x | UnrealEngine | ^385 c7 | [20+ professional Unreal Engine courses are now FREE on the Epic Developer Commun](https://x.com/UnrealEngine/status/2066756710166093914) |
| x | necrolipe | ^372 c15 | [Epic anuncia suporte ao Lumen Light para a Unreal Engine 5.8 no Nintendo Switch ](https://x.com/necrolipe/status/2067248147026288868) |
| x | OpalDesuwa | ^360 c20 | [Kuro needs to transition to UE5, the current build is extremely unstable.](https://x.com/OpalDesuwa/status/2066945679008702803) |
| x | WuWa_Ani_Info | ^343 c19 | [🚨Wuthering Waves might be planning to Upgrade to UE5!! in v3.5 Beta Kuro added U](https://x.com/WuWa_Ani_Info/status/2066928552742686860) |
| x | godotengine | ^329 c8 | [Thanks to your help, we've been able to identify and address even more critical ](https://x.com/godotengine/status/2066611724812218709) |
| x | RobloxFactsNews | ^310 c4 | [I dont know what else to say. Play something else. Use Godot or some shit. If yo](https://x.com/RobloxFactsNews/status/2067091453419897009) |
| x | IRONY_the_game | ^308 c10 | [THE IRONY Kickstarter pre-launch page is now live. Check it out now, and please ](https://x.com/IRONY_the_game/status/2066951928786141359) |
| x | shkinteractive | ^234 c8 | [It's been a long time since I last shared anything about the project, so here's ](https://x.com/shkinteractive/status/2066969182495817976) |
| x | UnrealEngine | ^224 c14 | [State of Unreal is 24 hours away and we're eager to show you what we've been wor](https://x.com/UnrealEngine/status/2066883800559398940) |
| x | unitygames | ^207 c4 | [Unity 6.5 is here ⚒️ Upgrade today and level up your project with powerful Physi](https://x.com/unitygames/status/2066903695564874189) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ShiinaBR</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3903 · 💬 52</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ShiinaBR/status/2066961185652576583">View @ShiinaBR on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“SIMPSONS UEFN WILL LIKELY BE ANNOUNCED TOMORROW Unreal Engine just posted a teaser for it (Thanks to @MoralzzX for the info) https://t.co/HxENo1Hr59”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Leaker @ShiinaBR คาดว่า Epic จะประกาศ UEFN map ธีม The Simpsons วันถัดไป โดยอ้าง teaser จาก Unreal Engine เป็นหลักฐาน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ShiinaBR/status/2066961185652576583" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HYPEX</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2793 · 💬 62</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HYPEX/status/2066962076480786639">View @HYPEX on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“SIMPSONS x UEFN MIGHT GET ANNOUNCED TOMORROW Unreal Engine posted a teaser for Unreal Fest (tomorrow), and it featured Homer Simpson https://t.co/Pxri6JN5Z3”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Leaker @HYPEX คาดเดาว่า Simpsons จะ collab กับ UEFN โดยอิงจาก teaser รูป Homer Simpson ที่ Unreal Engine โพสต์ก่อน Unreal Fest เท่านั้น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HYPEX/status/2066962076480786639" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Riju1T_T</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2234 · 💬 88</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Riju1T_T/status/2066929143527428184">View @Riju1T_T on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Wuwa 3.5 beta info// NOT A LEAK- THIS IS JUST SPECULATIONS As you may have noticed, the visuals in the 3.5 beta are a lot better than before because Kuro keeps backporting UE5 to WuWa. And this time i”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนเกม Wuthering Waves ตั้งทฤษฎีว่า Kuro Games backport UE5 เข้าตัวเกมสด และอาจใช้ฟีเจอร์ UE 5.8 ที่ยังไม่ official ใน beta 3.5 — เป็นแค่ speculation ไม่ใช่ leak</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Riju1T_T/status/2066929143527428184" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MortalCrux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1385 · 💬 30</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MortalCrux/status/2066545937963434286">View @MortalCrux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Based on feedback from the inventory physics update, additional gear and clothing items like the knife on the sorceress's thigh are now responsive to movement and mouse clicks. #indiegamedev #indiegam”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev @MortalCrux ขยาย physics system ใน Unity RPG ของตัวเอง ให้ gear และ clothing items (เช่น มีดที่ต้นขา) ตอบสนองต่อ movement และ mouse input หลังได้ feedback จาก inventory physics update ก่อนหน้า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป็นตัวอย่าง pattern ที่ดี: ship physics layer สำหรับ core items ก่อน รับ feedback แล้วค่อย extend ระบบเดิมไปยัง secondary props — ควบคุม scope ได้ดีขณะที่ polish ดีขึ้นเรื่อยๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง apply แนวทางนี้: ใส่ cloth/rigidbody physics ให้ hero props ก่อน ship แล้วรับ feedback ค่อย roll out ไปยัง secondary equipment ทีหลัง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MortalCrux/status/2066545937963434286" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Stealth40k</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1283 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Stealth40k/status/2067250232912482784">View @Stealth40k on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Unreal Engine 5.8 Lumen Light functionality is compatible with Switch 2. Preserves visual impact at a lower GPU cost, making Lumen functionality viable were it wasn't before. Announced at State of Unr”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>UE 5.8 รองรับ Lumen dynamic GI บน Nintendo Switch 2 แล้ว ประกาศที่ State of Unreal 2026 — GPU cost ต่ำพอให้ใช้งานได้จริงบน hardware นี้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เกม UE5 บน Switch 2 ใช้ Lumen GI แบบ real-time ได้เลย ไม่ต้อง bake lighting — visual ceiling สูงขึ้นชัดเจน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าสตูดิโอจะทำเกม UE5 บน Switch 2 ให้นับ Lumen เป็น feature ที่พร้อมใช้ได้เลยตอน scope platform</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Stealth40k/status/2067250232912482784" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@boxhead20277086</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1222 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/boxhead20277086/status/2066944593908953260">View @boxhead20277086 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Guys... I think Sonic found something in the hills #indiedev #robloxstudio #RobloxDev #SonicTheHedgehog #SonicExpedition #thebackrooms https://t.co/QkDd571cS2”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev แชร์ teaser ของ fan-made Sonic horror/exploration game ใน Roblox Studio สไตล์ Backrooms</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/boxhead20277086/status/2066944593908953260" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@wuwaguy</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1188 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/wuwaguy/status/2066933181614567832">View @wuwaguy on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“From the release of Septimont and V2.4, we're getting insane quality stuffs whether it's a character animation or the overworld map design... &amp; it's probably not something that you haven't noticed yet”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Kuro Games backport feature ของ UE5 รวมถึง UE5.8 ที่ยังไม่ release อย่างเป็นทางการ เข้าไปใน Wuthering Waves ที่สร้างบน UE4 ได้คุณภาพกราฟิกดีขึ้นโดยไม่ต้อง migrate engine ทั้งก้อน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การ backport render feature ทีละส่วนเป็นทางเลือกที่ใช้ได้จริงแทนการ migrate engine ทั้งก้อน ตรงกับสถานการณ์ที่ studio ต้องตัดสินใจเรื่อง URP/HDRP บน Unity project ที่ deploy อยู่แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">เมื่อ Unity team ต้องอัปเกรด render pipeline ให้ประเมินการ backport SRP feature ทีละ module แทนการสลับ pipeline ทั้งก้อนในครั้งเดียว</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/wuwaguy/status/2066933181614567832" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1108 · 💬 241</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2066686216779509850">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here's a look at how Epic's artists approach concept work. From blank canvas to final concepts, they sketch, block out, and refine using traditional tools and evolving ones like Nano Banana, with the ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีม artist ของ Epic โชว์ขั้นตอน concept art ตั้งแต่ sketch → block-out → refine โดยใช้ traditional tools ควบคู่กับ tool ภายในชื่อ Nano Banana โดยมี vision ของ artist เป็นตัวนำ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Structure concept pipeline ของ AAA studio (sketch → final) ใช้เป็น reference ในการวาง pre-production workflow สำหรับโปรเจกต์ game และ XR ของ studio ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม game และ XR ใช้ structure sketch-block-refine นี้เป็น template สำหรับ pre-production concept phase ของ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2066686216779509850" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
