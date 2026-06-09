---
type: social-topic-report
date: '2026-06-09'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-09T03:12:43+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 155
salience: 0.55
sentiment: mixed
confidence: 0.6
tags:
- game-dev
- godot
- unreal-engine-5
- unity
- xbox
- ai-asset-generation
thumbnail: https://pbs.twimg.com/media/HKTU_iEXIAA3eG1.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-09

## TL;DR
- Godot 4.7 ถึงขั้น Release Candidate พร้อม HDR output, official Godot Asset Store, และ drawable textures [17]; Microsoft ออกคู่มือ 'Building Xbox Games with Godot' พร้อม GDExtensions สำหรับ GDK, PlayFab, และ GameInput [32]
- Unreal Engine 5 ได้ทั้งกระแสบวก — Gears of War: E-Day ได้รับคำชมด้านภาพและ fidelity [4][12][53], Mortal Shell 2 บน UE5 [27] — และกระแสวิจารณ์ที่เห็นได้ชัดเรื่อง art direction ซ้ำซาก, กรอบ 'slop', และ optimization ที่ย่ำแย่จากการพึ่ง UE5/DLSS [5][6][39][43]
- TT Games มีรายงานว่ากำลังพัฒนาเกมใหม่บน IP ใหญ่ของ Warner Bros. (คาดว่าเป็น DC) บน UE5 [1] — เป็นข่าวลือ ไม่ใช่ประกาศทางการ
- Unity tooling ฟรี/ราคาต่ำโผล่หลายชิ้น: AERO 1.4 volumetric fog สำหรับ URP ฟรีบน Asset Store [22] พร้อม shader/editor-tool bundles [25][46]
- AI image generation (GPT Image 2) ถูกนำมาใช้สร้างภาพสไตล์ marketing/editorial ในโพสต์แวดวง gamedev [37][60]

## สิ่งที่เกิดขึ้น
ข่าว engine แบ่งเป็นสามทาง Godot ถึงขั้น production-ready 4.7 RC พร้อม HDR output, official Asset Store, และ drawable textures [17], และ Microsoft ออก guidance พร้อม GDExtensions (GDK, PlayFab, GameInput) สำหรับสร้างเกม Xbox-on-PC ด้วย Godot [32] Unreal Engine 5 ครองพื้นที่ด้วยปริมาณ: Gears of War: E-Day ได้รับคำชมด้านภาพอย่างแรงก่อนจะมี session จาก The Coalition ที่ Unreal Fest Chicago [4][12][53], Mortal Shell 2 ถูกยกเป็นตัวอย่างก้าวกระโดดของ UE5 [27], และ TT Games มีข่าวลือว่ากำลังทำเกม Warner Bros. IP บน UE5 [1] ในทางกลับกัน กระแสวิจารณ์ที่วนซ้ำชี้ว่า UE5 สร้าง art direction ที่เหมือนกันหมดและ optimization แย่ลง โดยโทษการพึ่ง DLSS เป็นส่วนหนึ่ง [5][6][39][43][48] Carmack ออกมาชื่นชม Fabrice Bellard ต่อสาธารณะ [2]

## ทำไมถึงสำคัญ
สัญญาณของ Godot สำคัญที่สุดสำหรับ studio ที่ใช้หลาย stack Official Asset Store [17] บวกกับ Xbox export tooling ที่ Microsoft หนุนหลัง [32] ลดอุปสรรคสองอย่างที่มีมานาน ได้แก่ การกระจาย asset และการเข้าถึง console ซึ่งเดิมผลักให้ทีมหันไปใช้ Unity หรือ Unreal แม้จะยังไม่แทนที่ Unity ได้ แต่ทำให้ Godot เป็นตัวเลือกที่ defend ได้มากขึ้นสำหรับเกม 2D/3D ขนาดเล็กและ edutech กระแสวิจารณ์ UE5 [5][6][39][43] ส่วนใหญ่เป็น discourse ไม่ใช่ข้อมูล แต่ปัญหา optimization เป็น second-order effect ที่จริง: การพึ่ง upscaler (DLSS) และค่า Lumen/Nanite default มากเกินไปสัมพันธ์กับปัญหา performance ของเกมที่ ship แล้ว ซึ่งส่งผลต่อ XR/VR และ mobile ที่ frame budget ตึง Unity tooling [22][25][46] และการใช้ AI image [37][60] สะท้อนการ commoditize asset การผลิตระดับกลางที่ต่อเนื่อง — มีประโยชน์ด้านต้นทุน แต่เป็นกลางต่อความแตกต่าง

