---
type: social-topic-report
date: '2026-06-04'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-04T03:23:19+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 43
salience: 0.5
sentiment: mixed
confidence: 0.68
tags:
- gamedev
- unity
- godot
- unreal
- ai-pipeline
- mobile-optimization
thumbnail: https://pbs.twimg.com/ext_tw_video_thumb/2061825229672882176/pu/img/osb_frpHWRsO-Lra.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-04

## TL;DR
- Godot รองรับการ build และ publish เกมบน Android หรืออุปกรณ์ XR ได้โดยตรง [1] และ Godot 4.7 beta 5 กำลังเตรียม Release Candidate [10]
- Unity เน้นวินัยการ production บนมือถือ: แนะนำให้จัดกลุ่ม Addressables ตามความต้องการ runtime แทนประเภท asset [7] พร้อม webinar วันที่ 4 มิถุนายน ว่าด้วย Addressables, optimization และ build size [33]
- State of Unreal keynote ของ Unreal คือวันที่ 17 มิถุนายน ที่ Chicago [12]; Fab June flash sale ลดสูงสุด 70% ถึงวันที่ 5 มิถุนายน [15]
- สัญญาณ AI-in-pipeline: tutorial จับคู่ Claude Code กับ Unity MCP เพื่อ prototype เกม 3D platformer [23]
- ธุรกิจ: PlayerUnknown Productions ปลดพนักงานและระงับ Go Wayback [36]; Team17 ตัดตำแหน่งฝ่าย marketing [37]; ยอดใช้จ่ายเกมในสหรัฐฯ ทะลุ $60B ในปี 2025 [38]; Mina the Hollower ขายได้ 300k copies ใน 3 วัน [39]

## สิ่งที่เกิดขึ้น
ข่าว engine นำวัน Godot ประกาศ build และ publish บนอุปกรณ์ Android/XR ได้เต็มรูปแบบ [1] พร้อมปล่อย 4.7 beta 5 ก่อน Release Candidate [10] Unity โฟกัสแนวปฏิบัติ mobile production — คู่มือจัดกลุ่ม Addressables ตาม runtime [7], session live ด้านการ optimize และ build size ร่วมกับทีม Big Farm Homestead [33] และ case study หลายชิ้น (Death Cult of Labor [27], Monster Walk fitness game [29]) — บวกกับ commerce play ที่ partner กับ Fetch Rewards เพื่อเชื่อม gameplay กับสัญญาณการซื้อที่ยืนยันแล้ว [21][35] Unreal โปรโมต keynote วันที่ 17 มิถุนายน [12], Fab sale [15] และ production story ของ NBA THE RUN บน UE5 [4] มี tutorial Claude Code + Unity MCP สำหรับการ prototype ปรากฏขึ้น [23]

## เหตุใดจึงสำคัญ
การสื่อสารของ engine vendor รอบนี้หมุนรอบประสิทธิภาพ production และการเข้าถึง ไม่ใช่ feature หลัก Unity กลับมาที่ Addressables และวินัยด้าน build size ซ้ำๆ [7][33] ซึ่งตรงกับข้อจำกัดด้านการส่งมอบบน mobile และ edutech โดยตรง เส้นทาง build บนอุปกรณ์/XR ของ Godot [1] ลดอุปสรรคด้านฮาร์ดแวร์สำหรับการทดลองและ prototype XR demo Claude Code + Unity MCP [23] เป็นหลักฐานรูปธรรมว่า LLM-driven prototyping ภายใน Unity กำลังเคลื่อนจากแนวคิดสู่ workflow ที่มีเอกสารจริง ฝั่งธุรกิจ สัญญาณปนกัน: ยอดใช้จ่ายผู้บริโภคที่แข็งแกร่ง ($60B [38]) และผลลัพธ์ indie ที่โดดเด่น (Mina the Hollower, 300k ใน 3 วัน [39]) อยู่คู่กับการหดตัวของสตูดิโอ (PlayerUnknown ระงับโปรเจกต์ [36], Team17 ตัด marketing [37], การลาออกของ senior Tekken [40]) และยอดขาย PlayStation first-party ที่ลดลง (58.4M FY20 เหลือ 28.9M FY24 [41]) รูปแบบ: การใช้จ่ายยังดีแต่กระจุกตัว และสตูดิโอกำลังตัด overhead — เงื่อนไขเหล่านี้เอื้อต่อทีมเล็กที่ ship แบบกระชับและมีกลุ่มเป้าหมายชัดเจน

