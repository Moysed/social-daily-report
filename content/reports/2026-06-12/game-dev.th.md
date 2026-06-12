---
type: social-topic-report
date: '2026-06-12'
topic: game-dev
lang: th
pair: game-dev.en.md
generated_at: '2026-06-12T03:13:59+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- rss
- x
regions:
- global
post_count: 174
salience: 0.6
sentiment: mixed
confidence: 0.55
tags:
- unreal-engine-5
- godot
- unity
- ai-in-gamedev
- xr-vr
- performance
thumbnail: https://pbs.twimg.com/amplify_video_thumb/2065109409844334592/img/OxNFlG_QeTBaXhVj.jpg
translated_by: claude-sonnet-4-6
---

# Game Dev — 2026-06-12

## TL;DR
- UE5 ครองสัญญาณ game-dev วันนี้ ประเด็นหลักคือ performance backlash — Halo: Campaign Evolved (UE5 remake, วางจำหน่าย 28 ก.ค. 2026 [9][13]) รายงานว่า RTX 5090 แทบไม่ทะลุ 100 FPS ที่ 1440p ultra [58] และมีเสียงบ่นว่า UE5 titles render ภายในที่ ~540p เพื่อให้ได้ '1080p' 60fps ผ่าน upscaling [17]
- Epic's State of Unreal (17 มิ.ย. ที่ Chicago) ตั้งธงชัดเรื่อง optimization ทั่ว Epic tools [44] — ตอบรับคำวิจารณ์ด้าน performance โดยตรง
- Generative AI เข้าสู่ production AAA จริงแล้ว: Tomb Raider: Legacy of Atlantis (UE5 remake) ยืนยันการใช้ gen-AI ใน Game Informer interview [3][21][47]; Carmack เสนอแนวคิด LLMs ปรับโครงสร้างโค้ดให้ weaker model ทำงานต่อได้ [6]
- Godot 4.7 Release Candidate 2 ออกแล้ว รอรายงาน regression ก่อน stable [25]
- tooling ฝั่ง XR/mobile: UnRealityKit เชื่อม UE5 กับ Apple Vision Pro RealityKit รองรับ eye tracking, gestures, room lighting [49]; Arm demo Android upscaler แบบ DLSS พร้อมเกม UE5 MegaLights จาก Sumo Digital [26]

## What happened
Unreal Engine 5 คือจุดศูนย์กลางของวัน Halo: Campaign Evolved ซึ่งเป็น UE5 remake กำหนดวันออก 28 ก.ค. 2026 [9][13] แต่มีรายงานว่า RTX 5090 ผ่าน 100 FPS ที่ 1440p ultra แทบไม่ได้ [58] เป็นเชื้อให้เสียงร้องเรียนกว้างขึ้นว่า UE5 games วิ่งที่ internal resolution ~540p เพื่อบรรลุ '1080p' 60fps หลัง upscaling [17] Clutch เกมแข่งรถจากอดีต developers Forza Horizon ใช้ UE5 กับ custom physics layer สำหรับ tire temperature, grip และ suspension ใน open world จำลองทางใต้ของฝรั่งเศสและ Monaco แบบ 1:1 [5][10][35] Tomb Raider: Legacy of Atlantis (UE5 remake) ยืนยันการใช้ generative AI ผ่าน Game Informer interview กับ experience director [3][21][47] State of Unreal ของ Epic วันที่ 17 มิ.ย. ตั้งธงเรื่อง optimization ทั่ว Epic tools [44]

