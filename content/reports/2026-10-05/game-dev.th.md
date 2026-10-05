---
type: social-topic-report
date: '2026-10-05'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-10-05T03:08:12+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 134
salience: 0.45
sentiment: neutral
confidence: 0.6
tags:
- unreal-engine
- unity
- godot
- indie-tools
- runescape
- mobile-games
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2106481097404284928/img/KwQjONA25d9fRY4z.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-10-05

## TL;DR
- Jagex ประกาศ RS4 เป็น RuneScape MMORPG ภาคใหม่ที่สร้างด้วย Unreal Engine ฉากอยู่ใน Gielinor ตอนนี้อยู่ช่วงพัฒนาระยะแรก เริ่มต้นที่ Ashenfall และถูกบอกว่า "อีกไม่กี่ปี" กว่าจะเปิดตัว [2][7][14][42] มีแหล่งหนึ่งระบุว่าเริ่มจากการเป็น expansion ของ Dragonwilds [4]
- Unreal Engine 5 ได้รับความสนใจมากที่สุดในหมวด engine: ผู้เล่นชมภาพของ Gears of War: E-Day early access และ Ace Combat 8 (Xbox Series X, Performance Mode) [20][36][54] บางโพสต์วิจารณ์ว่า cutscene มีลุค "Unreal lighting" แบบซ้ำๆ [12] และเกม UE ต้องจูนเป็นรายเกม [59]
- มี tool ขนาดเล็กออกใหม่หลายตัว: hun0fx Pixel Art VFX Generator (demo ฟรี ลด 25% ช่วงเปิดตัว) [6], Crocotile 3D v2.7.4 [28], RPG Paper Maker 3.2.14 [52], Character Sprite Sheet Creator v1.0 [35] และ Amplify Decals สำหรับ Unity ที่ประกาศว่าจะขึ้น Asset Store [51]
- สตูดิโอหนึ่งปล่อยเกมมือถือ 'Ninety-Nine' โดยไม่ใช้ game engine ใช้ React Native, Expo, Skia และ Reanimated [55]
- แทบไม่มีสัญญาณเรื่อง AI ใน game pipeline มีโพสต์เดียวอ้างว่าสร้าง pipeline จาก Street View ไปเป็น scene ใน Unreal ด้วย Sol 6.1, Opus 5.5 และ Qwen2.5-image โดยไม่มีรายละเอียดทางเทคนิค [46]

## What happened
ข่าวจริงที่ใหญ่ที่สุดคือ Jagex ประกาศ RS4 RuneScape MMO เจนเนอเรชันที่ 4 ที่สร้างด้วย Unreal Engine เกมอยู่ในไทม์ไลน์หลัง Dragonwilds เริ่มที่ Ashenfall ในยุค Sixth Age และ Jagex บอกว่ายังห่างจากวันวางจำหน่ายอีกหลายปี [2][4][7][14][29][42] หลายโพสต์เป็นปฏิกิริยาของผู้เล่นต่อภาพในเกม UE5 ที่วางขายหรืออยู่ใน early access ได้แก่ Gears of War: E-Day [36][39][54], Ace Combat 8 บน Series X [20] และงาน tribute ของแฟนเกม Sega Rally [18] โพสต์กลุ่มเล็กกว่าวิจารณ์ลุคและ performance ของ UE [12][59]

ส่วนที่เหลือเป็นเรื่อง tooling และงาน indie: pixel-art VFX generator [6], อัปเดต Crocotile 3D [28], ฟีเจอร์ของ RPG Paper Maker [52], sprite sheet creator [35], decal tool สำหรับ Unity ที่กำลังจะออก [51], หนังสือเรื่อง shader ของ Godot [40] และ breakdown VFX แบบ procedural ใน Unity [21] Fortnite asset-porting fork ตัวหนึ่งแปลง material graph ของ Unreal เป็น node graph ใน Blender แทนการใช้ shader สำเร็จรูป [26] มีโพสต์หนึ่งแย้งว่า s&box ('game creation platform') ไม่มีกลุ่มเป้าหมายชัดเจน เพราะ developer มี Godot, Unreal และ Unity อยู่แล้ว [8] โพสต์ engagement สูงจำนวนมากเป็น noise นอกหัวข้อที่ติดมาเพราะคำว่า 'unreal' หรือ 'Godot' [1][5][9][24][32][33][34]

