---
type: social-topic-report
date: '2026-05-26'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-05-26T03:19:07+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- bluesky
- reddit
- x
regions:
- global
post_count: 162
salience: 0.85
sentiment: mixed
confidence: 0.72
tags:
- unreal-engine-6
- godot
- unity
- indie-dev
- engine-comparison
- tooling
thumbnail: https://pbs.twimg.com/media/HJJ5cGGXoAAxSNX.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-05-26

## TL;DR
- Epic เปิดตัว Unreal Engine 6 อย่างเป็นทางการ ครองวงสนทนาด้วยปฏิกิริยาหลากหลาย — ความตื่นเต้น ความสงสัยต่อความต้องการฮาร์ดแวร์ และมุมมอง 'แค่ปิด Lumen/Nanite/VSM' [15][29][30][37][50][57]
- การเปรียบเทียบเกมสยองขวัญ Unity vs Godot แบบ side-by-side ของ Studio Interrupt กลายเป็น viral และเอนเอียงไปทาง Godot แต่นักวิจารณ์ชี้ว่าการตั้งค่า lighting/shader ที่ไม่เทียบเท่ากันอาจเป็นตัวแปรรบกวน [1][31]
- Godot มีโมเมนตัมที่จับต้องได้: GLES รันลื่นบนโทรศัพท์ปี 2016, wishlists กว่า 3,300 รายการสำหรับ indie tactics RPG, ฟีเจอร์ credits roll ในตัว, blog สอน shader [14][25][28][39]
- สัญญาณการผลิต UE5: 962 commits บน ue5-main สัปดาห์ที่แล้ว, การ refactor Control Rig, build infra ลดลง -67%, และ beta medium-Lumen เร็วกว่า high ราว ~2x [18][57]
- Workflow tooling ที่น่าสนใจ: Lattice Modifier สำหรับ deformation ใน Unity, ไปป์ไลน์ PixZels 2D→3D, RPG Paper Maker 3.1.15 dig mode [4][12][20]

## What happened
Epic Games ประกาศ Unreal Engine 6 ครอง discourse ของวงการ game dev — ข่าวหลุด มุกตลกเรื่อง hardware bloat และบทความใน r/unrealengine ที่ระบุ 962 commits บน ue5-main, การแยก topology/storage ของ Control Rig, และการลด build infra 67% ในสัปดาห์ที่แล้ว [15][37][50][57] กระแสความคิดเห็นแตกออกเป็นสองฝั่ง คือฝ่ายตื่นเต้น ('UE4→UE6 ในช่วงเดียวกับ GTA5→GTA6' [50]) และฝ่ายเบื่อหน่าย ('การ optimize รุ่นใหม่ = คอมพิวเตอร์รุ่นหน้าอาจรันได้' [30]) โดยฝ่ายที่ปกป้องชี้ว่า UE5 ใช้งานได้ดีถ้าปิด Lumen/Nanite/VSM [29] และ beta medium-Lumen เร็วกว่า high ราว ~2x [18]

เรื่องคู่ขนาน: การเปรียบเทียบ Unity vs Godot เกมสยองขวัญของ Thomas Grové กลายเป็น viral [1] มีการโต้แย้งว่า lights/shaders ไม่ได้ตั้งค่าให้เทียบเท่ากัน [31] Godot ยังคงสะสมชัยชนะต่อเนื่อง — GLES รันลื่นบน Samsung S7 ปี 2016 [25], wishlists 3,300 รายการสำหรับ indie tactics RPG RuneCipher [28], ฟีเจอร์ credits roll ในตัวถูกค้นพบ [14], blog สอน interactive shader [39] ฝั่ง Unity มีเครื่องมือในทางปฏิบัติ — Lattice Modifier deformation [4], dynamic fog ด้วย single directional light [22], PixZels 2D→3D [12] ชัยชนะของ indie: เกมท่องคาถาด้วยเสียงภาษาญี่ปุ่นกลายเป็น viral [9], เกม mecha มี wishlists กว่า 22,000 รายการ [11] Porsche เปิดตัว UE car configurator ธีม Fortnite [34]