## ความเป็นไปได้
น่าจะเกิด: Godot RC ตามมาหลัง beta 5 ไม่นาน [10] และ on-device build support [1] จะขยาย appeal ของ Godot สำหรับ XR/mobile น่าจะเกิด: keynote วันที่ 17 มิถุนายนของ Unreal [12] จะกำหนด roadmap ของ Epic (UEFN/Fab/engine) สำหรับรอบต่อไป — เป็น event ที่มีวันแน่นอนให้วางแผนได้ เป็นไปได้: workflow Unity ที่ใช้ LLM ผ่าน MCP [23] จะกลายเป็นขั้นตอน prototyping มาตรฐานสำหรับทีมเล็ก แม้ demo ยังอยู่ในช่วงต้นและยังไม่ใช่ pipeline production ที่พิสูจน์แล้ว เป็นไปได้: studio layoffs ต่อเนื่อง [36][37] จากตลาดที่ใช้จ่ายสูงแต่กระจุกตัว [38][41] ไม่มีแหล่งข้อมูลใดระบุตัวเลขความน่าจะเป็น จึงไม่มีการระบุ

## การนำไปใช้กับ NDF DEV
1) ทบทวน Unity Addressables strategy เทียบกับแนวทางการจัดกลุ่มตาม runtime [7] และเข้าร่วม/ดูย้อนหลัง webinar ด้าน optimization + build size [33] — เกี่ยวข้องโดยตรงกับขนาด app บน mobile และ edutech; effort ต่ำ 2) ทดลอง Claude Code + Unity MCP แบบจำกัดขอบเขตสำหรับการ prototype ตาม tutorial ที่เผยแพร่ [23]; effort กลาง — ถือเป็นการประเมิน ไม่ใช่ pipeline ที่ commit แล้ว 3) ดู State of Unreal keynote วันที่ 17 มิถุนายน [12] เพื่อติดตาม roadmap ที่ส่งผลต่องาน UE/XR; effort ต่ำ 4) สำหรับการทดลอง XR ทดสอบ on-device build path ของ Godot [1]; effort กลาง — มีประโยชน์เฉพาะเมื่อ Godot เป็น engine ที่พิจารณาอยู่ ข้ามได้: indie showcase และ asset-sale [2][3][6][8][9][11][13][14][16][17][18][19][20][22][24][25][26][28][30][31][32][34] ยกเว้นกรณีซื้อ asset เฉพาะเรื่อง; Unity–Fetch Rewards commerce partnership [21][35] เน้น US retail และไม่เกี่ยวกับงาน NDF DEV ปัจจุบัน

## สัญญาณที่ต้องติดตาม
- กำหนด Godot 4.7 Release Candidate หลัง beta 5 [10] และความพร้อมของ on-device/XR builds [1]
- State of Unreal keynote วันที่ 17 มิถุนายน สำหรับ roadmap ของ engine/UEFN/Fab [12]
- การนำ LLM + Unity MCP prototyping ไปใช้จริงเกินกว่า demo [23]
- studio layoffs ที่ต่อเนื่องเทียบกับยอดใช้จ่ายผู้บริโภคระดับ record — ความเสี่ยงจากการกระจุกตัวสำหรับทีมเล็ก [36][37][38][41]