## Why it matters (reasoning)
RS4 เสริมแพตเทิร์นที่สตูดิโอ live-service รายใหญ่ย้าย IP อายุยาวมาใช้ Unreal [2][7] เกมยังอีกหลายปี จึงไม่กระทบระยะใกล้ แต่สนับสนุนมุมมองว่า Unreal คือตัวเลือกเริ่มต้นสำหรับโปรเจกต์ fidelity สูง เสียงวิจารณ์ลุค "UE lighting" ที่ซ้ำกัน [12] และงานจูนรายเกม [59] คืออีกด้านของการเป็นตัวเลือกเริ่มต้น คือลุคแบบ out-of-the-box ของ engine เริ่มถูกจำได้ และ art direction คือสิ่งที่ทำให้เกมโดดเด่น สำหรับสตูดิโอเล็ก หลักฐานที่เกี่ยวข้องกว่าคือ tool ราคาถูกเฉพาะทางที่ออกมาสม่ำเสมอ ทั้งด้าน pixel art, decal, sprite และการทำโมเดล voxel/tile [6][28][35][51] tool เหล่านี้ลดเวลาผลิต asset โดยไม่ต้องเปลี่ยน engine เกม React Native/Skia ที่ไม่ใช้ engine [55] ชี้ว่าเกมมือถือ 2D แบบเรียบง่ายสร้างบน web/mobile stack ได้ ซึ่งสำคัญกับทีมที่ ship แอป React Native อยู่แล้ว ส่วนข้ออ้างเรื่อง AI pipeline [46] เป็นเพียงเรื่องเล่า ไม่ควรใช้ตัดสินใจ

## Possibility
น่าจะเกิด: ข้อมูลเพิ่มเติมเกี่ยวกับ Jagex และ RS4 ในอีกไม่กี่เดือนข้างหน้า เพราะเกมประกาศแล้วแต่ยังอยู่ช่วงต้น [7][42] น่าจะเกิด: เสียงชมและเสียงวิจารณ์ performance ของ UE5 ต่อเนื่อง เมื่อ Gears of War: E-Day วางจำหน่ายเต็มรูปแบบ [36][59] เป็นไปได้: สตูดิโอเล็กมากขึ้น ship เกมมือถือ 2D แบบเรียบง่ายด้วย React Native + Skia แทน Unity แต่ตอนนี้มี data point เดียว [55] ไม่น่าเกิด: s&box ขยายกลุ่มผู้ใช้ได้เร็วๆ นี้ บทวิจารณ์ [8] สะท้อนความสงสัย แต่โพสต์เดียวเป็นหลักฐานอ่อน ยังไม่ชัด: pipeline สร้าง environment ด้วย AI อย่าง [46] พร้อมใช้งานจริงหรือไม่ เพราะไม่มีรายละเอียดทางเทคนิค

## Org applicability — NDF DEV
1) ประเมิน Amplify Decals เมื่อขึ้น Asset Store สำหรับ environment Unity XR และ edutech ที่ต้องการ decal ขอบหรือแถบบนพื้นผิวไม่เรียบ (effort ต่ำ) [51] 2) สำหรับ mini-game edutech แบบ 2D หรือ pixel-style ลอง demo ของ hun0fx VFX generator และ Character Sprite Sheet Creator ก่อนจ้างทำ art เฉพาะ (ต่ำ) [6][35] 3) สำหรับเกมมือถือ edutech แบบเรียบง่ายที่ทีมship React Native อยู่แล้ว ลอง prototype หนึ่งเกมด้วย Expo + Skia + Reanimated แล้วเทียบขนาดแอปและความเร็วในการ iterate กับ Unity (กลาง) [55] 4) สำหรับ technical art ใน Unity อ่าน breakdown VFX Eldritch Blast แบบ procedural เป็น shader reference (ต่ำ) [21] ข้าม: ข่าว RS4 (ไม่มีผลที่ลงมือทำได้) [2], s&box [8], ข้ออ้าง AI Street View-to-Unreal จนกว่าจะมีรายละเอียดที่ทำซ้ำได้ [46] และ thread ชมภาพ UE5 [20][36]