## Why it matters (reasoning)
การเปิดตัว UE6 เป็นแค่การรีแบรนด์เป็นส่วนใหญ่ — สัญญาณจริงอยู่ที่ commit velocity และ infra work บน ue5-main ของ Epic [57] บวกกับ performance beta อย่าง medium-Lumen [18] กระแสต้าน hardware-bloat [2][30] กำลังแข็งตัวเป็น market segment จริงสำหรับ engine ที่เบากว่า ซึ่งเป็นประโยชน์โดยตรงต่อ Godot และอธิบายได้ว่าทำไมการเปรียบเทียบ Unity vs Godot ที่มีข้อบกพร่อง [1][31] ถึงแพร่กระจายได้กว้าง ผลกระทบลำดับที่สอง: ตำแหน่งของ Unity ถูกบีบ — หนักเกินไปสำหรับกลุ่ม Godot-aesthetic, เบาเกินไปสำหรับงาน AAA UE — ทำให้ต้องรักษาตลาด mid-tier indie/mobile/XR ที่เครื่องมืออย่าง Lattice [4] และ asset ecosystem ที่พิสูจน์แล้วยังคงได้เปรียบ กรณี virality ของ indie [9][11][28] แสดงให้เห็นว่า wishlist traction ตอนนี้มาจาก hook (voice input, niche genre, art identity) ไม่ใช่การเลือก engine

## Possibility
ความน่าจะเป็นสูง (~70%): UE6 วางจำหน่ายแบบ evolutionary — Nanite/Lumen scaling ที่ดีขึ้น, แก้ shader-comp stutter, รีแบรนด์เชิงการตลาดมากกว่าการเขียนใหม่ทั้งหมด; การนำไปใช้ช้าจนถึงปี 2027 ความน่าจะเป็นปานกลาง (~45%): Godot 5.x มีความเทียบเท่า rendering สำหรับ 2D/stylized 3D และดึง mid-indie developer ที่ออกจาก Unity มาได้มากขึ้น โดยเฉพาะบนมือถือ ความน่าจะเป็นต่ำกว่า (~25%): ความล้มเหลวเชิงพาณิชย์หรือปัญหา governance ของ Godot ที่โด่งดัง [41][49] ทำให้โมเมนตัมหยุดชะงัก จับตาดู: Unity ตอบโต้ด้วยการเคลื่อนไหวด้านราคา/runtime เพื่อรักษา indie กลุ่มกลาง AI ในไปป์ไลน์แทบไม่ปรากฏในรอบนี้ — รายงานน้อยไป ไม่ใช่ไม่มี

## Org applicability — NDF DEV
ความเกี่ยวข้องโดยตรงกับ NDF DEV:
- งาน Unity (XR/VR, edutech): คง Unity เป็น primary — Lattice Modifier [4] มีประโยชน์สำหรับงาน character/vehicle ใน VRoom (V), fog system [22] สำหรับฉาก edutech แบบ atmospheric ไม่มีเหตุผลต้อง migrate
- การประเมิน Godot: คุ้มค่าทำ spike 1 สัปดาห์สำหรับ prototype 2D/mobile edutech แบบเบา — GLES perf บน Android เก่า [25] สำคัญสำหรับความเป็นจริงของอุปกรณ์ในโรงเรียนไทย Tactics RPG [28] และ shader blog [39] เป็น reference ที่ดีสำหรับการศึกษา
- Unreal: ยังไม่คุ้มค่า UE6 hype [37][50] เป็นเสียงรบกวนสำหรับ scope ของเรา; กลับมาดูเมื่อถึงเวลาส่งมอบงาน Porsche configurator [34] เป็น reference point ถ้าลูกค้าต้องการ product-viz XR สักวัน
- AI ในไปป์ไลน์: สัญญาณบางในรอบนี้ ยังไม่ต้องดำเนินการ

สรุป: ติดตาม UE6, ทดลอง Godot กับโปรเจกต์เล็กหนึ่งโปรเจกต์, คงใช้ Unity สำหรับ production

