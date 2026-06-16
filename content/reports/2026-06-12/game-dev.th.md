---
type: social-topic-report
date: '2026-06-12'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-12T15:16:17+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 156
salience: 0.55
sentiment: mixed
confidence: 0.6
tags:
- unreal-engine-5
- godot
- unity
- ai-in-pipeline
- performance
- game-engines
thumbnail: https://pbs.twimg.com/media/HKi2wG4bYAENem6.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-12

## TL;DR
- Unreal Engine 5 ครองฟีดวันนี้: Halo: Campaign Evolved (UE5, วางจำหน่าย 28 ก.ค. 2026) [6], เกมแข่งรถ Clutch ที่ใช้ physics engine ของ UE5 แบบ custom [3][7], รีเมค Tomb Raider: Legacy of Atlantis [19], KH4 [25], และรายงาน job posting ของ Riot ที่ระบุว่า Teamfight Tactics จะย้ายมาใช้ Unreal [57][24]
- ปัญหา performance ของ UE5 ดังที่สุด: Halo: Campaign Evolved รายงานว่า RTX 5090 'แทบไม่ถึง 100 FPS ที่ 1440p ultra' [36] และนักพัฒนาวิจารณ์การ render ภายในที่ 540p แล้ว upscale เป็น '1080p' 60fps [11] — แม้ Series X Performance Mode จะล็อก 60fps ที่ 1080p ด้วย Lumen + hardware RT ได้ [47]
- Godot 4.7 Release Candidate 2 ออกแล้ว นิยามเป็นโอกาสสุดท้ายรับรายงาน regression ก่อน stable [17]; Godot ยังมี Xbox console sample พร้อม Q&A จากทีม [52] และฉากการ port จาก Roblox ไป Godot ที่คึกคัก [60]
- Generative AI ในไปป์ไลน์ยังเป็นที่ถกเถียง: ผู้กำกับรีเมค Tomb Raider พูดถึงการใช้ generative AI [34], มีคนสร้าง prototype ที่เล่นได้ด้วย AI agent ('GTA 6 agent in the loop' [10], เกม Pokémon×Clash Royale ใน '5 นาที' [56]), ขณะที่นักวิจารณ์โต้ว่า output จาก AI 'ดูถูก' หากไม่มีทักษะ art/design จริง [37]
- สัญญาณ Unity tooling: Real Fake Interiors เครื่องมือ baking + shader ใน Unity ที่จำลองห้องที่มีเฟอร์นิเจอร์ให้มองเห็นผ่านหน้าต่างแบน [22]

## สิ่งที่เกิดขึ้น
หัวข้อนี้หนักไปทาง Unreal อย่างชัดเจน มีหลาย production บน UE5 โผล่พร้อมกัน: Halo: Campaign Evolved กำหนด 28 ก.ค. 2026 [6][47], เกมแข่งรถ Clutch ใช้ custom UE5 physics จำลองอุณหภูมิยาง แรงยึดเกาะ และระบบกันสะเทือนในโลกเปิด 1:1 ของ Monaco/South-of-France สร้างโดยทีมอดีต Forza Horizon [3][7][21], รีเมค Tomb Raider: Legacy of Atlantis [19][34], รีเมค Halo 3 Sierra 117 [4], KH4 [25], Danganronpa Another v3 [14], และรายงาน job posting ของ Riot ที่ชี้ว่า TFT จะเปลี่ยนมาใช้ Unreal [57][24] ประเด็น performance ถูกวิจารณ์ซ้ำ — framerates ของฮาร์ดแวร์ระดับสูงที่อ่อนแอ [36] และการ upscale จาก resolution ภายในต่ำ [11] — โดยมีรายงาน Series X Performance Mode ที่ทำได้ดีพอควรเป็นข้อยันกลับ [47] ฝั่ง Godot, 4.7 RC2 ลงมาเป็นรอบตรวจ regression สุดท้ายก่อน stable [17] พร้อม session Xbox Godot sample [52] และการ port จาก Roblox มา Godot [60] Unity ปรากฏหลักผ่านเครื่องมือ baking/shader ของ Real Fake Interiors [22] เธรด AI-in-pipeline รันคู่ขนาน: ถกเรื่อง generative AI ในรีเมค Tomb Raider [34], การทดลองสร้างเกมด้วย AI agent [10][56][8], และความสงสัยเรื่องคุณภาพ output ของ AI [37] รายการที่เหลือส่วนใหญ่เป็น indie marketing, tutorials [32][45][28], และ engine-fandom debate รอบ Glitch Productions/Epic [1][16][31]