## ความเป็นไปได้
**น่าจะเกิด:** เรื่องราว console reach ของ Godot พัฒนาต่อเนื่อง เพราะ Microsoft ออก tooling อย่างแข็งขัน [32] ควบคู่ก้าวกระโดดของ 4.7 [17] คาดว่า GDExtensions จากบุคคลที่สามจะตามมาอีก **เป็นไปได้:** เกม TT Games/Warner Bros UE5 มีจริง แต่รายละเอียด 'DC' ยังไม่ยืนยันจนกว่าจะมีประกาศทางการ [1] **ไม่น่าเกิด:** การใช้ UE5 ชะลอลงอย่างมีนัยสำคัญจากคำวิจารณ์เรื่อง 'slop'/optimization [5][6][39] — pipeline ระดับ AAA ที่ผูกพันแล้วอย่าง Gears E-Day [4][53] และ Mortal Shell 2 [27] แสดงว่า install base ยังแน่น **เป็นไปได้:** AI image tools อย่าง GPT Image 2 [37][60] ขยายเข้าสู่ workflow concept/marketing เร็วกว่า in-game asset จริง เพราะ consistency และ licensing ยังเป็นอุปสรรค

## การนำไปใช้ใน NDF DEV
1) ติดตาม Godot 4.7 RC และ Microsoft Xbox/Godot tooling สำหรับ prototype ที่ไม่ใช่ Unity และ edutech ที่ต้องการ console export หรือ engine เบากว่า — ลงทุนน้อยในการประเมิน [17][32] 2) ดาวน์โหลด AERO 1.4 free URP volumetric fog ทันทีสำหรับงาน Unity/XR ปัจจุบัน — ลงทุนน้อย คุ้มทันที [22] 3) ใช้คำวิจารณ์ UE5 optimization เป็น checklist input ไม่ใช่คำตัดสิน: หากโปรเจกต์ใดใช้ UE5 ให้วางงบสำหรับ performance ที่ไม่พึ่ง upscaler และทบทวนค่า Lumen/Nanite default — ลงทุนปานกลาง [39][43] 4) ทดลองใช้ GPT Image 2 สำหรับภาพ marketing/store-page และ concept art (ไม่ใช่ in-game asset) — ลงทุนน้อย [37][60] ข้ามได้: กระแสวัฒนธรรม Gears/UE5 [4][12][14], โพสต์ indie showcase ที่ไม่มี technique นำกลับมาใช้ [8][9][16][21][33][36][42], และข่าวลือ TT Games จนกว่าจะยืนยัน [1]

