---
type: social-topic-report
date: '2026-06-05'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-05T03:12:49+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 161
salience: 0.5
sentiment: neutral
confidence: 0.6
tags:
- game-dev
- godot
- unreal-engine
- unity
- tooling
- ai-pipeline
thumbnail: https://pbs.twimg.com/media/HJ_PpB3acAAfr1B.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-05

## TL;DR
- Microsoft เผยแพร่ 'XBOX Godot Sample' แบบ source-only บน GitHub เพื่อช่วยให้ build เกม Xbox บน PC ด้วย Godot และ GDK โดยระบุว่าเป็นส่วนหนึ่งของการเปิด developer ecosystem [1][2][28]
- Godot 4.7 beta 5 ออกแล้ว เตรียมขึ้น Release Candidate เร็วๆ นี้ [16]
- นักวิจัยปล่อย 'World' ซึ่งเป็น open-source UE5 simulator สำหรับฝึกและทดสอบ LLM/VLM agents ใน 3D รองรับ output ทั้ง RGB และ depth [39]
- มี free tools ใหม่สองตัว: AERO 1.3.0 volumetric fog สำหรับ Unity 6 URP (เพิ่ม height fog และ texturing) [44] และ Mesh2Motion เครื่องมือ animation 3D open-source สไตล์ Mixamo [24]
- Epic ประกาศ 'State of Unreal' วันที่ 17 มิถุนายน ที่ Chicago ครอบคลุม Unreal Engine และ UEFN [38]

## What happened
ข่าวด้าน platform ที่ชัดเจนที่สุดของวันคือ Microsoft เผยแพร่ XBOX Godot sample แบบ source-only สู่สาธารณะบน GitHub ใช้เป็นจุดเริ่มต้นสำหรับการสร้างเกม Xbox ผ่าน GDK โดย staff ของ Microsoft ระบุว่าเป็นส่วนหนึ่งของการเปิด developer ecosystem [1][2][28] ด้านเอนจิน Godot 4.7 beta 5 ออกก่อน Release Candidate [16] และ Epic ประกาศงาน State of Unreal วันที่ 17 มิถุนายน ที่ McCormick Place, Chicago [38] รายการ research/tooling ได้แก่ 'World' open-source UE5 simulator สำหรับ LLM/VLM agents รองรับ RGB และ depth [39], UE5 AutoLOD tool สำหรับ optimize assets 3D ที่ผลิตด้วย GenAI [25], Mesh2Motion เครื่องมือ animation open-source ฟรี [24] และ AERO 1.3.0 volumetric fog สำหรับ Unity 6 URP [44] รายการที่เหลือส่วนใหญ่เป็น indie WIP promo, shader/VFX clips [27][36][48][20] และ noise ที่ไม่เกี่ยวข้อง [7][11][13][15][59]

## Why it matters (reasoning)
XBOX Godot sample คือสัญญาณที่ควรจับตา: open-source engine ที่ได้รับการรองรับจาก first-party สำหรับ console ลดอุปสรรคในการ target console สำหรับ studio ขนาดเล็ก และลด lock-in กับ proprietary engine [1][2][28] ผลสืบเนื่องคือแรงกดดันต่อช่องว่างด้าน build tooling ระหว่าง Godot กับ Unity/Unreal สำหรับการ ship บน console อย่างไรก็ตาม 'source-only reference' หมายความว่างาน integration ยังตกอยู่ที่ developer แนวโน้ม AI-in-pipeline ที่กลับมาซ้ำ ทั้ง UE5 simulator สำหรับฝึก agents [39] และเครื่องมือสำหรับ clean up assets 3D จาก GenAI [25] สะท้อนว่า AI assets กลายเป็นความจริงในการผลิตที่ต้องการขั้นตอน optimization (LOD, retopo) ไม่ใช่ input ที่พร้อมใช้งาน ปริมาณ assets ของ Unity และ shader ที่ฟรีหรือราคาถูก [44][27][5] สะท้อนถึง asset ecosystem ที่แข็งแกร่ง แต่ก็สะท้อน commoditization ซึ่งเชื่อมโยงกับวาทกรรมที่ดำเนินอยู่เรื่อง 'Generic UE5 slop' และกระแส backlash ด้าน AI-attribution ต่อนักสร้าง [31]