## ทำไมถึงสำคัญ (เหตุผล)
สัญญาณที่ซ่อนอยู่ใต้เสียงรบกวนคือ feature set ระดับสูงของ UE5 (Lumen, Nanite, hardware RT) ยังคงถูกส่งมอบใน AAA remake แต่แลกมาด้วย performance headroom จนต้องพึ่ง upscaling เชิงรุกที่ทำให้ความคมชัดของภาพตกลงอย่างเห็นได้ชัด [11][36] trade-off นี้สำคัญมากต่อสตูดิโอที่มุ่งเป้า XR/VR หรือ mobile ซึ่ง resolution ภายในต่ำและ artifact จากการ upscale ทนได้น้อยกว่าบนทีวีมาก ตัวอย่างที่ขัดกัน [47] แสดงว่า engine เดียวกันล็อก 60fps ได้หากกำหนดขอบเขตที่ 1080p ด้วยการตั้งค่าที่มีวินัย — บทเรียนคือวินัยการ configuration ไม่ใช่ตัวเลือก engine Godot 4.7 stable ที่ใกล้เข้ามา [17] บวกกับเส้นทาง console (Xbox) [52] สะท้อนความสุกงอมอย่างช้าๆ ในฐานะทางเลือกน้ำหนักเบาสำหรับงาน 2D และ 3D เล็ก/edutech ด้าน AI ความแตกต่างระหว่างความตื่นเต้นแบบ 'สร้าง prototype ได้ในไม่กี่นาที' [10][56] กับการวิจารณ์ว่า 'ดูถูกหากขาดงานฝีมือจริง' [37] สะท้อนสถานะที่แท้จริงของ tooling: เร็วสำหรับ throwaway prototype และ scaffolding แต่ยังทดแทน art และ design direction ไม่ได้ การที่ generative AI ถูกใช้ใน remake ระดับ marquee [34] บ่งชี้ว่าสตูดิโอกำลังทดสอบแบบเปิดเผยใน production ซึ่งจะกำหนดความคาดหวังของลูกค้าและผู้เล่น

## ความเป็นไปได้
Godot 4.7 จะ stable ในเร็วๆ นี้มีความน่าจะเป็นสูง เพราะ RC2 ถูกนิยามชัดว่าเป็น regression window สุดท้าย [17] กระแสต่อต้าน performance ของ UE5 น่าจะยังต่อเนื่อง เนื่องจากมีสองรายงานอิสระในวันเดียว [11][36] ต่อหนึ่งข้อมูลเชิงบวก [47] การย้าย TFT ไป Unreal เป็นไปได้แต่ยังไม่ยืนยัน — อาศัยการอ่าน job posting เพียงรายการเดียว [57][24] ให้ถือเป็นข่าวลือจนกว่า Riot จะยืนยัน การนำ generative AI มาใช้ในไปป์ไลน์กระแสหลักในวงกว้างเป็นไปได้และกำลังเติบโต แต่จะยังคงเป็นที่ถกเถียงเรื่องคุณภาพแทนที่จะกลายเป็น default [34][37] ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น จึงไม่ได้ให้ไว้

## การประยุกต์ใช้สำหรับ NDF DEV
1) ประเมิน Real Fake Interiors สำหรับ scene arch-viz/mobile/XR ใน Unity ที่สามารถ fake ห้องมีเฟอร์นิเจอร์ผ่านหน้าต่างแทนการ model จริง — ลด geometry และ draw calls (effort ต่ำ) [22] 2) จัดทำ settings-discipline checklist สำหรับงาน UE5 หรือ Unity ฟิเดลิตีสูง โดยเฉพาะ XR/VR: จำกัดการพึ่งพา Lumen/Nanite และตรวจสอบ native internal resolution เพราะ upscaling ที่พอรับได้บนทีวีพังในหน้าจอ headset (effort ต่ำ, internal policy) [11][36][47] 3) ติดตาม Godot 4.7 stable สำหรับ prototype 2D และ edutech/e-learning เบาๆ และดู Xbox Godot sample session เพื่อเส้นทาง console (effort ต่ำ) [17][52] 4) Pilot AI agent เฉพาะสำหรับ greybox/prototype scaffolding อย่างรวดเร็ว โดยให้มนุษย์เป็นเจ้าของ art และ design — กำหนดความคาดหวังว่า raw output จาก AI ดูถูกหากขาดงานฝีมือ (effort ปานกลาง) [10][56][37] ข้าม: engine-fandom และ debate ของ Glitch/Epic [1][16][25][31], ข้อโต้เถียงทางการเมืองของ Pronoun Palace [18], โพสต์การเมืองนอกเรื่อง [41][43], และโพสต์ indie marketing/wishlist — ไม่มีสิ่งใดต้องดำเนินการ

