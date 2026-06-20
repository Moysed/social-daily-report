---
type: social-topic-report
date: '2026-06-20'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-20T15:14:26+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 164
salience: 0.62
sentiment: mixed
confidence: 0.6
tags:
- unreal-engine
- ue6
- ai-pipeline
- unity
- godot
- engine-strategy
thumbnail: https://pbs.twimg.com/media/HLOsAYdaIAAWohf.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-20

## TL;DR
- Epic ยืนยัน Unreal Engine 6 ตั้งเป้า Early Access ปลายปี 2027; Blueprints ยังรองรับใน EA และ release แรก แต่กำหนดยกเลิกในภายหลัง — ชุมชนตอบรับเชิงลบ [2][52]
- ผู้กำกับ FF7 Revelation นาโอกิ ฮามากูชิ ยืนยันเกมยังอยู่บน Unreal Engine 4 (ไม่ใช่ UE5) เพื่อส่งงานได้เร็วขึ้น มองว่าเป็นการตัดสินใจด้านธุรกิจและตาราง — 'เทคโนโลยีคือวิธีการ ไม่ใช่เป้าหมาย' [1][3][7]
- UE 5.8 เปิด Microsoft GDK plug-ins สู่สาธารณะ ทีมงานสามารถ build, package และ ship เกม Xbox จาก PC ได้โดยไม่ต้องเปลี่ยน workflow [5]
- ภาพจริงของ AI ในสาย pipeline: dev ที่ recreate demo 'build a city' ของ Unreal ชี้ว่า AI ที่ ship จริงไม่ตรงกับ demo และ 'ยุ่งเหยิง' — งานทำมือเร็วกว่า [36] ขณะที่อีกคนใช้ AI-agent loop ค่อยๆ สร้างแผนที่สไตล์ GTA ใน 10 วัน [8]
- เครื่องมือ Unity/Godot ที่น่าสนใจ — GPU wireframe shader แบบ topology จริง [49], TUI renderer บน ratatui สำหรับ Unity [29] และการทดสอบ Claude Code กับ UE 5.8 MCP plugin สำหรับ Blueprint generation [23]

## What happened
กลยุทธ์ engine ครองพื้นที่วันนี้ Epic ระบุ UE6 ตั้งเป้า Early Access ปลายปี 2027 โดย Blueprints ยังรองรับใน EA และ release แรก แต่จะยกเลิกในภายหลัง [2] กระแสตอบรับเป็นลบอย่างกว้างขวาง โดยมีโพสต์หนึ่งที่แชร์กันมากชี้ให้เห็นว่า timeline 3 ปีนับจากนี้ และการเลิกใช้ Blueprint ราวๆ 5 ปี ยังไม่ต้องตื่นตระหนก [52] ฝั่ง FF7 Revelation ผู้กำกับ Naoki Hamaguchi อธิบายว่าเกมอยู่บน UE4 ต่อไป ไม่ย้ายไป UE5 เพราะเหตุผลด้านตารางเวลา ธุรกิจ และความต่อเนื่องจาก Remake/Rebirth [1][3][7][53] Epic ยืนยันด้วยว่า Launcher V2 ไม่ได้สร้างบน Unreal Engine [6][60] และ Unreal Fest Chicago / State of Unreal ปิดฉากพร้อม highlights [27][32] ด้าน tooling UE 5.8 เปิด Microsoft GDK plug-ins สาธารณะสำหรับ Xbox build จาก PC [5]

## Why it matters (reasoning)
สัญญาณยกเลิก Blueprint ใน UE6 [2] คือประเด็นที่มีผลกระทบมากสุด: visual scripting คือเครื่องมือหลักที่ทีมเล็กและกลุ่ม non-programmer ใช้สร้างงานใน Unreal ดังนั้น deprecation path หลายปีสร้างความเสี่ยงในการวางแผน และผลักบางทีมไปหา Godot (สังเกตกระแส 'reimplement visual scripting เพื่อต่อต้าน Epic' [46]) การตัดสินใจของ FF7 [1][3] เป็นบทเรียนสวนกระแสสำหรับสตูดิโอที่ถูกกดดันให้ไล่ตาม engine ใหม่ล่าสุด — สตูดิโอใหญ่เลือก schedule และความคุ้นเคยเหนือ version ล่าสุดอย่างชัดเจน ประเด็น AI pipeline อยู่ทั้งสองด้าน — demo ของ vendor สำหรับ AI level/asset generation วิ่งนำหน้าความเป็นจริงที่ ship ได้ [36][8] ขณะที่ AI tooling ที่ขอบเขตชัดและแคบกว่า (MetaHuman modular characters [17], bulk asset import [38], MCP-driven scripting [23]) แสดงให้เห็นว่า AI ช่วยงาน production ได้จริงในจุดใด GDK plug-in ของ Xbox [5] ลด friction การ ship console ซึ่งเกี่ยวข้องกับทีมที่มองตลาด console port