## Possibility
**Likely:** Godot ยังคงได้รับการรองรับจาก first-party และ platform ต่อเนื่องจาก sample นี้ เนื่องจาก Microsoft ประกาศ open-ecosystem framing อย่างชัดเจน และ release cadence ของ 4.7 ยังคงต่อเนื่อง [1][2][16][28] **Plausible:** State of Unreal วันที่ 17 มิถุนายนอาจมีประกาศด้าน UEFN และ AI-pipeline ที่เปลี่ยนการตัดสินใจด้าน tooling — รอดูก่อนตัดสินใจ [38] **Plausible:** open agent simulators อย่าง 'World' [39] อาจกลายเป็นมาตรฐานเฉพาะกลุ่มสำหรับงานวิจัย embodied-AI แต่จะอยู่นอก game production ทั่วไป **Unlikely (จากหลักฐานวันนี้):** Godot sample เพียงอย่างเดียวจะทำให้ Godot กลายเป็น console path ในระยะใกล้สำหรับ studio ที่ใช้ Unity เป็นหลัก — มันคือ reference ไม่ใช่ pipeline สำเร็จรูป [1][28]

## Org applicability — NDF DEV
ทดลอง AERO 1.3.0 volumetric fog ฟรีในโปรเจกต์ Unity 6 URP ปัจจุบัน — effort ต่ำ ตรงกับงาน Unity ของ studio [44] ทดลอง Mesh2Motion เป็นตัวเลือก rigging/animation ฟรีทดแทน Mixamo สำหรับตัวละครใน edutech และเกม — effort ต่ำ [24] บุ๊กมาร์กคอร์ส Real-Time Water in Unity และ breakdown shader dissolve/VFX เป็น reference สำหรับการฝึก tech-art — effort ต่ำ [5][27][36] ใส่ State of Unreal (17 มิถุนายน) ไว้ในปฏิทินเพื่อดู update ด้าน UEFN และเอนจินที่เกี่ยวข้องกับงาน Unreal หรือ XR — effort ต่ำ [38] สำหรับ XR โดยเฉพาะ รับทราบการทดลอง Godot บน Apple Vision Pro เป็น data point แต่ให้ถือว่าเป็น early/experimental — effort ต่ำในการติดตาม [58] **ข้ามได้:** XBOX Godot sample เว้นแต่มี roadmap สำหรับ console shipping [1][2][28]; 'World' UE5 agent simulator [39] และ UE5 AutoLOD [25] ซึ่งออกนอกเส้นทาง Unity-first; และรายการ indie promo/off-topic ทั้งหมด