## สัญญาณที่ต้องจับตา
- การ release Godot 4.7 stable หลัง RC2 — ยืนยัน timing และตรวจ regression ก่อนพิจารณานำไปใช้ในโปรเจกต์ [17]
- Riot จะยืนยันอย่างเป็นทางการว่า TFT ย้ายมา Unreal หรือไม่ ตอนนี้ยังเป็นแค่การอนุมานจาก job posting [57][24]
- การตอบรับการใช้ generative AI ในรีเมค Tomb Raider ตอนและหลัง reveal — เป็นการทดสอบสาธารณะว่า AI-in-production จะเป็นที่ยอมรับหรือไม่ [34]
- กระแสต้าน image clarity ของ UE5 (การ upscale จาก internal resolution ต่ำ) — เกี่ยวข้องหากลูกค้าผลักดัน UE5 สำหรับ VR หรือ mobile [11][36]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | iDuckFilms | ^4714 c35 | [There are plenty of valid reasons to criticize Glitch Productions, but why are s](https://x.com/iDuckFilms/status/2065102252789174337) |
| x | Windpress | ^4301 c16 | [This SFW Horror game leaves a BIG impact on the player. You must navigate tight ](https://x.com/Windpress/status/2065119093124899111) |
| x | farzam_plays | ^1934 c73 | [Clutch will be using UE5 with a custom physics engine for aspects such as: - Tir](https://x.com/farzam_plays/status/2065117350551076925) |
| x | Infiniteforges | ^1271 c42 | [Here's an update on my Halo 3: Sierra 117 remake in Unreal Engine 5 https://t.co](https://x.com/Infiniteforges/status/2065218610587382231) |
| x | ciirulean | ^1035 c5 | [very pleased to see godot feature our game for obvious reasons but also I'm just](https://x.com/ciirulean/status/2065135580166737933) |
| x | Pirat_Nation | ^1011 c137 | [A new look at Halo Campaign Evolved realistic graphics The game has been develop](https://x.com/Pirat_Nation/status/2065170541992890415) |
| x | GameRiot | ^647 c19 | [NEW details on Clutch from recent previews 👀 • Open world set in the South of Fr](https://x.com/GameRiot/status/2065134642483835132) |
| x | itsnicholash | ^573 c31 | [fable, I want you to grab a MetaHuman file off of Unreal Engine Marketplace or F](https://x.com/itsnicholash/status/2065189876035629322) |
| x | HedProtag | ^431 c2 | [Discord Server for Synapse is now open. Exclusive roles are still preserved for ](https://x.com/HedProtag/status/2065117361129033869) |
| x | ziwenxu_ | ^370 c102 | [Day 2 of building my GTA 6 agent in the loop. It's working better than yesterday](https://x.com/ziwenxu_/status/2065090683501728110) |
| x | Weston_Mitchell | ^368 c11 | [all these new ue5 games have all the shit turned on and they have to do 540p int](https://x.com/Weston_Mitchell/status/2065111412981293266) |
| x | IsThisA3DModel | ^349 c5 | [@ABAOProductions @Kling_ai @kitbash3d kling is not a render engine. unreal actua](https://x.com/IsThisA3DModel/status/2065140983461789840) |
| x | AboveLandGame | ^337 c6 | [Hack-and-slash? Sports? YES! ⚔️🏀 #ShowcaseThursday #gamedev #indiedev #gamingcli](https://x.com/AboveLandGame/status/2065226330220712292) |
| x | _Buckadeer | ^291 c3 | [Danganronpa Another v3 forced to resume progress with unreal engine](https://x.com/_Buckadeer/status/2065214437318066345) |
| x | Hairtails1 | ^291 c4 | [The full version of 《The Shu Legend》 is now available on Steam. Thank you for su](https://x.com/Hairtails1/status/2065277108365255154) |
| x | iDuckFilms | ^271 c3 | [If people want Glitch Productions to not work with Epic Games, what are they sup](https://x.com/iDuckFilms/status/2065102255922291035) |
| x | godotengine | ^255 c6 | [Our second Release Candidate for #GodotEngine 4.7 has arrived! This will be your](https://x.com/godotengine/status/2065123733367345515) |
| x | LundukeJournal | ^243 c42 | [The Open Source Godot Game Engine is promoting an extreme, pro-Trans game titled](https://x.com/LundukeJournal/status/2065149436951667038) |
| x | DMC_Ryan | ^242 c8 | [We got to play about 45 minutes of Tomb Raider: Legacy of Atlantis, the upcoming](https://x.com/DMC_Ryan/status/2065124279218487748) |
| x | IRONY_the_game | ^226 c6 | [THE IRONY has reached 50,000 wishlists! Thank you so much for all your support a](https://x.com/IRONY_the_game/status/2065256898098864131) |
| x | everyonebpup | ^201 c12 | [🚨 HOLY CRAP the ex-Forza Horizon team just dropped their new game and it's NFS a](https://x.com/everyonebpup/status/2065144209489764622) |
| x | 80Level | ^195 c1 | [Real Fake Interiors by @AmplifyCreates is a Unity baking tool and shader combo t](https://x.com/80Level/status/2065109302562422981) |
| x | artyfact_game | ^192 c12 | [⚡️ Why Artyfact is different 🎮 AAA graphics powered by Unreal Engine 5.7 ⚡️ Thri](https://x.com/artyfact_game/status/2065102885265014849) |
| x | SkinSpotlights | ^188 c6 | [@0Replex0 I just can't imagine them doing a transition like this but I don't kno](https://x.com/SkinSpotlights/status/2065339159963693506) |
| x | MasterLeytrx | ^175 c6 | ["KH4's combat looks like KH3 combat!!!" I mean… yeah? Did you expect otherwise? ](https://x.com/MasterLeytrx/status/2065114248754135163) |
| x | drivethegame | ^158 c5 | [Not every run is perfect. #indiegames #indiedev #unity https://t.co/NB70qCsSjB](https://x.com/drivethegame/status/2065101755734757421) |
| x | RPGPaperMaker | ^143 c2 | [New feature added in RPG Paper Maker 3.1.20: Camera properties live preview! #ga](https://x.com/RPGPaperMaker/status/2065132137200697430) |
| x | delaigrodela | ^142 c3 | [Thursday. Tea. Because it's not time for coffee. Warming up with Unreal Engine. ](https://x.com/delaigrodela/status/2065125980117606512) |
| x | SCF_Games | ^140 c6 | [When you miss the toss.. Wishlist Black Tides on Steam now link in Bio! #BlackTi](https://x.com/SCF_Games/status/2065097577666683232) |
| x | novasoupONLINE | ^134 c8 | [looks like bad Shovelware with an Unreal Engine coat of paint. same tier as Garf](https://x.com/novasoupONLINE/status/2065124874935280106) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@iDuckFilms</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4714 · 💬 35</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/iDuckFilms/status/2065102252789174337">View @iDuckFilms on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“There are plenty of valid reasons to criticize Glitch Productions, but why are so many people surprised that they are collaborating with Fortnite? A lot of their stuff is partially funded by Epic and ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>คนโพสต์ชี้ว่าการที่ Glitch Productions ร่วมงานกับ Fortnite ไม่ใช่เรื่องน่าแปลกใจ เพราะ Epic Games ให้ทุนสตูดิโอนี้บางส่วนและพวกเขาใช้ Unreal Engine อยู่แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/iDuckFilms/status/2065102252789174337" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Windpress</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4301 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Windpress/status/2065119093124899111">View @Windpress on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This SFW Horror game leaves a BIG impact on the player. You must navigate tight corridors while avoiding being spotted. Triple A Horror games have been SLOP since Unreal Engine became a thing. Indie D”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ X ยก indie horror game ไม่ระบุชื่อเป็นตัวอย่างความสำเร็จ โดยบอกว่า AAA horror ตกต่ำลงนับตั้งแต่วงการย้ายมาใช้ Unreal Engine</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Windpress/status/2065119093124899111" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@farzam_plays</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1934 · 💬 73</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/farzam_plays/status/2065117350551076925">View @farzam_plays on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Clutch will be using UE5 with a custom physics engine for aspects such as: - Tire temperature - grip levels - suspension - etc. From what I've seen the game is very gorgeous and didn't seem that have ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>เกม Clutch ใช้ UE5 ร่วมกับ custom physics engine ดูแล tire temperature, grip, และ suspension — และนักพัฒนารายงานว่าไม่พบ traversal stutter แบบที่เห็นใน UE5 open-world เกมอื่น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การวาง custom physics layer บน UE5 เพื่อหลีก traversal stutter เป็น architecture pattern ที่ควรติดตามสำหรับงาน open-world simulation-heavy</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าทีม Unity ประเมิน UE5 สำหรับ open-world หรือ driving sim ให้ใช้ approach ของ Clutch เป็น reference สำหรับแก้ปัญหา stutter</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/farzam_plays/status/2065117350551076925" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Infiniteforges</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1271 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Infiniteforges/status/2065218610587382231">View @Infiniteforges on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here’s an update on my Halo 3: Sierra 117 remake in Unreal Engine 5 https://t.co/rguNb6D3Fh”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาเดี่ยวกำลัง recreate ด่าน Sierra 117 จาก Halo 3 ใน Unreal Engine 5 พร้อมแชร์ความคืบหน้าด้านภาพ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แสดงคุณภาพ environment art ที่ทำได้จริงด้วยคนเดียวใน UE5 — ใช้เป็น visual benchmark ตอน scope งาน level design ได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ใช้ clip นี้เป็น reference ด้าน environment fidelity ถ้าทีมประเมิน UE5 สำหรับ 3D project ในอนาคต</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Infiniteforges/status/2065218610587382231" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ciirulean</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1035 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ciirulean/status/2065135580166737933">View @ciirulean on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“very pleased to see godot feature our game for obvious reasons but also I'm just glad that they didn't censor the clown boobs. I wanted to make a point of including nonsexual nudity in pp because the ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev ดีใจที่ Godot นำเกมของตัวเองไปแนะนำ และชื่นชมที่ platform ไม่เซนเซอร์ nudity ที่ตั้งใจใส่ไว้เพื่อสื่อ artistic statement</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ciirulean/status/2065135580166737933" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1011 · 💬 137</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2065170541992890415">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A new look at Halo Campaign Evolved realistic graphics The game has been developed in Unreal Engine 5 with updated high-definition visuals. The game is scheduled to release on July 28 2026 https://t.c”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนนักพัฒนา (@Pirat_Nation) รีเมค Halo Campaign Evolved ใน Unreal Engine 5 พร้อม visuals แบบ photorealistic กำหนดปล่อย 28 กรกฎาคม 2026</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แสดง visual bar ที่ UE5 Nanite/Lumen ทำได้บน classic shooter IP — ใช้อ้างอิงเวลา client ถามเรื่อง scope งาน high-fidelity 3D</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2065170541992890415" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GameRiot</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 647 · 💬 19</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GameRiot/status/2065134642483835132">View @GameRiot on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“NEW details on Clutch from recent previews 👀 • Open world set in the South of France 🇫🇷 • 1:1 recreation of Monaco 🇲🇨 • Collectibles, stunt jumps, speed traps &amp; more • Custom Unreal Engine 5 tech • In”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Clutch คือเกม arcade racing open-world ที่กำลังจะมา สร้างบน custom UE5 มี Monaco จำลอง 1:1, รถ 150 คัน, โหมด PvPvE และ co-op story เต็มรูปแบบ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GameRiot/status/2065134642483835132" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@itsnicholash</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 573 · 💬 31</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/itsnicholash/status/2065189876035629322">View @itsnicholash on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“fable, I want you to grab a MetaHuman file off of Unreal Engine Marketplace or Fab Marketplace or something like that. There should be free ones. Find a character controller that works with that for w”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Fable AI agent สร้าง three.js demo บินแบบ Superman ครบ — MetaHuman character, environment จาก World Labs gsplats, camera animation, bloom+grain post-FX — จาก 1 prompt, ผู้เขียนให้คะแนน 'not bad'</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>1 prompt สามารถ scaffold 3D web experience ครบ (assets + physics + post-FX) ได้แล้ว — เป็น baseline ความเร็วที่จับต้องได้สำหรับงาน XR/web prototype</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ลอง Fable สร้าง three.js + gsplat prototype สำหรับ demo XR concept ให้ลูกค้าก่อน commit Unity build เต็ม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/itsnicholash/status/2065189876035629322" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
