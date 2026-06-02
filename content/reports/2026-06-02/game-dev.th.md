---
type: social-topic-report
date: '2026-06-02'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-02T03:13:38+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 141
salience: 0.45
sentiment: neutral
confidence: 0.5
tags:
- game-dev
- unreal-engine
- godot
- unity
- summer-game-fest
- ai-npc
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2061309399818285059/img/Wj6TFbABBEnXU3VQ.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-02

## TL;DR
- NetEase จะนำ "Blood Message" ไปโชว์ที่ Summer Game Fest — AAA single-player เกมแรกของค่าย, third-person action-adventure, ไม่มี open world, ใช้ Unreal Engine 5 [2]
- Tim Sweeney จาก Epic ยืนยัน Unreal Engine และ Fortnite รองรับ Windows ARM แล้ว [4]; อีกโพสต์ระบุว่า UE รองรับ Linux แต่ Fortnite ยังไม่รองรับ [19]
- Godot มีโมเมนตัมชัดเจนในหลายโพสต์: thread โปรโมตแนว free/keep-100%-revenue [3] และ update PCG (procedural content generation) graph ที่เร็วขึ้นและ compose ได้ง่ายขึ้น [29]
- WEMADE's MIR5 (UE5 MMORPG) โปรโมต "AI-driven boss" ชื่อ Asterion ที่ขับเคลื่อนด้วย NVIDIA ACE [10] — เป็น runtime AI ใน NPC ไม่ใช่ pipeline tooling
- Unity tooling: Unity Shaders Bible กำลังเพิ่ม 40+ หน้า [7] และมีการแชร์ Shader Graph stylized liquid shader โดยใช้ vertex-painted flow maps [53]

## What happened
ส่วนใหญ่เป็น X posts จาก solo/indie developer (WIP clips, pixel art, VFX, wishlists) ช่วง Summer Game Fest season ข่าวที่มีน้ำหนัก: NetEase จะเปิดตัว AAA single-player action-adventure บน Unreal Engine 5 ชื่อ "Blood Message" ที่ Summer Game Fest [2]; Tim Sweeney จาก Epic ยืนยัน Unreal Engine และ Fortnite ทำงานบน Windows ARM [4] ขณะที่อีกโพสต์ระบุว่า Fortnite ยังขาด Linux support แม้ engine จะรองรับอยู่แล้ว [19]; MIR5 ของ WEMADE โปรโมต "AI-driven boss" พลัง NVIDIA ACE บน UE5 [10]; Godot ปรากฏซ้ำหลายครั้ง — promotional thread [3], PCG performance/composability update [29], และโปรเจกต์ 3D/2D ขนาดเล็กอีกหลายรายการ [31][32][38]; Unity ปรากฏส่วนใหญ่ผ่านเนื้อหาเรียนรู้และ shader tooling [7][53][39][58]

## Why it matters (reasoning)
สัญญาณการเลือก engine แบ่งตามแนวที่คุ้นเคย: Unreal ครองตลาด AAA และ high-fidelity tier ([2][10][26][28]), Godot ได้รับการยอมรับในกลุ่ม grassroots ด้วยเหตุผลเรื่องต้นทุนและความเป็นเจ้าของ ([3][29]), Unity ปรากฏผ่านเนื้อหา shader/tooling ไม่ใช่ headline projects ([7][53]); สำหรับ studio ที่ใช้ Unity เป็นหลัก pattern นี้คือสิ่งที่ควรอ่านให้ขาด — สุขภาพ ecosystem ของ Unity ตอนนี้หน้าตาเหมือน tooling content ที่ต่อเนื่อง ไม่ใช่การชนะ platform ใหม่ Windows ARM support [4] มีความสำคัญในฐานะ second-order effect ของ ARM hardware ที่แพร่หลายขึ้น (Snapdragon laptops, ARM-based handhelds, และต่อเนื่องไปยัง mobile/XR ARM targets) ซึ่งเกี่ยวข้องโดยตรงกับ mobile และ XR builds; NVIDIA ACE boss [10] เป็น marketing claim เรื่อง runtime LLM-driven NPC behavior — เป็น vendor demo รายเดียว ไม่ใช่หลักฐานว่า AI NPCs เป็น production-standard; [13] เป็น joke post และ [17] เป็น unverified leaker account จึงไม่ควรนำไปใช้ตัดสินใจใดๆ