## Possibility
**Likely:** การยกเลิก Blueprint ใน UE6 ผลักดันความสนใจ Godot และทางเลือก visual-scripting ใน 1-2 ปีข้างหน้า จากกระแสต่อต้านและ timeline ที่ชัด [2][46][52] **Plausible:** สตูดิโออื่นจะออกมาพูดถึงการอยู่กับ engine เวอร์ชันเก่าเพื่อรักษา ship date เช่นเดียวกับที่ FF7 ทำ [1][3] **Plausible:** ฟีเจอร์ AI 'auto-generate a level/city' ยังคง over-promise ใน demo และ under-deliver ใน shipped build ระยะใกล้ ขณะที่ AI tool แบบแคบ (character parts, asset import, scripting assist) จะ mature เร็วกว่า [36][8][17][38][23] **Unlikely (ไม่มี source รองรับ):** การบังคับ migrate ออกจาก Blueprints ในระยะใกล้ — Epic ระบุชัดว่า deprecation จะเกิดหลัง EA ปี 2027 [2][52]

## Org applicability — NDF DEV
1) ปฏิบัติต่อ AI level/asset auto-generation แบบ experimental ไม่ใช่ production: ช่องว่าง demo-vs-reality [36][8] บอกว่าไม่ควรพึ่งพาใน Unity/XR pipeline ตอนนี้ (low effort — กำหนดความคาดหวัง, ข้ามสำหรับงาน ship จริง) 2) ทดลอง MCP-driven engine scripting: การทดสอบ Claude Code + UE 5.8 MCP [23] ตรงกับ UnityMCP ของ NDF — รัน trial แคบๆ บน Unity editor automation ก่อนพึ่งพาจริง (med effort) 3) นำบทเรียน engine-version จาก FF7 [1][3] มาใช้: สำหรับโปรเจกต์ Unity edutech/XR ให้ยึด stable LTS และหลีกเลี่ยง major upgrade กลางโปรเจกต์เพราะความอยากได้ใหม่ (low effort — policy note) 4) ประเมิน Unity asset ราคาถูกที่ออกวันนี้: GPU wireframe shader [49], free VFX texture pack [42] และ ratatui-unity TUI renderer สำหรับ in-game terminal UI [29] (low effort) ข้าม: ความกังวล UE6 timeline [2][52] และ internals ของ Epic Launcher [6] — ไม่เกี่ยวกับสตูดิโอที่ใช้ Unity เป็นหลัก