## Why it matters (reasoning)
ธีมซ้ำๆ คือช่องว่างระหว่าง fidelity กับ performance ของ UE5 [17][58] หนักพอที่ Epic ต้องนำ optimization ขึ้นหน้าในงาน showcase ของตัวเอง [44] นั่นยืนยันว่าต้องระวัง: เปิด UE5 features เต็มทุกตัวโดย default คือกับดักที่รู้จักกันดี และแนวคิดเรื่อง resolution/feature budgeting ใช้ได้กับทุก engine เช่นกัน on-device upscaling ที่ย้ายมาบน Android ผ่าน Arm [26] กระทบ performance budget ของ mobile และ standalone XR โดยตรง เพราะไม่มี desktop GPU headroom มารองรับ UnRealityKit [49] สะท้อน friction จริงในการ ship immersive content ไปยัง Apple Vision Pro และเป็น pattern ที่คนอื่นกำลังหาทางเลี่ยง Generative AI เริ่มเปลี่ยนจากการทดลองข้างเคียง [15][38][51] ไปสู่ production pipeline ที่ระบุชื่อ [47] และการพัฒนา pipeline tooling [6] ซึ่งสร้างความคาดหวังที่ clients และ tools จะนำเข้ามาใน edutech และ asset workflows

## Possibility
เป็นไปได้สูง: State of Unreal (17 มิ.ย.) นำด้วย optimization tooling เพราะ performance backlash และ framing ของ Epic เอง [44][17][58] เป็นไปได้: การใช้ on-device/mobile upscaling ขยายตัวเมื่อ Arm ผลักดัน DLSS-style path บน Android [26] ซึ่งเกี่ยวข้องกับ mobile และ standalone XR เป็นไปได้: generative AI ใน production กลายเป็นเรื่องปกติถ้า Tomb Raider ได้รับการตอบรับดีหรือกลางๆ [47] ไม่น่าจะเกิด: คำวิจารณ์เรื่อง UE5 internal resolution/upscaling จะหายไปในระยะใกล้ [17][58] — นี่คือ engine default และ hardware tradeoff ไม่ใช่ patch แก้ได้เร็ว ไม่มี source ใดให้ตัวเลขความน่าจะเป็น จึงไม่ระบุ

## Org applicability — NDF DEV
ติดตาม State of Unreal 17 มิ.ย. สำหรับ optimization roadmap และการเปลี่ยนแปลง tool [44] (low) นำบทเรียน UE5 perf ไปใช้กับงาน high-fidelity ทุกชิ้น — budget internal resolution และอย่าเปิดทุก feature โดย default [17][58] (low) สำหรับงาน Unity มี tool ที่ใช้ได้โดยตรงสองตัว: Real Fake Interiors ซึ่งเป็น Unity baking-tool-plus-shader สำหรับจำลองห้องเฟอร์นิเจอร์หลังหน้าต่าง [41] และ stylized water VFX shader technique [20] (low) ถ้า XR/VR roadmap เล็งไปที่ Apple Vision Pro ให้ศึกษาแนวทาง UnRealityKit bridge สำหรับ eye tracking/gestures/room lighting [49] (med) ติดตาม Android upscaler ของ Arm รอ SDK/availability ก่อนผูกมัด mobile perf budget [26] (med) สำหรับ edutech/asset pipeline ประเมินที่ที่ generative AI เหมาะสม โดยใช้ production case ของ Tomb Raider [47] และ coding-style note ของ Carmack [6] เป็นจุดอ้างอิง (med) ถ้าพิจารณา Godot เป็น lightweight/2D option ให้รู้ว่า 4.7 RC2 ใกล้ stable แล้ว [25] (low) ข้ามได้: Halo/Clutch AAA hype [5][10][35], โพสต์ D&D ของ Carmack [4][19][22][24], indie marketing/wishlist posts และ Godot 'Pronoun Palace' controversy [33] — ไม่มี signal ที่นำไปปฏิบัติได้