## แหล่งข้อมูลดิบ
| platform | author | engagement | url |
|---|---|---|---|
| x | godotengine | ^1230 c27 | [No desktop? No problem. You can now build and publish #GodotEngine games entirel](https://x.com/godotengine/status/2061855408260563116) |
| x | ReBladeG | ^320 c13 | [Ever seen a frog fight with swords? 🐸⚔️ Got an outfit suggestion? Let us know in](https://x.com/ReBladeG/status/2061825270764417077) |
| x | PotentKnight | ^200 c3 | [Horror Survival Game Devlog. Have a great day✨ #horrorgame #indiegame #Unity #in](https://x.com/PotentKnight/status/2061969725048180798) |
| x | UnrealEngine | ^187 c8 | [With the help of Unreal Engine 5, Play by Play Studios were able to bring @NBATH](https://x.com/UnrealEngine/status/2062203103659839731) |
| x | UnrealEngine | ^166 c178 | [What game genre would you like to see a resurgence of? Or what genre would you l](https://x.com/UnrealEngine/status/2061870631634030861) |
| x | itchio | ^158 c1 | [Witherspring Wilds: Reincarnate into an open world of danger and opportunity. Fa](https://x.com/itchio/status/2062217749460398450) |
| x | unitygames | ^150 c3 | [Stop grouping your Unity Addressables by asset type! 🛑 For peak performance, org](https://x.com/unitygames/status/2061811029659570575) |
| x | ushadersbible | ^137 c1 | [Here's a WIP of our upcoming course, Real-Time Water in Unity: From Splashes to ](https://x.com/ushadersbible/status/2062327058324169202) |
| x | JussiKemppainen | ^136 c10 | [day593: new wetness shader feature for the vehicles. Supports soapy water and ge](https://x.com/JussiKemppainen/status/2061971294271238436) |
| x | godotengine | ^133 c4 | [That's strange… The amount of chickens we counted doesn't line up with the numbe](https://x.com/godotengine/status/2062298613712064579) |
| x | itchio | ^122 c0 | [The Power of Pride Bundle 2026 is now live on Itchio! All in support of 284 quee](https://x.com/itchio/status/2061810065934364900) |
| x | UnrealEngine | ^88 c6 | [2 weeks until we are live from Chicago's McCormick Place Convention Center for t](https://x.com/UnrealEngine/status/2062172776992268772) |
| x | TheMirzaBeig | ^87 c4 | [Good morning! AERO 1.3.0 is now live. The latest update adds height fog, texturi](https://x.com/TheMirzaBeig/status/2062140060540051685) |
| x | OzgursAssets | ^64 c1 | [Pickup (Truck) 1 (Driveable) - 30% off https://t.co/YvztZ1ndV2 Passenger Van (Dr](https://x.com/OzgursAssets/status/2062098392126263639) |
| x | UnrealEngine | ^57 c2 | [The @fab June Flash Sale is now on. Get up to 70% off thousands of assets until ](https://x.com/UnrealEngine/status/2061814683867500822) |
| x | gamefromscratch | ^54 c0 | [June FREE #gamedev round-up time! We have 3x #UnrealEngine assets + 1 #Unity3d a](https://x.com/gamefromscratch/status/2061811840028434733) |
| x | DAVFXArt | ^38 c0 | [Illugen swirly fire #vfx #realtimevfx #unity3d #illugen #gamedev https://t.co/Jt](https://x.com/DAVFXArt/status/2062199478048727343) |
| x | Darktree_Games | ^38 c2 | [Remnants of R'lyeh A One man team's Final Lovecraft Fantasy... Add to Your Wishl](https://x.com/Darktree_Games/status/2061950195307602164) |
| x | ushadersbible | ^38 c1 | [This outline technique is achieved using reflection. What's the difference? For ](https://x.com/ushadersbible/status/2061663479300296851) |
| x | the_mancojo | ^36 c0 | [I also included my symmetry system to install the asset. I'm so glad I thought o](https://x.com/the_mancojo/status/2061862567149002924) |
| x | unity | ^33 c2 | [Gaming is already one of the most powerful ways to reach consumers. Now, brands ](https://x.com/unity/status/2062172669429096825) |
| x | LazyDevNL | ^32 c8 | [My ultimate goal with this game is actually really simple: I just want at least ](https://x.com/LazyDevNL/status/2061938177183527017) |
| x | SunnyVStudio | ^31 c0 | [Learn how to use Claude Code and Unity MCP to rapidly prototype a 3D Platformer ](https://x.com/SunnyVStudio/status/2061879369950282060) |
| x | R2RGames | ^30 c2 | [Stress testing spline walls &amp; thick GPU grass for my "semi-cozy" builder. Is](https://x.com/R2RGames/status/2061805105998119262) |
| x | itchio | ^30 c0 | [OFFBEAT: Build the recording studio of your dreams! https://t.co/qWF5tjazOM by @](https://x.com/itchio/status/2061855366670176302) |
| x | itchio | ^29 c1 | [Traveloot: Run-based incremental game. Explore islands, gather resources, recrui](https://x.com/itchio/status/2062172452156015050) |
| x | unitygames | ^26 c2 | [Corporate anxiety turned into a blistering, hand-drawn FPS? 🎨💥 Discover how the ](https://x.com/unitygames/status/2062217971754262585) |
| x | itchio | ^26 c0 | [Kibble Cats: Click an ancient shrine. Hire cats. Revive a village. But the Pawbe](https://x.com/itchio/status/2062263052217831771) |
| x | unitygames | ^25 c1 | [Fitness meets gaming! 👟 Learn how Talofa Games used Unity to turn real-world ste](https://x.com/unitygames/status/2061855640897655130) |
| x | godotengine | ^25 c0 | [Featured game: GIRLBALLS https://t.co/1LoQWpH4GM](https://x.com/godotengine/status/2062298615846952963) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@godotengine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1230 · 💬 27</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/godotengine/status/2061855408260563116">View @godotengine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“No desktop? No problem. You can now build and publish #GodotEngine games entirely from your Android or XR device! https://t.co/NOOVdzwDMK”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Godot Engine รองรับการ build และ publish เกมทั้งหมดบน Android หรือ XR device แล้ว โดยไม่ต้องพึ่ง desktop</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>สำหรับทีม XR นี่หมายความว่า Godot รองรับ dev loop แบบ on-device ครบวงจรแล้ว build และ publish ได้จากใน headset โดยตรง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ลอง trial Godot pipeline ใหม่บน Android/XR device เป็น option ไม่ต้องพึ่ง desktop สำหรับ XR prototype เร็วๆ ควบคู่ Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/godotengine/status/2061855408260563116" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ReBladeG</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 320 · 💬 13</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ReBladeG/status/2061825270764417077">View @ReBladeG on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Ever seen a frog fight with swords? 🐸⚔️ Got an outfit suggestion? Let us know in the comments!! #cyberpunk #gamedev #indiedev #indiegame #ゲーム制作 #Unity3D https://t.co/IZozk9isI1”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev @ReBladeG โชว์คลิปตัวละคร Unity3D เป็นกบถือดาบ สไตล์ cyberpunk แล้วถามผู้ติดตามว่าอยากให้ใส่ชุดอะไร</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ReBladeG/status/2061825270764417077" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@PotentKnight</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 200 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/PotentKnight/status/2061969725048180798">View @PotentKnight on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Horror Survival Game Devlog. Have a great day✨ #horrorgame #indiegame #Unity #indiedev #gamedev https://t.co/7ecbjie9MC”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev โพสต์ devlog เกม horror survival บน Unity ใน X โดยไม่มีรายละเอียดเทคนิคหรือบทเรียนใดๆ มีแค่ link กับ hashtag</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/PotentKnight/status/2061969725048180798" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 187 · 💬 8</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2062203103659839731">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“With the help of Unreal Engine 5, Play by Play Studios were able to bring @NBATHERUN to life. After all, ball IS life🏀 We spoke with the team to learn how they used the EU toolset to help craft the fa”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Play by Play Studios เปิด case study การสร้าง NBA THE RUN เกม basketball 3v3 ด้วย Unreal Engine 5 พร้อมรายละเอียดการใช้ toolset</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>case study นี้เปิดรายละเอียด production จริง — animation, physics, และ networking ในเกม multiplayer fast-paced ที่ทีม game dev ใช้เปรียบเทียบแนวทางได้</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity อ่าน case study เพื่อดู animation blending และ multiplayer physics แล้วเทียบกับ approach ที่ใช้อยู่ใน Unity ปัจจุบัน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2062203103659839731" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@UnrealEngine</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 166 · 💬 178</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/UnrealEngine/status/2061870631634030861">View @UnrealEngine on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“What game genre would you like to see a resurgence of? Or what genre would you like to see have a golden age, if it hasn't yet? 🌅”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@UnrealEngine ถามชุมชนว่าอยากเห็น game genre ไหน comeback หรือมี golden age</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/UnrealEngine/status/2061870631634030861" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@itchio</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 158 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/itchio/status/2062217749460398450">View @itchio on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Witherspring Wilds: Reincarnate into an open world of danger and opportunity. Farm, build, tame, fight, craft, and explore https://t.co/sUUtrORHlb https://t.co/1JgQJ5FVtc”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>itch.io โปรโมต Witherspring Wilds เกม indie open-world ที่รวม farming, building, taming, crafting และ combat ไว้ด้วยกัน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/itchio/status/2062217749460398450" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@unitygames</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 150 · 💬 3</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/unitygames/status/2061811029659570575">View @unitygames on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Stop grouping your Unity Addressables by asset type! 🛑 For peak performance, organize your assets based on when they’re needed at runtime. In this quick tip, you’ll learn how to optimize your asset ma”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unity แนะนำให้จัด Addressables groups ตาม timing ที่ต้องใช้งาน runtime แทนการแยกตาม asset type เพื่อลด bundle loading ที่ไม่จำเป็น</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>แยก group ตาม type ทำให้โหลด asset เกินความจำเป็น แยกตาม load context ลด hitch ได้ตรงจุด</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ตรวจ Addressables group structure ใน Unity projects แล้วจัดใหม่ตาม load context (boot, per-level, UI) แทนการแยกตาม type</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/unitygames/status/2061811029659570575" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ushadersbible</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 137 · 💬 1</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ushadersbible/status/2062327058324169202">View @ushadersbible on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here's a WIP of our upcoming course, Real-Time Water in Unity: From Splashes to Oceans 🌊 More content is coming soon! Help us reach 2k wishlists ✨ https://t.co/5A4nXsEMJz #unity3d #gamedev https://t.c”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unity Shaders Bible กำลังทำคอร์ส real-time water ใน Unity ตั้งแต่ splash เล็กๆ จนถึง ocean ขนาดใหญ่ อยู่ในช่วงระดมคนกด wishlist ก่อน launch</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Water simulation เป็น visual requirement ที่เจอบ่อยใน Unity — คอร์สจาก shader expert ช่วยลดเวลา research ได้จริง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ให้ Unity team เพิ่มคอร์สนี้ใน learning backlog แล้วกด wishlist ไว้ติดตาม launch date</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ushadersbible/status/2062327058324169202" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