## Possibility
**Likely:** Summer Game Fest จะมี UE5 single-player AAA เพิ่มอีกในวันถัดไป เพราะ [2] คือการ positioning ก่อนงาน **Plausible:** Godot adoption โตต่อเนื่องในกลุ่ม solo/indie 2D และ lightweight 3D dev ด้วยเหตุผลด้านต้นทุน [3][29] แต่ไม่แทนที่ Unreal/Unity ใน studio ที่ต้องการ mature XR/mobile pipeline ในปีนี้ **Plausible:** AI-driven NPC features ยังคงอยู่ในขั้น demo/marketing ([10]) ก่อนจะกลายเป็น production tooling ที่เชื่อถือได้ เพราะ claim นี้มาจากแหล่งเดียวและยังไม่ได้รับการยืนยัน **Unlikely:** จะสรุปอะไรจาก [17] (Valve/UE6 rumor) — เป็น leaker source ไม่มีแหล่งยืนยัน; ไม่มีแหล่งใดระบุตัวเลขความน่าจะเป็น

## Org applicability — NDF DEV
1) ติดตาม Summer Game Fest UE5 single-player reveals เพื่อใช้เป็น design และ market reference ไม่ใช่แรงกดดันให้เปลี่ยน engine — effort ต่ำ [2]. 2) บันทึก Unreal Windows ARM support เป็นข้อมูลสำหรับวางแผน ARM mobile/XR target; ตรวจสอบว่า ARM coverage ใน Unity pipeline ปัจจุบันทันสมัยหรือไม่ — effort ต่ำในการประเมิน [4]. 3) สำหรับ 2D/edutech prototype น้ำหนักเบาหรือ web-deliverable builds ให้ประเมิน Godot เป็น secondary option บนฐานต้นทุน/ความเป็นเจ้าของ โดยมอง [3] เป็นการตลาดและ validate ด้วย PCG update จริง [29] — effort ปานกลาง. 4) ส่ง Unity Shaders Bible [7] และ Shader Graph flow-map liquid technique [53] ให้ artists/TDs ใช้เป็นเนื้อหาเรียนรู้ Unity โดยตรง — effort ต่ำ. ข้าม: NVIDIA ACE AI-boss claim [10] สำหรับ build target ตอนนี้ (vendor demo รายเดียว, infrastructure หนัก); Valve/UE6 rumor [17]; และ joke/NSFW posts [13][44]