## Signals to Watch
- UE6 first dev preview build + ความต้องการระบบจริงเทียบกับ UE5
- Godot 5.x rendering roadmap และ console-port story ใดๆ
- การประกาศ Unity ด้านราคา/runtime เพื่อตอบสนองต่อแรงกดดันจาก Godot
- ว่า indie hit ที่ใช้ voice-input/AI-NPC [9] จะซ้ำได้หรือไม่ — สัญญาณสำหรับ edutech voice mechanics

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | Pirat_Nation | ^5221 c120 | [Game developer Thomas Grové from Studio Interrupt recreated the same horror game](https://x.com/Pirat_Nation/status/2058865663217975447) |
| x | jnvcia | ^4315 c75 | [Everyone's too busy forcing UE5 to look like a 1998 engine. What they could do i](https://x.com/jnvcia/status/2058882543273816233) |
| x | Shpeshal_Nick | ^3821 c60 | [Do people not know Unreal Engine 3 is 21 years old?](https://x.com/Shpeshal_Nick/status/2058863580725027128) |
| x | unity3dvfx | ^3240 c16 | [Check out Lattice Modifier for Unity ➡️a tool that lets you easily deform object](https://x.com/unity3dvfx/status/2058816195701153948) |
| x | KenneyNL | ^2908 c41 | [okay Godot all you need to do is skip a few versions, this is worth it https://t](https://x.com/KenneyNL/status/2058919708728910317) |
| x | ShatterPointGS | ^1986 c17 | [Sometimes, we like to take a break and have a bit of fun in the lab. #indiegame ](https://x.com/ShatterPointGS/status/2058986461362336194) |
| x | ShittyHaloTakes | ^1462 c4 | [I miss the E3 era because there would have been a fucking car lowered from the c](https://x.com/ShittyHaloTakes/status/2058831533427884447) |
| x | gembia2 | ^1225 c42 | [really hate how when you can tell how a game was made in godot because of how Ba](https://x.com/gembia2/status/2058888804719530434) |
| x | RezeroStudio_ | ^1152 c28 | [My game somehow went viral in Japan. People are literally having fun casting spe](https://x.com/RezeroStudio_/status/2058911017909027236) |
| x | Osmg900 | ^1024 c14 | [Dev Log — "You're not alone" P1, Music: Annihilation OST - The Alien @s8box #sbo](https://x.com/Osmg900/status/2058914095294796050) |
| x | GarageArts_Max | ^1015 c25 | [I was just making the mecha game I love... but I am completely stunned by this s](https://x.com/GarageArts_Max/status/2058897366598750464) |
| x | Pixel_Salvaje | ^974 c8 | [#Gamedev: How do you turn 2D orthographic views into a clean 3D model? It's all ](https://x.com/Pixel_Salvaje/status/2058988028551364694) |
| x | KrakenCombo | ^912 c34 | [Ah sweet! Man-made horrors beyond my comprehension!! #gamedev #indiedev https://](https://x.com/KrakenCombo/status/2058840605791277324) |
| reddit | PensiveDemon | ^899 c22 | [[Easter Egg] - Did you know Godot has a built in credits roll feature? Not reall](https://www.reddit.com/r/godot/comments/1tn7h3h/easter_egg_did_you_know_godot_has_a_built_in/) |
| x | gaming_leaker | ^779 c13 | [Unreal Engine 6 has a bigger number in it than Unreal Engine 5. https://t.co/PgR](https://x.com/gaming_leaker/status/2058997525445767469) |
| x | Ninjago9101 | ^739 c8 | [Lord of Mysteries MMORPG has been listed for release on November 1, 2026. Accord](https://x.com/Ninjago9101/status/2058894467151912977) |
| x | unity3dvfx | ^598 c9 | [This looks absolutely heavenly! ☁️✨ Procedural texturing + divine city-building ](https://x.com/unity3dvfx/status/2058598704488079660) |
| x | Star_Wyse | ^544 c10 | [i learned recently that one of the recent versions of ue5 added a beta feature w](https://x.com/Star_Wyse/status/2058982905892753722) |
| x | Kai_zen78 | ^517 c11 | [Swords of Legends • Premium single-player action RPG from Aurogon Shanghai, publ](https://x.com/Kai_zen78/status/2058859867516063927) |
| x | RPGPaperMaker | ^497 c4 | [New feature added in RPG Paper Maker 3.1.15: dig mode for mountains! #gamedev / ](https://x.com/RPGPaperMaker/status/2058971494772847047) |
| x | JamaicanCocoRL | ^471 c20 | [My RLCS 2026 Paris Major Takeaways: 1. Epic wants Rocket League to succeed. With](https://x.com/JamaicanCocoRL/status/2058849891053379904) |
| reddit | No_Telephone5992 | ^442 c33 | [Working on a fog system. Working on a dynamic fog system. It uses one directiona](https://www.reddit.com/r/Unity3D/comments/1tnbztd/working_on_a_fog_system/) |
| x | ilovechrissia | ^393 c4 | [@Shpeshal_Nick that's sort of a disingenuous response because it's less "Rocket ](https://x.com/ilovechrissia/status/2058916160876482921) |
| x | suitNtie22 | ^352 c34 | [So the character has no name btw. I'm open to suggestions in the comments 📜✒️🧐 #](https://x.com/suitNtie22/status/2058927628342718669) |
| reddit | Sea-Good5788 | ^337 c20 | [it runs surprisingly fast on an ancient 2016 phone [GLES] i tried it on a moded ](https://www.reddit.com/r/godot/comments/1tn5wid/it_runs_surprisingly_fast_on_an_ancient_2016/) |
| reddit | edmonddantees | ^314 c14 | [Made a little free game in Godot where you defend your castle from medieval mons](https://www.reddit.com/r/godot/comments/1tn3ki0/made_a_little_free_game_in_godot_where_you_defend/) |
| x | AndreCastroArt | ^308 c6 | [Realtime creature sculpted in Zbrush, Painted on Substancr Painter and rendered ](https://x.com/AndreCastroArt/status/2058968892618207733) |
| reddit | daintydoughboy | ^306 c46 | [Using Godot to create my first game! 3300 wishlists so far! Would you play this?](https://www.reddit.com/r/godot/comments/1tnaoz3/using_godot_to_create_my_first_game_3300/) |
| x | munsplit | ^282 c36 | [nah, unreal haters dont get it just turn off lumen+nanite+vsm and you got yourse](https://x.com/munsplit/status/2058822388452671885) |
| x | ShitpostRock2 | ^279 c4 | [&gt;did you hear they're making Unreal Engine 6? &gt;yeah, they say it's "next-g](https://x.com/ShitpostRock2/status/2059094921987146169) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5221 · 💬 120</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2058865663217975447">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Game developer Thomas Grové from Studio Interrupt recreated the same horror game in both Unity and Godot to compare the engines side by side, and the results were surprisingly one-sided. The project, ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Thomas Grové สร้างเกมสยองขวัญเกมเดียวกันใน Unity และ Godot แล้วเปรียบเทียบ — Godot ชนะทุกด้าน: startup, export, install size, compile speed, และ visual quality</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ช่อง export time (2s vs 15 นาที) กระทบ iteration speed โดยตรง ยิ่ง team ใหญ่ยิ่งเสียเวลาสะสมมาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team วัด build/export pipeline ตัวเองก่อน ถ้าตัวเลขใกล้เคียงรายงานนี้ ให้ประเมิน Godot สำหรับ project ขนาดเล็ก-กลางในอนาคต ก่อนล็อก engine</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2058865663217975447" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jnvcia</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4315 · 💬 75</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jnvcia/status/2058882543273816233">View @jnvcia on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Everyone's too busy forcing UE5 to look like a 1998 engine. What they could do instead is just make 1998 engines, which were routinely created by teams of 1-2 people. Use OpenGL 1.2, people, it's stil”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แทนที่จะบังคับ UE5 ให้ดูเหมือนเกม 1998 ให้สร้าง engine สไตล์ 1998 จริงๆ ด้วย OpenGL 1.2 เลย — ทีม 1-2 คนทำได้สมัยนั้น และ performance จะดีมาก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Engine สไตล์ retro บน OpenGL 1.2 ทำได้จริงในทีมเล็ก หลีกเลี่ยง UE5 licensing, asset pipeline หนัก, และ compile time นานได้หมด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ลอง project low-poly หรือ pixel-art โดยใช้ rendering pipeline เบาๆ แทนที่จะ default ไป URP/HDRP ทุกครั้ง — ลด build time และรัน low-spec device ได้ดีขึ้น</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jnvcia/status/2058882543273816233" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Shpeshal_Nick</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3821 · 💬 60</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Shpeshal_Nick/status/2058863580725027128">View @Shpeshal_Nick on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Do people not know Unreal Engine 3 is 21 years old?”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ชี้ว่า Unreal Engine 3 อายุ 21 ปีแล้ว สื่อว่าคนยังพูดถึงมันเหมือนเป็น engine ปัจจุบัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แสดงให้เห็นว่า game engine เปลี่ยนรุ่นเร็วแค่ไหน — UE3 เก่ามากแล้วในแง่อุตสาหกรรม แต่ยังถูกพูดถึงอยู่ แปลว่า legacy tech ฝังอยู่ในหัวคนนาน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ควรระวังเรื่อง engine version ที่อ้างถึงใน e-learning หรือ internal docs — ระบุ version ให้ชัดเจนทุกครั้งเพื่อไม่ให้ developer รุ่นใหม่เข้าใจผิด</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Shpeshal_Nick/status/2058863580725027128" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@unity3dvfx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3240 · 💬 16</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/unity3dvfx/status/2058816195701153948">View @unity3dvfx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Check out Lattice Modifier for Unity ➡️a tool that lets you easily deform objects, customize characters, or create lifelike car crashes in seconds! #indiedev #gamedev #unity3d #procgen #indiegame http”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Lattice Modifier ใน Unity ช่วย deform mesh แบบ real-time ได้ ทั้งปรับแต่งตัวละคร บิดวัตถุ และทำเอฟเฟกต์การทำลาย เช่น รถชน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การ deform แบบ Lattice เร็วกว่าแก้ mesh มือหรือทำ blend shapes มาก ช่วยลดเวลา prototype ระบบตัวละครและการทำลายได้มาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity เอาไปใช้สร้าง character variant และ VFX รถชนได้เลย ไม่ต้องเขียน shader หรือทำ rigging เพิ่ม</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/unity3dvfx/status/2058816195701153948" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@KenneyNL</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2908 · 💬 41</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/KenneyNL/status/2058919708728910317">View @KenneyNL on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“okay Godot all you need to do is skip a few versions, this is worth it https://t.co/ixwhxKh7Yi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Kenney冗談ว่า Godot แค่ข้ามเลข version ไปก็พอ แล้วมันจะคุ้มกับการย้ายจาก Unity</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>engagement สูงบอกว่า community ยังมองว่า Godot ติดภาพ 'ยังไม่โต' มากกว่าปัญหาเทคนิคจริงๆ เทียบ Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ควรแยกให้ออกว่า Godot ยังขาด feature จริง หรือแค่ภาพลักษณ์ — ถ้าเป็นแค่ branding ความเสี่ยงในการ migrate ต่ำกว่าที่คิด</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/KenneyNL/status/2058919708728910317" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ShatterPointGS</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1986 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ShatterPointGS/status/2058986461362336194">View @ShatterPointGS on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Sometimes, we like to take a break and have a bit of fun in the lab. #indiegame #indiedev #fightinggames #FGC #animation #gamedev https://t.co/18VuKNKufF”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>สตูดิโอ indie fighting game ShatterPointGS แชร์คลิป animation ทดลองจาก lab session สบายๆ โดยแท็กหา FGC community.</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>คลิป lab แบบสบายๆ ได้ 1986 likes บอกว่า behind-the-scenes content ดิบๆ ดึง engagement ได้ดีกว่า announcement ทางการหลายครั้ง.</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team บันทึกคลิปสั้นๆ จาก animation ทดลองหรือ prototype mechanic แล้วโพสต์ตอน downtime ได้เลย สร้าง visibility ให้สตูดิโอโดยไม่เสียงบ.</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ShatterPointGS/status/2058986461362336194" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ShittyHaloTakes</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1462 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ShittyHaloTakes/status/2058831533427884447">View @ShittyHaloTakes on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I miss the E3 era because there would have been a fucking car lowered from the ceiling of LA Convention Center with an Unreal Engine 6 logo painted on it and that would have been so much more fun to m”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>คิดถึง E3 ยุคเก่าที่ทำ spectacle บ้าๆ มากกว่า เพราะอย่างน้อยก็สนุกกว่า metaverse hype ที่ยังไม่ยอมตาย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>คนยังชอบ marketing ที่ดูโง่แต่มีพลังงาน มากกว่า corporate messaging ที่ขัดเงาแต่ไม่มีจิตวิญญาณ — แม้จะเป็นแค่ hype</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Trailer และ XR demo ของ studio ควร lean เข้าหา spectacle และ personality มากกว่า safe presentation — bold ชนะ bland แม้งบน้อย</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ShittyHaloTakes/status/2058831533427884447" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@gembia2</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1225 · 💬 42</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/gembia2/status/2058888804719530434">View @gembia2 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“really hate how when you can tell how a game was made in godot because of how Bad the buttons system is and how Terrible the fonts look and how Abhorrent everything in general is”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Dev บ่นว่าเกมที่สร้างด้วย Godot สังเกตได้ทันที เพราะ default UI — ปุ่ม, font, และทุกอย่าง — ดูห่วยและไม่ได้ถูก customize เลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>1,225 likes บอกว่าคนเห็นด้วยเยอะ — default engine UI ทำให้เกมดูไม่น่าเล่นก่อนที่ผู้เล่นจะแตะ gameplay เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Unity team ต้องล็อค custom UI theme และ font ตั้งแต่เริ่ม project ทุกตัว อย่า ship ด้วย default เด็ดขาด — สร้าง UI kit กลางไว้ใน studio asset library</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/gembia2/status/2058888804719530434" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