## Signals to Watch
- อัปเดตการพัฒนา RS4 และคำแถลงของ Jagex เรื่อง Unreal tooling หรือเวอร์ชัน engine [7][42]
- วันเปิดตัวและราคาของ Amplify Decals บน Asset Store [51]
- เกมมือถือที่ไม่ใช้ engine บน React Native/Skia เพิ่มเติม [55]
- tool ที่แปลง material graph ของ Unreal เป็น Blender ในฐานะเส้นทาง asset interop [26]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | SpicyCurty | ^22254 c93 | [Okay but imagine if this scene was made in unreal engine and the camera was over](https://x.com/SpicyCurty/status/2106730096937603270) |
| x | Wario64 | ^6675 c123 | [4th RuneScape MMO in development, built in Unreal Engine and set in the world of](https://x.com/Wario64/status/2106481517598052357) |
| x | syni_bread | ^3117 c12 | [Godot as a new freebie sticker You don’t get to choose your freebie I just vibe ](https://x.com/syni_bread/status/2106501542312636696) |
| x | JayOddity | ^2581 c61 | [RuneScape 4 Has Been Announced - It Was Originally A Dragonwilds Expansion - Pos](https://x.com/JayOddity/status/2106515896969863562) |
| x | TeamCRonaldo | ^2155 c71 | [It's funny how fast the tone changes when real pressure hits... Something clearl](https://x.com/TeamCRonaldo/status/2106629006283993535) |
| x | hun0fx | ^1795 c28 | [I just released my first tool: hun0fx Pixel Art VFX Generator Hope it helps for ](https://x.com/hun0fx/status/2106586854342676712) |
| x | Pirat_Nation | ^1711 c45 | [Jagex has officially announced RS4, a new RuneScape MMORPG that aims to start a ](https://x.com/Pirat_Nation/status/2106490758983229585) |
| x | Rivo9_ | ^1062 c57 | [S&box is a solution in need of a problem -Players don't want a "game creation pl](https://x.com/Rivo9_/status/2106607219626434794) |
| x | GodotIsW8ing4U | ^1011 c7 | [@KenFarmer @ReviewsPossum In just the past few months we have not only learned t](https://x.com/GodotIsW8ing4U/status/2106506934132298075) |
| x | Nanju_Bami | ^937 c5 | [dialog test #unity3d #FPS #indiedev #gamedev #unity #ゲーム制作 https://t.co/5Kr2CFFW](https://x.com/Nanju_Bami/status/2106478273496776744) |
| x | worblir | ^609 c10 | [Paper Jerma tracks down the JWF wrestling superstar, the Glue Man, at the dodgy ](https://x.com/worblir/status/2106816164156624943) |
| x | droolvana | ^524 c13 | [These 3d rendered cutscenes have the most stereotypical unreal engine lighting e](https://x.com/droolvana/status/2106817291031564352) |
| x | ewoera | ^505 c1 | [Meet our new centaur, Calista!🐎❤️ #furry #VR #centaur #gamedev #indiedev #vrgame](https://x.com/ewoera/status/2106782723897544763) |
| x | Ninjago9101 | ^502 c16 | [RS4 – A New RuneScape MMO announced A new 4th-generation RuneScape MMORPG built ](https://x.com/Ninjago9101/status/2106500806363230472) |
| x | indieforgames | ^396 c7 | [When an animator gets bored, make a crow breakdance in Blender. 🐦🕺 Character ani](https://x.com/indieforgames/status/2106708930403475867) |
| x | Jyunaut | ^342 c6 | [Revamped some heavy attack animations. #gamedev #indiegame #unity https://t.co/d](https://x.com/Jyunaut/status/2106743734947958798) |
| x | ProjectAliveDev | ^338 c9 | [Attack helicopters are now units you can command in Ebbtide. Meet the Apache and](https://x.com/ProjectAliveDev/status/2106796377284231402) |
| x | GamewithDave | ^330 c12 | [Sega Rally fans need to see this. Over Jump Rally is an unofficial tribute to th](https://x.com/GamewithDave/status/2106821675522089203) |
| x | lowpolylover | ^310 c7 | [First things first: deal with the ranged guy. Map update • Enemy range • Low clo](https://x.com/lowpolylover/status/2106742397204115836) |
| x | JamieMoranUK | ^300 c5 | [This is my actual in game footage of Ace Combat 8 (Mission Replay) It’s literall](https://x.com/JamieMoranUK/status/2106572212832456746) |
| x | jettelly | ^295 c0 | [Ryan Gee made this stylized take on Eldritch Blast in Unity! The eyes inside the](https://x.com/jettelly/status/2106398881693012244) |
| x | GarrettSavo | ^271 c0 | [Trying to bring back mystery to games Wishlist on Steam -> https://t.co/ULaGMhXZ](https://x.com/GarrettSavo/status/2106569551676621298) |
| x | BorgesDev | ^270 c14 | [Just kidding :) #MinecraftGodot #Minecraft #Godot #Fangame https://t.co/Gg20gFaT](https://x.com/BorgesDev/status/2106818188772102630) |
| x | goth600 | ^241 c44 | [unreal engine, hyper realistic, Minecraft, photorealistic, reflections, The Lege](https://x.com/goth600/status/2106822881376415965) |
| x | SpicyCurty | ^223 c0 | [@SH3Enjoyer Unfortunately this wouldn’t solve the unreal engine issue…](https://x.com/SpicyCurty/status/2106809389596258803) |
| x | psdkyo | ^192 c19 | [For the past few days i've been working on a Fortnite Porting Fork that translat](https://x.com/psdkyo/status/2106489569747071212) |
| x | RealCashEnt | ^187 c23 | [Blade Royal is back and Reborn. Jump, guard, and strike through 3D worlds in **B](https://x.com/RealCashEnt/status/2106542295789277440) |
| x | Crocotile3D | ^158 c0 | [New version of Crocotile 3d (v2.7.4) is released! Various bug fixes and qol impr](https://x.com/Crocotile3D/status/2106823613584224547) |
| x | RinoTheBouncer | ^155 c3 | [RuneScape 4 is officially in development🚀 ✅Aims to bring the MMO world of Gielin](https://x.com/RinoTheBouncer/status/2106497938432110688) |
| x | cagyjan1 | ^150 c23 | [Still extremely bullish on @staratlas. The foundation they’ve built is insane. A](https://x.com/cagyjan1/status/2106599965082436051) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SpicyCurty</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 22254 · 💬 93</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SpicyCurty/status/2106730096937603270">View @SpicyCurty on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Okay but imagine if this scene was made in unreal engine and the camera was over her shoulder”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ไวรัลบน X ที่จินตนาการว่าฉากหนึ่งถูกทำใน Unreal Engine ด้วยกล้องมุมข้ามไหล่ เป็นแค่ fan 'what if' ไม่มีเครื่องมือ รีลีส หรือเทคนิคจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SpicyCurty/status/2106730096937603270" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Wario64</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 6675 · 💬 123</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Wario64/status/2106481517598052357">View @Wario64 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“4th RuneScape MMO in development, built in Unreal Engine and set in the world of Gielinor Releasing &quot;a few years away&quot; https://t.co/1pTZEoDTo7 https://t.co/K6nDFH7lyp”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Wario64 รายงานว่า MMO ภาคที่ 4 ของ RuneScape กำลังพัฒนาด้วย Unreal Engine ฉากอยู่ในโลก Gielinor และจะวางจำหน่ายอีก &quot;อีกไม่กี่ปี&quot;</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แฟรนไชส์ MMO ที่ทำมานานซึ่งเคยใช้เทคโนโลยีของตัวเอง ย้ายเกมถัดไปมาใช้ Unreal Engine เป็นข้อมูลอ้างอิงเรื่องการเลือก engine สำหรับเกมออนไลน์ขนาดใหญ่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Wario64/status/2106481517598052357" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@syni_bread</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 3117 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/syni_bread/status/2106501542312636696">View @syni_bread on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Godot as a new freebie sticker You don’t get to choose your freebie I just vibe check you https://t.co/z7nn4ZUfm1”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์บน X ที่มียอดไลก์กว่า 3,100 โชว์โลโก้ Godot เป็นสติกเกอร์แจกฟรี พร้อมมุกว่าผู้รับเลือกเองไม่ได้ ต้องรับสติกเกอร์ตามที่ได้</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป็นมีมจากชุมชน ไม่มีการปล่อยเวอร์ชัน เครื่องมือ หรือเทคนิคใหม่ แต่ยอดไลก์สะท้อนฐานแฟนของ Godot ที่ยังคึกคัก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/syni_bread/status/2106501542312636696" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@JayOddity</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2581 · 💬 61</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/JayOddity/status/2106515896969863562">View @JayOddity on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“RuneScape 4 Has Been Announced - It Was Originally A Dragonwilds Expansion - Possibly Action Combat (based on the above) - Unreal Engine - Set In Gielinor, Starts In Ashenfall - Set After Dragonwilds ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>มีการประกาศ RuneScape 4 เป็น MMO บน Unreal Engine ฉากในโลก Gielinor เริ่มที่ Ashenfall ต่อจากเหตุการณ์ใน Dragonwilds โดยเดิมเป็นภาคเสริมของ Dragonwilds และอาจใช้ action combat</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แฟรนไชส์ MMO ที่ดำเนินมานานย้ายมาใช้ Unreal Engine และอาจใช้ action combat แสดงว่าภาคเสริมของเกมแยกสามารถขยายเป็นภาคต่อเต็มตัวได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/JayOddity/status/2106515896969863562" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@TeamCRonaldo</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2155 · 💬 71</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TeamCRonaldo/status/2106629006283993535">View @TeamCRonaldo on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It's funny how fast the tone changes when real pressure hits... Something clearly changed suddenly ​All week, Jorge Jesus was acting tough in press conferences. Bragging to journalists that “I can pro”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>บัญชีแฟนบอลอ้างว่า Jorge Jesus โค้ชทีมชาติโปรตุเกสลดท่าทีแข็งกร้าวเรื่องการนั่งสำรอง Ronaldo หลัง Bruno Fernandes ออกมาสนับสนุน Ronaldo ต่อสาธารณะ และ Joao Felix ลบรูปที่ถ่ายกับโค้ช</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TeamCRonaldo/status/2106629006283993535" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@hun0fx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1795 · 💬 28</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/hun0fx/status/2106586854342676712">View @hun0fx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I just released my first tool: hun0fx Pixel Art VFX Generator Hope it helps for your games! It's on https://t.co/bzbSH3k86f with a free demo, 25% off for the first two weeks: https://t.co/b1XVd33T1e #”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาอินดี้ @hun0fx เปิดตัว Pixel Art VFX Generator ซึ่งเป็นเครื่องมือชิ้นแรก มีเดโมให้ลองฟรีและลดราคา 25% ในสองสัปดาห์แรก</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>โปรเจกต์ pixel art มักต้องใช้เอฟเฟกต์วาดมือจำนวนมาก เช่น ระเบิดและแรงกระแทก เครื่องมือที่มีเดโมฟรีช่วยลดเวลางานอาร์ตได้โดยไม่เสียต้นทุน</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าสตูดิโอมีโปรเจกต์ pixel art ให้ลองเดโมฟรีกับเอฟเฟกต์หนึ่งชิ้น แล้วเทียบคุณภาพและเวลากับ VFX ที่วาดเอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/hun0fx/status/2106586854342676712" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Pirat_Nation</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1711 · 💬 45</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Pirat_Nation/status/2106490758983229585">View @Pirat_Nation on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Jagex has officially announced RS4, a new RuneScape MMORPG that aims to start a new era for the series. &gt;New MMORPG: RS4 is being built as an entirely new RuneScape game, rather than an update to the ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Jagex ประกาศ RS4 เกม RuneScape MMORPG ภาคใหม่ที่สร้างใหม่ทั้งหมดด้วย Unreal Engine โดยเริ่มจากพื้นที่ Ashenfall ใน RuneScape: Dragonwilds ยังอีกหลายปีกว่าจะเปิดตัวและยังไม่มีวันวางจำหน่าย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สตูดิโอ MMO ที่ทำเกมมานานย้ายแฟรนไชส์หลักไปใช้ Unreal Engine โดยยังดูแลเกมเดิมต่อ เป็นข้อมูลอ้างอิงเรื่องการเลือก engine สำหรับเกมออนไลน์ขนาดใหญ่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Pirat_Nation/status/2106490758983229585" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Rivo9_</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1062 · 💬 57</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Rivo9_/status/2106607219626434794">View @Rivo9_ on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“S&amp;box is a solution in need of a problem -Players don't want a &quot;game creation platform&quot; they want a game. -Devs can either use godot, unreal, unity, zdoom, adventure game studio, and mod hundreds of g”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์บน X วิจารณ์ว่า S&amp;box ซึ่งเป็นแพลตฟอร์มสร้างเกม ไม่มีกลุ่มเป้าหมายชัดเจน เพราะผู้เล่นอยากได้เกมสำเร็จรูป ส่วน dev มี Godot, Unreal, Unity และการม็อดอยู่แล้ว แทนที่จะจ่าย $10 เข้า walled garden</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เป็นความเห็นเดียว แต่ชี้คำถามที่แพลตฟอร์มสร้างเกมใหม่ต้องตอบ: ทำไม dev หรือผู้เล่นต้องย้ายจาก engine และชุมชนม็อดที่ใช้อยู่แล้ว</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Rivo9_/status/2106607219626434794" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