## Signals to Watch
- Epic จะเผยแพร่ Blueprint migration/replacement path ที่ชัดเจนก่อน UE6 EA หรือไม่ — ส่งผลต่อทุกทีมที่พึ่ง visual scripting [2][52]
- ความ mature ของ MCP plugin สำหรับ engine (Unity/Unreal) ในการช่วย scripting ด้วย AI — เกี่ยวโดยตรงกับ UnityMCP ของ NDF [23]
- ผลลัพธ์จริงที่ ship ได้จาก AI level/asset generation เทียบกับ marketing demo [36][8][38]
- Varsapura ของ miHoYo ในฐานะ UE5 title ใหญ่ตัวแรก — สัญญาณการ adopt engine ของสตูดิโอ AAA [54]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | nhamaguc | ^6935 c141 | [I spoke about why we chose Unreal Engine 4 over 5. Technology is a means, not th](https://x.com/nhamaguc/status/2068127708543078789) |
| x | UnrealEngine | ^1800 c571 | [Hey Everyone. Our aim is to ship Early Access for UE6 by the end of 2027 and Blu](https://x.com/UnrealEngine/status/2067661808903577646) |
| x | Genki_JPN | ^1261 c41 | [Naoki Hamaguchi says they stuck with Unreal Engine 4 instead of switching to UE5](https://x.com/Genki_JPN/status/2068185785254453474) |
| x | EyesOfTheGhost | ^1038 c2 | [this but with godot in the thumbnail and instead of adding flavour shots its lik](https://x.com/EyesOfTheGhost/status/2067990637253722136) |
| x | XBOXGameDev | ^865 c15 | [Unreal Engine 5.8 just made building for Xbox even easier. Microsoft GDK plug-in](https://x.com/XBOXGameDev/status/2068058675689001089) |
| x | BackersGamesF | ^698 c25 | [EPIC CONFIRMED THAT THE LAUNCHER V2 IS NOT BUILD ON UNREAL ENGINE 👀 Someone aske](https://x.com/BackersGamesF/status/2068022135155491316) |
| x | NinEverything | ^570 c12 | [Final Fantasy 7 Revelation director explains why the game is sticking with Unrea](https://x.com/NinEverything/status/2068095743471362215) |
| x | ziwenxu_ | ^443 c68 | [10 days ago this was an empty map. A loop of AI agents has been building GTA 6 o](https://x.com/ziwenxu_/status/2068090138232586327) |
| x | TonemanLives | ^429 c98 | [Democrats have no ideas, no agenda, offer no hope to the American people and def](https://x.com/TonemanLives/status/2067918494306291966) |
| x | AdamNapper2 | ^397 c6 | [Silent Hill 2 inspired Alpha Clipping Vertex Painting :) #Unity #Gamedev https:/](https://x.com/AdamNapper2/status/2068253644693361109) |
| x | Mr_Rebs_ | ^375 c18 | [Just a reminder: I reported Campaign Evolved is an unreal engine training exerci](https://x.com/Mr_Rebs_/status/2068078291660013782) |
| x | WOAH_MAAAN_DEV | ^362 c4 | [Punch her belly! #gamedev #indiedev #ScreenshotSaturday https://t.co/4QKUfDg5cf](https://x.com/WOAH_MAAAN_DEV/status/2068328315815969009) |
| x | ushadersbible | ^349 c0 | [Included in the Godot Shaders Bible as well ➡️ https://t.co/1kYkAqSE2L #GodotEng](https://x.com/ushadersbible/status/2068184144819982688) |
| x | owensmowen_ | ^303 c12 | [Over here in dev texture land, working on some new firing animations 🤠 #UE5 #ind](https://x.com/owensmowen_/status/2068037844539752577) |
| x | ProfHall1955 | ^241 c13 | [😂 'top economists' aka neoliberal bankers and a bureaucrat. Western politicians ](https://x.com/ProfHall1955/status/2068060149802029523) |
| x | skx_doom | ^222 c5 | [Rain Effects test from Sky Creator 2.0 (heavy in development) - all dynamic obje](https://x.com/skx_doom/status/2068250397006090614) |
| x | assethub_io | ^211 c2 | [New 3D AI + MetaHuman Workflow for a Modular Game Character Running in-game in U](https://x.com/assethub_io/status/2068012076673769711) |
| x | jettelly | ^202 c1 | [Artificeofbees showed some material tests using iterative parallax mapping on a ](https://x.com/jettelly/status/2068031054724608236) |
| x | oopsallsolace | ^197 c17 | [Not sure, but is it supposed to do that while i'm aiming? 👀 #LegionofHonorGame #](https://x.com/oopsallsolace/status/2068092103951868214) |
| x | gruntdotapi | ^196 c6 | [Technically speaking, the game does seem to support some kind of flying camera /](https://x.com/gruntdotapi/status/2068275818942386468) |
| x | SaveChan_Dev | ^187 c2 | ["Data shows Ret Paladins only get hit on the shoulders. That's why the armor des](https://x.com/SaveChan_Dev/status/2068245511501738232) |
| x | lonve69686 | ^187 c4 | [Gentleman's Violence - John Wick-inspired Gun-fu FPS #indiedev #gamedev #indiega](https://x.com/lonve69686/status/2068001554276504031) |
| x | smart_poly | ^182 c9 | [I tested Claude code + Unreal Engine 5.8 MCP plugin. I conducted 5 tests where I](https://x.com/smart_poly/status/2068071720246816855) |
| x | itchio | ^174 c1 | [When The Snow is Gone: Do you remember the snow? https://t.co/LaqeVzWNVS by @gum](https://x.com/itchio/status/2068015959370289435) |
| x | aeternathegame | ^166 c15 | [This is #AeternaLucis and we've taken its gameplay to a whole new level. Fast-pa](https://x.com/aeternathegame/status/2068047489597317299) |
| x | Willibab89 | ^164 c3 | [Early night for me. Here is some WIP on classes. #nes #rpg #wip #gamedev #indied](https://x.com/Willibab89/status/2068083358794407944) |
| x | UnrealEngine | ^154 c7 | [Thank you to everyone for coming along to Unreal Fest Chicago and to those who j](https://x.com/UnrealEngine/status/2067971700986372465) |
| x | JamieMoranUK | ^150 c2 | [Gears Of War E-Day looks like it's going to be the Gears game I've wanted for a ](https://x.com/JamieMoranUK/status/2068185017746894908) |
| x | orhundev | ^148 c2 | [Damn, what... I wasn't expecting to see this today 🤯 🌐 ratatui-unity — Brings th](https://x.com/orhundev/status/2068067713264779423) |
| x | being_becoming | ^133 c4 | [Corruption hits different in every realm. Don't let the serene beauty weaken you](https://x.com/being_becoming/status/2067974180264427643) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@nhamaguc</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6935 · 💬 141</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/nhamaguc/status/2068127708543078789">View @nhamaguc on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I spoke about why we chose Unreal Engine 4 over 5. Technology is a means, not the goal. In an environment where our team can perform at its highest level, we will deliver FFVII Revelation as the best ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ทีม FFVII Revelation เลือก Unreal Engine 4 แทน UE5 โดยให้เหตุผลว่าทีมถนัด UE4 มากกว่า และต้องการส่งมอบเกมได้เร็วกว่า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สตูดิโอใหญ่ยืนยันสาธารณะว่า 'ใช้สิ่งที่ทีมถนัด' สำคัญกว่าการอัปเกรด engine — เป็นการ validate แนวคิดนี้สำหรับทีมเล็กด้วย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อน commit engine version ใหม่ในโปรเจกต์ Unity หรือ UE ควร map skill gap ของทีมก่อนตัดสินใจ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/nhamaguc/status/2068127708543078789" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1800 · 💬 571</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2067661808903577646">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Hey Everyone. Our aim is to ship Early Access for UE6 by the end of 2027 and Blueprints will be supported in Early Access and the initial UE6 releases, but deprecated in the future. Deprecation will m”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Epic Games วางแผน UE6 Early Access ภายในปลายปี 2027 — Blueprints ยังใช้ได้ตอนเปิดตัว แต่อยู่ในเส้นทาง deprecation อย่างเป็นทางการ โดย Verse จะเป็น scripting system หลักในอนาคต</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่มีโปรเจกต์ UE Blueprints อยู่ตอนนี้รู้ชัดแล้วว่ามี end-of-life — มีเวลาประมาณ 18 เดือนเรียน Verse และวางแผน migrate ก่อน UE6 ออก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">มอบหมายคนในทีมหนึ่งคนไปศึกษา Verse fundamentals ตอนนี้ เพื่อให้ studio มีความรู้ภายในก่อนรับโปรเจกต์ UE6 จาก client</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2067661808903577646" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Genki_JPN</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1261 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Genki_JPN/status/2068185785254453474">View @Genki_JPN on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Naoki Hamaguchi says they stuck with Unreal Engine 4 instead of switching to UE5 for FF7 Revelation so that they could release the game a lot sooner! “But simply, for this series, considering a busine”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Naoki Hamaguchi ผู้กำกับ FF7 Rebirth เลือกอยู่กับ UE4 แทน UE5 เพราะ team สะสม customization ไว้มากแล้ว และการ migrate จะทำให้ release ช้าออกไปมาก — ถึงขั้นสร้าง rendering system ของตัวเองแทน Nanite</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Team AAA พิสูจน์ว่า customization ที่สะสมใน engine เก่านั้นมีมูลค่ามากกว่า feature ใหม่ใน engine ถัดไป — การ 'อยู่กับของเดิมและต่อยอด' ทำให้ release ได้เร็วกว่า migrate ใหม่ทั้งหมด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ก่อนตัดสินใจ upgrade Unity LTS กลาง project ควร audit custom editor tools และ runtime extensions ที่สะสมไว้ก่อน เพื่อชั่งน้ำหนักต้นทุนจริงของการ migrate กับประโยชน์ที่จะได้</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Genki_JPN/status/2068185785254453474" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@EyesOfTheGhost</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1038 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/EyesOfTheGhost/status/2067990637253722136">View @EyesOfTheGhost on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“this but with godot in the thumbnail and instead of adding flavour shots its like. a splash of milk. maybe 1 sugar”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ meme คลุมเครือ เปรียบ Godot กับการสั่งกาแฟแบบ minimal ไม่มีข้อมูลเชิงเทคนิค release หรือบทเรียนใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/EyesOfTheGhost/status/2067990637253722136" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@XBOXGameDev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 865 · 💬 15</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/XBOXGameDev/status/2068058675689001089">View @XBOXGameDev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Unreal Engine 5.8 just made building for Xbox even easier. Microsoft GDK plug-ins are now public—so you can build, package, and ship to Xbox on PC without changing your workflow. 👉 Get started: https:”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Microsoft เปิด GDK plug-ins สำหรับ Unreal Engine 5.8 เป็น public แล้ว — dev สามารถ build, package, และ ship เกมขึ้น Xbox จาก PC ได้โดยไม่ต้องเปลี่ยน workflow</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การ ship ขึ้น Xbox ง่ายขึ้นมากสำหรับ Unreal Engine studio — สะท้อนทิศทาง Microsoft ที่ดึง dev เข้า console ecosystem ตัวเอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/XBOXGameDev/status/2068058675689001089" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BackersGamesF</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 698 · 💬 25</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BackersGamesF/status/2068022135155491316">View @BackersGamesF on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“EPIC CONFIRMED THAT THE LAUNCHER V2 IS NOT BUILD ON UNREAL ENGINE 👀 Someone asked: &quot;..Epic Launcher v2 will not be built using Unreal engine? Is it true?&quot; Epic: &quot;Correct, not built on UE&quot; #EpicGames h”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Epic Games ยืนยันอย่างเป็นทางการว่า Launcher v2 ไม่ได้สร้างบน Unreal Engine ทลายความเชื่อที่ว่า Epic ใช้ UE กับ internal tool ทุกตัว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ยืนยันว่า UE ไม่เหมาะกับ desktop app development แม้แต่ในมือ Epic เอง — standard app framework ชนะในงานประเภทนี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BackersGamesF/status/2068022135155491316" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NinEverything</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 570 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NinEverything/status/2068095743471362215">View @NinEverything on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Final Fantasy 7 Revelation director explains why the game is sticking with Unreal Engine 4 instead of 5 https://t.co/ESmOlIe555 https://t.co/WJ2hjv1kHf”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้กำกับ Final Fantasy 7 Revelation อธิบายเหตุผลที่ทีมเลือกใช้ Unreal Engine 4 ต่อ แทนที่จะย้ายไป UE5</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เหตุผลจาก studio AAA ระดับใหญ่ที่เลือกอยู่กับ UE4 เป็น reference ดีสำหรับทีมที่กำลังตัดสินใจเรื่อง UE upgrade</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">อ่านบทความและบันทึก trade-off ที่ทีมอ้างถึง ไว้ใช้อ้างอิงตอน client ถามเรื่อง UE4 vs UE5</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NinEverything/status/2068095743471362215" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ziwenxu_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 443 · 💬 68</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ziwenxu_/status/2068090138232586327">View @ziwenxu_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“10 days ago this was an empty map. A loop of AI agents has been building GTA 6 on it and the community building it together while I sleep. day 10. look at it now. People are walking around. a skyline ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนารายหนึ่งใช้ AI agent loop สร้าง open-world สไตล์ GTA ใน Unreal Engine ภายใน 10 วัน — มี skyline, NPC เดินได้, และ community ช่วยกันสร้างด้วย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>AI agent loop ที่รันอัตโนมัติข้ามคืนลด production เวลา open-world map จากหลายเดือนเหลือไม่กี่วัน — เป็น benchmark ความเร็วที่จับต้องได้สำหรับทีมเล็ก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ของ studio ลอง AI agent loop สำหรับ procedural asset placement หรือ level generation ในโปรเจกต์ที่มีอยู่เพื่อดูคุณภาพ output จริง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ziwenxu_/status/2068090138232586327" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