## Signals to Watch
- Microsoft open-ecosystem framing สำหรับ Godot — จับตาว่า tooling/docs จะก้าวข้าม source-only sample หรือไม่ [2][28]
- State of Unreal วันที่ 17 มิถุนายน สำหรับประกาศด้าน UEFN และ AI-pipeline [38]
- AI-asset cleanup tooling ที่กำลังเติบโต (AutoLOD สำหรับ GenAI meshes) บ่งชี้ว่า AI assets ต้องการ post-processing ในสาย production [25]
- กระแส backlash ของนักสร้างต่อ 'Generic UE5 slop' และ AI attribution — ปัจจัยด้านชื่อเสียงหากใช้ assets ที่ผลิตด้วย AI [31]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | XBOXGameDev | ^2002 c26 | [🌟 XBOX Godot Sample - now available as a public, source-only reference on @githu](https://x.com/XBOXGameDev/status/2062595972212068561) |
| x | jronald | ^1376 c40 | [We have work to do as we move to a more open developer ecosystem. Today we shipp](https://x.com/jronald/status/2062594763241791618) |
| x | Owl34Games | ^1347 c4 | [While you're playing v0.53, we're already working on the next update 👀 How are y](https://x.com/Owl34Games/status/2062524466144383381) |
| x | HedProtag | ^1031 c10 | [Steam page + First Trailer for my new game coming soon! STAY TUNED! #indiegame #](https://x.com/HedProtag/status/2062639599168704753) |
| x | ushadersbible | ^973 c5 | [Here's a WIP of our upcoming course, Real-Time Water in Unity: From Splashes to ](https://x.com/ushadersbible/status/2062327058324169202) |
| x | SeepProduction | ^792 c2 | [The first three weeks since the launch of Nightfall Empress have been amazing! 💜](https://x.com/SeepProduction/status/2062515125282537733) |
| x | jasonappleton | ^579 c84 | [I'm personally tired of the bots and trolls crashing out on Charles. The market ](https://x.com/jasonappleton/status/2062592937414853085) |
| x | mrkomps | ^487 c12 | [saw someone post an object avoidance system made in UE5, and I wanted to make it](https://x.com/mrkomps/status/2062542893014032448) |
| x | Aaron_Victor_ | ^486 c11 | [Crawling and stance switching WIP. There's still a lot of work to do. So far, yo](https://x.com/Aaron_Victor_/status/2062526169396977989) |
| x | 80Level | ^401 c1 | [.@ChoskerSanz has written a guide on implementing colored penumbra shadows in Un](https://x.com/80Level/status/2062504646019555636) |
| x | afcslxt | ^344 c2 | [Rice carried it through everyone and served it up. the engine on him is unreal h](https://x.com/afcslxt/status/2062444527558840751) |
| x | itchio | ^336 c2 | [Witherspring Wilds: Reincarnate into an open world of danger and opportunity. Fa](https://x.com/itchio/status/2062217749460398450) |
| x | AlligatorFiendz | ^296 c6 | [AT LEAST GODOT ACTUALLY DRINKS THE 17 CUPS OF COFEE THAT WILL MAKE HIM FIGHT FOR](https://x.com/AlligatorFiendz/status/2062544019763122276) |
| x | Ninjago9101 | ^295 c6 | [New Game Announced: Codename ZQPC/Host A sci-fi post-apocalyptic co-op PvE loote](https://x.com/Ninjago9101/status/2062629347861930319) |
| x | ShaykhSulaiman | ^293 c8 | [BREAKING: IRANIAN PRESIDENT PEZESHKIAN: "Preserving the unity, cohesion, and sol](https://x.com/ShaykhSulaiman/status/2062531160714932266) |
| x | godotengine | ^249 c7 | [That's strange… The amount of chickens we counted doesn't line up with the numbe](https://x.com/godotengine/status/2062298613712064579) |
| x | UnrealEngine | ^248 c4 | [Want to create games in Unreal Engine but not sure where to start? Our new begin](https://x.com/UnrealEngine/status/2062589020299985088) |
| x | UnrealEngine | ^226 c8 | [With the help of Unreal Engine 5, Play by Play Studios were able to bring @NBATH](https://x.com/UnrealEngine/status/2062203103659839731) |
| x | MoonlightPeaks | ^214 c4 | [channeling my inner peace 🧘‍♀️ a little wobble here and there is okay! take time](https://x.com/MoonlightPeaks/status/2062580263561879782) |
| x | Petcson | ^205 c4 | [Came up with a real simple way to make these flasks look like they have liquid! ](https://x.com/Petcson/status/2062663436618654148) |
| x | SpiritValeGame | ^204 c9 | [This solo dev is making an indie mmorpg that will launch Early Access on July 15](https://x.com/SpiritValeGame/status/2062515012887781581) |
| x | itchio | ^202 c1 | [Loving Decays [FULL GAME]: Love me, love me not. https://t.co/frLLeeF8qT by @lin](https://x.com/itchio/status/2062323451420114968) |
| x | progdruid | ^181 c5 | [my custom c++ game engine: edge-detected pixel-art-style post-processing shader ](https://x.com/progdruid/status/2062507655818531064) |
| x | gamefromscratch | ^177 c1 | [Mesh2Motion is an awesome, stupidly easy to use, FREE and open source 3D animati](https://x.com/gamefromscratch/status/2062553333907235124) |
| x | rms80 | ^176 c10 | [seen a few posts about optimizing GenAI 3D assets for game use so I figured I wo](https://x.com/rms80/status/2062615703207760203) |
| x | FiresquidGames | ^165 c69 | [We're delighted to officially host this week's #TurnBasedThursday! Dear #IndieDe](https://x.com/FiresquidGames/status/2062489910041284621) |
| x | VFX_Therapy | ^151 c0 | [Dissolve Shader = Interactive edge glow + world space control. Perfect for enemy](https://x.com/VFX_Therapy/status/2062607977186738307) |
| x | scottvanvliet | ^149 c9 | [Come build for XBOX WITH Godot.](https://x.com/scottvanvliet/status/2062617760329535903) |
| x | valigo | ^149 c27 | [Epic has everything to become a real Steam competitor. Their issue is that Epic ](https://x.com/valigo/status/2062583157137056235) |
| x | 80Level | ^139 c0 | [.@ArthurTasquin has released a comprehensive tutorial on physically based lighti](https://x.com/80Level/status/2062534847076126834) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@XBOXGameDev</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2002 · 💬 26</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/XBOXGameDev/status/2062595972212068561">View @XBOXGameDev on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🌟 XBOX Godot Sample - now available as a public, source-only reference on @github We’re making it easier to build for XBOX on PC with @godotengine. Check out our new sample that helps you integrate Mi”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Xbox Game Dev ปล่อย sample บน GitHub สาธารณะ แสดงวิธี integrate Microsoft GDK, Xbox Services, และ PlayFab เข้ากับ Godot Engine สำหรับ build บน PC/Xbox</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Xbox รองรับ Godot อย่างเป็นทางการด้วย GDK + PlayFab module สำเร็จรูป ทำให้ publish ไปยัง Xbox/PC มี path ที่ชัดเจนและ support แล้ว ไม่ต้อง integrate เอง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ถ้าทีมประเมิน Godot สำหรับ PC title ที่เล็ง Xbox ดู sample นี้ก่อนเขียน platform integration เอง</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/XBOXGameDev/status/2062595972212068561" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jronald</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1376 · 💬 40</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jronald/status/2062594763241791618">View @jronald on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“We have work to do as we move to a more open developer ecosystem. Today we shipped an XBOX Godot sample to GitHub, giving developers a simple starting point for building games with the GDK and other t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Microsoft ปล่อย Xbox Godot sample บน GitHub สำหรับนักพัฒนาที่ต้องการสร้างเกมด้วย GDK และ Xbox title services — เป็นก้าวแรกของ open-engine support บน Xbox อย่างเป็นทางการ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Xbox รองรับ Godot ด้วย GDK อย่างเป็นทางการแล้ว ทำให้ Godot เป็นตัวเลือก engine ที่น่าเชื่อถือสำหรับ Xbox publishing ไม่แพ้ Unity</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ดู Xbox Godot GDK sample เพื่อประเมิน effort ถ้าโปรเจกต์ Xbox ในอนาคตจะใช้ Godot แทน Unity</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jronald/status/2062594763241791618" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Owl34Games</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1347 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Owl34Games/status/2062524466144383381">View @Owl34Games on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“While you're playing v0.53, we're already working on the next update 👀 How are you enjoying the update so far? What's your favorite part? 🙂 #gamedev #indiedev #visualnovel #adultgame https://t.co/NhzL”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนา indie @Owl34Games โพสต์ถามผู้เล่นว่าชอบ update v0.53 แค่ไหน ไม่มีข้อมูลเชิงเทคนิคใดเลย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/Owl34Games/status/2062524466144383381" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@HedProtag</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1031 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/HedProtag/status/2062639599168704753">View @HedProtag on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Steam page + First Trailer for my new game coming soon! STAY TUNED! #indiegame #indiedev”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@HedProtag ประกาศว่าจะปล่อย Steam page และ trailer แรกของเกมใหม่เร็วๆ นี้ ยังไม่มีรายละเอียดเรื่อง genre หรือ engine</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/HedProtag/status/2062639599168704753" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ushadersbible</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 973 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ushadersbible/status/2062327058324169202">View @ushadersbible on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Here's a WIP of our upcoming course, Real-Time Water in Unity: From Splashes to Oceans 🌊 More content is coming soon! Help us reach 2k wishlists ✨ https://t.co/5A4nXsEMJz #unity3d #gamedev https://t.c”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Unity Shaders Bible เตรียมออก course real-time water rendering ใน Unity ครอบคลุมตั้งแต่ splashes ถึง ocean-scale กำลัง wishlist ก่อน launch</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Water rendering เป็นจุดอ่อนที่เจอบ่อยใน Unity projects — course ที่เน้น shader โดยตรงช่วยลดเวลา research ได้มาก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ให้ Unity team wishlist course นี้ไว้ก่อน เพื่อรับ launch pricing ตอน release</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ushadersbible/status/2062327058324169202" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@SeepProduction</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 792 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/SeepProduction/status/2062515125282537733">View @SeepProduction on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“The first three weeks since the launch of Nightfall Empress have been amazing! 💜 A huge thank you to everyone for your incredible support! 🙏✨ If you'd like to join the Twilight, you can find the game ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Studio Seep Production โพสต์ขอบคุณแฟนๆ หลัง launch Nightfall Empress บน Steam ครบ 3 สัปดาห์ ไม่มีตัวเลขยอดขายหรือ data ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/SeepProduction/status/2062515125282537733" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@jasonappleton</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 579 · 💬 84</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/jasonappleton/status/2062592937414853085">View @jasonappleton on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I'm personally tired of the bots and trolls crashing out on Charles. The market has been getting manipulated down for the past year. &quot;They&quot; want a reset before Clarity. It's the banks, institutions an”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักลงทุน Cardano โต้ว่าราคา ADA ร่วงเพราะ institution จงใจกดราคาก่อน upgrade 'Clarity' ไม่ใช่เพราะโปรเจกต์ล้มเหลว</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/jasonappleton/status/2062592937414853085" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@mrkomps</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 487 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/mrkomps/status/2062542893014032448">View @mrkomps on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“saw someone post an object avoidance system made in UE5, and I wanted to make it in roblox cuz im unoriginal asf https://t.co/xJsfNdF6tU”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักพัฒนาคนหนึ่ง port ระบบ object avoidance จาก Unreal Engine 5 มาทำใหม่ใน Roblox พร้อมแชร์ video demo</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>พฤติกรรม avoidance แบบนี้ใช้ได้ข้ามเครื่องยนต์ — concept เดียวกันนำมาใช้กับ Unity AI/navigation ได้เลย</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ดู video เป็น reference พฤติกรรมตอนทำหรือ review object avoidance ใน Unity NavMesh หรือ custom steering</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/mrkomps/status/2062542893014032448" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