## Signals to Watch
- Summer Game Fest reveals ในวันถัดไป — จำนวนและระดับของ UE5 single-player titles [2]
- PCG และ composability improvements ของ Godot ที่กำลังพัฒนาสู่ production use [29]
- NVIDIA ACE-style runtime AI NPCs จะก้าวพ้น marketing demos ไปสู่ shipped, supported features หรือไม่ [10]
- ARM target support ข้าม engine ต่างๆ (Unreal ยืนยันแล้ว [4]) เมื่อ ARM laptops/handhelds/XR ขยายตัว

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | 3DxDEV7 | ^1009 c12 | [1 year of gamedev in 54 seconds.. by @BruteForceGame #unity3d #solodev #gamedev ](https://x.com/3DxDEV7/status/2061309835740631504) |
| x | GermanStrands | ^1006 c28 | [Blood Message will be shown at Summer Game Fest: -First AAA single-player title ](https://x.com/GermanStrands/status/2061427656822817263) |
| x | ihtesham2005 | ^840 c40 | [Two Argentinian friends killed the entire game engine industry. It's called Godo](https://x.com/ihtesham2005/status/2061415843146375517) |
| x | TimSweeneyEpic | ^822 c151 | [This is insanely cool! And nowadays Unreal Engine and Fortnite support Windows A](https://x.com/TimSweeneyEpic/status/2061473405853938054) |
| x | ib4aplays | ^787 c11 | [The game has been in development for more than three full years. According to th](https://x.com/ib4aplays/status/2061167772386607393) |
| x | ShatterPointGS | ^766 c10 | [We've added one more system mechanic: Burst Breaker. Green Bursts can be used to](https://x.com/ShatterPointGS/status/2061523176618664347) |
| x | ushadersbible | ^679 c3 | [A new update for the Unity Shaders Bible is coming soon! Over 40 new pages will ](https://x.com/ushadersbible/status/2061320519660552375) |
| x | KrakenCombo | ^614 c18 | [One of the best things about writting clean code is how easy it is to do cool sh](https://x.com/KrakenCombo/status/2061382095969062958) |
| x | HauntSoft | ^614 c17 | [TRASH BAG TOMB In active development #gamedev #indiedev #indiegames #flash #horr](https://x.com/HauntSoft/status/2061262109996884061) |
| x | Kai_zen78 | ^563 c4 | [MIR5 • Upcoming open-world MMORPG from WEMADE, built on Unreal Engine 5 • Succes](https://x.com/Kai_zen78/status/2061309239004709115) |
| x | ashlee3dee | ^498 c1 | [stylized black hole vfx with geometry nodes :3 i will port this to unreal engine](https://x.com/ashlee3dee/status/2061195779952275511) |
| x | sinknode | ^486 c2 | [great helm #pixelart #ドット絵 #gamedev #indiedev https://t.co/Gyz7q3tpkc](https://x.com/sinknode/status/2061421726278242319) |
| x | tfembunny | ^438 c7 | [June patch notes: -boobs size increased by 15% -switch to unreal engine 5 for be](https://x.com/tfembunny/status/2061241326679506961) |
| x | Tooley1998 | ^425 c9 | [Portals are coming to Lay of the Land. Soon you'll be able to easily connect dif](https://x.com/Tooley1998/status/2061314913247826028) |
| x | devkidd_ | ^400 c14 | [I just finished the initial version of my character template. Which do you prefe](https://x.com/devkidd_/status/2061434478258774325) |
| x | ID_AA_Carmack | ^353 c37 | [Back in the Armadillo Aerospace days, our liquid oxygen loadouts were 50 to 100 ](https://x.com/ID_AA_Carmack/status/2061454639434739826) |
| x | valveleaker | ^331 c5 | [valve developers will not use unreal engine 6 to develop a new valve game https:](https://x.com/valveleaker/status/2061218213107532092) |
| x | rafaelborven | ^328 c4 | [Got asked how I did the last VFX animation for @6EyesStudioLLC, was basically a ](https://x.com/rafaelborven/status/2061470983769252282) |
| x | fortniteonlinux | ^327 c2 | [Unreal engine supports linux but not fortnite](https://x.com/fortniteonlinux/status/2061494643506717147) |
| x | retrotesque | ^305 c0 | [&lt; waiting for waiting for godot &gt; team attended the concert as well 🥹 minh](https://x.com/retrotesque/status/2061274483890299014) |
| x | FNaFFangameWiki | ^304 c0 | [New Hire Classic is a recently-announced game using Unreal Engine to retake its ](https://x.com/FNaFFangameWiki/status/2061508076650238173) |
| x | HideWorksGames | ^299 c29 | [NEW TRAILER for LIMINAL POINT, our Silent Hill, Resident Evil and Signalis inspi](https://x.com/HideWorksGames/status/2061526544170786926) |
| x | MythicLoveGame | ^296 c0 | [And you can wishlist our human-made VN on Steam! #MythicLove #gamedev #indiedev ](https://x.com/MythicLoveGame/status/2061232110225051883) |
| x | LesenNow | ^226 c0 | [The dream team (Zero still WIP) #MegaManX #indiedev #Fangame https://t.co/FaGtBH](https://x.com/LesenNow/status/2061364460846010591) |
| x | hypnobius | ^208 c2 | [Been working hard on my "Everyday Home" pixel art tileset 💪 Here's a preview scr](https://x.com/hypnobius/status/2061481628661326108) |
| x | Leave_MeBee | ^183 c3 | [Destiny is lookin CRAZY in unreal engine https://t.co/BIAmuERZvV](https://x.com/Leave_MeBee/status/2061198572951937402) |
| x | GarageArts_Max | ^160 c3 | [Based on user feedback, I have made it possible to switch between keyboard/mouse](https://x.com/GarageArts_Max/status/2061438926200754443) |
| x | Neurotic3D | ^153 c3 | [Stumbled upon some old #WIPㅤㅤㅤ screenshots from this environment that give off s](https://x.com/Neurotic3D/status/2061274102740992139) |
| x | digisculp | ^148 c1 | [The PCG system in Godot is now much faster and easier to use. It can now handle ](https://x.com/digisculp/status/2061301248381309366) |
| x | coinmakersim | ^141 c18 | [This morning I woke up to 10 thousand wishlists. Graduation felt nothing compare](https://x.com/coinmakersim/status/2061366766228619740) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@3DxDEV7</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1009 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/3DxDEV7/status/2061309835740631504">View @3DxDEV7 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“1 year of gamedev in 54 seconds.. by @BruteForceGame #unity3d #solodev #gamedev https://t.co/zrPAO74kwK”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Solo dev @BruteForceGame โพสต์ timelapse 54 วินาที รวม 1 ปีของการทำ Unity 3D game ได้ 1,009 likes บน X</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Timelapse devlog สร้าง audience และโชว์ความสามารถของทีม — format ที่ได้ผลจริงสำหรับทีมเล็กที่ทำ Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลองเก็บ milestone ของ project ที่ทำอยู่แล้วตัด timelapse สั้นลง social ของ studio</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/3DxDEV7/status/2061309835740631504" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@GermanStrands</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1006 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/GermanStrands/status/2061427656822817263">View @GermanStrands on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Blood Message will be shown at Summer Game Fest: -First AAA single-player title by NetEase -Third-person action-adventure -Singleplayer only -Cinematic storytelling -No open world -Unreal Engine 5 -Se”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>NetEase ประกาศ Blood Message เกม AAA single-player เกมแรก สร้างด้วย UE5 เป็น third-person action-adventure ฉากราชวงศ์ถัง มี stealth และ survival combat เตรียมโชว์ใน Summer Game Fest 2026</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>NetEase เข้าสู่ AAA single-player แบบ narrative-driven บน UE5 ชี้ให้เห็นว่า publisher ฝั่งเอเชียเริ่มลงทุนกับ cinematic non-open-world — รูปแบบที่ studio เล็กๆ ก็ทำได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดูแนวทาง Blood Message — ไม่มี open world เน้น narrative และ cultural setting — เป็น template สำหรับ pitch single-player ที่ scope ชัดเจน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/GermanStrands/status/2061427656822817263" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ihtesham2005</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 840 · 💬 40</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ihtesham2005/status/2061415843146375517">View @ihtesham2005 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Two Argentinian friends killed the entire game engine industry. It's called Godot. You build full 2D and 3D games for free, ship them anywhere, and keep 100% of every dollar you ever make. Here's how ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Godot Engine (MIT license, 111k stars) เป็น open-source engine สำหรับเกม 2D/3D ไม่มีค่า license ไม่มี royalty รองรับ GDScript, C#, C++ และ export ได้ทุก platform</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ถ้า studio จ่าย Unity fee อยู่ Godot ตัดต้นทุนนั้นทิ้งทั้งหมดโดยยังครอบคลุม platform เดิม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง prototype โปรเจกต์เล็กใน Godot เพื่อเทียบ build time และ workflow ก่อนตัดสินใจ migrate</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ihtesham2005/status/2061415843146375517" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TimSweeneyEpic</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 822 · 💬 151</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TimSweeneyEpic/status/2061473405853938054">View @TimSweeneyEpic on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This is insanely cool! And nowadays Unreal Engine and Fortnite support Windows ARM devices 100%.”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Tim Sweeney (CEO Epic Games) ยืนยัน Unreal Engine และ Fortnite รองรับ Windows ARM 100% แล้ว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Windows ARM (Snapdragon X) ขยายตลาดเร็ว UE5 รองรับครบแล้ว ไม่มี barrier ในการ ship เกมไปยัง device กลุ่มนี้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้ามีโปรเจกต์ Unreal Engine ให้ทดสอบ build บน Windows ARM เพื่อยืนยัน compatibility</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TimSweeneyEpic/status/2061473405853938054" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ib4aplays</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 787 · 💬 11</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ib4aplays/status/2061167772386607393">View @ib4aplays on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The game has been in development for more than three full years. According to the information obtained the project relies on Unreal Engine, one of the most powerful game engines today, which raises ex”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>เกมที่ถูกแท็ก #FIFA #Netflix พัฒนามากกว่า 3 ปีด้วย Unreal Engine ตามข้อมูลที่ผู้โพสต์ได้รับ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ib4aplays/status/2061167772386607393" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ShatterPointGS</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 766 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ShatterPointGS/status/2061523176618664347">View @ShatterPointGS on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We've added one more system mechanic: Burst Breaker. Green Bursts can be used to escape combos, but cannot be used while Broken. Gold Bursts can be used in neutral and fully restores Resolve and also ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>เกม fighting indie ShatterPoint เพิ่มระบบ Burst Breaker — Green Burst หนี combo ได้แต่ใช้ไม่ได้ตอน Broken; Gold Burst ใช้ใน neutral และ reset ทั้ง Resolve กับ Broken state</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัวอย่าง asymmetric escape mechanic ที่ชัด — resource เดียวสองแบบ สร้าง risk/reward หลายชั้นโดยไม่ซับซ้อน UI เป็น reference ดีสำหรับ action/fighting game design</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้า Unity project มี escape mechanic ลอง prototype ตาม pattern นี้ — resource สองระดับ (หนี combo vs. reset เต็ม) ก่อนออกแบบ UI</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ShatterPointGS/status/2061523176618664347" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ushadersbible</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 679 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ushadersbible/status/2061320519660552375">View @ushadersbible on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“A new update for the Unity Shaders Bible is coming soon! Over 40 new pages will be added. Get your copy now before the price goes up 🔗 https://t.co/Pb0Py61gN6 #indiedev https://t.co/FaqtpFPXcC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unity Shaders Bible จะเพิ่มเนื้อหากว่า 40 หน้าในอัปเดตที่กำลังจะมา และจะขึ้นราคาหลัง release</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ทีมที่ทำ Unity game และ XR/VR ได้ประโยชน์ตรงๆ จาก shader reference ที่เพิ่มเนื้อหาอีก 40 หน้า</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดูว่าทีม Unity มีหนังสืออยู่แล้วหรือยัง ถ้าไม่มี ซื้อก่อนขึ้นราคาได้เนื้อหาใหม่ในราคาเดิม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ushadersbible/status/2061320519660552375" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KrakenCombo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 614 · 💬 18</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KrakenCombo/status/2061382095969062958">View @KrakenCombo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“One of the best things about writting clean code is how easy it is to do cool shit. For example, I changed a goblin's faction and now he's my personal protector. Little dude is a BEAST. #gamedev #indi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา indie คนหนึ่งแสดงให้เห็นว่า clean code ทำให้เปลี่ยน faction ของ goblin ได้ใน edit เดียว จนกลายเป็น bodyguard NPC ทันที</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ตัวอย่างจริงที่แสดงว่า faction system แบบ data-driven ช่วยเปลี่ยน behavior NPC โดยไม่ต้องแก้ AI logic เลย — ดีมากสำหรับ replayability และ QA</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ตรวจสอบ NPC/enemy design ที่มีอยู่ว่า faction/allegiance data แยกออกจาก behavior logic แล้วหรือยัง ก่อนที่ระบบจะใหญ่ขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KrakenCombo/status/2061382095969062958" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