## สัญญาณที่ควรจับตา
- Godot 4.7 final release และการใช้งาน official Asset Store — วัดว่า tooling gap ของ Godot เทียบ Unity ใกล้ชิดแค่ไหน [17]
- การสนับสนุน Godot/Xbox GDExtension ต่อเนื่องของ Microsoft — proxy วัด console viability ของ Godot [32]
- ประกาศทางการของ TT Games / Warner Bros เพื่อยืนยันหรือล้มข่าวลือ UE5 DC [1]
- คำวิจารณ์ UE5 optimization จะเปลี่ยนจาก discourse ไปสู่รูปแบบ shipped-performance ที่วัดได้หรือไม่ [39][43]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | LEGOTtNewsI | ^6419 c236 | [TT Games' Next Title will be based on a Major Warner Bros. IP on Unreal Engine 5](https://x.com/LEGOTtNewsI/status/2064008728047727003) |
| x | ID_AA_Carmack | ^3639 c69 | [I admire Fabrice Bellard. He is almost certainly a better overall programmer tha](https://x.com/ID_AA_Carmack/status/2064095424420487226) |
| x | MortalCrux | ^2313 c83 | [I might not have a new trailer for any gaming showcases today, but here are a fe](https://x.com/MortalCrux/status/2063710959793750424) |
| x | Grummz | ^969 c146 | [Gears of War E-Day was the best of the show. - A return to masculinity and broth](https://x.com/Grummz/status/2063846556806328380) |
| x | LookAtMyMeat1 | ^944 c4 | [The Unreal engine has been a disaster for art direction in gaming](https://x.com/LookAtMyMeat1/status/2064026736732393492) |
| x | NomadicAllo | ^921 c23 | ["UE5 looks like slop" Nuh uh https://t.co/awY78D0H1a](https://x.com/NomadicAllo/status/2063834614339178757) |
| x | LucasLiu_XY | ^765 c9 | [Finally got my character running in-game using UE5's GASP project! The feeling o](https://x.com/LucasLiu_XY/status/2063821404978712691) |
| x | ABGameDeveloper | ^499 c6 | [The Fox caught you and he wants to num num... 🦊🔪 (It's an old model 🤭) #furry #h](https://x.com/ABGameDeveloper/status/2063808353575534745) |
| x | zzeljkokos | ^467 c33 | [Surprise! 😊 After years spent building cities, it's time to return to the stars.](https://x.com/zzeljkokos/status/2064053479748903312) |
| x | Look_behindyou | ^458 c5 | [🚨 Only 70 hours left! The final countdown for Soverain has begun! If you've been](https://x.com/Look_behindyou/status/2063996243450233026) |
| x | ShatterPointGS | ^419 c6 | [A little bit of testing with one of Sylphie's mechanics. #indiegame #indiedev #f](https://x.com/ShatterPointGS/status/2064059889064853554) |
| x | JamieMoranUK | ^405 c20 | [I've played 1000s of Video Games , since I was old enough to pick up a Controlle](https://x.com/JamieMoranUK/status/2063835937931452727) |
| x | SharkyLeo_YT | ^384 c4 | [this is slander not seen since the fucking unreal engine Mario video](https://x.com/SharkyLeo_YT/status/2064109001281847521) |
| x | VladTheInflator | ^379 c15 | [If I wanted to destroy a country, I would: 1. Change their founding history to p](https://x.com/VladTheInflator/status/2063666428444868795) |
| x | rafaelborven | ^362 c4 | [Animation done for @TributeGames's game @MARVELCosmicInv #Pixelart #animation #i](https://x.com/rafaelborven/status/2063995185491493316) |
| x | Talegamesnews | ^301 c3 | [Eyes glowed. Chains clanked. Ghosts howled. She said "Cute" 👻⚔️😏 #metroidvania #](https://x.com/Talegamesnews/status/2063940098828169255) |
| x | godotengine | ^299 c10 | [#GodotEngine 4.7 has at last arrived at the Release Candidate stage! HDR output ](https://x.com/godotengine/status/2064079841985470893) |
| x | Hoodie_monk | ^261 c15 | [Version 1.0 Community: We need to talk. #HoodieMonk #GameDev #IndieDev #Gaming #](https://x.com/Hoodie_monk/status/2063946101401481265) |
| x | OzgursAssets | ^258 c6 | [FREE 🎁 Sharing these two cars I modeled almost 20 years ago for free. You can gr](https://x.com/OzgursAssets/status/2063900380547649761) |
| x | smokingcatsdev | ^257 c8 | [Day 15 of posting about my game, until a release a Steam Demo I've been wanting ](https://x.com/smokingcatsdev/status/2064107001949676030) |
| x | drattzy | ^237 c3 | [Alterium Shift is a retro-inspired JRPG where three heroes set out to prevent a ](https://x.com/drattzy/status/2063999695375016326) |
| x | TheMirzaBeig | ^198 c4 | [Just released! ✅ Dense, self-shadowing, volumetric fog. Need lit, volumetric fog](https://x.com/TheMirzaBeig/status/2063938424109715502) |
| x | OzgursAssets | ^197 c4 | [Kei Truck - WIP 9 Modeling is done, now it's UV time! #keitruck #gamedev #indied](https://x.com/OzgursAssets/status/2063583946303000701) |
| x | blargisdev | ^197 c5 | [Implemented this swingy lantern that projects cool shadows #gamedev #indiedev ht](https://x.com/blargisdev/status/2064088764641947758) |
| x | ushadersbible | ^182 c0 | [The Unity Dev Bundle ➡️ https://t.co/1eA8907m5M #gamedev https://t.co/aEAZAQ6jVV](https://x.com/ushadersbible/status/2063481988208533947) |
| x | unity3dvfx | ^182 c2 | [Really cool to see indie FPS devs sharing progress like this 🙌 The responsivenes](https://x.com/unity3dvfx/status/2063878484905058742) |
| x | BMKing23 | ^181 c8 | [I'm genuinely surprised by #MortalShell2. It's a massive leap over the original ](https://x.com/BMKing23/status/2064053901796479115) |
| x | HedProtag | ^176 c6 | [Working on a cool new feature for my game. Can you guess what it is? #indiegame ](https://x.com/HedProtag/status/2064159133826191719) |
| x | GinoKolling | ^174 c0 | [Unreal Engine Creatures https://t.co/3AkERddbH6](https://x.com/GinoKolling/status/2063918745295393199) |
| x | GameZoneHQ | ^165 c0 | [Procedurally generated impact frame with shader and particle system by @namutree](https://x.com/GameZoneHQ/status/2063878287865028798) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LEGOTtNewsI</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6419 · 💬 236</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LEGOTtNewsI/status/2064008728047727003">View @LEGOTtNewsI on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“TT Games’ Next Title will be based on a Major Warner Bros. IP on Unreal Engine 5 We believe it will be DC https://t.co/0eLnlz5nY5”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>TT Games (ผู้พัฒนา LEGO series) กำลังสร้างเกมใหม่บน Unreal Engine 5 โดยใช้ IP ใหญ่ของ Warner Bros. — คาดว่าเป็น DC Comics</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>TT Games ย้ายจาก custom engine มา UE5 บ่งชี้ว่า studio ขนาดกลางที่ทำ licensed IP กำลัง standardize บน UE5 สำหรับ production รุ่นถัดไป</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า studio วางแผนทำ licensed หรือ XR title บน UE5 — ข่าวนี้ยืนยันว่า UE5 คือ long-term bet ที่ปลอดภัยกว่า Unity สำหรับ scope นั้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LEGOTtNewsI/status/2064008728047727003" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3639 · 💬 69</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2064095424420487226">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I admire Fabrice Bellard. He is almost certainly a better overall programmer than I am.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>John Carmack ยกย่อง Fabrice Bellard (ผู้สร้าง QEMU, FFmpeg, TinyCC) ว่าน่าจะเก่งกว่าตัวเองในแง่ programmer โดยรวม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ID_AA_Carmack/status/2064095424420487226" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@MortalCrux</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2313 · 💬 83</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/MortalCrux/status/2063710959793750424">View @MortalCrux on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I might not have a new trailer for any gaming showcases today, but here are a few updates to how menus work. 😂 1) Character physics are now simulated and respond to mouse input while previewing your g”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา indie RPG ใน Unity เปิด physics ตัวละครและ real-time lighting จากคบไฟในหน้า menu — ก่อนหน้านี้ทำได้แค่ใน gameplay scene</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เปิด physics กับ real-time lighting ใน menu ได้เลยโดยไม่ต้องสร้าง system ใหม่ เพราะ Unity project มีอยู่แล้ว — polish ที่ได้คุ้มมาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ลอง reuse physics rig กับ lighting ที่มีอยู่ใน character preview หรือ equipment screen แทนการ bake static model สำหรับ menu</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/MortalCrux/status/2063710959793750424" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Grummz</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 969 · 💬 146</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Grummz/status/2063846556806328380">View @Grummz on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Gears of War E-Day was the best of the show. - A return to masculinity and brotherhood themes - Unreal Engine 5 and looks great - Interview said the were focused on the vibes of the original game, ins”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Gears of War E-Day บน UE5 เปิดตัว micro cover-destruction system, ระบบ movement/cover ใหม่รองรับ jump, gore system ใหม่ และ city environment ที่สร้างขึ้นทั้งหมดเพื่อเกมนี้โดยเฉพาะ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Micro-destruction และ cover/movement system ใหม่เป็น design reference ที่จับต้องได้สำหรับเกม third-person หรือ combat — ดูว่า AAA team scope environmental interactivity ยังไง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตอน Unity team ออกแบบ combat หรือ cover mechanics ให้ใช้ E-Day เป็น benchmark เปรียบ interaction depth กับ performance cost</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Grummz/status/2063846556806328380" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LookAtMyMeat1</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 944 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LookAtMyMeat1/status/2064026736732393492">View @LookAtMyMeat1 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Unreal engine has been a disaster for art direction in gaming”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X รายหนึ่งโพสต์ความเห็นว่า Unreal Engine ทำให้ art direction ในวงการเกมแย่ลง โดยไม่มีหลักฐานหรือตัวอย่างประกอบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LookAtMyMeat1/status/2064026736732393492" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@NomadicAllo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 921 · 💬 23</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/NomadicAllo/status/2063834614339178757">View @NomadicAllo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“&quot;UE5 looks like slop&quot; Nuh uh https://t.co/awY78D0H1a”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>User @NomadicAllo แชร์ลิงก์มีเดียโต้กลับความเห็นว่า UE5 ดูธรรมดา โดยไม่มีข้อมูล project, technique หรือ settings ใดเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/NomadicAllo/status/2063834614339178757" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@LucasLiu_XY</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 765 · 💬 9</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/LucasLiu_XY/status/2063821404978712691">View @LucasLiu_XY on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Finally got my character running in-game using UE5's GASP project! The feeling of seeing your own design move is indescribable.Who understands this feeling? 🎉 https://t.co/01R5YL6d2U”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาคนหนึ่งแชร์ความสำเร็จในการรัน character animation ใน UE5 ผ่าน GASP (Game Animation Sample Project) เป็นครั้งแรก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/LucasLiu_XY/status/2063821404978712691" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ABGameDeveloper</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 499 · 💬 6</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ABGameDeveloper/status/2063808353575534745">View @ABGameDeveloper on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The Fox caught you and he wants to num num... 🦊🔪 (It's an old model 🤭) #furry #horrorgame #indiedev #gamedev https://t.co/fhuN56oP95”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev @ABGameDeveloper โชว์ clip horror game ตัวละคร fox ที่กำลังพัฒนา โดยบอกว่า model เป็นเวอร์ชันเก่า</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ABGameDeveloper/status/2063808353575534745" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