## Signals to Watch
- State of Unreal 17 มิ.ย. — optimization tooling ที่ Epic จะ ship จริง [44]
- Android upscaler ของ Arm — SDK release และ engine/device ที่รองรับ [26]
- การตอบรับ Tomb Raider: Legacy of Atlantis เป็นบททดสอบการยอมรับ gen-AI ใน production [47]
- UE5 perf backlash จะเริ่มเปลี่ยน engine choice ของ indie/studio หรือไม่ [17][58]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | bilawalsidhu | ^5982 c46 | [OG Anunoby is too sick. Here is the full point-of-view 3d reconstruction of his ](https://x.com/bilawalsidhu/status/2065109650475712908) |
| x | iDuckFilms | ^4284 c32 | [There are plenty of valid reasons to criticize Glitch Productions, but why are s](https://x.com/iDuckFilms/status/2065102252789174337) |
| x | TheGameVerse | ^2944 c53 | [New gameplay montages from Tomb Raider: Legacy of Atlantis. - Set in the same un](https://x.com/TheGameVerse/status/2065083789559341334) |
| x | ID_AA_Carmack | ^1591 c52 | [Trista had never played tabletop Dungeons & Dragons before, so I recently dusted](https://x.com/ID_AA_Carmack/status/2064720302005748031) |
| x | farzam_plays | ^1382 c53 | [Clutch will be using UE5 with a custom physics engine for aspects such as: - Tir](https://x.com/farzam_plays/status/2065117350551076925) |
| x | ID_AA_Carmack | ^1171 c131 | [It seems like LLMs could optimize coding style by exploring ways of structuring ](https://x.com/ID_AA_Carmack/status/2065138674950414428) |
| x | Windpress | ^926 c5 | [This SFW Horror game leaves a BIG impact on the player. You must navigate tight ](https://x.com/Windpress/status/2065119093124899111) |
| x | ciirulean | ^619 c4 | [very pleased to see godot feature our game for obvious reasons but also I'm just](https://x.com/ciirulean/status/2065135580166737933) |
| x | Pirat_Nation | ^587 c97 | [A new look at Halo Campaign Evolved realistic graphics The game has been develop](https://x.com/Pirat_Nation/status/2065170541992890415) |
| x | GameRiot | ^478 c15 | [NEW details on Clutch from recent previews 👀 • Open world set in the South of Fr](https://x.com/GameRiot/status/2065134642483835132) |
| x | Infiniteforges | ^455 c27 | [Here's an update on my Halo 3: Sierra 117 remake in Unreal Engine 5 https://t.co](https://x.com/Infiniteforges/status/2065218610587382231) |
| x | HedProtag | ^406 c2 | [Discord Server for Synapse is now open. Exclusive roles are still preserved for ](https://x.com/HedProtag/status/2065117361129033869) |
| x | digitalfoundry | ^402 c11 | [Halo: Campaign Evolved Is a Fascinating Preview of the Series' Unreal Engine Fut](https://x.com/digitalfoundry/status/2065077868158234952) |
| x | Stoneshard | ^381 c12 | [Wands ability tree - all speculation welcome 🪄✨ #teaser #medieval #pixelart #gam](https://x.com/Stoneshard/status/2065089439982846130) |
| x | ziwenxu_ | ^305 c89 | [Day 2 of building my GTA 6 agent in the loop. It's working better than yesterday](https://x.com/ziwenxu_/status/2065090683501728110) |
| x | IsThisA3DModel | ^286 c4 | [@ABAOProductions @Kling_ai @kitbash3d kling is not a render engine. unreal actua](https://x.com/IsThisA3DModel/status/2065140983461789840) |
| x | Weston_Mitchell | ^281 c8 | [all these new ue5 games have all the shit turned on and they have to do 540p int](https://x.com/Weston_Mitchell/status/2065111412981293266) |
| x | iDuckFilms | ^242 c3 | [If people want Glitch Productions to not work with Epic Games, what are they sup](https://x.com/iDuckFilms/status/2065102255922291035) |
| x | ID_AA_Carmack | ^221 c4 | [A novel thing for me happened during character creation: one of the players had ](https://x.com/ID_AA_Carmack/status/2064720305868640532) |
| x | jettelly | ^215 c0 | [Ever wondered how to make a clean, stylized water pipeline VFX in Unity? Here's ](https://x.com/jettelly/status/2064678973775155209) |
| x | DMC_Ryan | ^214 c8 | [We got to play about 45 minutes of Tomb Raider: Legacy of Atlantis, the upcoming](https://x.com/DMC_Ryan/status/2065124279218487748) |
| x | ID_AA_Carmack | ^213 c12 | [I always add a few low-level player friendly rule tweaks, but my favorite house ](https://x.com/ID_AA_Carmack/status/2064720308490092844) |
| x | MagicStone23 | ^203 c17 | [After over two years of solo development, my game is finally live on Steam! 🎉🐟🏠✨](https://x.com/MagicStone23/status/2065089825850716384) |
| x | ID_AA_Carmack | ^200 c5 | [@evildojo666 Trista is my partner, not my daughter 😃. You can see my original 4'](https://x.com/ID_AA_Carmack/status/2064755973336482288) |
| x | godotengine | ^195 c6 | [Our second Release Candidate for #GodotEngine 4.7 has arrived! This will be your](https://x.com/godotengine/status/2065123733367345515) |
| x | digitalfoundry | ^180 c2 | [Arm shows off its answer to DLSS on Android - and a whole-ass game by Sumo Digit](https://x.com/digitalfoundry/status/2065011189776625949) |
| x | jaderbxm | ^177 c11 | [working on server authority (connected to an actual remote server) #threatcentra](https://x.com/jaderbxm/status/2064967800310149423) |
| x | Talegamesnews | ^173 c2 | [Just your casual forest stroll 🐍🐗💥 #metroidvania #platformer #indiegame #indiede](https://x.com/Talegamesnews/status/2065027262345330793) |
| x | KrakenCombo | ^169 c9 | [After 23 days of dev, I finally rebuilt my UI system and I'm honestly pretty hap](https://x.com/KrakenCombo/status/2065047980759982477) |
| x | SaveChan_Dev | ^168 c3 | [BEEN PRACTICING MY DANCE MOVES Daluob is an action roguelite with fast builds an](https://x.com/SaveChan_Dev/status/2064965491513569612) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@bilawalsidhu</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 5982 · 💬 46</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/bilawalsidhu/status/2065109650475712908">View @bilawalsidhu on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“OG Anunoby is too sick. Here is the full point-of-view 3d reconstruction of his winning tip-in from the Knicks game last night. You can literally relive it from his perspective. Built with viewpoint p”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Viewpoint Pro ใช้ tracking camera ในสนามกีฬา + Unreal Engine สร้าง 3D scene แบบ first-person POV จากท่วงท่าของนักบาส OJ Anunoby ได้หลังจบเกมจริง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>พิสูจน์ว่า pipeline จริง spatial tracking → Unreal Engine POV scene ทำได้แล้ว ตรงกับงาน XR/VR live-event ของทีม</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ใช้ Viewpoint Pro เป็น reference architecture เวลา scope งาน spatial capture สำหรับโปรเจกต์ XR หรือ sports simulation</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/bilawalsidhu/status/2065109650475712908" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@iDuckFilms</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 4284 · 💬 32</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/iDuckFilms/status/2065102252789174337">View @iDuckFilms on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“There are plenty of valid reasons to criticize Glitch Productions, but why are so many people surprised that they are collaborating with Fortnite? A lot of their stuff is partially funded by Epic and ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจารณ์ชี้ว่าการ collab ของ Glitch Productions กับ Fortnite ไม่ใช่เรื่องน่าแปลก เพราะ Epic Games อัดฉีดทุนบางส่วนให้ และ Glitch ใช้ Unreal Engine ในงาน 3D ทุกชิ้น</dd>
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
    <span class="ndf-author">@TheGameVerse</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 2944 · 💬 53</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/TheGameVerse/status/2065083789559341334">View @TheGameVerse on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“New gameplay montages from Tomb Raider: Legacy of Atlantis. - Set in the same universe as the Survivor Trilogy - Features scanning mechanics - Hints at expanded skill trees for Lara Croft - Introduces”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Tomb Raider: Legacy of Atlantis สร้างใน Unreal Engine 5 กำหนดปล่อย 12 ก.พ. 2027 เผย mechanics ใหม่สามอย่าง — environmental scanning, skill tree แบบแบ่งชั้น และ grapple gadget ต่อจาก Survivor Trilogy</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Mechanics สามอย่างที่ระบุชัดเป็น AAA design pattern ที่ทีม game ของ studio ใช้เป็น reference สำหรับระบบ traversal, progression และ exploration ได้ตรงๆ</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม Unity ของ studio เก็บ mechanics เหล่านี้เป็น design reference แบบ tag ไว้ใช้กับโปรเจกต์ที่มี skill progression หรือ gadget traversal</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/TheGameVerse/status/2065083789559341334" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1591 · 💬 52</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2064720302005748031">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Trista had never played tabletop Dungeons &amp; Dragons before, so I recently dusted off some old skills and ran a little four player game for her. I never learned modern 5e rules, and I wanted to keep it”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>John Carmack จัด session D&amp;D แบบ tabletop โดยใช้ Rules Cyclopedia และผู้เล่นที่ paint Warhammer figures มาช่วยทำ miniature — เขายอมรับว่า visual aids ดีกว่าที่คิด</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ID_AA_Carmack/status/2064720302005748031" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@farzam_plays</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1382 · 💬 53</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/farzam_plays/status/2065117350551076925">View @farzam_plays on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Clutch will be using UE5 with a custom physics engine for aspects such as: - Tire temperature - grip levels - suspension - etc. From what I've seen the game is very gorgeous and didn't seem that have ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>เกม Clutch (racing) ใช้ UE5 คู่กับ custom physics engine สำหรับ tire temperature, grip และ suspension โดยนักพัฒนาระบุว่าไม่มีปัญหา traversal stutter แบบที่พบใน UE5 open-world ทั่วไป</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>การ layer custom physics engine เฉพาะทางบน commercial engine เป็น architecture ที่ใช้ได้จริงสำหรับเกม simulation-heavy และการแก้ traversal stutter ตรง pain point จริงของ UE5 open-world</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">Studio ใช้ Unity ไม่ใช่ UE5 แต่ pattern ของ custom physics layer ใช้ได้กับ Unity simulation project (VR driving, physics puzzle) ที่ PhysX built-in ไม่พอ</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/farzam_plays/status/2065117350551076925" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@ID_AA_Carmack</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 1171 · 💬 131</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ID_AA_Carmack/status/2065138674950414428">View @ID_AA_Carmack on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“It seems like LLMs could optimize coding style by exploring ways of structuring code so weaker and weaker models can still successfully perform tasks in a codebase. There are surely stylistic quirks t”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Carmack ชี้ว่า code ที่เขียนให้ LLM อ่านง่าย (structure ชัด, ชื่อ explicit) ช่วยให้ AI coding tools ทุก tier ทำงานได้ดีขึ้น และตรงกับสิ่งที่ช่วย developer คนอ่านด้วย</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Studio ที่ใช้ AI coding tools ทุกวันได้ประโยชน์ต่อเนื่องจาก codebase อ่านง่าย — AI แนะ code ได้ดีขึ้นโดยไม่ต้องเปลี่ยน model แพงขึ้น</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">จัด 1 วัน audit repo ที่ใช้ AI tools บ่อย: ปรับชื่อตัวแปร, ลด nesting ลึก, เพิ่ม inline comment อธิบาย intent ตรงจุดที่ logic ซับซ้อน</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ID_AA_Carmack/status/2065138674950414428" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@Windpress</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 926 · 💬 5</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/Windpress/status/2065119093124899111">View @Windpress on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“This SFW Horror game leaves a BIG impact on the player. You must navigate tight corridors while avoiding being spotted. Triple A Horror games have been SLOP since Unreal Engine became a thing. Indie D”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>มีคนโปรโมต indie horror game ที่ไม่ได้เปิดเผยชื่อ บน X โดยบอกว่า corridor stealth ให้ผลดีกว่า AAA horror ที่ใช้ Unreal Engine</dd>
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
    <span class="ndf-author">@ciirulean</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 619 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/ciirulean/status/2065135580166737933">View @ciirulean on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“very pleased to see godot feature our game for obvious reasons but also I'm just glad that they didn't censor the clown boobs. I wanted to make a point of including nonsexual nudity in pp because the ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Indie dev บอกว่าเกมตัวเองถูก Godot feature อย่างเป็นทางการ และทาง Godot ไม่ได้ censor nudity ที่ตั้งใจใส่ไว้ในเกม</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/ciirulean/status/2065135580166737933" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
